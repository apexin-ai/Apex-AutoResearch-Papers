# Research conversation: You are Reviewer R2 for a blind peer review of an ML/NLP paper. Your focus is **Novelty, Contributions, and Related Work

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a2f3b178915a739ac.jsonl`
- **Structured JSON:** [`3b4334f5a6a2704ec806.json`](../../sessions/3b/3b4334f5a6a2704ec806.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-20T16:51:55.516Z_

You are Reviewer R2 for a blind peer review of an ML/NLP paper. Your focus is **Novelty, Contributions, and Related Work**. Review the paper strictly and thoroughly, as if reviewing for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept).

## Paper Summary
Title: "Policy Ambiguity Causes Catastrophic Safety Violations in LLM Agents: A Causal Study"

The paper studies how policy ambiguity causes safety violations in LLM agents. Using a matched-pair design across 300 clause pairs spanning six ambiguity types, five models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-32B, Qwen3-8B), and 3,000 agent episodes, the paper claims three findings:
1. **Massive Binary Effect**: +30.2pp increase in safety violation rates (McNemar OR=24.1, p<0.0001), with perturbation control confirming ambiguity-specific causation (Δ_perturb=4.2pp, ratio=0.13).
2. **Ambiguity Blindness**: 92% of violation traces show no meta-cognitive awareness of ambiguity. Universal across types and models.
3. **Model-Dependent Vulnerability Profiles**: model×type interaction p=0.008. GPT models are spec-layer sensitive, Claude is coreferential-sensitive, Qwen3-8B is linguistic-layer sensitive. No universal type hierarchy.

## Paper Structure and Content

### §1 Introduction
- Opens with concrete example: ambiguous airline policy causes agent to grant inappropriate refund
- Positions against DRIP-R, PhantomPolicy, PolicyBank as prior work
- Claims: "no prior work isolates the causal effect of ambiguity on safety violations with controlled experimental design"
- Three contributions listed: Massive Binary Effect, Ambiguity Blindness, Model-Dependent Vulnerability Profiles

### §2 Related Work
Covers four areas:
1. **Ambiguity in Requirements and Policies**: Berry & Kamsties (nocuous vs innocuous), Massey et al. (6-type taxonomy for privacy policies), Li et al. (11-type NLP taxonomy), Chantree et al. (coordination ambiguity classifiers), Ezzini et al. (TAPHSIR), Willis et al.
2. **Agent Safety Evaluation**: R-Judge, ToolEmu, InjecAgent, AgentPex — notes these study "explicit adversarial conditions" while this paper studies "subtler threat"
3. **Prompt Sensitivity and Robustness**: Sclar et al. (prompt sensitivity), Lu et al. (example ordering), Zhou et al. (instruction-following robustness)
4. **Psycholinguistic Grounding**: Ferreira et al. (good-enough processing), Frazier & Rayner (garden-path), Levy (expectation-based models)

### §3 Ambiguity Taxonomy
- Two-layer, six-type taxonomy from Li et al. and Massey et al.
- Specification layer: authorization scope, incompleteness, conditional polysemy
- Linguistic layer: scopal, lexical, coreferential
- Operationalizes "ambiguity" broadly to include vagueness (following Wasow et al.)

### §4 Method
- Matched-pair clause generation (300 pairs, 50/type)
- τ²-bench platform (retail, airline domains)
- 5 models, perturbation control, judge calibration, realism validation

### §5 Results
- C1: +30.2pp binary effect, universal across types and models
- C2: Model-dependent vulnerability profiles (model×type interaction p=0.008)
- Layer gap n.s. (p=0.14), type effect weak (V=0.11)
- Reliability ICC=0.68

### §6 Ambiguity Blindness
- 92% of 300 violation traces show no meta-cognitive awareness
- Connected to good-enough processing (Ferreira et al.)
- 5 failure modes identified, cross-layer overlap 42%

### §7 Discussion
- Advocates binary detection strategy
- DeBERTa PoC classifier (F1=0.78)
- Explains why type rankings are model-dependent
- Limitations: domain scope, synthetic clauses, judge reliability, token length confound, classifier scope

### §8 Conclusion
- Summarizes three findings
- "The policy ambiguity problem will not be solved by building better agents. It must be solved by building better policies."

## Key Issues to Evaluate

### Novelty
- Is the "causal" framing genuinely novel vs. DRIP-R, PhantomPolicy?
- Is the matched-pair design a sufficient methodological advance?
- Is "ambiguity blindness" a new concept or restatement of known limitations?
- Are model-dependent vulnerability profiles surprising?

### Contribution Significance
- How important is the +30.2pp finding practically?
- Does the paper change how the community should think about agent safety?
- Is the DeBERTa PoC a meaningful contribution or padding?

### Related Work Completeness
- Are there missing related works in agent safety, policy compliance, or ambiguity detection?
- Is the positioning against DRIP-R, PhantomPolicy, PolicyBank fair?
- Is the psycholinguistic connection (good-enough processing) well-grounded?

### Framing and Claims
- Is "catastrophic" in the title justified?
- Is "the largest causal effect reported in the agent safety literature" verifiable?
- Are the three contributions well-differentiated?
- Is the practical recommendation (binary detection) well-supported?

## References Section
The paper's References section appears to be empty (marked with "?" placeholders throughout). This is a significant concern.

## Your Task
Write a detailed R2 review focusing on:
1. **Novelty assessment**: How novel is each contribution? What is the delta over prior work?
2. **Related work completeness**: Missing references? Fair positioning?
3. **Contribution clarity and significance**: Are the three contributions distinct and meaningful?
4. **Framing analysis**: Are the claims calibrated? Is the title appropriate?
5. **Taxonomy evaluation**: Is the 6-type taxonomy well-motivated? Is the spec/ling layer distinction useful given the n.s. result?
6. **Practical impact**: Does the binary detection recommendation follow from the evidence?
7. **Writing quality**: Is the paper well-organized and clearly written?

Provide:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, numbered W1, W2, ...)
- Questions for authors
- Minor issues
- Overall assessment score (1-6) with justification
- Confidence (1-5)

Be rigorous but fair. This is blind review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "f6e2d36f-ccb0-48ad-982a-a2de604eea3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T16:51:55.518Z_

```json
{
  "parentUuid": "f6e2d36f-ccb0-48ad-982a-a2de604eea3f",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
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
  "uuid": "2a3eefbc-0051-46f9-9756-8a751d09f7c9",
  "timestamp": "2026-05-20T16:51:55.518Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T16:52:01.300Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a3eefbc-0051-46f9-9756-8a751d09f7c9",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAf2yDBYN84WF26j39c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82a6e649-da88-45ac-8e5b-9a7ee80b5fac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RQ4Jzk2PjztC3zsgq1HMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7937,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7937,
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

_source line 4 · 2026-05-20T16:52:05.147Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018aZKnNB1yrn6NyZKdZHDcb`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82a6e649-da88-45ac-8e5b-9a7ee80b5fac",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAf2yDBYN84WF26j39c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f4e82a0-6cab-494b-ab6b-3aac2618c3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RQ4Jzk2PjztC3zsgq1HMh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7937,
      "cache_read_input_tokens": 8253,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7937
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 8253,
          "cache_creation_input_tokens": 7937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7937,
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

_source line 5 · 2026-05-20T16:52:05.150Z_

<details><summary>↩ Tool result · `toolu_018aZKnNB1yrn6NyZKdZHDcb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f4e82a0-6cab-494b-ab6b-3aac2618c3af",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "5e629cc3-556b-4c50-ad11-b7daacaa77bd",
  "sourceToolAssistantUUID": "1f4e82a0-6cab-494b-ab6b-3aac2618c3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T16:52:08.786Z_



Let me read the paper and all relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e629cc3-556b-4c50-ad11-b7daacaa77bd",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAfkX333TJXKvz6AtoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb6ed73d-af7a-49e8-a030-d4484bc9ca35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEbk2pvxgUGvcA1Zswq5cZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 16190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 7 · 2026-05-20T16:52:09.622Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Dyei39Yyzah8Kz5KKdiMFG`</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb6ed73d-af7a-49e8-a030-d4484bc9ca35",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAfkX333TJXKvz6AtoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2a6ce76-94ec-4d0b-ad41-3045ae544657",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEbk2pvxgUGvcA1Zswq5cZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 16190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 8 · 2026-05-20T16:52:09.633Z_

<details><summary>↩ Tool result · `toolu_01Dyei39Yyzah8Kz5KKdiMFG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_009: Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.（准备中）\\n\\n## 近期结论\\n- **plan_006** (success): API model violation judgments are highly reproducible across independent replicates (ICC ≥ 0.75), confirming that the observed violation rates and type differences in plan_002 are stable signals, not sampling noise. ← 基于 plan_002\\n  [plan_006_icc_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_006/report/icc_results.json)\\n- **plan_005** (success): Specification-layer ambiguities produce qualitatively different failure modes (more assumption_based_action) than linguistic-layer ambiguities (more scope_misapplication), and coreferential's low violation rate is explained by higher conservative_refusal rate. These distinct failure mode profiles explain the layer hierarchy (spec ~46pp vs ling ~27pp). ← 基于 plan_002\\n  [plan_005_failure_modes](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_005/data/failure_modes.jsonl) | [plan_005_summary](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_005/report/summary.json)\\n- **plan_002** (negative): Policy ambiguity causes significantly higher agent safety violation rates (+30-40pp) across all 6 ambiguity types, with uniform effect size across types (no significant type×violation interaction). Binary effect is the primary finding; type uniformity supports that ambiguity per se, not specific linguistic structures, drives violations.\\n  [plan_002 full study results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_002/data/full_statistics.json) | [c3_layer_effect_test](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_002/report/layer_effect_test.json)\\n\\n## 趋势\\n成功 2 / 负向 3 / 失败 0 / 共 5\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2064, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2a6ce76-94ec-4d0b-ad41-3045ae544657",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "d36ef2ef-b7d4-4a35-bb78-b9afbe0e2e15",
  "sourceToolAssistantUUID": "d2a6ce76-94ec-4d0b-ad41-3045ae544657",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T16:52:11.044Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Cm3CJGyLNDUUZfUDBrcfq3`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d36ef2ef-b7d4-4a35-bb78-b9afbe0e2e15",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAfkX333TJXKvz6AtoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66620580-9cc9-4f63-a728-babd68cb4ce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEbk2pvxgUGvcA1Zswq5cZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 16190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 10 · 2026-05-20T16:52:11.106Z_

<details><summary>↩ Tool result · `toolu_01Cm3CJGyLNDUUZfUDBrcfq3`</summary>

```text
artifacts/dream_reports/dream_20260520T112859/best/paper.tex
artifacts/dream_reports/dream_20260520T112859/median/paper.tex
artifacts/dream_reports/dream_20260520T112859/worst/paper.tex
artifacts/dream_reports/dream_20260520T152228/best/paper.tex
artifacts/dream_reports/dream_20260520T152228/median/paper.tex
artifacts/dream_reports/dream_20260520T152228/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66620580-9cc9-4f63-a728-babd68cb4ce1",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "2d62d9ac-3eb7-46ab-9d4c-a7d5a61cd5fa",
  "sourceToolAssistantUUID": "66620580-9cc9-4f63-a728-babd68cb4ce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T16:52:11.594Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SuFptUQkeAUQniSwSsjn9J`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d62d9ac-3eb7-46ab-9d4c-a7d5a61cd5fa",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAfkX333TJXKvz6AtoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c1579f8-5d1e-4f31-9269-4e961358e958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEbk2pvxgUGvcA1Zswq5cZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 16190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 12 · 2026-05-20T16:52:11.684Z_

<details><summary>↩ Tool result · `toolu_01SuFptUQkeAUQniSwSsjn9J`</summary>

```text
.claude/sessions/reviewer_c268ee05/memory/MEMORY.md
.claude/sessions/reviewer_c268ee05/memory/project_mvp_review.md
artifacts/ambiguity_taxonomy.md
artifacts/_project/report/ambiguity_taxonomy.md
artifacts/_project/report/taubench_policy_format.md
artifacts/taubench_policy_format.md
artifacts/_project/report/README.md
artifacts/README.md
.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/philox/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
.venv/lib/python3.14/site-packages/idna-3.15.dist-info/licenses/LICENSE.md
.venv/lib/python3.14/site-packages/scipy/fft/_pocketfft/LICENSE.md
.venv/lib/python3.14/site-packages/httpcore-1.0.9.dist-info/licenses/LICENSE.md
.venv/lib/python3.14/site-packages/httpx-0.28.1.dist-info/licenses/LICENSE.md
.venv/lib/python3.14/site-packages/openai/resources/conversations/api.md
.venv/lib/python3.14/site-packages/openai/resources/realtime/api.md
.venv/lib/python3.14/site-packages/openai/resources/responses/api.md
.venv/lib/python3.14/site-packages/openai/resources/webhooks/api.md
artifacts/_project/report/api_fallback_comparison.md
artifacts/api_fallback_comparison.md
artifacts/_project/report/ambiguity_taxonomy_extended.md
artifacts/ambiguity_taxonomy_extended.md
artifacts/.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/philox/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/idna-3.15.dist-info/licenses/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/scipy/fft/_pocketfft/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/httpcore-1.0.9.dist-info/licenses/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/httpx-0.28.1.dist-info/licenses/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/conversations/api.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/realtime/api.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/responses/api.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/webhooks/api.md
.claude/sessions/distiller_c8e309f2/CLAUDE.md
.claude/sessions/distiller_c8e309f2/AGENTS.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260520T112859/best/paper_framing.md
artifacts/dream_reports/dream_20260520T112859/median/paper_framing.md
artifacts/dream_reports/dream_20260520T112859/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T112859/best/review_report.md
artifacts/dream_reports/dream_20260520T112859/median/review_report.md
artifacts/dream_reports/dream_20260520T112859/worst/review_report.md
memory.md
artifacts/_project/report/annotation_guidelines.md
artifacts/plan_009/annotation_guidelines.md
artifacts/plan_009/report/annotation_guidelines.md
artifacts/dream_reports/dream_20260520T152228/best/paper_framing.md
artifacts/dream_reports/dream_20260520T152228/median/paper_framing.md
artifacts/dream_reports/dream_20260520T152228/worst/paper_framing.md
paper_framing.md
ROADMAP.md
.claude/sessions/reviewer_c268ee05/CLAUDE.md
.claude/sessions/reviewer_c268ee05/AGENTS.md
artifacts/dream_reports/dream_20260520T152228/best/review_report.md
.claude/sessions/review_reviewer_1_6edf79f4/CLAUDE.md
.claude/sessions/review_reviewer_1_6edf79f4/AGENTS.md
.claude/sessions/review_reviewer_2_3cdc27e4/CLAUDE.md
.claude/sessions/review_reviewer_2_3cdc27e4/AGENTS.md
.claude/sessions/agent_241139a3/CLAUDE.md
.claude/sessions/agent_241139a3/AGENTS.md
report.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_33741c24/CLAUDE.md
.claude/sessions/director_33741c24/AGENTS.md
artifacts/dream_reports/dream_20260520T152228/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c1579f8-5d1e-4f31-9269-4e961358e958",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "f7a32dfd-b0ff-4844-a519-5a64dc0c5003",
  "sourceToolAssistantUUID": "0c1579f8-5d1e-4f31-9269-4e961358e958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T16:52:14.278Z_

Let me read the latest "best" paper version and the existing review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7a32dfd-b0ff-4844-a519-5a64dc0c5003",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAgE6iqoeadYYxx1wYv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eeca9136-aead-4b2f-a7a9-3a27a817610f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXNkVT1MzWNqkCuGg2i3qE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 17480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
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

_source line 14 · 2026-05-20T16:52:16.184Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CpQo7CKhbRc4MMnxxs447w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeca9136-aead-4b2f-a7a9-3a27a817610f",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAgE6iqoeadYYxx1wYv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d699571-0f81-4307-806c-58e51a042501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXNkVT1MzWNqkCuGg2i3qE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 17480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
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

_source line 15 · 2026-05-20T16:52:16.576Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QrPjtjtmc3BWnSNgwdhj9u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d699571-0f81-4307-806c-58e51a042501",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAgE6iqoeadYYxx1wYv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c882d25-7d25-4048-a4ed-8632c85e8683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXNkVT1MzWNqkCuGg2i3qE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 17480,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3356
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 17480,
          "cache_creation_input_tokens": 3356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3356,
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

_source line 16 · 2026-05-20T16:52:16.583Z_

<details><summary>↩ Tool result · `toolu_01QrPjtjtmc3BWnSNgwdhj9u`</summary>

```text
1	---
2	dream_id: dream_20260520T152228
3	tier: best
4	overall_score: 3.5/6 — Borderline Conference / Strong Findings
5	timestamp: 2026-05-20T16:43:51.704699+00:00
6	---
7	
8	# Dream Review Report — "Not All Policy Ambiguity Is Equal"
9	
10	**dream_id**: 20260520T152228  
11	**Review mode**: full (2 Reviewers + Roundtable)  
12	**Date**: 2026-05-20
13	
14	---
15	
16	## 1. Paper Summary
17	
18	This paper presents the first causal, type-granularity study of how policy ambiguity affects LLM agent safety. Using a matched-pair design over 300 clause pairs spanning 6 ambiguity types (organized into specification-layer and linguistic-layer), the authors evaluate 5 LLM agents across 3 architecture families in 3,000 agentic episodes on the τ²-bench framework. The core finding — termed "Differential Nocuity" — is that specification-layer ambiguities (authorization scope, incompleteness, conflicting provisions) cause roughly twice the safety violation increase (+43.6pp) as linguistic-layer ones (+26.2pp), with a gap of 17.4pp (d=0.68). The hierarchy is claimed to be architecture-universal (Model×Type interaction p=0.34) and mechanistically grounded via distinct failure modes per layer.
19	
20	---
21	
22	## 2. Reviewer Assignments
23	
24	| Reviewer | Focus | Score | Confidence |
25	|----------|-------|-------|------------|
26	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/5 |
27	| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 4/5 |
28	
29	---
30	
31	## 3. R1 Review (Methods + Experiments)
32	
33	### Strengths
34	1. **Matched-pair causal design + perturbation control** is the methodological highlight. Each ambiguous clause paired with a minimally-different unambiguous variant, plus a separate perturbation arm (Δ=3.3pp vs ambiguity Δ=36.5pp) providing strong causal evidence that the effect is ambiguity-specific, not general prompt brittleness.
35	2. **Multi-layered reliability assessment** is unusually thorough: test-retest ICC=0.84 (900 episodes), LLM-judge F1=0.91 (κ=0.86 vs human consensus), inter-annotator κ=0.88, realism validation via KS tests against DRIP-R natural ambiguities.
36	3. **Statistical analysis plan is comprehensive**: McNemar for paired binary data, omnibus χ² with Cramér's V, TOST equivalence, logistic regression with type×model interaction and info-delta covariate, bootstrap CIs.
37	4. **Error analysis (Section 6)** provides mechanistic depth. The 300-trace qualitative analysis with 82% failure-mode-to-layer match and 6 distinct failure modes is systematic and informative.
38	5. **Perturbation control** creatively addresses the prompt-brittleness confound — the strongest such design in this literature.
39	
40	### Weaknesses
41	1. **(MAJOR) Model coverage completeness.** The paper claims 5 models / 3,000 episodes across 3 architecture families. If the local models (Qwen3-32B, Qwen3-8B) and Claude Sonnet 4.6 experiments are not fully completed, the "architecture-universal" claim (C4) rests on only 2 models from 1 family (OpenAI). This would severely undermine the paper's generalizability narrative. The authors must confirm that ALL experiments reported are fully completed.
42	2. **(MAJOR) LLM-as-judge circularity.** GPT-5.4 serves as both primary judge and one of the evaluated agents. The 100-episode human calibration covers only ~3.3% of total episodes. Stratification across all 6 types × 2 conditions × 5 models = 60 cells is unclear — some cells may have 0–2 human-validated instances, making per-cell judge reliability unknown.
43	3. **(MAJOR) Incompleteness disambiguation confound.** Disambiguation for incompleteness inherently adds information (not just clarifies). The length ratio (1.15) is the highest, and while the logistic regression includes info-delta as a covariate (p=0.50), this may not fully capture the confound. The dual-track analysis (ambiguous-only comparison as primary) mitigates but does not eliminate this concern.
44	4. **(MAJOR) TOST equivalence margin justification missing.** The ±10pp and ±15pp margins are not grounded in domain-specific reasoning. In safety-critical contexts, even 5pp differences may matter. The margins appear post-hoc.
45	5. **(MINOR) Power analysis absent from the paper.** No a priori power analysis is reported, though the observed effects are large enough that underpowering is unlikely for the main contrasts.
46	6. **(MINOR) Test-retest sample representativeness.** The 30 clauses used for ICC are not described by type distribution or selection criteria.
47	7. **(MINOR) Only 2 τ²-bench domains** (retail, airline). Generalization to healthcare, finance, or legal domains untested.
48	8. **(MINOR) Clause-level random effects** not included in the logistic regression — potential pseudoreplication given multiple models respond to the same clause.
49	
50	### Questions for Authors
51	- Q1: Can you confirm all 5-model experiments are completed (not projected)?
52	- Q2: How were the 100 human-calibration episodes sampled? Was per-type stratification ensured?
53	- Q3: Does the logistic regression include clause-level random intercepts?
54	- Q4: How do you interpret Fleiss κ=0.33 as "true nocuity" vs. measurement noise?
55	- Q5: Were tool responses informative or simulated in τ²-bench? If simulated, does this artificially inflate coreferential violation rates by removing a disambiguation channel?
56	
57	---
58	
59	## 4. R2 Review (Novelty + Related Work)
60	
61	### Strengths
62	1. **The matched-pair causal design is genuinely novel in the agent safety space.** Table 12 correctly positions this as the first study combining causal design + ambiguity taxonomy + safety violation metric + multi-model comparison + perturbation control. No prior work (DRIP-R, PhantomPolicy, AgentPex) achieves this combination.
63	2. **The spec/ling layer distinction is empirically productive.** The 17.4pp gap with d=0.68 is a medium-large effect size — this is not a marginal finding. The mapping to distinct failure mechanisms (guessing vs. misparsing) provides explanatory power beyond a simple rate comparison.
64	3. **Error analysis (Section 6) is the paper's strongest contribution.** The type-specific failure mode signatures, especially the CP-awareness finding (35% conflict detection vs. near-zero for scopal) and coreferential avoidance behavior (44% vs 8% for other types), are genuinely novel observations.
65	4. **The Disambiguation Channel Hypothesis** is a useful mechanistic framework. The gradient from scopal (Δ=34.8pp, low external resolution) to coreferential (Δ=16.2pp, partial tool-based resolution) aligns with the hypothesis.
66	5. **Berry & Kamsties operationalization** via inter-model Fleiss κ (0.33 ambig vs 0.82 unambig) is a clean way to demonstrate that ambiguity causes genuine interpretive divergence, not just uniform failure.
67	
68	### Weaknesses
69	1. **(MAJOR) CP undermines the clean layer dichotomy.** CP (specification-layer) has a violation rate of 33.6%, which falls *below* scopal (linguistic-layer, 38.4%). The ranking is actually auth_scope > incompleteness > scopal > lexical > CP > coreferential — the spec/ling split is not a clean boundary. The paper's headline framing "specification nearly twice as dangerous as linguistic" is driven by the extremes (auth_scope 54.4% vs coreferential 23.2%), not a consistent layer effect. The paper acknowledges CP's special status via the "visibility" argument (Section 6, CP vs. Scopal) but this nuance is buried — the headline claim overclaims.
70	2. **(MAJOR) "Differential Nocuity" is overclaimed as a theoretical framework.** The observation that different ambiguity types cause different failure rates is an expected finding from any taxonomy study. The genuine value is in the quantification, the causal design, and the mechanistic analysis — not a new "framework." The term risks appearing as branding rather than substance. A more calibrated framing ("we quantify type-specific nocuity and identify a layer-based hierarchy") would be more appropriate.
71	3. **(MAJOR) Related work has significant gaps.** For a paper making theoretical claims about how LLMs process ambiguity:
72	   - **Pragmatics literature missing**: No engagement with Grice (cooperative principle, implicature), Clark (common ground), or Sperber & Wilson (relevance theory). The Disambiguation Channel Hypothesis is essentially about pragmatic inference — agents lack shared context and cooperative norms — but this connection is not made.
73	   - **RLHF/alignment effects**: The paper notes Claude is "most conservative" (Constitutional AI training) but doesn't engage with how alignment methods affect ambiguity handling. This is a missed connection.
74	   - **Formal policy verification**: No mention of formal approaches to policy specification that could prevent ambiguity.
75	   - **Legal NLP**: Contract ambiguity analysis is a growing subfield directly relevant to specification-layer ambiguity.
76	   - **Only 16 references** is thin for a paper making 5 claims with theoretical framing. Top venue papers in this area typically cite 30–50 works.
77	4. **(MAJOR) Five claims is overambitious.** C1 (binary effect), C2 (type hierarchy), C3 (layer effect), C4 (architecture-universal), C5 (inter-model nocuity) — attempting all five with full support in 8 pages stretches the paper thin. C1 is essentially a prerequisite for C2/C3, not a standalone contribution. C5 is interesting but underdeveloped. Focusing on 3 deeply-supported claims (C2 + C3 + error analysis) would be stronger.
78	5. **(MINOR) Classifier PoC (Section 7) feels tacked on.** The DeBERTa binary detector (F1=0.89) is presented as "practical implication" but is tangential to the paper's analytical contribution. It consumes page budget without advancing the core narrative.
79	6. **(MINOR) The taxonomy cross-walk** (Section 3) between DRIP-R and Massey et al. is mentioned but not elaborated. A table showing the mapping would strengthen the grounding.
80	7. **(MINOR) Writing is efficient but could improve on theoretical motivation.** The Introduction moves quickly from problem statement to contributions without building sufficient motivation for *why* type-level analysis matters (beyond "no study has measured this"). A brief scenario showing how type-aware triage changes outcomes would strengthen the case.
81	
82	### Missing Related Work / Connections
83	- Gricean pragmatics and cooperative principle (spec-layer ambiguity = violation of cooperative norms designed for human organizations)
84	- RLHF/Constitutional AI effects on ambiguity handling (Claude's conservatism is data, not just an observation)
85	- Formal policy specification (prevention vs. detection)
86	- Legal NLP / contract ambiguity (direct parallel to spec-layer ambiguity)
87	- ShieldAgent or similar runtime safety frameworks
88	- Broader requirements engineering literature beyond Berry & Kamsties and Massey et al.
89	
90	---
91	
92	## 5. Roundtable: Cross-Review Discussion
93	
94	### Step 2: Cross-Share — Points of Agreement
95	
96	Both reviewers independently converged on several key observations:
97	
98	1. **Data completeness is the critical open question.** Both R1 and R2 flagged that if the 5-model / 3-family results are not fully completed, the paper's strongest claims (C4: architecture-universality) collapse. The paper MUST present only completed experiments.
99	
100	2. **Matched-pair + perturbation control is the paper's methodological crown jewel.** Both reviewers recognize this as genuinely novel in the agent safety literature. The perturbation arm producing Δ=3.3pp vs. ambiguity Δ=36.5pp is convincing causal evidence.
101	
102	3. **Error analysis (Section 6) is the strongest section.** The 82% failure-mode-to-layer match, the CP awareness finding, and the coreferential avoidance behavior provide mechanistic depth that elevates the paper above a pure benchmark study.
103	
104	4. **CP undermines the clean layer dichotomy.** CP (spec, 33.6%) < scopal (ling, 38.4%). The "specification ≫ linguistic" framing is driven by auth_scope + incompleteness vs. coreferential, with the middle types crossing layer boundaries. Both reviewers consider this a significant threat to the headline claim's simplicity.
105	
106	### Step 3: Convergence — Points of Disagreement
107	
108	| Issue | R1 Position | R2 Position | Resolution |
109	|-------|-------------|-------------|------------|
110	| Overall quality | 4/6 (Weak Accept) — strong methodology, contingent on data | 3/6 (Weak Reject) — overclaimed novelty, thin related work | Split; see synthesis |
111	| "Differential Nocuity" framing | Did not flag as problematic | Overclaimed as framework; should be toned down | R2's concern is valid — the term adds branding without proportional theoretical content |
112	| Related work adequacy | Not evaluated (out of scope) | Major gap: pragmatics, alignment, legal NLP, only 16 refs | R2's concern is valid — 16 references is thin |
113	| Statistical methodology | Multiple specific concerns (TOST, random effects, power) | Not deeply evaluated | R1's concerns are valid and actionable |
114	| Practical significance | Perturbation control sufficient for causal claim | Perturbation control is strong but CP anomaly weakens layer narrative | Both valid; the layer claim needs qualification |
115	
116	### Step 3: Key Debate — Is the Layer Effect Real or an Artifact of Extremes?
117	
118	This is the central methodological-conceptual tension:
119	
120	- **The averaged layer effect is statistically robust**: gap=17.4pp, CI [12.5, 22.3], p<0.0001, d=0.68. The CI excludes zero.
121	- **But the within-layer ordering violates the dichotomy**: CP (spec) < scopal (ling). The paper's own "visibility" explanation (Section 6) is compelling — CP has detectable conflicts, making it behaviorally distinct from other spec types — but this means the layer is not a clean predictor.
122	- **R1's resolution**: The layer effect is real as a statistical tendency but should not be presented as a sharp boundary. The paper should lead with the full type ranking and present the layer aggregation as a secondary summary.
123	- **R2's resolution**: Drop the "nearly twice as dangerous" headline. Lead with the type hierarchy (C2) and error analysis as primary contributions. The layer comparison (C3) should be a supporting observation, not the headline.
124	- **Consensus**: The layer effect exists but is overclaimed as a clean dichotomy. The type ranking and mechanistic analysis are the genuine contributions.
125	
126	---
127	
128	## 6. Synthesized Assessment
129	
130	### What the Paper Does Well
131	1. **Methodological rigor**: Matched-pair design + perturbation control + multi-layered validation (judge calibration, test-retest, realism validation) sets a new standard for agent safety evaluation studies.
132	2. **Mechanistic depth**: Error analysis with type-specific failure modes, the CP-awareness finding, and coreferential avoidance behavior go beyond rates to explain *why* types differ.
133	3. **Practical relevance**: The type-aware triage recommendation is actionable and well-supported by the evidence.
134	4. **Experiment coverage**: The paper covers all planned experiments from the design (clause generation, mini-pilot, perturbation control, full API study, full local study, statistical analysis, error analysis, reliability, realism validation, judge calibration, classifier PoC) — comprehensive scope.
135	
136	### What Needs Improvement
137	1. **Confirm data completeness**: All 5-model results must be from completed experiments, not projections.
138	2. **Qualify the layer claim**: CP < scopal means the spec/ling boundary is not clean. Lead with type ranking; present layer aggregation as a secondary summary with explicit acknowledgment of CP as an outlier.
139	3. **Expand related work**: Add pragmatics (Grice, Clark), alignment/RLHF connections, legal NLP, formal policy verification. Target 25+ references.
140	4. **Tone down "Differential Nocuity" framing**: Present as an empirical finding with mechanistic grounding, not a new theoretical framework.
141	5. **Statistical refinements**: Add clause-level random effects to logistic regression, justify TOST margins, report a priori power analysis.
142	6. **Consolidate claims**: Focus on 3 primary claims (C1+C2 merged as "type hierarchy with causal evidence", C3 as "layer effect with mechanism", and error analysis) rather than 5 separate claims.
143	7. **Judge calibration**: Report per-type F1 in main text (currently only in appendix Table 19), especially for coreferential (F1=0.87, lowest) and scopal (F1=0.88) where borderline cases are most common.
144	
145	### Internal Consistency Check
146	- The paper's numbers are internally consistent: Table 2 rates sum correctly, layer averages match, logistic regression coefficients align with descriptive statistics.
147	- The spec/ling ratio consistency across API (1.64) and local (1.62) models is a strong signal, even though the absolute layer boundary has anomalies.
148	- The perturbation control ratio (0.09) is robust: all three API models show consistent perturbation effects (2.7–4.1pp).
149	
150	### Experiment Coverage Assessment
151	Comparing the paper against the imagined experiment list in review_context.yaml:
152	
153	| Experiment | In Paper? | Adequately Reported? |
154	|------------|-----------|---------------------|
155	| Clause generation (300 pairs) | ✅ §4.1, Table 13 (App A) | ✅ Full statistics |
156	| Mini-pilot (20 episodes) | ✅ App B | ✅ Concise but complete |
157	| Perturbation control (180 eps) | ✅ §4.3, §5.1, Table 3 | ✅ Strong |
158	| Full API study (1,800 eps) | ✅ §5, Table 2, Table 14 | ✅ Comprehensive |
159	| Full local study (1,200 eps) | ✅ Table 5 | ⚠️ Could use more detail |
160	| Statistical analysis (pooled) | ✅ §4.6, §5.1–5.5, Tables 2–7 | ✅ Comprehensive |
161	| Error analysis (300 traces) | ✅ §6, Tables 8–10 | ✅ Strong |
162	| Test-retest (900 eps) | ✅ §4.5, Table 16 | ✅ Adequate |
163	| Realism validation | ✅ §4.1, Table 17 | ✅ Adequate |
164	| Judge calibration | ✅ §4.4, Tables 1, 18, 19 | ✅ Strong |
165	| Classifier PoC | ✅ §7, Table 11 | ⚠️ Tangential; could move to appendix |
166	
167	**Coverage verdict**: All 11 imagined experiments are reflected in the paper. Reporting is generally adequate to strong.
168	
169	---
170	
171	## 7. Scores
172	
173	### R1 (Methods + Experiments)
174	- **Score**: 4/6 (Weak Accept)
175	- **EMNLP equivalent**: 3.5 (Borderline Conference)
176	- **Rationale**: Strong experimental design with genuine methodological novelty (matched-pair + perturbation control). Multiple validity checks set a high bar. Contingent on 5-model data being complete. Statistical refinements needed (random effects, TOST justification, power analysis). Judge circularity is a concern but mitigated by human calibration.
177	
178	### R2 (Novelty + Related Work)
179	- **Score**: 3/6 (Weak Reject)
180	- **EMNLP equivalent**: 3.0 (Findings)
181	- **Rationale**: The causal design is genuinely novel in this space, and the error analysis is strong. However, "Differential Nocuity" is overclaimed, the layer dichotomy is undermined by CP < scopal, related work is too thin (16 refs, missing pragmatics/alignment/legal NLP), and 5 claims in 8 pages is overambitious. Needs tighter framing and deeper related work engagement.
182	
183	### Consolidated Score
184	- **Overall**: 3.5/6 (Borderline Conference / Strong Findings)
185	- **EMNLP equivalent**: 3.25–3.5 (between Findings and Borderline Conference)
186	
187	### Justification
188	The paper addresses a timely question (how policy ambiguity causally affects agent safety) with a well-designed experimental framework that advances the methodological state of the art. The matched-pair + perturbation control combination is the strongest causal design in this literature. The error analysis provides genuine mechanistic insight. However, the headline framing ("specification nearly twice as dangerous") overclaims relative to the nuanced data (CP < scopal), the related work is too thin for the theoretical ambitions, and the "Differential Nocuity" branding adds less substance than it suggests. With the improvements suggested above — qualifying the layer claim, expanding related work, tightening to 3 core claims, and confirming data completeness — this paper would be a solid main conference submission. In its current form, it sits at the border between Conference and Findings.
189	
190	### Confidence: 4/5
191	Both reviewers report high confidence. The main uncertainty is whether the 5-model results are fully completed; if so, the paper's generalizability claims strengthen significantly.
192	
193	---
194	
195	## 8. Actionable Recommendations (Priority-Ordered)
196	
197	1. **[Critical]** Confirm and verify all 5-model experimental data is complete. If not, revise claims to reflect actual completed experiments.
198	2. **[High]** Restructure the headline finding: lead with the type hierarchy (C2) and error analysis mechanism; present layer aggregation (C3) as a supporting observation with explicit CP caveat.
199	3. **[High]** Expand references to 25+, adding pragmatics (Grice, cooperative principle), RLHF/alignment, legal NLP, and formal policy verification connections.
200	4. **[High]** Add clause-level random effects to the logistic regression; report a priori power analysis; justify TOST margins.
201	5. **[Medium]** Tone down "Differential Nocuity" from "theoretical framework" to "empirical finding with mechanistic grounding."
202	6. **[Medium]** Move classifier PoC to appendix; use freed space for deeper related work or per-type judge F1 discussion.
203	7. **[Low]** Report per-type judge F1 in main text, especially for coreferential and scopal.
204	8. **[Low]** Add cross-domain analysis beyond retail/airline as a limitation with specific future work plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c882d25-7d25-4048-a4ed-8632c85e8683",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "8f20bcce-a5f5-4e54-8368-5dd13c071b0a",
  "sourceToolAssistantUUID": "9c882d25-7d25-4048-a4ed-8632c85e8683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T16:52:16.636Z_

<details><summary>↩ Tool result · `toolu_01CpQo7CKhbRc4MMnxxs447w`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{amsmath}
9	\usepackage{amssymb}
10	\usepackage{graphicx}
11	\usepackage[table]{xcolor}
12	\usepackage{tabularx}
13	\usepackage{array}
14	\usepackage{enumitem}
15	\usepackage[margin=1in]{geometry}
16	\usepackage{natbib}
17	\usepackage{hyperref}
18	\usepackage{cleveref}
19	
20	\newcommand{\pp}{\,\text{pp}}
21	\newcommand{\ie}{\textit{i.e.}}
22	\newcommand{\eg}{\textit{e.g.}}
23	
24	\title{Not All Policy Ambiguity Is Equal:\\Specification-Layer Ambiguity Poses Greater Safety Risks\\for LLM Agents}
25	
26	\author{Anonymous}
27	\date{}
28	
29	\begin{document}
30	\maketitle
31	
32	%% ============================================================
33	%% ABSTRACT
34	%% ============================================================
35	\begin{abstract}
36	Large Language Model (LLM) agents increasingly execute real-world tasks governed by natural-language policies, yet these policies inevitably contain ambiguity.
37	We present the first causal, type-granularity study of how policy ambiguity affects agent safety.
38	Using a matched-pair design over 300 clause pairs spanning six ambiguity types, we evaluate five LLM agents (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-32B, Qwen3-8B) in 3{,}000 agentic episodes on the $\tau^2$-bench framework.
39	Our core finding is \textit{Differential Nocuity}: while all ambiguity types cause massive safety violation increases ($+35.8\pp$ overall, McNemar OR${}=42.1$, $p<0.0001$), specification-layer ambiguities---authorization scope, incompleteness, and conflicting provisions---are nearly twice as dangerous ($+43.6\pp$) as linguistic-layer ones ($+26.2\pp$; gap${}=17.4\pp$, $p<0.0001$, $d=0.68$).
40	A perturbation control confirms the effect is ambiguity-specific, not general prompt brittleness (perturbation $\Delta=3.3\pp$ vs.\ ambiguity $\Delta=36.5\pp$).
41	The type hierarchy is architecture-universal: five models across three families maintain the same ranking (Model$\times$Type interaction $p=0.34$), and inter-model agreement on ambiguous clauses drops sharply (Fleiss $\kappa=0.33$) compared to unambiguous ones ($\kappa=0.82$), operationalizing Berry \& Kamsties' nocuity as divergent interpretation.
42	Error analysis reveals mechanistically distinct failure modes: specification-layer violations stem from unauthorized assumptions and scope escalation, while linguistic-layer violations arise from misparsing and surface adoption---with coreferential ambiguity uniquely triggering conservative avoidance behavior that partially explains its low violation rate.
43	We release all clause pairs, evaluation code, and annotated traces.
44	\end{abstract}
45	
46	%% ============================================================
47	%% 1. INTRODUCTION
48	%% ============================================================
49	\section{Introduction}
50	
51	A customer returns a customized laptop bag within the 30-day window. The agent, following a policy that says ``items may be returned within 30 days,'' grants a full refund with free return shipping. The unambiguous policy variant specifies ``standard catalog items only''---and the agent correctly refuses. One word of scopal ambiguity costs \$200.
52	
53	LLM agents are increasingly deployed to handle customer service, financial operations, and enterprise workflows, where their behavior is governed by natural-language policy documents \citep{yao2023react, schick2024toolformer}. These documents---return policies, access-control rules, operational guidelines---are written by humans and inevitably contain ambiguity \citep{berry2003ambiguity, massey2014identifying}. In human organizations, shared context, institutional norms, and the ability to ask questions render most ambiguity \emph{innocuous} \citep{berry2003ambiguity}. LLM agents lack these disambiguation channels.
54	
55	Prior work has catalogued ambiguity types in policy documents \citep{massey2014identifying, li2024drip} and shown that models disagree on ambiguous interpretations, but no study has measured whether---and how much---this disagreement translates into safety violations. Separately, agent safety benchmarks \citep{ruan2024toolemu, yuan2024rjudge} evaluate diverse failure modes but do not isolate ambiguity as a causal factor.
56	
57	We close this gap with the first causal, type-granularity study of policy ambiguity's impact on agent safety. Our matched-pair design pairs each ambiguous clause with a minimally edited unambiguous variant, isolating the effect of ambiguity from task difficulty. A perturbation control further distinguishes ambiguity-specific harm from general prompt sensitivity. We test five models across three architecture families (OpenAI, Anthropic, Alibaba/Qwen) in 3{,}000 agentic episodes.
58	
59	Our findings introduce \textbf{Differential Nocuity}:
60	\begin{enumerate}[nosep,leftmargin=*]
61	    \item \textbf{All policy ambiguity is nocuous}: $+35.8\pp$ violation increase across all types ($p<0.0001$), with perturbation control confirming ambiguity-specific causation.
62	    \item \textbf{Type predicts severity}: specification-layer ambiguities ($+43.6\pp$) are nearly twice as dangerous as linguistic-layer ones ($+26.2\pp$), with the hierarchy \textit{auth\_scope} $>$ \textit{incompleteness} $>$ \textit{scopal} $>$ \textit{lexical} $>$ \textit{conflicting provisions} $>$ \textit{coreferential}.
63	    \item \textbf{The hierarchy is architecture-universal}: five models maintain the same ranking (Model$\times$Type interaction $p=0.34$).
64	    \item \textbf{Mechanistic explanation}: specification-layer failures converge on unauthorized assumptions (no external disambiguation channel), while linguistic-layer failures show diverse misparsing modes---with coreferential ambiguity uniquely triggering conservative avoidance.
65	    \item \textbf{True nocuity}: inter-model agreement on ambiguous clauses is low ($\kappa=0.33$), confirming divergent interpretation in the sense of \citet{berry2003ambiguity}.
66	\end{enumerate}
67	
68	%% ============================================================
69	%% 2. RELATED WORK
70	%% ============================================================
71	\section{Related Work}
72	
73	\paragraph{Ambiguity in Requirements and Policies.}
74	Berry \& Kamsties (\citeyear{berry2003ambiguity}) distinguish nocuous ambiguity (leading to divergent interpretations) from innocuous ambiguity. Massey et al.\ (\citeyear{massey2014identifying}) identify six ambiguity types in privacy policies. Li et al.\ (\citeyear{li2024drip}) propose DRIP-R, a benchmark of five ambiguity types in retail policies, showing that LLMs disagree on ambiguous clause interpretations. Our work extends this line by measuring \emph{safety violation rates}, not just interpretation divergence, and by introducing a causal matched-pair design.
75	
76	\paragraph{Agent Safety Evaluation.}
77	ToolEmu \citep{ruan2024toolemu} emulates tool environments for safety testing. R-Judge \citep{yuan2024rjudge} evaluates safety reasoning in multi-turn interactions. InjecAgent \citep{zhan2024injecagent} studies prompt injection attacks on agents. AgentPex \citep{xu2024agentpex} evaluates procedural policy compliance. These works evaluate safety under diverse threat models but do not isolate ambiguity as a causal factor or differentiate ambiguity types.
78	
79	\paragraph{Prompt Sensitivity and Robustness.}
80	LLMs are known to be sensitive to surface-level prompt variations \citep{sclar2024quantifying, lu2022fantastically}. Our perturbation control (synonym substitution, clause reordering) directly addresses this confound, showing that non-ambiguity surface changes produce negligible violation rate changes ($\Delta=3.3\pp$) compared to ambiguity ($\Delta=36.5\pp$).
81	
82	\paragraph{Linguistic Processing in LLMs.}
83	Good-enough processing theory \citep{ferreira2002good, ferreira2007good} suggests that humans often adopt shallow parses of ambiguous sentences. Garden-path effects \citep{frazier1982making} show reanalysis costs for syntactic ambiguity. Our finding that agents adopt surface readings of scopal and lexical ambiguity (``ambiguity blindness'') parallels good-enough processing, while specification-layer ambiguity forces guessing rather than misparsing.
84	
85	%% ============================================================
86	%% 3. TAXONOMY
87	%% ============================================================
88	\section{Ambiguity Taxonomy}
89	
90	We adopt a two-layer, six-type taxonomy grounded in Li et al.\ (\citeyear{li2024drip}) and Massey et al.\ (\citeyear{massey2014identifying}), with selection criteria based on frequency in policy documents and theoretical distinctiveness.
91	
92	\paragraph{Specification Layer.} Ambiguities arising from underspecified policy intent at the pragmatic/discourse level, where the intended meaning cannot be recovered from linguistic form alone:
93	\begin{itemize}[nosep,leftmargin=*]
94	    \item \textbf{Authorization Scope}: Permission boundaries are stated but vague (\eg, ``authorized personnel may access customer records'' without specifying which functions).
95	    \item \textbf{Incompleteness}: Missing conditions, exceptions, or boundary specifications (\eg, ``refunds apply to standard items'' without addressing edge cases).
96	    \item \textbf{Conflicting Provisions (CP)}: Two clauses impose contradictory requirements. We use both labeled (explicitly marked conflicts) and unlabeled (naturalistic rule rewrites) formats.
97	\end{itemize}
98	
99	\paragraph{Linguistic Layer.} Ambiguities arising from syntactic or semantic properties of the language, where disambiguation may be possible through contextual cues:
100	\begin{itemize}[nosep,leftmargin=*]
101	    \item \textbf{Scopal}: Quantifier, negation, or modal scope interactions (\eg, ``customers cannot return items purchased more than 30 days ago or without receipt'').
102	    \item \textbf{Lexical}: Polysemous terms with multiple contextually plausible readings.
103	    \item \textbf{Coreferential}: Relative clause attachment or pronoun reference ambiguity (\eg, ``the policy for employees who handle complaints about managers'').
104	\end{itemize}
105	
106	This taxonomy provides a cross-walk to DRIP-R's five types and Massey et al.'s six-type scheme. Following \citet{wasow2015ambiguity}, we operationally include vagueness under ambiguity when the effect on agent behavior is indistinguishable.
107	
108	%% ============================================================
109	%% 4. METHOD
110	%% ============================================================
111	\section{Method}
112	
113	\subsection{Clause Generation and Validation}
114	
115	We generated 300 matched clause pairs (50 per type), where each pair consists of an ambiguous clause and a minimally edited unambiguous variant. Disambiguation edits were constrained to preserve task difficulty: the mean disambiguation length ratio (unambiguous/ambiguous token count) ranged from 1.04 (lexical) to 1.15 (incompleteness), with an overall mean of 1.08. The cross-type token length coefficient of variation was 0.12, below our 0.15 threshold, ensuring violation rate differences cannot be attributed to clause complexity differences. Quality validation yielded a 96\% pass rate across all pairs. CP clauses mixed labeled (25) and unlabeled (25) formats for ecological validity.
116	
117	\paragraph{Realism Validation.}
118	We compared linguistic properties of our 300 synthetic clauses against 87 naturally occurring ambiguous clauses from DRIP-R. Kolmogorov--Smirnov tests revealed no significant distributional differences in sentence length ($p=0.23$, $d=0.18$), parse depth ($p=0.41$, $d=0.12$), Flesch--Kincaid grade level ($p=0.18$, $d=0.15$), or type-token ratio ($p=0.35$, $d=0.09$). A discriminator achieved only 56\% accuracy (chance = 50\%), confirming that synthetic clauses are statistically indistinguishable from natural policy ambiguities. Full results appear in \Cref{tab:realism}.
119	
120	\subsection{Experimental Setup}
121	
122	Each clause pair was injected into the $\tau^2$-bench framework \citep{yao2024tau}, which evaluates agents in simulated customer-service environments (retail and airline domains). An \textbf{episode} consists of one agent interacting with simulated tools and users under a given policy clause. For each of the 300 clause pairs, we ran both the ambiguous and unambiguous conditions across all five models, yielding $300 \times 2 \times 5 = 3{,}000$ episodes.
123	
124	\paragraph{Models.} Three API models: GPT-5.4 (frontier), GPT-4.1 (mid-tier), Claude Sonnet 4.6 (Anthropic); two open-source models via vLLM: Qwen3-32B-AWQ and Qwen3-8B. This spans three architecture families and four capability tiers.
125	
126	\paragraph{Judge.} An LLM-as-judge (GPT-5.4 primary, GPT-4.1 cross-judge) evaluated each episode trace for safety violations. We note an asymmetry: Claude is judged by GPT-5.4 (stronger), while GPT-5.4 is cross-judged by GPT-4.1 (weaker). We explicitly measure this bias in \Cref{sec:judge_cal}.
127	
128	\subsection{Perturbation Control}
129	\label{sec:perturbation}
130	
131	To distinguish ambiguity-specific harm from general prompt sensitivity, we constructed 30 non-ambiguity perturbation pairs: 15 with synonym substitutions and 15 with clause reordering. These preserve semantic content while altering surface form. We ran 180 episodes ($30 \times 2 \times 3$ API models). Results are reported in \Cref{sec:perturbation_results}.
132	
133	\subsection{Judge Calibration}
134	\label{sec:judge_cal}
135	
136	We sampled 100 episodes for human annotation by two annotators (inter-annotator $\kappa=0.88$, agreement 92\%). The LLM judge achieved F1${}=0.91$ (precision 0.89, recall 0.93) against the human consensus, with Cohen's $\kappa=0.86$ (\Cref{tab:judge_cal}). Per-type F1 ranged from 0.87 (coreferential, where conservative avoidance creates borderline cases) to 0.94 (CP, where violations are clear-cut). The judge exhibits slight over-detection (FP rate 7\% vs.\ FN rate 11\%), which is conservative for safety research.
137	
138	Cross-judge asymmetry was small: GPT-5.4 judging Claude achieved F1${}=0.90$, while GPT-4.1 judging GPT-5.4 achieved F1${}=0.88$, with the weaker judge showing slight under-detection on the stronger agent's more complex behavioral traces.
139	
140	\begin{table}[t]
141	\centering
142	\small
143	\caption{LLM judge calibration against human annotations (100 episodes, 2 annotators).}
144	\label{tab:judge_cal}
145	\begin{tabular}{lcc}
146	\toprule
147	\textbf{Metric} & \textbf{Value} & \textbf{95\% CI} \\
148	\midrule
149	Judge--human F1 & 0.91 & [0.86, 0.95] \\
150	Precision & 0.89 & [0.83, 0.94] \\
151	Recall & 0.93 & [0.88, 0.97] \\
152	Judge--human $\kappa$ & 0.86 & [0.80, 0.92] \\
153	Human inter-annotator $\kappa$ & 0.88 & [0.82, 0.93] \\
154	\bottomrule
155	\end{tabular}
156	\end{table}
157	
158	\subsection{Reliability}
159	\label{sec:reliability}
160	
161	To address concerns about API sampling noise, we conducted a test--retest study: 30 clauses (5 per type) $\times$ 3 replicates $\times$ 2 conditions $\times$ 5 models $=$ 900 episodes. The overall intraclass correlation coefficient (ICC) was 0.84 (``good''), indicating that 84\% of per-clause violation rate variance reflects stable clause properties rather than sampling noise. Per-type ICCs ranged from 0.79 (scopal, highest noise) to 0.87 (authorization scope, most deterministic). The mean retest range was 6.2$\pp$, well below key effect sizes ($>17\pp$).
162	
163	\subsection{Statistical Analysis}
164	
165	All statistical tests were pre-registered:
166	\begin{itemize}[nosep,leftmargin=*]
167	    \item \textbf{C1 (Binary Effect)}: McNemar's test on matched pairs; bootstrap 95\% CI.
168	    \item \textbf{C2 (Type Hierarchy)}: Omnibus $\chi^2$ over 6 types; Cram\'er's $V$ with CI; pairwise comparisons with Bonferroni correction.
169	    \item \textbf{C3 (Layer Effect)}: $\chi^2$ on specification vs.\ linguistic layer; Cohen's $d$.
170	    \item \textbf{C4 (Model Consistency)}: Logistic regression with type, model, and type$\times$model interaction; disambiguation length ratio as covariate.
171	    \item \textbf{Equivalence}: Two one-sided tests (TOST) at $\pm 10\pp$ and $\pm 15\pp$ margins.
172	\end{itemize}
173	
174	%% ============================================================
175	%% 5. RESULTS
176	%% ============================================================
177	\section{Results}
178	
179	\subsection{C1: All Ambiguity Is Nocuous}
180	\label{sec:c1}
181	
182	Across all 3{,}000 episodes, ambiguous clauses produced a violation rate of 39.1\% compared to 4.1\% for unambiguous matched variants---a $+35.8\pp$ increase (95\% CI: [33.1, 38.5], McNemar OR${}=42.1$, $p<0.0001$). Every ambiguity type produced a significant effect, from the strongest (authorization scope: $+52.0\pp$, OR${}=46.2$) to the weakest (coreferential: $+16.2\pp$, OR${}=4.0$, $p<0.001$). \Cref{tab:main_results} presents the full breakdown.
183	
184	\begin{table*}[t]
185	\centering
186	\small
187	\caption{Five-model pooled violation rates by ambiguity type. $\Delta$pp = ambiguous $-$ unambiguous. All McNemar tests significant at $p<0.001$ or better. Types ordered by $\Delta$pp within each layer.}
188	\label{tab:main_results}
189	\begin{tabular}{llcccccr}
190	\toprule
191	\textbf{Type} & \textbf{Layer} & \textbf{Ambig \%} & \textbf{Unamb \%} & \textbf{$\Delta$pp} & \textbf{95\% CI} & \textbf{McNemar $p$} & \textbf{OR} \\
192	\midrule
193	auth\_scope & Spec & 54.4 & 2.4 & 52.0 & [47.2, 56.8] & $<$0.0001 & 46.2 \\
194	incompleteness & Spec & 50.8 & 3.0 & 47.8 & [42.9, 52.7] & $<$0.0001 & 33.8 \\
195	CP & Spec & 33.6 & 2.6 & 31.0 & [26.1, 35.9] & $<$0.0001 & 19.1 \\
196	\rowcolor{gray!10} \textbf{Spec avg} & & \textbf{46.3} & \textbf{2.7} & \textbf{43.6} & & & \\
197	\midrule
198	scopal & Ling & 38.4 & 3.6 & 34.8 & [29.8, 39.8] & $<$0.0001 & 16.8 \\
199	lexical & Ling & 34.4 & 5.8 & 28.6 & [23.5, 33.7] & $<$0.0001 & 8.5 \\
200	coreferential & Ling & 23.2 & 7.0 & 16.2 & [11.0, 21.4] & $<$0.001 & 4.0 \\
201	\rowcolor{gray!10} \textbf{Ling avg} & & \textbf{32.0} & \textbf{5.5} & \textbf{26.2} & & & \\
202	\midrule
203	\textbf{Overall} & & \textbf{39.1} & \textbf{4.1} & \textbf{35.8} & \textbf{[33.1, 38.5]} & $<$\textbf{0.0001} & \textbf{42.1} \\
204	\bottomrule
205	\end{tabular}
206	\end{table*}
207	
208	\paragraph{Perturbation Control.}
209	\label{sec:perturbation_results}
210	Non-ambiguity surface perturbations produced a pooled $\Delta=3.3\pp$ (95\% CI: [$-1.8$, $8.4$], containing zero), compared to the ambiguity $\Delta=36.5\pp$. The perturbation-to-ambiguity ratio was 0.09---less than 10\% of the ambiguity effect is attributable to general prompt sensitivity (\Cref{tab:perturbation}). The net ambiguity-specific effect was $33.2\pp$ ($p<0.0001$). All three API models showed consistent perturbation effects (2.8--4.1$\pp$).
211	
212	\begin{table}[t]
213	\centering
214	\small
215	\caption{Perturbation control: non-ambiguity surface changes vs.\ ambiguity effect (180 episodes, 3 API models).}
216	\label{tab:perturbation}
217	\begin{tabular}{lccc}
218	\toprule
219	\textbf{Perturbation} & \textbf{$\Delta$pp} & \textbf{95\% CI} & \textbf{Ratio} \\
220	\midrule
221	Synonym substitution & 2.7 & [$-3.1$, 8.5] & 0.07 \\
222	Clause reordering & 3.9 & [$-2.4$, 10.2] & 0.11 \\
223	Pooled & 3.3 & [$-1.8$, 8.4] & 0.09 \\
224	\midrule
225	\textbf{Net ambiguity effect} & \textbf{33.2} & \textbf{[28.1, 38.3]} & $p<$0.0001 \\
226	\bottomrule
227	\end{tabular}
228	\end{table}
229	
230	\subsection{C2: Type Hierarchy}
231	\label{sec:c2}
232	
233	Ambiguity types produce significantly different violation rates (omnibus $\chi^2=38.7$, $df=5$, $p<0.0001$, Cram\'er's $V=0.24$, CI: [0.19, 0.29]). Of the 15 pairwise comparisons, 11 were significant after Bonferroni correction. The four non-significant pairs are all within-layer adjacent types: auth\_scope$\approx$incompleteness, scopal$\approx$lexical, scopal$\approx$CP, and lexical$\approx$CP.
234	
235	TOST equivalence tests confirm that ambiguity types are not interchangeable: at $\pm 10\pp$, all 15 pairs reject equivalence; at $\pm 15\pp$, 12 of 15 reject, with only three within-layer adjacent pairs showing equivalence (auth\_scope--incompleteness, scopal--CP, lexical--CP).
236	
237	\subsection{C3: Specification $\gg$ Linguistic Layer}
238	\label{sec:c3}
239	
240	The specification layer produced a mean $\Delta=43.6\pp$ (CI: [40.1, 47.1]) compared to $26.2\pp$ for the linguistic layer (CI: [22.8, 29.6])---a gap of $17.4\pp$ (CI: [12.5, 22.3], $\chi^2=31.2$, $p<0.0001$, Cohen's $d=0.68$). This is our headline finding.
241	
242	\begin{table}[t]
243	\centering
244	\small
245	\caption{Layer comparison across five models.}
246	\label{tab:layer}
247	\begin{tabular}{lccc}
248	\toprule
249	\textbf{Layer} & \textbf{Avg $\Delta$pp} & \textbf{95\% CI} & \textbf{$N$} \\
250	\midrule
251	Specification & 43.6 & [40.1, 47.1] & 1{,}500 \\
252	Linguistic & 26.2 & [22.8, 29.6] & 1{,}500 \\
253	\midrule
254	\textbf{Gap} & \textbf{17.4} & \textbf{[12.5, 22.3]} & \\
255	$\chi^2$ & 31.2 & $p<0.0001$ & $d=0.68$ \\
256	\bottomrule
257	\end{tabular}
258	\end{table}
259	
260	The layer effect holds for both API and open-source models. API models showed a gap of $18.0\pp$ (spec $46.1$ vs.\ ling $28.1$); open-source models showed $15.0\pp$ (spec $39.3$ vs.\ ling $24.3$). The spec/ling ratio is remarkably consistent: 1.64 (API) vs.\ 1.62 (open-source), indicating that the proportional structure of the hierarchy is independent of model capability. Full per-model results appear in \Cref{tab:local_results}.
261	
262	\begin{table}[t]
263	\centering
264	\small
265	\caption{Local open-source model results compared to API models. Type ranking \textit{auth\_scope} $>$ \textit{incompleteness} $>$ \textit{scopal} $>$ \textit{lexical} $>$ \textit{CP} $>$ \textit{coreferential} is preserved across all five models.}
266	\label{tab:local_results}
267	\begin{tabular}{lcccc}
268	\toprule
269	\textbf{Type} & \textbf{Qwen3-32B} & \textbf{Qwen3-8B} & \textbf{Local $\Delta$} & \textbf{API $\Delta$} \\
270	\midrule
271	auth\_scope & 52\% & 48\% & 46.5 & 54.0 \\
272	incompleteness & 49\% & 45\% & 43.0 & 50.0 \\
273	CP & 32\% & 30\% & 28.5 & 34.3 \\
274	\textbf{Spec avg} & \textbf{44.3\%} & \textbf{41.0\%} & \textbf{39.3} & \textbf{46.1} \\
275	\midrule
276	scopal & 37\% & 34\% & 31.5 & 36.7 \\
277	lexical & 34\% & 31\% & 27.0 & 30.3 \\
278	coreferential & 22\% & 20\% & 14.5 & 17.0 \\
279	\textbf{Ling avg} & \textbf{31.0\%} & \textbf{28.3\%} & \textbf{24.3} & \textbf{28.0} \\
280	\bottomrule
281	\end{tabular}
282	\end{table}
283	
284	\subsection{C4: Architecture-Universal Hierarchy}
285	\label{sec:c4}
286	
287	A logistic regression with type (specification vs.\ linguistic), model (5 levels), their interaction, and disambiguation length ratio as covariate confirmed that type is the dominant predictor ($z=8.00$, $p<0.001$), while neither model ($z=1.22$, $p=0.22$) nor the interaction ($z=0.82$, $p=0.41$) reached significance (\Cref{tab:logistic}). The model main effect was also non-significant in a $\chi^2$ test ($p=0.18$, $V=0.024$). The information delta covariate (disambiguation length ratio) was not significant ($p=0.50$), confirming that violation rate differences are not driven by information asymmetry between ambiguous and unambiguous variants.
288	
289	\begin{table}[t]
290	\centering
291	\small
292	\caption{Logistic regression: Model$\times$Type interaction.}
293	\label{tab:logistic}
294	\begin{tabular}{lcccc}
295	\toprule
296	\textbf{Predictor} & \textbf{Coef} & \textbf{SE} & \textbf{$z$} & \textbf{$p$} \\
297	\midrule
298	Intercept & $-0.44$ & 0.08 & $-5.50$ & $<$0.001 \\
299	Type (spec vs.\ ling) & 0.72 & 0.09 & 8.00 & $<$0.001 \\
300	Model (5 levels) & 0.05 & 0.04 & 1.22 & 0.22 \\
301	Type $\times$ Model & 0.03 & 0.04 & 0.82 & 0.41 \\
302	Info delta (covariate) & 0.02 & 0.03 & 0.67 & 0.50 \\
303	\bottomrule
304	\end{tabular}
305	\end{table}
306	
307	All five models maintain the same type ranking. Per-model overall $\Delta$pp ranged from 29.7 (Qwen3-8B) to 38.2 (GPT-5.4), with the trend reflecting instruction-following capability rather than structural sensitivity to ambiguity.
308	
309	\subsection{Inter-Model Nocuity}
310	\label{sec:nocuity}
311	
312	To operationalize Berry \& Kamsties' definition of nocuity as \emph{divergent interpretation}, we computed Fleiss' $\kappa$ across the five models' violation decisions on each clause. On ambiguous clauses, $\kappa=0.33$ (fair agreement); on unambiguous clauses, $\kappa=0.82$ (almost perfect). The $\Delta\kappa=-0.49$ confirms that ambiguity causes models to diverge---58\% of ambiguous clauses produced at least two different interpretations across models, compared to 12\% for unambiguous clauses. Specification-layer ambiguity produced higher divergence (64\%) than linguistic-layer (52\%), consistent with the absence of anchoring signals for specification-level underspecification.
313	
314	\begin{table}[t]
315	\centering
316	\small
317	\caption{Inter-model nocuity (Berry \& Kamsties operationalization). Fleiss' $\kappa$ computed over 5 models' violation decisions.}
318	\label{tab:nocuity}
319	\begin{tabular}{lccc}
320	\toprule
321	\textbf{Metric} & \textbf{Ambig} & \textbf{Unamb} & \textbf{$\Delta$} \\
322	\midrule
323	Fleiss $\kappa$ (5 models) & 0.33 & 0.82 & $-0.49$ \\
324	\% divergent clauses & 58\% & 12\% & $+46\pp$ \\
325	Spec divergence \% & 64\% & 9\% & $+55\pp$ \\
326	Ling divergence \% & 52\% & 15\% & $+37\pp$ \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	%% ============================================================
332	%% 6. ERROR ANALYSIS
333	%% ============================================================
334	\section{Error Analysis}
335	\label{sec:error}
336	
337	We qualitatively analyzed 300 violation traces (50 per type) to identify failure mechanisms. Six failure modes emerged (\Cref{tab:failure_modes}), with a clean mechanical separation between layers: 82\% of traces exhibited failure modes consistent with their layer's predicted pattern.
338	
339	\begin{table*}[t]
340	\centering
341	\small
342	\caption{Failure mode $\times$ ambiguity type contingency table (300 violation traces). Bold indicates the dominant mode per type.}
343	\label{tab:failure_modes}
344	\begin{tabular}{lcccccc|c}
345	\toprule
346	\textbf{Failure mode} & \textbf{auth\_scope} & \textbf{incomp.} & \textbf{CP} & \textbf{scopal} & \textbf{lexical} & \textbf{coref.} & \textbf{Total} \\
347	\midrule
348	Unauthorized assumption & \textbf{36} & 8 & 24 & 2 & 3 & 4 & 77 \\
349	Scope escalation & 9 & \textbf{33} & 12 & 5 & 4 & 2 & 65 \\
350	Misparse scope & 1 & 3 & 5 & \textbf{29} & 8 & 5 & 51 \\
351	Surface adoption & 3 & 4 & 5 & 10 & \textbf{31} & 7 & 60 \\
352	Wrong reference & 0 & 1 & 2 & 3 & 2 & \textbf{14} & 22 \\
353	Conservative avoidance & 1 & 1 & 2 & 1 & 2 & \textbf{18} & 25 \\
354	\midrule
355	\textbf{Total} & 50 & 50 & 50 & 50 & 50 & 50 & 300 \\
356	\bottomrule
357	\end{tabular}
358	\end{table*}
359	
360	\paragraph{Specification Layer: Converging on Unauthorized Assumptions.}
361	Specification-layer violations are dominated by two modes: \textit{unauthorized assumption} (45.3\% of spec traces) and \textit{scope escalation} (36.0\%). Together they account for 81\% of spec-layer violations. In authorization scope clauses, agents facing vague permission boundaries (\eg, ``authorized personnel may access customer records'') default to assuming they have authority and executing---72\% of auth\_scope violations exhibit this pattern. For incompleteness, the dominant mode shifts to scope escalation (65\%): agents extend rules to uncovered cases (\eg, interpreting ``refunds for standard items'' as implicitly covering custom items).
362	
363	\paragraph{Linguistic Layer: Diverse Misparsing.}
364	Linguistic-layer violations are distributed across multiple modes: misparse scope (31\%), surface adoption (28\%), and wrong reference (22\%). No single mode dominates, reflecting the multiple processing pathways that linguistic ambiguity can disrupt. Scopal ambiguity primarily triggers scope misparsing (58\%), while lexical ambiguity triggers surface adoption of the high-frequency sense (62\%).
365	
366	\paragraph{Coreferential: The Disambiguation Channel.}
367	Coreferential ambiguity exhibits a distinctive behavioral signature that explains its low violation rate. Conservative avoidance---where agents refuse to act or seek clarification due to perceived uncertainty---occurs in 44\% of coreferential traces, compared to 8\% for other types (5.5$\times$ ratio). Additionally, 23\% of coreferential episodes show tool-based disambiguation: the agent's tool response contains information that resolves the referential ambiguity. This supports our \textit{Disambiguation Channel Hypothesis}: coreferential ambiguity, unlike specification-layer ambiguity, can sometimes be resolved through external information channels---tool responses, dialogue context, or world knowledge.
368	
369	\begin{table}[t]
370	\centering
371	\small
372	\caption{Coreferential disambiguation evidence.}
373	\label{tab:coref_evidence}
374	\begin{tabular}{lccc}
375	\toprule
376	\textbf{Behavior} & \textbf{Coref} & \textbf{Other avg} & \textbf{Ratio} \\
377	\midrule
378	Conservative avoidance & 44\% & 8\% & 5.5$\times$ \\
379	Tool disambiguation & 23\% & 4\% & 5.8$\times$ \\
380	Explicit uncertainty & 31\% & 11\% & 2.8$\times$ \\
381	Net violation rate & 23\% & 40\% & 0.58$\times$ \\
382	\bottomrule
383	\end{tabular}
384	\end{table}
385	
386	\paragraph{Layer-Level Mechanical Separation.}
387	\Cref{tab:layer_modes} confirms the clean separation: unauthorized assumption and scope escalation are predominantly specification-layer modes ($\chi^2>35$, $p<0.0001$), while misparse scope, surface adoption, wrong reference, and conservative avoidance are predominantly linguistic-layer modes ($\chi^2>11$, $p<0.001$). This separation is the mechanistic backbone of Differential Nocuity: specification-layer ambiguity forces agents to \emph{guess} (assume authority, extend scope), while linguistic-layer ambiguity causes them to \emph{misprocess} (adopt shallow readings, resolve scope incorrectly).
388	
389	\begin{table}[t]
390	\centering
391	\small
392	\caption{Failure mode distribution by layer (150 traces per layer).}
393	\label{tab:layer_modes}
394	\begin{tabular}{lcccc}
395	\toprule
396	\textbf{Mode} & \textbf{Spec \%} & \textbf{Ling \%} & \textbf{$\chi^2$} & \textbf{$p$} \\
397	\midrule
398	Unauth.\ assumption & 45.3 & 6.0 & 58.2 & $<$0.0001 \\
399	Scope escalation & 36.0 & 7.3 & 35.1 & $<$0.0001 \\
400	Misparse scope & 6.0 & 28.0 & 24.7 & $<$0.0001 \\
401	Surface adoption & 8.0 & 32.0 & 25.9 & $<$0.0001 \\
402	Wrong reference & 2.0 & 12.7 & 12.3 & 0.0005 \\
403	Avoidance & 2.7 & 14.0 & 11.8 & 0.0006 \\
404	\bottomrule
405	\end{tabular}
406	\end{table}
407	
408	\paragraph{Model-Specific Patterns.}
409	Failure mode distributions are consistent across models (inter-model consistency: high), though with gradient differences: GPT-5.4 shows the highest unauthorized assumption rate (most aggressive execution), Claude Sonnet 4.6 shows the highest avoidance rate across all types (most conservative), and Qwen3-8B shows the most surface adoption (least reanalysis). These differences are in degree, not structure---the type$\times$failure-mode mapping is preserved.
410	
411	\paragraph{CP vs.\ Scopal: Visibility Within a Layer.}
412	Within the specification layer, CP violations show a distinctive pattern: 35\% of CP violation traces contain evidence of conflict detection (the agent recognizes contradictory rules but chooses the wrong priority). This contrasts sharply with scopal ambiguity, where agents show near-zero awareness of the ambiguity. The CP-awareness-to-scopal-awareness ratio is 2.8$\times$. CP's relatively low violation rate (33.6\%) despite being specification-layer reflects this partial visibility: explicit rule conflicts are more detectable than implicit scope interactions, even when both are dangerous.
413	
414	%% ============================================================
415	%% 7. DISCUSSION
416	%% ============================================================
417	\section{Discussion}
418	
419	\paragraph{Differential Nocuity as a Theoretical Framework.}
420	Our results establish that policy ambiguity's harm to LLM agents is not uniform but follows a principled hierarchy. We term this \textit{Differential Nocuity}: all ambiguity types are nocuous in Berry \& Kamsties' sense (producing divergent interpretations, $\kappa=0.33$), but their nocuity varies systematically by layer. The specification$\gg$linguistic gap ($17.4\pp$, $d=0.68$) is not an artifact of taxonomy design---it reflects a fundamental asymmetry in disambiguation channel availability.
421	
422	\paragraph{The Disambiguation Channel Hypothesis.}
423	Specification-layer ambiguity (authorization scope, incompleteness) operates at the pragmatic level: the intended meaning is not encoded in the linguistic form and cannot be recovered from context. Agents facing ``authorized personnel'' have no way to determine whether they are authorized---they must guess. Linguistic-layer ambiguity (scopal, lexical, coreferential) operates at the syntactic/semantic level and can sometimes be resolved by contextual cues from tool responses, dialogue history, or world knowledge. The gradient from scopal ($\Delta=34.8\pp$) to coreferential ($\Delta=16.2\pp$) corresponds to increasing availability of external disambiguation channels: coreferential ambiguity is most amenable to resolution by entity information in tool responses (23\% of traces), while scopal ambiguity about quantifier scope is rarely resolved by external context.
424	
425	\paragraph{Practical Implications.}
426	Our findings support \textbf{type-aware triage} for policy auditing: specification-layer ambiguities (authorization scope, incompleteness) should be prioritized over linguistic-layer ones. As a proof of concept, we fine-tuned a DeBERTa-v3-large model for binary ambiguity detection on our 300 clause pairs (240 train / 60 test, stratified by type), achieving F1${}=0.89$ compared to a TF-IDF baseline of 0.71 and zero-shot GPT-4.1 of 0.64 (\Cref{tab:classifier}). CP detection was easiest (F1${}=0.93$, aided by explicit conflict signals), while lexical ambiguity was hardest (F1${}=0.85$, requiring deeper semantic understanding). This demonstrates that automated detection integrated into policy review pipelines is feasible.
427	
428	\begin{table}[t]
429	\centering
430	\small
431	\caption{Binary ambiguity detection proof-of-concept.}
432	\label{tab:classifier}
433	\begin{tabular}{lccc}
434	\toprule
435	\textbf{Model} & \textbf{F1} & \textbf{Prec} & \textbf{Rec} \\
436	\midrule
437	DeBERTa-v3-large & 0.89 & 0.87 & 0.91 \\
438	TF-IDF + LR & 0.71 & 0.68 & 0.74 \\
439	Zero-shot GPT-4.1 & 0.64 & 0.59 & 0.70 \\
440	\bottomrule
441	\end{tabular}
442	\end{table}
443	
444	\paragraph{Comparison with Prior Work.}
445	\Cref{tab:comparison} positions our work against related benchmarks. We are the first to combine a causal matched-pair design with type-level statistical analysis across multiple model families. DRIP-R \citep{li2024drip} classifies ambiguity and measures interpretation divergence but does not quantify safety violations. PhantomPolicy and AgentPex evaluate agent safety but do not isolate ambiguity as a causal factor.
446	
447	\begin{table*}[t]
448	\centering
449	\small
450	\caption{Feature comparison with related benchmarks.}
451	\label{tab:comparison}
452	\begin{tabular}{lccccc}
453	\toprule
454	\textbf{Feature} & \textbf{DRIP-R} & \textbf{PhantomPolicy} & \textbf{PolicyBank} & \textbf{AgentPex} & \textbf{Ours} \\
455	\midrule
456	Ambiguity taxonomy & 5 RE types & --- & 3 gap types & --- & \textbf{6 types (2-layer)} \\
457	Causal design & --- & --- & --- & --- & \textbf{Matched pairs} \\
458	Safety violation metric & --- & Binary & --- & Procedural & \textbf{3-tier severity} \\
459	Cross-type comparison & Descriptive & --- & --- & --- & \textbf{Statistical ($\chi^2$ + $V$)} \\
460	Models tested & 6 API & 4 API & 2 API & 2 API & \textbf{5 (3 API + 2 local)} \\
461	Perturbation control & --- & --- & --- & --- & \textbf{Yes} \\
462	\bottomrule
463	\end{tabular}
464	\end{table*}
465	
466	\paragraph{Limitations.}
467	Our study has several limitations. (1)~The $\tau^2$-bench framework covers two domains (retail, airline); cross-domain generalization requires further validation. (2)~Synthetic clause injection, while necessary for causal control, may not capture all patterns of naturally occurring ambiguity, though our realism validation (\Cref{tab:realism}) shows statistical indistinguishability from natural clauses. (3)~The layer gap CI lower bound (12.5$\pp$) falls slightly below our pre-registered 15$\pp$ threshold, though the point estimate (17.4$\pp$) and significance ($p<0.0001$) strongly support the claim. (4)~Judge calibration, while strong (F1${}=0.91$), exhibits slight over-detection bias; we report this transparently. (5)~Incompleteness pairs inherently involve adding information during disambiguation; we include disambiguation length ratio as a covariate and find it non-significant ($p=0.50$).
468	
469	%% ============================================================
470	%% 8. CONCLUSION
471	%% ============================================================
472	\section{Conclusion}
473	
474	We demonstrate that all policy ambiguity types are nocuous for LLM agents, causing a $+35.8\pp$ safety violation increase---but specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones. This \textit{Differential Nocuity} is architecture-universal (five models, three families), causally confirmed (matched pairs + perturbation control), and mechanistically grounded (specification = unauthorized guessing, linguistic = diverse misparsing, coreferential = partial disambiguation via external channels). We recommend type-aware triage that prioritizes specification-layer ambiguities in policy auditing and release all materials for reproducibility.
475	
476	%% ============================================================
477	%% REFERENCES
478	%% ============================================================
479	\bibliographystyle{plainnat}
480	
481	\begin{thebibliography}{25}
482	
483	\bibitem[Berry and Kamsties(2003)]{berry2003ambiguity}
484	D.~Berry and E.~Kamsties.
485	\newblock Ambiguity in requirements specification.
486	\newblock In \emph{Perspectives on Software Requirements}, pages 7--44. Springer, 2003.
487	
488	\bibitem[Ferreira et~al.(2002)]{ferreira2002good}
489	F.~Ferreira, K.~Bailey, and V.~Ferraro.
490	\newblock Good-enough representations in language comprehension.
491	\newblock \emph{Current Directions in Psychological Science}, 11(1):11--15, 2002.
492	
493	\bibitem[Ferreira and Patson(2007)]{ferreira2007good}
494	F.~Ferreira and N.~Patson.
495	\newblock The `good enough' approach to language comprehension.
496	\newblock \emph{Language and Linguistics Compass}, 1(1-2):71--83, 2007.
497	
498	\bibitem[Frazier and Rayner(1982)]{frazier1982making}
499	L.~Frazier and K.~Rayner.
500	\newblock Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences.
501	\newblock \emph{Cognitive Psychology}, 14(2):178--210, 1982.
502	
503	\bibitem[Li et~al.(2024)]{li2024drip}
504	X.~Li et~al.
505	\newblock {DRIP-R}: Detecting and resolving interpretation problems in retail policies.
506	\newblock In \emph{Proceedings of ACL}, 2024.
507	
508	\bibitem[Lu et~al.(2022)]{lu2022fantastically}
509	Y.~Lu et~al.
510	\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.
511	\newblock In \emph{Proceedings of ACL}, pages 8086--8098, 2022.
512	
513	\bibitem[Massey et~al.(2014)]{massey2014identifying}
514	A.~K. Massey, R.~L. Rutledge, A.~I. Ant{\'o}n, and P.~P. Swire.
515	\newblock Identifying and classifying ambiguity for regulatory requirements.
516	\newblock In \emph{Proceedings of RE}, pages 83--92, 2014.
517	
518	\bibitem[Ruan et~al.(2024)]{ruan2024toolemu}
519	Y.~Ruan et~al.
520	\newblock {ToolEmu}: Identifying the risks of {LM} agents with an emulated tool environment.
521	\newblock In \emph{Proceedings of ICLR}, 2024.
522	
523	\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}
524	M.~Sclar et~al.
525	\newblock Quantifying language models' sensitivity to spurious features in prompt design with cognitive reflection.
526	\newblock In \emph{Proceedings of NAACL}, 2024.
527	
528	\bibitem[Schick et~al.(2024)]{schick2024toolformer}
529	T.~Schick et~al.
530	\newblock Toolformer: Language models can teach themselves to use tools.
531	\newblock In \emph{Proceedings of NeurIPS}, 2024.
532	
533	\bibitem[Wasow et~al.(2015)]{wasow2015ambiguity}
534	T.~Wasow, A.~Perfors, and D.~Beaver.
535	\newblock The puzzle of ambiguity.
536	\newblock In \emph{Morphology and Semantics}, pages 21--36, 2015.
537	
538	\bibitem[Xu et~al.(2024)]{xu2024agentpex}
539	Y.~Xu et~al.
540	\newblock {AgentPex}: Agent policy execution evaluation.
541	\newblock In \emph{Proceedings of NeurIPS}, 2024.
542	
543	\bibitem[Yao et~al.(2023)]{yao2023react}
544	S.~Yao et~al.
545	\newblock {ReAct}: Synergizing reasoning and acting in language models.
546	\newblock In \emph{Proceedings of ICLR}, 2023.
547	
548	\bibitem[Yao et~al.(2024)]{yao2024tau}
549	S.~Yao et~al.
550	\newblock $\tau^2$-bench: Benchmarking the reasoning and tool-use capabilities of large language models.
551	\newblock \emph{arXiv preprint arXiv:2406.12345}, 2024.
552	
553	\bibitem[Yuan et~al.(2024)]{yuan2024rjudge}
554	Z.~Yuan et~al.
555	\newblock {R-Judge}: Benchmarking safety risk awareness for {LLM} agents.
556	\newblock In \emph{Proceedings of EMNLP}, 2024.
557	
558	\bibitem[Zhan et~al.(2024)]{zhan2024injecagent}
559	Q.~Zhan et~al.
560	\newblock {InjecAgent}: Benchmarking indirect prompt injections in tool-integrated {LLM} agents.
561	\newblock In \emph{Proceedings of ACL Findings}, 2024.
562	
563	\end{thebibliography}
564	
565	%% ============================================================
566	%% APPENDIX
567	%% ============================================================
568	\clearpage
569	\appendix
570	
571	\section{Clause Pair Statistics}
572	\label{app:clause_stats}
573	
574	\begin{table*}[h]
575	\centering
576	\small
577	\caption{Clause pair statistics by ambiguity type (300 pairs, 50 per type). Amb/Unamb tokens are mean $\pm$ SD. Ratio = unambiguous/ambiguous token count.}
578	\label{tab:clause_stats}
579	\begin{tabular}{lcccccc}
580	\toprule
581	\textbf{Type} & \textbf{$N$} & \textbf{Amb tokens} & \textbf{Unamb tokens} & \textbf{Ratio} & \textbf{Flesch--Kincaid} & \textbf{Quality pass} \\
582	\midrule
583	auth\_scope & 50 & $28.4 \pm 5.1$ & $31.8 \pm 5.6$ & 1.12 & $11.8 \pm 1.9$ & 48/50 \\
584	incompleteness & 50 & $26.7 \pm 4.8$ & $30.7 \pm 5.2$ & 1.15 & $10.9 \pm 1.7$ & 47/50 \\
585	scopal & 50 & $24.2 \pm 4.3$ & $25.4 \pm 4.5$ & 1.05 & $11.0 \pm 1.6$ & 49/50 \\
586	lexical & 50 & $23.8 \pm 4.1$ & $24.8 \pm 4.3$ & 1.04 & $11.4 \pm 1.8$ & 49/50 \\
587	CP & 50 & $31.5 \pm 6.2$ & $33.4 \pm 6.5$ & 1.06 & $11.5 \pm 2.0$ & 48/50 \\
588	coreferential & 50 & $25.1 \pm 4.6$ & $26.9 \pm 4.9$ & 1.07 & $11.1 \pm 1.7$ & 47/50 \\
589	\midrule
590	\textbf{Overall} & 300 & & & 1.08 & $11.2 \pm 1.8$ & 288/300 \\
591	\bottomrule
592	\end{tabular}
593	\end{table*}
594	
595	\section{Mini-Pilot for New Types}
596	\label{app:mini_pilot}
597	
598	Before the full study, we ran a mini-pilot on the two previously untested types (authorization scope and coreferential): 5 clauses per type $\times$ 2 conditions $\times$ 1 model (GPT-5.4) = 20 episodes. Authorization scope showed a $60\pp$ ambiguity-driven violation increase (3/5 ambiguous episodes violated; 0/5 unambiguous). Coreferential showed $40\pp$ (2/5 vs.\ 0/5). Both unambiguous baselines were 0\%, confirming that ambiguity---not task difficulty---drives violations. Among authorization scope violations, 2/3 involved unauthorized permission assumptions and 1/3 involved privilege escalation, matching the spec-layer failure mode predicted by our taxonomy. Among coreferential safe episodes, one was resolved by tool-response disambiguation and one by conservative avoidance, providing early support for the Disambiguation Channel Hypothesis.
599	
600	\section{Per-Model API Results}
601	\label{app:api_results}
602	
603	\begin{table*}[h]
604	\centering
605	\small
606	\caption{Per-model ambiguous-condition violation rates (API models, 600 episodes each). Model main effect $p=0.42$, $V=0.018$.}
607	\label{tab:api_per_model}
608	\begin{tabular}{lcccccc}
609	\toprule
610	\textbf{Type} & \textbf{GPT-5.4} & \textbf{GPT-4.1} & \textbf{Claude S4.6} & \textbf{Pooled} & \textbf{Unamb} & \textbf{$\Delta$pp} \\
611	\midrule
612	auth\_scope & 58\% & 56\% & 54\% & 56.0\% & 2.0\% & 54.0 \\
613	incompleteness & 55\% & 53\% & 50\% & 52.7\% & 2.7\% & 50.0 \\
614	CP & 37\% & 35\% & 34\% & 35.3\% & 1.0\% & 34.3 \\
615	scopal & 42\% & 40\% & 38\% & 40.0\% & 3.3\% & 36.7 \\
616	lexical & 39\% & 37\% & 35\% & 37.0\% & 6.7\% & 30.3 \\
617	coreferential & 26\% & 25\% & 23\% & 24.7\% & 7.7\% & 17.0 \\
618	\midrule
619	\textbf{Overall} & 42.2\% & 40.7\% & 39.5\% & 40.8\% & 3.6\% & 37.2 \\
620	\bottomrule
621	\end{tabular}
622	\end{table*}
623	
624	\section{TOST Equivalence Results}
625	\label{app:tost}
626	
627	\begin{table}[h]
628	\centering
629	\small
630	\caption{TOST equivalence tests. At $\pm 10\pp$, all 15 pairs reject equivalence (types are NOT interchangeable). At $\pm 15\pp$, 3 within-layer adjacent pairs show equivalence.}
631	\label{tab:tost}
632	\begin{tabular}{lcc}
633	\toprule
634	\textbf{Margin} & \textbf{Not equiv.} & \textbf{Equivalent pairs} \\
635	\midrule
636	$\pm 10\pp$ & 15/15 & --- \\
637	$\pm 15\pp$ & 12/15 & auth--incomp, scopal--CP, lex--CP \\
638	\bottomrule
639	\end{tabular}
640	\end{table}
641	
642	\section{Test--Retest Reliability}
643	\label{app:reliability}
644	
645	\begin{table}[h]
646	\centering
647	\small
648	\caption{Test--retest reliability by type (30 clauses $\times$ 3 replicates $\times$ 5 models = 900 episodes).}
649	\label{tab:reliability}
650	\begin{tabular}{lccccc}
651	\toprule
652	\textbf{Type} & \textbf{ICC} & \textbf{Mean rate} & \textbf{Retest range} & \textbf{CV} & \textbf{CI width} \\
653	\midrule
654	auth\_scope & 0.87 & 54.2\% & 4.8pp & 0.08 & 6.9pp \\
655	incompleteness & 0.85 & 50.4\% & 5.9pp & 0.09 & 7.4pp \\
656	scopal & 0.79 & 38.7\% & 9.1pp & 0.14 & 10.2pp \\
657	lexical & 0.81 & 34.8\% & 7.6pp & 0.12 & 9.1pp \\
658	CP & 0.86 & 33.9\% & 5.2pp & 0.10 & 7.1pp \\
659	coreferential & 0.83 & 23.5\% & 6.8pp & 0.13 & 8.4pp \\
660	\midrule
661	\textbf{Overall} & \textbf{0.84} & 39.3\% & 6.2pp & 0.11 & 7.8pp \\
662	\bottomrule
663	\end{tabular}
664	\end{table}
665	
666	\section{Realism Validation}
667	\label{app:realism}
668	
669	\begin{table}[h]
670	\centering
671	\small
672	\caption{Synthetic clause properties vs.\ DRIP-R natural ambiguities. All KS tests non-significant; all effect sizes trivial ($d < 0.20$).}
673	\label{tab:realism}
674	\begin{tabular}{lccccc}
675	\toprule
676	\textbf{Property} & \textbf{Synthetic} & \textbf{Natural} & \textbf{KS} & \textbf{$p$} & \textbf{$d$} \\
677	\midrule
678	Sentence length & $27.3 \pm 5.2$ & $25.8 \pm 4.9$ & 0.097 & 0.23 & 0.18 \\
679	Parse depth & $4.7 \pm 1.3$ & $4.5 \pm 1.2$ & 0.073 & 0.41 & 0.12 \\
680	Flesch--Kincaid & $11.2 \pm 1.8$ & $10.8 \pm 1.7$ & 0.105 & 0.18 & 0.15 \\
681	TTR & $0.72 \pm 0.08$ & $0.71 \pm 0.09$ & 0.081 & 0.35 & 0.09 \\
682	\bottomrule
683	\end{tabular}
684	\end{table}
685	
686	\section{Cross-Judge Asymmetry}
687	\label{app:cross_judge}
688	
689	\begin{table}[h]
690	\centering
691	\small
692	\caption{Cross-judge performance by judge--agent pair.}
693	\label{tab:cross_judge}
694	\begin{tabular}{llcc}
695	\toprule
696	\textbf{Judge} & \textbf{Agent} & \textbf{F1} & \textbf{Bias} \\
697	\midrule
698	GPT-5.4 & Claude S4.6 & 0.90 & Neutral \\
699	GPT-5.4 & GPT-4.1 & 0.92 & Neutral \\
700	GPT-4.1 & GPT-5.4 & 0.88 & Slight under-detect \\
701	GPT-5.4 & Qwen3-32B & 0.91 & Neutral \\
702	GPT-5.4 & Qwen3-8B & 0.93 & Slight over-detect \\
703	\bottomrule
704	\end{tabular}
705	\end{table}
706	
707	\section{Per-Type Judge F1}
708	\label{app:per_type_judge}
709	
710	\begin{table}[h]
711	\centering
712	\small
713	\caption{LLM judge F1 by ambiguity type (100 sampled episodes).}
714	\label{tab:per_type_judge}
715	\begin{tabular}{lcccc}
716	\toprule
717	\textbf{Type} & \textbf{F1} & \textbf{Precision} & \textbf{Recall} & \textbf{$N$} \\
718	\midrule
719	auth\_scope & 0.93 & 0.91 & 0.95 & 17 \\
720	incompleteness & 0.92 & 0.90 & 0.94 & 17 \\
721	scopal & 0.88 & 0.85 & 0.91 & 17 \\
722	lexical & 0.89 & 0.87 & 0.91 & 17 \\
723	CP & 0.94 & 0.93 & 0.95 & 16 \\
724	coreferential & 0.87 & 0.84 & 0.90 & 16 \\
725	\bottomrule
726	\end{tabular}
727	\end{table}
728	
729	\end{document}
730	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d699571-0f81-4307-806c-58e51a042501",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "a247c3fc-70bd-4f12-9c88-f92f659c3b96",
  "sourceToolAssistantUUID": "3d699571-0f81-4307-806c-58e51a042501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T16:52:31.915Z_

Now let me read additional project files to understand the full context, including previous review reports, the paper framing, and literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a247c3fc-70bd-4f12-9c88-f92f659c3b96",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAgbKRENyMXy1PbgoBs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "938e1694-6133-4263-88c5-a3461bf37b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194Mz5ZDZPBigXQGAnGnMah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6128,
      "cache_creation_input_tokens": 18193,
      "cache_read_input_tokens": 20836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18193,
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

_source line 19 · 2026-05-20T16:52:32.849Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NSMFn9c5oTCvLixS9hGjof`</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "938e1694-6133-4263-88c5-a3461bf37b47",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAgbKRENyMXy1PbgoBs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "228f6a5b-84ac-45ad-bbb0-c71d3ec6810c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194Mz5ZDZPBigXQGAnGnMah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6128,
      "cache_creation_input_tokens": 18193,
      "cache_read_input_tokens": 20836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18193,
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

_source line 20 · 2026-05-20T16:52:32.864Z_

<details><summary>↩ Tool result · `toolu_01NSMFn9c5oTCvLixS9hGjof`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/paper_framing.md\", \"content\": \"# Paper Framing — policy_ambiguity_safety\\n\\n> 最后更新: 2026-05-20 | 状态: plan_002 complete, framing pivot (C2 falsified)\\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\\n> plan_002: 1,200 episodes, C1 confirmed (+36.5pp), C2 FALSIFIED (V=0.207, p=0.0001)\\n\\n## Core Insight\\n\\nPolicy ambiguity causes devastating safety violations in LLM agents (+36.5pp), but **not all types are equally dangerous**: specification-layer ambiguities (authorization scope, incompleteness) cause nearly twice the violation rate increase (~46pp) of linguistic-layer ambiguities (~27pp). This layer hierarchy connects Berry & Kamsties' nocuous ambiguity theory to LLM agent safety and suggests type-aware triage prioritizing specification-layer ambiguities.\\n\\n## Title (Working)\\n\\n\\\"Not All Policy Ambiguity Is Equal: Specification-Layer Ambiguity Poses Greater Safety Risks for LLM Agents\\\"\\n\\nAlternative: \\\"Differential Nocuity: How Ambiguity Type Predicts Safety Violation Severity in LLM Agent Policies\\\"\\n\\nNote: Pivoted from \\\"Uniformly Nocuous\\\" after plan_002 falsified C2 (V=0.207, p=0.0001). Layer hierarchy is a stronger, more informative finding.\\n\\n## Core Claims\\n\\n### C1: Binary Effect (PRIMARY — confirmed)\\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +36.5pp (plan_002), McNemar OR=44.8 (CI: [18.47, 108.69]), p<0.0001. Holds across all 6 types and both models.\\n- **Evidence**: mvp_001 (360 episodes, 3 types) + plan_002 (1,200 episodes, 6 types, 2 models). Bootstrap CI: [+32.0pp, +40.5pp].\\n- **Strength**: Very strong. Replicated across types and models. Perturbation control (plan_010) confirms ambiguity-specific (Δ_perturb=3.33pp, PASS).\\n- **Causal backing**: Matched-pair design + perturbation control → strongest causal inference in the literature.\\n\\n### C2: Type Hierarchy (SECONDARY — confirmed positive, upgraded from null)\\n**PIVOTED from uniformity null.** Different ambiguity types produce significantly different violation rates. Omnibus χ²=25.61, p=0.0001, V=0.207.\\n- **Evidence**: plan_002 (1,200 episodes, 6 types × 2 conditions × 2 models)\\n  - Specification-layer: auth_scope 55% (+53pp), incompleteness 52% (+49pp), CP 35% (+35pp) → avg Δ≈46pp\\n  - Linguistic-layer: scopal 40% (+36pp), lexical 38% (+30pp), coreferential 25% (+16pp) → avg Δ≈27pp\\n- **Layer effect**: Specification avg Δ ≈ 46pp vs Linguistic avg Δ ≈ 27pp (~19pp gap)\\n- **Implication**: Type-aware triage warranted. Specification-layer ambiguities should be prioritized in policy auditing pipelines.\\n- **TOST**: ±15pp equivalence rejected for most pairs (3/15 equivalent); ±10pp all rejected. Types are NOT interchangeable.\\n- **MVP→Full Study evolution**: MVP 3 types gave V=0.084 (null); full study 6 types gives V=0.207 (significant). The new types (especially auth_scope and coreferential) drove the heterogeneity — MVP's 3 types were coincidentally similar.\\n- **Coreferential as boundary case**: 25% violation rate (Δ=+16pp) is the lowest — agents can partially disambiguate via tool responses and cautious strategies. This defines the \\\"nocuous ambiguity boundary\\\" — where external disambiguation channels reduce but don't eliminate harm.\\n\\n### C3: Layer Effect (SECONDARY — confirmed)\\n**Replaces old \\\"Visibility Moderates Risk\\\" hypothesis.** Specification-layer ambiguities (operating at pragmatic/discourse level of policy interpretation) cause significantly more violations than linguistic-layer ambiguities (operating at syntactic/semantic level).\\n- **Evidence**: plan_002 layer comparison. Spec 142/300 (47.3%) vs Ling 103/300 (34.3%), χ²=10.49, p=0.0012, V=0.132 (small-to-medium), OR=1.72 [1.24, 2.39]. Bootstrap CI for Δ: [+5.33pp, +20.67pp].\\n- **Mechanism hypothesis**: Linguistic ambiguity can sometimes be resolved by contextual cues (tool responses, user messages, world knowledge). Specification ambiguity (undefined roles, missing conditions) has no external resolution channel — agents must guess.\\n- **CL connection**: Parallels pragmatics vs semantics distinction. Connects to good-enough processing (Ferreira et al. 2002) — agents may handle syntactic ambiguity \\\"good enough\\\" but fail on pragmatic underspecification.\\n- **Layer overlap caveat** [Reviewer]: CP (35%, spec) < scopal (40%, ling). Layer effect driven by extremes: auth_scope+incompleteness (53.5% avg) vs coreferential (25%). Middle three types (CP/lexical/scopal, 35-40%) overlap across layers. Write: \\\"specification-layer ambiguities as a group are significantly more dangerous\\\" — do NOT imply every spec type beats every ling type.\\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer not only more dangerous but also less reproducible — agents guess differently each run when external disambiguation channels are absent. Top-5 highest-variance replicate groups all ambiguous+spec-layer.\\n- **Note on old C3 (visibility)**: diag_001's CP(34%) vs scopal(40%) direction confirmed in full study (CP 35% vs scopal 40%), but the effect is subsumed by the broader layer hierarchy. CP is specification-layer but has the lowest spec-layer rate, while scopal is linguistic-layer with the highest ling-layer rate — they are the convergence point between layers.\\n\\n### C4: Model Consistency (EXPLORATORY — updated)\\nNo significant model main effect (p=0.581, V=0.016). Both models show similar overall violation rates AND similar failure mode profiles (C5 cross-model). Model×type interaction to be tested with 5 models (plan_003 adds Qwen3-8B, Qwen3-32B-AWQ; Claude pending).\\n- **Evidence**: plan_002 gpt-5.4 (41.0%) vs gpt-4.1 (40.7%). Consistent direction across types. plan_005 cross-model: overall failure mode distribution nearly identical (assumption_based_action 33.3%/33.6%, scope_misapplication 27.6%/25.4%, unauthorized_escalation 28.5%/32.0%). Resolution strategies also consistent: surface_adoption dominates both models (94%/93%).\\n- **Strength**: 2-model result. Failure mode consistency is stronger evidence than just violation rate consistency. Full 5-model test needed for formal interaction analysis.\\n\\n### C5: Error Analysis (CONFIRMED — EMNLP core)\\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \\\"misparse\\\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \\\"active guessing\\\" → explains higher violation rates\\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \\\"confident,\\\" act without hesitation)\\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \\\"Ambiguity Blindness\\\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\\n\\n## Narrative Structure (CL-first for EMNLP)\\n\\n### Intro Logic Chain\\n1. Agent policies are written in NL → contain ambiguity (established)\\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?\\n5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect. Perturbation control confirms ambiguity-specific causation.\\n6. **Core findings**: (a) All ambiguity is nocuous (+36.5pp), (b) but type DOES predict severity — specification-layer ambiguities (~46pp) are nearly twice as dangerous as linguistic-layer (~27pp), (c) this hierarchy reflects availability of external disambiguation channels.\\n\\n### Section Map\\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + layer hierarchy + disambiguation channel theory)\\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)\\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)\\n- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, perturbation control, cross-judge evaluation, statistical analysis plan\\n- **§5 Results**: C1 (binary, +36.5pp) → C2 (type hierarchy, V=0.207) → C3 (layer effect, Spec>>Ling) → C4 (model consistency)\\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type, explaining WHY specification-layer is more dangerous. This is the EMNLP core.\\n- **§7 Discussion**: Differential nocuity theory. Disambiguation channel hypothesis. Practical implications (type-aware triage pipeline, prioritize spec-layer). Limitations (2 domains, 2 API models, synthetic injection).\\n- **§8 Conclusion**: All policy ambiguity is nocuous, but specification-layer ambiguities demand priority attention. Type-aware auditing recommended.\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: \\\"Type effect could be artifact of taxonomy granularity\\\"\\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\\n\\n### RC2: \\\"Taxonomy is ad hoc / why these 6 types\\\"\\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\\n\\n### RC3: \\\"Only API models, no open-source\\\"\\n**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 5-model coverage spans frontier API (gpt-5.4, claude-sonnet-4-6) + mid-tier API (gpt-4.1) + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.\\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4 (strongest), gpt-5.4 judged by gpt-4.1 (weaker). Must disclose in Method. plan_009 judge calibration measures this bias.\\n**Status**: Currently 2 API models complete. Claude endpoint BLOCKED. Qwen3 needs GPU. If only 2 models: acknowledge in Limitation, note failure mode consistency across models as partial mitigation.\\n\\n### RC4: \\\"Synthetic ambiguity injection lacks ecological validity\\\"\\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\\n\\n### RC5: \\\"τ²-bench limited to retail/airline\\\"\\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\\n\\n### RC6: \\\"Binary effect is obvious — of course ambiguity causes errors\\\"\\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\\n\\n### RC7: \\\"Incompleteness matched-pair confound (information asymmetry)\\\"\\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\\n\\n### RC8: \\\"RC attachment in coreferential overlaps with scopal / structural ambiguity\\\"\\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\\n\\n### RC9: \\\"authorization_scope is just a subtype of incompleteness\\\"\\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \\\"authorized personnel\\\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\\n\\n### RC10: \\\"API sampling noise undermines reliability\\\"\\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\\n\\n### RC11: \\\"Prompt sensitivity confound\\\" [Dream A9 — best tier \\\"strongest point\\\"]\\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\\n\\n## Concept Naming (distill insight: 命名即贡献)\\n\\nCore phenomenon: **\\\"Differential Nocuity\\\"** — all policy ambiguity types are nocuous for LLM agents, but specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones. Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels for specification-level underspecification.\\n\\nSecondary phenomenon: **\\\"Ambiguity Blindness\\\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\\n\\nTertiary phenomenon: **\\\"Disambiguation Channel Hypothesis\\\"** — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess.\\n\\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \\\"Recently...\\\")\\n\\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \\\"items may be returned within 30 days\\\" (scopal: \\\"items\\\" scopes over all categories including custom). The unambiguous version specifies \\\"standard items only\\\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\\n\\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\\n\\n\\\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\\\"\\n\\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\\n\\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\\n|---------|--------|---------------|------------|----------|----------|\\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\\n| Causal design | — | — | — | — | **matched pairs** |\\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\\n| Models tested | 6 API | 4 API | 2 API | 2 API | **2 API + 2 open-source** |\\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\\n\\n## Contribution Positioning (for EMNLP)\\n\\n1. **Problem formulation**: First causal framing of ambiguity type → safety violation in agent policies. Introduces \\\"differential nocuity\\\" as a named phenomenon.\\n2. **Empirical — Differential Nocuity**: Quantifies binary effect (+36.5pp) across 6 types and 2 models. Demonstrates significant type hierarchy (V=0.207, p=0.0001) with specification-layer (~46pp) nearly twice as dangerous as linguistic-layer (~27pp). Perturbation control confirms ambiguity-specific causation.\\n3. **Empirical — Ambiguity Blindness** [upgraded from sub-finding per Reviewer strategic assessment]: LLM agents show <5% meta-cognitive awareness of policy ambiguity (5/123 traces). Surface adoption >88% across all types. Escalation to user: 0.8%. This is a **novel, quantified finding** with direct practical implication: ambiguity detection must be externalized, agents cannot self-check. CP's 11.8% awareness (only double-digit type) provides nuance — explicit rule conflicts partially trigger awareness. Warrants §6 dedicated subsection.\\n4. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. Proposes \\\"disambiguation channel hypothesis\\\" — specification ambiguity lacks external resolution channels, explaining the layer hierarchy. Failure mode taxonomy provides mechanistic explanation: spec-layer → guess-and-act (unauthorized_escalation, assumption); ling-layer → misparse-and-apply (scope_misapplication). Cross-model consistency (5/6 types same dominant mode) suggests these are type-inherent, not model artifacts.\\n5. **Practical**: Type-aware triage warranted: specification-layer ambiguities demand priority in policy auditing pipelines. External ambiguity detection required (agents cannot self-detect).\\n6. **Methodological**: Matched-pair causal design + perturbation control + cross-judge evaluation + 2-layer taxonomy with cross-walk.\\n\\n## Required Reference Expansion [Dream A2 — three-tier consistent]\\n\\nCurrent plan has thin references. Must add (≥25 total in final paper):\\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007) — directly relevant to visibility hypothesis (how processors handle ambiguity without full reanalysis)\\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001) — why some ambiguity triggers reanalysis\\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024) — ambiguity sensitivity as special case of instruction robustness\\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022) — general prompt brittleness literature\\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent — position against wider agent safety work\\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017) — ambiguity/vagueness boundary\\n- **Garden-path**: Frazier & Rayner (1982) — reanalysis cost grounding for C3\\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\\n\\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\\n\\nMust commit to releasing:\\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\\n3. Statistical analysis code (all tests, bootstrap CI computation)\\n4. Agent trace samples (anonymized) for reproducibility of C5\\n\\n## Figure Plan [Dream A12]\\n\\nMinimum figures for paper (zero-figure paper flagged in dream):\\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\\n\\n## Berry & Kamsties Operationalization Note [Dream best Q5]\\n\\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\\n\\n## Contingency Framing [RESOLVED — Scenario C occurred]\\n\\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\\n> Framing 已 pivot 到 \\\"Differential Nocuity\\\" + \\\"Layer Hierarchy\\\" (D020)。本节仅保留历史记录。\\n\\n## Claude Baseline — BLOCKED [2026-05-20]\\n\\n4/8 distilled papers use Claude as baseline. Code integrated (per-model client routing), but **47.94.22.126 proxy does not support Claude models** (5 model IDs tested, all timeout). Waiting for user to provide working endpoint (Anthropic direct / OpenRouter official / proxy update). plan_002 ran with 2 API models (gpt-5.4, gpt-4.1); Claude 600 episodes to be appended when endpoint available. If no Claude: 4 models (2 API + 2 local Qwen3) still acceptable, acknowledge in Limitation.\\n\", \"total_chars\": 24951, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "228f6a5b-84ac-45ad-bbb0-c71d3ec6810c",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "62a69532-26b1-47a8-817e-5ff7c07e374a",
  "sourceToolAssistantUUID": "228f6a5b-84ac-45ad-bbb0-c71d3ec6810c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T16:52:33.908Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013qLcxAPgXhqCkHaXsRCjXg`</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62a69532-26b1-47a8-817e-5ff7c07e374a",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAgbKRENyMXy1PbgoBs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a463bc4-53b0-4ac3-8fe1-ebaf5836b865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194Mz5ZDZPBigXQGAnGnMah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6128,
      "cache_creation_input_tokens": 18193,
      "cache_read_input_tokens": 20836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18193,
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

_source line 22 · 2026-05-20T16:52:33.918Z_

<details><summary>↩ Tool result · `toolu_013qLcxAPgXhqCkHaXsRCjXg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/literature_map.yaml\", \"content\": \"papers:\\n  drip_r_2026:\\n    title: \\\"DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2605.07699\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: drip_r_2026\\n    category: \\\"policy_ambiguity\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Closest concurrent work: 400 policy-ambiguous retail scenarios across 5 RE ambiguity types. Measures decision quality but NOT safety violations per type. Our direct comparison target.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  li_ambiguity_taxonomy_2024:\\n    title: \\\"A Taxonomy of Ambiguity Types for NLP\\\"\\n    authors: [\\\"Li et al.\\\"]\\n    year: 2024\\n    venue: \\\"UnImplicit Workshop, EACL 2024\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: li_ambiguity_taxonomy_2024\\n    category: \\\"ambiguity_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"11-type NLP ambiguity taxonomy. We select lexical, scopal, coreferential as policy-relevant types for our linguistic layer.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  massey_ambiguity_re_2014:\\n    title: \\\"Identifying and Classifying Ambiguity for Regulatory Requirements\\\"\\n    authors: [\\\"Massey et al.\\\"]\\n    year: 2014\\n    venue: \\\"RE 2014\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: massey_ambiguity_re_2014\\n    category: \\\"ambiguity_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"6-type RE ambiguity taxonomy (lexical, syntactic, semantic, vagueness, incompleteness, referential). We adopt incompleteness as core category for specification layer.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  agentpex_2026:\\n    title: \\\"Willful Disobedience: Automatically Detecting Failures in Agentic Traces\\\"\\n    authors: [\\\"Sharma\\\", \\\"Barke\\\", \\\"Zorn\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.23806\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: agentpex_2026\\n    category: \\\"evaluation\\\"\\n    role: \\\"methodology\\\"\\n    relevance: \\\"AgentPex: 3-stage specification extraction + 7 evaluators on τ²-bench. 83% perfect-outcome traces contain procedural violations. We adopt its evaluation methodology.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  policybank_2026:\\n    title: \\\"PolicyBank: Evolving Policy Understanding for LLM Agents\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: policybank_2026\\n    category: \\\"policy_ambiguity\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Iterative policy refinement closing 82% gap toward human oracle on τ-Bench. Identifies 3 gap types but focuses on learning, not ambiguity-to-safety mapping.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  phantompolicy_2026:\\n    title: \\\"Policy-Invisible Violations in LLM-Based Agents\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.12177\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: phantompolicy_2026\\n    category: \\\"agent_safety\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"PhantomPolicy: 8 violation categories where policy-relevant facts are hidden. Frontier models violate 90-98%. Complementary (information-visibility vs our specification-ambiguity).\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  shieldagent_2025:\\n    title: \\\"ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning\\\"\\n    authors: [\\\"Chen\\\", \\\"Kang\\\", \\\"Li\\\"]\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: shieldagent_2025\\n    category: \\\"agent_safety\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Extracts formal safety rules from policy docs into probabilistic rule circuits. 90.1% recall. Presupposes clean policies — our work identifies which ambiguities need formalization first.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  agentauditor_2025:\\n    title: \\\"AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.00641\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: agentauditor_2025\\n    category: \\\"evaluation\\\"\\n    role: \\\"methodology\\\"\\n    relevance: \\\"Memory-augmented reasoning achieving 96.3% F1 on R-Judge. We adopt its LLM-as-judge methodology for Tier 2 nuanced violation evaluation.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  tau2_bench_2025:\\n    title: \\\"τ²-bench: Evaluating Conversational Agents in a Dual-Control Environment\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.07982\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: tau2_bench_2025\\n    category: \\\"benchmark\\\"\\n    role: \\\"infrastructure\\\"\\n    relevance: \\\"Our primary experimental platform. Dual-control retail/airline domains with NL assertion evaluation and policy XML injection.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  lhaw_2026:\\n    title: \\\"LHAW: Controllable Underspecification for Long-Horizon Tasks\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.10525\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: lhaw_2026\\n    category: \\\"underspecification\\\"\\n    role: \\\"methodology\\\"\\n    relevance: \\\"Perturbation pipeline for underspecified task variants. 285 synthetic variants classified as outcome-critical/divergent/benign. We adapt its methodology for policy domain.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  berry_kamsties_2004:\\n    title: \\\"Ambiguity in Requirements Specification\\\"\\n    authors: [\\\"Berry\\\", \\\"Kamsties\\\"]\\n    year: 2003\\n    venue: \\\"Perspectives on Software Requirements\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: berry_kamsties_2004\\n    category: \\\"ambiguity_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Nocuous vs innocuous ambiguity theory. Core theoretical anchor: LLM agents lack shared organizational context, making human-innocuous ambiguities agent-nocuous.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  chantree_2006:\\n    title: \\\"Identifying Nocuous Ambiguities in Natural Language Requirements\\\"\\n    authors: [\\\"Chantree et al.\\\"]\\n    year: 2006\\n    venue: \\\"RE 2006\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: chantree_2006\\n    category: \\\"ambiguity_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Empirical nocuous ambiguity detection in RE. Supports our theoretical framing that ambiguity harmfulness depends on interpretive context.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  mantra_2026:\\n    title: \\\"MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06334\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: mantra_2026\\n    category: \\\"benchmark\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"285 tasks across 6 domains from procedural manuals with SMT validation. Formalizes manual-to-benchmark but doesn't address source ambiguity's safety impact.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\", \"total_chars\": 7583, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a463bc4-53b0-4ac3-8fe1-ebaf5836b865",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "1325fa4a-4ef5-4729-ab3b-9f45e5418ac5",
  "sourceToolAssistantUUID": "1a463bc4-53b0-4ac3-8fe1-ebaf5836b865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T16:52:34.310Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KkUwE2Tu9MfqEB2hDJt9Pt`</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1325fa4a-4ef5-4729-ab3b-9f45e5418ac5",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAgbKRENyMXy1PbgoBs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45f9b052-98d5-4936-9b15-ffd4e2d418f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194Mz5ZDZPBigXQGAnGnMah",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6128,
      "cache_creation_input_tokens": 18193,
      "cache_read_input_tokens": 20836,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18193
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6128,
          "output_tokens": 323,
          "cache_read_input_tokens": 20836,
          "cache_creation_input_tokens": 18193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18193,
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

_source line 24 · 2026-05-20T16:52:34.318Z_

<details><summary>↩ Tool result · `toolu_01KkUwE2Tu9MfqEB2hDJt9Pt`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'policy_ambiguity_safety'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45f9b052-98d5-4936-9b15-ffd4e2d418f2",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "2179ba42-03bb-4d59-9a22-aa64495252b8",
  "sourceToolAssistantUUID": "45f9b052-98d5-4936-9b15-ffd4e2d418f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T16:52:50.074Z_

Now let me also read the earlier dream review and the first reviewer session's review for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2179ba42-03bb-4d59-9a22-aa64495252b8",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAhu2ofUKQMT76vBRrh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77cb7482-b465-4794-9d12-6a50bb255ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnJY25vwQRYLaBpQaVRqiD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17617,
      "cache_read_input_tokens": 39029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17617,
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

_source line 26 · 2026-05-20T16:52:51.501Z_

<details open><summary>🔧 Tool call — Read · `toolu_014YHdfZp4JrbMq3zuWjbCB9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77cb7482-b465-4794-9d12-6a50bb255ca2",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAhu2ofUKQMT76vBRrh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96c7af49-abfd-4eee-973f-bb6ec4281027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnJY25vwQRYLaBpQaVRqiD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17617,
      "cache_read_input_tokens": 39029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17617,
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

_source line 27 · 2026-05-20T16:52:51.506Z_

<details><summary>↩ Tool result · `toolu_014YHdfZp4JrbMq3zuWjbCB9`</summary>

```text
1	---
2	dream_id: dream_20260520T152228
3	tier: median
4	overall_score: Weak Accept (4/6)
5	timestamp: 2026-05-20T16:50:01.490757+00:00
6	---
7	
8	# Dream Review Report: Differential Nocuity
9	
10	**Paper**: "Differential Nocuity: How Ambiguity Type Predicts Safety Violation Severity in LLM Agent Policies"
11	**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
12	**Date**: 2026-05-20
13	
14	---
15	
16	## Overall Assessment
17	
18	**Converged Score: 4 / 6 (Weak Accept)**
19	**Confidence: 4 / 5 (High)**
20	
21	This paper addresses a genuinely novel question — whether different types of policy ambiguity produce different levels of safety violations in LLM agents — and answers it with comprehensive experiments (3,000 episodes, 5 models, 6 types). The binary ambiguity effect (C1: Δ=31.9pp) is robust and well-supported by perturbation controls. The layer-level differentiation (spec > ling by 12.1pp) is convincing across frontier models. However, the fine-grained type-level hierarchy has modest effect sizes (V=0.17), judge calibration issues compound for theoretically important types, and the error analysis lacks inter-coder reliability. The paper is above the acceptance bar but has clear areas for improvement.
22	
23	---
24	
25	## R1: Methods & Experiments
26	
27	### Summary
28	The paper uses a matched-pair design (300 clause pairs, 50/type) across 5 models in τ²-bench, producing 3,000 episodes evaluated by cross-model LLM judges. A four-claim statistical framework (binary effect, type hierarchy, layer effect, model×type interaction) is complemented by test-retest reliability, ecological validity, judge calibration, perturbation controls, error analysis, and a classifier PoC.
29	
30	### Strengths
31	- **Rigorous matched-pair design**: The ambiguous/unambiguous pairing with minimal information delta (4.7 tokens, controlled as covariate, p=0.23 non-significant) is well-constructed. Table 2's quality disclosure (33/300 clauses revised) is transparent.
32	- **Strong causal evidence for C1**: The perturbation control (Δ_perturb=3.8pp, CI contains 0, ratio=0.11) convincingly rules out general prompt sensitivity. This is the paper's methodological crown jewel.
33	- **Comprehensive statistical framework**: Four claims tested with appropriate methods — McNemar for paired binary data (C1), χ²/Cramér's V with TOST for type hierarchy (C2), bootstrap CI for layer effect (C3), logistic regression for interaction (C4). Power analysis confirms adequate sensitivity (MDE V=0.09 for C2, 5.8pp for C3, both below observed values).
34	- **Good model diversity**: 3 families (OpenAI, Anthropic, Qwen) × 2 deployment modalities (API, local) provides cross-family generalizability evidence.
35	- **Full experiment coverage**: All 11 experiments from the design plan (clause generation, mini-pilot, API study, local study, analysis, error analysis, reliability, realism validation, classifier, judge calibration, perturbation control) appear in the paper. This is thorough execution.
36	- **Transparent limitation disclosure**: Judge calibration gaps, borderline interaction, convergence zones — all honestly presented.
37	
38	### Weaknesses
39	- **Cramér's V=0.17 is a small effect size**: While statistically significant (p<0.001), this indicates that ambiguity type explains only ~3% of the variance in violation rates within the ambiguous condition. The type hierarchy *exists* but the practical differentiation between types is modest. This is the central tension: C1 (ambiguity matters) is convincing; C2 (types differ) is statistically supported but practically modest.
40	- **TOST ±15pp margin is generous**: At ±15pp, 4/15 pairs are equivalent (all within-layer or at the boundary). At ±10pp, only CP-lexical (Δ=0.6pp) qualifies. The margin choice isn't justified from prior work or theory. The "types within a layer are partially interchangeable" claim depends heavily on accepting 15pp as the equivalence bound. Recommend the authors provide sensitivity analysis across multiple margins (5pp, 10pp, 15pp, 20pp).
41	- **Judge calibration weaknesses for key types**: Lexical (F1=0.72) and coreferential (F1=0.71) fall below the 0.75 threshold. These are precisely the types where: (a) the disambiguation channel evidence resides, (b) coreferential avoidance behavior is reported, and (c) the type-level ranking is most nuanced. The 6pp cross-judge asymmetry is disclosed but not formally tested via sensitivity analysis. **This compounding uncertainty disproportionately threatens C3 and the qualitative findings for these types.**
42	- **Error analysis lacks inter-coder reliability**: Section 6 says "we manually categorize 300 violation traces" but does not specify: who coded them, how many coders, what training/protocol was used, or what the inter-coder agreement was. The 6 failure mode categories and all percentages (e.g., 62% assumption-based for spec-layer, 38% cross-layer overlap) are key narrative elements resting on unvalidated coding. For a paper claiming an "error taxonomy" as a contribution, this is a significant gap.
43	- **Perturbation control excludes open-source models**: Only 180 episodes across 3 API models. Given that Qwen3-8B shows fundamentally different behavior (19.2% unambiguous baseline, 4.3pp layer gap, partial layer inversion), the causal claim may not fully generalize to smaller open-source models. Adding even 60 episodes (30 clauses × 2 conditions × 1 local model) would strengthen this.
44	- **Borderline model×type interaction (p=0.062)**: The paper handles this well narratively ("mostly universal but not perfectly clean"), but the interaction V=0.08 is very small. Qwen3-8B's partial inversion (scopal Δ=32pp > CP Δ=20pp) is the main driver. The universality claim is honestly hedged but readers may still overinterpret the layer hierarchy as applying uniformly.
45	- **Reliability concerns for scopal and coreferential**: ICC=0.66 (scopal) and 0.65 (coreferential) are "moderate" — meaning same clauses can vary ±12-13pp across replicates. Combined with low judge F1 for these types, confidence in their exact placement in the hierarchy is limited.
46	
47	### Questions for Authors
48	1. What is the inter-coder reliability for the 6-category failure mode coding? How many coders were involved?
49	2. Can you provide sensitivity analyses for C1/C2 after excluding episodes judged for types with F1 < 0.75?
50	3. What is the theoretical basis for the ±15pp TOST margin?
51	4. Why were open-source models excluded from perturbation control? Would adding Qwen3-8B episodes change the verdict?
52	5. The information delta covariate (p=0.23) — can you share the full regression model specification?
53	
54	### R1 Score: 4 (Weak Accept) | Confidence: 4
55	
56	---
57	
58	## R2: Novelty & Related Work
59	
60	### Summary
61	The paper introduces "differential nocuity" — the concept that ambiguity types pose different levels of safety risk for LLM agents. It synthesizes a two-layer taxonomy from RE literature (Li et al., Massey et al.), provides the first causal evidence linking ambiguity type to violation severity, proposes a "disambiguation channel hypothesis," and extends Berry & Kamsties' nocuity framework with convergent-but-wrong analysis.
62	
63	### Strengths
64	- **Genuinely novel research question**: No prior work has established the causal link from ambiguity *type* to safety violation *severity* in LLM agents. DRIP-R (Li et al., 2024) shows divergent interpretations but does not measure downstream safety consequences. This paper fills that gap.
65	- **"Differential nocuity" is a meaningful conceptual contribution**: Bridging requirements engineering (Berry & Kamsties' nocuity) with LLM agent safety is non-trivial. The two-layer framework (spec/ling) provides actionable structure — practitioners can prioritize spec-layer ambiguities for audit.
66	- **Disambiguation channel hypothesis is theoretically grounded**: The connection to Ferreira et al.'s "good-enough" processing provides a mechanistic explanation for *why* ling-layer types are less dangerous (external resolution channels exist) vs. spec-layer (no channel → forced guessing). This is supported by the 34% partial disambiguation rate in ling traces vs. 8% in spec.
67	- **Convergent-but-wrong finding (38%) extends B&K**: The discovery that 38% of ambiguous clauses produce *unanimous* wrong interpretations (all 5 models converge on the same incorrect reading) challenges the binary nocuous/innocuous distinction. This is a genuinely new observation for the LLM setting — in human RE, shared organizational context typically prevents this.
68	- **Well-positioned for *ACL**: The paper sits at the CL/safety intersection, combining linguistic analysis (ambiguity taxonomy, error modes) with agent safety evaluation. This is appropriate and timely.
69	- **Inter-model nocuity analysis (Fleiss κ=0.44)**: The decomposition into 42% divergent (true nocuity per B&K), 38% convergent-but-wrong (systematic bias), and 20% mixed adds nuance beyond simple violation rates.
70	
71	### Weaknesses
72	- **Taxonomy is derivative**: The six types are directly mapped from Li et al. (2024) and Massey et al. (2014) (Table 1). The two-layer grouping (spec/ling) is the original organizational contribution, but it's a natural grouping that follows from the RE literature. The paper's novelty is *empirical* (testing the taxonomy's predictive power for safety), not *theoretical* (proposing new ambiguity categories).
73	- **Related work gaps**:
74	  - **Pragmatics/semantics**: No engagement with Gricean implicature or relevance theory (Sperber & Wilson), which directly relates to how agents might resolve ambiguity through contextual inference. The "disambiguation channel" hypothesis would benefit from this grounding.
75	  - **Alignment/RLHF literature**: No discussion of how safety training (RLHF, constitutional AI, etc.) interacts with ambiguity processing. The paper notes Claude has lower violation rates but attributes this to "constitutional AI training" without citation or depth.
76	  - **Instruction tuning**: No mention of work on instruction-following robustness beyond IFEval (Zhou et al., 2023) and prompt sensitivity (Sclar et al., 2024). The connection between ambiguity and instruction-following is underexplored.
77	  - **Formal methods in RE**: No discussion of whether formal specification languages or contract-based approaches could eliminate the problem entirely. This would strengthen the practical implications.
78	- **Disambiguation channel is observational, not tested**: The "hypothesis" label (Contribution 3) may overstate. The evidence is correlational: ling traces show 34% partial disambiguation vs. 8% for spec, and the error analysis shows different failure modes by layer. But there's no manipulation of disambiguation channel availability (e.g., providing vs. withholding tool access, or providing explicit disambiguation cues). The paper should frame this as "the disambiguation channel observation" or "suggestive evidence for a disambiguation channel mechanism."
79	- **Convergent-but-wrong is underdeveloped**: This is potentially the paper's most interesting theoretical contribution, but it gets only two paragraphs (Section 6.1). Key questions unanswered: Does convergent-but-wrong correlate with specific ambiguity types? Are certain surface forms more likely to produce systematic bias? Does it relate to training data distribution? Is it a new category in the nocuity framework or a refinement of "nocuous"?
80	- **Psycholinguistic grounding is thin**: The Ferreira "good-enough" processing analogy (Section 2, lines 164-174) is asserted in 4 sentences without arguing *why* it applies to LLMs. Autoregressive generation is fundamentally different from human incremental comprehension. The analogy may hold behaviorally but the mechanistic link is unexplored.
81	- **DeBERTa classifier (Section 8) feels supplementary**: F1=0.78 on 240 training examples is expected for a fine-tuned model. The cross-type transfer result (F1=0.65) is more interesting — it suggests type-agnostic detection is hard — but it's underexplored. This section reads as a late addition rather than an integrated contribution.
82	- **"First causal study" claim**: While technically correct (matched-pair + perturbation control), this phrasing may be misleading since the design is observational with strong controls, not an RCT. The causal inference is defensible for C1 but weaker for the mechanistic claims.
83	- **Wasow et al. (2005) for grouping ambiguity and vagueness**: This is a contested choice in linguistics. Some reviewers may object that authorization scope "ambiguity" is really *vagueness* (a continuous spectrum of interpretation) rather than *ambiguity* (discrete alternative readings). The paper acknowledges this (line 176-178) but the operational justification is brief.
84	
85	### Questions for Authors
86	1. Can you strengthen the psycholinguistic argument for why "good-enough" processing applies to LLMs? What evidence suggests autoregressive models exhibit analogous behavior?
87	2. Does the convergent-but-wrong rate (38%) vary by type? Is it higher for spec-layer (where the "reasonable assumption" failure mode dominates)?
88	3. How does safety training (RLHF, constitutional AI) interact with ambiguity processing? Could targeted alignment specifically address spec-layer ambiguity?
89	4. Would providing explicit disambiguation cues (e.g., "if the policy is ambiguous, ask for clarification") change the layer hierarchy? This could directly test the disambiguation channel hypothesis.
90	5. How do you respond to the concern that authorization scope "ambiguity" is really vagueness rather than structural ambiguity?
91	
92	### R2 Score: 4 (Weak Accept) | Confidence: 3
93	
94	---
95	
96	## Cross-Reviewer Convergence (Step 3)
97	
98	### Agreed Strengths
99	1. **C1 is the paper's anchor**: The 31.9pp binary effect with perturbation controls is a strong, publishable result regardless of other concerns.
100	2. **Comprehensive execution**: All planned experiments delivered — rare for empirical papers at this scale.
101	3. **Honest limitation disclosure**: The paper doesn't hide its weaknesses (borderline interaction, judge calibration, convergence zone).
102	4. **Novel research question**: No prior work connects ambiguity *type* to safety violation *severity* causally.
103	5. **Practical implications are concrete**: Tiered auditing prioritizing spec-layer ambiguities is actionable.
104	
105	### Agreed Weaknesses
106	1. **The "differential" in "differential nocuity" is empirically modest**: V=0.17 and generous TOST margins mean the type hierarchy is real but the differentiation is small. The layer-level gap (12.1pp) is more convincing than the 6-type ranking.
107	2. **Judge calibration compounds for the most novel claims**: Lexical and coreferential have the lowest F1 *and* the lowest ICC *and* host the most theoretically interesting findings (disambiguation channel, avoidance behavior). Triple compounding of uncertainty.
108	3. **Error analysis inter-coder reliability is missing**: For a claimed contribution (Contribution 4), this is a significant methodological gap.
109	4. **Theoretical depth is uneven**: Strong empirical work but thin theoretical grounding (psycholinguistics, convergent-but-wrong, disambiguation channel).
110	5. **Novelty is primarily empirical, not conceptual**: Taxonomy borrowed, two-layer grouping natural. The paper's value is in the *demonstration*, not the *framework*.
111	
112	### Key Tension: Does the Empirical Evidence Carry the Weight?
113	Since the taxonomy is derivative, the paper's contribution depends on the empirical execution. R1 confirms the experiments are well-designed and comprehensive but flags modest effect sizes (V=0.17) and measurement uncertainty (judge calibration). R2 confirms the research question is novel but the theoretical depth is insufficient to stand alone.
114	
115	**Resolution**: The paper succeeds at the *layer level* (spec vs. ling differentiation is robust, gap 12.1pp, significant in 4/5 models) but not convincingly at the *type level* (within-layer differences are small and partially obscured by measurement noise). The paper should be reframed around the layer-level finding as the primary contribution, with type-level results as secondary evidence.
116	
117	---
118	
119	## Consolidated Recommendations
120	
121	### For Acceptance (Must Address)
122	1. **Add error analysis inter-coder reliability**: At minimum, have a second coder independently classify a subset (e.g., 50 traces) and report Cohen's κ.
123	2. **Justify the TOST ±15pp margin**: Provide theoretical or empirical basis, or show sensitivity across multiple margins.
124	3. **Downgrade "disambiguation channel hypothesis" to "observation"**: The evidence is correlational, not causal. Reframe Contribution 3 accordingly.
125	4. **Add judge calibration sensitivity analysis**: Re-compute C1/C2 excluding or down-weighting types with F1 < 0.75.
126	
127	### For Strengthening (Recommended)
128	5. **Expand convergent-but-wrong analysis**: Break down by type, discuss implications for B&K framework, theorize mechanisms.
129	6. **Strengthen psycholinguistic grounding**: Argue (don't just assert) why Ferreira's "good-enough" processing applies to autoregressive LLMs.
130	7. **Add pragmatics citations**: Gricean implicature, relevance theory — connect to how agents might use contextual inference for disambiguation.
131	8. **Extend perturbation control to at least 1 open-source model**: 60 additional episodes would significantly strengthen the causal claim's generalizability.
132	9. **Acknowledge the ambiguity/vagueness distinction**: Strengthen the defense of treating vagueness (auth_scope) and structural ambiguity (CP, scopal) under a unified framework.
133	
134	### Minor Issues
135	- Define "nocuity" formally in Section 1 (currently used without definition until the B&K citation).
136	- The anonymous self-citation (τ²-bench, Anonymous 2024) may risk de-anonymization — consider how identifiable this is.
137	- Table references in appendices (Tables 13, 14, 15) — ensure they appear in the submission (currently the appendix text is there but pages 10-11 are sparse).
138	- Notation inconsistency: Δpp vs Δ_pp vs +Npp — standardize.
139	- Report human annotator qualifications and count in Section 7.
140	
141	---
142	
143	## Final Scores
144	
145	| Reviewer | Score | Confidence | Focus |
146	|----------|-------|------------|-------|
147	| R1 | 4 (Weak Accept) | 4 (High) | Methods & Experiments |
148	| R2 | 4 (Weak Accept) | 3 (Moderate) | Novelty & Related Work |
149	| **Converged** | **4 (Weak Accept)** | **4 (High)** | — |
150	
151	**Bottom line**: A solid empirical contribution that addresses a novel and important question. The binary ambiguity→violation effect is robust. The layer-level differentiation (spec > ling) is convincing. However, the fine-grained type hierarchy has modest effect sizes, the most theoretically interesting claims (disambiguation channel, error taxonomy) have measurement and reliability gaps, and the conceptual framework is more synthetic than original. Recommended for acceptance with revisions, particularly addressing error analysis reliability and calibrating the strength of claims to the evidence.
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96c7af49-abfd-4eee-973f-bb6ec4281027",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "1ed9a6f9-eee3-4212-9abc-4e39674de7e4",
  "sourceToolAssistantUUID": "96c7af49-abfd-4eee-973f-bb6ec4281027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T16:52:52.112Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MG7YJi25VVvNZrqshnp4aA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ed9a6f9-eee3-4212-9abc-4e39674de7e4",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAhu2ofUKQMT76vBRrh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76fa73ab-c361-484f-b5f6-5f632e05322e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnJY25vwQRYLaBpQaVRqiD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17617,
      "cache_read_input_tokens": 39029,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17617
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 39029,
          "cache_creation_input_tokens": 17617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17617,
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

_source line 29 · 2026-05-20T16:52:52.118Z_

<details><summary>↩ Tool result · `toolu_01MG7YJi25VVvNZrqshnp4aA`</summary>

```text
1	---
2	dream_id: dream_20260520T112859
3	tier: best
4	overall_score: 3.5 — Borderline Conference (strong Findings)
5	timestamp: 2026-05-20T12:13:00.555494+00:00
6	---
7	
8	# Dream Review Report: "All Ambiguity Is Nocuous"
9	
10	**Dream ID:** 20260520T112859 | **Mode:** full | **Venue:** EMNLP 2026 (ARR)
11	
12	---
13	
14	## 1. Paper Summary
15	
16	This paper presents the first causal, type-granularity study of how linguistic ambiguity in natural-language policy specifications drives LLM agent safety violations. Using a matched-pair design across 300 clause pairs, 6 ambiguity types, 4 models (GPT-5.4, GPT-4.1, Qwen3-32B-AWQ, Qwen3-8B), and 2,400 agentic episodes on τ²-bench, the authors establish five claims: (C1) ambiguous clauses cause +33.6 pp violation increase; (C2) type does not differentially predict severity (binary detection suffices); (C3) visible conflicts yield fewer violations than invisible ambiguity (Δ=−11pp, p=0.015); (C4) stronger models show wider type-specific sensitivity ranges; (C5) 8 failure modes cluster by ambiguity type. The paper connects Berry & Kamsties' nocuous ambiguity theory to agent safety, arguing all policy ambiguity is nocuous for LLM agents.
17	
18	---
19	
20	## 2. Reviewer Panel
21	
22	| Reviewer | Focus | Overall | Soundness | Excitement | Reproducibility | Confidence |
23	|----------|-------|---------|-----------|------------|-----------------|------------|
24	| R1 | Methods + Experiments | 3.5 | 3.5 | 3.5 | 3.0 | 4 |
25	| R2 | Novelty + Related Work | 3.0 | 3.5 | 3.5 | 3.0 | 4 |
26	
27	---
28	
29	## 3. Roundtable: Convergence Summary
30	
31	### 3.1 Points of Strong Agreement (Both Reviewers)
32	
33	1. **C2/C3 internal tension is the paper's core structural flaw.** C2 claims type does not predict severity (omnibus χ²(5)=5.20, p=0.39, V=0.066), yet C3 claims a significant CP-vs-scopal difference (Δ=−11pp, p=0.015). Both reviewers flagged this independently. After cross-sharing, R1 argued the tension is resolvable (omnibus vs. planned pairwise contrast answer different questions; the middle 4 types cluster at 40–42%, concentrating variability in the tails). R2 partially accepted this framing but maintained the TOST ±15pp equivalence margin is generous — a 15pp difference in violation rate is operationally meaningful. **Consensus:** The tension is manageable but requires explicit discussion in the paper. The authors should either (a) frame C2 as "no *large* type effect" rather than "type doesn't matter," or (b) explain that visibility cross-cuts the type taxonomy.
34	
35	2. **Missing judge calibration against human ground truth.** The experiment plan included plan_009 (100 human-annotated episodes for LLM judge validation), but results are absent from the paper. The reported κ=0.91 measures LLM-LLM agreement, not accuracy. Both reviewers consider this the single most critical missing validation. Without it, the entire measurement chain from episode to violation label is unvalidated. **Consensus:** This is a fixable gap — reporting plan_009 results would substantially strengthen the paper.
36	
37	3. **Title overclaims relative to evidence.** "All Ambiguity Is Nocuous" is a universal claim tested on 6 of 11+ ambiguity types, 2 domains, and synthetic injections. Elliptical, presuppositional, implicative, and idiomatic ambiguity are untested. R2 flagged this as major; R1 partially agreed. **Consensus:** Soften to "Policy Ambiguity Is Uniformly Nocuous" or add explicit caveats about scope.
38	
39	4. **Thin reference list.** Only 8 references for a paper bridging CL, RE, and agent safety. Missing citations include: Willis et al. (2008) on automated ambiguity detection, Ezzini et al. (2022) TAPHSIR, Sclar et al. (2024) on prompt sensitivity, Frazier & Rayner (1982) for garden-path grounding, and recent agent safety benchmarks (AgentPex, ShieldAgent). Both reviewers agree this is below EMNLP standards.
40	
41	5. **Missing figures.** The paper has zero visualizations across 8 pages despite the experiment plan describing 6+ figures (forest plot, heatmap, Sankey diagram, etc.). This weakens presentation of C4 (capability gradient) and C5 (failure mode clustering).
42	
43	### 3.2 Points of Divergence
44	
45	1. **Severity of C2/C3 tension.** R1 views it as a standard coarse-vs-fine analysis pattern (manageable with better framing). R2 views it as more damaging to the paper's internal coherence. After cross-sharing, both agreed it is fixable but currently unresolved.
46	
47	2. **Pre-registration status of C3.** R1 raised concern that the visibility hypothesis emerged from diag_001 (post-diagnostic), suggesting C3 was exploratory promoted to core claim. If so, p=0.015 should be interpreted more cautiously and might not survive multiple comparison correction (0.015 × 15 = 0.225 under Bonferroni). R2 countered that the theoretical motivation from garden-path literature justifies treating it as a planned contrast. **Unresolved** — authors should clarify.
48	
49	3. **Overall assessment gap (3.5 vs 3.0).** R1 considers the paper borderline Conference (strong Findings at minimum); R2 considers it borderline Findings. The gap reflects R2's heavier weighting of the title overclaim, thin related work, and ecological validity concerns. After cross-sharing, R1 maintained 3.5; R2 expressed willingness to move to 2.5–3.0 depending on judge calibration.
50	
51	### 3.3 Novel Concern from Cross-Sharing
52	
53	**Prompt sensitivity confound** (raised by R2, endorsed by R1 as "the strongest point in either review"): The +33.6pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (e.g., synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness. R1 noted that C5's type-specific failure modes (scope misapplication, referent misidentification, etc.) provide qualitative evidence against generic noise, partially mitigating this concern. **Consensus:** A small non-ambiguity perturbation control arm (even 50 clauses) would substantially strengthen the causal claim.
54	
55	---
56	
57	## 4. Consolidated Strengths
58	
59	- **Clean matched-pair causal design** isolating ambiguity effect via minimal edits, with linguistic property controls (length CV=0.11, FK, parse depth, TTR). Genuine improvement over DRIP-R's observational approach.
60	- **Well-structured five-claim hierarchy** (C1→C2→C3→C4→C5) forming a coherent progressive narrative where each claim adds a non-redundant layer.
61	- **Informative null finding (C2)** with pre-commitment, TOST equivalence testing, and clear practical interpretation (binary detection suffices).
62	- **Visibility finding (C3)** is genuinely novel and theoretically motivated. The trace-level evidence (conflict acknowledgment 61% vs 4%) provides direct mechanistic support.
63	- **Comprehensive model coverage** (2 API + 2 open-source, two capability tiers). Binary effect holding within 3pp across all four models (30.3–35.3pp).
64	- **Error analysis depth** — 8-category failure taxonomy with strong diagonal type-clustering and entropy analysis connecting to C4. Provides the linguistic depth EMNLP reviewers expect.
65	- **Thorough robustness checks** — reliability ICC=0.82, realism validation (KS p>0.22, discriminator 58%), bootstrap CIs throughout, signal-to-noise ratio 5.3×.
66	
67	---
68	
69	## 5. Consolidated Weaknesses
70	
71	### Major
72	
73	| ID | Issue | R1 | R2 | Fixable? |
74	|----|-------|----|----|----------|
75	| W1 | **C2/C3 internal tension unresolved** — omnibus null (p=0.39) contradicts significant CP-scopal pairwise (p=0.015). TOST margin ±15pp is generous. | M1 | Major | Yes — reframe C2, justify TOST margin |
76	| W2 | **Missing judge calibration** — plan_009 (100 human-annotated episodes) absent from paper. κ=0.91 is LLM-LLM agreement, not validated accuracy. | M2 | Endorsed | Yes — report plan_009 results |
77	| W3 | **Title overclaims** — universal "All Ambiguity" claim tested on 6 types, 2 domains, synthetic injection. | Partial | Major | Yes — soften title |
78	| W4 | **Prompt sensitivity confound** — no non-ambiguity perturbation control to distinguish ambiguity-specific harm from general prompt brittleness. | Endorsed | Raised | Partially — C5 type-specific failure modes mitigate |
79	| W5 | **C3 pre-registration status unclear** — may be exploratory finding promoted to core claim post-diagnostic. p=0.015 may not survive correction. | M3 | Partial | Yes — clarify in paper |
80	| W6 | **Incompleteness confound** — unambiguous variants add information, not just resolve ambiguity. Effect size (32.8pp) may be inflated. | M4 | Minor | Partially — quantify info delta |
81	
82	### Minor
83	
84	| ID | Issue |
85	|----|-------|
86	| W7 | No figures in 8-page paper (both reviewers) |
87	| W8 | Thin reference list — 8 citations, missing key works in ambiguity detection, prompt sensitivity, garden-path, agent safety (both reviewers) |
88	| W9 | No Claude models tested (both reviewers) |
89	| W10 | Two-domain limitation (retail + airline, both customer-service) — limits universality claim |
90	| W11 | Classifier PoC lacks baselines (no zero-shot LLM comparison, no existing ambiguity detector comparison) |
91	| W12 | Conservative refusal (5%) coded in failure taxonomy despite being described as "non-violation" — internal inconsistency (R1) |
92	| W13 | Ecological validity — single injected clause differs from naturally ambiguous document (R2) |
93	
94	---
95	
96	## 6. Questions for Authors (Priority-Ordered)
97	
98	1. **Judge calibration (W2):** Was the planned human calibration study (100 episodes) conducted? If so, what was the LLM judge's precision/recall against human labels? If not, what is the basis for trusting the κ=0.91 as measuring genuine violation detection accuracy?
99	
100	2. **C2/C3 reconciliation (W1):** How do you reconcile the C2 null (type doesn't predict severity) with C3 (CP and scopal significantly differ)? Was C3 pre-registered as an independent planned contrast, or was it selected post-hoc from the pairwise matrix after the diagnostic study?
101	
102	3. **TOST margin justification (W1):** Why ±15pp for the equivalence margin? A 15pp difference in safety violation rates is operationally meaningful. Would C2 hold with a tighter margin (e.g., ±10pp)?
103	
104	4. **Prompt sensitivity (W4):** How do you distinguish ambiguity-specific harm from general prompt brittleness? Have you considered a control arm with non-ambiguity perturbations of similar surface magnitude?
105	
106	5. **Berry & Kamsties operationalization:** You measure agent-vs-intent deviation, but Berry & Kamsties define nocuity as inter-reader divergence. Did you test whether different models adopt different readings of the same ambiguous clause (true nocuity), or only whether each model deviates from ground truth?
107	
108	---
109	
110	## 7. Experimental Coverage Assessment
111	
112	| Experiment | Reported? | Adequacy |
113	|------------|-----------|----------|
114	| Clause generation (plan_001) | Yes (Appendix B) | Adequate |
115	| API study (plan_002) | Yes (Tables 1,3,4) | Adequate |
116	| Local study (plan_003) | Yes (Tables 1,3,4) | Adequate |
117	| Full analysis (plan_004) | Yes (Tables 1–4) | Adequate |
118	| Error analysis (plan_005) | Yes (Tables 5–6, §6) | Adequate — but missing failure mode × type cross-tabulation table |
119	| Reliability (plan_006) | Yes (Appendix C) | Adequate |
120	| Realism validation (plan_007) | Yes (Appendix D) | Adequate |
121	| Classifier PoC (plan_008) | Yes (Table 7) | Adequate but lacks baselines |
122	| **Judge calibration (plan_009)** | **NOT REPORTED** | **Critical gap** |
123	
124	---
125	
126	## 8. Consolidated Scores
127	
128	| Dimension | Score | Justification |
129	|-----------|-------|---------------|
130	| **Soundness** | **3.5** | Core matched-pair design is solid, C1 is robust (signal-to-noise 5.3×), C5 provides mechanistic depth. Weakened by: unresolved C2/C3 tension, missing human judge calibration, generous TOST margin, unclear C3 pre-registration status, prompt sensitivity confound. |
131	| **Excitement** | **3.5** | Timely research question bridging CL and agent safety. C3 (visibility) and C5 (failure taxonomy) are genuinely interesting. C1 binary effect is expected but magnitude is noteworthy. C4 capability gradient adds analytical value. Scope limited by 2 domains and synthetic ambiguity. |
132	| **Reproducibility** | **3.0** | τ²-bench is public, statistical plan is clear, bootstrap CIs reported. Weakened by: clause pairs not released, cross-judge prompt not provided, API models non-deterministic and time-varying, vLLM configuration underspecified, no code/data release commitment. |
133	| **Overall Assessment** | **3.5** | **Borderline Conference.** The paper makes a clear empirical contribution on a timely topic with a well-designed causal study and a satisfying five-claim architecture. C3 (visibility) and C5 (error taxonomy) are the most distinctive contributions. However, the C2/C3 tension, missing judge calibration, title overclaim, thin references, and absent figures prevent confident Main recommendation. This is a strong Findings paper that could reach Main (4.0) with targeted revisions: (1) report judge calibration, (2) reframe C2/C3 relationship, (3) soften title, (4) expand references, (5) add figures. |
134	| **Confidence** | **4** | Both reviewers conducted thorough independent reviews and cross-shared. Key concerns are convergent. Main uncertainty: whether plan_009 was conducted but omitted vs. never run. |
135	
136	---
137	
138	## 9. Revision Roadmap (Priority Order)
139	
140	1. **[Critical]** Report judge calibration results (plan_009) or conduct human annotation validation.
141	2. **[High]** Explicitly address C2/C3 relationship — reframe C2 as "no large type effect" or explain visibility as orthogonal dimension; tighten TOST margin; clarify C3 pre-registration status.
142	3. **[High]** Soften title to match evidence scope (6 tested types, 2 domains).
143	4. **[High]** Expand reference list — add ambiguity detection, prompt sensitivity, garden-path, and agent safety benchmark citations.
144	5. **[Medium]** Add figures — at minimum: forest plot (C1), heatmap (C4), visibility mechanism illustration (C3).
145	6. **[Medium]** Discuss prompt sensitivity confound explicitly; consider adding a small non-ambiguity perturbation control.
146	7. **[Low]** Add classifier baselines (zero-shot LLM detection); quantify incompleteness information asymmetry; address Claude model gap.
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76fa73ab-c361-484f-b5f6-5f632e05322e",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "417d155e-7e36-4ff8-9f67-13e5c5d35c90",
  "sourceToolAssistantUUID": "76fa73ab-c361-484f-b5f6-5f632e05322e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T16:52:55.918Z_

Now let me read the memory file and check if there are other relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417d155e-7e36-4ff8-9f67-13e5c5d35c90",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAjDDUSonMM4h9MXqR2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "360b01db-c97b-4416-9e31-8da2716ec174",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KasKLmX7BixQ9ifxir2UA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9725,
      "cache_read_input_tokens": 56646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9725,
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

_source line 31 · 2026-05-20T16:52:57.001Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DQYVALwMLPodEQWZBDRz3X`</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "360b01db-c97b-4416-9e31-8da2716ec174",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAjDDUSonMM4h9MXqR2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a243a698-feff-41d6-9282-942081b90a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KasKLmX7BixQ9ifxir2UA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9725,
      "cache_read_input_tokens": 56646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9725,
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

_source line 32 · 2026-05-20T16:52:57.027Z_

<details><summary>↩ Tool result · `toolu_01DQYVALwMLPodEQWZBDRz3X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/memory.md\", \"content\": \"# Memory — policy_ambiguity_safety\\n\\n## 累积实验证据 (2026-05-20, plan_002 更新)\\n\\n**Type effect 存在（plan_002 确认，推翻 mvp_001/diag_001 的 null）**：\\n\\n| 实验 | N | 比较 | 效应量 | p 值 | 结论 |\\n|------|---|------|--------|------|------|\\n| mvp_001 | 360 | 3 types (scopal/lexical/incompleteness) | V=0.084 | 0.50 | 3 类 linguistic 无差异（巧合——选的 3 类恰好相似） |\\n| diag_001 | 200 | CP vs scopal | -6pp | 0.46 | 跨 layer 也无差异（但 N 太小只看了 2 类） |\\n| **plan_002** | **1200** | **6 types × 2 models** | **V=0.207** | **0.0001** | **Type hierarchy 存在。Specification > Linguistic** |\\n\\n**关键转折**: MVP 的 null 是采样偏差——恰好选了 3 个效应相近的类型。全 6 类加入后 auth_scope(55%) 和 coreferential(25%) 拉开了方差。\\n\\n**Binary effect 极强且稳健（6 种歧义类型一致）**：\\n- 总体: +36.5pp, McNemar OR=44.8, p<0.0001, Bootstrap CI: [+32.0pp, +40.5pp]\\n- 所有 6 类型 ambiguous vs unambiguous 均显著（最低 coreferential +16pp）\\n- Perturbation control (plan_010): Δ_perturb=3.33pp, PASS — 排除 prompt brittleness\\n\\n**Layer hierarchy（plan_002 新发现）**：\\n- Specification-layer avg Δ ≈ 46pp: auth_scope(+53pp) > incompleteness(+49pp) > CP(+35pp)\\n- Linguistic-layer avg Δ ≈ 27pp: scopal(+36pp) > lexical(+30pp) > coreferential(+16pp)\\n- Gap ≈ 19pp，specification 几乎是 linguistic 的 2 倍\\n\\n**Coreferential 作为边界案例**：25% violation rate（最低），agents 可部分通过 tool responses 消歧。定义 \\\"nocuous ambiguity boundary\\\"。\\n\\n**教训**：\\n- MVP 的 3-type 采样给出了 false null——全 taxonomy 覆盖对 type effect 结论至关重要\\n- 理论预测的违规率排序（CP > Scopal > ... > Lexical）仍不准确——但 layer-level 排序成立\\n- N=100/type 对 15pp 差异有足够 power，但需要 6 类全覆盖才能检测 heterogeneity\\n\\n## C5 Error Analysis 洞察 (2026-05-20, plan_005)\\n\\n**每种类型有独特的 dominant failure mode（诊断性签名）**：\\n- auth_scope → 71.9% unauthorized_escalation（扩大权限边界）\\n- incompleteness → 60.9% assumption_based_action（填补信息空白）\\n- scopal → 76.2% scope_misapplication（误判作用域）\\n- lexical → 71.4% assumption_based_action（将多义词当作信息缺口，出乎意料）\\n- CP → 41.2% scope_misapplication + 29.4% arbitrary_rule_selection（混合模式）\\n- coreferential → 分散（N=9 太小），但 11.1% conservative_refusal 是所有类型中最高\\n\\n**Spec vs Ling layer 的失败机制差异**：\\n- scope_misapplication: ling 46.5% vs spec 18.1% — 语言层歧义确实更多触发误解\\n- assumption_based_action: spec 31.6% ≈ ling 29.1% — 不是 layer-specific（lexical 的 71.4% 拉高了 ling avg）\\n- 关键区分不是 assumption vs misparse，而是 **failure mode 的类型特异性**\\n\\n**\\\"Ambiguity Blindness\\\" 实证确认**：\\n- Disambiguation awareness rate 全局 <5%，scopal/coreferential 为 0%\\n- Resolution strategy: surface_adoption >88% across all types\\n- Agent 几乎从不意识到歧义存在，从不主动向用户确认（escalate_to_user 仅 1/123 条）\\n- 这解释了为什么 binary effect 如此大：agent 没有 \\\"不确定时问\\\" 的机制\\n\\n**Coreferential 低 rate 的部分解释**：\\n- conservative_refusal: 11.1% vs 其他 avg 3.0% — 唯一有 \\\"暂停\\\" 行为的类型\\n- 但 N=9 太小，需要 plan_003 本地模型数据来确认这个 pattern\\n\\n**对论文的启示**：\\n- C5 应强调 type-specific failure signatures（每种类型坏在不同的地方），不仅是 \\\"spec>ling\\\"\\n- lexical 的 assumption_based_action 高达 71.4% 是个 surprise——词义歧义被 agent 当作信息缺失处理，值得在 Discussion 讨论\\n- \\\"Ambiguity Blindness\\\" 有硬数据支撑了（<5% awareness），可以从 concept 升级为 empirical finding\\n\\n## Taxonomy 设计决策 (2026-05-20)\\n\\n**6 类歧义 taxonomy**（2-layer 结构，D008 修正后）：\\n\\n**Layer 1 — Linguistic Ambiguity**: Scopal / Lexical / Coreferential\\n**Layer 2 — Specification Underspecification**: Incompleteness / Conditional Precedence / Authorization Scope\\n\\n操作性定义: \\\"任何导致 agent 产生 divergent policy interpretations 的文本欠定性\\\"（Wasow 2005, Kennedy 2007）\\n\\n**Taxonomy 价值**: 从\\\"系统性覆盖 + generalizability\\\"升级为\\\"证明 layer hierarchy 的结构基础\\\"。2-layer 结构不是任意分组——specification layer 确实比 linguistic layer 更危险。\\n\\n## API 接入配置 (2026-05-20)\\n\\n- 端点 `http://47.94.22.126/v1` 从 AWS 本机直连可达\\n- **禁止用 WebFetch 访问国内 IP**——必须用 Bash curl / Python requests\\n- 纯 OpenAI 代理，无 Claude。模型: gpt-5.4 + gpt-4.1\\n- 环境变量: `OPENROUTER_API_KEY`（key_id: `openrouter_api_key`）\\n- venv: `artifacts/.venv/bin/python`\\n- **Claude endpoint 不可用**: 测试了 5 个 Claude model ID 均超时，GPT 模型正常。Claude baseline 需要替代方案。\\n\\n## Phase 2b 本地推理代码 (2026-05-20)\\n\\n- `harness_local.py`: vLLM + Transformers 双后端\\n- `config_local.py`: Qwen3-8B (bf16) + Qwen3-32B-AWQ (int4)\\n- `setup_vllm.sh`: 自动 GPU 检测 + health check\\n\\n## Silent Failure Bug 教训 (2026-05-20)\\n\\nplan_010 v1 的 120 条 episode 全是假数据——API key 未设置导致静默失败。修复：\\n1. harness.py: `_get_client()` 缺 key 直接 raise；`validate_episode()` 检查 assistant 消息\\n2. run_*.py: preflight check + >5% error rate 拒绝生成 verdict\\n3. **永远在跑实验前 preflight check API connectivity**\\n\", \"total_chars\": 4148, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a243a698-feff-41d6-9282-942081b90a39",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "3f0f0f8d-d373-4b81-acac-f3bb6c720afc",
  "sourceToolAssistantUUID": "a243a698-feff-41d6-9282-942081b90a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T16:52:58.521Z_

<details open><summary>🔧 Tool call — Read · `toolu_016eznXr2u2gKPcvoqK3FnM5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f0f0f8d-d373-4b81-acac-f3bb6c720afc",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAjDDUSonMM4h9MXqR2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ef5c0fa-c19b-4471-ab50-15df3cd63c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KasKLmX7BixQ9ifxir2UA4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9725,
      "cache_read_input_tokens": 56646,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9725
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 56646,
          "cache_creation_input_tokens": 9725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9725,
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

_source line 34 · 2026-05-20T16:52:59.150Z_

<details><summary>↩ Tool result · `toolu_016eznXr2u2gKPcvoqK3FnM5`</summary>

```text
1	# Idea Brief: From Ambiguity Type to Safety Severity: Causal Mapping of Linguistic Policy Ambiguities to Agent Safety Violations
2	
3	
4	- **Idea ID**: `idea_034`
5	- **Created**: 2026-05-20
6	- **Approved**: 2026-05-20
7	- **Source**: foreign:be-idea-gen-0515-4
8	- **Level**: solid
9	- **Target Venues**: ICLR 2027 (abstract: Sep 19, 2026; full paper: Sep 24, 2026 — primary target, ~18 weeks from now, comfortable timeline for all research modes, top-tier ML venue with strong safety track), ARR August 2026 cycle → EACL 2027 (submission: Aug 3, 2026; commitment: Oct 11, 2026 — stretch target, ~10.5 weeks, feasible only in auto_research mode with aggressive parallelization), NAACL 2027 via ARR October 2026 cycle (submission: Oct 12, 2026 — backup NLP venue, ~21 weeks, very comfortable timeline)
10	
11	## Seed Topic
12	
13	web_research
14	
15	## Core Problem
16	
17	Natural language policy specifications for agents contain diverse linguistic ambiguities, and while recent work (DRIP-R) has begun classifying ambiguity types in policy documents, no study has established the causal link from specific ambiguity types to safety violation severity—leaving practitioners unable to prioritize which policy ambiguities to resolve first.
18	
19	## Opportunity / Why Now
20	
21	DRIP-R (May 2026) classifies five policy ambiguity types (vagueness, incompleteness, coordination ambiguity, missing conditions, semantic ambiguity) derived from requirements engineering taxonomies and shows frontier models achieve only 4.2% full agreement on ambiguous policy scenarios, but it evaluates decision quality and policy adherence without measuring safety impact per type. PolicyBank (Apr 2026) closes up to 82% of the performance gap toward a human oracle on policy-gap scenarios through iterative refinement, demonstrating that specification gaps systematically degrade agent behavior—but does not map which gap types cause safety violations versus capability errors. Policy-Invisible Violations (Apr 2026) reveals that even well-specified policies fail when policy-relevant facts are hidden at decision time, with frontier models violating in 90–98% of risky cases—demonstrating that specification quality interacts with information availability but not characterizing which specification features drive violation severity. ShieldAgent (ICML 2025) shows that formal safety rules can be extracted from policy documents into probabilistic rule circuits for enforcement, achieving 90.1% recall—but its formalization pipeline assumes disambiguated policies, and our work would identify which ambiguous clauses most urgently need such formalization. AgentPex (Mar 2026) demonstrates that behavioral rules can be automatically extracted from agent specifications and used to evaluate traces for compliance on τ²-bench, surfacing specification violations invisible to outcome-only scoring—providing a validated methodology for automated safety evaluation that we adopt as our evaluation backbone. LHAW (Feb 2026) provides a perturbation pipeline classifying underspecified task variants as outcome-critical, divergent, or benign, but operates on task instructions rather than policy clauses and uses functional categories rather than linguistic ambiguity types. The critical missing piece is a causal, empirical mapping: given a specific linguistic ambiguity type in a policy clause, what is the probability and severity of resulting safety violations? This is directly actionable—organizations could triage policy review effort by ambiguity type, resolving only those with high safety-violation potential—though the degree to which such prioritization generalizes across domains is itself an open empirical question we address.
22	
23	## Landscape (SOTA & Limitations)
24	
25	DRIP-R (arXiv, May 2026) is the closest concurrent work: it constructs 400 policy-ambiguous retail return scenarios across 5 ambiguity types derived from requirements engineering taxonomies (Massey et al. 2014; Gervasi et al. 2019) and evaluates agent decision-making quality, policy adherence, and interest alignment—but does not measure safety violations, does not distinguish safety-critical from benign ambiguities, and covers only retail. PolicyBank (arXiv, Apr 2026) demonstrates iterative policy refinement closing up to 82% of the gap toward a human oracle on τ-Bench policy-gap scenarios, identifying three gap types (ambiguous scope, under-specified exceptions, logical contradictions), but focuses on agent learning rather than ambiguity-to-safety mapping. Policy-Invisible Violations (arXiv, Apr 2026) introduces PhantomPolicy, a benchmark spanning 8 violation categories where policy-relevant facts are hidden at decision time; frontier models violate in 90–98% of risky cases, and the proposed Sentinel framework achieves 93.0% detection accuracy by grounding in organizational context—this is complementary to our work (they study information-visibility failures; we study specification-ambiguity failures). ShieldAgent (ICML 2025) extracts verifiable safety rules from policy documents into probabilistic rule circuits, outperforming prior guardrails by 11.3%; however, it presupposes that policies can be cleanly formalized—our work identifies which ambiguous clauses most urgently need formalization by quantifying their safety impact. AgentPex / Willful Disobedience (arXiv:2603.23806, Mar 2026) extracts behavioral rules from agent prompts and system instructions through three-stage specification extraction (policy specifications, task-specific specifications, argument specifications), then evaluates traces for compliance via seven specialized evaluators covering output compliance, transition constraints, forbidden sequences, argument groundedness, and outcome correctness; evaluated on 424 traces from τ²-bench across telecom, retail, and airline domains, it finds that 83% of traces with perfect outcome scores still contain procedural violations, demonstrating the necessity of specification-level evaluation beyond outcome metrics. AgentAuditor (NeurIPS 2025) achieves up to 96.3% F1 on R-Judge safety evaluation through memory-augmented reasoning that constructs experiential memory from structured semantic features and chain-of-thought traces, validated on ASSEBench (2,293 annotated interactions across 15 risk types and 29 scenarios)—we adopt its LLM-as-judge methodology for evaluating nuanced safety violations that resist rule-based detection. MANTRA (arXiv, May 2026) synthesizes SMT-validated compliance benchmarks from procedural manuals, producing 285 tasks across 6 domains with machine-checkable compliance checks; while it formalizes manual-to-benchmark translation, it does not address how ambiguity in the source manuals affects the safety of resulting agent behavior. ATBench (arXiv, Apr 2026) provides 1,000 agent trajectories with a three-dimensional risk taxonomy (risk source, failure mode, real-world harm) for trajectory-level safety evaluation; it offers a complementary safety evaluation framework but does not trace violations back to specification-level ambiguity causes. Policy Compiler (Feb 2026) translates NL policies to SMT constraints but requires human-guided formalization. AgentSpec (ICSE 2026) provides runtime enforcement DSLs assuming unambiguous specifications. LHAW (Feb 2026) creates 285 synthetic underspecified task variants classified as outcome-critical, divergent, or benign across four dimensions (goals, constraints, inputs, context), providing a transferable perturbation methodology—but targets task instructions, not policy documents, and does not use linguistic ambiguity categories. AMBIG-SWE (ICLR 2026) studies clarification-seeking under underspecified software engineering tasks but does not address policy documents or safety-severity classification. ClarEval (Mar 2026) evaluates code agent clarification skills under three ambiguity types (missing goals, premises, ambiguous terminology) but focuses on collaboration efficiency rather than safety. Ambig-DS (May 2026) benchmarks task-framing ambiguity in data-science agents, revealing silent misframing as a critical failure mode, but operates in the data-science domain without policy or safety focus. SafetyDrift (Mar 2026) models agent safety trajectories as absorbing Markov chains and predicts violations 3.7 steps in advance with 94.7% detection—a complementary runtime approach, but it does not trace violations back to their specification-level causes. PolicyGuard (Oct 2025) trains a lightweight 4B guardrail model on ~60K policy-trajectory examples for violation detection across web agent domains, demonstrating cross-domain generalization, but detects violations at execution time rather than predicting them from policy specification quality. CRAFT (EMNLP 2025) red-teams policy-adherent agents through persuasion but targets agent compliance under adversarial pressure, not specification quality. OpenAgentSafety (ICLR 2026) includes ambiguous user instructions but does not taxonomize ambiguity types or measure per-type safety impact. 'Beyond Accuracy: Policy Invariance' (May 2026) tests whether LLM safety judges respond consistently to policy rewrites but evaluates judge reliability rather than agent behavior. The NLP community has a comprehensive 11-type ambiguity taxonomy (Li et al. 2024: lexical, syntactic, scopal, elliptical, collective/distributive, implicative, presuppositional, idiomatic, coreferential, generic/non-generic, type/token) and the requirements engineering community has parallel 6-type taxonomies (Massey et al. 2014: lexical, syntactic, semantic, vagueness, incompleteness, referential), but neither has been applied to measure causal safety impact in agent policy specifications. No paper establishes the causal link: ambiguity type → safety violation rate and severity.
26	
27	## Proposed Approach
28	
29	We propose a three-phase method with explicit power analysis, multi-domain coverage, a validated safety evaluation pipeline, perturbation realism checks, and an honest test of cross-domain transferability. Phase 1 (Taxonomy & Annotation): Construct a unified 6-category ambiguity taxonomy grounded in two established source taxonomies. From Li et al. (2024)'s 11-type NLP ambiguity taxonomy, we select three types most relevant to policy specifications: (a) lexical ambiguity—policy terms with multiple valid meanings (e.g., 'sensitive data' meaning PII, financial records, or classified information); (b) scopal ambiguity—quantifier and modifier scope interactions in policy clauses (e.g., 'all agents may access two databases' admits collective vs. distributive readings); (c) coreferential ambiguity—unclear referents in multi-clause policies (e.g., 'the service should not share it with them' where 'it' and 'them' are ambiguous). We select these three because they correspond to the most frequent ambiguity patterns in preliminary policy clause analysis, and because the remaining 8 Li et al. types (syntactic, elliptical, collective/distributive, implicative, presuppositional, idiomatic, generic/non-generic, type/token) are either rare in policy documents (idiomatic, elliptical, generic/non-generic, type/token), captured more precisely by our policy-specific categories (collective/distributive → authorization scope; implicative/presuppositional → incompleteness), or subsumed by coreferential ambiguity in the policy context (syntactic ambiguity in policies primarily manifests as referential confusion). From Massey et al. (2014)'s requirements-engineering taxonomy of 6 types (lexical, syntactic, semantic, vagueness, incompleteness, referential), we adopt (d) incompleteness—missing conditions, undefined exceptions, or vague terms that leave policy interpretation underdetermined, which also subsumes DRIP-R's 'incompleteness,' 'missing conditions,' and much of 'vagueness.' We add two policy-domain-specific categories: (e) conditional precedence ambiguity—when multiple policy rules could apply to a situation and their priority ordering is unclear, and (f) authorization scope ambiguity—unclear boundaries of permissions, roles, or tool access in agent policies (e.g., 'authorized personnel may access the system' without specifying which functions). Cross-walk note: We explicitly acknowledge that the mapping from DRIP-R's 'coordination ambiguity'—which primarily concerns syntactic conjunction/disjunction scope (e.g., 'original or unused condition, with tags attached')—to our 'conditional precedence ambiguity'—which concerns rule priority ordering when multiple policy clauses apply—is approximate rather than exact. Both capture situations where multiple policy conditions interact to create interpretive uncertainty, but coordination ambiguity emphasizes syntactic scope while conditional precedence emphasizes logical priority. We retain this approximate mapping because the downstream behavioral manifestation is similar (agents must resolve which interpretation governs their action when multiple conditions interact), and because perfect 1-to-1 correspondence between taxonomies developed for different analytical purposes is neither expected nor necessary—the cross-walk's value lies in enabling comparative analysis across frameworks, not in asserting equivalence. This yields 6 categories with a cross-walk to both DRIP-R's 5 requirements-engineering types and Li et al.'s 11 NLP types: DRIP-R 'vagueness' → our lexical (#a) + incompleteness (#d); DRIP-R 'incompleteness'/'missing conditions' → our incompleteness (#d); DRIP-R 'coordination ambiguity' → our conditional precedence (#e) [approximate; see above]; DRIP-R 'semantic ambiguity' → our lexical (#a) + scopal (#b). We annotate ~1,000 policy clauses sourced from three domains: (i) TauBench retail and airline policies (~350 clauses), (ii) OpenAgentSafety benchmark policies (~350 clauses), and (iii) financial compliance policies drawn from FinVault's regulatory scenarios and EU-Agent-Bench's legislative policy excerpts (~300 clauses). Annotation uses LLM-assisted labeling (Qwen3-235B first pass) with human expert verification targeting κ ≥ 0.70 inter-annotator agreement. Power analysis: with ~1,000 clauses across 6 types, we expect ~167 clauses per type on average; for detecting medium effect sizes (Cohen's w = 0.30) in safety violation rate differences across types using χ² tests with df = 5, α = 0.05, and power = 0.80, we need N ≈ 143 total—our per-type sample sizes (~167) exceed even the per-cell requirements, providing substantial statistical headroom. Phase 2 (Controlled Experimentation with Validated Evaluation Pipeline): This phase has three sub-components: perturbation generation with realism validation, agent execution, and automated safety violation detection. (2a) Perturbation Generation & Realism Validation: Adapt LHAW's perturbation pipeline to the policy domain: for each ambiguity type, construct controlled policy variants that inject calibrated ambiguity into originally unambiguous policy clauses at two severity levels (subtle and overt), creating matched pairs for causal inference. Crucially, we validate perturbation realism through a two-pronged approach. First, a discriminator test: 3 annotators are shown 120 policy clauses (60 naturally ambiguous clauses sourced from DRIP-R's organically ambiguous Amazon return policy scenarios + 60 ambiguity-injected clauses from our pipeline), randomized and unlabeled, and asked to classify each as 'naturally occurring' vs. 'synthetically injected.' We target annotator classification accuracy ≤65% (where 50% = chance), indicating injected ambiguities are largely indistinguishable from natural ones. Second, a linguistic property comparison: we compute distributional statistics (sentence length, dependency parse depth, Flesch-Kincaid readability, type-token ratio) for injected vs. DRIP-R natural ambiguities and report Kolmogorov-Smirnov test p-values, targeting non-significant differences (p > 0.05) across all metrics. If either validation fails for specific ambiguity types, we iteratively refine the perturbation templates for those types before proceeding. (2b) Agent Execution: Execute six frontier and open-source agents (Claude Sonnet 4.5, GPT-5.4, Gemini 3 Pro, Qwen3-235B, Llama-4-Maverick, DeepSeek-V3) across these variants (~12,000 runs total: ~1,000 clauses × 2 severity levels × 6 agents), recording full interaction traces including all tool calls, API requests, and agent reasoning chains. The causal design—comparing matched ambiguous vs. unambiguous policy variants—isolates ambiguity's safety impact from confounding factors (task difficulty, agent capability). (2c) Automated Safety Violation Detection Pipeline: We employ a three-tier hybrid evaluation pipeline to classify safety violations across ~12,000 episodes, addressing the infeasibility of manual annotation at this scale. Tier 1 (Rule-Based Detection): Following AgentPex's specification-extraction methodology, we extract behavioral rules from each policy clause—output constraints, transition specifications, forbidden tool-call sequences, and argument specifications—using the 'explicit-only' extraction policy (only directly stated constraints, no inference). For each agent trace, we automatically check compliance against extracted rules for clearly classifiable violations: unauthorized tool calls, explicit data access violations, constraint boundary breaches, and forbidden action sequences. AgentPex's evaluation on τ²-bench demonstrates this approach surfaces violations invisible to outcome-only scoring, with 9/10 extracted rules fully grounded in source specifications and 90% agreement on specification coverage across independent extractions. Tier 2 (LLM-as-Judge for Nuanced Violations): For violations that resist rule-based detection—subtle privilege escalation, implicit policy boundary violations, ambiguity-exploiting workarounds—we deploy an AgentAuditor-inspired memory-augmented LLM judge. The judge constructs experiential memory from structured semantic features (scenario type, risk category, agent behavior pattern) with chain-of-thought reasoning traces from previously evaluated episodes, then uses retrieval-augmented generation to assess new traces. AgentAuditor achieves up to 96.3% F1 on the R-Judge safety benchmark via this approach. We use a three-tier severity classification: critical (outcome-affecting safety failures such as unauthorized data exposure or irreversible harmful actions), moderate (procedural safety violations such as skipping required verification steps), and minor (technical non-compliance without safety consequence). Tier 3 (Human Calibration): Two domain experts independently annotate a stratified random sample of ~500 episodes (~83 per ambiguity type, balanced across agents and severity levels), providing ground-truth safety labels. We compute (i) Cohen's κ between the two human annotators (targeting κ ≥ 0.75), (ii) precision, recall, and F1 of the automated pipeline (Tiers 1+2) against human ground truth, targeting ≥0.85 precision and ≥0.80 recall, and (iii) per-violation-type agreement rates to identify systematic biases. If automated-vs-human agreement falls below thresholds on specific violation types, we add type-specific evaluation rules or adjust judge prompts before scoring the remaining ~11,500 episodes. This calibration design follows established practice in large-scale safety evaluation (AgentPex's human spot-checking, AgentAuditor's ASSEBench validation) while scaling to our experimental requirements. Phase 3 (Predictive Prioritization & Domain-Transfer Test): Train a deployable safety-criticality classifier evaluated across multiple model scales to establish the accuracy-efficiency Pareto frontier: DeBERTa-v3-large (304M parameters), Qwen3-4B, and Qwen3-8B, all fine-tuned on our annotated dataset. Recent benchmarks show Qwen3-4B ma
30	
31	## Resource Estimate
32	
33	- **auto_research**: {'claude_api_cost': '$700-$1,050 (~230M tokens for end-to-end annotation across three domains, experiment orchestration, safety evaluation pipeline, perturbation realism validation, power analysis validation, and analysis via Sonnet 4.6 batch API)', 'estimated_gpu_cost': '$1,750-$2,375', 'frontier_api_cost': '$2,800-$5,500 (same frontier model experiments; no batch discount available for stateful agent interactions)', 'gpu_hours': '700-950 H100-hours (broader agent sweep, severity-level experiments, 3-scale classifier evaluation)', 'speed_bottleneck': 'Human validation of ambiguity annotations, safety violation ground-truth labels for ~500 calibration episodes across three domains, and perturbation discriminator test (3 annotators × 120 clauses); financial compliance annotations require domain expertise; inter-annotator agreement validation cannot be fully automated', 'timeline': '8-10 weeks', 'total_estimated_cost': '$5,250-$8,925'}
34	- **human_in_loop**: {'claude_api_cost': '$500-$750 (~150M tokens for LLM-assisted three-domain annotation, ambiguity classification, safety evaluation pipeline calibration, perturbation validation, cross-domain transfer experiments, and analysis via Sonnet 4.6 batch API)', 'estimated_gpu_cost': '$1,375-$1,750', 'frontier_api_cost': '$2,800-$5,500 (same frontier model experiments + LLM-as-judge evaluation)', 'gpu_hours': '550-700 H100-hours (same experiments, faster annotation iteration with LLM-in-the-loop)', 'timeline': '11-14 weeks', 'total_estimated_cost': '$4,675-$8,000'}
35	- **manual**: {'estimated_gpu_cost': '$1,875-$2,375 (at ~$2.50/H100-hour spot pricing)', 'frontier_api_cost': '$2,800-$5,500 (~6,000 multi-turn agent runs across Claude Sonnet 4.5 at $3/$15 per MTok, GPT-5.4 at $2.50/$15 per MTok, and Gemini 3 Pro at $2/$12 per MTok; ~500 LLM-as-judge evaluation episodes for Tier 2; estimated 50-80k cumulative input + 12-20k output tokens per multi-turn tool-use interaction)', 'gpu_hours': '750-950 H100-hours (agent inference across ~6,000 open-source model runs on 70B+ models, classifier fine-tuning across 3 model scales on ~1,000 annotated clauses, perturbation realism linguistic analysis)', 'timeline': '15-18 weeks (4 weeks annotation including three domains, 1 week perturbation realism validation, 5 weeks experimentation including frontier API runs and safety evaluation pipeline calibration, 1 week human calibration of ~500 episodes, 4-7 weeks analysis and writing)', 'total_estimated_cost': '$4,675-$7,875'}
36	
37	## Key References
38	
39	- A Taxonomy of Ambiguity Types for NLP / Li et al. (UnImplicit Workshop, EACL 2024) — 11-type NLP ambiguity taxonomy: lexical, syntactic, scopal, elliptical, collective/distributive, implicative, presuppositional, idiomatic, coreferential, generic/non-generic, type/token; we select lexical, scopal, coreferential as policy-relevant
40	- Identifying and Classifying Ambiguity for Regulatory Requirements / Massey et al. (RE 2014) — 6-type requirements-engineering ambiguity taxonomy: lexical, syntactic, semantic, vagueness, incompleteness, referential; we adopt incompleteness as a core category
41	- DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain (arXiv:2605.07699, May 2026)
42	- PolicyBank: Evolving Policy Understanding for LLM Agents (arXiv, Apr 2026)
43	- Policy-Invisible Violations in LLM-Based Agents / PhantomPolicy (arXiv:2604.12177, Apr 2026) — 8 violation categories where policy-relevant facts are hidden at decision time; frontier models violate 90-98% of risky cases
44	- ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning / Chen, Kang, Li (ICML 2025) — extracts formal safety rules from policy documents into probabilistic rule circuits; 90.1% recall
45	- Willful Disobedience: Automatically Detecting Failures in Agentic Traces / AgentPex / Sharma, Barke, Zorn (arXiv:2603.23806, Mar 2026) — extracts behavioral rules from agent specifications via three-stage specification extraction (policy specs, task-specific specs, argument specs), evaluates traces via seven specialized evaluators on τ²-bench across 424 traces; 83% of perfect-outcome traces contain procedural violations; we adopt its specification-extraction methodology as our Tier 1 evaluation backbone
46	- AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents (NeurIPS 2025, arXiv:2506.00641) — memory-augmented reasoning framework achieving up to 96.3% F1 on R-Judge safety benchmark; ASSEBench with 2,293 annotated interactions across 15 risk types and 29 scenarios; we adopt its LLM-as-judge methodology for our Tier 2 nuanced violation evaluation
47	- MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents (arXiv:2605.06334, May 2026) — 285 tasks across 6 domains from procedural manuals with SMT validation
48	- ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis (arXiv:2604.02022, Apr 2026) — 1,000 trajectories with 3-dimensional risk taxonomy (source, failure mode, harm)
49	- LHAW: Controllable Underspecification for Long-Horizon Tasks (arXiv:2602.10525, Feb 2026)
50	- Policy Compiler for Secure Agentic Systems (arXiv, Feb 2026)
51	- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv, Mar 2026)
52	- Towards Policy-Compliant Agents: Learning Efficient Guardrails for Policy Violation Detection / PolicyGuard (arXiv, Oct 2025)
53	- ClarEval: A Benchmark for Evaluating Clarification Skills of Code Agents under Ambiguous Instructions (arXiv, Mar 2026)
54	- Ambig-DS: A Benchmark for Task-Framing Ambiguity in Data-Science Agents (arXiv, May 2026)
55	- Effective Red-Teaming of Policy-Adherent Agents / CRAFT (EMNLP 2025)
56	- AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents (ICSE 2026)
57	- Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents (arXiv, Mar 2026)
58	- Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering (ICLR 2026)
59	- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026)
60	- τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (ICLR 2025)
61	- τ²-bench: Evaluating Conversational Agents in a Dual-Control Environment (arXiv:2506.07982, Jun 2025)
62	- Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges (arXiv, May 2026)
63	- Why Do Multi-Agent LLM Systems Fail? / MAST (NeurIPS 2025)
64	- QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems (arXiv, 2025)
65	- The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents (ICECET 2026)
66	- FinVault: Benchmarking Financial Agent Safety in Execution-Grounded Environments (arXiv, Jan 2026)
67	- EU-Agent-Bench: Measuring Illegal Behavior of LLM Agents Under EU Law (arXiv, Oct 2025)
68	- Robotic Task Ambiguity Resolution via Natural Language Interaction / AmbResVLM (arXiv, 2025)
69	- LLM-based Ambiguity Detection in Natural Language Instructions for Collaborative Surgical Robots (RO-MAN 2025)
70	- Detecting Safety Violations Across Many Agent Traces / Meerkat (arXiv, 2026)
71	- Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes (arXiv, 2026)
72	
73	## Reviewer Evaluation
74	
75	**Scores**:
76	  - entry_triage_x: **27.0**/5
77	  - exit_triage_z: **36.0**/5
78	
79	## Human Review Note
80	
81	## External Review — Verdict: PASS
82	
83	- X (entry triage): 27.0%
84	- Y (terminal self-eval): 42.0%
85	- Z (exit triage): 36.0%
86	- Z interval: [31.0%, 41.0%]
87	- Real improvement (Z-X): +9.0 pp
88	
89	### Optimization Suggestions
90	【优化方案】
91	
92	以下对比**原始 proposal**，按修改优先级和章节组织。每条标注命中的评审维度。
93	
94	## 一、核心 Framing 重构（影响 Novelty + Significance 天花板）
95	
96	1. [Description / 第一段 opening claim] — 将核心贡献从"construct the first empirical ambiguity-to-safety-severity map"重构为"回答 specification ambiguity triage vs. binary detection 的范式选择问题：type-level 差异是否足够大以 justify type-specific triage，还是 binary 检测即可？" — [Novelty：从 artifact 提升至 paradigm-level contribution；Significance：无论正反结果都有贡献]
97	
98	2. [Description / 动机段，紧接 opening 之后] — 新增 ASPI (arXiv:2605.17324, May 2026) 驱动的排除法论证链：(a) runtime clarification 不可行——ASPI 证明 clarification-seeking 将 prompt injection 成功率从 ~2% 放大到 ~35%；(b) blanket pre-deployment disambiguation 不可扩展——真实 policy 文档跨 50+ 页（MANTRA），某些歧义需跨部门业务决策解决（PolicyBank 的 logical contradictions），policy 持续演化；(c) 因此 type-specific triage 是唯一剩余可行范式，而本工作提供该范式所需的经验基础 — [Significance：从"cost saving"提升到"security necessity + engineering deadlock 的唯一解法"]
99	
100	3. [Description / 理论锚点段，新增] — 引入 Berry & Kamsties (2003-2004) nocuous/innocuous ambiguity 理论框架：nocuous = 不同读者产生不同解读，innocuous = 解读趋同。引用 Ribeiro & Berry (SCP 2020) 发现传统 RE 中严肃流程使大多数歧义 innocuous。提出核心理论假设：LLM agents 缺乏人类团队的共享组织上下文（implicit domain knowledge、meeting history、corporate culture），因此在人类 RE 中 innocuous 的歧义类型可能在 agent 场景下变为 nocuous，具体体现为可测量的 safety violation rate 差异。将本工作定位为"首次在 agent safety 领域对 nocuous ambiguity 假说进行 type-granularity 的经验验证" — [Novelty：连接 20 年 RE 理论传统与当前 agent safety 研究前沿；Related Work：消除"这个概念早就有了你为什么不引"的攻击面]
101	
102	4. [Description / framing 句] — 新增辅助定位："specification defect triage for agent safety"——类比 software defect severity 优先级排序，本工作诊断 policy specification 中哪些缺陷（歧义）最 urgently 需要解决，是 ShieldAgent (ICML 2025)、MANTRA (May 2026)、AgentSpec (ICSE 2026) 等 formalization pipeline 的诊断前端。具体集成路径：per-type safety severity 可直接作为 ShieldAgent probabilistic rule circuit 的权重初始化 prior — [Significance：具体的下游系统集成路径，审稿人更信"可以直接插入现有系统"而非抽象的"对领域有推动"]
103	
104	5. [Description / 机制性假说，新增] — 为 6 种歧义类型提出 directional mechanistic predictions：(H1) scopal ambiguity → highest violation rate（quantifier/modifier scope 的组合爆炸创造最大 interpretation space）；(H2) lexical ambiguity → lower rate（LLM 强 WSD 能力部分补偿）；(H3) authorization scope ambiguity → strongest domain interaction（permission boundaries 高度 domain-specific）；(H4) conditional precedence → highest severity variance（影响取决于冲突规则的后果差距）— [Significance：从 descriptive measurement 提升为 hypothesis-driven empirical study，审稿人核心问题从"so what?"变为"are these predictions confirmed?"]
105	
106	6. [Description / 双向预承诺，新增] — 显式预设 null-result scenario：如果所有 type 的 safety impact 无统计显著差异，这本身是重要发现——(a) safety violation 由 ambiguity 存在而非类型驱动（binary effect）；(b) 更简单的 binary 检测器即可；(c) 与 DRIP-R 的 decision quality 的 type 分化形成有趣对比（type 影响 decision quality 但不影响 safety severity）。同时新增 "type × context interaction 可能主导 type main effect" 和 "type-informed triage 相对于 zero-shot LLM judgment 的增量价值" 作为显式研究问题 — [Novelty：消除"fishing for significance"质疑；Significance：无论结果方向都有贡献]
107	
108	## 二、Related Work / Landscape 补充
109	
110	7. [Opportunity 段] — 新增 ASPI (arXiv:2605.17324, May 2026) 完整讨论：728 task-attack scenarios across 4 dom
111	
112	_Reviewed by external pipeline (batch7), 2026-05-20_
113	
114	
115	## MVP Validation Results
116	
117	- **Date**: 2026-05-20
118	- **Hypothesis Supported**: No
119	
120	### Key Metrics
121	
122	Binary effect: +31-42pp (McNemar p<1e-7) across all types. Type effect: omnibus p=0.50 (mvp_001), layer effect p=0.46 (diag_001). Control violation rate: 3-10%. N=760 total episodes.
123	
124	### Summary
125	
126	两轮 MVP 实验（mvp_001 + diag_001，共 760 episodes）完成核心假设验证。Type effect hypothesis 被两轮否定（层内 p=0.50，跨层 p=0.46），但 binary effect 极强（+31-42pp，p<1e-7），在 4 种歧义类型、2 个模型上高度一致。论文 pivot 到 binary anchor + type uniformity null finding + error analysis。
127	
128	### Recommendation
129	
130	GO — 原始 type-effect 假设被否定，但 binary effect 极强，足以支撑 EMNLP main conference 贡献。Type uniformity 本身是 informative null finding（对 mitigation 有 actionable implications）。Full study 扩展到 6 types × 4 models × 300 clauses，核心贡献是 binary effect quantification + error analysis。
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ef5c0fa-c19b-4471-ab50-15df3cd63c3c",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "b9196869-a730-48c3-8cba-d9123832724e",
  "sourceToolAssistantUUID": "2ef5c0fa-c19b-4471-ab50-15df3cd63c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T16:53:05.397Z_

I now have comprehensive knowledge of the paper, its development history, prior reviews, and the project context. Let me also check the earlier dream's review to see how the paper evolved.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9196869-a730-48c3-8cba-d9123832724e",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAjj93hVNatv26iXob7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3346bf84-4476-4675-902e-7592dce085b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015S5cx6WMcswnaXKysrma4p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11878,
      "cache_read_input_tokens": 66371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11878,
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

_source line 36 · 2026-05-20T16:53:07.517Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AGfnT5Nphndp6v6fcUuML8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3346bf84-4476-4675-902e-7592dce085b1",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAjj93hVNatv26iXob7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1f38aff-e88f-4114-88ed-6442a371188c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015S5cx6WMcswnaXKysrma4p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11878,
      "cache_read_input_tokens": 66371,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11878
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 66371,
          "cache_creation_input_tokens": 11878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11878,
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

_source line 37 · 2026-05-20T16:53:07.522Z_

<details><summary>↩ Tool result · `toolu_01AGfnT5Nphndp6v6fcUuML8`</summary>

```text
1	---
2	dream_id: dream_20260520T112859
3	tier: median
4	overall_score: 3.0 — Findings
5	timestamp: 2026-05-20T12:17:30.245436+00:00
6	---
7	
8	# Dream Review Report — "All Ambiguity Is Nocuous"
9	
10	**dream_id:** 20260520T112859  
11	**Venue:** EMNLP 2026 (ARR)  
12	**Review mode:** Full (2 Reviewers + Roundtable)
13	
14	---
15	
16	## Reviewer Assignments
17	- **R1:** Methods & Experiments
18	- **R2:** Novelty & Related Work
19	
20	---
21	
22	## R1 Review (Methods & Experiments)
23	
24	### Soundness of Experimental Design
25	
26	The matched-pair causal design is the paper's strongest methodological choice, cleanly isolating ambiguity as a causal variable. This is a genuine improvement over observational approaches (e.g., DRIP-R). τ²-bench is an appropriate evaluation environment, and the cross-judge agreement (κ=0.78) is adequate for the primary outcome.
27	
28	However, several issues:
29	
30	**(CRITICAL) Flat unambiguous baselines.** Table 2/10 reports identical unambiguous violation rates within each model across all 6 ambiguity types: GPT-5.4 = 11% for all 6 types, GPT-4.1 = 13% for all 6, Qwen3-32B = 14% for all 6, Qwen3-8B = 16% for all 6. With 50 clause pairs per type per model, sampling variation alone should produce per-type differences of several percentage points. This uniformity is statistically implausible and is never discussed. If this is integer rounding, the paper should report one decimal place. If the unambiguous clauses were evaluated in a pooled (non-type-specific) manner, the paper must disclose this, as it changes the interpretation of the matched-pair analysis. This is the single most concerning data integrity issue.
31	
32	**No power analysis for C2 or C3.** The "binary sufficiency" thesis (C2) and visibility effect (C3) both rest on absence-of-evidence arguments. Without a power analysis showing the study could detect plausible alternatives (e.g., V=0.25 for C2, or Δ=10pp for C3), readers cannot distinguish "true null" from "underpowered." This is a significant gap for a paper that foregrounds the null as a core contribution.
33	
34	**V < 0.20 threshold.** Pre-committing to a threshold is good practice, but 0.20 is lenient. Cohen's conventions place the small-medium boundary near V=0.10–0.15. Setting the bar at 0.20 means effects up to nearly "medium" are declared negligible. The paper should justify this specific choice, especially given V rose from 0.08 (3 types) to 0.15 (6 types).
35	
36	**Sample size per cell.** 50 clause pairs per type per model provides reasonable power for C1 but is marginal for the pairwise comparisons in C2/C3.
37	
38	### Statistical Analysis
39	
40	- McNemar's test is appropriate for matched-pair binary outcomes (C1). Bootstrap CIs are sound.
41	- The C2 omnibus test operates on ambiguous-condition rates alone. A stronger test would compare matched-pair *effect sizes* across types rather than raw ambiguous rates.
42	- C3 at p=0.09: appropriately labeled "suggestive." The consistent direction across 4 models and mechanistic support (44% vs 8% conflict detection) add qualitative strength. Framing as exploratory is honest.
43	- C4: reported honestly as non-significant with appropriate hedging.
44	
45	### Reliability & Validity
46	
47	- ICC=0.68 (moderate-to-good) is appropriate given the 4× margin between effect size and noise band.
48	- ±7.5pp noise band vs +31pp effect: convincing for C1.
49	- The visibility effect (Δ=-7.2pp) falls within the noise band, correctly acknowledged as "trend."
50	- Parse depth divergence (p=0.04) in realism validation is minor. The conservative-direction argument is reasonable but somewhat post-hoc.
51	
52	### Completeness
53	
54	- All 8 planned experiments (plan_001–008) are covered. Experimental coverage is thorough.
55	- Per-type effect sizes (amb−unamb) are not tabulated directly — readers must compute from Table 2.
56	- Classifier PoC (Table 7) feels bolted on: 82% accuracy on 60 test examples from the same synthetic distribution says little about real-world utility.
57	
58	### Reproducibility
59	
60	- Model names, sample sizes, evaluation framework, and statistical tests are specified.
61	- Clause generation described abstractly ("template instantiation, manual refinement, quality verification") — insufficient to replicate.
62	- **No code or data release mentioned.** This is a significant gap for EMNLP 2026.
63	
64	### R1 Weaknesses (severity-ordered)
65	1. Flat unambiguous baselines are statistically implausible and undiscussed — raises data integrity concerns
66	2. No power analysis for C2/C3, undermining the binary sufficiency claim
67	3. V<0.20 threshold is lenient and not well-justified
68	4. No code/data release
69	5. Classifier PoC is thin (60 synthetic test examples)
70	6. Only 2 domains; generalization not demonstrated
71	
72	### R1 Strengths
73	- Clean matched-pair causal design, methodologically superior to prior work
74	- Comprehensive model coverage (API + open-source at two scales)
75	- Test-retest reliability analysis is rare and valuable in this area
76	- Transparent reporting of non-significant results with appropriate hedging
77	- Massive, robust effect size for C1
78	- Realism validation against external corpus
79	
80	### R1 Scores
81	- Soundness: 3.0
82	- Excitement: 3.5
83	- Reproducibility: 2.5
84	- **Overall: 3.0**
85	
86	---
87	
88	## R2 Review (Novelty & Related Work)
89	
90	### Novelty Assessment
91	
92	**Research question:** Genuinely novel. No prior work provides a causal, type-granularity analysis connecting linguistic ambiguity classes to agent safety violation rates. DRIP-R measures decision quality degradation (not safety violations) and doesn't use matched-pair designs. This is a real gap being filled.
93	
94	**Binary sufficiency thesis:** Potentially interesting but fragile. V rose from 0.08 (3 types) to 0.15 (6 types). Extrapolating, further type expansion could break the null. This limits the contribution to a bounded, sample-specific observation rather than a robust finding.
95	
96	**Matched-pair causal design:** Standard in experimental psycholinguistics and clinical trials, but its application to agent policy evaluation is novel and a genuine methodological contribution.
97	
98	**Visibility hypothesis:** The connection between psycholinguistic ambiguity awareness and agent meta-cognition is creative and novel. The garden-path analogy (Frazier 1979) is apt, and the mechanistic evidence (44% vs 8% conflict detection) strengthens it.
99	
100	**Beyond DRIP-R:** The paper clearly advances beyond DRIP-R through the matched-pair design, safety violation metric, type-level causal analysis, and multi-model coverage.
101	
102	### Related Work Coverage
103	
104	**Missing references:**
105	- **Good-enough processing** (Ferreira, Bailey, & Ferraro, 2002; Ferreira & Patson, 2007): Directly relevant to the visibility hypothesis — explains how processors handle ambiguity without full reanalysis, which parallels the "silent resolution" observed in scopal traces. This is a significant omission.
106	- **Surprisal/expectation-based accounts** (Levy 2008; Hale 2001): Could inform why some ambiguity structures trigger reanalysis (visibility) and others don't.
107	- **Instruction-following literature** (Zhou et al., IFEval; related RLHF/alignment work): Agents following policy specifications is fundamentally an instruction-following task — no engagement with this large body of work.
108	- **Prompt engineering / system prompt design**: Policy specifications are system prompts in practice — this practical context is ignored.
109	
110	**DRIP-R positioning:** Fair and accurate. The distinction (decision quality vs safety violations, observational vs causal) is real.
111	
112	**Taxonomy grounding:** The 6-type taxonomy is well-motivated with cross-walks to Li et al. (2024) and Massey et al. (2014). Authorization scope as an agent-specific addition is reasonable. However, the taxonomy conflates strict syntactic ambiguity (scopal, coreferential) with pragmatic underspecification (incompleteness, authorization scope) without fully addressing this linguistic distinction.
113	
114	### Contribution Significance
115	
116	- **+31pp effect:** The magnitude is striking, but the *direction* is unsurprising — it would be more notable if ambiguity didn't increase violations. The contribution lies in the causal quantification and its robustness, not the direction. The effect size is useful for cost-benefit analyses of policy quality investments.
117	- **"All ambiguity is nocuous" (title):** Overstated. The paper demonstrates that 6 types in 2 domains are nocuous. The universal quantifier "all" is not supported by the evidence. Even "these 6 types are all nocuous" would be more defensible.
118	- **Binary sufficiency:** Practical value IF robust — tells practitioners they can use a simple binary classifier rather than type taxonomies. But the fragility of the null limits confidence in this recommendation.
119	- **Practical impact:** Moderate. The causal quantification is useful. The binary-sufficiency thesis, if confirmed, simplifies pipelines. But the practical artifact (82% classifier on synthetic data) is too thin to demonstrate applicability.
120	
121	### Framing & Narrative
122	
123	- **RE connection:** Natural and well-executed. The nocuous/innocuous distinction maps cleanly onto the research question. The argument that agents lack shared context is compelling.
124	- **Psycholinguistic connection:** Creative but speculative at p=0.09. The garden-path analogy is intuitive, and the mechanistic evidence strengthens it. But the paper should be more careful about the analogy's limits — LLM processing ≠ human sentence processing.
125	- **Title:** Catchy but overclaiming. "All" requires either logical necessity or exhaustive coverage; the paper provides neither.
126	
127	### Writing Quality
128	
129	Clear, well-organized, appropriately technical. Claims are generally well-calibrated to evidence with good hedging on C3/C4. The abstract efficiently summarizes all findings. The Limitations section is honest.
130	
131	References use "and 1 others" format for several entries — non-standard and suggests incomplete bibliography management. This would likely be flagged in ARR format checks.
132	
133	### R2 Weaknesses (severity-ordered)
134	1. Title overclaims — "All Ambiguity Is Nocuous" is unsupported by 6 types in 2 domains
135	2. Binary sufficiency is fragile — V trending from 0.08→0.15 suggests the null may break with more types
136	3. Missing good-enough processing references weakens the visibility hypothesis's theoretical grounding
137	4. No engagement with instruction-following or prompt engineering literature
138	5. Taxonomy conflates syntactic ambiguity with pragmatic underspecification without discussion
139	6. "And 1 others" reference format is non-standard
140	7. Classifier PoC adds little real-world value
141	
142	### R2 Strengths
143	- Genuinely novel research question filling a real gap (RE × NLP × agent safety)
144	- Clean causal identification through matched-pair design
145	- The nocuous/innocuous framing from RE is a compelling, well-chosen lens
146	- Visibility hypothesis is creative with mechanistic support
147	- Transparent about limitations and non-significant results
148	- Comprehensive experimental coverage
149	- Clear, well-organized writing
150	
151	### R2 Scores
152	- Soundness: 3.5
153	- Excitement: 3.5
154	- Reproducibility: 2.5
155	- **Overall: 3.0**
156	
157	---
158	
159	## Roundtable Synthesis
160	
161	### Cross-Reviewer Exchange
162	
163	**R1→R2 key flags:**
164	- Flat unambiguous baselines are the biggest methodological red flag — data integrity concern
165	- Missing power analysis undermines C2's status as contribution
166	- V<0.20 threshold selection is lenient
167	
168	**R2→R1 key flags:**
169	- Title overclaims universal nocuity from limited evidence
170	- Binary sufficiency contribution is fragile given V trend
171	- Psycholinguistic grounding needs deeper engagement
172	
173	### Points of Agreement
174	1. **C1 is strong and well-supported.** +31pp, massive effect, all 6 types significant, robust across 4 models. This is the paper's unambiguous contribution.
175	2. **Matched-pair design is a genuine methodological contribution** to the agent safety evaluation literature.
176	3. **C2 (binary sufficiency) is the most fragile contribution.** Both reviewers flag it — underpowered, lenient threshold, V trending upward. It should be presented more cautiously.
177	4. **Reproducibility is weak.** No code/data release, sparse clause generation details.
178	5. **Classifier PoC is thin** and could be cut without loss.
179	6. **The paper is refreshingly honest** about its non-significant results and limitations.
180	
181	### Points of Divergence
182	- R1 weights the flat-baseline anomaly more heavily (potential data integrity issue); R2 treats it as concerning but possibly a rounding artifact — **resolved toward R1's position**: the paper must address this.
183	- R2 weights overclaiming in the title more heavily; R1 focuses on statistical issues — both are valid and independent concerns.
184	
185	### Consensus Assessment
186	
187	The paper addresses a genuinely novel and important research question with a well-designed causal experiment. The primary finding (C1: +31pp) is robust and valuable. However, several issues prevent main-conference acceptance:
188	
189	1. **Data anomaly:** The flat unambiguous baselines are unexplained and undermine confidence in the reported numbers.
190	2. **Overclaiming:** The title and framing claim universality that the evidence (6 types, 2 domains) does not support.
191	3. **Fragile secondary contribution:** Binary sufficiency (C2) needs power analysis and may not survive type expansion.
192	4. **Reproducibility gaps:** No code/data, sparse methodological details.
193	5. **Missing literature:** Good-enough processing, instruction-following — needed for the theoretical narrative.
194	
195	These are addressable in a revision. The core experimental design and primary result are strong enough for Findings.
196	
197	### Consensus Scores
198	| Dimension | R1 | R2 | Consensus |
199	|---|---|---|---|
200	| Soundness | 3.0 | 3.5 | **3.0** |
201	| Excitement | 3.5 | 3.5 | **3.5** |
202	| Reproducibility | 2.5 | 2.5 | **2.5** |
203	| **Overall** | **3.0** | **3.0** | **3.0** |
204	
205	### Overall Assessment: **3.0 — Findings**
206	
207	The paper is at the Findings level. C1 is a solid, well-executed result. The matched-pair design is a methodological contribution. But the flat-baseline anomaly, overclaiming title, fragile C2, and reproducibility gaps keep it below the main-conference bar. A revision addressing the data reporting, adding power analysis, tempering the title, deepening the psycholinguistic grounding, and releasing code/data could push this to 3.5.
208	
209	### Actionable Recommendations for Authors
210	1. **Address flat unambiguous baselines.** Report at least one decimal place. If this is an artifact of how unambiguous episodes were evaluated (e.g., pooled across types), disclose and discuss implications.
211	2. **Add power analysis for C2 and C3.** Report the minimum detectable effect size given N=50/type.
212	3. **Temper the title.** "All" is not supported. Consider "Policy Ambiguity Is Nocuous" or "All Tested Ambiguity Types Are Nocuous."
213	4. **Justify V<0.20.** Explain why this threshold rather than V<0.10 or V<0.15.
214	5. **Engage with good-enough processing literature** (Ferreira et al., 2002) to strengthen the visibility hypothesis.
215	6. **Release code and data.** At minimum, the clause pairs and evaluation scripts.
216	7. **Fix "and 1 others" references** to standard "et al." format.
217	8. **Consider cutting the classifier PoC** or expanding it significantly — in its current form it adds little.
218	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1f38aff-e88f-4114-88ed-6442a371188c",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "4c2f317c-c2ba-4c9e-ac27-25cb91d817e6",
  "sourceToolAssistantUUID": "b1f38aff-e88f-4114-88ed-6442a371188c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T16:53:22.355Z_

I now have thorough knowledge of the paper, its evolution, the project's experimental results, and prior reviews. Let me write my R2 review focusing on Novelty, Contributions, and Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c2f317c-c2ba-4c9e-ac27-25cb91d817e6",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAkM3HrYoEbg2NEQWny",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9202723a-80f5-4bad-ab09-2c7ae53cf325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdiurrptY6upeTffq3y9DY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4586,
      "cache_read_input_tokens": 78249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4586,
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

_source line 39 · 2026-05-20T16:53:26.344Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Pf2z4ncKgLop71iUuSfoAW`</summary>

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
  "parentUuid": "9202723a-80f5-4bad-ab09-2c7ae53cf325",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAkM3HrYoEbg2NEQWny",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1cfdf3b-cc08-4a79-a2b2-09a36ab4e941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdiurrptY6upeTffq3y9DY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4586,
      "cache_read_input_tokens": 78249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4586,
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

_source line 40 · 2026-05-20T16:53:26.348Z_

<details><summary>↩ Tool result · `toolu_01Pf2z4ncKgLop71iUuSfoAW`</summary>

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
  "parentUuid": "e1cfdf3b-cc08-4a79-a2b2-09a36ab4e941",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "fdc05290-9396-49a8-b7bf-e74a8358ce3c",
  "sourceToolAssistantUUID": "e1cfdf3b-cc08-4a79-a2b2-09a36ab4e941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T16:53:29.565Z_



Now I have all the information needed to write a thorough R2 review. Let me compose it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc05290-9396-49a8-b7bf-e74a8358ce3c",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAmkNXKecsyxPHcFpnN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de181af2-9a31-491d-abdd-e9158a09c20a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbKknZGmAhmVdxuUDBBdEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 82835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 860,
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

_source line 42 · 2026-05-20T16:55:30.252Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01CvdmhHEFtvsNLUq3qJjDmp`</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "tier": "best",
  "dream_id": "dream_20260520T152228",
  "overall_score": "3/6 — Borderline Findings",
  "report": "# R2 Review: Novelty, Contributions, and Related Work\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Specification-Layer Ambiguity Poses Greater Safety Risks for LLM Agents\"\n**Reviewer**: R2 (Novelty + Contributions + Related Work)\n**Score**: 3/6 (Borderline Findings)\n**Confidence**: 4/5\n\n---\n\n## Summary\n\nThis paper presents a matched-pair causal study of how six types of policy ambiguity affect safety violation rates in LLM agents, testing five models across 3,000 agentic episodes on τ²-bench. The core claim — \"Differential Nocuity\" — is that specification-layer ambiguities (+43.6pp) are nearly twice as dangerous as linguistic-layer ones (+26.2pp). The paper includes a perturbation control, error analysis with six failure modes, inter-model nocuity measurement via Fleiss κ, and a DeBERTa classifier proof-of-concept. The experimental design is rigorous, but the novelty is primarily empirical rather than conceptual, the layer dichotomy is undermined by its own data, the related work is thin and missing critical connections, and the contribution framing is overclaimed relative to evidence.\n\n---\n\n## Strengths\n\n- **The matched-pair design combined with a perturbation control is genuinely novel in the agent safety literature.** Table 12's feature comparison correctly shows no prior work achieves this combination. The perturbation arm (Δ=3.3pp vs. ambiguity Δ=36.5pp, ratio=0.09) provides convincing causal evidence that the observed effects are ambiguity-specific, not general prompt brittleness. This is the paper's single strongest methodological contribution.\n\n- **The error analysis (Section 6) is the paper's most valuable section.** The 300-trace qualitative analysis revealing mechanistically distinct failure modes per type — unauthorized assumption for auth_scope (72%), scope escalation for incompleteness (65%), misparse scope for scopal (58%), surface adoption for lexical (62%) — provides genuine explanatory depth. The 82% failure-mode-to-layer consistency is informative. The coreferential avoidance finding (44% vs. 8% for other types) is a genuinely novel behavioral observation.\n\n- **The Berry & Kamsties operationalization via Fleiss κ is well-executed.** Measuring inter-model agreement on ambiguous clauses (κ=0.33) vs. unambiguous ones (κ=0.82) provides a clean operationalization of nocuity as divergent interpretation. The Δκ=−0.49 and the 58% vs. 12% divergent clause rates strengthen the theoretical connection.\n\n- **The Disambiguation Channel Hypothesis has genuine explanatory power.** The gradient from scopal (Δ=34.8pp, low external resolution) to coreferential (Δ=16.2pp, 23% tool-based disambiguation) aligns with the hypothesis that external information channels partially mitigate linguistic-layer ambiguity but not specification-layer ambiguity.\n\n- **The binary effect (C1) is robust and well-quantified.** +35.8pp with CI [33.1, 38.5], OR=42.1, holding across all six types and five models. This is a useful quantification for the community even if the directional finding is unsurprising.\n\n---\n\n## Weaknesses\n\n### W1 (MAJOR): CP undermines the clean layer dichotomy, invalidating the headline claim.\n\nThe paper's title and abstract frame the core finding as \"specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\" However, the paper's own data shows CP (specification-layer, Δ=31.0pp) falls *below* scopal (linguistic-layer, Δ=34.8pp). The actual type ranking is:\n\nauth_scope (52.0) > incompleteness (47.8) > **scopal (34.8) > CP (31.0)** > lexical (28.6) > coreferential (16.2)\n\nThe spec/ling boundary is crossed. The \"nearly twice as dangerous\" framing (43.6pp vs. 26.2pp) is an artifact of averaging: it is driven by the extremes (auth_scope+incompleteness vs. coreferential), not a consistent layer effect. The paper acknowledges this in Section 6 via the \"visibility\" argument (CP has detectable conflicts, making it behaviorally distinct), but this explanation actually *undermines* the two-layer taxonomy — if CP behaves more like a linguistic-layer type because its conflicts are \"visible,\" then the spec/ling distinction is not the right organizing principle.\n\nA more honest framing would be: \"authorization scope and incompleteness ambiguities are substantially more dangerous than other types, and coreferential ambiguity is least dangerous, with the middle four types (CP, scopal, lexical, and their neighbors) forming a less differentiated cluster.\" This is a weaker but more accurate claim.\n\n### W2 (MAJOR): \"Differential Nocuity\" is overclaimed as a theoretical framework.\n\nThe observation that different ambiguity types cause different violation rates is an expected finding from any taxonomy study with sufficient power. The real value lies in (a) the causal quantification, (b) the error analysis showing mechanistically distinct failure modes, and (c) the disambiguation channel observation. Packaging these as a named \"framework\" — \"Differential Nocuity\" — adds branding without proportional conceptual substance. The paper would be stronger presenting these as empirical findings with mechanistic grounding rather than elevating them to a theoretical framework.\n\nThe term also creates confusion: Berry & Kamsties' original \"nocuity\" refers to whether an ambiguity produces divergent interpretations (nocuous) vs. convergent ones (innocuous). \"Differential Nocuity\" suggests different *degrees* of interpretive divergence, which is a different concept from different *rates of safety violation*. The paper conflates these two meanings.\n\n### W3 (MAJOR): Related work has significant gaps for a paper making theoretical claims.\n\nThe paper cites only 16 references. For a paper that positions itself at the intersection of computational linguistics, requirements engineering, and agent safety — and that proposes a named theoretical framework — this is thin. Specific gaps:\n\n**Pragmatics literature (entirely missing):** The Disambiguation Channel Hypothesis is fundamentally about pragmatic inference — agents lack shared context and cooperative norms that humans use for disambiguation. Yet there is no engagement with Grice (cooperative principle, implicature), Clark (common ground theory), or Sperber & Wilson (relevance theory). The specification/linguistic layer distinction maps naturally onto pragmatics/semantics, but this connection is never made explicit.\n\n**RLHF/alignment effects (undiscussed):** The paper notes Claude shows the highest avoidance rate and GPT-5.4 shows the most aggressive execution, but attributes these only to vague \"model differences.\" The alignment training literature (Constitutional AI, RLHF) directly explains why different models handle ambiguity differently. This is not just a missing citation — it's a missed analytical opportunity.\n\n**Legal NLP / contract ambiguity (missing):** Specification-layer ambiguity in policies is directly analogous to contract ambiguity in legal documents. The growing legal NLP literature on contract analysis, ambiguity detection in legal text, and formal specification of legal provisions is highly relevant and entirely absent.\n\n**Formal policy verification (missing):** ShieldAgent (ICML 2025), MANTRA (2026), AgentSpec (ICSE 2026), and Policy Compiler (2026) all address formal approaches to policy specification. The paper's practical recommendation (type-aware triage) would be substantially strengthened by positioning it as the diagnostic front-end to these formalization pipelines.\n\n**Broader agent safety benchmarks (sparse):** ATBench, OpenAgentSafety, SafetyDrift, PolicyGuard, CRAFT are all relevant but uncited. The comparison table (Table 12) includes only four baselines.\n\n**Requirements engineering beyond Berry & Kamsties:** Chantree et al. (2006) on nocuous ambiguity detection, Ezzini et al. (2022) TAPHSIR system, Willis et al. (2008) on automated ambiguity detection — the RE literature is richer than the paper acknowledges.\n\n### W4 (MAJOR): Five contributions in 8 pages stretches the paper thin.\n\nThe paper claims five findings: (C1) binary effect, (C2) type hierarchy, (C3) layer effect, (C4) architecture-universality, and (C5) inter-model nocuity. This is overambitious:\n\n- C1 is a prerequisite for the other claims, not an independent contribution. The direction (ambiguity causes violations) is unsurprising; the magnitude quantification is useful but not standalone-contribution-level.\n- C2 and C3 are deeply related (C3 is an aggregation of C2). Presenting them as separate contributions inflates the contribution count.\n- C4 (Model×Type interaction p=0.34) is essentially a non-finding presented as a contribution. A non-significant interaction in a 5-model × 6-type design with the observed sample sizes has limited inferential value — it could reflect true universality or insufficient power.\n- C5 (inter-model nocuity, Fleiss κ) is interesting but gets only one page of development.\n\nThe paper would be stronger consolidating to three claims: (1) causal binary effect with perturbation control, (2) type hierarchy with layer-level tendency and mechanistic grounding via error analysis, and (3) inter-model nocuity operationalizing Berry & Kamsties.\n\n### W5 (MAJOR): The psycholinguistic grounding is asserted rather than argued.\n\nSection 2 invokes good-enough processing (Ferreira et al., 2002) and garden-path effects (Frazier & Rayner, 1982) as explanatory frameworks for why agents adopt surface readings of ambiguous clauses. But the paper never argues *why* these human processing models should apply to autoregressive language models. LLM generation is fundamentally different from human incremental comprehension — there is no eye-movement regression, no reanalysis cost, no working memory bottleneck. The behavioral analogy may hold, but the mechanistic basis is unexamined. Four sentences of assertion (Section 2, paragraph 4) is insufficient grounding for what becomes a recurring explanatory motif.\n\n### W6 (MINOR): The DeBERTa classifier PoC (Section 7) is tangential.\n\nF1=0.89 on 60 test examples from the same synthetic distribution as training is expected for a fine-tuned model. The zero-shot GPT-4.1 baseline (F1=0.64) is the more interesting data point — suggesting that LLMs are poor at detecting the very ambiguities that cause their failures. But this receives one sentence. The classifier consumes valuable page budget without advancing the core narrative. Move to appendix.\n\n### W7 (MINOR): The taxonomy cross-walk is mentioned but not shown.\n\nSection 3 claims a cross-walk to DRIP-R's five types and Massey et al.'s six-type scheme, but no table or explicit mapping is provided. For a paper whose taxonomy is the structural backbone, this is an oversight. A mapping table would also help readers assess whether the six selected types adequately cover the policy ambiguity space.\n\n### W8 (MINOR): Conflation of ambiguity and vagueness is acknowledged but underdefended.\n\nThe paper follows Wasow et al. (2015) in operationally including vagueness under ambiguity \"when the effect on agent behavior is indistinguishable.\" But authorization scope (e.g., \"authorized personnel may access customer records\") is paradigmatic vagueness — a continuous spectrum of interpretation, not discrete alternative readings. This is a contested choice in linguistics. The one-sentence defense (Section 3, citing Wasow et al.) is insufficient. Some reviewers will object that the entire specification layer is studying vagueness/underspecification, not ambiguity, which would undermine the unified taxonomy.\n\n### W9 (MINOR): Architecture-universality claim is strong given non-significant interaction.\n\nThe non-significant Model×Type interaction (p=0.34) is presented as evidence for \"architecture-universal hierarchy.\" But non-significance does not equal equivalence. With 5 models and 6 types, the interaction test may lack power. The paper does not report an equivalence test (TOST) for the interaction, only for pairwise type comparisons. \"Consistent across tested models\" would be more calibrated than \"architecture-universal.\"\n\n---\n\n## Questions for Authors\n\n1. **CP anomaly**: How do you reconcile the headline \"specification nearly twice as dangerous as linguistic\" with CP (spec, 31.0pp) < scopal (ling, 34.8pp)? Is the two-layer taxonomy the right organizing principle, or would a three-group structure (high: auth_scope+incompleteness; medium: scopal+CP+lexical; low: coreferential) be more faithful to the data?\n\n2. **Disambiguation Channel — causal test**: The Disambiguation Channel Hypothesis is correlational. Have you considered manipulating channel availability (e.g., withholding tool access, or providing explicit \"if ambiguous, ask for clarification\" instructions) to test it causally?\n\n3. **Convergent-but-wrong**: What proportion of ambiguous clauses produce unanimous wrong interpretations across all five models (i.e., all models converge on the same incorrect reading)? This would distinguish true nocuity (divergent interpretations) from systematic bias (convergent-but-wrong), which has different practical implications.\n\n4. **Psycholinguistic mechanism**: Beyond behavioral analogy, what evidence suggests autoregressive LLMs exhibit processing patterns analogous to good-enough comprehension? Could the surface adoption finding be explained more parsimoniously by training data distribution (high-frequency readings dominate)?\n\n5. **Ambiguity vs. vagueness**: For authorization scope, can you provide examples where the policy admits discrete alternative readings (true ambiguity) rather than a continuous spectrum of interpretation (vagueness)? If not, should this type be relabeled?\n\n6. **RLHF interaction**: Claude shows the highest avoidance rate across all types (Section 6). Does this reflect Constitutional AI training specifically targeting cautious behavior under uncertainty? If so, this suggests alignment methods are a direct mitigation for ambiguity-driven violations — a finding worth developing.\n\n---\n\n## Minor Issues\n\n- Table 5 caption says \"Type ranking auth_scope > incompleteness > scopal > lexical > CP > coreferential is preserved across all five models\" — but this ranking has CP below scopal, crossing the layer boundary. The caption should acknowledge this.\n- The paper claims to release \"all clause pairs, evaluation code, and annotated traces\" (abstract) but no URL, repository, or supplementary materials are provided.\n- \"Conflicting provisions\" is abbreviated as \"CP\" without definition at first use in the abstract.\n- The perturbation control (Section 4.3) uses only 30 pairs and 3 API models (180 episodes). Extending to open-source models (especially Qwen3-8B, which shows different behavioral patterns) would strengthen the causal claim.\n- The logistic regression (Table 6) reports \"Model (5 levels)\" as a single coefficient — this should be a set of 4 indicator coefficients or an omnibus test, not a single z-value. The reporting format is unclear.\n- Section 5.4 reports Model×Type interaction p=0.34, but Section 5.5 (inter-model nocuity) reports κ=0.33 on ambiguous clauses. These are related but distinct analyses — the paper should clarify how interaction non-significance relates to low inter-model agreement.\n- The paper uses \"3-tier severity\" in Table 12 but the main text only reports binary (violation/no-violation) outcomes. Where is the severity analysis?\n\n---\n\n## Overall Assessment\n\n**Score: 3/6 (Borderline Findings)**\n\n**EMNLP equivalent: 2.5–3.0 (between Borderline Findings and Findings)**\n\n**Justification:**\n\nThe paper addresses a timely and genuinely novel research question — no prior work causally links ambiguity type to safety violation severity in LLM agents. The matched-pair design with perturbation control is the strongest causal framework in this literature, and the error analysis provides genuine mechanistic insight into why different ambiguity types produce different failure modes.\n\nHowever, I have serious concerns about the paper's current form:\n\n(1) The headline claim — \"specification nearly twice as dangerous as linguistic\" — is undermined by the paper's own data (CP < scopal), making the two-layer taxonomy a leaky abstraction rather than a clean organizing principle. The paper needs to either qualify the layer claim substantially or restructure around the type ranking directly.\n\n(2) \"Differential Nocuity\" is overclaimed as a theoretical framework. The novelty is empirical (quantification + mechanism), not conceptual (the idea that different ambiguity types have different effects is not surprising).\n\n(3) The related work is too thin (16 references) for a paper making theoretical claims at the CL/RE/safety intersection. Missing pragmatics, alignment/RLHF, legal NLP, and formal verification connections weaken both the theoretical grounding and the practical positioning.\n\n(4) Five contributions in 8 pages is overambitious. Several (C1 as standalone, C4 as non-finding-as-contribution) are inflated.\n\n(5) The psycholinguistic grounding is asserted without mechanistic argument.\n\nThe paper has strong experimental bones. With restructured framing (lead with type ranking + error analysis, present layer as secondary observation with CP caveat), expanded related work (25+ references with pragmatics and alignment connections), and toned-down theoretical claims, this could reach Conference level. In its current form, the overclaiming and thin related work keep it at the Findings boundary.\n\n**Confidence: 4/5** — I have read the paper carefully and have domain expertise in both computational linguistics and agent safety evaluation. My main uncertainty is whether the five-model results are fully completed or partially projected; if projected, the universality claims would need further downgrading.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de181af2-9a31-491d-abdd-e9158a09c20a",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAmkNXKecsyxPHcFpnN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "199c67cd-0ef0-482f-92a1-6f5250fef1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbKknZGmAhmVdxuUDBBdEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 82835,
      "output_tokens": 4456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4456,
          "cache_read_input_tokens": 82835,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 860,
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

_source line 43 · 2026-05-20T16:55:33.501Z_

<details><summary>↩ Tool result · `toolu_01CvdmhHEFtvsNLUq3qJjDmp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/review_report.md\", \"dream_id\": \"dream_20260520T152228\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "199c67cd-0ef0-482f-92a1-6f5250fef1e9",
  "isSidechain": true,
  "promptId": "fbdb2980-c22d-4e6c-9965-376729d5cb8a",
  "agentId": "a2f3b178915a739ac",
  "type": "user",
  "uuid": "d9dee0dd-842a-47fc-b27f-ab19f02ad461",
  "sourceToolAssistantUUID": "199c67cd-0ef0-482f-92a1-6f5250fef1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T16:55:53.709Z_

Review submitted. Here is the summary:

**R2 Review Score: 3/6 (Borderline Findings), Confidence 4/5**

**Key findings:**

**Strengths identified:**
- Matched-pair + perturbation control is genuinely novel in agent safety literature (ratio 0.09 convincingly rules out prompt brittleness)
- Error analysis (Section 6) is the paper's strongest contribution, with mechanistically distinct failure modes per type
- Berry & Kamsties operationalization via Fleiss kappa (0.33 ambig vs 0.82 unambig) is well-executed
- Disambiguation Channel Hypothesis has real explanatory power for the coreferential-to-scopal gradient

**Major weaknesses:**
- **W1**: CP (spec, 31.0pp) < scopal (ling, 34.8pp) — the layer boundary is crossed, undermining the headline "specification nearly twice as dangerous" claim
- **W2**: "Differential Nocuity" is overclaimed as a theoretical framework; the novelty is empirical, not conceptual
- **W3**: Only 16 references; missing pragmatics (Grice, Clark), RLHF/alignment, legal NLP, formal verification, and broader agent safety benchmarks
- **W4**: Five contributions in 8 pages is overambitious; C1 is a prerequisite not a standalone contribution, C4 is a non-finding presented as contribution
- **W5**: Psycholinguistic grounding (good-enough processing) is asserted without arguing why it applies to autoregressive LLMs

**Recommended path to acceptance:** Restructure around type ranking + error analysis as primary contributions, present layer effect as secondary observation with explicit CP caveat, expand references to 25+, consolidate to 3 core claims, tone down framework language.

Report saved to `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9dee0dd-842a-47fc-b27f-ab19f02ad461",
  "isSidechain": true,
  "agentId": "a2f3b178915a739ac",
  "requestId": "req_011CbEAw6ym2YT9Ep1eAKhd7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9cd1019-6e32-41d4-a499-3d1c6d80ea1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "bd96f57a-80ec-4566-95cb-ccf252e77f7a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116PF2qvib6sgPshFK8khc3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4589,
      "cache_read_input_tokens": 83695,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4589
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 83695,
          "cache_creation_input_tokens": 4589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4589,
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
