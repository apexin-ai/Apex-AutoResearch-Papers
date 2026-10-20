# writing rebuttal framework update

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_writing_rebuttal-framework-update_20260521T084223.log`
- **Structured JSON:** [`c93b73dfbc8dde3f9f8e.json`](../../sessions/c9/c93b73dfbc8dde3f9f8e.json)

## Before a recorded user message

21 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "de6ff976-b37e-4217-804e-5b687700131b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
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
    "resetsAt": 1779369000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "97230f47-1ddb-4f68-aa2e-4803f5277f0b",
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436"
}
```

---

### Assistant

_source line 4_

Let me start by reading the existing rebuttal framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "27846f2d-22c6-4cb1-906a-7052097d92cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZYohdX7iXYJibVYQWBGGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13630,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13630
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Read · `toolu_01HJUDoHKyAXpJe4GEyAPiUh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "da19be87-2c43-4114-8542-fbfec84812bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZYohdX7iXYJibVYQWBGGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13630,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13630
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-21T08:42:37.303Z_

<details><summary>↩ Tool result · `toolu_01HJUDoHKyAXpJe4GEyAPiUh`</summary>

```text
1	# Rebuttal Framework — Pre-Submission Attack Surface Analysis
2	
3	Date: 2026-05-20 | Venue: EMNLP 2026 ARR
4	
5	---
6	
7	## Attack #1: CWM ≤8B LoRA ≠ Real 32B CWM
8	
9	### Reviewer 可能措辞
10	
11	> "The CWM baseline is a ≤8B LoRA fine-tuned model, not the original 32B Code World Model with execution trace mid-training. The comparison is unfair—CWM was designed to operate at much larger scale with specialized pretraining. The paper's conclusion that 'generation degrades at repo level' may simply reflect insufficient model capacity rather than a fundamental formulation limitation."
12	
13	### 回应要点
14	
15	**核心论点：matched comparison at controlled capacity isolates formulation effect from scale confounds, which is complementary to—not competing with—scaling studies.**
16	
17	1. **Function-level 证明 LoRA 可以成功适配 CWM formulation。** CLS 和 CWM 在 function-level 达到统计等价（TOST p=0.007, 5 seeds, ±2pp margin），证明同一 LoRA 配置下 CWM formulation 能完全发挥作用。退化仅在 repo-level 出现，不是 LoRA 容量不足的全局问题。
18	
19	2. **退化模式指向 formulation 本身，而非容量瓶颈——四种标准干预全部失败。**
20	   - Format collapse (53–74% unparseable outputs) 是输出空间复杂度问题：function-level 输出为短字符串（integers, booleans），repo-level 输出为无约束执行轨迹（均值 ~477 tokens），错误呈乘性积累
21	   - 即使在可解析输出中，accuracy (38–43%) 仍低于 majority baseline (72.96%)，表明存在超越格式合规的语义鸿沟
22	   - **LoRA rank-32 ablation（双倍参数）：无改善（−0.51pp）**，排除 adapter 容量瓶颈
23	   - **Majority voting K=3：accuracy 反降 0.68pp**（87.51→86.83%），93.3% 样本三次一致，errors 是系统性偏差非随机噪声
24	   - **Relaxed matching（放宽格式要求）：accuracy 反降 1.06pp**（58.04→56.98%），因为 unparseable 默认为 majority class 比模型自身预测更准
25	   - **Model scaling 4B→8B：parseable-only accuracy 反降**（42.88→38.52%），表面 accuracy 提升完全是 default-assignment artifact
26	   - Matched-context ablation：输入差异仅解释 <3% 的 gap
27	   
28	   **每种干预分别靶向不同的替代解释（容量不足 / 随机噪声 / 解析严格 / 模型规模），全部失败。这构成 formulation-level bottleneck 的最强证据链。**
29	
30	   **Convergent null results summary (rebuttal 可直接引用):**
31	   > "Four convergent null results strengthen this argument: (1) doubling model size yields +0.16pp (flat); (2) majority voting K=3 decreases accuracy by 0.69pp, confirming errors are systematic; (3) forced parsing rescues 90.6% of unparseable outputs but accuracy remains below majority baseline (49.4% vs 72.96%); (4) at repo level, scaling from 4B to 8B worsens parseable-only accuracy (42.88→38.52%) while increasing format collapse (54→74%). These collectively rule out adapter capacity, model capacity, inference stochasticity, and format compliance as explanations, localizing the bottleneck to the generation formulation's output space complexity."
32	
33	3. **我们的贡献是 formulation comparison methodology，不是 CWM SOTA。** 本文的价值在于提供首个 matched experimental framework 来隔离 formulation effects。32B CWM 在更大规模上可能表现不同（我们在 Limitations 中明确承认），但 matched comparison 是理解 formulation dynamics 的必要第一步。
34	
35	4. **预备回应："execution trace mid-training 可能改变结果"**
36	
37	   如果 reviewer 追问 "execution trace pretraining is an integral part of CWM, without it your comparison is incomplete"：
38	
39	   > "Function-level equivalence demonstrates LoRA successfully adapts both formulations (TOST p=0.007). The degradation is complexity-conditional, not LoRA-global. Execution trace mid-training may improve CWM's long-output generation capacity, but this represents an orthogonal training paradigm—not a formulation change. Our contribution is isolating the formulation dimension; scaling and pretraining dimensions require separate matched studies."
40	
41	   此论点将 execution trace pretraining 重新定位为 **training paradigm** 而非 **formulation property**——reviewer 如果坚持这是 formulation 的一部分，则需要论证为什么 CLS 和 TRAJ 不需要类似 pretraining 来"公平比较"。
42	
43	### 支撑证据
44	
45	| Evidence | Location |
46	|----------|----------|
47	| TOST equivalence at function-level | §4.2, Table 1 |
48	| Format collapse rates 53–74% | §4.3, Table 4 |
49	| Parseable-only accuracy 38–43% < majority 72.96% | §4.3, Appendix C |
50	| Rank-32 ablation −0.51pp | Appendix B |
51	| Majority voting K=3 −0.68pp | Appendix (g) |
52	| Relaxed matching −1.06pp | Appendix (c) |
53	| Model scaling 4B→8B parseable acc ↓ | §4.3 |
54	| Matched-context ablation <3% | Appendix B |
55	| Output token ratio 1:477 (CLS:CWM) | §4.4 |
56	| Four failed interventions summary | §4.4, Appendix (g) |
57	| Limitation acknowledged | Limitations, §4.5 |
58	
59	### 如果 CWM multi-seed + 14B pilot 数据到齐（增补版）
60	
61	> "We additionally provide multi-seed CWM results (N seeds) confirming the single-seed findings: [具体数据]. A 14B pilot [如果跑了] shows [结果], suggesting that [scaling 趋势]."
62	
63	此段可在 camera-ready 或 rebuttal 中按实际数据填入。
64	
65	---
66	
67	## Attack #2: Repo-Level 单 Seed → 统计力不足
68	
69	### Reviewer 可能措辞
70	
71	> "The repo-level results rely on a single seed for most comparisons. With n=48 variant-level instances, the 19–26pp gap could be an artifact of seed variance. The authors themselves note 'single-seed design and multiple confounds limit causal attribution.' Without multi-seed replication, these results are suggestive at best."
72	
73	### 回应要点（当前版本：数据到齐前）
74	
75	**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**
76	
77	1. **区分两层证据。** Formulation×complexity interaction 在 per-test level 已经 statistically confirmed：
78	   - Cross-complexity LPM：z=−23.7, p<0.001, n=56,480, 139 problem clusters (DeepSeek-Coder)
79	   - Cross-model LPM：CWM deficit −22pp, z=−64.4, p<0.001
80	   - Formulation 解释 >95% of predictable variance
81	   - 这不是 "suggestive evidence"，而是 overwhelming statistical evidence for the interaction
82	
83	2. **Cross-model 方向一致性。** Qwen3 和 DeepSeek-Coder 两个架构不同的模型家族展现相同方向（CLS > CWM），model identity 仅调节 gap magnitude (+1.6pp interaction, z=2.8) 而不改变方向。
84	
85	3. **Gap magnitude 超过所有已评估 confounds。** §4.5 逐一评估 5 个潜在混淆因素，19–26pp gap 超过任何单个 confound（checkpoint <1pp, seq_length ~1.5pp, preprocessing ~8pp cross-config variance）。即使 confounds 相关，gap 的量级提供 substantial margin。
86	
87	4. **Holm-Bonferroni 控制 FWER。** 两个核心 claim 在校正后仍然 significant（adjusted p=0.012 and p=0.021）。
88	
89	5. **Variant-level power 分析。** 即使在 variant-level (n=48)，MDE (minimum detectable effect) ≈ 25pp（two-sided, α=0.05, power=0.8, McNemar's test）。观测到的 CLS–CWM gap 为 29–35pp（视配置），超过 MDE。也就是说：即使在 n=48 的严苛条件下，观测 gap 仍足够大以被统计检测到。这不是 underpowered——是 gap 太大了。
90	
91	### 回应要点（增补版：CWM multi-seed 数据到齐后）
92	
93	> "We have completed multi-seed CWM replication. The [N]-seed mean CWM accuracy is [X]% ± [Y]%, confirming the single-seed finding. The CLS–CWM gap at repo level is [Z]pp (p=[value], [N] seeds), consistent with the per-test interaction effect (z=−23.7). This addresses the reviewer's concern about seed-specific artifacts."
94	
95	如果 multi-seed 方差大于预期：
96	> "The multi-seed variance is [较大], but the gap remains directionally consistent across all seeds. The per-test interaction (z=−23.7, n=56,480) remains the primary evidence for complexity-dependent divergence; variant-level accuracy provides a practical summary statistic."
97	
98	### 支撑证据
99	
100	| Evidence | Location |
101	|----------|----------|
102	| Per-test LPM z=−23.7, n=56,480 | §4.3 |
103	| Cross-model z=−64.4 | §4.3 |
104	| Formulation explains >95% variance | §4.3 |
105	| 5 confounds assessed | §4.5, Appendix F |
106	| Holm-Bonferroni adjusted p | §4.5, Table 5 |
107	| Cross-model consistency | §4.3 |
108	
109	---
110	
111	## Attack #3: 合成突变 vs 真实 Bug
112	
113	### Reviewer 可能措辞
114	
115	> "The training data is synthetically generated via mutation operators, not real developer bugs. SWE-bench uses real GitHub issues, but the training-side synthetic distribution may not transfer. The paper's findings about formulation divergence could be an artifact of the synthetic data distribution rather than a genuine property of the verification task."
116	
117	### 回应要点
118	
119	**核心论点：our core finding concerns relative ordering, not absolute accuracy—relative rankings are expected to be preserved under uniform distributional shifts.**
120	
121	1. **Mutation testing 文献的 established validity。** Andrews et al. (2005) 和 Just et al. (2014) 建立了 mutants 作为真实 faults 的 reasonable proxies 在 test effectiveness 研究中的有效性。我们的 mutation operators (operator_swap, off_by_one, return_value, boundary_removal) 覆盖 PMT 文献中的标准突变类型。
122	
123	2. **Coupling effect 支持 relative ranking validity。** Mutation testing 的 coupling effect 表明：能检测简单突变的 verifier 也倾向于检测复杂真实 bug。这意味着：
124	   - Domain shift 从 synthetic mutations 到 real bugs 可能影响 absolute accuracy levels
125	   - 但 relative performance ordering（即 "formulation choice matters at repo level but not function level"）预期在均匀 distributional shift 下保持不变
126	   - 除非某个 formulation 对 synthetic mutations 有 specific bias（没有理论或实证根据）
127	
128	3. **Evaluation-side 已包含真实数据。** Repo-level evaluation 使用 SWE-bench Verified（来自真实 GitHub issues 和 pull requests），不是 synthetic data。Function-level 使用 HumanEval/MBPP mutants，但 function-level 结果（near-equivalence）恰恰是我们的 positive finding——即使这受 synthetic bias 影响，也只会低估 formulation difference（如果真实 bugs 更难，divergence 可能更大）。
129	
130	4. **Gold parse rate 反直觉证据。** Gold mutations（未修改代码，所有测试通过）是 CWM 最简单的目标——模型只需生成"全部通过"的输出。但 gold 的 parse rate 在 8B 仅 23.9%（最差），parseable-only accuracy 仅 16.5%。这直接反驳 "failure comes from mutation difficulty" 的解释：最简单的任务反而最差，说明失败源于输出空间复杂度本身，而非 mutation-specific 难度。
131	
132	5. **回应 "uniform shift" 质疑的 3 条 counter：**
133	   - **Counter 1 (directionality):** 如果 synthetic bias 导致了 formulation divergence，我们预期 bias 在 function-level 和 repo-level 一致。但 function-level 观察到 equivalence，repo-level 观察到 divergence。一个 uniform bias 无法同时解释 equivalence 和 divergence。
134	   - **Counter 2 (mechanism):** CWM 退化的直接机制是 format collapse (53–74% unparseable) 和 long-output generation failure (mean ~477 tokens)。这些是模型能力的物理限制，与训练数据分布无关——无论用 synthetic 还是 real bugs 训练，477-token output 的生成难度不变。
135	   - **Counter 3 (conservative direction):** 如果 real bugs 比 synthetic mutations 更难（合理假设），那么 CWM 的 repo-level 退化只会更严重——我们的 synthetic 实验给出了 divergence 的 **下界**。
136	
137	6. **Acknowledging the gap。** 我们在 Limitations 中明确承认："the synthetic-to-real transfer gap for absolute accuracy remains untested." 这是诚实的 scope limitation，不削弱 relative ranking finding。
138	
139	### 支撑证据
140	
141	| Evidence | Location |
142	|----------|----------|
143	| Andrews & Just citations | Limitations |
144	| Coupling effect → relative ranking argument | Limitations, Appendix G |
145	| SWE-bench Verified (real GitHub issues) | §4.1 |
146	| HumanEval/MBPP mutation operators | §4.1, Appendix D |
147	| 5 mutation types listed | Appendix D |
148	| Gold parse rate 23.9% (worst among all types) | Appendix C, Table cwm_mutation_parse |
149	| Gold parseable-only accuracy 16.5% | Appendix C |
150	| Limitations acknowledgment | Limitations |
151	
152	---
153	
154	## 交叉防御：多个攻击面的组合回应
155	
156	如果 reviewer 同时提出多个攻击面，统一回应模板：
157	
158	> "We appreciate the reviewer's thorough engagement with our experimental design. We address each concern below, and note a unifying theme: our contribution is primarily **methodological**—providing the first matched experimental framework for comparing verification formulations. The per-test interaction effect (z=−23.7, n=56,480) is statistically robust regardless of (1) model scale, since it isolates formulation effects at controlled capacity; (2) seed count, since it is based on >56K observations with 139 problem-level clusters, not variant-level aggregates; and (3) training data source, since the interaction concerns relative ordering across formulations that share the same training distribution."
159	
160	---
161	
162	## Q2 预备：Re-repair Negative + Oracle Ensemble
163	
164	### Reviewer 可能追问
165	
166	> "The re-repair pilot found no benefit (p=0.42). Doesn't this undermine the practical value of per-test diagnostics, which is one of CLS's main advantages over TRAJ?"
167	
168	### 回应要点
169	
170	1. **Statistical power 不足以检测 medium effect。** n=44 instances, power ≈ 0.3 for medium effect size (Cohen's h=0.3)。p=0.42 是 inconclusive, not evidence of absence。需要 n≈200 才能 power=0.8。
171	
172	2. **Oracle ensemble ceiling 证明 formulation diversity 有实际价值。** 即使 re-repair 未证明直接 downstream benefit：
173	   - Function-level oracle ensemble: 90.63% (+2.80pp over best single)
174	   - Repo-level oracle routing: 95.83% variant accuracy (+14.58pp over best single, n=48)
175	   - 95.83% 意味着：如果有一个 perfect router，只需从已有 formulations 中选择，就可以 resolve 95.83% 的 variants
176	   - 这是 "formulation design space worth exploring" 的最直接证据
177	
178	3. **Per-test diagnostics 的价值不仅限于 re-repair。** CLS 的 per-test granularity 还支持：
179	   - Failure localization（哪些测试失败）
180	   - Confidence estimation（多少测试通过 / 总测试数）
181	   - Selective re-execution（只重跑可疑测试）
182	   - 这些 downstream applications 未被 re-repair pilot 覆盖
183	
184	4. **诚实承认 limitation。** 论文已在 Limitations 中明确标注 re-repair negative + insufficient power。这是透明的科学报告，不是 weakness——reviewer 如果因此降分，可以在 rebuttal 中指出这恰恰是 rigorous self-assessment。
185	
186	---
187	
188	## 状态标注
189	
190	| 攻击面 | 当前防御强度 | 数据到齐后 |
191	|--------|------------|----------|
192	| #1 CWM scale | ★★★★ (4 convergent nulls + exec trace reframing + methodology argument) | ★★★★+ if 14B pilot confirms |
193	| #2 Single seed | ★★★★ (per-test LPM overwhelming + MDE analysis + variant gap > MDE) | ★★★★+ with multi-seed CWM |
194	| #3 Synthetic data | ★★★☆ (coupling effect + gold parse rate counter + 3 uniform-shift counters) | 不变（需要 real-bug training data 才能完全 close，超出 scope） |
195	| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "e5d69ba0-fb36-4541-b260-9fa84c10b615",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
      "content": "# Rebuttal Framework — Pre-Submission Attack Surface Analysis\n\nDate: 2026-05-20 | Venue: EMNLP 2026 ARR\n\n---\n\n## Attack #1: CWM ≤8B LoRA ≠ Real 32B CWM\n\n### Reviewer 可能措辞\n\n> \"The CWM baseline is a ≤8B LoRA fine-tuned model, not the original 32B Code World Model with execution trace mid-training. The comparison is unfair—CWM was designed to operate at much larger scale with specialized pretraining. The paper's conclusion that 'generation degrades at repo level' may simply reflect insufficient model capacity rather than a fundamental formulation limitation.\"\n\n### 回应要点\n\n**核心论点：matched comparison at controlled capacity isolates formulation effect from scale confounds, which is complementary to—not competing with—scaling studies.**\n\n1. **Function-level 证明 LoRA 可以成功适配 CWM formulation。** CLS 和 CWM 在 function-level 达到统计等价（TOST p=0.007, 5 seeds, ±2pp margin），证明同一 LoRA 配置下 CWM formulation 能完全发挥作用。退化仅在 repo-level 出现，不是 LoRA 容量不足的全局问题。\n\n2. **退化模式指向 formulation 本身，而非容量瓶颈——四种标准干预全部失败。**\n   - Format collapse (53–74% unparseable outputs) 是输出空间复杂度问题：function-level 输出为短字符串（integers, booleans），repo-level 输出为无约束执行轨迹（均值 ~477 tokens），错误呈乘性积累\n   - 即使在可解析输出中，accuracy (38–43%) 仍低于 majority baseline (72.96%)，表明存在超越格式合规的语义鸿沟\n   - **LoRA rank-32 ablation（双倍参数）：无改善（−0.51pp）**，排除 adapter 容量瓶颈\n   - **Majority voting K=3：accuracy 反降 0.68pp**（87.51→86.83%），93.3% 样本三次一致，errors 是系统性偏差非随机噪声\n   - **Relaxed matching（放宽格式要求）：accuracy 反降 1.06pp**（58.04→56.98%），因为 unparseable 默认为 majority class 比模型自身预测更准\n   - **Model scaling 4B→8B：parseable-only accuracy 反降**（42.88→38.52%），表面 accuracy 提升完全是 default-assignment artifact\n   - Matched-context ablation：输入差异仅解释 <3% 的 gap\n   \n   **每种干预分别靶向不同的替代解释（容量不足 / 随机噪声 / 解析严格 / 模型规模），全部失败。这构成 formulation-level bottleneck 的最强证据链。**\n\n   **Convergent null results summary (rebuttal 可直接引用):**\n   > \"Four convergent null results strengthen this argument: (1) doubling model size yields +0.16pp (flat); (2) majority voting K=3 decreases accuracy by 0.69pp, confirming errors are systematic; (3) forced parsing rescues 90.6% of unparseable outputs but accuracy remains below majority baseline (49.4% vs 72.96%); (4) at repo level, scaling from 4B to 8B worsens parseable-only accuracy (42.88→38.52%) while increasing format collapse (54→74%). These collectively rule out adapter capacity, model capacity, inference stochasticity, and format compliance as explanations, localizing the bottleneck to the generation formulation's output space complexity.\"\n\n3. **我们的贡献是 formulation comparison methodology，不是 CWM SOTA。** 本文的价值在于提供首个 matched experimental framework 来隔离 formulation effects。32B CWM 在更大规模上可能表现不同（我们在 Limitations 中明确承认），但 matched comparison 是理解 formulation dynamics 的必要第一步。\n\n4. **预备回应：\"execution trace mid-training 可能改变结果\"**\n\n   如果 reviewer 追问 \"execution trace pretraining is an integral part of CWM, without it your comparison is incomplete\"：\n\n   > \"Function-level equivalence demonstrates LoRA successfully adapts both formulations (TOST p=0.007). The degradation is complexity-conditional, not LoRA-global. Execution trace mid-training may improve CWM's long-output generation capacity, but this represents an orthogonal training paradigm—not a formulation change. Our contribution is isolating the formulation dimension; scaling and pretraining dimensions require separate matched studies.\"\n\n   此论点将 execution trace pretraining 重新定位为 **training paradigm** 而非 **formulation property**——reviewer 如果坚持这是 formulation 的一部分，则需要论证为什么 CLS 和 TRAJ 不需要类似 pretraining 来\"公平比较\"。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| TOST equivalence at function-level | §4.2, Table 1 |\n| Format collapse rates 53–74% | §4.3, Table 4 |\n| Parseable-only accuracy 38–43% < majority 72.96% | §4.3, Appendix C |\n| Rank-32 ablation −0.51pp | Appendix B |\n| Majority voting K=3 −0.68pp | Appendix (g) |\n| Relaxed matching −1.06pp | Appendix (c) |\n| Model scaling 4B→8B parseable acc ↓ | §4.3 |\n| Matched-context ablation <3% | Appendix B |\n| Output token ratio 1:477 (CLS:CWM) | §4.4 |\n| Four failed interventions summary | §4.4, Appendix (g) |\n| Limitation acknowledged | Limitations, §4.5 |\n\n### 如果 CWM multi-seed + 14B pilot 数据到齐（增补版）\n\n> \"We additionally provide multi-seed CWM results (N seeds) confirming the single-seed findings: [具体数据]. A 14B pilot [如果跑了] shows [结果], suggesting that [scaling 趋势].\"\n\n此段可在 camera-ready 或 rebuttal 中按实际数据填入。\n\n---\n\n## Attack #2: Repo-Level 单 Seed → 统计力不足\n\n### Reviewer 可能措辞\n\n> \"The repo-level results rely on a single seed for most comparisons. With n=48 variant-level instances, the 19–26pp gap could be an artifact of seed variance. The authors themselves note 'single-seed design and multiple confounds limit causal attribution.' Without multi-seed replication, these results are suggestive at best.\"\n\n### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**\n\n1. **区分两层证据。** Formulation×complexity interaction 在 per-test level 已经 statistically confirmed：\n   - Cross-complexity LPM：z=−23.7, p<0.001, n=56,480, 139 problem clusters (DeepSeek-Coder)\n   - Cross-model LPM：CWM deficit −22pp, z=−64.4, p<0.001\n   - Formulation 解释 >95% of predictable variance\n   - 这不是 \"suggestive evidence\"，而是 overwhelming statistical evidence for the interaction\n\n2. **Cross-model 方向一致性。** Qwen3 和 DeepSeek-Coder 两个架构不同的模型家族展现相同方向（CLS > CWM），model identity 仅调节 gap magnitude (+1.6pp interaction, z=2.8) 而不改变方向。\n\n3. **Gap magnitude 超过所有已评估 confounds。** §4.5 逐一评估 5 个潜在混淆因素，19–26pp gap 超过任何单个 confound（checkpoint <1pp, seq_length ~1.5pp, preprocessing ~8pp cross-config variance）。即使 confounds 相关，gap 的量级提供 substantial margin。\n\n4. **Holm-Bonferroni 控制 FWER。** 两个核心 claim 在校正后仍然 significant（adjusted p=0.012 and p=0.021）。\n\n5. **Variant-level power 分析。** 即使在 variant-level (n=48)，MDE (minimum detectable effect) ≈ 25pp（two-sided, α=0.05, power=0.8, McNemar's test）。观测到的 CLS–CWM gap 为 29–35pp（视配置），超过 MDE。也就是说：即使在 n=48 的严苛条件下，观测 gap 仍足够大以被统计检测到。这不是 underpowered——是 gap 太大了。\n\n### 回应要点（增补版：CWM multi-seed 数据到齐后）\n\n> \"We have completed multi-seed CWM replication. The [N]-seed mean CWM accuracy is [X]% ± [Y]%, confirming the single-seed finding. The CLS–CWM gap at repo level is [Z]pp (p=[value], [N] seeds), consistent with the per-test interaction effect (z=−23.7). This addresses the reviewer's concern about seed-specific artifacts.\"\n\n如果 multi-seed 方差大于预期：\n> \"The multi-seed variance is [较大], but the gap remains directionally consistent across all seeds. The per-test interaction (z=−23.7, n=56,480) remains the primary evidence for complexity-dependent divergence; variant-level accuracy provides a practical summary statistic.\"\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Per-test LPM z=−23.7, n=56,480 | §4.3 |\n| Cross-model z=−64.4 | §4.3 |\n| Formulation explains >95% variance | §4.3 |\n| 5 confounds assessed | §4.5, Appendix F |\n| Holm-Bonferroni adjusted p | §4.5, Table 5 |\n| Cross-model consistency | §4.3 |\n\n---\n\n## Attack #3: 合成突变 vs 真实 Bug\n\n### Reviewer 可能措辞\n\n> \"The training data is synthetically generated via mutation operators, not real developer bugs. SWE-bench uses real GitHub issues, but the training-side synthetic distribution may not transfer. The paper's findings about formulation divergence could be an artifact of the synthetic data distribution rather than a genuine property of the verification task.\"\n\n### 回应要点\n\n**核心论点：our core finding concerns relative ordering, not absolute accuracy—relative rankings are expected to be preserved under uniform distributional shifts.**\n\n1. **Mutation testing 文献的 established validity。** Andrews et al. (2005) 和 Just et al. (2014) 建立了 mutants 作为真实 faults 的 reasonable proxies 在 test effectiveness 研究中的有效性。我们的 mutation operators (operator_swap, off_by_one, return_value, boundary_removal) 覆盖 PMT 文献中的标准突变类型。\n\n2. **Coupling effect 支持 relative ranking validity。** Mutation testing 的 coupling effect 表明：能检测简单突变的 verifier 也倾向于检测复杂真实 bug。这意味着：\n   - Domain shift 从 synthetic mutations 到 real bugs 可能影响 absolute accuracy levels\n   - 但 relative performance ordering（即 \"formulation choice matters at repo level but not function level\"）预期在均匀 distributional shift 下保持不变\n   - 除非某个 formulation 对 synthetic mutations 有 specific bias（没有理论或实证根据）\n\n3. **Evaluation-side 已包含真实数据。** Repo-level evaluation 使用 SWE-bench Verified（来自真实 GitHub issues 和 pull requests），不是 synthetic data。Function-level 使用 HumanEval/MBPP mutants，但 function-level 结果（near-equivalence）恰恰是我们的 positive finding——即使这受 synthetic bias 影响，也只会低估 formulation difference（如果真实 bugs 更难，divergence 可能更大）。\n\n4. **Gold parse rate 反直觉证据。** Gold mutations（未修改代码，所有测试通过）是 CWM 最简单的目标——模型只需生成\"全部通过\"的输出。但 gold 的 parse rate 在 8B 仅 23.9%（最差），parseable-only accuracy 仅 16.5%。这直接反驳 \"failure comes from mutation difficulty\" 的解释：最简单的任务反而最差，说明失败源于输出空间复杂度本身，而非 mutation-specific 难度。\n\n5. **回应 \"uniform shift\" 质疑的 3 条 counter：**\n   - **Counter 1 (directionality):** 如果 synthetic bias 导致了 formulation divergence，我们预期 bias 在 function-level 和 repo-level 一致。但 function-level 观察到 equivalence，repo-level 观察到 divergence。一个 uniform bias 无法同时解释 equivalence 和 divergence。\n   - **Counter 2 (mechanism):** CWM 退化的直接机制是 format collapse (53–74% unparseable) 和 long-output generation failure (mean ~477 tokens)。这些是模型能力的物理限制，与训练数据分布无关——无论用 synthetic 还是 real bugs 训练，477-token output 的生成难度不变。\n   - **Counter 3 (conservative direction):** 如果 real bugs 比 synthetic mutations 更难（合理假设），那么 CWM 的 repo-level 退化只会更严重——我们的 synthetic 实验给出了 divergence 的 **下界**。\n\n6. **Acknowledging the gap。** 我们在 Limitations 中明确承认：\"the synthetic-to-real transfer gap for absolute accuracy remains untested.\" 这是诚实的 scope limitation，不削弱 relative ranking finding。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Andrews & Just citations | Limitations |\n| Coupling effect → relative ranking argument | Limitations, Appendix G |\n| SWE-bench Verified (real GitHub issues) | §4.1 |\n| HumanEval/MBPP mutation operators | §4.1, Appendix D |\n| 5 mutation types listed | Appendix D |\n| Gold parse rate 23.9% (worst among all types) | Appendix C, Table cwm_mutation_parse |\n| Gold parseable-only accuracy 16.5% | Appendix C |\n| Limitations acknowledgment | Limitations |\n\n---\n\n## 交叉防御：多个攻击面的组合回应\n\n如果 reviewer 同时提出多个攻击面，统一回应模板：\n\n> \"We appreciate the reviewer's thorough engagement with our experimental design. We address each concern below, and note a unifying theme: our contribution is primarily **methodological**—providing the first matched experimental framework for comparing verification formulations. The per-test interaction effect (z=−23.7, n=56,480) is statistically robust regardless of (1) model scale, since it isolates formulation effects at controlled capacity; (2) seed count, since it is based on >56K observations with 139 problem-level clusters, not variant-level aggregates; and (3) training data source, since the interaction concerns relative ordering across formulations that share the same training distribution.\"\n\n---\n\n## Q2 预备：Re-repair Negative + Oracle Ensemble\n\n### Reviewer 可能追问\n\n> \"The re-repair pilot found no benefit (p=0.42). Doesn't this undermine the practical value of per-test diagnostics, which is one of CLS's main advantages over TRAJ?\"\n\n### 回应要点\n\n1. **Statistical power 不足以检测 medium effect。** n=44 instances, power ≈ 0.3 for medium effect size (Cohen's h=0.3)。p=0.42 是 inconclusive, not evidence of absence。需要 n≈200 才能 power=0.8。\n\n2. **Oracle ensemble ceiling 证明 formulation diversity 有实际价值。** 即使 re-repair 未证明直接 downstream benefit：\n   - Function-level oracle ensemble: 90.63% (+2.80pp over best single)\n   - Repo-level oracle routing: 95.83% variant accuracy (+14.58pp over best single, n=48)\n   - 95.83% 意味着：如果有一个 perfect router，只需从已有 formulations 中选择，就可以 resolve 95.83% 的 variants\n   - 这是 \"formulation design space worth exploring\" 的最直接证据\n\n3. **Per-test diagnostics 的价值不仅限于 re-repair。** CLS 的 per-test granularity 还支持：\n   - Failure localization（哪些测试失败）\n   - Confidence estimation（多少测试通过 / 总测试数）\n   - Selective re-execution（只重跑可疑测试）\n   - 这些 downstream applications 未被 re-repair pilot 覆盖\n\n4. **诚实承认 limitation。** 论文已在 Limitations 中明确标注 re-repair negative + insufficient power。这是透明的科学报告，不是 weakness——reviewer 如果因此降分，可以在 rebuttal 中指出这恰恰是 rigorous self-assessment。\n\n---\n\n## 状态标注\n\n| 攻击面 | 当前防御强度 | 数据到齐后 |\n|--------|------------|----------|\n| #1 CWM scale | ★★★★ (4 convergent nulls + exec trace reframing + methodology argument) | ★★★★+ if 14B pilot confirms |\n| #2 Single seed | ★★★★ (per-test LPM overwhelming + MDE analysis + variant gap > MDE) | ★★★★+ with multi-seed CWM |\n| #3 Synthetic data | ★★★☆ (coupling effect + gold parse rate counter + 3 uniform-shift counters) | 不变（需要 real-bug training data 才能完全 close，超出 scope） |\n| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |\n",
      "numLines": 196,
      "startLine": 1,
      "totalLines": 196
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full content of the rebuttal framework. Let me plan the edits:

1. **素材 1: CLS 过拟合鲁棒性** — Add under Attack #1 as a new defense point (point 5 or a new subsection)
2. **素材 2: 统计数据更新** — Need to find where Cohen's d, statistical power, Qwen CLS mean are mentioned. Looking at the current content, I don't see these specific numbers in the rebuttal framework. Let me check if there's a section I'm missing... 

I'm searching through the document for the existing statistics section with Cohen's d, statistical power, and Qwen CLS mean values, but they don't appear to be in the current rebuttal framework. They might need to be added as a new section or integrated into Attack #2.

For the materials, I'll add the checkpoint sensitivity analysis to a new reserve section at the end, and place the CWM epoch curve there as well. Then I'll update Attack #1 with the CLS overfitting robustness defense point and incorporate the corrected statistical values into the appropriate sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "77f14bb9-0978-455b-9f98-ceec9643f2f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4DfrhR8NcVbKnW7ANE9UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5576,
      "cache_read_input_tokens": 25331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5576
      },
      "output_tokens": 8,
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

### Assistant

_source line 8_

Now I'll make the edits. I need to:
1. Add CLS overfitting robustness defense under Attack #1
2. Add corrected statistical data to Attack #2
3. Create a "储备/待用" section at the end with the two reserve items

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "ac84c16f-b2b1-46d8-b042-7c5ca22a6889",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4DfrhR8NcVbKnW7ANE9UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5576,
      "cache_read_input_tokens": 25331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5576
      },
      "output_tokens": 8,
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01JcNfu2Lg59EG27qdjsYMqW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
  "old_string": "4. **预备回应：\"execution trace mid-training 可能改变结果\"**",
  "new_string": "4. **CLS 过拟合鲁棒性（formulation-level 差异）。** CLS 和 CWM 在相同训练配置下表现出截然不同的过拟合行为：\n   - CLS: eval_loss 涨 123%，但 accuracy 仅下降 0.1pp → classification formulation 对过拟合天然鲁棒\n   - CWM: eval_loss 上升后 accuracy 下降 5.36pp (epoch 2→3) → generation formulation 更敏感\n   - 即使 oracle early stopping (epoch 1 = 75.45%)，CWM 仍 ~7pp below CLS 且 66% unparseable\n   - 结论：这是 formulation-level 的固有差异，不是 training-level 的超参问题\n\n   数据来源：\n   - CLS: registry cls8b-s42 系列\n   - CWM epoch 2→3: deepseek-cwm-repo-s42 (66.85% → 61.49%, -5.36pp)\n   - CWM epoch 1: deepseek-cwm-repo-s123-eval-1epoch (75.45%, unparseable 66.4%)\n\n5. **预备回应：\"execution trace mid-training 可能改变结果\"**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "1f77f2d5-d602-4232-862f-ea51616233d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4DfrhR8NcVbKnW7ANE9UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5576,
      "cache_read_input_tokens": 25331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5576
      },
      "output_tokens": 8,
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

_source line 10 · 2026-05-21T08:43:08.815Z_

<details><summary>↩ Tool result · `toolu_01JcNfu2Lg59EG27qdjsYMqW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "c53aedce-b190-42a5-bc3a-3240706b96cd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
    "oldString": "4. **预备回应：\"execution trace mid-training 可能改变结果\"**",
    "newString": "4. **CLS 过拟合鲁棒性（formulation-level 差异）。** CLS 和 CWM 在相同训练配置下表现出截然不同的过拟合行为：\n   - CLS: eval_loss 涨 123%，但 accuracy 仅下降 0.1pp → classification formulation 对过拟合天然鲁棒\n   - CWM: eval_loss 上升后 accuracy 下降 5.36pp (epoch 2→3) → generation formulation 更敏感\n   - 即使 oracle early stopping (epoch 1 = 75.45%)，CWM 仍 ~7pp below CLS 且 66% unparseable\n   - 结论：这是 formulation-level 的固有差异，不是 training-level 的超参问题\n\n   数据来源：\n   - CLS: registry cls8b-s42 系列\n   - CWM epoch 2→3: deepseek-cwm-repo-s42 (66.85% → 61.49%, -5.36pp)\n   - CWM epoch 1: deepseek-cwm-repo-s123-eval-1epoch (75.45%, unparseable 66.4%)\n\n5. **预备回应：\"execution trace mid-training 可能改变结果\"**",
    "originalFile": "# Rebuttal Framework — Pre-Submission Attack Surface Analysis\n\nDate: 2026-05-20 | Venue: EMNLP 2026 ARR\n\n---\n\n## Attack #1: CWM ≤8B LoRA ≠ Real 32B CWM\n\n### Reviewer 可能措辞\n\n> \"The CWM baseline is a ≤8B LoRA fine-tuned model, not the original 32B Code World Model with execution trace mid-training. The comparison is unfair—CWM was designed to operate at much larger scale with specialized pretraining. The paper's conclusion that 'generation degrades at repo level' may simply reflect insufficient model capacity rather than a fundamental formulation limitation.\"\n\n### 回应要点\n\n**核心论点：matched comparison at controlled capacity isolates formulation effect from scale confounds, which is complementary to—not competing with—scaling studies.**\n\n1. **Function-level 证明 LoRA 可以成功适配 CWM formulation。** CLS 和 CWM 在 function-level 达到统计等价（TOST p=0.007, 5 seeds, ±2pp margin），证明同一 LoRA 配置下 CWM formulation 能完全发挥作用。退化仅在 repo-level 出现，不是 LoRA 容量不足的全局问题。\n\n2. **退化模式指向 formulation 本身，而非容量瓶颈——四种标准干预全部失败。**\n   - Format collapse (53–74% unparseable outputs) 是输出空间复杂度问题：function-level 输出为短字符串（integers, booleans），repo-level 输出为无约束执行轨迹（均值 ~477 tokens），错误呈乘性积累\n   - 即使在可解析输出中，accuracy (38–43%) 仍低于 majority baseline (72.96%)，表明存在超越格式合规的语义鸿沟\n   - **LoRA rank-32 ablation（双倍参数）：无改善（−0.51pp）**，排除 adapter 容量瓶颈\n   - **Majority voting K=3：accuracy 反降 0.68pp**（87.51→86.83%），93.3% 样本三次一致，errors 是系统性偏差非随机噪声\n   - **Relaxed matching（放宽格式要求）：accuracy 反降 1.06pp**（58.04→56.98%），因为 unparseable 默认为 majority class 比模型自身预测更准\n   - **Model scaling 4B→8B：parseable-only accuracy 反降**（42.88→38.52%），表面 accuracy 提升完全是 default-assignment artifact\n   - Matched-context ablation：输入差异仅解释 <3% 的 gap\n   \n   **每种干预分别靶向不同的替代解释（容量不足 / 随机噪声 / 解析严格 / 模型规模），全部失败。这构成 formulation-level bottleneck 的最强证据链。**\n\n   **Convergent null results summary (rebuttal 可直接引用):**\n   > \"Four convergent null results strengthen this argument: (1) doubling model size yields +0.16pp (flat); (2) majority voting K=3 decreases accuracy by 0.69pp, confirming errors are systematic; (3) forced parsing rescues 90.6% of unparseable outputs but accuracy remains below majority baseline (49.4% vs 72.96%); (4) at repo level, scaling from 4B to 8B worsens parseable-only accuracy (42.88→38.52%) while increasing format collapse (54→74%). These collectively rule out adapter capacity, model capacity, inference stochasticity, and format compliance as explanations, localizing the bottleneck to the generation formulation's output space complexity.\"\n\n3. **我们的贡献是 formulation comparison methodology，不是 CWM SOTA。** 本文的价值在于提供首个 matched experimental framework 来隔离 formulation effects。32B CWM 在更大规模上可能表现不同（我们在 Limitations 中明确承认），但 matched comparison 是理解 formulation dynamics 的必要第一步。\n\n4. **预备回应：\"execution trace mid-training 可能改变结果\"**\n\n   如果 reviewer 追问 \"execution trace pretraining is an integral part of CWM, without it your comparison is incomplete\"：\n\n   > \"Function-level equivalence demonstrates LoRA successfully adapts both formulations (TOST p=0.007). The degradation is complexity-conditional, not LoRA-global. Execution trace mid-training may improve CWM's long-output generation capacity, but this represents an orthogonal training paradigm—not a formulation change. Our contribution is isolating the formulation dimension; scaling and pretraining dimensions require separate matched studies.\"\n\n   此论点将 execution trace pretraining 重新定位为 **training paradigm** 而非 **formulation property**——reviewer 如果坚持这是 formulation 的一部分，则需要论证为什么 CLS 和 TRAJ 不需要类似 pretraining 来\"公平比较\"。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| TOST equivalence at function-level | §4.2, Table 1 |\n| Format collapse rates 53–74% | §4.3, Table 4 |\n| Parseable-only accuracy 38–43% < majority 72.96% | §4.3, Appendix C |\n| Rank-32 ablation −0.51pp | Appendix B |\n| Majority voting K=3 −0.68pp | Appendix (g) |\n| Relaxed matching −1.06pp | Appendix (c) |\n| Model scaling 4B→8B parseable acc ↓ | §4.3 |\n| Matched-context ablation <3% | Appendix B |\n| Output token ratio 1:477 (CLS:CWM) | §4.4 |\n| Four failed interventions summary | §4.4, Appendix (g) |\n| Limitation acknowledged | Limitations, §4.5 |\n\n### 如果 CWM multi-seed + 14B pilot 数据到齐（增补版）\n\n> \"We additionally provide multi-seed CWM results (N seeds) confirming the single-seed findings: [具体数据]. A 14B pilot [如果跑了] shows [结果], suggesting that [scaling 趋势].\"\n\n此段可在 camera-ready 或 rebuttal 中按实际数据填入。\n\n---\n\n## Attack #2: Repo-Level 单 Seed → 统计力不足\n\n### Reviewer 可能措辞\n\n> \"The repo-level results rely on a single seed for most comparisons. With n=48 variant-level instances, the 19–26pp gap could be an artifact of seed variance. The authors themselves note 'single-seed design and multiple confounds limit causal attribution.' Without multi-seed replication, these results are suggestive at best.\"\n\n### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**\n\n1. **区分两层证据。** Formulation×complexity interaction 在 per-test level 已经 statistically confirmed：\n   - Cross-complexity LPM：z=−23.7, p<0.001, n=56,480, 139 problem clusters (DeepSeek-Coder)\n   - Cross-model LPM：CWM deficit −22pp, z=−64.4, p<0.001\n   - Formulation 解释 >95% of predictable variance\n   - 这不是 \"suggestive evidence\"，而是 overwhelming statistical evidence for the interaction\n\n2. **Cross-model 方向一致性。** Qwen3 和 DeepSeek-Coder 两个架构不同的模型家族展现相同方向（CLS > CWM），model identity 仅调节 gap magnitude (+1.6pp interaction, z=2.8) 而不改变方向。\n\n3. **Gap magnitude 超过所有已评估 confounds。** §4.5 逐一评估 5 个潜在混淆因素，19–26pp gap 超过任何单个 confound（checkpoint <1pp, seq_length ~1.5pp, preprocessing ~8pp cross-config variance）。即使 confounds 相关，gap 的量级提供 substantial margin。\n\n4. **Holm-Bonferroni 控制 FWER。** 两个核心 claim 在校正后仍然 significant（adjusted p=0.012 and p=0.021）。\n\n5. **Variant-level power 分析。** 即使在 variant-level (n=48)，MDE (minimum detectable effect) ≈ 25pp（two-sided, α=0.05, power=0.8, McNemar's test）。观测到的 CLS–CWM gap 为 29–35pp（视配置），超过 MDE。也就是说：即使在 n=48 的严苛条件下，观测 gap 仍足够大以被统计检测到。这不是 underpowered——是 gap 太大了。\n\n### 回应要点（增补版：CWM multi-seed 数据到齐后）\n\n> \"We have completed multi-seed CWM replication. The [N]-seed mean CWM accuracy is [X]% ± [Y]%, confirming the single-seed finding. The CLS–CWM gap at repo level is [Z]pp (p=[value], [N] seeds), consistent with the per-test interaction effect (z=−23.7). This addresses the reviewer's concern about seed-specific artifacts.\"\n\n如果 multi-seed 方差大于预期：\n> \"The multi-seed variance is [较大], but the gap remains directionally consistent across all seeds. The per-test interaction (z=−23.7, n=56,480) remains the primary evidence for complexity-dependent divergence; variant-level accuracy provides a practical summary statistic.\"\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Per-test LPM z=−23.7, n=56,480 | §4.3 |\n| Cross-model z=−64.4 | §4.3 |\n| Formulation explains >95% variance | §4.3 |\n| 5 confounds assessed | §4.5, Appendix F |\n| Holm-Bonferroni adjusted p | §4.5, Table 5 |\n| Cross-model consistency | §4.3 |\n\n---\n\n## Attack #3: 合成突变 vs 真实 Bug\n\n### Reviewer 可能措辞\n\n> \"The training data is synthetically generated via mutation operators, not real developer bugs. SWE-bench uses real GitHub issues, but the training-side synthetic distribution may not transfer. The paper's findings about formulation divergence could be an artifact of the synthetic data distribution rather than a genuine property of the verification task.\"\n\n### 回应要点\n\n**核心论点：our core finding concerns relative ordering, not absolute accuracy—relative rankings are expected to be preserved under uniform distributional shifts.**\n\n1. **Mutation testing 文献的 established validity。** Andrews et al. (2005) 和 Just et al. (2014) 建立了 mutants 作为真实 faults 的 reasonable proxies 在 test effectiveness 研究中的有效性。我们的 mutation operators (operator_swap, off_by_one, return_value, boundary_removal) 覆盖 PMT 文献中的标准突变类型。\n\n2. **Coupling effect 支持 relative ranking validity。** Mutation testing 的 coupling effect 表明：能检测简单突变的 verifier 也倾向于检测复杂真实 bug。这意味着：\n   - Domain shift 从 synthetic mutations 到 real bugs 可能影响 absolute accuracy levels\n   - 但 relative performance ordering（即 \"formulation choice matters at repo level but not function level\"）预期在均匀 distributional shift 下保持不变\n   - 除非某个 formulation 对 synthetic mutations 有 specific bias（没有理论或实证根据）\n\n3. **Evaluation-side 已包含真实数据。** Repo-level evaluation 使用 SWE-bench Verified（来自真实 GitHub issues 和 pull requests），不是 synthetic data。Function-level 使用 HumanEval/MBPP mutants，但 function-level 结果（near-equivalence）恰恰是我们的 positive finding——即使这受 synthetic bias 影响，也只会低估 formulation difference（如果真实 bugs 更难，divergence 可能更大）。\n\n4. **Gold parse rate 反直觉证据。** Gold mutations（未修改代码，所有测试通过）是 CWM 最简单的目标——模型只需生成\"全部通过\"的输出。但 gold 的 parse rate 在 8B 仅 23.9%（最差），parseable-only accuracy 仅 16.5%。这直接反驳 \"failure comes from mutation difficulty\" 的解释：最简单的任务反而最差，说明失败源于输出空间复杂度本身，而非 mutation-specific 难度。\n\n5. **回应 \"uniform shift\" 质疑的 3 条 counter：**\n   - **Counter 1 (directionality):** 如果 synthetic bias 导致了 formulation divergence，我们预期 bias 在 function-level 和 repo-level 一致。但 function-level 观察到 equivalence，repo-level 观察到 divergence。一个 uniform bias 无法同时解释 equivalence 和 divergence。\n   - **Counter 2 (mechanism):** CWM 退化的直接机制是 format collapse (53–74% unparseable) 和 long-output generation failure (mean ~477 tokens)。这些是模型能力的物理限制，与训练数据分布无关——无论用 synthetic 还是 real bugs 训练，477-token output 的生成难度不变。\n   - **Counter 3 (conservative direction):** 如果 real bugs 比 synthetic mutations 更难（合理假设），那么 CWM 的 repo-level 退化只会更严重——我们的 synthetic 实验给出了 divergence 的 **下界**。\n\n6. **Acknowledging the gap。** 我们在 Limitations 中明确承认：\"the synthetic-to-real transfer gap for absolute accuracy remains untested.\" 这是诚实的 scope limitation，不削弱 relative ranking finding。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Andrews & Just citations | Limitations |\n| Coupling effect → relative ranking argument | Limitations, Appendix G |\n| SWE-bench Verified (real GitHub issues) | §4.1 |\n| HumanEval/MBPP mutation operators | §4.1, Appendix D |\n| 5 mutation types listed | Appendix D |\n| Gold parse rate 23.9% (worst among all types) | Appendix C, Table cwm_mutation_parse |\n| Gold parseable-only accuracy 16.5% | Appendix C |\n| Limitations acknowledgment | Limitations |\n\n---\n\n## 交叉防御：多个攻击面的组合回应\n\n如果 reviewer 同时提出多个攻击面，统一回应模板：\n\n> \"We appreciate the reviewer's thorough engagement with our experimental design. We address each concern below, and note a unifying theme: our contribution is primarily **methodological**—providing the first matched experimental framework for comparing verification formulations. The per-test interaction effect (z=−23.7, n=56,480) is statistically robust regardless of (1) model scale, since it isolates formulation effects at controlled capacity; (2) seed count, since it is based on >56K observations with 139 problem-level clusters, not variant-level aggregates; and (3) training data source, since the interaction concerns relative ordering across formulations that share the same training distribution.\"\n\n---\n\n## Q2 预备：Re-repair Negative + Oracle Ensemble\n\n### Reviewer 可能追问\n\n> \"The re-repair pilot found no benefit (p=0.42). Doesn't this undermine the practical value of per-test diagnostics, which is one of CLS's main advantages over TRAJ?\"\n\n### 回应要点\n\n1. **Statistical power 不足以检测 medium effect。** n=44 instances, power ≈ 0.3 for medium effect size (Cohen's h=0.3)。p=0.42 是 inconclusive, not evidence of absence。需要 n≈200 才能 power=0.8。\n\n2. **Oracle ensemble ceiling 证明 formulation diversity 有实际价值。** 即使 re-repair 未证明直接 downstream benefit：\n   - Function-level oracle ensemble: 90.63% (+2.80pp over best single)\n   - Repo-level oracle routing: 95.83% variant accuracy (+14.58pp over best single, n=48)\n   - 95.83% 意味着：如果有一个 perfect router，只需从已有 formulations 中选择，就可以 resolve 95.83% 的 variants\n   - 这是 \"formulation design space worth exploring\" 的最直接证据\n\n3. **Per-test diagnostics 的价值不仅限于 re-repair。** CLS 的 per-test granularity 还支持：\n   - Failure localization（哪些测试失败）\n   - Confidence estimation（多少测试通过 / 总测试数）\n   - Selective re-execution（只重跑可疑测试）\n   - 这些 downstream applications 未被 re-repair pilot 覆盖\n\n4. **诚实承认 limitation。** 论文已在 Limitations 中明确标注 re-repair negative + insufficient power。这是透明的科学报告，不是 weakness——reviewer 如果因此降分，可以在 rebuttal 中指出这恰恰是 rigorous self-assessment。\n\n---\n\n## 状态标注\n\n| 攻击面 | 当前防御强度 | 数据到齐后 |\n|--------|------------|----------|\n| #1 CWM scale | ★★★★ (4 convergent nulls + exec trace reframing + methodology argument) | ★★★★+ if 14B pilot confirms |\n| #2 Single seed | ★★★★ (per-test LPM overwhelming + MDE analysis + variant gap > MDE) | ★★★★+ with multi-seed CWM |\n| #3 Synthetic data | ★★★☆ (coupling effect + gold parse rate counter + 3 uniform-shift counters) | 不变（需要 real-bug training data 才能完全 close，超出 scope） |\n| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 8,
        "newStart": 32,
        "newLines": 19,
        "lines": [
          " ",
          " 3. **我们的贡献是 formulation comparison methodology，不是 CWM SOTA。** 本文的价值在于提供首个 matched experimental framework 来隔离 formulation effects。32B CWM 在更大规模上可能表现不同（我们在 Limitations 中明确承认），但 matched comparison 是理解 formulation dynamics 的必要第一步。",
          " ",
          "-4. **预备回应：\"execution trace mid-training 可能改变结果\"**",
          "+4. **CLS 过拟合鲁棒性（formulation-level 差异）。** CLS 和 CWM 在相同训练配置下表现出截然不同的过拟合行为：",
          "+   - CLS: eval_loss 涨 123%，但 accuracy 仅下降 0.1pp → classification formulation 对过拟合天然鲁棒",
          "+   - CWM: eval_loss 上升后 accuracy 下降 5.36pp (epoch 2→3) → generation formulation 更敏感",
          "+   - 即使 oracle early stopping (epoch 1 = 75.45%)，CWM 仍 ~7pp below CLS 且 66% unparseable",
          "+   - 结论：这是 formulation-level 的固有差异，不是 training-level 的超参问题",
          " ",
          "+   数据来源：",
          "+   - CLS: registry cls8b-s42 系列",
          "+   - CWM epoch 2→3: deepseek-cwm-repo-s42 (66.85% → 61.49%, -5.36pp)",
          "+   - CWM epoch 1: deepseek-cwm-repo-s123-eval-1epoch (75.45%, unparseable 66.4%)",
          "+",
          "+5. **预备回应：\"execution trace mid-training 可能改变结果\"**",
          "+",
          "    如果 reviewer 追问 \"execution trace pretraining is an integral part of CWM, without it your comparison is incomplete\"：",
          " ",
          "    > \"Function-level equivalence demonstrates LoRA successfully adapts both formulations (TOST p=0.007). The degradation is complexity-conditional, not LoRA-global. Execution trace mid-training may improve CWM's long-output generation capacity, but this represents an orthogonal training paradigm—not a formulation change. Our contribution is isolating the formulation dimension; scaling and pretraining dimensions require separate matched studies.\""
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01HBuRiFVVYp1UVSGeNQ5anE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
  "old_string": "### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**",
  "new_string": "### 补充统计数据（M027 修正后）\n\n| Metric | 修正前 | 修正后 | 备注 |\n|--------|--------|--------|------|\n| Cohen's d (CLS vs TRAJ, Qwen) | 5.015 | **4.590** | 仍为 very large (>0.8 threshold) |\n| Statistical power (Qwen) | 0.940 | **0.914** | 仍 >0.80 sufficient threshold |\n| Qwen CLS mean | 85.11 | **84.83** | — |\n\n修正原因：Qwen CLS s42 和 TRAJ s42 值与 D159 决策对齐。\n\n### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "f681863f-9a7d-41a7-be11-47a7c4bf9ab7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013frgHydrT9AMuhoVw6ytBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1214,
      "cache_read_input_tokens": 30907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1214
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

_source line 12 · 2026-05-21T08:43:18.711Z_

<details><summary>↩ Tool result · `toolu_01HBuRiFVVYp1UVSGeNQ5anE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "83a36c4c-7f79-4e87-9ee5-56b48832ab43",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
    "oldString": "### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**",
    "newString": "### 补充统计数据（M027 修正后）\n\n| Metric | 修正前 | 修正后 | 备注 |\n|--------|--------|--------|------|\n| Cohen's d (CLS vs TRAJ, Qwen) | 5.015 | **4.590** | 仍为 very large (>0.8 threshold) |\n| Statistical power (Qwen) | 0.940 | **0.914** | 仍 >0.80 sufficient threshold |\n| Qwen CLS mean | 85.11 | **84.83** | — |\n\n修正原因：Qwen CLS s42 和 TRAJ s42 值与 D159 决策对齐。\n\n### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**",
    "originalFile": "# Rebuttal Framework — Pre-Submission Attack Surface Analysis\n\nDate: 2026-05-20 | Venue: EMNLP 2026 ARR\n\n---\n\n## Attack #1: CWM ≤8B LoRA ≠ Real 32B CWM\n\n### Reviewer 可能措辞\n\n> \"The CWM baseline is a ≤8B LoRA fine-tuned model, not the original 32B Code World Model with execution trace mid-training. The comparison is unfair—CWM was designed to operate at much larger scale with specialized pretraining. The paper's conclusion that 'generation degrades at repo level' may simply reflect insufficient model capacity rather than a fundamental formulation limitation.\"\n\n### 回应要点\n\n**核心论点：matched comparison at controlled capacity isolates formulation effect from scale confounds, which is complementary to—not competing with—scaling studies.**\n\n1. **Function-level 证明 LoRA 可以成功适配 CWM formulation。** CLS 和 CWM 在 function-level 达到统计等价（TOST p=0.007, 5 seeds, ±2pp margin），证明同一 LoRA 配置下 CWM formulation 能完全发挥作用。退化仅在 repo-level 出现，不是 LoRA 容量不足的全局问题。\n\n2. **退化模式指向 formulation 本身，而非容量瓶颈——四种标准干预全部失败。**\n   - Format collapse (53–74% unparseable outputs) 是输出空间复杂度问题：function-level 输出为短字符串（integers, booleans），repo-level 输出为无约束执行轨迹（均值 ~477 tokens），错误呈乘性积累\n   - 即使在可解析输出中，accuracy (38–43%) 仍低于 majority baseline (72.96%)，表明存在超越格式合规的语义鸿沟\n   - **LoRA rank-32 ablation（双倍参数）：无改善（−0.51pp）**，排除 adapter 容量瓶颈\n   - **Majority voting K=3：accuracy 反降 0.68pp**（87.51→86.83%），93.3% 样本三次一致，errors 是系统性偏差非随机噪声\n   - **Relaxed matching（放宽格式要求）：accuracy 反降 1.06pp**（58.04→56.98%），因为 unparseable 默认为 majority class 比模型自身预测更准\n   - **Model scaling 4B→8B：parseable-only accuracy 反降**（42.88→38.52%），表面 accuracy 提升完全是 default-assignment artifact\n   - Matched-context ablation：输入差异仅解释 <3% 的 gap\n   \n   **每种干预分别靶向不同的替代解释（容量不足 / 随机噪声 / 解析严格 / 模型规模），全部失败。这构成 formulation-level bottleneck 的最强证据链。**\n\n   **Convergent null results summary (rebuttal 可直接引用):**\n   > \"Four convergent null results strengthen this argument: (1) doubling model size yields +0.16pp (flat); (2) majority voting K=3 decreases accuracy by 0.69pp, confirming errors are systematic; (3) forced parsing rescues 90.6% of unparseable outputs but accuracy remains below majority baseline (49.4% vs 72.96%); (4) at repo level, scaling from 4B to 8B worsens parseable-only accuracy (42.88→38.52%) while increasing format collapse (54→74%). These collectively rule out adapter capacity, model capacity, inference stochasticity, and format compliance as explanations, localizing the bottleneck to the generation formulation's output space complexity.\"\n\n3. **我们的贡献是 formulation comparison methodology，不是 CWM SOTA。** 本文的价值在于提供首个 matched experimental framework 来隔离 formulation effects。32B CWM 在更大规模上可能表现不同（我们在 Limitations 中明确承认），但 matched comparison 是理解 formulation dynamics 的必要第一步。\n\n4. **CLS 过拟合鲁棒性（formulation-level 差异）。** CLS 和 CWM 在相同训练配置下表现出截然不同的过拟合行为：\n   - CLS: eval_loss 涨 123%，但 accuracy 仅下降 0.1pp → classification formulation 对过拟合天然鲁棒\n   - CWM: eval_loss 上升后 accuracy 下降 5.36pp (epoch 2→3) → generation formulation 更敏感\n   - 即使 oracle early stopping (epoch 1 = 75.45%)，CWM 仍 ~7pp below CLS 且 66% unparseable\n   - 结论：这是 formulation-level 的固有差异，不是 training-level 的超参问题\n\n   数据来源：\n   - CLS: registry cls8b-s42 系列\n   - CWM epoch 2→3: deepseek-cwm-repo-s42 (66.85% → 61.49%, -5.36pp)\n   - CWM epoch 1: deepseek-cwm-repo-s123-eval-1epoch (75.45%, unparseable 66.4%)\n\n5. **预备回应：\"execution trace mid-training 可能改变结果\"**\n\n   如果 reviewer 追问 \"execution trace pretraining is an integral part of CWM, without it your comparison is incomplete\"：\n\n   > \"Function-level equivalence demonstrates LoRA successfully adapts both formulations (TOST p=0.007). The degradation is complexity-conditional, not LoRA-global. Execution trace mid-training may improve CWM's long-output generation capacity, but this represents an orthogonal training paradigm—not a formulation change. Our contribution is isolating the formulation dimension; scaling and pretraining dimensions require separate matched studies.\"\n\n   此论点将 execution trace pretraining 重新定位为 **training paradigm** 而非 **formulation property**——reviewer 如果坚持这是 formulation 的一部分，则需要论证为什么 CLS 和 TRAJ 不需要类似 pretraining 来\"公平比较\"。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| TOST equivalence at function-level | §4.2, Table 1 |\n| Format collapse rates 53–74% | §4.3, Table 4 |\n| Parseable-only accuracy 38–43% < majority 72.96% | §4.3, Appendix C |\n| Rank-32 ablation −0.51pp | Appendix B |\n| Majority voting K=3 −0.68pp | Appendix (g) |\n| Relaxed matching −1.06pp | Appendix (c) |\n| Model scaling 4B→8B parseable acc ↓ | §4.3 |\n| Matched-context ablation <3% | Appendix B |\n| Output token ratio 1:477 (CLS:CWM) | §4.4 |\n| Four failed interventions summary | §4.4, Appendix (g) |\n| Limitation acknowledged | Limitations, §4.5 |\n\n### 如果 CWM multi-seed + 14B pilot 数据到齐（增补版）\n\n> \"We additionally provide multi-seed CWM results (N seeds) confirming the single-seed findings: [具体数据]. A 14B pilot [如果跑了] shows [结果], suggesting that [scaling 趋势].\"\n\n此段可在 camera-ready 或 rebuttal 中按实际数据填入。\n\n---\n\n## Attack #2: Repo-Level 单 Seed → 统计力不足\n\n### Reviewer 可能措辞\n\n> \"The repo-level results rely on a single seed for most comparisons. With n=48 variant-level instances, the 19–26pp gap could be an artifact of seed variance. The authors themselves note 'single-seed design and multiple confounds limit causal attribution.' Without multi-seed replication, these results are suggestive at best.\"\n\n### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**\n\n1. **区分两层证据。** Formulation×complexity interaction 在 per-test level 已经 statistically confirmed：\n   - Cross-complexity LPM：z=−23.7, p<0.001, n=56,480, 139 problem clusters (DeepSeek-Coder)\n   - Cross-model LPM：CWM deficit −22pp, z=−64.4, p<0.001\n   - Formulation 解释 >95% of predictable variance\n   - 这不是 \"suggestive evidence\"，而是 overwhelming statistical evidence for the interaction\n\n2. **Cross-model 方向一致性。** Qwen3 和 DeepSeek-Coder 两个架构不同的模型家族展现相同方向（CLS > CWM），model identity 仅调节 gap magnitude (+1.6pp interaction, z=2.8) 而不改变方向。\n\n3. **Gap magnitude 超过所有已评估 confounds。** §4.5 逐一评估 5 个潜在混淆因素，19–26pp gap 超过任何单个 confound（checkpoint <1pp, seq_length ~1.5pp, preprocessing ~8pp cross-config variance）。即使 confounds 相关，gap 的量级提供 substantial margin。\n\n4. **Holm-Bonferroni 控制 FWER。** 两个核心 claim 在校正后仍然 significant（adjusted p=0.012 and p=0.021）。\n\n5. **Variant-level power 分析。** 即使在 variant-level (n=48)，MDE (minimum detectable effect) ≈ 25pp（two-sided, α=0.05, power=0.8, McNemar's test）。观测到的 CLS–CWM gap 为 29–35pp（视配置），超过 MDE。也就是说：即使在 n=48 的严苛条件下，观测 gap 仍足够大以被统计检测到。这不是 underpowered——是 gap 太大了。\n\n### 回应要点（增补版：CWM multi-seed 数据到齐后）\n\n> \"We have completed multi-seed CWM replication. The [N]-seed mean CWM accuracy is [X]% ± [Y]%, confirming the single-seed finding. The CLS–CWM gap at repo level is [Z]pp (p=[value], [N] seeds), consistent with the per-test interaction effect (z=−23.7). This addresses the reviewer's concern about seed-specific artifacts.\"\n\n如果 multi-seed 方差大于预期：\n> \"The multi-seed variance is [较大], but the gap remains directionally consistent across all seeds. The per-test interaction (z=−23.7, n=56,480) remains the primary evidence for complexity-dependent divergence; variant-level accuracy provides a practical summary statistic.\"\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Per-test LPM z=−23.7, n=56,480 | §4.3 |\n| Cross-model z=−64.4 | §4.3 |\n| Formulation explains >95% variance | §4.3 |\n| 5 confounds assessed | §4.5, Appendix F |\n| Holm-Bonferroni adjusted p | §4.5, Table 5 |\n| Cross-model consistency | §4.3 |\n\n---\n\n## Attack #3: 合成突变 vs 真实 Bug\n\n### Reviewer 可能措辞\n\n> \"The training data is synthetically generated via mutation operators, not real developer bugs. SWE-bench uses real GitHub issues, but the training-side synthetic distribution may not transfer. The paper's findings about formulation divergence could be an artifact of the synthetic data distribution rather than a genuine property of the verification task.\"\n\n### 回应要点\n\n**核心论点：our core finding concerns relative ordering, not absolute accuracy—relative rankings are expected to be preserved under uniform distributional shifts.**\n\n1. **Mutation testing 文献的 established validity。** Andrews et al. (2005) 和 Just et al. (2014) 建立了 mutants 作为真实 faults 的 reasonable proxies 在 test effectiveness 研究中的有效性。我们的 mutation operators (operator_swap, off_by_one, return_value, boundary_removal) 覆盖 PMT 文献中的标准突变类型。\n\n2. **Coupling effect 支持 relative ranking validity。** Mutation testing 的 coupling effect 表明：能检测简单突变的 verifier 也倾向于检测复杂真实 bug。这意味着：\n   - Domain shift 从 synthetic mutations 到 real bugs 可能影响 absolute accuracy levels\n   - 但 relative performance ordering（即 \"formulation choice matters at repo level but not function level\"）预期在均匀 distributional shift 下保持不变\n   - 除非某个 formulation 对 synthetic mutations 有 specific bias（没有理论或实证根据）\n\n3. **Evaluation-side 已包含真实数据。** Repo-level evaluation 使用 SWE-bench Verified（来自真实 GitHub issues 和 pull requests），不是 synthetic data。Function-level 使用 HumanEval/MBPP mutants，但 function-level 结果（near-equivalence）恰恰是我们的 positive finding——即使这受 synthetic bias 影响，也只会低估 formulation difference（如果真实 bugs 更难，divergence 可能更大）。\n\n4. **Gold parse rate 反直觉证据。** Gold mutations（未修改代码，所有测试通过）是 CWM 最简单的目标——模型只需生成\"全部通过\"的输出。但 gold 的 parse rate 在 8B 仅 23.9%（最差），parseable-only accuracy 仅 16.5%。这直接反驳 \"failure comes from mutation difficulty\" 的解释：最简单的任务反而最差，说明失败源于输出空间复杂度本身，而非 mutation-specific 难度。\n\n5. **回应 \"uniform shift\" 质疑的 3 条 counter：**\n   - **Counter 1 (directionality):** 如果 synthetic bias 导致了 formulation divergence，我们预期 bias 在 function-level 和 repo-level 一致。但 function-level 观察到 equivalence，repo-level 观察到 divergence。一个 uniform bias 无法同时解释 equivalence 和 divergence。\n   - **Counter 2 (mechanism):** CWM 退化的直接机制是 format collapse (53–74% unparseable) 和 long-output generation failure (mean ~477 tokens)。这些是模型能力的物理限制，与训练数据分布无关——无论用 synthetic 还是 real bugs 训练，477-token output 的生成难度不变。\n   - **Counter 3 (conservative direction):** 如果 real bugs 比 synthetic mutations 更难（合理假设），那么 CWM 的 repo-level 退化只会更严重——我们的 synthetic 实验给出了 divergence 的 **下界**。\n\n6. **Acknowledging the gap。** 我们在 Limitations 中明确承认：\"the synthetic-to-real transfer gap for absolute accuracy remains untested.\" 这是诚实的 scope limitation，不削弱 relative ranking finding。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Andrews & Just citations | Limitations |\n| Coupling effect → relative ranking argument | Limitations, Appendix G |\n| SWE-bench Verified (real GitHub issues) | §4.1 |\n| HumanEval/MBPP mutation operators | §4.1, Appendix D |\n| 5 mutation types listed | Appendix D |\n| Gold parse rate 23.9% (worst among all types) | Appendix C, Table cwm_mutation_parse |\n| Gold parseable-only accuracy 16.5% | Appendix C |\n| Limitations acknowledgment | Limitations |\n\n---\n\n## 交叉防御：多个攻击面的组合回应\n\n如果 reviewer 同时提出多个攻击面，统一回应模板：\n\n> \"We appreciate the reviewer's thorough engagement with our experimental design. We address each concern below, and note a unifying theme: our contribution is primarily **methodological**—providing the first matched experimental framework for comparing verification formulations. The per-test interaction effect (z=−23.7, n=56,480) is statistically robust regardless of (1) model scale, since it isolates formulation effects at controlled capacity; (2) seed count, since it is based on >56K observations with 139 problem-level clusters, not variant-level aggregates; and (3) training data source, since the interaction concerns relative ordering across formulations that share the same training distribution.\"\n\n---\n\n## Q2 预备：Re-repair Negative + Oracle Ensemble\n\n### Reviewer 可能追问\n\n> \"The re-repair pilot found no benefit (p=0.42). Doesn't this undermine the practical value of per-test diagnostics, which is one of CLS's main advantages over TRAJ?\"\n\n### 回应要点\n\n1. **Statistical power 不足以检测 medium effect。** n=44 instances, power ≈ 0.3 for medium effect size (Cohen's h=0.3)。p=0.42 是 inconclusive, not evidence of absence。需要 n≈200 才能 power=0.8。\n\n2. **Oracle ensemble ceiling 证明 formulation diversity 有实际价值。** 即使 re-repair 未证明直接 downstream benefit：\n   - Function-level oracle ensemble: 90.63% (+2.80pp over best single)\n   - Repo-level oracle routing: 95.83% variant accuracy (+14.58pp over best single, n=48)\n   - 95.83% 意味着：如果有一个 perfect router，只需从已有 formulations 中选择，就可以 resolve 95.83% 的 variants\n   - 这是 \"formulation design space worth exploring\" 的最直接证据\n\n3. **Per-test diagnostics 的价值不仅限于 re-repair。** CLS 的 per-test granularity 还支持：\n   - Failure localization（哪些测试失败）\n   - Confidence estimation（多少测试通过 / 总测试数）\n   - Selective re-execution（只重跑可疑测试）\n   - 这些 downstream applications 未被 re-repair pilot 覆盖\n\n4. **诚实承认 limitation。** 论文已在 Limitations 中明确标注 re-repair negative + insufficient power。这是透明的科学报告，不是 weakness——reviewer 如果因此降分，可以在 rebuttal 中指出这恰恰是 rigorous self-assessment。\n\n---\n\n## 状态标注\n\n| 攻击面 | 当前防御强度 | 数据到齐后 |\n|--------|------------|----------|\n| #1 CWM scale | ★★★★ (4 convergent nulls + exec trace reframing + methodology argument) | ★★★★+ if 14B pilot confirms |\n| #2 Single seed | ★★★★ (per-test LPM overwhelming + MDE analysis + variant gap > MDE) | ★★★★+ with multi-seed CWM |\n| #3 Synthetic data | ★★★☆ (coupling effect + gold parse rate counter + 3 uniform-shift counters) | 不变（需要 real-bug training data 才能完全 close，超出 scope） |\n| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |\n",
    "structuredPatch": [
      {
        "oldStart": 81,
        "oldLines": 6,
        "newStart": 81,
        "newLines": 16,
        "lines": [
          " ",
          " > \"The repo-level results rely on a single seed for most comparisons. With n=48 variant-level instances, the 19–26pp gap could be an artifact of seed variance. The authors themselves note 'single-seed design and multiple confounds limit causal attribution.' Without multi-seed replication, these results are suggestive at best.\"",
          " ",
          "+### 补充统计数据（M027 修正后）",
          "+",
          "+| Metric | 修正前 | 修正后 | 备注 |",
          "+|--------|--------|--------|------|",
          "+| Cohen's d (CLS vs TRAJ, Qwen) | 5.015 | **4.590** | 仍为 very large (>0.8 threshold) |",
          "+| Statistical power (Qwen) | 0.940 | **0.914** | 仍 >0.80 sufficient threshold |",
          "+| Qwen CLS mean | 85.11 | **84.83** | — |",
          "+",
          "+修正原因：Qwen CLS s42 和 TRAJ s42 值与 D159 决策对齐。",
          "+",
          " ### 回应要点（当前版本：数据到齐前）",
          " ",
          " **核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**"
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01WjkbTkBydGSGLMcfUd4Z1R`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
  "old_string": "| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |",
  "new_string": "| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |\n\n---\n\n## 储备/待用\n\n以下素材已有数据支撑或数据部分就绪，reviewer 问到时可快速出图或展开论述。\n\n### Checkpoint Selection Sensitivity（储备，reviewer 问时出图）\n\n28 个 val/test checkpoint sweep 数据点已存在 registry，覆盖：\n- CLS 8B: ckpt-1000 到 ckpt-6400，多个 seq_length\n- CLS 4B: ckpt-800 到 ckpt-4600\n- 跨 checkpoint 的 accuracy 波动 <1pp（例：s42 三个 ckpt = 85.34/84.48/85.29）\n\nReviewer 如果质疑 checkpoint selection bias，可在 rebuttal 期间 <1h 画出 sensitivity 图。\n\n### CWM Epoch-wise Accuracy Curve（储备，等数据到齐后画）\n\n已有数据点：\n- s42: epoch 2 = 66.85% (partial coverage 31.2%), epoch 3 = 61.49%\n- s123-v2: epoch 1 = 75.45% (checkpoint-4209)\n- s456-v2: 训练中，epoch 2 eval_loss = 4.727\n\n完整 multi-seed epoch 曲线需要：\n- s123-v3 和 s456-v2 完成 3-epoch 训练后的 final accuracy\n- 各 seed 的 epoch 1/2 checkpoint eval（如果 checkpoint 保留了的话）\n\n用途：证明 CWM 在 repo-level 随训练推进而退化，支撑 \"CWM generation + long traces = fundamental mismatch\" 的论点。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "62261a70-7989-4254-932e-988d7d70cf39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwFen9DuA9Jq5r134so8i8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 519,
      "cache_read_input_tokens": 32121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 519
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

_source line 14 · 2026-05-21T08:43:37.229Z_

<details><summary>↩ Tool result · `toolu_01WjkbTkBydGSGLMcfUd4Z1R`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "12c4015b-41a7-46ce-b690-e60f550afc42",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
    "oldString": "| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |",
    "newString": "| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |\n\n---\n\n## 储备/待用\n\n以下素材已有数据支撑或数据部分就绪，reviewer 问到时可快速出图或展开论述。\n\n### Checkpoint Selection Sensitivity（储备，reviewer 问时出图）\n\n28 个 val/test checkpoint sweep 数据点已存在 registry，覆盖：\n- CLS 8B: ckpt-1000 到 ckpt-6400，多个 seq_length\n- CLS 4B: ckpt-800 到 ckpt-4600\n- 跨 checkpoint 的 accuracy 波动 <1pp（例：s42 三个 ckpt = 85.34/84.48/85.29）\n\nReviewer 如果质疑 checkpoint selection bias，可在 rebuttal 期间 <1h 画出 sensitivity 图。\n\n### CWM Epoch-wise Accuracy Curve（储备，等数据到齐后画）\n\n已有数据点：\n- s42: epoch 2 = 66.85% (partial coverage 31.2%), epoch 3 = 61.49%\n- s123-v2: epoch 1 = 75.45% (checkpoint-4209)\n- s456-v2: 训练中，epoch 2 eval_loss = 4.727\n\n完整 multi-seed epoch 曲线需要：\n- s123-v3 和 s456-v2 完成 3-epoch 训练后的 final accuracy\n- 各 seed 的 epoch 1/2 checkpoint eval（如果 checkpoint 保留了的话）\n\n用途：证明 CWM 在 repo-level 随训练推进而退化，支撑 \"CWM generation + long traces = fundamental mismatch\" 的论点。",
    "originalFile": "# Rebuttal Framework — Pre-Submission Attack Surface Analysis\n\nDate: 2026-05-20 | Venue: EMNLP 2026 ARR\n\n---\n\n## Attack #1: CWM ≤8B LoRA ≠ Real 32B CWM\n\n### Reviewer 可能措辞\n\n> \"The CWM baseline is a ≤8B LoRA fine-tuned model, not the original 32B Code World Model with execution trace mid-training. The comparison is unfair—CWM was designed to operate at much larger scale with specialized pretraining. The paper's conclusion that 'generation degrades at repo level' may simply reflect insufficient model capacity rather than a fundamental formulation limitation.\"\n\n### 回应要点\n\n**核心论点：matched comparison at controlled capacity isolates formulation effect from scale confounds, which is complementary to—not competing with—scaling studies.**\n\n1. **Function-level 证明 LoRA 可以成功适配 CWM formulation。** CLS 和 CWM 在 function-level 达到统计等价（TOST p=0.007, 5 seeds, ±2pp margin），证明同一 LoRA 配置下 CWM formulation 能完全发挥作用。退化仅在 repo-level 出现，不是 LoRA 容量不足的全局问题。\n\n2. **退化模式指向 formulation 本身，而非容量瓶颈——四种标准干预全部失败。**\n   - Format collapse (53–74% unparseable outputs) 是输出空间复杂度问题：function-level 输出为短字符串（integers, booleans），repo-level 输出为无约束执行轨迹（均值 ~477 tokens），错误呈乘性积累\n   - 即使在可解析输出中，accuracy (38–43%) 仍低于 majority baseline (72.96%)，表明存在超越格式合规的语义鸿沟\n   - **LoRA rank-32 ablation（双倍参数）：无改善（−0.51pp）**，排除 adapter 容量瓶颈\n   - **Majority voting K=3：accuracy 反降 0.68pp**（87.51→86.83%），93.3% 样本三次一致，errors 是系统性偏差非随机噪声\n   - **Relaxed matching（放宽格式要求）：accuracy 反降 1.06pp**（58.04→56.98%），因为 unparseable 默认为 majority class 比模型自身预测更准\n   - **Model scaling 4B→8B：parseable-only accuracy 反降**（42.88→38.52%），表面 accuracy 提升完全是 default-assignment artifact\n   - Matched-context ablation：输入差异仅解释 <3% 的 gap\n   \n   **每种干预分别靶向不同的替代解释（容量不足 / 随机噪声 / 解析严格 / 模型规模），全部失败。这构成 formulation-level bottleneck 的最强证据链。**\n\n   **Convergent null results summary (rebuttal 可直接引用):**\n   > \"Four convergent null results strengthen this argument: (1) doubling model size yields +0.16pp (flat); (2) majority voting K=3 decreases accuracy by 0.69pp, confirming errors are systematic; (3) forced parsing rescues 90.6% of unparseable outputs but accuracy remains below majority baseline (49.4% vs 72.96%); (4) at repo level, scaling from 4B to 8B worsens parseable-only accuracy (42.88→38.52%) while increasing format collapse (54→74%). These collectively rule out adapter capacity, model capacity, inference stochasticity, and format compliance as explanations, localizing the bottleneck to the generation formulation's output space complexity.\"\n\n3. **我们的贡献是 formulation comparison methodology，不是 CWM SOTA。** 本文的价值在于提供首个 matched experimental framework 来隔离 formulation effects。32B CWM 在更大规模上可能表现不同（我们在 Limitations 中明确承认），但 matched comparison 是理解 formulation dynamics 的必要第一步。\n\n4. **CLS 过拟合鲁棒性（formulation-level 差异）。** CLS 和 CWM 在相同训练配置下表现出截然不同的过拟合行为：\n   - CLS: eval_loss 涨 123%，但 accuracy 仅下降 0.1pp → classification formulation 对过拟合天然鲁棒\n   - CWM: eval_loss 上升后 accuracy 下降 5.36pp (epoch 2→3) → generation formulation 更敏感\n   - 即使 oracle early stopping (epoch 1 = 75.45%)，CWM 仍 ~7pp below CLS 且 66% unparseable\n   - 结论：这是 formulation-level 的固有差异，不是 training-level 的超参问题\n\n   数据来源：\n   - CLS: registry cls8b-s42 系列\n   - CWM epoch 2→3: deepseek-cwm-repo-s42 (66.85% → 61.49%, -5.36pp)\n   - CWM epoch 1: deepseek-cwm-repo-s123-eval-1epoch (75.45%, unparseable 66.4%)\n\n5. **预备回应：\"execution trace mid-training 可能改变结果\"**\n\n   如果 reviewer 追问 \"execution trace pretraining is an integral part of CWM, without it your comparison is incomplete\"：\n\n   > \"Function-level equivalence demonstrates LoRA successfully adapts both formulations (TOST p=0.007). The degradation is complexity-conditional, not LoRA-global. Execution trace mid-training may improve CWM's long-output generation capacity, but this represents an orthogonal training paradigm—not a formulation change. Our contribution is isolating the formulation dimension; scaling and pretraining dimensions require separate matched studies.\"\n\n   此论点将 execution trace pretraining 重新定位为 **training paradigm** 而非 **formulation property**——reviewer 如果坚持这是 formulation 的一部分，则需要论证为什么 CLS 和 TRAJ 不需要类似 pretraining 来\"公平比较\"。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| TOST equivalence at function-level | §4.2, Table 1 |\n| Format collapse rates 53–74% | §4.3, Table 4 |\n| Parseable-only accuracy 38–43% < majority 72.96% | §4.3, Appendix C |\n| Rank-32 ablation −0.51pp | Appendix B |\n| Majority voting K=3 −0.68pp | Appendix (g) |\n| Relaxed matching −1.06pp | Appendix (c) |\n| Model scaling 4B→8B parseable acc ↓ | §4.3 |\n| Matched-context ablation <3% | Appendix B |\n| Output token ratio 1:477 (CLS:CWM) | §4.4 |\n| Four failed interventions summary | §4.4, Appendix (g) |\n| Limitation acknowledged | Limitations, §4.5 |\n\n### 如果 CWM multi-seed + 14B pilot 数据到齐（增补版）\n\n> \"We additionally provide multi-seed CWM results (N seeds) confirming the single-seed findings: [具体数据]. A 14B pilot [如果跑了] shows [结果], suggesting that [scaling 趋势].\"\n\n此段可在 camera-ready 或 rebuttal 中按实际数据填入。\n\n---\n\n## Attack #2: Repo-Level 单 Seed → 统计力不足\n\n### Reviewer 可能措辞\n\n> \"The repo-level results rely on a single seed for most comparisons. With n=48 variant-level instances, the 19–26pp gap could be an artifact of seed variance. The authors themselves note 'single-seed design and multiple confounds limit causal attribution.' Without multi-seed replication, these results are suggestive at best.\"\n\n### 补充统计数据（M027 修正后）\n\n| Metric | 修正前 | 修正后 | 备注 |\n|--------|--------|--------|------|\n| Cohen's d (CLS vs TRAJ, Qwen) | 5.015 | **4.590** | 仍为 very large (>0.8 threshold) |\n| Statistical power (Qwen) | 0.940 | **0.914** | 仍 >0.80 sufficient threshold |\n| Qwen CLS mean | 85.11 | **84.83** | — |\n\n修正原因：Qwen CLS s42 和 TRAJ s42 值与 D159 决策对齐。\n\n### 回应要点（当前版本：数据到齐前）\n\n**核心论点：variant-level 是单 seed，但 per-test interaction effect 基于 n=56,480 observations 且统计上不可争议。**\n\n1. **区分两层证据。** Formulation×complexity interaction 在 per-test level 已经 statistically confirmed：\n   - Cross-complexity LPM：z=−23.7, p<0.001, n=56,480, 139 problem clusters (DeepSeek-Coder)\n   - Cross-model LPM：CWM deficit −22pp, z=−64.4, p<0.001\n   - Formulation 解释 >95% of predictable variance\n   - 这不是 \"suggestive evidence\"，而是 overwhelming statistical evidence for the interaction\n\n2. **Cross-model 方向一致性。** Qwen3 和 DeepSeek-Coder 两个架构不同的模型家族展现相同方向（CLS > CWM），model identity 仅调节 gap magnitude (+1.6pp interaction, z=2.8) 而不改变方向。\n\n3. **Gap magnitude 超过所有已评估 confounds。** §4.5 逐一评估 5 个潜在混淆因素，19–26pp gap 超过任何单个 confound（checkpoint <1pp, seq_length ~1.5pp, preprocessing ~8pp cross-config variance）。即使 confounds 相关，gap 的量级提供 substantial margin。\n\n4. **Holm-Bonferroni 控制 FWER。** 两个核心 claim 在校正后仍然 significant（adjusted p=0.012 and p=0.021）。\n\n5. **Variant-level power 分析。** 即使在 variant-level (n=48)，MDE (minimum detectable effect) ≈ 25pp（two-sided, α=0.05, power=0.8, McNemar's test）。观测到的 CLS–CWM gap 为 29–35pp（视配置），超过 MDE。也就是说：即使在 n=48 的严苛条件下，观测 gap 仍足够大以被统计检测到。这不是 underpowered——是 gap 太大了。\n\n### 回应要点（增补版：CWM multi-seed 数据到齐后）\n\n> \"We have completed multi-seed CWM replication. The [N]-seed mean CWM accuracy is [X]% ± [Y]%, confirming the single-seed finding. The CLS–CWM gap at repo level is [Z]pp (p=[value], [N] seeds), consistent with the per-test interaction effect (z=−23.7). This addresses the reviewer's concern about seed-specific artifacts.\"\n\n如果 multi-seed 方差大于预期：\n> \"The multi-seed variance is [较大], but the gap remains directionally consistent across all seeds. The per-test interaction (z=−23.7, n=56,480) remains the primary evidence for complexity-dependent divergence; variant-level accuracy provides a practical summary statistic.\"\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Per-test LPM z=−23.7, n=56,480 | §4.3 |\n| Cross-model z=−64.4 | §4.3 |\n| Formulation explains >95% variance | §4.3 |\n| 5 confounds assessed | §4.5, Appendix F |\n| Holm-Bonferroni adjusted p | §4.5, Table 5 |\n| Cross-model consistency | §4.3 |\n\n---\n\n## Attack #3: 合成突变 vs 真实 Bug\n\n### Reviewer 可能措辞\n\n> \"The training data is synthetically generated via mutation operators, not real developer bugs. SWE-bench uses real GitHub issues, but the training-side synthetic distribution may not transfer. The paper's findings about formulation divergence could be an artifact of the synthetic data distribution rather than a genuine property of the verification task.\"\n\n### 回应要点\n\n**核心论点：our core finding concerns relative ordering, not absolute accuracy—relative rankings are expected to be preserved under uniform distributional shifts.**\n\n1. **Mutation testing 文献的 established validity。** Andrews et al. (2005) 和 Just et al. (2014) 建立了 mutants 作为真实 faults 的 reasonable proxies 在 test effectiveness 研究中的有效性。我们的 mutation operators (operator_swap, off_by_one, return_value, boundary_removal) 覆盖 PMT 文献中的标准突变类型。\n\n2. **Coupling effect 支持 relative ranking validity。** Mutation testing 的 coupling effect 表明：能检测简单突变的 verifier 也倾向于检测复杂真实 bug。这意味着：\n   - Domain shift 从 synthetic mutations 到 real bugs 可能影响 absolute accuracy levels\n   - 但 relative performance ordering（即 \"formulation choice matters at repo level but not function level\"）预期在均匀 distributional shift 下保持不变\n   - 除非某个 formulation 对 synthetic mutations 有 specific bias（没有理论或实证根据）\n\n3. **Evaluation-side 已包含真实数据。** Repo-level evaluation 使用 SWE-bench Verified（来自真实 GitHub issues 和 pull requests），不是 synthetic data。Function-level 使用 HumanEval/MBPP mutants，但 function-level 结果（near-equivalence）恰恰是我们的 positive finding——即使这受 synthetic bias 影响，也只会低估 formulation difference（如果真实 bugs 更难，divergence 可能更大）。\n\n4. **Gold parse rate 反直觉证据。** Gold mutations（未修改代码，所有测试通过）是 CWM 最简单的目标——模型只需生成\"全部通过\"的输出。但 gold 的 parse rate 在 8B 仅 23.9%（最差），parseable-only accuracy 仅 16.5%。这直接反驳 \"failure comes from mutation difficulty\" 的解释：最简单的任务反而最差，说明失败源于输出空间复杂度本身，而非 mutation-specific 难度。\n\n5. **回应 \"uniform shift\" 质疑的 3 条 counter：**\n   - **Counter 1 (directionality):** 如果 synthetic bias 导致了 formulation divergence，我们预期 bias 在 function-level 和 repo-level 一致。但 function-level 观察到 equivalence，repo-level 观察到 divergence。一个 uniform bias 无法同时解释 equivalence 和 divergence。\n   - **Counter 2 (mechanism):** CWM 退化的直接机制是 format collapse (53–74% unparseable) 和 long-output generation failure (mean ~477 tokens)。这些是模型能力的物理限制，与训练数据分布无关——无论用 synthetic 还是 real bugs 训练，477-token output 的生成难度不变。\n   - **Counter 3 (conservative direction):** 如果 real bugs 比 synthetic mutations 更难（合理假设），那么 CWM 的 repo-level 退化只会更严重——我们的 synthetic 实验给出了 divergence 的 **下界**。\n\n6. **Acknowledging the gap。** 我们在 Limitations 中明确承认：\"the synthetic-to-real transfer gap for absolute accuracy remains untested.\" 这是诚实的 scope limitation，不削弱 relative ranking finding。\n\n### 支撑证据\n\n| Evidence | Location |\n|----------|----------|\n| Andrews & Just citations | Limitations |\n| Coupling effect → relative ranking argument | Limitations, Appendix G |\n| SWE-bench Verified (real GitHub issues) | §4.1 |\n| HumanEval/MBPP mutation operators | §4.1, Appendix D |\n| 5 mutation types listed | Appendix D |\n| Gold parse rate 23.9% (worst among all types) | Appendix C, Table cwm_mutation_parse |\n| Gold parseable-only accuracy 16.5% | Appendix C |\n| Limitations acknowledgment | Limitations |\n\n---\n\n## 交叉防御：多个攻击面的组合回应\n\n如果 reviewer 同时提出多个攻击面，统一回应模板：\n\n> \"We appreciate the reviewer's thorough engagement with our experimental design. We address each concern below, and note a unifying theme: our contribution is primarily **methodological**—providing the first matched experimental framework for comparing verification formulations. The per-test interaction effect (z=−23.7, n=56,480) is statistically robust regardless of (1) model scale, since it isolates formulation effects at controlled capacity; (2) seed count, since it is based on >56K observations with 139 problem-level clusters, not variant-level aggregates; and (3) training data source, since the interaction concerns relative ordering across formulations that share the same training distribution.\"\n\n---\n\n## Q2 预备：Re-repair Negative + Oracle Ensemble\n\n### Reviewer 可能追问\n\n> \"The re-repair pilot found no benefit (p=0.42). Doesn't this undermine the practical value of per-test diagnostics, which is one of CLS's main advantages over TRAJ?\"\n\n### 回应要点\n\n1. **Statistical power 不足以检测 medium effect。** n=44 instances, power ≈ 0.3 for medium effect size (Cohen's h=0.3)。p=0.42 是 inconclusive, not evidence of absence。需要 n≈200 才能 power=0.8。\n\n2. **Oracle ensemble ceiling 证明 formulation diversity 有实际价值。** 即使 re-repair 未证明直接 downstream benefit：\n   - Function-level oracle ensemble: 90.63% (+2.80pp over best single)\n   - Repo-level oracle routing: 95.83% variant accuracy (+14.58pp over best single, n=48)\n   - 95.83% 意味着：如果有一个 perfect router，只需从已有 formulations 中选择，就可以 resolve 95.83% 的 variants\n   - 这是 \"formulation design space worth exploring\" 的最直接证据\n\n3. **Per-test diagnostics 的价值不仅限于 re-repair。** CLS 的 per-test granularity 还支持：\n   - Failure localization（哪些测试失败）\n   - Confidence estimation（多少测试通过 / 总测试数）\n   - Selective re-execution（只重跑可疑测试）\n   - 这些 downstream applications 未被 re-repair pilot 覆盖\n\n4. **诚实承认 limitation。** 论文已在 Limitations 中明确标注 re-repair negative + insufficient power。这是透明的科学报告，不是 weakness——reviewer 如果因此降分，可以在 rebuttal 中指出这恰恰是 rigorous self-assessment。\n\n---\n\n## 状态标注\n\n| 攻击面 | 当前防御强度 | 数据到齐后 |\n|--------|------------|----------|\n| #1 CWM scale | ★★★★ (4 convergent nulls + exec trace reframing + methodology argument) | ★★★★+ if 14B pilot confirms |\n| #2 Single seed | ★★★★ (per-test LPM overwhelming + MDE analysis + variant gap > MDE) | ★★★★+ with multi-seed CWM |\n| #3 Synthetic data | ★★★☆ (coupling effect + gold parse rate counter + 3 uniform-shift counters) | 不变（需要 real-bug training data 才能完全 close，超出 scope） |\n| Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |\n",
    "structuredPatch": [
      {
        "oldStart": 214,
        "oldLines": 3,
        "newStart": 214,
        "newLines": 31,
        "lines": [
          " | #2 Single seed | ★★★★ (per-test LPM overwhelming + MDE analysis + variant gap > MDE) | ★★★★+ with multi-seed CWM |",
          " | #3 Synthetic data | ★★★☆ (coupling effect + gold parse rate counter + 3 uniform-shift counters) | 不变（需要 real-bug training data 才能完全 close，超出 scope） |",
          " | Q2 Re-repair | ★★★☆ (power analysis + oracle ceiling + broader diagnostic utility) | 需要 n≈200 re-repair 才能 close |",
          "+",
          "+---",
          "+",
          "+## 储备/待用",
          "+",
          "+以下素材已有数据支撑或数据部分就绪，reviewer 问到时可快速出图或展开论述。",
          "+",
          "+### Checkpoint Selection Sensitivity（储备，reviewer 问时出图）",
          "+",
          "+28 个 val/test checkpoint sweep 数据点已存在 registry，覆盖：",
          "+- CLS 8B: ckpt-1000 到 ckpt-6400，多个 seq_length",
          "+- CLS 4B: ckpt-800 到 ckpt-4600",
          "+- 跨 checkpoint 的 accuracy 波动 <1pp（例：s42 三个 ckpt = 85.34/84.48/85.29）",
          "+",
          "+Reviewer 如果质疑 checkpoint selection bias，可在 rebuttal 期间 <1h 画出 sensitivity 图。",
          "+",
          "+### CWM Epoch-wise Accuracy Curve（储备，等数据到齐后画）",
          "+",
          "+已有数据点：",
          "+- s42: epoch 2 = 66.85% (partial coverage 31.2%), epoch 3 = 61.49%",
          "+- s123-v2: epoch 1 = 75.45% (checkpoint-4209)",
          "+- s456-v2: 训练中，epoch 2 eval_loss = 4.727",
          "+",
          "+完整 multi-seed epoch 曲线需要：",
          "+- s123-v3 和 s456-v2 完成 3-epoch 训练后的 final accuracy",
          "+- 各 seed 的 epoch 1/2 checkpoint eval（如果 checkpoint 保留了的话）",
          "+",
          "+用途：证明 CWM 在 repo-level 随训练推进而退化，支撑 \"CWM generation + long traces = fundamental mismatch\" 的论点。"
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

### Assistant

_source line 15_

Now register the updated artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "b91afb66-2e83-466c-a344-f4901d8d4c10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175bKGEqMJq14HPeY5aZ2T5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 32640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XrEcX1FkgMjT1ZoBLFBbBw`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "3ee8b06d-9acf-4adf-a6ed-2ad0bf0b4f24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175bKGEqMJq14HPeY5aZ2T5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 32640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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

_source line 17 · 2026-05-21T08:43:40.377Z_

<details><summary>↩ Tool result · `toolu_01XrEcX1FkgMjT1ZoBLFBbBw`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "ed11b617-9458-490d-a806-efe4f54ccc52",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_018aWysadzaVw7fiorEG26ak`</summary>

```json
{
  "name": "rebuttal_framework",
  "type": "report",
  "description": "Rebuttal framework updated: added CLS overfitting robustness defense (Attack #1), M027-corrected statistics (Attack #2), checkpoint sensitivity and CWM epoch curve reserves",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/rebuttal_framework.md",
  "tags": [
    "rebuttal",
    "emnlp2026",
    "defense"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "c3741a31-7aa0-4e58-8e97-677f5cb770b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5oVQ4NvynG7qr5HoLZVP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 33394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 62,
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

_source line 19 · 2026-05-21T08:43:48.761Z_

<details><summary>↩ Tool result · `toolu_018aWysadzaVw7fiorEG26ak`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_38318e\", \"name\": \"rebuttal_framework\", \"type\": \"report\", \"description\": \"Rebuttal framework updated: added CLS overfitting robustness defense (Attack #1), M027-corrected statistics (Attack #2), checkpoint sensitivity and CWM epoch curve reserves\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/rebuttal_framework.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T08:43:48.453659+00:00\", \"tags\": [\"rebuttal\", \"emnlp2026\", \"defense\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "a82602a4-f0af-496a-abc5-e7a75de369be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_38318e\\\", \\\"name\\\": \\\"rebuttal_framework\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Rebuttal framework updated: added CLS overfitting robustness defense (Attack #1), M027-corrected statistics (Attack #2), checkpoint sensitivity and CWM epoch curve reserves\\\", \\\"path\\\": \\\"projects/exec-sim-repair-verifier/artifacts/_project/report/rebuttal_framework.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"exec-sim-repair-verifier\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T08:43:48.453659+00:00\\\", \\\"tags\\\": [\\\"rebuttal\\\", \\\"emnlp2026\\\", \\\"defense\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_38318e\", \"name\": \"rebuttal_framework\", \"type\": \"report\", \"description\": \"Rebuttal framework updated: added CLS overfitting robustness defense (Attack #1), M027-corrected statistics (Attack #2), checkpoint sensitivity and CWM epoch curve reserves\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/rebuttal_framework.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T08:43:48.453659+00:00\", \"tags\": [\"rebuttal\", \"emnlp2026\", \"defense\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

已完成 4 项更新：

1. **Attack #1 新增第 4 点**：CLS 过拟合鲁棒性防线，含 CLS/CWM 过拟合行为对比和数据来源，原第 4 点（execution trace 预备回应）顺延为第 5 点
2. **Attack #2 新增统计表**：M027 修正后的 Cohen's d (4.590)、power (0.914)、Qwen CLS mean (84.83)，插入在回应要点之前
3. **新建「储备/待用」分区**：Checkpoint Selection Sensitivity（28 个 sweep 数据点，<1pp 波动）
4. **储备分区第二条**：CWM Epoch-wise Accuracy Curve（已有 3 个 seed 部分数据点，待数据到齐画图）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "uuid": "b505ed3e-e44d-4d38-9cc7-3c3ad1c87032",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFRPqs7YD465hJC6DWSeSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 34113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 550
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

### Task result

_source line 21_

已完成 4 项更新：

1. **Attack #1 新增第 4 点**：CLS 过拟合鲁棒性防线，含 CLS/CWM 过拟合行为对比和数据来源，原第 4 点（execution trace 预备回应）顺延为第 5 点
2. **Attack #2 新增统计表**：M027 修正后的 Cohen's d (4.590)、power (0.914)、Qwen CLS mean (84.83)，插入在回应要点之前
3. **新建「储备/待用」分区**：Checkpoint Selection Sensitivity（28 个 sweep 数据点，<1pp 波动）
4. **储备分区第二条**：CWM Epoch-wise Accuracy Curve（已有 3 个 seed 部分数据点，待数据到齐画图）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 84971,
  "duration_api_ms": 85626,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "7bf2e05f-f8b9-4cb8-bb3f-094f4ac6d436",
  "total_cost_usd": 0.32042699999999996,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 22962,
    "cache_read_input_tokens": 200207,
    "output_tokens": 2990,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22962,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 242,
        "cache_read_input_tokens": 34113,
        "cache_creation_input_tokens": 550,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 550
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1916,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002006,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 2990,
      "cacheReadInputTokens": 200207,
      "cacheCreationInputTokens": 22962,
      "webSearchRequests": 0,
      "costUSD": 0.31842099999999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "36a77621-f789-4c69-95f4-a723603b9c7b"
}
```

</details>

---
