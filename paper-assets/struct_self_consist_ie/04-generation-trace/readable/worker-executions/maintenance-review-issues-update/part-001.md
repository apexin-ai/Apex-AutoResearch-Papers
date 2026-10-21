# maintenance review issues update — Part 1 of 3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[Transcript overview](../maintenance-review-issues-update.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/34/346dc4b7baed2be42f7b.json)

## Before a recorded user message

## Before a recorded user message

69 recorded events


### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---


### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "bf9b3eee-39d5-41df-be22-6779fe2cd812",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778887800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4bc9262a-8958-40aa-8435-813563a993d1",
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the file first to understand its structure, then make the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "ef8a4ab7-9085-47fe-8e47-4f6050b12424",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnTq1PjhtLjPuWQfhE2SHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12382,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12382
      },
      "output_tokens": 21,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01HPoHu8oKC5LU9pSwDSfYUA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "e69396c9-a109-4959-9582-4329d906f5ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnTq1PjhtLjPuWQfhE2SHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12382,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12382
      },
      "output_tokens": 21,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 6 · 2026-05-15T22:26:55.232Z_

<details><summary>↩ Tool result · `toolu_01HPoHu8oKC5LU9pSwDSfYUA`</summary>

```text
1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-7) =====
3	- id: R0-C1
4	  summary: 模型规模单一（仅 8B）
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  mentions:
11	  - round: 0
12	    reviewers: [1, 2]
13	    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性
14	  - round: 1
15	    reviewers: [1, 2]
16	    note: model-agnostic 与 Limitations 矛盾
17	  action_items:
18	  - round: 1
19	    action: 全文替换 model-agnostic → consistent across tested model families
20	    assigned_to: Paper Agent
21	    status: resolved
22	  resolution: Round 2 Reviewer 确认措辞修正到位，无再提
23	  resolution_round: 2
24	- id: R0-C2
25	  summary: 相关工作显著遗漏
26	  category: framing
27	  severity: warning
28	  status: resolved
29	  first_raised_round: 0
30	  last_seen_round: 1
31	  mentions:
32	  - round: 0
33	    reviewers: [1, 2]
34	    note: 5 篇核心文献缺失
35	  - round: 1
36	    reviewers: [1, 2]
37	    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC
38	  action_items:
39	  - round: 1
40	    action: 补充 6 篇引用到 Related Work
41	    assigned_to: Paper Agent
42	    status: resolved
43	  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'
44	  resolution_round: 2
45	- id: R0-C3
46	  summary: RE 结论仅基于 SciERC 单数据集
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 0
51	  last_seen_round: 4
52	  mentions:
53	  - round: 0
54	    reviewers: [1, 2]
55	    note: 需跨数据集验证或降级措辞
56	  - round: 2
57	    reviewers: [1, 2]
58	    note: Abstract RE 措辞需修正
59	  - round: 3
60	    reviewers: [1, 2]
61	    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围
62	  - round: 4
63	    reviewers: [1, 2]
64	    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪
65	  action_items:
66	  - round: 1
67	    action: 降级措辞 universal → observed in SciERC
68	    assigned_to: Paper Agent
69	    status: resolved
70	  - round: 2
71	    action: Abstract 改为 NER (three datasets) and RE (SciERC)
72	    assigned_to: Paper Agent
73	    status: resolved
74	  - round: 3
75	    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis
76	    assigned_to: Agent + Paper Agent
77	    status: resolved
78	  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'
79	  resolution_round: 4
80	- id: R0-C4
81	  summary: SJ 方法新颖性有限
82	  category: method
83	  severity: warning
84	  status: resolved
85	  first_raised_round: 0
86	  last_seen_round: 1
87	  mentions:
88	  - round: 1
89	    reviewers: [2]
90	    note: Nedellec 增量贡献论证不足 + 引用错误
91	  action_items:
92	  - round: 1
93	    action: 修正 bib + 加强增量贡献论证
94	    assigned_to: Paper Agent
95	    status: resolved
96	  resolution: Round 2 确认三点差异化清晰
97	  resolution_round: 2
98	- id: R0-C5
99	  summary: 全文零图表
100	  category: writing
101	  severity: critical
102	  status: resolved
103	  first_raised_round: 0
104	  last_seen_round: 0
105	  mentions:
106	  - round: 0
107	    reviewers: [1, 2]
108	    note: 缺少 selection curves、reliability diagrams
109	  action_items: []
110	  resolution: 论文已包含 6 个 figures
111	  resolution_round: 1
112	- id: R0-C6
113	  summary: 成本分析 negligible 误导
114	  category: method
115	  severity: critical
116	  status: resolved
117	  first_raised_round: 0
118	  last_seen_round: 0
119	  mentions:
120	  - round: 0
121	    reviewers: [1, 2]
122	    note: 8-16× 推理开销不应描述为 negligible
123	  action_items: []
124	  resolution: Round 1+ 未再提及
125	  resolution_round: 1
126	- id: R0-W1
127	  summary: 未探索 signal combination
128	  category: experiment
129	  severity: warning
130	  status: resolved
131	  first_raised_round: 0
132	  last_seen_round: 0
133	  mentions:
134	  - round: 0
135	    reviewers: [1, 2]
136	    note: 互补性已证明但未尝试组合
137	  action_items: []
138	  resolution: Round 1+ 未再提及
139	  resolution_round: 1
140	- id: R0-W4
141	  summary: 统计检验不系统
142	  category: experiment
143	  severity: critical
144	  status: resolved
145	  first_raised_round: 0
146	  last_seen_round: 1
147	  mentions:
148	  - round: 1
149	    reviewers: [1, 2]
150	    note: Bootstrap 细节不足
151	  action_items:
152	  - round: 1
153	    action: 补完整 bootstrap 规范
154	    assigned_to: Paper Agent
155	    status: resolved
156	  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准
157	  resolution_round: 2
158	- id: R0-RR-D1
159	  summary: Voting Conf N-scaling +0.018 与数据矛盾
160	  category: experiment
161	  severity: warning
162	  status: resolved
163	  first_raised_round: 0
164	  last_seen_round: 0
165	  mentions:
166	  - round: 0
167	    reviewers: [Research Reviewer]
168	    note: +0.018 实际为 -0.080
169	  action_items:
170	  - round: 0
171	    action: 修正声明
172	    assigned_to: Main Agent
173	    status: resolved
174	  resolution: 已修正
175	  resolution_round: 1
176	- id: R1-N1
177	  summary: Bootstrap 检验细节不足
178	  category: method
179	  severity: critical
180	  status: resolved
181	  first_raised_round: 1
182	  last_seen_round: 1
183	  mentions:
184	  - round: 1
185	    reviewers: [1, 2]
186	    note: p=0.39 支撑核心结论但细节缺失
187	  action_items:
188	  - round: 1
189	    action: 补完整 bootstrap 规范
190	    assigned_to: Paper Agent
191	    status: resolved
192	  resolution: Round 2 Reviewer 评价统计规范达到高标准
193	  resolution_round: 2
194	- id: R1-N2
195	  summary: Gap 解释力不足 + logprob 失败未分析
196	  category: method
197	  severity: critical
198	  status: resolved
199	  first_raised_round: 1
200	  last_seen_round: 1
201	  mentions:
202	  - round: 1
203	    reviewers: [1, 2]
204	    note: 4/5 定义性 + logprob 机制缺失
205	  action_items:
206	  - round: 1
207	    action: 区分 by-design vs empirical + logprob failure 分析段
208	    assigned_to: Paper Agent
209	    status: resolved
210	  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分
211	  resolution_round: 2
212	- id: R1-N3
213	  summary: Per-sample signal 单薄
214	  category: method
215	  severity: warning
216	  status: resolved
217	  first_raised_round: 1
218	  last_seen_round: 1
219	  mentions:
220	  - round: 1
221	    reviewers: [1, 2]
222	    note: consensus-proximity = LOO-SJ 是表述问题
223	  action_items:
224	  - round: 1
225	    action: 显式说明等价关系
226	    assigned_to: Paper Agent
227	    status: resolved
228	  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确
229	  resolution_round: 2
230	- id: R1-N4
231	  summary: Nedellec 引用错误 + 增量贡献弱
232	  category: framing
233	  severity: critical
234	  status: resolved
235	  first_raised_round: 1
236	  last_seen_round: 1
237	  mentions:
238	  - round: 1
239	    reviewers: [1, 2]
240	    note: Yao vs Nédellec 事实错误
241	  action_items:
242	  - round: 1
243	    action: 修正 bib + 加强论证
244	    assigned_to: Paper Agent
245	    status: resolved
246	  resolution: Round 2 确认差异化清晰
247	  resolution_round: 2
248	- id: R1-W1
249	  summary: SJ 形式化有歧义
250	  category: method
251	  severity: warning
252	  status: resolved
253	  first_raised_round: 1
254	  last_seen_round: 4
255	  mentions:
256	  - round: 2
257	    reviewers: [1, 2]
258	    note: Hungarian threshold + max denominator 需补充
259	  - round: 3
260	    reviewers: [1, 2]
261	    note: R3-R1 再次指出 Hungarian cost function 未明确
262	  - round: 4
263	    reviewers: [2]
264	    note: R2 Round 4 确认 SJ 形式化已完善
265	  action_items:
266	  - round: 1
267	    action: 补全 Eq(4) 定义
268	    assigned_to: Paper Agent
269	    status: resolved
270	  - round: 2
271	    action: 补 threshold 说明 + max vs union 设计理由
272	    assigned_to: Paper Agent
273	    status: resolved
274	  - round: 3
275	    action: 补 Hungarian optimization objective + zero-IoU pairs handling
276	    assigned_to: Paper Agent
277	    status: resolved
278	  resolution: 'Round 4: R2 确认 SJ 形式化已完善'
279	  resolution_round: 4
280	- id: R1-W2
281	  summary: Voting-SJ 冗余度未分析
282	  category: method
283	  severity: warning
284	  status: resolved
285	  first_raised_round: 1
286	  last_seen_round: 1
287	  mentions:
288	  - round: 1
289	    reviewers: [1, 2]
290	    note: instance-level correlation 未报告
291	  action_items:
292	  - round: 1
293	    action: 报告 Voting-SJ ρ=0.659/0.605
294	    assigned_to: Paper Agent
295	    status: resolved
296	  resolution: 中等相关数据已报告
297	  resolution_round: 2
298	- id: R1-W3
299	  summary: ρ=0.38 缺 contextualization
300	  category: framing
301	  severity: warning
302	  status: resolved
303	  first_raised_round: 1
304	  last_seen_round: 2
305	  mentions:
306	  - round: 2
307	    reviewers: [1, 2]
308	    note: 需 cross-method footnote
309	  action_items:
310	  - round: 2
311	    action: '§5 footnote: semantic entropy AUROC comparison'
312	    assigned_to: Paper Agent
313	    status: resolved
314	  resolution: Footnote 已加
315	  resolution_round: 2
316	- id: R1-W4
317	  summary: Logprob 温度数据缺失
318	  category: experiment
319	  severity: warning
320	  status: resolved
321	  first_raised_round: 1
322	  last_seen_round: 1
323	  mentions:
324	  - round: 1
325	    reviewers: [1, 2]
326	    note: robustness 结论需限定
327	  action_items:
328	  - round: 1
329	    action: 限定为 consistency-based signals robust
330	    assigned_to: Paper Agent
331	    status: resolved
332	  resolution: 措辞限定到位
333	  resolution_round: 2
334	- id: R1-W5
335	  summary: WNUT-17 establishing 措辞过度
336	  category: framing
337	  severity: warning
338	  status: resolved
339	  first_raised_round: 1
340	  last_seen_round: 1
341	  mentions:
342	  - round: 1
343	    reviewers: [1, 2]
344	    note: fail to reject ≠ accept
345	  action_items:
346	  - round: 1
347	    action: establishing → consistent with/suggests
348	    assigned_to: Paper Agent
349	    status: resolved
350	  resolution: 已修正
351	  resolution_round: 2
352	- id: R1-W6
353	  summary: LLaMA 训练设置不对称
354	  category: experiment
355	  severity: warning
356	  status: resolved
357	  first_raised_round: 1
358	  last_seen_round: 1
359	  mentions:
360	  - round: 1
361	    reviewers: [1, 2]
362	    note: LLaMA fine-tuning 状态未说明
363	  action_items:
364	  - round: 1
365	    action: 明确两模型 identical LoRA 配置
366	    assigned_to: Paper Agent
367	    status: resolved
368	  resolution: Round 2 未再提及
369	  resolution_round: 2
370	- id: R1-W7
371	  summary: 约束解码 diversity 影响
372	  category: method
373	  severity: warning
374	  status: resolved
375	  first_raised_round: 1
376	  last_seen_round: 2
377	  mentions:
378	  - round: 2
379	    reviewers: [1, 2]
380	    note: 需扩展为全局 confound + Limitations 条目
381	  action_items:
382	  - round: 2
383	    action: Discussion 扩展 + Limitations 新增条目
384	    assigned_to: Paper Agent
385	    status: resolved
386	  resolution: 已扩展为全局 confound 讨论
387	  resolution_round: 2
388	- id: R1-W8
389	  summary: first systematic 过强
390	  category: framing
391	  severity: warning
392	  status: resolved
393	  first_raised_round: 1
394	  last_seen_round: 1
395	  mentions:
396	  - round: 1
397	    reviewers: [1, 2]
398	    note: 需收窄 scope
399	  action_items:
400	  - round: 1
401	    action: first multi-family
402	    assigned_to: Paper Agent
403	    status: resolved
404	  resolution: Round 2 无再提
405	  resolution_round: 2
406	- id: R1-W9
407	  summary: 遗漏引用
408	  category: framing
409	  severity: warning
410	  status: resolved
411	  first_raised_round: 1
412	  last_seen_round: 1
413	  mentions:
414	  - round: 1
415	    reviewers: [1, 2]
416	    note: Optimal SC, Difficulty-Adaptive SC 等
417	  action_items:
418	  - round: 1
419	    action: 补充引用
420	    assigned_to: Paper Agent
421	    status: resolved
422	  resolution: Round 2 确认无遗漏
423	  resolution_round: 2
424	- id: R1-W10
425	  summary: ρ-AUROC dissociation 分析浅
426	  category: experiment
427	  severity: warning
428	  status: resolved
429	  first_raised_round: 1
430	  last_seen_round: 1
431	  mentions:
432	  - round: 1
433	    reviewers: [1, 2]
434	    note: EM=1 压缩效应需主文提及
435	  action_items:
436	  - round: 1
437	    action: Section 5 简述 + 引导 Appendix
438	    assigned_to: Paper Agent
439	    status: resolved
440	  resolution: Round 2 确认 dissociation 分析为 actionable finding
441	  resolution_round: 2
442	- id: R1-M1
443	  summary: Logistic regression proxy 无结果
444	  category: writing
445	  severity: info
446	  status: resolved
447	  first_raised_round: 1
448	  last_seen_round: 1
449	  mentions:
450	  - round: 1
451	    reviewers: [1, 2]
452	    note: 展示结果或删除
453	  action_items:
454	  - round: 1
455	    action: 删除提及
456	    assigned_to: Paper Agent
457	    status: resolved
458	  resolution: 已删除
459	  resolution_round: 2
460	- id: R1-M2
461	  summary: GSM8K +18pp 未注明模型
462	  category: writing
463	  severity: info
464	  status: resolved
465	  first_raised_round: 1
466	  last_seen_round: 1
467	  mentions:
468	  - round: 1
469	    reviewers: [1, 2]
470	    note: 补注 PaLM-540B
471	  action_items:
472	  - round: 1
473	    action: 补注
474	    assigned_to: Paper Agent
475	    status: resolved
476	  resolution: 已补注
477	  resolution_round: 2
478	- id: R1-M3
479	  summary: Cross-model Δ=0.005 未报告 CI
480	  category: experiment
481	  severity: info
482	  status: resolved
483	  first_raised_round: 1
484	  last_seen_round: 1
485	  mentions:
486	  - round: 1
487	    reviewers: [1, 2]
488	    note: within 3-seed σ≈0.007
489	  action_items:
490	  - round: 1
491	    action: 补注
492	    assigned_to: Paper Agent
493	    status: resolved
494	  resolution: 已补注
495	  resolution_round: 2
496	- id: R2-C1
497	  summary: Selection 证据面过窄
498	  category: experiment
499	  severity: critical
500	  status: resolved
501	  first_raised_round: 2
502	  last_seen_round: 2
503	  mentions:
504	  - round: 2
505	    reviewers: [1, 2]
506	    note: 需补 LLaMA SciERC + CoNLL selection
507	  action_items:
508	  - round: 2
509	    action: 补 4 配置 selection 分析
510	    assigned_to: Agent + Paper Agent
511	    status: resolved
512	  resolution: 6 configurations 全部补齐
513	  resolution_round: 2
514	- id: R2-C2
515	  summary: WNUT-17 仅报告 1 个信号
516	  category: experiment
517	  severity: critical
518	  status: resolved
519	  first_raised_round: 2
520	  last_seen_round: 2
521	  mentions:
522	  - round: 2
523	    reviewers: [1, 2]
524	    note: 5 signals 中仅 SJ
525	  action_items:
526	  - round: 2
527	    action: 补全 5 信号
528	    assigned_to: Agent + Paper Agent
529	    status: resolved
530	  resolution: WNUT-17 全信号表完整
531	  resolution_round: 2
532	- id: R2-W1
533	  summary: ρ=0.38 缺 cross-method 对比
534	  category: framing
535	  severity: warning
536	  status: resolved
537	  first_raised_round: 2
538	  last_seen_round: 2
539	  mentions:
540	  - round: 2
541	    reviewers: [1, 2]
542	    note: 需 footnote 引用 semantic entropy AUROC
543	  action_items:
544	  - round: 2
545	    action: §5 footnote
546	    assigned_to: Paper Agent
547	    status: resolved
548	  resolution: Footnote 已加
549	  resolution_round: 2
550	- id: R2-W2
551	  summary: N=8 QE ρ 无 uncertainty
552	  category: experiment
553	  severity: warning
554	  status: resolved
555	  first_raised_round: 2
556	  last_seen_round: 2
557	  mentions:
558	  - round: 2
559	    reviewers: [1, 2]
560	    note: 需 bootstrap CIs
561	  action_items:
562	  - round: 2
563	    action: 计算 B=10,000 bootstrap CI
564	    assigned_to: Agent + Paper Agent
565	    status: resolved
566	  resolution: Bootstrap CI 表已加入 Appendix
567	  resolution_round: 2
568	- id: R2-W3
569	  summary: SJ Hungarian threshold + max denominator
570	  category: method
571	  severity: warning
572	  status: resolved
573	  first_raised_round: 2
574	  last_seen_round: 2
575	  mentions:
576	  - round: 2
577	    reviewers: [1, 2]
578	    note: 无 threshold 声明需验证
579	  action_items:
580	  - round: 2
581	    action: 代码验证 + method.tex 补充
582	    assigned_to: Agent + Paper Agent
583	    status: resolved
584	  resolution: 无 threshold, max denominator 已解释
585	  resolution_round: 2
586	- id: R2-W4
587	  summary: RE selection 无统计检验
588	  category: experiment
589	  severity: warning
590	  status: resolved
591	  first_raised_round: 2
592	  last_seen_round: 2
593	  mentions:
594	  - round: 2
595	    reviewers: [1, 2]
596	    note: 需 bootstrap p-value
597	  action_items:
598	  - round: 2
599	    action: RE bootstrap
600	    assigned_to: Agent + Paper Agent
601	    status: resolved
602	  resolution: RE logprob p=0.80
603	  resolution_round: 2
604	- id: R2-W5
605	  summary: Constrained decoding 全局 confound
606	  category: method
607	  severity: warning
608	  status: resolved
609	  first_raised_round: 2
610	  last_seen_round: 2
611	  mentions:
612	  - round: 2
613	    reviewers: [1, 2]
614	    note: 需扩展到全局 + Limitations
615	  action_items:
616	  - round: 2
617	    action: Discussion 扩展 + Limitations 条目
618	    assigned_to: Paper Agent
619	    status: resolved
620	  resolution: 已处理
621	  resolution_round: 2
622	- id: R2-W6
623	  summary: Abstract RE 措辞误导
624	  category: framing
625	  severity: warning
626	  status: resolved
627	  first_raised_round: 2
628	  last_seen_round: 2
629	  mentions:
630	  - round: 2
631	    reviewers: [1, 2]
632	    note: NER (three datasets) and RE (SciERC)
633	  action_items:
634	  - round: 2
635	    action: 修正 Abstract
636	    assigned_to: Paper Agent
637	    status: resolved
638	  resolution: 已修正
639	  resolution_round: 2
640	- id: R2-W7
641	  summary: n=529 vs 551 未解释
642	  category: experiment
643	  severity: warning
644	  status: resolved
645	  first_raised_round: 2
646	  last_seen_round: 2
647	  mentions:
648	  - round: 2
649	    reviewers: [1, 2]
650	    note: 22 instances filtering criteria
651	  action_items:
652	  - round: 2
653	    action: 补一句说明
654	    assigned_to: Paper Agent
655	    status: resolved
656	  resolution: 已说明 gold-empty filtering
657	  resolution_round: 2
658	- id: R2-DATA
659	  summary: RE selection 数据矛盾
660	  category: experiment
661	  severity: critical
662	  status: resolved
663	  first_raised_round: 2
664	  last_seen_round: 2
665	  mentions:
666	  - round: 2
667	    reviewers: [Research Reviewer]
668	    note: Table 2 vs L129 矛盾
669	  action_items:
670	  - round: 2
671	    action: Agent 确认 Table 2 正确
672	    assigned_to: Agent + Paper Agent
673	    status: resolved
674	  resolution: 数据已统一
675	  resolution_round: 2
676	- id: R2-AUROC
677	  summary: L64 AUROC 归属错误
678	  category: writing
679	  severity: warning
680	  status: resolved
681	  first_raised_round: 2
682	  last_seen_round: 2
683	  mentions:
684	  - round: 2
685	    reviewers: [Research Reviewer]
686	    note: corresponding 暗示同一信号
687	  action_items:
688	  - round: 2
689	    action: 分别标注
690	    assigned_to: Paper Agent
691	    status: resolved
692	  resolution: 已拆分归属
693	  resolution_round: 2
694	- id: R3-C1
695	  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量
696	  category: method
697	  severity: critical
698	  status: resolved
699	  first_raised_round: 3
700	  last_seen_round: 6
701	  mentions:
702	  - round: 3
703	    reviewers: [1, 2]
704	    note: constrained decoding 可能压缩 per-sample diversity
705	  - round: 4
706	    reviewers: [1, 2]
707	    note: R2 确认部分解决
708	  - round: 5
709	    reviewers: [1, 2]
710	    note: Round 5 两位 Reviewer 再次独立提出
711	  - round: 6
712	    reviewers: [1, 2]
713	    note: R1 列 critical。R2 rebut 降为 should-fix
714	  action_items:
715	  - round: 3
716	    action: Agent 量化 diversity
717	    assigned_to: Agent + Paper Agent
718	    status: resolved
719	  - round: 4
720	    action: 量化 logprob 分布
721	    assigned_to: Agent + Paper Agent
722	    status: resolved
723	  - round: 5
724	    action: Title/Abstract/Conclusion 限定 claim scope
725	    assigned_to: Paper Agent
726	    status: resolved
727	  - round: 6
728	    action: Introduction 和 Discussion 声明
729	    assigned_to: Paper Agent
730	    status: superseded
731	  resolution: exp-018 free-form ablation 证明 gap task-intrinsic
732	  resolution_round: 7
733	- id: R3-C2
734	  summary: Failure-to-reject 不等于 evidence of absence
735	  category: method
736	  severity: warning
737	  status: resolved
738	  first_raised_round: 3
739	  last_seen_round: 4
740	  mentions:
741	  - round: 3
742	    reviewers: [1, 2]
743	    note: 需修改措辞或补充等价性检验
744	  - round: 4
745	    reviewers: [2]
746	    note: R2 确认 RESOLVED
747	  action_items:
748	  - round: 3
749	    action: 修改措辞 + TOST
750	    assigned_to: Paper Agent
751	    status: resolved
752	  resolution: TOST 等价检验已补充
753	  resolution_round: 4
754	- id: R3-C3
755	  summary: N=8 核心结果 single seed
756	  category: experiment
757	  severity: warning
758	  status: resolved
759	  first_raised_round: 3
760	  last_seen_round: 4
761	  mentions:
762	  - round: 3
763	    reviewers: [1, 2]
764	    note: Table 1 N=8 和 Table 2 全部 single seed
765	  - round: 4
766	    reviewers: [2]
767	    note: R2 确认 RESOLVED
768	  action_items:
769	  - round: 3
770	    action: Limitations 中明确 single-seed 风险
771	    assigned_to: Paper Agent
772	    status: resolved
773	  resolution: 3-seed 稳定性验证已补充
774	  resolution_round: 4
775	- id: R3-W1
776	  summary: 多重比较校正缺失
777	  category: experiment
778	  severity: warning
779	  status: resolved
780	  first_raised_round: 3
781	  last_seen_round: 4
782	  mentions:
783	  - round: 3
784	    reviewers: [1, 2]
785	    note: SJ-EM 在 Bonferroni 下不 survive
786	  - round: 4
787	    reviewers: [2]
788	    note: R2 确认 RESOLVED
789	  action_items:
790	  - round: 3
791	    action: 声明未做多重比较校正
792	    assigned_to: Paper Agent
793	    status: resolved
794	  resolution: Bonferroni 声明已加
795	  resolution_round: 4
796	- id: R3-W3
797	  summary: Consensus-proximity 未与 MBR 建立联系
798	  category: method
799	  severity: warning
800	  status: resolved
801	  first_raised_round: 3
802	  last_seen_round: 4
803	  mentions:
804	  - round: 3
805	    reviewers: [1, 2]
806	    note: MBR 未讨论
807	  - round: 4
808	    reviewers: [2]
809	    note: R2 确认 RESOLVED
810	  action_items:
811	  - round: 3
812	    action: 明确与 MBR 联系
813	    assigned_to: Paper Agent
814	    status: resolved
815	  resolution: §5 MBR decoding 连接段已写入
816	  resolution_round: 4
817	- id: R3-W6
818	  summary: First multi-family comparison claim scope 过宽
819	  category: framing
820	  severity: warning
821	  status: resolved
822	  first_raised_round: 3
823	  last_seen_round: 7
824	  mentions:
825	  - round: 3
826	    reviewers: [1, 2]
827	    note: 需限定为 structured IE
828	  - round: 7
829	    reviewers: [1]
830	    note: 论文当前版本未声称 first
831	  action_items:
832	  - round: 5
833	    action: 去掉 first claim
834	    assigned_to: Paper Agent
835	    status: resolved
836	  resolution: introduction.tex 无 first claim
837	  resolution_round: 7
838	- id: R3-W7
839	  summary: 术语不一致
840	  category: writing
841	  severity: warning
842	  status: resolved
843	  first_raised_round: 3
844	  last_seen_round: 7
845	  mentions:
846	  - round: 7
847	    reviewers: []
848	    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP
849	  action_items:
850	  - round: 6
851	    action: 全文统一缩写
852	    assigned_to: Paper Agent
853	    status: resolved
854	  resolution: 全文一致
855	  resolution_round: 7
856	- id: R3-W8
857	  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin
858	  category: framing
859	  severity: warning
860	  status: resolved
861	  first_raised_round: 3
862	  last_seen_round: 4
863	  mentions:
864	  - round: 4
865	    reviewers: [2]
866	    note: R2 确认 RESOLVED
867	  action_items:
868	  - round: 3
869	    action: 补充引用
870	    assigned_to: Paper Agent
871	    status: resolved
872	  resolution: 引用已补全
873	  resolution_round: 4
874	- id: R3-M1
875	  summary: WNUT-17 54% 与数据不一致
876	  category: experiment
877	  severity: info
878	  status: resolved
879	  first_raised_round: 3
880	  last_seen_round: 3
881	  mentions:
882	  - round: 3
883	    reviewers: [1]
884	    note: 355/689 ≈ 51.5% vs 54%
885	  action_items:
886	  - round: 3
887	    action: Agent 核实
888	    assigned_to: Agent + Paper Agent
889	    status: resolved
890	  resolution: 54% → 52% 已修正
891	  resolution_round: 4
892	- id: R3-M2
893	  summary: EM selection exclusion 缺乏支持
894	  category: experiment
895	  severity: info
896	  status: resolved
897	  first_raised_round: 3
898	  last_seen_round: 3
899	  mentions:
900	  - round: 3
901	    reviewers: [1, 2]
902	    note: 需报告频率
903	  action_items:
904	  - round: 3
905	    action: 计算 exact match 频率
906	    assigned_to: Agent + Paper Agent
907	    status: resolved
908	  resolution: EM 已加入 Table 2
909	  resolution_round: 4
910	- id: R3-M3
911	  summary: Ethics Statement 缺失
912	  category: format
913	  severity: info
914	  status: resolved
915	  first_raised_round: 3
916	  last_seen_round: 5
917	  mentions:
918	  - round: 5
919	    reviewers: [2]
920	    note: Ethics Statement 现为独立 section
921	  action_items:
922	  - round: 4
923	    action: 移出为独立 section
924	    assigned_to: Paper Agent
925	    status: resolved
926	  resolution: Ethics Statement 已为独立 section
927	  resolution_round: 5
928	- id: R3-M4
929	  summary: ρ-AUROC dissociation 过度强调
930	  category: framing
931	  severity: info
932	  status: resolved
933	  first_raised_round: 3
934	  last_seen_round: 3
935	  mentions:
936	  - round: 3
937	    reviewers: [1, 2]
938	    note: 承认统计预期性
939	  action_items:
940	  - round: 3
941	    action: §4.2 承认
942	    assigned_to: Paper Agent
943	    status: resolved
944	  resolution: 已承认
945	  resolution_round: 4
946	- id: R3-M5
947	  summary: Nedellec 措辞偏 adversarial
948	  category: writing
949	  severity: info
950	  status: resolved
951	  first_raised_round: 3
952	  last_seen_round: 3
953	  mentions:
954	  - round: 3
955	    reviewers: [1, 2]
956	    note: 用更 neutral 语气
957	  action_items:
958	  - round: 3
959	    action: 改为 neutral
960	    assigned_to: Paper Agent
961	    status: resolved
962	  resolution: 已修正
963	  resolution_round: 4
964	- id: R3-M6
965	  summary: LOO-SJ Δρ 量纲混淆
966	  category: writing
967	  severity: info
968	  status: resolved
969	  first_raised_round: 3
970	  last_seen_round: 3
971	  mentions:
972	  - round: 3
973	    reviewers: [1]
974	    note: Δρ vs per-instance max
975	  action_items:
976	  - round: 3
977	    action: 澄清含义
978	    assigned_to: Paper Agent
979	    status: resolved
980	  resolution: 已澄清
981	  resolution_round: 4
982	- id: R3-M7
983	  summary: Figure 1 caption 引入未直接可视化的 p=0.39
984	  category: writing
985	  severity: info
986	  status: resolved
987	  first_raised_round: 3
988	  last_seen_round: 3
989	  mentions:
990	  - round: 3
991	    reviewers: [1]
992	    note: 补交叉引用
993	  action_items:
994	  - round: 3
995	    action: 补 (Table 2) 交叉引用
996	    assigned_to: Paper Agent
997	    status: resolved
998	  resolution: 已补
999	  resolution_round: 4
1000	- id: R4-C1
1001	  summary: 训练配置和 prompt template 缺失
1002	  category: experiment
1003	  severity: critical
1004	  status: resolved
1005	  first_raised_round: 4
1006	  last_seen_round: 5
1007	  mentions:
1008	  - round: 5
1009	    reviewers: [1, 2]
1010	    note: Appendix E 已包含 Table 8
1011	  action_items:
1012	  - round: 4
1013	    action: 附录补充完整训练配置表
1014	    assigned_to: Paper Agent
1015	    status: resolved
1016	  resolution: Appendix E Table 8 完整
1017	  resolution_round: 5
1018	- id: R4-M1
1019	  summary: SJ normalizer 选择（max vs union）缺乏对比
1020	  category: method
1021	  severity: info
1022	  status: wont_fix
1023	  first_raised_round: 4
1024	  last_seen_round: 4
1025	  mentions:
1026	  - round: 4
1027	    reviewers: [1]
1028	    note: 未比较
1029	  action_items:
1030	  - round: 4
1031	    action: 附录补结果或提供理论依据
1032	    assigned_to: Agent + Paper Agent
1033	    status: wont_fix
1034	  resolution: max normalizer 设计已有理由，超出 scope
1035	  resolution_round: 4
1036	- id: R4-M3
1037	  summary: Table 1 N=16 block 空白
1038	  category: writing
1039	  severity: info
1040	  status: resolved
1041	  first_raised_round: 4
1042	  last_seen_round: 7
1043	  mentions:
1044	  - round: 7
1045	    reviewers: []
1046	    note: Table 1 仅含 N=8，N=16 在 Appendix
1047	  action_items:
1048	  - round: 6
1049	    action: Table 1 删除 N=16 行
1050	    assigned_to: Paper Agent
1051	    status: resolved
1052	  resolution: N=16 委托至 Appendix
1053	  resolution_round: 7
1054	- id: R4-W2
1055	  summary: SJ vs EM 应改为 difficulty-dependent complementarity
1056	  category: framing
1057	  severity: warning
1058	  status: resolved
1059	  first_raised_round: 4
1060	  last_seen_round: 5
1061	  mentions:
1062	  - round: 5
1063	    reviewers: [1, 2]
1064	    note: §4.2 已使用 complementarity 措辞
1065	  action_items:
1066	  - round: 4
1067	    action: 弱化 structural advantage
1068	    assigned_to: Paper Agent
1069	    status: resolved
1070	  resolution: complementarity 措辞到位
1071	  resolution_round: 5
1072	- id: R4-W4
1073	  summary: 缺少 Xiong et al. (2024)
1074	  category: framing
1075	  severity: warning
1076	  status: resolved
1077	  first_raised_round: 4
1078	  last_seen_round: 5
1079	  mentions:
1080	  - round: 5
1081	    reviewers: [1, 2]
1082	    note: Related Work 已引用
1083	  action_items:
1084	  - round: 4
1085	    action: 引用 Xiong et al.
1086	    assigned_to: Paper Agent
1087	    status: resolved
1088	  resolution: 已引用
1089	  resolution_round: 5
1090	- id: R5-W1
1091	  summary: Qwen3-8B thinking token 训练不一致
1092	  category: experiment
1093	  severity: warning
1094	  status: resolved
1095	  first_raised_round: 5
1096	  last_seen_round: 7
1097	  mentions:
1098	  - round: 7
1099	    reviewers: []
1100	    note: §4.1 现已显式声明，Limitations 讨论
1101	  action_items:
1102	  - round: 6
1103	    action: Experiments Setup 中显著声明
1104	    assigned_to: Paper Agent
1105	    status: resolved
1106	  resolution: experiments.tex 明确声明 + limitations.tex 讨论
1107	  resolution_round: 7
1108	- id: R5-W2
1109	  summary: Semantic entropy 脚注比较可能误导
1110	  category: writing
1111	  severity: info
1112	  status: resolved
1113	  first_raised_round: 5
1114	  last_seen_round: 7
1115	  mentions:
1116	  - round: 7
1117	    reviewers: []
1118	    note: 脚注已缩短
1119	  action_items:
1120	  - round: 6
1121	    action: 缩短脚注
1122	    assigned_to: Paper Agent
1123	    status: resolved
1124	  resolution: 脚注已缩短
1125	  resolution_round: 7
1126	- id: R5-W3
1127	  summary: he2024uncertainty bib entry 不匹配
1128	  category: writing
1129	  severity: info
1130	  status: resolved
1131	  first_raised_round: 5
1132	  last_seen_round: 7
1133	  mentions:
1134	  - round: 7
1135	    reviewers: []
1136	    note: R1 验证通过
1137	  action_items:
1138	  - round: 5
1139	    action: 修正引用上下文
1140	    assigned_to: Paper Agent
1141	    status: resolved
1142	  resolution: 正确指向 Findings of NAACL 2024
1143	  resolution_round: 7
1144	- id: R5-M3
1145	  summary: LOO-SJ 等价性缺少推导
1146	  category: method
1147	  severity: info
1148	  status: resolved
1149	  first_raised_round: 5
1150	  last_seen_round: 6
1151	  mentions:
1152	  - round: 6
1153	    reviewers: [1, 2]
1154	    note: Appendix D 已包含
1155	  action_items:
1156	  - round: 5
1157	    action: 附录补简要推导
1158	    assigned_to: Paper Agent
1159	    status: resolved
1160	  resolution: Appendix D 完整等价性证明
1161	  resolution_round: 6
1162	- id: R5-M4
1163	  summary: 部分 bib entries 在 OpenAlex 未找到
1164	  category: writing
1165	  severity: info
1166	  status: resolved
1167	  first_raised_round: 5
1168	  last_seen_round: 7
1169	  mentions:
1170	  - round: 7
1171	    reviewers: []
1172	    note: 62 篇全部通过验证
1173	  action_items:
1174	  - round: 6
1175	    action: 核实 bib entries
1176	    assigned_to: Paper Agent
1177	    status: resolved
1178	  resolution: 62 篇引用全部通过验证
1179	  resolution_round: 7
1180	- id: R5-M5
1181	  summary: Ethics Statement 仅 2 句
1182	  category: writing
1183	  severity: info
1184	  status: resolved
1185	  first_raised_round: 5
1186	  last_seen_round: 7
1187	  mentions:
1188	  - round: 7
1189	    reviewers: []
1190	    note: 包含 CoNLL Reuters 出处
1191	  action_items:
1192	  - round: 6
1193	    action: 补充 CoNLL Reuters license
1194	    assigned_to: Paper Agent
1195	    status: resolved
1196	  resolution: 实质性内容完整
1197	  resolution_round: 7
1198	- id: R5-Q4
1199	  summary: WNUT-17 logprob 负相关机制未解释
1200	  category: method
1201	  severity: warning
1202	  status: resolved
1203	  first_raised_round: 5
1204	  last_seen_round: 6
1205	  mentions:
1206	  - round: 6
1207	    reviewers: [1, 2]
1208	    note: §4.2 已加机制假设
1209	  action_items:
1210	  - round: 5
1211	    action: 加机制解释
1212	    assigned_to: Paper Agent
1213	    status: resolved
1214	  resolution: §4.2 已包含 overconfidence 假设
1215	  resolution_round: 6
1216	- id: R5-C1
1217	  summary: Constrained decoding 混淆变量 claim scope 不匹配
1218	  category: framing
1219	  severity: critical
1220	  status: resolved
1221	  first_raised_round: 5
1222	  last_seen_round: 6
1223	  mentions:
1224	  - round: 6
1225	    reviewers: [1, 2]
1226	    note: 与 R3-C1 合并
1227	  action_items:
1228	  - round: 5
1229	    action: Title 加限定
1230	    assigned_to: Paper Agent
1231	    status: resolved
1232	  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic
1233	  resolution_round: 7
1234	- id: R6-W2
1235	  summary: Figure 1 caption 冗余
1236	  category: writing
1237	  severity: info
1238	  status: resolved
1239	  first_raised_round: 6
1240	  last_seen_round: 7
1241	  mentions:
1242	  - round: 7
1243	    reviewers: []
1244	    note: 2 句简洁 caption
1245	  action_items:
1246	  - round: 6
1247	    action: 精简 caption
1248	    assigned_to: Paper Agent
1249	    status: resolved
1250	  resolution: 2 句简洁 caption
1251	  resolution_round: 7
1252	
1253	# ===== IN-PROGRESS ISSUES (updated with Round 8) =====
1254	- id: R3-W2
1255	  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然
1256	  category: framing
1257	  severity: critical
1258	  status: in_progress
1259	  first_raised_round: 3
1260	  last_seen_round: 8
1261	  mentions:
1262	  - round: 3
1263	    reviewers: [1, 2]
1264	    note: 需在 Discussion 中分离两层论证
1265	  - round: 4
1266	    reviewers: [1, 2]
1267	    note: Introduction 未正面论证 why not obvious a priori
1268	  - round: 5
1269	    reviewers: [1, 2]
1270	    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial
1271	  - round: 6
1272	    reviewers: [1, 2]
1273	    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression
1274	  - round: 7
1275	    reviewers: [1, 2]
1276	    note: 需根本性 reframing——dismiss instance-level failure in one sentence
1277	  - round: 8
1278	    reviewers: [1, 2]
1279	    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'
1280	  action_items:
1281	  - round: 7
1282	    action: 根本性 reframing——以 LP compression + MBR failure 为核心
1283	    assigned_to: Paper Agent
1284	    status: in_progress
1285	  - round: 8
1286	    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分
1287	    assigned_to: Paper Agent
1288	    status: in_progress
1289	  resolution: ''
1290	  resolution_round: null
1291	- id: R3-W4
1292	  summary: FK 独立性假设 justification 不足
1293	  category: method
1294	  severity: warning
1295	  status: in_progress
1296	  first_raised_round: 3
1297	  last_seen_round: 8
1298	  mentions:
1299	  - round: 3
1300	    reviewers: [1, 2]
1301	    note: 需报告 inter-sample correlation
1302	  - round: 7
1303	    reviewers: [1, 2]
1304	    note: n=5 t-test 功效极低
1305	  - round: 8
1306	    reviewers: [1, 2]
1307	    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'
1308	  action_items:
1309	  - round: 7
1310	    action: 改用 permutation test 或 bootstrap CI
1311	    assigned_to: Paper Agent
1312	    status: in_progress
1313	  - round: 8
1314	    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification
1315	    assigned_to: Paper Agent
1316	    status: in_progress
1317	  resolution: ''
1318	  resolution_round: null
1319	- id: R3-W5
1320	  summary: Cross-model 实为 cross-architecture at fixed 8B scale
1321	  category: framing
1322	  severity: warning
1323	  status: in_progress
1324	  first_raised_round: 3
1325	  last_seen_round: 8
1326	  mentions:
1327	  - round: 7
1328	    reviewers: [1, 2]
1329	    note: 标题 scope 问题
1330	  - round: 8
1331	    reviewers: [1, 2]
1332	    note: 'R2 N3 标题 "8B-Scale" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'
1333	  action_items:
1334	  - round: 7
1335	    action: 标题 scope down
1336	    assigned_to: Paper Agent
1337	    status: in_progress
1338	  - round: 8
1339	    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）
1340	    assigned_to: Paper Agent
1341	    status: in_progress
1342	  resolution: ''
1343	  resolution_round: null
1344	- id: R4-M2
1345	  summary: TOST δ 选择缺乏实践意义论证
1346	  category: experiment
1347	  severity: warning
1348	  status: in_progress
1349	  first_raised_round: 4
1350	  last_seen_round: 8
1351	  mentions:
1352	  - round: 7
1353	    reviewers: [1, 2]
1354	    note: δ 循环锚定于 oracle headroom
1355	  - round: 8
1356	    reviewers: [1, 2]
1357	    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。
1358	  action_items:
1359	  - round: 7
1360	    action: 用外部标准替代 oracle headroom 锚定
1361	    assigned_to: Paper Agent
1362	    status: in_progress
1363	  resolution: ''
1364	  resolution_round: null
1365	- id: R4-W1
1366	  summary: RE 证据需进一步加强（consistent preliminary 标注）
1367	  category: experiment
1368	  severity: critical
1369	  status: in_progress
1370	  first_raised_round: 4
1371	  last_seen_round: 8
1372	  mentions:
1373	  - round: 7
1374	    reviewers: [1, 2]
1375	    note: RE 标注不一致
1376	  - round: 8
1377	    reviewers: [1, 2]
1378	    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'
1379	  action_items:
1380	  - round: 7
1381	    action: 全文 RE 引用一致标注
1382	    assigned_to: Paper Agent
1383	    status: in_progress
1384	  - round: 8
1385	    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed
1386	    assigned_to: Paper Agent
1387	    status: in_progress
1388	  resolution: ''
1389	  resolution_round: null
1390	- id: R4-W3
1391	  summary: Abstract 过于密集
1392	  category: writing
1393	  severity: warning
1394	  status: in_progress
1395	  first_raised_round: 4
1396	  last_seen_round: 8
1397	  mentions:
1398	  - round: 7
1399	    reviewers: [1, 2]
1400	    note: 精简为问题-发现-意义三段式
1401	  - round: 8
1402	    reviewers: [1, 2]
1403	    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'
1404	  action_items:
1405	  - round: 8
1406	    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写
1407	    assigned_to: Paper Agent
1408	    status: in_progress
1409	  resolution: ''
1410	  resolution_round: null
1411	- id: R5-N1
1412	  summary: 与 Nédellec et al. (2026) 的增量贡献不充分
1413	  category: framing
1414	  severity: warning
1415	  status: in_progress
1416	  first_raised_round: 5
1417	  last_seen_round: 7
1418	  mentions:
1419	  - round: 7
1420	    reviewers: []
1421	    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解
1422	  - round: 8
1423	    reviewers: []
1424	    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。
1425	  action_items:
1426	  - round: 6
1427	    action: 降低 Contribution 1 claim 强度
1428	    assigned_to: Paper Agent
1429	    status: in_progress
1430	  resolution: ''
1431	  resolution_round: null
1432	- id: R5-C2
1433	  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性
1434	  category: framing
1435	  severity: critical
1436	  status: in_progress
1437	  first_raised_round: 5
1438	  last_seen_round: 8
1439	  mentions:
1440	  - round: 7
1441	    reviewers: [1, 2]
1442	    note: 与 R3-W2 合并
1443	  - round: 8
1444	    reviewers: [1, 2]
1445	    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。
1446	  action_items:
1447	  - round: 6
1448	    action: 见 R3-W2 action
1449	    assigned_to: Paper Agent
1450	    status: in_progress
1451	  resolution: ''
1452	  resolution_round: null
1453	- id: R5-W4
1454	  summary: First multi-family comparison claim = scope engineering
1455	  category: framing
1456	  severity: warning
1457	  status: resolved
1458	  first_raised_round: 5
1459	  last_seen_round: 7
1460	  mentions:
1461	  - round: 7
1462	    reviewers: []
1463	    note: 与 R3-W6 合并。论文当前版本未含 first claim。
1464	  - round: 8
1465	    reviewers: []
1466	    note: 本轮未提及。R3-W6 已 resolved。
1467	  action_items:
1468	  - round: 5
1469	    action: first → a systematic
1470	    assigned_to: Paper Agent
1471	    status: resolved
1472	  resolution: 与 R3-W6 合并。论文当前版本无 first claim。
1473	  resolution_round: 7
1474	- id: R5-W5
1475	  summary: Cross-architecture 用词过度
1476	  category: framing
1477	  severity: warning
1478	  status: in_progress
1479	  first_raised_round: 5
1480	  last_seen_round: 8
1481	  mentions:
1482	  - round: 7
1483	    reviewers: [1, 2]
1484	    note: 标题 scope
1485	  - round: 8
1486	    reviewers: [1, 2]
1487	    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。
1488	  action_items:
1489	  - round: 6
1490	    action: 见 R3-W5 action
1491	    assigned_to: Paper Agent
1492	    status: in_progress
1493	  resolution: ''
1494	  resolution_round: null
1495	- id: R5-W6
1496	  summary: FK independence justification 不够严格
1497	  category: method
1498	  severity: warning
1499	  status: in_progress
1500	  first_raised_round: 5
1501	  last_seen_round: 8
1502	  mentions:
1503	  - round: 8
1504	    reviewers: [1, 2]
1505	    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。
1506	  action_items:
1507	  - round: 6
1508	    action: 见 R3-W4 action
1509	    assigned_to: Paper Agent
1510	    status: in_progress
1511	  resolution: ''
1512	  resolution_round: null
1513	- id: R5-W7
1514	  summary: SJ 方法论新颖性有限
1515	  category: framing
1516	  severity: warning
1517	  status: in_progress
1518	  first_raised_round: 5
1519	  last_seen_round: 8
1520	  mentions:
1521	  - round: 7
1522	    reviewers: []
1523	    note: 未直接提及
1524	  - round: 8
1525	    reviewers: [2]
1526	    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'
1527	  action_items:
1528	  - round: 5
1529	    action: core → primary structural signal
1530	    assigned_to: Paper Agent
1531	    status: in_progress
1532	  resolution: ''
1533	  resolution_round: null
1534	- id: R5-M1
1535	  summary: 缺少 test-time scaling survey 引用
1536	  category: framing
1537	  severity: info
1538	  status: resolved
1539	  first_raised_round: 5
1540	  last_seen_round: 7
1541	  mentions:
1542	  - round: 7
1543	    reviewers: []
1544	    note: 论文 Related Work 已引用 zhang2025tts
1545	  - round: 8
1546	    reviewers: []
1547	    note: 本轮未提及。已引用。
1548	  action_items:
1549	  - round: 6
1550	    action: 补充 Zhang et al. (2025)
1551	    assigned_to: Paper Agent
1552	    status: resolved
1553	  resolution: Related Work 已引用 zhang2025tts
1554	  resolution_round: 8
1555	- id: R5-M2
1556	  summary: 缺少 MBR 在非 MT 任务中的应用引用
1557	  category: framing
1558	  severity: info
1559	  status: in_progress
1560	  first_raised_round: 5
1561	  last_seen_round: 8
1562	  mentions:
1563	  - round: 7
1564	    reviewers: [2]
1565	    note: Eikema 仅在 Discussion
1566	  - round: 8
1567	    reviewers: [1, 2]
1568	    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'
1569	  action_items:
1570	  - round: 7
1571	    action: 将 eikema2025structured 前移到 Related Work
1572	    assigned_to: Paper Agent
1573	    status: in_progress
1574	  resolution: ''
1575	  resolution_round: null
1576	- id: R6-W1
1577	  summary: VC 公式（Eq.6）与实现不一致
1578	  category: method
1579	  severity: warning
1580	  status: in_progress
1581	  first_raised_round: 6
1582	  last_seen_round: 7
1583	  mentions:
1584	  - round: 7
1585	    reviewers: [1, 2]
1586	    note: Table 3 标注不清
1587	  - round: 8
1588	    reviewers: []
1589	    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。
1590	  action_items:
1591	  - round: 7
1592	    action: Table 3 caption 明确标注 VC selection 使用 majority threshold
1593	    assigned_to: Paper Agent
1594	    status: in_progress
1595	  resolution: ''
1596	  resolution_round: null
1597	- id: R7-C1
1598	  summary: Selection gap 分析缺乏多种子验证
1599	  category: experiment
1600	  severity: critical
1601	  status: in_progress
1602	  first_raised_round: 7
1603	  last_seen_round: 8
1604	  mentions:
1605	  - round: 7
1606	    reviewers: [1, 2]
1607	    note: 核心 selection failure 仅 seed=42
1608	  - round: 8
1609	    reviewers: [1, 2]
1610	    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'
1611	  action_items:
1612	  - round: 7
1613	    action: 将 3-seed 分析扩展至 Table 3
1614	    assigned_to: Agent + Paper Agent
1615	    status: in_progress
1616	  resolution: ''
1617	  resolution_round: null
1618	- id: R7-C2
1619	  summary: ε=0.05 effectively tied 阈值缺乏论证
1620	  category: method
1621	  severity: critical
1622	  status: in_progress
1623	  first_raised_round: 7
1624	  last_seen_round: 8
1625	  mentions:
1626	  - round: 7
1627	    reviewers: [1, 2]
1628	    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff
1629	  - round: 8
1630	    reviewers: [1, 2]
1631	    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'
1632	  action_items:
1633	  - round: 7
1634	    action: 提供 LP range 完整 CDF 或连续度量替代二元划分
1635	    assigned_to: Agent + Paper Agent
1636	    status: in_progress
1637	  - round: 8
1638	    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字
1639	    assigned_to: Paper Agent
1640	    status: in_progress
1641	  resolution: ''
1642	  resolution_round: null
1643	- id: R7-C3
1644	  summary: Free-form ablation 范围过窄但支撑过强泛化声称
1645	  category: experiment
1646	  severity: critical
1647	  status: in_progress
1648	  first_raised_round: 7
1649	  last_seen_round: 8
1650	  mentions:
1651	  - round: 7
1652	    reviewers: [1, 2]
1653	    note: 1 dataset × 1 model × 1 seed
1654	  - round: 8
1655	    reviewers: [1, 2]
1656	    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。
1657	  action_items:
1658	  - round: 7
1659	    action: 降级 fundamental/intrinsic 措辞
1660	    assigned_to: Paper Agent
1661	    status: in_progress
1662	  - round: 8
1663	    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work
1664	    assigned_to: Paper Agent
1665	    status: in_progress
1666	  resolution: ''
1667	  resolution_round: null
1668	- id: R7-W1
1669	  summary: LP 温度敏感性完全缺失
1670	  category: experiment
1671	  severity: critical
1672	  status: in_progress
1673	  first_raised_round: 7
1674	  last_seen_round: 8
1675	  mentions:
1676	  - round: 7
1677	    reviewers: [1, 2]
1678	    note: LP 是核心诊断对象但无 T=0.7 数据
1679	  - round: 8
1680	    reviewers: [1, 2]
1681	    note: 'R1 N2 列 critical：Section 4.4 "robust across T" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'
1682	  action_items:
1683	  - round: 7
1684	    action: Limitations 中充分讨论
1685	    assigned_to: Paper Agent
1686	    status: in_progress
1687	  - round: 8
1688	    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据
1689	    assigned_to: Paper Agent
1690	    status: in_progress
1691	  resolution: ''
1692	  resolution_round: null
1693	- id: R7-W2
1694	  summary: Contribution 1 定性有分歧
1695	  category: framing
1696	  severity: warning
1697	  status: in_progress
1698	  first_raised_round: 7
1699	  last_seen_round: 8
1700	  mentions:
1701	  - round: 7
1702	    reviewers: [1, 2]
1703	    note: engineering benchmark vs methodological contribution
1704	  - round: 8
1705	    reviewers: [1, 2]
1706	    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'
1707	  action_items:
1708	  - round: 7
1709	    action: 考虑将 Contribution 1 从 contribution 降级
1710	    assigned_to: Paper Agent
1711	    status: in_progress
1712	  - round: 8
1713	    action: 至少改措辞为以发现为主语的表述（如 "We find that metrics decouple" 而非 "Multi-metric evaluation revealing..."）
1714	    assigned_to: Paper Agent
1715	    status: in_progress
1716	  resolution: ''
1717	  resolution_round: null
1718	- id: R7-W3
1719	  summary: Eikema et al. (2025) 应前移到 Related Work
1720	  category: framing
1721	  severity: warning
1722	  status: in_progress
1723	  first_raised_round: 7
1724	  last_seen_round: 8
1725	  mentions:
1726	  - round: 7
1727	    reviewers: [1, 2]
1728	    note: 仅在 Discussion 出现
1729	  - round: 8
1730	    reviewers: [1, 2]
1731	    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'
1732	  action_items:
1733	  - round: 8
1734	    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系
1735	    assigned_to: Paper Agent
1736	    status: in_progress
1737	  resolution: ''
1738	  resolution_round: null
1739	- id: R7-W4
1740	  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B
1741	  category: writing
1742	  severity: critical
1743	  status: in_progress
1744	  first_raised_round: 7
1745	  last_seen_round: 7
1746	  mentions:
1747	  - round: 7
1748	    reviewers: [Research Reviewer]
1749	    note: Appendix 模型名错误
1750	  - round: 8
1751	    reviewers: []
1752	    note: 本轮未检查。待 Research Director 确认。
1753	  action_items:
1754	  - round: 7
1755	    action: 全文搜索替换
1756	    assigned_to: Paper Agent
1757	    status: in_progress
1758	  resolution: ''
1759	  resolution_round: null
1760	
1761	# ===== NEW ISSUES (Round 8) =====
1762	- id: R8-N1
1763	  summary: 正文页数严重超过 8 页限制（估计 10-11 页）
1764	  category: format
1765	  severity: critical
1766	  status: in_progress
1767	  first_raised_round: 8
1768	  last_seen_round: 8
1769	  mentions:
1770	  - round: 8
1771	    reviewers: [1, 2]
1772	    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'
1773	  action_items:
1774	  - round: 8
1775	    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'
1776	    assigned_to: Paper Agent
1777	    status: in_progress
1778	  resolution: ''
1779	  resolution_round: null
1780	- id: R8-N2
1781	  summary: 标题 "Do Not Select" overclaim——论文自身数据显示 LP 在子集上 significantly selects
1782	  category: framing
1783	  severity: critical
1784	  status: in_progress
1785	  first_raised_round: 8
1786	  last_seen_round: 8
1787	  mentions:
1788	  - round: 8
1789	    reviewers: [1, 2]
1790	    note: 'R2 列 critical N3："Do Not Select" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'
1791	  action_items:
1792	  - round: 8
1793	    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'
1794	    assigned_to: Paper Agent
1795	    status: in_progress
1796	  resolution: ''
1797	  resolution_round: null
1798	- id: R8-W1
1799	  summary: 缺少代码/数据发布承诺
1800	  category: experiment
1801	  severity: warning
1802	  status: in_progress
1803	  first_raised_round: 8
1804	  last_seen_round: 8
1805	  mentions:
1806	  - round: 8
1807	    reviewers: [1, 2]
1808	    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'
1809	  action_items:
1810	  - round: 8
1811	    action: 添加 Code and Data 段落说明发布计划
1812	    assigned_to: Paper Agent
1813	    status: in_progress
1814	  resolution: ''
1815	  resolution_round: null
1816	- id: R8-W2
1817	  summary: enable_thinking 对 LP score distribution 的影响未量化
1818	  category: experiment
1819	  severity: warning
1820	  status: in_progress
1821	  first_raised_round: 8
1822	  last_seen_round: 8
1823	  mentions:
1824	  - round: 8
1825	    reviewers: [1, 2]
1826	    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'
1827	  action_items:
1828	  - round: 8
1829	    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略
1830	    assigned_to: Paper Agent
1831	    status: in_progress
1832	  resolution: ''
1833	  resolution_round: null
1834	- id: R8-W3
1835	  summary: SJ max normalizer 未做 sensitivity analysis / ablation
1836	  category: method
1837	  severity: warning
1838	  status: in_progress
1839	  first_raised_round: 8
1840	  last_seen_round: 8
1841	  mentions:
1842	  - round: 8
1843	    reviewers: [1, 2]
1844	    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'
1845	  action_items:
1846	  - round: 8
1847	    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略
1848	    assigned_to: Paper Agent
1849	    status: in_progress
1850	  resolution: ''
1851	  resolution_round: null
1852	- id: R8-W4
1853	  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为
1854	  category: experiment
1855	  severity: warning
1856	  status: in_progress
1857	  first_raised_round: 8
1858	  last_seen_round: 8
1859	  mentions:
1860	  - round: 8
1861	    reviewers: [1]
1862	    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'
1863	  action_items:
1864	  - round: 8
1865	    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略
1866	    assigned_to: Paper Agent
1867	    status: in_progress
1868	  resolution: ''
1869	  resolution_round: null
1870	- id: R8-W5
1871	  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称
1872	  category: experiment
1873	  severity: warning
1874	  status: in_progress
1875	  first_raised_round: 8
1876	  last_seen_round: 8
1877	  mentions:
1878	  - round: 8
1879	    reviewers: [1]
1880	    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'
1881	  action_items:
1882	  - round: 8
1883	    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据
1884	    assigned_to: Paper Agent
1885	    status: in_progress
1886	  resolution: ''
1887	  resolution_round: null
1888	- id: R8-M1
1889	  summary: nedellec2026 bib key 与实际第一作者不一致
1890	  category: writing
1891	  severity: info
1892	  status: in_progress
1893	  first_raised_round: 8
1894	  last_seen_round: 8
1895	  mentions:
1896	  - round: 8
1897	    reviewers: [1, 2]
1898	    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'
1899	  action_items:
1900	  - round: 8
1901	    action: 修正 bib key
1902	    assigned_to: Paper Agent
1903	    status: in_progress
1904	  resolution: ''
1905	  resolution_round: null
1906	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "09d2f4ae-d9cc-4c26-bafd-3660005c6889",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
      "content": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
      "numLines": 1906,
      "startLine": 1,
      "totalLines": 1906
    }
  }
}
```

</details>

---


### Assistant

_source line 7_

文件共 1906 行。现在逐项编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "2daff089-a857-424a-9e9c-0c90790ae259",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVEyHksifcAwt6ZbxAPvgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24487,
      "cache_read_input_tokens": 24083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24487
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q7g166JkVq7dXFmeFXDFuU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "dcfb42e8-1d1a-4e09-839b-3e6a737eb49d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVEyHksifcAwt6ZbxAPvgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24487,
      "cache_read_input_tokens": 24083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24487
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-15T22:27:18.685Z_

<details><summary>↩ Tool result · `toolu_01Q7g166JkVq7dXFmeFXDFuU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "3ed15303-85af-4b50-b8ac-b564773e9592",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1255,
        "oldLines": 7,
        "newStart": 1255,
        "newLines": 7,
        "lines": [
          "   summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然",
          "   category: framing",
          "   severity: critical",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 3",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1281,
        "oldLines": 13,
        "newStart": 1281,
        "newLines": 13,
        "lines": [
          "   - round: 7",
          "     action: 根本性 reframing——以 LP compression + MBR failure 为核心",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "+    status: resolved",
          "   - round: 8",
          "     action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"",
          "+  resolution_round: 8",
          " - id: R3-W4",
          "   summary: FK 独立性假设 justification 不足",
          "   category: method"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Edit · `toolu_01RajFGHNWj6QUuwWGtdo7ip`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "f63089aa-03e3-4f7a-b191-9199a2f98dd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5jb1web5d41M9pPjxPCcZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 48570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1453
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-15T22:27:29.932Z_

<details><summary>↩ Tool result · `toolu_01RajFGHNWj6QUuwWGtdo7ip`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "e68595dc-c44c-4d5d-9f76-77f9845d1713",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1292,
        "oldLines": 7,
        "newStart": 1292,
        "newLines": 7,
        "lines": [
          "   summary: FK 独立性假设 justification 不足",
          "   category: method",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 3",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1309,
        "oldLines": 13,
        "newStart": 1309,
        "newLines": 13,
        "lines": [
          "   - round: 7",
          "     action: 改用 permutation test 或 bootstrap CI",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "+    status: resolved",
          "   - round: 8",
          "     action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"",
          "+  resolution_round: 8",
          " - id: R3-W5",
          "   summary: Cross-model 实为 cross-architecture at fixed 8B scale",
          "   category: framing"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Edit · `toolu_019nB1HR7wsC4yHC6FFjg2LT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "35503b7c-9d00-4603-ac8c-e497526a7ec3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFmzdxwss8zyUDHyv4RXFX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 50023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 888
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-15T22:27:41.027Z_

<details><summary>↩ Tool result · `toolu_019nB1HR7wsC4yHC6FFjg2LT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "cb05c665-690f-445e-9fb3-697e0d1a290f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1320,
        "oldLines": 7,
        "newStart": 1320,
        "newLines": 7,
        "lines": [
          "   summary: Cross-model 实为 cross-architecture at fixed 8B scale",
          "   category: framing",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 3",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1334,
        "oldLines": 13,
        "newStart": 1334,
        "newLines": 13,
        "lines": [
          "   - round: 7",
          "     action: 标题 scope down",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "+    status: resolved",
          "   - round: 8",
          "     action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"",
          "+  resolution_round: 8",
          " - id: R4-M2",
          "   summary: TOST δ 选择缺乏实践意义论证",
          "   category: experiment"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_01VJZKLSYaBh4m5m4Cozmm6b`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "15ff39be-d0e6-4584-a860-f2ba12ff2f10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST58c5zCdxdwmhbzJYsMGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 50911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-15T22:27:52.852Z_

<details><summary>↩ Tool result · `toolu_01VJZKLSYaBh4m5m4Cozmm6b`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "c6ca1070-e410-4688-9564-2d4f762d555b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1345,
        "oldLines": 7,
        "newStart": 1345,
        "newLines": 7,
        "lines": [
          "   summary: TOST δ 选择缺乏实践意义论证",
          "   category: experiment",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 4",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1359,
        "oldLines": 9,
        "newStart": 1359,
        "newLines": 9,
        "lines": [
          "   - round: 7",
          "     action: 用外部标准替代 oracle headroom 锚定",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"",
          "+  resolution_round: 8",
          " - id: R4-W1",
          "   summary: RE 证据需进一步加强（consistent preliminary 标注）",
          "   category: experiment"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01VCe1oGnr2Cv1rk7ZVwjaok`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "53baae01-095f-46c4-9e8d-615c81e206f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZockKftRymMXbWTn4CCZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 51761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 678
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-15T22:28:10.125Z_

<details><summary>↩ Tool result · `toolu_01VCe1oGnr2Cv1rk7ZVwjaok`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "0ad4736f-8bd5-4ba8-988f-9522ad1ba7d9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1366,
        "oldLines": 7,
        "newStart": 1366,
        "newLines": 7,
        "lines": [
          "   summary: RE 证据需进一步加强（consistent preliminary 标注）",
          "   category: experiment",
          "   severity: critical",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 4",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1380,
        "oldLines": 13,
        "newStart": 1380,
        "newLines": 13,
        "lines": [
          "   - round: 7",
          "     action: 全文 RE 引用一致标注",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "+    status: resolved",
          "   - round: 8",
          "     action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"",
          "+  resolution_round: 8",
          " - id: R4-W3",
          "   summary: Abstract 过于密集",
          "   category: writing"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01R7PcXXS7ujpvJwYCEja7Ar`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "df219957-4670-4159-b515-0a5163000caa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8rXnePHTM4CTiYiML56qw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 52439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-15T22:28:19.129Z_

<details><summary>↩ Tool result · `toolu_01R7PcXXS7ujpvJwYCEja7Ar`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "d5d787fa-bd82-40dc-956a-b458a95d952b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1391,
        "oldLines": 7,
        "newStart": 1391,
        "newLines": 7,
        "lines": [
          "   summary: Abstract 过于密集",
          "   category: writing",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 4",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1405,
        "oldLines": 9,
        "newStart": 1405,
        "newLines": 9,
        "lines": [
          "   - round: 8",
          "     action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"",
          "+  resolution_round: 8",
          " - id: R5-N1",
          "   summary: 与 Nédellec et al. (2026) 的增量贡献不充分",
          "   category: framing"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_017Ti9zikPjEoV91J95vxY1o`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"核心贡献 reframed 为 LP compression + MBR failure，Nédellec 增量贡献问题自然缓解\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "a8405527-6a0c-40db-87a8-1076dc7fab66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2CfXTugN2p1PEKjNcU7ab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 53282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 729
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-15T22:28:30.405Z_

<details><summary>↩ Tool result · `toolu_017Ti9zikPjEoV91J95vxY1o`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "b57ff952-ac73-416f-801c-d8ca6389bf1a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"核心贡献 reframed 为 LP compression + MBR failure，Nédellec 增量贡献问题自然缓解\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"\n  resolution_round: 8\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1412,
        "oldLines": 7,
        "newStart": 1412,
        "newLines": 7,
        "lines": [
          "   summary: 与 Nédellec et al. (2026) 的增量贡献不充分",
          "   category: framing",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 5",
          "   last_seen_round: 7",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1426,
        "oldLines": 9,
        "newStart": 1426,
        "newLines": 9,
        "lines": [
          "   - round: 6",
          "     action: 降低 Contribution 1 claim 强度",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"核心贡献 reframed 为 LP compression + MBR failure，Nédellec 增量贡献问题自然缓解\"",
          "+  resolution_round: 8",
          " - id: R5-C2",
          "   summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性",
          "   category: framing"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01CHfsAE1bJ7B9o57wJGrire`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W2 合并。两层结构清晰，LP/MBR 为核心实证贡献\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "8f06fbde-0e1d-411b-9ab2-7856f10e4b87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8sosy4D8HcjtkyxwpAuAG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 54011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 697
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-15T22:28:42.090Z_

<details><summary>↩ Tool result · `toolu_01CHfsAE1bJ7B9o57wJGrire`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "c59c6e93-669d-49b9-97a6-5b4a709363dc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W2 合并。两层结构清晰，LP/MBR 为核心实证贡献\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"\n  resolution_round: 8\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"核心贡献 reframed 为 LP compression + MBR failure，Nédellec 增量贡献问题自然缓解\"\n  resolution_round: 8\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1433,
        "oldLines": 7,
        "newStart": 1433,
        "newLines": 7,
        "lines": [
          "   summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性",
          "   category: framing",
          "   severity: critical",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 5",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1447,
        "oldLines": 9,
        "newStart": 1447,
        "newLines": 9,
        "lines": [
          "   - round: 6",
          "     action: 见 R3-W2 action",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"与 R3-W2 合并。两层结构清晰，LP/MBR 为核心实证贡献\"",
          "+  resolution_round: 8",
          " - id: R5-W4",
          "   summary: First multi-family comparison claim = scope engineering",
          "   category: framing"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01HjpAG8HKtXC73gaaZumYPu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W5 合并。标题无 cross-architecture overclaim\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "26a8291c-358b-4fb0-aae7-6f3cd2ba1181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198xnUs5ZyaR9VR3akJEPSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 54708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 770
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T22:28:48.237Z_

<details><summary>↩ Tool result · `toolu_01HjpAG8HKtXC73gaaZumYPu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "cb267381-17d0-49b8-8fca-617281226698",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W5 合并。标题无 cross-architecture overclaim\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"\n  resolution_round: 8\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"核心贡献 reframed 为 LP compression + MBR failure，Nédellec 增量贡献问题自然缓解\"\n  resolution_round: 8\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W2 合并。两层结构清晰，LP/MBR 为核心实证贡献\"\n  resolution_round: 8\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1475,
        "oldLines": 7,
        "newStart": 1475,
        "newLines": 7,
        "lines": [
          "   summary: Cross-architecture 用词过度",
          "   category: framing",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 5",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1489,
        "oldLines": 9,
        "newStart": 1489,
        "newLines": 9,
        "lines": [
          "   - round: 6",
          "     action: 见 R3-W5 action",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"与 R3-W5 合并。标题无 cross-architecture overclaim\"",
          "+  resolution_round: 8",
          " - id: R5-W6",
          "   summary: FK independence justification 不够严格",
          "   category: method"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01S1Z9JGGryc9oG1TGQoawPK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W4 合并。Instance-level permutation test 已补充\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "86d769d2-2bb2-4e28-80c4-cbd0d839cda2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MoQtZYuSb13ioehoVZ9VK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 55478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 605
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-15T22:28:54.478Z_

<details><summary>↩ Tool result · `toolu_01S1Z9JGGryc9oG1TGQoawPK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "2993fc26-5bd7-4ca4-9f34-0d661f9ecffd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W4 合并。Instance-level permutation test 已补充\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"\n  resolution_round: 8\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"核心贡献 reframed 为 LP compression + MBR failure，Nédellec 增量贡献问题自然缓解\"\n  resolution_round: 8\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W2 合并。两层结构清晰，LP/MBR 为核心实证贡献\"\n  resolution_round: 8\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W5 合并。标题无 cross-architecture overclaim\"\n  resolution_round: 8\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1496,
        "oldLines": 7,
        "newStart": 1496,
        "newLines": 7,
        "lines": [
          "   summary: FK independence justification 不够严格",
          "   category: method",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 5",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1507,
        "oldLines": 9,
        "newStart": 1507,
        "newLines": 9,
        "lines": [
          "   - round: 6",
          "     action: 见 R3-W4 action",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"与 R3-W4 合并。Instance-level permutation test 已补充\"",
          "+  resolution_round: 8",
          " - id: R5-W7",
          "   summary: SJ 方法论新颖性有限",
          "   category: framing"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01JaNHM5ZeMbF5bzMhWS4asf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"论文未将 SJ 作为方法论贡献，Introduction 仅称 structural matching\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "232e9cf5-07be-4589-ad9b-d9efeac7f1a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfCmEZDwuAAS9CHFQ4yY56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 56083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-15T22:29:04.179Z_

<details><summary>↩ Tool result · `toolu_01JaNHM5ZeMbF5bzMhWS4asf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "24bc375f-d847-4ece-aef4-df55f6de0a8f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "oldString": "- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
    "newString": "- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"论文未将 SJ 作为方法论贡献，Introduction 仅称 structural matching\"\n  resolution_round: 8",
    "originalFile": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Table 2 两层视觉分组 (Per-sample signal / Instance-level signals); Discussion 两层结构 (definitional + score compression); Abstract 明确两层\"\n  resolution_round: 8\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix FK Independence: Instance-Level Permutation Test, n=529-2756, all p<0.001, split-half r reported\"\n  resolution_round: 8\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"标题 'Strong Predictors, Weak Selectors: ...Struggle to Select...' 无 8B-Scale overclaim\"\n  resolution_round: 8\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Appendix External equivalence margins: δ_SEM, δ_practical=0.5pp (Ratinov 2009), δ_literature=1.0pp (Berg-Kirkpatrick 2012)\"\n  resolution_round: 8\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"全文 RE 一致标注 preliminary (Abstract, Table 1 caption, experiments.tex, Conclusion)\"\n  resolution_round: 8\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Abstract 精简为 9 行 问题-发现-意义 结构，移除具体数字和信号缩写\"\n  resolution_round: 8\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"核心贡献 reframed 为 LP compression + MBR failure，Nédellec 增量贡献问题自然缓解\"\n  resolution_round: 8\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W2 合并。两层结构清晰，LP/MBR 为核心实证贡献\"\n  resolution_round: 8\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W5 合并。标题无 cross-architecture overclaim\"\n  resolution_round: 8\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"与 R3-W4 合并。Instance-level permutation test 已补充\"\n  resolution_round: 8\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n",
    "structuredPatch": [
      {
        "oldStart": 1514,
        "oldLines": 7,
        "newStart": 1514,
        "newLines": 7,
        "lines": [
          "   summary: SJ 方法论新颖性有限",
          "   category: framing",
          "   severity: warning",
          "-  status: in_progress",
          "+  status: resolved",
          "   first_raised_round: 5",
          "   last_seen_round: 8",
          "   mentions:"
        ]
      },
      {
        "oldStart": 1528,
        "oldLines": 9,
        "newStart": 1528,
        "newLines": 9,
        "lines": [
          "   - round: 5",
          "     action: core → primary structural signal",
          "     assigned_to: Paper Agent",
          "-    status: in_progress",
          "-  resolution: ''",
          "-  resolution_round: null",
          "+    status: resolved",
          "+  resolution: \"论文未将 SJ 作为方法论贡献，Introduction 仅称 structural matching\"",
          "+  resolution_round: 8",
          " - id: R5-M1",
          "   summary: 缺少 test-time scaling survey 引用",
          "   category: framing"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_0152qBpGM9zq3SW2veHx97eF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "old_string": "- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null",
  "new_string": "- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: \"Eikema 2025 在 Related Work 3 句讨论，明确互补关系\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "083ad18c-1969-447f-bc42-4f4048d96c65",
  "uuid": "2584d821-5aa8-4568-b89d-601085d3095a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSYTVqUdxWDEsTofuGwxnS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 56635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 694
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
