# Research conversation: Read all review report files in /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-adc40b630705b75d4.jsonl`
- **Structured JSON:** [`3b52767b1de9307c74df.json`](../../sessions/3b/3b52767b1de9307c74df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-23T14:17:10.232Z_

Read all review report files in /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/ (round_0.md through round_16.md). For each round, extract:
1. The overall score (usually expressed as X/5 or X.X/5)
2. The review mode (fresh vs continue)
3. The top 2-3 most critical issues raised
4. Whether the score went up, down, or stayed the same vs previous round

Present all this as a compact table. Read each file but focus on the summary/score section at the top of each report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "ee90f85d-decc-44a0-a9ac-ce0642a67f52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T14:17:12.080Z_

I'll read all the review report files and extract the key information for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee90f85d-decc-44a0-a9ac-ce0642a67f52",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHKssWZg92GqXQGdWS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a56fd9db-cff5-4423-a80a-31b93eb0df97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7daHbvoGGK8mVcQT6VSHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37312,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37312,
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

_source line 3 · 2026-05-23T14:17:12.238Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PotzsjvKFsBM8wNfujzE8u`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a56fd9db-cff5-4423-a80a-31b93eb0df97",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHKssWZg92GqXQGdWS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c9e7fe05-a829-41c4-9d18-a65fdbf913ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7daHbvoGGK8mVcQT6VSHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37312,
      "cache_read_input_tokens": 0,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37312,
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

_source line 4 · 2026-05-23T14:17:12.413Z_

<details><summary>↩ Tool result · `toolu_01PotzsjvKFsBM8wNfujzE8u`</summary>

```text
total 312
drwxr-xr-x  2 ubuntu ubuntu  4096 May 23 14:07 .
drwxr-xr-x 64 ubuntu ubuntu 12288 May 23 14:04 ..
-rw-r--r--  1 ubuntu ubuntu 11085 May 17 17:54 round_0.md
-rw-r--r--  1 ubuntu ubuntu 13704 May 18 01:49 round_1.md
-rw-r--r--  1 ubuntu ubuntu 16183 May 22 08:01 round_10.md
-rw-r--r--  1 ubuntu ubuntu 16173 May 22 13:40 round_11.md
-rw-r--r--  1 ubuntu ubuntu 15617 May 23 00:52 round_12.md
-rw-r--r--  1 ubuntu ubuntu 20615 May 23 08:27 round_13.md
-rw-r--r--  1 ubuntu ubuntu 15694 May 23 09:39 round_14.md
-rw-r--r--  1 ubuntu ubuntu 16541 May 23 10:30 round_15.md
-rw-r--r--  1 ubuntu ubuntu 19537 May 23 14:07 round_16.md
-rw-r--r--  1 ubuntu ubuntu 11519 May 19 05:12 round_2.md
-rw-r--r--  1 ubuntu ubuntu 17577 May 20 13:21 round_3.md
-rw-r--r--  1 ubuntu ubuntu 17871 May 20 15:17 round_4.md
-rw-r--r--  1 ubuntu ubuntu 15543 May 20 20:08 round_5.md
-rw-r--r--  1 ubuntu ubuntu 14354 May 21 01:59 round_6.md
-rw-r--r--  1 ubuntu ubuntu 13998 May 21 06:51 round_7.md
-rw-r--r--  1 ubuntu ubuntu 16747 May 21 08:03 round_8.md
-rw-r--r--  1 ubuntu ubuntu 18698 May 22 01:20 round_9.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9e7fe05-a829-41c4-9d18-a65fdbf913ef",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "cc5c0744-7928-4c2a-b109-9db6c1e5cd97",
  "sourceToolAssistantUUID": "c9e7fe05-a829-41c4-9d18-a65fdbf913ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T14:17:13.773Z_

Now I'll read each round file to extract the scores and critical issues. Let me start with all the rounds:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc5c0744-7928-4c2a-b109-9db6c1e5cd97",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0379335f-192d-40e5-ab17-6bcdd0f4e779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

_source line 6 · 2026-05-23T14:17:14.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_011349dB4rCVQwMQ2arWdbLH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_0.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0379335f-192d-40e5-ab17-6bcdd0f4e779",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "adf25703-4e78-4e28-9f78-1be6912fe72c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

### Tool result

_source line 7 · 2026-05-23T14:17:14.738Z_

<details><summary>↩ Tool result · `toolu_011349dB4rCVQwMQ2arWdbLH`</summary>

```text
1	---
2	round: 0
3	overall_score: 2.5 - Borderline Findings (Resubmit next cycle)
4	timestamp: 2026-05-17T17:54:16.039955+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 1
11	**项目**: symb_invariant_consensus
12	**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)
13	**日期**: 2026-05-17
14	**Reviewer 配置**: R1（方法+实验）+ R2（新颖性+相关工作）
15	
16	---
17	
18	## Summary
19	
20	论文研究 self-extracted symbolic constraints（FOL formalization + MAX-SAT aggregation）能否改善 LLM majority voting (Self-Consistency)。核心发现是 "capability trap"：模型自身能力限制了约束质量，导致 self-extracted SICA 在大部分条件下无法超越 SC。论文定义了 C0-precision 诊断框架并给出部署建议。
21	
22	---
23	
24	## Strengths
25	
26	1. **研究问题有实际意义** — Practitioners 确实需要知道何时值得为 SC 增加 symbolic aggregation overhead [R1, R2 共识]
27	2. **Constraint ablation 设计精巧** — Table 2 的 MAX-SAT ≡ count-only ≡ random-weight（803/804 agreement）干净地验证了 constraints 无区分力 [R1]
28	3. **Capability trap 概念框架清晰** — Diversity vs quality tradeoff 叙事连贯 [R1, R2]
29	4. **Overhead analysis 务实** — 报告 wall-time 和 cost multiplier，对 practitioner 有参考价值 [R1]
30	5. **Negative result paper 结构完整** — Motivation → Method → Evaluation → Failure analysis → Diagnostic 逻辑线条清楚 [R1, R2]
31	
32	---
33	
34	## Weaknesses (Critical — 影响接收决定)
35	
36	### W-C1: Method Section Stage 3 完全未描述 [R1-N1, R2 AGREE]
37	- `sat(a, c_{i,j}) ∈ {0,1}` 的实现方式未说明：LLM 调用？FOL solver model checking？字符串匹配？
38	- 这是 pipeline 核心步骤，直接决定 constraint precision 度量方式
39	- 如果 sat() 由 LLM 完成，overhead 分析 (Table 4) 漏算 O(|C|·|A|) 次调用
40	- **影响**: 方法不可复现，整个 precision 分析的度量基础不明
41	
42	### W-C2: 大部分实验严重 underpowered [R1-N2, R2 强烈 AGREE]
43	- Table 1 的 11 行中 8 行 n≤60
44	- McNemar's test 在 n=60 时检测 3-5pp 差异的 power 仅约 15-20%
45	- 论文从未报告 power analysis
46	- 核心贡献是 negative result，无法排除 Type II error（"no significant effect" ≠ "no effect"）
47	- **影响**: 论文的 negative conclusion 的统计基础不成立
48	
49	### W-C3: Oracle/upper-bound 实验完全缺失 [R1-N6, R2 AGREE 并更正自身]
50	- 论文声称 capability trap 根源是 self-extracted constraints precision ≈ 0.50
51	- 未通过 gold FOL constraints 验证："好的 constraints 是否真能帮 MAX-SAT 超越 SC？"
52	- 无法区分 H1（self-extracted constraints 太差）vs H2（MAX-SAT 框架本身无效）
53	- FOLIO 原始数据集带 gold FOL 标注，此实验完全可行
54	- **影响**: 论文的整个 "capability trap" 因果叙事缺少关键控制实验
55	
56	### W-C4: 与 Huang et al. (ICLR 2024) 严重 novelty 重叠且未引用 [R2-N1, R1 AGREE]
57	- "LLMs Cannot Self-Correct Reasoning Yet" 已证明 LLMs 在无外部反馈时无法可靠自我纠正
58	- "Capability trap" 本质上是 correlated error problem 在 symbolic constraint extraction 场景的特化
59	- 论文未引用、未区分、未讨论增量
60	- R1 补充：SICA 引入了 FOL+MAX-SAT 结构化中间层，这是可论证的差异点，但论文需要明确 position
61	- **影响**: 核心 novelty claim 可能已被覆盖
62	
63	### W-C5: 关键相关工作大面积缺失 [R2-N2, R1 AGREE 并修正]
64	- 缺失：Huang et al. 2024、"Two Failures of Self-Consistency" (EMNLP 2024)、"Self-Consistency Falls Short" (TACL 2025)、"Beyond Majority Voting" (2025)、"Reasoning Aware Self-Consistency" (NAACL 2025)
65	- R1 修正：FOLIO 原始论文 Han et al. 2022 实际已被引用；实际引用量 ~30 篇（非 R2 初评的 ~18 篇）
66	- 但 SC 失败模式、self-correction 局限性、aggregation 替代方法三个子话题完全空白
67	- **影响**: 审稿人会认为对领域 landscape 理解不充分
68	
69	### W-C6: "18 experimental conditions" 无法验证 [R1-N3, R2 AGREE]
70	- Table 1 仅 11 行，最大合理拆分后为 13 个
71	- 达到 18 需将 n=60 pilot 的子域各算独立条件（n≈20/domain）
72	- 进一步恶化 W-C2 的 power 问题
73	- **影响**: 核心数字不透明，meta-level 分析自由度存疑
74	
75	### W-C7: Introduction 列出 Mistral-7B 但全文无结果 [R1-N4, R2 AGREE]
76	- Section 1 L59 列出 5 个 model families 含 Mistral-7B
77	- 实际实验中无 Mistral 数据
78	- 明显的 draft 残留错误
79	- **影响**: 损害论文可信度，暗示结果可能被选择性删除
80	
81	### W-C8: Abstract Δ 范围与 Table 1 矛盾 [R1-N5, R2 AGREE]
82	- Abstract: "−3.3pp to +2.0pp"，Table 1: StrategyQA Δ=+3.33pp
83	- 事实性错误
84	- **影响**: 对论文其他数字准确性产生系统性怀疑
85	
86	### W-C9: Capability Trap 概念独立贡献不清晰 [R2-N3, R1 部分 AGREE]
87	- 四个子组件单独来看均非新洞察
88	- 组合增量主要是量化（阈值数字），但 n=30-60 样本量不足以支撑精确阈值
89	- R1 归因为 soundness 问题（量化基础不扎实），R2 归因为 novelty 问题（概念非新）
90	- **影响**: 核心 framing 需要在已有知识之上提供更清晰的增量
91	
92	---
93	
94	## Weaknesses (Warning — 影响评分但不一票否决)
95	
96	1. **Constraint extraction prompt 完全缺失** — 核心方法环节无法复现 [R1-W1, R2 AGREE]
97	2. **Temperature τ 未指定** — 影响 C0 和 SC baseline 强度 [R1-W2, R2 AGREE]
98	3. **LLaMA-8B 行缺少绝对 accuracy** — 无法判断 Δ 的实际意义 [R1-W3, R2 AGREE]
99	4. **Confidence intervals 未展示** — negative result paper 中 CI 比 p-value 更重要 [R1-W4, R2 AGREE]
100	5. **Constraint precision 分析仅 Qwen-14B** — precision>0.6 阈值的泛化性未验证 [R1-W5, R2 AGREE]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adf25703-4e78-4e28-9f78-1be6912fe72c",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "441fa07f-5a1f-49dd-bc6c-2557ed2cec56",
  "sourceToolAssistantUUID": "adf25703-4e78-4e28-9f78-1be6912fe72c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T14:17:15.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PFR3YEWhuBnewRan4SexSw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_1.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "441fa07f-5a1f-49dd-bc6c-2557ed2cec56",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4ef22091-08d4-48c1-9ec3-6b13a81dd3cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

### Tool result

_source line 9 · 2026-05-23T14:17:15.075Z_

<details><summary>↩ Tool result · `toolu_01PFR3YEWhuBnewRan4SexSw`</summary>

```text
1	---
2	round: 1
3	overall_score: 3.0 - Findings
4	timestamp: 2026-05-18T01:49:05.406319+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	
11	# 审稿报告：The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting
12	
13	**目标 venue**: EMNLP 2026 (ARR May cycle)
14	**审稿轮次**: Round 2（论文修订后重新审稿）
15	**Reviewer 编排**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性）
16	**交叉分享**: 完成，两位 Reviewer 均提交了逐条回应
17	
18	---
19	
20	## Summary
21	
22	本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理轨迹中自提取 FOL 约束，通过 weighted partial MAX-SAT 聚合答案，旨在改进 Self-Consistency (SC) 的多数投票。在 6 个模型（7B-32B）、3 个推理领域、超过 1,500 个实例上，SICA 相比 SC 无统计显著提升（Δ 范围 -3.3 至 +3.3 pp）。Oracle 实验用 gold FOL 注释替代自提取，获得 +8.82 pp（p < 0.001），证明聚合机制本身有效，瓶颈在自提取质量。作者将此命名为"capability trap"，提出 C0 诊断指标作为从业者工具。
23	
24	---
25	
26	## Strengths
27	
28	**S1. Oracle control 实验设计精巧 [R1, R2 共识]**
29	通过 component-level intervention 隔离自提取质量与聚合机制，遵循 Press et al. (2023)、Trivedi et al. (2023) 的 established methodology。+8.82 pp 的显著提升（McNemar p = 6.15e-5）是全文最有力的证据，方法论设计值得肯定。
30	
31	**S2. 统计方法严谨完整 [R1, R2 共识]**
32	McNemar test + 10,000 次 bootstrap CI + power analysis（MDE 计算）构成三层统计论证链。n≤60 条件明确标注为 exploratory。这对负面结果论文尤为重要。
33	
34	**S3. Constraint ablation 有说服力 [R1, R2 共识]**
35	MAX-SAT vs count-only 在 804 个预测中一致 803 个（Table 2），直接证明满足性求解器退化为计数。Random-weight 变体进一步确认约束无判别信号。
36	
37	**S4. C0 diagnostic 有实用价值 [R1, R2 共识]**
38	定义简洁，零成本可计算，双向论证完整（低 C0 退化 + 高 C0 不保证改进）。QwQ-32B C0=2.6% vs DeepSeek-R1-7B C0=58.3% 的对比清晰展示 reasoning model 特殊行为。
39	
40	**S5. Limitations section 诚实全面 [R1]**
41	列出 7 项具体限制，未过度推广结论。
42	
43	**S6. 写作质量整体较高 [R2]**
44	Abstract 简洁回答四个核心问题，Introduction 叙事线完整，Related Work 6 段分类合理、positioning 诚实。
45	
46	---
47	
48	## Weaknesses
49	
50	### Must-Fix（3 项）
51	
52	**W1. σ(c, a) 的 Z3 评估机制描述不完整，影响 soundness 判断 [R1 提出, R2 AGREE]**
53	- Section 3.3 Eq.(2) 定义 σ(c, a) 为"Z3 determines: σ(c, a) = 1 if constraint c is satisfiable under the assignment implied by answer a"，但未具体说明 answer a 如何为 Z3 创建 variable assignment。
54	- Appendix 的 prompt 显示 domain constraints 使用独立变量（如 kind_anne），answer assertion 使用独立变量（__sica_answer_True）。如果两者无逻辑桥接，则 σ(c, a) = 1 对所有 a 恒成立，SICA 在数学上严格退化为 SC。
55	- R2 进一步指出：803/804 agreement 恰好验证了这一假设。如果退化是 mechanism 设计问题而非 model capability 问题，则"capability trap"的归因需要重新定义。
56	- **影响**: 这是 soundness 核心问题。无法判断论文的核心发现是"模型无法产生 discriminative constraints"还是"评分机制设计上就无法利用 constraints 进行区分"。
57	- **要求**: 补充完整的 Z3 evaluation 流程伪代码，明确 domain constraint 变量和 answer 变量之间的关系。
58	
59	**W2. Oracle 实验仅限 FOLIO 单一数据集（n=204），因果论证的外部效度不足 [R1, R2 共识]**
60	- 核心因果论证完全依赖 FOLIO 一个数据集的 oracle 实验。
61	- FOLIO 是形式逻辑领域，约束天然以 FOL 表达。对 commonsense（StrategyQA）或 science（ARC）域的 constraint extraction 能否同样受益于 oracle 完全未知。
62	- "the aggregation mechanism is sound" 的一般性结论由单数据集 oracle 支撑不足。
63	- ProofWriter 也有结构化 proof chain 和 ground-truth labels，理论上可以构造 oracle constraints。
64	- **要求**: 至少增加一个域的 oracle 验证（如 ProofWriter），或将 claim 范围限定为 formal logic。
65	
66	**W3. 核心概念"Capability Trap"与已有工作重叠，新颖性不足 [R2 Must-Fix, R1 Should-Fix]**
67	- "同一模型无法有效验证/纠正自身推理"已被以下工作明确建立：
68	  - Huang et al. (ICLR 2024): LLM 在无外部反馈时无法自纠错
69	  - **Stechly, Valmeekam & Kambhampati (ICLR 2025)**: self-verification 导致性能崩溃，sound external verification 有效，self-generated critique 内容无实质影响。这与本文发现结构同构。
70	- R1 认为可降为 Should-Fix，理由是本文的实证贡献（oracle 设计、ablation、C0）独立于概念命名。R2 认为概念层面的重叠构成对 main conference 接收的实质障碍。
71	- **Director 判断**: 作为 Findings track 论文，实证贡献可成立。但必须引用 Stechly et al. 并明确差异化（NL self-critique vs formal constraint extraction + satisfiability solving）。
72	
73	### Should-Fix（7 项）
74	
75	**W4. 手动约束质量分析样本过小 [R1, R2 共识]**
76	- 11.5% discriminative rate 来自 43 problems（23 multi-candidate），仅覆盖 Qwen2.5-14B 在 FOLIO+PW 上。该数字在 Abstract/Intro/Conclusion 均被引用作为核心证据，但 CI 极宽。
77	- 建议扩大到 100+ 问题覆盖多模型，或设计自动化指标，或限定 claim 范围。
78	
79	**W5. 7/11 conditions n≤60，广度声称需更审慎 [R1, R2 共识]**
80	- 真正 confirmatory 的仅 3 组分析（n=804, n=200, n=204）。
81	- LLaMA StrategyQA 95% CI 上界 +5.5pp，无法排除 practically meaningful 正向效应。
82	- Abstract/Conclusion 中"across six models and three domains"措辞需区分 confirmatory 和 exploratory evidence。
83	
84	**W6. 未测试替代提取策略 [R1, R2 共识]**
85	- 仅使用单一 zero-shot prompt + T=0.1 提取约束。
86	- "Cannot improve"的标题级 claim 需至少排除 few-shot extraction 等替代方案。
87	- Limitations §5 承认但未尝试，对负面结果论文来说是显著缺陷。
88	
89	**W7. "Five model families"表述有误导性 [R1, R2 共识]**
90	- QwQ-32B、Qwen2.5、DeepSeek-R1-Distill-Qwen-7B 均基于 Qwen 架构。
91	- 实际独立架构可能仅 3 个（Qwen 系、Mistral、LLaMA）。
92	- 需区分 architecture family 与 release/training family。
93	
94	**W8. Related Work 遗漏关键引用 [R1, R2 共识]**
95	- **Stechly et al. (ICLR 2025)** "On the self-verification limitations of LLMs on reasoning and planning tasks": 最直接的先行工作，必须引用。
96	- Ai et al. (2025) "Beyond Majority Voting": 不依赖形式化的 aggregation 改进。
97	- Valmeekam et al. (2023) "Can LLMs Really Improve by Self-Critique?": self-refinement 负面结果。
98	- Beirami et al. (2024): Best-of-N / reward model reranking。
99	
100	**W9. StrategyQA/ARC extraction prompt 未在 Appendix 文档化 [R2 提出, R1 AGREE]**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ef22091-08d4-48c1-9ec3-6b13a81dd3cc",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "3ea58400-eb9c-45a4-823a-b4b0913bbf13",
  "sourceToolAssistantUUID": "4ef22091-08d4-48c1-9ec3-6b13a81dd3cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T14:17:15.284Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FDnQfk5YFrnJD3ptatzijP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_2.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ea58400-eb9c-45a4-823a-b4b0913bbf13",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "07b71a83-66a6-4423-9283-fde65f662928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

### Tool result

_source line 11 · 2026-05-23T14:17:15.292Z_

<details><summary>↩ Tool result · `toolu_01FDnQfk5YFrnJD3ptatzijP`</summary>

```text
1	---
2	round: 2
3	review_mode: 
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-19T05:12:50.407694+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: True
9	---
10	
11	# 圆桌审稿报告 — Round 4 (Final, Revised Paper)
12	
13	**论文**: Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning
14	**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**审稿模式**: 重新审稿（Fresh）— 修订版论文全文独立评审
16	
17	---
18	
19	## 审稿人配置与流程
20	
21	| Reviewer | 类型 | 侧重 | 初审评分 |
22	|----------|------|------|---------|
23	| R1 | Dream | 方法+实验严谨性 | 3/6 (Borderline Reject, 6分制) |
24	| R2 | Agent | 新颖性+完整性+写作质量 | **3.5/5 (Borderline Conference, ARR标准)** |
25	
26	**流程**：R1 + R2 独立初审 → Director 对 R1 全部 claim 独立验证（发现多处与实际论文不符）→ R1 验证后发现 + Director 独立发现交叉分享给 R2 → R2 逐条回应（7/7 AGREE）→ 完全收敛。
27	
28	---
29	
30	## ⚠️ Director 独立验证：Dream R1 版本偏差
31	
32	Dream R1 的多个 critical claim 与实际论文不符：
33	
34	| R1 声称 | 实际状态 | 判定 |
35	|---------|---------|------|
36	| MAX-SAT scoring function 未形式化定义 | Eq.(2)-(4) + Alg 1-2 完整 | **不正确** |
37	| Oracle 仅 1 数据集 | FOLIO + ProofWriter 双 Oracle | **不正确** |
38	
39	R2 (Agent) 的审稿与实际论文完全一致，确认了 ~50 篇引用、完整形式化、双 Oracle、全面 Related Work 等。**本报告以 R2 的准确评估为主体，仅保留 R1 经验证后成立的发现。**
40	
41	---
42	
43	## Summary
44	
45	论文评估 SICA，一个从 LLM reasoning traces 提取 FOL 式约束并通过 MAX-SAT 聚合答案的管线。在 7 个模型（7B-32B）、4 个推理域、2400+ 实例上系统测试，发现 SICA 仅在窄带（SC ~50-55%）内有正面趋势，提出 Type A/B/C 三种失败模式。双 Oracle 控制（FOLIO +14.22pp, ProofWriter +11.50pp, 均 p<0.001）因果定位瓶颈在约束提取质量。CJT/Eff-K 框架量化 trace 相关性。Entropy-conditioned mechanism 解释微观作用路径。9 种 remediation 策略全部失败。
46	
47	---
48	
49	## Strengths
50	
51	**S1: 实验覆盖面与系统性。** 7 模型 × 4+ 域 × 14 非 Oracle 条件 + 2 Oracle 条件 + 3-seed 复制。覆盖面远超同类负面结果论文。
52	
53	**S2: 双 Oracle 控制设计精巧。** FOLIO（gold FOL）+ ProofWriter（gold DSL）双独立数据集，产生 +14.22pp (p=2.0×10⁻⁷) 和 +11.50pp (p=9.21×10⁻¹⁵)。ProofWriter 的 per-subtype breakdown（RelNeg +17.86pp > AttNoneg +9.09pp）提供额外粒度。这是论文最有说服力的贡献。
54	
55	**S3: Entropy-conditioned mechanism 是最有价值的新贡献。** （R2 特别强调）SICA gains 集中于 high-entropy 问题（+9.6pp, n=73），aggregate effect 取决于高 entropy 问题比例（Mistral 35.8% vs Qwen 10.3%）。Qwen2.5-14B 在高 entropy subgroup 内也达 +4.8pp 但 aggregate 仅 -0.49pp 因 subgroup 太小。这 elegant 地解释了 regime 依赖于模型强度的原因。
56	
57	**S4: 约束消融干净利落。** MAX-SAT vs count-only 803/804 一致，直接证明 Z3 solver 退化为加权计票。
58	
59	**S5: Variable naming inconsistency 的具体发现（56.4% cross-answer constraint pairs share zero Z3 variables）** 提供了 mechanistic insight：Z3 无法从不相关符号集中发现逻辑关系。
60	
61	**S6: Type C（error amplification, Δ=−2.83pp, p=0.0095）是新发现**，提供了 SICA 何时 actively harm 的边界条件。
62	
63	**S7: 形式化完整。** 5 equations, 2 algorithms, full prompts, α=0.5 explicit。
64	
65	**S8: 文献覆盖充分（~50 引用）。** Related Work 5 段覆盖所有主要研究线。关键先行工作均已引用并 positioned。
66	
67	**S9: 写作质量好，无 AI 痕迹**（R2 独立验证：零 em-dash，零黑名单词汇，零 -ing phrase endings）。
68	
69	**S10: Limitations 诚实详尽**（11 条）。
70	
71	---
72	
73	## Weaknesses
74	
75	### Must-Fix (Critical) — 3 items
76	
77	**W1 [数据不一致]: 跨章节 Δ 数值矛盾。**
78	*R2 W4 + Director D1。交叉共识：critical。*
79	
80	Abstract、Introduction（含 Contribution #1）、Discussion、Conclusion 均报告 Mistral-7B PW-D5 Δ=−4.67pp (Introduction 还标注 n=303)。但 Table 1 和 Experiments §4.2 报告 Δ=−2.83pp (n=600, p=0.0095)。四个叙述章节保留了旧实验数据，表格已更新至全量结果。
81	
82	审稿人发现此类矛盾会系统性降低对所有定量结论的信任。**必须统一。**
83	
84	---
85	
86	**W2 [CJT Framing Gap]: 标题声称 "trace independence limits" 但 Oracle 数据证明 constraint quality 是瓶颈。**
87	*Director D2。R2 交叉回应中从 significant 提升为 critical。*
88	
89	Oracle 实验使用**完全相同的 correlated traces**，仅替换约束来源（gold vs self-extracted），gain 从 ~0pp 跳至 +14.22pp。这证明 trace independence 不是瓶颈——同样的 correlated traces 在 gold constraints 下完美工作。
90	
91	论文内部证据也指向 constraint quality：8.2% discriminative rate（§6.2）、56.4% zero shared variables（§6.2）、entropy mechanism（§6.5）。CJT/κ/Eff-K 解释的是 SC plateau（为什么更多 traces 不能持续提升投票），不是 SICA 失败（为什么约束聚合无效）。
92	
93	论文将两个不同现象混为一谈：(1) SC plateau（由 trace correlation 解释 → CJT），(2) SICA 失败（由 constraint quality 解释 → discriminative rate）。标题和 framing 应区分这两个层次。
94	
95	R2 建议的修复方向：要么调整标题强调 constraint quality，要么明确论证 trace correlation 如何通过双通道（直接限制投票多样性 + 间接限制约束多样性）同时影响两种机制。
96	
97	---
98	
99	**W3 [Goldilocks Zone 证据窄]: 所有正面证据来自 1 模型 × 1 数据集（2/3 seeds）。**
100	*R1-F3 + R2 N1。交叉共识：critical。*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07b71a83-66a6-4423-9283-fde65f662928",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "53e4e9ed-06a5-4876-9cd3-0d35df0021e8",
  "sourceToolAssistantUUID": "07b71a83-66a6-4423-9283-fde65f662928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T14:17:15.703Z_

<details open><summary>🔧 Tool call — Read · `toolu_0128xnZwY85AM3xiXZaC1k2A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53e4e9ed-06a5-4876-9cd3-0d35df0021e8",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0029c3dd-1b92-429d-b8cc-9f068e02c240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

### Tool result

_source line 13 · 2026-05-23T14:17:15.710Z_

<details><summary>↩ Tool result · `toolu_0128xnZwY85AM3xiXZaC1k2A`</summary>

```text
1	---
2	round: 3
3	review_mode: fresh
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-20T13:21:27.432763+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告：Round 5 (Fresh Review)
12	
13	**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Fail in LLM Reasoning"
14	**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
15	**Reviewers**: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性 + 论文质量)
16	**审稿模式**: Fresh (重新审稿)
17	
18	---
19	
20	## Summary
21	
22	本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取 FOL 约束并通过 Z3 MAX-SAT 聚合。在 6 个模型（7B-32B）、3 个推理域、3000+ 条件评估中，发现自提取约束无法超越 majority voting。核心发现包括：(1) symbolic confirmation bias（83.3% 错误约束支持错误多数答案）；(2) independence-accuracy trade-off（κ≥0.40 across three model families）；(3) process-level independence bottleneck（CoT cosine 0.69 >> answer κ 0.41）。Oracle controls 确认聚合机制 sound（+14.22pp FOLIO, +11.50pp ProofWriter）。论文还报告了两个正面发现：constraint-answer decoupling（interim Δ=+11.3pp）和 cross-architecture NLI verification（Δ=+3.43pp, p=0.039）。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 实验规模罕见的全面。** 6 个模型、3 个推理域、~1,250 unique instances、4-seed replication、15+ distinct 补救策略（含 prompt-level, method-level, additional directions）。这种穷举性搜索为社区提供了有价值的负面证据，减少重复劳动。[R1, R2 一致]
29	
30	**S2. 统计方法论强于该领域平均水平。** McNemar exact tests、10,000-resample bootstrap CIs、formal power analysis（Appendix D 诚实承认 underpowering）、4-seed replication。这是负面结果论文的方法论标杆。[R1, R2 一致]
31	
32	**S3. Oracle controls 设计精妙。** Gold FOL/DSL 替换有效隔离 extraction vs aggregation bottleneck。Z3 agreement rate（95.1% FOLIO, 97.1% ProofWriter）验证了转换保真度。[R1, R2 一致]
33	
34	**S4. "Symbolic confirmation bias" 概念有独立价值。** 83.3% 错误约束支持错误多数答案、4.97× bias ratio、94% error overlap with SC——量化清晰、跨模型可复制（3 families）、可测试。[R1, R2 一致]
35	
36	**S5. Condorcet 理论框架优雅。** CJT + Effective-K 为 SC 的 saturation 行为提供了理论解释，尽管 κ→ICC 代理需更强论证。[R1]
37	
38	**S6. 高度透明的报告。** Power analysis、bootstrap CI、seed sensitivity、computational cost 完整报告。Case studies（Appendix F）和 constraint quality 对比（Appendix R）提供了可复现所需的细节。[R1, R2 一致]
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（影响接收决定）
45	
46	**[MF-1] §4.1 Decoupling 实验报告未完成的 interim results（n=70/204）** [R1-N2 + R2-N1, 完全共识]
47	
48	论文在 Abstract、Introduction（Contribution 4）、§4.1、Conclusion 中均报告了一个仅完成 34% 的实验（Δ=+11.3pp over SC, +6.4pp over SICA）。这是论文仅有的两个正面发现之一，直接支撑 "breaking confirmation bias" 叙事线。
49	
50	审稿人无法评估一个未完成实验的真实效果。更关键的是：若 full-scale 确认 Δ≈+11pp，将直接推翻核心 claim——因为 decoupling 仍是同一模型的 self-extraction（只是去除了结论信息），说明问题不在 self-extraction 本身而在提取时看到了自己的答案。这会根本性地改变论文定位。
51	
52	→ **建议**: 投稿前完成实验。若无法完成，删除 §4.1 相关内容（Abstract/Intro/Conclusion 中均需修改），将 decoupling 作为 future work 在 Discussion 中简述。
53	
54	**[MF-2] Oracle "24% ceiling" 跨模型比较不成立** [R1-N1, R2 交叉回应完全同意]
55	
56	Oracle 实验仅在 Qwen2.5-14B 上运行（SC=75.49%, Δ=+14.22pp），但 "24% ceiling" 将此与 Mistral-7B 的自提取结果（SC=55.88%, Δ=+3.43pp）对比。两个模型基准准确率相差近 20pp，oracle gain 天花板是模型依赖的。该比较出现在 Abstract、Introduction、§5.3，是核心量化结论之一。
57	
58	→ **建议**: 在 Mistral-7B FOLIO 上运行 oracle 实验（技术可行，FOLIO 有 gold annotations），报告同模型 ceiling；或改为定性陈述，不给出具体百分比。
59	
60	**[MF-3] Discussion（~100 词）和 Conclusion（~60 词）对负面结果论文严重不足** [R2-N4, R1 交叉回应同意]
61	
62	负面结果论文的核心价值在于 insight 深度。当前 Discussion 仅复述发现，缺少：(a) 对 neuro-symbolic reasoning 研究议程的 broader implications；(b) 在什么条件下 self-extraction 可能 work（更大模型？不同架构？trained extractors？）；(c) 与 CoT faithfulness 文献的联系（Turpin et al. 2024）；(d) 与经典 ensemble diversity 文献的关系（Krogh & Vedelsby 1995）。
63	
64	→ **建议**: 扩展 Discussion 至≥2 段实质内容；Conclusion 增加 community-level takeaway。修复 §3/§5 内容重复可释放 ~0.5-0.7 页空间。
65	
66	### Strong Should-Fix（影响评分）
67	
68	**[SF-1] "Fundamental" independence-accuracy trade-off overclaim** [R2-N2(must-fix), R1 partially agrees(should-fix)]
69	
70	Pareto frontier 仅基于 4 种聚合方法在 Mistral-7B 上 + 3 个模型家族（均 7B-14B）在单一 benchmark（FOLIO, n=204）上的 7 个数据点构建。"Fundamental" 暗示理论上不可避免，但 Limitations 明确承认未测试 70B+。R1 认为措辞修改即可，R2 认为严重性更高。
71	
72	→ **建议**: 将 "fundamental" 替换为 "persistent"/"empirical"；称 "observed trade-off pattern" 而非 "Pareto frontier"；添加显式 scope qualifier "at the 7B-32B scale tested"。
73	
74	**[SF-2] Cross-architecture DeBERTa PoC 统计脆弱** [R2-N3(must-fix), R1-W1(should-fix)]
75	
76	p=0.039 来自仅 9 个 discordant pairs（b=1, c=8）。McNemar 在 discordant n<25 时 power 极低。p=0.039 在 15+ 条件的多重比较下无法存活（Bonferroni threshold ~0.003）。单一 benchmark、单一 LLM、单一外部模型，无跨数据集/跨模型 replication。这是论文唯一 p<0.05 的正面结果。
77	
78	→ **建议**: 弱化 Abstract/Introduction 中的措辞（"demonstrating" → "suggesting"）；增加 discordant-pair 数量的 caveat；若可行，在 ProofWriter 上复制。
79	
80	**[SF-3] Variable name isolation confound 未与 confirmation bias 区分** [R1-W3, R2 强烈同意]
81	
82	56.4% 的跨答案约束对共享零个 Z3 变量——MAX-SAT 退化可能不是因为 confirmation bias，而是因为变量名不一致导致 Z3 无法检测跨 trace 语义矛盾。Oracle 成功部分可归因于 gold FOL 使用规范变量名（此为另一 confound）。两种解释有不同实践含义——若是变量名问题，canonical normalization 可能解决而无需外部模型。缺少 canonicalization 消融是实质性缺陷。
83	
84	→ **建议**: 添加 canonical variable normalization 消融实验，以区分 confirmation bias 和 variable isolation 各自的贡献；或在 Discussion 中将此作为重要 confound 充分讨论。
85	
86	### Should-Fix
87	
88	**[W1] Fleiss' κ 作为 ICC 代理缺乏形式化论证** [R1-W2, R2 agrees]
89	Eq.1 直接将 κ 代入 Kish design-effect formula，但 ICC 和 κ 是不同的统计量。之前的修复（添加 Kish 引用 + 渐近等价注记）被本轮 Reviewer 认为不充分。
90	→ 建议: 增加 caveat "K_eff serves as a qualitative indicator" 或换用 ICC/Krippendorff's alpha。
91	
92	**[W2] 缺失经典 ensemble diversity 文献** [R2-W1, R1 agrees]
93	Independence-accuracy trade-off 正是 Krogh & Vedelsby (1995) ambiguity decomposition 和 Brown et al. (2005) diversity survey 在 LLM traces 上的重述。未引用这些奠基性工作削弱理论可信度。
94	→ 建议: 在 Related Work 或 Discussion 中引用并讨论。
95	
96	**[W3] §3/§5 内容重复浪费 ~0.5-0.7 页** [R1-W4, R2 agrees]
97	实验设置和 Oracle Control 描述在 method.tex 和 experiments.tex 中几乎重复。
98	→ 建议: 合并为一处，释放空间用于 Discussion 扩展。
99	
100	**[W4] "25+ strategies" 计数膨胀** [R2-W3, R1 partially agrees]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0029c3dd-1b92-429d-b8cc-9f068e02c240",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "e7643f1a-e9e2-414d-a73c-8254f1712236",
  "sourceToolAssistantUUID": "0029c3dd-1b92-429d-b8cc-9f068e02c240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T14:17:15.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Cw8zPCUNMdyc2S3Jdw5YK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_4.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7643f1a-e9e2-414d-a73c-8254f1712236",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d2a9b1d-fa88-4114-ae8c-7a7937b9b684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

### Tool result

_source line 15 · 2026-05-23T14:17:15.925Z_

<details><summary>↩ Tool result · `toolu_012Cw8zPCUNMdyc2S3Jdw5YK`</summary>

```text
1	---
2	round: 4
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-20T15:17:11.662860+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	
12	# 审稿报告 — Round 6 (Fresh)
13	
14	**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Fail in LLM Reasoning"
15	**Venue**: EMNLP 2026 (ARR May 2026 cycle)
16	**Deadline**: 2026-05-25 (ARR submission) / 2026-08-02 (EMNLP commitment)
17	**Reviewer 配置**: R1 (方法严谨性 + 实验设计 + 统计分析) / R2 (新颖性 + 相关工作完整性 + 格式合规)
18	**流程**: Round 1 独立审稿 → 交叉分享 ([AGREE]/[REBUT]) → 收敛 → 汇总
19	
20	---
21	
22	## Summary
23	
24	论文提出 SICA（Symbolic Invariant Consensus Aggregation），从 K 条 CoT traces 中提取 FOL 约束并通过 Z3 加权 partial MAX-SAT 选择答案，系统评估其在 6 个模型（7B–32B）、3 个推理域、~1,250 unique instances 上的表现。核心发现为负面结果：自提取约束无法超越 SC 多数投票。论文提出 "Symbolic Mirage" 假说解释此失败，识别三个机制（Independence-Accuracy Trade-off, Symbolic Confirmation Bias, Process-Level Homogeneity），并通过 Oracle 控制和 DeBERTa 跨架构 PoC 论证外部验证信号是突破方向。
25	
26	---
27	
28	## Strengths
29	
30	**S1: 系统性实验设计与精巧的 Oracle 控制。** [R1-S1/S2/S3, R2-S1, 共识]
31	6 个模型 × 3 域 × 3000+ 条件评估，22+ remediation strategies 全部失败，形成强有力的负面结论闭环。Oracle 控制（gold FOL → +29.90pp Mistral-7B, +14.22pp Qwen-14B, +11.50pp ProofWriter）精确分离了聚合机制与约束质量的因果关系，是全文最有说服力的实验。
32	
33	**S2: Symbolic Confirmation Bias 的定量化有独立贡献价值。** [R1-S1, R2-S3, 共识]
34	Bias ratio 4.97×、94% 错误与 SC 重叠、跨 3 个模型族的一致性（Table 14）——这些定量指标超越了 "LLMs cannot self-correct" 的定性结论，为社区理解自验证失败的具体机制提供了可操作的诊断工具。
35	
36	**S3: CJT + Effective-K 框架提供有价值的分析透镜。** [R2-S2, R1-S5]
37	将 Condorcet Jury Theorem 引入 LLM trace 分析，Effective-K 指标直观量化了"额外采样的边际收益递减"。跨 4 种聚合方法和 3 个模型族的 κ ≥ 0.40 ceiling（Table 3）支撑了 independence bottleneck 的普遍性。
38	
39	**S4: 写作结构清晰，统计报告完整。** [R1-S6, R2-S5]
40	正文 8 页内容密度高，Contribution 列表精确对应后续 sections。McNemar exact test、bootstrap CI、power analysis（虽然结论不利于作者）的全面报告体现了统计诚实性。Limitations 段覆盖 scale/language/power/computation 各维度。
41	
42	**S5: 跨架构 PoC 提供建设性出路。** [R1-S4, R2-S4]
43	DeBERTa NLI 在 ProofWriter 上 +3.50pp（p=0.013），打破 same-model ceiling，为论文从纯负面转向有条件的正面展望提供了实验支撑。
44	
45	---
46	
47	## Weaknesses
48	
49	### Must-Fix
50	
51	**W1: 统计功效严重不足，标题 "Fail" 过度断言。** [R1-W1(must-fix), R2-AGREE]
52	Power analysis（Appendix E）显示 observed power 仅 5.7%–20.6%，MDE 为 4.64–8.84pp。如果 SICA 真实效应为 1–2pp（对 reasoning benchmark 已属 meaningful），当前样本量根本无法检测到。标题 "Fail" 和 abstract "fail to surpass majority voting" 是 evidence of absence 的措辞，但统计证据仅支持 absence of evidence。
53	- **修复方案**: (1) 对 confirmatory conditions 运行 TOST equivalence test（margin ±2pp）——若 TOST 显著拒绝效应 ≥2pp 的假设，可有底气声称 "no practically meaningful improvement"；(2) 若 TOST 不显著，软化语言："...provide no detectable improvement at current sample sizes" 或 "...do not yield statistically significant gains"；(3) 标题改为 "Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning"。
54	
55	**W2: 跨架构 PoC 多重比较未校正。** [R1-W2(must-fix), R2-AGREE]
56	DeBERTa 在 2 datasets × 3+ weight configurations 上测试。ProofWriter w=3 的 p=0.013 在 Bonferroni（6 comparisons, threshold 0.0083）下不再显著；仅 w=5 的 p<0.001 可能存活。论文未报告任何多重比较校正。
57	- **修复方案**: 报告 Bonferroni/BH 校正后 p 值，或明确标注 §6 为 exploratory analysis。以 ProofWriter w=5（p<0.001，校正后仍显著）为主要证据。
58	
59	**W3: 核心发现与 self-correction/self-verification 文献的区分不足。** [R2-W1(must-fix), R1-partial-rebut]
60	"Symbolic Confirmation Bias" 本质上是 Huang et al. (2024) self-correction failure 和 Stechly et al. (2025) self-verification failure 在符号域的具体实例化。论文引用了这些工作但未充分论证其增量贡献。R1 部分反驳：认为定量框架（κ, Effective-K, BR）本身有价值；R2 坚持需要更清晰的区分。
61	- **修复方案**: 在 Introduction 或 §7 增加段落，明确对比 (a) Huang/Stechly 的定性结论 vs (b) 本文的定量贡献（Effective-K 框架、BR 指标作为诊断工具、process-level independence 发现形式验证也无法突破 confirmation bias）。
62	
63	**W4: 关键相关工作缺失。** [R2-W2(must-fix), R1-AGREE]
64	- **CLOVER** (Ryu et al., ICLR 2025): compositional FOL translation + SAT verification，在 7 个逻辑推理 benchmark 上 SOTA。与 SICA pipeline 直接相关——为什么 compositional translation 有效而 self-extraction 失败？
65	- **VERGE** (arXiv 2601.20055): SMT solver iterative refinement
66	- **"Not All Votes Count! Programs as Verifiers"** (Xia et al., 2024): programs-as-verifiers 增强 SC
67	- **"Logical Soundness is not a Reliable Criterion..."** (arXiv 2604.04177): LLM formal logic 系统性失败 position paper
68	- **修复方案**: 在 §2 Neuro-symbolic reasoning 段落补充 CLOVER 和 VERGE，讨论 compositional translation vs free-form extraction 的对比。
69	
70	### Should-Fix
71	
72	**W5: CJT 框架应用不够严谨——Fleiss' κ 作为 ICC proxy 有统计学问题。** [R1-W3(should-fix), R2-Q3, 共识]
73	Fleiss' κ 是名义尺度一致性指标，与 Ladha (1992) 意义上的投票者相关系数统计含义不同。Kish (1965) design-effect 公式假设等相关结构（constant pairwise correlation），在 LLM traces 中未被验证。论文已添加 "qualitative proxy" 声明，但 K_eff 数值仍被大量用于定量推断。
74	- **修复方案**: (a) 补充 pairwise vote correlation 作为替代/交叉验证指标；(b) 或弱化 CJT 框架的定量角色至 conceptual motivation。
75	
76	**W6: Bias ratio 报告不一致。** [R1-W4(should-fix)]
77	§5.2 报告 4.97× raw / 4.24× weighted，跨模型 "1.97×, 3.93×, 2.88×" raw——但 Table 14 中 weighted 数字为 2.14/3.05/2.86×。4.97× 的计算范围（哪个条件、pooled 还是单条件）不明确。
78	- **修复方案**: 在 §5.2 明确标注 4.97× 的计算条件和 raw/weighted 区别，Table 14 同时报告两种 ratio。
79	
80	**W7: Type A/B/C failure mode 分类为 post-hoc 但呈现为理论框架。** [R1-W5(should-fix), R2-AGREE]
81	SC 准确率阈值（60%, 40%）无理论推导或 sensitivity 分析。
82	- **修复方案**: 明确标注为 post-hoc empirical taxonomy。
83	
84	**W8: Process-Level Independence 的 TF-IDF cosine similarity 过于粗糙。** [R2-W3(should-fix), R1-Q3, 共识]
85	TF-IDF 只捕获 lexical overlap，无法区分语义相似但表述不同的推理路径。论文已声明 "lower bound"，但作为 Contribution 3 的核心方法论，需要更强的支撑。
86	- **修复方案**: 补充 sentence embedding（SimCSE/SBERT）对比验证，或在 Limitations 中更显著地讨论此限制。
87	
88	**W9: Degeneration condition (Eq. 4) 推导不完备。** [R1-W6(should-fix)]
89	从 constraint coupling 到 score 退化为 majority voting 的推导缺少关键步骤——需假设 SAT 检查在退化 regime 下几乎不淘汰约束。
90	- **修复方案**: 补充退化条件下 constraint rejection rate 的经验证据，或标注 Eq. 4 为 approximate。
91	
92	**W10: "Symbolic Mirage" 术语精确度。** [R2-W5(should-fix), R1-rebut]
93	"Mirage" 暗示约束方法论整体失效，但 Oracle 实验证明机制有效。R2 认为命名误导，R1 认为有教学价值但需 scoping。分歧点。
94	- **修复方案**: 保留术语但在首次出现时明确定义范围："self-extraction 产生的约束是 mirage，而非符号约束方法论本身"。
95	
96	### Minor
97	
98	**W11**: α=0.5 penalty weight 无 sensitivity analysis 或 justification。[R1-W7]
99	**W12**: GSM8K (n=30) / AIME (n=22) 在 Table 1 中与大样本条件并列，应加分区标注。[R1-W8]
100	**W13**: orphan bib entry `press2023compositionality`。[R1-W9, R2-W6]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d2a9b1d-fa88-4114-ae8c-7a7937b9b684",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "6e8d1e46-b061-4e49-adcf-75c00b640b60",
  "sourceToolAssistantUUID": "6d2a9b1d-fa88-4114-ae8c-7a7937b9b684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T14:17:16.327Z_

<details open><summary>🔧 Tool call — Read · `toolu_0178RKTkrGioTwCuP39KaGcK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_5.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e8d1e46-b061-4e49-adcf-75c00b640b60",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2395879a-4cb5-480b-864f-5e8c453dfbad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

### Tool result

_source line 17 · 2026-05-23T14:17:16.333Z_

<details><summary>↩ Tool result · `toolu_0178RKTkrGioTwCuP39KaGcK`</summary>

```text
1	---
2	round: 5
3	review_mode: fresh
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-20T20:08:40.344865+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 8 (Fresh Review)
12	
13	**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning"
14	**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
15	**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work + 写作质量)
16	
17	---
18	
19	## Summary
20	
21	本文研究 LLM 自提取的符号约束能否通过 Symbolic Invariant Consensus Aggregation (SICA)——基于 FOL 约束提取和 Z3 weighted partial MAX-SAT——改善 Self-Consistency majority voting。在 6 个模型（7B–32B）、3 个推理域、3000+ 条件评估中，自提取约束未能显著提升准确率。作者将此归因于 "Symbolic Mirage"：自提取约束是模型分布偏差的投射（confirmation bias rate 83.3%, BR ≈ 1.97+），trace 之间的 process-level 相关性（cosine similarity 0.69）远超 answer-level 独立性（κ ≈ 0.41）。25+ 补救策略均失败，揭示持久的 independence-accuracy trade-off。Oracle controls 确认聚合机制 sound（+29.90pp, +14.22pp, +11.50pp），瓶颈在自提取质量。Cross-architecture DeBERTa NLI verifier 在 ProofWriter 上显示初步正向信号。
22	
23	---
24	
25	## Strengths
26	
27	**S1. 实验规模和系统性出色。** 6 模型 × 6 数据集 × 3 推理域覆盖高/中/低 SC 准确率区间，25+ 补救策略的穷举式搜索在负面结果论文中罕见，大幅增强结论可信度。[R1-S2, R1-S6, R2-S2]
28	
29	**S2. 统计方法论严谨。** TOST 等价性检验（±2pp margin）确认负面结果而非仅依赖 NHST，Bootstrap 95% CI（10,000 resamples）、BH 多重比较校正、统计功效分析均超出 NLP 论文平均水准。[R1-S4, R2-S1]
30	
31	**S3. Oracle controls 设计巧妙。** Gold FOL oracle 大幅提升性能（Mistral-7B FOLIO +29.90pp, Qwen-14B FOLIO +14.22pp, ProofWriter +11.50pp），精确分离聚合机制（sound）与提取质量（bottleneck）。[R1-S3, R2-S5]
32	
33	**S4. CJT 框架和量化诊断工具有独立贡献。** Effective-K（§5.1）、Bias Ratio（§3.3）、C_D diagnostic 将 SC 失效模式诊断从定性变为定量，可被后续工作直接复用。[R1-S1, R1-S5, R2-S3]
34	
35	**S5. Independence-Accuracy Trade-off（Figure 7）是最具洞察力的贡献。** 清晰展示同模型方法的 κ ≈ 0.40–0.47 ceiling，Debate 降 κ 但毁 accuracy，形成 Pareto 关系。[R2-S4]
36	
37	**S6. 叙事结构完整。** 假设建立 → 主实验否定 → 三重诊断 → 补救失败 → 跨架构出口 → 讨论，逻辑连贯。格式合规：8 页正文、Limitations 完整、双盲匿名、48 条引用。[R2-S6, R2-S7]
38	
39	---
40	
41	## Weaknesses
42	
43	### Must-Fix（影响接收决定）
44	
45	**W1. FOL 术语误导，负面结论 scope 不清晰。** [R1-N1 critical, R2 agrees at warning]
46	论文通篇使用 "first-order logic (FOL) constraints"，但 Limitations（p.21）承认提取结果 "predominantly propositional ground clauses without quantifiers"。数学域 extraction prompt 提取的是 equation/inequality/comparison，无量词。标题使用 "Symbolic Constraints" 无误，但正文大量出现 "FOL constraints" 有术语膨胀。
47	- **Action**: (1) 统一改为 "symbolic/logical constraints"，仅在 Z3 接口描述中保留 "FOL-style"；(2) 报告含量词约束的比例（按域/模型）；(3) Discussion 讨论真正 FOL 提取是否改变结论。
48	- **R2 缓解观点**: 命题逻辑 ⊂ FOL，如果更弱形式都失败，更强形式失败可能性只会更大——但这需要在论文中显式论证，不能让读者自己推断。
49	
50	**W2. Cross-architecture PoC 双重 underpowered。** [R1-N2 critical + R2-W2 warning, 双方交叉确认]
51	- **生成端**（R1）: 仅 Mistral-7B 一个生成模型，不同模型有 Type A/B/C 不同行为模式。
52	- **验证端**（R2）: FOLIO +2.94pp (n.s.) vs. ProofWriter SICA 自身 −2.83pp (p=0.014)，两个数据集方向相反。α=3 在 n=204 上有 overfitting 风险。
53	- **综合**: §6 "confirming the effect is not verifier-specific" 仅基于三个 NLI 架构在同一生成模型上的一致性，不等于跨生成模型一致性。
54	- **Action**: 至少补一个 Qwen2.5-14B 的 DeBERTa combo 实验（traces 已有）；将 §6 结论 qualify 为 "preliminary signal on Mistral-7B ProofWriter"；讨论 α selection 的 overfitting 风险。
55	
56	### Should-Fix（提升论文质量）
57	
58	**W3. 增量新颖性定位需加强。** [R2-W1 warning, R1 partial REBUT — **DIVERGENCE**]
59	- **R2 立场**: Huang et al. (2024) self-correction failure、Stechly et al. (2025) self-verification limitations、Amonkar et al. (2025) LLM formalization quality、Chan et al. (2026) logical soundness limitations——核心洞察在概念层面已被覆盖。Excitement 2.5/5。
60	- **R1 立场**: 本文测试了一个更强的假设——FOL + Z3 确定性 solver 能否绕过自然语言 self-correction 的局限。BR/C_D/Eff-K 是新的量化工具，先行工作停留在 "doesn't work"，本文给出 "why, how much, where exactly"。
61	- **共识**: §2 Related Work 应更明确 position：不是重复 "self-correction fails"，而是 "即便引入确定性形式验证（FOL + Z3），self-extraction 的 confirmation bias 仍然阻断这条路径"。
62	
63	**W4. Domain + Model 覆盖范围与 Abstract 表述不匹配。** [R1-W3 + R2-W4, 双方共识]
64	- Abstract "across the full LLM capability range" 仅 7B–32B 开源模型。
65	- "Three reasoning domains" 中数学域全部 degenerate（SC ≥ 85%），主要结论限于 formal/logical reasoning。
66	- **Action**: Abstract 修改为 "across a range of open-source LLMs (7B–32B)" + "formal and logical reasoning domains, with exploratory results on mathematical reasoning"。
67	
68	**W5. Symbolic Confirmation Bias 缺乏与 Turpin et al. (2024) unfaithful CoT 的理论连接。** [R2-W3, R1 agrees]
69	BR = 1.97 可能是 unfaithful CoT 在 FOL 层面的投射。论文未区分 (a) 模型故意生成支持错误答案的约束 vs. (b) 约束生成与答案生成共享同一 biased representation。
70	- **Action**: §3.3 增加 Turpin et al. 连接讨论。
71	
72	**W6. 种子复制 + 统计功效标注不足。** [R1-W1 + R2-W5, 双方共识]
73	Table 1 大多数条件未标注 seed 数量，7 个条件 n ≤ 60 MDE 极大，未区分 confirmatory vs. exploratory。
74	- **R2 缓解观点**: TOST 用 per-item paired comparison，统计结论本身 well-powered。但 Table 1 标注仍需改善。
75	- **Action**: Table 1 增加 seed 列和 powered/exploratory 标注。
76	
77	**W7. 语义去重缺失 ablation。** [R1-W2 + R2-Q5, 双方共识]
78	Syntactic dedup 可能系统性放大 verbose traces 权重。论文未报告去重前后约束数量比，未做 Z3 semantic equivalence ablation。
79	- **Action**: 报告去重统计；讨论影响或做 ablation。
80	
81	**W8. 约束质量分析仅覆盖单一模型。** [R1-W4, R2 agrees]
82	Extraction error taxonomy (N=804) 仅 Qwen2.5-14B on FOLIO + ProofWriter。91.8% discriminative rate 在 Type B/C 模型上可能不同。
83	- **Action**: 扩展到 2-3 个模型，或明确限定 claim scope。
84	
85	### Nice-to-Have
86	
87	**W9.** Figure 5（intervention strategies summary）深埋 Appendix p.22，应移入正文——两位 Reviewer + 视觉审查均建议。[R2-W6, R1 agrees]
88	
89	**W10.** Figure 2 线性回归 R² ≈ 4.4%，需说明 R² 并讨论离群点影响。[R1-W5]
90	
91	**W11.** 83.3% confirmation bias 是 aggregate 数字，per-model 变异大（69%–94%），主文应报告 breakdown。[R1-Q3]
92	
93	---
94	
95	## Reviewer Consensus
96	
97	以下问题双方达成共识（[AGREE]）：
98	1. **PoC 不足**: Cross-architecture PoC 在生成端（single model）和验证端（inconsistent datasets）双重 underpowered [R1-N2 + R2-W2]
99	2. **术语修正**: "FOL constraints" 应改为 "symbolic/logical constraints" [R1-N1 + R2 agrees]
100	3. **覆盖范围校准**: Abstract 的 domain 和 model claims 需 downscope [R1-W3 + R2-W4]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2395879a-4cb5-480b-864f-5e8c453dfbad",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "5d5ccaca-e660-4b3a-b89c-9f26337ce1df",
  "sourceToolAssistantUUID": "2395879a-4cb5-480b-864f-5e8c453dfbad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T14:17:17.247Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TQWiMGAHU7ebtnGJyk37P8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_6.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d5ccaca-e660-4b3a-b89c-9f26337ce1df",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "75de6d55-f005-4b2c-8391-a0cde88bbad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

### Tool result

_source line 19 · 2026-05-23T14:17:17.258Z_

<details><summary>↩ Tool result · `toolu_01TQWiMGAHU7ebtnGJyk37P8`</summary>

```text
1	---
2	round: 6
3	review_mode: fresh
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-21T01:59:54.375917+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 9 (Fresh Review)
12	
13	**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning
14	**Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)
16	**审稿模式**: Fresh (重新审稿)
17	
18	---
19	
20	## Summary
21	
22	本文研究 SICA（Symbolic Invariant Consensus Aggregation），从 LLM reasoning traces 中自提取逻辑约束并通过 Z3 MAX-SAT 聚合，试图改善 Self-Consistency majority voting。在 6 个模型 (7B-32B)、3 个逻辑推理 domain、3000+ condition-evaluations 上，结论为：self-extracted constraints 因 Symbolic Confirmation Bias（BR=4.97×, 83.3% wrong-supporting rate）无法改善 SC。Oracle controls 证明机制本身有效（FOLIO +29.90pp），瓶颈定位在 self-extraction 质量。27 种 remediation 策略全部失败，cross-architecture NLI verification 提供了建设性的正向方向。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 实验规模和系统性.** 6 个模型（3 model families, 7B-32B）、3 个 domain、3000+ condition-evaluations、~1250 unique instances、4-seed replication。对负面结果论文而言覆盖面出色。[R1, R2 共识]
29	
30	**S2. Oracle Controls 精准定位瓶颈.** Gold-SICA 在 FOLIO +29.90pp（p < 10⁻¹³）、ProofWriter +11.50pp（p < 10⁻¹⁴），干净地将「机制有效性」与「self-extraction 信号质量」解耦。这是论文最有说服力的实验设计。[R1, R2 共识]
31	
32	**S3. 25+ Remediation 穷举.** 涵盖 prompt-level、method-level、paradigm-level 共 15 个 family 的 27 种策略，全部 neutral-to-negative。封堵了"只是 prompt 没调好"的反驳空间。[R1, R2 共识]
33	
34	**S4. 统计方法论透明.** Power analysis 明确指出 underpowered conditions，TOST 等价检验区分三类结论，bootstrap CIs 报告，seed-level 不稳定性如实呈现。[R1, R2 共识]
35	
36	**S5. 可复用诊断指标.** Effective-K、Bias Ratio、ProcessSim 超越本文语境，可用于任何 trace-aggregation 系统的失败预测。[R1]
37	
38	**S6. Cross-Architecture Escape.** DeBERTa NLI 在 ProofWriter 上 +3.50pp（BH 校正后 adj p=0.038），3 种 NLI architecture 复现，提供建设性方向。[R1, R2 共识]
39	
40	**S7. 写作结构清晰.** 论文组织合理，从 CJT 动机 → SICA pipeline → 实验 → 分析 → remediation → cross-arch escape 的叙事逻辑完整。[R2]
41	
42	**S8. 格式合规.** 8 页正文、匿名化完整、Limitations 位置正确、引用格式规范。[R2 确认]
43	
44	---
45	
46	## Weaknesses
47	
48	### Must-Address（影响整体评估）
49	
50	**W1 [Warning] 相对于 Huang/Stechly 的增量新颖性不足.** 核心发现（LLM self-extracted verification 无法改善推理）与 Huang et al. (ICLR 2024) 和 Stechly et al. (ICLR 2025) 在概念层面高度一致。三个诊断指标（Eff-K, BR, process-κ）分别是 Kish's design effect、条件概率比、TF-IDF cosine similarity 的直接应用。"Symbolic Mirage" 本质是已知原理在符号约束 domain 的 instantiation。R1 认为 Z3 形式化验证场景的 non-triviality 和 27 种 remediation 穷举超越 prior work，但 R2 认为概念层面的增量不足以支撑 main conference。
51	- **R1/R2 divergence**: R1=3.5 Borderline Conference vs R2=3.0 Findings
52	- **Director 裁决**: R2 的判断更有说服力——论文的核心 insight 在 prior work 中已有定性论证，本文的主要贡献在于 domain-specific 的定量验证和穷举分析，这更适合 Findings 定位。
53	
54	**W2 [Warning] Independence-Accuracy Trade-off 作为第一贡献存在部分同义反复.** Table 2/Figure 7 的 cross-model pattern（弱模型=高独立性+低准确率，强模型=低独立性+高准确率）本质上接近经典 bias-variance tradeoff。27 种 within-model remediation 全部失败增强了 inescapability claim，但 cross-model pattern 本身新颖性有限。双方共识建议将 Symbolic Confirmation Bias 提升为第一贡献。[R1 AGREE, R2 raised]
55	
56	**W3 [Warning] Table 1 的显著性声称缺少多重比较校正.** 16 个 non-degenerate 条件的 McNemar tests 未做 BH 校正。两个 "significant degradation"（Mistral-7B PW p=0.014, Qwen2.5-14B PW p=0.011）BH 校正后均不再显著。不影响核心负面结论，但 degradation 声称被高估。论文在 NLI 结果中正确使用了 BH（m=12），应统一标准。[R1 raised, R2 AGREE]
57	
58	**W4 [Warning] κ→Effective-K 映射形式化不足.** Eq.1 的 design-effect 公式源自 Kish (1965) 的 ICC (ρ)，Fleiss' κ 是 chance-corrected 一致性指标，数值范围和统计性质与 ICC 不同。论文仅一句 "qualitative proxy"，但 K_eff 在全文中作为核心诊断指标反复使用（如 "≤1.30 never improves"），超出了 proxy 的定位。[R1 raised, R2 AGREE]
59	
60	### Should-Fix（投稿前建议修复）
61	
62	**W5 [Warning] 遗漏关键相关工作.** SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 且报告正面结果——可与 SICA 负面结果形成 problem-level vs trace-level 对比，强化 Symbolic Mirage 论点。VeriCoT (Nov 2025) 将 CoT 形式化为 FOL 验证。CRITIC (Gou et al., ICLR 2024) 涉及 tool-interactive self-correction。[R2 raised, R1 AGREE]
63	
64	**W6 [Warning] NLI combo weight parameter w 未交叉验证.** w ∈ {1, 3, 5} 在同一测试集选择和评估。w=5 在 Mistral-7B 上 +10.67pp 但在 LLaMA-3.1-8B 上仅 +1.67pp (n.s.)，表明最优 w 不稳定。PoC 可接受但需声明 w 是 dataset-specific hyperparameter。[R1 raised, R2 AGREE]
65	
66	**W7 [Warning] Capability Gap Hypothesis sigmoid fit (R²=0.875) 基于 8 个数据点.** 3 参数 sigmoid 拟合 8 个点，adjusted R² 会大幅低于 0.875。Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。应改用 rank correlation 作为主要证据，弱化 inflection point 数值声称。[R1 raised, R2 AGREE]
67	
68	**W8 [Warning] T_ext=0.3 extraction temperature 缺 sensitivity analysis.** 采样 T 和 K 均有 sensitivity 分析，但 extraction——论文认定的核心瓶颈环节——的关键参数仅用单一值。[R1 raised, R2 AGREE via Q2]
69	
70	**W9 [Warning] Cross-architecture escape 实验规模不足.** 仅一种外部 verifier (DeBERTa NLI)、两个 dataset、三个 generator family。LogiQA 上无效。缺少与 trained verifiers/code-based verification 的对比。论文已定位为 PoC 并在 Limitations 中承认，但短板明显。[R2 raised, R1 AGREE]
71	
72	### Minor Issues
73	
74	**W10 [Info] Abstract "sixteen" vs §4.2 "fifteen" 数字不一致.** Table 1 有 16 个 non-degenerate 行，Abstract "sixteen" 正确，§4.2 "fifteen" 为笔误。[R2 raised, R1 confirms]
75	
76	**W11 [Info] 术语品牌化讨论.** R2 认为 "Symbolic Mirage"、"Symbolic Confirmation Bias"、"capability trap" 对 incremental 负面结果论文而言品牌术语过多。R1 反驳前两者有精确操作定义（Eq.5, §5.2），但同意 "capability trap" 可弱化。[DIVERGENCE — R1 REBUT, R2 raised]
77	
78	**W12 [Info] σ(c,a) provenance-based 设计未作为 design limitation 讨论.** R1 指出 σ(c,a)=1 iff c 来自产生 answer a 的 trace，这是导致 degeneration 的直接原因，论文未讨论基于 Z3 semantic evaluation 的替代设计。R2 反驳存在循环依赖问题且在 BR=4.97× 下两种 σ 定义结果应趋同。[DIVERGENCE — R1 raised, R2 REBUT]
79	
80	---
81	
82	## Reviewer Consensus [AGREE]
83	
84	1. **Table 1 需要多重比较校正**（W3）—— 不影响核心结论但需统一标准
85	2. **κ→K_eff 形式化不足**（W4）—— 需要更 rigorous 的论证或 caveat
86	3. **NLI weight w 未交叉验证**（W6）—— 需声明 dataset-specific
87	4. **Sigmoid fit 过拟合**（W7）—— 改用 Spearman ρ 作为主要证据
88	5. **T_ext sensitivity 缺失**（W8）—— 核心瓶颈参数应有消融
89	6. **遗漏 SatLM/VeriCoT/CRITIC**（W5）—— 必须引用
90	7. **"fifteen" 笔误**（W10）—— 修正为 "sixteen"
91	8. **Contribution 排序**（W2）—— Symbolic Confirmation Bias 应为第一贡献
92	9. **实验覆盖面 + Oracle controls + 25+ remediation 穷举是论文核心优势**（S1-S3）
93	10. **统计透明度和可复用诊断指标有独立价值**（S4-S5）
94	
95	## Reviewer Divergence [REBUT remaining]
96	
97	1. **Novelty 判断**（W1）: R1 认为 Z3 非 triviality + exhaustive remediation 足够 Borderline Conference (3.5)；R2 认为概念层面是 Huang/Stechly instantiation，仅够 Findings (3.0)。Director 倾向 R2 的判断。
98	2. **术语品牌化**（W11）: R1 认为有操作定义不算品牌化；R2 认为过度。部分共识：前两个可保留，"capability trap" 弱化。
99	3. **σ(c,a) 设计**（W12）: R1 认为应讨论替代方案；R2 认为循环依赖使替代不可行。
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75de6d55-f005-4b2c-8391-a0cde88bbad8",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "befca8b5-687f-4cd6-b396-36cca8743f72",
  "sourceToolAssistantUUID": "75de6d55-f005-4b2c-8391-a0cde88bbad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T14:17:17.447Z_

<details open><summary>🔧 Tool call — Read · `toolu_0173SEfZdHBgw1EGMPuHYYMV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_7.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "befca8b5-687f-4cd6-b396-36cca8743f72",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa3821a6-872e-4ab1-aa40-333463fc0ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "output_tokens": 878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1544
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 878,
          "cache_read_input_tokens": 37312,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1544,
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

_source line 21 · 2026-05-23T14:17:17.469Z_

<details><summary>↩ Tool result · `toolu_0173SEfZdHBgw1EGMPuHYYMV`</summary>

```text
1	---
2	round: 7
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-21T06:51:29.427085+00:00
6	reviewer_ids: ['1', '2']
7	cross_response_reviewer_ids: ['1', '2']
8	force_resubmit: False
9	---
10	
11	# 审稿报告（Round 10 — Fresh Review）
12	
13	**论文**: *Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*
14	**Venue**: EMNLP 2026 (via ACL Rolling Review) — Long Paper
15	**ARR Deadline**: 2026-05-25
16	
17	---
18	
19	## Summary
20	
21	本文研究自提取符号约束能否突破 Self-Consistency (SC) 的性能天花板。作者提出 SICA（Symbolic Invariant Consensus Aggregation），从 CoT 推理轨迹中提取形式逻辑约束并通过加权 Partial MAX-SAT (Z3) 选择答案。在 6 个模型（7B-32B）、3 个逻辑推理数据集 + 3 个辅助数据集、3,000+ 条件评估上，自提取约束均未显著改善 SC（BH 校正后无条件达到显著）。作者将失败归因为 "Symbolic Confirmation Bias"（错误问题上 83.3% 约束支持错误多数答案，BR=4.97×），识别出 independence-accuracy trade-off（同模型 κ≥0.40 ceiling），并测试了 27 种修复策略（全部失败）。Oracle 控制确认机制本身有效（+29.90pp, +14.22pp FOLIO）。跨架构 DeBERTa NLI 验证在弱 generator 上显著有效（+6.67pp ProofWriter, p<0.001），DRC 以 39% 验证成本恢复 90% 增益。
22	
23	---
24	
25	## Strengths
26	
27	1. **穷举式负面结果令人信服**：27 种补救策略横跨 15 个方法族（prompt-level, method-level, solver-level, diversity-level），系统性地关闭了"也许换策略就行"的反驳空间。这是该领域对 self-extraction 最全面的实验评估。
28	
29	2. **Oracle 控制实验设计精良**：用 FOLIO gold FOL 和 ProofWriter DSL 替换自提取约束，在相同 MAX-SAT 管道下获得 +29.90/+14.22/+11.50pp 增益（p < 10⁻⁷），干净地隔离了"约束质量"这一瓶颈变量。这是论文方法论上最强的部分。
30	
31	3. **多层次诊断体系**：answer-level κ、process-level cosine similarity、confirmation bias ratio、C₀ diagnostic、entropy decomposition 从不同角度三角验证同一结论。统计处理（McNemar + BH FDR + TOST + Bootstrap CI + Power Analysis）在 NLP 论文中罕见地严谨。
32	
33	4. **CJT 理论框架有启发性**：用 Condorcet Jury Theorem 的独立性条件分析 SC 的失败模式，为理解 LLM 采样局限性提供了清晰的理论透镜。
34	
35	5. **建设性方案缓解纯负面问题**：DeBERTa NLI escape + DRC 展示了"怎样才行得通"，DRC 以 39% cost 恢复 90% gain 有实用价值。
36	
37	6. **可重复性高**：完整 prompt 模板、算法伪代码、22 个 Appendix section，代码承诺开源。
38	
39	---
40	
41	## Weaknesses
42	
43	### Critical（Must-Fix，影响接收决定）
44	
45	**C1. Proposition 1（Self-Extraction Ceiling）无证明** [R1-N1, R2-W3 — 共识]
46	- §3.3 的 Proposition 1 声称 Δ_max^self ≲ Δ_oracle / BR(M)，但全文无证明或推导。"≲" 不精确（上界？渐近？近似？）。Page 5 的 "proof sketch" 实际论证的是 Corollary 1 的单调性，非 Proposition 1。Δ_oracle 的定义依赖于实验设置而非纯数学构造——这是 "empirical claim dressed as theorem"。
47	- **必须**：提供完整证明（可放 Appendix）或降级为 "Empirical Finding"。
48	
49	**C2. κ→Effective-K 映射理论基础不足** [R1-N2, R2 交叉同意 — 共识]
50	- Kish (1965) design effect 公式使用 ICC，非 Fleiss' κ。论文以 r=0.625 验证，仅中等相关（~61% 方差未被解释）。§3.1 有 ordinal diagnostic caveat，但 Abstract ("K_eff ≈ 1.20-3.62") 和 §5.1 中 K_eff 被作为定量指标使用——ordinal caveat 与 quantitative usage 矛盾。
51	- **必须**：(a) 报告 ICC 值并与 κ 对比；(b) Appendix 中提供 sensitivity analysis；(c) 全文统一为 ordinal 使用。
52	
53	**C3. Capability gap "perfectly monotonic" 结论依赖 n=6 非独立数据点** [R1-N3, R2 交叉同意 — 共识]
54	- Spearman ρ=1.0 基于 6 个 verifier-generator pairs（3 NLI 架构 × 2 有效 generator 水平），非完全独立（共享 Mistral-7B traces 和 DeBERTa verifier）。n=9 robustness check (ρ=0.836, p=0.007) 更诚实。R2 指出可能存在选择性纳入显著结果的循环论证风险。
55	- **必须**：将 "perfectly monotonically" 降级为 "strongly monotonically" 或 "consistent directional trend"；以 n=9 result 为主；显式承认 n=6 局限。
56	
57	**C4. 相对于 Huang et al. (2024) / Stechly et al. (2025) 的增量新颖性论证不足** [R2-N1, R1 部分 REBUT — 分歧]
58	- 核心发现——"自提取约束继承模型偏差"——与 Huang (LLMs cannot self-correct) 和 Stechly (self-verification limitations) 的已知结论在概念层面高度一致。R1 REBUT 指出 Z3 formal verification channel 使其非平凡（neurosymbolic 社区假设"形式化 → 可靠"），但 R2 认为这仍是 instantiation 而非 fundamental discovery。
59	- **Director 判断**：R1 的 Z3 论据有道理——formal verification 下偏差仍存在确实比 NL self-correction 更令人惊讶。但论文当前仅用 §1 中 2 句话区分，远不够显著。如果这个区分无法在修改中变得足够有说服力，则论文的 Excitement 不足以支撑主会议。
60	- **必须**：在 §1 和 §2 中用 1-2 段显式论证：(a) 为什么 Z3 formal verification 不同于 NL self-correction；(b) neurosymbolic 社区的隐含假设是什么；(c) 本文如何挑战该假设。
61	
62	**C5. SatLM 正面结果与 SICA 负面结果的对比不充分** [R2-N2, R1 部分 REBUT — 共识需扩展]
63	- SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 但报告正面结果。论文在 §2 中有 2 句话对比（specification-generation vs trace-extraction），但对理解"为什么 SatLM works 而 SICA doesn't"远不够充分。这个对比恰恰能强化论文论点：trace-level extraction 的 answer contamination 是结构性的。
64	- **必须**：在 §2 或 §7 中系统化展开 specification-generation / program-generation / trace-extraction 三种范式的对比。
65	
66	---
67	
68	### Warning（Should-Fix，影响评分但不一票否决）
69	
70	**W1. DRC τ 阈值无 held-out 评估** [R1-W1, R2 同意 — 共识]
71	- τ ∈ {0.3, 0.5, 0.7, 0.9} 均在同一 ProofWriter (n=600) 上选择和评估。作为第 4 个正式 contribution，"90% recovery at 39% cost" 可能 overfitted。
72	- 建议：dev/test split 或跨数据集 τ 验证，或显式标注 oracle selection。
73	
74	**W2. Cross-architecture NLI escape 适用面极窄** [R1-W2, R2-W5 — 强共识]
75	- BH 校正后仅 2/12 条件存活（均为 Mistral-7B ProofWriter）。NLI 仅适用于弱 generator + premise-conclusion 可分解 + verifier 强于 generator 的场景。LogiQA 无效。
76	- 建议：显式框定为 narrow PoC，讨论适用条件，避免暗示 general escape。
77	
78	**W3. 四种子复制方差大 + 统计功效 <21%** [R1-W3, R2 有 nuance 地同意 — 共识]
79	- Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp。Power analysis 显示所有确认性条件观测功效 <21%。R2 补充：四种子不是唯一证据支柱（还有 15 条件 FDR null + oracle + 27 策略失败），但 power limitation 应在主文更显著。
80	- 建议：在核心 claim 措辞中更明确承认 power limitation。
81	
82	**W4. TOST ±2pp margin 缺少显式理由** [R1-W4, R2 同意 — 共识]
83	- 未论证 2pp 为何是合适的实际意义阈值。NLP 领域缺乏共识，但至少应讨论 SC 文献中的典型改进幅度并展示不同 margin 下的 sensitivity。
84	
85	**W5. Bias Ratio 无置信区间** [R1-W5, R2 同意 — 共识]
86	- BR (4.97×, 3.93×, 2.88×) 缺 CI。Bootstrap CI 计算成本极低。无 CI 则无法判断跨模型 BR 差异是否显著。
87	
88	**W6. "Symbolic Confirmation Bias" 需与近期 CoT confirmation bias 工作区分** [R2-N3, R1 同意 — 共识]
89	- 近期 arXiv:2506.12301 和 arXiv:2604.02485 已研究 CoT confirmation bias。本文的特殊性——偏差在 Z3 satisfiability 验证后仍存在——需要更清晰地表述。
90	
91	**W7. Related Work 过度压缩** [R2-W2, R1 同意 — 共识]
92	- 三段 Related Work 将约 25 篇论文压缩为引用列表。Neurosymbolic 段混合 specification-generation / program-generation / trace-extraction 未分类。
93	
94	**W8. 27 种修复策略正文展示不足** [R2-W4, R1 同意 — 共识]
95	- §5.4 仅 5 行文字 + Figure 2 概览。作为核心论证环节应在正文增加代表性策略的分类讨论。
96	
97	---
98	
99	### Info（小问题，不影响接收）
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa3821a6-872e-4ab1-aa40-333463fc0ad3",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "9f4ded53-b66a-4ade-8f48-3d91aa1e7b52",
  "sourceToolAssistantUUID": "aa3821a6-872e-4ab1-aa40-333463fc0ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T14:17:17.477Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q5Eqv9EPwkzV4jKsGWzPea`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4ded53-b66a-4ade-8f48-3d91aa1e7b52",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHV3mzJvTkdnumZFWD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "690192c7-0d9a-4e15-9fc7-89660db5444c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HUxXr1tnboyYes57Hej6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 37312,
      "output_tokens": 878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1544
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 878,
          "cache_read_input_tokens": 37312,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1544,
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

_source line 23 · 2026-05-23T14:17:17.503Z_

<details><summary>↩ Tool result · `toolu_01Q5Eqv9EPwkzV4jKsGWzPea`</summary>

```text
1	---
2	round: 8
3	review_mode: fresh
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-21T08:03:10.601697+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# Round 11 审稿报告（Fresh Review）
12	
13	**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning
14	**Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验可靠性; R2: 新颖性+完整性+写作质量）
16	**流程**: Round 1 独立审稿 → 交叉分享 → 逐条 AGREE/REBUT → 收敛（1轮达成）
17	
18	---
19	
20	## Summary
21	
22	本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束、通过加权部分 MAX-SAT 聚合答案。在 6 个开源 LLM（7B-32B）、3 个逻辑推理数据集、3,000+ 条件评估上，作者发现自提取符号约束在任何已测试的模型能力水平上都无法改进 Self-Consistency。论文识别了"Symbolic Confirmation Bias"（BR=4.97×）和 process-level independence bottleneck（CoT cosine similarity 0.69 >> answer κ 0.46），证明 27 种 same-model remediation 策略全部失败。Oracle 控制实验确认聚合机制本身有效（+29.90pp, +14.22pp），瓶颈在 self-extraction 质量。Cross-architecture NLI 验证在 verifier 能力超过 generator 时产生显著增益（Mistral-7B +6.67pp, p<0.001），DRC 路由方法在 39% 成本下恢复 90% 增益。
23	
24	---
25	
26	## Strengths
27	
28	1. **实验设计的系统性前所未有**：6 models × 3 datasets × 27 strategies × oracle controls × cross-arch escape × 4-seed replication，覆盖面远超同类工作。穷举式搜索有效排除了"只是没找到正确配置"的反驳。
29	2. **统计方法论在 NLP 实证研究中属上乘**：McNemar + BH FDR + TOST 等价性检验 + Bootstrap CI + Power analysis 构成完整统计推断链。TOST 的使用（区分"无效果证据"和"证据不足"）值得肯定。
30	3. **Oracle 控制实验设计精妙**：FOLIO gold annotations + ProofWriter DSL 作为 oracle constraints，干净隔离了 extraction quality 和 aggregation mechanism，是论文最强的方法论贡献。
31	4. **"Symbolic Mirage" 概念框架完整**：包含三个可测试预测（BR>1 跨架构、same-model 无法突破 BR<1、only external verification escapes），全部被数据确认。
32	5. **K_eff 和 BR 诊断指标有方法论可复用价值**：将 Kish design effect 引入 LLM 投票分析，为社区提供了量化 same-model 独立性的工具。
33	6. **Case studies（Appendix G）提供机制性理解**：三个 discordant case 超越统计汇总数字。
34	7. **诚实的负面结果报告**：未为"正面故事"隐瞒负面发现，学术诚信值得肯定。
35	8. **Comprehensive appendix**：14 页附录含 prompt templates、pseudocode、ablation、error analysis，reproducibility 条件好。
36	
37	---
38	
39	## Weaknesses
40	
41	### Must-Fix（影响接收决定）
42	
43	**N1** [critical, consensus AGREE] **Spearman ρ=1.0 (n=6) 被过度使用，统计基础不足以承受论证权重**
44	- 6 个数据点中 4 个共享 DeBERTa verifier，违反 permutation test 的交换性假设，有效自由度仅 2-3。然而 "strongly monotonic ρ=1.0, p=0.003" 在论文中重复至少 7 次（Abstract, Introduction Contribution 2, Section 3.3, Section 6, Discussion×2, Conclusion）。这是论文从负面结果转向正面贡献的关键桥梁——如果统计基础不牢固，论文退化为纯粹的负面结果论文。
45	- **建议**：(1) 降级为 "consistent with a monotonic trend"；(2) 减少重复至 ≤3 次；(3) 增加 non-DeBERTa verifier；(4) 添加讨论 shared-verifier 对 p 值有效性的影响。
46	
47	**N2** [critical, consensus AGREE] **中心 claim 强度超出统计证据——标题和 Abstract 需限定范围**
48	- Abstract "do not improve majority voting at any capability level" 在 10/16 条件 underpowered（观测功效 <21%）的情况下是过强的否定命题。TOST 方法论本身是正确的（4 条件等价 + 2 条件负面 = 6/16 有实质证据），但措辞未反映 10/16 条件的 inconclusive 状态。同时标题未限定模型规模（仅测 7B-32B），而约束提取质量可能随规模提升。
49	- **建议**：(1) Abstract 改为 "we find no evidence of improvement, with equivalence established in four conditions and significant degradation in two"；(2) 标题加限定（如 "at the 7B-32B Scale"）。
50	
51	**N3** [critical, consensus AGREE] **TOST ±2pp 等价性 margin 缺乏 principled 论证**
52	- 跨 39-86% SC baseline 使用固定绝对 margin 不合理（39% baseline 的 2pp ≈5% relative vs 86% baseline 的 2pp ≈2.3% relative）。Sensitivity analysis（±1pp → 0 等价, ±3pp → 10 等价）显示等价结论对 margin 高度敏感。Lakens (2017) 要求基于 SESOI 的领域论证，论文未提供。
53	- **建议**：(1) 提供 margin 的 principled justification；(2) 考虑 relative margin（如 baseline 的 ±5%）；(3) 正文报告 sensitivity 结果。
54	
55	### Should-Fix（影响评分但不一票否决）
56	
57	**W1** [warning, consensus AGREE] **Proposition 1 / Observation 2 伪形式化——empirical claim dressed as math**
58	- "Bound 1" 中 "≲" 未定义，无证明推导；"Observation 2" 基于 n=6 经验观察但用了数学命题格式。建议改用 "Empirical Finding" 或 "Observation"，去除数学化包装。
59	
60	**W2** [warning, consensus AGREE] **DRC 评估不充分——不足以作为 Contribution 4**
61	- 仅在 ProofWriter 上完整评估；τ=0.7 在 evaluation set 上选择（过拟合风险）；3 个 verifier 全是 encoder-only MNLI-finetuned；未与 multi-agent debate 等方法对比。建议降级为 proof-of-concept 或增加 cross-dataset validation。
62	
63	**W3** [warning, consensus AGREE] **Single-seed 变异性与统计可靠性问题叠加**
64	- 4-seed 复现 Δ 从 +3.43 到 -0.49pp（range ≈4pp），完全覆盖 TOST ±2pp margin。多数条件 single-seed，Δ 可信度存疑。Single-seed + underpowered + margin-sensitive TOST 构成系统性可靠性风险。
65	
66	**W4** [warning, 分歧 — R2 critical / R1 rebut] **核心负面结果的增量新颖性定位需改善**
67	- R2 认为 SCB 可从 Huang/Stechly/Wan/Amonkar/Chan 组合预测；R1 反驳称 formal channel (Z3) failure 是 genuine surprise——99% 约束语法合法但语义偏差，与 NL self-correction 失败是不同 failure mode。双方共识：论文应在 Introduction 中更早、更明确地建立 formal channel 的额外假设和区分。
68	
69	**W5** [warning, 分歧 — R2 critical / R1 rebut] **Independence-Accuracy Trade-off 与经典 ensemble dilemma 的区分**
70	- R2 认为是 Krogh/Brown diversity-accuracy dilemma 的 CJT 语言重述；R1 认为 CJT 提供了 LLM-specific 量化工具（K_eff, BR, C_0）。双方共识：应明确声明贡献在于量化而非发现新 tradeoff。
71	
72	**W6** [warning, consensus partial] **BR 指标的循环论证倾向**
73	- R1 指出 "模型错时约束也错" 是 self-extraction 的定义性结果。R2 反驳称 magnitude (4.97×) 和 per-condition variation 有价值。共识：应定位为 "quantification of expected phenomenon" 而非 "discovery"，减少 BR=4.97× 的重复频次。
74	
75	**W7** [warning, consensus partial] **术语品牌化过度——"Independence Bottleneck" 接近 rebranding**
76	- R2 认为所有品牌化术语过多；R1 认为 "Symbolic Mirage"（有3个可测试预测）命名合理，但 "Independence Bottleneck" 确实是 Ladha (1992) correlated voting 的 rebranding。建议保留核心术语，降低次要术语的品牌化。
77	
78	**W8** [warning, R2 raised, R1 conditional agree] **Related Work 遗漏引用**
79	- Byerly & Khashabi (2026 TACL) "Self-Consistency Falls Short!" 和 arxiv 2506.07962 "Correlated Errors in Large Language Models" 高度相关但未引用。Related Work 部分段落以 citation listing 为主，缺乏 critical discussion。
80	
81	**W9** [warning, R1 raised, R2 partial rebut] **27 策略计数膨胀 + 未尝试 trained extractor**
82	- 含超参变体（T=0.3/0.5/0.7/1.0）和 n≤60 条件。R2 反驳称穷举论证仍成立。但双方同意 trained constraint extractor（如在 oracle annotations 上 SFT）是重要实验空白，应在 Discussion 中讨论。
83	
84	---
85	
86	## Reviewer Consensus
87	
88	以下问题两位 Reviewer 达成一致 [AGREE]：
89	
90	1. ρ=1.0 (n=6) 被过度使用，需降级描述并减少重复 [N1]
91	2. 标题/Abstract 需限定模型规模（7B-32B）[N2]
92	3. Abstract 措辞 "do not improve at any capability level" 过强 [N2]
93	4. TOST ±2pp margin 需 principled justification 和 sensitivity 分析 [N3]
94	5. DRC 评估不足（τ 过拟合、范围窄）[W2]
95	6. Single-seed 变异性构成系统性可靠性风险 [W3]
96	7. Proposition/Bound 应降级为 Empirical Finding [W1]
97	8. SCB 与 CoT confirmation bias 的区分应在 Introduction 前移 [W4]
98	9. 应声明 Independence-Accuracy Trade-off 贡献在量化而非发现 [W5]
99	
100	---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "690192c7-0d9a-4e15-9fc7-89660db5444c",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "14b59d1d-b985-47ac-9656-431c7b150a67",
  "sourceToolAssistantUUID": "690192c7-0d9a-4e15-9fc7-89660db5444c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-23T14:17:19.024Z_

Now let me read the remaining rounds:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b59d1d-b985-47ac-9656-431c7b150a67",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "427b89b2-b27d-417e-b635-0993570f5039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

_source line 25 · 2026-05-23T14:17:20.084Z_

<details open><summary>🔧 Tool call — Read · `toolu_017voob2D5tuHmuJ1hdbhsVX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_9.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "427b89b2-b27d-417e-b635-0993570f5039",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1b9d3a17-381f-4436-8c29-cf89c3a11e78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

### Tool result

_source line 26 · 2026-05-23T14:17:20.099Z_

<details><summary>↩ Tool result · `toolu_017voob2D5tuHmuJ1hdbhsVX`</summary>

```text
1	---
2	round: 9
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-22T01:20:27.502522+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# Round 12 审稿报告
12	
13	## Summary
14	
15	本文提出 SICA（Symbolic Invariant Consensus Aggregation），通过从 LLM 推理 trace 中自提取逻辑约束并用 MAX-SAT 聚合来扩展 Self-Consistency。核心发现是负面结果：自提取约束继承模型偏差（"symbolic confirmation bias"，BR=4.97×），27 种修复策略全部失败。跨架构 NLI 验证提供逃逸路径（ProofWriter +6.67pp），DRC 自适应路由方法恢复 83-90% 增益。实验规模令人印象深刻（11 模型、3 数据集、27 策略），oracle 控制设计精妙（+29.90pp），但核心新颖性不足、统计功效偏低、标题 overclaiming 制约了论文水平。
16	
17	## Strengths
18	
19	1. **实验规模和系统性出色**：6 个开源模型 + 5 个 frontier 模型、3 个逻辑推理数据集、27 种修复策略（12 principled + 15 参数变体）、4-seed replication、TOST equivalence tests——对负面结果论文来说覆盖面突出。[R1/R2 共识]
20	
21	2. **Oracle 控制设计精妙**：用 FOLIO/ProofWriter 的 gold FOL annotations 替换自提取约束，展示 +29.90pp/+17.17pp 增益，精确定位瓶颈在 extraction 而非 MAX-SAT/Z3 mechanism。自提取仅捕获 ~12% 的 oracle ceiling。这是论文最有说服力的部分。[R1/R2 共识]
22	
23	3. **CJT 框架提供清晰理论语言**：Condorcet Jury Theorem 的 independence assumption 解释了 SC plateau 和 SICA 失败，比纯经验描述更有洞察力。K_eff 作为 ordinal diagnostic 的定位恰当。[R2 首提，R1 同意]
24	
25	4. **诊断框架有实用价值**：C₀ < 5% 意味 SICA 退化为 SC、三类 failure mode（Type A/B/C）、process-level independence 分析——对后续研究有参考价值。[R1]
26	
27	5. **诚实的局限性披露**：论文在 Limitations 中详细讨论了统计功效、单 seed、capability-gap 分析弱点、计算成本等。学术诚信值得肯定。[R1/R2 共识]
28	
29	6. **BH 多重比较校正和 TOST 等价性检验**使用恰当，sensitivity 分析（±1/±2/±3pp margins, relative TOST）是良好的统计实践。[R1]
30	
31	## Weaknesses
32	
33	### Must-Fix（影响接收决定）
34	
35	**W1 [critical, 共识]** **标题 "Do Not Improve...from 7B to Frontier Scale" overclaiming**
36	- Frontier 模型（gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro）使用 Mistral-7B 做跨模型提取，不是 self-extraction。标题中 "Self-Extracted" 与 frontier 实验设计不匹配。
37	- 开源模型中 QwQ-32B 仅在退化条件（AIME n=22, GSM8K n=30, C₀<5%）上测试。有效实验范围集中在 7B-14B。
38	- **建议**：修改标题去掉 "to Frontier Scale" 或加限定词（如 "from 7B to 14B, with Cross-Model Evidence at Frontier Scale"）；Abstract/Introduction 明确区分 self-extraction 和 cross-model extraction。
39	- [R2 首提 N2, R1 AGREE]
40	
41	**W2 [critical, 共识]** **SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化**
42	- Huang et al. (2024) 已证明 LLMs cannot self-correct without external feedback；Stechly et al. (2025) 证明 self-verification 不可靠；Wan et al. (2025) / Jhaveri et al. (2026) 研究了 CoT confirmation bias。SCB 是同一机制在不同载体（FOL 约束 vs 自然语言）上的实例化，非概念突破。
43	- Z3 验证通道的 provable soundness 是有趣切入点（证明瓶颈在提取而非验证），但更接近实验发现而非概念突破。99% 约束通过 Z3 语法检查却仍无用——这一点比 SCB 本身更有趣，应在 framing 中更突出。
44	- **建议**：(1) 降低 Contribution 1 的 novelty claim 调门；(2) 重新定位贡献重心为量化诊断体系（BR=4.97×, K_eff, C₀）和实验规模（27 策略系统排除）；(3) 突出 formal channel 下 SCB 的 non-obvious 之处。
45	- [R2 首提 N1, R1 AGREE with nuance: 量化贡献不应低估]
46	
47	**W3 [critical, 共识]** **统计功效 <21% 无法支撑"无效果"核心结论**
48	- McNemar 在 n=200-600 条件下检测 |Δ|=2pp 效应的功效 <21%。16 个非退化条件中 10 个 TOST "underpowered"。最大研究（n=804）MDE=1.86pp，但观测 Δ=+0.25pp。
49	- 标题 "Do Not Improve" 将"检测不到效果"等同于"没有效果"，不被 power<21% 支撑。
50	- R2 补充 nuance：Abstract 正文措辞（"no evidence of improvement...ten conditions remaining underpowered"）实际较审慎；aggregate pattern（16/16 无显著正面）仍有信息量，可补充 meta-analytic sign test。
51	- **建议**：(1) 标题和 Contribution framing 使用更审慎措辞；(2) 报告各条件可排除的效应大小范围；(3) 补充 aggregate sign test。
52	- [R1 首提 N1, R2 AGREE]
53	
54	**W4 [critical, 共识]** **单 seed 复制严重不足**
55	- 唯一 4-seed 复制（Mistral-7B FOLIO）Δ 范围 +3.43 到 -0.49pp（~4pp 跨度），超过 TOST ±2pp 边界。温度敏感性也显示 T=0.7 是"孤立峰"。其他单 seed 条件可靠性存疑。
56	- R2 补充：aggregate pattern（16/16 无正面）在 seed variance 下仍有信息量——如果 SICA 真有 2-3pp 正效果，16 条件全无显著正面不太可能。建议补充 meta-analytic 分析。
57	- **建议**：至少对 3-4 个关键条件做多 seed 复制，或明确降低单 seed 结论强度。
58	- [R1 首提 N2, R2 AGREE]
59	
60	**W5 [critical, 共识]** **Capability-gap 分析证据过于薄弱**
61	- Spearman ρ=1.0, p=0.003, 但 n=6 且 4/6 共享 DeBERTa verifier。Verifier-collapsed 分析（n=3 独立 verifier）p=0.167，不显著。Process-κ gradient 也只有 n=5。
62	- Introduction/Conclusion 以 p=0.003 呈现，但 Limitations 承认 p=0.167——framing 不一致。
63	- **建议**：(1) 增加更多独立 NLI verifier 架构（≥5 独立 verifier）；(2) 正文中引用 p=0.003 时同步报告 collapsed p=0.167 作为 robustness check；(3) 使用 "consistent empirical pattern rather than statistically confirmed law" 的措辞（论文 Limitations 已有，需一致化到正文）。
64	- [R1 首提 N3, R2 AGREE = R2-W3]
65	
66	**W6 [critical, 共识]** **DRC 作为 Contribution 4 不够充分**
67	- DRC 本质是基于 trace agreement 阈值 τ 的 confidence-based routing，标准 cascade 设计。τ=0.7 仅在 2 个数据集验证（ProofWriter 选择, FOLIO held-out），τ 敏感性分析缺失。
68	- full-combo gain 本身仅在 Mistral-7B（最弱模型）上显著；对更强模型 full-combo 就不显著，DRC 无从发挥。
69	- **建议**：将 DRC 降级为 §6 的 practical observation，不作为独立 Contribution 编号；或增加 routing 策略对比和 τ 敏感性分析。
70	- [R2 首提 N3, R1 AGREE]
71	
72	### Should-Fix（影响评分但不一票否决）
73	
74	**S1 [warning, 共识]** **BR 可能存在循环论证**
75	- 56.4% 约束零变量重叠，约束几乎按定义"支持"source trace 的答案。BR=4.97× 中多少是提取设计产物 vs 模型级 bias 未被区分。
76	- **建议**：做控制实验——随机 shuffle 约束-trace 映射后计算 BR，量化 "design artifact" 成分比例。
77	- [R1 首提 W1, R2 AGREE: 重要遗漏]
78	
79	**S2 [warning, 共识]** **CIL 名称和 information-theoretic 声称有误导**
80	- "Cumulative Information Lift" 实际是 log-odds ratio，非互信息/KL 散度。"Cumulative" 无体现。"unify" 过强（仅经验相关，无数学推导关联 K_eff/BR）。n=8 非独立样本上 ρ=0.881 可能受 outlier 影响。
81	- **建议**：重命名为 "Conditional Correction Ratio" 或类似；删除 "unify" 措辞；添加 leave-one-out sensitivity。
82	- [R1 首提 W2, R2 AGREE]
83	
84	**S3 [warning, 共识]** **Independence-Accuracy Trade-off（Contribution 2）framing 问题**
85	- K_eff 是 Kish design effect 的直接应用，BR 是条件概率比，C₀ 是 zero-cost filter。各自简单直观，价值在组合应用到 LLM 自提取场景，更像 Contribution 1 的量化工具集。
86	- **建议**：将 Contribution 2 重新措辞为"量化诊断工具集"，降低 "trade-off" 的发现性措辞。引用 Krogh & Vedelsby (1994) 明确不是新发现。
87	- [R2 首提 W1, R1 AGREE]
88	
89	**S4 [warning, 共识]** **Figure 2（27 strategies summary）placement 问题**
90	- 在 §5.6（page 7）引用但实际出现在 page 25。核心贡献的视觉支撑不应在 appendix。
91	- **建议**：调整 LaTeX placement 确保 Figure 2 出现在 §5.6 附近。
92	- [R2 首提 W4, R1 AGREE; 视觉审查也确认]
93	
94	**S5 [warning, 共识]** **Appendix ~18 页，关键信息分配不合理**
95	- Table 15（frontier SCB, 9 models）支撑标题级 claim 却在 appendix。主文 8 页仅 3 个 display items（1 figure + 2 tables），密度偏低。
96	- **建议**：合并 Discussion+Conclusion 省空间；将 Table 15 和 capability-gap scatter plot 移入正文；精简 Case Studies 和 Extraction Error Taxonomy。
97	- [R2 首提 W5, R1 AGREE; 视觉审查也确认]
98	
99	**S6 [warning, 分歧]** **27 策略 scope 限定——排除 trained extractor**
100	- R1 观点：Oracle +29.90pp 显示 trained extractor 最有前途，排除后 "all fail" 有误导。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b9d3a17-381f-4436-8c29-cf89c3a11e78",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "b0fa3282-d4df-42f4-aa5c-872c4b6fab7f",
  "sourceToolAssistantUUID": "1b9d3a17-381f-4436-8c29-cf89c3a11e78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T14:17:20.478Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MQKvySTYUP2qmjYM6RvfiH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_10.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0fa3282-d4df-42f4-aa5c-872c4b6fab7f",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71ac8ec6-2a23-4032-8eb9-7e677f83855d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

### Tool result

_source line 28 · 2026-05-23T14:17:20.485Z_

<details><summary>↩ Tool result · `toolu_01MQKvySTYUP2qmjYM6RvfiH`</summary>

```text
1	---
2	round: 10
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-22T08:01:19.264516+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# Consolidated Review Report — Round 10 (Fresh)
12	
13	**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning"
14	**Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**Reviewer Panel**: 2 Reviewers (R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量)
16	**审稿模式**: 圆桌多轮（Round 1 独立审稿 → 交叉分享 → 收敛，1轮完成）
17	
18	---
19	
20	## Summary
21	
22	本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取逻辑约束并通过加权 partial MAX-SAT (Z3) 聚合答案，试图突破 Self-Consistency (SC) 的多数投票瓶颈。在 6 个开源模型 (7B–32B)、3 个逻辑推理领域 (FOLIO, ProofWriter, LogiQA)、3,000+ 条件评估（~1,250 unique instances）中，未发现统计显著的改善。论文将失败归因于 Symbolic Confirmation Bias (SCB)：自提取约束系统性支持模型多数答案（BR 1.05–4.97×），MAX-SAT 在 94.4% 情况下退化为简单计数。27 种无训练修复策略均失败。跨架构 NLI 验证 (DeBERTa) 在 ProofWriter 上获得 +6.67pp (p<0.001)。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 实验规模和系统性为负面结果论文树立标杆。** [R1-S1, R2-S1 共识] 6 个主模型 + 5 个 frontier 模型，3 个推理领域，~1,250 unique 实例，4-seed 复制，27 种修复策略——远超典型负面结果论文的评估力度。
29	
30	**S2. 实验控制设计精巧。** [R1-S2 主导，R2 认可] Oracle control (§4.3) 用 gold 约束证明 MAX-SAT 机制本身有效 (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter)，精准定位瓶颈在约束质量。Shuffle control (§5.2) 证明 SCB 是结构性偏差（BR_shuffle ≈ BR_real, p>0.7）。Cross-model extraction 扩展到 9 个模型确认 SCB 普遍性。
31	
32	**S3. 诊断框架有独立复用价值。** [R1-S3, R2-S2 共识] BR、CCR (Eq. 7)、K_eff 构成可复用的诊断工具包，可评估任何"自提取+聚合"范式。CCR > 0 vs. CCR < 0 清晰分离了跨架构 vs. 同模型条件。
33	
34	**S4. CJT 理论框架提供原则性解释。** [R1-S4, R2-S3 共识] 将 SC/SICA 放在 Condorcet Jury Theorem 框架下，K_eff 将"有效独立样本数"量化（K_eff = 1.2–3.6 for nominal K=12），为理解采样收益递减提供了理论支撑。
35	
36	**S5. 叙事层次超越多数负面结果论文。** [R2-S5 主导，R1 认可] 不是简单报告"方法 X 不 work"，而是：机制性解释 (SCB) → 理论框架 (CJT violation) → 可操作诊断 (K_eff, BR, C₀) → 初步逃逸方案 (cross-architecture NLI)。
37	
38	**S6. 附录质量极高。** [R2-S4, R1 Reproducibility 4/5] 14+ 页附录含完整 prompt 模板、MAX-SAT 算法伪代码、per-condition 统计分析、case studies、failure mode taxonomy。
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（影响接收决定）
45	
46	**MF1. [CRITICAL] 摘要 BR 数值选择性报告，有夸大嫌疑。** [R1-N1, R2 AGREE]
47	- 摘要报告 "bias ratio 4.97×" 和 "83.3%"——来自 Mistral-7B/FOLIO 这一最极端条件
48	- Table 2 (p7) 实际 BR 范围：Mistral-7B 4.97 → o3 1.66 → Gemini-2.5-Pro 2.79（注：frontier 模型使用 cross-model extraction，非 self-extraction）
49	- 摘要应报告中位数或范围（如 "BR ranges from 1.66 to 4.97"），而非最极端值
50	- Frontier 模型 BR 相对较低，暗示 SCB 严重性可能与模型能力负相关——论文的 "universal" framing 需更强限定
51	
52	**MF2. [CRITICAL] 统计功效呈现不足，"No Evidence" 声明与统计结论存在张力。** [R1-N2 + R2-N2，完全共识]
53	- 16 个非退化条件中 10 个 underpowered（MDE > 2pp at 80% power）
54	- TOST 仅确认 4/16 条件等价于零效应
55	- Aggregate sign test 8+/15− (p=0.21) 是"inconclusive"而非"negative"
56	- Power analysis (Appendix E Table 6) 是关键信息但被埋在附录中
57	- 标题 "Show No Evidence" 在日常学术用语中可被理解为"效果已被排除"，但论文只是"未检测到显著效果"——且部分条件下检测力不足以区分无效果与小正效果
58	- **必须修改**：§4.2 增加明确 power statement（如 "For the 10 underpowered conditions, we cannot rule out effects smaller than ±X pp"）；将 MDE 核心数字从附录提到正文
59	
60	**MF3. [CRITICAL] α=0.5 参数无敏感性分析。** [R1-N3 主导，R2 AGREE with nuance]
61	- α=0.5 控制约束权重与投票权重的相对影响
62	- 94.4% MAX-SAT≡count-only 的核心发现可能依赖于 α 的特定取值
63	- R2 认为影响可能有限（当 BR>1 时约束方向与投票一致，α 调整不影响最终选择），但缺少实验验证
64	- **必须修改**：在 2–3 个代表性条件（高 BR + 低 BR）上跑 α∈{0.1, 0.3, 0.7} 消融，报告退化率变化
65	
66	### Should-Fix（影响评分但不一票否决）
67	
68	**SF1. Discussion/Conclusion 过于压缩。** [R2-W2, R1 AGREE]
69	- §7 (p8) 不到半页，缺少：(1) SCB 与 CoT unfaithfulness 关系讨论，(2) 对 neuro-symbolic 实践者的可操作建议，(3) test-time scaling 含义展开
70	- 视觉审查发现 Discussion 约 3–4 行溢出到 page 9 顶部——需压缩或重排
71	
72	**SF2. 符号/指标过载。** [R2-W1, R1 AGREE]
73	- 8 页正文引入 7 个定量工具（K_eff, κ, BR, C₀, CCR, ProcessSim, ρ_same），认知负担重
74	- 建议：ProcessSim (§5.3) 和 CCR (§5.4) 移至附录，正文聚焦 K_eff/BR/C₀ 三个核心指标
75	
76	**SF3. 跨架构 NLI claim 须限定到命题逻辑任务。** [R1-W1, R2 部分涉及]
77	- FOLIO 和 ProofWriter 均为命题/一阶逻辑任务，NLI 模型天然对齐 textual entailment
78	- 未在 StrategyQA、LogiQA 等非逻辑域测试 NLI 验证
79	- 摘要应限定为 "on propositional-logic benchmarks"；§6 或 Limitations 讨论 domain limitation
80	- 注：R2 初审误称"仅一个验证器"，R1 交叉纠正（实际 3 个 NLI 架构 × 4 generators × 5 weights），证据规模比 R2 初判更充分
81	
82	**SF4. TOST ±2pp margin 缺乏独立论证。** [R1-W4, R2 AGREE]
83	- 用 SC 自身效应量定义"可忽略"有循环性
84	- ±3pp 时所有条件均 equivalent——结论对 margin 敏感
85	- 建议引用领域公认的最小实际意义差异，或提供 margin sensitivity analysis
86	
87	**SF5. 语法去重可能系统性膨胀 BR。** [R1-W2, R2 AGREE]
88	- 语义等价但语法不同的约束被分别计数（去重率仅 46.0%）
89	- 论文有 shuffle control 部分回应（BR_shuffle ≈ BR_real），但未报告 Z3 语义去重后 BR
90	- 建议补充语义去重后 BR 值
91	
92	**SF6. Table 1 核心结果表可读性不足。** [R2-W4, R1 小问题#1 一致]
93	- Type A/B/C 子区域分隔视觉层次不够，显著性标记系统复杂
94	- 建议增加水平线分隔或浅色底纹；简化显著性标记
95	
96	**SF7. "Symbolic Mirage Hypothesis" 定位不一致。** [R2-W3, R1 AGREE 低严重性]
97	- §3.3 提出假设，§5 直接以结论性措辞使用，缺显式验证回溯
98	- 建议 §5 结尾增加总结段，显式对应三个 testable predictions
99	
100	**SF8. 4-seed replication 充分性存疑。** [R1-W5, R2 PARTIALLY AGREE]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71ac8ec6-2a23-4032-8eb9-7e677f83855d",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "ec7b2a90-6d7a-45f9-96eb-59b4030673ac",
  "sourceToolAssistantUUID": "71ac8ec6-2a23-4032-8eb9-7e677f83855d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T14:17:20.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VErkA4MxVZUFZERtzX8xeY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_11.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec7b2a90-6d7a-45f9-96eb-59b4030673ac",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8e320e7-1c93-4f7f-be2f-1288ee4c97a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

### Tool result

_source line 30 · 2026-05-23T14:17:20.726Z_

<details><summary>↩ Tool result · `toolu_01VErkA4MxVZUFZERtzX8xeY`</summary>

```text
1	---
2	round: 11
3	review_mode: fresh
4	overall_score: 3.5
5	timestamp: 2026-05-22T13:40:33.147709+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 14 (Fresh)
12	
13	**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning
14	**Venue**: EMNLP 2026 (ARR May 2026)
15	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析；R2: 新颖性+完整性+Related Work+写作质量）
16	**审稿模式**: Fresh（重新审稿，无历史轮次记忆）
17	
18	---
19	
20	## Summary
21	
22	本文研究 Self-Consistency (SC) 的一个零成本扩展——Symbolic Invariant Consensus Aggregation (SICA)，从推理链中提取逻辑约束并用 MAX-SAT (Z3) 选择最佳答案。在 6 个开源 LLM（7B–32B）+ 9 个模型（含 frontier）、3 个逻辑推理数据集、3000+ 条件评估上，论文发现 SICA 无显著改善（aggregate sign test: 5+/10−, p=0.30），并将失败归因于 Symbolic Confirmation Bias (SCB)：83.3% 的自提取约束支持错误多数答案（BR 1.66×–4.97×），MAX-SAT 在 94.4% 的问题上退化为 majority voting。论文提出三个诊断工具（K_eff, BR, C₀），测试了 27 种 training-free 补救策略（全部失败），并通过 cross-architecture NLI 验证证明外部验证可打破瓶颈（+6.67pp ProofWriter, p<0.001）。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 统计方法论异常扎实。** McNemar exact test + BH FDR correction + TOST equivalence test + Bootstrap CI + Power analysis 构成四重互补检验体系。10 个 underpowered 条件的 MDE 被透明报告（Appendix E），体现统计诚实性。在负面结果论文中达到极高水准。[R1 S1, R2 S1, 共识]
29	
30	**S2. 实验规模和系统性覆盖令人信服。** 6 模型 × 3 数据集 × ~3000 condition-evaluations，覆盖 7B–32B 能力谱。Oracle control (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter) 有效分离 mechanism soundness 与 extraction quality，将问题精确定位到约束提取环节。[R1 S2, R2 S1, 共识]
31	
32	**S3. 结构性归因超越简单否定。** Shuffle control（BR_null ≈ BR_obs, p>0.7）、process-level independence analysis（ProcessSim 0.69 vs κ 0.46）、CCR 分析（cross-arch CCR>0 vs same-model CCR<0）系统解释了*为什么*失败。这不是"一个方法不行"而是对失败机制的量化诊断。[R1 S3, R2 S2, 共识]
33	
34	**S4. 补救分析近乎穷举。** 27 种 training-free 策略跨 4 类（prompt/method/trace-filtering/scoring）系统测试，全部 neutral-to-negative，显著增强了负面结论的说服力。[R1 S4, R2 S3, 共识]
35	
36	**S5. 叙事结构清晰自洽。** CJT 理论 → SICA 方法 → 负面实验 → SCB 诊断 → Symbolic Mirage 形式化 → remediation 失败 → cross-arch escape，逻辑链完整。[R1 S5, R2 S5, 共识]
37	
38	**S6. 附录详尽（~19 页）。** Case studies、prompts、algorithms、ablations、统计分析齐全。[R1 implied, R2 S5, 共识]
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（影响接收决定）
45	
46	**N1. [critical, 共识] 标题声明范围显著超出实验证据覆盖面。**
47	标题说"LLM Reasoning"但全部主实验仅覆盖逻辑推理（FOLIO/ProofWriter/LogiQA）。数学推理（GSM8K）仅 n=30 pilot，StrategyQA/ARC-Challenge 仅出现在附录诊断中。当前社区对 symbolic verification 的主要兴趣在数学推理领域——标题 overclaim 是 *ACL 审稿常见降分理由。
48	- **R1**: critical（首提）
49	- **R2**: major（W4），交叉后同意 R1
50	- **建议**: 标题改为"Formal/Logical Reasoning"，或补充 GSM8K/MATH 中等规模实验（n≥200）
51	
52	**N2. [critical→major, 共识] Symbolic Mirage Hypothesis 的验证存在部分循环论证。**
53	三个 predictions 中，Prediction 1（BR>1 across architectures）和 Prediction 2（no same-model intervention reduces BR below 1）本质上是对已观察数据的事后总结。只有 Prediction 3（cross-architecture escape）涉及独立数据。
54	- **R1**: major（N2, 首提循环论证角度）
55	- **R2**: critical（N1, 从新颖性角度；交叉后同意循环论证观点，但指出 Pred1 覆盖 9 模型超出初始 3 个为缓和因素）
56	- **建议**: 将 Pred 1-2 重定位为"observations that motivate the hypothesis"，仅 Pred 3 为 genuine prediction。降低"Hypothesis"措辞为"Diagnostic Framework"或"Empirical Pattern"
57	
58	### Should-Fix（影响评分但不一票否决）
59	
60	**W1. [major, 共识] Cross-architecture escape 证据不足以支撑结论强度。**
61	仅 6 个条件（4 generators × 1 dataset significant），单一 verifier 类型（NLI），仅 Mistral-7B 组合达到统计显著（+6.67pp, p<0.001）。NLI 三分类与 MAX-SAT 约束验证在任务性质上有本质区别，论文未充分讨论此 task gap。Capability gap 的单调性基于 n=6 数据点（共享 verifier 后有效 n 更小），Limitations 已标注 p=0.167。
62	- **R1**: major（W1）
63	- **R2**: major（W2），交叉后完全同意
64	- **建议**: 增加 generator/verifier 组合；讨论 NLI vs 约束逻辑验证的 task gap；结论措辞软化为"preliminary evidence"
65	
66	**W2. [major, 共识] 8 页正文信息过载，关键贡献展开不足。**
67	§5.5（Remediation）仅 ~15 行总结 27 种策略；§6（Cross-Architecture）约半页完成方法+结果+分析；§7（Discussion）被压缩在 page 8 底部约 1/3 页，design principles 各仅一句话。
68	- **R2**: critical（N2, 首提）
69	- **R1**: 同意但降级为 major（8 页硬限制下空间约束真实存在）
70	- **建议**: 压缩 §3.1 CJT/K_eff 推导（非原创公式），将 ProcessSim/CCR 细节移入附录，腾出空间给 §5.5 深度分析 3-5 种代表性策略和 §7 Discussion
71	
72	**W3. [major, 部分分歧] Claim scope 与统计功效不完全匹配。**
73	Abstract "no evidence of improvement" 暗示 SICA 确实无效，但 16 个非退化条件中 10 个 underpowered（MDE>2pp at 80% power），仅 4 个通过 TOST 等价检验。
74	- **R2**: major（W1）
75	- **R1**: REBUT——"no evidence"是统计学标准用语（absence of evidence），sign test + bootstrap CI + oracle control + 27 remediation 构成多层证据汇聚。但同意 Abstract 可增加 hedge。
76	- **建议**: Abstract 增加 power caveat，如"with Y conditions remaining underpowered for effects below ~2pp"
77	
78	**W4. [moderate, 共识] BR 计算子集大小（n_err）未报告。**
79	高准确率模型（SC>80%）上错误子集可能<40题（Gemini-2.5-Pro interim n_err≈12），BR 统计可靠性存疑。
80	- **R1**: moderate（W3）
81	- **R2**: 同意
82	- **建议**: Table 2 增加 n_err 列
83	
84	**W5. [moderate, 共识] Fleiss' κ 作为 ICC 近似仅有中等经验验证（r=0.625）。**
85	高准确率时 Fleiss' κ 系统性偏低（prevalence paradox），可能高估 K_eff。
86	- **R1**: moderate（W2）
87	- **R2**: 同意，但指出论文已声明 ordinal diagnostic
88	- **建议**: 报告 ICC 直接计算值作 robustness check
89	
90	**W6. [minor-to-major, R2 首提] Related Work 遗漏近期重要工作。**
91	SETS (2025, self-verification 正面效果) 与本文负面发现形成直接对比但未被讨论。MAV (2025, multi-agent verification) 与 §6 高度相关。
92	- **R1**: 部分同意（需注意 concurrent submissions）
93	- **R2**: minor-to-major（W5）
94	- **建议**: §2 增加 SETS 等工作讨论，明确本文负面结论的适用边界
95	
96	**W7. [minor, 共识] TOST equivalence margin ±2pp 选择依据不够充分。**
97	论文已有 margin sensitivity（±1/2/3pp），但正文呈现不够显著。
98	- **建议**: 在 §4.2 增加 margin sensitivity 结果摘要
99	
100	### 小问题（不影响接收）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8e320e7-1c93-4f7f-be2f-1288ee4c97a7",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "25c0f362-4ada-48b4-b9b7-2fa218711998",
  "sourceToolAssistantUUID": "f8e320e7-1c93-4f7f-be2f-1288ee4c97a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T14:17:21.116Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qmhhio3PCiJBYckVi51DKM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_12.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25c0f362-4ada-48b4-b9b7-2fa218711998",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1cdcca37-7361-4bc1-bc18-0d5bacb272fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

### Tool result

_source line 32 · 2026-05-23T14:17:21.123Z_

<details><summary>↩ Tool result · `toolu_01Qmhhio3PCiJBYckVi51DKM`</summary>

```text
1	---
2	round: 12
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-23T00:52:46.372005+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 15 (Fresh)
12	
13	**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning
14	**Venue**: EMNLP 2026 via ARR (May cycle)
15	**截止日期**: 2026-05-25
16	**审稿模式**: Fresh (2 Reviewers × 1 Round + 交叉分享)
17	
18	---
19	
20	## Summary
21	
22	本文系统评估了 LLM 自提取符号约束（SICA pipeline: trace → FOL constraint extraction → Z3 MAX-SAT → scoring）能否突破 Self-Consistency (SC) 投票天花板。在 6 个开源模型（7B–32B）× 3 个逻辑推理数据集上的 3,000+ condition-evaluations 显示 SICA 未能显著超越 SC（aggregate sign test: 8+/7−, p=1.00; McNemar + BH 校正后无一显著）。作者将此归因于"Symbolic Confirmation Bias" (SCB)：自提取约束是模型分布先验的投射（BR 1.66–4.97×），shuffle 控制证实偏差具有结构性。论文贡献了三个诊断指标（K_eff, BR, C₀）和跨架构 NLI 验证的概念验证。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 评估规模出色**
29	3,000+ condition-evaluations 覆盖 6 个开源模型 + 5 个 frontier 跨模型提取、3 个核心逻辑推理数据集 + 3 个探索性数据集。27 种 training-free remediation 策略的穷举排查。在负面结果论文中属于罕见的覆盖度。[共识]
30	
31	**S2. 多重收敛证据策略**
32	不依赖单一统计检验：符号检验 + McNemar + BH 校正 + Bootstrap 95% CIs + TOST 等价检验 + BR 机制分析 + ProcessSim 过程独立性 + Oracle 控制。这种三角验证方法论值得肯定。[共识]
33	
34	**S3. Shuffle 控制设计精巧**
35	§5.2 打乱 constraint-answer 配对后 BR_shuf ≈ BR_orig (p > 0.17)，令人信服地证明偏差来自 trace-count 分布（结构性）而非提取质量本身。这是本文方法论上最亮眼的设计。[共识]
36	
37	**S4. Oracle 控制精确定位问题**
38	Oracle SICA 在 Mistral-7B FOLIO 上 +29.90pp，证明约束聚合方法在获得高质量约束时有效，将问题精确定位到自提取环节而非 pipeline 本身。[R1 提出, R2 认可]
39	
40	**S5. 诊断框架有泛化价值**
41	K_eff、BR、C₀ 三个指标定义清晰（Eq. 1-5），可直接应用于任何 trace-aggregation 方法的事前评估。C₀ 作为退化条件零成本检测器正确分类全部 60 个条件。[共识]
42	
43	**S6. 附录极其详尽，可复现性优秀**
44	27 页中 18 页附录，覆盖 prompt 模板、Z3 伪代码、case study、oracle control、failure mode 分类、温度敏感性、多种子复现等。[共识]
45	
46	---
47	
48	## Weaknesses
49	
50	### Must-Fix (影响接收决定)
51	
52	**W1 [critical/major, 共识] 统计功效不足 vs "Fail to Improve" claim 强度**
53	全部 10 个非退化条件 observed power < 21%（Table 6, Appendix E），MDE 远大于观测效应量。Bootstrap 95% CIs 区间宽度达 ±1.5–2pp（Table 7），无法排除 ±1pp 级别的真实正效应。标题 "Fail to Improve" 表述为 evidence of absence，但实际证据仅支持 absence of evidence。R1 视为 critical，R2 视为 major（论文有 oracle/shuffle/SCB 机制等多重收敛证据部分缓解），两位均同意标题和 Abstract 需弱化措辞。
54	
55	→ **建议**: 标题改为 "No Evidence That..." 或 "Limitations of..."；Abstract 增加 power caveat（"observed power < 21% for individual conditions; our conclusion rests on converging evidence across..."); 主文 §4.2 增加对功效局限性的显式讨论。
56	
57	**W2 [major, 共识] SCB 概念独立性不足——与 CoT confirmation bias 机制同构**
58	SCB 的因果链（distributional prior → biased self-generated output → downstream confirmation）与 Wan et al. (ACL Findings 2025) 的 CoT confirmation bias 在机制层面同构。论文 §2 仅用一句话区分，未充分论证 SCB 作为独立概念的必要性。R1 交叉回应中同意此判断，但补充 SCB 的贡献在于量化该偏差在形式化验证管道中的具体表现（BR 1.66–4.97×）以及证明 Z3 solver 的 provable soundness 无法弥补 input 偏差。
59	
60	→ **建议**: §2 或 §3.3 坦诚承认与 CoT confirmation bias 的机制同构性，将 SCB 定位为该现象在符号约束管道中的特例和实证深化，而非独立概念。
61	
62	**W3 [major, 共识] 多种子复制极其有限**
63	仅 Mistral-7B（3 seeds, σ=±2.70pp）和 Qwen2.5-14B（4 seeds）进行了多种子复制。种子间方差已超过大多数观测效应量（|Δ| < 2pp），其余 4 个模型单种子运行。在种子方差未充分量化下报告精确 Δ 值有虚假精度之嫌。
64	
65	→ **建议**: 至少再对 2 个模型补充 3-seed 复制；或在主文诚实讨论单种子结果的局限性，将 Δ 值呈现附带种子不确定性范围。
66	
67	**W4 [major, 共识] §6 跨架构 NLI escape 证据偏薄，结论外推过度**
68	显著增益仅出现在 Mistral-7B（SC < 40%，最弱模型），4/6 main conditions 共享 DeBERTa 系列 verifier。§6 claim "generators up to SC ≈ 70%" 无数据支撑——实际验证仅覆盖 SC < 40%。Table 3 显示强生成器（Qwen2.5-14B, SC > 70%）无显著改善。
69	
70	→ **建议**: claim 限定为 "works on weak generators (SC < 40%)"；"SC ≈ 70% 阈值" 改为 suggestive observation；§7 的实践建议相应弱化。
71	
72	### Should-Fix (提升论文质量)
73	
74	**W5 [major, 共识] K_eff 作为贡献的新颖性 overstated**
75	K_eff = K/[1+(K−1)·κ] 是 Kish (1965) effective sample size 的直接应用（论文自引 Kish 1965）。将其称为 "general diagnostic framework"（Contribution 2）夸大了方法论创新。R1 补充指出 Fleiss' κ→ICC 近似在高 prevalence 下受 paradox 影响（K_eff 偏高）。
76	
77	→ **建议**: Contribution 2 重新定位为 "application of established diagnostics to LLM trace-aggregation evaluation"。
78	
79	**W6 [major, 共识] Independence-accuracy trade-off 未与 ensemble learning bias-variance 文献建立联系**
80	§6 的权衡（独立但较弱的 verifier 引入更多 variance 但降低 correlated bias）是 ensemble learning 经典 bias-variance tradeoff。论文引用了 Krogh & Vedelsby (1994) 但未讨论对应关系。缺引 Lakshminarayanan et al. (2017) Deep Ensembles。
81	
82	→ **建议**: §6 或 §7 显式建立与 ensemble diversity 文献的联系。
83	
84	**W7 [major→部分共识] Symbolic Mirage Hypothesis 的 Predictions post-hoc 性质**
85	R1 认为 Predictions 1-2 均为事后构造；R2 部分反驳——P1（结构性独立验证打破 SCB）是 out-of-sample prediction（§6 用全新实验设计验证），P2（MAX-SAT ≈ count-only, 94.4%）确实是 SCB 假说的同义反复。
86	
87	→ **建议**: P2 重定位为 "diagnostic observation"；P1 的 prediction 框架可保留；在 §3.3 明确标注 exploratory/post-hoc 性质。
88	
89	**W8 [major, 共识] BR 指标存在部分循环论证——措辞混淆结构性局限与提取质量问题**
90	当多数答案错误时，更多 trace 产生错误答案 → 更多约束来自这些 trace → BR > 1 部分是 trace-count 不平衡的数学必然。Shuffle 控制实际确认了这一点（BR_real ≈ BR_shuf），但论文措辞时而暗示"提取质量"问题，时而作为"结构性局限"证据。两位 Reviewer 共识：核心论点成立（自提取约束不提供超越 trace 分布的独立信号），但需更精确区分 BR 的两个组成部分。
91	
92	→ **建议**: 明确区分 (a) BR 中由 trace-count 不平衡导致的 trivial 分量 与 (b) 约束未能提供超越 trace 分布的独立信号（non-trivial 发现）。
93	
94	**W9 [minor-major, 共识] Abstract 中 BR 1.66–4.97× 选择性报告**
95	仅给出 min-max 范围，未提供中位数或均值。4.97× 可能是单一异常值。定性结论（BR 全 > 1）不受影响，但数值呈现有 cherry-picking 之嫌。
96	
97	→ **建议**: Abstract 报告中位数或 IQR 而非 min-max。
98	
99	### Nice-to-Fix (次要改进)
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cdcca37-7361-4bc1-bc18-0d5bacb272fc",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "7f6b2544-3bb1-4149-a581-5060f898abb4",
  "sourceToolAssistantUUID": "1cdcca37-7361-4bc1-bc18-0d5bacb272fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T14:17:21.353Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NrUMWGJ3WH4kVExMQhQ4yc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_13.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f6b2544-3bb1-4149-a581-5060f898abb4",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5bd8879e-0fc9-481c-8f1f-c34fdcb22fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

### Tool result

_source line 34 · 2026-05-23T14:17:21.361Z_

<details><summary>↩ Tool result · `toolu_01NrUMWGJ3WH4kVExMQhQ4yc`</summary>

```text
1	---
2	round: 13
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-23T08:27:17.176743+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 16 (Fresh)
12	
13	**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning
14	**Venue**: EMNLP 2026 ARR
15	**审稿模式**: Fresh（重新审稿，无上轮记忆）
16	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+Related Work+写作质量+Claims合理性）
17	**交叉轮次**: 1 轮交叉分享 + 逐条 [AGREE]/[REBUT] 回应，关键问题已收敛
18	
19	---
20	
21	## Summary
22	
23	本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取一阶逻辑约束，经去重后用 weighted partial MAX-SAT（Z3 求解）选择答案。核心发现为 null result：尽管 Z3 验证 99% 的自提取约束有效，SICA 在 6 个模型（7B–32B）、3 个推理数据集上与 majority voting 结果几乎一致（94.4% 问题答案相同），FDR 校正后无显著正效应。论文提出"Symbolic Confirmation Bias"概念（自提取约束系统性偏向模型多数答案），通过 Proposition 1（source-attribution 退化 + DPI information ceiling）给出理论论证，测试 27 种 training-free 修复策略均失败，并初步探索 cross-architecture NLI 验证作为突破路径。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 实验规模和系统性达到顶会标准。** 9 个模型 × 3 个数据集 × 60 个非退化条件 × 27 种修复策略的实验矩阵，附录 18 页包含详尽的 ablation（K sensitivity、temperature、multi-seed、oracle、error taxonomy、constraint ablation、entropy decomposition）。这种彻底性对 negative result paper 至关重要。[共识]
30	
31	**S2. Oracle 控制实验设计精巧。** 用 gold FOL annotations 替换自提取约束后，FOLIO 上获得 +29.90/+13.73pp 的显著提升（Mistral-7B/Qwen2.5-14B），精确分离方法论有效性与提取质量，定位瓶颈在 extraction 而非 verification/aggregation。[共识]
32	
33	**S3. 统计方法论多层次且诚实。** McNemar exact test + BH FDR 校正、bootstrap 95% CI（Table 7）、power analysis（Appendix D）、TOST equivalence test（Appendix U）、shuffle control（§5.1）。明确报告 observed power < 21%，承认 "absence of evidence is not evidence of absence"。这种统计诚实性在 NLP 社区中少见。[共识]
34	
35	**S4. 诊断框架有潜在实用价值。** 三个 zero-cost diagnostics（C₀, K_eff, BR）从 K=12 pilot run 即可预测 trace-aggregation 方法是否有帮助，为实践者提供部署前筛选工具。Table 5 的 per-condition diagnostics 具体可操作。[共识，但泛化性存疑——见 W3]
36	
37	**S5. Cross-architecture escape 提供建设性方向。** 不仅报告负面结果，还识别了 capability-gap 条件下 DeBERTa verifier 的显著提升路径（Mistral-7B 上 +6.67pp, p < 0.001），domain-adapted fine-tuning 进一步放大至 +12.67pp。[共识]
38	
39	**S6. 附录极为详尽，可复现性强。** Prompt 模板（Appendix A）、MAX-SAT 伪代码（Appendix B）、完整 per-condition 结果、子群分析等 25 个 appendix sections。[共识]
40	
41	---
42	
43	## Weaknesses
44	
45	### Must-Fix 问题（影响接收决定）
46	
47	**W1 [Critical] Proposition 1 证明范围与声称范围不匹配 [共识]**
48	- **位置**: §5.1, page 6, Proposition 1 及证明
49	- **问题**: Proposition 1 标题 "Symbolic Confirmation Bias is Structural" 暗示普遍性，但证明由两部分组成：
50	  - Part (i) voting degeneration 依赖 SICA 特定的 source attribution scoring (Eq. 3)。如果用逻辑一致性（而非来源归属）对约束打分，Part (i) 不一定成立。论文 Remark 承认但未反映在 Proposition 表述中。
51	  - Part (ii) information ceiling 是 data processing inequality 的直接应用（I(C;Y) ≤ I(T;Y)），数学正确但平凡——只证明约束不能比 traces 包含更多信息，不排除约束通过重新组织信息打破相关模式。
52	- **Reviewer 共识**: R1 首提（N1 critical），R2 fully AGREE 并补充 DPI 部分是教科书推论。两者互补：R1 指出 validity/scope 问题，R2 指出 significance/novelty 问题。
53	- **修改建议**: 拆分为 (a) source-attribution 下的退化定理（精确但 SICA-specific）和 (b) DPI bound（普遍但弱）；正文明确区分两者适用范围。
54	
55	**W2 [Critical] 统计功效 < 21% 与 negative claim 强度不匹配 [共识]**
56	- **位置**: Title, Abstract, §4, Appendix D
57	- **问题**: 
58	  - Observed power < 21%，MDE ≥ 1.86pp（最大样本条件）。即使 SICA 有 2pp 真实效果，~79% 概率无法检测。
59	  - TOST equivalence test 仅 8/16 条件达到等价显著，6 条件 underpowered，2 条件 genuinely different (negative)。±2pp equivalence margin 缺乏先验理论依据。
60	  - Bootstrap 95% CI（Table 7）全部包含零，宽度约 ±1.5pp。
61	  - 标题 "Fail to Improve" 是无条件否定声明，但论文无法排除 1-2pp 量级的正效应。
62	- **Reviewer 共识**: R1-N2 critical + R2-W1 major，交叉后 R2 fully AGREE R1 的详细分析。
63	- **修改建议**: (a) 标题软化（如 "Do Not Substantially Improve"）；(b) Abstract 加 power caveat；(c) 补充 TOST margin sensitivity analysis（±1/3/5pp）。
64	
65	**W3 [Critical] Diagnostics 100% 准确率是 in-sample 评估——overfitting 风险 [共识]**
66	- **位置**: §5.3, §1 contributions, §7 conclusion, Abstract
67	- **问题**: 
68	  - 决策边界（C₀ < 5%, K_eff ≤ 1.30, SC < 40%）从 60 个条件推导，并在同一 60 个条件上评估 → in-sample fitting。
69	  - 60 个条件全为 negative cases，任何 trivial classifier（"永远预测不帮助"）都能 100%。
70	  - "Holdout" 验证仅 LLaMA-3.1-8B on FOLIO 1 个条件 → 不构成充分 OOD 验证。
71	  - 未在 positive cases（cross-architecture escape, oracle）上验证诊断框架能否正确预测"会帮助"。
72	- **Reviewer 共识**: R2-N3 critical，R1 fully AGREE（承认初审疏漏）。
73	- **修改建议**: (a) 增加完整的 held-out model family；(b) 弱化 claim 为 "correctly classify all tested conditions within our experimental scope"；(c) 讨论 OOD 失败条件。
74	
75	**W4 [Critical] BR 指标存在循环论证风险——缺乏 null model [共识]**
76	- **位置**: §3.1 (Eq. 5), §5.1, Table 2
77	- **问题**: 
78	  - BR 通过 source attribution 衡量约束是否偏向支持多数答案。但约束从产生答案的 trace 中提取——如果 60% traces 产生答案 A，提取的约束自然更多支持 A（base-rate 效应）。
79	  - 论文未建立 null model：如果约束提取完全"无偏"（support 比例精确反映 trace 投票分布），BR 期望值是多少？只有观测 BR 显著超过 null expectation 才能声称"额外的" confirmation bias。
80	  - Shuffle control（§5.1, p.5: BR_shuffle ≈ BR_obs）确认 BR 主要反映 trace-count 分布而非提取特异性——但论文措辞混淆这两个组成部分。
81	- **Reviewer 共识**: R2-N2 critical，R1 fully AGREE（初审未注意此问题），但共识补充：BR 循环论证不否定 SCB 整体论证（Table 11、degeneration condition、oracle 独立支持），只影响 BR 指标本身的概念有效性。
82	- **修改建议**: (a) 构建 permutation-based null distribution；(b) 或将 BR 降级为描述性指标，明确声明 base-rate 组成。
83	
84	### Should-Fix 问题（影响评分但不一票否决）
85	
86	**W5 [Major] 新颖性定位——SCB 是已知结论的实证深化而非概念突破 [部分共识]**
87	- **位置**: §1 contributions, §5 "The Symbolic Mirage", Abstract
88	- **问题**: 
89	  - Huang et al. (2024) 已建立 "LLMs cannot self-correct without external feedback"。SCB 将此延伸到形式化约束自验证——可预见但不平凡。
90	  - Wan et al. (2025, ACL Findings) 已从认知心理学角度证明 CoT 推理中存在 confirmation bias。SCB 底层机制（model beliefs dominate downstream processing）高度重叠。
91	  - Proposition 1 Part (ii) 是 DPI 的教科书应用。
92	- **Reviewer 分歧**: R2 认为 critical（可预见的延伸），R1 partial REBUT（negative result 不应事后贬低；诊断框架 + 27 策略否证 + 机制定位是非平凡贡献）。
93	- **最终判定**: 部分共识——两者同意定位应从"发现"转为"系统性量化"，弱化 Proposition 1 呈现权重。R1 的反驳有一定道理：negative result paper 的价值在于提供系统性证据，不应仅因"可预见"而否定。
94	
95	**W6 [Major] "Extending Huang et al. (2024) to formal verification" 是 overselling [共识]**
96	- **位置**: Abstract, §1 contribution 1, §5.1
97	- **问题**: Huang et al. 基于 value/policy iteration 分析 self-correction，本文基于 DPI + source attribution 分析 self-verification。形式化框架、假设条件和证明技术完全不同，不构成逻辑 extension。
98	- **修改建议**: 改为 "consistent with / complement / provide independent evidence for"。
99	
100	**W7 [Major] 缺少 training-based self-verification 方法讨论 [部分共识]**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bd8879e-0fc9-481c-8f1f-c34fdcb22fa8",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "db0fe980-b4c1-4f5a-af6e-2bc1079ed8cd",
  "sourceToolAssistantUUID": "5bd8879e-0fc9-481c-8f1f-c34fdcb22fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T14:17:21.749Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WWh5jZZnz79mykaPSEsC9N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_14.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db0fe980-b4c1-4f5a-af6e-2bc1079ed8cd",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "958f181a-d645-4fc3-be5f-ddd25a2d091c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

### Tool result

_source line 36 · 2026-05-23T14:17:21.755Z_

<details><summary>↩ Tool result · `toolu_01WWh5jZZnz79mykaPSEsC9N`</summary>

```text
1	---
2	round: 14
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-23T09:39:17.381201+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# Round 17 (Fresh) 审稿报告
12	
13	**论文**: "Beyond Self-Consistency: Self-Extracted Constraints Do Not Substantially Improve LLM Logical Reasoning"
14	**Venue**: EMNLP 2026 via ACL Rolling Review
15	**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）
16	**交叉分享**: 完成，1 轮收敛
17	
18	---
19	
20	## Summary
21	
22	本文引入 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束并通过加权 MAX-SAT 聚合答案。在 6 个模型（7B–32B）、3 个推理领域上，SICA 与多数投票结果在 94.4% 的问题上一致，无条件显示显著正向效果（BH 校正后）。论文将此归因于 "Symbolic Confirmation Bias"（SCB），通过 Proposition 1（Source-Attribution Degeneration）和 Corollary 1（DPI Information Ceiling）形式化。27 个 training-free 变体均产生中性至负面结果。三个零成本诊断指标（C₀, BR, K_eff）在 60 个条件上 100% 分类。跨架构验证（DeBERTa NLI）在弱生成器上展示逃逸可能。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 实验规模与方法论严谨性。** 9 个模型（含 frontier）、3 个推理域、27 个 training-free 变体的系统覆盖。统计方法完备：TOST 等价性检验、McNemar + BH 校正、bootstrap CI、功效分析。这是该领域最系统的 negative result 研究之一。[R1-S1, R2-S1]
29	
30	**S2. 因果分析链条清晰。** 从现象（SICA ≈ SC）→ 机制（trace-count 分布决定约束分布）→ 理论（DPI Markov chain）→ 逃逸条件（跨架构独立性），层层递进。Figure 3 因果 DAG 和 Figure 1 pipeline 图有效辅助理解。[R1-S2, R2-S3]
31	
32	**S3. Oracle 对照设计精确定位瓶颈。** Gold FOL 替换自提取约束后 MAX-SAT 产生 +29.91pp 增益（Appendix G），明确瓶颈在约束提取而非求解器，避免了对 MAX-SAT 机制的混淆。[R1-S3]
33	
34	**S4. 诊断框架具有实际潜力。** C₀、BR、K_eff 三个指标可在 pilot run 中预估 self-extraction 方法的前景，对从业者有指导意义——尽管 100% accuracy 声称需要软化（见 W3）。[R2-S2]
35	
36	**S5. 诚实的统计报告。** 论文坦承 10/16 条件统计功效不足、模型范围局限、multi-seed 覆盖不完整。这种透明度在 negative result 论文中值得肯定。[R1-S5, R2-S5]
37	
38	---
39	
40	## Weaknesses
41	
42	### Must-Fix（影响接收决定）
43	
44	**W1** [critical, 共识] **Proposition 1 证明存在关键逻辑跳跃。**
45	证明直接声称 "score(a) = Σ 1[aᵢ = a] = nₐ"，但 SICA 的实际评分函数（Eq. 3）涉及约束权重 wc（去重后 trace 计数）和源归属指示函数 σ(c,a)。从 Eq. 3 到 score(a) = nₐ 需要证明：(1) 退化条件下 |C⁻| ≈ 0；(2) 不同答案组约束不重叠；(3) 42.9% 去重率下权重分布使 Σwc 精确等于 nₐ 而非仅成比例。R2 补充：比例关系可能保持 argmax 但精确等式不成立。Proposition 1 是全文理论框架的基石，证明不完整使理论贡献从 "形式化证明" 降级为 "经验观察"。
46	**修复方向**: (a) 完善证明列出所有假设；或 (b) 弱化为 argmax preservation（ranking 保持）；或 (c) 补充经验 rank agreement 验证。
47	[R1-N1 提出, R2 fully AGREE]
48	
49	**W2** [critical, 共识] **标题/Abstract 的全称否定与统计证据不匹配。**
50	标题 "Do Not Substantially Improve" 和 Abstract 的 "We show the answer is no" 是全称判断，但 TOST 仅 4/16 条件确立等价（±2pp），10 条件 underpowered（power < 21%, MDE ≥ 1.86pp）。论文无法区分 "SICA 无效" 和 "样本不够大"。GSM8K (n=30) 和 AIME (n=22) 在 Table 1 中与 n=200+ 条件无区分地并列，加剧误导。
51	**修复方向**: (a) 标题改为限定性表述（如 "Show No Significant Improvement"）；(b) Abstract 区分 confirmed-equivalent vs. underpowered/inconclusive；(c) Table 1 视觉标记 powered/underpowered 条件；(d) GSM8K/AIME 移至 Appendix 或标为 exploratory。
52	[R2-N1 提出, R1 fully AGREE]
53	
54	**W3** [critical, 共识] **诊断框架 100% 准确率是 trivial 的。**
55	60 个条件全部为 null 或 negative，trivial "always predict no improvement" classifier 也能达到 100%。Holdout 验证仅 2 个模型系列（LLaMA-3.1-8B、Qwen3-14B），且同为 negative cases。框架的区分能力（discriminative power）未经正例验证。论文将此列为三大贡献之一，但无正例的框架无法预测何时 self-extraction *会* 有效。R2 精辟指出：框架的实际价值在于 failure mode 分类（退化型/多样性不足型/确认偏差型），而非二分类预测。
56	**修复方向**: (a) 改 "correctly classifies" 为 "correctly characterizes the failure mode"；(b) 用 §6 cross-arch escape 的 Mistral-7B 条件作 positive validation；(c) 定位为 "ruling-out tool" 而非通用诊断。
57	[R1-N3 提出, R2 fully AGREE]
58	
59	**W4** [critical, 部分共识] **SCB 与已有 confirmation bias 工作的新颖性区分不充分。**
60	Wan et al. (2025) 已证明 CoT confirmation bias，SCB 可能是同一现象在 FOL/symbolic 载体上的实例化。论文 §2 仅一句区分（"symbolic confirmation bias is distinct from CoT unfaithfulness"），未充分对比。Jhaveri & Kersting (2026) 进一步削弱新颖性。R1 部分反驳：SCB 有独立的 aggregation-level 结构性区分——source-attribution scoring 退化是关于 aggregation mechanism 的形式化结论，非推理忠实性结论；且 94.4% 约束通过 Z3 验证说明问题不在约束不可靠而在不提供超越 trace 的信息。
61	**共识**: 需 1-2 段显式对比 Wan et al.，明确 SCB 的增量贡献在于 DPI 形式化和 source-attribution 机制，定位为 "complementary instance in formal verification" 而非全新概念。
62	[R2-N3 提出, R1 AGREE with nuance]
63	
64	### Should-Fix（影响评分但不一票否决）
65	
66	**W5** [warning, 共识] **Corollary 1 (DPI) 理论贡献度偏弱。**
67	I(C;Y) ≤ I(T;Y) 是 DPI 在 Markov chain T→C 上的直接应用，接近信息论教科书练习。贡献在于 Markov chain 建模识别而非推导。建议降级为 Remark。[R1-W1, R2-W1, 共识]
68	
69	**W6** [warning, 共识] **Bias Ratio (BR) 缺少 null model 分解。**
70	60% trace 产生答案 a 时，纯随机约束-答案关联已产生 BR = 1.5。Table 2 的 BR 值（1.66×–4.97×）部分可能由 base rate 解释。需 permutation null model 量化 excess bias。即使 excess = 0，negative result 仍成立，但 "structural bias" 声称需 excess > 0。[R1-W2 提出, R2 fully AGREE]
71	
72	**W7** [warning, 共识] **Cross-architecture escape (§6) 结论过度推断。**
73	仅 6 个 generator-verifier 条件，仅 Mistral-7B (SC=39.33%) 显著。Spearman ρ=1.0 (n=6) 鲁棒性低。"Capability-gap pattern" 数据不足。R2 补充：方向性发现有启示价值但不足以建立一般规律。建议措辞从 "confirming" 改为 "suggesting" 或 "preliminary evidence"。[R1-W3, R2 AGREE]
74	
75	**W8** [warning, 共识] **α=0.5 sensitivity 分析实质上确认退化。**
76	Table 11 所有 α∈{0.1,...,1.0} 下 SICA-SC agreement ≥ 99%——这是 ceiling effect（|C⁻| ≈ 0 使 α 无关），非方法鲁棒性。论文应重新解释为退化的 corroborating evidence。[R1-W4, R2 AGREE]
77	
78	**W9** [warning, 共识] **Scope 震荡。**
79	论文在 SICA-specific findings 和 general impossibility claims 之间摆动。Proposition 1 声称适用于 "any self-extraction pipeline"，但 27 个实验变体全在 SICA 范式内。建议在 §1 contributions 中明确界定实验覆盖的 scope 边界。[R2-W3, R1 AGREE with nuance]
80	
81	**W10** [warning, 共识] **K_eff 可读性不足。**
82	K_eff = K/[1+(K-1)·κ] 对非 ensemble-theory 背景读者缺少直觉解释。建议添加具体示例（如 "K=12, κ=0.7 → K_eff ≈ 1.3"）。[R2-W4, R1 AGREE]
83	
84	### Minor Issues
85	
86	- **符号过载**: 正文 8 页内引入 BR, K_eff, C₀, κ, σ, α, Δ, score(a), CCR, ProcessSim 等。建议 CCR/ProcessSim 定义移至 Appendix。[R2]
87	- **Abstract 信息密度过高**: ~6 个核心发现压缩在一段。建议精简为中心 negative finding + 机制 + scope。[R2]
88	- **§2 段间衔接**: 三个子节间缺显式逻辑连接句。[R2]
89	- **Table 1 统计功效未标注**: 读者需翻 Appendix D 才发现 10/16 underpowered。[R1]
90	- **TOST ±2pp margin 缺先验依据**: 是领域惯例还是事后选择？存在 specification searching 风险。[R1-Q3, R2 AGREE]
91	- **Multi-seed 覆盖率**: 仅 2/6 模型有 multi-seed replication。[R1-W5, R2 REBUT：现有两模型方向一致，降级 nice-to-have]
92	
93	---
94	
95	## Reviewer Consensus
96	
97	以下问题两位 Reviewer 完全达成一致（[AGREE]）：
98	
99	1. **Proposition 1 证明不完整**——score(a) = nₐ 从 Eq. 3 推导缺关键步骤 [R1-N1, R2 AGREE]
100	2. **标题/Abstract overclaim**——10/16 underpowered，"We show the answer is no" 逻辑不一致 [R2-N1, R1 AGREE]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "958f181a-d645-4fc3-be5f-ddd25a2d091c",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "e11c9f46-32b0-4fc5-9c0e-516d1e129cb7",
  "sourceToolAssistantUUID": "958f181a-d645-4fc3-be5f-ddd25a2d091c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T14:17:22.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_014eHbzJG7D5J8Kc3AtR2TSC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_15.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e11c9f46-32b0-4fc5-9c0e-516d1e129cb7",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d5b564e-0053-459d-85a0-103d9d2e819d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30809,
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

### Tool result

_source line 38 · 2026-05-23T14:17:22.056Z_

<details><summary>↩ Tool result · `toolu_014eHbzJG7D5J8Kc3AtR2TSC`</summary>

```text
1	---
2	round: 15
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-23T10:30:30.239957+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 18 (Fresh)
12	
13	**论文**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning
14	**Venue**: EMNLP 2026 via ARR | **Deadline**: 2026-05-25
15	**Reviewer 编排**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + 写作质量）
16	**交叉分享**: 完成，关键问题高度收敛
17	
18	---
19	
20	## Summary
21	
22	论文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束并通过 MAX-SAT 选择答案。核心发现为负面结果：自提取约束因 "symbolic confirmation bias"（SCB）系统性对齐模型多数票答案，使 SICA 退化为多数投票。论文在 6 个开源模型 (7B–32B) + 5 个 frontier 模型、3 个核心数据集、27 种 training-free 修复策略上验证了这一现象，提供了理论分析（Proposition 1, Remark 1）和诊断框架（C₀, K_eff, BR），并展示 cross-architecture verification 作为初步 escape path。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 实验覆盖度和系统性极高 [R1, R2 共识]。** 6 个开源模型 + 5 个 frontier 模型的 cross-model extraction，3 个核心 + 3 个辅助数据集，27 种修复策略的系统排除，multi-seed replication (3-seed/4-seed)，oracle control 验证 MAX-SAT 机制 soundness (+29.90pp FOLIO, +17.17pp PW)。这种覆盖度在 negative-result 论文中极为罕见。
29	
30	**S2. 统计方法论严谨 [R1, R2 共识]。** McNemar exact test + BH correction (m=16)、TOST equivalence test (±1/±2/±3pp sensitivity analysis)、bootstrap CI (10,000 resamples)、permutation null model (1,000 permutations)。论文坦诚报告 10/16 conditions underpowered，透明度值得肯定。
31	
32	**S3. 诊断框架有实用价值 [R1, R2 共识]。** 三个 zero-cost diagnostics (C₀, K_eff, BR) 在全部 60 个测试条件上正确表征失败模式，并在两个 held-out model families (LLaMA-3.1-8B, Qwen3-14B) 上前瞻性验证。可直接被从业者采用。
33	
34	**S4. Oracle control 设计精良 [R1]。** Gold annotations 替代自提取约束，干净分离 "MAX-SAT 机制是否 sound" 和 "自提取约束是否有效" 两个问题。
35	
36	**S5. Permutation null model 验证 BR [R1]。** BR_null ≈ BR_obs (p > 0.7) 证实 bias ratio 由 trace-count base rate 解释——反而加强了论文核心论点（bias 是结构性的）。
37	
38	**S6. Related Work 覆盖全面 [R2]。** 结构清晰的分类（specification-generation / program-generation / trace-extraction），与 Huang et al. (2024) 和 Wan et al. (2025) 的区分在概念上成立。
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（影响接收决定）
45	
46	**W1 [critical, R1+R2 共识] 标题 "Do Not Improve" 与统计证据不匹配**
47	标题是全称否定命题，但 10/16 条件 underpowered（MDE 1.86–4.84pp, observed power < 21%），仅 4 条件通过 TOST 等价检验。论文自身承认 "Absence of evidence is not evidence of absence for small effects"（§4），与标题矛盾。Abstract 中 "find no evidence" 更审慎但标题未反映。R1 建议 "Provide No Detectable Improvement"，R2 建议 "Show No Evidence of Improving"——两种表述均优于现标题。
48	
49	**W2 [critical, R1 提出 + R2 共识] Proposition 1 形式化不严谨**
50	假设 (i) 使用 |C^∖| ≈ 0 而非精确条件；假设 (iii) "approximately uniform constraint yield" 无数学定义（CV < δ?）且未直接验证（论文给出 extraction rate 但未展示每 trace 约束数量分布）；证明全程使用 ≈ 而非 =。结论通过 >90% 经验一致性支撑而非严格推导。作为论文理论核心支柱，应降格为 Empirical Observation 或给出误差界。R2 补充：配合 Remark 1 的 DPI 论证，即使降格核心论点仍成立。
51	
52	**W3 [critical, R2 提出 + R1 部分共识] SCB 相对于 Huang et al. (2024) 增量新颖性论证不足**
53	论文定位为 "independent evidence consistent with" Huang et al.——风险是降级为 case study。§2 对 CoT bias（trace level）和 SCB（aggregation level）的区分是概念性的，缺少实证证据证明两者可分离（如控制 trace faithfulness 后 SCB 是否仍存在）。R1 指出论文实际贡献超出 case study（形式化、诊断框架、27 变体排除），但 "consistent with" 措辞自我降级，应改为 "extends"。
54	
55	### Should-Fix（影响评分但不一票否决）
56	
57	**W4 [major, R1 提出 + R2 共识] Remark 1 (DPI) 与 Figure 3 间存在 claim 升级**
58	I(C;Y) ≤ I(T;Y) 对任何确定性后处理 C = f(T) 成立，接近 trivial。真正有价值的 claim 是 Figure 3 DAG 中隐含的 C ⊥ Y | A——约束在给定答案后不携带关于真值的额外信息——但这个更强的条件独立性声明未被形式化证明。R2 补充：需在 Proposition 1 条件下显式证明 I(C;Y) ≤ I(A;Y)，将 trivial DPI 和 non-trivial C ⊥ Y | A 明确区分。
59	
60	**W5 [major, R1 提出 + R2 共识] BR 指标的 by-construction 循环性**
61	Source-attribution scoring 下，多数 trace 产生 a_M → 多数约束 support a_M → BR > 1 几乎 tautological。Permutation test (BR_null ≈ BR_obs, p > 0.7) 证实 BR 完全由 trace-count base rate 解释。56.4% 零变量重叠使约束无法跨答案判别。R2 洞察：BR_excess ≈ 0 意味着 SCB 的 "bias" 完全来自结构性 source-attribution——这反而强化 Proposition 1 的 degeneration 论点，但需将 BR 从 "bias 度量" 重新框定为 "degeneration 度量"。建议报告 BR_excess = BR_obs - BR_null。
62	
63	**W6 [major, R1+R2 共识] Cross-architecture escape (§6) 证据过弱**
64	(a) Spearman ρ=1.0 基于 n=6，Table 3 中 3 个 generator 的 Δ 在 0.50–0.83pp 几乎无差异，monotonicity 由 Mistral-7B 单个 outlier 驱动——实质是二元判断（generator 低于/高于 verifier）而非连续 pattern。
65	(b) Zero-shot DeBERTa 仅在最弱 generator (Mistral-7B, SC=39.33%) 上显著；domain-adapted verifier 引入 training 与论文 training-free 主线矛盾，混淆了 independence 和 supervision 两个因素。
66	(c) 仅 ProofWriter 一个数据集。
67	作为三个 contribution 之一，evidence base 不足。建议降级为 preliminary finding。
68	
69	**W7 [major, R2 提出 + R1 共识] Scope 震荡**
70	标题说通用（"Self-Extracted Constraints Do Not Improve LLM Logical Reasoning"）；Contribution 1 说 SICA-specific（"Z3 verification becomes vacuous under self-extraction"）；Discussion 扩展到 "any self-verification method"。Proposition 1 假设是 SICA 设计选择（degeneration, source-attribution, uniform yield），非所有 self-extraction pipeline 共性。Remark 1 的 DPI bound 更通用但接近 trivial。需在 §1/§5/§7 明确区分 SICA-specific 结论（Proposition 1）和一般性结论（Remark 1）。
71	
72	**W8 [moderate, R2 提出 + R1 AGREE 降级] "LLM Logical Reasoning" 标题范围与实验覆盖不匹配**
73	实际测试包含 FOLIO/PW（FOL）、LogiQA（NL 逻辑）、StrategyQA（常识）、GSM8K/AIME（数学），但 GSM8K/AIME 在 degenerate regime (C₀ < 5%)，StrategyQA 仅一个模型。核心有效测试集中在 FOLIO 和 ProofWriter。R1 认为严重性低于 major——核心机制不依赖推理类型。建议标题去掉 "Logical"。
74	
75	**W9 [moderate, R2 提出 + R1 共识] K_eff 缺少直觉解释**
76	Eq. 1 后应加一句 "K_eff measures how many effectively independent votes K correlated traces contribute"。Abstract 中 K_eff 首次出现时也需括号解释（如 "effective independent sample count"）。修改成本极低。
77	
78	**W10 [moderate, R1 提出, R2 部分 REBUT] TOST ±2pp margin 选择依据**
79	R1 认为 FOLIO 近二分类，1pp/class 阈值不适用。R2 REBUT：FOLIO 实为三分类 (True/False/Unknown)，±2pp ≈ ±0.67pp/class 在三分类上合理。共识：需在 §4 区分二分类 (ProofWriter) 和三分类 (FOLIO) 数据集的 margin 适用性。
80	
81	### Nice-to-Have
82	
83	- **M1 [minor, R2 提出, R1 REBUT]** Abstract 信息密度高但 R1 认为适合 ACL/EMNLP venue。共识：在 Abstract 中给 K_eff 加括号解释即可。
84	- **M2 [minor, R1]** Table 1 中 Mistral-7B multi-seed 行间关系需在 caption/脚注说明（s123/s456/s789 vs. 3s aggregated）。
85	- **M3 [minor, R1]** 56.4% 零变量重叠的计算粒度需说明（per-problem? per-dataset?）。
86	- **M4 [minor, R1+R2]** Appendix Y (Extended Discussion) 中 SCB evaluation framework 内容有价值但缺乏主文指引。
87	- **M5 [minor, R2 提出, R1 REBUT]** "Symbolic Mirage" 作为 Section 标题——R2 认为稍 dramatic，R1 REBUT 认为准确且 ACL 常见。保留。
88	- **M6 [minor, R2 提出, R1 REBUT]** Limitations 仅约 50 词——R2 认为偏短，R1 认为符合 EMNLP 规则（3 点即可）。R1 判断合规。
89	- **M7 [minor, R1]** Z3 3.4% rejection rate 应在 Method/Results 开头更早指出 vacuous verification。
90	
91	---
92	
93	## Reviewer Consensus
94	
95	以下问题两位 Reviewer 独立达成 [AGREE] 共识：
96	
97	1. **标题 overclaiming** [W1]：最高优先级修改项。"Do Not Improve" → "Provide No Detectable Improvement" 或类似表述。
98	2. **Proposition 1 形式化不足** [W2]：降格为 Empirical Observation 或补充误差界。
99	3. **Cross-architecture escape 证据不足** [W6]：降级为 preliminary finding，n=6 的 Spearman ρ=1.0 是 outlier-driven。
100	4. **BR 循环性** [W5]：重新框定为 degeneration 度量，报告 BR_excess。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d5b564e-0053-459d-85a0-103d9d2e819d",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "37d5c242-6d33-4d74-a771-1c72a7abef50",
  "sourceToolAssistantUUID": "4d5b564e-0053-459d-85a0-103d9d2e819d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T14:17:22.194Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FGquuxKXUVPzaNnCoy9kQJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_16.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37d5c242-6d33-4d74-a771-1c72a7abef50",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeHs3MwCLgrPcYqR22V",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6aac1b93-aabe-4b33-9206-9c8e4afba369",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014AEjuSyj8LPcMivpdw4gkf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30809,
      "cache_read_input_tokens": 38856,
      "output_tokens": 770,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 770,
          "cache_read_input_tokens": 38856,
          "cache_creation_input_tokens": 30809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30809,
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

_source line 40 · 2026-05-23T14:17:22.200Z_

<details><summary>↩ Tool result · `toolu_01FGquuxKXUVPzaNnCoy9kQJ`</summary>

```text
1	---
2	round: 16
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-23T14:07:38.531897+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 19 (Fresh)
12	
13	**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning
14	**Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
16	**审稿模式**: Fresh（重新审稿，无上轮记忆）
17	
18	---
19	
20	## Summary
21	
22	本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，通过 Z3 MAX-SAT 求解选择答案。核心发现是 negative result：SICA 在 6 个模型（7B–32B）、3 个推理数据集上均未显著优于 majority voting（Self-Consistency）。论文将此诊断为"symbolic confirmation bias"——自提取约束系统性地追踪模型自身的答案分布而非提供独立信号。27 种 training-free 修补策略均失败。形式化分析提供了 Observation 1（argmax preservation under degeneration）和 Remark 1（DPI information ceiling）。跨架构验证（DeBERTa NLI）在最弱生成器上显示初步逃逸（+6.67pp）。三个零成本诊断指标（K_eff, BR, C₀）在 60 个条件上 correctly characterize failure modes。
23	
24	---
25	
26	## Strengths
27	
28	1. **统计方法论极为扎实** [R1 Strength 1, R2 Strength 1, 共识]：McNemar paired test + BH FDR correction (m=16) + TOST equivalence testing + Bootstrap CI (10,000 resamples) + Power analysis + multi-seed replication 的完整组合在 NLP 论文中极为罕见。诚实报告 underpowered conditions 和 power limitations 体现了高水准的科学诚信。
29	
30	2. **Oracle control 设计精巧** [R1 Strength 2]：用 gold FOL/DSL 标注替换 self-extracted constraints 的对照实验（+29.90pp FOLIO, +17.17pp ProofWriter, p < 10⁻⁷）清晰地将问题定位在 extraction 而非 solver。这是本文最有说服力的实验设计。
31	
32	3. **27 种 remediation 变体的系统化测试** [R1 Strength 3, R2 Strength 3, 共识]：涵盖 prompt-level、method-level、paradigm、solver、input diversity、filtering 六个维度，彻底排除了 "换个方法就行" 的反驳。Independence-accuracy trade-off 的实证支持充分。
33	
34	4. **形式化声明命名克制得当** [R1 Strength 4]：使用 Observation 和 Remark 而非 Theorem/Proposition，诚实反映了其依赖经验条件的本质。
35	
36	5. **诊断框架有实践价值** [R1 Strength 5, R2 Strength 4]：C₀ < 5%, K_eff ≤ 1.30, BR + SC regime 三个 zero-cost diagnostics 在 60 个条件上 correctly characterize failure modes，prospective validation 在 held-out families (LLaMA, Qwen3) 上通过。对从业者有直接实用价值。
37	
38	6. **Entropy decomposition 分析精细** [R1 Strength 6]：low-entropy 问题 Δ ≈ 0、high-entropy 问题方向取决于 SC regime 的发现强化了 regime-dependent 叙事。
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（影响接收决定）
45	
46	**MF-1** [critical, R2-N1, R1 交叉 AGREE] **两条引用存在严重元数据错误**
47	
48	- `byerly2026selfconsistency`：bib 记录作者 "Nicholas Byerly and Daniel Khashabi, 2026"，但 arXiv:2411.01101 实际作者是 **Adam Byerly**，发表于 **2024**，实际标题/主题（positional bias on long-context problems）与引用标题（mathematical reasoning）完全不同。作者名、年份、主题三重错误。
49	- `dupo2025`：bib 记录标题 "DuPO: Dual **Process** Optimization"、一作 "Yang, Chenxu"，但 arXiv:2508.14460 实际标题是 "DuPO: Enabling Reliable LLM Self-Verification via Dual **Preference** Optimization"，一作为 **Shuaijie She**，Yang Chenxu 不在作者列表中。
50	- 错误模式（真实 arXiv ID 配上错误元数据）高度暗示 LLM-assisted hallucination。byerly2026 在 Related Work 中支持 "SC gains plateau" 论点，dupo2025 在 training-based verification 段落中被引用——文献支撑存在漏洞。
51	- **要求**：对全部参考文献进行系统性交叉验证，修正所有错误条目。
52	
53	**MF-2** [critical, R2-N2, R1 AGREE with nuance] **"Advances beyond Huang et al. (2024)" 的 claim 过度**
54	
55	- 论文在 Abstract、Section 1（Introduction）、Section 2（Related Work）、Section 7（Discussion）至少四处使用 "advances beyond Huang et al. (2024)" 措辞。
56	- Huang et al. (ICLR 2024) 已建立 "LLMs cannot self-correct reasoning without external feedback" 核心结论。本文的贡献是 (a) 将此洞见扩展到 formal symbolic verification setting，(b) 提供 Markov chain 形式化（Observation 1, Remark 1），(c) 系统排除 27 种 remediation——这是 **scope extension + formalization**，而非 fundamental insight 上的 "advance beyond"。
57	- 核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. + Condorcet Jury Theorem 框架下是可预见的。
58	- **要求**：将 "advances beyond" 改为更精确的表述如 "extends and formalizes ... in the context of formal self-verification"。
59	
60	**MF-3** [critical, R1-N1 + R2-N3, 共识] **Cross-architecture escape 证据不足以支撑 top-level contribution**
61	
62	- Capability-gap pattern 仅基于 6 个 verifier-generator 组合（Spearman ρ=1.0, p=0.003），其中 **4/6 共享同一 DeBERTa verifier**，实际有效自由度远小于 n=6。
63	- Table 3 的 n=4 generators 全部 paired with 同一 DeBERTa-large-mnli，排列空间仅 24 种。
64	- "Generator SC < verifier standalone accuracy 才有增益" 可能是 **trivial condition**——本质上是 "用更好的模型替代更差的模型" 的必然结果，不需要 information independence 理论。
65	- R1 额外指出：增益可能只是 **ensemble diversity 效应**（Dietterich 2000），而非 SCB escape。需要 cross-model majority vote ensemble 作为 ablation 区分两种假说。
66	- Domain-adapted verifier (99.67% standalone) 引入了 training，与 training-free 叙事线矛盾。论文自己承认 "directional evidence rather than a proposed method"，但叙事结构仍将其作为 escape 证据呈现。
67	- **要求**：将 Contribution 3 从并列贡献降级为 "preliminary observation"，或增加不同架构的 verifier + cross-model majority vote ablation。
68	
69	**MF-4** [critical, R1-N2 + R2-W2(升级), 共识] **10/16 条件 underpowered，中心论断表述超出统计证据范围**
70	
71	- Appendix D Table 6：3 个 confirmatory conditions 的 observed power 均低于 21%（Qwen-14B FOLIO+PW: 5.7%, LLaMA-8B StrategyQA: 20.6%, LLaMA-8B FOLIO: 18.6%）。MDE 为 1.86–4.84pp。
72	- TOST 等价检验仅 4/16 条件确认等价（±2pp margin），10 条件 underpowered。
73	- Abstract "We find no evidence of improvement" 和标题 "No Detectable Improvement" 构成 blanket negative claim，但统计证据仅能排除 >~2pp 的效果。"Absence of evidence is not evidence of absence" 在正文中有提及（Section 4），但 Abstract/标题层面的表述未反映这一 nuance。
74	- **要求**：(a) Abstract 改为 "no evidence of improvement exceeding ~2 percentage points"；(b) 在 Discussion 中显式论证 <2pp 在 4.5× 计算开销下无实际价值，将 power limitation 转化为 practical insignificance 论证。
75	
76	### Should-Fix（影响评分但不一票否决）
77	
78	**SF-1** [warning, R1-W1 + R2-W4, 共识] **BR/SCB 概念框架混淆 structural degeneration 与 extraction bias**
79	
80	- R1 从技术层面指出：source-attribution scoring 下 BR > 1 是 trace-count 分布的**数学必然结果**。Permutation test 证实 BR_excess ≈ 0 (p > 0.7, §5.1)——BR 完全由 trace-count 结构解释，不含 extraction 过程的额外偏差。BR 度量的是 degeneration 程度，不是独立于 Observation 1 的 bias 证据。
81	- R2 从概念层面指出："Symbolic **Confirmation Bias**" 暗示 cognitive bias 类比（主动寻找支持性证据），但实际机制是 structural limitation（约束和答案来自同一信息源而结构性耦合）。
82	- 两个批评收敛到同一结论：论文应更清楚地区分 "structural degeneration"（Observation 1 的后果）和 "extraction bias"（如果存在的话）。目前混淆使 BR 看起来提供了 Observation 1 之外的独立证据，但实际上没有。
83	- **建议**：(a) 在首次定义 SCB 时明确说明这是 structural limitation 而非 cognitive bias 类比；(b) 报告 BR_excess 作为判断是否存在 extraction-level 额外偏差的指标；(c) 考虑更精确的术语如 "symbolic information collapse" 或 "self-referential degeneration"。
84	
85	**SF-2** [warning, R2-W1, R1 AGREE] **Abstract 超过 200 词限制**
86	
87	- 经去除 LaTeX 命令后词数统计约 202 词，超过 EMNLP 2026/ARR 的 200-word 硬约束。虽仅超出 2 词，但属明确格式违规。
88	
89	**SF-3** [warning, R1-W2, R2 AGREE] **"Pre-registered" margin ±2pp 无注册凭证**
90	
91	- Section 4 使用 "pre-registered margin ±2 pp" 但未提供 OSF/AsPredicted 等预注册链接。"Pre-registered" 在实证研究中有严格操作定义。改为 "pre-specified" 或 "predetermined" 即可。
92	
93	**SF-4** [warning, R1-W3, R2 AGREE with nuance] **BH correction m=16 包含非独立条件**
94	
95	- 16 个条件中包含 Mistral-7B×FOLIO 的 3 个单独 seed (s123, s456, s789) 和 1 个 3-seed aggregate，以及 Qwen2.5-14B×FOLIO 的 4-seed aggregate。Aggregate 是 component seeds 的函数，非独立检验。虽然更大的 m 使 BH 更保守，但方法论应更干净地区分 confirmatory vs exploratory 条件。
96	
97	**SF-5** [warning, R1-W4, R2 AGREE] **Observation 1 条件 (iii) "approximately uniform constraint yield" 缺乏系统验证**
98	
99	- 条件 (i) |C\| ≈ 0 由 Z3 rejection rate 3.4% 实证支持，条件 (ii) source-attribution 是系统设计，但条件 (iii) 缺乏直接验证。论文未报告 per-trace constraint yield 的分布统计量（mean, std, CV），应按 answer group 分层报告。
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6aac1b93-aabe-4b33-9206-9c8e4afba369",
  "isSidechain": true,
  "promptId": "2363c93b-9d0d-4e17-8628-08354997b01b",
  "agentId": "adc40b630705b75d4",
  "type": "user",
  "uuid": "d8a28baa-741d-4f2d-93b8-e3cb614f6096",
  "sourceToolAssistantUUID": "6aac1b93-aabe-4b33-9206-9c8e4afba369",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-23T14:17:42.413Z_

Perfect! Now I have all 17 review rounds. Let me compile the comprehensive table with all the information extracted:

## Review Score and Critical Issues Summary — Rounds 0-16

| Round | Score | Mode | Top 2-3 Critical Issues | Score Trend |
|-------|-------|------|------------------------|-------------|
| **0** | 2.5/5 | Fresh | 1) Stage 3 sat() function completely undescribed; 2) Experiments severely underpowered (8/11 rows n≤60); 3) Oracle/upper-bound experiment missing | baseline |
| **1** | 3.0/5 | Fresh | 1) σ(c,a) Z3 evaluation incomplete; 2) Oracle only FOLIO (n=204), external validity insufficient; 3) "Capability Trap" overlaps with Huang et al. (ICLR 2024) without citation | ↑ 0.5 |
| **2** | 3.0/5 | Fresh | 1) Dream R1 version has discrepancies with actual paper; 2) §4.1 decoupling experiment incomplete (n=70/204); 3) Oracle "24% ceiling" cross-model comparison flawed | = |
| **3** | 3.0/5 | Fresh | 1) §4.1 Decoupling interim results (n=70/204) incomplete; 2) Oracle "24% ceiling" not on same model; 3) Discussion/Conclusion too compressed (~100 words) | = |
| **4** | 3.0/5 | Fresh | 1) Statistical power <21%, "Fail" claim overclaimed; 2) Cross-architecture PoC underpowered & multiple comparisons uncorrected; 3) Variable name isolation confound not distinguished from confirmation bias | = |
| **5** | 3.0/5 | Fresh | 1) FOL terminology misleading (mostly propositional); 2) Cross-architecture PoC double underpowered (single model + inconsistent datasets); 3) Novelty positioning vs Huang/Stechly insufficient | = |
| **6** | 3.0/5 | Fresh | 1) "Fail" overclaims given power <21%; 2) Cross-architecture PoC multiple comparisons uncorrected; 3) Core findings vs self-correction/self-verification literature distinction unclear | = |
| **7** | 3.0/5 | Fresh | 1) Spearman ρ=1.0 (n=6) overused, violates independence; 2) Abstract "do not improve at any capability level" too strong for underpowered conditions; 3) TOST ±2pp margin lacks principled justification | = |
| **8** | 3.0/5 | Fresh | 1) Proposition 1 unproven (≲ undefined, no rigorous derivation); 2) κ→K_eff mapping lacks theoretical basis; 3) Capability gap ρ=1.0 (n=6) based on non-independent datapoints | = |
| **9** | 3.0/5 | Fresh | 1) Novelty vs Huang/Stechly at concept level insufficient; 2) Independence-Accuracy Trade-off is bias-variance tradeoff restatement; 3) Table 1 lacks Bonferroni correction | = |
| **10** | 3.5/5 | Fresh | 1) Abstract BR 4.97× is extreme value (range 1.66–4.97×); 2) Power <21% vs "No Evidence" claim tension; 3) α=0.5 parameter lacks sensitivity analysis | ↑ 0.5 |
| **11** | 3.5/5 | Fresh | 1) ρ=1.0 (n=6) overused, contains shared verifier; 2) Title/Abstract claim strength exceeds statistical evidence; 3) TOST ±2pp margin margin-sensitive, lacks principled defense | = |
| **12** | 3.0/5 | Fresh | 1) Title "Do Not Improve from 7B to Frontier Scale" overclaiming (frontier uses cross-model, not self-extraction); 2) SCB novelty insufficient (self-correction failure in FOL context); 3) Power <21%, statistical functionality <21% unfit for negative claim | ↓ 0.5 |
| **13** | 3.0/5 | Fresh | 1) Proposition 1 proof incomplete (score(a)=nₐ lacks rigorous derivation from Eq. 3); 2) Power <21% vs "No Evidence" mismatch; 3) Diagnostics 100% accuracy is in-sample (60 all negative cases, trivial classifier wins) | = |
| **14** | 3.0/5 | Fresh | 1) Title overclaims scope (covers only 7B-32B, all logical reasoning); 2) Symbolic Mirage predictions partially post-hoc; 3) Cross-architecture PoC evidence weak (single model, inconsistent datasets) | = |
| **15** | 3.5/5 | Fresh | 1) Title "Do Not Improve" vs 10/16 underpowered conditions inconsistent; 2) Proposition 1 formalization not rigorous; 3) Cross-architecture escape limited evidence (n=6, 4 shared verifier) | ↑ 0.5 |
| **16** | 3.0/5 | Fresh | 1) Two bib entries hallucinated (Byerly 2026 & DuPO 2025 metadata wrong); 2) "Advances beyond Huang et al." overclaimed; 3) Cross-architecture escape insufficient evidence (n=6 with shared components, trivial when verifier > generator) | ↓ 0.5 |

### Key Observations:

**Score Stability**: The paper oscillates between 3.0 and 3.5/5, clustering at **3.0 (Findings)** with occasional **3.5 (Borderline Conference)** ratings from rounds 10, 11, and 15.

**Recurring Themes** (appearing in 10+ rounds):
- **Statistical Power (<21%)** — Most critical and persistent issue
- **Cross-architecture PoC weakness** — Consistently underpowered evidence
- **Novelty vs Huang et al. (2024)** — Self-correction failure is known concept
- **Proposition 1 incompleteness** — Proof lacks rigor starting Round 8
- **BR/SCB circular reasoning** — Base-rate effect confounds Round 12 onward
- **Title overclaiming** — "Fail/Do Not Improve" vs underpowered conditions tension

**Progressive Problems**:
- Rounds 0-2: Method description issues (Stage 3, σ function)
- Rounds 3-9: Statistical methodology refinements
- Rounds 10+: Fundamental novelty/formalization critiques

**Scoring Rationale**: All reviews maintain 3.0 base with brief 3.5 excursions when reviewers view experimental comprehensiveness as compensating for novelty gaps, reverting to 3.0 when statistical or methodological flaws dominate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8a28baa-741d-4f2d-93b8-e3cb614f6096",
  "isSidechain": true,
  "agentId": "adc40b630705b75d4",
  "requestId": "req_011CbKeJD38wVVWZ4jJpqdTd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d64e71e6-0ab7-4954-9a92-867ebd9ed814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XT6zGYaALinYMzr63EziYY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 30428,
      "cache_read_input_tokens": 69665,
      "output_tokens": 1747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30428
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1747,
          "cache_read_input_tokens": 69665,
          "cache_creation_input_tokens": 30428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30428,
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
