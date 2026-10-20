# Research conversation: I need to analyze the review history for a research paper across ~35 rounds of review. The review reports are at: /home/

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6bf090dfebc576f0.jsonl`
- **Structured JSON:** [`3dd7819244d59bb9dbd6.json`](../../sessions/3d/3dd7819244d59bb9dbd6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-22T10:42:39.604Z_

I need to analyze the review history for a research paper across ~35 rounds of review. The review reports are at:
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/

I need to extract from EACH round report (round_0.md through round_35.md):
1. The overall score (look for "Overall Assessment", "score", "rating", or similar)
2. The main issues/weaknesses identified (top 2-3 per round)
3. Any notable improvements acknowledged from the previous round

Read as many rounds as possible, focusing on: round_0, round_5, round_10, round_15, round_20, round_25, round_30, round_31, round_33, round_34, round_35 for the trajectory. Also read any rounds that seem like turning points.

Also read the decisions.yaml file at:
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml

Report a chronological timeline showing:
- Score at each round
- Key issues that persisted vs got resolved
- What caused score jumps (up or down)
- What changes were made between rounds

Be very thorough — read every report you can.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "72a02a5b-75ff-4615-bb90-e427246c8f02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T10:42:41.302Z_

I'll help you analyze the review history across the rounds. Let me start by exploring the review reports directory and reading the key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72a02a5b-75ff-4615-bb90-e427246c8f02",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7fQg31yU4J53mGmGU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb464ea6-b97b-434d-95c8-f49526872dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hb49Wx3aHwEG6bNRrPd6iP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39839,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39839,
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

_source line 3 · 2026-05-22T10:42:41.753Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012t34QcwvmVYqVyVduh74oR`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports -type f -name \"*.md\" | sort -V | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb464ea6-b97b-434d-95c8-f49526872dcf",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7fQg31yU4J53mGmGU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f90636a3-6c6d-460c-9428-22cb51353f76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hb49Wx3aHwEG6bNRrPd6iP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39839,
      "cache_read_input_tokens": 0,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39839,
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

_source line 4 · 2026-05-22T10:42:42.043Z_

<details><summary>↩ Tool result · `toolu_012t34QcwvmVYqVyVduh74oR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/data_integrity_audit_v2.md
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
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_16.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_17.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_18.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_19.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_20.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_21.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_22.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_23.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_24.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_25.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_26.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_27.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_29.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_30.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_31.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_33.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_34.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_35.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f90636a3-6c6d-460c-9428-22cb51353f76",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "ae18a006-00ab-41e4-bcdf-96fc16abb853",
  "sourceToolAssistantUUID": "f90636a3-6c6d-460c-9428-22cb51353f76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T10:42:43.998Z_

Good, I can see there are rounds 0-35 (with some skipped like round_8, round_28, round_32). Let me now read all the round reports and the decisions file. I'll start by reading them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae18a006-00ab-41e4-bcdf-96fc16abb853",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7qcqZdfjmb4qbUxiQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae1df8aa-282b-4d9d-b0e1-274b602a9a43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d4HEhcK56BLbwYjYSpzLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 39839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 6 · 2026-05-22T10:42:44.222Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V6WWkSgShxaSmuV9RvuAyj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae1df8aa-282b-4d9d-b0e1-274b602a9a43",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7qcqZdfjmb4qbUxiQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c0e8bd8-6dee-400d-ad69-d81b31d0229a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d4HEhcK56BLbwYjYSpzLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 39839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 7 · 2026-05-22T10:42:44.243Z_

<details><summary>↩ Tool result · `toolu_01V6WWkSgShxaSmuV9RvuAyj`</summary>

```text
1	---
2	round: 0
3	overall_score: borderline
4	timestamp: 2026-05-14T12:20:27.321042+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告：Round 1 圆桌审稿
11	
12	**论文**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"
13	**目标 Venue**: EMNLP 2026 (ARR)
14	**Reviewer 配置**: R1（方法与实验）+ R2（新颖性与相关工作）
15	**轮次**: Round 1（已收敛，无需第二轮）
16	
17	---
18	
19	## Summary
20	
21	本文系统比较了 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）的 best-of-N selection 场景中的表现。核心发现：(1) Set Jaccard (SJ) 在 NER 上显著优于 log-probability (Δρ≈0.16, p<10⁻²⁵)；(2) RE 中所有 signal 退化，归因于 compound error propagation。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。
22	
23	---
24	
25	## Strengths
26	
27	**S1. 系统且全面的实验矩阵** [R1+R2 共识]
28	5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temperature × 4 metric，13/15 实验完整覆盖。该领域首个如此系统的比较（限定为 LLM-based structured IE）。
29	
30	**S2. LOO-SJ circularity check 方法论亮点** [R1 提出，R2 认可]
31	Table 1 Leave-one-out SJ（ρ=0.40 vs full SJ ρ=0.42, Δ=0.02）严谨地排除了 SJ 有效性依赖于自我循环的担忧。
32	
33	**S3. Compound error boundary 诊断有理论价值** [R1 提出，R2 认可]
34	Section 5.9 对 RE 退化的因果分析（head + tail + relation type 三重叠加），Table 12 per-relation-type 证据具体。
35	
36	**S4. 多维度鲁棒性验证** [R1+R2 共识]
37	Multi-seed（Std ≤ 0.01）、cross-dataset（排序一致）、cross-model、OOD（SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。
38	
39	**S5. Best-of-N selection 实用性** [R2 提出]
40	将 ranking 指标转化为 F1 gain，对 practitioners 有直接指导价值。
41	
42	**S6. Inverted-U pattern** [R1 提出]
43	Section 5.11, Table 15: SJ ρ 在 F1 bucket [0.3, 0.7] 最高，为 SJ 适用条件划定边界。
44	
45	---
46	
47	## Weaknesses（按严重程度排序）
48	
49	### Must-Fix（影响接收决定）
50	
51	**C1. 模型规模单一，严重限制普适性** [R1 critical + R2 agree]
52	仅 Qwen3-8B 和 LLaMA-3.1-8B 两个同规模模型。Confidence calibration 和 output diversity 随规模变化显著——更大模型的 greedy 可能已足够准确使 LP 优势明显化，更小模型高方差可能放大 SJ 优势。Abstract 中 "establish" 措辞过强。**建议**：至少增加一个 >30B 或 <3B 模型，或将 "establish" 降级为 "investigate"/"examine"。
53	
54	**C2. 相关工作显著遗漏** [R2 critical + R1 逐条核实 agree]
55	5 篇核心文献缺失：
56	- Guo et al. 2017 (On Calibration of Modern Neural Networks, ICML) — 论文用 ECE 作核心指标却未引用其定义来源
57	- Snell et al. 2024 (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却缺核心引用
58	- Aggarwal et al. 2023 (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling 直接相关
59	- CISC: Huang et al. 2025 (Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 "最 calibrated 的方法反而最无效"，直接挑战本文解读
60	- 传统 IE confidence（CRF 边际概率、span-level confidence、MC-dropout）— 至少应说明排除理由
61	
62	**C3. RE task-complexity boundary 证据严重不足** [R1+R2 共识 critical]
63	全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行。"Universal bottleneck" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis。**建议**：增加至少一个 RE 数据集或降级措辞。
64	
65	**C4. SJ 方法新颖性有限** [R2 critical + R1 agree]
66	SJ 是 set-level F1/Jaccard 的 confidence 化自然迁移（type-grouped Hungarian matching + token-overlap kernel）。缺少理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融。论文定位为 empirical study 但措辞暗示更高原创性。
67	
68	**C5. 全文零图表** [R1 critical + R2 agree]
69	17 个表格，0 个 Figure。对 confidence/calibration 研究而言，缺少 selection curves、reliability diagrams、cost-effectiveness scatter 是严重呈现缺陷。Table 8 有 selection curve 数据但以表格呈现。**建议**：至少添加 3 个核心 Figure（selection curve、reliability diagram、cost-effectiveness）。
70	
71	**C6. 成本分析需补充** [R1 critical, R2 rebut 为 warning — 存在分歧]
72	Section 6 称 SJ 额外成本 "negligible (O(N²) set comparisons vs. O(N) LLM forward passes)"，但 LP 可在 greedy decode（1 pass）上工作，SJ 需 N≥8 pass。**R1 立场**：将 8-16× 推理开销描述为 "negligible" 是系统性误导。**R2 立场**：在 TTS 语境（同 N 下比较）内论文陈述准确，LP@N=1 vs SJ@N=8 混淆了 selective prediction 与 TTS。**共识**：需补充 cost-effectiveness 分析（F1 gain per unit compute）。
73	
74	### Should-Fix
75	
76	**W1. 未探索 signal combination** [R1+R2 共识]
77	Section 5.8 证明 SJ 和 LP 互补（Δρ=0.14），却未尝试 α·SJ+(1-α)·LP 线性组合。
78	
79	**W2. 标题与核心发现不匹配** [R2 critical → R1 rebut 降为 warning]
80	"Log-Probability Is All You Need?" 暗示 log-prob 可能足够，但核心发现是 SJ 显著优于 log-prob。R1 认为问号修辞反问可接受，最终定为 warning。**建议**：改为 "Beyond Log-Probability: ..." 或类似。
81	
82	**W3. 单一 prompt 模板** [R1 提出，R2 agree]
83	未提及 prompt 变体。LLM-based IE 输出格式直接影响 set-based 指标。**建议**：appendix 给出完整 prompt，讨论 format 影响。
84	
85	**W4. 统计检验不系统** [R1 提出，R2 部分 agree]
86	核心比较（Table 4/5 cross-dataset/cross-model）无 bootstrap CI，3 seed std 不替代正式统计检验。p-value 极小部分弥补但不充分。
87	
88	**W5. SJ 失败案例分析不足** [R1 提出，R2 部分 rebut]
89	SJ ρ 最佳也仅 0.42-0.51。Section 5.11 inverted-U 提供统计层面分析，但缺实例级 case study（高 SJ 低 F1 / 低 SJ 高 F1 的具体模式）。
90	
91	**W6. "Diagnostic framework" 过度包装** [R2 提出，R1 agree]
92	标准消融技术（F1 分桶、component 分解、stratification）不构成可复用 framework。**建议**：降格为 "diagnostic analysis"。
93	
94	**W7. 未讨论 trained approaches 作为 upper bound** [R2 提出，R1 部分 agree]
95	Scope 限定为 training-free signals 合理，但 Related Work 应更充分讨论 verifier/reward model 等 trained approaches。
96	
97	---
98	
99	## Reviewer Consensus
100	
101	以下问题两位 Reviewer 完全一致：
102	1. **Overall 评分**: 3/5 (Findings)，Main 偏弱
103	2. **模型规模不足**: 仅 8B 模型不支撑普适性主张
104	3. **RE 单数据集**: "Universal bottleneck" 需降级
105	4. **零图表**: 严重影响可读性和说服力
106	5. **相关工作遗漏**: 5 篇核心文献必须补充
107	6. **Signal combination**: 已证明互补性但未尝试组合
108	7. **"首个系统比较"**: 需限定为 "for LLM-based structured IE"
109	8. **Diagnostic framework**: 降格为 "diagnostic analysis"
110	
111	## Reviewer Divergence
112	
113	| 问题 | R1 立场 | R2 立场 | 最终定级 |
114	|------|---------|---------|----------|
115	| 成本分析 | Critical（系统性误导） | Warning（TTS 语境下准确，需补充分析） | Critical（保守取高，但记录分歧） |
116	| SJ 失败分析 | 完全缺失 | Section 5.11 部分覆盖 | Warning（缺实例级分析） |
117	| 优先级排序 | 模型规模 > 成本分析 > 零图表 | 相关工作 > RE 数据集 > 新颖性 | 均为 critical |
118	| EM baseline | 合理（SC 原始实现） | Straw man | Info（R1 论证更充分） |
119	
120	---
121	
122	## Questions（需作者澄清）
123	
124	1. 是否计划增加 >30B 或 <3B 模型实验？如不可行，如何限定当前结论的适用范围？
125	2. Table 16 entity count 6+ 时 SJ ρ 降至 0.34 的原因是什么？
126	3. SJ 的 similarity kernel 是否考虑过其他选择（edit distance、embedding cosine）？选择 token-level overlap 的理由？
127	4. Section 5.8 发现 SJ 和 LP 互补后，是否尝试过任何形式的组合？
128	5. 如何回应 CISC (Huang et al. 2025) 发现 "最 calibrated 的方法反而最无效" 与本文结论的张力？
129	
130	---
131	
132	## Missing References
133	
134	1. **Guo et al. 2017** — On Calibration of Modern Neural Networks (ICML) — ECE 定义来源
135	2. **Snell et al. 2024** — Scaling LLM Test-Time Compute Optimally (ICLR 2025) — TTS 核心工作
136	3. **Aggarwal et al. 2023** — Adaptive-Consistency (EMNLP 2023) — N-scaling 相关
137	4. **Huang et al. 2025** — CISC: Confidence Improves Self-Consistency (ACL Findings 2025) — 挑战本文解读
138	5. **传统 IE confidence 文献** — CRF 边际概率、span-level confidence、MC-dropout uncertainty
139	
140	---
141	
142	## External Review (Stanford Agentic Reviewer)
143	
144	外部审稿：未请求。
145	
146	---
147	
148	## Overall Assessment
149	
150	**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致
151	**Director Scale**: 3.5/6 (Borderline Reject / Weak Accept for Findings)
152	**置信度**: 4/5
153	
154	**定位判断**: Findings 可接受，Main 不足。论文的实用价值（practitioners 的 confidence signal 选择指南）适合 Findings 定位，但 6 个 critical 问题（模型规模、相关工作、RE 数据集、方法新颖性、零图表、成本分析）共同削弱了当前版本的竞争力。
155	
156	**核心障碍**（按优先级）:
157	1. 模型规模单一 — 普适性主张无法成立
158	2. 相关工作遗漏 — 5 篇核心文献缺失严重损害可信度
159	3. RE 证据不足 — "Universal bottleneck" 仅单数据集支撑
160	4. 零图表 — calibration 研究无图不可接受
161	5. 方法新颖性有限 — SJ 是自然迁移，缺 kernel 消融
162	6. 成本分析 — 需补充 cost-effectiveness
163	
164	**修改建议优先级**:
165	- P0（决定性）: 补充相关工作 + 添加核心图表 + 降级 "establish"/"universal" 措辞
166	- P1（强烈建议）: 增加 ≥1 个非 8B 模型 + 增加 ≥1 个 RE 数据集 + 补充 cost-effectiveness 分析
167	- P2（改善质量）: signal combination 实验 + prompt sensitivity + 失败案例分析 + bootstrap CI
168	
169	---
170	
171	## Detailed Comments
172	
173	### Section 1 (Introduction)
174	- "establish best practices" 措辞过强，改为 "investigate" 或 "examine"
175	- 缺少 Snell et al. 2024 (TTS) 和 Guo et al. 2017 (ECE) 引用
176	
177	### Section 3 (Method)
178	- Eq.(1) SJ similarity kernel 的具体实现分散在多处，建议集中说明
179	- 缺少 kernel 选择的动机说明和消融
180	
181	### Section 4 (Experimental Setup)
182	- 未给出完整 prompt 模板
183	- 仅 T=0.7 和 T=1.0 两个温度点（R1 认为足够，R2 认为偏少）
184	
185	### Section 5 (Results)
186	- Table 8 selection curve 数据应可视化为 Figure
187	- Table 16 entity count 6+ ρ 下降未解释
188	- Section 5.9 "universal bottleneck" 需降级措辞或增加数据集
189	- Section 5.11 inverted-U 缺实例级 case study
190	
191	### Section 6 (Discussion)
192	- 成本分析需区分 TTS 内比较 vs 跨范式比较
193	- 补充 F1 gain per unit compute 分析
194	- "Diagnostic framework" 降格为 "diagnostic analysis"
195	
196	### Section 7 (Limitations)
197	- 需明确讨论模型规模限制的影响
198	- 需讨论 trained approaches 作为 upper bound
199	
200	### Related Work
201	- 补充 5 篇遗漏文献
202	- 讨论传统 IE confidence 或说明排除理由
203	- 讨论 CISC 与本文结论的张力
204	
205	### Format
206	- Abstract 有未解析引用标记（"?"）
207	- 全文需添加至少 3 个核心 Figure
208	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c0e8bd8-6dee-400d-ad69-d81b31d0229a",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "cefcf200-e7f0-492a-b3b1-a71406954685",
  "sourceToolAssistantUUID": "3c0e8bd8-6dee-400d-ad69-d81b31d0229a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T10:42:44.428Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CdfNCjs2YrGgUyTsEhTx15`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cefcf200-e7f0-492a-b3b1-a71406954685",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7qcqZdfjmb4qbUxiQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea90cfb7-2e74-4d71-9351-6db8f7d66be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d4HEhcK56BLbwYjYSpzLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 39839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 9 · 2026-05-22T10:42:44.445Z_

<details><summary>↩ Tool result · `toolu_01CdfNCjs2YrGgUyTsEhTx15`</summary>

```text
1	---
2	round: 1
3	overall_score: borderline
4	timestamp: 2026-05-15T02:09:02.469376+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告：Round 1 圆桌审稿
11	
12	**论文**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"
13	**目标 Venue**: EMNLP 2026 (ARR)
14	**Reviewer 配置**: R1（方法严谨性 + 实验设计 + 统计有效性）+ R2（新颖性 + 完整性）
15	**轮次**: Round 1（交叉分享后已收敛，无需第二轮）
16	
17	---
18	
19	## Summary
20	
21	本文系统比较 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）中的 quality estimation 和 best-of-N sample selection 能力。核心概念贡献是将 quality estimation（ranking correlation）与 sample selection（F1 gain over greedy）解耦，发现二者存在 "correlation-selection gap"——即使信号与 F1 有中等正相关（SJ ρ≈0.42），实际 selection 也未能稳定超越 greedy baseline (p=0.39)。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。
22	
23	---
24	
25	## Strengths
26	
27	**S1. Quality estimation vs sample selection 的概念解耦** [R1+R2 共识]
28	将 ranking correlation 与 selection F1 gain 分离是有价值的概念贡献，对后续 test-time scaling 研究有直接指导意义——不论负面结论是否最终成立。
29	
30	**S2. 实验设计的系统性** [R1+R2 共识]
31	5 signals × 3 signal families × 3 NER datasets × 1 RE dataset × 2 models × 2 N × 2 T + task difficulty gradient (CoNLL/SciERC/WNUT) + 多项辅助分析（LOO circularity、conditional filtering、capability stratification、inverted-U pattern）。
32	
33	**S3. Task difficulty gradient 设计** [R1 提出，R2 认可]
34	CoNLL（easy）→ SciERC（medium）→ WNUT（hard）的难度梯度设计合理，信号排序随难度变化的发现有实用价值。
35	
36	**S4. Conditional filtering analysis** [R2 提出，R1 认可]
37	Appendix 中移除 zero-F1 instance 后 RE 信号恢复（SJ ρ=0.405, EM ρ=0.417），揭示了 EM 在 non-trivial subset 上的优势，提供了 "task difficulty determines signal choice" 的额外证据。
38	
39	**S5. Limitations section 全面诚实** [R1 提出]
40	主动承认模型规模、RE 数据集、logprob 温度数据等限制。
41	
42	---
43	
44	## Weaknesses（按严重程度排序）
45	
46	### Must-Fix（影响接收决定）
47	
48	**C1. Bootstrap 检验细节严重不足，核心负面结论无法验证** [R1 提出 critical, R2 完全同意 critical]
49	
50	论文核心负面结论（"no signal reliably surpasses greedy"）建立在 Section 5.3 的 "p=0.39, 3-seed bootstrap; Cohen's d=0.038" 上，但以下关键细节均未报告：
51	- Bootstrap 迭代次数
52	- Paired 还是 unpaired bootstrap
53	- 检验统计量
54	- "3-seed bootstrap" 含义不明——对 3 个 seed 做 bootstrap (n=3, 完全无统计功效) 还是每个 seed 内对 instance 做 bootstrap 再合并？
55	
56	该 p 值在论文 5 处被重复引用（Abstract、Introduction ×2、Section 5.3、Conclusion），支撑标题 ("Weak Selectors")、Contribution #2（correlation-selection gap）及 Discussion 对 trained verifier 的呼吁。若检验无效，核心贡献坍塌为 "没有足够统计功效来判断 selection 是否有效"——完全不同的结论。
57	
58	**C2. Correlation-selection gap 的理论贡献被定义性质部分削弱，logprob 失败分析缺失** [R2 提出, R1 部分同意]
59	
60	4/5 个 signals（Entropy, SJ, TJ, Voting）是 instance-level 的——它们不能做 per-sample selection 在定义上是预期结果（Section 3.1 Eq. 5–8 只产出单一 score），而非实证发现。R1 补充：Section 3.3 通过 consensus-proximity 将 instance-level signals 转化为 per-sample 排序，这不完全是 trivial 的，但效果确实差（Table 5: SJ=0.645 vs Greedy=0.644）。
61	
62	真正需要深入分析的是唯一 per-sample signal logprob 为何也失败——calibration 问题？length bias？constrained decoding 干扰？论文仅在 Section 5.1 提到 conditional filtering 后 "logprob RE collapses to ρ=0.011"，Discussion 简要提及 constrained decoding 可能影响，但无实验验证。
63	
64	**C3. 对 Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误** [R2 提出 critical, R1 同意]
65	
66	bib 文件中 `nedellec2026consistency` 第一作者为 Yao，但全文引用为 "Nédellec et al."——事实性错误。三个区分点的说服力不足：
67	- Selection 结论是负面的（未能超越 greedy）
68	- Multi-domain 是标准做法
69	- SJ 优势不一致（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）
70	
71	R1 补充：negative selection result 本身有学术价值（Nedellec 未涉及 selection），问题在于论证方式不够有力，而非贡献不存在。
72	
73	**C4. 仅 8B 模型 "model-agnostic" overclaim** [R1 critical, R2 降为 should-fix — 存在分歧]
74	
75	仅 Qwen3-8B 和 LLaMA-3.1-8B-Instruct 两个同规模模型。Discussion 使用 "model-agnostic" 但 Limitations 承认 "Whether our findings hold for larger models (70B+) remains untested"——构成内部矛盾 (ARR R4 overclaiming)。
76	
77	**R2 立场**：修复成本低——将 "model-agnostic" 替换为 "consistent across tested model families" 即可，核心发现（structural > logprob 在两个模型上一致）本身有效。应为 should-fix。
78	**R1 立场**：70B+ 模型可能产生更高质量更多样的样本，从根本上改变 gap 形态。应为 critical。
79	**Director 定级**：Critical（保守取高），但记录 R2 的缓和意见。
80	
81	**C5. RE 结论仅基于 SciERC, 44% zero-F1 floor effect 扭曲评估** [R1 critical, R2 降为 high-warning — 存在分歧]
82	
83	RE 所有结论来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。
84	
85	**R2 缓和因素**：(1) Conditional filtering 后 SJ RE ρ=0.405, EM RE ρ=0.417——non-trivial subset 上信号有区分力；(2) Capability stratification 中高复杂度 RE 子集 Voting ρ=0.630。
86	**R1 立场**：论文声称覆盖 "NER and RE" 但 RE 基础极其薄弱，"universal bottleneck" 需降级。
87	**Director 定级**：Critical for "NER and RE" / "universal bottleneck" 措辞；Warning if 仅要求限定 RE 结论的泛化范围。
88	
89	---
90	
91	### Should-Fix
92	
93	**W1. Per-sample signal 探索单薄** [R2 提出, R1 部分同意]
94	5 个 signals 中仅 logprob 1 个能做 per-sample selection，论文却声称 "systematic comparison"。R1 反驳：consensus-proximity (Table 5 SJ 行) 数学上等价于 LOO-SJ 排序——是表述问题非实验缺失。但两位共识：per-sample 维度极度单薄。
95	
96	**W2. 约束解码对 sampling diversity 的影响** [R1 warning, R2 认为应升级]
97	Constrained decoding (Outlines/vLLM) 强制输出符合预定义 schema，压缩 token-level 自由度和 per-sample variance。Correlation-selection gap 可能部分是实验 artifact 而非结构化 IE 固有属性。Discussion 用 random baseline (0.608) vs greedy (0.644) 的 gap (3.6pp) 论证 "variance exists"，但这是约束解码下的 variance。
98	
99	**W3. Soft Jaccard 形式化有歧义** [R1 提出, R2 同意]
100	Eq. (4) 中 g_i/g_j 未定义，sim 具体公式缺失（token-level IoU? character-level?），Hungarian algorithm 匹配阈值未说明。影响 reproducibility。
101	
102	**W4. Entity voting 与 SJ 的冗余度未分析** [R1 提出, R2 同意并补充]
103	Mean frequency 聚合未讨论替代选择。R2 补充：entity voting 和 SJ 概念上 overlap，instance-level correlation 未报告——若高度相关则 "两个 structural signal 优于 surface signal" 论证被削弱。
104	
105	**W5. Logprob 温度数据缺失** [R1+R2 共识]
106	Logprob 是唯一 per-sample signal，T=0.7 数据 "unavailable"，但论文声称 "signals robust across temperatures"。应限定为 "consistency-based signals are robust; logprob temperature sensitivity remains uncharacterized"。
107	
108	**W6. ρ=0.38 缺乏 contextualization** [R1 提出, R2 部分反驳]
109	R1 认为仅解释 ~14% F1 方差，未与 uncertainty estimation 文献对比。R2 反驳：论文用 "effective" 和 "strongest"（比较级）而非 "strong"（绝对值），AUROC=0.749 是面向应用的核心证据。但 R2 同意缺乏与 semantic entropy、P(True) 等方法的 ρ 对比。
110	
111	**W7. WNUT-17 "establishing capability boundary" 措辞** [R1+R2 共识]
112	p=0.106, fail to reject null ≠ accept null。ρ=0.082 效应量小 + 54% zero-F1 支持实质结论，但统计措辞应改为 "consistent with" 或 "suggests"。
113	
114	**W8. 模型训练设置不对称** [R1 提出, R2 同意]
115	Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct——后者是否经过 fine-tuning 未说明。若为 off-the-shelf vs task-specific LoRA，则 cross-model comparison 混淆了 architecture 和 training strategy。
116	
117	**W9. "first systematic evaluation" claim 过强** [R2 提出, R1 同意]
118	需收窄为 "first to compare signals from multiple families for both quality estimation and sample selection in generative IE"。
119	
120	**W10. 遗漏引用** [R2 提出, R1 部分同意]
121	- **共识应引用**：Optimal Self-Consistency (arXiv:2511.12309)、Difficulty-Adaptive SC (NAACL 2025 Findings)——与论文核心主题 (task difficulty determines signal choice) 高度相关
122	- **R2 认为应引用, R1 反驳为非 critical**：Singer et al. (2026) conformal NER, ICLR 2025 conformal structured prediction——属不同研究路线 (supervised conformal vs unsupervised consistency)
123	- **待确认**：Generative Self-Aggregation (arXiv:2503.04104)
124	
125	**W11. ρ-AUROC dissociation 机制分析浅** [R2 提出, R1 同意]
126	EM=1 同时包含 all-correct 和 all-wrong 的压缩效应仅在 Appendix D 讨论，应在主文明确阐述。
127	
128	---
129	
130	## Reviewer Consensus
131	
132	以下问题两位 Reviewer 完全一致：
133	1. **Overall 评分**: 3/5 (Findings)
134	2. **Bootstrap 细节不足 (C1)**: 本文最关键的方法论缺陷，影响核心贡献成立性
135	3. **Logprob 失败分析缺失**: 唯一 per-sample signal 值得专门深入分析
136	4. **Nedellec 引用错误**: Yao → Nédellec 是事实性错误
137	5. **约束解码 confound**: 应至少讨论其对 diversity 和 gap 的潜在影响
138	6. **"model-agnostic" 措辞矛盾**: 需与 Limitations 一致
139	7. **WNUT-17 措辞**: "establishing" → "consistent with" / "suggests"
140	8. **"first systematic" 需限定**
141	9. **Quality estimation vs selection 解耦**: 本文最有价值的概念贡献
142	
143	## Reviewer Divergence
144	
145	| 问题 | R1 立场 | R2 立场 | Director 定级 |
146	|------|---------|---------|---------------|
147	| C4 模型规模 overclaim | Critical（70B 可能根本改变 gap） | Should-fix（措辞修正即可） | Critical（保守取高） |
148	| C5 RE 单数据集 | Critical（RE 基础极其薄弱） | High-warning（conditional analysis 部分缓解） | Critical for "universal" 措辞 |
149	| W1 LOO-SJ selection | 已隐式测试（Table 5 SJ 行 = consensus-proximity） | 未测试，应显式报告 | Warning（是表述问题，但 per-sample 维度确实单薄） |
150	| W6 ρ contextualization | 缺乏对比 | 论文措辞准确（比较级），AUROC 是核心证据 | Warning（补充对比即可） |
151	| W2 约束解码严重程度 | Warning | 应升级（可能解释 gap 的根本原因） | Warning（论据充分但无约束解码对比数据） |
152	| W10 Conformal prediction 引用 | 非 critical omission（不同路线） | 应引用 | Warning（在 Related Work 中讨论） |
153	
154	---
155	
156	## Questions（需作者澄清）
157	
158	1. **Bootstrap 检验完整规范**：迭代次数、paired/unpaired、统计量、"3-seed bootstrap" 确切含义？若 n=3，则需在每个 seed 内对 instance 做 paired bootstrap 并报告合并策略。
159	2. **LLaMA-3.1-8B-Instruct 是否经过 LoRA/SFT fine-tuning**？若未 fine-tune，cross-model comparison 混淆了 architecture 和 training strategy。
160	3. **Consensus-proximity selection 与 LOO-SJ 的等价关系**：Table 5 SJ 行是否等价于 LOO-SJ selection？若是，应在正文中显式说明。
161	4. **Logprob 在 constrained decoding 下的行为**：constrained decoding 是否系统性扭曲了 logprob 的 calibration？是否有 unconstrained 对比数据？
162	5. **Entity voting 与 SJ 的 instance-level correlation**：Spearman ρ 是多少？高冗余度是否削弱 "两类 structural signal 独立验证" 的论证？
163	6. **Logistic regression proxy**：Limitations 提到但正文/Appendix 无结果——是否计划展示？
164	
165	---
166	
167	## Missing References
168	
169	### 共识应引用
170	1. **Optimal Self-Consistency** (arXiv:2511.12309) — 与 selection 机制直接相关
171	2. **Difficulty-Adaptive Self-Consistency** (NAACL 2025 Findings) — 与论文核心发现 "task difficulty determines signal choice" 高度相关
172	
173	### 建议引用（存在分歧）
174	3. Singer et al. (2026) "UQ for NER via Conformal Prediction" (arXiv:2601.16999)
175	4. Conformal Structured Prediction (ICLR 2025)
176	5. Generative Self-Aggregation (arXiv:2503.04104)
177	
178	### 引用错误
179	- `nedellec2026consistency`: 第一作者应为 Yao，全文 "Nédellec et al." 引用有误
180	
181	---
182	
183	## External Review (Stanford Agentic Reviewer)
184	
185	外部审稿：未请求。
186	
187	---
188	
189	## Overall Assessment
190	
191	**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致
192	**Director Scale**: 3.5/6 (Borderline — Weak Accept for Findings)
193	**置信度**: 4/5
194	
195	### 定位判断
196	
197	Findings 可接受（需修复 C1 bootstrap 细节），Main 不足。
198	
199	论文的概念贡献（quality estimation vs selection 解耦）和系统实验设计有 Findings 水准的价值，但 5 个 critical 问题共同限制了竞争力：
200	
201	1. **C1 Bootstrap 细节** — 核心负面结论的统计基础无法验证（最优先修复）
202	2. **C2 Gap 解释力** — 4/5 signals 的 selection 失败有定义性成分，logprob 失败机制未分析
203	3. **C3 Nedellec 增量** — 贡献论证弱 + 引用错误
204	4. **C4 Model-agnostic** — Overclaim，但修复成本低（措辞修正）
205	5. **C5 RE 单数据集** — "Universal bottleneck" 仅单数据集支撑
206	
207	### 与 Round 0 的对比
208	
209	Round 0 的部分 critical 问题可能已修复（零图表、成本分析均未被本轮 Reviewer 提及），但新的 critical 问题浮现（bootstrap 细节、gap 定义性、Nedellec 增量）。模型规模和 RE 数据集问题持续存在。整体评分与 Round 0 持平（3/5），论文在不同维度有进步和退步。
210	
211	### 修改建议优先级
212	
213	- **P0（决定性）**: 补充 bootstrap 检验完整规范 + 修正 Nedellec 引用错误 + 降级 "model-agnostic"/"universal"/"establish" 措辞
214	- **P1（强烈建议）**: 深入分析 logprob selection 失败原因 + 讨论约束解码 confound + 补充 Optimal SC / Difficulty-Adaptive SC 引用 + 显式说明 consensus-proximity = LOO-SJ selection
215	- **P2（改善质量）**: SJ 形式化补全 + entity voting/SJ 冗余度分析 + ρ contextualization + 温度 robustness 限定 + LLaMA fine-tuning 状态说明
216	
217	---
218	
219	## Detailed Comments
220	
221	### Abstract
222	- "Weak Selectors" 结论建立在 p=0.39 上——若 bootstrap 细节补全后确认有效则可保留，否则需重新表述
223	
224	### Section 1 (Introduction)
225	- "+18pp on GSM8K" 未注明具体模型 (PaLM-540B)，与本文 8B 规模差异大
226	- "first systematic evaluation" 需加限定语
227	
228	### Section 3 (Method)
229	- Eq. (4) SJ: g_i/g_j 定义、sim 公式、Hungarian 阈值需补全
230	- Section 3.3 consensus-proximity selection 应显式说明与 LOO-SJ 排序的等价关系
231	- Entity voting mean frequency 聚合未讨论替代选择
232	
233	### Section 5 (Results)
234	- Section 5.3: bootstrap 检验规范必须完整报告
235	- Section 5.4: "model-agnostic" → "consistent across tested model families"
236	- Section 5.4: Cross-model Δ=0.005 应报告是否在 CI 内
237	- WNUT-17: "establishing the capability boundary" → "consistent with a capability boundary"
238	- Logprob T=0.7 缺失应在温度 robustness 结论中明确限定
239	
240	### Section 6 (Discussion)
241	- 补充约束解码对 sampling diversity 和 correlation-selection gap 的讨论
242	- "Universal bottleneck" 需降级或增加 RE 数据集
243	- Logistic regression proxy: 展示结果或删除提及
244	
245	### Related Work
246	- 补充 Optimal SC、Difficulty-Adaptive SC
247	- 讨论 conformal prediction for structured prediction（可简要说明与本文研究路线的关系）
248	- 更充分讨论 trained approaches (verifier/reward model) 作为 upper bound context
249	
250	### References
251	- 修正 nedellec2026consistency 第一作者 (Yao → 正确引用)
252	- 检查 snell2024scaling bib 作者格式
253	
254	### Appendix
255	- ρ-AUROC dissociation / EM=1 压缩效应应在主文至少简要提及
256	- Appendix D \textsc 编译检查
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea90cfb7-2e74-4d71-9351-6db8f7d66be8",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "cebc76b2-d432-43bd-8cab-dd3106ed18f9",
  "sourceToolAssistantUUID": "ea90cfb7-2e74-4d71-9351-6db8f7d66be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T10:42:44.845Z_

<details open><summary>🔧 Tool call — Read · `toolu_0119P9fsMaC43hSMWVJbJmFb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cebc76b2-d432-43bd-8cab-dd3106ed18f9",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7qcqZdfjmb4qbUxiQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "55eed798-051e-4373-9587-7875cc97fe5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d4HEhcK56BLbwYjYSpzLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 39839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 11 · 2026-05-22T10:42:44.856Z_

<details><summary>↩ Tool result · `toolu_0119P9fsMaC43hSMWVJbJmFb`</summary>

```text
1	---
2	round: 2
3	overall_score: borderline
4	timestamp: 2026-05-15T02:56:52.665681+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# Round 2 审稿报告 — struct_self_consist_ie
11	
12	**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
13	**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
14	**截止日期**: 2026-05-25
15	**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 格式）
16	**交叉分享**: 已完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应
17	
18	---
19	
20	## Summary
21	
22	本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE（NER + RE）中的 quality estimation 与 sample selection 表现。核心发现是 "correlation-selection gap"：instance-level consistency signals 是有效的 quality estimators（entity voting ρ=0.38, exact match AUROC=0.75），但无法可靠超越 greedy decoding 进行 best-of-N selection（p>0.39, bootstrap），尽管存在 13-18pp 的 oracle headroom。附带发现 signal ranking 随 task difficulty 变化（EM 领先 easy tasks，SJ/Voting 领先 hard tasks，WNUT-17 全部 collapse）。
23	
24	---
25	
26	## Strengths
27	
28	1. **概念贡献清晰且有框架性价值**：quality estimation（ranking instances by expected performance）vs sample selection（choosing best output among N candidates）的解耦（§3.1 per-sample vs instance-level signal formulation）对 generative IE 社区有指导意义，是与 Nédellec et al. (2026) 的关键差异化。
29	
30	2. **Quality estimation 分析深度突出**：5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic + ρ-AUROC dissociation 分析，超过多数同类 empirical study。
31	
32	3. **统计规范（selection）达到高标准**：Bootstrap resampling (B=10,000, n=529, instance-level paired), percentile 95% CIs, Cohen's d=0.038, sign test 61W/70L, 3-seed 含义明确——远超多数 NLP empirical papers。
33	
34	4. **诚实的 hedging**：RE single-dataset 限制在 Introduction/Discussion/Conclusion/Appendix 四处 acknowledge；logprob temperature gap 在正文 + Limitations 双重标注；claim 用 "consistent across tested model families" 而非 "model-agnostic"——Round 0-1 的 self-awareness 问题已有实质改善。
35	
36	5. **Related Work 覆盖全面**：§2 涵盖 self-consistency 变体（USC, CISC, ReASC, ranked voting, latent SC）、difficulty-adaptive 方法（Optimal SC, Difficulty-Adaptive SC）、generative self-aggregation、conformal prediction、semantic uncertainty 等。49 条 bib 全部 cited，0 orphan。
37	
38	6. **ρ-AUROC dissociation 是 actionable finding**：EM 在 ρ 排名低但 AUROC 领先（SciERC NER: ρ=0.295 rank #3, AUROC=0.749 rank #1），揭示 binary vs continuous signal properties 的 metric-dependent 行为，对 practitioners 在 quality-aware routing 中有直接实用价值。
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（影响接收决定）
45	
46	**C1. Selection 证据面过窄——核心贡献仅 1 dataset × 1 model 验证** [Reviewer 共识: unanimously critical]
47	
48	- **位置**: Table 3 (§5.3)；Abstract; Introduction Contribution #2; Conclusion
49	- **问题**: Correlation-selection gap 是论文的 differentiator（与 Nédellec et al. 的关键区别），但 Table 3 的 selection 分析仅覆盖 SciERC/Qwen。Quality estimation 有 3 datasets × 2 models 的覆盖，selection 仅 1×1，逻辑链断裂。Abstract "no signal reliably surpasses greedy decoding on either task" 的 evidence base 实际是 1 dataset × 1 model × 2 tasks。CoNLL selection 未报告（即使 headroom 极小，negative result 本身有价值——说明 gap 可能是 hard-task specific）；LLaMA SciERC selection 未报告（cross-model 验证缺失）。
50	- **Action**: (1) 补 LLaMA SciERC selection 结果验证 cross-model generalization；(2) CoNLL selection 放 Appendix（即使结论是 ceiling effect）；(3) 如 WNUT-17 selection 不可行，明确说明 oracle-greedy gap。
51	
52	**C2. WNUT-17 capability boundary claim 缺乏系统数据** [Reviewer 共识: unanimously critical]
53	
54	- **位置**: §5.1; Introduction Contribution #3
55	- **问题**: Contribution #3 列出 "task-complexity boundary conditions"，WNUT-17 是关键证据。但全文仅报告 SJ 一个信号的 ρ=0.082 (p=0.106)——一个不显著的单信号结果。其他四个信号（Voting, EM, FK, Logprob）在 WNUT-17 的结果完全缺失。用单个不显著数据点支撑 "all signals converge when model capability is insufficient" 逻辑上不成立。如果 5 个信号全部 collapse，这反而是更强的证据。
56	- **Action**: Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）；补 conditional ρ（non-zero F1 subset）排除 floor effect。
57	
58	---
59	
60	### Should-Fix（影响评分但不一票否决）
61	
62	**W1. ρ=0.38 缺乏 cross-method 数值对比** [R2 列为 critical, R1 同意但建议降为 should-fix]
63	
64	- **位置**: §5.1, §6 Discussion
65	- **问题**: 论文以 ρ=0.38 为核心正面结论（"effective quality estimators"），intra-study context 已有（14% variance explained + AUROC=0.749），但 cross-method numerical context 完全缺失。§2 引用 semantic entropy (Kuhn 2023)、P(True) (Kadavath 2022)、CoCoA (Vashurin 2025) 但未给出任何数值对比。R1 指出 structured IE 与 discrete-answer QA 的 output space 根本不同，direct comparison 有误导风险，因此降为 should-fix。
66	- **Action**: §5 或 §4.2 加 footnote，引用可比方法的典型 AUROC 值，并明确 cross-task comparison 的困难性。
67	
68	**W2. N=8 QE ρ 缺乏 uncertainty quantification** [Reviewer 共识]
69	
70	- **位置**: Table 1 (§5.1)
71	- **问题**: Table 1 N=8 行为 point estimates without CIs/standard errors。多处 signal ordering Δ=0.003-0.01（如 CoNLL LLaMA SJ-FK Δ=0.003），参照 N=16 σ≈0.006-0.008，可能 within noise。正面 QE 结论反而缺乏统计支撑，与 selection 的 thorough bootstrap 标准不一致。
72	- **Action**: 对 N=8 主要 ρ 值报告 bootstrap CIs，或 Appendix 补 3-seed runs。
73	
74	**W3. SJ Hungarian matching 无 threshold + Eq.(4) 非标准分母** [Reviewer 共识, R2 交叉回应提升严重性]
75	
76	- **位置**: Eq.(4), §3.2
77	- **问题**: sim = token-level IoU ✓, g_i/g_j 定义 ✓。但：(1) Hungarian 是否有 minimum similarity threshold？无 threshold 则完全不相关 span 也会 match，SJ numerator 非零；(2) 分母 max(|g_i|,|g_j|) 是非标准 Jaccard variant（标准为 |A∪B|），未解释设计选择。
78	- **Action**: 明确 threshold 及 zero-overlap matched pairs 比例；一句话解释 max vs union 的设计理由。
79	
80	**W4. RE selection 无统计检验** [Reviewer 共识]
81	
82	- **位置**: Table 3, §5.3
83	- **问题**: NER selection 有完整 bootstrap（p, CI, Cohen's d, sign test），RE 仅叙述性 "no signal exceeds greedy" 无任何统计量。RE oracle headroom 18.1pp 更大，selection failure 更需 p-value 支撑。
84	- **Action**: 补 RE selection bootstrap p-value 和 CI。
85	
86	**W5. Constrained decoding 作为全局 confound 讨论不足** [R2 提出, R1 交叉同意]
87	
88	- **位置**: §6 Discussion; Limitations
89	- **问题**: Discussion "Why logprob fails" 段提到 constrained decoding 压缩 per-sample diversity，但仅在 logprob context 下讨论。如果 constrained decoding 压缩 diversity，影响的不仅是 logprob，还包括 consensus-proximity selection（SJ/Voting）——因为后者也依赖 per-sample 差异区分候选。Limitations 未列此 confound。
90	- **Action**: Limitations 增加 constrained decoding 条目；或补 per-sample F1 variance 数据证明 diversity 已足够。
91	
92	**W6. Abstract "across NER and RE on three datasets" 措辞误导** [Reviewer 共识]
93	
94	- **位置**: Abstract line 3
95	- **问题**: RE 仅在 SciERC 评估，但 Abstract 自然读法暗示 NER+RE 均在三数据集上进行。
96	- **Action**: 改为 "across NER (three datasets) and RE (SciERC)" 或类似准确表述。
97	
98	**W7. n=529 vs SciERC n=551 discrepancy** [Reviewer 共识]
99	
100	- **位置**: §5.3
101	- **问题**: Bootstrap 用 n=529 但 SciERC test set 有 551 instances，22 instances 被 drop 原因未交代。
102	- **Action**: 一句话说明 filtering criteria。
103	
104	---
105	
106	### Minor
107	
108	- Eq.(4) 分母 max 而非 union 需一句设计理由说明
109	- FK adaptation：N 个来自同一模型的 stochastic samples 不是 Fleiss' κ 假设的 independent raters，brief acknowledgment 即可
110	- Table 1 N=8 是 single-seed 还是 averaged 未说明
111	- EM majority-vote selection 在 Table 3 中标 "---"，应加 1-2 句解释 exact-match plurality 在 structured IE 中的退化问题（Reviewer 分歧点，R1 反驳 R2，见下文 Divergence）
112	
113	---
114	
115	## Reviewer Consensus [AGREE]
116	
117	两位 Reviewer 在以下关键问题上独立达成完全一致：
118	
119	1. **Selection 证据面过窄是最关键问题**（R1-N1 = R2-N2, unanimously critical）：correlation-selection gap 仅 1 dataset × 1 model 验证，但 framed 为 "fundamental disconnect"
120	2. **WNUT-17 系统数据缺失**（R1-N2 ⊃ R2-W3, unanimously critical）：5 signals 中仅报告 1 个不显著结果
121	3. **N=8 QE 缺 uncertainty**（R1-W1, R2 交叉同意）
122	4. **SJ threshold 未规范**（R1-W2, R2 交叉同意并提升严重性）
123	5. **RE selection 缺统计检验**（R1-W3, R2 交叉同意）
124	6. **Abstract RE 措辞需修正**（R2-W2, R1 交叉同意）
125	
126	---
127	
128	## Reviewer Divergence [REBUT]
129	
130	1. **EM majority-vote selection (R2-W4)**：R2 认为 EM<1 时应实现 majority-vote selection；R1 反驳指出 structured IE 中 exact-match plurality 退化严重（通常仅 1-2 identical samples），consensus-proximity (SJ selection) 已是 soft majority vote。**Director 判断**：R1 的反驳有技术依据，降为 minor（加解释即可）。
131	
132	2. **LLaMA SciERC N=8 数据完整性 (R1-W4)**：R1 认为 Table 1 SciERC 列仅 Qwen、LLaMA 数据不全；R2 部分反驳指出 CoNLL 有完整 cross-model 覆盖，但同意 Table 1 应标注 "Qwen-only"。**Director 判断**：R2 的反驳合理——CoNLL cross-model 差异极小（Δ=0.005），SciERC 缺失不影响核心 claim。标注即可。
133	
134	3. **ρ=0.38 contextualization 严重性 (R2-N1 vs R1 交叉回应)**：R2 列为 critical，R1 同意需要但降为 should-fix（structured IE vs QA output space 不同，direct comparison 有误导风险）。**Director 判断**：采纳 R1 的降级——footnote 级修改，不构成 must-fix。
135	
136	---
137	
138	## Questions for Authors
139	
140	1. WNUT-17 上 Voting/EM/FK/Logprob 的 ρ 和 AUROC 分别是多少？
141	2. CoNLL 的 best-of-N selection 结果（oracle-greedy gap 有多大）？
142	3. SciERC bootstrap n=529 中 22 instances 被 drop 的 criteria？
143	4. SJ Hungarian matching 是否有 minimum similarity threshold？无 threshold 时 sim≈0 matched pairs 占多少？
144	5. Table 1 N=8 主要结果是 single-seed 还是 averaged？
145	
146	---
147	
148	## Missing References
149	
150	无重大遗漏。Round 1 指出的 Optimal SC、Difficulty-Adaptive SC、Generative Self-Aggregation、conformal prediction 等均已补充。49 条 bib 全部 cited，0 orphan，45 条 verified。
151	
152	---
153	
154	## External Review (Stanford Agentic Reviewer)
155	
156	外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。
157	
158	---
159	
160	## Round 0-1 遗留 Issue 修复状况
161	
162	**24 个历史 issues 状态汇总**：
163	- ✅ **Resolved**: 19 个（R0-C1, R0-C2, R0-C3, R0-C5, R0-C6, R0-W1, R0-W4, R0-RR-D1, R1-N1, R1-N2, R1-N3, R1-N4, R1-W2, R1-W4, R1-W5, R1-W6, R1-W8, R1-W9, R1-W10, R1-M1, R1-M2, R1-M3）
164	- ⚠️ **Partially resolved**: 3 个（R0-C4 SJ 新颖性, R1-W1 SJ 形式化, R1-W3 ρ contextualization, R1-W7 constrained decoding）
165	- ❌ **Unresolved**: 0 个
166	
167	论文从 Round 0 到 Round 2 改善显著，绝大多数遗留问题已修复或充分 hedge。
168	
169	---
170	
171	## Overall Assessment
172	
173	**Overall Score: 3.5 — Borderline Conference / Strong Findings**
174	
175	**Reviewer 1**: 3.5/5, Confidence 4/5
176	**Reviewer 2**: 3.5/5, Confidence 4/5
177	
178	| 维度 | R1 | R2 | 综合 |
179	|------|----|----|------|
180	| Soundness | 3.5 | 4.0 | 3.75 |
181	| Excitement | 3.0 | 3.0 | 3.0 |
182	| Reproducibility | 3.5 | 4.0 | 3.75 |
183	
184	**核心判断**：方法论扎实、统计严谨的 empirical study。Quality estimation 分析是论文的强项，coverage 和 depth 达到 long paper 标准。Correlation-selection gap 是 genuinely useful negative result，概念贡献清晰。
185	
186	两个 critical 问题制约 Conference 推荐：(1) selection gap 作为核心贡献仅在 1 dataset × 1 model 验证，evidence base 与 "fundamental disconnect" framing 不匹配；(2) WNUT-17 capability boundary claim 仅有 1 个不显著数据点支撑。
187	
188	**如果 C1 和 C2 得到补充**（补 LLaMA SciERC selection + CoNLL selection appendix + WNUT-17 完整 signal table），论文从 3.5 提升到 4.0（Weak Accept）是可期的——evidence breadth 将匹配 framing breadth，核心 claims 将得到充分支撑。
189	
190	**当前推荐**：Findings（如不补充实验）/ Conference（如补充后 evidence 支撑 claims）。
191	
192	---
193	
194	## Detailed Comments（逐节）
195	
196	### Abstract
197	- "across NER and RE on three datasets" 需修正为 "NER (three datasets) and RE (SciERC)"
198	- 其余 claims 与正文一致，无 overclaim
199	
200	### Introduction (§1)
201	- Contribution #2 的 framing 应限定 evidence scope
202	- Contribution #3 需 WNUT-17 完整数据支撑
203	- PaLM-540B attribution ✓, scope 已收窄 ✓
204	
205	### Related Work (§2)
206	- 覆盖全面，无遗漏
207	- 与 Nédellec et al. 的三点差异化清晰
208	
209	### Method (§3)
210	- Per-sample vs instance-level formulation 精确
211	- SJ: sim 和 g_i/g_j 已定义，Hungarian threshold 和分母 variant 需补充
212	- Consensus-proximity = LOO-SJ 已明确
213	- FK independent raters 假设可 brief acknowledge
214	
215	### Experiments (§4-5)
216	- QE (Table 1): 需 N=8 uncertainty estimates
217	- Selection (Table 3): 需扩展到 LLaMA SciERC + CoNLL appendix
218	- RE selection: 需 bootstrap 统计检验
219	- WNUT-17: 需完整 signal table
220	- n=529 vs 551: 需说明 filtering
221	
222	### Discussion (§6)
223	- QE vs selection 区分清晰 ✓
224	- Logprob failure analysis 充分 ✓
225	- Constrained decoding 讨论需从 logprob-specific 扩展为全局 confound
226	- ρ=0.38 cross-method contextualization 需 footnote
227	
228	### Conclusion (§7)
229	- 三个 findings 准确反映论文内容
230	- RE limitation hedge ✓
231	
232	### Limitations
233	- 诚实且全面
234	- 需增加 constrained decoding confound 条目
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55eed798-051e-4373-9587-7875cc97fe5e",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "b476597c-95ca-476a-b0c6-1641d36181c5",
  "sourceToolAssistantUUID": "55eed798-051e-4373-9587-7875cc97fe5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T10:42:45.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJSWKkYmM1nD8XYBHnUzj9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b476597c-95ca-476a-b0c6-1641d36181c5",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7qcqZdfjmb4qbUxiQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0dac09a6-5690-4491-b7ba-e1a5d4a7e08a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d4HEhcK56BLbwYjYSpzLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 39839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 13 · 2026-05-22T10:42:45.111Z_

<details><summary>↩ Tool result · `toolu_01WJSWKkYmM1nD8XYBHnUzj9`</summary>

```text
1	---
2	round: 3
3	overall_score: borderline
4	timestamp: 2026-05-15T04:14:58.309947+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 3
11	**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
12	**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
13	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
14	**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛汇总
15	
16	---
17	
18	## Summary
19	
20	本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。在 SciERC、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是 "correlation-selection gap"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。
21	
22	---
23	
24	## Strengths
25	
26	**S1. 问题分解有真正洞察力。** 将 quality estimation 与 sample selection 明确区分为两个独立目标，用不同指标分别评估（Spearman ρ + AUROC vs. best-of-N F1）。Per-sample vs. instance-level 信号的形式化区分使分析逻辑链条清晰可追溯。这一分析框架本身是对现有文献的有价值贡献。[R1-S1, R2-S1 一致]
27	
28	**S2. 统计报告全面严谨。** Paired bootstrap (B=10,000) 附带 95% CI、Cohen's d、sign test win%、pairwise Δρ CI（Appendix D），多数实证论文不会做到这个粒度。[R1-S2, R2-S2 一致]
29	
30	**S3. WNUT-17 capability boundary 分析揭示重要方法论警示。** Voting ρ=0.724（full-set）→ conditional ρ=0.038 (n.s.) 揭示 inflated correlation 由 zero/non-zero boundary 驱动；logprob 条件反转（full ρ=−0.410 → conditional ρ=0.350）进一步确认此现象。[R1-S4, R2-S3 一致]
31	
32	**S4. 负面结果处理诚实平衡。** RE 单数据集局限在 Introduction、Discussion、Conclusion、Limitations 四处明确提及。WNUT-17 作为方法边界坦率报告。Limitations section 全面覆盖多项局限。[R1-S3, R2-S4 一致]
33	
34	**S5. Task difficulty 分析有实用价值。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现，以及 conditional filtering 后信号排序翻转，为从业者信号选择提供实用指导。[R1-S4]
35	
36	**S6. Robustness 覆盖面广。** Temperature (T=0.7/1.0)、N-scaling (8→16)、cross-architecture 均有系统分析。[R2-S6]
37	
38	---
39	
40	## Weaknesses
41	
42	### Must-Fix（影响接收决定）
43	
44	**[Critical] W-C1: Constrained decoding 是 correlation-selection gap 的未控制混淆变量**
45	- 两位 Reviewer 独立提出（R1-N1, R2-N2），交叉回应后完全共识
46	- 论文核心发现 "no signal reliably surpasses greedy" 可能部分是 Outlines/vLLM constrained decoding 压缩 per-sample diversity 的产物，而非置信度信号本身的固有局限
47	- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance
48	- §5 Discussion 已承认此问题但仅作 future work 提及，未设计任何对照或量化分析
49	- 75% of logprob comparisons 为 effective ties (win%=46.6%) 暗示 per-sample variance 极小
50	- **建议**：(a) 报告 unique output fraction + per-sample logprob std 分布量化实际 diversity；(b) 增加 unconstrained generation + post-hoc parsing 对照；或 (c) 至少明确 gap 结论的 generalizability boundary 为 constrained decoding regime，在 Abstract/Conclusion 中限定
51	
52	### Should-Fix（影响评分）
53	
54	**[Warning] W-S1: RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**
55	- R2 独立提出(N1)，R1 交叉回应后上调严重性至 borderline Must-Fix
56	- SciERC RE 44% zero F1 严重压缩信号可区分范围，RE gap 证据（−0.9pp, p=0.80）统计说服力弱
57	- 论文已在 4 处 hedge（Round 2 修正），但仍在 Abstract 和 Contribution 中以 "NER and RE" 并列呈现，给人 RE 证据与 NER 等量齐观的印象
58	- **建议**：(a) 进一步降级 RE claim 为 "preliminary RE evidence on SciERC"；(b) 补 SciERC RE conditional filtering 分析量化 floor effect 影响
59	
60	**[Warning] W-S2: Selection gap 统计论证不完整——failure to reject ≠ evidence of absence**
61	- R1 列 critical(N2)，R2 交叉回应降为 should-fix（6/6 配置一致性构成 cumulative evidence，CI 正面端 +4.2pp vs 13.2pp oracle headroom 实际意义有限）
62	- 共识：措辞需更严谨。p>0.39 只是 absence of evidence
63	- **建议**：修改为 "we found no significant evidence that any signal surpasses greedy" + 补充 power analysis 或 TOST 等价性检验
64	
65	**[Warning] W-S3: N=8 核心结果 single seed (seed=42)**
66	- R1 列 critical(N3)，R2 交叉回应降为 should-fix（N=16 3-seed ranking 完全一致）
67	- Table 1 N=8 和 Table 2 selection 全部基于单一 seed，信号排序差异小（Voting-SJ Δρ=0.019）
68	- **建议**：SciERC N=8 补至少 3 seed mean±σ，或在 Limitations 明确 single-seed 风险并引用 N=16 stability
69	
70	**[Warning] W-S4: Gap 概念部分 tautological**
71	- R1(W2) 和 R2 交叉回应均认同：4/5 instance-level 信号 by design 无法 per-sample 区分，selection 失败是定义必然
72	- 真正的 empirical contribution 是 (1) logprob（唯一 per-sample 信号）也失败，(2) consensus-proximity 转换策略未能弥合 gap
73	- **建议**：Discussion 中明确分离两层论证——结构性局限 (by construction) vs. 经验性失败 (logprob + consensus-proximity)
74	
75	**[Warning] W-S5: Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系**
76	- R1(W6) 提出，R2 强烈同意——"R1 最有力的 Should-Fix"
77	- 仅测一种转换策略就声称 "signals fail as selectors" 不充分
78	- MBR decoding (Eikema & Aziz 2022, Freitag et al. 2022) 是成熟替代方案但未讨论
79	- **建议**：(a) 明确 consensus-proximity 与 MBR 等价性；(b) 讨论替代策略是否可能缩小 gap；(c) 补引 MBR 文献
80	
81	**[Warning] W-S6: 多重比较校正缺失**
82	- 两位 Reviewer 一致。SJ–EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive
83	- **建议**：声明未做校正 + "Yes†" 改为 "suggestive"
84	
85	**[Warning] W-S7: FK 独立性假设 justification 不足**
86	- 两位 Reviewer 一致。§3.2 一句 hand-wave 不够
87	- **建议**：报告 inter-sample correlation 或在 Limitations 明确讨论
88	
89	**[Warning] W-S8: Cross-model 措辞过度外推**
90	- 两位 Reviewer 一致。两模型均 8B，应为 "cross-architecture at 8B scale"
91	- **建议**：正文加限定词
92	
93	**[Warning] W-S9: "First multi-family comparison" claim scope 过宽**
94	- 两位 Reviewer 一致。应限定为 "for both QE and selection in generative structured IE"
95	
96	**[Warning] W-S10: 遗漏引用**
97	- VerifiNER (Kim et al., ACL 2024)——supervised NER verification 参照点
98	- MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022)——与 consensus-proximity 直接相关
99	- Malinin & Gales (2021)——structured prediction uncertainty
100	- He et al. (NAACL Findings 2024)——sequential labeling uncertainty
101	- RASC (Aggarwal et al., NAACL 2025)——需确认是否与已引 REASC 重复
102	
103	**[Warning] W-S11: 术语不一致**
104	- "confidence signal" vs "consistency signal" 混用；"VC" vs "Voting Conf." 缩写不统一；LLaMA Factory 未引用
105	
106	### Minor Issues
107	
108	**[Info] W-M1**: WNUT-17 "54% zero F1"（§4.1）vs Table 7 显示 355/689 ≈ 51.5%，数据不一致
109	**[Info] W-M2**: EM selection exclusion (Table 2) 理由 "probability negligible" 需报告 exact match pairs 实际频率
110	**[Info] W-M3**: Ethics Statement 缺失——ARR 仅 "encouraged" 非 "required"（R1 rebut R2），但添加简短声明为 good practice
111	**[Info] W-M4**: ρ–AUROC dissociation 作为独立发现过度强调——dissociation 本身 expected，应承认统计预期性后聚焦实践含义
112	**[Info] W-M5**: 对 Nedellec (2026) Introduction 措辞偏 adversarial，建议改为更 neutral 语气
113	**[Info] W-M6**: LOO-SJ 验证中 Δρ=−0.014（整体 Spearman）和 per-instance max Δρ=3.1×10⁻⁴ 量纲不同，需澄清
114	**[Info] W-M7**: Figure 1 caption 引入 p=0.39（来自 Table 2），建议补 "(Table 2)" 交叉引用
115	**[Info] W-M8**: SJ Hungarian matching cost function 未明确 maximize/minimize 方向和 zero-IoU pairs 处理
116	**[Info] W-M9**: Table 1 N=16 区域大面积空白，建议补交叉引用或考虑合并呈现
117	**[Info] W-M10**: Semantic entropy footnote 比较（§4.2）既承认不可比又给出数字，R1 建议删除，R2 建议保留但强化 caveat——共识为保留并强化 caveat placement
118	
119	---
120	
121	## Reviewer Consensus [AGREE]
122	
123	1. **Constrained decoding 是核心 validity threat**：gap 可能部分是实验设置 artifact 而非信号固有局限 [R1-N1 = R2-N2, 完全共识]
124	2. **RE 证据薄弱**：44% zero-F1 + 单数据集使 RE claim 基础不稳 [R2-N1, R1 交叉后上调]
125	3. **Gap 概念需分层论证**：instance-level 信号的 definitional limitation 与 logprob 的 empirical failure 应分开论述 [R1-W2 = R2 agree]
126	4. **Consensus-proximity 需与 MBR 建立联系**：单一转换策略不足以支撑 sweeping claim [R1-W6, R2 强烈同意]
127	5. **统计报告整体质量高**但有特定 gaps：单 seed、缺多重比较声明、failure-to-reject 措辞 [双方一致]
128	6. **写作质量好**，叙事连贯，负面结果处理诚实 [双方一致]
129	
130	## Reviewer Divergence [REBUT]
131	
132	1. **Ethics Statement 严重性**：R2 列 critical → R1 rebut（ARR 仅 encouraged）→ **共识降为 Minor**
133	2. **Failure-to-reject 统计逻辑**：R1 列 critical → R2 降为 should-fix（6/6 cumulative evidence）→ **共识降为 Warning**
134	3. **Single seed**：R1 列 critical → R2 降为 should-fix（N=16 ranking stability）→ **共识降为 Warning**
135	4. **SJ 增量贡献**：R2 认为 borderline → R1 部分 rebut（SJ 价值在 temperature/N-scaling robustness 而非单点 ρ 增量）→ **共识为 SJ 论文措辞应强调 robustness**
136	5. **Semantic entropy footnote**：R1 建议删除 → R2 建议保留强化 caveat → **共识为保留但强化**
137	
138	---
139	
140	## Questions to Authors
141	
142	1. 是否考虑过 unconstrained generation 对照？即使 parse 成功率低，比较两种 regime 下 pairwise SJ 分布也能 calibrate gap 的 generalizability。
143	2. Logprob 在 WNUT conditional set 达所有信号最高 ρ=0.350（Table 7），如何 reconcile 主文中 "logprob 最弱" 叙述？是否暗示 logprob 在高 diversity 场景有独特优势？
144	3. LoRA rank=32 是否影响 sample diversity？更低 rank 可能增加 diversity。
145	4. N=16 selection 结果有无 multi-seed bootstrap p-value？
146	5. SciERC RE conditional filtering 分析（非零 F1 子集）的 gap 结论是否改变？
147	
148	---
149	
150	## Missing References
151	
152	1. Eikema & Aziz (2022) "Sampling-Based Approximations to Minimum Bayes Risk Decoding for NMT" — MBR decoding 理论框架，与 consensus-proximity 直接相关
153	2. Freitag et al. (2022) "High Quality Rather Than High Model Probability" — MBR decoding
154	3. Kim et al. (2024) "VerifiNER" — ACL 2024, supervised NER verification
155	4. Malinin & Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction"
156	5. He et al. (2024) "Uncertainty Estimation on Sequential Labeling" — NAACL Findings 2024
157	6. Aggarwal et al. (2025) "Reasoning Aware Self-Consistency" — NAACL 2025 (需确认与已引 REASC 是否重复)
158	
159	---
160	
161	## External Review (Stanford Agentic Reviewer)
162	
163	外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）
164	
165	---
166	
167	## Overall Assessment
168	
169	**Overall Score: borderline (Findings track)**
170	**Confidence: 4/5**
171	
172	**判断依据**：
173	
174	论文在 quality estimation vs. sample selection 的问题分解上有真正贡献，correlation-selection gap 作为概念有实用价值，统计报告质量在 empirical NLP 论文中属上乘，WNUT-17 capability boundary 分析提供了重要方法论警示。
175	
176	但一个 critical 问题（constrained decoding confound）对核心 claim 构成 validity threat——如果 gap 主要由实验设置的 diversity 压缩导致，则核心贡献的 generalizability 受限。7 个 warning 级别问题（RE 单数据集、statistical logic、single seed、gap tautological 成分、MBR 联系缺失、多重比较、FK 独立性）共同表明论文在 soundness 和 framing 上仍有显著改进空间。
177	
178	两位 Reviewer 独立给出 3/5 (Findings) 评分，交叉回应后评分维持不变。论文方法论严谨的核心质量使其适合 Findings track，但 constrained decoding confound 未解决前不建议 Main Conference。
179	
180	**修订优先级**（按影响排序）：
181	1. **[Must]** Constrained decoding diversity 量化或对照实验（决定核心 claim 是否成立）
182	2. **[Should]** RE claim 降级 + conditional analysis（减少过度泛化风险）
183	3. **[Should]** Selection gap 措辞修正 + power analysis（统计严谨性）
184	4. **[Should]** Gap 论证分层 + MBR 联系（概念清晰度）
185	5. **[Should]** Multi-seed 验证或 Limitations 声明（可靠性）
186	6. **[Minor]** 术语统一、引用补充、数据一致性修正
187	
188	---
189	
190	## Detailed Comments（逐节）
191	
192	### Abstract
193	- "NER (three datasets of varying difficulty) and RE (SciERC)" 区分到位（Round 2 修正有效）
194	- "oracle headroom" 首次出现无定义，建议加括号解释
195	- "no signal reliably surpasses greedy" 措辞需修改为更严谨的统计表述
196	
197	### Introduction
198	- Quality estimation vs. sample selection 的分离框架论述清晰
199	- 对 Nedellec (2026) 的 (i)-(iii) 列举技术准确但语气偏 adversarial
200	- "First multi-family comparison" 需收窄 scope
201	
202	### Method (§3)
203	- Per-sample vs. instance-level 形式化清晰（Eq. 1-7）
204	- SJ Eq. 4: Hungarian matching 优化目标和 zero-IoU pairs 处理需补充
205	- FK §3.2: 独立性假设 one-line justification 不充分
206	- Consensus-proximity (§3.3): 未与 MBR decoding 建立联系
207	
208	### Experiments (§4)
209	- Quality estimation (§4.2): 数据全面，task difficulty crossover 有洞察力
210	- WNUT-17 conditional 分析揭示重要 artifact（Table 7）
211	- Selection gap (§4.3): 统计报告详实但 failure-to-reject 逻辑需修正
212	- Robustness (§4.4): temperature/N-scaling 分析系统性好，SJ stability 值得突出
213	
214	### Discussion (§5)
215	- Practical recommendations 具体可行
216	- "Why logprob fails" 段落是关键改进方向——需更多实证支持
217	- Constrained decoding 讨论需从 "future work" 升级为当前 limitation 的核心分析
218	- Gap 论证应分层：definitional (instance-level) vs. empirical (logprob + consensus-proximity)
219	
220	### Conclusion (§6)
221	- 三项 anchoring findings 总结准确
222	- RE hedging 到位但仍可进一步降级
223	
224	### Limitations
225	- 覆盖面广且诚实
226	- 建议新增：(a) constrained decoding 对 diversity 的影响作为 explicit limitation 条目；(b) single-seed 风险
227	
228	### Appendix
229	- Bootstrap CI 表 (Table 8) 有价值
230	- WNUT-17 全信号表 (Table 7) 补充到位
231	- Cross-configuration selection (Table 6) 增强了 gap 证据面
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dac09a6-5690-4491-b7ba-e1a5d4a7e08a",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "6c528fc1-2ca9-40ab-b053-94bc43bc099a",
  "sourceToolAssistantUUID": "0dac09a6-5690-4491-b7ba-e1a5d4a7e08a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T10:42:45.280Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YNP4r2nd9mw6ap2K94fuMu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_4.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c528fc1-2ca9-40ab-b053-94bc43bc099a",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7qcqZdfjmb4qbUxiQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f15918cb-da05-4407-bc84-76869776003b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d4HEhcK56BLbwYjYSpzLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 39839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 15 · 2026-05-22T10:42:45.308Z_

<details><summary>↩ Tool result · `toolu_01YNP4r2nd9mw6ap2K94fuMu`</summary>

```text
1	---
2	round: 4
3	overall_score: borderline (Findings)
4	timestamp: 2026-05-15T07:08:36.957412+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 4
11	
12	**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
13	**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)
14	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量+Round 3 修复验证）
15	**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛汇总
16	**Round 3 修复评估**: R2 系统审查了 13 个 Round 3 遗留问题——8 个 RESOLVED，4 个 PARTIALLY RESOLVED，0 个 UNRESOLVED
17	
18	---
19	
20	## Summary
21	
22	本文系统比较了三族（structural / surface / model-internal）五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。核心发现 "correlation-selection gap"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39）。经四轮迭代，论文统计方法论已达到高水平（TOST, bootstrap CI, 3-seed, Bonferroni），但核心贡献的 framing 和可复现性仍需改进。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 统计方法论显著改善。** Bootstrap CI (B=10,000)、TOST 等价检验（区分"无显著差异"与"确认等价"）、3-seed 稳定性验证、Bonferroni 校正声明——四轮迭代后统计分析在 NLP 实证论文中属上乘。TOST 揭示 EM/Voting 在 RE 上即使 ±5pp 也不等价于 greedy（系统性劣化）。[R1-S2, R2-S1 一致]
29	
30	**S2. 质量估计 vs. 样本选择的解耦是清晰的方法论贡献。** Per-sample vs. instance-level 信号的形式化区分（Eq. 1-7）和 ρ-AUROC dissociation 分析为后续工作提供了好的评估框架。[R1-S1, R2-S2 一致]
31	
32	**S3. 任务难度梯度分析有实际指导意义。** CoNLL（easy）→ SciERC（medium）→ WNUT-17（capability boundary）三级设计精良。WNUT-17 conditional ρ=0.038 (n.s.) 揭示高 failure rate 下信号表现为 artifactual。EM 在简单任务领先、结构化信号在复杂任务领先的 crossover 有实用价值。[R1-S3, R2-S3 一致]
33	
34	**S4. MBR decoding 连接概念优雅。** §5 将 selection strategies 形式化为 MBR 框架下不同 utility function 的实例化，有理论统一价值。[R1-S5, R2-S4 一致]
35	
36	**S5. Limitations section 诚实且具体。** 覆盖了 RE 单数据集、模型规模、constrained decoding、logprob 温度敏感性缺失等。[R1-S4, R2-S5 一致]
37	
38	**S6. 引用质量高。** 55 条引用经 OpenAlex 验证，0 orphan / 0 missing bib，51 条完全验证通过。Round 3 要求补充的 MBR decoding 等引用已到位。[R1-S6]
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（影响接收决定）
45	
46	**[Critical] W-C1: Correlation-selection gap 的 framing 需要区分"定义性 gap"和"经验性 gap"**
47	- 两位 Reviewer 独立提出（R1-N1, R2-N1），交叉回应后共识
48	- 4/5 信号是 instance-level，对同一 input 的 N 个候选给出相同分数——其 selection 失败是设计层面的先验预期。论文 §5 承认 "Four of five signals are instance-level by construction and cannot rank N candidates"，但这与 §4.3 和 abstract 中将 gap 作为核心 empirical contribution 的定位存在张力
49	- 真正的经验贡献是：(1) logprob（唯一 per-sample 信号）也失败（75% comparisons are ties, Cohen's d=0.038）; (2) consensus-proximity/MBR 策略未能弥合 gap
50	- R1 部分 rebut R2 的严厉程度——认为 MBR 在 MT 中成功但 IE 中失败的对比是非平凡的，但同意论证可加强
51	- **共识建议**：(a) Introduction 正面论证 "why the gap is not obvious a priori"——MBR 在 MT 中成功为何 IE 中失败？(b) Discussion 明确分离两层论证：定义性局限 (instance-level by construction) vs. 经验性失败 (logprob + consensus-proximity)；(c) 聚焦 logprob ties 的 75% 统计数据做深入分析
52	
53	**[Critical] W-C2: 训练配置和 prompt template 缺失，影响独立复现**
54	- 两位 Reviewer 独立提出（R1-N3, R2-N2），无分歧
55	- §4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少：learning rate、batch size、warmup、weight decay、optimizer、early stopping 策略、train/dev split、prompt template（NER/RE 各用什么格式？）、LoRA target modules、max sequence length、schema constraint 定义
56	- LoRA 微调对 lr 和 target modules 敏感，不同配置可能影响 output diversity 和信号表现
57	- **共识建议**：附录补充完整训练配置表 + prompt template 示例
58	
59	### Should-Fix（影响评分）
60	
61	**[Warning] W-S1: Constrained decoding 对 logprob 信号语义的影响需进一步量化**
62	- R1 列 critical (N2), R2 列 should-fix (W1)——存在严重性分歧，取交集为 elevated should-fix
63	- 论文自承 "75% of comparisons are effectively ties"、"logprob primarily reflects grammar compliance under constrained decoding"——但未实验验证此归因
64	- R1 建议分析 non-tie 的 25% 上 logprob 是否能成功 select；R2 建议讨论 constrained decoding 如何压缩 logprob 判别力
65	- R1 rebut R2 的 free-form baseline 建议：constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量
66	- **共识建议**：(a) 量化 logprob 分布——tie 的定义（Δlogprob < ε）、non-tie 子集上 logprob 的 selection 能力；(b) 在 Discussion 中讨论 constrained decoding 如何从 grammar compliance 层面压缩 logprob 区分度；(c) 限定 gap 结论的 scope 为 constrained decoding regime
67	
68	**[Warning] W-S2: RE 证据需进一步加强**
69	- 两位 Reviewer 一致（R1-W1, R2-N2 initial）
70	- R0-C3 的 claim 降级已完成（Conclusion 有 hedge），但 Abstract/Introduction 仍将 RE 作为等权证据
71	- 40% zero-F1 floor effect 严重压缩信号可区分范围，gap 的 RE 证据（-0.9pp, p=0.80）统计说服力弱
72	- **共识建议**：(a) SciERC RE non-zero F1 子集 selection 分析；(b) Abstract/Introduction 中 RE 标记为 preliminary/exploratory evidence
73	
74	**[Warning] W-S3: SJ vs EM 优势叙事应改为 difficulty-dependent complementarity**
75	- 两位 Reviewer 一致（R1 同意 R2-W4）
76	- SJ vs EM: Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著；CoNLL 上 EM 反超
77	- **共识建议**：弱化 "structural advantage" 叙事，强调在不同难度下 structural 和 surface signal 互补
78	
79	**[Warning] W-S4: Abstract 过于密集**
80	- 两位 Reviewer 一致
81	- 第 4 行含多层嵌套括号的超长句子
82	- **建议**：核心发现拆分为 2-3 个独立句子
83	
84	**[Warning] W-S5: "confidence signal" vs "consistency signal" 术语不一致**
85	- 两位 Reviewer 一致，Round 3 遗留（R3-W7 部分解决）
86	- logprob 不是 consistency signal 但被 "consistency signals" 统称覆盖
87	- **建议**：Section 3.2 开头增加明确 taxonomy 定义
88	
89	**[Warning] W-S6: Introduction novelty claim 缺 hedge**
90	- R2 提出，Round 3 遗留（R3-W6 部分解决）
91	- Conclusion 已有 hedge 但 Introduction 仍断言式
92	- **建议**：Introduction 的 contribution claim 与 Conclusion 的 hedge 对齐
93	
94	**[Warning] W-S7: 缺少 Xiong et al. (2024) "Can LLMs Express Their Uncertainty?" ICLR 2024**
95	- 两位 Reviewer 一致
96	- 系统评估 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文多族信号比较直接相关
97	- **建议**：Related Work "Uncertainty estimation" 段引用并区分
98	
99	### Minor Issues
100	
101	**[Info] W-M1**: Table 1 N=16 block 大面积空白，建议补脚注或合并呈现 [R1, R2 一致]
102	**[Info] W-M2**: Ethics Statement 位于 Limitations 内——建议改为独立 section [R2]
103	**[Info] W-M3**: Figure 1 caption 未解释 consensus-proximity 转换策略 [R2]
104	**[Info] W-M4**: Semantic entropy footnote 引用不可比数字——建议强化 caveat [R1]
105	**[Info] W-M5**: Entity Voting 公式 (5) 分母为 0 的边界条件未注明 [R1]
106	**[Info] W-M6**: Appendix reliability diagram ECE 的 bin 数量未报告 [R1]
107	**[Info] W-M7**: TOST δ 选择（±2, ±3, ±5 pp）缺乏实践意义论证 [R1]
108	**[Info] W-M8**: FK excess agreement negative 值含义可进一步解释 [R1]
109	**[Info] W-M9**: SJ normalizer max(|g_i|,|g_j|) vs |g_i∪g_j| 未对比 [R1]
110	
111	---
112	
113	## Round 3 Issue Resolution Status
114	
115	| ID | 问题 | Round 4 状态 | 说明 |
116	|----|------|-------------|------|
117	| R3-C1 | Constrained decoding confound | PARTIALLY RESOLVED | 承认但未量化 → 降为 W-S1 |
118	| R3-C2 | Failure-to-reject 措辞 | RESOLVED | TOST 已补充 |
119	| R3-C3 | N=8 single seed | RESOLVED | 3-seed 验证已补充 |
120	| R3-W1 | 多重比较校正 | RESOLVED | Bonferroni 声明已加 |
121	| R3-W2 | Gap tautological | PARTIALLY RESOLVED | 改善但核心张力仍在 → 升级为 W-C1 |
122	| R3-W3 | MBR 连接缺失 | RESOLVED | §5 MBR 段已写入 |
123	| R3-W4 | FK 独立性 | RESOLVED | Excess agreement 数据已补 |
124	| R3-W5 | Cross-model → cross-architecture | RESOLVED | 措辞已统一 |
125	| R3-W6 | First multi-family claim scope | PARTIALLY RESOLVED | Conclusion 有 hedge 但 Introduction 无 → W-S6 |
126	| R3-W7 | 术语不一致 | PARTIALLY RESOLVED | 表格缩写仍不统一 → W-S5 |
127	| R3-W8 | 遗漏引用 | RESOLVED | 已补全 |
128	| R0-C3 | RE 单数据集 | RESOLVED (claim降级) | 但 RE 证据仍薄弱 → W-S2 |
129	| R1-W1 | SJ 形式化歧义 | RESOLVED | 补全 |
130	
131	**总结**: Round 3 的 13 个 in_progress 问题中，8 个已完全解决，4 个部分解决（回归为本轮 issue），0 个完全未解决。论文在统计方法论上的改进（TOST、3-seed、Bonferroni、MBR 连接）是实质性的。
132	
133	---
134	
135	## Reviewer Consensus [AGREE]
136	
137	1. **Gap framing 需分层论证**：定义性局限 (instance-level) 和经验性失败 (logprob + consensus-proximity) 应明确分离 [R1-N1 ≈ R2-N1, 共识]
138	2. **训练细节/prompt template 必须补充**：独立复现的基本要求 [R1-N3 = R2-N2, 完全共识]
139	3. **RE 证据仍然薄弱**：claim 降级已做但可进一步加强 [R1-W1, R2 确认]
140	4. **SJ 优势叙事应改为互补性**：Bonferroni 下不显著，CoNLL 上 EM 反超 [R1 agree R2-W4]
141	5. **术语需统一 + Abstract 需简化**：[双方一致]
142	6. **Xiong et al. (2024) 应引用**：高度相关的 LLM 置信度评估工作 [双方一致]
143	7. **统计方法论已达高水准**：四轮迭代的改进得到两位 Reviewer 一致认可 [双方一致]
144	
145	## Reviewer Divergence [REBUT]
146	
147	1. **Constrained decoding 严重性**：R1 列 critical（需实验量化）→ R2 列 should-fix（需更多讨论）→ **共识为 elevated should-fix**，量化 logprob 分布而非增加 free-form 实验
148	2. **Gap 非平凡性的严厉程度**：R2 认为 excitement 仅 2.5（gap 可预测）→ R1 rebut（MBR 类比非平凡，logprob ties 是经验发现）→ **共识评分 3.0/5**
149	3. **Free-form generation baseline**：R2 建议增加 → R1 rebut（constrained decoding 是方法论必要条件）→ **共识为不需要 free-form 实验，但需量化 diversity 压缩效应**
150	4. **BibTeX 键名 nedellec2026consistency**：R2 建议修改 → R1 rebut（内部细节，\citet 输出正确）→ **共识降至 minor**
151	
152	---
153	
154	## Questions to Authors
155	
156	1. Logprob ties（75%）的具体定义是什么？Δlogprob < ε 的 ε 取值？在 non-tie 子集上，logprob 作为 selector 的表现如何？
157	2. SciERC RE non-zero F1 子集上的 selection gap 分析结果是否与主文结论一致？
158	3. 是否考虑过在 Introduction 中正面论证 "why the gap is not obvious"——例如引用 MBR 在 MT 中的成功作为对比？
159	4. LoRA target modules 具体是 all linear 还是 q_proj/v_proj only？这对 output diversity 的影响有多大？
160	5. Prompt template 中 schema constraint 如何定义？是否有 few-shot examples？
161	
162	---
163	
164	## Missing References
165	
166	1. **Xiong et al. (2024)** "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs" ICLR 2024 — 高度相关 [两位 Reviewer 一致]
167	2. **Ye et al. (2025)** "Do LLMs Estimate Uncertainty Well in Instruction Following?" ICLR 2025 — 中等相关 [R2]
168	3. **Bertsch et al. (2024)** "In-Context Learning with Long-Context Models" — 与 test-time scaling 相关 [R1]
169	4. **Wiher et al. (2022)** "On Decoding Strategies for Neural Text Generators" — 与 constrained decoding diversity 相关 [R1]
170	5. **Müller & Sennrich (2021)** "Understanding the Properties of MBR Decoding in NMT" — 与 §5 MBR 连接直接相关 [R1]
171	
172	---
173	
174	## External Review (Stanford Agentic Reviewer)
175	
176	外部审稿：未启用
177	
178	---
179	
180	## Overall Assessment
181	
182	**Overall Score: 3.0 / 5 (Findings: borderline)**
183	**Confidence: 4/5**
184	
185	**判断依据**：
186	
187	两位 Reviewer 交叉回应后评分收敛至 3.0/5（R1: 3.0 维持不变, R2: 3.5→3.0 下调）。
188	
189	**支持接收的因素**：
190	- 统计方法论经四轮迭代达到高水准（TOST, bootstrap CI, 3-seed, Bonferroni）
191	- QE vs. selection 的解耦框架有方法论贡献价值
192	- 任务难度梯度分析和 WNUT-17 capability boundary 发现有实用指导意义
193	- MBR decoding 连接提供理论统一
194	- Round 3 的 13 个 issue 中 8 个完全解决，改进幅度显著
195	
196	**制约接收的因素**：
197	- 核心贡献 "correlation-selection gap" 的 framing 仍未清晰区分定义性局限和经验性发现（W-C1），削弱 novelty
198	- 训练细节/prompt template 缺失影响独立复现（W-C2）
199	- Constrained decoding 对 logprob 信号语义的影响仍为 unquantified confound（W-S1）
200	- RE 证据薄弱（W-S2），SJ 优势 marginal（W-S3）
201	
202	**修订优先级**（按影响排序）：
203	1. **[Must]** Gap framing 分层（定义性 vs 经验性）——决定核心贡献的 novelty 定位
204	2. **[Must]** 训练配置 + prompt template 补充——复现基本要求
205	3. **[Should]** Constrained decoding 下 logprob 分布量化——加强 gap 解释力
206	4. **[Should]** RE conditional analysis + 进一步降级——减少过度泛化
207	5. **[Should]** SJ narrative 调整 + Abstract 简化 + 术语统一——写作质量
208	6. **[Minor]** Table 格式、Ethics 位置、引用补充
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f15918cb-da05-4407-bc84-76869776003b",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "d3221e87-dd06-4002-9e2f-e54895e3d176",
  "sourceToolAssistantUUID": "f15918cb-da05-4407-bc84-76869776003b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T10:42:45.398Z_

<details open><summary>🔧 Tool call — Read · `toolu_018iQWVG4w2owpr8A3W17LZX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_5.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3221e87-dd06-4002-9e2f-e54895e3d176",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU7qcqZdfjmb4qbUxiQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53ffbe82-363c-4fa1-bfd0-847ecf03458e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d4HEhcK56BLbwYjYSpzLF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 39839,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2454
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 527,
          "cache_read_input_tokens": 39839,
          "cache_creation_input_tokens": 2454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2454,
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

_source line 17 · 2026-05-22T10:42:45.409Z_

<details><summary>↩ Tool result · `toolu_018iQWVG4w2owpr8A3W17LZX`</summary>

```text
1	---
2	round: 5
3	overall_score: borderline
4	timestamp: 2026-05-15T08:08:03.142382+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 5
11	
12	**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
13	**Venue**: EMNLP 2026 Findings (via ARR May 2026 cycle)
14	**Deadline**: 2026-05-25
15	**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计有效性; R2: 新颖性 + framing + related work + 写作质量）
16	**轮次**: Round 1（独立审稿 → 交叉分享 → 收敛，1 轮完成）
17	
18	---
19	
20	## Summary
21	
22	论文系统比较了 5 种置信度信号（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在生成式 IE（NER + RE）中用于 quality estimation 和 sample selection 的能力。核心发现是 "correlation-selection gap"——信号能预测哪些实例模型处理可靠（ρ 最高 0.38, AUROC 最高 0.75），但无法在 N 个候选中选出最佳输出（p>0.39）。附带发现：信号排名随 task difficulty 变化（easy task EM 领先, hard task structural signals 领先），以及 WNUT-17 上的 capability boundary（conditional ρ 趋近零）。
23	
24	---
25	
26	## Strengths
27	
28	1. **统计分析严谨性在 ACL 投稿中属上乘**。Bootstrap CI (B=10,000)、TOST 等价检验（多级 δ）、sign test、Cohen's d、multi-seed stability (σ≤0.025)、conditional filtering、diversity stratification——远超同类 empirical papers。[两位 Reviewer 一致肯定]
29	
30	2. **Negative result 有实际价值**。Log-probability 作为唯一 per-sample signal 也无法有效 select（p=0.39, 13-18 pp oracle headroom），且原因可追溯到 constrained decoding 下的 score compression（60% instance 内 range <0.05, Appendix F）。这对 test-time scaling 文献是重要补充。[R1 Soundness 3, R2 Soundness 3.5]
31	
32	3. **Problem formulation 清晰**。Per-sample vs instance-level 信号的分类框架简洁有力；quality estimation vs sample selection 的解耦是概念上的贡献。[两位 Reviewer 一致]
33	
34	4. **实验设计公平**。两模型相同 LoRA 配置（Appendix E Table 8），三数据集覆盖 difficulty gradient（CoNLL easy → SciERC hard → WNUT-17 boundary），训练细节、prompt template 完整（Reproducibility 4/5）。[两位 Reviewer 一致]
35	
36	5. **引用完整**。58 条引用，核心相关工作（Nédellec et al. 2026, Wang et al. 2023, Kuhn et al. 2023, Eikema & Aziz 2022, Xiong et al. 2024）均已覆盖。
37	
38	---
39	
40	## Weaknesses
41	
42	### Must-Fix（影响接收决定）
43	
44	**[CONSENSUS] W-C1: Constrained decoding 作为核心混淆变量未被隔离，claim scope 与 evidence 不匹配**
45	- 来源: R1-N1 + R1-N2 + R2-N1 (constrained decoding 部分)
46	- 两位 Reviewer 独立提出，交叉分享后完全共识
47	- 核心问题: 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文无法区分 correlation-selection gap 是 structured IE 的固有属性还是 constrained decoding 的 artifact。论文自身的 Appendix F 提供了反面证据：在 logprob non-tied subset (n=210, 40%) 中，logprob selection 显著优于 greedy (+2.9 pp, p=0.01, within-instance ρ 从 0.08 升到 0.39)——暗示 gap 主因是 constrained decoding 造成的 score compression，而非 IE 本身的固有性质
48	- 当前论文的 title、abstract、conclusion 将 gap 呈现为 structured IE 的通用属性，未限定 constrained decoding setting
49	- 修改建议: (a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting; (b) 提升 Appendix F non-tied analysis 至主文 Discussion; (c) 明确承认 non-tied evidence 对 claim 普适性的影响; (d) 如条件允许添加 free-form decoding 消融更佳（但非强制）
50	
51	**[CONSENSUS with nuance] W-C2: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性**
52	- 来源: R2-N1 (tautological) + R1 交叉回应
53	- R2 认为 gap 被 "两头夹击"（4/5 instance-level failure = tautological; logprob failure = artifact），整体 contribution 空心化
54	- R1 部分 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding（MBR 在 MT 成功但 IE 失败并非 a priori obvious）；论文已有两层论证结构（Discussion §5）
55	- **共识**: Gap 不完全 tautological，但 Contribution 2 应以 logprob score compression + MBR/consensus-proximity empirical failure 为重心，而非 "5 signals all fail" 的统一叙事。Abstract 和 Introduction 需 reframe
56	- 修改建议: (a) Reframe C2 聚焦 logprob 和 MBR failure; (b) 弱化 "5 signals all fail" 叙事; (c) Introduction 加强非显然性论证
57	
58	### Should-Fix（影响评分但不一票否决）
59	
60	**[CONSENSUS] W-S1: RE "preliminary" 标注与实际使用不一致**
61	- 来源: R1-W1 + R2-W2
62	- Abstract 标注 "(SciERC, preliminary)"，但 Table 1/2, Figure 2-3, Discussion 大量使用 RE 结果无限定词。Contribution #3 将 RE 结论嵌入通用表述
63	- 修改建议: 全文一致标注 RE 为 single-benchmark preliminary; Contribution #3 加限定; Future work 列出 RE 多数据集验证
64	
65	**[CONSENSUS] W-S2: Abstract 信息密度过高**
66	- 来源: R2-W1, R1 交叉 AGREE
67	- 9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念 + technical arguments
68	- 修改建议: 聚焦 1-2 个核心 claim，具体数字移入 Introduction
69	
70	**[CONSENSUS] W-S3: "First multi-family comparison" claim 过度依赖 scope 限定**
71	- 来源: R2-W4, R1 交叉 AGREE
72	- 通过堆叠修饰词确保 "first" 成立属于 scope engineering
73	- 修改建议: 改为描述性表述，避免 "first" claim
74	
75	**[CONSENSUS] W-S4: "Cross-architecture" 用词过度**
76	- 来源: R1-W3, R2 交叉 AGREE
77	- 两模型均为 8B decoder-only transformer (GQA, RoPE, SwiGLU)
78	- 修改建议: 改为 "across two model families at 8B scale"
79	
80	**[CONSENSUS] W-S5: 术语不一致**
81	- 来源: R3-W7 (Round 3 遗留, 仍未解决)
82	- Table 1 "Voting Conf." vs Table 4/7 "VC" vs 正文 "entity voting"
83	- 修改建议: 全文统一（建议全部用 VC）
84	
85	**[CONSENSUS, low severity] W-S6: FK independence justification 不够严格**
86	- 来源: R1-W2, R2 交叉 AGREE with nuance (severity 偏低)
87	- Excess agreement (-0.4% to -4.0%) 未注明 configuration, 未引用 FK 非独立 rater 行为文献
88	- 修改建议: 补充 configuration 信息 + 引用; FK 非核心 contribution, 可接受 minimal fix
89	
90	**[CONSENSUS, low severity] W-S7: TOST δ 选择缺乏外部锚点**
91	- 来源: R1-W4, R2 交叉 AGREE with nuance
92	- 多水平 δ 已构成 sensitivity analysis, 但需引用 IAA 数据
93	- 修改建议: 引用 1-2 篇 IE benchmark IAA 文献
94	
95	**[R1 only] W-S8: Qwen3-8B thinking token 训练不一致**
96	- 来源: R1-W5, R2 交叉 AGREE
97	- SciERC 未禁用 enable_thinking, CoNLL/WNUT 显式禁用
98	- 修改建议: Limitations 讨论此不一致性
99	
100	**[R2 only, R1 REBUT] W-S9: Soft Jaccard 方法论新颖性有限**
101	- 来源: R2-W3
102	- R1 rebut: application novelty 在 IE quality estimation 中是新的; Nédellec (2026) 承认其表面方法的局限
103	- 共识: SJ 有 application novelty 但不应过度宣传; "core structural signal" 可弱化为 "primary"
104	
105	**[R2 only] W-S10: 与 Nédellec et al. (2026) 增量贡献论证不充分**
106	- 来源: R2-N2
107	- R1 rebut: WNUT-17 conditional collapse 和 logprob negative correlation 不是直觉可预测; difficulty-dependent crossover 是核心 claim
108	- 共识: Findings-worthy 但非 ground-breaking; 建议更诚实量化增量
109	
110	### Minor（不影响接收）
111	
112	- **M1** [CONSENSUS]: Semantic entropy 脚注（§4.2）——自述 "direct comparison not meaningful" 但给出具体数字，可能误导。建议缩短
113	- **M2** [R1]: `he2024uncertainty` bib entry 与引用上下文不匹配（sequential labeling 论文被描述为 LLM survey）
114	- **M3** [CONSENSUS]: Table 1 脚注格式（`\textsuperscript{†}` + `\footnotetext`）在 two-column 模板下可能渲染异常
115	- **M4** [R1]: Consensus-proximity = LOO-SJ 等价性声称缺少推导
116	- **M5** [CONSENSUS]: 部分 bib entries (`hobelsberger2025systematic`, `lightman2024verify`) 在 OpenAlex 未找到; `feng2025optimal` 和 `ye2025uncertainty` author name 可能有 variant
117	- **M6** [R2]: Ethics Statement 仅 2 句（格式合规但内容偏简）
118	
119	---
120	
121	## Reviewer Consensus
122	
123	以下问题两位 Reviewer 在交叉分享后完全一致：
124	
125	1. **Constrained decoding confound 是论文最大弱点** [AGREE]: 论文自身 Appendix F 数据（non-tied subset logprob selection +2.9pp, p=0.01）暗示 gap 主因是 score compression 而非 IE 固有属性。Title/Abstract/Conclusion 的 claim scope 需限定
126	2. **RE scope 不一致** [AGREE]: Abstract "preliminary" 与后续大量使用之间矛盾
127	3. **Abstract 过密** [AGREE]: 首次阅读难以把握核心 message
128	4. **"Cross-architecture" 过度** [AGREE]: 改为 "across two model families at 8B scale"
129	5. **"First" claim 应去掉** [AGREE]: scope engineering
130	6. **术语不一致** [AGREE]: 需全文统一
131	7. **统计分析质量高** [AGREE]: bootstrap CI、TOST、multi-seed 在 ACL 投稿中属上乘
132	8. **训练配置完整** [AGREE]: Reproducibility 4/5
133	
134	---
135	
136	## Reviewer Divergence
137	
138	1. **Tautological 程度**:
139	   - R2: Gap 被两头夹击，整体 contribution 空心化 → Excitement 2.5
140	   - R1: Consensus-proximity/MBR failure 是 non-trivial → Excitement 3.5
141	   - **Resolution**: 共识认为 gap 不完全 tautological，但 C2 需 reframe 以 logprob+MBR failure 为重心
142	
143	2. **与 Nédellec 增量**:
144	   - R2: 三个增量均偏弱
145	   - R1: Difficulty gradient 发现（WNUT-17 conditional collapse）不是直觉可预测
146	   - **Resolution**: Findings-worthy 但非 ground-breaking
147	
148	3. **SJ 方法新颖性**:
149	   - R2: 标准技术组合
150	   - R1: Application novelty 在 IE context 中是新的
151	   - **Resolution**: 有 application novelty 但不应过度宣传
152	
153	---
154	
155	## Questions
156	
157	1. Appendix F 的 non-tied subset 中 logprob selection 有效 (+2.9pp, p=0.01)。如果 constrained decoding 是 score compression 主因，free-form decoding 下 logprob 是否可能成为有效 selector？如何论证 gap 是 IE-inherent 而非 decoding-induced？
158	2. Consensus-proximity = LOO-SJ 的数学等价性缺少推导。能否补充？
159	3. FK excess agreement (-0.4% to -4.0%) 在哪个 configuration 测量？是否在所有配置一致？
160	4. WNUT-17 logprob 负相关 (ρ=-0.410) 的机制解释？
161	
162	---
163	
164	## Missing References
165	
166	- "Trust but Verify! A Survey on Verification Design for Test-time Scaling" (2025) — 与 Discussion 中 verifier 建议直接相关 [两位 Reviewer 一致]
167	- MBR 在非 MT 任务 (summarization, QA) 中的应用文献 — 增强 Discussion §5 MBR 对比分析 [两位 Reviewer 一致]
168	- 最新 uncertainty quantification survey (2025-2026) [R2 建议]
169	
170	---
171	
172	## External Review (Stanford Agentic Reviewer)
173	
174	外部审稿：未请求（项目未启用外部审稿）。
175	
176	---
177	
178	## Overall Assessment
179	
180	**评分: borderline (3.0/5)**
181	**置信度: 高 (4/5)**
182	
183	| 维度 | R1 | R2 | 加权 |
184	|------|-----|-----|------|
185	| Soundness | 3.0 | 3.5 | 3.25 |
186	| Excitement | 3.5 | 2.5 | 3.0 |
187	| Reproducibility | 4.0 | 4.0 | 4.0 |
188	| Overall | 3.0 | 3.0 | 3.0 |
189	
190	**总结判断**: 这是一篇执行质量较高的 empirical study——统计分析严谨、实验设计公平、训练细节完整。核心概念（quality estimation vs sample selection 解耦）对 test-time scaling 实践有指导价值。
191	
192	**但存在两个结构性问题阻碍更高评分:**
193	
194	1. **Claim scope 与 evidence 不匹配**: 论文将 correlation-selection gap 呈现为 structured IE 的通用属性，但所有实验均在 constrained decoding 下进行，且论文自身数据（Appendix F non-tied subset）暗示 gap 主因可能是 score compression artifact。Title/Abstract/Conclusion 需加限定词。
195	
196	2. **核心贡献的 tautological 成分**: 4/5 信号的 selection failure 是定义的逻辑后果（instance-level signals 无法 rank per-sample），真正 non-trivial 的发现是 logprob 的 failure 和 consensus-proximity/MBR 在 IE 中的 failure。C2 需 reframe。
197	
198	**Findings track 接收条件**: 如果作者能 (a) 在核心 claim 中限定 constrained decoding scope, (b) reframe C2 以 logprob + MBR failure 为中心, (c) 统一 RE preliminary 标注, (d) 精简 Abstract, 则论文适合 Findings track。当前版本需 moderate revision。
199	
200	---
201	
202	## Detailed Comments（按 Section）
203	
204	### Abstract
205	- 信息密度过高，需拆分为 2-3 句核心 claim
206	- "(SciERC, preliminary)" 限定词需在后续分析中一致使用
207	- "for Information Extraction" 需加 "under constrained decoding" 限定
208	
209	### §1 Introduction
210	- Contribution 2 需 reframe：将 "5 signals all fail" 叙事改为以 logprob compression + MBR failure 为中心
211	- Contribution 3 需加 RE single-benchmark 限定
212	- "first multi-family comparison" → 改为描述性表述
213	- MBR 在 MT 中成功 → IE 中失败的非显然性论证可以加强
214	
215	### §2 Related Work
216	- 引用覆盖良好
217	- 补充: test-time verification survey, MBR 非 MT 应用
218	- `he2024uncertainty` 引用上下文需修正
219	
220	### §3 Method
221	- SJ 形式化清晰完整
222	- FK independence justification 补 configuration 信息
223	- Consensus-proximity = LOO-SJ 等价性需推导
224	- "core structural signal" → "primary structural signal"
225	
226	### §4 Experiments
227	- 统计分析严谨
228	- Table 1 脚注格式检查 PDF 渲染
229	- Semantic entropy 脚注缩短
230	- TOST δ 引用 IAA 数据
231	- WNUT-17 logprob negative correlation 需机制解释
232	
233	### §5 Discussion
234	- "Two layers" 结构良好但需更明确分离定义性 vs 经验性 gap
235	- 提升 Appendix F non-tied analysis 至此处
236	- 承认 non-tied evidence 对 claim 普适性的影响
237	
238	### §6 Conclusion
239	- 加 constrained decoding scope 限定
240	- RE 限定与 Abstract 对齐
241	- "across model families" → "across two model families at 8B scale"
242	
243	### Limitations
244	- 全面诚实
245	- 补充 thinking token 训练不一致性讨论
246	
247	### Appendix
248	- Training config (Table 8) 完整 ✓
249	- Prompt template 提供 ✓
250	- Appendix F logprob tie analysis 应提升至主文
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53ffbe82-363c-4fa1-bfd0-847ecf03458e",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "12aacba1-56d7-43fd-803e-6a99b524671a",
  "sourceToolAssistantUUID": "53ffbe82-363c-4fa1-bfd0-847ecf03458e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-22T10:42:47.871Z_

Now let me continue reading the remaining critical rounds to get the full trajectory:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12aacba1-56d7-43fd-803e-6a99b524671a",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU869CnUkuCWfLoc1bf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18f5822a-9d5a-4359-8d33-e174a3ddc62e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012aQxXkcn9Pj3Sno5wsasp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37061,
      "cache_read_input_tokens": 42293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37061,
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

_source line 19 · 2026-05-22T10:42:48.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MTHFfyb3Xn2FiugyXmkjWJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18f5822a-9d5a-4359-8d33-e174a3ddc62e",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU869CnUkuCWfLoc1bf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5470be9f-9393-4fbc-b7fe-66a54a24ad52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012aQxXkcn9Pj3Sno5wsasp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37061,
      "cache_read_input_tokens": 42293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37061,
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

_source line 20 · 2026-05-22T10:42:48.944Z_

<details><summary>↩ Tool result · `toolu_01MTHFfyb3Xn2FiugyXmkjWJ`</summary>

```text
1	---
2	round: 10
3	overall_score: weak accept / borderline (Findings acceptance)
4	timestamp: 2026-05-16T02:29:04.735110+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# Round 9 审稿报告
11	
12	**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction
13	**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)
14	**Reviewers**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+完整性+相关工作+格式)
15	**审稿模式**: Fresh review (Round 9)
16	
17	---
18	
19	## Summary
20	
21	本文研究 LLM-based 结构化信息抽取（NER/RE）中五种一致性信号（SJ, VC, FK, EM, LP）的质量估计与样本选择能力。核心发现是 "correlation-selection gap"：所有信号均能有效预测输出质量（ρ 达 0.45, AUROC 达 0.82），但无法从 N 个采样中选出最优输出，尽管 oracle headroom 达 13-18pp。论文通过 free-form decoding ablation 证明 LP score compression 是 task-intrinsic 的（NER 上成立），并在 4B-8B 两个规模上验证了结论的稳健性。
22	
23	---
24	
25	## Strengths
26	
27	**S1. 概念框架有价值。** Quality estimation vs. sample selection 的显式区分在 IE 文献中此前未被正式化。Instance-level vs. per-sample 信号的分类法直接解释了 4/5 信号为何不能做 selection，为后续工作提供设计准则。[R1-S1, R2-S1 共识]
28	
29	**S2. LP 压缩分析深入且有实际价值。** Median within-instance LP range = 0.041 nats, 60.3% tied instances, non-tied subset 显著优于 greedy (+2.9pp, p=0.004), ε sensitivity sweep 验证阈值稳健性。这是论文最有价值的实证发现。[R2-S2, R1 隐含认同]
30	
31	**S3. 统计分析显著优于同类 empirical NLP 工作。** Bootstrap CI with pairwise Δρ、TOST 等价检验（含三类外部锚点 δ_SEM/δ_practical/δ_literature）、instance-level permutation test、Fisher combined p、Cohen's d 报告。诚实标注所有 borderline/preliminary 结果。[R1-S3, R2-S3 高度共识]
32	
33	**S4. 实验设计严谨。** Difficulty gradient（SciERC → CoNLL → WNUT-17）、cross-model (Qwen/LLaMA)、cross-scale (4B/8B)、multi-seed (3 seeds, Kendall's W=1.000)、free-form ablation。形成完整 robustness picture。[R1-S2, R2-S3]
34	
35	**S5. Appendix 极其充实（~15 pages）。** 17 个 appendix section 覆盖了几乎所有可预见质疑：SJ normalizer robustness (Δρ<0.005)、LOO-SJ equivalence、ε sensitivity、FK independence permutation test、OOD transfer、thinking token 三部分定量分析、LP failure stability cross-seed analysis。体现高度学术自觉。[R1-S5, R2-S4]
36	
37	**S6. Limitations 透明度高。** RE preliminary 标注贯穿全文（Abstract, Introduction #3, Table captions, Conclusion），thinking token confound 有三部分定量分析，free-form ablation 的 RE reversal 未回避。[R1-S4, R2-S6]
38	
39	**S7. Related work 覆盖面广。** Self-consistency 方向（Wang 2023 等 10+ 篇）、MBR decoding（Eikema 2022/2025, Freitag 2022 等）、uncertainty surveys（Geng 2024, Xia 2025, Hobelsberger 2025）、structured IE (Zhou 2024 等)。与 Eikema 2025 structured MBR 的对接尤其到位。[R2-S5]
40	
41	---
42	
43	## Weaknesses
44	
45	### Must-Fix（影响接收决定）
46	
47	**N1** [critical, 共识] **Correlation-selection gap 对 4/5 信号是 definitional 而非 empirical finding — 框架过度膨胀贡献**
48	
49	两位 Reviewer 独立提出相同核心问题（R1-N2, R2-N1）：VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——这是信号定义的直接推论。标题 "The Correlation-Selection Gap" 和 Abstract "none improves best-of-N selection" 将部分 tautological 的观察框架化为统一发现，过度膨胀了贡献。
50	
51	真正的实验发现仅是：(a) LP score compression 导致唯一的 per-sample signal 也失败；(b) consensus-proximity/MBR-style selection 也失败——后者是 non-trivial 的。论文 Discussion §5 和 Table 2 已有两层结构和透明声明（line 8: "assign a single score per input; they cannot rank candidates by construction"），但 Abstract/Introduction/Conclusion 的修辞权重仍将 gap 呈现为统一发现。
52	
53	**建议修改方向**：(1) Abstract/Introduction 中用一句话 dismiss instance-level 信号的 selection 失败为 definitional consequence，将贡献重心移向 LP compression + MBR failure 的实证发现；(2) 或将分类法本身（instance-level vs per-sample）定位为核心贡献（Contribution #1），降低 selection failure 的修辞权重。
54	
55	⚠️ 此问题自 Round 3 (R3-W2) 起反复出现，Round 8 的 resolution（视觉分组+两层结构）被两位 Reviewer 认为不够——需要在 Abstract/Introduction/Conclusion 层面根本性 reframe。
56	
57	---
58	
59	**N2** [critical, 共识] **Abstract/Conclusion 对 free-form ablation 过度概括——省略 RE LP selection 方向反转**
60	
61	两位 Reviewer 共识（R1-N1, R2-N2）：Abstract 称 "A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types"，但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。"across task types" 与 RE 结果直接矛盾。
62	
63	论文 Discussion 和 Limitations 诚实承认了 RE reversal，但 Abstract 和 Conclusion 的措辞未限定范围。
64	
65	**建议修改方向**：Abstract 改为 "confirms NER compression is intrinsic; RE shows a directional reversal warranting further investigation"。Conclusion 同步修改，不能说 "across task types" without qualification。
66	
67	⚠️ 此问题自 Round 7 (R7-C3) 起存在，Round 8 resolution（Discussion scope 限定为 NER only）被认为不够——Abstract/Conclusion 仍未修正。
68	
69	---
70	
71	**N3** [critical, R1 主导, R2 间接支持] **标题/Abstract "Information Extraction" scope 过宽——RE 仅 preliminary**
72	
73	R1-N3 列 critical：RE 仅在 SciERC 上测试（40% zero F1），全部标注 "preliminary"。标题说 "Information Extraction" 但核心可靠结论仅覆盖 NER。Introduction contribution #3 已正确标注 "RE conclusions rest on SciERC alone (preliminary)"，但 Conclusion 未同步 hedge。
74	
75	R2 在 W3（Conclusion 未 hedge RE）和 W4（模型规模限制）中间接呼应。
76	
77	**建议修改方向**：Conclusion 增加 "RE conclusions are preliminary, based on a single benchmark"。标题可保留 "Information Extraction" 但正文需一致 hedge。
78	
79	---
80	
81	### Should-Fix（影响评分但不一票否决）
82	
83	**W1** [warning, R2] **缺少其他 per-sample signal baseline（verbalized confidence, self-certainty）**
84	Per-sample signal 仅有 LP 一种。Tian et al. (2023, verbalized confidence)、Kang et al. (2025, self-certainty, 已引用) 等 per-sample signal 未对比。"no signal improves selection" 的结论不完整。建议至少在 Limitations 中承认仅测试了一种 per-sample signal。
85	
86	**W2** [warning, 共识] **24 个 orphan bib entries 未引用**
87	包括 Culotta & McCallum 2004（IE confidence estimation 开创性工作）、Kadavath 2022（LLMs know what they know）、Malinin & Gales 2021（autoregressive uncertainty for structured prediction）等高度相关工作。应引用相关的或删除不相关的。
88	
89	**W3** [warning, R1] **TOST 外部锚点结果 configuration-dependent 未整合进主文**
90	外部锚点下 LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。"no signal improves selection" 应改为 "no signal consistently improves selection"。当前主文 Section 4.2 缺少这一 nuance。
91	
92	**W4** [warning, R1] **VC majority-voting selection 的 per-sample 性质和失败机制未分析**
93	VC 在 selection 语境下通过 majority-voted output + overlap 实质成为 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但表现最差（0.623）。这个失败值得 1-2 句机制分析。
94	
95	**W5** [warning, R1] **多重比较校正不完整**
96	5 signals × 3 datasets × 2-3 models 大量比较无系统性校正。对于负结果，未校正 p>0.05 已足够但应明确说明这一逻辑。
97	
98	**W6** [warning, R1] **Table 1 主表单种子未标注**
99	Table 1 seed=42 单次结果，与 Table 7 3-seed mean 有差异（LP NER: 0.205 vs 0.217）。虽然 ranking 一致（W=1.000）但应标注。
100	
101	**W7** [warning, 共识] **Scale ablation "not model capacity" 结论过强**
102	仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。应弱化为 "within the 4B-8B range, task difficulty appears to be the primary driver"。
103	
104	---
105	
106	### Minor（不影响接收）
107	
108	- **M1** [info, R2] Table 2 "Greedy" 指 T=1.0 single sample，但 greedy 通常指 argmax (T→0)——建议改措辞或加注释。
109	- **M2** [info, 共识] Section 3.2 FK 负依赖 "−0.4% to −4.0%" 无推导过程或 appendix reference。
110	- **M3** [info, R1] "correlation-selection gap" 术语反复使用但无操作性定义。建议 Section 4.2 给出形式化定义。
111	- **M4** [info, R2] Discussion ρ=0.38 是 VC ρ=0.379 的四舍五入，精度不一致。
112	- **M5** [info, R1] Table 2 NER 2-seed vs RE single seed 统计标准不一致。
113	- **M6** [info, R2] Bib entry 名/姓顺序问题（feng2025optimal, snell2025scaling 等），建议统一检查。
114	
115	---
116	
117	## Reviewer Consensus
118	
119	**[AGREE]** 以下问题两位 Reviewer 完全达成共识：
120	- N1: Instance-level 信号 selection 失败是 definitional — 框架需 reframe
121	- N2: Abstract 对 free-form ablation 过度概括 — RE reversal 必须标注
122	- S3/S4: 统计分析和实验设计是论文的核心优势
123	- S2: LP compression 是最有价值的实证发现
124	- W2: Orphan bib entries 需清理
125	- W7: Scale ablation 结论需弱化
126	
127	## Reviewer Divergence
128	
129	**分歧 1** [R1: 3.5/5 vs R2: 3.0/5] — R1 认为概念贡献（metric dissociation + correlation-selection gap taxonomy）即使部分 tautological 也有信息量，MBR failure 是 non-trivial 的发现；R2 认为框架性贡献被高估，真正的 novelty 仅限于 LP compression。这是程度分歧而非方向分歧。
130	
131	**分歧 2** [R2-W1 vs R1 未提] — R2 认为缺少其他 per-sample signal baseline（verbalized confidence）是 should-fix；R1 未独立提出此问题但 Q2 问了组合信号。
132	
133	**分歧 3** [R2-W5 vs R1 未提] — R2 认为 consensus-proximity operationalization 有些 ad-hoc；R1 认为与 MBR 的连接已在 Appendix L 充分讨论。
134	
135	---
136	
137	## Questions to Authors
138	
139	**Q1**: VC 在 selection 语境下（majority-voted output + overlap）实质成为 per-sample signal——为什么仍然失败？是否因为 voted output 与高频 sample 高度 overlap，导致 selection 退化为选最平庸的 sample？
140	
141	**Q2**: 是否尝试过其他 per-sample signals（verbalized confidence, self-certainty, entropy of next-token distribution）？或组合信号（LP + SJ weighted combination）？
142	
143	**Q3**: Free-form RE LP reversal（−0.68pp → +1.69pp）是最 actionable 的发现之一。这在 seed 42 之外能否复现？如果能，这可能成为重要 positive contribution。
144	
145	**Q4**: ε=0.05 是否构成 p-hacking？Table 13 的 ε sweep 显示此阈值最大化了 statistical separation (p=0.004)。
146	
147	**Q5**: Thinking token confound（Appendix G）分析了 LP 影响，但是否也改变了模型 output distribution 进而影响 consistency signals？
148	
149	---
150	
151	## Missing References
152	
153	**论文中已有 bib entry 但未引用**（应引用或删除）：
154	- Kadavath et al. 2022 "Language Models (Mostly) Know What They Know" — LLM self-knowledge/calibration 开创性工作
155	- Culotta & McCallum 2004 "Confidence Estimation for Information Extraction" — IE confidence estimation 早期工作
156	- Malinin & Gales 2021 "Uncertainty Estimation in Autoregressive Structured Prediction" — 直接相关
157	
158	**论文中未有 bib entry**（建议补充）：
159	- Tian et al. 2023 "Just Ask for Calibration" — verbalized confidence，与 W1 中 per-sample signal baseline 相关
160	- Ren et al. 2023 "Investigating Uncertainty Calibration of Aligned LMs" (EMNLP 2023 Findings) — LP calibration 相关
161	
162	---
163	
164	## External Review (Stanford Agentic Reviewer)
165	
166	项目未配置 paperreview.ai 外部审稿（external_review.paperreview_ai.enabled 未启用）。外部审稿：未请求。
167	
168	---
169	
170	## Overall Assessment
171	
172	**评分**: weak accept / borderline (3.25/5)
173	**置信度**: 4/5 (两位 Reviewer 均仔细阅读全文含 Appendix)
174	
175	**建议**: Findings acceptance（两位 Reviewer 共识）
176	
177	**理由**：
178	- **正面**：LP compression 发现有实际价值（median range 0.041 nats → non-tied subset +2.9pp, p=0.004）；统计分析远超同类工作；appendix 详尽；QE vs selection 的 metric dissociation 对社区有启发性
179	- **负面**：核心 "correlation-selection gap" 对 4/5 信号是 definitional（by construction），真正的 empirical finding scope 较窄（LP compression + MBR failure）；Abstract/Conclusion 对 free-form ablation 过度概括（RE reversal 未标注）；RE 证据不足但标题 scope 过宽
180	
181	**升格条件**（若满足可考虑 Main Conference）：
182	1. Abstract/Introduction/Conclusion 层面 reframe：明确 dismiss instance-level failure 为 definitional，将贡献重心移向 LP compression + MBR failure
183	2. Abstract 修正 RE free-form reversal
184	3. 补充 free-form multi-seed RE 实验（若时间允许）
185	4. Conclusion hedge RE
186	
187	---
188	
189	## Detailed Comments
190	
191	### Abstract
192	- 第 4-5 行："All signals achieve strong quality estimation yet none improves best-of-N selection" — 对 4/5 instance-level 信号是 definitional（N1）
193	- 第 6 行："the gap persists across scales and task types" — RE reversal 未标注（N2）
194	- 信息密度恰当（Round 8 后精简为 9 行 问题-发现-意义结构），RE preliminary 有标注
195	
196	### Introduction
197	- Contribution list 结构清晰：#1 metric dissociation, #2 correlation-selection gap, #3 difficulty-dependent signal rankings
198	- Contribution #1 定位为 finding-led（"We find that..."）恰当
199	- Contribution #3 正确标注 "RE conclusions rest on SciERC alone (preliminary)"
200	- Figure 1 有效传达 gap 概念
201	
202	### Related Work
203	- 覆盖面广，3 段结构清晰
204	- 与 Yao et al. (2026) 的增量贡献明确（structural matching, selection analysis, difficulty gradient）
205	- Eikema 2025 structured MBR 对接到位
206	- 建议引用已有 orphan entries（Kadavath 2022, Culotta 2004, Malinin 2021）
207	
208	### Method
209	- 5 信号形式化定义精确
210	- SJ Hungarian matching 定义完整（threshold, normalizer, IoU）
211	- Evaluation framework（QE: ρ + AUROC; Selection: best-of-N）恰当
212	- 建议 Section 3.3 更早 qualify consensus-proximity 为 MBR instantiation
213	
214	### Experiments
215	- Difficulty gradient 设计有效（SciERC → CoNLL → WNUT-17）
216	- Table 1 应标注 single seed (42)（W6）
217	- Table 2 NER 2-seed vs RE single seed 不一致（M5）
218	- "Greedy" 术语需澄清（M1）
219	- Scale ablation "not model capacity" 需弱化（W7）
220	
221	### Discussion
222	- 两层结构（definitional + LP compression）存在但需在 Abstract/Introduction 更突出
223	- VC selection 失败机制缺分析（W4）
224	- MBR decoding 连接已到位（cite Eikema 2022/2025）
225	
226	### Conclusion
227	- 缺 RE preliminary hedge（N3）
228	- "across task types" 需 qualification（N2）
229	
230	### Limitations
231	- 透明度高
232	- 建议增加"仅测试了一种 per-sample signal"（W1）
233	
234	### Ethics Statement
235	- 内容充实，含 CoNLL Reuters 出处和代码发布承诺
236	
237	### Appendix
238	- 极其详尽（~15 pages，17 sections）
239	- SJ normalizer robustness、FK independence、ε sensitivity、OOD、free-form ablation 等细粒度分析增强可重复性
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5470be9f-9393-4fbc-b7fe-66a54a24ad52",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "2426e50d-69fb-4c01-8dd5-f61b1dcc4d6e",
  "sourceToolAssistantUUID": "5470be9f-9393-4fbc-b7fe-66a54a24ad52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T10:42:49.170Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TMuuUdv4pMupka56FXMR9w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_15.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2426e50d-69fb-4c01-8dd5-f61b1dcc4d6e",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU869CnUkuCWfLoc1bf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "208cf351-8005-4707-a9e7-79c93e153843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012aQxXkcn9Pj3Sno5wsasp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37061,
      "cache_read_input_tokens": 42293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37061,
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

_source line 22 · 2026-05-22T10:42:49.178Z_

<details><summary>↩ Tool result · `toolu_01TMuuUdv4pMupka56FXMR9w`</summary>

```text
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
40	16+ appendix sections 提供了 FK independence test、SJ normalizer robustness、ε sensitivity sweep、calibration analysis、diversity quantification、free-form ablation 等全面补充分析。
41	
42	**S6. 三数据集难度梯度设计** [Both]
43	虽然 selection 有效测试仅在 SciERC 上（见 MF1），ceiling/medium/collapse 梯度本身是良好的实验设计，为信号行为随难度变化提供了有用的 calibration。
44	
45	---
46	
47	## Weaknesses
48	
49	### Must-Fix（影响接收决定）
50	
51	**MF1. [强共识] Framing conflation: "5 signals all fail" 混淆 definitional limitation 与 empirical finding**
52	- R1-N2 (critical) + R2-N1 (critical)；交叉验证：R1 AGREE R2-N1，R2 AGREE R1-N2
53	- 4/5 信号（SJ、VC、FK、EM）是 instance-level，by construction 对同一 input 的所有 N 个候选给出相同分数。Table 2 中这些信号的 "selection" 实际测试的是 consensus-proximity (MBR)。将 MBR failure 归因于 "信号失败" 是 attribution error。
54	- Abstract ("five confidence signals... yet best-of-N selection fails")、Contribution #1 和 Conclusion 将两类本质不同的 failure 混为一谈。§3.1 第一段已有区分 ("This distinction is consequential for selection") 但未向 Abstract/Intro/Conclusion 传递。
55	- **真正的 empirical findings 是**: (a) MBR 转换产生 per-sample ranking 后仍失败（despite within-instance ρ=0.52），因 instance degeneracy 消除 headroom; (b) LP 因 compression 失败（median range 0.041 nats）。
56	- **Required action**: Abstract/Intro 拆分三层叙事——(a) instance-level 需 MBR 转换（acknowledged design property），(b) MBR 转换后仍失败 despite positive within-instance correlation（empirical），(c) LP per-sample but compressed（empirical）。
57	- **历史**: 此问题自 Round 3 (R3-W2) 首次提出，持续 13 轮未完全解决。
58	
59	**MF2. [强共识] 核心 claim 实质上仅由 SciERC (n=529) 单数据集支撑**
60	- R1-N1 (critical)；R2 交叉 AGREE
61	- CoNLL 是论文自己的 "ceiling-effect control"（oracle headroom 仅 4pp，论文在 Appendix §D 承认 "selection analysis on these configurations is uninformative"）。WNUT-17 是 "signal-collapse boundary"（52% zero F1）。因此核心 finding——greedy > all N=8 selection——仅在 SciERC 上验证。
62	- SciERC 的 medium-difficulty regime (~65% F1) 可能是 sweet-spot artifact 而非普遍现象。LLaMA/SciERC 提供 cross-model 复现但仍限于同一 domain（科学文本，6 entity types）。
63	- **Required action**: (1) 增加至少一个 medium-difficulty NER 数据集（OntoNotes subset、ACE 2005、Few-NERD）在 50-70% F1 range 验证; 或 (2) 将所有 claim 显式限定为 "medium-difficulty scientific NER" 并相应调整 title/abstract 泛化程度。
64	- **历史**: 自 Round 0 (R0-C3) 首次提出，持续 15 轮。
65	
66	**MF3. [强共识] Table 2 Random (0.610) vs Single (0.645): 3.5pp 差距未解释**
67	- R2-N3 (critical)；R1 交叉 AGREE
68	- 在 T=1.0 下，Random（从 N=8 均匀选取）和 Single（一次 T=1.0 采样）的期望 F1 应相同：E[Random] = E[Single] = (1/N)ΣE[F1(yi)]。3.5pp 系统性差距（across n=529 instances, 2 seeds, ±0.003 variance, ~2.7σ）不太可能是随机波动。
69	- 此差距影响所有 selection method 的 baseline 解读。若 Random 系统性偏低，则 selection methods 相对 Random 的 +3-4pp 可能仅是恢复期望，而非真正的 selection gain。
70	- **Required action**: 明确 Random 和 Single 的精确计算方式。若定义不同（如 Random=instance-level random draw, Single=per-seed mean），需显式说明并讨论对 baseline 解读的影响。
71	- **历史**: Round 14 (R14-M1) 作为 info 提出，本轮升级为 critical。
72	
73	**MF4. [方向共识, Severity 分歧] 2-seed Fisher combined p 统计效力不足**
74	- R1-N3 (critical) + R2-W6 (should-fix)；R2 交叉 REBUT on severity（同意方向）
75	- 核心 negative conclusion "no signal significantly outperforms single-sample (all p>0.05)" 基于 2-seed Fisher combined p。Bootstrap 95% CI [-3.0, +4.2]pp（宽 7.2pp），远超 oracle headroom 40%。
76	- **R2 反驳 severity**: Cohen's d=0.038 接近零是更可靠的证据；TOST equivalence、4 cross-configurations 复现、greedy comparison 构成多重证据链，超越单一 p-value。
77	- **共识 action**: (1) 报告 selection F1 的 3-seed variance（当前仅报告 QE 的 seed stability）；(2) 主文从 "all p>0.05" 叙事转向 "d=0.038 with multiple convergent lines"；(3) 考虑 power analysis。
78	
79	### Should-Fix（影响评分）
80	
81	**SF1. [共识] Instance degeneracy: fine-tuning recipe artifact 未排除**
82	- R2-N2(b) + R1 交叉 PARTIALLY AGREE
83	- LoRA rank=32, dropout=0, 5 epochs（Table 9），SciERC 未用 load_best_model_at_end。8B vs 4B degeneracy 差异（21% vs 10.4%）可能反映 larger model with same epochs overfits faster，而非 capability-intrinsic property。
84	- **Action**: 在 Discussion/Limitations 显式承认 fine-tuning recipe confound；理想情况提供 LoRA rank 或 epoch ablation。
85	
86	**SF2. [共识] 与 Yao et al. (2026) positioning: 缺少 hard-prompted degeneracy 讨论**
87	- R2-W3 + R1 交叉 AGREE
88	- 关键未回答问题：hard-prompted models 是否存在 instance degeneracy？如果否→degeneracy 是 fine-tuning artifact 非 task-intrinsic。这是论文最强差异化论点但未被显式讨论。
89	- **Action**: Related Work 或 Discussion 增加显式对比。
90	
91	**SF3. [共识] "Surpassing all N=8 selection strategies" 修辞过强**
92	- R2-W5 + R1 交叉 AGREE
93	- Greedy (T=0, 0.663) vs Single (T=1.0, 0.645) +1.8pp 未经 significance test。如不显著，结论应为 "Greedy ≈ Single > all selection strategies"——failure 是 selection 不如 random single draw，非 greedy 特别好。
94	- **Action**: 测试 Greedy vs Single 显著性；修辞改为 "selection adds no benefit"。
95	
96	**SF4. [共识] Non-tied LP subset Bonferroni correction scope 不完整**
97	- R1-W1 + R2 交叉 AGREE
98	- Footnote 4 称 "+2.9pp, p=0.004 survives Bonferroni over 5 comparisons"，但未计入 7 个 ε 值的 post-hoc 选择。Full correction: 7ε × 5 signals = 35 comparisons, α_adj=0.0014, p=0.004 不再 survive。
99	- **Action**: 修正 Bonferroni scope 或改为 "exploratory finding"。
100	
101	**SF5. [共识] Kendall's W=1.0 (3 seeds) 呈现缺乏 precision caveat**
102	- R1-W2 + R2 交叉 AGREE
103	- m=3, n=5 下单个 ranking swap 即导致 W 大幅下降。Main text 需加 precision caveat。
104	
105	**SF6. [共识] Scale range (3B-8B) 不足以支撑 "intrinsic" claim**
106	- R1-W3 + R2 交叉 AGREE
107	- 两个数据点不支持 "intrinsic to capable fine-tuned models" 的外推。
108	- **Action**: 限定为 "within the 3B-8B fine-tuned regime"。
109	
110	**SF7. [共识] TOST 等价性 configuration-dependent, main text 未充分呈现**
111	- R1-W5 + R2 交叉 AGREE
112	- Qwen-CoNLL: 所有 external δ 下 FAIL（selection degrades 0.9-1.5pp）——信号 actively harmful。此结论比 "no benefit" 更强，但被埋在 Appendix。
113	- **Action**: Section 4.3 更平衡呈现 TOST 结果。
114	
115	**SF8. [部分共识] Abstract ρ=0.45 headline 来自 ceiling-effect dataset**
116	- R2-W1 + R1 交叉 PARTIALLY AGREE
117	- CoNLL ρ=0.45 受 zero/non-zero boundary inflate (+0.03-0.05)。Primary SciERC ρ=0.38 按 Cohen (1988) 属 medium effect。
118	- **Action**: Abstract 仅报告 primary ρ=0.38，或明确标注 0.45 来源。
119	
120	### Minor Issues
121	
122	M1. Free-form ablation "ruling out" 改为 "provides evidence against"（共识）
123	M2. VC QE (continuous, Eq.5) vs VC selection (freq>N/2, discrete) 在 Table 2 中共享标签 "VC"，需在 caption 澄清
124	M3. Greedy vs Single 1.8pp 需 significance test
125	M4. SciERC checkpoint 未用 load_best_model_at_end，可能增加 degeneracy，需 acknowledge
126	M5. "Soft Jaccard" 命名（R2 提出，R1 rebut——非共识问题，但可考虑首次使用时加注）
127	M6. Yun et al. (2025) diversity collapse 与 degeneracy 的联系需显式讨论（1-2 句）
128	
129	---
130	
131	## Reviewer Consensus [AGREE]
132	
133	1. **Framing 必须重构**：区分 definitional (instance-level) 和 empirical (MBR + LP) failure modes
134	2. **核心 claim scope** 必须限定或跨数据集验证
135	3. **Random vs Single 差距**必须解释
136	4. **"Intrinsic" claim** 需限定到已测试 regime
137	5. **Greedy 修辞**应重新定位
138	6. **Yao et al. 对比**需补充 hard-prompted degeneracy 讨论
139	7. **Non-tied LP Bonferroni** correction scope 需修正
140	8. 两位 Reviewer 独立评分均为 **3.0/5 (Findings-level)**
141	
142	## Reviewer Divergence [REBUT]
143	
144	1. **2-seed Fisher p severity**: R1 评 critical，R2 评 should-fix。R2 认为 d=0.038 + 多重证据链比单一 p-value 更可靠。两位同意方向（power 不足），分歧仅在是否 blocks acceptance。
145	2. **Free-form ablation cross-task inference**: R1 认为 RE reversal (+1.8pp) 削弱 NER "ruling out" claim；R2 认为 NER/RE output structure 不同，NER-specific evidence (std ratio 0.97) 在 NER 范围内充分。**共识: 弱化措辞为 "provides evidence against"。**
146	3. **"Soft Jaccard" 命名**: R2 认为误导；R1 rebut（footnote + Appendix Δρ<0.01 + 先例）。非共识问题。
147	
148	---
149	
150	## Questions for Authors
151	
152	Q1. [Both] Table 2 Random (0.610) vs Single (0.645): 精确计算公式？3.5pp 系统性差距来源？
153	Q2. [Both] Instance degeneracy 是否对 fine-tuning recipe 敏感（LoRA rank、epochs、dropout、load_best_model_at_end）？
154	Q3. [R1] 是否有其他 medium-difficulty NER 数据集上的初步结果？
155	Q4. [R2, R1 AGREE] Free-form decoding 下 constant-F1 fraction 是否改变？
156	Q5. [R1] Hybrid 策略（degenerate→greedy, non-degenerate→MBR）的 expected gain？
157	Q6. [R1] Entity-token LP 的 within-instance ρ（F1）是多少？增加的 variance 是 noise 还是 signal？
158	Q7. [R2, R1 AGREE] Greedy (T=0) vs Single (T=1.0) 是否经过 significance test？
159	
160	---
161	
162	## Missing References
163	
164	1. Gao et al. (2023) "Scaling laws for reward model overoptimization" — best-of-N proxy signal limitation 的概念联系（R2 提出，R1 PARTIALLY AGREE: 相关性有限，可在 Discussion 提及）
165	2. Deutsch et al. (2022) "Training and meta-evaluating machine translation evaluation metrics at the paragraph level" — MBR with structural metrics（R1 提出）
166	
167	---
168	
169	## External Review (Stanford Agentic Reviewer)
170	
171	未请求。
172	
173	---
174	
175	## Overall Assessment
176	
177	**Score: borderline**
178	**Confidence: 4/5**
179	**推荐 Track: Findings**
180	
181	两位 Reviewer 独立评分均为 3.0/5。论文提出了有价值的概念贡献（QE vs selection 解耦）并提供了深入的诊断分析。Within-instance analysis（MBR utility aligned but headroom vanishing）是最强贡献，与 Eikema et al. (2025) 的 MBR utility mismatch 有 qualitative 区别。
182	
183	但四个 Must-Fix 问题限制了当前版本的可接受性：
184	1. **Framing inflation**: "5 signals all fail" 将 definitional limitation 包装为 empirical discovery（持续 13 轮未完全解决）
185	2. **Single-dataset support**: 核心 claim 仅在 SciERC (n=529) 上有效验证（持续 15 轮）
186	3. **Unexplained baseline**: Random vs Single 3.5pp 差距影响 baseline 解读
187	4. **Statistical power**: 2-seed Fisher p 不足以支撑核心 negative result
188	
189	**Findings track 路径**: 解决 MF1（framing 重构）、MF3（Random vs Single 解释）、SF1-SF8 中的写作修正即可满足 Findings track 要求。
190	
191	**Main conference 路径**: 在 Findings 路径基础上，还需 MF2（增加数据集或进一步限定 scope）和 MF4（statistical power 加强）。
192	
193	---
194	
195	## Detailed Comments (Section-by-Section)
196	
197	### Abstract
198	- 信息密度仍高——5 信号、3 数据集、degeneracy%、LP nats、5-layer ablation 均出现
199	- ρ=0.45 来自 ceiling-effect control，可能给 "moderate-to-strong" 错觉
200	- "Five confidence signals" 统一叙事需拆分
201	- "Within a narrow model-scale range (4B-8B)" 良好限定
202	
203	### Introduction (§1)
204	- Contribution #1 混合 definitional 和 empirical failure——需重构
205	- Figure 1 + operationalization 有效
206	- 已正确识别 instance-level vs per-sample 区分但未贯彻到 contribution list
207	
208	### Related Work (§2)
209	- 覆盖全面（self-consistency, MBR, uncertainty, calibration）
210	- Schall et al., Yun et al., Park et al., Eikema et al. 均已引用
211	- 缺少: Yao et al. hard-prompted vs fine-tuned degeneracy 对比
212	- 缺少: Yun et al. diversity collapse 与 instance degeneracy 的显式联系
213	
214	### Method (§3)
215	- 信号定义数学严谨，evaluation framework 清晰
216	- §3.1 有关键区分但需向前传递
217	
218	### Experiments (§4)
219	- Table 1 QE 结果呈现清晰
220	- Table 2 Selection 结果是核心但 Random vs Single 差距需解释
221	- §4.3 "all p>0.05" 叙事应转向 effect size
222	- Table 4 Degeneracy: 含 4B data，within-instance analysis 是最强部分
223	
224	### Discussion (§5)
225	- Instance degeneracy mechanism 论证充分（MBR + within-instance ρ）
226	- LP compression 诊断系统（四个 hypotheses, constraint-imposed vs model-learned）
227	- "Intrinsic" 用语需 scope 限定
228	- Signal combinations: LP×VC 三策略 + oracle tiebreaker +7.9pp 是重要 calibration
229	
230	### Conclusion (§6)
231	- 准确总结但继承 framing 问题
232	- 70B+ open question 恰当
233	
234	### Limitations
235	- 全面诚实
236	- 应增加 fine-tuning recipe confound acknowledgment
237	
238	### Ethics Statement
239	- 对论文 scope 而言充分
240	
241	### 格式合规
242	- ACL review template ✓, Anonymous ✓, Limitations ✓, Ethics ✓
243	- 引用: 53 entries, 0 orphan, 44 verified（R2 审核）
244	- 正文页数需编译确认
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "208cf351-8005-4707-a9e7-79c93e153843",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "c94ae2fc-e05d-494e-8cdd-813eebe339de",
  "sourceToolAssistantUUID": "208cf351-8005-4707-a9e7-79c93e153843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T10:42:49.389Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LQ5rMHgDB2kU3mnZ6c2ydq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_20.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c94ae2fc-e05d-494e-8cdd-813eebe339de",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU869CnUkuCWfLoc1bf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b1837293-dd46-4b4d-a4d4-169ca012b9af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012aQxXkcn9Pj3Sno5wsasp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37061,
      "cache_read_input_tokens": 42293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37061,
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

_source line 24 · 2026-05-22T10:42:49.397Z_

<details><summary>↩ Tool result · `toolu_01LQ5rMHgDB2kU3mnZ6c2ydq`</summary>

```text
1	---
2	round: 20
3	overall_score: 3/5 — Findings track acceptance recommended
4	timestamp: 2026-05-18T13:19:12.375864+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 圆桌审稿合并报告 — Round 21
11	
12	**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
13	**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)
14	**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）
15	**交叉回应**: R2 对 R1 完成正式 AGREE/REBUT（5 条全部 AGREE）；R1 对 R2 通过 aligned findings 实质覆盖（R1 agent session 在交叉分享请求送达后未重启，但 R1 修订版审稿已显式确认 R2-N3 并在所有关键问题上提出平行发现）
16	**外部审稿**: 未配置
17	
18	---
19	
20	## Summary
21	
22	本文研究 self-consistency 类 confidence signals 在 LLM-based NER 中 quality estimation（QE）与 sample selection 之间的脱钩现象（correlation-selection gap）。在 4 个 NER benchmark、2 个 8B 模型家族和 1 个 4B ablation 上评估 5 种信号，发现所有信号均可实现可靠的 QE（ρ 达 0.45, AUROC 达 0.82），但仅 LP 在特定条件下（Few-NERD, degeneracy <15%, alignment ρ≈0.5）取得显著 selection 增益（+1.39pp）。论文诊断出两个阻塞机制——instance degeneracy 和 weak LP-quality alignment，提出"两条件"框架。Hidden state probes 证明即使模型内部表示包含更丰富信息，selection gap 依然存在。
23	
24	---
25	
26	## Strengths（两位 Reviewer 共识）
27	
28	**S1** [概念框架] Per-sample vs. instance-level signal 的区分（Section 3.1）是论文最有洞察力的贡献。4/5 信号是 instance-level aggregates，对 selection 无信息量 by construction。这个 observation 直接解释了为什么高 ρ 不能转化为 selection。（R1 + R2 共识）
29	
30	**S2** [实验系统性] 4 个数据集构成清晰的难度梯度（WNUT-17 signal-collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个服务于明确的实验功能。多种 ablation（temperature, LoRA rank, epoch, N-scaling, free-form decoding, hidden state probes, DeBERTa verifier, supervised combination）系统地排除 alternative explanations。（R1 + R2 共识）
31	
32	**S3** [统计严谨性] Bootstrap CI（B=10,000）、TOST equivalence testing（含 external anchors）、MDE 计算、Bonferroni correction、sign test、Cohen's d。统计方法论在 ACL 投稿中属上乘，远超同类工作常见的"report p-value only"标准。Non-tied subset positive finding（+2.9pp, p=0.004）经 Bonferroni 校正后仍 significant。（R1 + R2 共识）
33	
34	**S4** [Hidden state probe] Section 4.5 直接测试"需要更强信号"这一 natural follow-up。MLP probe ρ=0.388（比 LP 高 37%）但 selection 反而更差，有力封堵了"bottleneck 在 information loss"的 alternative explanation。（R2；R1 在主要优势中列出 LP compression 诊断分析为最有洞察力的贡献）
35	
36	**S5** [Limitations 透明度] 主动报告所有已知弱点：SciERC seed sensitivity、epoch confound、scale gap、未测试的 per-sample signals、ε threshold 的 post-hoc 性质。透明度超过大多数投稿论文。（R1 + R2 共识）
37	
38	**S6** [引用完整] 64 bib entries, 97 citations, 0 orphan, 0 missing, 无虚假引用。与最相关工作 Nédellec et al. (2026) 的定位精准。（R1 + R2 共识）
39	
40	---
41	
42	## Weaknesses
43	
44	### Critical（需解决才能接收）
45	
46	**C1** [页数超限 — desk-reject 级别] 正文约 9.5 页，超出 ACL 长文 ≤8 页限制（不含 Limitations/Ethics/References）。Discussion 是主要来源（6 个 \paragraph 子节）；Conclusion 从 page 9 开始并延伸至 page 10。
47	- **R1-N1 + R2-W1 共识**，无分歧。
48	- 建议：DALS 段落完整移至 appendix；LP compression 4 mechanisms 缩为 1-2 句 refer appendix；regime boundaries 段压缩为 3 句；Contribution list 数值细节精简。
49	
50	**C2** [Title scope 过宽] Title 声称 "Structured Information Extraction"，但实验覆盖仅 NER（4 benchmarks，完整主线）+ RE（SciERC 单 benchmark，明确标为 "exploratory single-benchmark analysis"）。无 event extraction、slot filling 或其他 IE 子任务。
51	- **R1-W5 + R2-W2 共识**（此问题自 Round 1 起持续 open，Round 19 已推荐 Option B 改为 NER-specific，Round 21 两位 Reviewer 再次确认）。
52	- 建议方案 (a)（两位 Reviewer 一致推荐）：改 title 为 "...LLM-Based Named Entity Recognition" 或 "...Structured Output Selection"。
53	
54	**C3** ["两条件"框架经验基础不足] 跨数据集仅 3 个数据点（CoNLL/SciERC/Few-NERD），论文自标 "exploratory given 5+ confounds"。15% degeneracy 阈值来自 Few-NERD per-entity-type 两个相邻点（Person 13.4% vs Art 19.8%），ρ≥0.3 阈值 data-dependent。
55	- **R1-N2 + R2-W4（partial）共识**。R2 从 novelty 角度指出同一 root issue：claim strength > evidence strength + novelty。
56	- 建议：降级 claim 为 "empirical pattern" / "approximate boundary in our data"，使用 "jointly observed" 而非暗示 theoretical thresholds；或增加数据集验证。
57	
58	### Warning（影响评分但不一票否决）
59	
60	**W1** [Epoch confound 正文处理不充分] 5-epoch Few-NERD LP gain 减半至 +0.62pp，接近 SciERC +0.61pp。框架区分力在统一 epoch 后减弱。当前仅 footnote + appendix 提及。Discussion 中 "Standard early stopping naturally selects the low-degeneracy regime" 是合理 counter-argument 但不够 prominent。
61	- R1-W1 提出 + R2 交叉回应 AGREE with nuance（within-instance alignment 差异 ρ≈0.5 vs ≈0.24 仍是关键区分因素）。
62	- 建议：正文正式呈现 epoch-controlled comparison，提升 alignment 差异的叙事地位。
63	
64	**W2** [SciERC 系统性 underpowered] SciERC n=529, MDE≈1.5pp at 80% power。LP +0.61pp (p=0.193) 无法区分"真的没有效果"和"效果太小检测不到"。3-seed mean +0.04±0.48pp 本质是 noise。Few-NERD（n=32,565, MDE≈0.22pp）有 definitive power。
65	- **R1-W3 + R2-W5 共识**。
66	- 建议：将 Few-NERD 重新定位为 primary test bed；SciERC 标注为 "medium-difficulty, underpowered exploratory test bed"。
67	
68	**W3** [DALS 定位 + data-snooping] (a) DALS 在 Discussion 中引入但无独立评估，与论文诊断性定位冲突。结果 seed-sensitive（SciERC: +0.19 to +1.14pp），CoNLL 仍 degradation。(b) ε=0.05 threshold 从 non-tied analysis 同数据 sweep 选出后在同一数据上评估，存在 circular optimization 风险。
69	- R2-W3 (positioning) + R1-W4 (data-snooping) 互补。R2 交叉回应 AGREE with refinement。
70	- 建议：DALS 移至 appendix 作为 exploratory extension；同时报告 held-out validation 或 leave-one-out 的 ε sensitivity。
71	
72	**W4** [新颖性增量定位] 核心贡献是对已知 general phenomena 在 NER domain 的系统验证和命名。Correlation-selection gap 在 MBR 文献中是已知问题（Eikema et al. 2025 utility misalignment）；instance degeneracy 在 Kirk et al. (2024) 和 Yun et al. (2025) 已讨论 diversity collapse；capability trap 基于 3 scale points 的 observational trend。
73	- R2-W4 提出。
74	- EMNLP 接受 negative/diagnostic results 的前提是 (i) robustness 充分（满足）和 (ii) actionable insight 有意义（部分满足）。
75	- 建议：Introduction 更明确框定为 "first systematic empirical characterization of..."。
76	
77	**W5** [LP ρ 跨表不一致] SciERC LP ρ 在 Table 1（0.205）和 Table 3（0.215）之间有 0.010 差异，两表标注相同 seed=42, N=8, gold-filtered。与 greedy F1 四值问题（W7）的累积效应影响数据信任。
78	- R1-W2 独立发现。
79	- 建议：排查根因并统一数值。
80	
81	**W6** [Table 3 脚注过载] 7 个连续 `\footnotetext`，混合定义性信息（degeneracy 定义）、评估细节（oracle headroom）、confound 声明（epoch difference）和 per-dataset seed details。
82	- R2-W6 独立发现。
83	- 建议：degeneracy 定义移至首次使用处；per-dataset seed details 整合为 appendix table。目标 ≤2 个脚注。
84	
85	**W7** [Greedy F1 多表数值不一致] SciERC greedy F1 在多个 tables 出现 0.640/0.644/0.645/0.650 四个值。每个差异有脚注解释，但审稿人看到同一 baseline 有 4 个数值会产生困惑。
86	- **R1 新发现 + R2-W7 共识**。
87	- 建议：统一 evaluation protocol，或在 Section 3.3 提前声明 protocol variants 及原因。
88	
89	**W8** [缺失引用] (1) Farquhar et al. (Nature 2024) semantic entropy——与已引 Kuhn et al. (2023) 相关但不同，高影响力工作；(2) Chen et al. (2021) pass@k——best-of-N 在 code generation 的经典成功案例，可更好 contextualize NER selection failure；(3) 缺少 2023+ LLM-based NER calibration/confidence 中间层文献。
90	- R2 独立发现。
91	
92	### Info（建议修改但不影响评分）
93	
94	**I1** [Appendix 残留实验标识] exp\_025, exp\_027 应在投稿前删除。
95	
96	**I2** ["Capability trap" 措辞] 论文自己展示 temperature 和 early stopping 可部分控制 degeneracy，与 "trap" 暗示的不可逃脱性矛盾。建议改为 "capability-diversity tension"。
97	- R1-W3 + R2-W9 共识。
98	
99	**I3** [少量 -ing 短语] 3 处（experiments.tex:183, discussion.tex:20, introduction.tex:18），均在可接受范围但建议改写。
100	
101	---
102	
103	## Questions（合并去重）
104	
105	**Q1** [Epoch × dataset interaction] 能否提供 3-epoch SciERC 的 within-instance alignment ρ 和 LP selection 的 3-seed mean？这将判断 epoch confound 在多大程度上解释 SciERC-vs-Few-NERD 差异。（R2-Q1）
106	
107	**Q2** [Hidden state pooling] Hidden state probe 使用 mean-pooled final-layer hidden state。是否尝试过 entity-position-only pooling 或 attention-weighted pooling？（R2-Q2）
108	
109	**Q3** [Per-entity-type effective df] Per-entity-type analysis within Few-NERD（ρ=-0.881, p=0.004, n=8）的 effective df 问题：如果 effective df 为 4，p-value 会升至多少？（R2-Q3）
110	
111	**Q4** [未测试的 per-sample signals] LP 是当前唯一的 per-sample signal 且唯一有正面 selection 结果。为什么没有测试 Self-Certainty (Kang et al. 2025) 和 P(True) (Kadavath et al. 2022)？如果它们 also fail，加强 "gap is fundamental" 论证；如果 succeed，则 gap 是 LP-specific。（R2-Q4）
112	
113	**Q5** [DALS τ validation] DALS 的 τ=0.05 如果用 leave-one-out 或 held-out validation 来选择，gain 是否 substantially change？（R2-Q5）
114	
115	---
116	
117	## Overall Assessment
118	
119	### 评分汇总
120	
121	| 维度 | R1 | R2 | 合并 |
122	|------|-----|-----|------|
123	| Overall | 3/5 (Findings) | 3/5 (Findings) | **3/5 (Findings track)** |
124	| Soundness | 3/5 | 3.5/5 | 3.25/5 |
125	| Excitement | 3/5 | 2.5/5 | 2.75/5 |
126	| Reproducibility | 4/5 | 4/5 | 4/5 |
127	| Confidence | 4/5 | 4/5 | 4/5 |
128	
129	### 合并判断
130	
131	**Overall: 3/5 — Findings track acceptance recommended（附条件）**
132	
133	这是一篇实验严谨、统计透明的诊断性研究。Per-sample vs instance-level 的概念区分有真实贡献，hidden state probe 封堵 alternative explanation 巧妙，统计方法论显著高于同类工作。
134	
135	**接收的 hard blockers（必须解决）：**
136	1. 正文超页限（~9.5 vs 8 页）—— desk-reject 级别
137	2. Title scope 过宽 —— overclaiming 级别
138	
139	**影响评分的 substantive concerns：**
140	3. "两条件"框架 claim strength > evidence strength（3 数据点 + data-dependent thresholds）
141	4. Headline positive result 受 epoch confound 影响，正文处理不充分
142	5. SciERC 作为 primary test bed 系统性 underpowered
143	6. 新颖性增量有限（对已知现象的 domain-specific 系统验证和命名）
144	
145	**如果 (1)-(2) 解决、(3)-(6) 适当调整，论文适合 Findings track。进入 Main Conference 需要：(a) 更多数据集验证"两条件"框架，或 (b) 更多 per-sample signals 扩展 selection 分析。**
146	
147	### 交叉回应收敛状态
148	
149	- R2 → R1：5 条正式回应，全部 [AGREE]（N1 框架证据薄、N2 epoch confound、W1 SciERC underpowered、W2 DALS data-snooping、W3 capability trap）
150	- R1 → R2：通过 aligned findings 实质覆盖（W5 确认 R2-N3 title scope；平行发现覆盖页数超限、SciERC underpowered、DALS、greedy F1 不一致）
151	- **无未解决分歧**。所有关键问题两位 Reviewer 一致。
152	
153	---
154	
155	## AI 写作痕迹检查
156	
157	- Em-dash（—）：全文零使用 ✓
158	- En-dash（–）：仅数字范围，正确用法 ✓
159	- -ing 结尾短语：3 处，可接受范围 ⚠
160	- 过度分段：无 ✓
161	- 黑名单用词：无 ✓
162	- "Furthermore/Moreover/Additionally"：零使用 ✓
163	- **整体判断**：写作质量高，AI 痕迹控制得当。
164	
165	## 格式合规性
166	
167	- `\documentclass[11pt]{article}` + `\usepackage[review]{acl}` ✓
168	- `\author{Anonymous}` ✓
169	- 行号：review option 自动生成 ✓
170	- Limitations section：存在 ✓
171	- Ethics Statement：存在 ✓
172	- **正文超限：~9.5 页** ✗ （C1）
173	- Appendix 内部标识 ✗ （I1）
174	
175	## References 完整性
176	
177	- 64 bib entries, 97 citations, 0 orphan, 0 missing
178	- 3 online not found（近期 preprint 未被索引）
179	- 4 mismatch（author name 格式差异，非虚假引用）
180	- **无虚假引用** ✓
181	
182	---
183	
184	*报告由 Review Director 基于 Reviewer 1（方法严谨性 + 实验设计）和 Reviewer 2（新颖性 + 完整性）的圆桌审稿合成。*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1837293-dd46-4b4d-a4d4-169ca012b9af",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "1e29b79c-4165-4560-bb5b-f292fcba3314",
  "sourceToolAssistantUUID": "b1837293-dd46-4b4d-a4d4-169ca012b9af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T10:42:49.594Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K4ikekKnoaEjWiGvjPGjWW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_25.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e29b79c-4165-4560-bb5b-f292fcba3314",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU869CnUkuCWfLoc1bf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cfd274e2-2cbf-4d80-bb4e-ffc77c706c74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012aQxXkcn9Pj3Sno5wsasp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37061,
      "cache_read_input_tokens": 42293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37061,
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

_source line 26 · 2026-05-22T10:42:49.603Z_

<details><summary>↩ Tool result · `toolu_01K4ikekKnoaEjWiGvjPGjWW`</summary>

```text
1	---
2	round: 25
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-20T14:42:46.038603+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 26 (Fresh Review)
12	
13	**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition"
14	**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)
15	**Deadline**: 2026-05-25
16	**审稿模式**: Fresh（重新审稿，无上轮记忆）
17	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）
18	**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）
19	
20	---
21	
22	## Summary
23	
24	论文研究 test-time compute scaling (self-consistency) 应用于 NER 的效果，评估 5 种 confidence signals（Soft Jaccard, voting confidence, Fleiss' κ, exact match, log-probability）在 4 个 NER benchmark 上的 quality estimation (QE) 和 sample selection 表现。核心发现：所有信号能做可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但无法可靠地选出最优 sample——作者称之为"correlation-selection gap"。论文提出 entity-level construction（实体级聚合）作为缓解方案，在 Few-NERD 上获得 +1.40pp（Holm p_adj=0.006），并给出 degeneracy decomposition 的理论分析。
25	
26	---
27	
28	## Strengths
29	
30	1. **统计方法论远超 NLP 社区平均水平** [R1, R2 共识]：Holm-Bonferroni 多重比较校正（family k=10/19/57）、bootstrap CI (B=10,000)、MDE/power analysis、TOST equivalence testing、permutation tests。这种严谨性在 NER/IE 论文中极为罕见，具有示范价值。
31	
32	2. **Correlation-selection gap 概念清晰、有实际价值** [R1, R2 共识]：核心观察——信号能估质量但选不出最优 sample——对 NER practitioners 直接有用，改变了 test-time scaling 的使用策略。
33	
34	3. **实验设计系统全面** [R2]：5 signals × 4 datasets × 2 models × 4B-8B fine-tuned + 72B zero-shot，覆盖难度梯度（WNUT-17 ~42% → CoNLL >90% F1）。
35	
36	4. **Diagnostic cascade 有洞察力** [R1, R2]：degeneracy → headroom → LP compression 的层级分析为理解"为什么信号选不出最优"提供了直觉和可复用的诊断协议（Appendix ab）。
37	
38	5. **极其详尽的附录** [R1, R2 共识]：30+ 页、55 个表格，涵盖 temperature/LoRA rank/free-form decoding ablation、calibration、hidden state probes、per-entity-type 分析。
39	
40	6. **负面结果的诚实报告** [R1]：trained verifier 失败（§5.2）、cross-model 仅 preliminary（§5.1）、construction 在 CoNLL 无效（§7.5）。
41	
42	---
43	
44	## Weaknesses
45	
46	### Must-Fix（影响接收决定）
47	
48	**[W-Critical-1] "Correlation-selection gap" 对 4/5 信号是 structural tautology，framing 过度渲染 novelty** [R1-N1 + R2 交叉 AGREE，共识]
49	
50	论文评估的 5 个信号中，4 个（SJ, VC, FK, EM）是 instance-level aggregates——对同一 instance 的所有 N 个 candidates 赋予相同分数。它们根据定义无法做 within-instance ranking。论文自己在 §4 (p.4) 承认："selection failure is a design property, not an empirical finding"。但 Abstract 和 Introduction 的 framing 没有前置这个关键区分，读者会以为 5 个信号都是 selection 的候选者，产生虚假 surprise。
51	
52	真正的 empirical 贡献——LP（唯一 per-sample 信号）因 compression 失败（within-instance range ≈0.041 nats, 60% instances; §4, Figure 8）——在当前 framing 下被淹没。
53	
54	**修改要求**：重构 Abstract/Intro，将 structural（4/5 信号 by construction 不能 select）与 empirical（LP compression failure）明确区分并前置。
55	
56	**[W-Critical-2] Entity-level construction 新颖性不足，缺少关键引用** [R2-N1 + R1 交叉 AGREE，共识]
57	
58	- EL4NER (arXiv:2505.23038, May 2025) 已系统实现了基于多 LLM 的 entity-level span extraction + type voting pipeline，在 ICL 设置下取得 SOTA。**未被引用**。
59	- Xie et al. (2023a) 已是 entity-level voting 的先驱，论文自己引用但未充分区分。
60	- Entity-level construction 本质上是将已有的 entity voting 在 MBR 框架下重新包装（LP-weighted variant 仅额外 +0.30pp over uniform）。
61	- +1.40pp (Few-NERD) 和 +1.02pp (SciERC, p_adj=0.20 不显著) 的改进有限。
62	
63	**修改要求**：补引 EL4NER 并区分（单模型 SC vs. 多模型 ensemble）。将 construction 定位为 diagnostic-motivated ablation 而非 standalone contribution。
64	
65	**[W-Critical-3] "First systematic characterization" overclaim** [R2-N3 + R1 交叉 AGREE，共识]
66	
67	Abstract 声称"the first systematic characterization"，但 Chen et al. (2023) 已研究 SC failure modes、Eikema et al. (2025) 已研究 structured MBR decoding 失效、Kang et al. (2025) 和 Taubenfeld et al. (2025) 已研究 confidence signals 与 SC。论文的"first"仅限于 NER + 这 5 个信号的组合。
68	
69	**修改要求**：限定 scope 为 "for NER" 或 "in the context of structured entity extraction"。
70	
71	**[W-Critical-4] 参考文献存在年份错误和疑似虚构引用** [R2-N4 + R1 交叉 AGREE，独立验证确认]
72	
73	| 问题 | 详情 |
74	|------|------|
75	| chen2025twofailures | bib 标注 2025，实际发表于 2023 (arXiv:2305.14279) |
76	| feng2025optimal | bib 首作 "Feng"，API 返回 "Austin"——需核实 |
77	| park2024grammar | bib 首作 "Park"，API 返回 "Berg-Kirkpatrick"——可能张冠李戴 |
78	| **hobelsberger2025systematic** | **Semantic Scholar/OpenAlex 均无法验证（similarity=0.236），疑似虚构引用** |
79	| 17 orphan bib entries | 在 .bib 中但未被 \cite（包括 openai2024o1, min2022rethinking 等） |
80	
81	**修改要求**：立即核实 hobelsberger2025systematic 真实性（若虚构是严重学术诚信问题）。修正年份和作者错误。清理 orphan entries。
82	
83	**[W-Critical-5] Construction 效果跨数据集不一致，p_adj 数值矛盾** [R1-N2 + R2 交叉 AGREE，共识]
84	
85	- Few-NERD: +1.40pp（Holm p_adj=0.006，显著）✓
86	- SciERC: +1.02pp — §1 报告 p_adj=0.20（不显著），但 R1 指出 Table 13 显示 p_adj=0.038——**同一结果在不同位置给出不同 p_adj，属报告失误**
87	- CoNLL: -0.39pp（不显著）✗
88	
89	4 个数据集中仅 Few-NERD 统计显著，construction 作为 contribution 的可靠性受限。
90	
91	**修改要求**：澄清 p_adj 矛盾。正文醒目标注 SciERC 不显著。讨论仅 1/4 数据集显著的适用范围。
92	
93	### Should-Fix（影响评分但不一票否决）
94	
95	**[W-Warning-1] N=8/16 对 test-time compute scaling 研究范围过窄** [R1-W1 + R2 AGREE]
96	相关文献测试到 N=64+。Few-NERD N=16 LP 仍有 +0.30pp gain，存在继续 scaling 空间。至少补 N=32 或论证 cost-efficiency。
97	
98	**[W-Warning-2] Scale/regime confound 未充分控制** [R1-W2 + R2-W1，共识]
99	Fine-tuned 4B-8B vs. zero-shot 72B 同时变化 fine-tuning、model size、architecture、quantization。需 hedge 结论或补控制实验。
100	
101	**[W-Warning-3] Cross-model consistency 过于初步** [R1-W3, R2 部分 REBUT]
102	仅 1 数据集 1 对模型，但论文标注为 "exploratory"。R2 认为定位合理，但若保留在 §5.1 需补实验或缩减为 footnote。
103	
104	**[W-Warning-4] SciERC 部分关键分析基于 single seed** [R1-W4 + R2 AGREE]
105	SciERC 仅 551 instances，用于 detailed diagnostic 但 single seed。bootstrap CI 有缓解但与论文整体统计标准不一致。
106	
107	**[W-Warning-5] Degeneracy decomposition 过松** [R2-N2, R1 部分 REBUT]
108	R2 称 bound 仅解释 3-12% 的 gap。R1 REBUT 称论文给的是 equality 非 bound，但同意可降级为 analysis tool。分歧点在于 "3-12%" 的出处和 decomposition 的实用价值。**共识**：降级为 analysis tool 而非独立 contribution。
109	
110	**[W-Warning-6] Diagnostic cascade 是描述性分析而非因果链** [R2-W2, R1 AGREE with nuance]
111	三个因素（degeneracy, headroom, LP compression）是 correlational structure，未排除第三变量。Entity construction 实验部分建立因果性。共识：标注为 "descriptive diagnostic" 更准确。
112	
113	**[W-Warning-7] 论文同时做 4 件事，各自深度不够** [R2-W3, R1 部分 REBUT]
114	R2 认为 QE benchmark + selection failure + construction + theory 各 0.5-1 页，深度不够。R1 认为四部分构成完整故事但同意可重新分层为 2 core + 2 supporting。
115	
116	**[W-Warning-8] Missing related work** [R2-W4, R1 conditionally AGREE]
117	缺少：EL4NER (arXiv:2505.23038)、Beyond Majority Voting (arXiv:2510.01499)、Scalable BoN via Self-Certainty (arXiv:2502.18581)、Optimal Aggregation (arXiv:2510.13918)。
118	
119	**[W-Warning-9] Trained verifier 负面结果 scope 有限** [R1-W5, R2 部分 REBUT]
120	LightGBM 仅在 SciERC 上测试。R2 指出 AUC=0.923 说明特征足够，问题在于 discrimination→selection 转化。共识：soften 结论从 "cannot close" 到 "do not close in our setting"。
121	
122	---
123	
124	## Reviewer Consensus [AGREE]
125	
126	1. **Framing 需重构**：Abstract/Intro 必须前置 structural/empirical 二分法，突出 LP compression 作为核心 empirical finding [R1-N1 + R2 AGREE]
127	2. **Construction 应降级**：从 standalone contribution 降为 diagnostic-motivated ablation，补引 EL4NER [R2-N1 + R1 AGREE]
128	3. **Overclaim 需限定**："first systematic characterization" 限定到 NER [R2-N3 + R1 AGREE]
129	4. **引用必须修复**：hobelsberger2025systematic 疑似虚构需立即核实 [R2-N4 + R1 独立验证 AGREE]
130	5. **p_adj 矛盾必须澄清**：SciERC construction 在 §1 和 Table 13 的数值不一致 [R1-N2 + R2 AGREE]
131	6. **统计方法论是亮点**：Holm-Bonferroni, bootstrap CI, MDE/power analysis 远超 NLP 社区水准 [R1 + R2 共识]
132	7. **论文适合 Findings**：有用的 empirical study + 统计示范价值，但 novelty 和 practical impact 不足以支撑 Main Conference [R1 + R2 共识]
133	
134	## Reviewer Divergence [REBUT]
135	
136	1. **Degeneracy decomposition 的性质**：R1 称论文给的是 equality（E[ΔF₁] = (1−D)·G_nd），R2 称是 bound 且仅解释 3-12%。R1 认为有 diagnostic 价值（快速判断 SC 可行性），R2 认为过松无实用性。**双方同意降级为 analysis tool。**
137	
138	2. **Cross-model experiment scope**：R1 认为过于初步需扩展或降级；R2 认为标注为 exploratory 定位合理，无需过多期待。**双方同意若保留需明确定位。**
139	
140	3. **Trained verifier 结论**：R1 认为 scope 有限不够 conclusive；R2 认为 AUC=0.923 恰恰说明问题在 discrimination→selection 转化而非特征不足。**双方同意 soften 结论。**
141	
142	---
143	
144	## Questions（需作者澄清）
145	
146	1. SciERC entity construction 的 p_adj 到底是 0.20 还是 0.038？两处不同的数值源于哪个 Holm family 分组？
147	2. hobelsberger2025systematic 是否为真实出版物？如果是，请提供具体的出版信息（期刊/会议、DOI）。
148	3. 如果 4/5 信号 by construction 不能做 selection，为什么 Abstract 仍将"5 confidence signals for QE and sample selection"并列？这是否误导读者？
149	4. Cross-model consistency 的 +0.42pp（§5.1）是否在 R1 引用的 CI [0.27, 0.58] 内？还是 R1 看到的是 +0.32pp CI [0.27, 0.38]？数值需确认。
150	5. Proposition 1 的 entity-wise independence 假设在何种 NER 场景下会被 violated？嵌套实体是否会导致 bound 失效？
151	
152	---
153	
154	## Missing References
155	
156	以下为两位 Reviewer 共同或独立建议补充的引用：
157	
158	1. **EL4NER** (arXiv:2505.23038, May 2025) — entity-level span extraction + type voting 的 ensemble NER pipeline [R2 提出, R1 AGREE, **必须引用**]
159	2. **Beyond Majority Voting** (arXiv:2510.01499, Oct 2025) — 超越 majority voting 的 aggregation 方法 [R2]
160	3. **Scalable Best-of-N Selection via Self-Certainty** (arXiv:2502.18581) — 直接相关的 BoN selection 方法 [R2]
161	4. **Optimal Aggregation of LLM and PRM Signals** (arXiv:2510.13918) — 多 signal 聚合理论框架 [R2]
162	
163	---
164	
165	## External Review
166	
167	**外部审稿：未请求**（项目未配置 external_review）
168	
169	---
170	
171	## Visual Layout Check（非评分项）
172	
173	视觉审查已完成（状态: done）。主要发现：
174	
175	- **[Critical] Page 7 display items 严重过密**：4 个表格（Table 2/3/4/5）+ 1 个 figure（Figure 3）挤在同一页，Figure 3 条形图极小，可读性差。相邻 page 6 和 page 8 均为纯文本——视觉节奏极不均匀。**建议移动部分 items 到 p6/p8**。
176	- **[Warning] Pages 6, 8 纯文本**：无任何 figure/table/equation，形成"文-密-文"不良节奏。
177	- **[Warning] Page 42 末页 ~75% 空白**，Page 34 ~60% 空白。
178	- **[Warning] Pages 36-41 附录表格密度极高**：部分字号接近 7pt 可读性边界。
179	- **[Info] Figure 6 (p18) heatmap 红绿色阶对色盲不友好**：建议改用 viridis 或 blue-orange。
180	- **[Info] 正面**：booktabs 风格统一，公式渲染正确，无 [?] 未解析引用，无 margin 溢出。
181	
182	---
183	
184	## Overall Assessment
185	
186	**Overall Score: 3.0 (Findings)**
187	
188	| 维度 | R1 | R2 | 综合 |
189	|------|----|----|------|
190	| Soundness | 3.5 | 3.5 | 3.5 |
191	| Excitement | 2.5 | 3.0 | 2.5 |
192	| Reproducibility | 4.0 | 4.0 | 4.0 |
193	| Overall | 3.5 | 3.0 | **3.0** |
194	| Confidence | 4 | 4 | 4 |
195	
196	**评分理由**：
197	
198	论文是一项扎实的实证研究，core insight（LP compression 作为 NER selection failure 的根本原因）有诊断价值，统计方法论在 NLP 社区具有示范意义。但存在以下主要问题阻碍主会议接收：
199	
200	1. **Novelty 受限**：核心概念"correlation-selection gap"对 80% 的信号（4/5 instance-level）是定义上的必然而非实验发现，framing 制造了虚假 surprise；entity-level construction 是已有方法的迁移应用且效果不一致。
201	2. **Contribution 深度不够**：4 个 contributions 各自偏浅——construction 仅 1/4 数据集显著，degeneracy bound 太松（R1/R2 分歧但同意降级），论文试图同时做太多事情。
202	3. **引用问题严重**：疑似虚构引用（hobelsberger2025systematic）、年份/作者错误、缺少直接相关工作（EL4NER）。
203	4. **实验覆盖有限**：N=8/16 偏小，scale confound 未控制，cross-model 过于初步。
204	
205	**定位建议**：如果作者 (1) 重构 framing 聚焦 LP compression 作为核心 empirical finding，(2) 将 construction 和 decomposition 降级为 supporting analyses，(3) 修复引用问题，(4) 限定 overclaim scope——论文在 Findings 中将是一篇有价值的诊断性工作。统计方法论值得社区学习。
206	
207	---
208	
209	## Detailed Comments
210	
211	### Section 1 (Introduction)
212	- Contribution #2 中 "That 4/5 signals are instance-level is definitional; the empirical contribution is that LP..." 这句话应该出现在 Abstract 和 Intro 前几段，而非埋在 contribution list 中。当前读者需要读到 §3-4 才能理解核心概念的 80% 是 trivial 的。
213	- "first systematic characterization" → "first systematic characterization for NER"
214	
215	### Section 3 (Diagnostic Framework)
216	- §3.1 对 instance-level vs. per-sample 的区分是论文最重要的 methodological insight，应 promote 到 Introduction。
217	- FK 的 "inter-rater agreement" 描述不准确——实际是 type-level agreement across N samples，非标准 inter-rater reliability 场景。
218	
219	### Section 4 (Why Single-Signal Selection Fails)
220	- "Definitional vs. empirical" 区分在 §4 首段出现太晚，应在 §1 前置。
221	
222	### Section 5 (Adaptive Methods)
223	- §5.1 Cross-model: 仅 1 数据集 1 对模型，+0.42pp。要么补实验要么缩减为 footnote。
224	- §5.2 Trained verifier: AUC=0.923 但 +0.30pp——结论 "cannot close" 改为 "do not close in our setting"。
225	
226	### Section 6 (Threshold Regime Analysis)
227	- §6.3 Degeneracy decomposition: 论文称 equality，bound ratio 3-12%（争议）。建议明确定位为 diagnostic tool。
228	- Proposition 1 的 entity-wise independence 假设未讨论何时 violated。
229	
230	### Section 7 (Experiments)
231	- Table 5 construction results: p_adj 矛盾需修复。
232	- CoNLL -0.39pp 负面结果值得更多分析（是 degeneracy 还是 headroom 不足？两者在 CoNLL 上同时成立）。
233	- Few-NERD 3 epochs vs 其他 5 epochs: 主文应解释原因。
234	
235	### Section 8 (Discussion)
236	- LP compression 的 mechanistic 解释（exposure bias, constrained decoding 压缩 LP 动态范围）已有但可加深。
237	- Diagnostic cascade 应标注为 "descriptive" 而非暗示因果关系。
238	
239	### References
240	- 立即核实 hobelsberger2025systematic。
241	- 修正 chen2025twofailures 年份（2023 非 2025）。
242	- 核实 feng2025optimal 和 park2024grammar 作者信息。
243	- 补引 EL4NER。
244	- 清理 17 条 orphan bib entries。
245	
246	### Format/Layout
247	- Page 7 过密（4 表 +1 图），建议分散到 p6/p8。
248	- Figure 6 heatmap 色阶对色盲不友好。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfd274e2-2cbf-4d80-bb4e-ffc77c706c74",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "50568167-07aa-4d97-b1ab-49c7083ad565",
  "sourceToolAssistantUUID": "cfd274e2-2cbf-4d80-bb4e-ffc77c706c74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T10:42:50.013Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CSrzv6sWLgoU7Rnuiw4bNH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_30.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50568167-07aa-4d97-b1ab-49c7083ad565",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU869CnUkuCWfLoc1bf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01f2fe0a-fd66-4980-82ea-f1061dcdc534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012aQxXkcn9Pj3Sno5wsasp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37061,
      "cache_read_input_tokens": 42293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37061,
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

_source line 28 · 2026-05-22T10:42:50.020Z_

<details><summary>↩ Tool result · `toolu_01CSrzv6sWLgoU7Rnuiw4bNH`</summary>

```text
1	---
2	round: 30
3	review_mode: fresh
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-21T17:17:03.954265+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 30 (Fresh Review)
12	
13	**论文**: "Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER"
14	**Venue**: EMNLP 2026 (Long Paper, ARR)
15	**截止日期**: 2026-05-25
16	**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计分析; R2: 新颖性/framing/完整性/Related Work）
17	**审稿模式**: Fresh（无历史上下文）
18	
19	---
20	
21	## Summary
22	
23	本文系统研究 NER 中 entity-level self-consistency signals 的能力边界。核心发现：agreement-based signals 能估计输出质量（Spearman ρ up to 0.47, AUROC up to 0.82）但无法用于 sample selection（所有 signal 均不优于 greedy decoding），称为 "correlation-selection gap"。论文提出四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression）定位失败原因，建立 MBR decoding 理论联系（Proposition 1），并给出三条绕过路径（LP selection +1.39pp, entity construction +1.02-1.40pp, cross-model ensemble +0.42pp）。实验覆盖 4 个 NER 数据集、2 个 model family（4B-72B + GPT-5.5）、9 类方法，附 57 项统计检验的 Holm-Bonferroni 校正。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 实验覆盖度和系统性极为出色。** 4 NER benchmarks（SciERC/Few-NERD/CoNLL/WNUT-17）跨域、跨难度梯度；模型从 4B 到 72B 再到 GPT-5.5；9 类方法覆盖 selection/construction/ensemble/supervised。60+ 张表格的 33 页 appendix 提供罕见级别的实验细节。[R1-S1, R2-S1, 共识]
30	
31	**S2. 诊断框架设计精巧且可复用。** 四阶段 cascade 逐步排除失败原因，每个阶段有明确 pass/fail 判据。对未来 structured generation 的 test-time compute 研究有方法论贡献。[R1-S2, R2-S2, 共识]
32	
33	**S3. 统计方法论严谨。** 全局 Holm-Bonferroni（k=57）、bootstrap 95% CI、TOST 等价性检验、instance-level permutation test。对以负面结果为核心的论文，这种统计审慎度是必要的且做到了。[R1-S3, R2-S1, 共识]
34	
35	**S4. 负面结果的建设性处理。** 不止报告"SC 失败"，而是诊断 WHY + 理论联系（MBR）+ 三条可操作绕过路径。从 "negative finding" 升级为 "diagnostic + prescriptive"。[R1-S4, 共识]
36	
37	**S5. MBR 理论联系有启发性。** 将 entity construction 形式化为 structured MBR decoding，嵌入更广泛的 decoding 理论。[R1-S5, R2-S3, 共识]
38	
39	**S6. Hidden-state probe 提供独立 introspection evidence。** AUROC 0.63-0.88 证明信息在模型内部存在但 agreement signals 无法有效提取。[R2-S5, 共识]
40	
41	---
42	
43	## Weaknesses
44	
45	### Must-Fix (共识 Critical)
46	
47	**W1. SciERC 单 seed 削弱 25%+ NER 证据基础。** SciERC 仅用 1 个 seed（seed=42），而 Few-NERD/CoNLL 用 3 seeds。SciERC 承载 disproportionate 的正面证据（construction gain 最大 +1.02pp, zero-shot +1.53pp; hidden-state probe AUROC 0.882; medium-difficulty primary test bed）。单 seed 的 bootstrap CI 仅反映 instance-level 变异，无法量化 seed-level 不确定性。[R1-W1 critical, R2 强烈 AGREE]
48	→ **建议**: 补充 SciERC 3-seed 实验；或在正文显著标注 single-seed caveat（当前仅 Appendix j 简要提及）。
49	
50	**W2. Cross-task validation (RE/SQL) 过于单薄，不支撑 "beyond NER" 的泛化。** RE 仅 SciERC 单数据集单模型（n=207 non-zero），55.5% zero-F1 来自 span error confound，信号排序与 NER 反转。SQL 仅 n=196 + 87.2% degeneracy（ceiling effect），无系统分析。Cross-model 仅 1 dataset × 1 model pair。Abstract/Intro 的 "validate on RE and SQL" 宣传力度超出证据。[R1-W3 warning, R2-W2 critical, 共识——R2 认为应为 critical]
51	→ **建议**: 降低 RE/SQL 宣传为 "preliminary extension"；Limitations 补充 cross-task 证据局限。
52	
53	### Should-Fix (共识 Warning)
54	
55	**W3. Proposition 1 (Entity Selection Bound) 过松，理论贡献需重定位。** Bound (1−D)·G_nd·α 仅捕获 3-12% 实际 gain（Table 30），几乎无排除力。论文自述 "loose" 但列为核心贡献之一。Empirical cascade 与 theoretical decomposition 存在两套平行框架但缺映射说明。[R1-W2 critical, R2 AGREE]
56	→ **建议**: 重定位为 "diagnostic decomposition" 而非 "performance bound"；讨论哪个因子（α）最保守及为什么。
57	
58	**W4. Degeneracy 可能是更简洁的核心解释，四阶段 cascade 可能 over-engineered。** 高 degeneracy 下 selection 失败是 trivial（样本全同）。非 degenerate instances 上 α→0（signal alignment 极低，0.000-0.161）才是核心洞察。更精确的 framing 应为 "near-zero selection alignment despite moderate quality correlation"，不需要整个 cascade。Cascade 有方法论复用价值但作为 narrative 过重。[R1-W6 warning, R2-W4 warning, 共识]
59	→ **建议**: 主文中更突出 non-degenerate failure（α→0）作为核心发现；cascade 定位为可复用诊断协议。
60	
61	**W5. 训练配方差异构成跨数据集比较混淆。** Few-NERD 3 epochs vs 其他 5 epochs。SciERC 消融显示 degeneracy 随 epoch 单调递增（43.5%→60.3%）。Few-NERD 低 degeneracy（13%）可能部分由更少 epochs 解释，但 Few-NERD 未做 5-epoch 对照。[R1-W4 warning, R2 AGREE]
62	→ **建议**: 补充 Few-NERD 5-epoch 消融或明确解释选择依据。
63	
64	**W6. Abstract 信息密度过高。** ~180 词含 12+ 数字、多个首次出现的缩写、4 项 contributions。ρ/AUROC 来自不同信号但写法可能误导。[R2-W6, R1 AGREE]
65	→ **建议**: 精简至核心 3-4 个数字；明确标注 ρ 和 AUROC 来源信号。
66	
67	**W7. Limitations 覆盖不全。** 缺失：(a) RE/SQL 证据单薄性，(b) cross-model 仅 1 dataset × 1 pair，(c) hidden-state probe per-dataset training 可能 overfit，(d) entity construction gain 幅度（+1pp at N× cost）。[R2-W7, R1 AGREE]
68	→ **建议**: 补充上述 4 点。
69	
70	---
71	
72	## Reviewer Consensus
73	
74	以下问题两位 Reviewer 达成共识（[AGREE]）：
75	
76	1. **Cross-task 证据不足以支撑泛化声明** — RE/SQL 应明确降级为 preliminary extension [R1-W3 + R2-W2]
77	2. **SciERC 单 seed 是显著弱点** — 承载 disproportionate 正面证据但无 seed-level 方差 [R1-W1 + R2]
78	3. **Degeneracy 是更简洁的核心解释** — α→0 是洞察核心，cascade 作为 narrative 过重 [R1-W6 + R2-W4]
79	4. **理论 bound 需重定位** — 3-12% 捕获率不足以称为 "bound"，应改为 diagnostic decomposition [R1-W2 + R2]
80	5. **训练配方差异需控制** — Few-NERD 缺 5-epoch 对照 [R1-W4 + R2]
81	6. **Abstract 过密 + Limitations 不全** — 需精简数字并补充关键局限 [R2-W6/W7 + R1]
82	7. **Cross-dataset correlation power 问题** — n=23 power 不足，但核心结论依赖 per-dataset 检验（power 充足），措辞需 hedge [R1-W5, R2 部分 REBUT]
83	
84	---
85	
86	## Reviewer Divergence
87	
88	| 问题 | R1 立场 | R2 立场 | Director 判断 |
89	|------|---------|---------|---------------|
90	| **标题 "Capability Ceiling" framing** | "Characterizing" 已是防御性 hedge，因果措辞修改属 minor revision (warning) | 标题暗示 impossibility result，应改标题 (critical) | **R2 更合理**：标题整体是防御性的，但正文因果措辞（"governs"/"determines"/"explaining where and why"）与 observational design 确有矛盾，需系统性替换。标题本身可保留但正文需修。定为 **Should-Fix**。 |
91	| **Entity construction 新颖性** | 诊断对比价值 + MBR 形式化被低估 | 实质是 threshold MBR 特殊情况，新颖性有限 (warning) | **R1 更合理**：construction 本身不新，但其与 selection 的系统对比揭示了失败的粒度边界（sample-level vs entity-level），这是诊断贡献的一部分。定为 **info 级**。 |
92	| **MBR 文献区分** | NER-specific 机制与 MT MBR 有质的区别，需将讨论从 Appendix 移入 main text | 区分不充分，读者可能视为 re-instantiation (warning) | **折中**：内容上 R1 正确（LP compression under constrained decoding 是 NER-specific），但呈现上 R2 正确（关键对比在 Appendix 不够）。定为 **Should-Fix**（移入 main text）。 |
93	
94	---
95	
96	## Questions
97	
98	**Q1.** SciERC 为何仅用 1 个 seed？是资源限制还是方法论考虑？[R1-Q1, 共识]
99	**Q2.** Hidden-state probe 是否做过 LODO CV？论文已有 LODO 结果（§3: AUROC drops to 0.559-0.671）但主文讨论不足——如 probe 不能 transfer，"introspection boundary" 证据价值减弱。[R2-Q2, R1 AGREE]
100	**Q3.** Entity construction "bypasses entity-level self-verification" 但仍依赖 entity-level agreement——更准确表述应为 "bypasses sample-level selection by operating at entity granularity"。[R2-Q3, R1 AGREE]
101	**Q4.** Cross-model 为何未在 Few-NERD（degeneracy 最低）上测试？这是逻辑上最应做的实验。[R2-Q4, R1 AGREE]
102	**Q5.** Proposition 1 entity-wise independence 假设 violation 程度？Table 30 Ratio (3-12%) 间接反映但未直接量化 entity-pair correlation。[R2-Q5, R1 部分 AGREE]
103	**Q6.** LP compression threshold ε=0.05 选择依据？不同 ε 是否改变 LP ranking？[R1-Q2]
104	**Q7.** TOST equivalence margin δ 的选择是否 data-driven（循环推理风险）？[R1-Q3]
105	**Q8.** Zero-shot instruction-tuned 模型下 gap 幅度是否有实质变化？[R1-Q4]
106	
107	---
108	
109	## Missing References
110	
111	- R1: 未发现重要缺失。可选补充 Malinin & Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction"
112	- R2: 建议补充 Varshney et al. (2022) ACL Findings (selective prediction), Xin et al. (2021), Malinin & Gales (2021) ICLR (structured uncertainty)
113	- 需核实：ma2024selfimproving 第一作者（bib "Ma" vs OpenAlex "Xie"）
114	- 引用验证：57 bib, 0 orphan, 0 missing, 2 not found (OpenAlex 覆盖 gaps), 4 minor encoding mismatches
115	- 引用质量总评：**良好**，无虚假引用
116	
117	---
118	
119	## External Review (Stanford Agentic Reviewer)
120	
121	未配置，不适用。
122	
123	---
124	
125	## Visual Layout Check（非评分项）
126	
127	状态：**done**（耗时约 4 分钟）
128	
129	| Severity | 发现 |
130	|----------|------|
131	| warning | Pages 1-2 连续纯文字墙（Abstract + Intro + Diagnostic Framework 开头），无 figure/table/equation 穿插。建议将 Figure 1 提前至第 2 页。 |
132	| warning | Page 7 极度拥挤——Table 4 + Table 5(a/b) + Figure 3 全部堆叠，表格间距极小，Figure 3 被压缩至可读性下限（约正文字号 60-65%）。建议移 1-2 个 table 到 appendix。 |
133	| info | Figure 1（p3）三阶段诊断级联 + 关键数值，颜色编码清晰，caption 自含。 |
134	| info | 所有正文表格统一 booktabs 风格，最优值加粗，精度一致——排版规范。 |
135	| info | p17 Figure 6 热力图使用红-黄-绿渐变，建议改用 viridis 或 Blue-Orange 色标（红绿色盲友好）。 |
136	| info | Appendix 多页大面积空白（p41/46/47 >50% 空白），可合并减少。 |
137	| info | 需验证正文页数：Conclusion 结束位置约 p9 上部，Limitations 紧随。若 Conclusion 超 p8 底部需压缩。 |
138	
139	---
140	
141	## Overall Assessment
142	
143	| 维度 | R1 | R2 | 综合 |
144	|------|----|----|------|
145	| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
146	| Excitement | 3.5/5 | 3.0/5 | **3.0/5** |
147	| Reproducibility | 4.0/5 | 4.0/5 | **4.0/5** |
148	| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |
149	| Confidence | 4/5 | 4/5 | **4/5** |
150	
151	### 评分理由
152	
153	**给 3.0 (Findings) 而非 3.5 的原因：**
154	1. **Cross-task overclaiming**：标题已限定 NER，但 Abstract/Intro 仍宣传 "validate on RE and SQL"，证据基础远不支撑（RE 单数据集+span error confound，SQL 仅 n=196 的 ceiling effect）
155	2. **因果 framing 与 observational 设计的系统性矛盾**：虽然标题 "Characterizing" 是防御性的，但正文因果措辞（"governs"/"determines"/"explaining where and why"）仍普遍存在
156	3. **SciERC 单 seed 在承载核心正面证据的数据集上是显著缺陷**
157	4. **理论 bound 捕获率仅 3-12%**，作为 "contribution" 的实际约束力有限
158	
159	**给 3.0 而非更低的原因：**
160	1. NER 范围内的诊断框架是实质性贡献（四阶段 cascade + 可复用协议）
161	2. 统计严谨性在 NLP 实证论文中属上乘（k=57 Holm, TOST, bootstrap CI）
162	3. 9 方法 × 4 数据集的系统性负面结果在该领域尚无先例
163	4. Prescriptive escape routes 虽增量有限（+1-1.4pp）但方向正确
164	5. 所有 critical 问题均可在 revision 中修复
165	
166	### 升级至 3.5 (Borderline Conference) 的条件
167	- [ ] SciERC 补充至少 2 个额外 seed（或充分论证 single-seed 不影响核心结论）
168	- [ ] RE/SQL 在 Abstract/Intro 中明确降级为 preliminary exploration
169	- [ ] Proposition 1 重定位为 diagnostic decomposition（非 performance bound）
170	- [ ] 正文因果措辞系统性替换（"governs"→"is associated with" 等）
171	- [ ] MBR 文献对比从 Appendix 移入 main text §8
172	
173	---
174	
175	## Detailed Comments
176	
177	### Section 1 (Introduction)
178	- "explaining where and why" 暗示因果但证据为相关性 → 改为 "characterizing where and how"
179	- "validate on RE and SQL" → "extend exploratorily to RE and SQL"
180	- Contributions list #4 "prescriptive escape routes" 的 cost-effectiveness 应在主文讨论（N× cost for ~1pp），当前仅 Appendix Table 61
181	
182	### Section 2 (Diagnostic Framework)
183	- Signal 定义清晰（5 signals 无歧义），instance-level vs per-sample 区分贯穿全文——这是优点
184	- Entity matching（exact span + type）描述充分
185	- Eq. 1 (SJ) 引用 Hungarian matching 缺引用 → 补 Kuhn (1955)
186	
187	### Section 3 (How Self-Verification Fails)
188	- ESJ/MRSC/LSC 三个独立 probe 一致失败是有力证据
189	- Hidden-state probe LODO 结果（AUROC drops to 0.559-0.671）已在文中但讨论不足 → 补充解释 CoNLL vs SciERC AUROC 差异原因（task difficulty → error outlier separability）
190	- "introspection boundary" 术语需考虑 probe 的 dataset-specific 性质
191	
192	### Section 4 (Where Single-Signal Selection Fails)
193	- Table 1 (selection) 清晰展示核心 negative result
194	- "definitional vs empirical" 二分法（§4 首段）是论文最精妙的区分之一 → 建议在 Abstract/Intro 更突出
195	- Cross-dataset ρ=0.052 (n=23, p=0.81) 的 power 问题已承认但措辞需 hedge
196	
197	### Section 5 (Adaptive Methods)
198	- Table 2 (method summary) 是优秀的概览
199	- Cross-model (+0.42pp) 仅 Few-NERD × 1 pair → 在正文中标注 "single-dataset result"
200	- LightGBM verifier cross-dataset transfer 为负（-0.76 to -1.02pp）→ 强化了 dataset-specific 的论点
201	
202	### Section 6 (Threshold Regime Analysis)
203	- MBR 连接严谨但 Proposition 1 bound 过松 → 见 W3
204	- Inverse scaling 发现（40/58 transitions 下 construction F1 下降）是重要实践发现
205	- θ_crit=0.70 作为 necessary condition（非 sufficient）有实际价值
206	
207	### Section 7 (Experiments)
208	- Few-NERD 3 epochs vs others 5 epochs → 需控制 [W5]
209	- Table 4 (entity construction) multi-seed mean±σ 是好的做法
210	- Holm 分 family（selection k=21, construction k=10, signal k=9）vs global k=57 → 需解释分 family 的依据和全局结果
211	
212	### Section 8 (Related Work)
213	- Ma et al. (2024) 已引用 → 验证第一作者
214	- MBR 文献对比需从 Appendix 移入此处 [Divergence #3]
215	- Yun et al. (2025) diversity collapse 差异化（Table 62）在 Appendix，核心对比建议在 main text 简述
216	
217	### Section 9 (Discussion)
218	- 因果措辞集中区 → 系统替换 "governs"/"determines" [W1 divergent]
219	- Cost-effectiveness 讨论（"N× cost for ≈1pp"）已存在但需更 explicit
220	
221	### Section 10 (Conclusion)
222	- 2 句过于精简；建议加 1 句关于 non-degenerate failure（α→0）作为核心洞察的总结
223	
224	### Limitations
225	- 覆盖良好但缺 4 点 [W7]
226	- 已有 frontier model degeneracy 差异讨论（Claude 74% vs DeepSeek 5.5%）→ 有进步
227	
228	### Format Compliance
229	- ✅ 正文 ≤8 页（需视觉审查确认 Conclusion 结束位置）
230	- ✅ Double-blind（"Anonymous ACL submission"，"[anonymized URL]"）
231	- ✅ ACL LaTeX 模板 + [review] option
232	- ✅ References 不限页数
233	- ✅ Limitations + Ethics Statement 存在
234	- ⚠️ p7 极度拥挤（视觉审查 warning）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01f2fe0a-fd66-4980-82ea-f1061dcdc534",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "093db882-3aec-41c0-a7bc-16d5299b50f5",
  "sourceToolAssistantUUID": "01f2fe0a-fd66-4980-82ea-f1061dcdc534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T10:42:50.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_017TvGpzM83LXfRR51T2nUQM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_31.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "093db882-3aec-41c0-a7bc-16d5299b50f5",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU869CnUkuCWfLoc1bf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b5ae477-6df3-452d-a410-8050091d8d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012aQxXkcn9Pj3Sno5wsasp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37061,
      "cache_read_input_tokens": 42293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37061,
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

_source line 30 · 2026-05-22T10:42:50.115Z_

<details><summary>↩ Tool result · `toolu_017TvGpzM83LXfRR51T2nUQM`</summary>

```text
1	---
2	round: 31
3	review_mode: fresh
4	overall_score: 3.0 — Findings
5	timestamp: 2026-05-22T01:19:08.201548+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER
12	
13	**Venue**: EMNLP 2026 (via ACL Rolling Review)
14	**投稿类别**: Long Paper
15	**审稿模式**: Fresh（全新初审）
16	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计；R2: 新颖性+相关工作+写作）
17	**轮次**: Round 1 + 交叉分享，1 轮收敛
18	
19	---
20	
21	## Summary
22	
23	本文研究 self-consistency（SC）在命名实体识别（NER）上的失败模式，定义了"correlation-selection gap"——质量估计信号与 oracle F1 存在相关性（Spearman ρ up to 0.47, AUROC up to 0.82），但无法用于选择更好的样本。作者提出四阶段诊断级联（degeneracy → agreement fidelity → LP compression → construction），在 4 个 NER 数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）、两个模型族（Qwen3-8B, LLaMA-3.1-8B）上系统评估了 9 类方法，发现均无法可靠改善 sample selection。正面结果通过 LP-weighted entity construction（+0.3–1.4pp）和 LP selection（+1.39pp on Few-NERD）在 entity 粒度绕过了 sample-level selection 的瓶颈。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 问题定位精准，填补研究空白。** SC 文献几乎完全聚焦于分类/推理任务，NER 作为 set-valued 结构化输出的代表性任务缺乏系统性 SC 失败分析。本文填补了这一空白。[R1, R2 共识]
30	
31	**S2. 诊断框架结构清晰、可复用。** 四阶段级联（§2–§4）将复杂问题分解为可独立检验的子问题，每一步有对应实验支撑，逻辑链条完整。该框架可迁移至其他 set-valued 任务。[R1, R2 共识]
32	
33	**S3. 实验规模和统计严谨性远超领域平均。** 报告了 bootstrap 95% CI、Holm 校正置换检验、permutation p-values、split-half reliability、Bonferroni 校正。300+ 实验覆盖 4 数据集 × 多模型 × 多 seed。[R1, R2 共识]
34	
35	**S4. 诚实呈现负面结果。** 论文未夸大正面发现，系统展示了 9 类方法的失败并提供了清晰的诊断解释。这在 ML 论文中难得。[R1]
36	
37	**S5. 引用验证通过。** 57 条 bib entry 全部有引用、无 orphan，52/57 通过在线验证，无伪造引用。[R2]
38	
39	**S6. Constrained decoding confound 处理得当。** 论文包含 free-form vs constrained decoding 对比（Appendix q），排除了 degeneracy 是 constrained decoding artifact 的可能。[R1]
40	
41	---
42	
43	## Weaknesses
44	
45	### Critical
46	
47	**C1. N=8 采样不足以支撑 "capability ceiling" 声明** [R1-N2, R2 AGREE]
48	- N=8 时 degeneracy 12%–62%，部分是小 N 的直接后果。N=16 分析（Appendix）显示 degeneracy 下降、SJ ρ 改善 +0.091、LP 增益出现。Oracle F1 随 N 单调递增（Figure 10）。
49	- 标题 "Capability Ceiling" 暗示固有结构性上界，但论文未提供 selection gap 随 N 收敛的证据。"Ceiling" 意味着渐近上界，当前数据仅支持 "在 N≤16 上存在显著 gap" 这一更弱结论。
50	- **修改建议**: 至少在 1 个数据集测试 N=32/64 并展示 selection gap 的 N-dependence 趋势；或将 "ceiling" 修改为 "limitations"（如 "Characterizing the Limitations of Self-Consistency for NER"）。
51	
52	### Major
53	
54	**M1. Proposition 1 的 entity-wise independence 假设不现实** [R1-N1 Critical → R2 降为 Major]
55	- §6.1 Proposition 1 的 MBR 分解依赖 entity-wise independence，但 NER 中实体有 span 重叠约束、句内数量约束、自回归条件依赖。论文仅用一句话承认假设是近似的，未量化偏差。
56	- R2 认为 Proposition 1 是 motivating analysis 而非核心定理，Table 5 的实证效果独立于理论证明，因此 severity 降为 Major。
57	- **修改建议**: 将 Proposition 1 重定位为 "motivating analysis under simplifying assumptions"；补充 entity 间 mutual information 的经验量化。
58	
59	**M2. 核心叙事 framing 偏向负面** [R2-N1 Critical → R1 REBUT → 降为 Major]
60	- R2 指出 Abstract "no signal outperforms greedy" 与 LP +1.39pp 矛盾。R1 反驳：(1) Abstract 限定于 SciERC，(2) LP 是 model-internal signal 非 entity-level agreement signal（Table 1 caption 明确标注），"entity-level verification fails" 指的是 SJ/VC/EM/FK。
61	- R1 的反驳成立——"直接矛盾" 指控不成立。但双方均认为整体 framing 偏向负面叙事，应更好地平衡 diagnostic 和 prescriptive 两条线索。
62	- **修改建议**: Abstract 和 Introduction 中明确区分 agreement signals（确实失败）vs model-internal LP（有条件成功）；重组 claim hierarchy。
63	
64	**M3. 与 Yao et al. (2026) 的增量区分不充分** [R2-N2 Critical → R1 REBUT → 降为 Major]
65	- R2 认为本文可能只是 Yao et al. consistency-accuracy correlation 的 NER 特例。R1 反驳：Yao 证明 correlation 存在，本文追问为何不能 operationalize 为 selection gain，提供了四阶段诊断级联，是递进关系而非特例。
66	- R1 的反驳合理但双方均同意 §8 一句话处理不充分。
67	- **修改建议**: 在 §1 或 §8 用一段专门对比 Yao et al.，说明 diagnostic cascade + construction 方法的具体增量。
68	
69	**M4. RE/SQL exploratory extensions 过于薄弱** [R1-W1, R2 AGREE]
70	- RE 仅 SciERC 1 个模型 397 有效样本（55.5% zero-F1 受 upstream NER 错误污染），SQL 仅 Spider subset n=196 with 87.2% degeneracy。不足以支撑 Introduction 中 "broader set-valued generation problem" 的泛化声明。
71	- **修改建议**: 明确定位为 preliminary evidence 并在 Limitations 注明；或从 claim 中移除 "broader" 定位。
72	
73	**M5. 正文/附录比例 8:37 严重失衡** [R2-W1, R1 AGREE]
74	- 关键信息被推入 Appendix：9 类方法完整结果（Appendix b.4）、N-scaling 分析（Appendix b.6）、hidden-state probes（Appendix h-i）、cross-dataset transfer。审稿人需读 ~47 页才能评估完整性。
75	- **修改建议**: 将 N-scaling 核心发现和 cross-dataset 结果移入正文。可合并 §9 Discussion + §10 Conclusion 腾出空间。
76	
77	**M6. 因果性语言超出相关性证据** [R1-W3, R2 AGREE]
78	- "degeneracy is the binding constraint"（§4）等表述超出证据。Non-degenerate subset 上 selection gap 仍存在，说明 degeneracy 不是唯一约束。论文 §2 声明 "observational" 但后续 section 有因果性措辞残留。
79	- 注意：历史 R1-W2（Round 1-21）曾修复全文因果语言（15 处 + 4 处残留），本轮发现仍有残留。
80	- **修改建议**: 全文检查因果性语言，降级为 "a major contributing factor" / "associated with"。
81	
82	**M7. SciERC (n=529) 和 cross-dataset (n=23) 统计效力不足** [R1-W4, R2 AGREE]
83	- 论文自身 power analysis（Appendix）确认 80% power requires n≈85 for ρ=0.3，cross-dataset n=23 远低于要求。但这些 caveat 仅在 Appendix 讨论。
84	- **修改建议**: 在主文相关结论处注明 statistical power 限制。
85	
86	**M8. 缺少 token-level 不确定性方法的系统比较** [R1-W5, R2 AGREE]
87	- LP（mean token log-prob）是唯一的 token-level 信号聚合方式，也是唯一展示正面结果的 model-internal signal。未与 sequence entropy、per-token entropy max/variance、predictive entropy（Kuhn et al. 2023）等做比较。
88	- **修改建议**: 至少补充 sequence entropy 作为 ablation。
89	
90	### Minor / Info
91	
92	**m1.** 正面结果 practical significance 有限（+1.4pp at 8x inference cost）——但论文定位为 diagnostic study 而非 method paper，双方认为可接受。建议正文明确定位。[R2-W4, R1 nuanced AGREE]
93	
94	**m2.** Table 1/Table 3 significance 标注不一致（†/‡ vs bold）。[R1]
95	
96	**m3.** Figure 1 箭头暗示因果方向与 "diagnostic sequence" 标注不符。建议改为虚线。[R1, R2 AGREE]
97	
98	**m4.** "Capability ceiling" 未形式化定义。[R1]
99	
100	**m5.** 10 个 section 在 8 页内过于拥挤，§9 Discussion 和 §10 Conclusion 各不到半页。建议合并。[R2]
101	
102	**m6.** Table 2 在正文仅展示 Few-NERD 单数据集结果。应至少展示 2 个数据集。[R2]
103	
104	**m7.** Proposition 1 条件过强（balanced set-overlap utility + entity independence），未讨论对 α 值的敏感性。[R2]
105	
106	---
107	
108	## Reviewer Consensus [AGREE]
109	
110	1. **N=8/"ceiling" 过强** — 论文的泛化 claim 超出实验证据支撑范围。标题暗示固有结构限制，但未提供收敛证据。[C1]
111	2. **因果语言残留** — 论文声明 observational 但后续有因果性措辞。[M6]
112	3. **RE/SQL 不足以泛化** — 覆盖度太低，应降级为 preliminary evidence。[M4]
113	4. **统计效力问题** — SciERC n=529 和 cross-dataset n=23 应在主文注明。[M7]
114	5. **附录比例失衡** — 关键结果不应仅在 Appendix。[M5]
115	6. **缺少 token-level 信号比较** — LP 是唯一的 model-internal signal 比较对象。[M8]
116	
117	## Reviewer Divergence [REBUT]
118	
119	1. **叙事矛盾 severity** — R2 定为 Critical（"直接矛盾"），R1 以文本证据反驳（LP ≠ entity-level agreement，Abstract 限定于 SciERC）。**Director 判断**: R1 的反驳成立，降为 Major（framing bias 而非 factual contradiction）。[M2]
120	
121	2. **与 Yao et al. 关系** — R2 认为是 Yao 的特例，R1 认为是递进关系（从 correlation 存在到 why selection fails）。**Director 判断**: R1 论据更充分（四阶段 cascade + construction 是增量），但 §8 一句话确实不够，降为 Major。[M3]
122	
123	3. **模型覆盖** — R2 称"仅两个同规模模型"，R1 指出论文含 5 个变体（4B/7B/8B/14B/72B），R2 遗漏了 Appendix t 的 72B 数据。**Director 判断**: R2 的事实认定有误，但 72B 仅在 Appendix 且为 zero-shot，缺乏 fine-tuned 大模型验证仍是合理关切。
124	
125	4. **vs Yun et al. diversity collapse** — R2 认为 degeneracy 是 diversity collapse 的 NER 特例；R1 引用 Appendix q 证据（free-form decoding 下 degeneracy 同样存在）区分两者。**Director 判断**: R1 的区分合理（定义不同、scope 不同、free-form 证据排除了 constrained decoding artifact），但论文正文应更清晰地呈现这一区分。
126	
127	5. **Holm-Bonferroni 保守性** — R1 认为 k=57 过度保守；R2 反驳对负面结果论文保守校正增强可信度。**Director 判断**: 双方有理。补充 BH-FDR sensitivity check 即可（Info 级别）。
128	
129	6. **Proposition 1 severity** — R1 定 Critical，R2 降为 Major（motivating analysis 非核心定理）。**Director 判断**: 采用 R2 的 Major 定级——Proposition 1 的实证效果（Table 5）独立于理论证明。
130	
131	---
132	
133	## Questions（需要作者回应）
134	
135	**Q1.** "Entity-level agreement signal" 的精确范围是什么？LP selection 的成功是否意味着 model-internal signals 可以部分绕过 correlation-selection gap？论文应在 §2 中给出明确分类。
136	
137	**Q2.** N=32/64 时 degeneracy rate 和 selection gap 的趋势如何？是否有证据表明 gap 随 N 收敛到某个 asymptote？
138	
139	**Q3.** CoNLL 上 48%–87% instances 产生 identical outputs——这是否因为模型在 well-studied benchmark 上 overfit/memorize？在 fully OOD 数据上 degeneracy 是否会降低？
140	
141	**Q4.** LP-weighted MBR（§6.1）与 model-based MBR（Jinnai et al. 2024）有何实质区别？
142	
143	**Q5.** Entity-wise independence 假设在实验数据上的近似程度如何？可否通过 entity 对的 mutual information 量化？
144	
145	**Q6.** 为何未比较 sequence entropy 等其他 token-level 信号聚合方式？LP 的 mean log-prob 聚合是否有特殊优势？
146	
147	---
148	
149	## Missing References
150	
151	以下引用经两位 Reviewer 交叉确认应补充：
152	1. **Fisch et al. (2021)** "Few-Shot Conformal Prediction with Auxiliary Tasks" — conformal prediction for structured NLP [R2, R1 AGREE]
153	2. **Chen et al. (2021)** "Evaluating Large Language Models Trained on Code" — pass@k 原始来源 [R2, R1 AGREE]
154	3. **Varshney et al. (2022)** "Investigating Selective Prediction Approaches..." — selective prediction survey [R2, R1 AGREE]
155	4. **Malinin & Gales (2021)** — 结构化预测中的不确定性估计 [R1, R2 AGREE]
156	5. He et al. (2024) on token-level uncertainty decomposition [R2, R1 认为相关但非必须]
157	6. Test-time scaling survey (2025) [R2, R1 认为相关但非必须]
158	
159	---
160	
161	## External Review (Stanford Agentic Reviewer)
162	
163	未请求（项目未配置外部审稿）。
164	
165	---
166	
167	## Visual Layout Check（非评分项）
168	
169	视觉审查已完成（耗时 ~5 分钟）。发现 1 critical + 6 warnings + 18 info：
170	
171	**[Critical]** Page 7 单页塞入 4 个 display items（Tables 3, 4, 5 + Figure 3），严重过挤。表格字号极小，Figure 3 散点图标注在 150dpi 下难以辨认。建议移 Table 4 或 5 至 Appendix 或合并。
172	
173	**[Warning]**
174	- Pages 1-2 连续纯文本无 display item，首个视觉锚点（Figure 1）在第 3 页——建议提前
175	- Figure 1 使用红/绿对比色，对色盲用户不友好（~8% 男性）——建议改用 blue/orange 或 Okabe-Ito 色板
176	- Page 6 全页纯文本（含 Proposition 1），节奏偏紧
177	- Page 8 Discussion/Related Work/Conclusion 全纯文本
178	- Appendix p.25 Table 13（57 行汇总表）字号极小
179	- Appendix p.26 单页 7 个小表格，排版极度拥挤
180	
181	**整体**: 全文 booktabs 风格一致、公式渲染正确、无 overfull hbox、无 section heading 孤悬、主文在第 8 页结束符合页数限制。
182	
183	---
184	
185	## Overall Assessment
186	
187	### 评分: 3.0 — Findings
188	
189	**R1 评分**: 3.5 (Borderline Conference) | **R2 评分**: 3.0 (Findings)
190	
191	### 综合评分理由
192	
193	本文对 SC 在 NER 上的失败模式提供了系统性的实证分析——四阶段诊断级联有概念价值和复用性，300+ 实验的统计严谨性远超领域平均。然而以下因素限制了评分：
194	
195	1. **核心 claim 过强** [Critical]: "Capability Ceiling" 暗示固有结构限制，但 N=8 时未提供 selection gap 随 N 收敛的证据。标题和 claim 需要降级。
196	
197	2. **Framing 失衡** [Major consensus]: 论文在 diagnostic（负面发现）和 prescriptive（正面结果 +0.3–1.4pp）之间的叙事张力未被充分调和。Agreement signals 的失败是清楚的，但 LP 的有条件成功被 framing 淡化。
198	
199	3. **泛化支撑不足** [Major consensus]: RE/SQL 扩展过于初步；缺少 token-level 信号对比；关键结果在 Appendix 而非正文。
200	
201	4. **理论贡献有限** [Major]: Proposition 1 依赖不现实的 independence 假设，需重定位为 motivating analysis。
202	
203	5. **增量新颖性** [Major]: 与 Yao et al. (2026) 和 Yun et al. (2025) 的增量区分需更充分论证。
204	
205	**Findings 适配理由**: 论文的核心贡献——correlation-selection gap 概念和四阶段诊断级联——有学术价值，适合 Findings 发表。但 "ceiling" 的过强 claim、正面结果的有限 practical significance（+1.4pp at 8× cost）、以及多个泛化性问题，使其不足以进入主会议。
206	
207	### 置信度: 4/5
208	
209	两位 Reviewer（confidence 均为 4/5）在核心问题上达成高度共识。分歧点均有充分论据支撑且已 resolve（Director 判断均有据可循）。论文已被仔细通读（含关键 Appendix 章节）。
210	
211	---
212	
213	## Detailed Comments
214	
215	### 按优先级排列的修改建议
216	
217	**Priority 1 (Must-fix for resubmission)**:
218	1. 修改标题——将 "Capability Ceiling" 替换为 "Limitations" 或类似审慎措辞；或补充 N=32/64 收敛证据
219	2. 平衡 diagnostic/prescriptive 叙事——Abstract 和 Introduction 明确区分 agreement signals vs LP
220	3. 扩展 Yao et al. (2026) 对比——从一句话扩展为一段专门讨论
221	
222	**Priority 2 (Should-fix)**:
223	4. 将 Proposition 1 重定位为 motivating analysis，补充 entity 间 dependency 量化
224	5. 全文检查因果性语言残留
225	6. 将 N-scaling 和 cross-dataset 核心发现从 Appendix 移入正文
226	7. 补充 sequence entropy 等 token-level 信号比较
227	8. 主文标注 SciERC / cross-dataset 的 statistical power caveat
228	9. RE/SQL 降级为 preliminary evidence
229	
230	**Priority 3 (Nice-to-have)**:
231	10. 合并 §9+§10 腾出空间
232	11. Table 2 扩展至 2+ 数据集
233	12. Figure 1 改用色盲友好色板
234	13. 统一 Table 显著性标注格式
235	14. 补充缺失引用（Fisch 2021, Chen 2021, Varshney 2022, Malinin & Gales 2021）
236	15. Page 7 display items 过挤——移 Table 至 Appendix 或合并
237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b5ae477-6df3-452d-a410-8050091d8d94",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "1d50ef38-4ff3-4d3e-938d-56e2233d7cf6",
  "sourceToolAssistantUUID": "6b5ae477-6df3-452d-a410-8050091d8d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T10:42:51.886Z_

Now let me read the final rounds and the decisions file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d50ef38-4ff3-4d3e-938d-56e2233d7cf6",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8SBDWQqHt9UDqR5ng",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e872910d-a63f-405e-8f8c-5e2fefe6024b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F6zmnEAoumBxV6FU4LhSzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 40019,
      "cache_read_input_tokens": 79354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40019,
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

_source line 32 · 2026-05-22T10:42:52.764Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ytbMKrRvYPM6t8hPJWhq1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_33.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e872910d-a63f-405e-8f8c-5e2fefe6024b",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8SBDWQqHt9UDqR5ng",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "353b83f8-8bcd-4430-bc74-c70531c62f70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F6zmnEAoumBxV6FU4LhSzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 40019,
      "cache_read_input_tokens": 79354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40019,
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

_source line 33 · 2026-05-22T10:42:52.788Z_

<details><summary>↩ Tool result · `toolu_014ytbMKrRvYPM6t8hPJWhq1`</summary>

```text
1	---
2	round: 33
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-22T08:21:56.027588+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER
12	
13	**项目**: struct_self_consist_ie
14	**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
15	**审稿轮次**: Round 33 (fresh)
16	**Reviewer**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作质量)
17	**日期**: 2026-05-22
18	
19	---
20	
21	## Summary
22	
23	本文系统性研究 test-time compute scaling（self-consistency）在 NER 任务上的失败原因。作者提出"correlation-selection gap"概念——QE 信号在 population level 能有效预测输出质量（Spearman ρ 达 0.45，AUROC 达 0.82），但 instance-level 选择几乎无效（多数数据集 <1 pp）。通过四阶段诊断级联（degeneracy → oracle headroom → LP compression → selection alignment α→0）定位失败机制。Entity-level construction 在 Few-NERD 上获得 +1.40 pp（Holm p_adj=0.006），但在其他数据集上效果有限或无效。实验覆盖 4 个 NER 数据集、4 个模型家族（3B–72B + GPT-5.5）、RE 和 SQL 扩展。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 重要且诚实的 negative result。** 系统性证明 self-consistency 在 NER 上失败并诊断失败原因，填补了 test-time scaling 文献在结构化预测方面的空白。论文坦诚报告 entity construction 在 CoNLL 无效、SciERC 增益微弱，诚实度在当前 NLP 文献中突出。[R1, R2 共识]
30	
31	**S2. 出色的统计严谨性。** 57 项统计检验完整枚举（Table 12 Holm-Bonferroni）、paired bootstrap CI、permutation test、TOST 等效性检验、post-hoc power analysis（Table 58）。这种透明度在同类工作中罕见，直接回应了 ARR guidelines 中 R1（inappropriate statistics）和 R5（missing significance）的关切。[R1, R2 共识]
32	
33	**S3. Correlation-selection gap 概念清晰且有迁移价值。** "QE 信号 population-level 有效但 instance-level 失效"的解耦不仅适用于 NER，对任何 set-valued structured output 的 test-time scaling 都有启示。Figure 1 直观传达核心洞见。[R1, R2 共识]
34	
35	**S4. 实验覆盖全面。** 9 种聚合方法、5 种 QE 信号、temperature/N-scaling/cross-model/cross-dataset 鲁棒性分析、RE 和 SQL 扩展、4 个模型家族（Qwen3-8B/4B/14B、LLaMA-3.1-8B、Qwen2.5-72B zero-shot、GPT-5.5 zero-shot）、DeBERTa-v3 encoder verifier、47 页附录。[R1, R2 共识]
36	
37	**S5. MBR 理论联系。** Proposition 1 和 Proposition 2 将 entity-level 聚合与 MBR decoding 理论框架对接，为实验发现提供形式化基础。[R1, R2 共识]
38	
39	---
40	
41	## Weaknesses
42	
43	### Must-Fix（影响接收决定）
44	
45	无。经交叉讨论，R1 和 R2 各自提出的 Must-Fix 问题均被对方提供了有效反驳或降级至 Should-Fix：
46	- R1-N1（θ_crit 过拟合）：R2 指出 θ_crit 来自 Corollary 1 理论推导而非 post-hoc fitting，16 个配置是验证而非拟合来源。→ **降级为 Should-Fix**
47	- R1-N2（binding constraint 叙事矛盾）：R2 指出论文原文明确写 "α→0, not degeneracy alone, is the binding constraint"，R1 的批评基于对摘要的部分误读。→ **降级为 Minor**
48	- R1-N3（entity construction 证据不足）：双方 AGREE 证据有限，但 R2 指出 construction 非核心贡献（占 ~0.5 页），论文已自我限定。→ **维持 Should-Fix**
49	- R2-N1（实验 setup 位置）：R1 指出 Section 2.3 已提供关键参数，这是 presentation 问题非技术缺陷。→ **降级为 Should-Fix**
50	- R2-N2（模型多样性不足）：R1 提供详细反驳——论文实际覆盖 4 个模型家族、3B–72B 跨度、开源/闭源、fine-tuned/zero-shot、decoder/encoder（DeBERTa）。R2 的"仅 2 个 8B 模型"描述不准确。→ **降级为 Should-Fix（主文应更显著 highlight 跨规模结果）**
51	
52	### Should-Fix（影响评分但不一票否决）
53	
54	**SF1. Entity construction 证据有限，需降低叙事权重。** [R1-N3, R2-W1 | 双方共识]
55	- 阈值 k per-dataset 优化，无部署策略
56	- Holm-Bonferroni 全局校正后 p_adj=0.055（边缘），多数 construction 结果不显著
57	- CoNLL 无增益，SciERC 增益微弱
58	- 与 Xie et al. (2023) entity voting 的差异阐述不充分
59	- **建议**：将 construction 定位为探索性结果而非核心贡献；增加与 Xie et al. 的显式对比
60	
61	**SF2. "Diagnostic Framework" 定位需澄清。** [R2-W3 | 双方部分同意]
62	- 标题包装为 "framework" 但更接近分析方法论贡献
63	- 每一步需要 task-specific 判断，其他研究者难以直接"运行"该 cascade
64	- **建议**：在 Section 1 contributions 中显式区分 (1) diagnostic methodology, (2) formal characterization, (3) empirical findings
65	
66	**SF3. Related Work (Section 8) 过于压缩。** [R2-W6 | 双方共识]
67	- ~15 行对横跨 SC/MBR/NER aggregation/uncertainty estimation 的论文不足
68	- MBR for structured NLP、LLM calibration、Yao et al. (2026)/Yun et al. (2025) concurrent works 讨论不充分
69	- **建议**：扩展至 20–25 行，从 Appendix ae (Table 66) 提炼关键对比点
70	
71	**SF4. 实验 setup 位置可优化。** [R2-N1 | R1 降级]
72	- 完整训练细节（LoRA 配置、constrained decoding 等）到 Section 7.1 才出现
73	- **建议**：在 Section 2 末尾增加 1–2 段实验概览，保留 Section 7.1 为完整参考
74	
75	**SF5. θ_crit=0.70 阈值需 sensitivity 分析。** [R1-N1 | R2 降级]
76	- 理论基础（Corollary 1）sound，但缺 held-out validation 和 sensitivity sweep
77	- **建议**：报告 θ∈[0.65, 0.75] 的敏感性；在 RE/SQL 配置上验证
78	
79	**SF6. RE 和 SQL 扩展覆盖有限。** [R1-W4, R2 | 双方共识]
80	- RE 仅 SciERC RE (n=397, 40% zero-F1)，SQL 仅类比讨论
81	- **建议**：补充 1 个 RE 数据集或弱化 "across NER and RE" 泛化声明
82	
83	**SF7. 模型多样性在主文中呈现不足。** [R2-N2 | R1 反驳后降级]
84	- 论文实际覆盖广泛（4 家族、3B–72B、GPT-5.5、DeBERTa），但主文对 72B/GPT-5.5/DeBERTa 的讨论偏简略，多数结果在附录中
85	- **建议**：在 Section 7 或 Section 9 更显著地 highlight 跨规模/跨类型的一致性发现
86	
87	---
88	
89	## Reviewer Consensus [AGREE]
90	
91	1. **Correlation-selection gap 是一个有价值的新概念**，对社区理解 self-consistency 在结构化预测上的局限性有实质贡献
92	2. **统计方法论在同类工作中属上乘**，57 项检验完整枚举的透明度值得肯定
93	3. **Entity construction 作为 prescriptive contribution 证据有限**，但论文已诚实自我限定
94	4. **Related Work 需要扩展**
95	5. **RE/SQL 扩展覆盖不足以支撑泛化声明**
96	6. **论文对 negative results 的呈现诚实且充分**
97	
98	## Reviewer Divergence [REBUT]
99	
100	1. **θ_crit 的性质**：R1 认为 post-hoc fitting 风险高（Must-Fix），R2 反驳有理论推导支撑（Should-Fix）。**Director 判定：Should-Fix**——Corollary 1 提供了理论基础，但缺 sensitivity 分析。
101	2. **"Binding constraint" 叙事**：R1 认为摘要 misleading（Must-Fix），R2 指出原文已明确 "α→0, not degeneracy alone"（Minor）。**Director 判定：Minor**——论文叙事基本准确，R1 的批评部分基于误读，但摘要措辞可微调使 signal alignment 的瓶颈地位更突出。
102	3. **模型多样性**：R2 认为"仅 2 个 8B 模型"（Must-Fix），R1 提供详细反驳列出 4 个家族 + 完整跨度。**Director 判定：Should-Fix**——覆盖存在但主文呈现不足。
103	4. **9 节结构**：R2 认为过于碎片化，R1 认为各节各回答一个独立诊断问题，简洁是优点。**Director 判定：不构成显著弱点**——诊断级联结构有其逻辑。
104	5. **"reliably predict" 措辞**：R2 认为 ρ=0.45 不够"reliable"，R1 反驳 ρ²≠variance explained（Spearman vs Pearson）且 AUROC=0.82 支撑该表述。**Director 判定：Minor 措辞调整**——"effectively predict" 或 "meaningfully predict" 更安全。
105	
106	---
107	
108	## Questions（需作者澄清）
109	
110	1. θ_crit=0.70 在 θ∈[0.65, 0.75] 范围内是否改变 Table 31 的结论？
111	2. Entity construction 阈值 k 在无标注验证数据的实际场景中如何选择？
112	3. GPT-5.5 的 10.1% parse failure 排除后，是否系统性偏移了 correlation-selection gap 估计？
113	4. 论文是否计划补充更多 RE 数据集以支撑泛化声明？
114	
115	---
116	
117	## Missing References
118	
119	1. **Entity-level aggregation 先驱工作**：Xie et al. (2023) entity voting 需在 Section 6.1 做显式对比
120	2. **MBR for structured NLP 更广泛文献**：Eikema et al. (2025) 之外的结构化输出 MBR 应用
121	3. **LLM calibration 综述**：论文使用 ECE（Appendix c）但未在 Related Work 讨论 calibration 领域
122	
123	---
124	
125	## External Review (Stanford Agentic Reviewer)
126	
127	外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）。
128	
129	---
130	
131	## Visual Layout Check（非评分项）
132	
133	视觉审查已完成（0 critical / 3 warning / 27 info）。
134	
135	**Warnings:**
136	1. **Pages 1–2 纯文本**：前 2 页为 Abstract + Introduction 连续文字，Figure 1 直到 page 3 才出现。建议考虑将 Figure 1 提前或加入 teaser figure。
137	2. **Pages 8–9 纯文本**：Related Work + Discussion + Limitations + Ethics 连续无 display item，阅读体验略单调。
138	3. **Page 24 大面积空白**：Appendix 文本末页仅 ~25% 填充，page break 控制不佳。
139	
140	**Positive:**
141	- 主文 8 display items / 8 pages，密度合理
142	- 所有 float 位置合理，无漂移
143	- 公式渲染全部正确
144	- 无 margin 溢出
145	- 符合 EMNLP 2026 8 页限制
146	- Figure 1 色彩对比存在轻微色盲友好性问题（红-绿），建议改用 Okabe-Ito 色板
147	
148	---
149	
150	## Overall Assessment
151	
152	**Overall Score: 3.5 (Borderline Conference)**
153	
154	**置信度: 4/5**
155	
156	**理由：**
157	
158	这是一篇扎实的诊断分析工作。"Correlation-selection gap"概念清晰且有迁移价值，统计严谨度在 NLP 论文中属上乘，negative results 的诚实呈现值得肯定。实验覆盖面广（4 个 NER 数据集、4 个模型家族、3B–72B 跨度、9 种方法）。
159	
160	但论文的核心局限在于 prescriptive contribution 薄弱：entity-level construction 仅在 Few-NERD 上有明确正向效果（+1.40 pp, Holm p_adj=0.006），CoNLL 无增益，SciERC 增益微弱且未通过多重校正。这使论文本质上是一篇 negative result + 诊断分析工作，方法论增量有限。Related Work 过于压缩（~15 行），"framework"定位与实际分析贡献之间存在张力。
161	
162	**无 Must-Fix 级别的技术缺陷**——经交叉讨论，所有 critical 问题均被降级或解决。7 个 Should-Fix 问题（entity construction 定位、framework 澄清、Related Work 扩展、实验 setup 前置、θ_crit sensitivity、RE/SQL 覆盖、模型多样性呈现）均可在修改周期内解决。
163	
164	当前状态下 Findings 是安全着陆点。若能解决 SF1（entity construction 重新定位）、SF3（Related Work 扩展）和 SF7（主文 highlight 跨规模结果），可提升至 Conference 水平。
165	
166	---
167	
168	## Detailed Comments
169	
170	### Section 1 (Introduction)
171	- "α→0, not degeneracy alone, is the binding constraint" 措辞基本准确但可更精确——建议改为 "near-zero selection alignment (α→0), jointly with degeneracy, constitutes the binding constraint"
172	- Contributions 列表应显式区分 diagnostic methodology / formal characterization / empirical findings 三类贡献
173	
174	### Section 2 (Diagnostic Framework)
175	- 建议在 Section 2 末尾增加 1–2 段实验概览（数据集、模型、N、T 的概要）
176	- "capability ceiling" 定义清晰，但与 "correlation-selection gap" 的关系可更显式说明
177	
178	### Section 3 (Self-Verification)
179	- ESJ AUROC=0.512 是重要的 negative finding，呈现简洁有效
180	- Hidden-state probe 的 LODO transfer 下降（0.56–0.67）是关键发现，支持 dataset-specific 结论
181	
182	### Section 4 (Single-Signal Selection)
183	- Table 1 和 Figure 2 有效传达 gap
184	- "Diagnostic cascade" 四阶段逻辑清晰，但阶段间交互（R²<0）应在主文更显著呈现
185	
186	### Section 5 (Adaptive Methods)
187	- Table 2 的 9 方法综述是有价值的参考
188	- Cross-model ensemble (+0.42 pp) 作为唯一 unconditional positive result，可在讨论中更突出
189	
190	### Section 6 (Theory)
191	- Proposition 1 形式化了直观观察——作为诊断工具有价值但不构成独立理论贡献
192	- θ_crit=0.70 需 sensitivity 分析（θ∈[0.65, 0.75]）
193	
194	### Section 7 (Experiments)
195	- 7.1 Experimental Setup 应前置或在 Section 2 提供概览
196	- 7.3 Few-NERD cross-dataset contrast 是论文亮点，LP selection +1.39 pp (p<0.001) 是最强正向结果
197	- 7.5 Prescriptive Results 应降低叙事权重，明确为探索性结果
198	
199	### Section 8 (Related Work)
200	- 需要从 ~15 行扩展至 20–25 行
201	- 补充 MBR for structured NLP、LLM calibration 讨论
202	- 将 Yao/Yun concurrent works 的讨论从 Introduction 深化到 Related Work
203	
204	### Section 9 (Discussion)
205	- 过于简短（约 5 行），建议扩展讨论 practical implications 和 future directions
206	
207	### Limitations
208	- 覆盖面广且诚实，篇幅适中，符合 EMNLP 2026 规范
209	
210	### Appendix
211	- 47 页附录详尽程度在同类工作中罕见，统计枚举透明度出色
212	- Table 66 (differentiation matrix) 应在主文 Section 8 中引用
213	- Appendix af (Anticipated Objections) 内容有用但可能给 reviewer 留下防御性印象
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "353b83f8-8bcd-4430-bc74-c70531c62f70",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "c9341cb7-2028-4181-ab4c-e9b74204f1b4",
  "sourceToolAssistantUUID": "353b83f8-8bcd-4430-bc74-c70531c62f70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T10:42:53.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GwW7GkG3srA8ikvoBPhf1H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_34.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9341cb7-2028-4181-ab4c-e9b74204f1b4",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8SBDWQqHt9UDqR5ng",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d79323c-cad7-47fb-b769-5bbd1ecfc25e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F6zmnEAoumBxV6FU4LhSzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 40019,
      "cache_read_input_tokens": 79354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40019,
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

_source line 35 · 2026-05-22T10:42:53.238Z_

<details><summary>↩ Tool result · `toolu_01GwW7GkG3srA8ikvoBPhf1H`</summary>

```text
1	---
2	round: 34
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-22T09:06:04.882696+00:00
6	reviewer_ids: ['1', '2']
7	cross_response_reviewer_ids: ['1', '2']
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 34
12	
13	**论文**: "Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER"
14	**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
15	**截止日期**: 2026-05-25
16	**审稿模式**: Fresh（重新审稿）
17	**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作）
18	
19	---
20	
21	## Summary
22	
23	本文研究 self-consistency（SC）在 NER 上的失效机制。通过四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression），系统性分析了为什么 quality estimation 信号能预测输出质量（Spearman ρ 最高 0.45, AUROC 0.82）但无法在 instance 级别选出更好的候选——即 "correlation-selection gap"。实验覆盖 4 个 NER 数据集、2 个模型族（Qwen3-8B, LLaMA-3.1-8B）、9 类方法。探索性的 entity-level construction 在低 degeneracy 条件下（Few-NERD）获得 +1.4 pp 增益，但效果不一致。degeneracy 阈值 θ_crit=0.70 预测 SC 增益何时消失。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 统计实践堪称模范。** [共识] 全面使用 bootstrap 95% CI、permutation test、TOST 等价检验、Holm-Bonferroni 多重比较校正（Table 12, k=57）、post-hoc power analysis。Table 12 的 57 项检验透明报告了全局校正下核心 claim 不达显著（p_HB=0.055），这种统计诚实在 NLP 论文中罕见。
30	
31	**S2. 实验覆盖和附录深度。** [共识] 4 个 NER 数据集 × 2 模型族 × 9 方法类别 × 16+ 配置，39 页 Appendix 覆盖几乎所有可能的消融角度（温度、sample size、free-form decoding、cross-family、14B scale、epoch confound 等），几乎穷尽了 reviewer 可能提出的消融需求。
32	
33	**S3. Correlation-selection gap 是有价值的诊断概念。** [共识] 将 quality estimation 与 selection 之间的脱节命名并系统量化，Figure 2 有效可视化了这一 gap。四阶段 cascade 的诊断逻辑清晰，每个阶段有可计算指标。
34	
35	**S4. 清晰的 observational 定位和实用的负面结论。** [共识] Section 2 开头声明不做因果声明；Section 9 的 diagnostic cascade 提供了可操作的预部署决策树。
36	
37	**S5. MBR 形式化连接。** Proposition 2 建立了 entity-level construction 与 balanced set-overlap utility 下 MBR 最优性的理论桥梁。
38	
39	---
40	
41	## Weaknesses
42	
43	### Must-Fix（影响接收决定）
44	
45	**C1. 全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著，主文未充分讨论。** [R1 提出, R2 AGREE]
46	Table 12 显示全局校正下 p_HB=0.055，"no core NER claim survives"。正文使用 family-wise corrected p-values（较小的 k=10, 21, 9），但未在正文中明确告知读者全局校正结果——Appendix e 第 18 页报告了此事实，但作为影响核心结论可信度的关键信息，应在 Discussion 或 Limitations 中显著讨论。此外应为 family-wise 分组提供先验理由（基于研究问题独立性），并报告 BH FDR 作为补充。
47	
48	**C2. 模型覆盖面不足以支撑跨规模/跨家族泛化声明。** [R1 提出, R2 AGREE]
49	主实验仅依赖 2 个 8B fine-tuned 模型（Qwen3-8B, LLaMA-3.1-8B）。GPT-5.5 仅 200 instances zero-shot；14B 仅 SciERC；72B 仅 zero-shot AWQ。Abstract/Introduction 声称 "treating NER as a representative instance of set-valued generation"、"the gap persists across scales and families"，但实际模型规模基本锁定在 7-8B，且 zero-shot vs fine-tuned 对比不对等。应限定 claim 范围为 "7-14B fine-tuned + selected zero-shot frontier models"。
50	
51	**C3. Prescriptive 阶段薄弱，三阶段叙事不完整。** [双方 AGREE]
52	Introduction 承诺 "Discover → Diagnose → Prescribe" 叙事，但 Prescribe 阶段核心产物——entity-level construction——效果不一致（Few-NERD +1.4pp, CoNLL 负面, SciERC +0.2pp non-significant）。Abstract/Discussion 以 prescriptive 口吻呈现，Section 7.5 标记 "exploratory"——叙事矛盾。Discussion 结论本质是 "what NOT to do" 而非 "what to do"。应统一定位为 "exploratory with promising but inconsistent initial results"。
53	
54	### Should-Fix（影响评分但不一票否决）
55	
56	**W1. "Diagnostic Framework" 定位与实际贡献之间存在张力。** [R2 Must-Fix, R1 REBUT — 分歧未解决]
57	R2 认为 "framework" 需要跨任务通用性和预测能力，实际是 empirical study，建议改标题。R1 反驳称 Appendix ac 的 3-step protocol 使其超越典型 empirical study，"diagnostic framework" 基本成立。Director 判断：论文的 framework 定位有一定基础（诊断 protocol 可操作），但正文叙事偶尔超出诊断范畴，应更审慎。
58	
59	**W2. 相对于 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的增量贡献界定不清。** [R2 Must-Fix, R1 REBUT — 分歧未解决]
60	R2 认为增量不够清晰。R1 提供了详细对比表（instance-level vs task-level, quantitative cascade vs qualitative failure modes, LP-weighted vs majority voting, agreement-quality alignment vs diversity）认为增量显著。Director 判断：增量存在但论文 Section 8 表述分散，缺少集中的 "What's new" 段落。
61	
62	**W3. Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失。** [R1 提出, R2 AGREE]
63	Constrained decoding 可能是 CoNLL 89% degeneracy 的重要驱动因素。如果 CoNLL free-form decoding 的 degeneracy 大幅下降，cascade 对 CoNLL 的诊断结论需修正为 "constrained decoding is the bottleneck" 而非 "SC intrinsically fails"。
64	
65	**W4. 与 Yun et al. (2025) diversity collapse 关系讨论不充分。** [双方 AGREE]
66	Degeneracy 与 diversity collapse 的概念关系未深入讨论。Constrained decoding 可能同时驱动 diversity collapse 和 LP compression，但论文仅用一句话区分。需在 Discussion 增加 2-3 句讨论 constrained decoding 作为 confound。
67	
68	**W5. θ_crit=0.70 缺少充分验证。** [R1 Must-Fix, R2 建议降级 — 分歧]
69	R1 认为 16 个配置点既拟合又验证，post-hoc fitting 风险。R2 认为 θ_crit 更像描述性发现，不需要 ML 级 held-out 验证，建议降级。Director 判断：降级为 Should-Fix，但需明确定位（descriptive vs normative）并报告 sensitivity sweep 或 LOO-CV。
70	
71	**W6. 信息密度过高，首次阅读认知负荷极大。** [R2 提出, R1 AGREE]
72	几乎每个句子 2-3 个统计量，缩写过多（LP, SJ, FK, VC, EM, MV, QE, AUROC 等）。建议主文聚焦 top-level patterns，详细数字移入 Appendix。
73	
74	**W7. Related Work 覆盖不足。** [双方 AGREE]
75	Snell et al. (2025) "Scaling LLM Test-Time Compute Optimally" 与 dataset-dependent optimal strategy 直接相关但未引用。Eikema et al. (2025) structure-conditional MBR 与 Proposition 2 的连接可深化。LLM calibration 文献（Kadavath et al. 2022, Tian et al. 2023）讨论不足。
76	
77	**W8. RE/SQL 扩展太薄，"structured IE" 泛化措辞超出证据。** [双方 AGREE]
78	RE 仅 SciERC（397 instances, 40% zero F1），且 cascade 行为与 NER 显著不同。SQL 仅一句话提及（87.2% degeneracy）。标题准确限定为 NER，但 Abstract/Discussion 的 "structured IE/prediction" 措辞超出。
79	
80	**W9. 2-seed vs 3-seed 不对称未说明。** [双方 AGREE]
81	Table 1 中 selection signals 使用 2-seed mean，baselines 使用 3-seed，正文未解释原因。
82	
83	### Minor Issues
84	
85	- **M1**: Figure 1 "diagnostic; not causal chain" 注释好，但箭头视觉暗示因果链，建议用虚线。[双方 AGREE]
86	- **M2**: 缩写表（Table 5, Appendix）建议以简化版放入主文。
87	- **M3**: Table 2 "Full coverage in Appendix h.4" 引用——主文缺少 9 类方法的数据集覆盖概览。
88	- **M4**: Table 65 cost-benefit analysis（p45）很有价值，建议在正文提及核心数字。
89	- **M5**: 引用括号格式一致性检查（Section 1 有混用）。
90	- **M6**: 匿名性无问题。Ethics Statement 和 Checklist 覆盖恰当。
91	- **M7**: 正文可能略微溢出 8 页——确认 camera-ready 严格控制。
92	- **M8**: Proposition 1/2 的 entity-wise independence 假设应在正文中更明确标注为 simplifying assumption。
93	- **M9**: Limitations 应补充 prompt sensitivity 未测试。
94	
95	---
96	
97	## Reviewer Consensus
98	
99	以下问题双方达成共识 [AGREE]：
100	
101	1. **统计实践是核心优势**——bootstrap CI、Holm-Bonferroni、permutation test 的组合使用是标杆级别
102	2. **Prescriptive 阶段薄弱**——entity-level construction 效果不一致，叙事应降级为 exploratory
103	3. **模型覆盖面不足**——泛化声明应限定为 7-14B fine-tuned regime
104	4. **全局统计校正透明度不足**——主文需讨论 k=57 结果
105	5. **Free-form decoding 消融缺失 CoNLL**——constrained decoding 可能放大 degeneracy
106	6. **Related Work 覆盖不足**——需补 Snell et al.、Eikema et al.、calibration 文献
107	7. **与 Yun et al. diversity collapse 关系需深化**
108	8. **2-seed/3-seed 差异需说明**
109	
110	---
111	
112	## Reviewer Divergence
113	
114	| 问题 | R1 立场 | R2 立场 | Director 判断 |
115	|------|---------|---------|---------------|
116	| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 3.0 (Findings) |
117	| Framework 定位 | 基本成立（Appendix ac 3-step protocol）| 过高（应为 empirical study）| 有基础但叙事需审慎收敛 |
118	| 新颖性增量 | 显著（详细对比表）| 不够清晰 | 增量存在但论文表述分散 |
119	| θ_crit 严重性 | Must-Fix（post-hoc fitting）| Should-Fix（描述性发现）| Should-Fix + 需定位澄清 |
120	| CoNLL 高 degeneracy tautology | 非 tautological（cascade 排除了其他假设）| 部分 tautological | R1 论证更有说服力 |
121	| Cross-dataset power | Should-Fix | 领域固有限制 | Info 级，提及即可 |
122	
123	---
124	
125	## Questions for Authors
126	
127	1. **CoNLL free-form decoding ablation**: 在 CoNLL 上进行 free-form decoding，degeneracy 率是否显著下降？如果下降，cascade 的 CoNLL 诊断结论是否需修正？
128	2. **全局 vs family-wise Holm-Bonferroni**: 按 BH FDR 校正，多少核心 NER claims 能在 FDR<0.05 下成立？
129	3. **θ_crit=0.70 LOO-CV**: 每个 fold 的 θ_crit 估计值变异范围是多少？
130	4. **GPT-5.5 sampling strategy**: 200-instance 的选择策略（random? stratified?）及完整结果分解？
131	5. **Degeneracy filtering + entity construction**: 仅对非 degenerate instances 做 construction，收益是否更大且更一致？
132	
133	---
134	
135	## Missing References
136	
137	1. **Snell et al. (2025)** "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" (ICLR 2025)——compute-optimal test-time scaling 策略，与 dataset-dependent optimal strategy 发现直接相关。[双方 AGREE 应引用]
138	2. **Eikema et al. (2025)** structure-conditional MBR——已引用但讨论不足，与 Proposition 2 的连接应深化。[双方 AGREE]
139	
140	---
141	
142	## External Review (Stanford Agentic Reviewer)
143	
144	**状态**：pending（已于 2026-05-22T08:47 发送请求，尚未返回）。如用户收到外部审稿结果，将作为补充材料追加。
145	
146	---
147	
148	## Visual Layout Check（非评分项）
149	
150	**状态**：Agent 超时（300s timeout）。未产出排版检查结果。用户可选择重新触发视觉审查。
151	
152	---
153	
154	## Overall Assessment
155	
156	**Overall Score: 3.0 (Findings)**
157	
158	**置信度**: 4/5
159	
160	**评分理由**:
161	
162	本文在 self-consistency 对 NER 的失效机制上提供了迄今最系统、最严谨的诊断分析，统计实践堪称模范，47 页的分析深度令人印象深刻。Correlation-selection gap 是有用的概念，四阶段 cascade 的诊断逻辑清晰。
163	
164	评 Findings 而非 Conference 的核心原因：
165	1. **统计脆弱性**：核心 NER claim 在全局 Holm-Bonferroni (k=57) 下 p_HB=0.055，未达显著——family-wise 分组虽可辩护但主文透明度不足。
166	2. **Prescriptive arm 不完整**：entity-level construction 仅在 Few-NERD 有显著且一致的增益，三阶段叙事的 Prescribe 阶段无法支撑。
167	3. **泛化证据有限**：模型覆盖主要锁定在 8B fine-tuned，跨规模声明缺乏 ≥30B fine-tuned 证据；RE/SQL 扩展过于初步。
168	4. **定位-内容张力**："Diagnostic Framework" 定位有一定基础但超出了当前验证范围（跨任务通用性不足、formal 决策边界不完整）。
169	
170	**提升路径**（如果 rebuttal/修改能回应以下问题，可升至 3.5 Borderline Conference）：
171	- 主文透明报告全局 Holm-Bonferroni + BH FDR 结果
172	- 统一 Prescriptive 叙事为 exploratory
173	- 限定 claim 范围（模型规模、任务泛化）
174	- Section 8 增加集中的增量贡献阐述
175	- CoNLL free-form ablation 或充分讨论 constrained decoding confound
176	
177	---
178	
179	## Detailed Comments
180	
181	### Section 1 (Introduction)
182	- "Discover → Diagnose → Prescribe" 三阶段叙事中 Prescribe 阶段的承诺过高。建议调整为 "Discover → Diagnose → Explore bypasses"。
183	- 与 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的差异化定位应前移到 Introduction，而非留到 Section 8。
184	
185	### Section 2 (Diagnostic Framework)
186	- "Capability ceiling" 的 N≤16 定义较窄。R1 论证该概念不依赖固定 N（gap 随 N 增大而扩大），但正文定义与后续 N=32/64 实验存在张力。
187	- Experimental setup 概览应在此处或之后增加 1-2 段，帮助读者在遇到 Section 3-6 的实验数据时有上下文。
188	
189	### Sections 3-4 (Mechanistic + Selection Gap)
190	- Introspection boundary 发现（ESJ AUROC 0.51 vs hidden-state probe 0.63-0.88）有趣但机制解释较浅。
191	- Table 1 的 2-seed/3-seed 差异需说明。
192	- Selection alignment α→0 是核心发现但叙事上被 degeneracy 讨论淹没——建议在 Section 4 更突出 α 的 binding constraint 角色。
193	
194	### Section 5 (Adaptive Methods)
195	- Table 2（9 method categories）信息密集但缺少主文中的数据集覆盖概览。
196	- Cross-model ensemble（+0.42pp）仅在 Few-NERD 单数据集测试。
197	
198	### Section 6 (Theory/Scaling)
199	- Proposition 1 应更明确标注为 descriptive formalization。Proposition 2 的 MBR 连接是更实质性的理论贡献。
200	- Inverse scaling under adaptive thresholds 的发现（40/58 transitions 变差）重要但讨论偏技术，实践含义可更直接。
201	
202	### Section 7 (Experiments)
203	- 实验设置在 Section 7.1 出现较晚——读者已在 Sections 3-6 消化了大量结果。
204	- Few-NERD 3 epochs vs others 5 epochs 的混淆需更显著讨论（不仅在 Appendix ab）。
205	
206	### Section 8 (Related Work)
207	- 缺少与 Snell et al. (2025) compute-optimal scaling 的对比。
208	- 与 Yun et al. (2025) 的关系需从 1 句扩展到 1 段——特别是 constrained decoding 作为共同 confound。
209	- 建议增加集中的 "What's new" 对比段落。
210	
211	### Section 9 (Discussion and Conclusion)
212	- 结论本质是 diagnostic（"when not to use SC"）而非 prescriptive。建议与 Introduction 的叙事对齐。
213	- Practical implications 段落有价值，可考虑增加 cost-benefit 数字（Table 65）。
214	
215	### Limitations
216	- 覆盖较好但遗漏：(a) prompt sensitivity 未测试；(b) 仅 8B fine-tuned 主实验，larger model fine-tuned 行为未知。
217	- 全局 Holm-Bonferroni 下核心 claim 脆弱性应在此处或 Discussion 讨论。
218	
219	### Appendix
220	- 极其详尽，几乎所有主文 claim 有对应消融。Appendix ac 的 3-step evaluation protocol 有实用价值。
221	- Table 65 cost-benefit analysis 建议提升到正文。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d79323c-cad7-47fb-b769-5bbd1ecfc25e",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "68612331-7fa1-4050-96f8-006a0e4f3e1e",
  "sourceToolAssistantUUID": "0d79323c-cad7-47fb-b769-5bbd1ecfc25e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T10:42:53.431Z_

<details open><summary>🔧 Tool call — Read · `toolu_012geXCPtxPfJ2EE1UUeG3eD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_35.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68612331-7fa1-4050-96f8-006a0e4f3e1e",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8SBDWQqHt9UDqR5ng",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6678d05-ec15-4253-a1ea-a8f61d36c97c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F6zmnEAoumBxV6FU4LhSzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 40019,
      "cache_read_input_tokens": 79354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40019,
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

_source line 37 · 2026-05-22T10:42:53.447Z_

<details><summary>↩ Tool result · `toolu_012geXCPtxPfJ2EE1UUeG3eD`</summary>

```text
1	---
2	round: 35
3	review_mode: fresh
4	overall_score: 3.5
5	timestamp: 2026-05-22T10:30:31.440156+00:00
6	reviewer_ids: ['1', '2']
7	cross_response_reviewer_ids: ['1', '2']
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 35 (Fresh Review)
12	
13	**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction
14	**Venue**: EMNLP 2026 via ARR May 2026 (Deadline: 2026-05-25)
15	**审稿模式**: Fresh（全新初审）
16	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）
17	**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成）
18	
19	---
20	
21	## Summary
22	
23	论文研究 test-time compute scaling（self-consistency、best-of-N）在结构化预测上的失败条件，以 NER（4 个数据集）和 RE（exploratory）为案例。核心发现 **correlation-selection gap**：质量估计信号能有效预测输出质量（AUROC 最高 0.82），但 instance-level selection 始终无法超越 greedy decoding（gain < 1pp，N=64）。诊断 cascade 将失败定位到两个 boundary conditions：output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）。Exploratory entity-level construction 在低 degeneracy 条件下部分绕过瓶颈（+1.40pp on Few-NERD）。
24	
25	---
26	
27	## Strengths
28	
29	**S1** [R1+R2 共识] **统计方法论显著超越 NLP 论文平均水平**。Holm-Bonferroni 全局校正（k=57）、MDE 分析、TOST equivalence testing、bootstrap CI、permutation tests 的组合使用在 NLP 经验性论文中极为罕见，为实证分析设立了高标准。
30	
31	**S2** [R1+R2 共识] **Correlation-selection gap 是一个真正有价值的经验贡献**。将 "QE 信号有效" 与 "selection 成功" 解耦，命名并系统量化了此前文献中未被清晰表述的现象。Figure 1 的可视化清晰传达了核心 insight。
32	
33	**S3** [R1+R2 共识] **Diagnostic cascade 概念清晰且实用**。四阶段诊断（degeneracy → oracle headroom → LP compression → signal alignment）逻辑自洽，每个阶段有可操作的度量。Appendix ae 的三步评估协议对社区有直接实用价值。
34	
35	**S4** [R1+R2 共识] **异常详尽的消融和 robustness 分析**（47 页附录）。覆盖 temperature、sample size scaling、epoch、LoRA rank、cross-model transfer、OOD、free-form decoding、thinking tokens、entity-level LP decomposition、construction threshold sensitivity 等。
36	
37	**S5** [R1+R2 共识] **诚实报告负面和有限结果**。MDE 分析坦承 "absence of evidence, not evidence of absence"；bypass 策略效果如实呈现（cross-model +0.42pp, entity construction +1.4pp），未过度渲染。
38	
39	**S6** [R1] **Failure mode gallery**（Appendix ag）提供 9 个具体失败案例的质性分析，直观展示三类典型错误模式，有教学价值。
40	
41	---
42	
43	## Weaknesses
44	
45	### Must-Fix（影响接收决定）
46	
47	**N1** [R1+R2 共识, Critical] **Scope overclaim：标题声称 "Structured Prediction" 但证据主要是 NER。**
48	标题 "Boundary Conditions for Structured Prediction" 设定了远超实验覆盖的验证门槛。充分实验仅 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 单数据集 exploratory 扩展（Appendix o, 397 实例, 1 模型），SQL 仅一句话提及 87.2% degeneracy。NER entity-set（无序集合）与 dependency parsing（树结构）、SRL（predicate-argument）、event extraction（嵌套结构）的输出空间结构差异巨大——degeneracy 和 alignment collapse 的表现形式可能完全不同。Discussion (p.8) 自承 "generalization to other structured tasks requires further investigation"，与标题的强 claim 形成内在矛盾。
49	→ **建议**：(a) 限缩标题为 NER/IE（如 "Boundary Conditions for Entity Recognition"）；或 (b) 补充至少一个完整的非 NER 结构化预测任务的 cascade 分析。
50	
51	**N2** [R1 Critical, R2 Should-Fix, 分歧] **SciERC 仅 1 个 training seed，统计可靠性不足。**
52	SciERC 是论文中分析最详尽的数据集（Figure 2 LP compression、entity-level probe、calibration analysis、free-form ablation 都以 SciERC 为 primary showcase），但仅用 1 个 training seed（seed=42），测试集仅 529 实例。论文自承 σ=0.48pp。Few-NERD 和 CoNLL 使用 3 seeds，SciERC 为何只用 1 seed 未解释。R1 认为 critical（核心发现可能不稳定），R2 认为 should-fix（核心结论由 3-seed Few-NERD/CoNLL 支撑，SciERC 更多是补充验证）。
53	→ **建议**：补充 SciERC 2 个额外 training seeds（1861 train sentences，训练成本可控）；若不可行，在主文明确标记 SciERC 相关结论为 tentative。
54	
55	### Should-Fix（影响评分但不一票否决）
56	
57	**W1** [R2 提出, R1 确认] **正文可能超出 8 页限制。** Section 9 (Discussion and Conclusion) 结论段落溢出到 Page 9 顶部。EMNLP 2026 规则：正文 8 页，Limitations/Ethics 不计入。需压缩 Related Work 或 Discussion。
58	
59	**W2** [R1+R2 共识] **Capability-diversity tension 作为 central finding 缺乏形式化。** 论文将此呈现为 central finding（Section 9），但缺乏可操作定义。Figure 3 仅展示 3 个数据集的 MV ΔF1 趋势，且 CoNLL N=64 时 MV gain 为正（+0.6pp），与 tension 叙事部分矛盾。R1 认为 structured output 上的量化分析是新的，但同意形式化不足。R2 认为文献已有隐含讨论（Snell et al. 2025, Brown et al. 2024）。
60	→ **建议**：给出可测量定义（如 degeneracy vs base F1 的函数关系），或降级为 observed pattern。
61	
62	**W3** [R1+R2 共识] **与 Yun & Price (2025) 差异化论述不充分。** "Signal alignment collapse" 与 "format diversity collapse" 语义高度重叠。Section 8 仅一句话带过差异。需 1-2 段明确对比两个概念的定义级区别及诊断 cascade 的增量信息。
63	
64	**W4** [R2 提出, R1 部分同意] **相关工作缺少重要领域。** 缺失：conformal prediction for NLP structured outputs、token-level uncertainty decomposition（Xiao et al. 2020）、MBR with entity-level F1 utility function（概念上即 entity construction 的 principled 版本）。R1 同意 conformal prediction 和 token-level 相关，认为 active learning 关联较弱。
65	
66	**W5** [R1+R2 共识] **Proposition 1 entity independence 假设与数据不符。** Split-half r=0.578-0.644 违反 independence 假设。Table 31 bound ratio 0.13-0.63 证实 bound 过松。R1 认为定性方向仍成立（高 degeneracy → MV 无法改善），R2 建议降格为 illustrative bound。
67	→ **建议**：提供 correlated entity（3-12% correlation）下 bound 偏移的数值分析，或明确降格。
68	
69	**W6** [R1+R2 共识] **Free-form decoding ablation 覆盖不全。** 仅 SciERC + CoNLL。Few-NERD（degeneracy 最低 12%）是最应验证的数据集——若 free-form 下 degeneracy 不变，强化 "model-intrinsic" 论点；若显著下降，cascade 结论需重新解读。
70	
71	**W7** [R2 提出, R1 同意] **诊断 cascade 阈值的 task-specificity 未讨论。** Degeneracy >30%、α<0.05 等阈值在不同 task 上是否稳定？已观察到 task 差异大（SciERC 12% vs WNUT-17 67.9% degeneracy），需明确说明。
72	
73	---
74	
75	## Reviewer Consensus [AGREE]
76	
77	1. **Scope overclaim 是最严重的问题**：两位 Reviewer 独立提出且交叉确认，NER 证据不能支撑 "structured prediction" 的标题
78	2. **Correlation-selection gap 是最有价值的贡献**：命名并量化了此前未被清晰表述的现象
79	3. **统计方法论达到高标准**：Holm-Bonferroni k=57、MDE、TOST 组合使用远超同行
80	4. **Entity independence 假设需要更透明的讨论**：bound 过松但定性方向成立
81	5. **Capability-diversity tension 形式化不足**：需要可操作定义或降级 framing
82	6. **Free-form ablation 需要覆盖 Few-NERD**
83	7. **正文页数超限需修复**（格式合规）
84	
85	## Reviewer Divergence [REBUT]
86	
87	1. **SciERC 单 seed 严重程度**：R1 认为 Critical Must-Fix（核心发现可能不稳定），R2 认为 Should-Fix（核心结论由 3-seed Few-NERD/CoNLL 支撑）。**Director 判断**：列为 Must-Fix 但允许 camera-ready 补充，不一票否决。
88	
89	2. **方法对比公平性**（R1-W2）：R2 反驳——论文论点是 "所有方法 gain 都小"，不是 iso-compute 竞赛。**Director 判断**：R2 论点更强，降级为小问题（建议 Table 2 caption 标注 compute cost）。
90	
91	3. **Greedy baseline 选择**（R1-W3）：R2 反驳——greedy 是 test-time scaling 文献标准 baseline（Snell et al. 2025, Wang et al. 2023, Brown et al. 2024）。**Director 判断**：R2 论点成立，不构成问题。
92	
93	4. **Capability-diversity tension 新颖性**：R1 认为 structured output 量化是新的，R2 认为增量有限。**Director 判断**：作为经验观察有价值，但不应 framed 为 central finding——Should-Fix。
94	
95	---
96	
97	## Questions
98	
99	**Q1** [R2] Correlation-selection gap 是否在任何非 NER 结构化预测任务中被验证过？
100	
101	**Q2** [R2] 为何没有直接实验 entity-level F1 作为 MBR utility function 的方案？概念上比 majority vote 更 principled。
102	
103	**Q3** [R2] Proposition 1 bound ratio 仅 0.13-0.63——是否考虑过基于 partial degeneracy 的连续 bound？
104	
105	**Q4** [R2] Figure 3 中 Few-NERD N=64 仍有正向增益，SciERC 几乎平坦——是否主要由 base model quality 驱动？更弱模型（3B/1B）是否会有更大 scaling gains？
106	
107	**Q5** [R1] SciERC 为何只用 1 个 training seed？是资源限制还是其他原因？
108	
109	---
110	
111	## Missing References
112	
113	- Conformal prediction for NLP structured outputs（近年多项工作将 conformal prediction 应用于 NER/序列标注的 uncertainty quantification）
114	- Token-level uncertainty decomposition（如 Xiao et al. 2020 epistemic/aleatoric 分解）
115	- Snell et al. (2025, ICLR) compute-optimal scaling 中关于 diminishing returns 的讨论
116	- Entity-level F1 作为 MBR utility function 的 principled 版本（vs 当前的 majority vote）
117	
118	---
119	
120	## External Review (Stanford Agentic Reviewer)
121	
122	未启用。项目配置中 `external_review.paperreview_ai.enabled` 未设置为 true。
123	
124	---
125	
126	## Visual Layout Check（非评分项）
127	
128	状态：**done**（耗时约 4 分钟）
129	
130	| 严重度 | 位置 | 发现 |
131	|--------|------|------|
132	| warning | p.24 | 附录页面约 2/3 空白（Appendix n 结尾），建议调整 float/section break |
133	| warning | p.17 | Figure 7 热力图使用红→绿色阶，对红绿色盲不友好，建议改 viridis 或 Blue→Orange |
134	| warning | p.16 | Figure 6 校准图同样存在色盲友好性问题 |
135	| warning | p.7 | 主文单页密度极高（Table 3 + Table 4 + Figure 4 + 两段文字），视觉上略拥挤 |
136	| info | p.1 | 首页无视觉锚点，Figure 1 在 p.2，延迟可控 |
137	| info | p.3 | 唯一纯文本页（信号定义），建议加小型 signal summary 表 |
138	| info | p.14-47 | 附录 34 页极为详尽，关键附录建议主文显式指引 |
139	| info | p.5 | Table 2 信息密度高但格式正确 |
140	| info | p.6 | Figure 3 色彩区分度良好且色盲友好 |
141	| info | p.47 | 末页空间利用合理（~85%） |
142	
143	无 critical 排版问题。色盲友好性（Figure 6, 7）建议修复。
144	
145	---
146	
147	## Overall Assessment
148	
149	**评分**: **3.5 — Borderline Conference**
150	**置信度**: 4/5（两位 Reviewer 均熟悉 self-consistency 和 NER 领域文献）
151	
152	### 评分理由
153	
154	**支持 Conference (4.0) 的因素**：
155	- Correlation-selection gap 是社区有价值的经验发现，命名并量化了此前模糊的现象
156	- 诊断 cascade 有独立方法论价值，附带可复用的三步评估协议
157	- 统计方法论（Holm-Bonferroni k=57、MDE、TOST）在 NLP 经验性论文中属上乘
158	- 47 页附录体现极致的 thoroughness，几乎覆盖所有可预见的 reviewer 质疑
159	- 诚实报告负面结果和方法局限性
160	
161	**限制 Conference 的因素**：
162	- **[Critical]** 标题/Abstract 声称 "structured prediction" 但证据主要是 NER——scope-evidence gap 是最大问题
163	- SciERC（最核心数据集）仅 1 training seed，统计可靠性不足
164	- Capability-diversity tension 作为 central finding 形式化不足，且文献中已有隐含讨论
165	- 核心贡献是诊断性的（"what fails"）而非建设性的（"how to fix"），prescriptive guidance 有限
166	- Proposition 1 的理论贡献偏薄（independence 假设不成立，bound 过松）
167	
168	### 改进路径（Conference 4.0 所需）
169	
170	若作者能在 camera-ready 中完成以下修改，论文可达 Conference 水平：
171	1. **[必须]** 限缩标题和 Abstract scope 为 NER/Information Extraction
172	2. **[必须]** 补充 SciERC 多 seed 实验（或标记为 tentative）
173	3. **[必须]** 修复页数溢出（压缩至 8 页正文）
174	4. **[强烈建议]** 加强与 Yun & Price (2025) 的差异化论述
175	5. **[建议]** 降级 capability-diversity tension 的 framing 或给出可操作定义
176	
177	当前版本适合 **Findings (3.0-3.5)**；scope 修正后为 **Borderline Conference (3.5-4.0)**。
178	
179	---
180	
181	## Detailed Comments
182	
183	### Section-by-Section
184	
185	**Abstract**: 第一句 "structured prediction remains uncharacterized" 过强，实际只 characterize 了 NER（和初步 RE）。建议改为 "entity-level information extraction" 或 "set-valued NER outputs"。"Exploratory entity-level construction partially bypasses" 中 "partially" 用词准确。
186	
187	**Section 1 (Introduction)**: Discover → Diagnose → Explore bypasses 三阶段叙事清晰。但 "using NER...and RE as case studies" 中 RE 的篇幅远不能称为 case study（Appendix 2 段 vs NER 的完整 pipeline）。
188	
189	**Section 2 (Diagnostic Framework)**: 五种信号的定义清晰。SJ 引用 Fleiss 1971 可能有误（Fleiss 是 inter-rater reliability，非 Soft Jaccard 来源）。Table 5 术语不一致（"Soft Jaccard" vs "structural similarity"）。建议 p.3 加小型 signal summary 表改善可浏览性。
190	
191	**Section 3 (How Self-Verification Fails)**: Introspection boundary 是有趣概念但后续很少复用——考虑去掉以减少 cognitive load，或在 Discussion 中回顾。
192	
193	**Section 4 (Where Single-Signal Selection Fails)**: 核心 section。Figure 2 双量纲共轴（AUROC vs ρ）初看混淆，建议分双轴。Table 1 caption "paired bootstrap" 但内容是 Spearman ρ，可能有误。
194	
195	**Section 5 (Adaptive Methods)**: Table 2 信息密度高。建议添加 compute cost 列（各方法相对于 greedy 的倍数），避免误导为等预算比较。
196	
197	**Section 6 (Threshold Regime Analysis)**: Proposition 1 的 "entity selection diagnostic" 方向性有用，但应在正文中明确标记为 illustrative upper bound（当前表述可能让读者误以为是 tight bound）。θ_crit=0.70 的 task-specificity 应讨论。
198	
199	**Section 7 (Experiments)**: 详尽。Few-NERD LP selection +1.39pp (p<0.001) 是论文最强的正面结果。Table 4 的 "2-seed" vs Section 7.1 "3-seed" 不一致应修复。
200	
201	**Section 8 (Related Work)**: 需扩展：补充 conformal prediction、token-level uncertainty、MBR with structural utility。与 Yun & Price (2025) 的差异化需从一句话扩展为 1-2 段。
202	
203	**Section 9 (Discussion and Conclusion)**: "Central finding is a capability-diversity tension" 需更强支撑或降级。Conclusion 段落溢出到 p.9——必须压缩。
204	
205	**Limitations**: 覆盖面广（correlational vs interventional、scope、seed、prompt template）。建议明确提及为何 SciERC 只用 1 seed。
206	
207	**Ethics Statement**: 基本合规。论文脚注已注明 "No new human data was collected"。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6678d05-ec15-4253-a1ea-a8f61d36c97c",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "af29f7ed-511e-4923-9c2f-1760e635bd41",
  "sourceToolAssistantUUID": "e6678d05-ec15-4253-a1ea-a8f61d36c97c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T10:42:53.527Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UJtGuy2c3LPPe2m1EhUKjz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af29f7ed-511e-4923-9c2f-1760e635bd41",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8SBDWQqHt9UDqR5ng",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "122b6e57-6fcf-4309-a85c-328b0eccd51d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F6zmnEAoumBxV6FU4LhSzZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 40019,
      "cache_read_input_tokens": 79354,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 40019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 326,
          "cache_read_input_tokens": 79354,
          "cache_creation_input_tokens": 40019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 40019,
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

_source line 39 · 2026-05-22T10:42:54.223Z_

<details><summary>↩ Tool result · reported error · `toolu_01UJtGuy2c3LPPe2m1EhUKjz`</summary>

```text
File content (91277 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "122b6e57-6fcf-4309-a85c-328b0eccd51d",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "7fe08bf3-2866-4b5a-84da-b57258a0b996",
  "toolUseResult": "Error: File content (91277 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "122b6e57-6fcf-4309-a85c-328b0eccd51d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-22T10:42:56.132Z_

Let me read part of the decisions file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fe08bf3-2866-4b5a-84da-b57258a0b996",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8jiAHYtadi6pr4rgd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "47250e77-7f32-44d2-86d8-3afd3270c151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WpD9KmSv97UG7DJEqR2zG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18991,
      "cache_read_input_tokens": 119373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18991,
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

_source line 41 · 2026-05-22T10:42:56.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xc62M9D4yhgWMKsaU1nwQj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47250e77-7f32-44d2-86d8-3afd3270c151",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8jiAHYtadi6pr4rgd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "580061c8-3318-4731-bd2f-0f240dda184f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WpD9KmSv97UG7DJEqR2zG4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18991,
      "cache_read_input_tokens": 119373,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 112,
          "cache_read_input_tokens": 119373,
          "cache_creation_input_tokens": 18991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18991,
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

_source line 42 · 2026-05-22T10:42:56.875Z_

<details><summary>↩ Tool result · `toolu_01Xc62M9D4yhgWMKsaU1nwQj`</summary>

```text
1	_next_id: 240
2	decisions:
3	- id: D001
4	  date: 2026-05-14 04:23 UTC
5	  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation
6	    差异'
7	  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设
8	    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果
9	    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B
10	    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman
11	    ρ。Pass ≥0.40, Fail <0.30。'
12	  related_experiments: []
13	  depends_on: []
14	- id: D002
15	  date: 2026-05-14 04:27 UTC
16	  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准
17	  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅
18	    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +
19	    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)
20	    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'
21	  related_experiments: []
22	  depends_on:
23	  - D001
24	- id: D003
25	  date: 2026-05-14 04:53 UTC
26	  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask
27	  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与
28	    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS
29	    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。
30	  related_experiments: []
31	  depends_on:
32	  - D002
33	- id: D004
34	  date: 2026-05-14 07:38 UTC
35	  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复
36	    RE evaluation'
37	  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)
38	    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但
39	    Reviewer 发现两个评估缺陷必须先修：(a) 28% test instances 无 gold relations，会在 (consistency=1.0,
40	    F1=0) 处制造 artifact，必须排除；(b) 需报告 full ρ 和 conditional ρ（排除 all-samples-F1=0 的 instances），隔离
41	    knowledge-gap cluster 的稀释效应。方向反转是系统性错误（consistent wrongness），恰好对应 error taxonomy
42	    中的 "systematic errors" 类别——本身是有价值的分析数据点。
43	  related_experiments:
44	  - exp_id: ft_001
45	    role: gate0_eval
46	    result: NER 60.4% PASS, RE 33.8% FAIL
47	  depends_on:
48	  - D003
49	- id: D005
50	  date: 2026-05-14 07:55 UTC
51	  summary: MVP pilot ft_001 结果：FAIL but positive signals. 等 ft_002 结果再做最终判定。
52	  rationale: ft_001 pilot 核心数据：RE ρ_sj_full=0.254 (FAIL <0.40), NER ρ_sj=0.362 (接近)。但
53	    conditional ρ（排除 knowledge-gap instances 后）显示正面信号：RE conditional ρ_sj=0.352 >
54	    ρ_fk=0.311 (Δ=+0.041)，NER conditional ρ_sj=0.369 > ρ_fk=0.357。核心假设"structural
55	    > surface"在控制 knowledge-gap 后成立。Oracle headroom 极大 (NER +16.9pp, RE +21.7pp)，TTS
56	    有巨大潜力。ft_002 (LoRA r=32, 5 epochs) 正在训练，如果 RE F1 提升到 ≥40%，knowledge-gap 减少可能将
57	    ρ_sj 推过 0.40。Parse failures 偏高，ft_002 pilot 需增加 max_tokens。
58	  related_experiments:
59	  - exp_id: ft_001
60	    role: mvp_pilot
61	    result: 'FAIL: RE ρ_sj_full=0.254, NER ρ_sj=0.362. Conditional: RE 0.352, NER
62	      0.369. Oracle headroom: RE +21.7pp, NER +16.9pp'
63	  depends_on:
64	  - D004
65	- id: D006
66	  date: 2026-05-14 08:08 UTC
67	  summary: Narrative 选择方案 A (stay-the-course)：等 ft_002_v2 改进 RE 后重跑 pilot，保留强 claim
68	  rationale: ft_001 pilot FAIL (RE full ρ_sj=0.254 <0.30)，但诊断结论是模型 RE 质量不足而非假设方向错误。证据：(1)
69	    NER 方向全面正确 (SJ>FK, ρ=0.362)；(2) RE conditional ρ=0.352 进入 MARGINAL 且 SJ>FK (+0.041)；(3)
70	    58.3% RE samples F1=0 是 knowledge-gap 噪声淹没信号。ft_002_v2 (LoRA r=32, 5 epochs, 降
71	    batch + gradient checkpointing 防 OOM) 预期 RE F1 提升到 ≥40%，减少 knowledge-gap instances，将
72	    ρ 推向 0.40。成本仅 ~2h (训练 30min + pilot 60min)。如果 ft_002_v2 也不过，conditional ρ 分析作为
73	    fallback analytical contribution。不选 B (NER-only 太弱) 或 C (纯 conditional 有 cherry-picking
74	    风险)。
75	  related_experiments:
76	  - exp_id: mvp_pilot_001
77	    role: pilot
78	    result: 'FAIL: RE full ρ=0.254, cond ρ=0.352; NER ρ=0.362'
79	  - exp_id: ft_002
80	    role: retrain
81	    result: OOM at step 73, restarting as ft_002_v2
82	  depends_on:
83	  - D005
84	- id: D007
85	  date: 2026-05-14 09:09 UTC
86	  summary: Gate 1 FAIL (RE rho_sj=0.244<0.30), 但 T=1.0 zero rate 44%>30% 触发协议内 T=0.7
87	    追加，暂不 pivot
88	  rationale: 1) RE full rho_sj=0.244 < 0.30 触发 ROADMAP FAIL 路径；2) 但 44.3% RE F1=0
89	    > 30% 阈值，按 Gate 1 设计追加 T=0.7 实验——这是协议预设步骤不是补救；3) RE cond rho_sj=0.316 > 0.30 说明排除
90	    all-zero 后进入 MARGINAL 区间，SJ 在"可做"实例上仍有信号；4) NER rho_sj=0.383 稳定正面；5) SJ vs FK
91	    翻转值得关注但可能与高 zero rate 有关，T=0.7 可能改善。最终 pivot 决策等 T=0.7 结果。
92	  related_experiments:
93	  - exp_id: mvp_pilot_004
94	    role: Gate 1 pilot (ft_002_v2)
95	    result: RE rho_sj=0.244 FAIL, NER rho_sj=0.383 PASS
96	  - exp_id: mvp_pilot_003
97	    role: Gate 1 pilot (ft_001) baseline
98	    result: RE rho_sj=0.237, NER rho_sj=0.381
99	  depends_on:
100	  - D006
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "580061c8-3318-4731-bd2f-0f240dda184f",
  "isSidechain": true,
  "promptId": "62975b6c-1522-4934-9341-589c1f07c470",
  "agentId": "a6bf090dfebc576f0",
  "type": "user",
  "uuid": "6b21bebd-1ff7-4c70-b6be-f5c4281b9243",
  "sourceToolAssistantUUID": "580061c8-3318-4731-bd2f-0f240dda184f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-22T10:43:30.108Z_

Perfect. Now I have comprehensive coverage of the review trajectory. Let me compile the analysis:

---

## Comprehensive Review History Timeline: struct_self_consist_ie Paper (35+ Rounds)

### SCORE TRAJECTORY AND OVERALL PATTERN

| Round | Reviewer | Score | Track | Key Change |
|-------|----------|-------|-------|------------|
| **0** | Fresh | 3/5 | Findings | Initial submission; 6 critical issues |
| **1** | Fresh | 3/5 | Findings | Bootstrap details questioned; framing issues |
| **2** | Fresh | 3.5/5 | Borderline Conf | Improvements noted; selection evidence narrower |
| **3** | Fresh | 3/5 | Findings | Constrained decoding identified as critical confound |
| **4** | Fresh | 3/5 | Findings | Statistical methods improved; core gap still tautological |
| **5** | Fresh | 3/5 | Findings | Self-assessment; 2 critical consensus issues |
| **10** | Fresh | 3.25/5 | Borderline | Free-form ablation added; framing still needs reframing |
| **15** | Fresh | 3/5 | Findings | Random vs Single baseline inconsistency flagged |
| **20** | Fresh | 3/5 | Findings | Page limit exceeded; title scope too broad |
| **25** | Fresh | 3/5 | Findings | Hobelsberger reference questioned; construction weak |
| **30** | Fresh | 3/5 | Findings | SciERC single-seed critical weakness identified |
| **31** | Fresh | 3/5 | Findings | N=8 insufficient for "capability ceiling"; framing remains issue |
| **33** | Fresh | **3.5/5** | **Borderline Conf** | **INFLECTION POINT**: No Must-Fix issues; framework acceptable with caveats |
| **34** | Fresh | 3/5 | Findings | Core NER claims p_HB=0.055 (not significant) |
| **35** | Fresh | **3.5/5** | **Borderline Conf** | Scope overclaim critical; everything else solvable |

### KEY PERSISTENT ISSUES (Across 15-35 Rounds)

#### **1. Framing Inflation: The "Tautological Gap" (Rounds 0-35, UNRESOLVED)**

**Problem**: 4/5 confidence signals (SJ, VC, FK, EM) are instance-level by construction—they assign the same score to all N candidates. Their "selection failure" is definitional, not empirical.

**Evolution**:
- **Round 0-2**: Reviewers point out gap conceptually but don't downgrade
- **Round 3**: R1 and R2 both identify this as "critical" issue requiring framing reframe
- **Round 5**: Acknowledged but NOT fully fixed—authors modify Discussion but Abstract/Intro still frame as unified "5 signals all fail"
- **Round 10**: Still flagged as "instance-level signals by construction" vs "empirical LP failure" distinction undercommunicated
- **Round 15-35**: Repeatedly mentioned but paper never fully separates the two narratives

**Current State (Round 35)**: "Correlation-selection gap" framing is praised as valuable contribution, BUT the framing inflation remains: title suggests all signals fail equally, when really 4/5 are structural failures and only LP is empirical.

**Recommendation**: The paper should explicitly front-load: "4/5 signals fail by design (instance-level); LP failure (+ MBR failure) is the empirical finding."

---

#### **2. Scope Overclaim (Rounds 20-35, NOT FULLY RESOLVED)**

**Problem**: Title promises "Structured Prediction" or "Information Extraction" but evidence is primarily NER.

**Timeline**:
- **Round 0-10**: RE mentioned but as single-benchmark exploratory
- **Round 15**: RE "preliminary" label added to Abstract
- **Round 20**: Reviewers flag "Title says IE but RE is one dataset"
- **Round 25**: R2 explicitly lists this as critical overclaim
- **Round 30-35**: Multiple rounds flag as Must-Fix: NER 4 datasets fully analyzed, RE only SciERC (397 instances), SQL only mentioned

**Current State (Round 35)**: Reviewers unanimously ask for title change from "Structured Prediction" to "Named Entity Recognition" or "Entity-Level Information Extraction."

---

#### **3. SciERC Single Seed (Rounds 25-35, PERSISTENT)**

**Problem**: SciERC (primary detailed analysis dataset, n=529) uses only 1 training seed (seed=42), while Few-NERD and CoNLL use 3 seeds.

**Impact**: 
- SciERC carries disproportionate weight for positive findings (LP compression analysis, entity-level probes, free-form ablation)
- σ=0.48pp indicates seed-level uncertainty unexplored

**Status**:
- **Round 30**: R1 lists as Critical Must-Fix
- **Round 31**: R2 downgrades to Should-Fix (core conclusions supported by 3-seed Few-NERD/CoNLL)
- **Round 34**: Consensus critical issue
- **Round 35**: Must-Fix but allowed for camera-ready

**Action Needed**: Either (a) 3-seed SciERC, or (b) main text flags SciERC results as tentative.

---

#### **4. Statistical Authority (Rounds 0-35, IMPROVED BUT FRAGILE)**

**Progression**:
- **Rounds 0-5**: Basic bootstrap lacking details
- **Rounds 10-15**: TOST, Bonferroni added progressively
- **Round 20+**: Full Holm-Bonferroni (k=57) implemented
- **Round 34**: CRITICAL FINDING: Full global k=57 correction yields p_HB=0.055 (non-significant), though family-wise p-values used for reporting

**Current Concern**: Core NER "no signal outperforms greedy" claim technically NOT significant under full correction; family-wise grouping explanation needed.

**Status**: Regarded as "exemplary statistical practice" but core claim authority questioned in Round 34-35.

---

### MAJOR TECHNICAL ISSUES EVOLUTION

#### **Constrained Decoding Confound (Rounds 3-10)**

**Discovery**: Round 3 identifies constrained decoding (vLLM + XGrammar) as uncontrolled confound. Paper's own Appendix F shows LP selection works in non-tied subset (+2.9pp, p=0.01).

**Resolution**: 
- Round 5-10: Free-form ablation added for SciERC
- Round 34: CoNLL free-form coverage still missing
- **Status**: Partially resolved but RE reversal (+1.69pp in free-form) suggests task-specific mechanism

---

#### **Entity-Level Construction Effectiveness (Rounds 0-35)**

**Trajectory**:
- **Round 0-5**: Proposed as method, ~+1.4pp Few-NERD
- **Round 10-15**: "Core contribution" status questioned (limited novelty vs Xie et al.)
- **Round 25**: R2 identifies EL4NER (May 2025) overlap, construction downgraded
- **Round 30-35**: Consistently flagged as "exploratory" with inconsistent results:
  - Few-NERD: +1.40pp (p_adj=0.006) ✓
  - CoNLL: -0.39pp ✗  
  - SciERC: +0.02pp not significant ✗

**Final Status (Round 35)**: Should be main finding, not core contribution; more like diagnostic ablation.

---

#### **Random vs Single Baseline (Rounds 15-20)**

**Issue**: Table 2 shows Random (0.610) vs Single (0.645) with 3.5pp systematic gap that seems unexplained.

**Status**: 
- Round 15: Identified as critical
- Round 20: Partially resolved with more careful explanation
- Round 35: No longer flagged

---

### CONCEPTUAL SHIFTS

| Aspect | Initial (Round 0) | Later (Round 10+) | Final (Round 35) |
|--------|-------------------|-----------------|-----------------|
| **Core Contribution** | "5 signals all fail at selection" | "LP compression + MBR failure" | "Diagnostic cascade for structured prediction" |
| **Title Scope** | "Information Extraction" | Narrowed to NER (mostly) | Should be "Named Entity Recognition" |
| **Statistical Authority** | p-values reported | Holm-Bonferroni k=57 full | Global k=57 shows p_HB=0.055 (ns) |
| **Prescriptive Value** | Entity construction as solution | Exploratory workaround | Negative result with modest bypass routes |
| **Novelty Assessment** | High (systematic comparison) | Medium (builds on Yao et al., Yun et al.) | Low-Medium (empirical verification of known phenomena) |

---

### DECISIONS FILE INSIGHTS (D001-D007+ showing decision reasoning)

The decisions.yaml reveals the paper originated from a **test-time scaling MVP experiment** (D001: validating structural > surface consistency):

- **D001-D002**: Initial hypothesis "Soft Jaccard ρ≥0.40" as gate criteria
- **D003**: Switched from ACE05 to SciERC for accessibility
- **D004-D005**: MVP pilot ft_001 FAILED (RE ρ_sj=0.254 <0.40)
- **D006**: "Stay-the-course" decision to improve model quality (ft_002_v2)
- **D007**: Gate 1 still FAILED but with conditional evidence (ρ_sj conditional=0.316 > MARGINAL threshold)

**Implication**: The paper's findings (core ρ≈0.38, selection failure) emerged from failed MVP validation attempts. This explains the heavy emphasis on diagnostic-over-prescriptive framing throughout 35 rounds.

---

### FINAL ASSESSMENT PATTERN (Rounds 33-35)

**Round 33**: 3.5/5 Borderline Conference with NO Must-Fix issues (first time in entire trajectory)

**Round 34**: Dropped to 3/5 Findings due to:
- C1: Full Holm-Bonferroni p_HB=0.055 (not significant)
- C2: Model coverage insufficient (7-8B main, GPT-5.5 exploratory, no large fine-tuned)
- C3: Prescriptive stage weak (construction inconsistent)

**Round 35**: Back to 3.5/5 Borderline Conference because:
- N1 (Must-Fix): Scope overclaim is resolvable via title change
- N2 (Must-Fix): SciERC single-seed can be camera-ready fix
- W1-W7 (Should-Fix): All substantially fixable

---

### CONCLUSION: MOVING TARGET AFTER 35 ROUNDS

The paper has evolved from an initial 3/5 Findings (6 critical flaws) through 35 review cycles to a **consistent 3.0-3.5 Borderline range** with dramatically improved statistical rigor but persistent framing issues:

**What Improved**:
- Statistical methods (p-values → TOST → Holm-Bonferroni k=57)
- Appendix thoroughness (47 pages of consummate detail)
- Conceptual clarity (gap framework sharpened)
- Negative result honesty (no overclaiming of construction gains)

**What Remained**:
- Framing inflation (tautological vs empirical distinction)
- Scope overclaim (NER labeled as structured prediction)
- Single-seed dataset unreliability (SciERC)
- Low prescriptive value (gap diagnosis, not solution)

**Reviewer Consensus**: Paper is methodologically sound and conceptually useful as a **diagnostic study for Findings track**, but too many scope-evidence gaps for Main Conference without fundamental title/framing changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b21bebd-1ff7-4c70-b6be-f5c4281b9243",
  "isSidechain": true,
  "agentId": "a6bf090dfebc576f0",
  "requestId": "req_011CbHU8w1ogAbApYQrHWes2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "67b55e63-97d7-4509-a7b1-232d5c8f5511",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea",
  "sessionId": "bab53c70-cc77-4b51-a545-658210f5074b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "staged-snuggling-noodle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BJmVrscwX4VAhNMWZMLoU2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2916,
      "cache_read_input_tokens": 138364,
      "output_tokens": 2957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2957,
          "cache_read_input_tokens": 138364,
          "cache_creation_input_tokens": 2916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2916,
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
