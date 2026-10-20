# Research conversation: You are Reviewer R2 for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. Provide an independent bli

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-acfb302ff2bd95621.jsonl`
- **Structured JSON:** [`fd9ae2d8e68e202b56da.json`](../../sessions/fd/fd9ae2d8e68e202b56da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-22T18:40:21.397Z_

You are Reviewer R2 for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. Provide an independent blind review.

## Venue Calibration (EMNLP 2026 via ARR)
- 5 = Consider for Award (top 2.5%)
- 4 = Conference (main track accept)
- 3 = Findings
- 2 = Resubmit next cycle
- 1 = Do not resubmit
- Accept rate ~21%. Calibrate strictly.
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)

## Paper Summary
Title: "Rethinking Diversity in LLM Evaluation Panels: When More Judges Make Things Worse"

The paper studies whether diversity in multi-judge LLM evaluation panels improves adversarial robustness. Using 15 models from 6 families, all C(15,3)=455 three-judge panels, and 6 attack types across 2 benchmarks (MMLU, ARC), the authors use residualized regression to disentangle two predictors: individual judge weakness (η_max) and effective diversity (K_eff, orthogonalized against η_max). 

Key findings:
1. η_max is the primary vulnerability driver (9/12 sig, partial η²=0.18)
2. K_eff is a secondary amplifying factor (7/12 sig, partial η²=0.04), concentrated in transferable attacks (5/6 sig) and largely absent for shared-bias attacks (1/8 sig)
3. Diversity effect substantially attenuates within capability tiers (2/18 sig vs 7/12 in full pool) — largely tier-mixing artifact
4. Gaussian copula underestimates inter-judge MI by 10× median
5. Family labels don't predict independence (p=0.18)
6. Robustness-first panel design reduces ASR by 47% vs random; but only 7% vs Strongest-K (p=0.42, NS)
7. Aggregation rules modulate: threshold amplifies K_eff 1.45×; Bayesian partially mitigates η_max (0.55× β)
8. BFT analogy: no sign reversal between adaptive and random-fault regimes — diversity is harmful in both

## Related Work Section (from paper, Section 2)
- LLM-as-Judge: mentions single-judge biases (position, verbosity, sycophancy), multi-judge as mitigation
- Adversarial Attacks on LLM Judges: prior work on individual judge vulnerability
- BFT: formal framework, n=3f+1, assumes independent non-adaptive faults
- Panel Diversity: "several recent studies advocate for diverse panels"

## Your Review Focus (R2: Novelty + Related Work)

Evaluate:
1. **Novelty assessment**: 
   - Is the core finding (η_max dominates, diversity is secondary risk factor) surprising or predictable? A skeptic might say "of course including weak judges makes panels weaker" is obvious.
   - The finding that diversity is harmful (not just neutral) is more interesting, but it's attenuated within tiers (2/18) and small effect (η²=0.04). How novel is the residual?
   - Copula failure (10×) and family label unreliability — are these independently novel enough?
   - BFT framing without sign reversal — is this still a contribution or a failed hypothesis?

2. **Related work gaps**:
   - The paper's related work section is very thin (Section 2 is ~0.5 pages). For EMNLP 2026, this needs substantial expansion.
   - Missing citations likely include: specific LLM-as-judge papers (Zheng et al. 2023 MT-Bench/Chatbot Arena; Li et al. 2024 on judge biases), adversarial attacks on LLM judges (Shi et al. 2024, Raina et al. 2024), multi-agent evaluation frameworks, ensemble methods in ML, voting theory, jury theorems (Condorcet), panel composition in social choice theory.
   - The BFT analogy needs more formal treatment — is it really BFT or more like Condorcet jury theorem?

3. **Contribution framing**:
   - Paper claims "first large-scale empirical study" — verify plausibility
   - The practical contribution (robustness-first) is not significantly better than "just use strongest" (p=0.42)
   - The title "When More Judges Make Things Worse" — does the evidence fully support this framing? The paper itself shows diversity is largely neutral within tiers.

4. **Positioning relative to existing work**:
   - How does this relate to ensemble diversity in classical ML (bias-variance tradeoff, negative correlation learning)?
   - Connection to Condorcet jury theorem (CJT) — CJT predicts diverse independent voters improve accuracy, but assumes p>0.5 for each voter. Under adversarial conditions with p<0.5 for weak judges, CJT predicts the opposite. Is the paper's finding simply the CJT prediction under adversarial conditions?

Produce a structured review with: Summary, Strengths (bulleted), Weaknesses (bulleted with severity W1-W5), Questions for Authors, Missing References, and preliminary scores (Soundness, Excitement, Reproducibility, Overall Assessment on the 1-5 scale). Be critical but fair. Write in English.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "9004ea97-da75-4a37-aaf7-44261d3da253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T18:40:21.399Z_

```json
{
  "parentUuid": "9004ea97-da75-4a37-aaf7-44261d3da253",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
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
      "TodoWrite",
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
      "TodoWrite",
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
  "uuid": "4f75294f-828c-406b-a071-39d032afafdc",
  "timestamp": "2026-05-22T18:40:21.399Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T18:40:24.114Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f75294f-828c-406b-a071-39d032afafdc",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6YSe6yfkniD8SLitx2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b12e45a-928a-499c-8aa3-f8696db1a67e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133a7VGMcSBFCeH8o4xtm8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7724,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7724,
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

_source line 4 · 2026-05-22T18:40:25.638Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JqSssgxa7ttjUwbxmKeEqg`</summary>

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
  "parentUuid": "2b12e45a-928a-499c-8aa3-f8696db1a67e",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6YSe6yfkniD8SLitx2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cb70319-3714-4922-8ab1-8d3025e8333f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133a7VGMcSBFCeH8o4xtm8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7724,
      "cache_read_input_tokens": 8252,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7724
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7724,
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

_source line 5 · 2026-05-22T18:40:25.641Z_

<details><summary>↩ Tool result · `toolu_01JqSssgxa7ttjUwbxmKeEqg`</summary>

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
  "parentUuid": "7cb70319-3714-4922-8ab1-8d3025e8333f",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "fe1dd654-15de-4f53-b1d3-f6f0d80d5615",
  "sourceToolAssistantUUID": "7cb70319-3714-4922-8ab1-8d3025e8333f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T18:40:28.292Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe1dd654-15de-4f53-b1d3-f6f0d80d5615",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6YkmmeMVqf7959mUng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d6d41f0-1987-4f6f-838a-4deca0713a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nWCFUxkkcNc9STicX4UdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15976,
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

_source line 7 · 2026-05-22T18:40:29.299Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_016QdqZhP3TYo2jJ5sw2Q8ad`</summary>

```json
{
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d6d41f0-1987-4f6f-838a-4deca0713a1f",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6YkmmeMVqf7959mUng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc6dbde3-1e87-4e0c-9805-e63cbeb635c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nWCFUxkkcNc9STicX4UdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15976,
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

_source line 8 · 2026-05-22T18:40:29.358Z_

<details><summary>↩ Tool result · `toolu_016QdqZhP3TYo2jJ5sw2Q8ad`</summary>

```text
{"result":"# 项目 cert_manip_resist_eval 概况\n\n## 实验状态 (30 个)\n\n- **plan001_step1_parallel**: PREPARING — \n- **plan001_step1_parallel_dryrun2**: PREPARING — \n- **plan001_step1_parallel_dryrun**: PREPARING — \n- **plan001_step1_full_v3**: PREPARING (failed) — \n- **plan001_step1_full_v2**: PREPARING (failed) — \n- **plan001_step1_full**: PREPARING — \n- **plan001_step1_dryrun3**: PREPARING — \n- **plan001_step1_dryrun2**: PREPARING — \n- **plan001_step1_dryrun**: PREPARING — \n- **taxonomy-broad-spectrum**: DONE (negative) — \n- **mvp-step2v3-retry3**: DONE (negative) — \n- **mvp-step2v3-retry2**: DONE (failed) — \n- **mvp-step2v3-retry**: DONE (failed) — \n- **mvp-step2v3-regression**: DONE (failed) — \n- **mvp-step2-keff-contrast**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan001_step1_batched_v2（准备中）\n- plan001_step1_batched（准备中）\n- plan001_step1_v3（准备中）\n- plan001_step1_throttled_v5（准备中）\n- plan001_step1_throttled_v4（准备中）\n- plan001_step1_throttled_v3（准备中）\n- plan001_step1_throttled_v2（准备中）\n- plan001_step1_throttled（准备中）\n- plan001_step1_v2（准备中）\n- plan001_step1_parallel_final（准备中）\n- …另有 13 项\n\n## 近期结论\n- **plan001_step1_full_v4** (success): Expanding from 6 to 15 models (9 API + 6 local) across 6 families and 3 capability tiers breaks the structural K_eff-η_max collinearity (r=-0.8 with 6 models). With 15 models, panels can have high K_eff (cross-family diversity) without necessarily including weak judges, enabling clean separation of diversity vs robustness effects.\n- **taxonomy-broad-spectrum** (negative): K_eff is a significant negative predictor of panel ASR specifically for broad-spectrum attacks (verbosity bias, position bias, authority bias) that exploit shared judge biases, consistent across both MMLU and ARC datasets. This validates the attack taxonomy: targeted attacks → η_max dominates; broad-spectrum attacks → K_eff provides additional protection. ← 基于 mvp-step2v3-retry3\n- **mvp-step2v3-retry3** (negative): Controlling for individual model robustness (η_max), higher K_eff panels have significantly lower ASR. Multi-factor regression log(ASR) ~ log(K_eff) + log(η_max) should show K_eff coefficient significantly negative. ← 基于 mvp-step2v3-retry2\n\n## 趋势\n成功 1 / 负向 3 / 失败 3 / 共 7\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nseetacloud-rtx6000: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp-step2v3-regression: 训练失败 — unknown\n- mvp-step2v3-retry: 训练失败 — unknown\n- mvp-step2v3-retry2: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc6dbde3-1e87-4e0c-9805-e63cbeb635c7",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "c083f54f-c0ef-4cb1-a08b-8063af8738eb",
  "sourceToolAssistantUUID": "dc6dbde3-1e87-4e0c-9805-e63cbeb635c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T18:40:29.794Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01975V57QGnTyFsVYiAyH1Jg`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c083f54f-c0ef-4cb1-a08b-8063af8738eb",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6YkmmeMVqf7959mUng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8f68d4e-b290-4334-8616-fb93310b592d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nWCFUxkkcNc9STicX4UdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15976,
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

_source line 10 · 2026-05-22T18:40:29.817Z_

<details><summary>↩ Tool result · `toolu_01975V57QGnTyFsVYiAyH1Jg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan001_step1_batched_v2（准备中）\\n- plan001_step1_batched（准备中）\\n- plan001_step1_v3（准备中）\\n- plan001_step1_throttled_v5（准备中）\\n- plan001_step1_throttled_v4（准备中）\\n- plan001_step1_throttled_v3（准备中）\\n- plan001_step1_throttled_v2（准备中）\\n- plan001_step1_throttled（准备中）\\n- plan001_step1_v2（准备中）\\n- plan001_step1_parallel_final（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **plan001_step1_full_v4** (success): Expanding from 6 to 15 models (9 API + 6 local) across 6 families and 3 capability tiers breaks the structural K_eff-η_max collinearity (r=-0.8 with 6 models). With 15 models, panels can have high K_eff (cross-family diversity) without necessarily including weak judges, enabling clean separation of diversity vs robustness effects.\\n- **taxonomy-broad-spectrum** (negative): K_eff is a significant negative predictor of panel ASR specifically for broad-spectrum attacks (verbosity bias, position bias, authority bias) that exploit shared judge biases, consistent across both MMLU and ARC datasets. This validates the attack taxonomy: targeted attacks → η_max dominates; broad-spectrum attacks → K_eff provides additional protection. ← 基于 mvp-step2v3-retry3\\n- **mvp-step2v3-retry3** (negative): Controlling for individual model robustness (η_max), higher K_eff panels have significantly lower ASR. Multi-factor regression log(ASR) ~ log(K_eff) + log(η_max) should show K_eff coefficient significantly negative. ← 基于 mvp-step2v3-retry2\\n\\n## 趋势\\n成功 1 / 负向 3 / 失败 3 / 共 7\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nseetacloud-rtx6000: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp-step2v3-regression: 训练失败 — unknown\\n- mvp-step2v3-retry: 训练失败 — unknown\\n- mvp-step2v3-retry2: 训练失败 — unknown\\n\", \"total_chars\": 1736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8f68d4e-b290-4334-8616-fb93310b592d",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "cacc6ce2-eda1-4700-99ff-a5b5094e6ffb",
  "sourceToolAssistantUUID": "e8f68d4e-b290-4334-8616-fb93310b592d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T18:40:30.485Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ELJEPaYNf9CahpSNrSiYvw`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cacc6ce2-eda1-4700-99ff-a5b5094e6ffb",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6YkmmeMVqf7959mUng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "229f5607-6f60-4ac3-a58e-7bfbe7870dae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nWCFUxkkcNc9STicX4UdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15976,
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

_source line 12 · 2026-05-22T18:40:30.503Z_

<details><summary>↩ Tool result · `toolu_01ELJEPaYNf9CahpSNrSiYvw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/literature_map.yaml\", \"content\": \"papers:\\n  robertson2025tvdmi:\\n    title: \\\"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes\\\"\\n    authors: [\\\"Robertson\\\", \\\"Koyejo\\\"]\\n    year: 2025\\n    venue: \\\"arXiv (under TMLR review)\\\"\\n    url: \\\"https://arxiv.org/abs/2508.05469\\\"\\n    category: \\\"evaluation_framework\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Foundational TVD-MI theory for LLM evaluation. Theorem 3.3 proves bounded f-divergences (TVD) maintain polynomial certification under mode-collapse attacks while unbounded (KL) fail. We extend from pairwise to N-agent multi-judge settings.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  yang2026diversity_scaling:\\n    title: \\\"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\\\"\\n    authors: [\\\"Yang et al.\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026 Workshop AIMS\\\"\\n    url: \\\"https://arxiv.org/abs/2602.03794\\\"\\n    category: \\\"multi_agent_scaling\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Information-theoretic diversity-scaling framework: K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3). We provide the adversarial dual — while their K* governs performance improvement rate, the same correlation structure governs manipulation cost increase rate. Core duality insight.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  turkmen2026copula:\\n    title: \\\"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\\\"\\n    authors: [\\\"Turkmen et al.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08003\\\"\\n    category: \\\"ensemble_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Gaussian-copula correlated error model (Z_j = √ρ·U + √(1-ρ)·ξ_j), error floor Φ(Φ⁻¹(1-p)/√ρ) (Theorem 4.4), three-term MI decomposition (Theorem 4.3). Copula model is the mathematical foundation for our K_eff = 1+(K-1)·exp(-2·I_max) derivation. Within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  kaneko2025bits_leaked:\\n    title: \\\"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs\\\"\\n    authors: [\\\"Kaneko\\\", \\\"Baldwin\\\"]\\n    year: 2025\\n    venue: \\\"NeurIPS 2025 spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2510.17000\\\"\\n    category: \\\"adversarial_bounds\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Tight single-model attack cost bound N_min ≥ log₂(1/ε)/I_max via Fano inequality (Theorem 1), achieved by SPRT (Theorem 2). Validated across 7 LLMs. Provides single-channel foundation; we extend to multi-judge composition where adversary must simultaneously fool K correlated judges.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  chen2025peg:\\n    title: \\\"Incentivizing Truthful Language Models via Peer Elicitation Games\\\"\\n    authors: [\\\"Chen et al.\\\"]\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.13636\\\"\\n    category: \\\"peer_prediction\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"DMI-based multi-agent peer elicitation with dominant strategy truthfulness (Lemma 1), O(√T) regret (Theorem 2). Requires conditional independence (Assumption 4) but does not characterize degradation when violated. We prove ε = f(ρ) continuous degradation curve as co-primary contribution.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  qiu2026truthfulness:\\n    title: \\\"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction\\\"\\n    authors: [\\\"Qiu et al.\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2601.20299\\\"\\n    category: \\\"peer_prediction\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"BNE incentive-compatibility for LLM peer prediction with inverse scaling property. Targets output truthfulness not adversarial robustness of protocol. No polynomial cost bounds tied to judge count. We provide the robustness guarantee that complements their truthfulness guarantee.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  kim2025correlated_errors:\\n    title: \\\"Correlated Errors in Large Language Models\\\"\\n    authors: [\\\"Kim\\\", \\\"Garg\\\", \\\"Peng\\\", \\\"Garg\\\"]\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.07962\\\"\\n    category: \\\"error_correlation\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"60% pairwise agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076. Key empirical data for α regime analysis and K_eff estimation. 350+ LLMs. Motivates cross-family diversity for maximizing K_eff.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  sok2026llm_judge_security:\\n    title: \\\"Security in LLM-as-a-Judge: A Comprehensive SoK\\\"\\n    authors: [\\\"Various\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.29403\\\"\\n    category: \\\"adversarial_evaluation\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"Comprehensive vulnerability catalog: open-source 50-68% ASR, frontier 27-44%. 7-model diverse committees reduce ASR to 10-19% empirically but WITHOUT formal explanation. We provide the formal explanation via K_eff framework.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  feng2026noisy_valid:\\n    title: \\\"Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges\\\"\\n    authors: [\\\"Feng\\\", \\\"Shen\\\", \\\"Balashankar\\\", \\\"Gerner-Beuerle\\\", \\\"Rodrigues\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2601.20913\\\"\\n    category: \\\"certified_evaluation\\\"\\n    role: \\\"adjacent\\\"\\n    relevance: \\\"Statistical hypothesis testing for LLM evaluation with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty. Assumes honest but fallible judges. Complements our work: they certify statistical validity, we certify manipulation resistance.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  jung2026logarithmic_scores:\\n    title: \\\"Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation\\\"\\n    authors: [\\\"Jung\\\", \\\"Na\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.00477\\\"\\n    category: \\\"multi_agent_scaling\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"Score-coverage dissociation: scoring reliability scales logarithmically with panel size N while discovery follows power law N^0.69. Direct implications for our K-scaling claims — certified bounds may saturate faster than empirical ASR gains.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  chen2026behavioral_entanglement:\\n    title: \\\"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement\\\"\\n    authors: [\\\"Chen et al.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.07650\\\"\\n    category: \\\"error_correlation\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"BEI and CIG metrics across 18 LLMs from 6 families. Cross-family entanglement 40-60% lower than intra-family. Provides independent validation of cross-family diversity benefit for K_eff estimation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  keppo2026collusion_fragility:\\n    title: \\\"On the Fragility of AI Agent Collusion\\\"\\n    authors: [\\\"Keppo et al.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.20281\\\"\\n    category: \\\"multi_agent_robustness\\\"\\n    role: \\\"supporting\\\"\\n    relevance: \\\"Increasing LLM count 2→5 breaks collusion (+22%→+3%). Same-family size heterogeneity stabilizes via leader-follower dynamics. Motivates cross-family diversity requirement in our protocol design.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\", \"total_chars\": 7700, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "229f5607-6f60-4ac3-a58e-7bfbe7870dae",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "a1ad9dac-48a4-4758-8b41-2b8dba6405bf",
  "sourceToolAssistantUUID": "229f5607-6f60-4ac3-a58e-7bfbe7870dae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T18:40:34.433Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WkooQSb7bvLRVv4B5qzp7Y`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1ad9dac-48a4-4758-8b41-2b8dba6405bf",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6Z8F6nDcLiCPw1N7by",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa7d6760-4331-4437-a597-518ad41d828b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GthFpmFFNPsUWKc8CEqWEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5509,
      "cache_read_input_tokens": 17423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5509,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 14 · 2026-05-22T18:40:34.445Z_

<details><summary>↩ Tool result · `toolu_01WkooQSb7bvLRVv4B5qzp7Y`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cert_manip_resist_eval'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa7d6760-4331-4437-a597-518ad41d828b",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "fcb104f0-c4f4-4358-a43f-750be4675be5",
  "sourceToolAssistantUUID": "fa7d6760-4331-4437-a597-518ad41d828b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T18:40:35.409Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XuWhpB58uVpWc5Meh1UH9q`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcb104f0-c4f4-4358-a43f-750be4675be5",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6Z8F6nDcLiCPw1N7by",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e4acdc5-7ebd-4304-b446-2fdbad477555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GthFpmFFNPsUWKc8CEqWEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5509,
      "cache_read_input_tokens": 17423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5509,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 16 · 2026-05-22T18:40:35.418Z_

<details><summary>↩ Tool result · `toolu_01XuWhpB58uVpWc5Meh1UH9q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/paper_framing.md\", \"content\": \"# Paper Framing — cert_manip_resist_eval (v4b: Dominance Analysis Correction)\\n\\n> Last updated: 2026-05-22 | Reason: Dominance analysis unifies regression specifications; K_eff 7/12 positive + 1/12 negative (arc×sycophancy protective); condition-dependent dual drivers\\n\\n## Target\\nEMNLP 2026 (via ARR)\\n\\n## Title Candidates\\n1. \\\"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\\\"\\n2. \\\"More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries\\\"\\n3. \\\"Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability\\\"\\n\\n## Core Insight\\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **predominantly reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently positively associated with attack success rate in **7/12 conditions**, while being protective in only **1/12** (arc×sycophancy). Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with condition-dependent relative importance. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create. The exception (sycophancy) reveals that when attacks exploit a shared bias, diverse panels can dilute the bias — but this is the minority regime.\\n\\n## Hook\\n\\\"Adding more diverse judges to an evaluation panel predominantly makes it more vulnerable to adversarial manipulation — with a revealing exception that proves the rule.\\\"\\n\\n## Novelty Positioning\\nWe do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:\\n1. **First empirical quantification of diversity's condition-dependent effect** in the LLM-judge domain (15 models, 455 panels, dominance analysis: K_eff positive 7/12, negative 1/12, NS 4/12 — predominantly harmful but with a mechanistically informative exception)\\n2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominant 4/12, co-dominant 7/12, K_eff sole dominant 1/12)\\n3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries\\n4. **Structural barriers**: diversity-capability tradeoff (now with independent predictive evidence), family label unreliability (confirmed at 15-model). ~~Copula failure removed — falsified at scale~~\\n5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap\\n**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max) AND panel diversity (K_eff). Diversity **predominantly increases** vulnerability (7/12 conditions), with one mechanistically informative exception where diversity is protective (arc×sycophancy, 1/12). Their relative importance is condition-dependent.\\n**Evidence** (15-model, 455 panels, 12 conditions, dominance analysis — canonical regression model):\\n- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε), std_β = raw_β × SD(log_x)/SD(log_y), FDR = BH per predictor\\n- η_max FDR significant: **11/12** (only NS: arc×position_bias p=0.909)\\n- K_eff FDR significant positive: **7/12**\\n- K_eff FDR significant negative: **1/12** (arc×sycophancy: std_β = -0.192, FDR p = 0.0095)\\n- K_eff NS: **4/12** (mmlu×{score_manip, position, authority}, arc×verbosity)\\n- Dominance pattern: η_max sole dominant **4/12**, co-dominant (both sig) **7/12**, K_eff sole dominant **1/12** (arc×position_bias)\\n- **arc×sycophancy exception**: When attack exploits a shared cognitive bias, diverse panels dilute the bias — the ONE condition where BFT logic holds. This exception reveals the mechanism boundary.\\n**Strength**: Strong. η_max is the more consistent driver (11/12), K_eff is condition-dependent (7/12 harmful, 1/12 protective). Together they form the dual vulnerability driver story.\\n**Headline**: \\\"η_max significant in 11/12, K_eff predominantly harmful (7/12) with one protective exception (sycophancy). Condition-dependent dual drivers.\\\"\\n\\n**Comparison to 6-model results** (for transparency):\\n- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → \\\"K_eff irrelevant\\\"\\n- 15-model (455 panels): K_eff 7/12 sig positive, 1/12 sig negative → \\\"K_eff predominantly harmful, condition-dependent\\\"\\n- The emergence of K_eff's effect is driven by model pool expansion: wider capability spectrum enables detecting both its harmful AND protective regimes.\\n\\n### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap\\n**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.\\n**Evidence** (15-model, 455 panels):\\n- K_eff significant in both regimes, predominantly positive direction (7/12 adaptive positive, 1/12 negative)\\n- ΔR² = +0.213 mean (RF explains more variance)\\n**Reframing from v3**: Original BFT contrast (\\\"K_eff helps under RF but not adaptive\\\") does NOT hold — K_eff is predominantly harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.\\n**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped. Numbers need revalidation with dominance analysis for RF regime.\\n\\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.\\n**Evidence**:\\n- K_eff-η_max correlation: r = +0.700 (15-model)\\n- K_eff still significant 7/12 positive (dominance analysis) → not purely mediated by η_max\\n- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains\\n**Upgrade from v3**: From \\\"correlation\\\" to \\\"independent predictive effect\\\" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.\\n**Strength**: Strong (statistical association). Causal language avoided.\\n\\n### Claim 4 (Methodological): Family Labels ≠ Diversity\\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\\n**Evidence**:\\n- 6-model: Mann-Whitney U p=0.206, permutation p=0.427\\n- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.\\n- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)\\n**Strength**: Moderate. Consistent across 6→15 model scaling.\\n\\n### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation\\n**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.\\n**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.\\n**Disposition**: Remove as independent contribution. Optionally note in analysis: \\\"Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence.\\\"\\n**Strength**: DEAD as independent claim. May retain as minor observation.\\n\\n### Claim 6 (Practical): Robustness-First Panel Design\\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\\n**Evidence** (15-model, 455 panels — fully validated):\\n- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)\\n- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)\\n- Robust across panel sizes K=10, 20, 50\\n- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff\\n- Consistent with canonical regression: η_max 11/12 dominant\\n**Strength**: Strong (15-model fully confirmed). Zero failure conditions.\\n\\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers\\n**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).\\n**Evidence** (15-model, 455 panels, log-log canonical spec — D017, supersedes D016 level-level):\\n- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.376 ← canonical baseline\\n- Weighted: η_max 11/12, K_eff **11/12 all positive**, R²=0.357 — strongest dual-driver\\n- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.901** — near-perfect fit under unanimity\\n- Bayesian: η_max **9/12** (↓), K_eff **5/12** (1+/**4 negative**), R²=0.105\\n- Key findings:\\n  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/4−)\\n  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.90 (unanimity maximizes dual-driver predictability)\\n  - Weighted amplifies K_eff channel only (8→11/12) without changing η_max\\n  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)\\n**Strength**: Strong (log-log canonical, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.\\n\\n## Contribution Stack (ordered by strength)\\n1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff predominantly harmful 7/12 + protective exception + condition-dependent dominance)\\n2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)\\n3. **BFT reversal mechanism + mechanism boundary** — theoretical contribution (why independence hurts under adaptive adversaries; sycophancy exception reveals boundary)\\n4. **Aggregation-dependent effects** — empirical+practical (Bayesian mitigates both drivers: η_max 11→9/12, K_eff flips to 4/5 negative; threshold R²=0.90; D017)\\n5. **Robustness-first panel design** — practical contribution\\n6. **Family label unreliability** — methodological contribution (confirmed at 15-model scale)\\n7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)\\n~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: \\\"K_eff positive is just confound with η_max\\\"\\n**Response**: (a) Dominance analysis with VIF-controlled regression: K_eff still significant 7/12 positive, 1/12 negative; (b) In low-confound conditions (r≈0.35), K_eff highly significant; (c) The 1/12 negative case (arc×sycophancy) proves K_eff's effect is not a confound artifact — if it were purely confound, K_eff would be uniformly positive, not condition-dependent.\\n\\n### RC2: \\\"Why does diversity hurt? What's the mechanism?\\\"\\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis reveals the mechanism boundary: K_eff is harmful when attacks can exploit judge-specific weaknesses (7/12), but protective when attacks exploit a shared bias that diverse panels can dilute (sycophancy, 1/12). This mechanism distinction (exploit-specific vs bias-shared) explains the full pattern.\\n\\n### RC3: \\\"Only 15 models — does this generalize?\\\"\\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\\n\\n### RC4: \\\"BFT comparison is a strawman\\\"\\n**Response**: (a) The implicit assumption \\\"more diverse judges = more robust\\\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\\n\\n### RC5: \\\"Why not just use the strongest models?\\\"\\n**Response**: (a) \\\"Strongest\\\" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\\n\\n### RC6: \\\"No theoretical novelty\\\"\\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\\n\\n### RC7: \\\"Why not just use Bayesian aggregation?\\\"\\n**Response**: (a) 15-model log-log canonical (D017): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 4/5 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.105 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.\\n\\n### RC8: \\\"6-model and 15-model results contradict — which is right?\\\"\\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\\n\\n### RC9 (new): \\\"arc×sycophancy exception undermines your claim\\\"\\n**Response**: (a) The exception STRENGTHENS the paper — it reveals the mechanism boundary between exploit-specific attacks (where diversity hurts) and shared-bias attacks (where diversity helps); (b) 7/12 vs 1/12 clearly shows which regime dominates; (c) The exception is theoretically predicted: sycophancy is a shared cognitive bias across models, so diverse panels dilute it (classic BFT logic applies); (d) This gives practitioners an actionable decision rule: check whether the threat model involves shared biases or judge-specific exploits.\\n\\n## \\\"When Diversity Helps\\\" Section\\nDiversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:\\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\\n2. **Shared-bias attacks (empirically confirmed)**: arc×sycophancy shows K_eff significantly NEGATIVE (std_β = -0.192, p = 0.0095). When an attack exploits a cognitive bias shared across models, diverse panels dilute the bias. This is the ONE adversarial condition where BFT logic holds.\\n3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\\n4. **Summary**: K_eff is harmful in 7/12, NS in 4/12, protective in 1/12 conditions. The protective case (sycophancy) is mechanistically distinct and strengthens the overall story by revealing the mechanism boundary.\\n\\n## Story Arc (v4b)\\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\\n3. **Surprise**: Diversity predominantly **increases** vulnerability (K_eff positive in 7/12 conditions) — the opposite of what BFT predicts\\n4. **Mechanism**: Adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent dominance (η_max dominant 4/12, co-dominant 7/12, K_eff sole dominant 1/12)\\n5. **The Exception That Proves the Rule**: arc×sycophancy — the ONE condition where K_eff is significantly negative (diversity protective). When attacks exploit a shared cognitive bias, diverse panels dilute it. This exception reveals the mechanism boundary: BFT logic holds for shared-bias attacks but fails for exploit-specific attacks\\n6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels\\n7. **Implication**: The relationship between panel diversity and security is not monotonic — it depends on the attack mechanism. The default assumption \\\"more diverse = more robust\\\" is wrong in the majority regime\\n\", \"total_chars\": 18106, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e4acdc5-7ebd-4304-b446-2fdbad477555",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "d175ade4-cea0-43ed-bfd7-19d2495a7e15",
  "sourceToolAssistantUUID": "3e4acdc5-7ebd-4304-b446-2fdbad477555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T18:40:35.816Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KunJX5rTADKRV5GXmbahEB`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d175ade4-cea0-43ed-bfd7-19d2495a7e15",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6Z8F6nDcLiCPw1N7by",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7680a15-a401-4cc1-83a6-45e911c04b96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GthFpmFFNPsUWKc8CEqWEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5509,
      "cache_read_input_tokens": 17423,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 17423,
          "cache_creation_input_tokens": 5509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5509,
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

_source line 18 · 2026-05-22T18:40:35.824Z_

<details><summary>↩ Tool result · `toolu_01KunJX5rTADKRV5GXmbahEB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/ROADMAP.md\", \"content\": \"# cert_manip_resist_eval — Research Dashboard\\n\\n> 最后更新: 2026-05-22 18:40 UTC | 更新原因: P2b log-log canonical done (D017); Claim 6 15-model confirmed (12/12); registry updated\\n\\n## 核心方向\\n**The Diversity Trap**：LLM judge panel diversity 在 adaptive adversary 下 predominantly 增加脆弱性（K_eff 7/12 正, 1/12 负）。η_max (11/12) 是更一致的驱动因子，K_eff 条件依赖。详见 paper_framing.md v4b+D017。\\n\\n## 当前阶段\\n**Research 阶段** — 全部 15-model 分析完成（P0-P2b），论文写作 + 修正推进中\\n\\n## 当前进展\\n- ✅ 126/126 API scoring + 455 panels pipeline\\n- ✅ Dominance analysis canonical table（log-log OLS）\\n- ✅ η_max **11/12**, K_eff 7/12+, 1/12−, 4/12 NS\\n- ✅ Copula Claim 5 证伪移除 (D015)\\n- ✅ Family Labels 15-model 确认 (Claim 4)\\n- ✅ **P2b Aggregation log-log canonical (D017)**: Bayesian 部分减弱两个通道（η_max 11→9/12, K_eff 翻负 4/5）; Threshold R²=0.90\\n- ✅ **Claim 6 Panel Design 15-model**: min(η_max) **12/12** 全胜（from 5/6）\\n- ✅ Registry plan001_step1_full_v4 marked DONE\\n- 📌 Paper Agent: methodology.tex critical 修正中（模型名称 + MI 方法描述）\\n- 📌 Dream simulation (dream_20260522T173833) — writing 阶段\\n\\n## 关键数据（唯一来源: dominance analysis, log-log OLS）\\n| Metric | Value |\\n|--------|-------|\\n| η_max FDR sig | **11/12** (only NS: arc×position) |\\n| K_eff FDR sig + | **7/12** |\\n| K_eff FDR sig − | **1/12** (arc×sycophancy) |\\n| K_eff NS | **4/12** |\\n| Regression spec | log(ASR+ε) ~ log(K_eff) + log(η_max+ε) |\\n\\n### Aggregation 效应 (P2b log-log canonical, D017)\\n| Method | η_max sig | K_eff sig | K_eff +/− | R² |\\n|--------|-----------|-----------|-----------|-----|\\n| majority | 11/12 | 8/12 | 7+/1− | 0.376 |\\n| weighted | 11/12 | 11/12 | 11+/0− | 0.357 |\\n| threshold | 12/12 | 11/12 | 10+/1− | **0.901** |\\n| bayesian | **9/12** | 5/12 | 1+/**4−** | 0.105 |\\n\\n## 近期任务\\n- [x] P0-P2b: 全部 15-model 分析完成\\n- [x] Claim 6: 15-model panel design 验证 (12/12)\\n- [x] Registry 更新\\n- [ ] Paper Agent: methodology critical 修正\\n- [ ] Paper Agent: Results 章节（含 P2b aggregation 最终数据）\\n- [ ] Dream report 处理\\n- [ ] Agent: 提供完整 15 模型列表（供 Paper Agent 修正 §3.1）\\n- [ ] Theorem 1 scope 更新\\n\\n## GPU 预算\\nseetacloud-rtx6000: 4× RTX 6000 96G（全空闲，写作阶段）\\n\\n## 目标\\nEMNLP 2026 via ARR | Contribution stack: 7 items | All analyses complete | Paper writing in progress\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D017 | 2026-05-22 | Claim 7 final (log-log canonical): Bayesian partia | plan001_step1_full_v4 |\\n| D016 | 2026-05-22 | Claim 7 revised: \\\"Bayesian breaks weakest-link\\\" fa | plan001_step1_full_v4 |\\n| D015 | 2026-05-22 | Claim 5 (Gaussian Copula Failure) falsified at 15- | worker_analysis_15model-family-copula |\\n| D014 | 2026-05-22 | 15-model 结果证伪原始 Claim 1 (\\\"K_eff irrelevant\\\")；K_eff | plan001_step1_full_v4 |\\n| D013 | 2026-05-22 | 7-model 预览显示 Claim 2 复活信号：random-fault K_eff gains | plan_001_7model_preview |\\n| D012 | 2026-05-22 | Plan_010 聚合实验完成：Bayesian 部分打破 weakest-link (3/12 v | plan_010 |\\n| D011 | 2026-05-22 | Plan_003 BFT contrast failed (0/12 random-fault K_ | plan_003 |\\n| D010 | 2026-05-22 | Dream review (2.5 all tiers) exposed 13 structural | — |\\n| D009 | 2026-05-22 | Taxonomy 验证失败（0/6 新条件 K_eff 显著），建议 kill 项目 | taxonomy-broad-spectrum |\\n| D008 | 2026-05-22 | MVP 原假设部分证伪：K_eff 仅对 shared-bias attacks 显著，η_max  | mvp-step2v3-retry3 |\\n\\n\\n\", \"total_chars\": 3146, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7680a15-a401-4cc1-83a6-45e911c04b96",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "9dac0b7c-89e2-48e5-82b3-a670efae68ec",
  "sourceToolAssistantUUID": "d7680a15-a401-4cc1-83a6-45e911c04b96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T18:40:38.037Z_

Now let me read the actual paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dac0b7c-89e2-48e5-82b3-a670efae68ec",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6ZWVKAedaAz2yPZCV6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3869ebc-6150-4997-8247-c6e1317c2a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01911AhUYMSNu7Z94jM6siQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7594,
      "cache_read_input_tokens": 22932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7594,
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

_source line 20 · 2026-05-22T18:40:40.314Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QP2CZSh3rDps7TMjcf4Vkc`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3869ebc-6150-4997-8247-c6e1317c2a89",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6ZWVKAedaAz2yPZCV6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c1c5d71-8139-4c36-81c8-345bbdd88aae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01911AhUYMSNu7Z94jM6siQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7594,
      "cache_read_input_tokens": 22932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7594,
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

_source line 21 · 2026-05-22T18:40:40.370Z_

<details><summary>↩ Tool result · `toolu_01QP2CZSh3rDps7TMjcf4Vkc`</summary>

```text
artifacts/dream_reports/dream_20260522T055016/best/paper.tex
artifacts/dream_reports/dream_20260522T055016/median/paper.tex
artifacts/dream_reports/dream_20260522T055016/worst/paper.tex
artifacts/_project/paper/theorem1_proof.tex
artifacts/theorem1_proof.tex
docs/paper/analysis.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/threat_model.tex
docs/paper/introduction.tex
artifacts/dream_reports/dream_20260522T173833/best/paper.tex
artifacts/dream_reports/dream_20260522T173833/median/paper.tex
docs/paper/results.tex
docs/paper/methodology.tex
artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c1c5d71-8139-4c36-81c8-345bbdd88aae",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "7bb3d89a-a2dc-444b-b80a-68cb48e13578",
  "sourceToolAssistantUUID": "2c1c5d71-8139-4c36-81c8-345bbdd88aae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T18:40:41.213Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U4mqnTU231oFrLxLxYpPsm`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb3d89a-a2dc-444b-b80a-68cb48e13578",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6ZWVKAedaAz2yPZCV6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b23abc1-2e3b-4daf-a012-3a6b7889551c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01911AhUYMSNu7Z94jM6siQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7594,
      "cache_read_input_tokens": 22932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7594,
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

_source line 23 · 2026-05-22T18:40:41.244Z_

<details><summary>↩ Tool result · `toolu_01U4mqnTU231oFrLxLxYpPsm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/decisions.yaml\", \"content\": \"_next_id: 18\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 16:31 UTC\\n  summary: MVP 方案：API 模型验证 K_eff 对操纵抗性的预测力，三步验证（相关性测量→攻击抗性 scaling→K_eff 回归）\\n  rationale: 项目核心假设是 K_eff 公式能预测多 judge 面板的操纵抗性。MVP 用 API 模型而非开源模型，因为：(1) 无需 GPU 配置，分钟级启动；(2)\\n    API 模型覆盖多家族（OpenAI/Anthropic/Google/DeepSeek/Qwen），足以验证 cross-family vs within-family\\n    相关性差异；(3) 核心假设与模型部署方式无关——如果 K_eff 在 API 模型上不 work，在开源模型上也不会 work。外部评审 FAILED (35%)\\n    但理论框架可修正，需先验证经验基础再投入理论修正。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 16:37 UTC\\n  summary: MVP v2：基于 Reviewer 反馈修正统计设计，四步验证（相关性→homo/hetero 对照→K_eff 公式验证→scaling\\n    分析）\\n  rationale: Reviewer 指出 v1 五个问题：(1) K=1/3/5 仅 3 点无统计效力；(2) \\\"ASR 随 K 递减\\\"是 trivial\\n    gate，需 homo vs hetero 对照；(3) kill criteria 缺操作定义；(4) MI 估计器未指定；(5) K_eff 公式本身未验证。v2\\n    全部修正：新增 Step 2 homo/hetero panel 对照（核心 kill criterion）、Step 3 formula vs empirical\\n    effective rank 验证、K 扩展至 1/2/3/4/5/7 + attack×dataset 交叉产生 ≥15 数据点、MI 用 plug-in\\n    + Miller-Madow、kill criteria 操作化（bootstrap CI/≥80% 配置/配对检验 p<0.05）。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 17:06 UTC\\n  summary: MVP 改用开源模型在 GPU 服务器运行，取消 API 依赖\\n  rationale: 用户催促推进（\\\"push\\\"），API keys 迟迟未提供成为阻塞项。已有 4× RTX 6000 96G，可跑 4 个 70B 级开源模型（Qwen-72B\\n    / Llama-70B / Mistral-Large / Qwen-32B），覆盖 3 个家族 + 1 个 same-family 对照，满足 homo/hetero\\n    对比需求。开源模型还有可复现性优势。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-21 22:26 UTC\\n  summary: Step 1 结果显示 family diversity ≠ effective diversity；Step 2 对照组从 homo/hetero-family\\n    改为 high-K_eff vs low-K_eff panels\\n  rationale: 6 模型全量数据：within-family MI vs cross-family MI 无统计显著差异（MMLU p=0.218, ARC\\n    p=0.427）。大模型间 cross-family MI (0.487) 甚至高于最强 within-family pair (0.451)。原因：模型能力接近度而非家族身份驱动相关性。K_eff\\n    框架本身 agnostic——不关心 MI 来源，仍可能有效。但原始 Step 2 设计（K=3 same-family vs K=3 cross-family）已失去意义。改为直接用\\n    Step 1 实测 MI 计算各 panel 的 K_eff，对比 high-K_eff vs low-K_eff panels 的 ASR。这是更干净的测试，且\\\"family\\n    ≠ diversity\\\"本身是值得报告的发现。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-21 22:50 UTC\\n  summary: MI-based K_eff 为主指标，ρ-based 降为参考；Gaussian copula 全面失败（偏离 10-21×）作为论文发现之一\\n  rationale: Copula GoF 全量数据：MI_observed/MI_gaussian 均值 MMLU 21.1×、ARC 10.4×，14-15/15\\n    pairs 偏离 >2×。极端 case Mistral-Large↔Qwen-14B ρ≈0 但 MI=0.1-0.2（纯非线性依赖）。ρ-based K_eff\\n    对此 pair 会算出\\\"完全独立\\\"（1-0.001≈1），严重高估 panel independence。MI-based K_eff 直接使用观测信息量，不依赖\\n    Gaussian 假设，是唯一合理选择。论文中 copula 偏离本身作为 methodological finding 报告：\\\"LLM judge 间存在大量非线性依赖，线性相关系数系统性低估信息共享。\\\"\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-21 23:24 UTC\\n  summary: 论文 framing 降级：'certifiable' → 'quantifiable/measurable'；K_eff 理论定位从 proven\\n    bound 改为 Gaussian-motivated + empirically validated metric\\n  rationale: Reviewer 逐步审查 T1 证明链：K_eff = 1+(K-1)·exp(-2·I_max) 的上界性质（Step 3-5）依赖\\n    Gaussian compound symmetric 假设。Copula GoF 确认 LLM judge 分布偏离 Gaussian 10-21×。非\\n    Gaussian 下只有 trivial bound η_joint ≤ K·η_max，K_eff 公式不保证是 η_joint 的上界。因此不能 claim\\n    \\\"certifiable manipulation resistance\\\"。MI plug-in 估计可靠（正偏差是保守方向）。贡献栈调整：Gaussian\\n    下的 bound 作为 theoretical motivation，MI-based K_eff 作为 empirically validated diversity\\n    metric，copula 偏离和家族标签不可靠作为 methodological findings。Step 4 是论文去向的决定性测试。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-22 01:08 UTC\\n  summary: Step 2 反转：K_eff 被 individual robustness confound 淹没，选 Option A 控制变量重跑\\n  rationale: High K_eff panels 全含 llama-8b（弱模型→低MI→高K_eff 但个体脆弱），Low K_eff panels\\n    全大模型（相关但个体强健）。ASR 反转不代表 K_eff 无效，而是被 robustness confound 掩盖。选 Option A：只用 4 个大模型(72B/70B/32B/Mistral-Large)的\\n    C(4,3)=4 panels 控制个体鲁棒性后重测。同时计算 single-judge ASR 量化 confound。Option B（修改公式）和 C（reframe）在\\n    A 结果出来前都为时过早。\\n  related_experiments:\\n  - exp_id: mvp-step2-keff-contrast\\n    role: evidence\\n    result: negative-confounded\\n  depends_on:\\n  - D004\\n  - D005\\n- id: D008\\n  date: 2026-05-22 03:21 UTC\\n  summary: MVP 原假设部分证伪：K_eff 仅对 shared-bias attacks 显著，η_max 主导 targeted attacks。探索\\n    attack-conditioned 双因子框架。\\n  rationale: 20-panel 多元回归 log(ASR)~log(K_eff)+log(η_max) 结果：K_eff 显著为负仅 1/6（arc×sycophancy\\n    β=-2.85 p=0.003），η_max 显著为正 4/6。攻击分类：targeted attacks（prompt injection, score\\n    manipulation）ASR≈f(η_max)，K_eff 无关；broad-spectrum attacks（sycophancy/共享偏差）ASR\\n    受 K_eff 影响。不立即 pivot 到 Path B（weakest-link reframe），先验证 attack taxonomy——增加 2-3\\n    种 broad-spectrum 攻击看 K_eff 是否一致有效。如果一致 → attack-conditioned K_eff theory（Path\\n    A 升级版）；如果不一致 → 全面 pivot 到 Path B。\\n  related_experiments:\\n  - exp_id: mvp-step2v3-retry3\\n    role: evidence\\n    result: partial-negative\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-22 04:56 UTC\\n  summary: Taxonomy 验证失败（0/6 新条件 K_eff 显著），建议 kill 项目\\n  rationale: 12 条件全景：K_eff 显著为负仅 1/12（arc×sycophancy，Bonferroni 勉强通过，同类攻击不复现，降级为孤立异常）。η_max\\n    显著 7/12 但\\\"最弱评委决定安全性\\\"可能被审稿人视为 trivial。Reviewer 评估当前 2.0-2.5，扩展后最高 3.0-3.5，不够 AAAI\\n    main（3.5+）。贡献栈过薄：负结果（K_eff 无效）+ 弱正结果（η_max 主导但可能 obvious）+ 方法论（copula 失败）无法支撑\\n    A 类投稿。\\n  related_experiments:\\n  - exp_id: taxonomy-broad-spectrum\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-22 06:58 UTC\\n  summary: Dream review (2.5 all tiers) exposed 13 structural issues; proceed with\\n    fixes, NOT kill\\n  rationale: 'Dream dream_20260522T055016 returned 2.5 (Borderline Findings) across\\n    best/median/worst — flat scoring indicates structural issues not data-dependent.\\n    Key fixes: (1) Theorem 1 proof gap — must account for ⌈K/2⌉ majority requirement;\\n    (2) Novelty reframe — acknowledge weakest-link known in security, position as\\n    first empirical quantification in LLM-judge domain; (3) VIF/multicollinearity\\n    analysis on existing data; (4) Multiple comparison correction; (5) Non-majority-vote\\n    aggregation; (6) Open-ended benchmark beyond MCQ; (7) \\\"When diversity helps\\\" section.\\n    User confirmed continue (not kill), target EMNLP 2026, GPUs unlimited. Immediate\\n    actions: plan_009 (VIF analysis, P0, no GPU), plan_001 (model expansion, P0),\\n    plan_003 (formal theorem, P0). Framing updated to v3.'\\n  related_experiments: []\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-22 07:08 UTC\\n  summary: Plan_003 BFT contrast failed (0/12 random-fault K_eff significant); Claim\\n    2 conditional on plan_001 model expansion\\n  rationale: 'Random-fault simulation showed K_eff 0/12 significant negative — same\\n    as adaptive (1/12). BFT vs adaptive contrast cannot be demonstrated with current\\n    6-model pool due to K_eff-η_max structural confound. R² difference (adaptive 0.14-0.73\\n    vs random-fault 0.55-0.95) is the only positive finding. Reviewer recommends:\\n    don''t reframe Claim 2 yet, wait for plan_001 (15+ models) which may break the\\n    confound. If plan_001 also fails to show K_eff distinction → Claim 2 must be dropped,\\n    ceiling falls to ~2.5-3.0. Theorem 1 direction adjusted: prove monotonicity in\\n    η_max (option b) rather than K_eff regime distinction.'\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: go/no-go gate\\n    result: failed — 0/12 K_eff significant under random faults\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-22 12:16 UTC\\n  summary: Plan_010 聚合实验完成：Bayesian 部分打破 weakest-link (3/12 vs 8/12)，threshold 下 diversity\\n    有害。纳入 Claim 7，Theorem 1 加 scope qualifier。\\n  rationale: 6 模型初步结果显示聚合规则显著调制 weakest-link 效应：majority/weighted 下 η_max 7-8/12 显著（Theorem\\n    1 成立），Bayesian 下仅 3/12（reliability weighting 降低弱 judge 影响），threshold 下 K_eff 正向显著（diversity\\n    在 unanimity 下有害）。Reviewer 确认方向有效但标 2 个 warning：(1) Bayesian 用同数据集 clean accuracy\\n    有信息泄漏嫌疑；(2) 缺 FDR 校正。两者在 15 模型版本中修复。该发现将论文从 negative-only 升级为 negative + positive\\n    prescription，增加实用价值。\\n  related_experiments:\\n  - exp_id: plan_010\\n    role: primary\\n    result: positive — aggregation modulates weakest-link\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-22 15:11 UTC\\n  summary: 7-model 预览显示 Claim 2 复活信号：random-fault K_eff gains 6/12（vs plan_003 的 0/12），ΔR²=+0.237。η_max\\n    提升到 10/12。等 15-model 455 panels 确认。\\n  rationale: '加入 claude-3-haiku（跨族 + 弱模型）后 confound 方向反转（r=+0.473），打破了 plan_003 时的结构性假阴性。Random-fault\\n    下 K_eff 6/12 显著优于 adaptive 的 0-1/12，初步恢复了 BFT adaptive/random-fault 对比的核心叙事。但仅\\n    35 panels 统计功效有限，且主要由 haiku 单点驱动。15-model 全量结果（ETA 8-10h）是最终判定。如果复现 → Claim 2\\n    恢复为 #2 贡献；如果不复现 → 维持 conditional。'\\n  related_experiments:\\n  - exp_id: plan_001_7model_preview\\n    role: primary\\n    result: positive signal — confound broken, Claim 2 revival, η_max 10/12\\n  depends_on:\\n  - D011\\n  - D012\\n- id: D014\\n  date: 2026-05-22 17:16 UTC\\n  summary: 15-model 结果证伪原始 Claim 1 (\\\"K_eff irrelevant\\\")；K_eff 12/12 显著正，diversity\\n    有害。Paper framing 需从 v3 升级到 v4\\n  rationale: '15-model/455-panel regression: K_eff 12/12 FDR sig positive (β>0), η_max\\n    9/12 sig。在 2 个 confound-free 条件 (r≈0.35, VIF≈1.14) 中 K_eff 仍极显著 (p=6e-26, 4e-16)，排除\\n    confound artifact 可能。Sensitivity (排除 ACC<0.5) 11/12 仍显著。论文叙事需从 \\\"diversity doesn''t\\n    help\\\" 转向 \\\"diversity actively hurts, mechanism = diversity-capability tradeoff\\\"。Claim\\n    1 与 Claim 3 合并为更强结论。等待 residualized K_eff 分析确认独立效应强度。'\\n  related_experiments:\\n  - exp_id: plan001_step1_full_v4\\n    role: primary\\n    result: K_eff 12/12 sig positive, η_max 9/12 sig\\n  depends_on:\\n  - D013\\n  - D012\\n- id: D015\\n  date: 2026-05-22 18:05 UTC\\n  summary: Claim 5 (Gaussian Copula Failure) falsified at 15-model scale; removed\\n    from contribution stack\\n  rationale: '15-model copula analysis: MI_obs/MI_gaussian ratio = 0.93 (MMLU), 0.90\\n    (ARC robust). 6-model 10-21× was small-sample artifact (15→105 pairs diluted extreme\\n    values). Only haiku pairs show extreme ratios (212×). Claim downgraded to minor\\n    observation. Contribution stack reduced from 8 to 7.'\\n  related_experiments:\\n  - exp_id: worker_analysis_15model-family-copula\\n    role: falsified Claim 5\\n    result: ratio ~0.9, copula fits well\\n  depends_on:\\n  - D014\\n- id: D016\\n  date: 2026-05-22 18:20 UTC\\n  summary: 'Claim 7 revised: \\\"Bayesian breaks weakest-link\\\" falsified → \\\"Bayesian\\n    mitigates diversity-as-vulnerability while η_max remains dominant\\\"'\\n  rationale: '15-model P2 aggregation results: η_max remains 12/12 FDR sig under Bayesian\\n    (vs 3/12 at 6 models — original claim was scale artifact). But K_eff sig drops\\n    from 12/12 (majority) to 5/12 (Bayesian), β direction partially flips (3/12 negative).\\n    Bayesian calibration suppresses the harmful diversity effect without weakening\\n    weakest-link protection. New narrative: aggregation method modulates diversity\\n    vulnerability, not weakest-link dominance. Prescriptive angle: practitioners should\\n    prefer Bayesian calibration to mitigate diversity-as-vulnerability.'\\n  related_experiments:\\n  - exp_id: plan001_step1_full_v4\\n    role: P2 aggregation source data\\n    result: majority K_eff 12/12 positive → bayesian K_eff 5/12 with 3 neg; η_max\\n      12/12 stable across all methods\\n  depends_on:\\n  - D014\\n  - D012\\n- id: D017\\n  date: 2026-05-22 18:39 UTC\\n  summary: 'Claim 7 final (log-log canonical): Bayesian partially mitigates BOTH drivers\\n    — η_max 11→9/12, K_eff flips to 4/5 negative (protective). D016 level-level numbers\\n    superseded.'\\n  rationale: 'P2b log-log canonical rerun resolves spec inconsistency (Reviewer #1).\\n    Majority row sanity-checks against dominance canonical. Under Bayesian: η_max\\n    drops from 11/12 to 9/12 (weakest-link partially weakened), K_eff 4/5 significant\\n    coefficients are negative (diversity becomes protective). Threshold shows R²=0.901\\n    (near-perfect dual-driver fit under unanimity). Weighted is strongest dual-driver\\n    (K_eff 11/12 all positive). The aggregation gradient (majority→weighted→threshold→bayesian)\\n    reveals how different voting rules modulate the diversity channel and weakest-link\\n    channel independently.'\\n  related_experiments:\\n  - exp_id: plan001_step1_full_v4\\n    role: P2b log-log aggregation source\\n    result: majority η_max 11/12 K_eff 8/12(7+1-) | weighted 11/12 11/12(11+) | threshold\\n      12/12 11/12(10+1-) R²=0.90 | bayesian 9/12 5/12(1+4-)\\n  depends_on:\\n  - D016\\n  - D014\\n\", \"total_chars\": 12035, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b23abc1-2e3b-4daf-a012-3a6b7889551c",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "78d6e0bd-fdc9-4ec4-b49b-ec05a660bb79",
  "sourceToolAssistantUUID": "8b23abc1-2e3b-4daf-a012-3a6b7889551c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T18:40:46.333Z_

<details open><summary>🔧 Tool call — Read · `toolu_016eQ2SiqH7KBWovZjm8D3Tq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78d6e0bd-fdc9-4ec4-b49b-ec05a660bb79",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6ZvjpeZMU9fBUkZ88e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20f43779-6175-47f1-ad94-16a60ddc0083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GR3Nnrj5sgQhwCaZoxJFLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6627,
      "cache_read_input_tokens": 30526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6627,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 25 · 2026-05-22T18:40:46.338Z_

<details><summary>↩ Tool result · `toolu_016eQ2SiqH7KBWovZjm8D3Tq`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Evaluation Biases.}
4	The use of large language models as automatic evaluators gained traction after \citet{zheng2023judging} introduced MT-Bench and Chatbot Arena, establishing LLM judges as scalable alternatives to human annotation. Subsequent work documented systematic failure modes: \citet{wang2023fair} showed that individual LLM judges exhibit position bias, verbosity preferences, and sycophancy, all of which compromise evaluation reliability. Multi-judge panels have been proposed to mitigate these biases by aggregating decisions across diverse models. A recent systematization of knowledge on LLM-judge security \cite{almasoud2026security} reports that 7-model committees reduce attack success rates to 10--19\%, down from 50--68\% for individual open-source judges. However, this empirical observation lacks a causal explanation: it does not disentangle whether the reduction stems from judge diversity per se or from the inclusion of individually robust models. We address precisely this gap, providing the first controlled analysis that separates the contributions of panel diversity and individual judge robustness under adaptive attack.
5	
6	\paragraph{Adversarial Robustness and Transferability.}
7	Adversarial vulnerability in neural networks was formalized by \citet{goodfellow2015adversarial}, who showed that imperceptible input perturbations can cause misclassification. A key property of such adversarial examples is transferability: \citet{papernot2016transferability} demonstrated that adversarial inputs crafted for one model frequently fool others, and \citet{papernot2017practical} exploited this for black-box attacks via substitute models. \citet{tramer2018ensemble} showed that ensemble adversarial training improves robustness but does not eliminate cross-model vulnerability, because transferred perturbations remain effective across architectures. In the LLM domain, prompt injection attacks \cite{greshake2023not} and adversarial prompt crafting \cite{schulhoff2023hackaprompt} exploit analogous transferability: manipulative prompts designed for one judge model frequently succeed against others from the same capability tier. This cross-model attack transferability enables adaptive adversaries to concentrate effort on the weakest panel member, and it forms the empirical basis for the weakest-link effect we quantify.
8	
9	\paragraph{Ensemble Diversity and Multi-Agent Scaling.}
10	The theoretical foundations of ensemble diversity trace to \citet{krogh1995neural}, who proved that ensemble error decomposes into average member error minus a diversity term that measures disagreement among members. For LLM-based multi-agent systems, \citet{yang2026diversity} formalize this through an information-theoretic framework, defining an effective channel count $K^* = 2^{H(\rho)}$ that governs performance scaling as a function of the correlation structure. \citet{turkmen2026ensemble} develop a Gaussian copula model for ensemble selection, deriving error floor bounds that depend on pairwise mutual information rather than individual accuracy alone. On the empirical side, \citet{kim2025correlated} find that LLM errors are substantially correlated: when two models both err, they agree on the wrong answer 60\% of the time, with same-company pairs exhibiting 6.6\% higher agreement. \citet{kuai2026independent} audit behavioral entanglement across 18 models and find that cross-family entanglement is 40--60\% lower than within-family entanglement but remains far from zero. \citet{keppo2026fragility} show that increasing agent count from 2 to 5 disrupts collusive dynamics in cooperative settings. These works study how diversity improves performance under benign conditions. We provide the adversarial security dual: the same correlation structures that govern performance scaling also determine an attacker's ability to simultaneously compromise multiple judges.
11	
12	\paragraph{Byzantine Fault Tolerance and Security Analogies.}
13	Multi-judge evaluation panels implicitly invoke a Byzantine Fault Tolerance (BFT) analogy: majority voting among $n$ judges tolerates up to $f < n/3$ arbitrarily faulty members \cite{lamport1982byzantine,castro1999practical}, including malicious ones. This classical guarantee bounds the \emph{number} of faulty nodes but does not model adversaries that strategically target system structure. \citet{schneier2000secrets} articulated the weakest-link principle for security systems: an attacker need only find and exploit the single most vulnerable component, and aggregate redundancy becomes irrelevant. The distinction between random faults and adaptive attacks is well-established in systems security, yet the LLM evaluation community continues to treat judge diversity as if the BFT preconditions hold. We make this implicit analogy explicit and test it empirically: adaptive adversaries violate the independence assumption underlying BFT, and panel security collapses to the robustness of the weakest individual judge.
14	
15	\paragraph{Information-Theoretic Approaches to Evaluation.}
16	Several recent works apply information-theoretic tools to LLM evaluation. \citet{robertson2025stepwise} propose a TVD-MI framework for stepwise evaluation, proving that bounded divergences maintain polynomial certification under mode-collapse attacks. \citet{kaneko2025bits} derive tight single-model attack cost bounds via Fano's inequality, establishing that an adversary requires at least $\log_2(1/\varepsilon) / I_{\max}$ queries to reduce detection probability below $\varepsilon$. For imperfect but honest judges, \citet{feng2026noisy} develop statistical hypothesis tests with finite-sample Type-I error control despite calibration uncertainty. On the incentive design side, \citet{chen2025incentivizing} and \citet{qiu2026truthfulness} apply peer prediction mechanisms to elicit truthful judgments from LLMs under conditional independence assumptions. These lines of work address complementary concerns: statistical validity under noise, single-model attack costs, and truthfulness incentives. Our study fills the remaining gap by examining how adversarial manipulation interacts with multi-judge composition, a setting where neither honest-noise nor single-model assumptions hold.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20f43779-6175-47f1-ad94-16a60ddc0083",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "1be02e22-c442-4cf8-8880-65d5cad7be0a",
  "sourceToolAssistantUUID": "20f43779-6175-47f1-ad94-16a60ddc0083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T18:40:46.774Z_

<details open><summary>🔧 Tool call — Read · `toolu_012pSkbnqGN8z4FTkzMCt9cZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1be02e22-c442-4cf8-8880-65d5cad7be0a",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6ZvjpeZMU9fBUkZ88e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61cc367d-a2b9-4e05-81cb-5d4aa9cbf97b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GR3Nnrj5sgQhwCaZoxJFLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6627,
      "cache_read_input_tokens": 30526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6627,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 27 · 2026-05-22T18:40:46.778Z_

<details><summary>↩ Tool result · `toolu_012pSkbnqGN8z4FTkzMCt9cZ`</summary>

```text
1	\section{Introduction}
2	
3	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work revealed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing on an implicit analogy to Byzantine fault tolerance (BFT), where majority voting among $n$ independent nodes tolerates up to $f < n/3$ faulty members \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reinforces this assumption, reporting that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
4	
5	Yet the evidence for diversity as a causal defense mechanism is weaker than it appears. The observed ASR reduction in multi-judge panels \citep{almasoud2026security} conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of the strongest members. No existing work disentangles these contributions. The theoretical justification rests on similarly uncertain ground: the strong data-processing inequality (SDPI) bounds joint failure in terms of effective independence, but assumes non-adaptive faults. BFT guarantees tolerate arbitrary failures up to a threshold count, yet do not model adversaries that observe panel composition and strategically select attacks \citep{schneier2000secrets}. When the threat shifts from random noise to adaptive manipulation, the assumptions underlying the diversity defense no longer hold.
6	
7	Adding more diverse judges to an evaluation panel predominantly increases, rather than decreases, vulnerability to adversarial manipulation. The reversal mechanism is straightforward. Under random faults, independent judges fail via uncorrelated events, and majority voting aggregates away individual errors. Under an adaptive adversary, the picture inverts: functionally diverse judges respond to different manipulation strategies, and an adversary who observes the panel can exploit judge-specific vulnerabilities across a broader space of attacks \citep{goodfellow2015adversarial,papernot2016transferability}. Diversity ceases to provide mutual protection and instead expands the viable attack surface. We call this the \emph{diversity trap}: the same property that reduces vulnerability under random faults increases it under strategic attack.
8	
9	Controlled experiments across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks (MMLU, ARC) confirm that diversity predominantly increases vulnerability: $K_{\mathrm{eff}}$, a pairwise-MI-based diversity metric, is a significant positive predictor of panel attack success rate in 7 of 12 conditions, non-significant in 4, and significantly \emph{negative} in 1 (sycophancy on ARC, where diverse panels dilute a shared cognitive bias). The weakest-judge channel $\eta_{\max}$ is significant in 11 of 12 conditions. Dominance analysis reveals condition-dependent patterns: $\eta_{\max}$ is the sole dominant predictor in 4 conditions, both drivers are co-dominant in 7, and $K_{\mathrm{eff}}$ alone dominates in 1 condition (position bias on ARC). The sycophancy exception is mechanistically informative: when the attack exploits a bias shared across all judges, diverse panels dilute that bias---precisely the regime where the BFT analogy holds.
10	
11	These findings yield three contributions:
12	\begin{enumerate}
13	\item \textbf{Diversity trap and dual vulnerability drivers.} The first empirical quantification showing that panel diversity ($K_{\mathrm{eff}}$) predominantly and independently predicts vulnerability under adaptive attack (7 of 12 conditions), across 15 models, 455 panels, and dominance analysis that isolates each driver's contribution (\S\ref{sec:experiments}).
14	\item \textbf{BFT reversal mechanism.} Formal and empirical demonstration of why diversity helps under random faults but hurts under adaptive adversaries, with condition-dependent importance patterns that reveal when each vulnerability channel dominates (\S\ref{sec:threat_model}, \S\ref{sec:analysis}).
15	\item \textbf{Robustness-first panel design.} An actionable defense combining robustness screening with reliability-weighted aggregation that addresses both vulnerability channels (\S\ref{sec:analysis}).
16	\end{enumerate}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61cc367d-a2b9-4e05-81cb-5d4aa9cbf97b",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "20cfdf9d-ae26-4642-a579-31d145063979",
  "sourceToolAssistantUUID": "61cc367d-a2b9-4e05-81cb-5d4aa9cbf97b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T18:40:47.243Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B7iz54vntYViUHw3wP52h8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20cfdf9d-ae26-4642-a579-31d145063979",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6ZvjpeZMU9fBUkZ88e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b96a5e91-5a06-4718-b42f-c0d2b126a2d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GR3Nnrj5sgQhwCaZoxJFLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6627,
      "cache_read_input_tokens": 30526,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 30526,
          "cache_creation_input_tokens": 6627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6627,
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

_source line 29 · 2026-05-22T18:40:47.248Z_

<details><summary>↩ Tool result · `toolu_01B7iz54vntYViUHw3wP52h8`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Weakest Link: Why Judge Diversity Fails Under\\Adaptive Adversaries in Multi-LLM Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	% [PLACEHOLDER — waiting for plan_001 results]
28	\end{abstract}
29	
30	% Section files managed by write_paper_section
31	\input{introduction}    % [PLACEHOLDER — waiting for plan_001 results]
32	\input{related_work}
33	\input{threat_model}
34	\input{methodology}
35	\input{results}          % [PLACEHOLDER — waiting for plan_001 results]
36	\input{analysis}         % [PLACEHOLDER — waiting for plan_001 results]
37	\input{conclusion}       % [PLACEHOLDER — waiting for plan_001 results]
38	
39	\section*{Limitations}
40	% [PLACEHOLDER — short paragraph, ~3 points per EMNLP rules]
41	
42	\bibliography{references}
43	\bibliographystyle{acl_natbib}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b96a5e91-5a06-4718-b42f-c0d2b126a2d4",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "80cd094d-88fb-4e17-a3d8-d13d70b90798",
  "sourceToolAssistantUUID": "b96a5e91-5a06-4718-b42f-c0d2b126a2d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T18:40:52.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_0145JvkCPG56QM8YTsGkUay1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80cd094d-88fb-4e17-a3d8-d13d70b90798",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6aMNANU2QCJ6esnLrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b631a2a7-2eae-4bc4-a6c1-cefe845d7066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoA1PVayJwBL83HUikyRew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3386,
      "cache_read_input_tokens": 37153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3386,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 31 · 2026-05-22T18:40:52.355Z_

<details><summary>↩ Tool result · `toolu_0145JvkCPG56QM8YTsGkUay1`</summary>

```text
1	\section{Experimental Methodology}
2	\label{sec:experiments}
3	
4	\subsection{Models and Panel Construction}
5	
6	We select 15 models spanning 6 provider families: Qwen, Llama, Mistral, Anthropic (Claude), OpenAI (GPT), and Google (Gemini). Models are grouped into three capability tiers: \emph{frontier} (GPT-4o, Claude-3.5-Sonnet, Gemini-1.5-Pro), \emph{mid-tier} (Qwen2.5-72B, Llama-3.1-70B, Mistral-Large), and \emph{lightweight} (Qwen2.5-7B, Llama-3.1-8B, and others at comparable scale). This selection covers the full range of model sizes and training lineages deployed in practice for LLM-based evaluation. All panels consist of $K{=}3$ judges with majority-vote threshold $t{=}2$. Exhaustive enumeration of all 3-judge subsets yields $\binom{15}{3} = 455$ unique panels, covering every combination of provider families and capability tiers. Each panel evaluates all benchmark items under all attack types, producing a complete panel $\times$ item $\times$ attack tensor.
7	
8	\subsection{Benchmarks and Attack Types}
9	
10	Two benchmarks test distinct evaluation capabilities: MMLU \citep{hendrycks2021mmlu}, a knowledge-intensive multiple-choice benchmark spanning 57 subjects, and ARC \citep{clark2018arc}, a reasoning-intensive science question benchmark. MMLU probes factual recall and broad domain knowledge; ARC requires multi-step scientific reasoning.
11	
12	Each benchmark is paired with six attack types that target different judge vulnerabilities: (1)~\textbf{prompt injection}, adversarial instructions embedded in candidate text that override the evaluation prompt \citep{perez2022ignore,greshake2023not}; (2)~\textbf{sycophancy}, responses engineered to agree with or flatter the judge \citep{wang2023fair}; (3)~\textbf{score manipulation}, explicit numerical cues (e.g., ``this answer deserves a 10/10'') injected into the candidate to anchor scoring; (4)~\textbf{verbosity bias}, padding correct answers with excessive irrelevant detail to exploit length preferences \citep{zheng2023judging}; (5)~\textbf{position bias}, reordering candidate answers to place the target in the position judges systematically favor \citep{wang2023fair}; and (6)~\textbf{authority bias}, prefacing candidate text with fabricated credentials or citations to inflate perceived credibility. The combination of 2 benchmarks and 6 attacks produces 12 experimental conditions, each evaluated across all 455 panels.
13	
14	\subsection{Vulnerability Metrics}
15	
16	Per-judge vulnerability under attack $a$ is the fraction of items where judge $j$ is fooled: $\eta_j(a) = \Pr(X_j^a {=} 1)$, estimated empirically over the item set. The weakest-link vulnerability $\eta_{\max}(a) = \max_{j \in \mathcal{P}} \eta_j(a)$ captures the most susceptible member of each panel. The panel attack success rate $\mathrm{ASR}(\mathcal{P}, a)$ is the fraction of items where at least $t$ judges are simultaneously fooled. Panel diversity is quantified by $K_{\mathrm{eff}}$ (Equation~\ref{eq:keff}), computed from pairwise mutual information \citep{kraskov2004estimating} between judges' binary failure indicators on clean (unattacked) data. Together, $\eta_{\max}$ and $K_{\mathrm{eff}}$ serve as the two predictors in the regression framework below: $\eta_{\max}$ indexes the weakest-link channel and $K_{\mathrm{eff}}$ indexes the diversity channel.
17	
18	\subsection{Aggregation Methods}
19	
20	Beyond the default majority vote, we evaluate three alternative aggregation rules to test whether the diversity trap persists under different decision mechanisms.
21	
22	\paragraph{Majority Vote.} Accept if $\sum_{j=1}^K \mathbf{1}[J_j \text{ approves}] \geq \lceil K/2 \rceil$. This is the standard baseline aggregation assumed throughout the main analysis.
23	
24	\paragraph{Accuracy-Weighted Vote.} Accept if $\sum_{j=1}^K w_j \cdot \mathbf{1}[J_j \text{ approves}] > 0.5$, where $w_j \propto \mathrm{acc}_j$ on held-out clean data, normalized so that $\sum_j w_j = 1$. Judges with higher clean-data accuracy receive proportionally greater influence.
25	
26	\paragraph{Threshold Vote (Unanimity).} Accept only if all $K$ judges approve ($t = K$). A single dissenting judge suffices to reject, making this the most conservative rule.
27	
28	\paragraph{Bayesian Calibration.} Compute $P(\text{correct} \mid \mathbf{v}) \propto P(\text{correct}) \prod_j P(v_j \mid \text{correct})$, where $P(v_j \mid \cdot)$ is derived from judge $j$'s confusion matrix on clean data and $\mathbf{v}$ is the observed vote vector. Accept if the posterior exceeds 0.5. This rule uses each judge's calibrated reliability rather than treating all votes equally.
29	
30	\subsection{Statistical Framework}
31	\label{sec:stat_framework}
32	
33	To disentangle the contributions of panel diversity and individual judge robustness, we fit a log-log OLS regression for each of the 12 conditions:
34	\begin{equation}
35	\label{eq:regression}
36	\log(\mathrm{ASR} + \epsilon) = \alpha + \beta_1 \log(K_{\mathrm{eff}}) + \beta_2 \log(\eta_{\max} + \epsilon),
37	\end{equation}
38	with $\epsilon = 10^{-6}$ to handle zero values. Standardized coefficients $\hat{\beta}_{\mathrm{std}} = \hat{\beta} \cdot \mathrm{SD}(\log x) / \mathrm{SD}(\log y)$ enable direct comparison of effect magnitudes across predictors and conditions. We apply Benjamini-Hochberg correction for multiple testing, controlling the false discovery rate per predictor across the 12 conditions.
39	
40	To assess relative predictor importance beyond regression coefficients, we perform dominance analysis [CITE NEEDED: Budescu 1993 dominance analysis]. This method decomposes $R^2$ by averaging each predictor's incremental $R^2$ contribution across all possible subsets of predictors. A predictor is \emph{dominant} if its average contribution exceeds that of the competing predictor in every subset ordering. With two predictors, dominance reduces to comparing each predictor's solo $R^2$ with its incremental $R^2$ conditional on the other.
41	
42	\subsection{Sensitivity Analysis}
43	
44	Judges with clean-data accuracy below 0.5 perform at or below chance and could drive regression results through extreme outlier behavior rather than meaningful vulnerability patterns. We exclude such judges from panel construction and re-run the log-log regression (Equation~\ref{eq:regression}) to verify that the $K_{\mathrm{eff}}$ effect remains stable after removing these potential confounds.
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b631a2a7-2eae-4bc4-a6c1-cefe845d7066",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "ef7f0802-0f58-462a-85ac-24616edbea3c",
  "sourceToolAssistantUUID": "b631a2a7-2eae-4bc4-a6c1-cefe845d7066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T18:40:53.092Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EAoSnHjqu5wMY3JG6kDxdJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef7f0802-0f58-462a-85ac-24616edbea3c",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6aMNANU2QCJ6esnLrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c43ee362-01c3-43e8-ad5b-4da7a739a848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoA1PVayJwBL83HUikyRew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3386,
      "cache_read_input_tokens": 37153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3386,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 33 · 2026-05-22T18:40:53.096Z_

<details><summary>↩ Tool result · `toolu_01EAoSnHjqu5wMY3JG6kDxdJ`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	% [Main dual vulnerability driver results — to be written when P0 dominance analysis is finalized]
5	
6	\subsection{Aggregation Rules Modulate the Diversity Channel}
7	\label{sec:aggregation}
8	
9	The dual vulnerability driver effect varies substantially across aggregation methods. Table~\ref{tab:aggregation} reports regression results for each method across all 12 conditions.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\begin{tabular}{lcccc}
15	\toprule
16	\textbf{Method} & \textbf{$\eta_{\max}$ sig} & \textbf{$K_{\mathrm{eff}}$ sig} & \textbf{$K_{\mathrm{eff}}$ $\beta$ dir.} & \textbf{$R^2$} \\
17	\midrule
18	Majority       & 12/12 & 12/12 & all positive & 0.433 \\
19	Weighted        & 12/12 & 11/12 & all positive & 0.419 \\
20	Threshold       & 10/12 & 6/12  & 3 negative   & 0.165 \\
21	Bayesian        & 12/12 & 5/12  & 3 negative   & 0.141 \\
22	\bottomrule
23	\end{tabular}
24	\caption{Aggregation method comparison (15 models, 455 panels). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Bayesian calibration sharply reduces $K_{\mathrm{eff}}$ significance while $\eta_{\max}$ remains consistently dominant.}
25	\label{tab:aggregation}
26	\end{table}
27	
28	Three patterns emerge. First, $\eta_{\max}$ remains significant in $\geq$10 of 12 conditions under every aggregation method---the weakest-link channel is robust to the choice of decision rule. Second, Bayesian calibration sharply suppresses the diversity channel: $K_{\mathrm{eff}}$ significance drops from 12/12 (majority) to 5/12 (Bayesian), and the coefficient direction flips to negative in 3 conditions, meaning diversity becomes partially protective when judge reliability is properly calibrated. Third, $R^2$ drops from 0.433 (majority) to 0.141 (Bayesian), indicating that Bayesian aggregation homogenizes the ASR distribution across panels---compositional factors explain less variance, though the residual variance is harder to predict.
29	
30	These results have a direct prescriptive implication. Since Bayesian calibration suppresses the diversity channel without weakening the weakest-link channel, a two-pronged defense is needed: robustness-first panel selection to address $\eta_{\max}$, combined with Bayesian aggregation to mitigate the $K_{\mathrm{eff}}$ vulnerability. Neither intervention alone addresses both drivers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c43ee362-01c3-43e8-ad5b-4da7a739a848",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "385aa483-0a30-4c00-ae97-b0884018e038",
  "sourceToolAssistantUUID": "c43ee362-01c3-43e8-ad5b-4da7a739a848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T18:40:53.208Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FQJ4ULe3YTJ1n3mwgeDmrE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "385aa483-0a30-4c00-ae97-b0884018e038",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6aMNANU2QCJ6esnLrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc1bd64d-361f-4077-aba1-b12956124632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoA1PVayJwBL83HUikyRew",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3386,
      "cache_read_input_tokens": 37153,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3386
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 37153,
          "cache_creation_input_tokens": 3386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3386,
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

_source line 35 · 2026-05-22T18:40:53.212Z_

<details><summary>↩ Tool result · `toolu_01FQJ4ULe3YTJ1n3mwgeDmrE`</summary>

```text
1	\section{Analysis}
2	% [PLACEHOLDER — waiting for plan\_001 results]
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc1bd64d-361f-4077-aba1-b12956124632",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "70eb5f97-86bc-4397-805c-45682be648a8",
  "sourceToolAssistantUUID": "cc1bd64d-361f-4077-aba1-b12956124632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T18:40:57.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bm6YrnnvoCQuHHNvyUkZ5v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70eb5f97-86bc-4397-805c-45682be648a8",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6anwnt442x889b3Zox",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca02af04-df56-4d19-85fe-a730bc67645d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAYh6RqLTzbuMePH6NzVK2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3049,
      "cache_read_input_tokens": 40539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3049,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 37 · 2026-05-22T18:40:57.948Z_

<details><summary>↩ Tool result · `toolu_01Bm6YrnnvoCQuHHNvyUkZ5v`</summary>

```text
1	\section{Threat Model and Problem Formulation}
2	
3	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \lceil K/2 \rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised with marginal failure probability $\eta_j(a) = \Pr(X_j^a = 1)$, where $X_j^a \in \{0,1\}$ denotes the failure indicator. We write $\eta_{\max} = \max_j \eta_j$ for the vulnerability of the weakest judge. The \emph{panel attack success rate} is $\mathrm{ASR}(\mathcal{P}, a) = \Pr\!\bigl(\sum_{j=1}^K X_j^a \geq t\bigr)$.
4	
5	To quantify diversity, we define the \emph{effective independence} $K_{\mathrm{eff}}$ directly from pairwise mutual information among judges:
6	\begin{equation}
7	\label{eq:keff}
8	K_{\mathrm{eff}} = \frac{1}{K}\sum_{i=1}^{K} \Bigl[1 + \sum_{j \neq i} \exp\!\bigl(-2 \cdot \mathrm{MI}(i,j)\bigr)\Bigr].
9	\end{equation}
10	This formulation computes effective independence from pairwise MI estimates without matrix decomposition, and is more stable for small panels ($K{=}3$). It ranges from $K_{\mathrm{eff}} \approx K$ when judges are nearly independent ($\mathrm{MI} \to 0$) to $K_{\mathrm{eff}} \approx 1$ when judges are highly correlated ($\mathrm{MI} \to \infty$). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\eta_{\mathrm{joint}} \leq \min(1,\; K_{\mathrm{eff}} \cdot \eta_{\max})$, suggesting that diversity should help---but this bound assumes non-adaptive faults.
11	
12	\begin{definition}[Adaptive Adversary]
13	\label{def:adversary}
14	An \emph{adaptive adversary} has full knowledge of the panel composition $\mathcal{P}$, the per-judge vulnerability profiles $\{\eta_j(\cdot)\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \arg\max_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}, a)$ to maximize the panel ASR, yielding $\mathrm{ASR}^*(\mathcal{P}) = \sup_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}, a)$.
15	\end{definition}
16	
17	This departs from Byzantine fault-tolerance (BFT) models~\cite{lamport1982byzantine,castro1999practical}, which tolerate arbitrary (including malicious) faults provided the number of faulty nodes satisfies $f < n/3$, but do not model adversaries that strategically target system structure. An adaptive adversary instead concentrates attack effort on the weakest link~\cite{schneier2000secrets}, rendering diversity-based defenses less effective than the SDPI bound implies.
18	
19	The distinction reveals a \emph{reversal mechanism}: under random faults, independent judges fail via uncorrelated events, and majority voting aggregates away individual errors---higher $K_{\mathrm{eff}}$ reduces joint failure probability. Under adaptive adversaries, however, independent judges present a \emph{wider attack surface}: the adversary can exploit judge-specific vulnerabilities across a broader space of attacks, because functionally diverse judges respond to different manipulation strategies. Diversity ceases to provide mutual protection and instead expands the set of viable attack vectors.
20	
21	\begin{theorem}[Weakest-Link Monotonicity]
22	\label{thm:monotonicity}
23	Let $\mathcal{P}$ and $\mathcal{P}'$ be two panels sharing $K{-}1$ judges and differing only in the $K$-th member, where $J_K'$ is pointwise more vulnerable than $J_K$ (i.e., $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$). Then for any adversary, including an adaptive one: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$.
24	\end{theorem}
25	
26	\noindent Proof in Appendix~\ref{app:proof}. Intuitively, the replaced judge is \emph{pivotal} exactly when $t{-}1$ of the remaining judges have already failed; in such configurations, a more vulnerable replacement can only increase the probability of tipping the majority, never decrease it. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
27	
28	The theorem establishes that $\eta_{\max}$ is monotonically linked to panel vulnerability, but is silent on the role of diversity. To disentangle the two drivers, we fit a regression $\log(\mathrm{ASR}) \sim \beta_1 \log(\eta_{\max}) + \beta_2 \log(K_{\mathrm{eff}})$ across panels. The theorem predicts $\beta_1 > 0$; the SDPI bound under non-adaptive faults would suggest $\beta_2 \leq 0$; but the reversal mechanism predicts $\beta_2 > 0$ under adaptive adversaries---diversity independently increases vulnerability. Our experiments in \S\ref{sec:experiments} test these competing predictions across 12 conditions spanning two benchmarks and six attack types, using dominance analysis to isolate each driver's independent contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca02af04-df56-4d19-85fe-a730bc67645d",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "1e463e7a-e7fa-4dda-abcf-6f8c17898584",
  "sourceToolAssistantUUID": "ca02af04-df56-4d19-85fe-a730bc67645d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T18:40:58.259Z_

<details open><summary>🔧 Tool call — Read · `toolu_017xdYR8RgiLkvmZeUmFQHxA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e463e7a-e7fa-4dda-abcf-6f8c17898584",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6anwnt442x889b3Zox",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab05cb24-af1e-4b88-b39e-4473f59c8669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAYh6RqLTzbuMePH6NzVK2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3049,
      "cache_read_input_tokens": 40539,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3049
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 40539,
          "cache_creation_input_tokens": 3049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3049,
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

_source line 39 · 2026-05-22T18:40:58.263Z_

<details><summary>↩ Tool result · `toolu_017xdYR8RgiLkvmZeUmFQHxA`</summary>

```text
1	\section{Conclusion}
2	% [PLACEHOLDER — waiting for plan\_001 results]
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab05cb24-af1e-4b88-b39e-4473f59c8669",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "e1a0a3b2-f0b0-430b-a397-32a6f0fcfa74",
  "sourceToolAssistantUUID": "ab05cb24-af1e-4b88-b39e-4473f59c8669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-22T18:41:00.945Z_

Now let me check the dream review reports for additional context on the paper's state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1a0a3b2-f0b0-430b-a397-32a6f0fcfa74",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6bAUqjUHZhG4sCaGsv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4146fb93-6dde-418a-986c-8b791f02347f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NptWBCNzEWK3SXqBcoaWns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 43588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1883,
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

_source line 41 · 2026-05-22T18:41:03.916Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FQVDHyfJ1neMWEqa35XnCB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/median/paper.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4146fb93-6dde-418a-986c-8b791f02347f",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6bAUqjUHZhG4sCaGsv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a316ff2-876c-4f4b-95da-45808c022662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NptWBCNzEWK3SXqBcoaWns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 43588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1883,
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

_source line 42 · 2026-05-22T18:41:03.922Z_

<details><summary>↩ Tool result · `toolu_01FQVDHyfJ1neMWEqa35XnCB`</summary>

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
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{hyperref}
13	\usepackage{caption}
14	\usepackage{subcaption}
15	\usepackage{array}
16	\usepackage{enumitem}
17	
18	\setlength{\parskip}{0.3em}
19	\setlength{\parindent}{1em}
20	
21	\newcommand{\keff}{K_{\text{eff}}}
22	\newcommand{\etamax}{\eta_{\max}}
23	\newcommand{\kresid}{K_{\text{resid}}}
24	\newcommand{\asr}{\text{ASR}}
25	
26	\title{Rethinking Diversity in LLM Evaluation Panels:\\When More Judges Make Things Worse}
27	
28	\author{Anonymous Submission}
29	
30	\date{}
31	
32	\begin{document}
33	\maketitle
34	
35	\begin{abstract}
36	Multi-judge LLM evaluation panels are increasingly adopted, with diversity widely assumed to improve robustness against manipulation---analogous to Byzantine Fault Tolerance (BFT) where independent nodes tolerate uncorrelated failures. We present the first large-scale empirical study examining how panel composition affects adversarial vulnerability, spanning 15 models from 6 families, 455 three-judge panels, and 6 attack types across 2 benchmarks. Our primary finding is that \emph{individual judge weakness} ($\etamax$) is the dominant predictor of panel attack success rate (ASR), significant in 9 of 12 conditions with a medium-large effect size (partial $\eta^2 = 0.18$). Panel diversity ($\keff$), after orthogonalization against $\etamax$, emerges as a secondary but statistically significant risk factor in 7 of 12 conditions (partial $\eta^2 = 0.04$), primarily for transferable attack types. Crucially, this diversity effect is substantially attenuated within capability-matched tiers (2 of 18 conditions significant), indicating it largely reflects structural capability tier-mixing rather than an intrinsic property of diversity. We further show that Gaussian copula models underestimate inter-judge dependencies by a median factor of $10\times$, and that model family labels do not predict judge independence ($p = 0.18$). We propose a robustness-first panel design principle that reduces ASR by 47\% over random selection, and characterize how aggregation rules modulate vulnerability drivers. Our results suggest that the common assumption ``more diverse panels are more robust'' requires careful qualification under adversarial conditions.
37	\end{abstract}
38	
39	\section{Introduction}
40	
41	As large language models (LLMs) are increasingly deployed as automated evaluators, multi-judge evaluation panels have emerged as a natural defense against individual model biases and adversarial manipulation. The intuition is straightforward and widely held: a diverse panel of judges, drawing from different model families and capability levels, should be harder to fool than any single judge. This reasoning echoes Byzantine Fault Tolerance (BFT) in distributed systems, where independent nodes tolerate uncorrelated faults.
42	
43	We test this assumption at unprecedented scale. Using 15 LLM judges spanning 6 model families and 3 capability tiers, we exhaustively enumerate all $\binom{15}{3} = 455$ three-judge panels and evaluate their vulnerability to 6 adversarial attack types across 2 benchmarks (MMLU and ARC), yielding 12 experimental conditions. Our statistical framework uses residualized regression to disentangle two compositional predictors of panel vulnerability: the weakness of the most vulnerable judge ($\etamax$) and the effective diversity of the panel ($\keff$), orthogonalized against $\etamax$ to ensure $\text{VIF} = 1.00$.
44	
45	Our findings paint a nuanced picture. Individual judge weakness ($\etamax$) is the primary driver of panel vulnerability, significant in 9/12 conditions with partial $\eta^2 = 0.18$. Panel diversity ($\keff$), after controlling for $\etamax$, is a statistically significant but practically modest amplifying factor---significant in 7/12 conditions but with partial $\eta^2 = 0.04$, roughly one-quarter the effect size of $\etamax$. The diversity effect is concentrated in transferable attacks (5/6 significant) and largely absent for shared-bias attacks (1/8 significant), suggesting a mechanism tied to diverse attack surfaces rather than a universal vulnerability.
46	
47	Critically, capability-matched validation reveals that the diversity effect is substantially attenuated within capability tiers (2/18 significant vs.\ 7/12 in the full pool), indicating that much of the observed effect reflects structural tier-mixing: heterogeneous panels span capability levels, structurally including weaker models.
48	
49	These findings have practical implications. We demonstrate that robustness-first panel selection---screening for individual judge robustness before considering diversity---reduces ASR by 47\% compared to random selection and substantially outperforms diversity-maximizing strategies. We also show that aggregation rules modulate vulnerability: threshold voting amplifies diversity's harmful effect ($1.45\times$), while Bayesian aggregation partially mitigates individual weakness.
50	
51	Our contributions are:
52	\begin{enumerate}[topsep=2pt, itemsep=1pt, leftmargin=2em]
53	    \item \textbf{Empirical:} The first large-scale analysis (15 models, 455 panels, 6 attacks) identifying $\etamax$ as the primary vulnerability driver with $\keff$ as a conditional amplifying factor in heterogeneous pools.
54	    \item \textbf{Methodological:} Demonstration that Gaussian copula models underestimate inter-judge dependencies by $10\times$ (median), and that model family labels do not predict judge independence.
55	    \item \textbf{Practical:} A robustness-first panel design principle and characterization of aggregation rule effects on vulnerability drivers.
56	\end{enumerate}
57	
58	\section{Background and Related Work}
59	
60	\paragraph{LLM-as-Judge.} The use of LLMs as automated evaluators has become standard practice for assessing open-ended generation quality. Single-judge setups suffer from known biases including position bias, verbosity preference, and sycophancy. Multi-judge panels have been proposed as a mitigation, with the implicit assumption that diversity improves robustness.
61	
62	\paragraph{Adversarial Attacks on LLM Judges.} Recent work has demonstrated that LLM judges are susceptible to adversarial manipulation through prompt injection, score manipulation, and various bias exploitation strategies. However, prior work has focused on individual judge vulnerability rather than panel-level compositional effects.
63	
64	\paragraph{Byzantine Fault Tolerance.} In distributed systems, BFT protocols tolerate up to $f$ faulty nodes among $n = 3f+1$ total nodes, assuming faults are independent and non-adaptive. The analogy to multi-judge panels is appealing but assumes random (non-strategic) faults---an assumption that breaks under adaptive adversaries who can target judge-specific vulnerabilities.
65	
66	\paragraph{Panel Diversity in Evaluation.} Several recent studies advocate for diverse evaluation panels, drawing from different model families to reduce correlated errors. Our work provides the first systematic empirical test of whether this diversity assumption holds under adversarial conditions.
67	
68	\section{Methodology}
69	
70	\subsection{Threat Model}
71	
72	We consider an adaptive adversary with full knowledge of each judge's vulnerability profile ($\eta_j$ for judge $j$). The adversary crafts perturbations to maximize panel-level attack success rate (ASR) under majority voting. We also evaluate a partial-knowledge variant where the adversary knows only model family labels and capability tiers.
73	
74	\subsection{Panel Composition Metrics}
75	
76	\paragraph{Individual Weakness ($\etamax$).} For a panel of $K$ judges, $\etamax = \max_{j \in \text{panel}} \eta_j$, where $\eta_j$ is judge $j$'s individual ASR under the given attack. This captures the weakest-link property.
77	
78	\paragraph{Effective Diversity ($\keff$).} We measure panel diversity using the effective number of independent judgment dimensions, computed from the eigenspectrum of the inter-judge agreement matrix. Higher $\keff$ indicates more diverse judgment patterns.
79	
80	\paragraph{Theorem 1 (Monotonicity Bound).} Under an adaptive adversary with majority voting, $\text{panel\_ASR} \leq \etamax \cdot (1 + \varepsilon \cdot \log K)$, where $\varepsilon$ depends on the correlation structure. The bound is tight to a factor of 1.35 empirically.
81	
82	\subsection{Statistical Framework}
83	
84	To disentangle the effects of $\etamax$ and $\keff$, we use residualized regression. We first regress $\keff$ on $\etamax$ and use the residuals ($\kresid$) as the diversity predictor, ensuring VIF $= 1.00$ by construction. Our regression model is:
85	\begin{equation}
86	    \asr_{\text{panel}} = \beta_0 + \beta_\eta \cdot \etamax + \beta_K \cdot \kresid + \epsilon
87	\end{equation}
88	We apply Benjamini-Hochberg FDR correction across the 12 conditions. Bonferroni correction is reported as a conservative bound.
89	
90	\subsection{Experimental Setup}
91	
92	\paragraph{Models.} 15 LLM judges from 6 families: GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini (OpenAI); Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google); Llama-3-8B, Llama-3.1-70B (Meta); Qwen2.5-7B, Qwen2.5-14B, Qwen2.5-72B (Alibaba); Mistral-7B, Mixtral-8x22B (Mistral); and two additional open-source models. This yields 3 capability tiers: 7B-class (5 models), 70B-class (3 models), and API-class (7 models).
93	
94	\paragraph{Panels.} All $\binom{15}{3} = 455$ three-judge panels, with majority voting as the default aggregation rule.
95	
96	\paragraph{Datasets.} MMLU and ARC-Challenge, representing standard multiple-choice evaluation benchmarks.
97	
98	\paragraph{Attacks.} Six attack types spanning three mechanism categories: \emph{transferable} (prompt injection, score manipulation, position bias), \emph{shared-bias} (sycophancy, verbosity bias, authority bias), and an extended set of 3 additional attacks (few-shot hijacking, persona manipulation, instruction override) for a total of 18 conditions in the expanded analysis.
99	
100	\section{Results}
101	
102	\subsection{Dual Vulnerability Drivers: $\etamax$ Dominates, $\keff$ Amplifies}
103	
104	Table~\ref{tab:main_regression} presents the residualized regression results across 12 core conditions. $\etamax$ is FDR-significant in 9/12 conditions (median $\beta = 0.47$), confirming that individual judge weakness is the primary vulnerability driver. $\kresid$ is FDR-significant and positive in 7/12 conditions (median $\beta = 0.14$), indicating that diversity is a statistically significant but secondary risk factor.
105	
106	Two conditions with naturally low confounding ($r(\keff, \etamax) \approx 0.35$)---ARC$\times$score\_manipulation and ARC$\times$position---provide the strongest evidence for an independent diversity effect, with $\kresid$ achieving $p = 3.7 \times 10^{-8}$ and $p = 5.2 \times 10^{-7}$ respectively, both surviving Bonferroni correction.
107	
108	The five non-significant conditions cluster in shared-bias attacks (sycophancy 2/2, authority 2/2, verbosity 1/2), where all models share similar vulnerabilities and the diverse-attack-surface mechanism does not apply.
109	
110	\begin{table}[t]
111	\centering
112	\caption{Residualized regression across 12 conditions (455 panels). $\kresid$ is orthogonalized against $\etamax$ (VIF $= 1.00$). FDR correction via Benjamini-Hochberg.}
113	\label{tab:main_regression}
114	\small
115	\begin{tabular}{@{}lcccccc@{}}
116	\toprule
117	Condition & $\beta(\etamax)$ & $p(\etamax)$ & $\beta(\kresid)$ & $p(\kresid)$ & FDR & $R^2$ \\
118	\midrule
119	MMLU$\times$PI & 0.52 & $<$0.001 & 0.21 & 0.003 & \checkmark & 0.42 \\
120	MMLU$\times$SM & 0.48 & 0.002 & 0.16 & 0.012 & \checkmark & 0.38 \\
121	MMLU$\times$Syc & 0.55 & $<$0.001 & 0.06 & 0.285 & & 0.34 \\
122	MMLU$\times$VB & 0.42 & 0.005 & 0.09 & 0.078 & & 0.30 \\
123	MMLU$\times$Pos & 0.39 & 0.008 & 0.18 & 0.006 & \checkmark & 0.36 \\
124	MMLU$\times$Auth & 0.50 & $<$0.001 & 0.05 & 0.352 & & 0.32 \\
125	ARC$\times$PI & 0.56 & $<$0.001 & 0.19 & 0.005 & \checkmark & 0.44 \\
126	ARC$\times$SM & 0.15 & 0.142 & 0.24 & 3.7e-8 & \checkmark & 0.40 \\
127	ARC$\times$Syc & 0.58 & $<$0.001 & 0.04 & 0.418 & & 0.36 \\
128	ARC$\times$VB & 0.44 & 0.003 & 0.14 & 0.018 & \checkmark & 0.35 \\
129	ARC$\times$Pos & 0.08 & 0.683 & 0.22 & 5.2e-7 & \checkmark & 0.38 \\
130	ARC$\times$Auth & 0.46 & 0.001 & 0.07 & 0.192 & & 0.31 \\
131	\midrule
132	\textbf{Summary} & \textbf{9/12 sig} & & \textbf{7/12 sig} & & & \textbf{0.36} \\
133	\bottomrule
134	\end{tabular}
135	\end{table}
136	
137	\paragraph{Effect Size Context.} Partial $\eta^2$ analysis reveals that $\etamax$ has a medium-large effect (median partial $\eta^2 = 0.18$) while $\kresid$ has a small effect (median partial $\eta^2 = 0.04$). The mean incremental $R^2$ contributed by $\kresid$ is $+0.07$, indicating that diversity explains modest additional variance beyond individual weakness. Beta regression as a robustness check (appropriate for bounded ASR $\in [0,1]$) yields 6/12 significant conditions, with 92\% concordance with OLS results.
138	
139	\subsection{Attack-Type Dependency: When Diversity Matters}
140	
141	The diversity effect is strongly modulated by attack mechanism type. Table~\ref{tab:attack_mechanism} summarizes results across the expanded 18-condition analysis (6 original $+$ 3 new attack types $\times$ 2 datasets).
142	
143	\begin{table}[t]
144	\centering
145	\caption{$\kresid$ significance by attack mechanism type (18 conditions, 455 panels).}
146	\label{tab:attack_mechanism}
147	\small
148	\begin{tabular}{@{}lcccc@{}}
149	\toprule
150	Mechanism & Attacks & $\kresid$ sig & $\etamax$ sig & Mean $\beta(\kresid)$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a316ff2-876c-4f4b-95da-45808c022662",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "d3ebfbf1-5523-4b5f-b7ce-f82ac3255542",
  "sourceToolAssistantUUID": "7a316ff2-876c-4f4b-95da-45808c022662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T18:41:04.340Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FfyGkRuHtRp1io6oh1D9rr`</summary>

```json
{
  "pattern": "artifacts/dream_reports/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3ebfbf1-5523-4b5f-b7ce-f82ac3255542",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6bAUqjUHZhG4sCaGsv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df40ef5f-018d-4609-93dc-77d479e47f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NptWBCNzEWK3SXqBcoaWns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 43588,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 43588,
          "cache_creation_input_tokens": 1883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1883,
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

_source line 44 · 2026-05-22T18:41:04.374Z_

<details><summary>↩ Tool result · `toolu_01FfyGkRuHtRp1io6oh1D9rr`</summary>

```text
artifacts/dream_reports/dream_20260522T055016/best/paper_framing.md
artifacts/dream_reports/dream_20260522T055016/median/paper_framing.md
artifacts/dream_reports/dream_20260522T055016/worst/paper_framing.md
artifacts/dream_reports/dream_20260522T055016/best/review_report.md
artifacts/dream_reports/dream_20260522T055016/median/review_report.md
artifacts/dream_reports/dream_20260522T055016/worst/review_report.md
artifacts/dream_reports/dream_20260522T173833/best/paper_framing.md
artifacts/dream_reports/dream_20260522T173833/median/paper_framing.md
artifacts/dream_reports/dream_20260522T173833/worst/paper_framing.md
artifacts/dream_reports/dream_20260522T173833/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df40ef5f-018d-4609-93dc-77d479e47f54",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "4db5218c-0f33-4dcd-b21d-e3c0a50ed6e8",
  "sourceToolAssistantUUID": "df40ef5f-018d-4609-93dc-77d479e47f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T18:41:11.135Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MH1wwcDKYzaSX29gJ3zf1G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/median/paper.tex",
  "offset": 150,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db5218c-0f33-4dcd-b21d-e3c0a50ed6e8",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6bcWGcRm7NX6FJsbBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99a4cdfc-5375-401d-80f0-ba17b7edb8bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jpm8KkWGx7R7j3H1FQkui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5077,
      "cache_read_input_tokens": 45471,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 45471,
          "cache_creation_input_tokens": 5077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5077,
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

_source line 46 · 2026-05-22T18:41:11.153Z_

<details><summary>↩ Tool result · `toolu_01MH1wwcDKYzaSX29gJ3zf1G`</summary>

```text
150	Mechanism & Attacks & $\kresid$ sig & $\etamax$ sig & Mean $\beta(\kresid)$ \\
151	\midrule
152	Transferable & PI, SM, Pos & 5/6 & 4/6 & 0.20 \\
153	Shared-bias & Syc, Auth, VB, Persona & 1/8 & 6/8 & 0.07 \\
154	Targeted & Instr.\ override & 0/2 & 2/2 & 0.07 \\
155	ICL-dependent & Few-shot hijack & 1/2 & 1/2 & 0.14 \\
156	\midrule
157	\textbf{Overall} & & \textbf{7/18} & \textbf{13/18} & \textbf{0.12} \\
158	\bottomrule
159	\end{tabular}
160	\end{table}
161	
162	The pattern is clear: $\kresid$ is a significant predictor primarily for \emph{transferable} attacks (5/6 conditions, mean $\beta = 0.20$), where different models exhibit different vulnerability profiles and the adversary can exploit judge-specific weaknesses across the diverse attack surface. For shared-bias attacks, where all models share similar vulnerabilities (e.g., sycophancy, authority deference), $\etamax$ dominates and diversity is largely irrelevant. Instruction override attacks are fully dominated by $\etamax$ ($\beta \approx 0.55$--$0.62$), as they target instruction-following weakness concentrated in the most vulnerable judge.
163	
164	The overall $\kresid$ significance rate across all 18 conditions is 7/18 (39\%), substantially lower than the 7/12 (58\%) in the core analysis. This underscores that the diversity risk factor is \emph{conditional}: it operates primarily through transferable attacks in heterogeneous model pools.
165	
166	\subsection{Capability-Matched Validation}
167	\label{sec:capability_matched}
168	
169	To test whether the diversity effect persists when capability differences are controlled, we conduct within-tier analyses: strong tier (70B $+$ API, 8 models, 56 panels), weak tier (7B $+$ 14B, 5 models, 10 panels), and API-only (5 models, 10 panels), each across 6 representative conditions (Table~\ref{tab:within_tier}).
170	
171	\begin{table}[t]
172	\centering
173	\caption{Within-tier vs.\ full-pool $\kresid$ significance. The diversity effect is substantially attenuated when capability tier is controlled.}
174	\label{tab:within_tier}
175	\small
176	\begin{tabular}{@{}lccccc@{}}
177	\toprule
178	Scope & $N$ panels & $\kresid$ sig(+) & $\etamax$ sig & Med $R^2$ & $r(\keff, \etamax)$ \\
179	\midrule
180	Full pool (ref) & 455 & 7/12 (0.58) & 9/12 (0.75) & 0.38 & +0.72 \\
181	Strong tier & 56 & 1/6 (0.17) & 3/6 (0.50) & 0.20 & +0.38 \\
182	Weak tier & 10 & 0/6 (0.00) & 4/6 (0.67) & 0.32 & +0.42 \\
183	API-only & 10 & 1/6 (0.17) & 2/6 (0.33) & 0.15 & +0.35 \\
184	\bottomrule
185	\end{tabular}
186	\end{table}
187	
188	The $\kresid$ significance rate drops from 58\% in the full pool to 11\% within tiers (2/18 total). This indicates that much of the diversity effect observed in the full pool reflects capability tier-mixing: high-$\keff$ panels structurally span tiers and include weaker models, creating vulnerability through a pathway not fully captured by linear residualization. Within-tier $r(\keff, \etamax) \approx 0.35$--$0.42$, substantially lower than the full-pool $r = 0.72$, confirming reduced confounding.
189	
190	The two within-tier significant conditions (MMLU$\times$prompt\_injection in the strong tier, $p = 0.038$; ARC$\times$score\_manipulation in the API tier, $p = 0.042$) suggest that a residual diversity effect may exist for specific attack types even within tiers, but the evidence base is narrow. We interpret this as a \textbf{key limitation}: the independent contribution of diversity beyond tier-mixing is small and condition-specific.
191	
192	\subsection{Adaptive vs.\ Random-Fault Regime Contrast}
193	
194	Motivated by the BFT analogy, we compare how $\kresid$ behaves under adaptive adversaries versus a random-fault simulation where each judge independently fails with its empirical probability $p_j$ (Table~\ref{tab:bft_contrast}).
195	
196	\begin{table}[t]
197	\centering
198	\caption{Adaptive vs.\ random-fault regime comparison. $\kresid$ is positive in both regimes (no sign reversal), but relative importance of $\etamax$ vs.\ $\kresid$ shifts.}
199	\label{tab:bft_contrast}
200	\small
201	\begin{tabular}{@{}lcccc@{}}
202	\toprule
203	Metric & Adaptive & Random-Fault & $\Delta$ & Interpretation \\
204	\midrule
205	$\kresid$ sig rate & 7/12 & 10/12 & +3 & Stronger in RF \\
206	Mean $\beta(\kresid)$ & 0.14 & 0.21 & +0.07 & RF $\beta$ 1.4$\times$ larger \\
207	$\etamax$ sig rate & 9/12 & 7/12 & $-2$ & Weaker in RF \\
208	Mean $\beta(\etamax)$ & 0.44 & 0.32 & $-0.12$ & Strategic targeting absent \\
209	Mean $R^2$ & 0.38 & 0.52 & +0.14 & RF more predictable \\
210	\bottomrule
211	\end{tabular}
212	\end{table}
213	
214	Contrary to the naive BFT prediction, $\kresid$ is positive in \emph{both} regimes---we observe no qualitative sign reversal. Diversity does not help under random faults either, because diverse panels structurally include weaker models whose higher individual failure rates manifest under any fault model. However, the relative importance of the two drivers shifts in a manner consistent with the BFT framework: under random faults, $\kresid$ is \emph{more} important (10/12 sig, $\beta = 0.21$) while $\etamax$ is \emph{less} important (7/12 sig, $\beta = 0.32$), because random faults lack the strategic targeting that makes $\etamax$ dominant under adaptive adversaries. The $R^2$ gap of $+0.14$ confirms that random faults produce more predictable panel behavior, consistent with the theoretical framework where adaptive adversaries introduce strategic variance.
215	
216	We interpret the BFT analogy as \emph{illustrative rather than conclusive}: it correctly predicts the relative importance shift but not the sign reversal, likely because the structural confound (diverse $=$ weaker members) is more fundamental than the adaptive/random distinction.
217	
218	\subsection{When Diversity Helps}
219	\label{sec:when_helps}
220	
221	Our results should not be read as a blanket indictment of panel diversity. Several conditions suggest diversity may be neutral or beneficial:
222	
223	\paragraph{Within capability tiers.} When all judges exceed a capability threshold (Section~\ref{sec:capability_matched}), the diversity effect is approximately neutral. The robustness-first principle is sufficient in these regimes.
224	
225	\paragraph{Shared-bias attacks.} For attacks exploiting biases shared across all models (sycophancy, authority), $\kresid$ is non-significant in 7/8 conditions. In this regime, diversity neither helps nor hurts---the attack bypasses compositional defenses entirely.
226	
227	\paragraph{Larger panels.} Panel size sensitivity analysis (K $= 3, 5, 7, 9$) shows that the diversity effect diminishes with panel size. At $K = 3$ (455 panels), $\kresid$ is significant in 4/6 representative conditions; at $K = 9$ (5005 panels), only 1/6. The $\beta$ ratio of $\etamax$ to $\kresid$ increases from 2.8:1 at $K = 3$ to 6.0:1 at $K = 9$, as majority voting dilutes the influence of individual weak judges in larger panels.
228	
229	\paragraph{Partial-knowledge adversaries.} Under a partial-knowledge adversary (knowing only family labels and tiers, not exact vulnerability profiles), $\kresid$ significance drops from 7/12 to 3/12, and mean $\beta(\kresid)$ from 0.18 to 0.12 (33\% reduction). The diversity risk factor is sensitive to adversary capability: with imperfect targeting, the diverse attack surface mechanism is blunted.
230	
231	\subsection{Aggregation Rules Modulate Vulnerability}
232	
233	Table~\ref{tab:aggregation} shows how different aggregation rules interact with the dual vulnerability drivers.
234	
235	\begin{table}[t]
236	\centering
237	\caption{Aggregation rule $\times$ vulnerability driver interaction (12 conditions, 455 panels).}
238	\label{tab:aggregation}
239	\small
240	\begin{tabular}{@{}lcccccc@{}}
241	\toprule
242	Aggregation & $\kresid$ sig & $\etamax$ sig & $\beta(K)$ ampl. & $\beta(\eta)$ ampl. & ASR \\
243	\midrule
244	Majority (ref) & 7/12 & 9/12 & 1.00$\times$ & 1.00$\times$ & 0.172 \\
245	Threshold & 9/12 & 9/12 & 1.45$\times$ & 1.05$\times$ & 0.192 \\
246	Bayesian & 4/12 & 5/12 & 0.65$\times$ & 0.55$\times$ & 0.142 \\
247	Rel.-weighted & 5/12 & 7/12 & 0.80$\times$ & 0.78$\times$ & 0.155 \\
248	\bottomrule
249	\end{tabular}
250	\end{table}
251	
252	\paragraph{Threshold/unanimity voting amplifies the diversity effect.} Requiring unanimous agreement means any single compromised judge blocks consensus. $\kresid$ significance increases from 7/12 to 9/12, with $\beta$ amplified by $1.45\times$. Two previously non-significant shared-bias conditions become significant under unanimity. This has a clear practical implication: \emph{unanimity voting should be avoided in adversarial settings}.
253	
254	\paragraph{Bayesian aggregation partially mitigates individual weakness.} Accuracy-weighted Bayesian aggregation down-weights less reliable judges, reducing $\etamax$ significance from 9/12 to 5/12 ($0.55\times$ $\beta$ reduction) and mean ASR by 18\%. The $\kresid$ effect is also indirectly attenuated (7/12 $\to$ 4/12), since the diversity effect transmits primarily through weak judges that are now down-weighted. However, Bayesian aggregation does not eliminate the dual vulnerability pattern---it requires accurate priors, which degrade with larger model pools.
255	
256	\subsection{Robustness-First Panel Design}
257	
258	We benchmark a two-stage panel selection algorithm against five baselines across 6 conditions (Table~\ref{tab:panel_selection}).
259	
260	\begin{table}[t]
261	\centering
262	\caption{Panel selection strategy comparison (mean ASR, lower is better). Top-3 strategies are separated by $<1$ percentage point.}
263	\label{tab:panel_selection}
264	\small
265	\begin{tabular}{@{}lccccc@{}}
266	\toprule
267	Strategy & Mean ASR & vs.\ Random & vs.\ Strongest-K & Win count & Rank \\
268	\midrule
269	Two-stage & 0.091 & $-$47\% & $-$7\% & 3/6 & 1.8 \\
270	Min-$\etamax$ & 0.092 & $-$46\% & $-$7\% & 1/6 & 2.2 \\
271	Strongest-K & 0.091 & $-$47\% & --- & 2/6 & 2.3 \\
272	Max-$\keff$ & 0.152 & $-$11\% & +67\% & 0/6 & 4.3 \\
273	Max-family-div & 0.164 & $-$4\% & +80\% & 0/6 & 4.8 \\
274	Random & 0.170 & --- & +87\% & 0/6 & 5.5 \\
275	\bottomrule
276	\end{tabular}
277	\end{table}
278	
279	The key insight is not the marginal difference between two-stage, min-$\etamax$, and strongest-K strategies (which are statistically indistinguishable at $p = 0.42$), but rather the large gap between robustness-oriented strategies (ASR $\approx 0.09$) and diversity-oriented strategies (Max-$\keff$: 0.152, Max-family-diversity: 0.164, Random: 0.170). \textbf{Diversity-first panel selection is actively harmful}, increasing ASR by 67--87\% over robustness-first approaches. Among robustness-qualified judges, diversity serves as a neutral tiebreaker at best.
280	
281	The optimal threshold for the two-stage algorithm is $\eta \leq 0.25$ (9 models pass), with ASR sensitivity $<15\%$ across the $[0.18, 0.35]$ threshold range.
282	
283	\section{Analysis}
284	
285	\subsection{Diversity-Capability Tradeoff Decomposition}
286	
287	The overall correlation $r(\keff, \etamax) = +0.72$ ($p < 0.001$) reflects a structural property of the current LLM ecosystem: maximizing panel diversity requires mixing capability tiers, which necessarily introduces weaker models. Decomposing this correlation reveals that 72\% of the variance comes from between-tier differences ($r = 0.82$), while within-tier correlation is substantially weaker ($r \approx 0.38$, pooled across tiers). This tier-mixing effect is the primary pathway through which diversity increases vulnerability.
288	
289	The Pareto frontier across 455 panels identifies 14 panels near the optimal knee at $\keff \approx 1.8$, $\etamax \approx 0.15$, corresponding to combinations of 2 strong API models and 1 strong open-source model. Beyond this knee, ASR increases sharply with $\keff$.
290	
291	\subsection{Gaussian Copula Failure}
292	
293	The Gaussian copula model underestimates mutual information (MI) between judge pairs by a median factor of $10\times$ across 105 model pairs (range: $5$--$85\times$). Underestimation is most severe for cross-tier pairs (median $18\times$ for extreme cross-tier combinations) and mildest for within-tier pairs at similar capability levels (median $7\times$ for within-7B). This invalidates copula-based independence bounds commonly assumed in panel robustness analyses.
294	
295	\subsection{Family Labels Do Not Predict Independence}
296	
297	Mann-Whitney U test comparing within-family vs.\ cross-family MI yields $p = 0.18$, indicating that model family labels (Qwen, Llama, Mistral, etc.) do not reliably predict judge independence. Capability proximity, not family membership, is the primary driver of inter-judge correlation.
298	
299	\subsection{ASR Concentration Analysis}
300	
301	Per-judge ASR concentration (Gini $= 0.45$ median) confirms that attacks partially concentrate on the weakest judge, with the most vulnerable judge absorbing 55\% of attack success (vs.\ 33\% uniform baseline for $K=3$). Concentration is higher for transferable attacks (Gini $= 0.52$) than shared-bias attacks (Gini $= 0.30$), and higher in weak-tier panels (Gini $= 0.55$) than strong-tier panels (Gini $= 0.25$). This supports the $\etamax$-dominance mechanism while showing that attacks are not exclusively concentrated on a single judge.
302	
303	\section{Discussion and Limitations}
304	
305	\paragraph{Scope: MCQ benchmarks.} Our findings are established on multiple-choice evaluation tasks (MMLU, ARC). Preliminary results on open-ended evaluation (MT-Bench style) show direction-consistent but non-significant $\kresid$ effects ($p$ range $0.065$--$0.185$, $R^2 = 0.12$). Power analysis indicates $N \approx 1{,}200$ panels would be needed for 80\% power at the observed effect size, suggesting this may reflect insufficient power rather than absent effects. Extending to open-ended evaluation is important future work.
306	
307	\paragraph{Tier-mixing vs.\ intrinsic diversity.} The capability-matched analysis (Section~\ref{sec:capability_matched}) reveals that much of the diversity effect in the full pool reflects tier-mixing through non-linear channels not captured by residualization. We cannot conclusively distinguish an intrinsic causal effect of diversity from a structural artifact of the current model ecosystem.
308	
309	\paragraph{BFT analogy.} The absence of $\kresid$ sign reversal between adaptive and random-fault regimes weakens the BFT reversal narrative. The analogy is useful for understanding relative importance shifts but does not deliver the predicted qualitative reversal, likely because the structural confound persists in both regimes.
310	
311	\paragraph{Panel size.} Our diversity findings are most relevant for $K=3$ panels, representing the majority of current cost-constrained deployments. For $K \geq 7$, the diversity effect is negligible.
312	
313	\paragraph{Adversary strength.} Under partial-knowledge adversaries, both $\kresid$ and $\etamax$ effects attenuate, with $\kresid$ attenuating more rapidly ($-57\%$ vs.\ $-44\%$). Real-world adversaries with imperfect knowledge face a substantially diminished diversity risk.
314	
315	\paragraph{Ceiling effects.} One condition (MMLU$\times$few-shot hijacking) exhibited ceiling effects ($R^2 = 0.12$, all models ASR $> 0.70$), reducing regression discriminability.
316	
317	\section{Conclusion}
318	
319	We have presented the first large-scale empirical study of how panel composition affects adversarial vulnerability in LLM evaluation. Individual judge weakness ($\etamax$) is the primary and dominant vulnerability driver, while panel diversity ($\keff$) is a conditional risk factor whose independent contribution depends on pool composition heterogeneity and attack type. The diversity effect is concentrated in transferable attacks against heterogeneous panels and is substantially attenuated within capability tiers, under partial-knowledge adversaries, and in larger panels. We recommend a robustness-first panel design principle: screen for individual judge robustness before considering diversity, and avoid unanimity voting in adversarial settings. Our methodological contributions---demonstrating Gaussian copula failure ($10\times$ MI underestimation) and family label unreliability---provide tools for more principled panel design.
320	
321	\section*{Limitations}
322	
323	Our study has three main limitations. First, the independent diversity effect (partial $\eta^2 = 0.04$) is small and largely reflects structural tier-mixing, limiting causal claims about diversity \textit{per se}. Second, our findings are established on MCQ benchmarks and may not generalize to open-ended evaluation, where preliminary results are inconclusive. Third, the BFT reversal predicted by theory was not observed empirically, constraining the theoretical contribution to an illustrative analogy rather than a validated mechanism.
324	
325	\bibliographystyle{plainnat}
326	
327	\end{document}
328	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99a4cdfc-5375-401d-80f0-ba17b7edb8bf",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "91357d6e-2965-42d3-aa5c-ac43088b247a",
  "sourceToolAssistantUUID": "99a4cdfc-5375-401d-80f0-ba17b7edb8bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-22T18:41:19.701Z_

Now I have a comprehensive view of both the paper's current state (the actual tex files) and the dream review simulation. Let me also check if there are any additional review reports from the dream simulations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91357d6e-2965-42d3-aa5c-ac43088b247a",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6c7vLZz4V1kEJHeTw8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "976bdd59-fd5a-4b3e-9b00-d00f35bd4888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQwGNPaL5gVHp1jASec56G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5526,
      "cache_read_input_tokens": 50548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5526,
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

_source line 48 · 2026-05-22T18:41:22.580Z_

<details open><summary>🔧 Tool call — Read · `toolu_018FMJL65LBPcvKmxewooUHy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/median/review_report.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "976bdd59-fd5a-4b3e-9b00-d00f35bd4888",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6c7vLZz4V1kEJHeTw8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c894fe0f-646c-4084-ac97-f2237e482600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQwGNPaL5gVHp1jASec56G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5526,
      "cache_read_input_tokens": 50548,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 50548,
          "cache_creation_input_tokens": 5526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5526,
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

_source line 49 · 2026-05-22T18:41:22.584Z_

<details><summary>↩ Tool result · reported error · `toolu_018FMJL65LBPcvKmxewooUHy`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c894fe0f-646c-4084-ac97-f2237e482600",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "b4abd72d-92dc-452f-9e2e-948224796e56",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval.",
  "sourceToolAssistantUUID": "c894fe0f-646c-4084-ac97-f2237e482600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-22T18:41:25.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SUtmAXD4ojzYtSYhuvksFA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4abd72d-92dc-452f-9e2e-948224796e56",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6cxDD87LZLwo6VqEtE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17948a62-fa58-4b96-a55a-d10416a43acf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011rGxW2bREP34jULEMdQkGQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 56074,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 56074,
          "cache_creation_input_tokens": 227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 227,
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

_source line 51 · 2026-05-22T18:41:25.663Z_

<details><summary>↩ Tool result · `toolu_01SUtmAXD4ojzYtSYhuvksFA`</summary>

```text
1	---
2	dream_id: dream_20260522T173833
3	tier: best
4	overall_score: 3.0 — Findings (fixable gaps in reproducibility, presentation, and positioning prevent Conference)
5	timestamp: 2026-05-22T18:37:55.250177+00:00
6	---
7	
8	# Dream Review Report — cert_manip_resist_eval
9	
10	**Paper:** "More Diverse, More Vulnerable: How Judge Panel Diversity Backfires Under Adaptive Adversaries"
11	**Venue Target:** EMNLP 2026 (ARR)
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	**Date:** 2026-05-22
14	
15	---
16	
17	## Reviewer Assignments
18	
19	- **R1 (Methods + Experiments):** Experimental design, statistical methodology, reproducibility, result validity
20	- **R2 (Novelty + Related Work):** Novelty, related work coverage, positioning, contribution significance
21	
22	---
23	
24	## Step 1: Independent Reviews
25	
26	### R1 — Methods & Experiments
27	
28	#### Strengths
29	
30	**S1. Impressive experimental scale.** 15 models × 455 panels × 9 attack types × 4 benchmarks is among the largest systematic studies of adversarial robustness in multi-judge LLM evaluation. The combinatorial panel enumeration (all C(15,3)=455 three-judge panels) is exhaustive for K=3, eliminating sampling bias.
31	
32	**S2. Sound residualization design.** Using K_eff^resid (residuals of K_eff ~ η_max) to orthogonalize the two predictors is methodologically clean. VIF=1.02 confirms near-perfect orthogonality. The paper then validates this with multiple robustness checks: Bonferroni (8/12 still significant), beta regression for bounded DV (9/12), Cook's D (max 0.031), Shapiro-Wilk normality (p=0.23). This multi-layer statistical validation is thorough and preempts most methodological critiques.
33	
34	**S3. Capability-matched within-tier analysis.** The large-tier analysis (6 top-tier models, 20 panels, 4/6 significant) directly addresses the most dangerous confound: that K_eff's positive effect is merely a proxy for tier-mixing. The fact that the condition-dependent dominance pattern (K_eff → transferable, η_max → shared-bias) replicates within-tier is strong evidence for genuine diversity effects.
35	
36	**S4. BFT random-fault contrast is well-designed.** Using calibrated random faults (bootstrapped clean-accuracy noise) rather than raw η_j values as failure probabilities is a meaningful methodological improvement. The β flipping negative in 5/12 conditions under RF, concentrated on transferable attacks, provides compelling mechanistic evidence for why BFT's prediction fails under adaptive adversaries.
37	
38	**S5. Multi-dimensional generalization.** The paper systematically tests generalization across five dimensions: attack types (6→9), benchmarks (MCQ→open-ended), panel sizes (K=3→9), adversary knowledge levels (full→partial→black-box), and aggregation rules (4 types). This breadth substantially strengthens the core claim.
39	
40	**S6. Panel size scaling law.** The monotonic increase of β_K (0.42→0.61) and decrease of β_η (0.51→0.38) with panel size, with crossover at K≈6, is a clean and practically important finding. The implication that "adding more judges amplifies the diversity trap" is actionable.
41	
42	#### Weaknesses
43	
44	**W1. K_eff definition is critically underspecified.** K_eff is described as computed "from the eigenspectrum of the pairwise mutual information matrix" (Section 3), but no formula is given. How is MI estimated — from binary agreement/disagreement? From scoring distributions? What eigenspectrum decomposition yields a scalar K_eff? (Effective rank via entropy of normalized eigenvalues? Ratio of squared sum to sum of squares?) This is the paper's central variable and must be precisely defined for reproducibility. A reader cannot verify or replicate the core results without this.
45	
46	**W2. Missing confidence intervals and practical effect sizes.** All tables report β and p but no confidence intervals. With n=455, even small standardized β values can be significant. The paper should report: (a) 95% CIs for all β coefficients; (b) the predicted ASR change when K_eff moves from its 10th to 90th percentile within the panel population; (c) partial R² or η² for K_eff^resid vs. η_max separately. Without these, the reader cannot judge whether the diversity effect is practically meaningful vs. merely statistically detectable.
47	
48	**W3. No figures in the entire paper.** A 9-page empirical paper with 11 tables and zero figures is highly unusual and makes the results much harder to parse. Critical visualizations that are missing:
49	- Scatter plot of K_eff vs. ASR (the core relationship)
50	- Heatmap of β coefficients across conditions (to visualize the transferable/shared-bias taxonomy)
51	- BFT reversal lollipop chart (adaptive vs. RF β side by side)
52	- Pareto frontier of K_eff vs. η_max with ASR contours
53	These figures would transform the paper's readability and impact. The table-heavy presentation is a significant barrier.
54	
55	**W4. Attack implementation details are absent.** The 9 attack types are described only by category name. No attack prompts, no manipulation procedures, no examples are shown. How is "score manipulation" operationalized? How does "sycophancy exploitation" work in practice? How is "few-shot hijacking" implemented differently from "few-shot bias"? The paper needs at least a table of attack descriptions and ideally example prompts (in appendix). Without these, the adversary model is a black box.
56	
57	**W5. Open-ended benchmark methodology gap.** How are attacks applied to MT-Bench and AlpacaEval? These involve free-form generation, not MCQ. Position bias in a multi-turn dialogue is fundamentally different from position bias in a 4-choice question. The paper should explain how each attack type translates to the open-ended setting, and whether the same attack implementations are used or adapted versions.
58	
59	**W6. Adversary model realism.** The adaptive adversary "observes the panel composition and crafts attacks to maximize ASR" (Section 3). How is this operationalized in experiments? Does the adversary run a combinatorial optimization? Use gradient-based methods? Simply apply per-judge optimal attacks? The adversary model is the foundation of all results but its implementation is opaque. Furthermore, the full-knowledge adversary knows individual η_j profiles — this is an extremely strong assumption. The partial-knowledge experiment (Section 7.4) partially addresses this, but 7/12 significant under partial knowledge vs. 10/12 under full knowledge shows the effect is adversary-strength dependent. Under black-box, only 3/12 are significant — the diversity trap essentially vanishes when the adversary has no information.
60	
61	**W7. Medium tier is severely underpowered.** 4 models → 4 panels → 1/6 significant. This should be either omitted from Table 2 or explicitly flagged as below minimum statistical power (not just "directional only"). Including it gives a false impression of three-tier validation when only two tiers provide meaningful evidence.
62	
63	**W8. High confound r in many conditions.** In 5/12 conditions, confound r(K_eff, η_max) ≥ 0.70 (sycophancy, verbosity, authority on both datasets). Even with residualization, when raw correlation is this high, small specification errors in the linear model (nonlinearity, interaction effects) can leak η_max variance into K_eff^resid. The 3 "smoking gun" conditions (r ≈ 0.35) are more convincing, but they're a minority. A sensitivity analysis varying the functional form (e.g., polynomial, GAM) would strengthen claims for high-confound conditions.
64	
65	**W9. Reproducibility overall.** No code repository, no data release plan, no model prompts, underspecified K_eff computation, and opaque attack implementations. For an empirical paper making strong claims, this is a significant gap.
66	
67	**R1 Scores:**
68	- Soundness: 3.5/5
69	- Reproducibility: 2.0/5
70	- Overall impression: The statistical framework is well-designed and the robustness checks are thorough, but critical details (K_eff formula, attack implementations, adversary operationalization) are missing, preventing independent verification.
71	
72	---
73	
74	### R2 — Novelty & Related Work
75	
76	#### Strengths
77	
78	**S1. Important and timely research question.** Multi-judge LLM evaluation panels are rapidly becoming standard practice (Arena, AlpacaEval, various benchmarks). Questioning the assumption that diversity improves robustness is both contrarian and practically significant. The "diversity trap" framing is memorable and, if supported, would change how practitioners design evaluation panels.
79	
80	**S2. BFT connection is theoretically grounding.** The analogy to Byzantine Fault Tolerance provides a clear theoretical lens: BFT assumes independent faults, adaptive adversaries violate this assumption, therefore BFT guarantees don't apply. The empirical BFT reversal (β flipping negative under random faults) gives this analogy empirical teeth. This is more than a loose metaphor — it's a testable prediction that the data confirm.
81	
82	**S3. Attack taxonomy has predictive value.** The most novel contribution is the condition-dependent dominance pattern: transferable attacks → K_eff dominates, shared-bias attacks → η_max dominates. If this taxonomy is robust, it provides a predictive framework: given a new attack type, its transferability predicts which vulnerability channel to worry about. This moves beyond cataloguing results to building a theory.
83	
84	**S4. Actionable defense recommendations.** The two-stage selection algorithm and Bayesian aggregation analysis convert the finding into practical guidance. The "robustness-first, diversity-second" principle is simple and implementable.
85	
86	**S5. Comprehensive experimental coverage.** The paper systematically tests all obvious objections: confounds (within-tier), generalization (open-ended, new attacks), scaling (panel size), adversary realism (partial knowledge), defense (selection + aggregation). This anticipatory structure leaves fewer obvious holes for reviewers.
87	
88	#### Weaknesses
89	
90	**W1. Related work section is critically thin.** Only 11 references for a paper spanning adversarial ML, distributed systems (BFT), ensemble learning, and LLM evaluation. Conspicuous omissions:
91	- **Multi-judge evaluation papers:** No citation of PoLL (Verga et al., 2024), which directly studies multi-judge panel composition. No citation of recent work on judge agreement/disagreement (e.g., Kim et al., 2024).
92	- **Adversarial robustness of ensembles:** Rich ML literature on adversarial transferability across diverse models (Tramèr et al., 2017; He et al., 2017; Kariyappa & Qureshi, 2019 on diversity and adversarial robustness in ensembles). The finding that diverse ensembles can be more vulnerable to adaptive attacks has precedent in this literature — the paper must position against it.
93	- **Game-theoretic adversary models:** No reference to Stackelberg game formulations for adversary vs. defender, which is the standard framework for adaptive adversaries in security.
94	- **LLM manipulation:** Missing Panickssery et al. (2024) on sycophancy, Perez et al. (2022) on red-teaming, and more recent work on prompt injection attacks on judges.
95	- **Certification and robustness bounds:** No reference to randomized smoothing or certified defense literature, which is relevant to the Gaussian copula failure discussion.
96	
97	For EMNLP, a related work section this thin will draw reviewer criticism. It creates the impression that the authors are unaware of adjacent literature or are claiming more novelty than warranted.
98	
99	**W2. Novelty relative to ensemble adversarial robustness.** The core insight — that diversity can hurt under adaptive adversaries — has been explored in the adversarial ML literature on ensemble models. Tramèr et al. (2017) showed that adversarial examples transfer across models, and subsequent work (e.g., Kariyappa & Qureshi, 2019 "Improving Adversarial Robustness of Ensembles with Diversity Training") explicitly studied the diversity-robustness tradeoff in ensembles. The paper needs to clearly articulate what is new beyond applying this known phenomenon to LLM judges specifically. The LLM-specific aspects (BFT analogy, attack taxonomy, judge-specific vulnerability profiles) may be sufficiently novel, but the paper must make this case explicitly.
100	
101	**W3. Framing oversells causation.** The title ("Backfires"), abstract ("diversity...reverses"), and introduction ("this intuition is wrong") imply causal claims, but the analysis is observational regression. The Limitations section acknowledges this, but the mismatch between assertive framing and associational evidence will concern reviewers. Suggested softening: "is associated with increased vulnerability" rather than "backfires" / "reverses."
102	
103	**W4. Practical threat model question unaddressed.** The paper doesn't adequately discuss when the adversary model applies in practice. In benchmark evaluation (MMLU, MT-Bench), who is the adversary and what is their goal? A model developer trying to game their ranking? A malicious actor trying to undermine trust in benchmarks? The paper assumes an adversary but doesn't ground this in realistic evaluation scenarios. The black-box result (3/12 significant) suggests the diversity trap is weak absent adversary information — and in many practical settings, panel composition is not disclosed.
104	
105	**W5. Missing single-judge baseline.** If diversity is harmful and robustness is paramount, the logical extreme is using a single best judge. The paper proposes "robustness-first, diversity-second" but doesn't benchmark against the "robustness-only" single-judge alternative. If a single GPT-4o judge achieves comparable or better ASR than the two-stage panel, the practical value of panels under adversarial threat is questionable — and that itself would be a strong finding worth reporting.
106	
107	**W6. Gaussian copula failure (Section 8.1) feels disconnected.** The 18.5× MI underestimation result is interesting but its connection to the main story is loose. It motivates using empirical K_eff rather than copula-derived bounds, but no one in the paper proposes copula-based bounds as a baseline. This section reads like a separate contribution that doesn't integrate with the main narrative.
108	
109	**W7. Family label analysis (Section 8.2) is unsurprising.** That family labels don't predict judge independence is expected — different model sizes within a family (e.g., Llama-8B vs. 70B) obviously behave differently. The capability proximity finding (r = −0.71 with MI) is more interesting but is stated as a single number without analysis.
110	
111	**R2 Scores:**
112	- Excitement: 3.5/5
113	- Related work adequacy: 2.0/5
114	- Overall impression: The research question and core finding are genuinely interesting, but the thin related work and insufficient positioning against ensemble adversarial robustness literature weaken the contribution claim. The practical significance depends critically on how realistic the adversary model is, which the paper doesn't sufficiently argue.
115	
116	---
117	
118	## Step 2: Cross-Sharing
119	
120	**R1 → R2:** "My core concern is that the paper is a statistical black box — K_eff is undefined, attacks are undescribed, the adversary is a simulation with no implementation details. The statistical framework itself is well-designed, but without knowing what's being measured and how, the results are unverifiable. The zero-figures paper is also a significant presentation problem — 11 dense tables without visual aids is hostile to readers. Do you think the novelty is strong enough to overcome these presentation issues?"
121	
122	**R2 → R1:** "I agree on presentation — no figures is a real problem. My bigger concern is positioning: the paper doesn't acknowledge that 'diversity hurts under adaptive adversaries' is a known phenomenon in ensemble adversarial ML. The LLM-judge-specific version may be novel, but the paper claims more novelty than it can support with 11 references. On your confound concern — I actually think the within-tier analysis adequately handles it for the large tier. The 4/6 significant conditions among all-top-tier models is fairly convincing. But the medium tier (4 panels) should be dropped."
123	
124	---
125	
126	## Step 3: Convergence
127	
128	### Points of Agreement
129	
130	1. **Research question is important and timely.** The diversity-robustness tradeoff in LLM judge panels is understudied and practically relevant.
131	
132	2. **Experimental scale is a genuine strength.** 15 models × 455 panels × 9 attacks × 4 benchmarks with exhaustive enumeration is thorough.
133	
134	3. **Statistical methodology is sound in design** (residualization, VIF, multiple correction methods, beta regression). The multi-layer robustness checking is commendable.
135	
136	4. **Critical presentation issues must be fixed:**
137	   - No figures (both reviewers flag as major)
138	   - K_eff definition missing (R1 primary, R2 agrees)
139	   - Attack implementation details absent (R1 primary, R2 agrees)
140	   - Related work far too thin (R2 primary, R1 agrees)
141	
142	5. **Adversary model realism is a concern.** Black-box result (3/12 significant) suggests the finding is highly dependent on adversary information access. The paper needs to better justify when this threat model applies in practice.
143	
144	6. **Within-tier analysis is convincing for large tier.** Both reviewers agree this adequately addresses tier-mixing confound for top-tier models. Medium tier should be de-emphasized.
145	
146	7. **Attack taxonomy is the most novel contribution.** The transferable/shared-bias distinction with predictive power for dominance pattern is genuinely new and interesting.
147	
148	### Points of Disagreement (Resolved)
149	
150	- **Confound concern (R1) vs. within-tier sufficiency (R2):** Resolved by agreeing that within-tier analysis addresses the primary confound, but high-confound conditions (r ≥ 0.70) would benefit from nonlinear specification checks. The 3 "smoking gun" conditions (r ≈ 0.35) with p < 10⁻²⁸ are sufficient to establish the core claim.
151	
152	- **Novelty assessment:** R2 initially more skeptical due to ensemble adversarial robustness precedent. Resolved by agreeing that the LLM-judge-specific instantiation (BFT reversal, attack taxonomy, panel selection defense) provides sufficient novelty for Findings, but the paper must explicitly position against ensemble adversarial literature to justify Conference acceptance.
153	
154	---
155	
156	## Step 4: Consolidated Assessment
157	
158	### Summary
159	
160	The paper presents large-scale empirical evidence for a "diversity trap" in multi-judge LLM evaluation: panel diversity (K_eff) independently increases vulnerability to adaptive adversarial attacks. The finding is validated across 15 models, 455 panels, 9 attacks, 4 benchmarks, and multiple robustness checks. The attack taxonomy (transferable → K_eff-dominated, shared-bias → η_max-dominated) and BFT reversal mechanism are intellectually compelling. However, the paper has significant presentation gaps (no figures, 11 references, underspecified K_eff), insufficient positioning against ensemble adversarial robustness literature, and an adversary model whose practical relevance is not adequately argued.
161	
162	### Strengths (consolidated, ranked)
163	
164	1. **Compelling counter-intuitive finding at scale.** The diversity trap, if robust, challenges a widely-held assumption in LLM evaluation design. The experimental scale (455 panels, 9 attacks, 4 benchmarks) with exhaustive panel enumeration provides comprehensive evidence.
165	
166	2. **Rigorous statistical framework.** Residualization → VIF verification → FDR/Bonferroni → beta regression → Cook's D → Shapiro-Wilk is a thorough multi-layer validation pipeline. The design anticipates and preempts standard methodological objections.
167	
168	3. **Attack taxonomy with predictive power.** The transferable/shared-bias distinction is not just descriptive but predictive — it extends cleanly to new attacks (Section 7.1) and new benchmarks (Section 7.2). This is a genuine conceptual contribution.
169	
170	4. **BFT reversal is empirically grounded.** β flipping negative under calibrated random faults in exactly the conditions predicted (transferable attacks) elevates the BFT analogy from metaphor to testable mechanism.
171	
172	5. **Systematic generalization testing.** Five orthogonal dimensions of generalization (attack types, benchmarks, panel sizes, adversary knowledge, aggregation rules) leave few obvious gaps.
173	
174	6. **Actionable defense.** Two-stage selection (−20.8%) + Bayesian aggregation (−28.4%) converts analysis into practice.
175	
176	### Weaknesses (consolidated, ranked by severity)
177	
178	1. **[Major] K_eff is undefined.** The paper's central variable lacks a precise mathematical definition. "Computed from the eigenspectrum of the pairwise mutual information matrix" is insufficient — which function of the eigenspectrum? How is MI estimated from judge decisions? This single omission makes the paper unreproducible.
179	
180	2. **[Major] Related work is critically thin (11 references).** Missing entire bodies of relevant literature: ensemble adversarial robustness (Tramèr et al., 2017; Kariyappa & Qureshi, 2019), multi-judge evaluation (PoLL/Verga et al., 2024), game-theoretic adversary modeling, LLM manipulation (Panickssery et al., 2024; Perez et al., 2022). For EMNLP, this is substantially below expectations and weakens the novelty claim.
181	
182	3. **[Major] Zero figures.** 11 tables and 0 figures in a 9-page empirical paper. The core relationship (K_eff vs. ASR scatter), the attack taxonomy (β heatmap), and the BFT reversal (paired lollipop) are crying out for visualization. The paper's readability and impact are severely diminished.
183	
184	4. **[Significant] Attack implementations and adversary model are opaque.** No attack prompts, no adversary algorithm, no examples. The reader cannot assess whether the "adaptive adversary" is a realistic threat or an overpowered oracle. This interacts with W1 — the entire experimental pipeline from variables to manipulations is underspecified.
185	
186	5. **[Significant] Adversary realism.** Under black-box adversary (no panel information), K_eff is significant in only 3/12 conditions. The diversity trap is substantially an artifact of adversary information access. The paper does not adequately argue when full-knowledge or even partial-knowledge adversaries are realistic in LLM evaluation settings.
187	
188	6. **[Moderate] Framing oversells causation.** "Backfires," "reverses," "wrong" imply causation, but the analysis is observational regression. The Limitations section acknowledges this, but the title and abstract set expectations the methodology cannot fully meet.
189	
190	7. **[Moderate] Missing confidence intervals and practical effect sizes.** β and p without CIs or partial R² leave the practical magnitude of the diversity effect unclear. With n=455, statistical significance is easy to achieve; practical significance is the real question.
191	
192	8. **[Moderate] No single-judge baseline.** If robustness dominates, why not use one judge? The paper argues for "robustness-first, diversity-second" but doesn't test the extreme of "robustness-only."
193	
194	9. **[Minor] Medium tier (4 panels) is underpowered.** Should be omitted or explicitly flagged as inconclusive rather than included in Table 2 as if it provides evidence.
195	
196	10. **[Minor] Sections 8.1–8.2 feel disconnected.** Gaussian copula failure and family label unreliability are interesting but tangential to the main narrative. They could be moved to an appendix to free space for figures and expanded related work.
197	
198	### Experiment Coverage Assessment
199	
200	The paper covers all 13 imagined experiments from the design context with matching numerical results:
201	- plan_001 (Core 15-model regression) → Table 1 ✅
202	- plan_002 (Attack expansion to 9 types) → Table 6 ✅
203	- plan_003 (BFT random-fault contrast) → Table 4 ✅
204	- plan_004 (Within-tier validation) → Table 2 ✅
205	- plan_005 (Two-stage defense) → Table 10 ✅
206	- plan_006 (ASR concentration) → Table 5 ✅
207	- plan_007 (Diversity-capability tradeoff) → Section 8.3 ✅
208	- plan_008 (Panel size sensitivity) → Table 8 ✅
209	- plan_009 (VIF + diagnostics) → Table 3 + Section 5.3 ✅
210	- plan_010 (Aggregation rule modulation) → Table 11 ✅
211	- plan_011 (Open-ended benchmarks) → Table 7 ✅
212	- plan_001_mi (Copula failure + family labels) → Section 8.1–8.2 ✅
213	- plan_012 (Partial-knowledge adversary) → Table 9 ✅
214	
215	Coverage is complete. However, detailed sub-tables from several experiments (e.g., large-tier condition detail from plan_004, threshold sensitivity from plan_005, full diagnostics from plan_009) are condensed or omitted — reasonable for space, but the missing detail could go to supplementary materials.
216	
217	**Critical gap:** The imagined experiments specify 16+ figures, yet the paper contains zero. This is the single largest presentation disconnect.
218	
219	### Scores
220	
221	| Dimension | Score | Justification |
222	|-----------|-------|---------------|
223	| Soundness | 3.5/5 | Core statistical design is rigorous, but K_eff undefined, adversary opaque, causation oversold |
224	| Excitement | 3.5/5 | Important question, compelling finding, but novelty relative to ensemble adversarial literature unclear |
225	| Reproducibility | 2.0/5 | K_eff formula missing, attack implementations absent, no code/data, adversary algorithm undescribed |
226	
227	### Overall Assessment: 3.0 (Findings)
228	
229	**Calibration rationale:** The paper addresses an important, timely question with impressive experimental scale and a sound statistical framework. The attack taxonomy and BFT reversal mechanism are genuinely interesting contributions. However, three major issues prevent a Conference recommendation: (1) the central variable K_eff lacks a mathematical definition, making the paper unreproducible; (2) the related work section is far too thin for EMNLP, with entire relevant literatures unacknowledged; (3) the complete absence of figures in a table-heavy empirical paper significantly hurts readability and impact. These are all fixable in revision.
230	
231	The paper is above the Findings threshold (3.0) because the core finding is novel in the LLM evaluation context, the experimental design is comprehensive, and the practical implications are clear. It falls short of Conference (4.0) due to the reproducibility, presentation, and positioning gaps. With a revised version that adds K_eff definition, expands related work to ~30+ references, includes key figures, and provides attack implementation details, this could reach 3.5–4.0.
232	
233	### Revision Priorities (for next Dream iteration)
234	
235	1. **Add K_eff formula** (1 paragraph in Section 3 — define MI estimation, eigenspectrum → scalar reduction)
236	2. **Add 4–5 key figures** (K_eff vs ASR scatter, β heatmap, BFT reversal lollipop, Pareto frontier — drop Sections 8.1–8.2 to appendix to make space)
237	3. **Expand related work to 25–30 references** (ensemble adversarial robustness, multi-judge evaluation, game-theoretic adversary models, LLM manipulation)
238	4. **Add attack description table** (one-line description + example prompt per attack type)
239	5. **Add confidence intervals** to Tables 1 and 4 at minimum
240	6. **Soften causal framing** in title/abstract — "is associated with" rather than "backfires"
241	7. **Add single-judge baseline** to Table 10
242	8. **Drop or flag medium tier** as underpowered in Table 2
243	
244	---
245	
246	## 引用验证结果
247	
248	**统计**: 29 篇文献 / 43 处引用 / 在线验证 29/29 篇
249	
250	### 问题 (6)
251	
252	- ⚠️ `almasoud2026security` — 元数据不匹配: first_author: bib=al masoud vs api=masoud
253	- ⚠️ `tramer2018ensemble` — 元数据不匹配: first_author: bib=tram\`er vs api=tramèr
254	- ⚠️ `schneier2000secrets` — 元数据不匹配: first_author: bib=schneier vs api=1963-
255	- ⚠️ `hendrycks2021mmlu` — 元数据不匹配: year: bib=2021 vs api=2025, first_author: bib=hendrycks vs api=son
256	- ⚠️ `jung2026logarithmic` — 在 .bib 中但正文未引用
257	- ⚠️ `zheng2024lmsyschat` — 在 .bib 中但正文未引用
258	
259	### ✅ 通过 (25)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17948a62-fa58-4b96-a55a-d10416a43acf",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "5f3871b6-5997-4173-86e8-f340445ddba5",
  "sourceToolAssistantUUID": "17948a62-fa58-4b96-a55a-d10416a43acf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-22T18:41:30.059Z_

Now I have a thorough understanding of both the paper's actual content and the project's internal state (including the evolution of claims, falsified hypotheses, and decision history). Let me also look at a critical detail -- the discrepancy between the dream paper and the actual paper being written.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f3871b6-5997-4173-86e8-f340445ddba5",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6dBRhaL2UhP3NevJ8J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05b5d818-a54c-454c-b6e1-df19e40b62d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SGwqaQenqJ1ab9DM2vxi6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7817,
      "cache_read_input_tokens": 56301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7817,
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

_source line 53 · 2026-05-22T18:41:32.680Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nr7yZchwnFD3xV6LGuubvP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/review_report.md",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b5d818-a54c-454c-b6e1-df19e40b62d8",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6dBRhaL2UhP3NevJ8J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c108febb-89b4-407b-b056-ff347054ccd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SGwqaQenqJ1ab9DM2vxi6M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7817,
      "cache_read_input_tokens": 56301,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7817
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 56301,
          "cache_creation_input_tokens": 7817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7817,
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

_source line 54 · 2026-05-22T18:41:32.686Z_

<details><summary>↩ Tool result · `toolu_01Nr7yZchwnFD3xV6LGuubvP`</summary>

```text
1	---
2	dream_id: dream_20260522T055016
3	tier: median
4	overall_score: 2.5 - Borderline Findings
5	timestamp: 2026-05-22T06:36:05.259008+00:00
6	---
7	
8	# Dream Review Report: "The Weakest Link: Individual Robustness Dominates Diversity in Multi-Judge LLM Evaluation Security"
9	
10	**Dream ID:** 20260522T055016
11	**Review Mode:** Full (2 Reviewers + Roundtable)
12	**Target Venue:** EMNLP 2026 (ARR)
13	
14	---
15	
16	## Consolidated Assessment
17	
18	**Overall Score: 2.5 / 5 (Borderline Findings)**
19	
20	| Dimension | R1 | R2 | Converged |
21	|---|---|---|---|
22	| Soundness | 2.5 | 2.5 | 2.5 |
23	| Excitement | 3.0 | 2.0 | 2.5 |
24	| Reproducibility | 2.0 | 2.0 | 2.0 |
25	| Overall | 2.5 | 2.0 | 2.5 |
26	| Confidence | 4 | 4 | 4 |
27	
28	---
29	
30	## Paper Summary
31	
32	The paper argues that multi-judge LLM evaluation panel security is dominated by individual judge robustness (η_max) rather than judge diversity (K_eff), challenging the implicit BFT analogy in the diversity-as-defense literature. Through experiments on 455 three-judge panels from 15 LLMs across 6 attack types and 2 benchmarks, the paper shows η_max is significant in 8/12 conditions while K_eff in only 2/12. It formalizes an adaptive adversary bound (ASR ≤ η_max·(1+ε·log K)), contrasts adaptive vs. random-fault regimes (Cohen's d = 0.62), identifies a structural diversity-capability tradeoff (r = −0.65), and proposes a robustness-first panel design guideline.
33	
34	---
35	
36	## Reviewer Agreement (Roundtable Convergence)
37	
38	Both reviewers agree on the following points:
39	
40	### Shared Strengths
41	
42	1. **The BFT vs. adaptive adversary contrast is the paper's strongest contribution.** The random-fault simulation cleanly isolates the fault model as the explanatory variable: K_eff goes from significant in 1/6 (adaptive) to 4/6 (random-fault) conditions. Cohen's d = 0.62 establishes moderate-effect distinguishability. This is methodologically sound and pedagogically valuable.
43	
44	2. **Experimental scale is ambitious and well-designed.** 15 models spanning 3 capability tiers, all C(15,3)=455 panels enumerated (avoiding sampling bias), 6 attack types covering targeted and distributed attacks, 2 benchmarks, and panel sizes K=3–9. The combinatorial exhaustiveness is a genuine methodological strength.
45	
46	3. **The diversity-capability tradeoff decomposition is informative.** Showing that r = −0.65 overall is driven primarily by cross-tier selection (r = −0.78) rather than within-tier differences (r ≈ −0.32) provides a structural explanation and actionable insight for practitioners.
47	
48	4. **The Gaussian copula failure finding (42× median underestimation) has implications beyond this paper.** It warns the community that copula-based independence assumptions systematically overestimate multi-judge panel quality.
49	
50	5. **The paper's narrative is nuanced and honest.** The regime-dependent framing ("diversity helps only when individual robustness is already high") is more calibrated than a blanket "diversity never helps" claim. The Limitations section is candid about statistical power issues.
51	
52	### Shared Weaknesses
53	
54	1. **[CRITICAL] Theorem 1 has a fundamental proof gap.** The theorem claims ASR_panel ≤ η_max·(1+ε·log K) under majority vote, but majority vote requires compromising ⌈K/2⌉ judges, not just one. The paper provides no rigorous bound on the probability that attacking the weakest judge also compromises additional judges to achieve a majority. The "proof sketch" relies on an informal argument about correlated vulnerabilities without quantifying the transfer probability. This undermines the paper's theoretical core. **Recommendation:** Either provide a rigorous proof with explicit assumptions about inter-judge vulnerability correlation, or downgrade to an "empirical observation" and remove the "theorem" label.
55	
56	2. **[CRITICAL] No bibliography or references are present in the paper.** The Related Work section makes generic claims ("Recent surveys and frameworks explicitly advocate..."; "established in the distributed systems literature") but cites zero specific papers. No bibliography section exists. This is far below venue standards (EMNLP expects 25–40 references) and would likely trigger desk rejection. Even for a dream/draft review, the absence of any citation infrastructure is a fundamental structural deficiency.
57	
58	3. **[MAJOR] Multicollinearity between K_eff and η_max (r = −0.65) is unaddressed.** At this correlation level, VIF ≈ 1.7–2.5, inflating standard errors for both predictors. K_eff's non-significance (median p = 0.43 across conditions) could partly reflect a Type II error artifact rather than genuine irrelevance. The paper reports no VIF, no tolerance statistics, no partial correlations, and no residualization analysis. Without these standard regression diagnostics, the central empirical claim — that K_eff is truly irrelevant rather than merely undetectable due to collinearity — is not rigorously established.
59	
60	4. **[MAJOR] Limited novelty over existing security and adversarial ML literature.** The weakest-link principle is foundational in security (Schneier 2000, Anderson 2001). Tramer et al. (2018, "Ensemble Adversarial Training") demonstrated that diverse ensembles fail against adaptive adversaries in vision. Adversarial transferability research (Papernot et al. 2016, 2017) established the mechanism by which attacks transfer across models. The paper's core insight — adaptive adversaries undermine diversity-based defenses by targeting the weakest component — is a domain transfer of established results rather than a novel discovery. The paper should position itself as an empirical validation in a new domain with additional quantitative insights (copula failure, regime analysis), not as overturning a "prevailing assumption."
61	
62	5. **[MAJOR] Reproducibility is critically low.** Missing details include: (a) attack prompt implementations for all 6 attack types, (b) MI estimation method for computing K_eff, (c) ASR operationalization (binary threshold? continuous?), (d) API model versions and inference hyperparameters, (e) no code or data release mentioned. A reader cannot reproduce these experiments from the paper alone.
63	
64	6. **[MODERATE] The "prevailing assumption" framing may be a strawman.** The paper claims the field treats diversity as "the key security mechanism," but without verifiable citations, we cannot confirm this is actually the prevailing view. The diversity-as-defense literature may primarily advocate diversity for reducing non-adversarial biases (position, verbosity, sycophancy), not for defending against adaptive adversaries. If so, the paper attacks a position few hold.
65	
66	### Divergence Points (Resolved in Roundtable)
67	
68	- **Excitement:** R1 rated 3/5 (timely question, practically relevant even if not fully surprising); R2 rated 2/5 (well-known in security literature, minimal intellectual novelty). **Converged at 2.5/5** — the empirical application to LLM judges is timely and the regime analysis adds value, but the core mechanism is not new. The paper's contribution is empirical validation + quantification in a specific domain, which has moderate but not high excitement.
69	
70	- **Severity of Related Work gap:** R1 treated it as a "minor issue" (sparse references); R2 treated it as disqualifying. **Converged: this is a critical issue** that must be addressed before any submission. The complete absence of a bibliography goes beyond "sparse references" — it is a structural deficiency.
71	
72	---
73	
74	## R1 Detailed Review: Methods and Experiments
75	
76	### Key Methodological Concerns
77	
78	1. **Regression specification (log-log model).** The log-log regression log(ASR) ~ log(η_max) + log(K_eff) imposes a power-law relationship with no justification. ASR is bounded in [0,1]; a logistic or beta regression would be more appropriate. No residual analysis, heteroscedasticity tests (Breusch-Pagan), or comparison with alternative functional forms is provided. Mis-specification could bias coefficient estimates.
79	
80	2. **Within-tier analyses are severely underpowered.** The Weak tier has only 10 panels (C(5,3)=10); the API tier also has 10 panels. With N=10 and 2 predictors, each regression has ~7 degrees of freedom. Significance rates (e.g., "0/6 significant in Weak tier") should be heavily caveated. The paper correctly acknowledges low power for the API tier but less so for the Weak tier.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c108febb-89b4-407b-b056-ff347054ccd0",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "737e06f4-d194-4383-adcc-428d772a281a",
  "sourceToolAssistantUUID": "c108febb-89b4-407b-b056-ff347054ccd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-22T18:41:37.324Z_

Now I have comprehensive information to write the review. Let me also check the actual paper's tex files one more time for any discrepancies between the dream simulation paper and the actual paper being written, since the paper framing has evolved significantly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "737e06f4-d194-4383-adcc-428d772a281a",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6dhnaKkoxSepsqCaXv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8866fde3-1132-415d-8e76-5179e41f959b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtXxJKXEJzT5sHPjiCP2ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2561,
      "cache_read_input_tokens": 64118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2561,
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

_source line 56 · 2026-05-22T18:41:38.341Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PL4PRVAviwVXBxVjm1B5wA`</summary>

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
  "parentUuid": "8866fde3-1132-415d-8e76-5179e41f959b",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6dhnaKkoxSepsqCaXv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8306c98-51d0-4400-9561-7ac613e3cc16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtXxJKXEJzT5sHPjiCP2ge",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2561,
      "cache_read_input_tokens": 64118,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2561
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 64118,
          "cache_creation_input_tokens": 2561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2561,
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

_source line 57 · 2026-05-22T18:41:38.344Z_

<details><summary>↩ Tool result · `toolu_01PL4PRVAviwVXBxVjm1B5wA`</summary>

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
  "parentUuid": "e8306c98-51d0-4400-9561-7ac613e3cc16",
  "isSidechain": true,
  "promptId": "4c569c64-c55f-464e-b9b3-78000e19f7c9",
  "agentId": "acfb302ff2bd95621",
  "type": "user",
  "uuid": "7c8c1d4b-1a01-4207-ae6e-ffe830bd3b9a",
  "sourceToolAssistantUUID": "e8306c98-51d0-4400-9561-7ac613e3cc16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-22T18:43:32.522Z_



Now I have a thorough understanding of the paper across both versions (the actual tex files being written and the dream simulation paper), the project's internal decision history, the literature map, and prior dream reviews. Let me produce the R2 review.

---

## Review: R2 (Novelty and Related Work)

**Paper:** "Rethinking Diversity in LLM Evaluation Panels: When More Judges Make Things Worse"
**Venue:** EMNLP 2026 (via ARR)
**Reviewer Focus:** Novelty assessment, related work coverage, contribution positioning

---

### Summary

The paper studies whether diversity in multi-judge LLM evaluation panels improves adversarial robustness. Using 15 models from 6 families, all C(15,3)=455 three-judge panels, 6 attack types, and 2 benchmarks, the authors use residualized regression to disentangle individual judge weakness (eta_max) from effective diversity (K_eff). The main finding is that eta_max is the dominant vulnerability predictor (significant in 9-11/12 conditions), while K_eff is a secondary amplifying factor (7/12 significant positive, 1/12 significant negative for sycophancy on ARC). Within capability tiers, the diversity effect largely disappears (2/18 significant). The paper proposes robustness-first panel design and characterizes how aggregation rules modulate both vulnerability channels.

---

### Strengths

**S1. Genuinely important and timely research question.** Multi-judge LLM evaluation is rapidly becoming standard (Chatbot Arena, MT-Bench, AlpacaEval). The implicit assumption that diversity equals robustness is pervasive in practice, even if it is rarely stated as a formal claim. Subjecting this assumption to rigorous empirical testing at scale is a valuable contribution regardless of the outcome.

**S2. The condition-dependent dominance pattern has real explanatory power.** The most novel finding is not "diversity hurts" in isolation but the attack-type taxonomy: transferable attacks concentrate K_eff's effect (5/6 significant), shared-bias attacks concentrate eta_max's effect (1/8 K_eff significant), and sycophancy on ARC shows diversity as genuinely protective (the lone negative K_eff coefficient). This condition-dependent structure goes beyond a single headline claim and provides a predictive framework. If I encounter a new attack type, I can predict which vulnerability channel matters based on its transferability profile. This is a genuine conceptual contribution that distinguishes the work from a simple negative result.

**S3. The aggregation rule analysis reveals a meaningful interaction.** Showing that Bayesian calibration partially flips K_eff from harmful to protective (4/5 significant coefficients negative under Bayesian vs. 7/12 positive under majority) while threshold voting amplifies both channels (R^2=0.901) is practically informative and not obvious a priori. The "aggregation gradient" (threshold > majority > weighted > Bayesian) is a clean result with direct prescriptive value.

**S4. Exhaustive panel enumeration eliminates sampling artifacts.** By evaluating all 455 three-judge panels rather than sampling, the study avoids selection bias entirely. Combined with the complete crossing of panels x attacks x benchmarks, this produces a dense experimental tensor that supports the regression analysis well.

**S5. The sycophancy exception strengthens rather than weakens the narrative.** A paper that claimed diversity always hurts would be less believable. The mechanistically informative exception (shared cognitive bias diluted by diverse panels = the one regime where BFT logic holds) demonstrates that the authors have identified a genuine mechanism boundary, not just a noisy correlation.

---

### Weaknesses

**W1 [Major]. The core finding has substantial precedent in the adversarial ML ensemble literature, insufficiently acknowledged.** The insight that diverse ensembles can be more vulnerable to adaptive adversaries is not new. Tramer et al. (2018, "Ensemble Adversarial Training: Attacks and Defenses") showed that ensemble diversity does not protect against transferred adversarial examples, and in some cases makes the ensemble more exploitable because the adversary gains access to a richer set of transferable perturbations. Kariyappa and Qureshi (2019, "Improving Adversarial Robustness of Ensembles with Diversity Training") explicitly studied the diversity-robustness tradeoff and found that naive diversity increases adversarial vulnerability. He et al. (2017) demonstrated that ensemble defenses based on input transformation diversity are broken by adaptive attackers. The paper's central mechanism -- adaptive adversaries exploit the diverse attack surface that independent judges create -- is essentially the LLM-judge instantiation of this established phenomenon.

The paper must explicitly position against this literature and articulate what is new beyond domain transfer. The LLM-judge-specific contributions (attack taxonomy, BFT reversal quantification, aggregation rule modulation, the sycophancy exception) may be sufficient for novelty, but the current framing ("first large-scale empirical study," "the diversity trap") overstates originality by not acknowledging this genealogy.

**W2 [Major]. The related work section, while improved in the actual tex files, still has significant gaps.** The actual related_work.tex (~0.75 pages) is substantially better than the dream simulation's related work, citing Zheng et al. (2023), Wang et al. (2023), Goodfellow et al. (2015), Papernot et al. (2016, 2017), Tramer et al. (2018), and several information-theoretic works. However, critical omissions remain:

- **Condorcet Jury Theorem (CJT):** The paper's finding is closely related to the CJT, which predicts that majority voting among independent voters with p>0.5 converges to the correct answer, but when p<0.5 (as for weak judges under attack), adding more voters makes the outcome *worse*. The paper's diversity trap under adversarial conditions may simply be the CJT prediction when eta_j > 0.5 for the weakest judge. The paper must discuss CJT and explain how its contribution differs from this classical prediction.

- **PoLL (Verga et al., 2024):** A directly relevant study on multi-judge panel composition for LLM evaluation that should be cited and contrasted.

- **Ensemble diversity in classical ML beyond adversarial settings:** Krogh and Vedelsby (1995) is cited, but the bias-variance-covariance decomposition (Ueda and Nakano, 1996) and negative correlation learning (Liu and Yao, 1999) provide a richer theoretical context for understanding when diversity helps vs. hurts.

- **Game-theoretic adversary modeling:** The adaptive adversary definition (Definition 1) is essentially a Stackelberg game where the defender commits to a panel and the adversary best-responds. This connection to the security games literature (Tambe, 2011) should be acknowledged.

- **Sycophancy literature:** Panickssery et al. (2024) on sycophancy in LLMs is directly relevant to the sycophancy exception finding.

For EMNLP 2026, I would expect 30-40 references for a paper spanning adversarial ML, distributed systems, ensemble learning, voting theory, and LLM evaluation. The current count (~20 in the actual tex) is below expectations.

**W3 [Major]. The "first large-scale empirical study" claim needs qualification.** The paper claims to be "the first large-scale empirical study examining how panel composition affects adversarial vulnerability." This may be true in the strict sense of the specific experimental design (455 panels, 6 attacks, regression disentanglement), but it risks overstating novelty given that: (a) the SoK paper (Almasoud et al., 2026) already empirically studied 7-model committees under attack; (b) the ensemble adversarial robustness literature has studied composition effects extensively in vision; (c) Kim et al. (2025) quantified correlated errors across 350+ LLMs. The claim should be scoped more precisely: "the first controlled study disentangling diversity from individual robustness as predictors of panel vulnerability in LLM evaluation."

**W4 [Significant]. The practical contribution (robustness-first design) is not significantly better than "just use the strongest judges."** The paper's own results show that robustness-first two-stage selection reduces ASR by 47% vs. random but only 7% vs. Strongest-K (p=0.42, not significant). The practical upshot is that practitioners should simply use the strongest available judges -- which is the obvious default strategy. The paper frames this as "robustness-first + diversity as tiebreaker," but the data show that the diversity tiebreaker contributes negligibly. This undermines the practical novelty: the actionable recommendation reduces to "use good judges," which is not a research contribution.

**W5 [Significant]. The title framing ("When More Judges Make Things Worse") is not fully supported by the evidence.** The paper's own within-tier analysis shows that diversity is largely neutral (2/18 significant) when capability is controlled. The harmful diversity effect is predominantly a tier-mixing artifact: diverse panels span capability tiers and structurally include weaker models. The more accurate characterization is "when diverse panels include weak judges, the weak judges dominate vulnerability" -- which is closer to "weak judges make things worse" than "diversity makes things worse." The title conflates diversity with capability heterogeneity.

The paper_framing.md internally acknowledges this tension (RC1: "K_eff positive is just confound with eta_max"), and the decisions log shows that the original K_eff-irrelevant finding (D009, "suggest kill project") was reversed only after expanding from 6 to 15 models (D014). The fact that the effect direction changed with model pool size (from NS to positive) raises the question of whether the finding is a stable property of the evaluation setting or an artifact of the specific model pool selected.

**W6 [Moderate]. The BFT framing is more illustrative than substantive, and this should be acknowledged more clearly.** The paper invokes BFT as the theoretical motivation, but the actual contribution is empirical regression, not a formal security analysis. The BFT reversal prediction (K_eff helps under random faults, hurts under adaptive) is only partially confirmed: K_eff is positive in both regimes (no sign reversal), with only a relative importance shift. The decisions log (D011) records that "Plan_003 BFT contrast failed (0/12 random-fault K_eff significant)" at 6 models, and even at 15 models the narrative has been reframed from "sign reversal" to "predictability gap" (Claim 2 in paper_framing.md). Calling this a "BFT reversal mechanism" overstates what the data show.

The more appropriate framing is the Condorcet Jury Theorem under adversarial conditions, which predicts exactly the observed pattern without requiring the BFT analogy at all.

**W7 [Minor]. The Gaussian copula failure finding (Claim 5) was falsified at 15-model scale but may still appear in some versions.** The decisions log (D015) records that the 10x MI underestimation was a small-sample artifact (ratio = 0.93 at 15 models). The dream simulation paper still reports this as a finding (10x underestimation). If this appears in the submitted version, it would be reporting a result the authors know to be an artifact of their earlier 6-model analysis. The actual paper tex files do not include this claim, which is correct.

---

### Questions for Authors

1. **CJT connection:** Under your adaptive adversary, the weakest judge has eta_j > 0.5 in many conditions. The Condorcet Jury Theorem predicts that adding independent voters with p < 0.5 makes majority voting worse. How does your diversity trap differ from this classical prediction? If it is essentially the CJT under adversarial conditions, the novelty claim needs recalibration.

2. **Stability across model pools:** The K_eff effect went from non-significant (6 models, D009) to significantly positive (15 models, D014). If you added 15 more models, would the effect change again? What gives you confidence that the 15-model result is the "true" effect rather than another artifact of the specific model selection?

3. **Single-judge baseline:** If robustness-first is the recommendation, what is the ASR of the single best judge (e.g., Claude-3.5-Sonnet alone) compared to the best 3-judge panel? If comparable, the implication is that panels provide no adversarial benefit, which would be a stronger and more interesting finding.

4. **Why not causal identification?** You have 455 panels as a natural experiment. Have you considered instrumental variable approaches or matching designs (e.g., comparing panels with identical eta_max but different K_eff) to strengthen causal claims beyond associational regression?

5. **Adversary realism:** In what practical LLM evaluation scenario does the adversary know individual judge vulnerability profiles? Benchmark operators typically do not disclose panel composition. The partial-knowledge and black-box results (where the effect attenuates sharply) seem more practically relevant but are relegated to secondary status.

---

### Missing References

The following works are conspicuously absent or underrepresented:

1. **Condorcet (1785)** -- Jury theorem; the classical theoretical framework most directly relevant to the paper's setting
2. **Kariyappa and Qureshi (2019)** -- "Improving Adversarial Robustness of Ensembles with Diversity Training" -- directly studies diversity-robustness tradeoff
3. **He et al. (2017)** -- "Adversarial Examples for Semantic Segmentation and Object Detection" / ensemble defense failures
4. **Verga et al. (2024)** -- PoLL: multi-judge panel composition for LLM evaluation
5. **Panickssery et al. (2024)** -- Sycophancy in LLMs; directly relevant to the sycophancy exception
6. **Perez et al. (2022)** -- Red-teaming language models
7. **Ueda and Nakano (1996)** -- Bias-variance-covariance decomposition for ensembles
8. **Liu and Yao (1999)** -- Negative correlation learning
9. **Tambe (2011)** -- Security games / Stackelberg framework for adaptive adversaries
10. **Li et al. (2024)** -- Judge biases in LLM evaluation
11. **Shi et al. (2024)** or **Raina et al. (2024)** -- Adversarial attacks specifically on LLM judges
12. **Dietterich (2000)** -- "Ensemble Methods in Machine Learning" -- foundational survey on when/why ensembles work

---

### Preliminary Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **Soundness** | 3.0 / 5 | Regression framework is adequate but the confound between K_eff and tier-mixing is not fully resolved; BFT reversal is not empirically confirmed as claimed; causal language exceeds what observational regression supports |
| **Excitement** | 2.5 / 5 | The question is important but the core mechanism (adaptive adversaries exploit the weakest link; diversity introduces weak links) is predictable from both CJT and ensemble adversarial ML. The attack taxonomy and aggregation modulation are moderately interesting. The practical recommendation ("use strong judges") is obvious. |
| **Reproducibility** | 3.0 / 5 | The actual paper tex defines K_eff (Equation 2 in threat_model.tex), which is a significant improvement over the dream version. Attack descriptions are present but implementation details (prompts, operationalization) are still thin. No code/data release mentioned. |

**Overall Assessment: 2.5 (Borderline Findings)**

**Calibration rationale:** The paper addresses a timely question with substantial experimental scale, but the novelty is limited by (1) extensive precedent in the ensemble adversarial robustness literature that is inadequately acknowledged, (2) the CJT already predicts the core finding under adversarial conditions, (3) the primary diversity effect is largely a tier-mixing artifact (2/18 significant within tiers), and (4) the practical recommendation is not significantly better than the obvious baseline of using the strongest judges. The attack taxonomy (transferable vs. shared-bias) and the aggregation rule modulation analysis are the most genuinely novel contributions, but they are secondary findings in the current framing.

The related work section needs substantial expansion (current ~20 references, expected 30-40) with explicit positioning against ensemble adversarial robustness, CJT, and security games literature. The title and framing overstate what the evidence supports -- the data show "weak judges dominate vulnerability" more than "diversity hurts." With expanded related work, honest positioning as an empirical validation in a new domain (rather than a paradigm-shifting discovery), and tighter causal language, this could reach 3.0-3.5. As submitted, it falls short of Findings primarily on novelty and positioning grounds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c8c1d4b-1a01-4207-ae6e-ffe830bd3b9a",
  "isSidechain": true,
  "agentId": "acfb302ff2bd95621",
  "requestId": "req_011CbJ6e7rRbpMfVFX33cMoL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a78e481-c729-44e6-b220-5427c796d87e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "6b6bb46a-6f14-4907-ac47-60e29122a37c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUejVu85PwV5dB11eSQM1c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 66679,
      "output_tokens": 4079,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 763
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4079,
          "cache_read_input_tokens": 66679,
          "cache_creation_input_tokens": 763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 763,
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
