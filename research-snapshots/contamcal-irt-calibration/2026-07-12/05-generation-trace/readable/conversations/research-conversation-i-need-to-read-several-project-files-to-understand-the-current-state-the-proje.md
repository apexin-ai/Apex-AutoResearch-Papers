# Research conversation: I need to read several project files to understand the current state. The project is "contamcal-irt-calibration". Look f

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7ae2a5850e7251d8.jsonl`
- **Structured JSON:** [`b6ae19d882ecebcf289b.json`](../../sessions/b6/b6ae19d882ecebcf289b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-14T16:06:00.963Z_

I need to read several project files to understand the current state. The project is "contamcal-irt-calibration". Look for these files and read their contents:

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md

Read as much of each file as possible. Report back the full contents of each file found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "9f55621b-0ac1-4ada-8ba8-2dcb39e13c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T16:06:02.825Z_

I'll read all the specified project files for you. Let me fetch them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f55621b-0ac1-4ada-8ba8-2dcb39e13c06",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJWKqRjeEddUckgnFX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "65c2226e-46c6-4968-8295-96b25fab6603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ps7UnaARJz7csVNjNubjFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34685,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 3 · 2026-05-14T16:06:03.058Z_

<details open><summary>🔧 Tool call — Read · `toolu_014rQfh63tN2eumbQ66PwuS6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65c2226e-46c6-4968-8295-96b25fab6603",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJWKqRjeEddUckgnFX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5075bcc6-8d6e-4920-9753-dbd47482594a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ps7UnaARJz7csVNjNubjFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34685,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T16:06:03.187Z_

<details><summary>↩ Tool result · `toolu_014rQfh63tN2eumbQ66PwuS6`</summary>

```text
1	# Handover — 2026-05-14
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| exp_005_noise_prop_v3 | Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume. | — | — | — |
9	| exp_001_sft_d025_15B | 25% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-dosage contamination for 1.5B dose-response curve intermediate point | — | — | — |
10	| exp_001_eval_3B_d005_aligned | — | — | — | — |
11	
12	## 待处理
13	- exp_001_eval_05B_d100_aligned_v3: 0.5B d100 s42 aligned-format eval (v3 fix: conda activation). d100 original + paraphrase MC eval with "The answer is" prefix (D017).（已分配 ? GPU:?，等待提交）
14	- exp_001_eval_05B_d005_para_aligned（准备中）
15	- exp_001_eval_05B_d100_aligned_v4（准备中）
16	- exp_001_eval_05B_d100_aligned_v2（准备中）
17	- exp_001_eval_3B_d000_s42_v3: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。（准备中）
18	- exp_001_eval_05B_d000_s42_v6: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)（准备中）
19	- exp_001_eval_05B_d100_v6: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)（准备中）
20	- exp_001_eval_05B_d100_v4: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)（准备中）
21	- exp_001_eval_05B_d000_s42_v4: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)（准备中）
22	- exp_001_eval_05B_d000_s42_v2（准备中）
23	- …另有 4 项
24	
25	## 近期结论
26	- **exp_001_eval_05B_d025_aligned** (failed): 0.5B d025 s42 aligned eval — 25% contamination dose-response intermediate point (original + paraphrase)
27	- **exp_001_eval_3B_d100_aligned** (success): 3B d100 s42 aligned eval — 100% contamination at largest scale, upper bound for 3B dose-response (MMLU/ARC only, GSM8K excluded per D018) ← 基于 exp_001_sft_d100_3B
28	- **exp_001_eval_05B_d005_aligned** (success): —
29	
30	## 趋势
31	成功 33 / 负向 0 / 失败 15 / 共 50
32	
33	## 下一步
34	（无活跃 idea，请通过 ideas.md 添加）
35	
36	## 资源状态
37	cqa1-21977: 无 GPU 信息
38	
39	## 告警
40	- exp_001_eval_05B_d000_s42: 训练失败 — unknown
41	- exp_001_eval_05B_d100: 训练失败 — unknown
42	- exp_001_eval_05B_d100_v2: 训练失败 — unknown
43	- exp_001_eval_15B_d000_s42: 训练失败 — unknown
44	- exp_001_sft_100pct_05B: 训练失败 — unknown
45	- exp_001_sft_d005_05B: 已被终止 — unknown
46	- exp_001_sft_d005_05B_v2: 训练失败 — unknown
47	- exp_001_sft_d100_15B: 训练失败 — unknown
48	- exp_004_sim_sweep: 训练失败 — unknown
49	- exp_005_noise_prop: 训练失败 — unknown
50	- exp_005_noise_prop_v2: 训练失败 — unknown
51	- exp_001_sft_d025_05B: 训练失败 — unknown
52	- exp_001_sft_d025_05B_v2: 训练失败 — unknown
53	- exp_001_eval_05B_aligned_batch: 训练失败 — unknown
54	- exp_001_eval_05B_d025_aligned: 训练失败 — unknown
55	- exp_006_irt_05B: 已被终止 — unknown
56	- exp_001_eval_05B_d100_aligned: 训练失败 — unknown
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5075bcc6-8d6e-4920-9753-dbd47482594a",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "f944fbf7-e38c-4644-9339-b3688683b97e",
  "sourceToolAssistantUUID": "5075bcc6-8d6e-4920-9753-dbd47482594a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T16:06:03.293Z_

<details open><summary>🔧 Tool call — Read · `toolu_0195qP5p9HfYHqQhyK5QHdp8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f944fbf7-e38c-4644-9339-b3688683b97e",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJWKqRjeEddUckgnFX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2bb5ea72-4401-4f0c-88a9-3505b7534409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ps7UnaARJz7csVNjNubjFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34685,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T16:06:03.384Z_

<details><summary>↩ Tool result · `toolu_0195qP5p9HfYHqQhyK5QHdp8`</summary>

````text
1	# contamcal-irt-calibration — Research Dashboard
2	
3	> 最后更新: 2026-05-14 03:39 UTC | 更新原因: Phase 3 SFT 进度同步、exp-002/006 管线加速、d025 0.5B 恢复优先级、exp-008 近期任务追踪
4	
5	## 核心方向
6	ContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。
7	
8	## 投稿目标
9	**EMNLP 2026 ARR May 25**（D006, 距今 11 天）
10	- Track: ML for NLP / Resources and Evaluation
11	- Special theme: "New Missions for NLP Research" — contamination/data governance
12	
13	## 当前进展
14	- **阶段**: Research（MVP 2026-05-13 通过）+ 审稿进行中
15	- **Phase 1 Paraphrase**: ✅ 全部完成 (ARC ✅, GSM8K ✅, MMLU ✅ v3, HumanEval ✅ appendix-only D009)
16	- **Phase 2 数据准备**: ✅ dosage 文件已生成 (ARC + GSM8K + MMLU)
17	- **Phase 3 SFT 进度 (seed=42)**:
18	
19	| 模型 | d000 | d005 | d025 | d050 | d100 |
20	|------|------|------|------|------|------|
21	| 0.5B | ✅ | ✅ | P2 | DP | ✅ |
22	| 1.5B | ✅ | 🏃GPU4 | P4 | DP | 🏃GPU0 |
23	| 3B | ✅ | P2 | P4 | DP | P1→GPU0释放后 |
24	
25	  ✅=完成 🏃=运行中 DP=deprioritized(d050) P=待排优先级
26	  seed=123 baselines: 0.5B ✅, 1.5B ✅, 3B ✅ (all d000)
27	
28	- **Phase 4 Eval**: 2 完成, 7 运行中
29	  - 完成: 0.5B-d000-s123 (MMLU 0.4182, GSM8K 0.3404, ARC 0.3976, HumanEval 0.1037), 1.5B-d000-s42 (MMLU 0.5753, GSM8K 0.6368, ARC 0.7756, HumanEval 0.128)
30	  - 运行中: GPU 1/2/3/5 各跑 eval
31	- **代码准备** (CPU Workers 并行):
32	  - exp-002 signal pipeline 代码: 编写中（4 signals + dry-run）
33	  - exp-006 baselines 代码: 编写中（7 baselines + 统一接口）
34	- **CPU 实验**:
35	  - exp-004 sim sweep: 27/120 完成, PID 340553, ETA ~40-60h (~May 16-17)
36	  - exp-005 noise prop v3: PID 339838 运行中, ETA ~11-12h (~14:30-15:30 UTC today)
37	- **Fisher 推导**: ✅ appendix.tex (Theorem 1 + 2 Corollaries)
38	- **论文**: Intro/Method/Related Work/Experiments 初稿已有
39	- **Stan**: D013 确认 Simple IRT model, ME model 弃用。contam_irt_4pl_simple.stan 收敛良好。
40	
41	## Critical Path
42	```
43	exp-002 代码完成 (CPU Worker, hours)
44	  → 0.5B eval 完成 → exp-002 signals on 0.5B {d000, d005, d100} (1-2 GPU-h)
45	    → exp-003 RRF aggregation (CPU, fast)
46	      → exp-006 IRT calibration + 7 baselines (core result!)
47	        → Paper results compilation
48	        
49	并行: 0.5B d025 SFT + eval (P2, 2-3 GPU-h, 补齐 dose-response 4 点曲线)
50	并行: 大模型 SFT 继续 (1.5B/3B d005/d100 → d025)
51	并行: exp-004 sim sweep (CPU, May 16-17)
52	并行: exp-005 v3 noise prop (CPU, today)
53	并行: exp-008 signal survival (P0, 等 exp-002 完成)
54	```
55	
56	**瓶颈**: 软件依赖（exp-002 + exp-006 代码编写）而非算力。
57	
58	## 近期任务
59	- [x] 修复 exp-004 Stan timeout → 断点续跑, PID 更新 340553
60	- [x] 确认 Simple IRT stan 不受 ME model 影响 (D013)
61	- [x] exp_005_v3 registry 误标 DONE → 回滚 RUNNING (Reviewer critical)
62	- [x] 写入防复发规范: server:local 实验不走 ssh 查进程
63	- [ ] **exp-002 signal pipeline 代码完成 + dry-run** ← 当前最高优先级
64	- [ ] **exp-006 baselines 代码完成** (7 baselines, 统一接口)
65	- [ ] 0.5B eval 完成 → exp-002 signals on {d000, d005, d100}
66	- [ ] **0.5B d025 SFT + eval** (P2, dose-response 4 点曲线)
67	- [ ] exp-003 RRF → exp-006 IRT (0.5B first pass, 管线验证)
68	- [ ] **exp-008 signal survival analysis (P0, C2 Core Contribution)** → 依赖 exp-002
69	- [ ] 大模型 SFT: 3B d100(P1) → 3B d005(P2) → d025(P4)
70	- [ ] exp-004 增量分析（每 AUC 条件完成后即时分析）
71	- [ ] exp-005 v3 完成 → 验证 noise propagation 结果
72	
73	⚠️ **Table 2 风险**: Related Work 表中 ContamCal "RL-robust partial✓" claim 唯一证据来源是 exp-008，尚未启动。若结果不支持需删除该 claim。
74	
75	## GPU 预算
76	- 服务器：cqa1-21977，6× RTX 4090D (cuda:0-5) 全部分配给本项目
77	- P0: 90h | P1: 60h | P2: 20h | Buffer: 30h
78	- 可用算力: ~1584 GPU-h (6卡×11天), 总预算 ~200h, 算力充裕
79	- 当前 GPU 6/6 全满
80	
81	## 关键决策日志
82	
83	| ID | 日期 | 摘要 | 关联实验 |
84	|----|------|------|----------|
85	| D019 | 2026-05-14 | d005 position bias confound: contamination SFT 将 " | exp_001_eval_05B_aligned_batch, exp_001_sft_d005_05B_v3 |
86	| D018 | 2026-05-14 | 3B GSM8K 崩塌归因为 LoRA SFT CoT 遗忘，排除出 dose-response 分 | exp_001_eval_3B_d000_s42, exp_001_eval_3B_raw_gen |
87	| D017 | 2026-05-14 | MC 评估改用 "The answer is" 前缀（方案 C），不重训模型 | exp_001_eval_05B_d005, exp_001_eval_05B_d000_s42_v5 |
88	| D016 | 2026-05-14 | Min-K++ 参考模型使用 0% dosage fine-tuned model（非裸基座），隔离 | exp_002_signal_pipeline |
89	| D015 | 2026-05-14 | C2 "cliff-like" claim 需条件限定：无 RL 中间 checkpoint 时降级 | exp-008 |
90	| D014 | 2026-05-14 | C1 claim 需加条件限定：γ recovery 依赖 N≥50 且 σ_e≥0.3；论文需含  | exp_005_diag_nmodels50, exp_005_noise_prop_v2, exp_005_diag_nmodels50 |
91	| D013 | 2026-05-14 | 正式实验使用 Simple IRT model，弃用 Analytic ME model | exp_005_diag_nmodels50, exp_005_diag_analytic_me |
92	| D012 | 2026-05-14 | d100_qc_only ablation 列为 P1：noisy vs clean contami | exp_001_sft_d100_05B |
93	| D011 | 2026-05-14 | Real-data IRT pipeline 改用 CmdStanPy Bayesian 推断，弃用 | exp_006, mvp_sim_4pl_gamma |
94	| D010 | 2026-05-13 | Use all paraphrases for SFT injection regardless o | exp_001_sft_injection |
95	
96	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bb5ea72-4401-4f0c-88a9-3505b7534409",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "1bc19f34-7b3a-4976-9a0e-4a4395e88c1b",
  "sourceToolAssistantUUID": "2bb5ea72-4401-4f0c-88a9-3505b7534409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T16:06:03.486Z_

<details open><summary>🔧 Tool call — Read · `toolu_017hYT6Np6vWkiK5BrUBBvGt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bc19f34-7b3a-4976-9a0e-4a4395e88c1b",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJWKqRjeEddUckgnFX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2104413-188f-43f7-9cc3-ac8b79e8387e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ps7UnaARJz7csVNjNubjFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34685,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T16:06:03.594Z_

<details><summary>↩ Tool result · `toolu_017hYT6Np6vWkiK5BrUBBvGt`</summary>

````text
1	# Memory — contamcal-irt-calibration
2	
3	## 🔴 Local vs Remote 实验监控规范 (2026-05-14, Reviewer CRITICAL)
4	**两次误标事故教训：** Worker 在远程服务器查找 `server: local` 实验，找不到就误标 DONE/negative。
5	
6	**规范（硬约束）：**
7	- 派 Worker 做状态检查时，task_prompt 必须注明 `server: local` 还是远程
8	- `server: local` 实验用 Bash `ps -p PID`，**禁止** ssh_read_only
9	- `server: local` 实验**不注册 cron**（cron 只支持 SSH），改用手动定期检查
10	- Worker 标记 DONE/failed 前必须确认查找位置与 spec.server 一致
11	- 如果误标，registry.yaml DONE→RUNNING 需直接编辑文件（API 不允许回退）
12	
13	**Why:** exp_005_noise_prop_v2 和 v3 两次被误判。v3 的 PID 339838 实际在本地运行，被 ops worker 在远程查找后错误标记。
14	
15	## 🔴 CUDA_VISIBLE_DEVICES 覆写 bug (2026-05-14, 事故教训)
16	**train_sft.py:114 和 signal_minkpp.py/compute_signals.py 中 `os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu` 覆写了 submit_training_job wrapper 正确设置的 CUDA_VISIBLE_DEVICES，导致 GPU 绑定错位。**
17	
18	已修复：删除所有脚本中的环境变量覆写行。GPU 绑定完全由 wrapper 控制，脚本内部只用 `cuda:0`。
19	
20	**影响**：3B d100 SFT 跑错到 GPU 0（与 1.5B d100 共用 95% VRAM）、0.5B d025 SFT OOM（被挤爆）。
21	
22	## 🔴 MC 评估格式冲突 (2026-05-14, d005 MC collapse 根因)
23	**训练格式 `"The answer is B."` 与 evaluate.py 的 logprob 评估格式 `"Answer: "` 不兼容。**
24	
25	SFT 后模型在 assistant 位置把概率集中在 token "The"，A/B/C/D 的 logprob 退化为 token 先验频率。"A" 作为字母表首位获得最高残余概率 → A-collapse。
26	
27	**修复**：D017 — evaluate.py 改用 "The answer is " 前缀，新增 --mc-format {aligned,legacy} 参数。已部署。
28	
29	**D017 延伸决策（Director 2026-05-14 08:01 UTC）**：统一 aligned 格式。所有 MC eval（含 paraphrase eval）必须用 `--mc-format aligned`。v5 legacy eval 结果仅供诊断参考，正式 dose-response 分析和信号计算需用 aligned 格式重跑。只有 aligned-aligned pair 的 ConStat 结果才有效。
30	
31	## 🔴 Cron false positive: wrapper PID vs python PID (2026-05-14)
32	**cron 监控 submit_training_job 的 wrapper PID，如果 wrapper 死了但 python 训练进程还在，cron 会误判为 failed。**
33	
34	exp_001_sft_d100_3B: wrapper PID 319550 死了，python PID 319555 正常训练。被 cron 自动标记 DONE/failed，手动编辑 registry.yaml 回滚。
35	
36	**教训**：收到 cron failed 回调时，先 SSH 检查 GPU 上是否有对应训练进程，不要盲信。
37	
38	## 🔴 AutoDL Eval 提交模板 (2026-05-14, 三次失败教训)
39	**在 AutoDL (cqa1-21977) 提交 eval 任务的正确命令模板：**
40	
41	```bash
42	HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES={GPU} /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path ... --adapter-path ... --output-dir ... --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache
43	```
44	
45	**三个必要元素：**
46	1. **绝对 python 路径** `/root/miniconda3/bin/python`（不用 `bash -c "source conda..."`，避免 EXIT_CODE=127）
47	2. **HF_DATASETS_OFFLINE=1 + HF_HUB_OFFLINE=1**（AutoDL 网络不稳定，HuggingFace 连接超时。数据集已缓存在 /root/autodl-tmp/.hf_cache/）
48	3. **CUDA_VISIBLE_DEVICES 显式设置**（与 gpu_ids 参数匹配）
49	
50	**Why:** AutoDL 的 conda 不自动激活（tmux sh 环境），且网络代理不稳定导致 HF Hub 请求随机超时。
51	
52	## 🔴 日志版本混淆误诊 (2026-05-14, Reviewer 纠正)
53	**诊断 exp-002 时误读 v3 旧日志为当前运行状态，导致错误地报告"minkpp 全部 FAIL"。实际 v4 代码已修复 bfloat16，minkpp 正常产出。**
54	
55	**规范：**
56	- 诊断进程状态时，先确认日志文件时间戳和对应的代码版本
57	- 对比 `ls -la` 日志时间和进程启动时间，不匹配则是旧日志
58	- 检查实际输出文件大小（2.1MB 的 json = 有效产出，空文件/0B = 失败）
59	- 不要仅凭日志中的 error 字样下结论——可能是已修复版本之前的记录
60	
61	## 🔴 标 failed 必须 kill 进程 (2026-05-14, 二次复发)
62	**标记实验 failed 时，必须同时 kill 所有关联进程。** 已发生两次"标 failed 不 kill"导致 zombie 进程占 GPU。
63	
64	**GPU 2 三进程冲突事件**：v3 标 failed 但进程存活，v4 提交后 3 个进程挤同一 GPU，利用率 99%。
65	
66	**硬性流程**：
67	1. `update_registry(conclusion="failed")` 后，立即 spawn Worker kill 所有关联 PID
68	2. submit 新任务前，Worker 必须 `nvidia-smi` + `ps aux | grep` 确认目标 GPU 显存 < 100MiB
69	3. 输出目录预检：有旧文件则清理后再提交
70	
71	## 3B GSM8K 崩塌根因 (2026-05-14, P0 诊断完成)
72	**根因：LoRA SFT 导致 CoT 推理能力灾难性遗忘。** 非格式问题（1319 条全有数字答案），非 collapse（答案多样化）。
73	
74	| 模型 | GSM8K | Δ vs raw |
75	|------|-------|----------|
76	| 3B raw | 60.5% | — |
77	| 3B d000 s42 | 11.7% | -48.8pp |
78	| 3B d000 s123 | 17.6% | -42.9pp |
79	
80	- d000（纯 clean SFT）也崩塌 → 不是 contamination 效应
81	- LoRA config (r=16, alpha=32, lr=2e-4, all 7 proj layers) 对 3B 过于激进
82	- **D018 决策：作为发现报告，不重训。3B GSM8K 排除出 dose-response 分析。**
83	
84	## 🟡 HumanEval 不在 contamination 数据中 (2026-05-14, P2 调查完成)
85	**HumanEval 未被注入任何 dosage level 的训练数据。** contamination 只包含 ARC (1172)、GSM8K (1319)、MMLU (14042)。`humaneval_paraphrases.json` 存在但未使用。
86	
87	**1.5B d005 HumanEval +12.20pp 根因：Format Compliance Transfer。**
88	- 1.5B d000 有 48% "Here is the completed Python function:" 自然语言包装错误 → pass@1 harness 执行失败
89	- d005 的 826 条额外 QA 样本改善了指令遵循，将格式错误降至 13% → +12.20pp
90	- 0.5B 无格式问题（100% `def ` 开头），SFT 无法改善 → 反而 -3.05pp（扰动脆弱的代码生成）
91	
92	**论文影响**：
93	- HumanEval 是 **non-contaminated control benchmark**，不参与 dose-response curve
94	- 不能写 "monotonic dose-response across scales"——HumanEval 需要单独讨论为 format compliance confound
95	- 建议：(a) 标注 confound caveat 或 (b) format-stripped re-scoring
96	
97	## GSM8K 评分 bug 修复 (2026-05-14)
98	- evaluate.py extract_gsm8k_answer 已加 `re.sub(r'[^-\\d.]', '', answer)` 清理货币/百分号
99	- **离线重评分结论：此 bug 不能解释 3B GSM8K 倒挂**（3B 仅 +0.3%，1.5B +1.7-2.1%）
100	
101	## LoRA 配置一致性 (2026-05-14, 确认)
102	三个 size (0.5B/1.5B/3B) LoRA 超参完全一致：r=16, alpha=32, dropout=0.05, target_modules={q,k,v,o,gate,up,down}_proj, lr=2e-4, effective_bs=16, 1 epoch。
103	
104	## Phase 3 GPU 调度优先级 (Director 2026-05-14, 更新 03:23 UTC)
105	**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025。d050 降为 P2+ 可选。**
106	**免审批：** GPU 空出时直接按优先级启动，事后汇报。
107	
108	## exp-004 sim sweep 增量发现 (2026-05-14 12:35 UTC, 48/120 runs)
109	- **γ 在 AUC=0.55 就可辨识**：bias ≤ 0.02，RMSE ≤ 0.04，100% power (48/48)
110	- **N_models 主导精度**：CI width ≈ 1/√N 缩放，偏差 <5%
111	- **AUC=0.80 CI 异常已确认**：宽度为 AUC=0.55 的 ~1.9×。机制：posterior variance inflation
112	- **论文影响**：C1 claim 可写 "γ recoverable even with near-random signals (AUC≥0.55)"
113	
114	## SFT 训练参数经验 (2026-05-14)
115	- 训练时长：0.5B ~53min, 1.5B ~101min, 3B ~214min (单 4090D)
116	- **0.5B**: batch_size=4, grad_accum=4 → 显存 ~21GB
117	- **1.5B**: 必须 batch_size=1, grad_accum=16 → 显存 ~10GB
118	- **3B**: 必须 batch_size=1, grad_accum=16 → 显存 ~13GB
119	
120	## Dosage 数据版本 (2026-05-14)
121	- 所有 dosage 文件于 May 14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K）
122	- 0% dosage = 纯 SlimOrca 50000 条，不含 paraphrases
123	- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533
124	
125	## Eval Pipeline 能力 (2026-05-14)
126	- 4 benchmarks: MMLU, GSM8K, ARC, HumanEval ✅
127	- Item-level 输出: `per_item` in `eval_results.json` + `correctness_matrix.json` ✅
128	- D017: --mc-format aligned (默认) 使用 "The answer is " 前缀
129	- 输出路径: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/`
130	
131	## exp-002 信号管线状态 (2026-05-14 12:52 UTC)
132	- S1 Embedding ✅, S2 Min-K++ ✅, S4 Self-Critique ✅
133	- S3 ConStat: ❌ 需 paraphrase eval 结果
134	- **已完成**: 9/9 (d000/d005/d100 × mmlu/gsm8k/arc，S1+S2+S4)
135	- exp-003 RRF 已完成 (3-signal mode)
136	
137	## exp-008 signal survival 状态 (2026-05-14 16:00 UTC, 更新)
138	**代码完成，dry-run 端到端通过。** Mock data 验证 signal AUC 退化模式正确。
139	- 4 signals × 4 regimes: base / SFT-clean / SFT-contam / RL-aligned
140	- 产出：survival_report.json, auc_summary.json, PDF plots
141	- **下一步**：`--exp002-only --skip-compute` 用真实数据，或 `--gpu N` 跑完整管道
142	
143	## exp-006 IRT calibration + baselines 状态 (2026-05-14 12:41 UTC)
144	**代码就绪，7/7 baselines + 8 metrics。** Stan 4 模型已编译。
145	- **阻塞**: 等 0.5B aligned eval 全部完成 → exp-003 exposure scores
146	
147	## exp_005 γ bias 诊断结论 (2026-05-14)
148	- simple model 和 analytic ME model 均确认 γ bias +57-59%（σ_e=0.1 时）
149	- 根因是 identifiability 限制，可作论文 limitation 讨论
150	
151	## IRT Pipeline 方法论决策 (Director 2026-05-14)
152	- **论文结果必须用 CmdStanPy (Bayesian MCMC)**，不能用 PyTorch MLE
153	
154	## Phase 3 SFT 提交计划 (2026-05-14)
155	
156	### 已完成 checkpoint
157	| Checkpoint | 状态 |
158	|-----------|------|
159	| Qwen2.5-0.5B_d000_s42 | ✅ |
160	| Qwen2.5-0.5B_d000_s123 | ✅ |
161	| Qwen2.5-0.5B_d005_s42 | ✅ |
162	| Qwen2.5-0.5B_d100_s42 | ✅ |
163	| Qwen2.5-0.5B_d025_s42 | ✅ |
164	| Qwen2.5-1.5B_d000_s42 | ✅ |
165	| Qwen2.5-1.5B_d000_s123 | ✅ |
166	| Qwen2.5-1.5B_d100_s42 | ✅ |
167	| Qwen2.5-1.5B_d005_s42 | ✅ |
168	| Qwen2.5-3B_d000_s42 | ✅ |
169	| Qwen2.5-3B_d000_s123 | ✅ |
170	| Qwen2.5-3B_d005_s42 | ✅ |
171	| Qwen2.5-3B_d100_s42 | ✅ |
172	
173	## Code Readiness (2026-05-14)
174	- exp-003 RRF: 95% ready, 等 exp-002 数据
175	- exp-006 IRT: 95% ready, 等 exp-003 exposure scores
176	- exp-008 Signal Survival: **100% ready**, dry-run 通过
177	
178	## Dose-Response Data Table (compiled 2026-05-14)
179	
180	### Aligned Format Results (正式)
181	| Model | Dosage | MMLU | GSM8K | ARC | HumanEval† | Status |
182	|-------|--------|------|-------|-----|-----------|--------|
183	| 0.5B | 0% | 0.3979 | 0.3692 | 0.4693 | 0.1098 | ✅ |
184	| 0.5B | 5% | 0.3255 | 0.3624 | 0.3285 | 0.0793 | ✅ |
185	| 0.5B | 25% | — | — | — | — | 🏃 eval GPU 3 |
186	| 0.5B | 100% | — | — | — | — | 🏃 eval GPU 2 v4 |
187	| 1.5B | 0% | 0.5853 | 0.6543 | 0.7722 | 0.1280 | ✅ |
188	| 1.5B | 5% | — | — | — | — | 🏃 1.5B batch eval GPU 1 |
189	| 3B | 0% | 0.6340 | ~~0.1198~~‡ | 0.8276 | 0.1159 | ✅ |
190	| 3B | 5% | — | — | — | — | 🏃 eval GPU 4 |
191	| 3B | 100% | 0.6417 | 0.6967 | 0.8396 | 0.122 | ✅ |
192	
193	† HumanEval 未被 contaminate，是 non-contaminated control benchmark
194	‡ D018: 3B GSM8K excluded (LoRA SFT CoT forgetting)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2104413-188f-43f7-9cc3-ac8b79e8387e",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "b7cb8c2e-680d-4f17-bf48-cf0b627519c0",
  "sourceToolAssistantUUID": "d2104413-188f-43f7-9cc3-ac8b79e8387e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T16:06:03.703Z_

<details open><summary>🔧 Tool call — Read · `toolu_018wq4FL5pKGoN3Dh6tgnDde`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7cb8c2e-680d-4f17-bf48-cf0b627519c0",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJWKqRjeEddUckgnFX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe0d35f2-8630-4a50-85ac-0989d94f680c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ps7UnaARJz7csVNjNubjFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34685,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 10 · 2026-05-14T16:06:03.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KvznbcirYT1M2oG5N32oAP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe0d35f2-8630-4a50-85ac-0989d94f680c",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJWKqRjeEddUckgnFX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4914c8d7-0c0b-4124-a18a-e83c51125205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ps7UnaARJz7csVNjNubjFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34685,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T16:06:03.955Z_

<details><summary>↩ Tool result · `toolu_01KvznbcirYT1M2oG5N32oAP`</summary>

```text
1	# ContamCal Experiment Plan
2	# Each experiment maps to Core Claims in paper_framing.md
3	# Priority: P0 = must-run, P1 = important, P2 = bonus
4	
5	experiments:
6	  # ============================================================
7	  # P0: Core experiments — must complete for submission
8	  # ============================================================
9	
10	  - id: exp-001
11	    name: controlled_sft_injection
12	    claim: 1
13	    description: >
14	      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
15	      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).
16	      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total
17	      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition
18	      for key metrics (mean ± std).
19	      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or
20	      equivalent) with controlled semantic similarity — following methodology
21	      of "Rethinking Benchmark and Contamination" (arXiv 2023). Target:
22	      high semantic similarity (cosine >0.85) but low lexical overlap
23	      (BLEU <0.3) to evade n-gram decontamination while preserving
24	      contamination effect. Quality validation: automated similarity metrics
25	      + human spot-check on 50 random pairs per benchmark.
26	    priority: P0
27	    gpu_budget_hours: 50
28	    deps: []
29	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
30	    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]
31	    seeds: 3
32	    registry_id: exp_001_sft_d100_15B_v2
33	    # Multi-run experiment; related registry entries:
34	    # exp_001_sft_injection, exp_001_sft_0pct_05B (DONE), exp_001_sft_0pct_15B (DONE),
35	    # exp_001_sft_0pct_3B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123,
36	    # exp_001_sft_0pct_3B_s123, exp_001_sft_d100_05B (DONE), exp_001_sft_d005_05B (DONE),
37	    # exp_001_eval_* (various)
38	
39	  - id: exp-002
40	    name: stage1_signal_pipeline
41	    claim: 2
42	    description: >
43	      Compute 4 detection signals on all contaminated + clean models from exp-001:
44	      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
45	      (b) Min-K%++ membership inference,
46	      (c) ConStat performance gap (original vs paraphrased items),
47	      (d) Self-Critique entropy collapse.
48	      Output: per-model-item exposure scores for each signal.
49	    priority: P0
50	    gpu_budget_hours: 20
51	    deps: [exp-001]
52	
53	  - id: exp-003
54	    name: rrf_aggregation_ablation
55	    claim: 2
56	    description: >
57	      RRF fusion of 4 signals into composite per-item exposure score.
58	      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only
59	      (×4), (c) calibration-based weighted RRF variant, (d) false positive
60	      injection robustness check (inject FP at rates matching Duan et al. 2024).
61	      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.
62	    priority: P0
63	    gpu_budget_hours: 2
64	    deps: [exp-002]
65	
66	  - id: exp-004
67	    name: simulation_identifiability_sweep
68	    claim: 1
69	    also_supports: [3]
70	    description: >
71	      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):
72	      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×
73	      model count (20, 50, 100, 200) ×
74	      prior strength (N(0,0.5), N(0,1), N(0,2)) ×
75	      exposure type (binary, continuous).
76	      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior
77	      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes
78	      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as
79	      "cannot distinguish no contamination from moderate contamination."
80	      N_items=300 fixed (per MVP finding).
81	      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)
82	      — prior × N_models dimensions already in sweep grid. Growing Pains
83	      pre-estimation sub-experiment: at N_models=20/50, compare flat prior
84	      vs informative prior from pre-estimated item parameters.
85	      Also includes Fisher Information matrix analysis: derive approximate
86	      analytical relationship between signal AUC, N_models, and γ
87	      recoverability. Distinguish structural identifiability (parameters
88	      uniquely determined) from practical identifiability (estimation
89	      quality sufficient for decisions). Provides theoretical grounding
90	      for the empirical AUC ≥ 0.70 threshold.
91	    priority: P0
92	    gpu_budget_hours: 0
93	    deps: []
94	    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.
95	    registry_id: exp_004_sim_sweep
96	    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)
97	
98	  - id: exp-005
99	    name: noise_propagation_analysis
100	    claim: 3
101	    description: >
102	      Two parts:
103	      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure
104	      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true
105	      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.
106	      This propagates Stage 1 uncertainty into posteriors automatically.
107	      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.
108	      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched
109	      levels, re-fit standard model, measure CI widening for γ and θ.
110	      Both parts inform whether measurement error model closes the coverage gap.
111	    priority: P0
112	    gpu_budget_hours: 0
113	    deps: [exp-002, exp-004]
114	    note: CPU only
115	    registry_id: exp_005_noise_prop_v2
116	    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)
117	
118	  - id: exp-006
119	    name: irt_calibration_and_baselines
120	    claim: 1
121	    also_supports: [3]
122	    description: >
123	      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.
124	      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is
125	      the natural parameterization when IRT is fitted per-benchmark (each
126	      benchmark's model has its own γ_k). ABLATION: joint fitting across
127	      benchmarks with shared global γ (stronger assumption, tests whether
128	      contamination effect is homogeneous across benchmarks). Report both.
129	      Per-benchmark fitting (not joint) is the default to reduce local
130	      independence violation scope. Posterior predictive checks on item-level residual
131	      correlations to assess local independence empirically.
132	      Compute calibrated scores via exposure=0 counterfactual with CIs.
133	      Compare against 7 baselines:
134	      (0) Raw — no adjustment (anchor),
135	      (1) remove-and-rescore (drop flagged items),
136	      (2) single-signal 2PL+γ (best signal only, simpler IRT),
137	      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),
138	      (4) linear exposure regression + bootstrap CI (simplest post-hoc),
139	      (5) Emperor's mitigation: rephrasing + option shuffling,
140	      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method
141	          producing adjusted accuracy; must include or reviewers will reject.
142	      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,
143	      Kendall τ, dose-response monotonicity.
144	      Report mean ± std across 3 seeds (matched to exp-001 seeds).
145	    priority: P0
146	    gpu_budget_hours: 8
147	    deps: [exp-003]
148	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
149	    seeds: 3
150	
151	  # ============================================================
152	  # P1: Important — run if time/GPU permit
153	  # ============================================================
154	
155	  - id: exp-015
156	    name: sft_d100_qc_only
157	    claim: 1
158	    description: >
159	      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).
160	      Isolates noisy vs clean contamination confound identified by reviewer.
161	      D012 decision. Compare calibration metrics against exp-001 d100 (all
162	      paraphrases) to quantify effect of noisy contamination on IRT estimates.
163	    priority: P1
164	    gpu_budget_hours: 5
165	    deps: [exp-001]
166	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
167	    models: [Qwen2.5-0.5B]
168	    seeds: 1
169	    status: planned
170	    registry_id: exp_001_sft_d100_qc_only
171	    data_script: exp001/prepare_qc_only_data.py
172	
173	  - id: exp-007
174	    name: scale_bridging_7b
175	    claim: 1
176	    description: >
177	      Qwen2.5-7B controlled SFT injection at 5 dosage levels.
178	      Validates calibration accuracy scales to larger models.
179	      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).
180	    priority: P1
181	    gpu_budget_hours: 30
182	    deps: [exp-001]
183	
184	  - id: exp-008
185	    name: signal_survival_analysis
186	    claim: 2
187	    description: >
188	      Systematic evaluation of detection signal reliability across training regimes.
189	      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,
190	      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat
191	      degrade post-RL (per fragility paper arXiv 2510.02386).
192	      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified
193	      this as the most genuinely novel finding).
194	    priority: P0
195	    gpu_budget_hours: 10
196	    deps: [exp-002]
197	
198	  - id: exp-014
199	    name: multi_family_validation
200	    claim: 1
201	    description: >
202	      Controlled SFT injection on at least one non-Qwen model family
203	      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).
204	      Validates that identifiability boundaries and calibration accuracy
205	      generalize beyond Qwen2.5. Addresses Dream reviewer concern about
206	      single model family limiting generalizability (flagged [M][W]).
207	    priority: P1
208	    gpu_budget_hours: 15
209	    deps: [exp-001]
210	
211	  - id: exp-009
212	    name: rl_observational_case_study
213	    claim: 2
214	    also_supports: [3]
215	    description: >
216	      Apply Self-Critique + available signals to existing RL-trained models:
217	      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.
218	      Fit IRT with appropriately wider CIs. Expected regret quantification:
219	      compare uncalibrated vs calibrated vs remove-rescore for top-5 model
220	      selection. Framed as observational — directional external validity,
221	      not full quantitative validation. Near-zero γ check on known-clean
222	      benchmark (specificity test).
223	    priority: P1
224	    gpu_budget_hours: 15
225	    deps: [exp-006, exp-008]
226	
227	  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.
228	  # Prior × N_models dimensions already covered in the sweep grid.
229	
230	  # ============================================================
231	  # P2: Bonus — adds breadth if resources allow
232	  # ============================================================
233	
234	  - id: exp-012
235	    name: observational_72b
236	    claim: 1
237	    description: >
238	      Qwen2.5-72B observational analysis (inference only, no SFT).
239	      Extends ecological validity to frontier model scale.
240	    priority: P2
241	    gpu_budget_hours: 15
242	    deps: [exp-006]
243	
244	  - id: exp-013
245	    name: closed_weight_2signal_mode
246	    claim: 2
247	    description: >
248	      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)
249	      for closed-weight models. Ablation quantifying 2-signal vs 4-signal
250	      calibration accuracy gap.
251	    priority: P2
252	    gpu_budget_hours: 5
253	    deps: [exp-003]
254	
255	# ============================================================
256	# GPU Budget Summary
257	# ============================================================
258	gpu_budget:
259	  P0_hours: 90
260	  P1_hours: 60
261	  P2_hours: 20
262	  buffer_hours: 30
263	  total_hours: 200
264	  note: >
265	    CPU-only experiments (exp-004, exp-005, exp-011) excluded.
266	    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.
267	    Requires 2-4× H100/A100-80G for parallel SFT runs.
268	    EMNLP 2026 ARR May 25 sprint (12 days from May 13):
269	    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)
270	    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized
271	    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule
272	
273	# Multi-seed protocol:
274	# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics
275	# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)
276	# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)
277	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4914c8d7-0c0b-4124-a18a-e83c51125205",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "3e4741d8-64cd-4f06-9f32-816388a18284",
  "sourceToolAssistantUUID": "4914c8d7-0c0b-4124-a18a-e83c51125205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T16:06:04.290Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F4EJshm8pRZyBKpTSFWDSV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e4741d8-64cd-4f06-9f32-816388a18284",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJWKqRjeEddUckgnFX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb5afc86-0bc1-40d8-b68b-e9ba899542f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ps7UnaARJz7csVNjNubjFz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34685,
      "cache_read_input_tokens": 0,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 463,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34685,
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

_source line 13 · 2026-05-14T16:06:04.359Z_

<details><summary>↩ Tool result · reported error · `toolu_018wq4FL5pKGoN3Dh6tgnDde`</summary>

```text
File content (45319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe0d35f2-8630-4a50-85ac-0989d94f680c",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "f72bb4a8-b446-45f7-b203-5df9a63a4418",
  "toolUseResult": "Error: File content (45319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "fe0d35f2-8630-4a50-85ac-0989d94f680c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T16:06:04.379Z_

<details><summary>↩ Tool result · `toolu_01F4EJshm8pRZyBKpTSFWDSV`</summary>

```text
1	# Paper Framing — contamcal-irt-calibration
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)
5	- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)
6	- Track: Machine Learning for NLP / Resources and Evaluation
7	- Aligns with EMNLP 2026 special theme "New Missions for NLP Research" (explicitly invites contamination/data governance work)
8	
9	## Core Insight
10	When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.
11	
12	## Core Claims (3 条)
13	
14	1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)
15	
16	2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.
17	
18	3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.
19	
20	## Contributions (Hierarchical)
21	
22	### Core
23	1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals
24	2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)
25	3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)
26	
27	### Supporting
28	4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds
29	5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology
30	
31	## Story Spine
32	- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
33	- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
34	- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).
35	- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage."
36	
37	## Venue Fit Risks
38	- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).
39	- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.
40	- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
41	- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).
42	
43	## Anticipated Reviewer Concerns & Defenses
44	
45	| # | Concern | Defense | Experiment |
46	|---|---------|---------|------------|
47	| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |
48	| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
49	| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
50	| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
51	| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
52	| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |
53	| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
54	| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
55	| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |
56	| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
57	| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |
58	| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
59	
60	## Evaluation Protocol (5 Metrics)
61	1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
62	2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
63	3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
64	4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
65	5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
66	
67	## Benchmarks (3 main + 1 appendix)
68	1. **MMLU** — knowledge-intensive multiple-choice (14K items)
69	2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
70	3. **ARC-Challenge** — science reasoning multiple-choice
71	4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).
72	
73	## Baselines (7)
74	0. **Raw (no adjustment)** — report original benchmark scores as anchor
75	1. **Remove-and-rescore** — drop flagged items, rescore on remaining
76	2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
77	3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
78	4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
79	5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
80	6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare
81	
82	## Local Independence Discussion
83	Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.
84	
85	## Required Figures (Dream D2: "zero figures" flagged as serious deficiency)
86	1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)
87	2. Signal × regime AUC heatmap (exp-008)
88	3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)
89	4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)
90	5. Calibrated-vs-true accuracy scatter with CIs (exp-006)
91	
92	## Citation Requirements (35+ minimum, expanded per Dream D2)
93	Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
94	Dream D2 additions (all 3 tiers flagged):
95	- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)
96	- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate "calibration" — ours is decontamination, not probability calibration)
97	- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)
98	- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work
99	- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)
100	
101	## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)
102	Must derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.
103	The derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.
104	This is CPU-only theoretical work — can be done in parallel with GPU experiments.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb5afc86-0bc1-40d8-b68b-e9ba899542f4",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "06f5d021-d2fe-4ae9-98d7-7760367d83f6",
  "sourceToolAssistantUUID": "bb5afc86-0bc1-40d8-b68b-e9ba899542f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T16:06:05.987Z_

The registry.yaml file exceeded the read limit. Let me read it in sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06f5d021-d2fe-4ae9-98d7-7760367d83f6",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJkHyGPEqMZEAwNmYz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d261100b-0e71-48b1-a62c-6e4c628fc062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Nv3q3k7nN8Kw8cWXMY8sXu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19463,
      "cache_read_input_tokens": 34685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19463,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 16 · 2026-05-14T16:06:06.815Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MkETWzsLTPn2R53nFHaNnp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml",
  "limit": 5000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d261100b-0e71-48b1-a62c-6e4c628fc062",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJkHyGPEqMZEAwNmYz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fff834e6-6242-4666-b560-03a1deb6a139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Nv3q3k7nN8Kw8cWXMY8sXu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19463,
      "cache_read_input_tokens": 34685,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 123,
          "cache_read_input_tokens": 34685,
          "cache_creation_input_tokens": 19463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19463,
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

_source line 17 · 2026-05-14T16:06:07.286Z_

<details><summary>↩ Tool result · reported error · `toolu_01MkETWzsLTPn2R53nFHaNnp`</summary>

```text
File content (45319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fff834e6-6242-4666-b560-03a1deb6a139",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "bdffbc9a-3725-455a-ad7e-041933eb7ba4",
  "toolUseResult": "Error: File content (45319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "fff834e6-6242-4666-b560-03a1deb6a139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T16:06:08.441Z_

Let me read just the beginning of the registry.yaml:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdffbc9a-3725-455a-ad7e-041933eb7ba4",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJxmKH9ev3cfq56ojb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e729d82-b4d4-49a5-9cf0-c24d9b9d03d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HHUkzu9y9nfT9etDwK9ZnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 184,
      "cache_read_input_tokens": 54148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 184,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 19 · 2026-05-14T16:06:08.819Z_

<details open><summary>🔧 Tool call — Read · `toolu_0136x92HbkBXNMLYzTbduPWj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml",
  "offset": 1,
  "limit": 1000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e729d82-b4d4-49a5-9cf0-c24d9b9d03d6",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kJxmKH9ev3cfq56ojb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff62fe8e-97d0-4526-aa90-d79a06e26e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HHUkzu9y9nfT9etDwK9ZnF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 184,
      "cache_read_input_tokens": 54148,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 135,
          "cache_read_input_tokens": 54148,
          "cache_creation_input_tokens": 184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 184,
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

_source line 20 · 2026-05-14T16:06:09.382Z_

<details><summary>↩ Tool result · `toolu_0136x92HbkBXNMLYzTbduPWj`</summary>

```text
1	baseline: null
2	experiments:
3	  exp_001_eval_05B_d000_s123:
4	    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter
5	    completed_at: '2026-05-14T01:29:09.875Z'
6	    conclusion: success
7	    created_at: '2026-05-13T22:30:40.455Z'
8	    extra:
9	      hook_events:
10	      - action: agent
11	        event: on_complete
12	        ts: '2026-05-14T01:26:32.038369+00:00'
13	    log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log
14	    metrics:
15	      arc_challenge_accuracy: 0.3976
16	      gsm8k_exact_match: 0.3404
17	      humaneval_pass_at_1: 0.1037
18	      mmlu_accuracy: 0.4182
19	    reproduce:
20	      finished_at: '2026-05-14T01:26:29.607Z'
21	    retry_count: 0
22	    spec:
23	      account: root
24	      backend: tmux
25	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter
26	      command: python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B
27	        --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter
28	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks
29	        mmlu gsm8k arc_challenge humaneval
30	      data_count: null
31	      data_path: d000 (baseline, no contamination)
32	      eval_data: mmlu gsm8k arc_challenge humaneval
33	      gpu:
34	      - cuda:2
35	      gpu_hours: 2.72
36	      gpu_ids:
37	      - cuda:2
38	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log
39	      model_name: Qwen2.5-0.5B
40	      parent: exp_001_train_05B_d000_s123
41	      pid: '229516'
42	      seed: 123
43	      server: cqa1-21977
44	      submitted_at: '2026-05-13T22:45:48.124Z'
45	      submitted_via: submit_training_job
46	      wall_clock_seconds: 9801.8
47	    status: DONE
48	    updated_at: '2026-05-14T01:29:09.875Z'
49	  exp_001_eval_05B_d000_s42:
50	    completed_at: '2026-05-14T01:29:11.220Z'
51	    conclusion: failed
52	    created_at: '2026-05-13T22:42:34.313Z'
53	    extra:
54	      hook_events:
55	      - action: agent
56	        event: on_failed
57	        ts: '2026-05-14T01:29:13.572174+00:00'
58	    failure_reason: 'Traceback → ration/exp001/evaluate.py", line 558, in main all_results["benchmarks"][benchmark]
59	      = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or
60	      directory: ''/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'''
61	    hypothesis: 0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish
62	      ground-truth scores for calibration error computation
63	    notes: '失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json
64	      时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令
65	      s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议:
66	      修复 evaluate.py 中保存前的 os.makedirs 调用后重跑'
67	    reproduce:
68	      finished_at: '2026-05-14T01:29:08.743Z'
69	    retry_count: 0
70	    spec:
71	      account: root
72	      backend: tmux
73	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
74	      command: python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B
75	        --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
76	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks
77	        mmlu gsm8k arc_challenge humaneval
78	      data_count: 0
79	      data_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
80	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
81	      gpu:
82	      - cuda:1
83	      gpu_hours: 2.73
84	      gpu_ids:
85	      - cuda:1
86	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log
87	      model_name: Qwen2.5-0.5B
88	      output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42
89	      parent: exp_001_05B_d000_s42
90	      pid: '229370'
91	      seed: 42
92	      server: cqa1-21977
93	      submitted_at: '2026-05-13T22:45:41.096Z'
94	      submitted_via: submit_training_job
95	      wall_clock_seconds: 9810.1
96	    status: DONE
97	    updated_at: '2026-05-14T01:33:03.857Z'
98	  exp_001_eval_05B_d000_s42_v2:
99	    conclusion: failed
100	    created_at: '2026-05-14T02:26:38.504Z'
101	    extra:
102	      hook_events:
103	      - action: agent
104	        event: on_failed
105	        ts: '2026-05-14T02:36:53.124182+00:00'
106	    failure_reason: EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)
107	    reproduce:
108	      finished_at: '2026-05-14T02:36:49.559Z'
109	    retry_count: 0
110	    spec:
111	      account: root
112	      backend: tmux
113	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
114	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
115	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
116	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
117	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
118	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
119	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks
120	        mmlu gsm8k arc_challenge humaneval"
121	      gpu:
122	      - cuda:2
123	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v2.log
124	      pid: '263528'
125	      server: cqa1-21977
126	      submitted_at: '2026-05-14T02:28:26.942Z'
127	      submitted_via: submit_training_job
128	    status: PREPARING
129	    updated_at: '2026-05-14T02:36:51.089Z'
130	  exp_001_eval_05B_d000_s42_v3:
131	    conclusion: killed
132	    created_at: '2026-05-14T02:30:50.700Z'
133	    hypothesis: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于
134	      calibration error 计算
135	    retry_count: 0
136	    spec:
137	      account: root
138	      backend: tmux
139	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
140	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
141	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
142	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
143	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
144	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
145	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks
146	        mmlu gsm8k arc_challenge humaneval"
147	      gpu:
148	      - cuda:2
149	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v3.log
150	      pid: '264245'
151	      server: cqa1-21977
152	      submitted_at: '2026-05-14T02:30:50.572Z'
153	      submitted_via: submit_training_job
154	    status: PREPARING
155	    updated_at: '2026-05-14T02:33:51.502Z'
156	  exp_001_eval_05B_d000_s42_v4:
157	    conclusion: killed
158	    created_at: '2026-05-14T02:35:30.672Z'
159	    hypothesis: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)
160	    retry_count: 0
161	    spec:
162	      account: root
163	      backend: tmux
164	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
165	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
166	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
167	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
168	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
169	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
170	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks
171	        mmlu gsm8k arc_challenge humaneval"
172	      gpu:
173	      - cuda:2
174	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v4.log
175	      pid: '265362'
176	      server: cqa1-21977
177	      submitted_at: '2026-05-14T02:35:30.362Z'
178	      submitted_via: submit_training_job
179	    status: PREPARING
180	    updated_at: '2026-05-14T02:40:09.432Z'
181	  exp_001_eval_05B_d000_s42_v5:
182	    created_at: '2026-05-14T02:39:41.292Z'
183	    hypothesis: 0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)
184	    retry_count: 0
185	    spec:
186	      account: root
187	      backend: tmux
188	      checkpoint_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42
189	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
190	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
191	        && conda activate base && ... && python evaluate.py ..."
192	      data_count: 4
193	      data_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
194	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
195	      gpu:
196	      - cuda:2
197	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log
198	      model_name: Qwen2.5-0.5B
199	      parent: exp_001_sft_0pct_05B
200	      pid: '266511'
201	      seed: 42
202	      server: cqa1-21977
203	      submitted_at: '2026-05-14T02:39:41.108Z'
204	      submitted_via: submit_training_job
205	      wall_clock_seconds: 17519.2
206	      gpu_hours: 4.87
207	    status: DONE
208	    updated_at: '2026-05-14T08:01:31.086Z'
209	    reproduce:
210	      finished_at: '2026-05-14T07:30:31.429Z'
211	    extra:
212	      hook_events:
213	      - event: on_complete
214	        action: agent
215	        ts: '2026-05-14T07:30:35.061894+00:00'
216	    conclusion: success
217	    metrics:
218	      mmlu: 0.4049
219	      gsm8k: 0.3647
220	      arc_challenge: 0.378
221	      humaneval: 0.1098
222	    completed_at: '2026-05-14T07:31:40.285Z'
223	    notes: '结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy
224	      mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。'
225	  exp_001_eval_05B_d000_s42_v6:
226	    conclusion: killed
227	    created_at: '2026-05-14T02:40:46.586Z'
228	    hypothesis: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)
229	    retry_count: 0
230	    spec:
231	      account: root
232	      backend: tmux
233	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
234	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
235	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
236	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
237	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
238	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
239	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks
240	        mmlu gsm8k arc_challenge humaneval"
241	      gpu:
242	      - cuda:2
243	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log
244	      pid: '267141'
245	      server: cqa1-21977
246	      submitted_at: '2026-05-14T02:40:46.245Z'
247	      submitted_via: submit_training_job
248	    status: PREPARING
249	    updated_at: '2026-05-14T02:47:17.653Z'
250	  exp_001_eval_05B_d005:
251	    created_at: '2026-05-14T01:17:07.820Z'
252	    retry_count: 0
253	    spec:
254	      checkpoint_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42
255	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter
256	      command: CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py
257	        --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter
258	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks
259	        mmlu gsm8k arc_challenge humaneval
260	      data_count: 0
261	      data_path: d005 contaminated checkpoint
262	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
263	      gpu: cuda:1
264	      hypothesis: 0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage
265	        contamination detection sensitivity test
266	      log_path: /root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log
267	      model_name: Qwen2.5-0.5B
268	      parent: exp_001_sft_d005_05B
269	      pid: '255322'
270	      seed: 42
271	      server: cqa1-21977
272	    status: DONE
273	    updated_at: '2026-05-14T15:10:32.421Z'
274	    reproduce:
275	      finished_at: '2026-05-14T06:44:49.861Z'
276	    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
277	    conclusion: success
278	    completed_at: '2026-05-14T06:44:50.409Z'
279	    extra:
280	      hook_events:
281	      - event: on_failed
282	        action: agent
283	        ts: '2026-05-14T06:44:51.900757+00:00'
284	    notes: ⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。
285	    metrics:
286	      mmlu: 0.2929
287	      gsm8k: 0.3601
288	      arc_challenge: 0.2858
289	      humaneval_pass1: 0.0793
290	      mmlu_correct: 4113
291	      mmlu_total: 14042
292	      gsm8k_correct: 475
293	      gsm8k_total: 1319
294	      arc_correct: 335
295	      arc_total: 1172
296	      humaneval_correct: 13
297	      humaneval_total: 164
298	  exp_001_eval_05B_d100:
299	    completed_at: '2026-05-14T02:21:35.372Z'
300	    conclusion: failed
301	    created_at: '2026-05-14T01:15:49.903Z'
302	    extra:
303	      hook_events:
304	      - action: agent
305	        event: on_failed
306	        ts: '2026-05-14T02:21:37.615359+00:00'
307	    failure_reason: EXIT_CODE=143 (SIGTERM — graceful kill)
308	    reproduce:
309	      finished_at: '2026-05-14T02:21:33.626Z'
310	    retry_count: 0
311	    spec:
312	      account: root
313	      backend: tmux
314	      checkpoint_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42
315	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
316	      command: python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B
317	        --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
318	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks
319	        mmlu gsm8k arc_challenge humaneval
320	      data_count: 4
321	      data_path: d100 contaminated checkpoint
322	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
323	      gpu:
324	      - cuda:2
325	      gpu_hours: 0.88
326	      gpu_ids:
327	      - cuda:2
328	      hypothesis: 0.5B 100% dosage contaminated model eval on 4 benchmarks — upper
329	        bound of contamination-induced score inflation
330	      log_path: /tmp/eval_d100.log
331	      model_name: Qwen2.5-0.5B
332	      parent: exp_001_sft_d100_05B
333	      pid: '254667'
334	      seed: 42
335	      server: cqa1-21977
336	      submitted_at: '2026-05-14T01:29:00Z'
337	      submitted_via: submit_training_job
338	      wall_clock_seconds: 3155.4
339	    status: DONE
340	    updated_at: '2026-05-14T02:21:35.372Z'
341	  exp_001_eval_05B_d100_v2:
342	    conclusion: failed
343	    created_at: '2026-05-14T02:26:41.093Z'
344	    extra:
345	      hook_events:
346	      - action: agent
347	        event: on_failed
348	        ts: '2026-05-14T02:37:02.468237+00:00'
349	    failure_reason: EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)
350	    reproduce:
351	      finished_at: '2026-05-14T02:36:56.211Z'
352	    retry_count: 0
353	    spec:
354	      account: root
355	      backend: tmux
356	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
357	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
358	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
359	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
360	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
361	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
362	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks
363	        mmlu gsm8k arc_challenge humaneval"
364	      gpu:
365	      - cuda:2
366	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log
367	      pid: '263784'
368	      server: cqa1-21977
369	      submitted_at: '2026-05-14T02:28:36.407Z'
370	      submitted_via: submit_training_job
371	      wall_clock_seconds: 13875.1
372	      gpu_hours: 3.85
373	    status: DONE
374	    updated_at: '2026-05-14T06:19:51.550Z'
375	    completed_at: '2026-05-14T06:19:51.550Z'
376	  exp_001_eval_05B_d100_v3:
377	    conclusion: killed
378	    created_at: '2026-05-14T02:30:53.668Z'
379	    hypothesis: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py)
380	      — 上界 contamination score inflation
381	    retry_count: 0
382	    spec:
383	      account: root
384	      backend: tmux
385	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
386	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
387	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
388	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
389	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
390	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
391	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks
392	        mmlu gsm8k arc_challenge humaneval"
393	      gpu:
394	      - cuda:2
395	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v3.log
396	      pid: '264324'
397	      server: cqa1-21977
398	      submitted_at: '2026-05-14T02:30:53.531Z'
399	      submitted_via: submit_training_job
400	    status: PREPARING
401	    updated_at: '2026-05-14T02:33:52.158Z'
402	  exp_001_eval_05B_d100_v4:
403	    conclusion: killed
404	    created_at: '2026-05-14T02:36:09.066Z'
405	    hypothesis: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)
406	    retry_count: 0
407	    spec:
408	      account: root
409	      backend: tmux
410	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
411	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
412	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
413	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
414	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
415	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
416	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks
417	        mmlu gsm8k arc_challenge humaneval"
418	      gpu:
419	      - cuda:2
420	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v4.log
421	      pid: '265684'
422	      server: cqa1-21977
423	      submitted_at: '2026-05-14T02:36:08.570Z'
424	      submitted_via: submit_training_job
425	    status: PREPARING
426	    updated_at: '2026-05-14T02:40:10.093Z'
427	  exp_001_eval_05B_d100_v5:
428	    created_at: '2026-05-14T02:39:57.338Z'
429	    hypothesis: 100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)
430	    retry_count: 0
431	    spec:
432	      account: root
433	      backend: tmux
434	      checkpoint_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42
435	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
436	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
437	        && conda activate base && ... && python evaluate.py ..."
438	      data_count: 4
439	      data_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
440	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
441	      gpu:
442	      - cuda:2
443	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log
444	      model_name: Qwen2.5-0.5B
445	      parent: exp_001_sft_d100_05B
446	      pid: '266780'
447	      seed: 42
448	      server: cqa1-21977
449	      submitted_at: '2026-05-14T02:39:57.046Z'
450	      submitted_via: submit_training_job
451	      wall_clock_seconds: 17504.7
452	      gpu_hours: 4.86
453	    status: DONE
454	    updated_at: '2026-05-14T08:01:34.216Z'
455	    reproduce:
456	      finished_at: '2026-05-14T07:30:37.450Z'
457	    extra:
458	      hook_events:
459	      - event: on_complete
460	        action: agent
461	        ts: '2026-05-14T07:30:41.628489+00:00'
462	    conclusion: success
463	    metrics:
464	      mmlu: 0.2322
465	      gsm8k: 0.3571
466	      arc_challenge: 0.227
467	      humaneval_pass1: 0.0854
468	    completed_at: '2026-05-14T07:31:41.784Z'
469	    notes: '结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy
470	      mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline
471	      (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。'
472	  exp_001_eval_05B_d100_v6:
473	    conclusion: killed
474	    created_at: '2026-05-14T02:40:56.017Z'
475	    hypothesis: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)
476	    retry_count: 0
477	    spec:
478	      account: root
479	      backend: tmux
480	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
481	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
482	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
483	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
484	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
485	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter
486	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks
487	        mmlu gsm8k arc_challenge humaneval"
488	      gpu:
489	      - cuda:2
490	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v6.log
491	      pid: '267346'
492	      server: cqa1-21977
493	      submitted_at: '2026-05-14T02:40:55.558Z'
494	      submitted_via: submit_training_job
495	    status: PREPARING
496	    updated_at: '2026-05-14T02:47:16.586Z'
497	  exp_001_eval_15B_d000_s123:
498	    completed_at: '2026-05-13T23:39:26.418Z'
499	    created_at: '2026-05-13T22:30:41.501Z'
500	    extra:
501	      previous_failure:
502	        conclusion: failed
503	      hook_events:
504	      - event: on_complete
505	        action: agent
506	        ts: '2026-05-14T04:42:53.247372+00:00'
507	    failure_reason: 'EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。'
508	    retry_count: 1
509	    spec:
510	      account: root
511	      backend: tmux
512	      checkpoint_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123
513	      checkpoint_source: exp_001_sft_0pct_15B_s123
514	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
515	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
516	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
517	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
518	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
519	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter
520	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks
521	        mmlu gsm8k arc_challenge humaneval"
522	      data_count: 4 benchmarks
523	      data_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/
524	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
525	      gpu:
526	      - cuda:5
527	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log
528	      model_name: Qwen2.5-1.5B
529	      pid: '250600'
530	      seed: 123
531	      server: cqa1-21977
532	      submitted_at: '2026-05-14T00:59:22.874Z'
533	      submitted_via: submit_training_job
534	      wall_clock_seconds: 13475.7
535	      gpu_hours: 3.74
536	    status: DONE
537	    updated_at: '2026-05-14T04:43:58.619Z'
538	    reproduce:
539	      finished_at: '2026-05-14T04:42:48.051Z'
540	    conclusion: success
541	    metrics:
542	      mmlu: 0.5762
543	      gsm8k: 0.6331
544	      arc_challenge: 0.7662
545	      humaneval_pass@1: 0.1707
546	  exp_001_eval_15B_d000_s42:
547	    completed_at: '2026-05-14T00:23:17.209Z'
548	    conclusion: failed
549	    created_at: '2026-05-13T21:30:03.433Z'
550	    failure_reason: 卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path
551	      Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。
552	    hypothesis: 0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish
553	      ground-truth scores for calibration error computation
554	    parent: exp_001_sft_0pct_15B
555	    retry_count: 0
556	    spec:
557	      checkpoint_path: N/A
558	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/
559	      command: python evaluate.py --model-path Qwen2.5-1.5B --adapter-path lora_adapter
560	        --benchmarks mmlu gsm8k arc_challenge humaneval
561	      data_count: ~26000 items total
562	      data_path: MMLU/GSM8K/ARC-Challenge/HumanEval (HuggingFace datasets)
563	      eval_data: MMLU, GSM8K, ARC-Challenge, HumanEval (original)
564	      gpu:
565	      - cuda:4
566	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log
567	      model_name: Qwen2.5-1.5B + LoRA (d000_s42)
568	      output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42
569	      pid: '221376'
570	      seed: 42
571	      server: cqa1-21977
572	    status: DONE
573	    updated_at: '2026-05-14T00:23:17.209Z'
574	  exp_001_eval_15B_d000_s42_v2:
575	    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter
576	    completed_at: '2026-05-14T03:12:11.373Z'
577	    conclusion: success
578	    created_at: '2026-05-14T00:23:20.112Z'
579	    extra:
580	      hook_events:
581	      - action: agent
582	        event: on_complete
583	        ts: '2026-05-14T03:09:29.636850+00:00'
584	    log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log
585	    metrics:
586	      arc_challenge_accuracy: 0.7756
587	      arc_challenge_correct: 909
588	      arc_challenge_total: 1172
589	      gsm8k_correct: 840
590	      gsm8k_exact_match: 0.6368
591	      gsm8k_total: 1319
592	      humaneval_correct: 21
593	      humaneval_pass_at_1: 0.128
594	      humaneval_total: 164
595	      mmlu_accuracy: 0.5753
596	      mmlu_correct: 8079
597	      mmlu_total: 14042
598	    reproduce:
599	      finished_at: '2026-05-14T03:09:26.521Z'
600	    retry_count: 0
601	    spec:
602	      account: root
603	      backend: tmux
604	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter
605	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
606	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
607	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
608	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
609	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
610	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter
611	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks
612	        mmlu gsm8k arc_challenge humaneval"
613	      data_count: 26000
614	      data_path: mmlu,gsm8k,arc_challenge,humaneval
615	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
616	      gpu:
617	      - cuda:4
618	      gpu_hours: 2.81
619	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log
620	      model_name: Qwen2.5-1.5B
621	      pid: '243290'
622	      seed: 42
623	      server: cqa1-21977
624	      submitted_at: '2026-05-14T00:23:34.122Z'
625	      submitted_via: submit_training_job
626	      wall_clock_seconds: 10117.3
627	    status: DONE
628	    updated_at: '2026-05-14T03:12:11.373Z'
629	  exp_001_eval_3B_d000_s123:
630	    created_at: '2026-05-14T00:18:07.960Z'
631	    retry_count: 0
632	    spec:
633	      account: root
634	      backend: tmux
635	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter
636	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
637	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
638	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
639	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
640	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
641	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter
642	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks
643	        mmlu gsm8k arc_challenge humaneval"
644	      data_count: 26000
645	      data_path: mmlu,gsm8k,arc_challenge,humaneval
646	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
647	      gpu:
648	      - cuda:3
649	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log
650	      model_name: Qwen2.5-3B
651	      pid: '242581'
652	      seed: 123
653	      server: cqa1-21977
654	      submitted_at: '2026-05-14T00:18:36.008Z'
655	      submitted_via: submit_training_job
656	      wall_clock_seconds: 15706.2
657	      gpu_hours: 4.36
658	      checkpoint_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123
659	    status: DONE
660	    updated_at: '2026-05-14T04:44:59.509Z'
661	    reproduce:
662	      finished_at: '2026-05-14T04:39:50.139Z'
663	    extra:
664	      hook_events:
665	      - event: on_complete
666	        action: agent
667	        ts: '2026-05-14T04:39:53.713806+00:00'
668	    conclusion: success
669	    metrics:
670	      mmlu_accuracy: 0.6362
671	      gsm8k_exact_match: 0.1759
672	      arc_challenge_accuracy: 0.8294
673	      humaneval_pass_at_1: 0.0854
674	    checkpoint_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123
675	    completed_at: '2026-05-14T04:40:22.199Z'
676	  exp_001_eval_3B_d000_s42:
677	    completed_at: '2026-05-13T23:43:16.876Z'
678	    created_at: '2026-05-13T23:36:54.086Z'
679	    extra:
680	      previous_failure:
681	        conclusion: failed
682	        notes: v1 --gpu param caused evaluate.py crash. Resubmitted without --gpu.
683	      hook_events:
684	      - event: on_failed
685	        action: agent
686	        ts: '2026-05-14T06:47:56.373112+00:00'
687	    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
688	    hypothesis: 0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k,
689	      arc_challenge, humaneval) to establish ground-truth scores for calibration error
690	      computation
691	    notes: v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294
692	      confirmed running on GPU 1 (cron monitored).
693	    parent: exp_001_sft_0pct_3B
694	    retry_count: 1
695	    spec:
696	      account: root
697	      backend: tmux
698	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter
699	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
700	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
701	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
702	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
703	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
704	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter
705	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks
706	        mmlu gsm8k arc_challenge humaneval"
707	      data_count: 26000
708	      data_path: mmlu,gsm8k,arc_challenge,humaneval
709	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
710	      gpu:
711	      - cuda:1
712	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log
713	      model_name: Qwen2.5-3B
714	      pid: '249294'
715	      seed: 42
716	      server: cqa1-21977
717	      submitted_at: '2026-05-14T08:54:00Z'
718	    status: DONE
719	    updated_at: '2026-05-14T07:03:36.187Z'
720	    reproduce:
721	      finished_at: '2026-05-14T06:47:54.565Z'
722	    conclusion: success
723	    metrics:
724	      mmlu: 0.634
725	      gsm8k: 0.117
726	      arc: 0.822
727	      humaneval: 0.116
728	  exp_001_eval_3B_d000_s42_v2:
729	    conclusion: failed
730	    created_at: '2026-05-13T23:51:39.462Z'
731	    failure_reason: killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)
732	    retry_count: 0
733	    spec:
734	      account: root
735	      backend: tmux
736	      checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter
737	      command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh
738	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
739	        TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
740	        && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1
741	        && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path
742	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter
743	        --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks
744	        mmlu gsm8k arc_challenge humaneval"
745	      data_count: 0
746	      data_path: d000
747	      eval_data: mmlu,gsm8k,arc_challenge,humaneval
748	      gpu:
749	      - cuda:5
750	      hypothesis: 0% dosage 3B s42 baseline eval (v2, fix --gpu bug from v1). No --gpu
751	        param, use CUDA_VISIBLE_DEVICES via gpu_ids.
752	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_v2.log
753	      model_name: Qwen2.5-3B
754	      parent: exp_001_sft_0pct_3B
755	      pid: '237865'
756	      seed: 42
757	      server: cqa1-21977
758	      submitted_at: '2026-05-13T23:51:50.500Z'
759	      submitted_via: submit_training_job
760	    status: PREPARING
761	    updated_at: '2026-05-14T00:12:13.851Z'
762	  exp_001_eval_3B_d000_s42_v3:
763	    conclusion: killed
764	    created_at: '2026-05-14T00:48:57.772Z'
765	    hypothesis: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。
766	    retry_count: 0
767	    status: PREPARING
768	    updated_at: '2026-05-14T03:06:54.726Z'
769	  exp_001_sft_0pct:
770	    checkpoint_path: N/A (parent entry)
771	    completed_at: '2026-05-14T00:36:52.832Z'
772	    conclusion: success
773	    created_at: '2026-05-13T19:26:42.106Z'
774	    hypothesis: 0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish
775	      ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32
776	      1-epoch training on pure instruction data should preserve base model capability
777	    log_path: N/A (parent entry)
778	    notes: Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.
779	    retry_count: 0
780	    status: DONE
781	    updated_at: '2026-05-14T00:36:52.832Z'
782	  exp_001_sft_0pct_05B:
783	    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42
784	    completed_at: '2026-05-13T20:36:06.744Z'
785	    conclusion: success
786	    created_at: '2026-05-13T19:35:01.170Z'
787	    extra:
788	      hook_events:
789	      - action: agent
790	        event: on_complete
791	        ts: '2026-05-13T20:33:54.496690+00:00'
792	    log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log
793	    metrics:
794	      adapter_size_mb: 34
795	      checkpoint_size_mb: 166
796	      exit_code: 0
797	      final_loss: 1.4894
798	      mean_train_loss: 1.5388
799	      steps: 3125/3125
800	      token_accuracy: 0.682
801	      training_time_min: 52.9
802	    reproduce:
803	      finished_at: '2026-05-13T20:33:53.420Z'
804	    retry_count: 0
805	    spec:
806	      account: root
807	      backend: tmux
808	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
809	        base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false
810	        && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name
811	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl
812	        --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed
813	        42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache"
814	      gpu:
815	      - cuda:3
816	      gpu_hours: 0.98
817	      log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log
818	      pid: '208933'
819	      server: cqa1-21977
820	      submitted_at: '2026-05-13T19:37:23.024Z'
821	      submitted_via: submit_training_job
822	      wall_clock_seconds: 3523.7
823	    status: DONE
824	    updated_at: '2026-05-13T20:37:01.562Z'
825	  exp_001_sft_0pct_05B_s123:
826	    completed_at: '2026-05-13T22:30:25.819Z'
827	    conclusion: success
828	    created_at: '2026-05-13T20:35:04.879Z'
829	    hypothesis: 0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance
830	      estimation)
831	    metrics:
832	      token_acc: 0.676
833	      train_loss: 1.5393
834	      train_time_min: 54.5
835	    notes: OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)
836	    retry_count: 0
837	    spec:
838	      checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123
839	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
840	        base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false
841	        && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name
842	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl
843	        --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 --seed
844	        123 --gpu 1 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache"
845	      data_count: '50000'
846	      data_path: /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl
847	      gpu:
848	      - cuda:1
849	      log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log
850	      model_name: Qwen2.5-0.5B
851	      pid: '216033'
852	      seed: 123
853	      server: cqa1-21977
854	    status: DONE
855	    updated_at: '2026-05-13T22:30:25.819Z'
856	  exp_001_sft_0pct_15B:
857	    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42
858	    completed_at: '2026-05-13T21:27:59.348Z'
859	    conclusion: success
860	    created_at: '2026-05-13T19:39:48.369Z'
861	    extra:
862	      hook_events:
863	      - action: agent
864	        event: on_complete
865	        ts: '2026-05-13T21:25:42.551081+00:00'
866	    log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log
867	    metrics:
868	      adapter_size_mb: 71
869	      checkpoint_size_mb: 313
870	      exit_code: 0
871	      final_loss: 1.2039
872	      mean_train_loss: 1.2599
873	      steps: 3125/3125
874	      token_accuracy: 0.711
875	      training_time_min: 101.5
876	    reproduce:
877	      finished_at: '2026-05-13T21:25:40.979Z'
878	    retry_count: 0
879	    spec:
880	      account: root
881	      backend: tmux
882	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
883	        base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false
884	        && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name
885	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl
886	        --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42 --seed
887	        42 --gpu 4 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache"
888	      gpu:
889	      - cuda:4
890	      gpu_hours: 1.78
891	      log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log
892	      pid: '210116'
893	      server: cqa1-21977
894	      submitted_at: '2026-05-13T19:41:11.760Z'
895	      submitted_via: submit_training_job
896	      wall_clock_seconds: 6407.6
897	    status: DONE
898	    updated_at: '2026-05-13T21:27:59.348Z'
899	  exp_001_sft_0pct_15B_s123:
900	    completed_at: '2026-05-13T22:30:26.882Z'
901	    conclusion: success
902	    created_at: '2026-05-13T20:35:07.346Z'
903	    hypothesis: 0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance
904	      estimation)
905	    metrics:
906	      token_acc: 0.731
907	      train_loss: 1.2602
908	      train_time_min: 101.5
909	    notes: OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)
910	    retry_count: 0
911	    spec:
912	      checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123
913	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
914	        base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false
915	        && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name
916	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl
917	        --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 --seed
918	        123 --gpu 2 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache"
919	      data_count: '50000'
920	      data_path: /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl
921	      gpu:
922	      - cuda:2
923	      log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log
924	      model_name: Qwen2.5-1.5B
925	      pid: '216111'
926	      seed: 123
927	      server: cqa1-21977
928	    status: DONE
929	    updated_at: '2026-05-13T22:30:26.882Z'
930	  exp_001_sft_0pct_3B:
931	    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42
932	    completed_at: '2026-05-13T23:25:49.016Z'
933	    conclusion: success
934	    created_at: '2026-05-13T19:44:40.471Z'
935	    extra:
936	      hook_events:
937	      - action: agent
938	        event: on_complete
939	        ts: '2026-05-13T23:23:43.393661+00:00'
940	    log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log
941	    metrics:
942	      adapter_size_mb: 115
943	      checkpoint_size_mb: 488
944	      exit_code: 0
945	      final_loss: 1.0736
946	      mean_train_loss: 1.1306
947	      steps: 3125/3125
948	      token_accuracy: 0.734
949	      training_time_min: 214.7
950	    reproduce:
951	      finished_at: '2026-05-13T23:23:41.844Z'
952	    retry_count: 0
953	    spec:
954	      account: root
955	      backend: tmux
956	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
957	        base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false
958	        && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name
959	        /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl
960	        --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed
961	        42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache"
962	      gpu:
963	      - cuda:5
964	      gpu_hours: 3.69
965	      log_path: ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log
966	      pid: '210666'
967	      server: cqa1-21977
968	      submitted_at: '2026-05-13T19:44:40.431Z'
969	      submitted_via: submit_training_job
970	      wall_clock_seconds: 13268.6
971	    status: DONE
972	    updated_at: '2026-05-13T23:25:49.016Z'
973	  exp_001_sft_0pct_3B_s123:
974	    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123
975	    completed_at: '2026-05-14T00:23:18.290Z'
976	    conclusion: success
977	    created_at: '2026-05-13T20:39:01.606Z'
978	    extra:
979	      hook_events:
980	      - action: agent
981	        event: on_complete
982	        ts: '2026-05-14T00:16:17.727184+00:00'
983	    hypothesis: 0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance
984	      estimation)
985	    metrics:
986	      adapter_model_mb: 114
987	      adapter_size_mb: 488
988	      checkpoint_size_mb: 488
989	      epochs: 1
990	      final_loss: 1.114
991	      mean_token_accuracy: 0.7505
992	      mean_train_loss: 1.1309
993	      steps_completed: 3125
994	      total_steps: 3125
995	      total_tokens: 19555717
996	      train_samples_per_second: 3.91
997	      training_time_min: 213.1
998	    notes: OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h
999	    reproduce:
1000	      finished_at: '2026-05-14T00:16:04.357Z'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff62fe8e-97d0-4526-aa90-d79a06e26e4b",
  "isSidechain": true,
  "promptId": "4e24b74c-d2c2-4f4f-949e-34c5ee055272",
  "agentId": "a7ae2a5850e7251d8",
  "type": "user",
  "uuid": "ec8c6cc5-dbf3-4964-ae16-d226fe7d9563",
  "sourceToolAssistantUUID": "ff62fe8e-97d0-4526-aa90-d79a06e26e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T16:06:34.665Z_

Due to the size limitations, let me provide you with a comprehensive summary of the project files I've successfully read:

## Summary of Project Files Read

### 1. **report.md** (Lines 1-57)
Auto-generated handover report updated 2026-05-14. Shows:
- **Running experiments**: exp_005_noise_prop_v3, exp_001_sft_d025_15B, exp_001_eval_3B_d005_aligned
- **Pending tasks**: Multiple eval variants (d005, d100, d000 at different scales) in preparation
- **Recent conclusions**: Successful evals on 0.5B-d000-s123, 0.5B-d005, 3B-d100. Multiple failures documented
- **Status**: 33 successes, 0 negative results, 15 failed experiments out of 50 total
- **GPU resource**: cqa1-21977 server with 6 RTX 4090D GPUs

### 2. **ROADMAP.md** (Lines 1-96)
Detailed research roadmap and progress tracking:
- **Submission target**: EMNLP 2026 ARR May 25 (11 days away from 2026-05-14)
- **Core direction**: ContamCal — post-hoc statistical calibration via contamination-augmented 4PL IRT
- **Phase completion**:
  - Phase 1 (Paraphrase): 100% complete
  - Phase 2 (Data preparation): 100% complete
  - Phase 3 (SFT): Multiple scale/dosage combinations in progress; critical path shows d025 0.5B as P2 priority
  - Phase 4 (Eval): 2 complete, 7 running
- **Critical path**: exp-002 code completion (highest priority), followed by 0.5B eval completion, then exp-003 RRF → exp-006 IRT calibration
- **Key decisions logged**: D019-D010 with dates and experiment linkages
- **GPU budget**: 6/6 GPUs fully allocated; tight but achievable timeline

### 3. **memory.md** (Lines 1-194)
Institutional knowledge and operational lessons learned:
- **🔴 Critical issues resolved**:
  - Local vs remote experiment monitoring (two incidents of misclassification)
  - CUDA_VISIBLE_DEVICES override bug fixed (GPU binding errors)
  - MC evaluation format conflict (training/eval mismatch with answer formats)
  - Cron false positives (wrapper vs actual process PID)
  - AutoDL eval template standardized
  - 3B GSM8K collapse root cause: LoRA SFT CoT forgetting (excluded from dose-response)
  
- **Discoveries**: HumanEval not in contamination data; it's a non-contaminated control benchmark
- **Phase 3 GPU priorities**: Each model size first runs extreme dosages (d005, d100), then fills d025
- **Baseline experimental results table**: Aligned format results compiled with success status
- **Code readiness**: exp-008 100% ready (dry-run passed); exp-003 RRF 95%; exp-006 IRT 95%

### 4. **experiment_plan.yaml** (Lines 1-277)
Structured experiment definitions mapping to paper claims:
- **exp-001** (P0): Controlled SFT injection on 0.5B/1.5B/3B at 5 dosage levels; registry_id tracking
- **exp-002** (P0): Signal pipeline (embedding, Min-K++, ConStat, Self-Critique)
- **exp-003** (P0): RRF aggregation & ablations
- **exp-004** (P0, CPU): 144-condition simulation sweep (AUC × N_models × prior strength); 27/120 complete, running
- **exp-005** (P0, CPU): Noise propagation analysis with measurement error model; v3 active
- **exp-006** (P0): IRT calibration + 7 baselines; 95% code ready
- **exp-008** (P0): Signal survival analysis; 100% code ready, dry-run passed
- **exp-007, exp-014, exp-015** (P1): Scale validation (7B), multi-family, QC-only ablation
- **GPU budget**: 90h P0, 60h P1, 20h P2, 30h buffer = 200h total
- **Multi-seed protocol**: 3 seeds for exp-001/006, 10 for simulations

### 5. **paper_framing.md** (Lines 1-105)
Paper positioning and methodological framework:
- **Core insight**: Post-hoc statistical calibration instead of mitigation (Emperor's New Clothes showed 20 strategies all fail)
- **3 core claims**:
  1. Contamination-augmented 4PL IRT recovers true performance with MAE improvement & nominal coverage
  2. Signal degradation under RL is cliff-like; RRF avoids meta-circularity
  3. Measurement error modeling propagates detection uncertainty into CIs automatically
  
- **Venue fit**: EMNLP primary (special theme on contamination/governance); AAAI/ICLR fallback
- **Benchmarks**: MMLU, GSM8K, ARC-Challenge (main); HumanEval appendix-only (low paraphrase QC rate ~16%)
- **Baselines**: 7 total (Raw, Remove-Rescore, Single-Signal-2PL, Vanilla-4PL, Linear-Regression, Emperor's-Mitigation, DCR)
- **Evaluation metrics**: 5 metrics — calibration error (MAE), interval coverage, sharpness, Kendall-τ, dose-response monotonicity
- **Anticipated concerns**: 12 reviewer concerns with defenses mapped to experiments
- **Required figures**: Pipeline diagram, Signal×Regime AUC heatmap, Dose-response curves, Identifiability phase diagram, Calibrated-vs-true scatter

### 6. **registry.yaml** (First 1000 lines visible)
Experiment execution log with detailed metadata:
- Tracks 50+ experiment runs with status (DONE, PREPARING, RUNNING)
- Each entry includes: checkpoint paths, metrics, GPU allocation, command specs, wall-clock time, conclusion
- Examples of successful evals: 0.5B-d000-s123 (MMLU 0.4182, GSM8K 0.3404, ARC 0.3976, HumanEval 0.1037)
- Documents failure modes: OOM kills (SIGKILL 137), relative path issues, network timeouts
- Contains extensive notes on diagnosis and fixes for each iteration

## Overall Project State

**Status**: Late-stage research (MVP completed 2026-05-13, review underway). The project is on a tight 11-day sprint to EMNLP ARR deadline.

**Bottleneck**: Software (exp-002 signal pipeline + exp-006 baselines code completion) rather than compute. All 6 GPUs allocated; experiments queued.

**Key achievements**: Phase 3 SFT producing good dose-response intermediate points; paraphrase data fully prepared; Stan model converging well on simple IRT formulation.

**Next critical steps** (from ROADMAP):
1. Complete exp-002 signal pipeline code + dry-run
2. Complete 0.5B aligned eval results
3. Run exp-002 signals on {d000, d005, d100}
4. Parallelize exp-003 (RRF) + exp-006 (IRT calibration)
5. Prioritize 0.5B d025 SFT + eval for full dose-response curve

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec8c6cc5-dbf3-4964-ae16-d226fe7d9563",
  "isSidechain": true,
  "agentId": "a7ae2a5850e7251d8",
  "requestId": "req_011Cb2kK7xxTTN5rk35JQgaP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6531d53-9c88-4b14-8665-faf73080428d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5d7b8dad",
  "sessionId": "7b8087ba-fe57-4650-8b0d-a27a973e3984",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LP7HAkKVk6YBMzv9iLQcbp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 20355,
      "cache_read_input_tokens": 54332,
      "output_tokens": 1869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20355
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1869,
          "cache_read_input_tokens": 54332,
          "cache_creation_input_tokens": 20355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20355,
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
