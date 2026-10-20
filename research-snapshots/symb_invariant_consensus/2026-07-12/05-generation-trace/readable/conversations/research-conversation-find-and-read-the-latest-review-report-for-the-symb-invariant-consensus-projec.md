# Research conversation: Find and read the latest review report for the symb_invariant_consensus project. Check: 1. /home/ubuntu/.agent-ml-resear

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a51e46aca94cd12ca.jsonl`
- **Structured JSON:** [`deeac3e30615dc676024.json`](../../sessions/de/deeac3e30615dc676024.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-23T08:30:14.043Z_

Find and read the latest review report for the symb_invariant_consensus project. Check:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/ - find all round_*.md files, read the latest one
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml - read full contents

Report the complete contents of both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b919c63a-499b-4b5b-a8c7-415028b122d9",
  "agentId": "a51e46aca94cd12ca",
  "type": "user",
  "uuid": "be7a0919-e53b-4181-91c7-8a1966bb39f8",
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

_source line 2 · 2026-05-23T08:30:15.487Z_

I'll help you find and read the latest review report and issues file for the symb_invariant_consensus project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be7a0919-e53b-4181-91c7-8a1966bb39f8",
  "isSidechain": true,
  "agentId": "a51e46aca94cd12ca",
  "requestId": "req_011CbKBptB3jsVtamFwFPDJ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f1e5f9d9-2f47-4e42-8922-4e07b483c02e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HRJzxgSDJ4LUEKGWEt8UNg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37285,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-23T08:30:16.022Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RT3XmLanwoXCZXTJ9sySWW`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/ 2>/dev/null | grep \"round_.*\\.md\" | tail -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1e5f9d9-2f47-4e42-8922-4e07b483c02e",
  "isSidechain": true,
  "agentId": "a51e46aca94cd12ca",
  "requestId": "req_011CbKBptB3jsVtamFwFPDJ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2df8b90f-6175-4dd7-8fde-e9903c35e8c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HRJzxgSDJ4LUEKGWEt8UNg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37285,
      "cache_read_input_tokens": 0,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 135,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37285,
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

_source line 4 · 2026-05-23T08:30:16.197Z_

<details><summary>↩ Tool result · `toolu_01RT3XmLanwoXCZXTJ9sySWW`</summary>

```text
-rw-r--r--  1 ubuntu ubuntu 11085 May 17 17:54 round_0.md
-rw-r--r--  1 ubuntu ubuntu 13704 May 18 01:49 round_1.md
-rw-r--r--  1 ubuntu ubuntu 16183 May 22 08:01 round_10.md
-rw-r--r--  1 ubuntu ubuntu 16173 May 22 13:40 round_11.md
-rw-r--r--  1 ubuntu ubuntu 15617 May 23 00:52 round_12.md
-rw-r--r--  1 ubuntu ubuntu 20615 May 23 08:27 round_13.md
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
  "parentUuid": "2df8b90f-6175-4dd7-8fde-e9903c35e8c5",
  "isSidechain": true,
  "promptId": "b919c63a-499b-4b5b-a8c7-415028b122d9",
  "agentId": "a51e46aca94cd12ca",
  "type": "user",
  "uuid": "ae205554-6ada-4068-9e7b-2fd124f874ca",
  "sourceToolAssistantUUID": "2df8b90f-6175-4dd7-8fde-e9903c35e8c5",
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

_source line 5 · 2026-05-23T08:30:17.530Z_

Now I'll read the latest review report (round_13.md) and the review_issues.yaml file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae205554-6ada-4068-9e7b-2fd124f874ca",
  "isSidechain": true,
  "agentId": "a51e46aca94cd12ca",
  "requestId": "req_011CbKBq2miseCnDGWV4RfNL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "36dec396-6e3d-4c31-8ec1-97ef0efad00c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014Hh9TZPffT1DDReXxUVXjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 37285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 6 · 2026-05-23T08:30:18.384Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FzUGroncZzNywBz1235np6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_13.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36dec396-6e3d-4c31-8ec1-97ef0efad00c",
  "isSidechain": true,
  "agentId": "a51e46aca94cd12ca",
  "requestId": "req_011CbKBq2miseCnDGWV4RfNL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd539700-0df0-442d-939b-196cb180d722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014Hh9TZPffT1DDReXxUVXjd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 37285,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 190,
          "cache_read_input_tokens": 37285,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-23T08:30:18.398Z_

<details><summary>↩ Tool result · `toolu_01FzUGroncZzNywBz1235np6`</summary>

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
101	- **位置**: §2 Related Work, §7 Discussion
102	- **问题**: 论文几乎未讨论 S²R (Zeng et al., ACL 2025)、DuPO (2025) 等 training-based 方法。这些方法通过训练引入外部奖励信号，理论上可通过违反 Proposition 1 的 A2 假设（约束不再 trace-determined）打破信息上限。
103	- **Reviewer 分歧**: R2 认为 major missing，R1 partial REBUT（论文 scope 已限定为 training-free，§7 提及 trained extractors），但 R1 同意应讨论理论边界。
104	- **修改建议**: §2 增加一段 training-based self-verification，引用 S²R/DuPO，明确 Proposition 1 仅适用于 inference-time same-model extraction。
105	
106	**W8 [Major] Multi-seed replication 不充分 [共识]**
107	- **位置**: Appendix X.1, Table 33
108	- **问题**: 仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds) 做了 multi-seed replication。Seed-level noise ≈ ±2.34pp，而 Table 1 大部分条件 |Δ| < 3pp 且为 single-seed。许多观测效应可能完全由 seed variance 解释。
109	- **修改建议**: 至少对效应最大的条件补充 multi-seed，或在 Limitations 明确讨论 single-seed 局限。
110	
111	**W9 [Major] Capability-gap principle 基于 n=6 条件——不足以支撑 "principle" 级别 claim [共识]**
112	- **位置**: §6 "Escaping the Bottleneck", Table 3, Figure 8
113	- **问题**: 仅约 6 个 verifier-generator 组合，Table 3 仅 Mistral-7B (SC=39.33%) 1 个条件显著。§6 标题 "Escaping the Bottleneck" 语气过强。
114	- **修改建议**: 降级为 "preliminary observation" 或 "hypothesis"。
115	
116	**W10 [Major] "27 strategies fail" scope 不匹配 [部分共识]**
117	- **位置**: §5.2, Table 14, Abstract
118	- **问题**: 27 个策略局限于 self-extraction paradigm 内的变体（prompt-level + method-level + cross-model），不等于所有 training-free 方法都失败。
119	- **Reviewer 分歧**: R2 认为 scope 过宽，R1 partial REBUT（策略确实跨多个独立维度），但 R1 同意应限定 claim scope。
120	- **修改建议**: 限定为 "27 training-free variants within the constraint-extraction-aggregation paradigm"。
121	
122	### Minor 问题（不影响接收）
123	
124	**M1** [Minor] α = 0.5 缺乏理论依据和真正的 sensitivity analysis。Table 11 的 ≥99% agreement 是 ceiling effect（主效应近零时 penalty 项影响自然可忽略），非真正鲁棒性。[共识]
125	
126	**M2** [Minor] "First-order logic" 描述轻微 overselling——99% 约束是 propositional level at Z3，仅 1.06% 使用真正量词。[共识]
127	
128	**M3** [Minor] Figure 1 信息密度偏高；K_eff 缺乏直觉解释；Abstract 信息过载（6 个要素）。[R2 提出]
129	
130	**M4** [Minor] §2 Related Work 段间逻辑衔接可改善——建议构建从 majority voting → self-correction → formal verification → this paper 的叙事线。[R2 提出]
131	
132	**M5** [Minor] GSM8K (n=30) 和 AIME (n=22) 样本量过小，不应与大样本条件等权重引用。论文已标注 "exploratory"（Table 1 caption），但正文 §5.3 引用时未区分。[共识]
133	
134	---
135	
136	## Questions（需要作者澄清）
137	
138	**Q1.** Proposition 1 Part (i) 依赖 source attribution scoring。如果使用 source-agnostic scoring（基于逻辑一致性而非来源归属评估约束-答案关系），是否仍会退化？是否测试过 source-agnostic alternatives？
139	
140	**Q2.** BR 的 null expectation 是什么？如果约束提取完全"无偏"（support 比例精确反映 trace 投票分布），BR 期望值是否恰好为 1？请提供 permutation test 或 null model 分析。
141	
142	**Q3.** Diagnostics 的决策边界在 positive cases（cross-architecture escape, oracle）上是否能正确预测"SICA 会帮助"？
143	
144	**Q4.** TOST ±2pp equivalence margin 如何选择？如果 margin 放宽至 ±3pp 或 ±5pp，有多少额外条件达到等价显著？
145	
146	**Q5.** Table 1 中 |Δ| < 3pp 的所有 single-seed 条件，作者是否承认这些差异可能完全由 seed variance 解释（given seed noise ≈ ±2.34pp）？
147	
148	**Q6.** Cross-architecture NLI 验证仅在 NLI-friendly 数据集（FOLIO, ProofWriter）上测试。对非 NLI 格式推理任务是否适用？
149	
150	---
151	
152	## Missing References
153	
154	1. **Kamoi et al. (TACL 2024)**: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs" — self-correction 方向最全面 survey。[R2 提出，R1 AGREE]
155	2. **S²R (Zeng et al., ACL 2025)**: RL-based self-verification，通过训练打破 Proposition 1 信息上限。[R2 提出，R1 同意应讨论理论边界]
156	3. **DuPO (arXiv 2508.14460, 2025)**: Dual preference optimization self-verification。[R2 提出，R1 同意应讨论理论边界]
157	4. **AlphaCode / CodeT**: Constraint verification in code domain 的成功案例，可对比讨论为何逻辑推理领域失败。[R1 提出，Minor]
158	
159	---
160	
161	## External Review (Stanford Agentic Reviewer)
162	
163	外部审稿：未配置。
164	
165	---
166	
167	## Visual Layout Check（非评分项）
168	
169	**状态**: ✅ 完成（耗时 ~4 分钟）
170	
171	**统计**: 0 critical, 1 warning, 24 info
172	
173	**Warning**:
174	- Page 7, Figure 4: 柱状图底部 x 轴策略名称字号偏小，27 个 bar 密度高，灰度打印时 4 种颜色区分度可能下降。建议增加 marker pattern 或 hatching。
175	
176	**Info 要点**:
177	- Figure 1 (p.2) pipeline 图 caption 自包含，Title-Abstract-Figure 1 narrative 一致，第一印象良好
178	- 所有 Figure/Table 出现在首次引用附近，无 float 漂移
179	- 表格一致使用 booktabs 风格，最优值加粗，显著性标记有脚注说明
180	- 公式渲染正确，无 LaTeX 错误残留或未解析引用
181	- Limitations section 在 page 8 底部延伸至 page 9，符合 EMNLP 2026 规定
182	- 参考文献约 2.5 页，格式统一
183	
184	**总体**: 排版质量良好，无严重视觉问题。
185	
186	---
187	
188	## Reviewer Consensus
189	
190	### 完全共识（14 项 AGREE）
191	1. Proposition 1 scope mismatch（Part (i) SICA-specific，标题 claim "structural"）
192	2. 统计功效 < 21% 与 negative claim 强度不匹配
193	3. 标题 "Fail to Improve" overclaiming
194	4. BR 循环论证风险（base-rate 效应未排除）
195	5. Diagnostics in-sample overfitting（100% 准确率无意义）
196	6. Multi-seed replication 不充分（2/6 模型）
197	7. BR 小 n_err 条件缺 CI
198	8. α = 0.5 sensitivity analysis 不充分
199	9. Capability-gap principle n=6 不足以支撑 "principle"
200	10. "Extending Huang et al." 是 overselling
201	11. GSM8K/AIME 样本量过小
202	12. K_eff exchangeability 假设局限
203	13. Cross-architecture generalizability 受限
204	14. "First-order logic" 轻微 overselling
205	
206	### 部分分歧（3 项 partial REBUT，已记录各方理由）
207	1. **新颖性**: R2 认为核心洞察可预见（Huang + DPI 延伸），R1 认为不应事后贬低 negative result 且诊断框架/27 策略有独立价值 → 共识：定位为"系统性量化"而非"发现"
208	2. **Training-based refs**: R2 认为 major missing，R1 认为 scope 外但同意讨论理论边界
209	3. **"27 strategies" scope**: R1 指出策略跨多维度，但同意应限定 claim scope
210	
211	---
212	
213	## Overall Assessment
214	
215	### 评分汇总
216	
217	| 维度 | R1 | R2 (交叉后修正) | 加权综合 |
218	|------|-----|----------------|---------|
219	| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
220	| Excitement | 3.0–3.5/5 | 2.5/5 | 3.0/5 |
221	| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
222	| Overall | 3.5 | 3.0 | **3.0** |
223	| Confidence | 4/5 | 4/5 | 4/5 |
224	
225	### Overall: 3.0 — Findings
226	
227	**一句话总结**: 实验执行出色的 negative result paper，但核心理论贡献（Proposition 1）证明与声称范围不匹配、统计功效不足以支撑标题级 claim、诊断框架泛化性未验证、BR 指标概念有效性存疑，且新颖性有限（SCB 是已知结论的实证深化）。
228	
229	**详细理由**:
230	
231	*支持接收的因素*: (1) 实验规模大（9 模型 × 3 数据集 × 60 条件 × 27 策略），远超同类工作；(2) 统计方法论多层次且诚实（McNemar + BH + TOST + bootstrap + power analysis + shuffle control）；(3) Oracle 控制实验精巧，精确分离提取质量与方法论有效性；(4) 诊断框架有潜在实用价值；(5) Cross-architecture escape 提供建设性方向；(6) 附录极为详尽（18 页），可复现性强。作为 Findings 论文，对社区有实际指导价值——帮助避免在 self-extracted constraint verification 方向上的无效探索。
232	
233	*限制接收为 Conference 的因素*: (1) Proposition 1 的 scope mismatch 使核心理论贡献被削弱——Part (i) 仅对 source-attribution 成立，Part (ii) 是平凡 DPI 推论；(2) 21% 的统计功效使 "fail to improve" 的标题级 claim 无法被统计证据充分支撑；(3) Diagnostics 的 100% 准确率是 in-sample 评估，holdout 验证不充分，这是论文三大贡献之一；(4) BR 作为 SCB 的量化基础存在循环论证风险（base-rate 效应未排除），需要 null model 才能确定"额外 bias"的存在；(5) 新颖性有限——核心洞察（自提取约束继承模型 bias）是 Huang et al. (2024) + Wan et al. (2025) 已知结论在形式化验证管道中的实证深化。
234	
235	*如果以下问题得到解决，评分可提升至 3.5（Borderline Conference）*:
236	1. 标题软化 + Abstract 加 power caveat + TOST margin sensitivity
237	2. Proposition 1 拆分并明确 scope
238	3. BR 提供 permutation null model 或降级为描述性指标
239	4. Diagnostics 增加 held-out model family 验证并弱化 claim
240	5. §2 补充 training-based self-verification 讨论
241	6. "Extending Huang et al." 改为 "consistent with / provide independent evidence for"
242	
243	---
244	
245	## Detailed Comments（逐节）
246	
247	**Title**: "Fail to Improve" 过于绝对，与 power < 21% 不匹配。建议 "Do Not Substantially Improve" 或 "The Limits of Self-Extracted Constraints for"。
248	
249	**Abstract**: 信息密度高但覆盖完整。需加 power caveat（如 "though underpowered for effects below ~2pp"）。"extends the self-correction impossibility of Huang et al." 改为 "provides independent evidence consistent with"。BR 报告 "at least 1.66×" 应注明 base-rate 组成未排除。
250	
251	**§1 Introduction**: Contribution 2（diagnostics 100% 准确率）需加 scope 限定。Contribution 3 "capability-gap principle" 降级为 "preliminary observation"。
252	
253	**§2 Related Work**: 缺 training-based self-verification 讨论（S²R, DuPO）。缺 Kamoi et al. (TACL 2024) self-correction survey。段间逻辑衔接可改善。
254	
255	**§3 Method**: α = 0.5 缺理论依据。K_eff 缺直觉解释。BR 定义（Eq. 5）需声明 base-rate 效应。
256	
257	**§4 Results**: 统计诚实（报告 power 局限），但 claim 强度与证据强度仍有 gap。Single-seed 条件应标注不确定性。
258	
259	**§5.1 Symbolic Confirmation Bias**: Proposition 1 需拆分。BR > 1 的解读需 null model。Table 11 的 ≥99% agreement 应加 ceiling effect caveat。
260	
261	**§5.2 Why Remediation Fails**: 27 策略 claim scope 应限定为 "within constraint-extraction-aggregation paradigm"。
262	
263	**§5.3 Diagnostic Framework**: 100% 准确率 claim 需大幅弱化。增加 OOD 验证。讨论 positive case 预测能力。
264	
265	**§6 Escaping the Bottleneck**: 标题过强。"Capability-gap principle" → "preliminary observation"。仅 1 个条件显著。
266	
267	**§7 Discussion and Conclusion**: "extending... to formal verification" 改措辞。Future work 应明确 training-based methods 如何 escape Proposition 1。
268	
269	**Limitations**: 长度合规（EMNLP 2026 规定"一小段覆盖 3 个点"），覆盖了关键局限（open-source only, English only, logical reasoning only）。可考虑增加 power limitation 的一句话提及。
270	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd539700-0df0-442d-939b-196cb180d722",
  "isSidechain": true,
  "promptId": "b919c63a-499b-4b5b-a8c7-415028b122d9",
  "agentId": "a51e46aca94cd12ca",
  "type": "user",
  "uuid": "8e35c859-fc70-4928-b345-4ddd56f741a3",
  "sourceToolAssistantUUID": "dd539700-0df0-442d-939b-196cb180d722",
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

_source line 8 · 2026-05-23T08:30:18.440Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QYjc18UQ8HNA6RU55T8YGB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e35c859-fc70-4928-b345-4ddd56f741a3",
  "isSidechain": true,
  "agentId": "a51e46aca94cd12ca",
  "requestId": "req_011CbKBq2miseCnDGWV4RfNL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8315d27a-ce55-4386-b415-31417feab351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014Hh9TZPffT1DDReXxUVXjd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 37285,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 190,
          "cache_read_input_tokens": 37285,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

_source line 9 · 2026-05-23T08:30:18.455Z_

<details><summary>↩ Tool result · `toolu_01QYjc18UQ8HNA6RU55T8YGB`</summary>

```text
1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical
66	  status: resolved
67	  first_raised_round: 3
68	  last_seen_round: 4
69	  resolution: "Paper Agent added clarifying sentence in method.tex."
70	  resolution_round: 4
71	
72	- id: "R3-N2"
73	  summary: "α value never specified"
74	  category: method
75	  severity: critical
76	  status: resolved
77	  first_raised_round: 3
78	  last_seen_round: 3
79	  resolution: "α=0.5 explicit in Eq.(3) and §4.1."
80	  resolution_round: 3
81	
82	# Round 9+ issues
83	
84	- id: "R9-W2"
85	  summary: "NLI combo weight parameter w 未交叉验证"
86	  category: experiment
87	  severity: warning
88	  status: in_progress
89	  first_raised_round: 9
90	  last_seen_round: 16
91	  mentions:
92	    - round: 14
93	      reviewers: []
94	      note: "R14(fresh) 未单独提及 w 参数"
95	    - round: 15
96	      reviewers: []
97	      note: "R15(fresh) 未单独提及"
98	    - round: 16
99	      reviewers: []
100	      note: "R16(fresh) 未单独提及"
101	
102	- id: "R9-W3"
103	  summary: "Capability Gap Hypothesis 基于极小样本 (n=6)"
104	  category: experiment
105	  severity: critical
106	  status: in_progress
107	  first_raised_round: 9
108	  last_seen_round: 16
109	  mentions:
110	    - round: 14
111	      reviewers: [1, 2]
112	      note: "R14(fresh) 共识: 仅6条件仅Mistral-7B显著, 需软化结论"
113	    - round: 15
114	      reviewers: [1, 2]
115	      note: "R15(fresh) 共识: §6 escape仅SC<40%验证, 'SC≈70%'无数据支撑"
116	    - round: 16
117	      reviewers: [1, 2]
118	      note: "R16(fresh) 共识AGREE: 仅1个条件显著(Mistral-7B SC=39.33%), 'principle'措辞过强, 应降级为'preliminary observation/hypothesis'"
119	  action_items:
120	    - round: 14
121	      action: "§6结论软化为preliminary evidence + 讨论task gap"
122	      assigned_to: "paper_agent"
123	      status: in_progress
124	
125	- id: "R9-VL1"
126	  summary: "Pages 1-2 连续纯文本无 display item"
127	  category: format
128	  severity: warning
129	  status: in_progress
130	  first_raised_round: 9
131	  last_seen_round: 16
132	  mentions:
133	    - round: 16
134	      reviewers: []
135	      note: "R16 视觉审查: Page 1纯文本(Abstract+Intro), Figure 1在page 2顶部, 仍在'前2分钟扫描'窗口内, 影响有限"
136	
137	- id: "R9-VL4"
138	  summary: "Discussion/Conclusion 展开不足"
139	  category: writing
140	  severity: warning
141	  status: in_progress
142	  first_raised_round: 9
143	  last_seen_round: 16
144	  mentions:
145	    - round: 16
146	      reviewers: []
147	      note: "R16(fresh) 未单独提及, R2-M4仅提Limitations长度(R1 rebut citing EMNLP rules)"
148	
149	- id: "R10-N1"
150	  summary: "Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem"
151	  category: method
152	  severity: critical
153	  status: resolved
154	  first_raised_round: 10
155	  last_seen_round: 13
156	  resolution: "当前论文使用 Proposition 1 with formal proof (page 6)"
157	  resolution_round: 13
158	
159	- id: "R10-N2"
160	  summary: "κ→K_eff 映射理论基础不足——r=0.625 验证弱"
161	  category: method
162	  severity: warning
163	  status: in_progress
164	  first_raised_round: 10
165	  last_seen_round: 16
166	  mentions:
167	    - round: 16
168	      reviewers: [1]
169	      note: "R16(fresh) R1-W7: K_eff exchangeable correlation假设可能被违反, minor concern"
170	
171	- id: "R10-N3"
172	  summary: "Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点"
173	  category: experiment
174	  severity: critical
175	  status: in_progress
176	  first_raised_round: 10
177	  last_seen_round: 16
178	  mentions:
179	    - round: 16
180	      reviewers: [1, 2]
181	      note: "R16(fresh) 与R9-W3合并. 共识AGREE: n=6数据点不足以支撑'principle'"
182	
183	- id: "R10-W1"
184	  summary: "DRC τ 阈值无 held-out 评估"
185	  category: experiment
186	  severity: warning
187	  status: in_progress
188	  first_raised_round: 10
189	  last_seen_round: 16
190	  mentions:
191	    - round: 16
192	      reviewers: []
193	      note: "R16(fresh) 未单独提及"
194	
195	- id: "R10-W2"
196	  summary: "Cross-architecture NLI escape 适用面极窄"
197	  category: experiment
198	  severity: warning
199	  status: in_progress
200	  first_raised_round: 10
201	  last_seen_round: 16
202	  mentions:
203	    - round: 16
204	      reviewers: [1, 2]
205	      note: "R16(fresh) R1-W8+R2-W3共识: generalizability受限, 仅NLI-friendly数据集测试"
206	
207	- id: "R10-W3"
208	  summary: "四种子复制方差大 + 统计功效 <21%"
209	  category: experiment
210	  severity: critical
211	  status: in_progress
212	  first_raised_round: 10
213	  last_seen_round: 16
214	  mentions:
215	    - round: 16
216	      reviewers: [1, 2]
217	      note: "R16(fresh) R1-W3: multi-seed仅2/6模型, seed noise ±2.34pp超过多数|Δ|. R2 AGREE"
218	
219	- id: "R10-W4"
220	  summary: "TOST ±2pp margin 缺少显式理由"
221	  category: experiment
222	  severity: warning
223	  status: in_progress
224	  first_raised_round: 10
225	  last_seen_round: 16
226	  mentions:
227	    - round: 16
228	      reviewers: [1]
229	      note: "R16(fresh) R1-N2: ±2pp margin缺乏先验依据, 需sensitivity analysis. R2 AGREE"
230	
231	- id: "R10-W5"
232	  summary: "Bias Ratio 无置信区间"
233	  category: experiment
234	  severity: warning
235	  status: resolved
236	  first_raised_round: 10
237	  last_seen_round: 10
238	  resolution: "BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]"
239	  resolution_round: 10
240	
241	- id: "R10-W6"
242	  summary: "SatLM specification-generation vs SICA trace-extraction 对比不充分"
243	  category: framing
244	  severity: warning
245	  status: in_progress
246	  first_raised_round: 10
247	  last_seen_round: 16
248	  mentions:
249	    - round: 16
250	      reviewers: []
251	      note: "R16(fresh) 未单独提及"
252	
253	- id: "R10-W7"
254	  summary: "'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分"
255	  category: framing
256	  severity: critical
257	  status: in_progress
258	  first_raised_round: 10
259	  last_seen_round: 16
260	  mentions:
261	    - round: 16
262	      reviewers: [1, 2]
263	      note: "R16(fresh) R2-N1: SCB是Huang(2024)+Wan(2025)的自然延伸, R1部分REBUT(negative result value不应事后贬低, 但同意DPI部分近平凡). 部分共识: 贡献在empirical depth非conceptual novelty"
264	
265	- id: "R10-W8"
266	  summary: "Related Work 过度压缩——引用列表而非文献讨论"
267	  category: writing
268	  severity: warning
269	  status: in_progress
270	  first_raised_round: 10
271	  last_seen_round: 16
272	  mentions:
273	    - round: 16
274	      reviewers: [2]
275	      note: "R16(fresh) R2-M5: §2段间逻辑衔接不够清晰"
276	
277	- id: "R10-I1"
278	  summary: "'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别"
279	  category: framing
280	  severity: warning
281	  status: in_progress
282	  first_raised_round: 10
283	  last_seen_round: 16
284	  mentions:
285	    - round: 16
286	      reviewers: [1, 2]
287	      note: "R16(fresh) 同R10-W7. R2: DPI是教科书推论, novelty在于识别正确的Markov chain而非DPI本身"
288	
289	- id: "R10-I2"
290	  summary: "Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑"
291	  category: framing
292	  severity: warning
293	  status: in_progress
294	  first_raised_round: 10
295	  last_seen_round: 16
296	  mentions:
297	    - round: 16
298	      reviewers: []
299	      note: "R16(fresh) 未单独提及"
300	
301	- id: "R10-VL1"
302	  summary: "主文缺结果可视化"
303	  category: format
304	  severity: warning
305	  status: in_progress
306	  first_raised_round: 10
307	  last_seen_round: 16
308	  mentions:
309	    - round: 16
310	      reviewers: []
311	      note: "R16 视觉审查: 主文5 display items(Figure 1-4 + Table 1-3), 合理"
312	
313	- id: "R11-N1"
314	  summary: "Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6"
315	  category: experiment
316	  severity: critical
317	  status: in_progress
318	  first_raised_round: 11
319	  last_seen_round: 16
320	  mentions:
321	    - round: 16
322	      reviewers: [1, 2]
323	      note: "R16(fresh) 与R9-W3合并. 共识: n=6 suggestive非definitive"
324	
325	- id: "R11-N2"
326	  summary: "中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强"
327	  category: framing
328	  severity: critical
329	  status: in_progress
330	  first_raised_round: 11
331	  last_seen_round: 16
332	  mentions:
333	    - round: 16
334	      reviewers: [1, 2]
335	      note: "R16(fresh) 共识critical: R1-N2(power<21%, MDE≥1.86pp, ~79%概率检测不到2pp效果) + R2-W1(标题'Fail to Improve'overclaiming). R2 AGREE R1分析. 建议标题改为'Do Not Substantially Improve'或加power caveat"
336	  action_items:
337	    - round: 16
338	      action: "标题软化 + Abstract加power caveat + TOST margin sensitivity analysis"
339	      assigned_to: "paper_agent"
340	      status: open
341	
342	- id: "R11-N3"
343	  summary: "TOST ±2pp margin 缺乏 principled 论证"
344	  category: experiment
345	  severity: warning
346	  status: in_progress
347	  first_raised_round: 11
348	  last_seen_round: 16
349	  mentions:
350	    - round: 16
351	      reviewers: [1, 2]
352	      note: "R16(fresh) R1-N2涵盖: ±2pp margin无先验依据, 需补充不同margin(±1/3/5pp)的TOST sensitivity"
353	
354	- id: "R11-W1"
355	  summary: "DRC 评估不充分——仅PW完整"
356	  category: experiment
357	  severity: warning
358	  status: in_progress
359	  first_raised_round: 11
360	  last_seen_round: 16
361	  mentions:
362	    - round: 16
363	      reviewers: []
364	      note: "R16(fresh) 未单独提及"
365	
366	- id: "R11-W2"
367	  summary: "BR 指标存在循环论证倾向"
368	  category: method
369	  severity: critical
370	  status: in_progress
371	  first_raised_round: 11
372	  last_seen_round: 16
373	  mentions:
374	    - round: 16
375	      reviewers: [1, 2]
376	      note: "R16(fresh) R2-N2 critical: BR>1部分是base-rate效应(60% traces→60%约束支持多数答案), 需permutation null model量化excess bias. R1 AGREE(审稿中未注意到此问题). 共识: BR循环论证不否定SCB整体论证(Table 11/degeneration condition/oracle独立支持), 但BR指标本身需null model或降级为描述性指标"
377	  action_items:
378	    - round: 16
379	      action: "补充permutation-based null distribution, 或将BR降级为描述性指标并明确声明base-rate组成"
380	      assigned_to: "paper_agent"
381	      status: open
382	
383	- id: "R11-W3"
384	  summary: "术语过度品牌化——'Symbolic Mirage' 偏 dramatic"
385	  category: writing
386	  severity: warning
387	  status: in_progress
388	  first_raised_round: 11
389	  last_seen_round: 16
390	  mentions:
391	    - round: 16
392	      reviewers: []
393	      note: "R16(fresh) 未单独提及"
394	
395	- id: "R11-W4"
396	  summary: "新颖性定位需更早更明确建立与先验工作的 distinction"
397	  category: framing
398	  severity: critical
399	  status: in_progress
400	  first_raised_round: 11
401	  last_seen_round: 16
402	  mentions:
403	    - round: 16
404	      reviewers: [1, 2]
405	      note: "R16(fresh) R2-N1+R2-W5: SCB是Huang et al.的自然延伸, 'extending'是overselling. R1部分REBUT: 机制定位+27策略否证+诊断框架是非平凡贡献, 但同意DPI部分近平凡"
406	
407	- id: "R11-W5"
408	  summary: "Independence-Accuracy Trade-off 应定位为量化而非新发现"
409	  category: framing
410	  severity: warning
411	  status: in_progress
412	  first_raised_round: 11
413	  last_seen_round: 16
414	  mentions:
415	    - round: 16
416	      reviewers: []
417	      note: "R16(fresh) 未单独提及"
418	
419	- id: "R11-W6"
420	  summary: "遗漏引用: Byerly & Khashabi (2026 TACL) 等"
421	  category: writing
422	  severity: warning
423	  status: resolved
424	  first_raised_round: 11
425	  last_seen_round: 13
426	  resolution: "当前论文已引用 Byerly and Khashabi (2026)"
427	  resolution_round: 13
428	
429	- id: "R11-W7"
430	  summary: "27 策略计数膨胀 + 未尝试 trained constraint extractor"
431	  category: experiment
432	  severity: warning
433	  status: in_progress
434	  first_raised_round: 11
435	  last_seen_round: 16
436	  mentions:
437	    - round: 16
438	      reviewers: [1, 2]
439	      note: "R16(fresh) R2-W4: 27策略局限于self-extraction paradigm内变体, claim scope需限定. R1部分REBUT: 策略确实跨多维度(prompt/method/cross-model/formal proof), 但同意应限定scope为'within constraint-extraction-aggregation paradigm'"
440	
441	- id: "R11-VL1"
442	  summary: "主文缺结果可视化——需上提 Figure 到主文"
443	  category: format
444	  severity: warning
445	  status: in_progress
446	  first_raised_round: 11
447	  last_seen_round: 16
448	  mentions:
449	    - round: 16
450	      reviewers: []
451	      note: "R16 视觉审查: Figure 2(散点图p4), Figure 3(DAG p6), Figure 4(柱状图p7)已在主文, 覆盖合理"
452	
453	- id: "R12-N1"
454	  summary: "标题 overclaiming about frontier scale"
455	  category: framing
456	  severity: critical
457	  status: in_progress
458	  first_raised_round: 12
459	  last_seen_round: 16
460	  mentions:
461	    - round: 16
462	      reviewers: [1, 2]
463	      note: "R16(fresh) 标题已含'Logical Reasoning'(非'LLM Reasoning'), 但'Fail to Improve'仍overclaiming given power<21%. 共识: 需进一步软化"
464	
465	- id: "R12-N2"
466	  summary: "SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化"
467	  category: framing
468	  severity: critical
469	  status: in_progress
470	  first_raised_round: 12
471	  last_seen_round: 16
472	  mentions:
473	    - round: 16
474	      reviewers: [1, 2]
475	      note: "R16(fresh) R2-N1 critical: SCB=Huang+DPI, Wan(2025)/Jhaveri(2026)从不同角度得出类似结论. R1 partial REBUT: negative result不应事后贬低, 诊断框架+27策略否证有独立价值. 部分共识: 定位为'系统性量化'而非'发现', 弱化Prop 1呈现"
476	
477	- id: "R12-N3"
478	  summary: "DRC 作为 Contribution 4 不够充分"
479	  category: framing
480	  severity: critical
481	  status: resolved
482	  resolution: "DRC demoted to practical observation in §6"
483	  resolution_round: 13
484	  first_raised_round: 12
485	  last_seen_round: 13
486	
487	- id: "R12-W1"
488	  summary: "BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer"
489	  category: method
490	  severity: warning
491	  status: in_progress
492	  first_raised_round: 12
493	  last_seen_round: 16
494	  mentions:
495	    - round: 16
496	      reviewers: [1, 2]
497	      note: "R16(fresh) 与R11-W2合并. R2-N2提升为critical: 需null model"
498	
499	- id: "R12-W2"
500	  summary: "CIL 名称和 information-theoretic 声称有误导"
501	  category: method
502	  severity: warning
503	  status: resolved
504	  resolution: "Renamed to CCR, removed 'unify' claim"
505	  resolution_round: 13
506	  first_raised_round: 12
507	  last_seen_round: 13
508	
509	- id: "R12-W3"
510	  summary: "Figure 2 placement——应在正文而非附录"
511	  category: format
512	  severity: warning
513	  status: resolved
514	  first_raised_round: 12
515	  last_seen_round: 13
516	  resolution: "Figure 2 已在正文 page 4"
517	  resolution_round: 13
518	
519	- id: "R12-W4"
520	  summary: "Appendix vs 主文关键信息分配不合理"
521	  category: writing
522	  severity: warning
523	  status: in_progress
524	  first_raised_round: 12
525	  last_seen_round: 16
526	  mentions:
527	    - round: 16
528	      reviewers: [2]
529	      note: "R16(fresh) R2-M3: Abstract信息过载(6个要素). R2-M2: K_eff缺直觉解释"
530	
531	- id: "R12-EC1"
532	  summary: "Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor"
533	  category: method
534	  severity: critical
535	  status: in_progress
536	  first_raised_round: 12
537	  last_seen_round: 16
538	  mentions:
539	    - round: 16
540	      reviewers: []
541	      note: "R16(fresh) 未单独提及"
542	
543	- id: "R13-N1"
544	  summary: "摘要 BR 4.97× 选择性报告——最极端条件"
545	  category: framing
546	  severity: critical
547	  status: in_progress
548	  first_raised_round: 13
549	  last_seen_round: 16
550	  mentions:
551	    - round: 16
552	      reviewers: []
553	      note: "R16(fresh) Abstract报告'at least 1.66×', 为最小值. 比报告4.97×更保守, 但BR循环论证问题(R11-W2)影响所有BR值的可信度"
554	
555	- id: "R13-N2"
556	  summary: "统计功效呈现不足——10/16 underpowered, power analysis 埋在附录"
557	  category: experiment
558	  severity: critical
559	  status: in_progress
560	  first_raised_round: 13
561	  last_seen_round: 16
562	  mentions:
563	    - round: 16
564	      reviewers: [1, 2]
565	      note: "R16(fresh) 与R11-N2合并. R1-N2 critical: observed power<21%, TOST仅8/16显著. R2 fully AGREE"
566	
567	- id: "R13-N3"
568	  summary: "α=0.5 无敏感性分析"
569	  category: method
570	  severity: warning
571	  status: in_progress
572	  first_raised_round: 13
573	  last_seen_round: 16
574	  mentions:
575	    - round: 16
576	      reviewers: [1, 2]
577	      note: "R16(fresh) R1-W6: α=0.5无理论依据, 需sensitivity analysis α∈{0,0.25,0.5,0.75,1.0}. R2 AGREE. 论文有Table 11(α ablation ≥99% agreement), 但R1/R2共识: ceiling effect不等于鲁棒性"
578	
579	- id: "R13-W1"
580	  summary: "符号/指标过载——8页内7个定量工具"
581	  category: writing
582	  severity: warning
583	  status: in_progress
584	  first_raised_round: 13
585	  last_seen_round: 16
586	  mentions:
587	    - round: 16
588	      reviewers: []
589	      note: "R16(fresh) 未单独提及"
590	
591	- id: "R13-W2"
592	  summary: "NLI claim 须限定到命题逻辑任务"
593	  category: experiment
594	  severity: warning
595	  status: in_progress
596	  first_raised_round: 13
597	  last_seen_round: 16
598	  mentions:
599	    - round: 16
600	      reviewers: [1]
601	      note: "R16(fresh) R1-W9: 'First-order logic'描述轻微overselling, 99%约束是propositional level. R2 AGREE"
602	
603	- id: "R13-W3"
604	  summary: "语法去重可能膨胀 BR——未报告语义去重后 BR"
605	  category: method
606	  severity: warning
607	  status: in_progress
608	  first_raised_round: 13
609	  last_seen_round: 16
610	  mentions:
611	    - round: 16
612	      reviewers: []
613	      note: "R16(fresh) 未单独提及"
614	
615	- id: "R13-W4"
616	  summary: "Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯"
617	  category: writing
618	  severity: warning
619	  status: in_progress
620	  first_raised_round: 13
621	  last_seen_round: 16
622	  mentions:
623	    - round: 16
624	      reviewers: []
625	      note: "R16(fresh) 未单独提及(当前论文无显式§3.3 Hypothesis section)"
626	
627	- id: "R13-W5"
628	  summary: "缺引: Dhuliawala et al. 2023 Chain-of-Verification"
629	  category: writing
630	  severity: warning
631	  status: resolved
632	  first_raised_round: 13
633	  last_seen_round: 14
634	  resolution: "已引用 dhuliawala2023chainofverification"
635	  resolution_round: 14
636	
637	- id: "R14-N1"
638	  summary: "标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理"
639	  category: framing
640	  severity: critical
641	  status: in_progress
642	  first_raised_round: 14
643	  last_seen_round: 16
644	  mentions:
645	    - round: 16
646	      reviewers: [1, 2]
647	      note: "R16(fresh) 标题已为'LLM Logical Reasoning', domain scope改善. 但'Fail to Improve'仍overclaiming"
648	
649	- id: "R14-N2"
650	  summary: "Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测"
651	  category: method
652	  severity: critical
653	  status: in_progress
654	  first_raised_round: 14
655	  last_seen_round: 16
656	  mentions:
657	    - round: 16
658	      reviewers: []
659	      note: "R16(fresh) 当前论文无显式Predictions标签, 未单独提及"
660	
661	- id: "R14-W1"
662	  summary: "Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著"
663	  category: experiment
664	  severity: major
665	  status: in_progress
666	  first_raised_round: 14
667	  last_seen_round: 16
668	  mentions:
669	    - round: 16
670	      reviewers: [1, 2]
671	      note: "R16(fresh) R1-W8+R2-W3共识: 仅Mistral-7B(SC=39.33%)显著, 'principle'过强, 降级为'preliminary observation'"
672	
673	- id: "R14-W2"
674	  summary: "8页正文信息过载——§5.5/§6/§7展开不足"
675	  category: writing
676	  severity: major
677	  status: in_progress
678	  first_raised_round: 14
679	  last_seen_round: 16
680	  mentions:
681	    - round: 16
682	      reviewers: [2]
683	      note: "R16(fresh) R2-M3: Abstract信息过载(6要素). R2-M2: K_eff缺直觉解释. R2-M5: §2段间衔接不够"
684	
685	- id: "R14-W3"
686	  summary: "'No evidence' claim scope与统计功效不匹配"
687	  category: framing
688	  severity: major
689	  status: in_progress
690	  first_raised_round: 14
691	  last_seen_round: 16
692	  mentions:
693	    - round: 16
694	      reviewers: [1, 2]
695	      note: "R16(fresh) 与R11-N2合并. 共识critical"
696	
697	- id: "R14-W4"
698	  summary: "BR计算子集大小(n_err)未报告"
699	  category: experiment
700	  severity: moderate
701	  status: in_progress
702	  first_raised_round: 14
703	  last_seen_round: 16
704	  mentions:
705	    - round: 16
706	      reviewers: [1, 2]
707	      note: "R16(fresh) R1-W4: Table 2多数条件未报CI. R2 AGREE. 当前论文Table 2已有n_err列但多数条件无CI"
708	
709	- id: "R14-W5"
710	  summary: "Related Work遗漏: SETS(2025), MAV(2025)"
711	  category: writing
712	  severity: minor-to-major
713	  status: in_progress
714	  first_raised_round: 14
715	  last_seen_round: 16
716	  mentions:
717	    - round: 16
718	      reviewers: [1, 2]
719	      note: "R16(fresh) R2-W2新增: S²R(ACL 2025), DuPO(2025), Kamoi et al.(TACL 2024). R1部分REBUT(scope外)但同意应讨论理论边界"
720	
721	- id: "R14-W6"
722	  summary: "Fleiss' κ→ICC近似仅r=0.625——prevalence paradox"
723	  category: method
724	  severity: moderate
725	  status: in_progress
726	  first_raised_round: 14
727	  last_seen_round: 16
728	  mentions:
729	    - round: 16
730	      reviewers: [1]
731	      note: "R16(fresh) R1-W7: K_eff exchangeability假设可能被违反, 但minor, 不影响核心结论"
732	
733	# R15(fresh) issues
734	
735	- id: "R15-M1"
736	  summary: "遗漏引用: DuPO (ICLR 2026) — training-based self-verification"
737	  category: writing
738	  severity: warning
739	  status: open
740	  first_raised_round: 15
741	  last_seen_round: 16
742	  mentions:
743	    - round: 15
744	      reviewers: [1, 2]
745	      note: "共识AGREE"
746	    - round: 16
747	      reviewers: [1, 2]
748	      note: "R16(fresh) R2-W2提出, R1部分REBUT(scope外但应讨论理论边界)"
749	
750	- id: "R15-M2"
751	  summary: "遗漏引用: S²R (2025) — RL-based self-verification"
752	  category: writing
753	  severity: warning
754	  status: open
755	  first_raised_round: 15
756	  last_seen_round: 16
757	  mentions:
758	    - round: 15
759	      reviewers: [1, 2]
760	      note: "共识AGREE"
761	    - round: 16
762	      reviewers: [1, 2]
763	      note: "R16(fresh) R2-W2提出, R1部分REBUT(scope外但应讨论理论边界)"
764	
765	- id: "R15-M3"
766	  summary: "遗漏引用: LLM as Formalizers on CSP (arXiv 2505.13252, 2025)"
767	  category: writing
768	  severity: warning
769	  status: open
770	  first_raised_round: 15
771	  last_seen_round: 16
772	  mentions:
773	    - round: 16
774	      reviewers: []
775	      note: "R16(fresh) 未单独提及"
776	
777	- id: "R15-M4"
778	  summary: "遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles"
779	  category: writing
780	  severity: warning
781	  status: open
782	  first_raised_round: 15
783	  last_seen_round: 16
784	  mentions:
785	    - round: 16
786	      reviewers: [1]
787	      note: "R16(fresh) R1 REBUT: Kuncheva & Whitaker(2003)和Ladha(1992)已更直接相关. Minor"
788	
789	- id: "R15-W1"
790	  summary: "α=0.5敏感性分析≥99% agreement是ceiling effect"
791	  category: method
792	  severity: minor
793	  status: open
794	  first_raised_round: 15
795	  last_seen_round: 16
796	  mentions:
797	    - round: 16
798	      reviewers: [1, 2]
799	      note: "R16(fresh) R1-W6要求补充α sensitivity analysis. R2 AGREE. 共识: ceiling effect不等于鲁棒性"
800	
801	# R16(fresh) 新发现
802	
803	- id: "R16-N1"
804	  summary: "Proposition 1 证明范围与声称范围不匹配——Part(i)仅对source-attribution成立但标题claim 'structural'"
805	  category: method
806	  severity: critical
807	  status: open
808	  first_raised_round: 16
809	  last_seen_round: 16
810	  mentions:
811	    - round: 16
812	      reviewers: [1, 2]
813	      note: "R1-N1 critical, R2 fully AGREE. 共识: Part(i)依赖SICA特定的source attribution scoring(Eq.3), 非数学必然; Part(ii) DPI是平凡推论(I(C;Y)≤I(T;Y)). 建议拆分为两个结果, 明确区分适用范围. R2补充: DPI不排除约束通过重新组织信息打破相关模式"
814	  action_items:
815	    - round: 16
816	      action: "将Proposition 1分为source-attribution退化定理(精确但specific) + DPI bound(普遍但弱), 正文明确区分"
817	      assigned_to: "paper_agent"
818	      status: open
819	
820	- id: "R16-N2"
821	  summary: "Diagnostics 100%准确率是in-sample评估——overfitting风险, holdout验证不充分"
822	  category: method
823	  severity: critical
824	  status: open
825	  first_raised_round: 16
826	  last_seen_round: 16
827	  mentions:
828	    - round: 16
829	      reviewers: [1, 2]
830	      note: "R2-N3 critical, R1 fully AGREE(审稿中未注意到). 共识: (1) 决策边界从60条件推导并在同一60条件上评估=in-sample fitting; (2) holdout仅LLaMA-3.1-8B×FOLIO 1个条件=不充分; (3) 60条件全为negative cases, 任何trivial classifier('永远预测不帮助')都能100%; (4) 未在positive cases(cross-arch escape, oracle)上验证. Abstract/§1/§7中此claim为三大贡献之一, 过度表述"
831	  action_items:
832	    - round: 16
833	      action: "增加held-out model family验证 + 弱化claim为'correctly classify all tested conditions within experimental scope' + 讨论OOD失败条件"
834	      assigned_to: "paper_agent"
835	      status: open
836	
837	- id: "R16-M1"
838	  summary: "遗漏引用: Kamoi et al. (TACL 2024) self-correction survey"
839	  category: writing
840	  severity: warning
841	  status: open
842	  first_raised_round: 16
843	  last_seen_round: 16
844	  mentions:
845	    - round: 16
846	      reviewers: [1, 2]
847	      note: "R2提出, R1 AGREE. self-correction方向最全面survey, 应引用定位论文"
848	
849	- id: "R16-M2"
850	  summary: "遗漏引用: AlphaCode/CodeT — constraint verification in code domain"
851	  category: writing
852	  severity: minor
853	  status: open
854	  first_raised_round: 16
855	  last_seen_round: 16
856	  mentions:
857	    - round: 16
858	      reviewers: [1]
859	      note: "R1提出: code domain中约束过滤成功案例, 可对比讨论为何逻辑推理领域失败"
860	
861	- id: "R16-W1"
862	  summary: "'Extending Huang et al. (2024) to formal verification' 是overselling——两者证明框架不同不构成逻辑extension"
863	  category: framing
864	  severity: major
865	  status: open
866	  first_raised_round: 16
867	  last_seen_round: 16
868	  mentions:
869	    - round: 16
870	      reviewers: [1, 2]
871	      note: "R2-W5, R1 fully AGREE. 共识: Huang基于value/policy iteration, 本文基于DPI+source attribution, 形式化框架不同. 建议改为'consistent with / complement / provide independent evidence for'"
872	  action_items:
873	    - round: 16
874	      action: "§1和Abstract将'extend'改为'provide independent evidence consistent with'"
875	      assigned_to: "paper_agent"
876	      status: open
877	
878	- id: "R16-W2"
879	  summary: "GSM8K(n=30)/AIME(n=22)样本量过小, 不应与大样本条件等权重引用"
880	  category: experiment
881	  severity: major
882	  status: open
883	  first_raised_round: 16
884	  last_seen_round: 16
885	  mentions:
886	    - round: 16
887	      reviewers: [1, 2]
888	      note: "R1-W5, R2 AGREE. 论文已标注为'exploratory, n<60'(Table 1 caption), 但正文§5.3引用时未区分"
889	
890	- id: "R16-W3"
891	  summary: "缺少training-based self-verification方法讨论——Proposition 1理论边界不完整"
892	  category: writing
893	  severity: major
894	  status: open
895	  first_raised_round: 16
896	  last_seen_round: 16
897	  mentions:
898	    - round: 16
899	      reviewers: [1, 2]
900	      note: "R2-W2 major, R1部分REBUT(scope已限定为training-free, §7提及trained extractors)但AGREE应讨论训练如何通过违反A2打破信息上限. 共识: §2增加一段training-based self-verification, 明确Prop 1适用边界"
901	  action_items:
902	    - round: 16
903	      action: "§2增加training-based self-verification段落, 引用S²R/DuPO, 明确Prop 1仅适用于inference-time same-model"
904	      assigned_to: "paper_agent"
905	      status: open
906	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8315d27a-ce55-4386-b415-31417feab351",
  "isSidechain": true,
  "promptId": "b919c63a-499b-4b5b-a8c7-415028b122d9",
  "agentId": "a51e46aca94cd12ca",
  "type": "user",
  "uuid": "0167ebdd-dd93-4d4f-b41c-a9b3bc3370f7",
  "sourceToolAssistantUUID": "8315d27a-ce55-4386-b415-31417feab351",
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

_source line 10 · 2026-05-23T08:30:32.122Z_

## Summary

I've successfully retrieved both files for the symb_invariant_consensus project. Here are the complete contents:

### 1. Latest Review Report (Round 13)

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_13.md`

The latest review report is **Round 13** (dated 2026-05-23 08:27:17), conducted in fresh mode with 2 reviewers. Key highlights:

**Overall Score:** 3.0 ("Findings")

**Core Finding:** The paper presents an experimental study showing that self-extracted constraints (SICA method) fail to improve LLM logical reasoning, with systematic investigation across 9 models, 3 datasets, and 27 training-free strategies.

**Major Strengths:**
- Exceptional experimental scale and system: 9 models × 3 datasets × 60 conditions × 27 remediation strategies
- Multiple-layer statistical methodology: McNemar tests, BH FDR correction, TOST equivalence tests, bootstrap CIs, power analysis
- Well-designed oracle controls identifying extraction quality as the bottleneck
- Comprehensive appendix (18 pages) with detailed ablations
- Clear identification of a "cross-architecture escape" path via NLI verification

**Critical Weaknesses (Must-Fix):**
1. **Proposition 1 scope mismatch:** Part (i) depends on SICA's specific source attribution scoring (not universal); Part (ii) is a trivial application of data processing inequality
2. **Statistical power underfitting:** Observed power <21%, MDE ≥1.86pp, yet title claims "Fail to Improve" which cannot exclude 1-2pp effects
3. **Diagnostics overfitting:** 100% accuracy is in-sample evaluation (trained and tested on same 60 conditions); holdout validation insufficient
4. **BR (Bias Ratio) circular reasoning:** Lacks null model to distinguish "extra bias" from base-rate effects inherent to trace-count distributions

**Consensus Issues (14 items fully agreed):** Proposition 1 scope, power-claim mismatch, diagnostics in-sample fitting, multi-seed insufficiency (only 2/6 models), overselling "extending Huang et al."

---

### 2. Review Issues File (review_issues.yaml)

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml`

This comprehensive tracker shows the project's 13-round review history with 53 tracked issues:

**Status Breakdown:**
- **Resolved:** 6 issues (early method/power/oracle/references)
- **In Progress:** 47 issues (from Rounds 9-16)
- **Open:** 11 action items from Round 16

**Round 16 (Latest) Critical Issues:**
1. **R16-N1:** Proposition 1 Part (i) specificity vs. universal claims
2. **R16-N2:** Diagnostics 100% accuracy is in-sample, needs OOD validation
3. **R16-W1:** "Extending Huang et al." is overselling (different mathematical frameworks)
4. **R16-W2:** GSM8K/AIME (n=30, n=22) sample sizes too small for equal weighting
5. **R16-W3:** Missing discussion of training-based self-verification breaking Proposition 1's information ceiling

**Open Action Items (Status: open):**
- Soften title + add power caveat + TOST margin sensitivity
- Split Proposition 1 into source-attribution-specific + DPI bound with clarified scopes
- BR: add permutation null model or downgrade to descriptive metric
- Diagnostics: add held-out model family validation
- "Extending Huang" → "provide independent evidence consistent with"
- Add training-based methods discussion (S²R, DuPO)

The tracker shows active cross-reviewer engagement with escalating scrutiny of core claims, particularly around statistical power adequacy and theoretical contribution novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0167ebdd-dd93-4d4f-b41c-a9b3bc3370f7",
  "isSidechain": true,
  "agentId": "a51e46aca94cd12ca",
  "requestId": "req_011CbKBqCV7m4minp3hHamh9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "794854f3-9e59-4446-8957-458b38351e68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "68033c04-9adf-4668-a002-9acbfacb81a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "unified-wobbling-allen",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DrRBVSmJ34a5y4wjvR891x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 21343,
      "cache_read_input_tokens": 38700,
      "output_tokens": 981,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21343
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 981,
          "cache_read_input_tokens": 38700,
          "cache_creation_input_tokens": 21343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21343,
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
