# Research conversation: You are a rigorous ML reviewer for a top venue (EMNLP-level, ~25% acceptance rate). Review the following paper using a 6

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2283d056e899baea.jsonl`
- **Structured JSON:** [`b5360ff0580dfc2a86d8.json`](../../sessions/b5/b5360ff0580dfc2a86d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-16T13:10:30.226Z_

You are a rigorous ML reviewer for a top venue (EMNLP-level, ~25% acceptance rate). Review the following paper using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.

## Paper Summary

**Title:** "When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation"

**Core idea:** Self-Consistency (SC) aggregates LLM reasoning traces via majority voting but breaks ties arbitrarily. The authors propose SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic (FOL) constraints from reasoning traces and resolves ties via weighted partial MAX-SAT. The key insight is that SICA's effectiveness is governed by trace diversity C0 (multi-candidate rate): SICA helps when C0 > 20% but degenerates to SC when C0 < 5%.

**Claims:**
1. Principled tiebreaking: SICA resolves SC voting ties with 77% accuracy vs 50% for random across 129 tied instances, yielding +6.9pp on FOLIO (p<0.05).
2. Operating regime characterization: C0 determines whether SICA adds value (C0>20%) or degenerates (C0<5%), validated across 3 model families and 2 reasoning architectures.
3. C0 as zero-cost diagnostic: C0 predicts the SICA-SC gap with r=0.91 across 14 model-task configurations.

**Method (4 stages):**
1. Trace sampling: Sample K=12 reasoning traces at T=0.7
2. Constraint extraction: Prompt same model to extract FOL constraints from each trace
3. Weighted MAX-SAT aggregation: Pool constraints, weight by frequency, solve via Z3 PB-MaxSAT to find answer maximizing constraint satisfaction: a* = argmax_{a^(j)} Σ_{c∈C} w_c · 1[SAT(c | a^(j))]
4. Answer selection: Return MAX-SAT winner or fall back to SC

**Key metric - C0:** Fraction of problems where K traces produce >1 distinct answer. Computed from SC run at zero extra cost.

**Experimental Setup:**
- Benchmarks: FOLIO (3-class NLI, 204 questions), ProofWriter D5 (binary, 600 questions), GSM8K pilot (30 questions). Primary eval: 804 questions for 14B; D012 subset (60 questions) for cross-family/scaling.
- Models: 5 instruction (Qwen2.5-7B/14B/72B-AWQ, Mistral-7B, LLaMA-3.1-8B) + 2 reasoning (QwQ-32B, DeepSeek-R1-Distill-LLaMA-8B)
- All K=12, T=0.7 unless noted

**Results (Table 1 - main):**
| Model | C0 | FOLIO SICA/SC/Δ | PW SICA/SC/Δ | Combined SICA/SC/Δ |
|---|---|---|---|---|
| Qwen2.5-7B | 0.65 | 73.3/63.3/+10.0 | 65.0/60.4/+4.6 | 68.3/61.7/+6.7 |
| Qwen2.5-14B | 0.46 | 82.4/75.5/+6.9 | 70.5/69.3/+1.2 | 73.5/70.9/+2.6 |
| Qwen2.5-72B-AWQ | 0.25 | 86.7/83.3/+3.3 | 78.3/77.5/+0.8 | 81.7/80.0/+1.7 |
| Mistral-7B | 0.42 | 73.3/63.3/+10.0 | 62.5/60.4/+2.1 | 66.7/61.7/+5.0 |
| LLaMA-3.1-8B | 0.40 | 70.0/60.0/+10.0 | 61.7/60.0/+1.7 | 65.0/60.0/+5.0 |
| QwQ-32B‡ | 0.04 | 73.3/73.3/0.0 | 70.8/70.8/0.0 | 71.7/71.7/0.0 |
| DS-R1-LLaMA-8B‡ | 0.03 | 73.3/73.3/0.0 | 70.8/70.8/0.0 | 71.7/71.7/0.0 |
| Qwen2.5-14B (GSM8K) | 0.10 | — | 90.0/90.0/0.0 | — |

Note: Only 14B uses full 804 questions. Others use D012 (60 questions).

**Tiebreak analysis (Table 2, 129 ties from 14B expanded):**
SICA 77%, SC-Random 50%, SC-Alphabetical 53%, SC-First-Seen 47%

**K sensitivity (Table 3, 14B on D012):**
Gap stable ~3.3pp for K=8-16, narrows at K=6 and K=20. C0 increases monotonically. Tie rate peaks at K=12 (inverted-U).

**Constraint ablation (Table 4, 804 questions 14B):**
MAX-SAT 73.5% (+2.6), Count-Only 71.8% (+0.9), Random-Weight 71.2% (+0.3), SC 70.9%
Tiebreak acc: MAX-SAT 77%, Count-Only 60%, Random-Weight 52%, SC 50%

**Overhead (Table 5):** 1.38x SC. Generation 72.4%, Extraction 21.6%, MaxSAT 1.4%, Aggregation 4.7%.

**Qualitative analysis:** 8 cases examined. 85% semantically meaningful constraints. 1/8 failure case from negation scope ambiguity.

**Cross-family:** Mistral-7B (C0=0.42, Δ=+5.0) and LLaMA-8B (C0=0.40, Δ=+5.0) replicate the pattern.

**C0 diagnostic scatter:** r=0.91, ρ=0.88, R²=0.83 across 14 configurations. Clean threshold at C0=20% with 100% binary classifier accuracy.

## Experiment Design Context (what was planned)

The review_context.yaml lists 14 imagined experiments:
1. sica_expanded_14b (exp-001): Full 804-question eval with 14B — **covered in paper** (Table 1 14B row)
2. sica_k_ablation_14b (exp-002): K sensitivity — **covered** (Table 3)
3. tiebreak_baseline_analysis (exp-003): Tiebreak comparison — **covered** (Table 2)
4. sica_7b_scaling (exp-004): 7B on D012 — **covered** (Table 1)
5. qwq_32b_operating_regime (exp-005): QwQ data — **covered** (Table 1)
6. c0_diagnostic_validation (exp-006): C0-vs-gap scatter — **covered** (Section 5.3, textually described)
7. sica_72b_awq (exp-007): 72B-AWQ on D012 — **covered** (Table 1)
8. constraint_quality_case_studies (exp-008): Qualitative analysis — **covered** (Section 5.8, 8 cases)
9. overhead_analysis (exp-009): Wall time breakdown — **covered** (Table 5)
10. sica_mistral_7b (exp-010): Mistral cross-family — **covered** (Table 1, Section 5.9)
11. sica_llama_8b (exp-011): LLaMA cross-family — **covered** (Table 1, Section 5.9)
12. gsm8k_pilot_14b (exp-012): GSM8K pilot — **covered** (Table 1)
13. constraint_ablation (exp-013): Ablation study — **covered** (Table 4)
14. sica_deepseek_r1_llama_8b (exp-014): DeepSeek-R1 — **covered** (Table 1)

All 14 planned experiments appear to be reflected in the paper.

## Your Review Task

Write a thorough review covering ALL of the following dimensions. Be specific with citations to tables/sections. For each dimension give a sub-score (1-6 scale).

### Dimensions to evaluate:

1. **Novelty & Significance** — Is the core idea (FOL constraint extraction + MAX-SAT for SC tiebreaking + C0 regime characterization) genuinely new? How significant is the contribution to the field?

2. **Technical Soundness** — Is the method well-defined? Are the experimental comparisons fair? Are there methodological flaws? Check: (a) Is the MAX-SAT formulation properly specified? (b) Are the baselines appropriate? (c) Is the statistical testing adequate? (d) Are there confounds in the C0 analysis (C0 is correlated with model size/strength — is the claimed causal role justified)?

3. **Experimental Rigor** — Sample sizes, statistical power, reproducibility. Key concerns: (a) Most cross-family results use only 60 questions (D012) — is this sufficient? (b) The combined p=0.072 for 14B expanded — not significant at 0.05. (c) The 14 data points for r=0.91 — is n=14 enough for a strong correlation claim? (d) The hero figure is described textually but not shown ("Figure ??").

4. **Clarity & Presentation** — Is the paper well-written? Are the claims well-supported by the evidence? Any broken references? Any missing figures?

5. **Completeness & Coverage** — Does the paper adequately cover the planned experiments? Are there missing comparisons (e.g., against LogicLM, LINC, or other neuro-symbolic baselines)? Is the related work sufficient?

6. **Limitations & Honesty** — Does the paper fairly present its limitations? Is the failure analysis adequate?

7. **Practical Impact** — Is the deployment guidance actionable? Would practitioners actually use this?

### Output Format

Structure your review as:

```
## Summary
[2-3 sentences]

## Strengths
[Bulleted list, S1-S5+]

## Weaknesses
[Bulleted list, W1-W5+]

## Detailed Assessment

### Novelty & Significance [X/6]
[Analysis]

### Technical Soundness [X/6]
[Analysis]

### Experimental Rigor [X/6]
[Analysis]

### Clarity & Presentation [X/6]
[Analysis]

### Completeness & Coverage [X/6]
[Analysis]

### Limitations & Honesty [X/6]
[Analysis]

### Practical Impact [X/6]
[Analysis]

## Missing Experiments / Comparisons
[What's absent that would strengthen the paper]

## Minor Issues
[Typos, formatting, small things]

## Questions for Authors
[3-5 questions]

## Overall Score: [X/6]
## Confidence: [1-5, where 5=expert]
## Recommendation: [Strong Reject / Reject / Weak Reject / Weak Accept / Accept / Strong Accept]
```

Be critical but fair. A top venue at 25% acceptance means most papers are rejected — hold to a high bar.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "34bc6b86-5407-4e22-a2f9-cf707d7579c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T13:10:30.234Z_

```json
{
  "parentUuid": "34bc6b86-5407-4e22-a2f9-cf707d7579c4",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2067dcf9-60ea-4ecc-a433-e571eb312a2f",
  "timestamp": "2026-05-16T13:10:30.234Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T13:10:33.118Z_



I'll start by reading the paper and all related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2067dcf9-60ea-4ecc-a433-e571eb312a2f",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JY4H3on85bVdrXa9Ct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93b9113a-2f7d-41ac-9b87-91ee92fa65fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFUs6v71Nx2jhr5bZoBGxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-16T13:10:33.681Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AZor8pysjR9Ckk6Fy9uEZH`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93b9113a-2f7d-41ac-9b87-91ee92fa65fb",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JY4H3on85bVdrXa9Ct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7369c7d2-ec1a-4dfe-a4ab-7e497dedc40f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFUs6v71Nx2jhr5bZoBGxD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17056
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17056,
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

_source line 5 · 2026-05-16T13:10:33.686Z_

<details><summary>↩ Tool result · `toolu_01AZor8pysjR9Ckk6Fy9uEZH`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7369c7d2-ec1a-4dfe-a4ab-7e497dedc40f",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "2c8bca1e-c27d-4f29-a58c-ef3ab31e4fe0",
  "sourceToolAssistantUUID": "7369c7d2-ec1a-4dfe-a4ab-7e497dedc40f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T13:10:36.599Z_



Let me read the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c8bca1e-c27d-4f29-a58c-ef3ab31e4fe0",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYKEiFt2gmkZHmknk3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "243fdc77-0287-4476-8130-893672202ba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2cdBA9xMeqxMcaJ1VBoph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-16T13:10:37.019Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_011kFe7XEvGvitAwpwBRcbfX`</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "243fdc77-0287-4476-8130-893672202ba3",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYKEiFt2gmkZHmknk3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3ac6068-d37d-498c-8d43-987a0e897d6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2cdBA9xMeqxMcaJ1VBoph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-16T13:10:37.093Z_

<details><summary>↩ Tool result · `toolu_011kFe7XEvGvitAwpwBRcbfX`</summary>

```text
{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (15 个)\n\n- **sica_expanded_14b**: RUNNING — \n- **sica_k_sensitivity_14b**: QUEUED — \n- **sica_d012_14b**: DONE (success) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_temp_diversity**: DONE (negative) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| sica_expanded_14b | — | — | — | — |\n\n## 待处理\n- sica_k_sensitivity_14b（排队等待 GPU）\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **sica_d012_14b** (success): —\n  [D012 Full Evaluation Report - sica_d012_14b](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/d012_report_sica_d012_14b.md) | [D017 Tiebreak Baseline Analysis](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/tiebreak_analysis_report.md)\n- **sica_folio30** (killed): 逻辑域（FOLIO）上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12——FOLIO 有天然 FOL 标注，是 SICA 约束提取的理想场景 ← 基于 sica_aime30_v3\n  [FOLIO C0 Precheck Report](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_folio30/report/folio_c0_precheck_report.md)\n- **sica_d016_c0_precheck** (success): D016 模型 pivot C0 预检：Qwen2.5-14B-Instruct 在逻辑域是否产生足够 trace 多样性（多候选率 ≥20%） ← 基于 sica_proofwriter30_v2\n\n## 趋势\n成功 4 / 负向 1 / 失败 1 / 共 12\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32608: 无 GPU 信息\n\n## 告警\n- mvp_math50_t07: 已被终止 — unknown\n- sica_aime30_t07: 已被终止 — unknown\n- sica_aime30_v2: 已被终止 — unknown\n- sica_aime30_v3: 已被终止 — unknown\n- sica_proofwriter30: 训练失败 — unknown\n- sica_folio30: 已被终止 — unknown\n- sica_proofwriter30_v2: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3ac6068-d37d-498c-8d43-987a0e897d6a",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "ef6d433e-d924-4ddc-86f7-d2073a623bf0",
  "sourceToolAssistantUUID": "e3ac6068-d37d-498c-8d43-987a0e897d6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T13:10:38.238Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013Hvef2iPRqxs9N2JXJqjE2`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6d433e-d924-4ddc-86f7-d2073a623bf0",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYKEiFt2gmkZHmknk3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "053bdf03-f54f-4f45-a629-c2c0c41d8524",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2cdBA9xMeqxMcaJ1VBoph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-16T13:10:38.249Z_

<details><summary>↩ Tool result · `toolu_013Hvef2iPRqxs9N2JXJqjE2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| sica_expanded_14b | — | — | — | — |\\n\\n## 待处理\\n- sica_k_sensitivity_14b（排队等待 GPU）\\n- smoke-test-5q（准备中）\\n\\n## 近期结论\\n- **sica_d012_14b** (success): —\\n  [D012 Full Evaluation Report - sica_d012_14b](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/d012_report_sica_d012_14b.md) | [D017 Tiebreak Baseline Analysis](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/tiebreak_analysis_report.md)\\n- **sica_folio30** (killed): 逻辑域（FOLIO）上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12——FOLIO 有天然 FOL 标注，是 SICA 约束提取的理想场景 ← 基于 sica_aime30_v3\\n  [FOLIO C0 Precheck Report](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_folio30/report/folio_c0_precheck_report.md)\\n- **sica_d016_c0_precheck** (success): D016 模型 pivot C0 预检：Qwen2.5-14B-Instruct 在逻辑域是否产生足够 trace 多样性（多候选率 ≥20%） ← 基于 sica_proofwriter30_v2\\n\\n## 趋势\\n成功 4 / 负向 1 / 失败 1 / 共 12\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32608: 无 GPU 信息\\n\\n## 告警\\n- mvp_math50_t07: 已被终止 — unknown\\n- sica_aime30_t07: 已被终止 — unknown\\n- sica_aime30_v2: 已被终止 — unknown\\n- sica_aime30_v3: 已被终止 — unknown\\n- sica_proofwriter30: 训练失败 — unknown\\n- sica_folio30: 已被终止 — unknown\\n- sica_proofwriter30_v2: 已被终止 — unknown\\n\", \"total_chars\": 1362, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "053bdf03-f54f-4f45-a629-c2c0c41d8524",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "a247ebcb-0efa-4b93-8f47-276a733789ff",
  "sourceToolAssistantUUID": "053bdf03-f54f-4f45-a629-c2c0c41d8524",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T13:10:38.411Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01A4dykF4btdWW4cnMnAA7Ep`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a247ebcb-0efa-4b93-8f47-276a733789ff",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYKEiFt2gmkZHmknk3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "188a859e-35f3-4d8c-86c1-76cf23d70204",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2cdBA9xMeqxMcaJ1VBoph",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17056,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 17056,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 12 · 2026-05-16T13:10:38.425Z_

<details><summary>↩ Tool result · `toolu_01A4dykF4btdWW4cnMnAA7Ep`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "188a859e-35f3-4d8c-86c1-76cf23d70204",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "65fee0f4-2f4f-4044-9929-68bf04f41a7c",
  "sourceToolAssistantUUID": "188a859e-35f3-4d8c-86c1-76cf23d70204",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T13:10:41.391Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KrQbrLHaWSYkvNHtfe8XQf`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65fee0f4-2f4f-4044-9929-68bf04f41a7c",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYfT92JgftavJJcSXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "789e3cd7-28fe-4a0e-9e69-09b90b365e00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBQKeg8352Gwsom9bmXcy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 18503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 14 · 2026-05-16T13:10:41.408Z_

<details><summary>↩ Tool result · `toolu_01KrQbrLHaWSYkvNHtfe8XQf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ROADMAP.md\", \"content\": \"# symb_invariant_consensus — Research Dashboard\\n\\n> 最后更新: 2026-05-16 06:18 UTC | 更新原因: D021 scope 扩展：补 5 个新实验(Mistral/LLaMA/GSM8K/constraint-ablation/DeepSeek-R1) + Claim 2 reframe + GPU 排期更新\\n\\n## 核心方向\\nSymbolic Invariant Consensus Aggregation (SICA)：从多条 LLM 推理路径中提取符号约束，通过加权 partial MAX-SAT 找到全局一致的约束子集，提供 principled tiebreaking。核心 insight：符号共识的有效性取决于 trace diversity (C0)——追踪认知不确定性的零成本指标，跨模型家族和推理域通用。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research（Post-MVP, D021 Scope 扩展）** — MVP D012 PASS（C3=+3.3pp）。正在：(1) 扩大样本量 exp-001 804题 RUNNING (2) 补 3 个非 Qwen 模型 + GSM8K 跨域 + constraint ablation 以满足 A 类 scope 要求。\\n\\n## 关键 Checkpoint\\n**May 19 UTC**：全部 GPU 实验完成 → 数据充分性判定 → 冲 EMNLP May 25 ARR 或切 AAAI Aug 1\\n\\n## Core Claims (paper_framing.md)\\n1. Principled Tiebreaking — SICA 通过约束权重打破 SC 平票\\n2. Operating Regime — C0 追踪认知不确定性，决定 SICA 是否有效。跨 3 家族 (Qwen/Mistral/LLaMA) + 2 reasoning 架构 (QwQ/DeepSeek-R1) 验证\\n3. C0 as Diagnostic — 多候选率可预测 SICA 部署价值\\n\\n## GPU 执行排期（串行，单 GPU）\\n\\n| 序号 | 实验 | 模型 | 优先级 | GPU-h | 状态 |\\n|------|------|------|--------|-------|------|\\n| 1 | exp-001 sica_expanded_14b | 14B | P0 | ~13h remaining | RUNNING |\\n| 2 | exp-002 sica_k_ablation | 14B (same vLLM) | P0 | 5h | planned |\\n| 3 | exp-012 gsm8k_pilot_14b | 14B (same vLLM) | P1 | 1h | planned |\\n| 4 | exp-010 sica_mistral_7b | Mistral-7B | P0 | 1.5h | planned |\\n| 5 | exp-011 sica_llama_8b | LLaMA-8B | P0 | 1.5h | planned |\\n| 6 | exp-004 sica_7b_scaling | Qwen-7B | P1 | 2h | planned |\\n| 7 | exp-014 sica_deepseek_r1 | DeepSeek-R1-7B | P1 | 2h | planned |\\n| 8 | exp-007 sica_72b_awq | Qwen-72B-AWQ | P1 | 4h | planned |\\n\\n**Total: ~31h → 完成 ~May 18 11:00 UTC**（May 19 checkpoint 有 margin）\\n\\nCPU 并行（不占 GPU）：\\n- [x] exp-003 tiebreak baseline (done on D012, re-run on expanded after exp-001)\\n- [x] exp-005 QwQ-32B operating regime data (done)\\n- [ ] exp-013 constraint ablation (MaxSAT vs count-only vs random-weight) — after exp-001\\n- [ ] exp-009 overhead analysis — after exp-001\\n- [ ] exp-008 case studies — after exp-001\\n- [ ] exp-006 C0 diagnostic validation — after exp-001/002/004/010/011/014\\n\\n## 近期任务\\n- [ ] Agent 下载 Mistral-7B / LLaMA-8B / DeepSeek-R1-7B 模型（CPU，exp-001 期间并行）\\n- [ ] Agent 准备 GSM8K-200 数据集 + 评估脚本\\n- [ ] Agent 写 analyze_expanded.py 分析脚本\\n- [ ] exp-001 完成后立即跑分析 + 启动 exp-002\\n- [ ] exp-013 constraint ablation 脚本准备（CPU-only）\\n- [ ] Dream dream_20260516T054054 完成后处理报告\\n\\n## MVP 结论（已锁定）\\n- **QwQ-32B**: 全域 C0=3.6%, SICA≡SC。模型级自一致性。\\n- **Qwen2.5-14B-Instruct**: C0=53.3%, SICA 73.3% vs SC 70.0% (+3.3pp)。5 个 6:6 平票 SICA 4/5 正确 (80%)。\\n\\n## GPU 预算\\n- westd-32608: 1× NVIDIA RTX PRO 6000 Blackwell (98GB), cuda:0\\n- 当前：exp-001 RUNNING (PID 181491, ETA ~13h)\\n- 总 GPU 预算：~31h（含 D021 新增 ~7h）\\n- May 19 前有 ~72h 窗口，单 GPU 充足\\n\\n## 目标投稿\\n- 主目标：EMNLP 2026（ARR May 25）\\n- 后备：AAAI 2027（Aug 1）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D023 | 2026-05-16 | D023: Contingency plan 确认——如 SICA≤SC 则 pivot 到 Ana | exp-001, exp-010, exp-011, exp-014 |\\n| D022 | 2026-05-16 | D022: 不 kill exp-001；exp-013 ablation 改用 exp-002 数 | exp-001, exp-002, exp-013 |\\n| D021 | 2026-05-16 | D021: Scope 扩展——补 3 个非 Qwen 模型 + GSM8K 跨域 + constr | exp-010, exp-011, exp-012, exp-013, exp-014 |\\n| D020 | 2026-05-16 | D020: Kill 140题进程B，保留804题进程A以最大化统计力 | exp-001 |\\n| D019 | 2026-05-16 | exp-007 (72B-AWQ) 从 P2 提升到 P1，Claim 2 至少需要 4 个模型 | exp-007, exp-004, exp-005 |\\n| D018 | 2026-05-16 | D017: D012 PASS, MVP 通过——SICA 在有多样性输入时确实≠SC（+3.3pp | sica_d012_14b |\\n| D017 | 2026-05-16 | D017: D012 技术 PASS（C3 +3.3pp）但统计 INCONCLUSIVE（p=0. | sica_d012_14b |\\n| D016 | 2026-05-16 | D016: QwQ-32B MVP FAIL，模型 pivot 到 Qwen2.5-14B-Inst | sica_folio30, sica_proofwriter30_v2, sica_temp_diversity, sica_aime30_v3 |\\n| D015 | 2026-05-16 | D015: FOLIO C0 预检 0% 多候选率——QwQ-32B 跨三域自一致性是模型级特征，S | sica_folio30, sica_proofwriter30_v2, sica_temp_diversity |\\n| D014 | 2026-05-16 | D014: MaxSAT 结构性失效根因确认——约束编码缺 answer assertion + 提 | sica_proofwriter30_v2 |\\n\\n\", \"total_chars\": 3867, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "789e3cd7-28fe-4a0e-9e69-09b90b365e00",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "eadde8c2-733e-4ee5-8f9a-65f1decb0203",
  "sourceToolAssistantUUID": "789e3cd7-28fe-4a0e-9e69-09b90b365e00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T13:10:42.331Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YNRyx3CiY8Sfh86dMh8rgd`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eadde8c2-733e-4ee5-8f9a-65f1decb0203",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYfT92JgftavJJcSXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "753fdfef-7152-4b42-a56a-3fc3c45be92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBQKeg8352Gwsom9bmXcy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 18503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 16 · 2026-05-16T13:10:42.342Z_

<details><summary>↩ Tool result · `toolu_01YNRyx3CiY8Sfh86dMh8rgd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Fallback: AAAI 2027 (Aug 1)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## Core Claims (3 条)\\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: \\\"C0 → epistemic uncertainty\\\" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]\\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\\n\\n## Core Insight\\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from \\\"yet another ensemble method\\\" into \\\"a method with formally characterizable applicability boundaries,\\\" validated across 3 model families and multiple reasoning domains.\\n\\n## Story Spine\\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).\\n- **Headline result template**: \\\"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n1. **\\\"Gains not statistically significant\\\"** → exp-001: Expand to 804 questions for statistical power\\n2. **\\\"Only a better tiebreaker, not worth the overhead\\\"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)\\n3. **\\\"Only Qwen models — family-specific artifact?\\\"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)\\n4. **\\\"Only one reasoning model\\\"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)\\n5. **\\\"Only logic domain — restricted answer space\\\"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)\\n6. **\\\"ProofWriter shows 0pp gain\\\"** → Domain analysis in exp-001 expanded results\\n7. **\\\"Random tiebreak baseline closes the gap\\\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)\\n8. **\\\"Why not just use a reasoning model?\\\"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit\\n9. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting\\n10. **\\\"Within-family scaling?\\\"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family\\n\\n## Working Title\\n**\\\"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation\\\"**\\n(Alternatives: \\\"Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning\\\")\\n\\n## Paper Structure (EMNLP 8pp + appendix)\\n- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)\\n- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)\\n- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail\\n\\n## Claim Risk Notes\\n- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as \\\"principled weighting\\\" not \\\"satisfiability-based reasoning\\\"\\n- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \\\"binary indicator\\\" not \\\"continuous predictor\\\". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.\\n- **\\\"Epistemic uncertainty\\\" terminology**: Reserve for Discussion section only. Main text uses \\\"effective output diversity\\\" / \\\"task-relative model confidence\\\". UQ community would attack formal misuse.\\n\\n## Contingency Plan (D023)\\n**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）\\n**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)\\n- 论文主线从\\\"SICA improves accuracy\\\"转为\\\"characterizing operating conditions of symbolic consensus\\\"\\n- C0 threshold pattern 成为核心贡献（\\\"at what C0 level does SICA begin to match/exceed SC?\\\")\\n- FOLIO 正向结果嵌入为\\\"domain formality → effectiveness\\\"子 claim\\n- Claim 1 弱化为\\\"principled + interpretable tiebreaking\\\"（不 claim accuracy gain）\\n- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）\\n- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback\\n**Decision point**: exp-001 FOLIO 70题的 C0 和 delta\\n\\n## Venue Fit Risks\\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \\\"operating regime characterization\\\" — the tiebreaking mechanism is evidence, not the claim.\\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\\n- Negative results: QwQ-32B data must be presented as insight (\\\"When Does Symbolic Consensus Degenerate?\\\"), not failure.\\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\\n- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer \\\"so what should practitioners do?\\\" → C0 as deployment diagnostic.\\n\", \"total_chars\": 7354, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "753fdfef-7152-4b42-a56a-3fc3c45be92a",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "8da83b7b-c484-43b7-925d-a928f9abfc1f",
  "sourceToolAssistantUUID": "753fdfef-7152-4b42-a56a-3fc3c45be92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T13:10:42.801Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RikGbJFNe9ykxbQZ74htHS`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da83b7b-c484-43b7-925d-a928f9abfc1f",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYfT92JgftavJJcSXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc10d9e0-3474-49ba-bebe-75f3abf652dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBQKeg8352Gwsom9bmXcy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 18503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 18 · 2026-05-16T13:10:42.814Z_

<details><summary>↩ Tool result · `toolu_01RikGbJFNe9ykxbQZ74htHS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml\", \"content\": \"# Literature Map — symb_invariant_consensus (SICA)\\n# Last updated: 2026-05-16\\n# Purpose: Track related work coverage for EMNLP 2026 submission\\n\\ndimensions:\\n\\n  self_consistency_and_variants:\\n    description: \\\"Self-Consistency (SC) decoding and improvements\\\"\\n    papers:\\n      - id: wang2023sc\\n        title: \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ICLR 2023\\\"\\n        arxiv: \\\"2203.11171\\\"\\n        relevance: \\\"Foundational SC method; our primary baseline\\\"\\n        status: must_cite\\n\\n      - id: chen2024usc\\n        title: \\\"Universal Self-Consistency for Large Language Model Generation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2311.17311\\\"\\n        relevance: \\\"Extends SC to free-form answers via LLM-based selection; alternative aggregation\\\"\\n        status: must_cite\\n\\n      - id: taubenfeld2025cisc\\n        title: \\\"Confidence Improves Self-Consistency in LLMs\\\"\\n        authors: \\\"Taubenfeld et al.\\\"\\n        venue: \\\"ACL Findings 2025\\\"\\n        arxiv: \\\"2502.06233\\\"\\n        relevance: \\\"Weighted voting via model confidence; reduces samples 40-50%. Shows SC can be improved with non-uniform weighting — SICA uses constraint-based weighting instead\\\"\\n        status: must_cite\\n\\n      - id: kim2026reasc\\n        title: \\\"Reliability-Aware Adaptive Self-Consistency (ReASC)\\\"\\n        authors: \\\"Kim et al.\\\"\\n        venue: \\\"2026\\\"\\n        relevance: \\\"Response-level confidence for early halting; 70-80% cost saving vs naive SC\\\"\\n        status: should_cite\\n\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — shows SC gains plateau early and can decline at high sample counts for strong models. Directly supports our QwQ-32B finding (SICA≡SC when model is too consistent)\\\"\\n        status: must_cite\\n\\n      - id: wan2024rasc\\n        title: \\\"Reasoning-Aware Self-Consistency (RASC)\\\"\\n        authors: \\\"Wan et al.\\\"\\n        venue: \\\"2024\\\"\\n        relevance: \\\"Combines answer-level and rationale-level features; reduces samples ~88%\\\"\\n        status: should_cite\\n\\n      - id: dsc2025\\n        title: \\\"Difficulty-Adaptive Self-Consistency\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL Findings 2025\\\"\\n        relevance: \\\"Ranks problem difficulty to allocate sampling budget; complementary efficiency approach\\\"\\n        status: optional\\n\\n  symbolic_reasoning_llm:\\n    description: \\\"Neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    papers:\\n      - id: pan2023logiclm\\n        title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n        authors: \\\"Pan et al.\\\"\\n        venue: \\\"EMNLP Findings 2023\\\"\\n        arxiv: \\\"2305.12295\\\"\\n        relevance: \\\"LLM→FOL→solver pipeline; closest architectural ancestor to SICA. Key difference: Logic-LM uses single-path translation, SICA aggregates across multiple paths\\\"\\n        status: must_cite\\n\\n      - id: xu2026dylos\\n        title: \\\"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)\\\"\\n        authors: \\\"Xu et al.\\\"\\n        venue: \\\"EACL 2026\\\"\\n        arxiv: \\\"2510.06774\\\"\\n        relevance: \\\"Multi-paradigm solver selection (LP/FOL/CSP/SMT); evaluated on FOLIO+ProofWriter. Outperforms Logic-LM. Key difference: DyLoS selects solver type, SICA aggregates constraints across paths\\\"\\n        status: must_cite\\n\\n      - id: fover2025\\n        title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"TACL 2025\\\"\\n        relevance: \\\"FOL verification for NL reasoning; strong results on ProofWriter+FOLIO. Uses verification rather than aggregation\\\"\\n        status: must_cite\\n\\n      - id: li2025survey\\n        title: \\\"A Survey on LLM Symbolic Reasoning\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"2025 (under review)\\\"\\n        relevance: \\\"Comprehensive survey; positions SICA within the broader landscape\\\"\\n        status: should_cite\\n\\n      - id: constraintllm2025\\n        title: \\\"ConstraintLLM: A Neuro-Symbolic Framework for Industrial Constraint Programming\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Multi-instruction SFT for constraint extraction; different domain (industrial) but related extraction methodology\\\"\\n        status: optional\\n\\n  maxsat_constraint_nlp:\\n    description: \\\"MAX-SAT and constraint satisfaction applied to NLP/reasoning\\\"\\n    papers:\\n      - id: llm_meets_cp2025\\n        title: \\\"Large Language Model Meets Constraint Propagation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"IJCAI 2025\\\"\\n        relevance: \\\"LLM+constraint propagation integration; validates feasibility of constraint-based reasoning with LLMs\\\"\\n        status: should_cite\\n\\n      - id: satbench2025\\n        title: \\\"SATBench: Benchmarking LLMs' Logical Reasoning via SAT Problems\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Evaluates LLMs on SAT-formulated problems; establishes that LLMs struggle with pure SAT but can benefit from solver integration\\\"\\n        status: should_cite\\n\\n      - id: maxsat_local_search2025\\n        title: \\\"Optimizing Local Search-based Partial MaxSAT Solving via Initial Assignment Prediction\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Science China Information Sciences 2025\\\"\\n        relevance: \\\"Solver-side advances in partial MaxSAT; technical reference for our WPMS formulation\\\"\\n        status: optional\\n\\n  folio_proofwriter_sota:\\n    description: \\\"State-of-the-art methods on FOLIO and ProofWriter benchmarks\\\"\\n    papers:\\n      - id: logicagent2025\\n        title: \\\"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2509.24765\\\"\\n        relevance: \\\"Multi-perspective logical reasoning; SOTA on logical reasoning benchmarks including FOLIO. +7.05% average gain\\\"\\n        status: must_cite\\n\\n      - id: aristotle2025\\n        title: \\\"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"ACL 2025\\\"\\n        relevance: \\\"Logic-complete decomposition framework; strong ProofWriter/FOLIO results\\\"\\n        status: must_cite\\n\\n      - id: qi2025symbolic_provers\\n        title: \\\"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\\\"\\n        authors: \\\"Qi et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv: \\\"2502.06563\\\"\\n        relevance: \\\"LLM+symbolic prover combination; evaluated on FOLIO\\\"\\n        status: should_cite\\n\\n      - id: dissecting2025\\n        title: \\\"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP Findings 2025\\\"\\n        arxiv: \\\"2506.04810\\\"\\n        relevance: \\\"Fine-grained analysis of LLM logical reasoning capabilities on ProofWriter/FOLIO\\\"\\n        status: optional\\n\\n  reasoning_model_diversity:\\n    description: \\\"Trace diversity in reasoning vs non-reasoning models; supports our QwQ-32B finding\\\"\\n    papers:\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — strong models produce near-identical paths, SC gains plateau/decline. Direct support for SICA≡SC on QwQ-32B\\\"\\n        status: must_cite\\n\\n      - id: diversity_aware_tts2025\\n        title: \\\"Diversity-Aware Training for Test-Time Scaling\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Under review 2025\\\"\\n        relevance: \\\"Independent reasoning attempts collapse into similar solutions; diversity training needed to unlock test-time scaling. Supports our claim that non-reasoning models have more useful diversity\\\"\\n        status: must_cite\\n\\n      - id: snell2025scaling_tts\\n        title: \\\"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters\\\"\\n        authors: \\\"Snell et al.\\\"\\n        venue: \\\"ICLR 2025 (Oral)\\\"\\n        arxiv: \\\"2408.03314\\\"\\n        relevance: \\\"Foundational test-time compute scaling; shows compute-optimal strategies vary by difficulty. Contextualizes why SICA needs diverse paths\\\"\\n        status: should_cite\\n\\n      - id: deepseek_r1_2025\\n        title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n        authors: \\\"DeepSeek-AI\\\"\\n        venue: \\\"Nature 2025\\\"\\n        arxiv: \\\"2501.12948\\\"\\n        relevance: \\\"Defines the reasoning model paradigm (RL-trained extended thinking); reference for why these models are highly self-consistent\\\"\\n        status: must_cite\\n\\n      - id: base_models_reason2025\\n        title: \\\"Base Models Know How to Reason, Thinking Models Learn When\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.07364\\\"\\n        relevance: \\\"RL teaches activation timing not new skills; implies reasoning models converge to similar reasoning patterns, reducing trace diversity\\\"\\n        status: should_cite\\n\\n      - id: korikov2025sc_ranking\\n        title: \\\"The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring\\\"\\n        authors: \\\"Korikov et al.\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        arxiv: \\\"2604.26954\\\"\\n        relevance: \\\"Temperature sampling helps but ensemble size (1→7) produces no significant gains; supports diminishing returns of naive SC\\\"\\n        status: optional\\n\\n  multi_path_aggregation:\\n    description: \\\"Methods for aggregating multiple reasoning paths beyond majority voting\\\"\\n    papers:\\n      - id: rc2025\\n        title: \\\"Representation Consistency for Accurate and Coherent LLM Answer Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2506.21590\\\"\\n        relevance: \\\"Aggregation via representation similarity; down-weights incoherent reasoning. Semantic alternative to SICA's symbolic approach\\\"\\n        status: should_cite\\n\\n      - id: multi_path_plan2025\\n        title: \\\"Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.11620\\\"\\n        relevance: \\\"Multi-path aggregation at plan level rather than answer level\\\"\\n        status: optional\\n\\n      - id: crest2025\\n        title: \\\"Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL 2025\\\"\\n        relevance: \\\"Consistency as training signal rather than inference-time aggregation\\\"\\n        status: optional\\n\\ngaps:\\n  resolved: []\\n  remaining:\\n    - dimension: \\\"reasoning_model_diversity\\\"\\n      gap: \\\"No published paper explicitly studies QwQ-32B trace diversity collapse under temperature sampling. Our empirical finding (3.6% multi-candidate across 83 problems) is novel but needs positioning against Loo et al. 2025 and Diversity-Aware TTS\\\"\\n    - dimension: \\\"maxsat_constraint_nlp\\\"\\n      gap: \\\"No direct precedent for weighted partial MAX-SAT as multi-path consensus mechanism in NLI. SICA's formulation appears novel — must frame clearly in Related Work\\\"\\n    - dimension: \\\"self_consistency_and_variants\\\"\\n      gap: \\\"Should verify if CRAFT (mentioned in project docs) is a real published method or internal shorthand\\\"\\n\", \"total_chars\": 11286, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc10d9e0-3474-49ba-bebe-75f3abf652dd",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "1aafb7b2-a16e-47d7-ac57-ce1b8e8b45e1",
  "sourceToolAssistantUUID": "bc10d9e0-3474-49ba-bebe-75f3abf652dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T13:10:43.385Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01B6LVHYkpSzuuTdfBYPnpAE`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aafb7b2-a16e-47d7-ac57-ce1b8e8b45e1",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JYfT92JgftavJJcSXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89c9457d-1061-4d72-bacb-372a8cade635",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBQKeg8352Gwsom9bmXcy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 18503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 20 · 2026-05-16T13:10:43.408Z_

<details><summary>↩ Tool result · `toolu_01B6LVHYkpSzuuTdfBYPnpAE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 24\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet spot\\\"的补充验证。如果 MATH+AIME 均 SICA≈SC → 准备 FAIL 路径决策。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 12:16 UTC\\n  summary: 'D005: 采用双管齐下方案——MATH-500 MVP 继续 + AIME 30 题紧跟，暂不换模型'\\n  rationale: Temperature 诊断确认 QwQ-32B 在 T=0.7/0.9/1.0 下均产生近零答案分歧——reasoning model\\n    的确定性推理压制采样随机性。MATH-500 MVP 高概率 FAIL on C2/C3，但数据仍有价值（负面结果本身有意义）。AIME 2024 是 QwQ-32B\\n    弱项（~79.5%），更可能产生 trace 分歧——如果 SICA 在 AIME 上有信号，paper story 改为\\\"SICA 在高难度/高不确定性场景下最有价值\\\"，反而比\\\"通用提升\\\"更有深度。模型切换（Qwen2.5-7B\\n    等）改变论文定位太大，留作 AIME 也失败后的最后手段。执行顺序：MATH MVP 跑完 → AIME 30 题 → 基于两组结果做 PASS/FAIL\\n    最终判定。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 12:19 UTC\\n  summary: 'D006: Kill 当前 MATH MVP（有 bug + 25-30h 不可接受），修 bug 后 AIME 30 题优先'\\n  rationale: D005 假设 MVP 4-7h 出结果，但实际第一题 20min+ 未完成（serial trace gen + extraction\\n    回归 5/12 JSON parse fail），外推 25-30h。加上多样性诊断已定论（零分歧），继续烧 25-30h GPU 等一个几乎确定 FAIL\\n    的结果不合理。改为：(1) Kill 当前 MVP；(2) 修两个 bug——trace gen 用 n=K batch 而非串行、extraction 回归（ProofWriter\\n    prompt 合并后可能破坏了 math 域的 JSON parse）；(3) AIME 30 题优先跑（QwQ-32B 弱项，最可能出现分歧，30 题修复后\\n    ~3-4h）；(4) AIME 有信号 → 回来跑修复后的 MATH MVP；AIME 也无信号 → FAIL。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-15 16:31 UTC\\n  summary: 'D007: z3 parser 是 0pp 差距根因——并行修 parser + scorer，v3 继续跑后批量重打分'\\n  rationale: '7/30 题 Reviewer 分析发现 parse_z3_formula() 损失率 41-100%（P7: 72→1, 98.6%），LLM\\n    提取的约束在 z3 转换时被大量丢弃，MAX-SAT 无法工作。P7（SC 1/12 极度分散）是 SICA 理论最佳场景但因 parser 失效无法发挥。策略：v3\\n    继续跑收集全部 traces（最贵部分），并行修 parser + scorer，30 题完成后批量重打分作为真正 MVP 结果。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: running, 7/30 done, 0pp差距但因parser bug无效\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 17:40 UTC\\n  summary: 'D008: P5 翻转为虚假声明（硬编码），A+C 实际翻转数=0。答案提取率过低是 C3 根本瓶颈，提升为最高优先级'\\n  rationale: '调查发现 P5 \\\"120→80 flip\\\" 是 rescore_pure.py 硬编码的对照值，v3 P5 实际仅 1 个候选答案 \\\"80\\\"。P7\\n    的 72→1 也是 parser 仍无法处理（2.8% parse rate），非 dedup 逻辑 bug。11/30 中 SICA=SC 的根因是答案提取率极低（P5:\\n    1/12, P2/P8/P9/P11: 0/12），多候选竞争场景不存在，任何 scorer 都无法差异化。将答案提取改进提升为最高优先级。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 11/30 done, SICA=SC=63.6%, 0pp\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-15 17:53 UTC\\n  summary: 'D009: max_tokens=10240 截断是 0-vote 根因，修为 16384 + fallback extraction +\\n    save intermediates，v3 完成后 v4 重跑截断题'\\n  rationale: P8/P9/P11 的 0/12 答案提取全因 trace 在 10240 tokens 截断，\\\\boxed{} 未生成。P11 有 60\\n    raw constraints（11/12 提取成功）证明模型推理充分但 token 不够。trace 耗时与截断强相关：350-435s→12/12 votes,\\n    730-810s→0-1/12 votes。修复 max_tokens + fallback extraction 预计恢复 P8/P9/P11 答案，创造多候选场景让\\n    SICA 有差异化空间。v3 继续跑（非截断题有效），v4 只重跑截断题，合并为最终 MVP。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 12/30 done, P8/P9/P11 confirmed truncated at 10240 tokens\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 19:11 UTC\\n  summary: 'D010: AIME 0pp gap 是结构性的——QwQ-32B 单候选主导，SICA≡SC。MATH-50 升为关键判定实验'\\n  rationale: Reviewer 审查 22/30 题发现：所有非空 SC vote 分布仅含 1 个候选答案（unanimous among voting\\n    traces）。SICA 只能在多候选竞争时产生差异，单候选场景下无论约束打分如何都选同一答案。这不是 parser/scorer bug，是 QwQ-32B\\n    在 AIME 上答案高度一致的结构性特征（temp_diversity 实验已佐证）。v4 修复 max_tokens+fallback 可能恢复截断题的答案，但如果恢复的仍是同一答案则\\n    0pp 不变。MATH-500 Level 1-5 混合难度可能存在更多答案多样性（模型错误率 ~9.4%，错题上不同 trace 可能给出不同错答案），是验证\\n    SICA 核心假设的关键实验。调整优先级：v3 完成 → vote diversity 分析 → v4 快速验证 → MATH-50（决定性实验）。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 完成, SICA=SC=72.7%, 0pp gap, 0 题多候选\\n  depends_on:\\n  - D007\\n  - D009\\n- id: D011\\n  date: 2026-05-15 19:47 UTC\\n  summary: 'D011: Reviewer 预判 MATH-50 将重现单候选模式（已有 32 题零分歧证据），修订策略：MATH-10 快速诊断 → 逻辑域优先'\\n  rationale: Reviewer 指出 temp_diversity 实验是在 MATH L4-5 上做的（非 AIME），3 个温度 × 5 题 = 零答案分歧；加上\\n    smoke_5q（5 题 MATH）和 AIME 22 题，共 32 题零多候选。QwQ-32B 答案一致性是模型级特征（CoT 链逻辑约束远强于采样温度），非任务特定。全量\\n    MATH-50（7-8h GPU）几乎确定重现 0pp。修订策略：(1) v3 完成后做 vote diversity 分析；(2) 取消 v4 AIME\\n    re-run，改为 MATH-10 trace-only 诊断（v4 代码，~1h）验证修复 + 确认/否定单候选假设；(3) 如确认单候选 → 立即转向\\n    ProofWriter + FOLIO 作为主实验（逻辑域 FOL 规范化程度高、answer distribution 天然多候选、Z3 parser 损耗低）；(4)\\n    MATH/AIME 数据保留为 domain boundary 分析。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 单候选\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: MATH L4-5 三温度零分歧\\n  - exp_id: smoke_5q\\n    role: evidence\\n    result: 5题MATH单候选\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-15 22:24 UTC\\n  summary: 'D012: 逻辑域 MVP 判定标准——ProofWriter-30 + FOLIO-30 合并 60 题，沿用 D003 框架 + 新增多候选前置条件'\\n  rationale: 'D011 将主实验从 MATH-500 pivot 到逻辑域，但 D003 判定标准仍针对 MATH-500，ProofWriter 定位仅为\\\"sanity\\n    check 不影响 PASS/FAIL\\\"。Reviewer 指出 proofwriter30_v2 完成后无法判定。新标准沿用 D003 框架（保持一致性避免\\n    goalpost-moving），新增多候选前置条件（吸取 AIME/MATH 教训）：\\n\\n\\n    PASS（全部满足）：\\n\\n    - C1: 约束提取率 ≥ 50%\\n\\n    - C2: 跨路径矛盾检出 ≥ 5 题（绝对数）\\n\\n    - C3: SICA accuracy ≥ SC + 2pp（合并 60 题），或 paired bootstrap p < 0.1\\n\\n    - C0（前置）: 多候选率 ≥ 20%（≥12/60 题有 >1 个 unique candidate）\\n\\n\\n    INCONCLUSIVE（触发扩展重测）：\\n\\n    - C3 为 +0~2pp，其余满足\\n\\n\\n    FAIL（任一触发）：\\n\\n    - C0 < 20% 多候选 → 结构性失效，同 MATH/AIME\\n\\n    - C1 < 30%\\n\\n    - C2 < 3 题\\n\\n    - C3 < SC\\n\\n\\n    ProofWriter-30 和 FOLIO-30 合并判定（60 题），但分别报告以观察域差异。'\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: target\\n    result: running\\n  - exp_id: sica_folio30\\n    role: target\\n    result: planned\\n  depends_on:\\n  - D003\\n  - D011\\n- id: D013\\n  date: 2026-05-16 01:30 UTC\\n  summary: 'D013: ProofWriter 中期 CRITICAL——MaxSAT 结构性失效(16/16 excluded=0)，终止当前实验，紧急诊断根因后再决定\\n    FOLIO'\\n  rationale: Reviewer 独立核实 16/30 题中期数据：C0/C1/C2/C3 四项全 FAIL。最关键的是 C2=0（矛盾检出为零），MaxSAT\\n    satisfied_ratio=1.000 贯穿全部问题，SICA 核心机制从未激活。C3=-6.25pp 说明 SICA 不仅无效还主动伤害准确率。继续跑剩余\\n    14 题无意义。需紧急诊断 MaxSAT 全满足的根因：(a) 约束太粗/抽象无法矛盾→设计缺陷 (b) SAT 编码 bug→可修 (c) 去重后约束太少→可调。根因决定\\n    FOLIO 是否值得跑以及 MVP 是否有救。May 19 checkpoint 仅剩 3 天。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: primary\\n    result: C2=0 structural failure, all 4 D012 criteria FAIL at midpoint\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-16 01:39 UTC\\n  summary: 'D014: MaxSAT 结构性失效根因确认——约束编码缺 answer assertion + 提取失败率 54%。选 A 方案：L3+L1\\n    修复 → 5 题验证 → 全量'\\n  rationale: 诊断 6/6 注入测试通过证明 MaxSAT 求解器无 bug。satisfied_ratio=1.0 的根因是：(1) 不同答案的 trace\\n    未注入 answer assertion 约束，MaxSAT 无法产生冲突；(2) 提取失败率 54.4%（QwQ 重新推理而非输出 JSON）。L3 修复（注入\\n    answer==trace_answer）是 SICA 能否工作的架构前提，L1（prompt 强制 JSON）是质量保障。先 5 题验证再全量，避免浪费\\n    GPU。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: trigger\\n    result: MaxSAT 16/16 satisfied_ratio=1.0, SICA worse than SC by 6.2pp\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-16 02:48 UTC\\n  summary: 'D015: FOLIO C0 预检 0% 多候选率——QwQ-32B 跨三域自一致性是模型级特征，SICA 核心前提（trace 分歧）不成立。等\\n    L3+L1 五题验证后做最终 MVP 判定。'\\n  rationale: FOLIO 10 题 K=6 traces 全部 unanimous（0% 多候选），与 AIME 0%、ProofWriter 18.8%\\n    汇总后，C0 合并判定确定性 FAIL（远低于 ≥20% 门槛）。QwQ-32B 在数学+逻辑+FOL 三个域均表现出极高 trace 一致性，SICA 的差异化空间不存在。5\\n    题 L3+L1 验证仍在跑，用于确认机制 soundness（与使用场景独立），完成后做最终 MVP 判定。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: C0 precheck\\n    result: 0/10 multi-candidate, all unanimous\\n  - exp_id: sica_proofwriter30_v2\\n    role: context\\n    result: 3/16 multi-candidate = 18.8%\\n  - exp_id: sica_temp_diversity\\n    role: context\\n    result: 0% diversity across 3 temperatures\\n  depends_on:\\n  - D012\\n  - D014\\n- id: D016\\n  date: 2026-05-16 02:51 UTC\\n  summary: 'D016: QwQ-32B MVP FAIL，模型 pivot 到 Qwen2.5-14B-Instruct——全域 C0=3.6% 远低于\\n    20% 阈值，模型级自一致性使 SICA≡SC，切换非 reasoning model 验证算法本身有效性'\\n  rationale: 全域证据（MATH 0%, AIME 0%, ProofWriter 18.75%, FOLIO 0%，合并 3/83=3.6%）确认 QwQ-32B\\n    自一致性是模型级特征而非域特征。SICA 算法需要多候选输入才能与 SC 产生差异。模型替换是唯一可测试\\\"算法本身是否有效\\\"的路径。选择 Qwen2.5-14B-Instruct：非\\n    reasoning model 采样多样性高、14B 在 98GB GPU 上轻松部署、Qwen2.5 系列逻辑能力强。预计 C0 预检 1h + 完整评估\\n    4h，May 19 checkpoint 可控。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: trigger\\n    result: FOLIO C0=0%\\n  - exp_id: sica_proofwriter30_v2\\n    role: evidence\\n    result: ProofWriter C0=18.75%\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: 3 temps 0% diversity\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: AIME 0pp gap\\n  depends_on:\\n  - D012\\n  - D015\\n- id: D017\\n  date: 2026-05-16 05:11 UTC\\n  summary: 'D017: D012 技术 PASS（C3 +3.3pp）但统计 INCONCLUSIVE（p=0.317）——全部增益来自 4 个 6:6\\n    tiebreak，SICA 机制是 principled tiebreaking 而非 constraint override。扩展实验到 200 题 +\\n    K 敏感性分析争取统计效力'\\n  rationale: 60 题中仅 4 题 SICA≠SC，全部为 6:6 精确平票。56 个非平票题 SICA=SC（约束从未推翻明确多数）。McNemar\\n    p=0.317，二项检验 p=0.3125，均不显著。FOLIO +6.7pp 但 ProofWriter 0pp，域泛化不成立。SICA 的实际贡献是 principled\\n    tiebreaking 而非原始假设的 symbolic constraint override。需要更多数据点来判断 tiebreaking 模式是否稳定可复现。扩展到全量\\n    PW+FOLIO + K=8/16/20 敏感性分析是最高效的统计加固路径。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: evidence\\n    result: C3 +3.3pp, p=0.317, 4 tiebreaks only\\n  depends_on:\\n  - D016\\n  - D012\\n- id: D018\\n  date: 2026-05-16 05:14 UTC\\n  summary: 'D017: D012 PASS, MVP 通过——SICA 在有多样性输入时确实≠SC（+3.3pp），核心假设验证。研究阶段首要任务：扩大样本量\\n    + tiebreak 基线分析 + K 消融'\\n  rationale: D012 四项标准全部技术达标：C0=53.3%, C1=100%, C2=34题, C3=+3.3pp。但 C3 实质弱点明确：全部增益来自\\n    4 个 6:6 平票（SICA 3/4 正确 vs SC 1/4），p=0.317 不显著，FOLIO +6.7pp / PW 0pp。MVP 标准以 OR\\n    条件通过（+3.3pp ≥ +2pp），核心假设\\\"SICA 在有多样性输入时≠SC\\\"已验证——机制是 principled tiebreaking via\\n    constraint weights。模型对照（QwQ-32B C0=3.6%, SICA≡SC）强化了\\\"多样性是 SICA 前提\\\"的结论。研究阶段需解决统计弱点：扩展到\\n    200+ 题、K sensitivity、random tiebreak baseline。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: primary\\n    result: SICA 73.3% vs SC 70.0%, +3.3pp, 4 tiebreaks, p=0.317\\n  depends_on:\\n  - D012\\n  - D016\\n- id: D019\\n  date: 2026-05-16 05:22 UTC\\n  summary: exp-007 (72B-AWQ) 从 P2 提升到 P1，Claim 2 至少需要 4 个模型\\n  rationale: Reviewer 指出 Claim 2 \\\"Operating Regime Characterization\\\" 仅有 QwQ-32B 和\\n    Qwen2.5-14B 两个模型，不足以支撑 \\\"model property, not task property\\\" 的论断。加上 exp-004 (7B)\\n    也只有 3 个模型。72B-AWQ 补齐后形成 7B/14B/72B instruction + 32B reasoning 的完整 scaling 证据链，4\\n    个模型是 \\\"operating regime\\\" claim 的最低门槛。GPU 时间预算 ~4h，串行排在 exp-002 和 exp-004 之后，总计\\n    ~22.5h，May 25 DDL 前充裕。\\n  related_experiments:\\n  - exp_id: exp-007\\n    role: promoted to P1\\n  - exp_id: exp-004\\n    role: P1 scaling point\\n  - exp_id: exp-005\\n    role: existing QwQ-32B data\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-16 05:29 UTC\\n  summary: 'D020: Kill 140题进程B，保留804题进程A以最大化统计力'\\n  rationale: Reviewer 发现两个进程同时请求 vLLM（违反独占规则）。进程A（PID 181491，804题 PW+FOLIO）预计~67个tie，统计力远优于进程B（140题，~12个tie）。13.4h\\n    ETA 在 May 19 checkpoint 前充裕。MVP 核心瓶颈是 p=0.317 统计不显著，最大化 N 是第一优先。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: target\\n    result: 保留804题运行，kill 140题重复进程\\n  depends_on: []\\n- id: D021\\n  date: 2026-05-16 06:16 UTC\\n  summary: 'D021: Scope 扩展——补 3 个非 Qwen 模型 + GSM8K 跨域 + constraint ablation，Claim\\n    2 reframe 为 C0=epistemic uncertainty'\\n  rationale: 用户指出 scope 不足，Reviewer 审计确认：(1) 全 Qwen 家族是 Claim 2 致命弱点 (critical)；(2)\\n    单域数据无法支撑 \\\"model property not task property\\\"；(3) 缺 constraint ablation 防御 \\\"over-engineering\\\"\\n    attack。补 Mistral-7B + LLaMA-8B + DeepSeek-R1-7B（跨 3 家族 + reasoning 第二点）+ GSM8K\\n    30题 pilot（跨域）+ CPU constraint ablation。总额外 GPU ~7h，May 25 ARR 前充裕。Claim 2 从 \\\"model\\n    architecture determines regime\\\" 升级为 \\\"C0 tracks epistemic uncertainty, correlates\\n    with but not identical to architecture\\\"。\\n  related_experiments:\\n  - exp_id: exp-010\\n    role: new\\n    result: planned\\n  - exp_id: exp-011\\n    role: new\\n    result: planned\\n  - exp_id: exp-012\\n    role: new\\n    result: planned\\n  - exp_id: exp-013\\n    role: new\\n    result: planned\\n  - exp_id: exp-014\\n    role: new\\n    result: planned\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-16 08:18 UTC\\n  summary: 'D022: 不 kill exp-001；exp-013 ablation 改用 exp-002 数据（新 pipeline 含 raw_constraints）'\\n  rationale: pipeline.py 的 raw_constraints 修改在 exp-001 启动后（16:04 vs 13:19），运行中进程不热更新，导致\\n    exp-001 结果中 raw_constraints 全空。三个选项评估：(A) kill+resume 有风险且前 162 题仍缺数据；(B) 全量重跑浪费\\n    3h；(C) 近似模式说服力弱。选择 Option D：保持 exp-001 不动（SICA vs SC 主结果不受影响），exp-013 ablation\\n    改在 exp-002（K ablation, 60题×5K, 新 pipeline）数据上运行。exp-002 的 D012 子集 C0~53%，约 32\\n    题多候选 × 5K = 160 个多候选评估点，统计充足。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: 保持运行\\n    result: running\\n  - exp_id: exp-002\\n    role: ablation 数据源\\n    result: planned\\n  - exp_id: exp-013\\n    role: 策略变更\\n    result: planned\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-16 08:27 UTC\\n  summary: 'D023: Contingency plan 确认——如 SICA≤SC 则 pivot 到 Analysis Paper (Option\\n    A)，FOLIO 正向则嵌入为子 claim (Option C)'\\n  rationale: exp-001 中间结果 (N=157 PW) SICA-SC gap 反转至 -1.27pp，tiebreak win 降至 50%。Reviewer\\n    评估三方案：A (Analysis Paper, Main 30-35% / Findings 60-70%)、B (Negative Result, Main\\n    15-25%)、C (Domain-Specific if FOLIO翻盘, Main 25-35%)。选 A 为主线：论文价值从\\\"SICA 提升准确率\\\"转向\\\"理解\\n    symbolic consensus 的 operating conditions\\\"。C0 threshold pattern 成为核心贡献。Option\\n    C 嵌入 A（如 FOLIO 正向则作为\\\"domain formality → effectiveness\\\"子 claim）。不选 B（天花板低、NLP 社区对负面结果接受度有限）。决策点：exp-001\\n    FOLIO 70 题的 C0 和 delta。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: 决策依赖\\n    result: running\\n  - exp_id: exp-010\\n    role: cross-family 关键数据\\n    result: planned\\n  - exp_id: exp-011\\n    role: cross-family 关键数据\\n    result: planned\\n  - exp_id: exp-014\\n    role: reasoning 泛化\\n    result: planned\\n  depends_on:\\n  - D021\\n  - D022\\n\", \"total_chars\": 14955, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89c9457d-1061-4d72-bacb-372a8cade635",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "b4e586e2-d6c1-4971-afc9-73e63288f9af",
  "sourceToolAssistantUUID": "89c9457d-1061-4d72-bacb-372a8cade635",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T13:10:46.441Z_

Now let me read the actual paper and experiment artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4e586e2-d6c1-4971-afc9-73e63288f9af",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JZ2koAvJ2E6x2i9vQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5940fc8e-8fa4-4c46-8edd-a5e4b81c6e00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtP2XJVUQ8uBDF8QhTB8Tc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19057,
      "cache_read_input_tokens": 20954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19057,
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

_source line 22 · 2026-05-16T13:10:47.927Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01A6qEXPJYFt2Dp6Kyt6Uo96`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5940fc8e-8fa4-4c46-8edd-a5e4b81c6e00",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JZ2koAvJ2E6x2i9vQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0894250-1777-4781-a80b-4b3bb0f2f8a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtP2XJVUQ8uBDF8QhTB8Tc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19057,
      "cache_read_input_tokens": 20954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19057,
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

_source line 23 · 2026-05-16T13:10:47.950Z_

<details><summary>↩ Tool result · `toolu_01A6qEXPJYFt2Dp6Kyt6Uo96`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0894250-1777-4781-a80b-4b3bb0f2f8a3",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "ad57a473-7d6e-4669-9551-f4b188c2b349",
  "sourceToolAssistantUUID": "a0894250-1777-4781-a80b-4b3bb0f2f8a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T13:10:48.834Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AHGZtqbKLP7sCj7GQwRBmg`</summary>

```json
{
  "pattern": "**/artifacts/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad57a473-7d6e-4669-9551-f4b188c2b349",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JZ2koAvJ2E6x2i9vQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82d6fa27-9935-4feb-a6dc-48bf0f4dd2e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtP2XJVUQ8uBDF8QhTB8Tc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19057,
      "cache_read_input_tokens": 20954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19057,
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

_source line 25 · 2026-05-16T13:10:48.855Z_

<details><summary>↩ Tool result · `toolu_01AHGZtqbKLP7sCj7GQwRBmg`</summary>

```text
artifacts/crd_audit_report.md
artifacts/sica_aime30_v2/intermediate/extraction_hang_fix.md
artifacts/_project/report/code_verify_report.md
artifacts/code_verify_report.md
artifacts/aime30_v2_partial_analysis.md
artifacts/sica_aime30_v2/report/aime30_v2_partial_analysis.md
artifacts/_project/report/scorer_improvement_analysis.md
artifacts/_project/report/scorer_ac_implementation.md
artifacts/_project/report/z3_parser_comprehensive_fix.md
artifacts/_project/report/math_domain_negative_analysis.md
artifacts/report_proofwriter30_v2_progress.md
artifacts/proofwriter30_v2/report/proofwriter30_v2_interim_analysis.md
artifacts/proofwriter30_v2_interim_analysis.md
artifacts/_project/report/maxsat_diagnosis_proofwriter30_v2.md
artifacts/maxsat_diagnosis_proofwriter30_v2.md
artifacts/sica_folio30/report/folio_c0_precheck_report.md
artifacts/folio_c0_precheck_report.md
artifacts/_project/report/d016_model_pivot_report.md
artifacts/d016_model_pivot_report.md
artifacts/_project/report/paper_prep_audit.md
artifacts/sica_d012_14b/report/d012_report_sica_d012_14b.md
artifacts/sica_d012_14b/report/tiebreak_analysis_report.md
artifacts/dream_reports/dream_20260516T051642/best/paper_framing.md
artifacts/exp-005/report/qwq_operating_regime.md
artifacts/dream_reports/dream_20260516T051642/median/paper_framing.md
artifacts/dream_reports/dream_20260516T051642/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/best/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/median/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/median/review_report.md
artifacts/dream_reports/dream_20260516T054054/best/review_report.md
artifacts/dream_reports/dream_20260516T054054/worst/review_report.md
artifacts/dream_reports/dream_20260516T124139/best/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82d6fa27-9935-4feb-a6dc-48bf0f4dd2e8",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "0ecb64d4-2ce1-4360-975a-8d64d0092ec4",
  "sourceToolAssistantUUID": "82d6fa27-9935-4feb-a6dc-48bf0f4dd2e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T13:10:49.348Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Bf21ouYZSjDWyo3xQsKds5`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ecb64d4-2ce1-4360-975a-8d64d0092ec4",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JZ2koAvJ2E6x2i9vQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc0e782b-f884-4435-bcc0-5a43f50062a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtP2XJVUQ8uBDF8QhTB8Tc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19057,
      "cache_read_input_tokens": 20954,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19057
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 20954,
          "cache_creation_input_tokens": 19057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19057,
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

_source line 27 · 2026-05-16T13:10:49.360Z_

<details><summary>↩ Tool result · `toolu_01Bf21ouYZSjDWyo3xQsKds5`</summary>

```text
literature_map.yaml
artifacts/dream_reports/dream_20260516T051642/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T051642/median/imagined_experiments.yaml
registry.yaml
artifacts/dream_reports/dream_20260516T051642/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T054054/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T054054/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T054054/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T054054/best/review_context.yaml
artifacts/dream_reports/dream_20260516T054054/median/review_context.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260516T054054/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T054054/meta.yaml
artifacts/manifest.yaml
decisions.yaml
artifacts/dream_reports/dream_20260516T124139/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T124139/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T124139/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260516T124139/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc0e782b-f884-4435-bcc0-5a43f50062a8",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "d805a242-b87a-4058-8903-fedf3c46e6fd",
  "sourceToolAssistantUUID": "cc0e782b-f884-4435-bcc0-5a43f50062a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T13:10:52.077Z_

<details open><summary>🔧 Tool call — Read · `toolu_018YKVZtpdWCvZNhSwFsc6QM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d805a242-b87a-4058-8903-fedf3c46e6fd",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JZU9XAZzhN1kWeizkZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "987840b6-611d-481a-98d2-0b04a7dd3f2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EivKqKCFk64ApwJYGJoyiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1581,
      "cache_read_input_tokens": 40011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1581,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 29 · 2026-05-16T13:10:52.094Z_

<details><summary>↩ Tool result · `toolu_018YKVZtpdWCvZNhSwFsc6QM`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb,amsfonts}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage[margin=2.5cm]{geometry}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	\usepackage{enumitem}
15	
16	\newcommand{\sica}{\textsc{Sica}}
17	\newcommand{\selfcon}{\textsc{SC}}
18	\newcommand{\czero}{C_0}
19	
20	\title{When Does Symbolic Consensus Help?\\Characterizing the Operating Regime of\\Constraint-Based Reasoning Aggregation}
21	
22	\author{
23	  Anonymous EMNLP Submission
24	}
25	\date{}
26	
27	\begin{document}
28	\maketitle
29	
30	% ============================================================
31	\begin{abstract}
32	Self-Consistency (SC) aggregates multiple LLM reasoning traces via majority voting but discards the logical structure within each trace.
33	When votes tie, SC falls back to arbitrary rules---random selection, alphabetical ordering---with no principled resolution.
34	We propose \emph{Symbolic Invariant Consensus Aggregation} (\sica{}), which extracts first-order logic constraints from reasoning traces and resolves ties through weighted partial MAX-SAT.
35	On FOLIO with Qwen2.5-14B-Instruct ($n{=}204$), \sica{} achieves 82.4\% vs.\ SC's 75.5\% (+6.9\,pp, $p{=}0.023$ bootstrap), with a tiebreak win rate of 78\% on 41 tied instances compared to 50\% for random tiebreaking.
36	We show that \sica{}'s effectiveness is governed by \emph{trace diversity} ($\czero{}$, the multi-candidate rate): \sica{} adds value when $\czero{}>20\%$ but degenerates to SC when $\czero{}<5\%$.
37	Across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and 2 domains (logic, math), $\czero{}$ predicts the \sica{}--SC gap with Pearson $r{=}0.91$ ($n{=}14$ configurations), enabling practitioners to decide whether to deploy \sica{} from a single SC run at zero additional cost.
38	\end{abstract}
39	
40	
41	% ============================================================
42	\section{Introduction}
43	\label{sec:intro}
44	
45	Self-Consistency \cite{wang2023selfconsistency} improves LLM reasoning by sampling multiple chain-of-thought traces and selecting the most frequent answer.
46	This simple majority-vote mechanism has become a standard inference-time technique, yet it treats each reasoning trace as an opaque ballot, discarding the logical structure within.
47	When two or more answers receive equal votes---a common occurrence with even-numbered sample sizes ($K$) and multi-class answer spaces---SC resorts to arbitrary tiebreaking (random, alphabetical, or first-seen), forfeiting a principled resolution opportunity.
48	
49	We propose \textbf{Symbolic Invariant Consensus Aggregation} (\sica{}), a post-hoc aggregation method that extracts first-order logic (FOL) constraints from each reasoning trace and uses weighted partial MAX-SAT solving to identify the answer best supported by the collective constraint set.
50	\sica{} does not modify the generation process: it operates on the same $K$ traces that SC uses, adding only a constraint-extraction and satisfiability-checking step.
51	
52	Our central finding is that symbolic consensus does \emph{not} uniformly improve reasoning.
53	Instead, its effectiveness is governed by \emph{trace diversity}, which we operationalize as $\czero{}$---the fraction of problems where the $K$ sampled traces produce more than one distinct candidate answer.
54	When $\czero{}$ is high (instruction-tuned models on challenging tasks), voting ties are frequent and \sica{}'s constraint-based tiebreaking yields substantial gains.
55	When $\czero{}$ is low (reasoning-specialized models or easy tasks), traces converge and \sica{} degenerates to SC.
56	This regime characterization transforms \sica{} from ``yet another ensemble method'' into a method with formally characterizable applicability boundaries.
57	
58	Our contributions are:
59	\begin{enumerate}[nosep,leftmargin=*]
60	  \item \textbf{Principled tiebreaking}: \sica{} resolves SC voting ties with 77\% accuracy vs.\ 50\% for random tiebreaking across 129 tied instances, yielding +6.9\,pp on FOLIO ($p{<}0.05$).
61	  \item \textbf{Operating regime characterization}: We show that $\czero{}$ determines whether \sica{} adds value ($\czero{}>20\%$) or degenerates ($\czero{}<5\%$), validated across 3 model families and 2 reasoning architectures.
62	  \item \textbf{$\czero{}$ as zero-cost diagnostic}: $\czero{}$ predicts the \sica{}--SC accuracy gap with $r{=}0.91$ across 14 model-task configurations, enabling deployment decisions from a single SC run.
63	\end{enumerate}
64	
65	
66	% ============================================================
67	\section{Related Work}
68	\label{sec:related}
69	
70	\paragraph{Self-Consistency and voting methods.}
71	Self-Consistency \cite{wang2023selfconsistency} samples diverse reasoning paths and marginalizes over them via majority voting.
72	Universal Self-Consistency \cite{chen2023universal} extends this to free-form outputs but remains voting-based.
73	Neither method exploits the internal logical structure of reasoning traces, and neither characterizes when voting-based aggregation is sufficient versus when richer aggregation is needed.
74	
75	\paragraph{Symbolic reasoning with LLMs.}
76	Recent work integrates symbolic solvers with LLM reasoning: Logic-LM \cite{pan2023logiclm} translates problems into symbolic form for external solvers, and LINC \cite{olausson2023linc} uses LLMs to generate formal proofs.
77	These approaches replace LLM reasoning with symbolic execution; \sica{} instead uses symbolic structure to \emph{aggregate} multiple LLM reasoning paths, preserving the benefits of diverse sampling.
78	
79	\paragraph{Uncertainty quantification in LLMs.}
80	Semantic entropy \cite{kuhn2023semantic} and verbalized confidence \cite{xiong2024llms} estimate LLM uncertainty.
81	Our $\czero{}$ metric captures a related but distinct quantity---effective output diversity under sampling---and serves as a deployment diagnostic rather than a calibration measure.
82	
83	
84	% ============================================================
85	\section{Method}
86	\label{sec:method}
87	
88	\subsection{Overview}
89	
90	Given a question $q$ and a language model $\mathcal{M}$, \sica{} operates in four stages:
91	
92	\begin{enumerate}[nosep,leftmargin=*]
93	  \item \textbf{Trace sampling}: Sample $K$ reasoning traces $\{(r_i, a_i)\}_{i=1}^{K}$ from $\mathcal{M}$ at temperature $T$, where $r_i$ is the chain-of-thought and $a_i$ is the extracted answer.
94	  \item \textbf{Constraint extraction}: For each trace $r_i$, prompt $\mathcal{M}$ to extract a set of FOL constraints $\mathcal{C}_i = \{c_{i,1}, \ldots, c_{i,m_i}\}$ that the reasoning implicitly relies upon.
95	  \item \textbf{Weighted MAX-SAT aggregation}: Pool all constraints $\mathcal{C} = \bigcup_i \mathcal{C}_i$, assign weights based on constraint frequency and trace confidence, and solve a weighted partial MAX-SAT instance to find the answer that maximizes global constraint satisfaction.
96	  \item \textbf{Answer selection}: If the MAX-SAT solution yields a unique best answer, return it; otherwise, fall back to the SC majority vote.
97	\end{enumerate}
98	
99	\subsection{Constraint Extraction}
100	
101	Each reasoning trace $r_i$ is processed by the same model $\mathcal{M}$ with a structured prompt that requests FOL predicates capturing the logical relationships in the trace.
102	For a FOLIO-style NLI problem, constraints take the form of universally or existentially quantified formulas (e.g., $\forall x\, (\text{Manager}(x) \to \text{Employee}(x))$).
103	We use self-extraction (the same model that generated the trace) to avoid introducing a separate extraction model.
104	
105	\subsection{Weighted Partial MAX-SAT}
106	
107	Let $\mathcal{A} = \{a^{(1)}, \ldots, a^{(L)}\}$ be the set of distinct candidate answers.
108	For each candidate $a^{(j)}$, we construct a partial MAX-SAT instance where the hard clauses encode the candidate's truth assignment and the soft clauses are the pooled constraints $\mathcal{C}$, each weighted by its occurrence frequency across traces.
109	The candidate whose MAX-SAT instance achieves the highest total satisfied weight is selected:
110	\begin{equation}
111	  a^* = \arg\max_{a^{(j)} \in \mathcal{A}} \sum_{c \in \mathcal{C}} w_c \cdot \mathbf{1}[\text{SAT}(c \mid a^{(j)})]
112	\end{equation}
113	where $w_c$ is the weight of constraint $c$ and $\text{SAT}(c \mid a^{(j)})$ indicates whether $c$ is satisfiable under the assignment implied by $a^{(j)}$.
114	We use Z3's PB-MaxSAT solver, which handles instances of ${\sim}145$ clauses in under 1 second on average.
115	
116	\subsection{Trace Diversity Metric: $\czero{}$}
117	
118	We define the \textbf{multi-candidate rate} $\czero{}$ as the fraction of problems in a dataset where the $K$ sampled traces produce more than one distinct candidate answer:
119	\begin{equation}
120	  \czero{} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}\!\left[|\{a_1^{(i)}, \ldots, a_K^{(i)}\}| > 1\right]
121	\end{equation}
122	$\czero{}$ is computed from the SC sampling pass alone and requires no additional inference.
123	It captures effective output diversity: models that are highly confident (strong models, easy tasks, reasoning-trained) produce low $\czero{}$; models with genuine uncertainty produce high $\czero{}$.
124	
125	
126	% ============================================================
127	\section{Experimental Setup}
128	\label{sec:setup}
129	
130	\paragraph{Benchmarks.}
131	We evaluate on \textbf{FOLIO} \cite{han2022folio}, a first-order logic NLI benchmark with 3-class labels (\textsc{True}, \textsc{False}, \textsc{Unknown}), and \textbf{ProofWriter} \cite{tafjord2021proofwriter} (depth-5), a binary logical reasoning benchmark (\textsc{True}, \textsc{False}).
132	For cross-domain validation, we include a 30-question pilot on \textbf{GSM8K} \cite{cobbe2021gsm8k}.
133	Our primary evaluation uses 204 FOLIO and 600 ProofWriter questions ($n{=}804$ combined) for the main model (Qwen2.5-14B-Instruct), and a 60-question subset (10 FOLIO + 50 ProofWriter, denoted D012) for scaling and cross-family experiments.
134	
135	\paragraph{Models.}
136	We evaluate 7 model configurations spanning 3 families and 2 training paradigms:
137	\begin{itemize}[nosep,leftmargin=*]
138	  \item \textbf{Instruction models}: Qwen2.5-7B/14B/72B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct
139	  \item \textbf{Reasoning models}: QwQ-32B, DeepSeek-R1-Distill-LLaMA-8B
140	\end{itemize}
141	All experiments use $K{=}12$ traces at temperature $T{=}0.7$ unless otherwise noted.
142	
143	\paragraph{Baselines.}
144	We compare \sica{} against SC with four tiebreak rules: \textbf{SC-Random} (uniform random among tied candidates), \textbf{SC-Alphabetical} (first in lexicographic order), \textbf{SC-First-Seen} (earliest generated candidate), and plain \textbf{SC} (random, the standard default).
145	
146	\paragraph{Statistical testing.}
147	We report bootstrap confidence intervals (10,000 resamples) for all accuracy comparisons.
148	
149	
150	% ============================================================
151	\section{Results}
152	\label{sec:results}
153	
154	\subsection{Main Results}
155	\label{sec:main-results}
156	
157	Table~\ref{tab:main} presents accuracy across all model configurations.
158	
159	\begin{table*}[t]
160	\centering
161	\caption{Main results: \sica{} vs.\ Self-Consistency (SC) accuracy (\%). $\czero{}$ is multi-candidate rate. $\Delta$ is \sica{}$-$SC in percentage points. Results for Qwen2.5-14B are on the full 804-question set; others on D012 (60 questions). $^\dagger$GSM8K pilot (30 questions). $^\ddagger$Reasoning models. Bold indicates the better method per row.}
162	\label{tab:main}
163	\small
164	\begin{tabular}{@{}l c rrr rrr rrr@{}}
165	\toprule
166	& & \multicolumn{3}{c}{\textbf{FOLIO}} & \multicolumn{3}{c}{\textbf{ProofWriter}} & \multicolumn{3}{c}{\textbf{Combined}} \\
167	\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11}
168	\textbf{Model} & $\czero{}$ & \sica{} & SC & $\Delta$ & \sica{} & SC & $\Delta$ & \sica{} & SC & $\Delta$ \\
169	\midrule
170	Qwen2.5-7B   & 0.65 & \textbf{73.3} & 63.3 & +10.0 & \textbf{65.0} & 60.4 & +4.6 & \textbf{68.3} & 61.7 & +6.7 \\
171	Qwen2.5-14B  & 0.46 & \textbf{82.4} & 75.5 & +6.9  & \textbf{70.5} & 69.3 & +1.2 & \textbf{73.5} & 70.9 & +2.6 \\
172	Qwen2.5-72B\textsc{-awq} & 0.25 & \textbf{86.7} & 83.3 & +3.3  & \textbf{78.3} & 77.5 & +0.8 & \textbf{81.7} & 80.0 & +1.7 \\
173	Mistral-7B   & 0.42 & \textbf{73.3} & 63.3 & +10.0 & \textbf{62.5} & 60.4 & +2.1 & \textbf{66.7} & 61.7 & +5.0 \\
174	LLaMA-3.1-8B & 0.40 & \textbf{70.0} & 60.0 & +10.0 & \textbf{61.7} & 60.0 & +1.7 & \textbf{65.0} & 60.0 & +5.0 \\
175	\midrule
176	QwQ-32B$^\ddagger$       & 0.04 & 73.3 & 73.3 & 0.0  & 70.8 & 70.8 & 0.0  & 71.7 & 71.7 & 0.0 \\
177	DS-R1-LLaMA-8B$^\ddagger$ & 0.03 & 73.3 & 73.3 & 0.0  & 70.8 & 70.8 & 0.0  & 71.7 & 71.7 & 0.0 \\
178	\midrule
179	Qwen2.5-14B$^\dagger$ (GSM8K) & 0.10 & \multicolumn{3}{c}{---} & \multicolumn{3}{c}{---} & 90.0 & 90.0 & 0.0 \\
180	\bottomrule
181	\end{tabular}
182	\end{table*}
183	
184	\sica{} consistently outperforms SC across all five instruction-tuned models, with gains ranging from +1.7\,pp (72B-AWQ) to +6.7\,pp (7B).
185	FOLIO shows the largest improvements (+6.9 to +10.0\,pp) due to its 3-class answer space, which produces more voting ties than ProofWriter's binary labels.
186	On the 804-question expanded evaluation with Qwen2.5-14B, the FOLIO improvement is statistically significant ($p{=}0.023$, bootstrap); the combined improvement of +2.6\,pp reaches $p{=}0.072$.
187	
188	Both reasoning models (QwQ-32B and DeepSeek-R1-Distill-LLaMA-8B) show $\czero{}<5\%$ and zero \sica{} gain, confirming that reasoning-trained models' deterministic inference renders symbolic consensus redundant.
189	The GSM8K pilot with Qwen2.5-14B ($\czero{}{=}0.10$) similarly shows no gain, demonstrating that $\czero{}$ captures task-relative model confidence, not a model-intrinsic property.
190	
191	
192	\subsection{Tiebreak Analysis}
193	\label{sec:tiebreak}
194	
195	Table~\ref{tab:tiebreak} isolates \sica{}'s performance on the 129 instances where SC produces a voting tie (from the 804-question Qwen2.5-14B evaluation).
196	
197	\begin{table}[t]
198	\centering
199	\caption{Tiebreak accuracy (\%) on 129 tied instances from the Qwen2.5-14B expanded evaluation. \sica{} uses MAX-SAT constraint weighting; baselines use different arbitrary rules.}
200	\label{tab:tiebreak}
201	\small
202	\begin{tabular}{@{}l ccc@{}}
203	\toprule
204	\textbf{Method} & \textbf{Overall} & \textbf{FOLIO} & \textbf{PW} \\
205	& ($n{=}129$) & ($n{=}41$) & ($n{=}88$) \\
206	\midrule
207	\sica{} (MAX-SAT)   & \textbf{77} & \textbf{80} & \textbf{75} \\
208	SC-Random            & 50 & 50 & 50 \\
209	SC-Alphabetical      & 53 & 53 & 53 \\
210	SC-First-Seen        & 47 & 47 & 47 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\sica{}'s MAX-SAT-based tiebreaking achieves 77\% accuracy on tied instances, a +27\,pp improvement over random tiebreaking.
216	The advantage is strongest on FOLIO (80\%), where FOL constraints are most naturally expressed and the 3-class label space produces more informative constraint structures.
217	SC-Alphabetical's slight edge over random (53\% vs.\ 50\%) is an artifact of label distribution (``False'' sorts first and is disproportionately correct in negation-heavy FOLIO problems), not a principled resolution.
218	
219	
220	\subsection{$\czero{}$ as a Diagnostic for \sica{} Deployment}
221	\label{sec:c0}
222	
223	Figure~\ref{fig:c0scatter} (described textually; see Appendix for data) plots $\czero{}$ against the \sica{}--SC accuracy gap across all 14 model-task-$K$ configurations evaluated in this work.
224	
225	The correlation is strong: Pearson $r{=}0.91$, Spearman $\rho{=}0.88$, $R^2{=}0.83$.
226	A linear fit yields $\Delta \approx 0.12 \cdot \czero{} - 2.1$, indicating that each 10\,pp increase in $\czero{}$ corresponds to ${\sim}1.2$\,pp additional \sica{} gain.
227	A clean threshold exists at $\czero{}{=}20\%$: all configurations above this threshold show positive \sica{}--SC gaps; all below show zero gap.
228	This binary classifier achieves 100\% accuracy on the 14 evaluated configurations.
229	
230	The 14 data points span:
231	\begin{itemize}[nosep,leftmargin=*]
232	  \item 3 model families: Qwen (7B, 14B, 72B), Mistral-7B, LLaMA-8B
233	  \item 2 reasoning architectures: QwQ-32B (Qwen-based), DeepSeek-R1 (LLaMA-based)
234	  \item 5 $K$-value variants (6, 8, 12, 16, 20) for Qwen2.5-14B
235	  \item $\czero{}$ range: 0.03--0.65
236	\end{itemize}
237	
238	The reasoning models cluster at the origin ($\czero{}<5\%$, $\Delta{=}0$), while instruction models distribute along the trend line with $\czero{}$ monotonically decreasing with model scale (7B: 0.65 $\to$ 14B: 0.46 $\to$ 72B: 0.25).
239	This validates $\czero{}$ as a continuous predictor---not merely a binary indicator---of \sica{}'s utility, reflecting the interaction between model confidence and task difficulty.
240	
241	
242	\subsection{$K$ Sensitivity Analysis}
243	\label{sec:ksensitivity}
244	
245	Table~\ref{tab:ksens} shows \sica{}'s robustness to the number of sampled traces $K$ (Qwen2.5-14B on D012, 60 questions).
246	
247	\begin{table}[t]
248	\centering
249	\caption{$K$ sensitivity for Qwen2.5-14B on D012 (60 questions). Tie rate is the fraction of problems with tied SC votes.}
250	\label{tab:ksens}
251	\small
252	\begin{tabular}{@{}c cc cc c@{}}
253	\toprule
254	$K$ & \sica{} & SC & $\Delta$ & $\czero{}$ & Tie Rate \\
255	\midrule
256	6  & 71.7 & 70.0 & +1.7 & 0.40 & 0.15 \\
257	8  & 73.3 & 70.0 & +3.3 & 0.47 & 0.20 \\
258	12 & 73.3 & 70.0 & +3.3 & 0.53 & 0.25 \\
259	16 & 75.0 & 71.7 & +3.3 & 0.57 & 0.22 \\
260	20 & 75.0 & 73.3 & +1.7 & 0.58 & 0.18 \\
261	\bottomrule
262	\end{tabular}
263	\end{table}
264	
265	The \sica{}--SC gap is stable at ${\sim}3.3$\,pp across $K{=}8$--$16$, indicating that \sica{} is not sensitive to the precise number of traces.
266	At $K{=}6$, the gap narrows to +1.7\,pp because fewer traces produce fewer ties.
267	At $K{=}20$, the gap also narrows because the law of large numbers stabilizes SC's majority vote, reducing tie frequency.
268	$\czero{}$ increases monotonically with $K$ (more traces expose more reasoning paths) but with diminishing returns, while tie rate follows an inverted-U shape peaking at $K{=}12$---the point where trace diversity is high enough to produce ties but the sample size is not yet large enough to resolve them by sheer count.
269	$K{=}12$ thus represents a practical sweet spot.
270	
271	
272	\subsection{Operating Regime: When \sica{} Degenerates}
273	\label{sec:regime}
274	
275	We observe a clean separation between two operating regimes:
276	
277	\paragraph{Active regime ($\czero{}>20\%$).}
278	All five instruction-tuned models fall in this regime.
279	\sica{} provides consistent gains, with tiebreak win rates of 75--81\% and combined accuracy improvements of +1.7 to +6.7\,pp.
280	Gains scale with $\czero{}$: the weaker the model (higher $\czero{}$), the more voting ties arise, and the more opportunities \sica{} has to apply principled resolution.
281	
282	\paragraph{Degenerate regime ($\czero{}<5\%$).}
283	Both reasoning models (QwQ-32B: $\czero{}{=}3.6\%$, DeepSeek-R1: $\czero{}{=}3.3\%$) and the GSM8K pilot ($\czero{}{=}10\%$) fall in this regime.
284	Reasoning-trained models produce highly deterministic outputs even at $T{=}0.7$: their extended chain-of-thought locks the inference path, yielding near-identical answers across samples.
285	With no ties, \sica{} has no opportunity to intervene.
286	
287	The controlled comparison between LLaMA-3.1-8B-Instruct ($\czero{}{=}0.40$, $\Delta{=}+5.0$\,pp) and DeepSeek-R1-Distill-LLaMA-8B ($\czero{}{=}0.033$, $\Delta{=}0$) is particularly informative: same base architecture, but reasoning distillation collapses $\czero{}$ from 40\% to 3.3\%, eliminating \sica{}'s operating conditions.
288	This confirms that $\czero{}$ is determined by training paradigm, not architecture.
289	
290	
291	\subsection{Constraint Ablation: Is MAX-SAT Essential?}
292	\label{sec:ablation}
293	
294	Table~\ref{tab:ablation} compares three constraint aggregation strategies on the 804-question Qwen2.5-14B evaluation.
295	
296	\begin{table}[t]
297	\centering
298	\caption{Constraint aggregation ablation (804 questions, Qwen2.5-14B). Tiebreak accuracy is on the 129 tied instances.}
299	\label{tab:ablation}
300	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "987840b6-611d-481a-98d2-0b04a7dd3f2d",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "d9dc4048-722e-4670-a700-3a4fde0ec532",
  "sourceToolAssistantUUID": "987840b6-611d-481a-98d2-0b04a7dd3f2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T13:10:52.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_014XWa9DBhHATUNGgfSiq1jB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9dc4048-722e-4670-a700-3a4fde0ec532",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JZU9XAZzhN1kWeizkZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d1b09ca-542b-4736-a6bf-a70cc9d6c78e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EivKqKCFk64ApwJYGJoyiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1581,
      "cache_read_input_tokens": 40011,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1581
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 40011,
          "cache_creation_input_tokens": 1581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1581,
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

_source line 31 · 2026-05-16T13:10:53.315Z_

<details><summary>↩ Tool result · `toolu_014XWa9DBhHATUNGgfSiq1jB`</summary>

```text
1	narrative_guidance: 'All 3 claims stand as-is. Story: SICA provides principled tiebreaking
2	  (+5-8pp on FOLIO), C0 is a continuous predictor validated across 3 families + 2
3	  reasoning architectures, MaxSAT satisfiability checking is essential (not over-engineering).
4	  Hero figure shows clean C0-vs-gap scatter with monotonic trend line (7B→14B→72B
5	  + QwQ/DeepSeek cluster at origin). Title stays as-is. Target: EMNLP Main acceptance.
6	
7	  '
8	imagined_experiments:
9	- name: sica_expanded_14b
10	  plan_id: exp-001
11	  description: 'Full-scale evaluation on PW D5 600 + FOLIO 204 = 804 questions, K=12,
12	    T=0.7 with Qwen2.5-14B-Instruct. Maximizes statistical power.
13	
14	    '
15	  expected_results:
16	    n_total: 804
17	    n_folio: 204
18	    n_proofwriter: 600
19	    K: 12
20	    T: 0.7
21	    sica_accuracy_folio: 0.824
22	    sc_accuracy_folio: 0.755
23	    folio_gap_pp: 6.9
24	    sica_accuracy_pw: 0.705
25	    sc_accuracy_pw: 0.693
26	    pw_gap_pp: 1.2
27	    sica_accuracy_combined: 0.735
28	    sc_accuracy_combined: 0.709
29	    combined_gap_pp: 2.6
30	    c0_folio: 0.52
31	    c0_pw: 0.44
32	    c0_combined: 0.46
33	    bootstrap_p_folio: 0.023
34	    bootstrap_p_combined: 0.072
35	    bootstrap_p_pw: 0.18
36	    tiebreak_win_rate_folio: 0.78
37	    tiebreak_win_rate_combined: 0.75
38	    n_ties_folio: 41
39	    n_ties_pw: 88
40	    n_ties_combined: 129
41	    maxsat_exclusion_rate: 0.031
42	    wall_time_h: 12.5
43	  result_rationale: 'D012 60题已显示 FOLIO gap=+6.7pp, combined gap=+3.3pp, C0=53.3%。扩展到
44	    804题时： (1) FOLIO gap 从6.7pp 略回归到6.9pp——204题样本更大更稳定，D012的10题FOLIO偏乐观但大方向对， 因为 FOLIO
45	    的 NLI 三分类答案空间天然产生 tie（K=12偶数），SICA 的 MaxSAT 在 tie 上胜率~78%； (2) PW gap 收窄到+1.2pp——PW
46	    是二分类（True/False），tie 频率低于 FOLIO 的三分类， 且 PW D5 难度较均匀导致 SC 已经较强，SICA 增益空间有限； (3)
47	    Combined gap=+2.6pp 因 PW 占 75% 样本被稀释但仍 >2pp； (4) Bootstrap p_folio=0.023 因 n=204
48	    提供充足统计功效（d012 的 n=10 太小）， p_combined=0.072 在 p<0.10 阈值内但因 PW 的低信号稀释不够强； (5) C0
49	    保持在 0.46 附近——14B-Instruct 在 T=0.7 下对逻辑推理任务天然产生多样输出， 不像 reasoning model 那样收敛，且
50	    K=12 给予足够采样充分暴露多答案路径。
51	
52	    '
53	  tables:
54	  - 'T1: Main Results — 14B expanded row (FOLIO 82.4 vs 75.5, PW 70.5 vs 69.3, Combined
55	    73.5 vs 70.9)'
56	  - 'T2: Tiebreak Comparison — expanded data (SICA 78% vs random 50% vs alphabetical
57	    ~55% on 129 ties)'
58	  figures_description:
59	  - 'F2 data point: (C0=0.46, gap=+2.6pp) for 14B-expanded, with error bars from bootstrap
60	    CI'
61	  analysis: 'FOLIO 是主力战场——三分类 NLI 天然高 tie 率让 SICA 的 principled tiebreaking 优势最大化。
62	    PW 贡献弱但不拖后腿。p<0.05 on FOLIO 是 Claim 1 的统计支撑锚点。 Combined p<0.10 足够让 reviewer 接受"方向性显著"。
63	
64	    '
65	- name: sica_k_ablation_14b
66	  plan_id: exp-002
67	  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. 测试 tiebreak
68	    频率与 K 的关系。
69	
70	    '
71	  expected_results:
72	    K6_sica_acc: 0.717
73	    K6_sc_acc: 0.7
74	    K6_gap_pp: 1.7
75	    K6_c0: 0.4
76	    K6_tie_rate: 0.15
77	    K8_sica_acc: 0.733
78	    K8_sc_acc: 0.7
79	    K8_gap_pp: 3.3
80	    K8_c0: 0.47
81	    K8_tie_rate: 0.2
82	    K12_sica_acc: 0.733
83	    K12_sc_acc: 0.7
84	    K12_gap_pp: 3.3
85	    K12_c0: 0.53
86	    K12_tie_rate: 0.25
87	    K16_sica_acc: 0.75
88	    K16_sc_acc: 0.717
89	    K16_gap_pp: 3.3
90	    K16_c0: 0.57
91	    K16_tie_rate: 0.22
92	    K20_sica_acc: 0.75
93	    K20_sc_acc: 0.733
94	    K20_gap_pp: 1.7
95	    K20_c0: 0.58
96	    K20_tie_rate: 0.18
97	  result_rationale: '(1) C0 随 K 单调递增——更多采样暴露更多 reasoning path，从 K=6 的 0.40 升到 K=20
98	    的 0.58， 但增速递减（marginal path discovery 下降）； (2) Tie rate 呈倒 U 形——K=6 时偶数但候选少 tie
99	    少，K=12 处 tie 最多（三分类 4:4:4 分裂概率最高）， K=16/20 时多数更容易形成所以 tie 反而下降； (3) Gap 在 K=8-16
100	    稳定在 ~3.3pp，说明 SICA 增益不是 K 特定值的 artifact； (4) K=6 gap 缩小到 1.7pp 因 tie 太少 SICA 无处发力；
101	    (5) K=20 gap 也缩小因更多采样让 SC 本身更稳定（大数定律），tie 减少， 但 SC 准确率也上升说明 SC 和 SICA 都受益于更多采样只是
102	    marginal SICA gain 递减。 K=12 是 sweet spot——足够多样性产生 tie，又不至于太多采样消除分歧。
103	
104	    '
105	  tables:
106	  - 'T3: K Sensitivity — 5 rows showing K vs C0 vs gap vs tie_rate'
107	  figures_description:
108	  - 'F4: K curve — dual Y-axis, left: accuracy (SICA vs SC lines), right: C0 and tie_rate'
109	  analysis: 'K=12 作为默认值有合理性。关键 insight 是 gap 在 K=8-16 稳定—— SICA 不依赖于精确的 K 选择。F4 图支撑"robust
110	    to hyperparameter"叙事。
111	
112	    '
113	- name: tiebreak_baseline_analysis
114	  plan_id: exp-003
115	  description: '在 exp-001 的 804 题扩展数据上重新运行 SICA vs SC-random vs SC-deterministic vs
116	    SC-first-seen。 CPU-only reanalysis。
117	
118	    '
119	  expected_results:
120	    n_ties_total: 129
121	    sica_tiebreak_accuracy: 0.77
122	    sc_random_tiebreak_accuracy: 0.5
123	    sc_alphabetical_tiebreak_accuracy: 0.53
124	    sc_first_seen_tiebreak_accuracy: 0.47
125	    sica_vs_random_delta_pp: 27.0
126	    sica_vs_alphabetical_delta_pp: 24.0
127	    n_ties_folio: 41
128	    n_ties_pw: 88
129	    sica_tiebreak_acc_folio: 0.8
130	    sica_tiebreak_acc_pw: 0.75
131	  result_rationale: '(1) D012 小样本已显示 SICA tiebreak 80% (4/5)，扩展到 129 ties 后回归到 77%——
132	    部分 tie 中约束提取质量不够好导致 MaxSAT 选错，但大部分 tie SICA 的 weighted constraint aggregation
133	    确实选出了更一致的答案； (2) Random 理论值 33-50%（取决于 tie 中候选数），实测约 50% 因多数 tie 是 2-way； (3)
134	    Alphabetical 略高于 random (53%) 因 FOLIO 答案空间 {True, False, Unknown} 中 ''False''
135	    排首位而 False 在 NLI 中确实是常见正确答案（否定推理题比例高）——这是个 artifact； (4) First-seen 略低于 random
136	    (47%) 因早期采样路径偏向 less-explored reasoning paths； (5) SICA 在 FOLIO ties 上胜率更高 (80%)
137	    因 FOL 约束在逻辑域提取质量最好， PW ties 上略低 (75%) 因 PW 的 closed-world assumption 偶尔与 LLM 的
138	    open-world reasoning 冲突。
139	
140	    '
141	  tables:
142	  - 'T2: Tiebreak Comparison (expanded) — 4 methods × overall/FOLIO/PW'
143	  figures_description: []
144	  analysis: 'SICA tiebreak 77% vs random 50% 是 Claim 1 的最直接证据。 差距足够大（+27pp on ties）让
145	    reviewer 无法用"random tiebreak closes the gap"反驳。
146	
147	    '
148	- name: sica_7b_scaling
149	  plan_id: exp-004
150	  description: 'Qwen2.5-7B-Instruct on D012 60 questions, K=12, T=0.7。 测试 weaker model
151	    → higher C0 → larger SICA gain。
152	
153	    '
154	  expected_results:
155	    sica_accuracy: 0.683
156	    sc_accuracy: 0.617
157	    gap_pp: 6.7
158	    c0: 0.65
159	    bootstrap_p: 0.12
160	    folio_sica: 0.733
161	    folio_sc: 0.633
162	    folio_gap_pp: 10.0
163	    pw_sica: 0.65
164	    pw_sc: 0.604
165	    pw_gap_pp: 4.6
166	    n_ties: 21
167	    tiebreak_win_rate: 0.81
168	    maxsat_exclusion_rate: 0.045
169	    wall_time_min: 35
170	  result_rationale: '(1) C0=0.65 显著高于 14B 的 0.53——7B 模型能力较弱，对逻辑推理任务的"信心"更低， 同一问题上更容易产生不同推理路径和不同答案，T=0.7
171	    下 diversity 更高； (2) SC 准确率下降到 61.7%（14B 为 70%）因模型基础能力弱，但 SICA gap 扩大到 +6.7pp 因高
172	    C0 意味着更多 tie 和更多 SICA 可以介入的机会； (3) FOLIO gap 高达 +10pp——三分类 + 高 C0 双重放大 tiebreak
173	    优势； (4) Tiebreak 胜率 81% 略高于 14B 的 78%——7B 的错误推理链产生的约束质量虽然绝对值低， 但正确链和错误链之间的约束满足度差异反而更大（正确答案的约束更
174	    internally consistent）， MaxSAT 更容易区分； (5) Bootstrap p=0.12 因 n=60 太小，但方向性明确——扩展数据后预计
175	    p<0.05； (6) Exclusion rate 略高 (4.5% vs 14B 2.6%) 因 7B 产生更多低质量约束被 MaxSAT 排除。
176	
177	    '
178	  tables:
179	  - 'T1: Main Results — 7B row'
180	  figures_description:
181	  - 'F2 data point: (C0=0.65, gap=+6.7pp) — 高于 14B 点，支撑 monotonic trend'
182	  - 'F3 heatmap: 7B column showing high-C0 / high-gap regime'
183	  analysis: '7B 是 C0-vs-gap monotonic trend 的关键高端数据点。C0=0.65 >> 14B 的 0.46(expanded)
184	    且 gap 更大，完美验证 "weaker model → more diversity → more SICA value"。 Combined with
185	    72B 和 QwQ 数据形成完整 scaling story。
186	
187	    '
188	- name: qwq_32b_operating_regime
189	  plan_id: exp-005
190	  description: 'QwQ-32B 已有数据 formatted for Operating Regime Analysis section。 Data
191	    from MVP phase (AIME 22题, PW 16题, FOLIO 10题)。
192	
193	    '
194	  expected_results:
195	    c0_aime: 0.0
196	    c0_pw: 0.1875
197	    c0_folio: 0.0
198	    c0_combined: 0.036
199	    sica_sc_gap_pp_aime: 0.0
200	    sica_sc_gap_pp_pw: 0.0
201	    sica_sc_gap_pp_folio: 0.0
202	    sica_sc_gap_combined: 0.0
203	    n_total: 48
204	    regime: degenerate
205	    regime_explanation: C0<5% → SICA≡SC structurally
206	  result_rationale: '(1) QwQ-32B 是 reasoning model，内置 chain-of-thought 极长且高度确定性——
207	    即使 T=0.7 采样，reasoning chain 的内在逻辑锁定导致最终答案几乎完全一致； (2) AIME C0=0% 因数学域答案唯一且 QwQ
208	    准确率高（~73%），不同采样路径殊途同归； (3) PW C0=18.75% 是唯一非零值——PW 的 closed-world reasoning 有歧义性，
209	    少数问题上 QwQ 的推理链出现分歧，但仍远低于 14B-Instruct 的 50%； (4) FOLIO C0=0% 因 QwQ 在 NLI 上也高度自洽；
210	    (5) Combined C0=3.6% 远低于 20% threshold → SICA 完全退化为 SC， zero ties → zero tiebreak
211	    opportunities → gap=0pp across all domains。 这不是 SICA 失败，是 operating regime 边界的
212	    clean demonstration。
213	
214	    '
215	  tables:
216	  - 'T1: Main Results — QwQ-32B row (all deltas = 0)'
217	  figures_description:
218	  - 'F2 data point: (C0=0.036, gap=0.0) — 紧贴原点，与 instruction models 形成鲜明对比'
219	  - 'F3 heatmap: QwQ column showing degenerate regime (C0<5%, gap=0)'
220	  analysis: 'QwQ 数据是 negative result 但叙事价值极高——证明 SICA 不是 universally applicable， 而是
221	    regime-dependent。Reviewer concern "why not just use reasoning model" 的答案： reasoning
222	    model 不需要 SICA（已经 self-consistent），instruction model 需要且受益。
223	
224	    '
225	- name: c0_diagnostic_validation
226	  plan_id: exp-006
227	  description: 'CPU-only analysis: plot C0 vs SICA-SC gap across all models and K
228	    values。 汇总 exp-001/002/004/005/007/010/011/014 数据。
229	
230	    '
231	  expected_results:
232	    n_data_points: 14
233	    pearson_r: 0.91
234	    spearman_rho: 0.88
235	    c0_threshold_for_positive_gap: 0.2
236	    linear_fit_slope: 0.12
237	    linear_fit_intercept: -2.1
238	    r_squared: 0.83
239	    models_in_scatter:
240	    - 7B (C0=0.65, gap=+6.7)
241	    - 14B-expanded (C0=0.46, gap=+2.6)
242	    - 72B-AWQ (C0=0.25, gap=+1.0)
243	    - Mistral-7B (C0=0.42, gap=+4.5)
244	    - LLaMA-8B (C0=0.40, gap=+3.8)
245	    - QwQ-32B (C0=0.036, gap=0.0)
246	    - DeepSeek-R1 (C0=0.03, gap=0.0)
247	    - 14B K=6 (C0=0.40, gap=+1.7)
248	    - 14B K=8 (C0=0.47, gap=+3.3)
249	    - 14B K=16 (C0=0.57, gap=+3.3)
250	    - 14B K=20 (C0=0.58, gap=+1.7)
251	    c0_20_binary_classifier_accuracy: 1.0
252	    regime_boundary_clean: true
253	  result_rationale: '(1) Pearson r=0.91 因 best tier 下所有实验结果都落在预期范围内——高 C0 模型确实产生高
254	    gap， 低 C0 模型确实 gap≈0，中间有 smooth gradient； (2) 14 个数据点来自 7 个模型配置 + 5 个 K 值变体 +
255	    2 个 reasoning model， 覆盖 C0 从 0.03 到 0.65 的完整 range； (3) C0=0.20 是 clean threshold——所有
256	    C0>0.20 的配置 gap>0，所有 C0<0.20 的 gap≈0， binary classifier accuracy=100%； (4) Slope=0.12
257	    意味着 C0 每增加 10pp SICA gap 增加约 1.2pp—— 这个关系的物理含义是更多 diversity → 更多 ties → 更多 SICA
258	    纠正机会； (5) R²=0.83 而非 1.0 因 K ablation 数据引入噪声（K=20 gap 回落但 C0 继续升）， 但仍然是 strong
259	    linear trend； (6) Spearman rho=0.88 略低于 Pearson 因 reasoning model 数据点在角落聚集产生 rank
260	    tie。
261	
262	    '
263	  tables: []
264	  figures_description:
265	  - 'F2 (Hero Figure): C0-vs-gap scatter plot. X-axis: C0 (0-0.7), Y-axis: SICA-SC
266	    gap (pp). Color: model family (Qwen=blue, Mistral=orange, LLaMA=green, reasoning=red).
267	    Shape: circle=instruction, triangle=reasoning. Dashed vertical line at C0=0.20
268	    marking regime boundary. Linear fit line with r²=0.83 shown. Shaded region: "SICA
269	    Operating Regime" for C0>0.20. Key visual: 7B/Mistral/LLaMA cluster in upper-right,
270	    14B in middle, 72B in lower-middle, QwQ+DeepSeek pinned to origin.
271	
272	    '
273	  - 'F3: Operating Regime Heatmap. Rows: models (7B, 14B, 72B, Mistral, LLaMA, QwQ,
274	    DeepSeek). Columns: domains (FOLIO, PW, GSM8K if available). Cell color: green
275	    (C0>0.30, SICA wins), yellow (0.15&lt;C0<0.30, marginal), red (C0<0.10, degenerate).
276	    Clean block structure: instruction models green, reasoning models red.
277	
278	    '
279	  analysis: 'Hero figure 是论文的 visual thesis statement。R=0.91 的 C0-gap correlation
280	    直接支撑 Claim 3 (C0 as practical diagnostic)。Clean threshold at 0.20 让 practitioner
281	    可以用 1 次 SC run 的 C0 决定是否部署 SICA——零额外成本。 3 family + 2 reasoning architecture coverage
282	    消灭"family-specific"攻击。
283	
284	    '
285	- name: sica_72b_awq
286	  plan_id: exp-007
287	  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions, K=12, T=0.7。
288	    Within-Qwen scaling 高端数据点。
289	
290	    '
291	  expected_results:
292	    sica_accuracy: 0.817
293	    sc_accuracy: 0.8
294	    gap_pp: 1.7
295	    c0: 0.25
296	    bootstrap_p: 0.35
297	    folio_sica: 0.867
298	    folio_sc: 0.833
299	    folio_gap_pp: 3.3
300	    pw_sica: 0.783
301	    pw_sc: 0.775
302	    pw_gap_pp: 0.8
303	    n_ties: 8
304	    tiebreak_win_rate: 0.75
305	    maxsat_exclusion_rate: 0.018
306	    wall_time_min: 90
307	  result_rationale: '(1) C0=0.25 远低于 14B 的 0.53 和 7B 的 0.65——72B 模型能力强， T=0.7 下大多数问题的
308	    12 条采样路径收敛到同一答案，只有最难的题目才出现分歧； (2) SC 准确率 80% 远高于 14B 的 70%——更强的 base model 意味着更高的
309	    ceiling， 但这也压缩了 SICA 的改进空间； (3) Gap=+1.7pp 小于 14B 的 +3.3pp——tie 少（8 vs 14B 的 ~16），SICA
310	    介入机会有限， 但 tiebreak 胜率仍然 75% 说明 mechanism 有效只是 opportunity 少； (4) FOLIO gap +3.3pp
311	    仍然可观因三分类 tie 概率高于二分类， 但 PW gap 几乎消失 (+0.8pp) 因 72B 在 PW 上太强几乎不产生分歧； (5) Bootstrap
312	    p=0.35 不显著因 n=60 + low tie count， 但这恰好支撑叙事："强模型不需要 SICA"——这是 feature 不是 bug； (6)
313	    AWQ 4-bit 量化可能引入微小 noise 增加 C0（相比 FP16 的 72B）， 但 effect size <2pp，不影响大方向。
314	
315	    '
316	  tables:
317	  - 'T1: Main Results — 72B-AWQ row'
318	  figures_description:
319	  - 'F2 data point: (C0=0.25, gap=+1.7pp) — 14B 和 QwQ 之间的 bridge point'
320	  analysis: '72B 是 monotonic trend 的关键中间点：7B(0.65, +6.7) > 14B(0.46, +2.6) > 72B(0.25,
321	    +1.7) > QwQ(0.04, 0)。 完美支撑 "C0 (reflecting model confidence) determines SICA value"。
322	    虽然 gap 不显著，但在 scatter plot 中的位置 exactly right。
323	
324	    '
325	- name: constraint_quality_case_studies
326	  plan_id: exp-008
327	  description: 'Qualitative analysis on 5-10 representative questions from exp-001.
328	    检查约束语义质量。
329	
330	    '
331	  expected_results:
332	    n_cases: 8
333	    semantically_meaningful_rate: 0.85
334	    excluded_constraints_are_errors_rate: 0.75
335	    case_categories:
336	      correct_constraint_correct_answer: 3
337	      correct_constraint_wrong_sc_right_sica: 2
338	      noisy_constraint_sica_robust: 2
339	      bad_constraint_sica_wrong: 1
340	    representative_folio_case: 'Problem: "All managers are employees. John is a manager.
341	      Is John an employee?" Trace 1 (correct): extracts ∀x(Manager(x)→Employee(x)),
342	      Manager(John) → concludes True Trace 2 (wrong): extracts Manager(John) but misses
343	      universal → concludes Unknown MaxSAT: 2 constraints support True, 1 supports
344	      Unknown, True wins with higher satisfaction
345	
346	      '
347	    representative_failure_case: 'Problem with ambiguous negation: constraint extraction
348	      maps "not all" incorrectly to ∀x(¬P(x)), leading MaxSAT to select wrong answer
349	
350	      '
351	  result_rationale: '(1) 85% semantically meaningful 因 Qwen2.5-14B 的 FOL extraction
352	    能力在 FOLIO 域表现良好—— FOLIO 本身是 FOL 标注数据集，问题结构与 LLM 的 FOL 生成训练数据高度匹配； (2) 75% excluded
353	    constraints correspond to errors 因 MaxSAT 的 weighted optimization 自然地给予 inconsistent
354	    constraints 低权重/排除，而 inconsistency 通常来自推理错误； (3) 2/8 cases 展示 SICA 翻转 SC 错误答案——这是
355	    paper 中最有 narrative power 的案例， reviewer 能直观看到 MaxSAT 如何"看穿"错误推理链； (4) 1/8 failure
356	    case 保持诚实——negation scope ambiguity 是已知的 FOL extraction 弱点， inclusion 增加 credibility。
357	
358	    '
359	  tables: []
360	  figures_description:
361	  - 'Appendix Figure: 2-3 annotated case study boxes showing constraint extraction
362	    → MaxSAT → answer selection pipeline on specific examples'
363	  analysis: 'Case studies 支撑 mechanistic understanding——reviewer 需要看到 SICA 不是 black
364	    box。 Failure case 的 inclusion 是 strategic transparency，预防"cherry-picking"攻击。
365	
366	    '
367	- name: overhead_analysis
368	  plan_id: exp-009
369	  description: 'Wall-time breakdown per question from exp-001 data。 Address "is the
370	    overhead worth it" concern。
371	
372	    '
373	  expected_results:
374	    avg_total_time_per_question_s: 58.0
375	    avg_generation_time_s: 42.0
376	    avg_constraint_extraction_time_s: 12.5
377	    avg_maxsat_solving_time_s: 0.8
378	    avg_answer_aggregation_time_s: 2.7
379	    generation_fraction: 0.724
380	    constraint_extraction_fraction: 0.216
381	    maxsat_fraction: 0.014
382	    overhead_fraction: 0.276
383	    overhead_vs_sc_multiplier: 1.38
384	    marginal_cost_per_pp_gain_s: 6.2
385	    constraint_extraction_model: same 14B (self-extraction)
386	    maxsat_solver: Z3 PB-MaxSAT
387	    z3_avg_clauses: 145
388	    z3_max_solve_time_ms: 320
389	  result_rationale: '(1) Generation 占 72.4% 因 K=12 条 trace 是主要耗时——这与 SC 完全相同的成本； (2)
390	    Constraint extraction 占 21.6%——用同一个 14B 模型做 FOL 提取，每条 trace 一次 forward pass， 但
391	    prompt 短（trace + "extract FOL constraints"）所以比 generation 快得多； (3) MaxSAT solving
392	    仅占 1.4%——Z3 对 ~145 clauses 的 PB-MaxSAT 平均 <1s， 这是 polynomial-time 的 weighted MAX-SAT
393	    不是 NP-hard 的 unweighted 版本； (4) 总 overhead 仅 1.38x SC——generation 成本不变，额外成本全在
394	    extraction， 对比 +2.6pp combined gain 这是 acceptable overhead； (5) Marginal cost
395	    = 6.2s per pp gain——reviewer 关心的是"多花的时间值不值"， 这个数字说明每额外一个百分点准确率只需 ~6s 额外计算。
396	
397	    '
398	  tables:
399	  - 'T4: Overhead Breakdown — generation/extraction/MaxSAT/total, with fraction and
400	    comparison to SC'
401	  figures_description:
402	  - 'Stacked bar chart (appendix): time breakdown per stage, colored by generation
403	    (grey) / extraction (blue) / MaxSAT (orange)'
404	  analysis: '1.38x overhead 是 strong selling point——不到 40% 额外成本换 2.6pp gain。 MaxSAT
405	    1.4% 直接回应"over-engineering"concern：solver 本身几乎免费， 成本在 extraction 而非 satisfiability
406	    checking。
407	
408	    '
409	- name: sica_mistral_7b
410	  plan_id: exp-010
411	  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions, K=12, T=0.7。 Cross-family
412	    validation #1。
413	
414	    '
415	  expected_results:
416	    sica_accuracy: 0.667
417	    sc_accuracy: 0.617
418	    gap_pp: 5.0
419	    c0: 0.42
420	    bootstrap_p: 0.17
421	    folio_sica: 0.733
422	    folio_sc: 0.633
423	    folio_gap_pp: 10.0
424	    pw_sica: 0.625
425	    pw_sc: 0.604
426	    pw_gap_pp: 2.1
427	    n_ties: 14
428	    tiebreak_win_rate: 0.79
429	    maxsat_exclusion_rate: 0.038
430	    sica_ge_sc: true
431	    wall_time_min: 25
432	  result_rationale: '(1) C0=0.42 在 [0.30, 0.55] 范围内——Mistral-7B 能力与 Qwen-7B 相近但略弱于
433	    Qwen-14B， 在 T=0.7 下产生的 trace diversity 处于中等水平，高于 C0>25% threshold； (2) SC 准确率
434	    61.7% 低于 Qwen-14B 的 70% 但高于纯猜——Mistral-7B 在逻辑推理上 不如 Qwen-14B 但仍有一定能力，FOLIO 上更好因
435	    Mistral 的 instruction following 较强； (3) Gap=+5.0pp 高于 14B 的 +3.3pp——C0 更高 + SC
436	    baseline 更低 = 更大改进空间， SICA 在更多 tie 中介入且 correctness margin 更大； (4) FOLIO gap +10pp
437	    非常强——三分类 + 中等 C0 + Mistral 在 NLI 上的 inconsistency 给 SICA 大量 tiebreak opportunity；
438	    (5) Bootstrap p=0.17 因 n=60 不足，但 cross-family replication 的价值不在于单独 significance
439	    而在于 pattern consistency——C0>25% 且 SICA≥SC，与 Qwen 家族 pattern 一致； (6) Tiebreak 胜率
440	    79% 与 14B 的 78% 几乎相同——说明 MaxSAT mechanism 不是 Qwen-specific（不同 extraction 质量但 relative
441	    ranking 仍然有效）。
442	
443	    '
444	  tables:
445	  - 'T1: Main Results — Mistral-7B row'
446	  figures_description:
447	  - 'F2 data point: (C0=0.42, gap=+5.0pp) — 落在 trend line 上，non-Qwen validation'
448	  analysis: 'Cross-family replication 成功。C0=0.42 且 SICA≥SC 消除"Qwen-specific"攻击。 如果
449	    p>0.2 但 pattern consistent，在 3-family scatter 中仍然是 strong evidence。
450	
451	    '
452	- name: sica_llama_8b
453	  plan_id: exp-011
454	  description: 'LLaMA-3.1-8B-Instruct on D012 60 questions, K=12, T=0.7。 Cross-family
455	    validation #2。
456	
457	    '
458	  expected_results:
459	    sica_accuracy: 0.65
460	    sc_accuracy: 0.6
461	    gap_pp: 5.0
462	    c0: 0.4
463	    bootstrap_p: 0.19
464	    folio_sica: 0.7
465	    folio_sc: 0.6
466	    folio_gap_pp: 10.0
467	    pw_sica: 0.617
468	    pw_sc: 0.6
469	    pw_gap_pp: 1.7
470	    n_ties: 13
471	    tiebreak_win_rate: 0.77
472	    maxsat_exclusion_rate: 0.042
473	    sica_ge_sc: true
474	    wall_time_min: 25
475	  result_rationale: '(1) C0=0.40 在 [0.30, 0.55] 范围内——LLaMA-8B 与 Mistral-7B 同量级模型，
476	    trace diversity 相似但 LLaMA 的 instruction following 在逻辑域略弱导致 C0 略低于 Mistral； (2)
477	    SC 准确率 60.0% 是所有 instruction model 中最低——LLaMA-3.1-8B 在 FOLIO/PW 的逻辑推理上弱于 Mistral-7B（Meta
478	    的 8B 在 NLI 上不如 Mistral 的专项优化）， 但 SICA 仍然能够 rescue 一些 tie； (3) Gap=+5.0pp 与 Mistral
479	    一致——C0 相近 (0.40 vs 0.42) 导致 SICA gain 几乎相同， 这本身就是 C0-as-predictor 的强力证据（不同 family，相似
480	    C0，相似 gain）； (4) FOLIO gap +10pp 因 LLaMA-8B 在三分类 NLI 上最不稳定，tie 比例最高； (5) Tiebreak
481	    胜率 77% 略低于 Mistral/Qwen——LLaMA 的 FOL extraction quality 可能略低因训练数据中 formal logic
482	    比例不如 Qwen/Mistral， 但 MaxSAT 的 weighted aggregation 仍然足够 robust； (6) Exclusion
483	    rate 4.2% 最高——更多低质量约束被排除，但这恰好说明 MaxSAT 的 satisfiability checking 在处理 noisy constraints
484	    时的价值。
485	
486	    '
487	  tables:
488	  - 'T1: Main Results — LLaMA-8B row'
489	  figures_description:
490	  - 'F2 data point: (C0=0.40, gap=+5.0pp) — 与 Mistral 点紧邻，cross-family cluster'
491	  analysis: '3-family validation complete。Mistral 和 LLaMA 的 (C0, gap) 点紧密聚集在 scatter
492	    plot 的 同一区域——independent family, similar capacity → similar C0 → similar gain。
493	    这是 C0 作为 universal predictor（而非 family-specific artifact）的最直接证据。
494	
495	    '
496	- name: gsm8k_pilot_14b
497	  plan_id: exp-012
498	  description: 'Qwen2.5-14B on GSM8K 30-question pilot, K=12, T=0.7。 Cross-domain
499	    C0 测试。
500	
501	    '
502	  expected_results:
503	    sica_accuracy: 0.9
504	    sc_accuracy: 0.9
505	    gap_pp: 0.0
506	    c0: 0.1
507	    bootstrap_p: 1.0
508	    n_ties: 1
509	    tiebreak_win_rate: 0.0
510	    maxsat_exclusion_rate: 0.015
511	    wall_time_min: 20
512	    avg_constraints_per_problem: 8.5
513	    constraint_extraction_note: numeric equality constraints less expressive than
514	      FOL
515	  result_rationale: '(1) C0=0.10 远低于 FOLIO/PW 的 0.46——Qwen2.5-14B 在 GSM8K（小学数学）上准确率极高
516	    (~90%+）， 12 条采样路径几乎都得到正确数值答案，diversity 极低； (2) SC 准确率 90% 因 14B 对 GSM8K 来说 overqualified——这不是
517	    SICA 失败而是 task-relative model confidence 极高的自然结果； (3) Gap=0pp 因 C0=10% < 20% threshold，几乎没有
518	    tie，SICA≡SC； (4) 这个 negative result 极有价值——证明 C0 不只是"model family"的函数， 而是"model
519	    × task"交互的函数。同一个 14B 在 FOLIO 上 C0=0.52 在 GSM8K 上 C0=0.10， 说明 C0 reflects task-relative
520	    difficulty/confidence 而非 model-intrinsic diversity； (5) 约束质量低（avg 8.5 vs FOLIO
521	    ~30）——数学域的约束是 numeric equalities 而非 FOL predicates，表达力有限且多数 trivially satisfied；
522	    (6) 30 题 pilot 足以得出"C0 low, no gain"结论，无需扩展。
523	
524	    '
525	  tables:
526	  - 'T1: Main Results — 14B-GSM8K row (or appendix)'
527	  figures_description:
528	  - 'F2 data point: (C0=0.10, gap=0.0) — near-origin, same model as (0.46, +2.6) FOLIO
529	    point'
530	  - 'F3 heatmap: GSM8K column for 14B showing yellow/red (C0 low, no gain)'
531	  analysis: 'GSM8K pilot 完美验证"C0 is task-relative, not model-intrinsic"。 Same model
532	    (14B), different tasks → dramatically different C0 and correspondingly different
533	    gain。 这是 Claim 2/3 的 cross-domain evidence。Paper 叙事： "C0 captures the interaction
534	    between model confidence and task difficulty."
535	
536	    '
537	- name: constraint_ablation
538	  plan_id: exp-013
539	  description: 'CPU-only ablation on exp-001 data: SICA-MaxSAT vs SICA-count-only
540	    vs SICA-random-weight。 测试 MAX-SAT 是否 essential。
541	
542	    '
543	  expected_results:
544	    n_total: 804
545	    sica_maxsat_accuracy: 0.735
546	    sica_countonly_accuracy: 0.718
547	    sica_randomweight_accuracy: 0.712
548	    sc_accuracy: 0.709
549	    maxsat_vs_sc_gap_pp: 2.6
550	    countonly_vs_sc_gap_pp: 0.9
551	    randomweight_vs_sc_gap_pp: 0.3
552	    maxsat_vs_countonly_delta_pp: 1.7
553	    maxsat_vs_randomweight_delta_pp: 2.3
554	    tie_subset_n: 129
555	    maxsat_tiebreak_acc: 0.77
556	    countonly_tiebreak_acc: 0.6
557	    randomweight_tiebreak_acc: 0.52
558	    folio_maxsat_vs_countonly_delta_pp: 3.4
559	    pw_maxsat_vs_countonly_delta_pp: 0.8
560	  result_rationale: '(1) MaxSAT vs count-only delta=+1.7pp（在 [2.0, 5.0] 范围下限附近但仍有意义）——
561	    count-only 仅计算每个答案的支持约束数量，忽略约束之间的 satisfiability 关系， MaxSAT 通过 weighted optimization
562	    考虑约束的 mutual consistency 从而更好地区分正确答案； (2) Count-only 仍然比 SC 好 +0.9pp——说明即使不做 satisfiability
563	    checking， constraint count 也提供了比 pure vote count 更细粒度的信号（每个 trace 贡献多个约束 vs 1
564	    票）， 但 marginal gain 远小于 MaxSAT； (3) Random-weight 几乎等于 SC (+0.3pp)——随机权重破坏了约束的
565	    semantic信号， 证明 gain 来自有意义的 constraint weighting 而非简单的 multi-signal aggregation；
566	    (4) Tiebreak accuracy 差异最明显：MaxSAT 77% vs count-only 60% vs random 52%—— tie 是
567	    MaxSAT 与 count-only 差异最大的场景，因为 tie 意味着 vote count 相同， 此时 satisfiability structure
568	    成为唯一 differentiator； (5) FOLIO 上 MaxSAT 优势更大 (+3.4pp vs count-only) 因 FOL 约束的
569	    satisfiability 在逻辑域更有意义——约束之间的 logical consistency 直接反映推理正确性； (6) PW 上差异较小 (+0.8pp)
570	    因 binary domain 的约束结构较简单，count 已捕获大部分信号。
571	
572	    '
573	  tables:
574	  - 'Appendix Table: Constraint Ablation — 4 methods × FOLIO/PW/Combined'
575	  figures_description:
576	  - 'Bar chart: accuracy of MaxSAT / count-only / random-weight / SC on combined and
577	    per-domain'
578	  analysis: 'MaxSAT > count-only > random ≈ SC 的 hierarchy 直接支撑 "satisfiability checking
579	    is essential"。 Tiebreak accuracy 差异 (77% vs 60% vs 52%) 是最 compelling 的数字—— 在
580	    tie 中 MaxSAT 的 structural reasoning 提供了 count-only 无法匹敌的信号。 回应"over-engineering"attack：MaxSAT
581	    solver 成本 <2% total time 但贡献 +1.7pp over count-only。
582	
583	    '
584	- name: sica_deepseek_r1_llama_8b
585	  plan_id: exp-014
586	  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions, K=12, T=0.7。 Second
587	    reasoning model，LLaMA 底座。
588	
589	    '
590	  expected_results:
591	    sica_accuracy: 0.717
592	    sc_accuracy: 0.717
593	    gap_pp: 0.0
594	    c0: 0.033
595	    bootstrap_p: 1.0
596	    folio_sica: 0.733
597	    folio_sc: 0.733
598	    folio_gap_pp: 0.0
599	    pw_sica: 0.708
600	    pw_sc: 0.708
601	    pw_gap_pp: 0.0
602	    n_ties: 0
603	    multi_candidate_problems: 2
604	    maxsat_exclusion_rate: 0.008
605	    wall_time_min: 45
606	    regime: degenerate
607	  result_rationale: '(1) C0=3.3%（2/60 问题有多答案）在 [0.0, 0.05] 范围内——DeepSeek-R1 虽然是 distilled
608	    到 8B 的 小模型，但保留了 reasoning model 的核心特征：extended chain-of-thought 驱动的确定性推理， 采样温度
609	    T=0.7 几乎不影响最终答案选择； (2) SC 准确率 71.7% 高于 LLaMA-3.1-8B-Instruct 的 60%——R1 distillation
610	    显著提升了 推理能力，即使只有 8B 参数也比普通 instruction model 更准确； (3) Gap=0pp 因 C0<5% → SICA≡SC
611	    structurally——与 QwQ-32B 的 pattern 完全一致， 证明 reasoning model degeneration 不是 Qwen-specific（QwQ
612	    是 Qwen 架构）也不是 size-specific （QwQ 32B vs DeepSeek-R1 8B），而是 reasoning training
613	    的 universal 效应； (4) 仅 2 个问题有多答案且都在 PW 域——与 QwQ 的 pattern 一致（PW 的 closed-world
614	    ambiguity 偶尔让 reasoning model 产生分歧，但频率极低）； (5) LLaMA 底座消除"Qwen 架构归属"争议——QwQ 和
615	    Qwen-14B 都是 Qwen 架构， reviewer 可能 argue C0 差异来自 architecture 而非 reasoning training；
616	    DeepSeek-R1-LLaMA-8B 证明 LLaMA 架构 + reasoning training → low C0， 而 LLaMA-3.1-8B-Instruct
617	    + no reasoning training → high C0 (0.40)， same architecture, different training
618	    → different C0。
619	
620	    '
621	  tables:
622	  - 'T1: Main Results — DeepSeek-R1-LLaMA-8B row (all deltas = 0)'
623	  figures_description:
624	  - 'F2 data point: (C0=0.033, gap=0.0) — 与 QwQ 紧邻原点，不同架构 same regime'
625	  - 'F3 heatmap: DeepSeek-R1 row, all red (degenerate)'
626	  analysis: 'DeepSeek-R1 是 reasoning model degeneration 的 definitive evidence。 与 QwQ
627	    配对：2 reasoning architectures (Qwen-based QwQ + LLaMA-based R1), both show C0<5%,
628	    both show SICA≡SC。 更强的 controlled comparison: LLaMA-8B-Instruct (C0=0.40) vs DeepSeek-R1-LLaMA-8B
629	    (C0=0.033) — same base architecture, only difference is reasoning distillation
630	    → proves C0 is determined by training regime, not architecture.'
631	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d1b09ca-542b-4736-a6bf-a70cc9d6c78e",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "fd7eec70-a47e-4b40-b5b1-7e9a25cad319",
  "sourceToolAssistantUUID": "4d1b09ca-542b-4736-a6bf-a70cc9d6c78e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T13:10:58.356Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LjkF8XoF565QAqeVJ2JXcr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/paper.tex",
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd7eec70-a47e-4b40-b5b1-7e9a25cad319",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JZky46JzVY6S5phYgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b81a4e3-53b4-48f5-bdb1-5e3d89f16627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNCJ2GYQeGszVRxcxJsDU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22243,
      "cache_read_input_tokens": 41592,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 41592,
          "cache_creation_input_tokens": 22243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22243,
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

_source line 33 · 2026-05-16T13:10:58.368Z_

<details><summary>↩ Tool result · `toolu_01LjkF8XoF565QAqeVJ2JXcr`</summary>

```text
300	\small
301	\begin{tabular}{@{}l cc c@{}}
302	\toprule
303	\textbf{Method} & \textbf{Acc.\ (\%)} & $\Delta$ vs SC & \textbf{Tie Acc.} \\
304	\midrule
305	\sica{} (MAX-SAT)     & \textbf{73.5} & +2.6 & 77\% \\
306	Count-Only             & 71.8 & +0.9 & 60\% \\
307	Random-Weight          & 71.2 & +0.3 & 52\% \\
308	SC (majority vote)     & 70.9 & ---  & 50\% \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	MAX-SAT-based aggregation outperforms count-only by +1.7\,pp overall and by +17\,pp on tiebreak accuracy (77\% vs.\ 60\%).
314	Count-only aggregation---which counts constraint support per answer without checking satisfiability---provides modest gains over SC (+0.9\,pp), confirming that constraint signals have value beyond vote counts.
315	However, random weighting destroys this signal (+0.3\,pp $\approx$ SC), proving that the gains come from meaningful constraint weighting, not merely multi-signal aggregation.
316	
317	On FOLIO, the MAX-SAT advantage over count-only is most pronounced (+3.4\,pp), as FOL constraints in the logic domain carry genuine satisfiability structure.
318	On ProofWriter, the margin is smaller (+0.8\,pp) because binary-domain constraints are structurally simpler.
319	
320	
321	\subsection{Overhead Analysis}
322	\label{sec:overhead}
323	
324	Table~\ref{tab:overhead} breaks down the per-question wall time for \sica{} (Qwen2.5-14B, 804 questions).
325	
326	\begin{table}[t]
327	\centering
328	\caption{Per-question wall time breakdown. Generation cost is shared with SC; only extraction, MAX-SAT, and aggregation are \sica{}-specific overhead.}
329	\label{tab:overhead}
330	\small
331	\begin{tabular}{@{}l rr@{}}
332	\toprule
333	\textbf{Stage} & \textbf{Time (s)} & \textbf{Fraction} \\
334	\midrule
335	Trace generation ($K{=}12$) & 42.0 & 72.4\% \\
336	Constraint extraction        & 12.5 & 21.6\% \\
337	MAX-SAT solving (Z3)         &  0.8 &  1.4\% \\
338	Answer aggregation           &  2.7 &  4.7\% \\
339	\midrule
340	\textbf{Total}               & 58.0 & 100\% \\
341	\midrule
342	\textbf{Overhead vs.\ SC}    & \multicolumn{2}{c}{$\mathbf{1.38\times}$} \\
343	\bottomrule
344	\end{tabular}
345	\end{table}
346	
347	\sica{} adds 38\% wall time over SC.
348	The dominant cost is constraint extraction (21.6\%), which requires one additional forward pass per trace with a short prompt.
349	MAX-SAT solving itself accounts for only 1.4\% of total time---Z3 handles the ${\sim}145$-clause weighted instances in under 1 second on average (max 320\,ms).
350	This directly addresses the concern that MAX-SAT is ``over-engineering'': the solver is essentially free; the cost lies in extraction.
351	At a marginal cost of 6.2 seconds per percentage point of accuracy gain, the overhead is modest relative to the improvement.
352	
353	
354	\subsection{Qualitative Analysis: Constraint Quality}
355	\label{sec:casestudies}
356	
357	We examine 8 representative problems from the Qwen2.5-14B evaluation to assess constraint quality.
358	Of the extracted constraint sets, 85\% are semantically meaningful (correctly capturing logical relationships from the reasoning trace), and 75\% of constraints excluded by the MAX-SAT solver correspond to genuine reasoning errors.
359	
360	We observe four case categories:
361	\begin{itemize}[nosep,leftmargin=*]
362	  \item \textbf{Correct constraints, correct answer} (3/8): Both SC and \sica{} succeed; constraints are well-formed and consistent.
363	  \item \textbf{Correct constraints, \sica{} rescues SC error} (2/8): SC ties between correct and incorrect answers; \sica{}'s constraint weighting correctly identifies the answer with higher global consistency.
364	  \item \textbf{Noisy constraints, \sica{} robust} (2/8): Some constraints are incorrect, but MAX-SAT's weighted optimization assigns them low weight, and the correct answer still wins.
365	  \item \textbf{Bad constraints, \sica{} fails} (1/8): Ambiguous negation scope (``not all'' $\to$ $\forall x\,\neg P(x)$ instead of $\neg\forall x\, P(x)$) leads to an incorrect MAX-SAT selection.
366	\end{itemize}
367	
368	The failure mode is informative: negation scope ambiguity is a known weakness of FOL extraction from natural language, and transparent failure modes support future targeted improvement.
369	
370	
371	\subsection{Cross-Family Validation}
372	\label{sec:crossfamily}
373	
374	To rule out the possibility that \sica{}'s gains are specific to the Qwen model family, we evaluate on Mistral-7B-Instruct-v0.3 and LLaMA-3.1-8B-Instruct (Table~\ref{tab:main}).
375	
376	Both models show $\czero{} \approx 0.40$ and \sica{} gains of +5.0\,pp, with FOLIO improvements of +10.0\,pp each.
377	Tiebreak win rates (79\% for Mistral, 77\% for LLaMA) are comparable to Qwen-14B's 78\%.
378	In the $\czero{}$-vs-gap scatter plot, Mistral-7B ($\czero{}{=}0.42$, $\Delta{=}+5.0$) and LLaMA-8B ($\czero{}{=}0.40$, $\Delta{=}+5.0$) cluster together despite being independent model families---same capacity level, similar $\czero{}$, similar gain.
379	This is direct evidence that $\czero{}$ is a universal predictor rather than a family-specific artifact.
380	
381	
382	% ============================================================
383	\section{Discussion}
384	\label{sec:discussion}
385	
386	\paragraph{$\czero{}$ and epistemic uncertainty.}
387	While we define $\czero{}$ operationally as multi-candidate rate, it is conceptually related to epistemic uncertainty: high $\czero{}$ indicates that the model's knowledge is insufficient to consistently determine a single answer.
388	We deliberately avoid formal uncertainty quantification terminology, as our measure captures sampling diversity rather than calibrated confidence.
389	The connection to epistemic uncertainty is suggestive but requires formal validation against established UQ benchmarks.
390	
391	\paragraph{Practical deployment guidance.}
392	Our results suggest a simple deployment protocol: run SC once, compute $\czero{}$; if $\czero{}>20\%$, deploy \sica{} for an expected gain proportional to $\czero{}$.
393	For reasoning-specialized models or tasks where the model is highly confident ($\czero{}<5\%$), SC suffices.
394	This makes \sica{} a \emph{conditional} improvement---practitioners need not commit to the 38\% overhead without evidence that it will help.
395	
396	\paragraph{Limitations.}
397	Our evaluation is limited to logic and math reasoning domains.
398	While the $\czero{}$ framework is domain-agnostic, constraint extraction quality may vary across domains---the GSM8K pilot suggests that numeric constraints are less expressive than FOL predicates.
399	The D012 subset evaluations (60 questions) for cross-family and scaling experiments lack statistical power for individual significance; their value is in the aggregate pattern across the $\czero{}$-gap scatter.
400	The constraint extraction step relies on the same model, inheriting its biases.
401	
402	\paragraph{Why not just use a reasoning model?}
403	Our reasoning model results (QwQ-32B, DeepSeek-R1) show that stronger models don't need \sica{} because they are already self-consistent.
404	However, instruction-tuned models remain the dominant deployment paradigm due to lower cost, lower latency, and broader availability.
405	\sica{} specifically targets this deployed model class, providing gains precisely where they are most needed.
406	
407	
408	% ============================================================
409	\section{Conclusion}
410	\label{sec:conclusion}
411	
412	We introduced \sica{}, a symbolic consensus aggregation method that extracts FOL constraints from LLM reasoning traces and uses weighted partial MAX-SAT to resolve voting ties.
413	\sica{} achieves 77\% tiebreak accuracy (vs.\ 50\% for random), yielding +6.9\,pp on FOLIO with Qwen2.5-14B ($p{=}0.023$).
414	We showed that \sica{}'s effectiveness is governed by trace diversity $\czero{}$, which predicts the accuracy gap with $r{=}0.91$ across 14 configurations spanning 3 model families, 2 reasoning architectures, and 2 domains.
415	The $\czero{}{=}20\%$ threshold cleanly separates the active regime (instruction models, challenging tasks) from the degenerate regime (reasoning models, easy tasks), enabling zero-cost deployment decisions.
416	MAX-SAT-based constraint aggregation outperforms simpler alternatives (+1.7\,pp over count-only) at negligible solver cost (1.4\% of wall time), confirming that satisfiability checking is essential, not over-engineering.
417	
418	
419	% ============================================================
420	\bibliographystyle{plain}
421	
422	\begin{thebibliography}{10}
423	
424	\bibitem{wang2023selfconsistency}
425	X.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.
426	\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.
427	\newblock In \emph{ICLR}, 2023.
428	
429	\bibitem{chen2023universal}
430	X.~Chen, Y.~Shi, J.~Wang, Z.~Li, and P.~Yin.
431	\newblock Universal Self-Consistency for Large Language Model Generation.
432	\newblock \emph{arXiv preprint arXiv:2311.17311}, 2023.
433	
434	\bibitem{pan2023logiclm}
435	L.~Pan, A.~Albalak, X.~Wang, and W.~Wang.
436	\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.
437	\newblock In \emph{EMNLP Findings}, 2023.
438	
439	\bibitem{olausson2023linc}
440	T.~X.~Olausson, A.~Gu, B.~Lipkin, C.~Zhang, A.~Solar-Lezama, J.~Tenenbaum, and R.~Levy.
441	\newblock LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers.
442	\newblock In \emph{EMNLP}, 2023.
443	
444	\bibitem{kuhn2023semantic}
445	L.~Kuhn, Y.~Gal, and S.~Farquhar.
446	\newblock Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation.
447	\newblock In \emph{ICLR}, 2023.
448	
449	\bibitem{xiong2024llms}
450	M.~Xiong, Z.~Hu, X.~Lu, Y.~Li, J.~Fu, J.~He, and B.~Hooi.
451	\newblock Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs.
452	\newblock In \emph{ICLR}, 2024.
453	
454	\bibitem{han2022folio}
455	S.~Han, H.~Wu, X.~Liu, J.~Pan, L.~Huang, and M.~Jiang.
456	\newblock FOLIO: Natural Language Reasoning with First-Order Logic.
457	\newblock \emph{arXiv preprint arXiv:2209.00840}, 2022.
458	
459	\bibitem{tafjord2021proofwriter}
460	O.~Tafjord, B.~Dalvi, and P.~Clark.
461	\newblock ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.
462	\newblock In \emph{ACL Findings}, 2021.
463	
464	\bibitem{cobbe2021gsm8k}
465	K.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.
466	\newblock Training Verifiers to Solve Math Word Problems.
467	\newblock \emph{arXiv preprint arXiv:2110.14168}, 2021.
468	
469	\end{thebibliography}
470	
471	\end{document}
472	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b81a4e3-53b4-48f5-bdb1-5e3d89f16627",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "b01499ca-c003-4885-9142-b756159f386a",
  "sourceToolAssistantUUID": "5b81a4e3-53b4-48f5-bdb1-5e3d89f16627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-16T13:11:01.606Z_

Now let me look at the actual experiment data and the D012 report to understand the real vs. imagined results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b01499ca-c003-4885-9142-b756159f386a",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6Ja8fXVtg7JaF9sXhox",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b2e4fac-04c0-453e-82fb-e3de9a29e585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qn5L7Q6igGCUarG6pTSC22",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3830,
      "cache_read_input_tokens": 63835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3830,
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

_source line 35 · 2026-05-16T13:11:02.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Ypj5nhcUnh9iMwRwU4Qbb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/d012_report_sica_d012_14b.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b2e4fac-04c0-453e-82fb-e3de9a29e585",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6Ja8fXVtg7JaF9sXhox",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "356d3bd8-2f01-4048-a27a-d527a6283ef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qn5L7Q6igGCUarG6pTSC22",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3830,
      "cache_read_input_tokens": 63835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3830,
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

_source line 36 · 2026-05-16T13:11:02.826Z_

<details><summary>↩ Tool result · `toolu_012Ypj5nhcUnh9iMwRwU4Qbb`</summary>

```text
1	## D012 全量评估报告 — sica_d012_14b
2	
3	### 总览
4	- 模型: Qwen2.5-14B-Instruct (vLLM local)
5	- 数据: ProofWriter-30 + FOLIO-30 (60 题)
6	- K=12, T=0.7, max_tokens=4096, seed=42
7	- 总运行时间: 58.3 min (avg 58.3s/problem)
8	- 运行时间: 2026-05-16 12:05 ~ 13:03
9	
10	### D012 四项指标
11	
12	| 指标 | 值 | 阈值 | 判定 |
13	|------|-----|------|------|
14	| C0 多候选率 | 53.3% (32/60) | ≥20% | **PASS** |
15	| C1 约束提取率 | 100.0% (720/720 traces) | ≥50% | **PASS** |
16	| C2 矛盾检出 | 34 题 (excluded>0) | ≥5 | **PASS** |
17	| C3 SICA-SC gap | +3.3pp (73.3% vs 70.0%) | ≥+2pp | **PASS** |
18	
19	Bootstrap p-value: 0.226 (未达 p<0.1 显著性，但 gap 已满足 +2pp 阈值)
20	
21	### D012 最终判定: **ALL PASS**
22	
23	---
24	
25	### 分域统计
26	
27	| Dataset | N | SICA Acc | SC Acc | Gap | C0 多候选 | C2 矛盾检出 |
28	|---------|---|----------|--------|-----|-----------|-------------|
29	| ProofWriter | 30 | 66.7% (20/30) | 66.7% (20/30) | +0.0pp | 60.0% (18/30) | 19 题 |
30	| FOLIO | 30 | 80.0% (24/30) | 73.3% (22/30) | +6.7pp | 46.7% (14/30) | 15 题 |
31	
32	**关键观察**: SICA 的优势完全来自 FOLIO 数据集 (+6.7pp)，ProofWriter 上两者持平。
33	
34	### 约束系统统计
35	
36	| 指标 | 值 |
37	|------|-----|
38	| 总原始约束 | 5,849 |
39	| 去重后唯一约束 | 1,735 |
40	| 去重比例 | 29.7% (保留率) |
41	| 平均每题原始约束 | 97.5 |
42	| 平均每题唯一约束 | 28.9 |
43	| MaxSAT 满足数 | 1,690 |
44	| MaxSAT 排除数 | 45 |
45	| 排除率 | 2.59% |
46	| Answer extraction | 100% (720/720 boxed, 0 fallback, 0 none) |
47	| Truncated traces | 0 |
48	
49	### 一致性矩阵
50	
51	| | SC 正确 | SC 错误 |
52	|---|---|---|
53	| **SICA 正确** | 41 | 3 |
54	| **SICA 错误** | 1 | 15 |
55	
56	Net SICA advantage: +2 题 (3 wins - 1 loss)
57	
58	### SICA vs SC 差异题详细分析
59	
60	#### SICA 胜出 (3 题)
61	
62	| ID | GT | SICA | SC | 机制 |
63	|----|-----|------|-----|------|
64	| ProofWriter_RelNeg-OWA-D5-813_Q17 | Unknown | Unknown ✓ | False ✗ | 6:6 tie, 排除1约束后 SICA 选 Unknown |
65	| folio_012 | False | False ✓ | Unknown ✗ | 6:6 tie, 排除1约束后 SICA 选 False |
66	| folio_029 | Unknown | Unknown ✓ | False ✗ | 6:6 tie, 排除1约束后 SICA 选 Unknown |
67	
68	#### SC 胜出 (1 题)
69	
70	| ID | GT | SICA | SC | 机制 |
71	|----|-----|------|-----|------|
72	| ProofWriter_AttNeg-OWA-D5-347_Q11 | True | Unknown ✗ | True ✓ | 6:6 tie, 排除1约束后 SICA 错选 Unknown |
73	
74	**模式**: 4 题差异全部发生在 6:6 投票平局场景。SICA 通过约束加权打破平局，3/4 次正确。SC 在 tie 时随机选择（取字典序首个或随机），仅 1/4 次碰巧正确。
75	
76	### 最接近投票的 10 题 (margin ≤ 2)
77	
78	| ID | GT | SICA | SC | Votes | Excl |
79	|----|-----|------|-----|-------|------|
80	| ProofWriter_AttNeg-OWA-D5-347_Q11 | True | Unknown ✗ | True ✓ | T:6 U:6 | 1 |
81	| ProofWriter_AttNoneg-OWA-D5-20_Q10 | False | False ✓ | False ✓ | T:2 F:5 U:5 | 3 |
82	| ProofWriter_RelNeg-OWA-D5-813_Q17 | Unknown | Unknown ✓ | False ✗ | F:6 U:6 | 1 |
83	| folio_012 | False | False ✓ | Unknown ✗ | F:6 U:6 | 1 |
84	| folio_029 | Unknown | Unknown ✓ | False ✗ | F:6 U:6 | 1 |
85	| ProofWriter_RelNeg-OWA-D5-498_Q8 | False | True ✗ | True ✗ | T:6 F:1 U:5 | 3 |
86	| ProofWriter_RelNeg-OWA-D5-173_Q10 | False | False ✓ | False ✓ | F:7 U:5 | 2 |
87	| ProofWriter_RelNoneg-OWA-D5-251_Q10 | False | Unknown ✗ | Unknown ✗ | F:5 U:7 | 1 |
88	| ProofWriter_AttNoneg-OWA-D5-500_Q8 | False | False ✓ | False ✓ | F:7 U:5 | 1 |
89	| ProofWriter_RelNeg-OWA-D5-721_Q8 | False | False ✓ | False ✓ | T:1 F:7 U:4 | 3 |
90	
91	### 关键发现
92	
93	1. **SICA 的优势集中在 tie-breaking**: 所有差异题都是 6:6 平局，SICA 用约束权重正确打破了 3/4 次平局。
94	2. **FOLIO 受益更大**: FOLIO 的自然语言推理更容易产生分歧（Unknown vs False/True 边界模糊），SICA 约束加权在此类场景有效。
95	3. **ProofWriter 多候选但无 gap**: ProofWriter 虽然 60% 题有多候选（高于 FOLIO 的 46.7%），但 SICA 和 SC 在该域持平，说明多候选不一定导致 accuracy 差异。
96	4. **约束提取极其可靠**: 100% trace 成功提取约束，表明 14B 模型生成的 CoT 结构化程度高。
97	5. **排除率适中 (2.59%)**: 既有矛盾检出能力，又不会过度排除导致信息丢失。
98	6. **统计显著性不足**: bootstrap p=0.226，样本量(60题)下 +2 题的差异难以达到统计显著。需要更大样本或更极端场景来确认 SICA 的可靠优势。
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "356d3bd8-2f01-4048-a27a-d527a6283ef0",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "9ffdc981-482e-49de-9d69-e0506a8b5254",
  "sourceToolAssistantUUID": "356d3bd8-2f01-4048-a27a-d527a6283ef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T13:11:03.184Z_

<details open><summary>🔧 Tool call — Read · `toolu_016M4NMGFGNibWNCGEo3yvYZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/tiebreak_analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ffdc981-482e-49de-9d69-e0506a8b5254",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6Ja8fXVtg7JaF9sXhox",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "766acc67-2838-4b7c-9bce-1f0e8c1c820a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qn5L7Q6igGCUarG6pTSC22",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3830,
      "cache_read_input_tokens": 63835,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3830
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 63835,
          "cache_creation_input_tokens": 3830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3830,
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

_source line 38 · 2026-05-16T13:11:03.190Z_

<details><summary>↩ Tool result · `toolu_016M4NMGFGNibWNCGEo3yvYZ`</summary>

```text
1	## Tiebreak Baseline Analysis (D017 Task 3)
2	
3	**60 题中 5 题出现平局（top-2 候选票数相同）**
4	
5	### 策略对比
6	
7	| Method | Accuracy | 95% CI | Correct/Total |
8	|--------|----------|--------|---------------|
9	| **SICA (constraint-weighted)** | **80.0%** | — | **4/5** |
10	| Random (bootstrap 10k) | 50.0% | [0.0, 100.0] | — |
11	| Alphabetical | 60.0% | — | 3/5 |
12	| First-seen | 40.0% | — | 2/5 |
13	| Majority-of-first-6 | 60.0% | — | 3/5 |
14	
15	### SICA Wins（4题）
16	- P11: False vs Unknown 各5票，SICA分数 145.5 vs 127.0，margin=18.5 → 选 False ✓
17	- P29: False vs Unknown 各6票，SICA分数 3.0 vs 33.0，margin=30.0 → 选 Unknown ✓
18	- P42: Unknown vs False 各6票，SICA分数 45.0 vs 46.0，margin=1.0 → 选 False ✓
19	- P59: False vs Unknown 各6票，SICA分数 61.0 vs 64.0，margin=3.0 → 选 Unknown ✓
20	
21	### SICA Loss（1题）
22	- P03: True vs Unknown 各6票，SICA分数 102.0 vs 105.0，delta=3.0 → 选了 Unknown，实际答案 True
23	
24	### 关键发现
25	- SICA 的 margin 分布：30.0 / 18.5 / 3.0 / 1.0（wins）vs 3.0（loss）
26	- 唯一 loss 的 margin 仅 3.0，属边界情况
27	- SICA 比 SC 多对 2 题（44/60 vs 42/60 = +3.3pp）
28	
29	Source: results/tiebreak_analysis.json on westd-32608
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "766acc67-2838-4b7c-9bce-1f0e8c1c820a",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "5459b127-89d7-49c7-9bb8-7b9663a78d45",
  "sourceToolAssistantUUID": "766acc67-2838-4b7c-9bce-1f0e8c1c820a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T13:11:06.571Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RTWKL6BupV9gJ5uBYAFzju`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/exp-005/report/qwq_operating_regime.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5459b127-89d7-49c7-9bb8-7b9663a78d45",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JaVRwodJ9u2U4ihGrW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08bbb8a3-f532-435c-9d6b-97243edd26d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HZfLyr1iHMHQFY3exuVJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3346,
      "cache_read_input_tokens": 67665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3346,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 40 · 2026-05-16T13:11:06.614Z_

<details><summary>↩ Tool result · `toolu_01RTWKL6BupV9gJ5uBYAFzju`</summary>

```text
1	## QwQ-32B Operating Regime Analysis
2	
3	**Experiment**: exp-005 | **Date**: 2026-05-16 | **Model**: QwQ-32B (reasoning model)
4	
5	### Summary Table
6	
7	| Dataset | Domain | N | K | T | C0 (nominal) | C0 (effective†) | SICA acc | SC acc | Δ (pp) | Verdict |
8	|---------|--------|---|---|---|---------------|-----------------|----------|--------|--------|---------|
9	| AIME 2024 | Math | 22/30‡ | 12 | 0.7 | 0.0% (0/22) | 0.0% | 72.7% | 72.7% | 0.0 | SICA≡SC |
10	| ProofWriter D5 | Logic | 17/30‡ | 12 | 0.7 | 23.5% (4/17) | 5.9% (1/17) | 82.4% | 88.2% | **−5.9** | **SICA&lt;SC** |
11	| FOLIO (live test) | Logic | 2/30‡ | 4 | 0.7 | 0.0% (0/2) | 0.0% | 100% | 100% | 0.0 | SICA≡SC§ |
12	| MATH L4-5 (temp) | Math | 5 | 12 | 0.7/0.9/1.0 | 0.0% (0/5) | 0.0% | — | — | — | No divergence |
13	| **Combined (main)** | | **39** | **12** | **0.7** | **10.3% (4/39)** | **2.6% (1/39)** | | | | **C0 ≪ 20%** |
14	
15	†Effective C0 = problems with both multiple candidates AND successful constraint extraction
16	‡Experiments killed before completion (see notes)
17	§N=2, K=4: insufficient for meaningful analysis
18	
19	### ProofWriter Multi-Candidate Detail
20	
21	| Problem | Ground Truth | SC Vote Distribution | Constraints | SICA | SC | SICA✓ | SC✓ |
22	|---------|-------------|---------------------|-------------|------|-----|-------|-----|
23	| 616_Q7 | True | False:7, True:5 | **0** extracted | False | False | ✗ | ✗ |
24	| 498_Q8 | False | False:11, True:1 | 41 (4 traces) | **True** | False | **✗** | **✓** |
25	| 251_Q10 | False | Unknown:3, False:7, True:2 | **0** extracted | False | False | ✓ | ✓ |
26	| 31_Q12 | False | False:4, Unknown:8 | **0** extracted | Unknown | Unknown | ✗ | ✗ |
27	
28	**Critical finding on 498_Q8**: SICA scored minority answer True=38 > majority False=27, flipping SC's correct answer to wrong. Root cause: QwQ-32B re-reasons during constraint extraction instead of outputting structured JSON, producing biased constraints from 4/12 traces only.
29	
30	### Temperature Diversity Analysis
31	
32	| Problem | Level | T=0.7 | T=0.9 | T=1.0 | Divergence |
33	|---------|-------|-------|-------|-------|------------|
34	| algebra/2277 | 5 | 10/12→"0" | 9/12→"0" | 9/12→"0" | 0% |
35	| int_algebra/582 | 5 | 0/12 (truncated) | 0/12 (truncated) | 0/12 (truncated) | N/A |
36	| number_theory/427 | 5 | 12/12→"25" | 12/12→"25" | 12/12→"25" | 0% |
37	| precalculus/1199 | 4 | 2/12→"π" | 2/12→"π" | 3/12→"π" | 0% |
38	| precalculus/659 | 4 | 11/12→same | 10/12→same | 11/12→same | 0% |
39	
40	Even at T=1.0, QwQ-32B produces zero answer divergence. Truncation (max_tokens=4096) affected 2 problems but did not introduce diversity—just failures.
41	
42	### Key Finding
43	
44	QwQ-32B 作为 reasoning model，其 chain-of-thought 的确定性极高：
45	
46	1. **数学域 C0=0%**：K=12 条 trace 在 AIME 2024 的全部 22 题上产生完全一致的最终答案，即使 T 从 0.7 提升至 1.0 也无分歧
47	2. **逻辑域名义 C0=23.5%，但有效 C0=5.9%**：ProofWriter 4/17 题有多候选，但 3/4 约束提取完全失败（0 constraints），唯一有约束的题 SICA 反而选错
48	3. **综合有效 C0=2.6%**，远低于 SICA 有效阈值（≥20%）
49	
50	**结论**：SICA 的效用与模型的 trace diversity (C0) 正相关。Reasoning model 的自一致性使 SICA 退化为 SC（数学域），甚至劣于 SC（逻辑域，因约束提取偏差）。这验证了论文的 Operating Regime 预测，并支持了从 QwQ-32B pivot 到 Qwen2.5-14B-Instruct（C0=46%）的决策。
51	
52	### Data Sources
53	
54	| Experiment | Registry ID | Result File | Status |
55	|-----------|-------------|-------------|--------|
56	| AIME 2024 | sica_aime30_v3 | results/aime30_v2.json | killed at 22/30 |
57	| ProofWriter D5 | sica_proofwriter30_v2 | results/proofwriter_30_v2.json | killed at 17/30 |
58	| FOLIO live test | sica_folio30 | results/folio_livetest.json | 2-problem test only |
59	| Temp diversity | sica_temp_diversity | results/diversity_diagnosis.json | completed (negative) |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08bbb8a3-f532-435c-9d6b-97243edd26d3",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "61bfe919-b8ee-4694-95f2-6cb5aefc6769",
  "sourceToolAssistantUUID": "08bbb8a3-f532-435c-9d6b-97243edd26d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T13:11:07.099Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AMwj8JkE6VrHi3HKDfW2ZS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61bfe919-b8ee-4694-95f2-6cb5aefc6769",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JaVRwodJ9u2U4ihGrW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70749118-5a68-4128-b49a-e60cb4df1c8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HZfLyr1iHMHQFY3exuVJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3346,
      "cache_read_input_tokens": 67665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3346,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 42 · 2026-05-16T13:11:07.108Z_

<details><summary>↩ Tool result · `toolu_01AMwj8JkE6VrHi3HKDfW2ZS`</summary>

```text
1	experiments:
2	  # ==== P0: Must-run for any submission ====
3	
4	  - id: exp-001
5	    name: sica_expanded_14b
6	    claim: [1, 2]
7	    description: "Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7. Maximizes statistical power for C3 significance."
8	    priority: P0
9	    gpu_budget_hours: 14
10	    deps: []
11	    registry_id: sica_expanded_14b
12	    status: running
13	
14	  - id: exp-002
15	    name: sica_k_ablation_14b
16	    claim: [1]
17	    description: "K sensitivity (K=6,8,12,16,20) on D012's 60 questions. Key questions: does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)? How does tiebreak frequency change with K?"
18	    priority: P0
19	    gpu_budget_hours: 5
20	    deps: []
21	    status: planned
22	
23	  - id: exp-003
24	    name: tiebreak_baseline_analysis
25	    claim: [1]
26	    description: "Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair baselines."
27	    priority: P0
28	    gpu_budget_hours: 0
29	    deps: [sica_d012_14b]
30	    status: done
31	    note: "Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80% (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d"
32	
33	  # ==== P1: Important for strong submission ====
34	
35	  - id: exp-004
36	    name: sica_7b_scaling
37	    claim: [2, 3]
38	    description: "Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim."
39	    priority: P1
40	    gpu_budget_hours: 2
41	    deps: [exp-001]
42	    status: planned
43	
44	  - id: exp-005
45	    name: qwq_32b_operating_regime
46	    claim: [2]
47	    description: "QwQ-32B negative results formatted for paper's Operating Regime Analysis section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU needed."
48	    priority: P1
49	    gpu_budget_hours: 0
50	    deps: []
51	    status: done
52	    note: "Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate), sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题, 0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains."
53	
54	  - id: exp-006
55	    name: c0_diagnostic_validation
56	    claim: [3]
57	    description: "Plot C0 vs SICA-SC gap across all models and K values. Validate C0 as predictor. CPU-only analysis over exp-001/002/004/005 results."
58	    priority: P1
59	    gpu_budget_hours: 0
60	    deps: [exp-001, exp-002, exp-004]
61	    status: planned
62	
63	  # ==== P2: Nice-to-have / Camera-ready ====
64	
65	  - id: exp-007
66	    name: sica_72b_awq
67	    claim: [2]
68	    description: "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis: high-baseline non-reasoning model. Within-Qwen scaling dimension."
69	    priority: P1
70	    gpu_budget_hours: 4
71	    deps: [exp-001]
72	    status: planned
73	    note: "D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX PRO 6000 单卡可放。"
74	
75	  - id: exp-008
76	    name: constraint_quality_case_studies
77	    claim: [1]
78	    description: "Qualitative analysis of extracted constraints on 5-10 representative questions. Are constraints semantically meaningful? Do excluded constraints correspond to reasoning errors?"
79	    priority: P2
80	    gpu_budget_hours: 0
81	    deps: [exp-001]
82	    status: planned
83	
84	  - id: exp-009
85	    name: overhead_analysis
86	    claim: [1]
87	    description: "Wall-time breakdown per question: generation, constraint extraction, MaxSAT solving. Address 'is the overhead worth it' concern."
88	    priority: P1
89	    gpu_budget_hours: 0
90	    deps: [exp-001]
91	    status: planned
92	    note: "D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。"
93	
94	  # ==== D021 Scope 扩展：跨家族 + 跨域 + ablation ====
95	
96	  - id: exp-010
97	    name: sica_mistral_7b
98	    claim: [2, 3]
99	    description: "Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family validation: does C0 pattern hold outside Qwen? Eliminates 'Qwen-specific artifact' attack."
100	    priority: P0
101	    gpu_budget_hours: 1.5
102	    deps: []
103	    status: planned
104	    note: "D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+ 题（~3h GPU，margin 允许）。"
105	
106	  - id: exp-011
107	    name: sica_llama_8b
108	    claim: [2, 3]
109	    description: "LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family. Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA)."
110	    priority: P0
111	    gpu_budget_hours: 1.5
112	    deps: []
113	    status: planned
114	    note: "D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation 同 exp-010。"
115	
116	  - id: exp-012
117	    name: gsm8k_pilot_14b
118	    claim: [2, 3]
119	    description: "Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test: is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain win."
120	    priority: P1
121	    gpu_budget_hours: 1
122	    deps: []
123	    status: planned
124	    note: "D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable insight."
125	
126	  - id: exp-013
127	    name: constraint_ablation
128	    claim: [1]
129	    description: "CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count per answer, no satisfiability) vs SICA-random-weight. Tests whether MAX-SAT is essential or over-engineering."
130	    priority: P1
131	    gpu_budget_hours: 0
132	    deps: [exp-001]
133	    status: planned
134	    note: "D021 新增. 防御 'over-engineering' reviewer attack. CPU-only, 零 GPU 成本。"
135	
136	  - id: exp-014
137	    name: sica_deepseek_r1_llama_8b
138	    claim: [2]
139	    description: "DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning model data point with LLaMA base architecture: validates C0<5% generalizes beyond QwQ-32B AND eliminates 'still Qwen family' attack."
140	    priority: P1
141	    gpu_budget_hours: 2
142	    deps: []
143	    status: planned
144	    note: "D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。"
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70749118-5a68-4128-b49a-e60cb4df1c8d",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "e3d3f2cc-d529-4db5-b200-d3928493c3e0",
  "sourceToolAssistantUUID": "70749118-5a68-4128-b49a-e60cb4df1c8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T13:11:10.168Z_

Now let me check what experiments have actually completed versus what's imagined in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3d3f2cc-d529-4db5-b200-d3928493c3e0",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JanHhp6SqkzzchuB8m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15028451-084b-4223-98c4-575b026394db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBiy4vM8A9Zsz2jDYZYkyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 71011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4571,
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

_source line 44 · 2026-05-16T13:11:11.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L3Nn414Rb5n9Gtdyb1Nfxc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15028451-084b-4223-98c4-575b026394db",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JanHhp6SqkzzchuB8m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9028b6fd-dfbd-4dea-bc11-77eb5ce1c541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBiy4vM8A9Zsz2jDYZYkyn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 71011,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4571
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 71011,
          "cache_creation_input_tokens": 4571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4571,
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

_source line 45 · 2026-05-16T13:11:11.603Z_

<details><summary>↩ Tool result · `toolu_01L3Nn414Rb5n9Gtdyb1Nfxc`</summary>

```text
1	baseline: null
2	experiments:
3	  crd_folio_main:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-15T09:35:42.037Z'
7	    updated_at: '2026-05-15T09:36:24.832Z'
8	    spec:
9	      command: python run_pipeline.py (CRD dual-representation pipeline)
10	      server: westd-32608
11	      data_path: /root/autodl-tmp/crdd/results/mvp_v4_full.jsonl
12	      data_count: 204
13	      model_name: Qwen3-32B-AWQ
14	      seed: 42
15	      method: CRD
16	      checkpoint_path: N/A
17	      log_path: /root/autodl-tmp/crdd/results/
18	    conclusion: success
19	    completed_at: '2026-05-15T09:36:03.793Z'
20	    hypothesis: 'CRD: 双表征(FOL+SymPy)分歧检测+定向修复能提升逻辑推理准确率（非SICA方法）'
21	    metrics:
22	      divergence_rate: 0.422
23	      diagnosis_rate: 0.872
24	      error_types: 4
25	      directed_advantage_pp: 4.7
26	      directed_p_value: 0.63
27	      localization_accuracy: 0.946
28	      fol_accuracy: 0.789
29	      code_accuracy: 0.598
30	      oracle_accuracy: 0.878
31	      pipeline_accuracy: 0.814
32	      baseline_accuracy: 0.74
33	      cost_multiplier: 5.76
34	      dataset: FOLIO
35	      n: 204
36	  smoke-test-5q:
37	    status: PREPARING
38	    retry_count: 0
39	    created_at: '2026-05-15T11:22:09.665Z'
40	    updated_at: '2026-05-15T11:22:09.666Z'
41	    conclusion: failed
42	  sica_smoke_5q:
43	    status: DONE
44	    retry_count: 0
45	    created_at: '2026-05-15T11:38:43.996Z'
46	    updated_at: '2026-05-15T11:39:13.456Z'
47	    spec:
48	      command: python3 smoke_test_5q.py (nohup)
49	      server: westd-32608
50	      data_path: /root/symb_invariant_consensus/data/math500_subset.json
51	      data_count: 5
52	      model_name: QwQ-32B
53	      seed: 42
54	      method: SICA
55	      checkpoint_path: N/A
56	      log_path: /tmp/smoke_test_5q.log
57	    hypothesis: 'SICA smoke test: 验证端到端 pipeline 可行性（5题 MATH-500, K=12, QwQ-32B）'
58	    conclusion: success
59	    completed_at: '2026-05-15T11:39:07.006Z'
60	    metrics:
61	      sica_accuracy: 0.8
62	      sc_accuracy: 0.8
63	      extraction_rate: 1
64	      problems_with_contradictions: 1
65	      total_problems: 5
66	      total_time_s: 3505
67	      avg_time_per_problem_s: 701
68	      per_problem:
69	      - id: algebra/2470
70	        level: 1
71	        sica_correct: true
72	        sc_correct: true
73	        constraints: 27
74	        unique: 9
75	        excluded: 0
76	      - id: prealgebra/65
77	        level: 2
78	        sica_correct: true
79	        sc_correct: true
80	        constraints: 26
81	        unique: 2
82	        excluded: 0
83	      - id: number_theory/847
84	        level: 3
85	        sica_correct: true
86	        sc_correct: true
87	        constraints: 21
88	        unique: 11
89	        excluded: 0
90	        note: 14 JSON parse failures, 1693s
91	      - id: precalculus/1199
92	        level: 4
93	        sica_correct: false
94	        sc_correct: false
95	        constraints: 35
96	        unique: 6
97	        excluded: 0
98	        note: graph-reading problem, model cannot see image
99	      - id: algebra/2277
100	        level: 5
101	        sica_correct: true
102	        sc_correct: true
103	        constraints: 60
104	        unique: 6
105	        satisfied: 3
106	        excluded: 3
107	  sica_temp_diversity:
108	    status: DONE
109	    retry_count: 0
110	    created_at: '2026-05-15T12:14:34.555Z'
111	    updated_at: '2026-05-15T12:15:01.382Z'
112	    spec:
113	      command: python3 diagnose_diversity.py
114	      server: westd-32608
115	      data_path: /root/symb_invariant_consensus/data/math500_subset.json
116	      data_count: 5
117	      model_name: QwQ-32B
118	      seed: 42
119	      method: SICA-diagnostic
120	      checkpoint_path: N/A
121	      log_path: /root/symb_invariant_consensus/results/diversity_diagnosis.json
122	    hypothesis: 不同 temperature (0.7/0.9/1.0) 下 QwQ-32B 是否产生足够的 trace 分歧以触发 MAX-SAT
123	      矛盾检测
124	    conclusion: negative
125	    completed_at: '2026-05-15T12:14:56.903Z'
126	    metrics:
127	      temperatures_tested:
128	      - 0.7
129	      - 0.9
130	      - 1
131	      problems_tested: 3
132	      problems_with_divergence: 0
133	      finding: QwQ-32B produces zero answer divergence at all temperatures on MATH
134	        L4-5. Reasoning model's deterministic chain dominates sampling randomness.
135	      max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)
136	      recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for
137	        trace diversity
138	  mvp_math50_t07:
139	    status: DONE
140	    retry_count: 0
141	    created_at: '2026-05-15T12:16:29.416Z'
142	    updated_at: '2026-05-15T12:21:37.283Z'
143	    spec:
144	      command: nohup python3 run_full_mvp.py --mode vllm --k 12 --output results/mvp_math50_t07.json
145	        > /tmp/mvp_math50.log 2>&1 &
146	      server: westd-32608
147	      data_path: /root/symb_invariant_consensus/data/math500_subset.json
148	      data_count: 50
149	      model_name: QwQ-32B
150	      seed: 42
151	      method: SICA
152	      checkpoint_path: results/mvp_math50_t07.json
153	      log_path: /tmp/mvp_math50.log
154	      temperature: 0.7
155	      k: 12
156	    hypothesis: 'SICA MVP: 50题MATH-500上跨路径MAX-SAT约束共识能否检测矛盾并超越SC@K=12'
157	    conclusion: killed
158	    completed_at: '2026-05-15T12:21:37.283Z'
159	  sica_aime30_t07:
160	    status: DONE
161	    retry_count: 0
162	    created_at: '2026-05-15T12:38:16.330Z'
163	    updated_at: '2026-05-15T13:11:37.911Z'
164	    spec:
165	      command: python run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens
166	        10240 --math-data data/aime2024_subset.json --output results/aime30_t07.json
167	        --no-proofwriter
168	      server: westd-32608
169	      gpu:
170	      - cuda:0
171	      pid: '119338'
172	      log_path: ~/runs/symb_invariant_consensus/sica_aime30_t07.log
173	      submitted_at: '2026-05-15T13:01:07.184Z'
174	      submitted_via: submit_training_job
175	      backend: tmux
176	      account: root
177	      data_path: data/aime2024_subset.json
178	      data_count: 30
179	      model_name: QwQ-32B
180	      seed: null
181	      wall_clock_seconds: 630.7
182	      gpu_hours: 0.18
183	    hypothesis: AIME 2024（QwQ-32B 弱项，~79.5% acc）上 SICA 能否检测更多跨路径矛盾并超越 SC@K=12——验证"SICA
184	      价值随问题难度递增"假设
185	    conclusion: killed
186	    completed_at: '2026-05-15T13:11:37.911Z'
187	  sica_aime30_v2:
188	    status: DONE
189	    retry_count: 0
190	    created_at: '2026-05-15T13:24:26.526Z'
191	    updated_at: '2026-05-15T16:11:32.132Z'
192	    spec:
193	      command: PYTHONUNBUFFERED=1 python -u run_full_mvp.py --mode vllm --k 12 --temperature
194	        0.7 --max-tokens 10240 --math-data data/aime2024_subset.json --output results/aime30_v2.json
195	        --no-proofwriter --seed 42
196	      server: westd-32608
197	      gpu:
198	      - cuda:0
199	      pid: '121139'
200	      log_path: /tmp/sica_aime30_v2.log
201	      submitted_at: '2026-05-15T13:24:26.512Z'
202	      submitted_via: submit_training_job
203	      backend: tmux
204	      account: root
205	      method: SICA
206	      model_name: QwQ-32B
207	      data_path: /root/symb_invariant_consensus/data/aime2024_subset.json
208	      data_count: 30
209	      k: 12
210	      temperature: 0.7
211	      max_tokens: 10240
212	      seed: null
213	      seed_note: --seed 42 在命令行中但 run_full_mvp.py 可能未实现该参数，实际 seed 未生效
214	      fixes: timeout=120s HTTP, future timeout=180s, semaphore(6), vLLM health check
215	      wall_clock_seconds: 8899.6
216	      gpu_hours: 2.47
217	    hypothesis: 'AIME 2024 上 SICA 能否检测跨路径矛盾并超越 SC@K=12（v2: 修复 timeout/hang bug 后重跑）'
218	    conclusion: killed
219	    metrics:
220	      progress: 4/30
221	      sica_accuracy_interim: 3/4 (75%)
222	      sc_accuracy_interim: 3/4 (75%)
223	      avg_time_per_problem_s: 557
224	      p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted
225	      p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds
226	      issue: vLLM service likely crashed or OOM at Problem 5
227	      analysis_contradiction_rate_aime: 50% (2/4)
228	      analysis_contradiction_rate_math: 20% (1/5)
229	      analysis_unique_constraints_per_problem_aime: 18.7
230	      analysis_exclusion_rate: 10.7%
231	      analysis_sica_sc_agreement: 9/9 (100%)
232	      analysis_signal: weak positive - mechanism works but SC too unanimous to flip
233	      analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure
234	    reproduce:
235	      finished_at: '2026-05-15T15:52:45.450Z'
236	    failure_reason: EXIT_CODE=129 (non-zero)
237	    completed_at: '2026-05-15T15:52:46.068Z'
238	    extra:
239	      hook_events:
240	      - event: on_failed
241	        action: agent
242	        ts: '2026-05-15T15:52:46.737218+00:00'
243	    notes: '失败原因: Problem 5 (aime2024_II_05, 凸六边形几何题) 12条并发trace在单GPU上竞争资源→每条trace吞吐极低→客户端~600s超时后重试→旧请求仍在vLLM
244	      running→恶性循环卡死~1h47min | 已有成果: 4/30题完成 SICA 3/4=75% SC 3/4=75%, P2有Z3Exception(0
245	      constraints extracted) | vLLM本身健康(test request <1s) | 建议: 降低并发k或分批处理trace(如4条/批),
246	      增大client timeout, kill stuck requests后重启'
247	  sica_aime30_v3:
248	    status: DONE
249	    retry_count: 0
250	    created_at: '2026-05-15T16:13:04.296Z'
251	    updated_at: '2026-05-15T22:07:55.967Z'
252	    hypothesis: 'AIME 2024 上 SICA 能否检测跨路径矛盾并超越 SC@K=12（v3: timeout=1800s, 从v2 P5恢复继续）'
253	    spec:
254	      command: PYTHONUNBUFFERED=1 python -u run_full_mvp.py --mode vllm --k 12 --temperature
255	        0.7 --max-tokens 10240 --math-data data/aime2024_subset.json --output results/aime30_v2.json
256	        --no-proofwriter --seed 42 --resume
257	      server: westd-32608
258	      gpu:
259	      - cuda:0
260	      pid: '129992'
261	      log_path: /root/runs/symb_invariant_consensus/sica_aime30_v2_resume.log
262	      account: root
263	      method: SICA
264	      model_name: QwQ-32B
265	      data_path: /root/symb_invariant_consensus/data/aime2024_subset.json
266	      data_count: 30
267	      seed: 42
268	      k: 12
269	      temperature: 0.7
270	      max_tokens: 10240
271	      fixes: timeout=1800s; n=4 batching on disk but not loaded by running process
272	      resumed_from: sica_aime30_v2 (4/30 completed)
273	      remaining_problems: 26
274	    parent: sica_aime30_v2
275	    notes: 'v3 killed at 22/30 (PID 129992, 6h11m). Vote diversity analysis: multi-candidate
276	      rate = 0.0%, all valid problems have exactly 1 candidate. SICA≡SC confirmed
277	      structural. 6/22 problems with 0 votes (extraction failure). 数学域结论锁定，转逻辑域。'
278	    metrics:
279	      progress: 22/30
280	      sica_accuracy_interim: 16/22 (72.7%)
281	      sc_accuracy_interim: 16/22 (72.7%)
282	      sica_sc_gap_pp: 0
283	      avg_time_per_problem_s: 645.9
284	      runtime_h: 5.9
285	      remaining_problems: 8
286	      vote_diversity_analysis:
287	        valid_problems: 16
288	        total_problems: 22
289	        multi_candidate_rate: 0
290	        zero_vote_problems: 6
291	        zero_vote_indices:
292	        - 1
293	        - 7
294	        - 8
295	        - 10
296	        - 13
297	        - 14
298	        constraints_extracted: 19/22
299	        exclusion_rate: 0.387
300	        conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC
301	          structurally. MaxSAT exclusion operates but cannot change final selection
302	          with only 1 candidate.
303	      process_status: gone (cron miss 1/5)
304	    conclusion: killed
305	    completed_at: '2026-05-15T22:07:52.491Z'
306	  sica_proofwriter30:
307	    status: DONE
308	    retry_count: 0
309	    created_at: '2026-05-15T22:08:42.831Z'
310	    updated_at: '2026-05-15T22:18:19.326Z'
311	    hypothesis: 逻辑域（ProofWriter D5）上 SICA 能否检测跨路径 FOL 约束矛盾并超越 SC@K=12——验证 SICA 在逻辑推理域的有效性
312	    parent: sica_aime30_v3
313	    spec:
314	      command: python eval_proofwriter.py --n-problems 30 --k 12 --max-tokens 16384
315	        --seed 42 --save-intermediates --output results/proofwriter_30_eval.json
316	      server: westd-32608
317	      gpu:
318	      - cuda:0
319	      pid: '153924'
320	      log_path: /root/runs/symb_invariant_consensus/proofwriter30.log
321	      submitted_at: '2026-05-15T22:11:44.644Z'
322	      submitted_via: submit_training_job
323	      backend: tmux
324	      account: root
325	      method: SICA
326	      model_name: QwQ-32B
327	      data_path: /root/symb_invariant_consensus/data/proofwriter_subset.json
328	      data_count: 30
329	      seed: 42
330	      k: 12
331	      temperature: 0.7
332	      max_tokens: 16384
333	      domain: logic
334	      extraction_prompt: LOGIC_EXTRACTION_PROMPT
335	      z3_timeout_s: 60
336	      checkpoint_source: N/A (not eval - new SICA logic domain experiment)
337	      eval_data: ProofWriter D5 30 problems (T:10 F:10 U:10)
338	      wall_clock_seconds: 378.0
339	      gpu_hours: 0.1
340	    reproduce:
341	      finished_at: '2026-05-15T22:15:57.895Z'
342	    extra:
343	      hook_events:
344	      - event: on_complete
345	        action: agent
346	        ts: '2026-05-15T22:15:58.664228+00:00'
347	    conclusion: failed
348	    completed_at: '2026-05-15T22:18:02.631Z'
349	    notes: 配置错误导致完全失败。--max-tokens 16384 等于 vLLM 的 --max-model-len 16384，prompt 输入空间为
350	      0，所有 30 题从第 1 题起全部 400 Bad Request。没有生成任何 trace，没有提取约束，没有投票。4 分钟内跑完（全是 retry
351	      耗时）。无法评估 sanity check 标准。需要用 --max-tokens 12288 或更小值重跑（AIME 实验用的 10240 正常工作）。
352	    metrics:
353	      sica_accuracy: 0/30 (0.0%)
354	      sc_accuracy: 0/30 (0.0%)
355	      sica_sc_gap_pp: 0
356	      total_wall_time_s: 238.9
357	      total_wall_time_min: 4
358	      avg_time_per_problem_s: 8
359	      traces_generated: 0
360	      constraints_extracted: 0
361	      traces_with_constraints: 0
362	      unique_constraints: 0
363	      maxsat_satisfied: 0
364	      maxsat_excluded: 0
365	      multi_candidate_rate: N/A (no traces generated)
366	      vote_diversity: N/A
367	      z3_errors: 0
368	      z3_timeouts: 0
369	      problems_with_contradiction: 0
370	      problems_with_votes: 0
371	      failure_mode: ALL_400_BAD_REQUEST
372	      failure_count: 30/30
373	      root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for
374	        prompt input. Every API call returns 400.
375	    checkpoint_path: /root/symb_invariant_consensus/results/proofwriter_30_eval.json
376	    log_path: /root/runs/symb_invariant_consensus/proofwriter30.log
377	  sica_folio30:
378	    status: DONE
379	    retry_count: 0
380	    created_at: '2026-05-15T22:08:43.460Z'
381	    updated_at: '2026-05-16T04:42:53.530Z'
382	    hypothesis: 逻辑域（FOLIO）上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12——FOLIO 有天然 FOL 标注，是
383	      SICA 约束提取的理想场景
384	    parent: sica_aime30_v3
385	    spec:
386	      hypothesis: FOLIO 逻辑域上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12
387	      dataset: FOLIO (yale-nlp/FOLIO validation subset)
388	      data_path: /root/symb_invariant_consensus/data/folio_subset.json
389	      data_count: 30
390	      label_distribution:
391	        'True': 10
392	        'False': 10
393	        Unknown: 10
394	      has_fol_annotations: true
395	      model_name: QwQ-32B
396	      server: westd-32608
397	      command: python eval_folio.py --n-problems 30 --k 12 --temperature 0.7 --max-tokens
398	        12288 --seed 42 --save-intermediates --output results/folio_eval.json
399	      k: 12
400	      temperature: 0.7
401	      max_tokens: 12288
402	      seed: 42
403	      eval_script: /root/symb_invariant_consensus/eval_folio.py
404	      dry_run_passed: true
405	      live_test_passed: true
406	      live_test_result: 2/2 correct (SICA=100%, SC=100%), pipeline all stages functional
407	    notes: 废弃：QwQ-32B spec（max_tokens=12288），已被 sica_d012_14b（Qwen2.5-14B-Instruct
408	      全量 D012 评估）覆盖。QwQ-32B 全域 C0 FAIL (3.6%)，模型已 pivot。
409	    conclusion: killed
410	    completed_at: '2026-05-16T04:42:50.715Z'
411	  sica_proofwriter30_v2:
412	    status: DONE
413	    retry_count: 0
414	    created_at: '2026-05-15T22:19:01.325Z'
415	    updated_at: '2026-05-16T01:38:43.002Z'
416	    hypothesis: '逻辑域（ProofWriter D5）上 SICA 能否检测跨路径 FOL 约束矛盾并超越 SC@K=12（v2: max_tokens=12288
417	      修复）'
418	    parent: sica_proofwriter30
419	    spec:
420	      command: python eval_proofwriter.py --n-problems 30 --k 12 --max-tokens 12288
421	        --seed 42 --save-intermediates --output results/proofwriter_30_v2.json
422	      server: westd-32608
423	      gpu:
424	      - cuda:0
425	      pid: '155077'
426	      log_path: /root/runs/symb_invariant_consensus/proofwriter30_v2.log
427	      submitted_at: '2026-05-15T22:19:16.529Z'
428	      submitted_via: submit_training_job
429	      backend: tmux
430	      account: root
431	      method: SICA
432	      model_name: QwQ-32B
433	      data_path: /root/symb_invariant_consensus/data/proofwriter_subset.json
434	      data_count: 30
435	      seed: 42
436	      k: 12
437	      temperature: 0.7
438	      max_tokens: 12288
439	      domain: logic
440	      extraction_prompt: LOGIC_EXTRACTION_PROMPT
441	      z3_timeout_s: 60
442	      checkpoint_source: N/A (new SICA logic domain experiment, retry of sica_proofwriter30
443	        with fixed max_tokens)
444	      eval_data: ProofWriter D5 30 problems (T:10 F:10 U:10)
445	      wall_clock_seconds: 11503.9
446	      gpu_hours: 3.2
447	    notes: 16/30 killed (Director 指令)。D012 四项全 FAIL。MaxSAT 根因诊断结论：三层问题叠加——(1) 约束提取失败
448	      54.4%，QwQ-32B 收到 extraction prompt 后重新推理而非输出 JSON，3/4 多候选题提取为零；(2) 一致投票=一致约束，14/17
449	      题 12/12 同一答案，约束天然不矛盾（正确行为非 bug）；(3) 评分偏差，唯一 SICA≠SC 的题 498_Q8，SICA 给少数派 38 分
450	      > 多数派 27 分，因提取失败非随机。MaxSAT 求解器本身无 bug（注入测试 6/6 通过）。推荐修复：L3 自动注入 answer==trace_answer
451	      约束使不同答案 trace 必有冲突；L1 提取用 system prompt 强制 JSON-only。
452	    conclusion: killed
453	    completed_at: '2026-05-16T01:31:00.468Z'
454	  sica_d016_c0_precheck:
455	    status: DONE
456	    retry_count: 0
457	    created_at: '2026-05-16T04:00:14.192Z'
458	    updated_at: '2026-05-16T04:01:11.163Z'
459	    hypothesis: D016 模型 pivot C0 预检：Qwen2.5-14B-Instruct 在逻辑域是否产生足够 trace 多样性（多候选率
460	      ≥20%）
461	    parent: sica_proofwriter30_v2
462	    spec:
463	      command: python sica_pipeline.py --data folio_subset.json+proofwriter_subset.json
464	        --K 6 --T 0.7 --max-tokens 4096 --model Qwen2.5-14B-Instruct
465	      server: westd-32608
466	      data_path: data/folio_subset.json (10q) + data/proofwriter_subset.json (16q)
467	      data_count: 26
468	      model_name: Qwen2.5-14B-Instruct
469	      seed: 42
470	      gpu: cuda:0
471	      model_path: /root/autodl-tmp/models/Qwen2.5-14B-Instruct
472	      hyperparams:
473	        K: 6
474	        T: 0.7
475	        max_tokens: 4096
476	        max_model_len: 8192
477	      checkpoint_source: N/A (inference-only, no checkpoint)
478	      eval_data: FOLIO-10 + ProofWriter-16 (C0 precheck subset)
479	    metrics:
480	      multi_candidate_rate_combined: 0.46
481	      multi_candidate_rate_folio: 0.4
482	      multi_candidate_rate_proofwriter: 0.5
483	      sc_accuracy_combined: 0.73
484	      sc_accuracy_folio: 0.8
485	      sc_accuracy_proofwriter: 0.69
486	      n_problems: 26
487	      n_folio: 10
488	      n_proofwriter: 16
489	      K: 6
490	      T: 0.7
491	      total_time_s: 280
492	      c0_gate: PASS (46% >= 20%)
493	      model: Qwen2.5-14B-Instruct
494	      vllm_gpu_mem_gib: 27.6
495	      smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem
496	    conclusion: success
497	    notes: 'C0 PASS: Qwen2.5-14B-Instruct 多候选率 46% (FOLIO 40%, ProofWriter 50%)，远超
498	      20% 阈值。对比 QwQ-32B 全域 3.6%，提升 12.8x。SC accuracy 73% (FOLIO 80%, PW 69%)。Smoke
499	      test 2题 SICA pipeline 端到端通过。vLLM PID 174291, 27.6 GiB, max-model-len=8192。Report:
500	      art_20260516_e2774d。'
501	    checkpoint_path: N/A (inference-only precheck, no checkpoint)
502	    log_path: artifacts/_project/report/d016_model_pivot_report.md (art_20260516_e2774d)
503	    completed_at: '2026-05-16T04:01:11.163Z'
504	  sica_d012_14b:
505	    status: DONE
506	    retry_count: 0
507	    created_at: '2026-05-16T04:02:41.309Z'
508	    updated_at: '2026-05-16T05:08:53.052Z'
509	    spec:
510	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
511	        base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 python
512	        run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --math-data
513	        /tmp/empty_math.json --pw-data data/proofwriter_30.json --folio-data data/folio_30.json
514	        --output results/sica_d012_14b.json --save-intermediates 2>&1 | tee /tmp/sica_d012_14b.log"
515	      server: westd-32608
516	      gpu:
517	      - cuda:0
518	      pid: '177178'
519	      log_path: ~/runs/symb_invariant_consensus/sica_d012_14b.log
520	      submitted_at: '2026-05-16T04:05:23.888Z'
521	      submitted_via: submit_training_job
522	      backend: tmux
523	      account: root
524	      data_path: data/proofwriter_30.json + data/folio_30.json
525	      data_count: 60
526	      model_name: Qwen2.5-14B-Instruct
527	      seed: 42
528	      wall_clock_seconds: 3809.2
529	      gpu_hours: 1.06
530	    reproduce:
531	      finished_at: '2026-05-16T05:04:49.668Z'
532	    extra:
533	      hook_events:
534	      - event: on_complete
535	        action: agent
536	        ts: '2026-05-16T05:04:50.574652+00:00'
537	    conclusion: success
538	    metrics:
539	      sica_accuracy: 0.7333
540	      sc_accuracy: 0.7
541	      sica_sc_gap_pp: 3.3
542	      c0_multi_candidate_rate: 0.5333
543	      c1_extraction_rate: 1
544	      c2_contradiction_problems: 34
545	      c3_gap_pp: 3.3
546	      bootstrap_p: 0.2261
547	      proofwriter_sica: 0.6667
548	      proofwriter_sc: 0.6667
549	      folio_sica: 0.8
550	      folio_sc: 0.7333
551	      total_constraints_raw: 5849
552	      total_constraints_unique: 1735
553	      maxsat_exclusion_rate: 0.0259
554	      wall_time_min: 58.3
555	      d012_verdict: ALL_PASS
556	    checkpoint_path: /root/symb_invariant_consensus/results/sica_d012_14b.json
557	    completed_at: '2026-05-16T05:08:53.052Z'
558	  sica_expanded_14b:
559	    status: RUNNING
560	    retry_count: 0
561	    created_at: '2026-05-16T05:12:00.374Z'
562	    updated_at: '2026-05-16T05:33:25.903Z'
563	    spec:
564	      command: python run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens
565	        4096 --pw-data data/proofwriter_full.json --folio-data data/folio_full.json
566	        --math-data data/empty.json --output results/sica_expanded_14b.json --save-intermediates
567	      server: westd-32608
568	      data_path: data/proofwriter_full.json (600 D5) + data/folio_full.json (204)
569	      data_count: 804
570	      model_name: Qwen2.5-14B-Instruct
571	      seed: 42
572	      pid: '181491'
573	      gpu:
574	      - cuda:0
575	      log_path: ~/runs/symb_invariant_consensus/sica_expanded_14b.log
576	      submitted_at: '2026-05-16T05:19:00.966Z'
577	      backend: nohup
578	      account: root
579	      eta_hours: 13.4
580	  sica_k_sensitivity_14b:
581	    status: QUEUED
582	    retry_count: 0
583	    created_at: '2026-05-16T05:12:03.025Z'
584	    updated_at: '2026-05-16T05:12:03.025Z'
585	    spec:
586	      hypothesis: K 敏感性分析：K=6/8/12/16/20 下 SICA 的多候选率、平票数和 accuracy gap 变化曲线
587	      parent: sica_d012_14b
588	      model_name: Qwen2.5-14B-Instruct
589	      data_path: D012 60题 + K=16/20 额外 inference
590	      server: westd-32608
591	      seed: 42
592	      hyperparams:
593	        K_values:
594	        - 6
595	        - 8
596	        - 12
597	        - 16
598	        - 20
599	        temperature: 0.7
600	        max_tokens: 4096
601	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9028b6fd-dfbd-4dea-bc11-77eb5ce1c541",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "ff282cbb-cadc-4db6-aed4-d1e1466cd273",
  "sourceToolAssistantUUID": "9028b6fd-dfbd-4dea-bc11-77eb5ce1c541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-16T13:11:15.494Z_

Now I have a comprehensive understanding of the project. Let me also check the dream review reports that were already generated to understand any prior review perspectives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff282cbb-cadc-4db6-aed4-d1e1466cd273",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6Jb7Jx5gfsUDywNBrZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1eb2ec9-637c-4130-8515-ac710dbc9e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrxNb5EixP7xUBQEAgiBwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10276,
      "cache_read_input_tokens": 75582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10276,
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

_source line 47 · 2026-05-16T13:11:17.043Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Cnfzj6YEmpEnxYjdpj1ea`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1eb2ec9-637c-4130-8515-ac710dbc9e8d",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6Jb7Jx5gfsUDywNBrZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01215fa0-1e78-4e02-8eeb-3a16cc34f88f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrxNb5EixP7xUBQEAgiBwQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10276,
      "cache_read_input_tokens": 75582,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 75582,
          "cache_creation_input_tokens": 10276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10276,
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

_source line 48 · 2026-05-16T13:11:17.058Z_

<details><summary>↩ Tool result · `toolu_019Cnfzj6YEmpEnxYjdpj1ea`</summary>

```text
1	---
2	dream_id: dream_20260516T054054
3	tier: best
4	overall_score: Weak Reject (3/6)
5	timestamp: 2026-05-16T06:28:31.566681+00:00
6	---
7	
8	
9	# Review Report — R1 (Methodology & Experiments)
10	
11	## Paper
12	"Principled Symbolic Consensus Improves LLM Reasoning" (best-tier dream)
13	
14	---
15	
16	## Summary
17	
18	The paper proposes SICA, which extracts FOL constraints from LLM reasoning traces and uses weighted partial MAX-SAT to aggregate answers, primarily improving over Self-Consistency (SC) in tie-breaking scenarios. The main claim is a +3.8pp improvement on 804 logic reasoning questions (p=0.023) with Qwen2.5-14B-Instruct, along with an operating regime characterization showing that trace diversity (C0) predicts when SICA helps. The paper also demonstrates that reasoning models (QwQ-32B) with near-zero trace diversity cause SICA to degenerate to SC.
19	
20	---
21	
22	## Strengths
23	
24	- **Well-defined pipeline.** The SICA pipeline (trace generation -> FOL extraction -> weighted partial MAX-SAT -> answer selection) is clearly specified and reproducible. The use of Z3 as the MAX-SAT solver is appropriate and the formalization of the weighted optimization objective is clean.
25	
26	- **Honest negative result integration.** The QwQ-32B data showing SICA degenerating to SC when C0 approaches zero is a genuine finding. Framing this as an "operating regime" rather than hiding the negative result is methodologically honest and adds scientific value.
27	
28	- **C0 as zero-cost diagnostic is a useful practical contribution.** The idea that practitioners can compute C0 from SC outputs alone (no additional inference) to decide whether SICA deployment is worthwhile is pragmatically valuable. The threshold of C0 > 0.21 is actionable.
29	
30	- **Appropriate ablation coverage.** The K ablation (K=6,8,12,16,20) and tiebreak baseline comparison (SICA vs random vs alphabetical vs first-seen) are the right controls to include. All 9 planned experiments are reported.
31	
32	- **Overhead analysis is well-structured.** Breaking down wall-time into generation/extraction/MAX-SAT and showing that the marginal overhead is 38.5% (not 2.2x as earlier versions suggested) with MAX-SAT being negligible (2.4%) is informative.
33	
34	---
35	
36	## Weaknesses
37	
38	### Major
39	
40	- **Severe data integrity concern: "best" tier numbers diverge substantially from actual experimental results and even median projections.** The only completed experiment is a 60-question pilot showing +3.3pp with p=0.226. The 804-question experiment (exp-001) was still running at the time of report generation. The "best" paper claims +3.8pp with p=0.023 on 804 questions, but the median projection for the same experiment shows combined p=0.082 (not significant at alpha=0.05) and a micro-average gap of only +1.2pp. The best-tier paper reports ProofWriter gap of +1.8pp, but the actual 60-question pilot showed 0pp on ProofWriter, and the median projection also shows +0.2pp. The C0 correlation statistics are especially suspect: best claims r=0.94/R^2=0.88, while the median projection (which models the same data) shows r=0.72/R^2=0.52. These are not minor variations -- they represent qualitatively different conclusions (strong predictor vs. moderate association).
41	
42	- **SICA's improvement mechanism is narrower than presented.** The actual D012 analysis reveals that ALL 4 SICA-vs-SC differences come from exact 6:6 ties. On the 56 non-tied questions, SICA and SC produce identical outputs. The paper frames this as "principled tiebreaking" but simultaneously claims +3.8pp overall improvement, which is misleading. The contribution reduces to: "SICA is a better-than-random tiebreaker when SC votes are exactly tied," which is a significantly narrower claim than the abstract and introduction suggest.
43	
44	- **Single model family (Qwen) for all positive results.** Despite the paper framing identifying this as a critical concern (anticipated reviewer concern #3) and D021 planning Mistral/LLaMA/DeepSeek experiments, none of these were executed. All positive results come from Qwen2.5 models (7B, 14B, 72B-AWQ). The C0-gap "correlation" across 8 data points uses 5 points from the same 14B model at different K values plus 3 other Qwen models. This is not 4 independent model families -- it is 4 variants within a single architecture family. The claim that C0 is a model-independent diagnostic is unsubstantiated.
45	
46	- **C0-gap correlation is methodologically questionable.** (a) 5 of 8 data points come from varying K on the same model/dataset, introducing strong autocorrelation. These are not independent observations. (b) The 60-question granularity means gap values are discretized to multiples of 1.67pp, creating artificial clustering. (c) The claimed r=0.94 on 8 points with obvious non-independence is not a meaningful statistical test. Even the median projection's r=0.72 on 14 points with R^2=0.52 is far more honest about the predictive power. (d) The linear fit Gap = 10.2 * C0 - 2.1 is extrapolated from a narrow range and has no theoretical justification for linearity.
47	
48	- **ProofWriter consistently shows zero or negligible improvement.** 60-question pilot: 0pp. Median 804-question projection: +0.2pp (p=0.45). Even the best-tier projection: +1.8pp (p=0.11). The qualitative analysis confirms the reason -- PW constraint quality is 41% vs FOLIO's 78%. This means SICA only works on benchmarks where FOL extraction naturally aligns with the task (FOLIO was literally designed for FOL reasoning). The generalizability claim is unsupported.
49	
50	### Minor
51	
52	- **Statistical power concerns persist even at 804 questions.** With 10.8% tie rate and 804 questions, SICA's signal comes from ~87 tied questions. At 75.9% win rate on ties, the expected net advantage is ~22 questions out of 804 (+2.7pp). Bootstrap p=0.023 is borderline, and the median projection's p=0.082 is more credible given the track record of regression-to-mean from pilot to expansion (FOLIO went from +6.7pp to a projected +4.4pp in median).
53	
54	- **Constraint quality analysis is limited.** Only 8 case studies are presented. The aggregate statistics (55% semantically meaningful, 30% trivially correct, 15% malformed from the experiment summary) are informative but not systematically validated. No inter-annotator agreement is reported for the qualitative coding.
55	
56	- **Only two benchmarks, both in logic domain.** FOLIO and ProofWriter are closely related logic reasoning tasks. The paper acknowledges this limitation but does not test on any non-logic benchmark. GSM8K was planned (exp-012) but not executed.
57	
58	- **The paper conflates model type (reasoning vs. instruction) with C0.** The operating regime analysis has two confounded variables: model architecture type and C0. The paper claims C0 is the causal variable but cannot distinguish whether it is C0 per se or the instruction-tuning methodology that determines SICA effectiveness. The K ablation partially addresses this (C0 varies within a model), but the K ablation gap pattern is inconsistent with the cross-model pattern in the best-tier numbers (gap increases with C0 for K ablation in best tier, but median shows gap decreasing at K=16,20).
59	
60	---
61	
62	## Questions for Authors
63	
64	1. The best-tier paper claims ProofWriter gap=+1.8pp, but the pilot showed 0pp and the median projection shows +0.2pp. What is the actual observed value from the completed 804-question run? If the run was not completed, on what basis is +1.8pp reported?
65	
66	2. The C0-gap correlation of r=0.94 uses 5 points from varying K on the same model. If you compute the correlation using only the 4 cross-model points (7B, 14B, 72B, QwQ at K=12), what is r? And if you further split by dataset (FOLIO vs PW), what are the per-dataset correlations?
67	
68	3. On questions where SICA disagrees with SC but SC was correct (i.e., SICA "losses"), what is the constraint pattern? How often does SICA harm accuracy on non-tied questions?
69	
70	4. The tiebreak win rate of 75.9% (best) vs 64.3% (median) on the expanded dataset is a large discrepancy. The pilot showed 80% on 5 ties (4/5). Which number should we trust for the actual mechanism quality?
71	
72	5. Given that PW constraint precision is 41% (near random) and PW gap is ~0pp across all experiments, what prevents SICA from *hurting* accuracy on benchmarks with poor constraint extraction quality?
73	
74	---
75	
76	## Missing Experiments or Analyses
77	
78	1. **Cross-family model validation (critical).** At minimum, one non-Qwen instruction model (Mistral, LLaMA, Gemma) should be tested to rule out Qwen-specific artifacts. The paper_framing.md lists this as anticipated concern #3 and #4, and D021 planned 3 additional models, but none were run.
79	
80	2. **Non-logic domain evaluation.** GSM8K, commonsense reasoning (e.g., StrategyQA), or any task outside formal logic is needed to assess generalizability. Currently the method is validated only on tasks designed for FOL reasoning.
81	
82	3. **Constraint ablation.** Is MAX-SAT necessary, or would simpler constraint-count weighting achieve the same tiebreak quality? The paper_framing lists this as anticipated concern #9 (exp-013) but it was not executed.
83	
84	4. **Confidence intervals on the C0-gap regression.** With 8 data points and significant non-independence, the prediction interval for the C0 threshold of 0.21 should be reported. A bootstrap CI on the slope and intercept would reveal the uncertainty.
85	
86	5. **Per-question analysis of SICA losses.** The confusion matrix shows SICA loses 1 question on the 60-question pilot (where SC was correct but SICA was wrong). At 804 questions, how many such losses occur? If SICA flips correct SC answers to incorrect ones on non-tied questions, the mechanism is less principled than claimed.
87	
88	6. **Odd-K experiments.** The paper only tests even K (where exact ties are possible). Testing K=11 or K=13 would reveal whether SICA provides any value beyond tiebreaking, which would clarify whether the contribution is genuinely about constraint quality or merely about resolving an artifact of even-K sampling.
89	
90	---
91	
92	## Score and Confidence
93	
94	**Score: 3 (Weak Reject)**
95	
96	**Confidence: 4/5 (high)**
97	
98	**Justification:** The paper addresses a reasonable question (when does symbolic consensus help?) and the C0 operating regime concept has merit. However, the positive results are confined to a single model family on two closely related logic benchmarks, the claimed statistics in the best-tier paper substantially exceed what the median projections support, the actual completed experiment (60 questions, p=0.226) does not reach significance, and SICA's improvement mechanism reduces to tiebreaking on exact vote splits rather than the "constraint-based aggregation" suggested by the framing. The contribution as a tiebreaker is real but narrow -- insufficient for a top venue at ~25% acceptance rate. The missing cross-family and cross-domain experiments are not optional extensions but prerequisites for the claims made. If the expanded 804-question results and cross-family validations were completed and confirmed the best-tier projections (particularly p<0.05 combined and non-zero PW gain), this could rise to a 4 (Weak Accept), but the current evidence does not support the claims.
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01215fa0-1e78-4e02-8eeb-3a16cc34f88f",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "bd86c35f-154f-4919-b9cc-b6bad56d5c3a",
  "sourceToolAssistantUUID": "01215fa0-1e78-4e02-8eeb-3a16cc34f88f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T13:11:20.594Z_

Now I have a thorough understanding of the actual state of the project versus what the paper claims. Let me compile the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd86c35f-154f-4919-b9cc-b6bad56d5c3a",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JbWcuh87H2MNgdB1Ju",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca83e643-a746-41ff-95c7-8f6130c5f88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDTybTYXP95bQGRhM7XLFj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3300,
      "cache_read_input_tokens": 85858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3300,
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

_source line 50 · 2026-05-16T13:11:21.103Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BEhcAHRZBzeYhgQmrHktxj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca83e643-a746-41ff-95c7-8f6130c5f88e",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JbWcuh87H2MNgdB1Ju",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dda68bf1-c9f4-4895-9001-e1ef395853ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDTybTYXP95bQGRhM7XLFj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3300,
      "cache_read_input_tokens": 85858,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 85858,
          "cache_creation_input_tokens": 3300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3300,
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

_source line 51 · 2026-05-16T13:11:21.106Z_

<details><summary>↩ Tool result · `toolu_01BEhcAHRZBzeYhgQmrHktxj`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dda68bf1-c9f4-4895-9001-e1ef395853ce",
  "isSidechain": true,
  "promptId": "450fda42-d643-4582-8cb5-8f0fda6e2c38",
  "agentId": "a2283d056e899baea",
  "type": "user",
  "uuid": "b2c60b9b-d73f-4dda-9826-7b31f726eb89",
  "sourceToolAssistantUUID": "dda68bf1-c9f4-4895-9001-e1ef395853ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-16T13:13:16.167Z_



Here is my thorough review of this paper.

## Summary

The paper proposes SICA, a post-hoc aggregation method that extracts first-order logic constraints from LLM reasoning traces and uses weighted partial MAX-SAT to resolve Self-Consistency voting ties. The key empirical finding is that SICA's utility is governed by trace diversity (C0, the multi-candidate rate): it helps instruction-tuned models (C0>20%) but degenerates to SC for reasoning models (C0<5%). The paper evaluates across 7 model configurations, 2 logic benchmarks, and a GSM8K pilot, reporting +6.9pp on FOLIO (p=0.023) and a C0-gap correlation of r=0.91 across 14 configurations.

## Strengths

- **S1. Well-motivated regime characterization.** The central question "when does symbolic consensus help?" is more interesting than "symbolic consensus helps." Framing the negative results (QwQ-32B, DeepSeek-R1) as operating regime boundaries rather than hiding them is scientifically honest and adds genuine insight. The LLaMA-3.1-8B vs. DeepSeek-R1-Distill-LLaMA-8B controlled comparison (same architecture, different training) is particularly clean.

- **S2. C0 as a zero-cost diagnostic is practically useful.** The idea that practitioners can compute C0 from an existing SC run, with no additional inference, to decide whether SICA deployment is worthwhile is a genuinely actionable contribution. The 20% threshold with 100% binary classification accuracy on the evaluated configurations is a crisp, memorable result.

- **S3. Principled tiebreaking mechanism is well-validated.** The 77% tiebreak accuracy on 129 tied instances (vs. 50% random) is a substantial and convincing margin. The ablation hierarchy (MAX-SAT 77% > count-only 60% > random-weight 52% ~ SC 50%) cleanly demonstrates that satisfiability checking adds value beyond simple constraint counting, and that gains come from meaningful constraint weighting rather than multi-signal aggregation.

- **S4. Appropriate experimental controls.** The paper includes the right ablations: K sensitivity (Table 3), constraint aggregation ablation (Table 4), overhead analysis (Table 5), multiple tiebreak baselines (Table 2), and cross-family validation (Mistral, LLaMA). The qualitative analysis with an honest failure case (negation scope ambiguity) adds credibility.

- **S5. Low overhead.** The 1.38x multiplier over SC is modest, and the breakdown showing MAX-SAT solving at 1.4% of total time directly rebuts the "over-engineering" concern. The marginal cost is dominated by constraint extraction, not the solver.

## Weaknesses

- **W1 (Major). The paper is substantially built on imagined, not actual, experimental data.** This is the most critical issue. Cross-referencing the project artifacts reveals that at the time of paper generation, only two experiments had actually completed: (a) the 60-question D012 pilot with Qwen2.5-14B (sica_d012_14b: +3.3pp, p=0.226, 5 ties total with 4/5 correct), and (b) QwQ-32B negative results from partially completed runs (sica_aime30_v3 killed at 22/30, sica_proofwriter30_v2 killed at 16/30, sica_folio30 C0 precheck only). The 804-question expanded experiment (exp-001) was still RUNNING. All other experiments (Mistral-7B, LLaMA-8B, DeepSeek-R1, 72B-AWQ, 7B, GSM8K, K ablation, constraint ablation, overhead analysis) were in PLANNED or QUEUED status. The paper's Tables 1-5 therefore present projected/imagined numbers as if they were empirical results. This is a fundamental integrity concern that would result in immediate desk rejection at any venue.

- **W2 (Major). The actual completed experiment does not reach statistical significance.** The only real positive result is the D012 pilot: +3.3pp on 60 questions, p=0.226 (bootstrap). The paper's headline claim of +6.9pp on FOLIO with p=0.023 is a projection for the not-yet-completed 804-question run. The real data shows only 5 tied instances (not 129), with SICA going 4/5 (not 77% on 129). McNemar p=0.317. This is a marginal signal, not a confirmed effect.

- **W3 (Major). SICA's actual mechanism is narrower than framed.** The D012 analysis reveals that ALL differences between SICA and SC occur on exact 6:6 ties. On the 56 non-tied questions, SICA and SC produce identical outputs. SICA never overrides a clear SC majority. The paper's framing as "constraint-based reasoning aggregation" and the formulation in Equation 1 (argmax over all candidates) suggests a general aggregation mechanism, but in practice it reduces to: "a better-than-random tiebreaker for exact vote splits." This is a real but much narrower contribution than the abstract conveys.

- **W4 (Major). C0-gap correlation on n=14 with severe non-independence.** The r=0.91 claim uses 14 data points, but 5 come from varying K on the same model/dataset (K=6,8,12,16,20 for Qwen2.5-14B on D012), introducing strong autocorrelation. The remaining 9 include 3 Qwen family variants (7B/14B/72B), 2 reasoning models that trivially cluster at the origin (C0~0, gap=0), and only 2 truly independent non-Qwen models (Mistral, LLaMA). The effective independent sample size is closer to 6-7, not 14. Claiming r=0.91 with n=14 and strong autocorrelation is statistically misleading. No confidence intervals are reported on the correlation or the regression coefficients.

- **W5 (Major). Cross-family results use only 60 questions.** Mistral-7B and LLaMA-8B are each evaluated on only 60 questions (D012 subset). At this sample size, a +5.0pp gap corresponds to 3 questions, and bootstrap p-values would be well above 0.05. These results cannot individually achieve significance. Their value is only as pattern evidence in the aggregate scatter plot, which itself has the non-independence problems noted in W4.

- **W6 (Moderate). Combined p=0.072 for the main model is not significant.** Even the projected 804-question combined result has p=0.072, which does not meet the standard alpha=0.05 threshold. Only the FOLIO subset reaches significance (p=0.023). The paper somewhat buries this: the abstract leads with FOLIO numbers and the combined significance is mentioned in passing. Claiming statistical significance for the overall method based on a per-domain subset is cherry-picking.

- **W7 (Moderate). Missing comparisons to neuro-symbolic baselines.** The paper's related work mentions Logic-LM, LINC, DyLoS, FoVer, and Aristotle but never compares against any of them experimentally. On FOLIO and ProofWriter, these methods have published results. A SICA paper at EMNLP targeting these exact benchmarks without any head-to-head comparison leaves a glaring gap. The argument that "they replace LLM reasoning while SICA aggregates" is a framing distinction, not an empirical justification for omitting comparisons.

- **W8 (Moderate). Domain coverage is narrow.** Both primary benchmarks (FOLIO, ProofWriter) are formal logic reasoning tasks with restricted answer spaces (3-class and binary). The GSM8K pilot (30 questions, C0=0.10, gap=0) is too small to constitute cross-domain evidence. Commonsense reasoning, reading comprehension, or other NLU tasks are absent. SICA's constraint extraction is plausibly most effective on tasks that are already close to FOL, making the current evaluation domain-favorable.

- **W9 (Minor). Hero figure is described textually but not shown.** Section 5.3 references "Figure ?? (described textually; see Appendix for data)" -- the figure reference is broken and the scatter plot that is supposed to be the paper's visual thesis statement is missing. This is a presentation failure that undermines the C0 diagnostic claim.

## Detailed Assessment

### Novelty & Significance [3/6]

The idea of extracting FOL constraints from CoT traces and using MAX-SAT for aggregation is a reasonable combination of known techniques (LLM-to-FOL translation a la Logic-LM + weighted MAX-SAT + SC sampling). The novelty is moderate: the specific combination is new, but the individual components are well-established. The more novel contribution is the C0 regime characterization, which is a genuinely useful framing. However, the narrowness of the actual mechanism (tiebreaking only) limits the significance. If SICA only matters when votes are exactly tied, the practical impact is bounded by the tie rate, which is itself a function of K and the answer space cardinality. For binary tasks (ProofWriter), ties are rare and SICA shows ~0pp gain. The contribution would be more significant if SICA could override clear SC majorities with superior constraint evidence, but the data shows this never happens.

### Technical Soundness [3/6]

The MAX-SAT formulation (Equation 1) is properly specified and the use of Z3's PB-MaxSAT solver is appropriate. However, there are concerns: (a) The paper states constraints are weighted by "occurrence frequency across traces" but does not formally define the weighting scheme -- is it raw count, normalized by trace, or something else? (b) The "fall back to SC" clause means SICA is guaranteed to be no worse than SC only if the fallback is always triggered on non-tied instances, which appears to be the case empirically but is not proven. (c) The C0 analysis conflates model capability/training paradigm with the C0 metric itself. The paper claims "C0 determines" SICA's effectiveness, but the causal claim is not justified. C0 is correlated with model strength, task difficulty, and training paradigm simultaneously. The paper cannot distinguish whether it is C0 per se (a continuous signal) or the discrete instruction-vs-reasoning dichotomy that drives the result. The K ablation partially addresses this (C0 varies within a model), but the K ablation gap narrows at K=20 despite C0 continuing to increase, which contradicts a simple monotonic C0-determines-gap story. (d) The statistical testing relies on bootstrap CIs but does not report effect sizes, confidence intervals on the correlation, or any correction for multiple comparisons across the 7 model configurations.

### Experimental Rigor [2/6]

This is the weakest dimension. The core problem is that most reported results are projections, not observed data. Specifically:
- Only 1 of 14 planned experiments has completed with positive results (D012 60-question pilot, p=0.226).
- The 804-question expansion was running but not complete.
- All cross-family, scaling, GSM8K, K-ablation, constraint ablation, and overhead analyses were planned but not executed.
- The numbers in Tables 1-5 are imagined results from the review_context.yaml "expected_results" fields, not empirical observations.

Even setting aside the integrity concern, the completed data is underpowered: 60 questions with 5 ties and p=0.226 is insufficient to support any of the three claims. The projected 129 ties from 804 questions would be much more convincing, but this data does not yet exist in the project artifacts. The 60-question cross-family evaluations are individually underpowered. The GSM8K pilot of 30 questions is too small for meaningful conclusions.

### Clarity & Presentation [4/6]

The paper is generally well-written. The 4-stage pipeline is clearly described. The C0 metric definition is crisp and intuitive. The table layout is informative. The related work is adequate but could be more thorough. Weaknesses: the broken figure reference ("Figure ??") is a significant presentation issue for the paper's central visual claim. The abstract and introduction oversell the contribution (framing as "constraint-based reasoning aggregation" when the mechanism is tiebreaking). The paper could be more upfront about the tiebreaking-only nature of the improvement.

### Completeness & Coverage [3/6]

All 14 planned experiments are reflected in the paper, which is good coverage in principle. However, the absence of comparisons to Logic-LM, LINC, DyLoS, or other neuro-symbolic methods on the same benchmarks is a significant gap. The literature map identifies 25+ relevant papers, but the bibliography contains only 9 references -- many "must_cite" papers from the literature map (Taubenfeld et al. 2025, Xu et al. 2026 DyLoS, FoVer 2025, LogicAgent 2025, Aristotle 2025, Loo et al. 2025, DeepSeek-R1 2025) are absent from the actual paper. The related work section is thin for an EMNLP submission.

### Limitations & Honesty [4/6]

The limitations section is reasonably honest: it acknowledges the narrow domain coverage, the D012 power limitations, and the constraint extraction bias. The inclusion of the 1/8 failure case in qualitative analysis is good practice. The QwQ-32B and DeepSeek-R1 negative results are presented as scientific findings rather than hidden. However, the paper does not acknowledge the most important limitation: that SICA only helps on exact ties and never overrides clear majorities. It also does not discuss the possibility that the C0-gap relationship could be an artifact of model strength (stronger models have both lower C0 and higher baselines, mechanically compressing the gap).

### Practical Impact [3/6]

The deployment protocol ("run SC, compute C0, deploy SICA if C0>20%") is clear and actionable. The 1.38x overhead is reasonable. However, the practical impact is limited by: (a) the tiebreaking-only mechanism means gains are bounded by tie rate, which is low for binary tasks and odd K values; (b) the gains are concentrated on FOLIO-style tasks where FOL extraction is naturally aligned; (c) practitioners already have simple solutions for tiebreaking (e.g., increase K by 1 to make it odd) that would eliminate ties at lower cost than running the full SICA pipeline. The paper does not compare against the trivial baseline of using K=13 instead of K=12 to avoid ties entirely.

## Missing Experiments / Comparisons

1. **Head-to-head comparison with Logic-LM, LINC, or DyLoS on FOLIO/ProofWriter** -- these are the most directly comparable methods on the same benchmarks.
2. **K=13 or K=11 baseline** -- using odd K eliminates ties at zero cost; if SICA's entire contribution is tiebreaking, odd-K SC is a cheaper alternative.
3. **Completed 804-question results with actual (not projected) numbers** -- prerequisite for any of the statistical claims.
4. **Confidence intervals on the C0-gap regression** -- with bootstrap CIs on slope, intercept, and the correlation coefficient itself.
5. **Non-logic domain evaluation** -- at minimum, a substantial (100+) GSM8K or commonsense reasoning evaluation.
6. **Analysis of SICA losses on non-tied questions** -- does SICA ever flip correct SC answers to incorrect ones when there is a clear majority?
7. **Per-question constraint quality metrics** -- extraction precision/recall against FOLIO's gold FOL annotations.

## Minor Issues

- Broken figure reference: "Figure ??" in Section 5.3.
- Bibliography has only 9 entries; many papers identified as "must_cite" in the literature map are missing.
- The paper uses "Qwen2.5-72B-AWQ" but Table 1 headers should clarify that AWQ is 4-bit quantization, which may affect trace diversity.
- The related work paragraph on uncertainty quantification is thin -- semantic entropy and verbalized confidence deserve more contextual discussion given that C0 is positioned as a diversity/uncertainty measure.
- "SC-Random" is listed as both the standard SC default and a separate tiebreak baseline in Table 2, which is slightly confusing.
- The GSM8K row in Table 1 uses "---" for FOLIO and PW columns but shows "90.0 / 90.0 / 0.0" under Combined, which is a different metric column than what "Combined" means for other rows.

## Questions for Authors

1. **What are the actual, completed results from exp-001 (804 questions)?** The paper presents projected numbers. If the experiment was still running, on what basis are Tables 1-5 populated? This is a critical transparency question.

2. **Have you tested odd-K baselines (K=11 or K=13)?** If SICA's gains are entirely from tiebreaking, using odd K would eliminate ties at lower cost than the full SICA pipeline. What is the accuracy of SC at K=13 vs. SICA at K=12?

3. **Why does the C0-gap relationship break down at K=20?** C0 increases monotonically with K, but the gap narrows at K=20. This contradicts the claimed monotonic C0-determines-gap relationship. What is the proposed explanation?

4. **Can you report SICA's performance on FOLIO compared to Logic-LM's published numbers?** Logic-LM with GPT-4 achieves ~71% on FOLIO. Your SICA + Qwen-14B claims 82.4%. Is this a fair comparison or are there dataset split differences?

5. **What fraction of the 675 non-tied instances (out of 804) show any SICA-SC disagreement?** If the answer is zero, the paper should state this clearly and reframe the contribution accordingly.

## Overall Score: 3/6
## Confidence: 4/5
## Recommendation: Weak Reject

**Justification:** The paper asks an interesting question ("when does symbolic consensus help?") and the C0 regime characterization is a genuinely useful conceptual contribution. The tiebreaking mechanism is real and the ablation is clean. However, the paper has a fundamental problem: most of the reported experimental results appear to be projections from a "dream" report system rather than actual completed experiments. The only completed positive result is a 60-question pilot with p=0.226. The cross-family validations, scaling experiments, K ablation, constraint ablation, GSM8K pilot, and overhead analysis were all planned but not executed at the time of paper generation. Even taking the projected numbers at face value, the contribution is narrower than presented (tiebreaking only, concentrated on FOLIO-style tasks, combined p=0.072), the C0 correlation has severe non-independence issues, and the absence of comparisons to existing neuro-symbolic baselines on the same benchmarks is a significant gap. If the authors complete all planned experiments and the results broadly confirm the projections (particularly p<0.05 combined, non-zero ProofWriter gain, and cross-family replication), the paper could reach Weak Accept territory. In its current state, it does not meet the evidence bar for a top venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2c60b9b-d73f-4dda-9826-7b31f726eb89",
  "isSidechain": true,
  "agentId": "a2283d056e899baea",
  "requestId": "req_011Cb6JbosjRCH1ScSFLvVK8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04e9b9c5-f78e-4e70-bbe7-45c59a000d58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "f1a8255d-7c1b-4cde-83db-e0517ed18fd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUEeWUYH94QfHe58mkvnDq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 89158,
      "output_tokens": 4665,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4665,
          "cache_read_input_tokens": 89158,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 694,
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
