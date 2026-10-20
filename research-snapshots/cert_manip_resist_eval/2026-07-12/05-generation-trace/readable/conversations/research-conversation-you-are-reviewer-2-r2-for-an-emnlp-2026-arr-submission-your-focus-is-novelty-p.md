# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **Novelty, Positioning, and Related Work**. ## V

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae36eb1bd3a5725c7.jsonl`
- **Structured JSON:** [`a052c826ed01ed6be709.json`](../../sessions/a0/a052c826ed01ed6be709.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-22T18:48:35.725Z_

You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **Novelty, Positioning, and Related Work**.

## Venue calibration
EMNLP 2026 via ARR. Overall Assessment scale (half-point):
- 5 = Award consideration (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit
Acceptance rate ~21%. Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper summary
**Title**: "Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation: Weakest-Link Dominance, Aggregation Defenses, and the Limits of Diversity"

**Central thesis**: The paper challenges the assumption that judge diversity protects multi-judge LLM evaluation panels against adversarial manipulation. Through a large-scale empirical study (15 models, 455 panels, 18 conditions, 2 benchmarks), it finds that:
1. Panel vulnerability is dominated by the weakest individual judge (η_max), not panel diversity (K_eff)
2. K_eff's apparent effect is largely a statistical artifact of capability heterogeneity (tier-mixing confound)
3. Aggregation rule choice matters more than panel composition
4. Adaptive adversaries target individual weakness, not structural diversity

**Three principal conclusions** (from Conclusion section):
1. Weakest-link dominance: η_max sig 9-14/18, K_eff fragile (2-5/12), ΔR²=0.04, vanishes under capability matching (1/6)
2. Aggregation > composition: Bayesian reduces ASR by 24% vs majority vote
3. Adaptive targeting tracks weakness not diversity: Gini-η_max r=0.67 vs Gini-K_eff r=0.21 (NS)

**Practical recommendation**: "Select the most individually robust judges available and employ reliability-weighted aggregation. Diversity is neither a reliable defense nor a consistent liability."

**Paper structure** (11 pages, appears to be within EMNLP 8-page limit for main text + unlimited references, with appendix tables):
- §1 Introduction (pages 1-2)
- §2 Related Work (page 2): 4 paragraphs — LLM-as-Judge, Adversarial Attacks on LLM Evaluators, Multi-Agent Robustness, Panel Diversity Metrics
- §3 Methodology (pages 2-4): Threat Model, Model Pool, Attack Types, Metrics, Regression framework
- §4 Experiments (pages 4-6): Weakest-Link, Attack Generalization, Targeting, Aggregation, Panel Selection, Panel Size, Open-Ended, Partial-Knowledge
- §5 Discussion (pages 6-8): K_eff exploratory analysis, BFT open question, Diversity-Capability Tradeoff
- §6 Conclusion (page 8)
- Limitations (page 9)
- Tables 13-19 (pages 10-11, appendix-style)

**Related Work section** (page 2, ~4 short paragraphs):
1. **LLM-as-Judge**: Mentions single-judge scoring, multi-judge panels, individual biases (position, verbosity, self-enhancement). No specific citations visible.
2. **Adversarial Attacks on LLM Evaluators**: Prompt injection, sycophancy exploitation, score manipulation. Notes most work focuses on single-judge.
3. **Multi-Agent Robustness**: BFT connection mentioned but notes specific LLM panel + adaptive adversary setting is "understudied."
4. **Panel Diversity Metrics**: K_eff from MI matrix eigenvalues, describes as "beyond simple model count or family-level heuristics."

**Key methodological contributions claimed**:
- K_eff metric (from MI matrix) as continuous diversity measure
- 15-model/455-panel exhaustive evaluation benchmark
- Copula failure finding (residualized K_eff fragile)
- Aggregation rule comparison under adversarial setting

**Model pool**: Qwen (7B/14B/72B), Llama (8B/70B), Mistral (7B/12B), Microsoft Phi-3 (mini/medium), Gemma-2-9B, GPT-4o-mini, GPT-4o, GPT-4.1, GPT-4.1-mini, Claude-3.5-Haiku

## Your review task
Write a detailed review focusing on:
1. **Novelty**: How novel are the findings? Is "weakest-link dominance" surprising or expected? Is the K_eff confound finding a genuine contribution?
2. **Related work coverage**: Are key related works missing? Is the positioning accurate? Does the paper adequately distinguish itself?
3. **Framing and narrative**: Is the reframing from "diversity trap" to "structural vulnerability anatomy" well-executed? Does the paper oversell or undersell?
4. **Contribution significance**: Would the NLP community benefit from these findings? Are the practical recommendations actionable and non-trivial?
5. **Presentation quality**: Writing clarity, figure/table organization, appropriate length.

Key questions to consider:
- Is "the weakest judge determines panel security" genuinely novel, or is it an obvious consequence that diversity pools tend to include weak members?
- The related work is very brief (4 short paragraphs). Is this sufficient for positioning a paper with 19 tables?
- The K_eff metric itself is borrowed (from information theory / MI matrix). What's the paper's methodological novelty vs empirical novelty?
- How does this compare to classical ensemble learning literature on diversity-accuracy tradeoffs?
- The paper's main finding is essentially negative (diversity doesn't help). Is the constructive contribution (aggregation, practical guidelines) sufficient?

Provide:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, specific and actionable)
- Questions for authors
- Preliminary scores: Soundness (1-5), Excitement (1-5), Reproducibility (1-5), Overall (1-5, half-point)
- Confidence (1-5)

Be rigorous. Calibrate to EMNLP acceptance rate (~21%). A score of 4 means you'd advocate for main conference acceptance.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "a8e4f853-044a-47f2-8a89-30ce237acbca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T18:48:35.730Z_

```json
{
  "parentUuid": "a8e4f853-044a-47f2-8a89-30ce237acbca",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
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
  "uuid": "1cb26175-fd3b-471b-9508-a78a6f1008ee",
  "timestamp": "2026-05-22T18:48:35.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T18:48:39.833Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cb26175-fd3b-471b-9508-a78a6f1008ee",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7AtGU6p9Zkp6jqso7Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31af9c5c-7014-4fdd-bfd9-130b21718f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8cZDLoYZRt6Lz3R8KMUXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7957,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7957,
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

_source line 4 · 2026-05-22T18:48:41.808Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NYje3dyeoTNbRb3fDEAyZx`</summary>

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
  "parentUuid": "31af9c5c-7014-4fdd-bfd9-130b21718f8b",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7AtGU6p9Zkp6jqso7Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d38adc7d-818c-4880-9293-179d2f0cdfdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8cZDLoYZRt6Lz3R8KMUXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7957,
      "cache_read_input_tokens": 8252,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7957,
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

_source line 5 · 2026-05-22T18:48:41.811Z_

<details><summary>↩ Tool result · `toolu_01NYje3dyeoTNbRb3fDEAyZx`</summary>

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
  "parentUuid": "d38adc7d-818c-4880-9293-179d2f0cdfdc",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "ca7e6fa2-8cf6-4773-9c04-426eaaea8060",
  "sourceToolAssistantUUID": "d38adc7d-818c-4880-9293-179d2f0cdfdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T18:48:45.192Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca7e6fa2-8cf6-4773-9c04-426eaaea8060",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7BLtNCXxypKkTx9abN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ff0770a-c8dc-49c4-9538-d7725d684627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115CveiMDanWXSAKLmMk7ry",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-22T18:48:46.739Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0119cJ589FeR1Pxd1MxiK1D8`</summary>

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
  "parentUuid": "4ff0770a-c8dc-49c4-9538-d7725d684627",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7BLtNCXxypKkTx9abN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "005b2e9b-09cc-40ad-94a5-85f72ea5f1a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115CveiMDanWXSAKLmMk7ry",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 8 · 2026-05-22T18:48:46.755Z_

<details><summary>↩ Tool result · `toolu_0119cJ589FeR1Pxd1MxiK1D8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan001_step1_batched_v2（准备中）\\n- plan001_step1_batched（准备中）\\n- plan001_step1_v3（准备中）\\n- plan001_step1_throttled_v5（准备中）\\n- plan001_step1_throttled_v4（准备中）\\n- plan001_step1_throttled_v3（准备中）\\n- plan001_step1_throttled_v2（准备中）\\n- plan001_step1_throttled（准备中）\\n- plan001_step1_v2（准备中）\\n- plan001_step1_parallel_final（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **plan001_step1_full_v4** (success): Expanding from 6 to 15 models (9 API + 6 local) across 6 families and 3 capability tiers breaks the structural K_eff-η_max collinearity (r=-0.8 with 6 models). With 15 models, panels can have high K_eff (cross-family diversity) without necessarily including weak judges, enabling clean separation of diversity vs robustness effects.\\n- **taxonomy-broad-spectrum** (negative): K_eff is a significant negative predictor of panel ASR specifically for broad-spectrum attacks (verbosity bias, position bias, authority bias) that exploit shared judge biases, consistent across both MMLU and ARC datasets. This validates the attack taxonomy: targeted attacks → η_max dominates; broad-spectrum attacks → K_eff provides additional protection. ← 基于 mvp-step2v3-retry3\\n- **mvp-step2v3-retry3** (negative): Controlling for individual model robustness (η_max), higher K_eff panels have significantly lower ASR. Multi-factor regression log(ASR) ~ log(K_eff) + log(η_max) should show K_eff coefficient significantly negative. ← 基于 mvp-step2v3-retry2\\n\\n## 趋势\\n成功 1 / 负向 3 / 失败 3 / 共 7\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nseetacloud-rtx6000: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp-step2v3-regression: 训练失败 — unknown\\n- mvp-step2v3-retry: 训练失败 — unknown\\n- mvp-step2v3-retry2: 训练失败 — unknown\\n\", \"total_chars\": 1736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "005b2e9b-09cc-40ad-94a5-85f72ea5f1a6",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "abf441ac-9e3e-4578-a862-58b28e57a2d0",
  "sourceToolAssistantUUID": "005b2e9b-09cc-40ad-94a5-85f72ea5f1a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T18:48:47.203Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013EgU6xKUjfp45pi5DD8Euh`</summary>

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
  "parentUuid": "abf441ac-9e3e-4578-a862-58b28e57a2d0",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7BLtNCXxypKkTx9abN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06049c1e-5cea-46f1-9ecd-dcbfab71873c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115CveiMDanWXSAKLmMk7ry",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 10 · 2026-05-22T18:48:47.215Z_

<details><summary>↩ Tool result · `toolu_013EgU6xKUjfp45pi5DD8Euh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/literature_map.yaml\", \"content\": \"papers:\\n  robertson2025tvdmi:\\n    title: \\\"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes\\\"\\n    authors: [\\\"Robertson\\\", \\\"Koyejo\\\"]\\n    year: 2025\\n    venue: \\\"arXiv (under TMLR review)\\\"\\n    url: \\\"https://arxiv.org/abs/2508.05469\\\"\\n    category: \\\"evaluation_framework\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Foundational TVD-MI theory for LLM evaluation. Theorem 3.3 proves bounded f-divergences (TVD) maintain polynomial certification under mode-collapse attacks while unbounded (KL) fail. We extend from pairwise to N-agent multi-judge settings.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  yang2026diversity_scaling:\\n    title: \\\"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\\\"\\n    authors: [\\\"Yang et al.\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026 Workshop AIMS\\\"\\n    url: \\\"https://arxiv.org/abs/2602.03794\\\"\\n    category: \\\"multi_agent_scaling\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Information-theoretic diversity-scaling framework: K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3). We provide the adversarial dual — while their K* governs performance improvement rate, the same correlation structure governs manipulation cost increase rate. Core duality insight.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  turkmen2026copula:\\n    title: \\\"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\\\"\\n    authors: [\\\"Turkmen et al.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08003\\\"\\n    category: \\\"ensemble_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Gaussian-copula correlated error model (Z_j = √ρ·U + √(1-ρ)·ξ_j), error floor Φ(Φ⁻¹(1-p)/√ρ) (Theorem 4.4), three-term MI decomposition (Theorem 4.3). Copula model is the mathematical foundation for our K_eff = 1+(K-1)·exp(-2·I_max) derivation. Within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  kaneko2025bits_leaked:\\n    title: \\\"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs\\\"\\n    authors: [\\\"Kaneko\\\", \\\"Baldwin\\\"]\\n    year: 2025\\n    venue: \\\"NeurIPS 2025 spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2510.17000\\\"\\n    category: \\\"adversarial_bounds\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Tight single-model attack cost bound N_min ≥ log₂(1/ε)/I_max via Fano inequality (Theorem 1), achieved by SPRT (Theorem 2). Validated across 7 LLMs. Provides single-channel foundation; we extend to multi-judge composition where adversary must simultaneously fool K correlated judges.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  chen2025peg:\\n    title: \\\"Incentivizing Truthful Language Models via Peer Elicitation Games\\\"\\n    authors: [\\\"Chen et al.\\\"]\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.13636\\\"\\n    category: \\\"peer_prediction\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"DMI-based multi-agent peer elicitation with dominant strategy truthfulness (Lemma 1), O(√T) regret (Theorem 2). Requires conditional independence (Assumption 4) but does not characterize degradation when violated. We prove ε = f(ρ) continuous degradation curve as co-primary contribution.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  qiu2026truthfulness:\\n    title: \\\"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction\\\"\\n    authors: [\\\"Qiu et al.\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2601.20299\\\"\\n    category: \\\"peer_prediction\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"BNE incentive-compatibility for LLM peer prediction with inverse scaling property. Targets output truthfulness not adversarial robustness of protocol. No polynomial cost bounds tied to judge count. We provide the robustness guarantee that complements their truthfulness guarantee.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  kim2025correlated_errors:\\n    title: \\\"Correlated Errors in Large Language Models\\\"\\n    authors: [\\\"Kim\\\", \\\"Garg\\\", \\\"Peng\\\", \\\"Garg\\\"]\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.07962\\\"\\n    category: \\\"error_correlation\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"60% pairwise agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076. Key empirical data for α regime analysis and K_eff estimation. 350+ LLMs. Motivates cross-family diversity for maximizing K_eff.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  sok2026llm_judge_security:\\n    title: \\\"Security in LLM-as-a-Judge: A Comprehensive SoK\\\"\\n    authors: [\\\"Various\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.29403\\\"\\n    category: \\\"adversarial_evaluation\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"Comprehensive vulnerability catalog: open-source 50-68% ASR, frontier 27-44%. 7-model diverse committees reduce ASR to 10-19% empirically but WITHOUT formal explanation. We provide the formal explanation via K_eff framework.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  feng2026noisy_valid:\\n    title: \\\"Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges\\\"\\n    authors: [\\\"Feng\\\", \\\"Shen\\\", \\\"Balashankar\\\", \\\"Gerner-Beuerle\\\", \\\"Rodrigues\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2601.20913\\\"\\n    category: \\\"certified_evaluation\\\"\\n    role: \\\"adjacent\\\"\\n    relevance: \\\"Statistical hypothesis testing for LLM evaluation with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty. Assumes honest but fallible judges. Complements our work: they certify statistical validity, we certify manipulation resistance.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  jung2026logarithmic_scores:\\n    title: \\\"Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation\\\"\\n    authors: [\\\"Jung\\\", \\\"Na\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.00477\\\"\\n    category: \\\"multi_agent_scaling\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"Score-coverage dissociation: scoring reliability scales logarithmically with panel size N while discovery follows power law N^0.69. Direct implications for our K-scaling claims — certified bounds may saturate faster than empirical ASR gains.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  chen2026behavioral_entanglement:\\n    title: \\\"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement\\\"\\n    authors: [\\\"Chen et al.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.07650\\\"\\n    category: \\\"error_correlation\\\"\\n    role: \\\"empirical-basis\\\"\\n    relevance: \\\"BEI and CIG metrics across 18 LLMs from 6 families. Cross-family entanglement 40-60% lower than intra-family. Provides independent validation of cross-family diversity benefit for K_eff estimation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  keppo2026collusion_fragility:\\n    title: \\\"On the Fragility of AI Agent Collusion\\\"\\n    authors: [\\\"Keppo et al.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.20281\\\"\\n    category: \\\"multi_agent_robustness\\\"\\n    role: \\\"supporting\\\"\\n    relevance: \\\"Increasing LLM count 2→5 breaks collusion (+22%→+3%). Same-family size heterogeneity stabilizes via leader-follower dynamics. Motivates cross-family diversity requirement in our protocol design.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\", \"total_chars\": 7700, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06049c1e-5cea-46f1-9ecd-dcbfab71873c",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "6d220b97-c139-48bd-8b78-71464c1556e4",
  "sourceToolAssistantUUID": "06049c1e-5cea-46f1-9ecd-dcbfab71873c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T18:48:47.838Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L9gokc73cLVKq1wHwZV5Rm`</summary>

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
  "parentUuid": "6d220b97-c139-48bd-8b78-71464c1556e4",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7BLtNCXxypKkTx9abN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ba9e6b1-222c-44ad-aa5a-e73459f9bf3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115CveiMDanWXSAKLmMk7ry",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16209,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 315,
          "cache_read_input_tokens": 16209,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 12 · 2026-05-22T18:48:47.848Z_

<details><summary>↩ Tool result · `toolu_01L9gokc73cLVKq1wHwZV5Rm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/paper_framing.md\", \"content\": \"# Paper Framing — cert_manip_resist_eval (v4b: Dominance Analysis Correction)\\n\\n> Last updated: 2026-05-22 | Reason: Dominance analysis unifies regression specifications; K_eff 7/12 positive + 1/12 negative (arc×sycophancy protective); condition-dependent dual drivers\\n\\n## Target\\nEMNLP 2026 (via ARR)\\n\\n## Title Candidates\\n1. \\\"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\\\"\\n2. \\\"More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries\\\"\\n3. \\\"Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability\\\"\\n\\n## Core Insight\\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **predominantly reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently positively associated with attack success rate in **7/12 conditions**, while being protective in only **1/12** (arc×sycophancy). Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with condition-dependent relative importance. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create. The exception (sycophancy) reveals that when attacks exploit a shared bias, diverse panels can dilute the bias — but this is the minority regime.\\n\\n## Hook\\n\\\"Adding more diverse judges to an evaluation panel predominantly makes it more vulnerable to adversarial manipulation — with a revealing exception that proves the rule.\\\"\\n\\n## Novelty Positioning\\nWe do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:\\n1. **First empirical quantification of diversity's condition-dependent effect** in the LLM-judge domain (15 models, 455 panels, dominance analysis: K_eff positive 7/12, negative 1/12, NS 4/12 — predominantly harmful but with a mechanistically informative exception)\\n2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominant 4/12, co-dominant 7/12, K_eff sole dominant 1/12)\\n3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries\\n4. **Structural barriers**: diversity-capability tradeoff (now with independent predictive evidence), family label unreliability (confirmed at 15-model). ~~Copula failure removed — falsified at scale~~\\n5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap\\n**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max) AND panel diversity (K_eff). Diversity **predominantly increases** vulnerability (7/12 conditions), with one mechanistically informative exception where diversity is protective (arc×sycophancy, 1/12). Their relative importance is condition-dependent.\\n**Evidence** (15-model, 455 panels, 12 conditions, dominance analysis — canonical regression model):\\n- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε), std_β = raw_β × SD(log_x)/SD(log_y), FDR = BH per predictor\\n- η_max FDR significant: **11/12** (only NS: arc×position_bias p=0.909)\\n- K_eff FDR significant positive: **7/12**\\n- K_eff FDR significant negative: **1/12** (arc×sycophancy: std_β = -0.192, FDR p = 0.0095)\\n- K_eff NS: **4/12** (mmlu×{score_manip, position, authority}, arc×verbosity)\\n- Dominance pattern: η_max sole dominant **4/12**, co-dominant (both sig) **7/12**, K_eff sole dominant **1/12** (arc×position_bias)\\n- **arc×sycophancy exception**: When attack exploits a shared cognitive bias, diverse panels dilute the bias — the ONE condition where BFT logic holds. This exception reveals the mechanism boundary.\\n**Strength**: Strong. η_max is the more consistent driver (11/12), K_eff is condition-dependent (7/12 harmful, 1/12 protective). Together they form the dual vulnerability driver story.\\n**Headline**: \\\"η_max significant in 11/12, K_eff predominantly harmful (7/12) with one protective exception (sycophancy). Condition-dependent dual drivers.\\\"\\n\\n**Comparison to 6-model results** (for transparency):\\n- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → \\\"K_eff irrelevant\\\"\\n- 15-model (455 panels): K_eff 7/12 sig positive, 1/12 sig negative → \\\"K_eff predominantly harmful, condition-dependent\\\"\\n- The emergence of K_eff's effect is driven by model pool expansion: wider capability spectrum enables detecting both its harmful AND protective regimes.\\n\\n### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap\\n**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.\\n**Evidence** (15-model, 455 panels):\\n- K_eff significant in both regimes, predominantly positive direction (7/12 adaptive positive, 1/12 negative)\\n- ΔR² = +0.213 mean (RF explains more variance)\\n**Reframing from v3**: Original BFT contrast (\\\"K_eff helps under RF but not adaptive\\\") does NOT hold — K_eff is predominantly harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.\\n**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped. Numbers need revalidation with dominance analysis for RF regime.\\n\\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.\\n**Evidence**:\\n- K_eff-η_max correlation: r = +0.700 (15-model)\\n- K_eff still significant 7/12 positive (dominance analysis) → not purely mediated by η_max\\n- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains\\n**Upgrade from v3**: From \\\"correlation\\\" to \\\"independent predictive effect\\\" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.\\n**Strength**: Strong (statistical association). Causal language avoided.\\n\\n### Claim 4 (Methodological): Family Labels ≠ Diversity\\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\\n**Evidence**:\\n- 6-model: Mann-Whitney U p=0.206, permutation p=0.427\\n- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.\\n- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)\\n**Strength**: Moderate. Consistent across 6→15 model scaling.\\n\\n### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation\\n**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.\\n**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.\\n**Disposition**: Remove as independent contribution. Optionally note in analysis: \\\"Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence.\\\"\\n**Strength**: DEAD as independent claim. May retain as minor observation.\\n\\n### Claim 6 (Practical): Robustness-First Panel Design\\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\\n**Evidence** (15-model, 455 panels — fully validated):\\n- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)\\n- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)\\n- Robust across panel sizes K=10, 20, 50\\n- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff\\n- Consistent with canonical regression: η_max 11/12 dominant\\n**Strength**: Strong (15-model fully confirmed). Zero failure conditions.\\n\\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers\\n**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).\\n**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):\\n- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)\\n- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive\\n- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity\\n- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104\\n- Key findings:\\n  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)\\n  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)\\n  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm\\n  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)\\n  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)\\n**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.\\n\\n## Contribution Stack (ordered by strength)\\n1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff predominantly harmful 7/12 + protective exception + condition-dependent dominance)\\n2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)\\n3. **BFT reversal mechanism + mechanism boundary** — theoretical contribution (why independence hurts under adaptive adversaries; sycophancy exception reveals boundary)\\n4. **Aggregation-dependent effects** — empirical+practical (Bayesian mitigates both drivers: η_max 11→9/12, K_eff flips to 6/7 negative; threshold R²=0.89; D017 Reviewer-verified)\\n5. **Robustness-first panel design** — practical contribution\\n6. **Family label unreliability** — methodological contribution (confirmed at 15-model scale)\\n7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)\\n~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: \\\"K_eff positive is just confound with η_max\\\"\\n**Response**: (a) Dominance analysis with VIF-controlled regression: K_eff still significant 7/12 positive, 1/12 negative; (b) In low-confound conditions (r≈0.35), K_eff highly significant; (c) The 1/12 negative case (arc×sycophancy) proves K_eff's effect is not a confound artifact — if it were purely confound, K_eff would be uniformly positive, not condition-dependent.\\n\\n### RC2: \\\"Why does diversity hurt? What's the mechanism?\\\"\\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis reveals the mechanism boundary: K_eff is harmful when attacks can exploit judge-specific weaknesses (7/12), but protective when attacks exploit a shared bias that diverse panels can dilute (sycophancy, 1/12). This mechanism distinction (exploit-specific vs bias-shared) explains the full pattern.\\n\\n### RC3: \\\"Only 15 models — does this generalize?\\\"\\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\\n\\n### RC4: \\\"BFT comparison is a strawman\\\"\\n**Response**: (a) The implicit assumption \\\"more diverse judges = more robust\\\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\\n\\n### RC5: \\\"Why not just use the strongest models?\\\"\\n**Response**: (a) \\\"Strongest\\\" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\\n\\n### RC6: \\\"No theoretical novelty\\\"\\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\\n\\n### RC7: \\\"Why not just use Bayesian aggregation?\\\"\\n**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.\\n\\n### RC8: \\\"6-model and 15-model results contradict — which is right?\\\"\\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\\n\\n### RC9 (new): \\\"arc×sycophancy exception undermines your claim\\\"\\n**Response**: (a) The exception STRENGTHENS the paper — it reveals the mechanism boundary between exploit-specific attacks (where diversity hurts) and shared-bias attacks (where diversity helps); (b) 7/12 vs 1/12 clearly shows which regime dominates; (c) The exception is theoretically predicted: sycophancy is a shared cognitive bias across models, so diverse panels dilute it (classic BFT logic applies); (d) This gives practitioners an actionable decision rule: check whether the threat model involves shared biases or judge-specific exploits.\\n\\n## \\\"When Diversity Helps\\\" Section\\nDiversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:\\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\\n2. **Shared-bias attacks (empirically confirmed)**: arc×sycophancy shows K_eff significantly NEGATIVE (std_β = -0.192, p = 0.0095). When an attack exploits a cognitive bias shared across models, diverse panels dilute the bias. This is the ONE adversarial condition where BFT logic holds.\\n3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\\n4. **Summary**: K_eff is harmful in 7/12, NS in 4/12, protective in 1/12 conditions. The protective case (sycophancy) is mechanistically distinct and strengthens the overall story by revealing the mechanism boundary.\\n\\n## Story Arc (v4b)\\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\\n3. **Surprise**: Diversity predominantly **increases** vulnerability (K_eff positive in 7/12 conditions) — the opposite of what BFT predicts\\n4. **Mechanism**: Adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent dominance (η_max dominant 4/12, co-dominant 7/12, K_eff sole dominant 1/12)\\n5. **The Exception That Proves the Rule**: arc×sycophancy — the ONE condition where K_eff is significantly negative (diversity protective). When attacks exploit a shared cognitive bias, diverse panels dilute it. This exception reveals the mechanism boundary: BFT logic holds for shared-bias attacks but fails for exploit-specific attacks\\n6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels\\n7. **Implication**: The relationship between panel diversity and security is not monotonic — it depends on the attack mechanism. The default assumption \\\"more diverse = more robust\\\" is wrong in the majority regime\\n\", \"total_chars\": 18358, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ba9e6b1-222c-44ad-aa5a-e73459f9bf3e",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "5e3d45e7-6954-47a7-9733-adbc40c63180",
  "sourceToolAssistantUUID": "2ba9e6b1-222c-44ad-aa5a-e73459f9bf3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T18:48:50.842Z_

Now let me read the actual paper draft and other relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e3d45e7-6954-47a7-9733-adbc40c63180",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7Bn7upGd3uhiFCcv9G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8215a425-67f7-404b-8dee-d75640fdd940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoerJhBUUQo89qiP8Cp2Mr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9843,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9843,
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

_source line 14 · 2026-05-22T18:48:52.976Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MkVgMuSeS4ANa5DKNd3MFW`</summary>

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
  "parentUuid": "8215a425-67f7-404b-8dee-d75640fdd940",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7Bn7upGd3uhiFCcv9G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cc4c6d5-a2fb-4409-b62a-ff9c750e6c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoerJhBUUQo89qiP8Cp2Mr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9843,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9843,
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

_source line 15 · 2026-05-22T18:48:53.011Z_

<details><summary>↩ Tool result · `toolu_01MkVgMuSeS4ANa5DKNd3MFW`</summary>

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
docs/paper/introduction.tex
artifacts/dream_reports/dream_20260522T173833/best/paper.tex
artifacts/dream_reports/dream_20260522T173833/median/paper.tex
artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
docs/paper/threat_model.tex
docs/paper/methodology.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cc4c6d5-a2fb-4409-b62a-ff9c750e6c01",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "8da7de8b-71ad-431c-ae4a-1a36bd0f96af",
  "sourceToolAssistantUUID": "5cc4c6d5-a2fb-4409-b62a-ff9c750e6c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T18:48:53.876Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VN9JkSeBNJaLFko9HF4hxC`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da7de8b-71ad-431c-ae4a-1a36bd0f96af",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7Bn7upGd3uhiFCcv9G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7be5e506-88c4-40e5-8769-86eccc6fc8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoerJhBUUQo89qiP8Cp2Mr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9843,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9843,
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

_source line 17 · 2026-05-22T18:48:53.886Z_

<details><summary>↩ Tool result · `toolu_01VN9JkSeBNJaLFko9HF4hxC`</summary>

```text
artifacts/dream_reports/dream_20260522T055016/best/paper.pdf
artifacts/dream_reports/dream_20260522T055016/median/paper.pdf
artifacts/dream_reports/dream_20260522T055016/worst/paper.pdf
artifacts/theorem1_proof.pdf
artifacts/dream_reports/dream_20260522T173833/best/paper.pdf
artifacts/dream_reports/dream_20260522T173833/median/paper.pdf
artifacts/dream_reports/dream_20260522T173833/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7be5e506-88c4-40e5-8769-86eccc6fc8ee",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "3dec99a7-f939-485c-b19a-4104e7b57780",
  "sourceToolAssistantUUID": "7be5e506-88c4-40e5-8769-86eccc6fc8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T18:48:54.734Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017zLDzidVvWfSms8hBGyWG1`</summary>

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
  "parentUuid": "3dec99a7-f939-485c-b19a-4104e7b57780",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7Bn7upGd3uhiFCcv9G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb2e03ec-8d1a-406b-b747-d7fa2d5c73f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoerJhBUUQo89qiP8Cp2Mr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9843,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9843,
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

_source line 19 · 2026-05-22T18:48:54.744Z_

<details><summary>↩ Tool result · `toolu_017zLDzidVvWfSms8hBGyWG1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/ROADMAP.md\", \"content\": \"# cert_manip_resist_eval — Research Dashboard\\n\\n> 最后更新: 2026-05-22 18:42 UTC | 更新原因: Reviewer-verified aggregation numbers (corrected weighted 9/12, bayesian K_eff 7/12 with 6 neg)\\n\\n## 核心方向\\n**The Diversity Trap**：LLM judge panel diversity 在 adaptive adversary 下 predominantly 增加脆弱性（K_eff 7/12 正, 1/12 负）。η_max (11/12) 是更一致的驱动因子，K_eff 条件依赖。详见 paper_framing.md v4b+D017。\\n\\n## 当前阶段\\n**Research 阶段** — 全部 15-model 分析完成，论文写作 + 修正推进中\\n\\n## 当前进展\\n- ✅ 全部 P0-P2b 分析完成（15 models, 455 panels）\\n- ✅ Claim 6 Panel Design: min(η_max) **12/12** 全胜\\n- ✅ P2b log-log canonical + Reviewer 验证通过\\n- ✅ Registry plan001_step1_full_v4 DONE\\n- 📌 Paper Agent: methodology critical 修正 + Results 章节\\n- 📌 Dream simulation (dream_20260522T173833) — writing 阶段\\n- 📌 Agent: 提供完整 15 模型列表\\n\\n## 关键数据（唯一来源: dominance analysis, log-log OLS）\\n| Metric | Value |\\n|--------|-------|\\n| η_max FDR sig | **11/12** (only NS: arc×position) |\\n| K_eff FDR sig + | **7/12** |\\n| K_eff FDR sig − | **1/12** (arc×sycophancy) |\\n| K_eff NS | **4/12** |\\n| Regression spec | log(ASR+ε) ~ log(K_eff) + log(η_max+ε) |\\n\\n### Aggregation 效应 (P2b log-log canonical, D017, Reviewer-verified)\\n| Method | η_max sig | K_eff sig | K_eff +/− | R² |\\n|--------|-----------|-----------|-----------|-----|\\n| majority | 11/12 | 8/12 | 7+/1− | 0.298 |\\n| weighted | 9/12 | 9/12 | 9+/0− | 0.284 |\\n| threshold | **12/12** | **11/12** | 10+/1− | **0.890** |\\n| bayesian | 9/12 | 7/12 | 1+/**6−** | 0.104 |\\n\\n## 近期任务\\n- [x] P0-P2b: 全部 15-model 分析完成 + Reviewer 验证\\n- [x] Claim 6: 15-model panel design 验证 (12/12)\\n- [ ] Paper Agent: methodology critical 修正（模型名 + MI 方法 + 实验细节）\\n- [ ] Paper Agent: Results 章节（含 P2b Reviewer-verified aggregation 数据）\\n- [ ] Dream report 处理\\n- [ ] Agent: 完整 15 模型列表\\n- [ ] Theorem 1 scope 更新\\n\\n## GPU 预算\\nseetacloud-rtx6000: 4× RTX 6000 96G（全空闲，写作阶段）\\n\\n## 目标\\nEMNLP 2026 via ARR | Contribution stack: 7 items | All analyses complete\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D017 | 2026-05-22 | Claim 7 final (log-log canonical): Bayesian partia | plan001_step1_full_v4 |\\n| D016 | 2026-05-22 | Claim 7 revised: \\\"Bayesian breaks weakest-link\\\" fa | plan001_step1_full_v4 |\\n| D015 | 2026-05-22 | Claim 5 (Gaussian Copula Failure) falsified at 15- | worker_analysis_15model-family-copula |\\n| D014 | 2026-05-22 | 15-model 结果证伪原始 Claim 1 (\\\"K_eff irrelevant\\\")；K_eff | plan001_step1_full_v4 |\\n| D013 | 2026-05-22 | 7-model 预览显示 Claim 2 复活信号：random-fault K_eff gains | plan_001_7model_preview |\\n| D012 | 2026-05-22 | Plan_010 聚合实验完成：Bayesian 部分打破 weakest-link (3/12 v | plan_010 |\\n| D011 | 2026-05-22 | Plan_003 BFT contrast failed (0/12 random-fault K_ | plan_003 |\\n| D010 | 2026-05-22 | Dream review (2.5 all tiers) exposed 13 structural | — |\\n| D009 | 2026-05-22 | Taxonomy 验证失败（0/6 新条件 K_eff 显著），建议 kill 项目 | taxonomy-broad-spectrum |\\n| D008 | 2026-05-22 | MVP 原假设部分证伪：K_eff 仅对 shared-bias attacks 显著，η_max  | mvp-step2v3-retry3 |\\n\\n\\n\\n\", \"total_chars\": 2882, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb2e03ec-8d1a-406b-b747-d7fa2d5c73f9",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "b4991f1f-34eb-408a-8418-0f21b088b23c",
  "sourceToolAssistantUUID": "cb2e03ec-8d1a-406b-b747-d7fa2d5c73f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T18:48:55.268Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JWzXnd61fWwUDDD4EcaZGn`</summary>

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
  "parentUuid": "b4991f1f-34eb-408a-8418-0f21b088b23c",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7Bn7upGd3uhiFCcv9G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ad7b60c-a92d-4147-9f65-f4a3c39c25b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoerJhBUUQo89qiP8Cp2Mr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9843,
      "cache_read_input_tokens": 17655,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9843
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 385,
          "cache_read_input_tokens": 17655,
          "cache_creation_input_tokens": 9843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9843,
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

_source line 21 · 2026-05-22T18:48:55.278Z_

<details><summary>↩ Tool result · `toolu_01JWzXnd61fWwUDDD4EcaZGn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cert_manip_resist_eval'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ad7b60c-a92d-4147-9f65-f4a3c39c25b2",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "28eae8fc-ee32-47c8-b847-187be486c7e2",
  "sourceToolAssistantUUID": "5ad7b60c-a92d-4147-9f65-f4a3c39c25b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-22T18:48:57.389Z_

Let me read the paper's main tex file and all sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28eae8fc-ee32-47c8-b847-187be486c7e2",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7CKhhqCsfk6EiGRYie",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93735468-a777-4b2f-8fa4-e8d5a87a0408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VxCkvSt7YNQBEZ8258jAp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2688,
      "cache_read_input_tokens": 27498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2688,
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

_source line 23 · 2026-05-22T18:48:59.321Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NnVYqco9n3pwvucTJmfhdE`</summary>

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
  "parentUuid": "93735468-a777-4b2f-8fa4-e8d5a87a0408",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7CKhhqCsfk6EiGRYie",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e25dce3-565c-499a-a786-4853c261beee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VxCkvSt7YNQBEZ8258jAp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2688,
      "cache_read_input_tokens": 27498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2688,
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

_source line 24 · 2026-05-22T18:48:59.340Z_

<details><summary>↩ Tool result · `toolu_01NnVYqco9n3pwvucTJmfhdE`</summary>

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
  "parentUuid": "8e25dce3-565c-499a-a786-4853c261beee",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "da393fee-bc56-477a-ab2d-0ae8033372b3",
  "sourceToolAssistantUUID": "8e25dce3-565c-499a-a786-4853c261beee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T18:48:59.400Z_

<details open><summary>🔧 Tool call — Read · `toolu_013gb1GUJUGsyGiVvd6K4pc4`</summary>

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
  "parentUuid": "da393fee-bc56-477a-ab2d-0ae8033372b3",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7CKhhqCsfk6EiGRYie",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02c5c275-b2d1-44cb-a00d-6d229e2e5ecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VxCkvSt7YNQBEZ8258jAp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2688,
      "cache_read_input_tokens": 27498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2688,
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

_source line 26 · 2026-05-22T18:48:59.406Z_

<details><summary>↩ Tool result · `toolu_013gb1GUJUGsyGiVvd6K4pc4`</summary>

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
  "parentUuid": "02c5c275-b2d1-44cb-a00d-6d229e2e5ecb",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "752c9014-105b-4eaf-a39d-b95282798ade",
  "sourceToolAssistantUUID": "02c5c275-b2d1-44cb-a00d-6d229e2e5ecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T18:48:59.991Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XBx9TqR5sKEwnuTtWkCZWj`</summary>

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
  "parentUuid": "752c9014-105b-4eaf-a39d-b95282798ade",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7CKhhqCsfk6EiGRYie",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f9e4942-8f4a-4183-9588-8951cae0ff62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VxCkvSt7YNQBEZ8258jAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2688,
      "cache_read_input_tokens": 27498,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 27498,
          "cache_creation_input_tokens": 2688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2688,
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

_source line 28 · 2026-05-22T18:48:59.994Z_

<details><summary>↩ Tool result · `toolu_01XBx9TqR5sKEwnuTtWkCZWj`</summary>

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
  "parentUuid": "4f9e4942-8f4a-4183-9588-8951cae0ff62",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "25081384-3f47-4172-8bf6-2bd4f9b75ebe",
  "sourceToolAssistantUUID": "4f9e4942-8f4a-4183-9588-8951cae0ff62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T18:49:03.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QSYjL7T28nVJvoXVYhoAu3`</summary>

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
  "parentUuid": "25081384-3f47-4172-8bf6-2bd4f9b75ebe",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7CgCzRcyiWhu4GCJU3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fc8a6cf-3075-4db7-ada0-3fe5689154de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Mi4rzWGuX9Z9ckLTeQmhA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3400,
      "cache_read_input_tokens": 30186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3400,
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

_source line 30 · 2026-05-22T18:49:03.845Z_

<details><summary>↩ Tool result · `toolu_01QSYjL7T28nVJvoXVYhoAu3`</summary>

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
28	The theorem establishes that $\eta_{\max}$ is monotonically linked to panel vulnerability, but is silent on the role of diversity. To disentangle the two drivers, we fit a regression $\log(\mathrm{ASR}) \sim \beta_1 \log(\eta_{\max}) + \beta_2 \log(K_{\mathrm{eff}})$ across panels. The theorem predicts $\beta_1 > 0$; the SDPI bound under non-adaptive faults would suggest $\beta_2 \leq 0$; but the reversal mechanism predicts $\beta_2 > 0$ when attacks exploit judge-specific vulnerabilities, and $\beta_2 < 0$ when attacks exploit shared cognitive biases that diverse panels can dilute---a distinction our experiments in \S\ref{sec:experiments} test across 12 conditions spanning two benchmarks and six attack types, using dominance analysis to isolate each driver's independent contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fc8a6cf-3075-4db7-ada0-3fe5689154de",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "0fbec2d5-fcad-4fd3-8efa-bd3f15c8ffd3",
  "sourceToolAssistantUUID": "8fc8a6cf-3075-4db7-ada0-3fe5689154de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T18:49:04.242Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JT2cbFdvaAmmTcPZ4YyEUK`</summary>

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
  "parentUuid": "0fbec2d5-fcad-4fd3-8efa-bd3f15c8ffd3",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7CgCzRcyiWhu4GCJU3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f67b57d-595f-4939-8699-e6df7c17aac9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Mi4rzWGuX9Z9ckLTeQmhA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3400,
      "cache_read_input_tokens": 30186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3400,
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

_source line 32 · 2026-05-22T18:49:04.247Z_

<details><summary>↩ Tool result · `toolu_01JT2cbFdvaAmmTcPZ4YyEUK`</summary>

```text
1	\section{Experimental Methodology}
2	\label{sec:experiments}
3	
4	\subsection{Models and Panel Construction}
5	
6	We select 15 LLM judges spanning 5 provider families and 3 capability tiers, listed in Table~\ref{tab:models}. Nine models are accessed via the OpenRouter API; six open-weight models are served locally using vLLM~0.21.0 with AWQ INT4 quantization on an NVIDIA RTX~6000 (96\,GB). Capability tiers are assigned by mean clean accuracy across both benchmarks: \emph{frontier} (top 5), \emph{mid-tier} (middle 5), and \emph{lightweight} (bottom 5). All panels consist of $K{=}3$ judges with majority-vote threshold $t{=}2$. Exhaustive enumeration yields $\binom{15}{3} = 455$ unique panels, covering every combination of families and tiers. Each panel evaluates all benchmark items under all attack types, producing a complete panel $\times$ item $\times$ attack tensor.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\begin{tabular}{llll}
12	\toprule
13	\textbf{Model} & \textbf{Family} & \textbf{Tier} & \textbf{Deploy} \\
14	\midrule
15	gpt-5.5              & OpenAI    & frontier    & API \\
16	gpt-4.1              & OpenAI    & frontier    & API \\
17	gpt-4.1-mini          & OpenAI    & mid-tier    & API \\
18	gpt-4.1-nano          & OpenAI    & lightweight & API \\
19	claude-opus-4-6       & Anthropic & frontier    & API \\
20	claude-sonnet-4-6     & Anthropic & mid-tier    & API \\
21	claude-3-haiku        & Anthropic & lightweight & API \\
22	gemini-3.1-pro-preview & Google   & frontier    & API \\
23	gemini-3.5-flash      & Google    & mid-tier    & API \\
24	qwen2.5-32b           & Qwen      & mid-tier    & local \\
25	qwen2.5-14b           & Qwen      & lightweight & local \\
26	llama-3.1-8b          & Llama     & lightweight & local \\
27	\emph{[3 local models TBD]} & --- & --- & local \\
28	\bottomrule
29	\end{tabular}
30	\caption{Judge models used in the study. API models accessed via OpenRouter; local models served with vLLM + AWQ INT4 quantization. Tier assignment is based on mean clean accuracy across MMLU and ARC.}
31	\label{tab:models}
32	\end{table}
33	
34	\subsection{Benchmarks and Attack Types}
35	
36	Two benchmarks test distinct evaluation capabilities: MMLU \citep{hendrycks2021mmlu}, a knowledge-intensive multiple-choice benchmark spanning 57 subjects, and ARC \citep{clark2018arc}, a reasoning-intensive science question benchmark. We sample 300 items from each benchmark. MMLU probes factual recall and broad domain knowledge; ARC requires multi-step scientific reasoning. All API calls use temperature~0 for deterministic outputs; local models are served with the same temperature setting. Attacked variants are generated by programmatically applying each manipulation to the candidate text, with a fixed random seed for reproducibility.
37	
38	Each benchmark is paired with six attack types that target different judge vulnerabilities: (1)~\textbf{prompt injection}, adversarial instructions embedded in candidate text that override the evaluation prompt \citep{perez2022ignore,greshake2023not}; (2)~\textbf{sycophancy}, responses engineered to agree with or flatter the judge \citep{wang2023fair}; (3)~\textbf{score manipulation}, explicit numerical cues (e.g., ``this answer deserves a 10/10'') injected into the candidate to anchor scoring; (4)~\textbf{verbosity bias}, padding correct answers with excessive irrelevant detail to exploit length preferences \citep{zheng2023judging}; (5)~\textbf{position bias}, reordering candidate answers to place the target in the position judges systematically favor \citep{wang2023fair}; and (6)~\textbf{authority bias}, prefacing candidate text with fabricated credentials or citations to inflate perceived credibility. The combination of 2 benchmarks and 6 attacks produces 12 experimental conditions, each evaluated across all 455 panels.
39	
40	\subsection{Vulnerability Metrics}
41	
42	Per-judge vulnerability under attack $a$ is the fraction of items where judge $j$ is fooled: $\eta_j(a) = \Pr(X_j^a {=} 1)$, estimated empirically over the item set. The weakest-link vulnerability $\eta_{\max}(a) = \max_{j \in \mathcal{P}} \eta_j(a)$ captures the most susceptible member of each panel. The panel attack success rate $\mathrm{ASR}(\mathcal{P}, a)$ is the fraction of items where at least $t$ judges are simultaneously fooled. Panel diversity is quantified by $K_{\mathrm{eff}}$ (Equation~\ref{eq:keff}), computed from pairwise mutual information between judges' three-category winner labels (model~A wins, model~B wins, tie) on clean (unattacked) data. MI is estimated via the plug-in estimator with Miller--Madow bias correction. In practice, $K_{\mathrm{eff}}$ is computed through the Gaussian copula correlation matrix: under the Gaussian assumption, pairwise MI and copula $\rho$ are related by $\mathrm{MI} = -\tfrac{1}{2}\log(1-\rho^2)$ \citep{nelsen2006copulas}, and we substitute $\exp(-2\,\mathrm{MI}) = 1 - \rho^2$ directly into Equation~\ref{eq:keff}. Together, $\eta_{\max}$ and $K_{\mathrm{eff}}$ serve as the two predictors in the regression framework below: $\eta_{\max}$ indexes the weakest-link channel and $K_{\mathrm{eff}}$ indexes the diversity channel.
43	
44	\subsection{Aggregation Methods}
45	
46	Beyond the default majority vote, we evaluate three alternative aggregation rules to test whether the diversity trap persists under different decision mechanisms. The aggregation comparison uses the same log-log regression specification as the primary analysis (Equation~\ref{eq:regression}).
47	
48	\paragraph{Majority Vote.} Accept if $\sum_{j=1}^K \mathbf{1}[J_j \text{ approves}] \geq \lceil K/2 \rceil$. This is the standard baseline aggregation assumed throughout the main analysis.
49	
50	\paragraph{Accuracy-Weighted Vote.} Accept if $\sum_{j=1}^K w_j \cdot \mathbf{1}[J_j \text{ approves}] > 0.5$, where $w_j \propto \mathrm{acc}_j$ on held-out clean data, normalized so that $\sum_j w_j = 1$. Judges with higher clean-data accuracy receive proportionally greater influence.
51	
52	\paragraph{Threshold Vote (Unanimity).} Accept only if all $K$ judges approve ($t = K$). A single dissenting judge suffices to reject, making this the most conservative rule.
53	
54	\paragraph{Bayesian Calibration.} Compute $P(\text{correct} \mid \mathbf{v}) \propto P(\text{correct}) \prod_j P(v_j \mid \text{correct})$, where $P(v_j \mid \cdot)$ is derived from judge $j$'s confusion matrix on clean data and $\mathbf{v}$ is the observed vote vector. Accept if the posterior exceeds 0.5. This rule uses each judge's calibrated reliability rather than treating all votes equally.
55	
56	\subsection{Statistical Framework}
57	\label{sec:stat_framework}
58	
59	To disentangle the contributions of panel diversity and individual judge robustness, we fit a log-log OLS regression for each of the 12 conditions:
60	\begin{equation}
61	\label{eq:regression}
62	\log(\mathrm{ASR} + \epsilon) = \alpha + \beta_1 \log(K_{\mathrm{eff}}) + \beta_2 \log(\eta_{\max} + \epsilon),
63	\end{equation}
64	with $\epsilon = 10^{-6}$ to handle zero values. Standardized coefficients $\hat{\beta}_{\mathrm{std}} = \hat{\beta} \cdot \mathrm{SD}(\log x) / \mathrm{SD}(\log y)$ enable direct comparison of effect magnitudes across predictors and conditions. We apply Benjamini-Hochberg correction for multiple testing, controlling the false discovery rate per predictor across the 12 conditions.
65	
66	To assess relative predictor importance beyond regression coefficients, we perform dominance analysis \citep{budescu1993dominance}. This method decomposes $R^2$ by averaging each predictor's incremental $R^2$ contribution across all possible subsets of predictors. A predictor is \emph{dominant} if its average contribution exceeds that of the competing predictor in every subset ordering. With two predictors, dominance reduces to comparing each predictor's solo $R^2$ with its incremental $R^2$ conditional on the other.
67	
68	\subsection{Sensitivity Analysis}
69	
70	Judges with clean-data accuracy below 0.5 perform at or below chance and could drive regression results through extreme outlier behavior rather than meaningful vulnerability patterns. We exclude such judges from panel construction and re-run the log-log regression (Equation~\ref{eq:regression}) to verify that the $K_{\mathrm{eff}}$ effect remains stable after removing these potential confounds.
71	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f67b57d-595f-4939-8699-e6df7c17aac9",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "f4d71846-cdee-448f-bdcc-6d549a38e068",
  "sourceToolAssistantUUID": "0f67b57d-595f-4939-8699-e6df7c17aac9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T18:49:04.533Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uo9XrGnb6p8q4LkFt7jQK1`</summary>

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
  "parentUuid": "f4d71846-cdee-448f-bdcc-6d549a38e068",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7CgCzRcyiWhu4GCJU3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8524da4a-fb69-4a9e-abd0-ae9bb7ecf73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Mi4rzWGuX9Z9ckLTeQmhA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3400,
      "cache_read_input_tokens": 30186,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3400
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 30186,
          "cache_creation_input_tokens": 3400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3400,
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

_source line 34 · 2026-05-22T18:49:04.537Z_

<details><summary>↩ Tool result · `toolu_01Uo9XrGnb6p8q4LkFt7jQK1`</summary>

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
18	Threshold       & 12/12 & 11/12 & 10+/1$-$  & 0.901 \\
19	Majority        & 11/12 & 8/12  & 7+/1$-$   & 0.376 \\
20	Weighted        & 11/12 & 11/12 & 11+/0$-$  & 0.357 \\
21	Bayesian        & 9/12  & 5/12  & 1+/4$-$   & 0.105 \\
22	\bottomrule
23	\end{tabular}
24	\caption{Aggregation method comparison (15 models, 455 panels, log-log canonical spec). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Methods are ordered by $R^2$ to highlight the vulnerability gradient from threshold (most predictable) to Bayesian (least).}
25	\label{tab:aggregation}
26	\end{table}
27	
28	Four patterns emerge. First, the aggregation methods form a clear vulnerability gradient: threshold voting ($R^2{=}0.901$) makes panel composition almost perfectly predictive of attack success, while Bayesian calibration ($R^2{=}0.105$) compresses the ASR distribution so that compositional factors explain little variance. Second, Bayesian calibration suppresses both vulnerability channels: $K_{\mathrm{eff}}$ significance drops from 8/12 (majority) to 5/12, and the coefficient direction flips from predominantly positive (7+/1$-$) to predominantly negative (1+/4$-$), meaning diversity shifts from harmful to partially protective under proper reliability calibration. Bayesian also partially weakens $\eta_{\max}$ (11/12 $\to$ 9/12). Third, threshold voting amplifies both channels: $\eta_{\max}$ reaches 12/12 and $K_{\mathrm{eff}}$ reaches 11/12, because unanimity requirements make panels maximally sensitive to both individual weakness and structural diversity. Fourth, weighted voting increases $K_{\mathrm{eff}}$ significance (11/12, all positive) relative to majority voting, suggesting that accuracy weighting does not mitigate the diversity trap.
29	
30	These results yield a prescriptive gradient. Bayesian calibration is the only aggregation method that suppresses the diversity channel and partially weakens the weakest-link channel, but it does not eliminate either. A two-pronged defense is needed: robustness-first panel selection to address $\eta_{\max}$, combined with Bayesian aggregation to mitigate $K_{\mathrm{eff}}$ vulnerability. Neither intervention alone addresses both drivers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8524da4a-fb69-4a9e-abd0-ae9bb7ecf73d",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "c40c15e9-d408-4c25-8b3c-7aedb0b3da15",
  "sourceToolAssistantUUID": "8524da4a-fb69-4a9e-abd0-ae9bb7ecf73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T18:49:16.485Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NkNXVAJbFf4roZxnXADGYU`</summary>

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
  "parentUuid": "c40c15e9-d408-4c25-8b3c-7aedb0b3da15",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7D1Xb3cxWjFFnymx98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "711f6026-8ce3-4fbc-890f-af98f4ba7a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015L15PddGV94SNq2sQqxVS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5479,
      "cache_read_input_tokens": 33586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5479,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 36 · 2026-05-22T18:49:16.491Z_

<details><summary>↩ Tool result · `toolu_01NkNXVAJbFf4roZxnXADGYU`</summary>

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
  "parentUuid": "711f6026-8ce3-4fbc-890f-af98f4ba7a86",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "6b8e37fb-c66b-4d48-937d-bf3d5a179434",
  "sourceToolAssistantUUID": "711f6026-8ce3-4fbc-890f-af98f4ba7a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T18:49:16.873Z_

<details open><summary>🔧 Tool call — Read · `toolu_0158BtAbFV6pBDiwiB2jaTTB`</summary>

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
  "parentUuid": "6b8e37fb-c66b-4d48-937d-bf3d5a179434",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7D1Xb3cxWjFFnymx98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d746cf1-23ca-4d7f-92e4-d312d9eaa32e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015L15PddGV94SNq2sQqxVS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5479,
      "cache_read_input_tokens": 33586,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 33586,
          "cache_creation_input_tokens": 5479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5479,
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

_source line 38 · 2026-05-22T18:49:16.880Z_

<details><summary>↩ Tool result · `toolu_0158BtAbFV6pBDiwiB2jaTTB`</summary>

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
  "parentUuid": "0d746cf1-23ca-4d7f-92e4-d312d9eaa32e",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "80280853-a1ee-4689-9f91-4a83b4f72eed",
  "sourceToolAssistantUUID": "0d746cf1-23ca-4d7f-92e4-d312d9eaa32e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-22T18:49:22.914Z_

Now let me look at the dream report (the most recent simulation) for the complete paper version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80280853-a1ee-4689-9f91-4a83b4f72eed",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7DvUm6ifTHwqTCjyjU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5018c860-b37c-4241-9853-4c56d1e7d747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rnuvs7emr8KvPTuzfRAvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 39065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 275,
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

_source line 40 · 2026-05-22T18:49:24.526Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2AHD7EUZriCbjVtupQ8Up`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5018c860-b37c-4241-9853-4c56d1e7d747",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7DvUm6ifTHwqTCjyjU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af1a0641-07c2-4003-88bc-9a3fd69589fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rnuvs7emr8KvPTuzfRAvb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 39065,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 39065,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 275,
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

_source line 41 · 2026-05-22T18:49:24.532Z_

<details><summary>↩ Tool result · `toolu_01Y2AHD7EUZriCbjVtupQ8Up`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{amsmath}
8	\usepackage{amsfonts}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{enumitem}
12	\usepackage{tabularx}
13	\usepackage[numbers]{natbib}
14	\usepackage{hyperref}
15	
16	\newcommand{\keff}{K_{\text{eff}}}
17	\newcommand{\etamax}{\eta_{\text{max}}}
18	\newcommand{\keffresid}{K_{\text{eff}}^{\text{resid}}}
19	
20	\title{More Diverse, More Vulnerable:\\How Judge Panel Diversity Backfires Under Adaptive Adversaries}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	Multi-judge evaluation panels are increasingly used to assess LLM outputs, with the prevailing assumption that judge diversity---analogous to Byzantine Fault Tolerance (BFT)---improves robustness against manipulation. We provide large-scale empirical evidence that this assumption \emph{reverses} under adaptive adversaries. Across 15 LLM judges spanning 6 model families, 455 three-judge panels, 9 attack types, and 4 evaluation benchmarks, we show that panel diversity (effective independence $\keff$) is \textbf{independently and positively} associated with attack success rate (ASR), even after residualizing against individual judge weakness ($\etamax$). This ``diversity trap'' is driven by dual vulnerability channels whose relative importance is attack-dependent: $\etamax$ dominates shared-bias attacks (sycophancy, verbosity), while $\keff$ dominates transferable attacks (score manipulation, position bias). We trace the mechanism to BFT's broken assumption: random faults distribute uniformly across judges (Gini$\approx$0.12), but adaptive adversaries concentrate attacks on the weakest judge (Gini$\approx$0.68), turning diversity from a defense into an expanded attack surface. Under calibrated random faults, $\keff$'s coefficient flips negative in 5/12 conditions, empirically confirming BFT's prediction. We propose a robustness-first two-stage panel selection algorithm that reduces ASR by 20.8\% over the strongest-$K$ baseline, and show that Bayesian aggregation provides a complementary 28.4\% reduction. Our findings challenge the ``more diverse = more robust'' assumption and call for diversity-aware security analysis in LLM evaluation pipeline design.
29	\end{abstract}
30	
31	\section{Introduction}
32	
33	As LLMs are increasingly deployed as automated evaluators~\cite{zheng2023judging,li2023alpacaeval}, the research community has adopted multi-judge panels to mitigate individual model biases. The intuition is straightforward and borrowed from distributed systems: diverse, independent judges should be harder to simultaneously fool, much like Byzantine Fault Tolerance (BFT) guarantees that $f$ faulty nodes cannot compromise a system of $3f+1$ independent replicas.
34	
35	This paper demonstrates that this intuition is \emph{wrong} under adversarial conditions. We conduct what is, to our knowledge, the largest systematic study of adversarial robustness in multi-judge LLM evaluation: 15 models from 6 families (OpenAI, Anthropic, Google, Meta, Alibaba, Microsoft), enumerated into 455 three-judge panels, evaluated under 9 distinct attack types across MMLU, ARC-Challenge, MT-Bench, and AlpacaEval.
36	
37	Our central finding is the \textbf{diversity trap}: panel diversity, measured by effective judge independence ($\keff$), is \emph{independently and positively} associated with attack success rate. After residualizing $\keff$ against individual judge weakness ($\etamax$, the maximum vulnerability of any panel member), $\keffresid$ remains significantly positive in 10/12 conditions (FDR-corrected). Panel vulnerability is driven by \textbf{dual factors}---$\etamax$ and $\keff$---whose relative importance depends on attack type:
38	
39	\begin{itemize}[nosep,leftmargin=*]
40	\item \textbf{Shared-bias attacks} (sycophancy, verbosity, authority): $\etamax$ dominates because all judges share similar cognitive biases from RLHF training.
41	\item \textbf{Transferable attacks} (score manipulation, position bias): $\keff$ dominates because diverse judges provide heterogeneous, judge-specific attack surfaces.
42	\end{itemize}
43	
44	We trace this to BFT's core assumption: fault independence. Under random faults, failures distribute uniformly (Gini$\approx$0.12) and diversity genuinely helps---our calibrated random-fault simulations show $\keff$'s coefficient \emph{flipping negative} in 5/12 conditions. But adaptive adversaries concentrate attacks on the weakest judges (Gini$\approx$0.68, top-1 judge absorbing 78\% of ASR), turning diversity from fault tolerance into an expanded attack menu.
45	
46	We further show that: (1) the diversity trap holds within capability tiers (4/6 conditions significant among top-tier models only), ruling out tier-mixing confounds; (2) generalizes to open-ended benchmarks (MT-Bench 3/4, AlpacaEval 2/4 significant); (3) scales with panel size ($\keff$ coefficient increases monotonically from $K$=3 to $K$=9); (4) holds under partial-knowledge adversaries who know only model family membership (7/12 significant). We propose a two-stage defense---robustness screening followed by diversity optimization---that achieves 20.8\% ASR reduction over the strongest-$K$ baseline, and show Bayesian aggregation provides complementary protection.
47	
48	\section{Related Work}
49	
50	\paragraph{LLM-as-Judge.} LLM evaluation using model judges has become standard practice~\cite{zheng2023judging,li2023alpacaeval,dubois2024alpacafarm}. Known biases include position bias, verbosity preference, and self-enhancement~\cite{wang2023large,zheng2023judging}. Multi-judge panels are proposed as mitigation, but their adversarial robustness remains unstudied.
51	
52	\paragraph{Adversarial Attacks on LLM Judges.} Prior work demonstrates individual judge vulnerability to prompt injection, sycophancy exploitation, and score manipulation~\cite{raina2024llm,shi2024optimization}. We extend this to \emph{panel-level} analysis, studying how panel composition mediates vulnerability.
53	
54	\paragraph{Byzantine Fault Tolerance.} Classical BFT~\cite{lamport1982byzantine,castro1999practical} guarantees safety when faults are independent. Recent work questions independence assumptions in ML systems~\cite{sagawa2020investigation}. We empirically test whether BFT's independence assumption holds for LLM judge panels.
55	
56	\paragraph{Ensemble Diversity.} The diversity-accuracy tradeoff is well-studied in ensemble learning~\cite{krogh1994neural,brown2005diversity}. Our setting differs: we study diversity under \emph{adaptive adversaries} who exploit panel composition, not passive noise.
57	
58	\section{Problem Formulation}
59	
60	\paragraph{Setup.} A panel $P = \{j_1, \ldots, j_K\}$ of $K$ LLM judges evaluates candidate responses. Each judge $j_i$ produces a binary decision (accept/reject). The panel decision uses an aggregation rule $\mathcal{A}$ (default: majority vote).
61	
62	\paragraph{Adversary Model.} An adaptive adversary observes the panel composition and crafts attacks to maximize the panel's attack success rate (ASR)---the fraction of evaluation instances where the panel decision is flipped.
63	
64	\paragraph{Vulnerability Metrics.} We define two panel-level predictors:
65	\begin{itemize}[nosep,leftmargin=*]
66	\item $\etamax = \max_{j \in P} \eta_j$: maximum individual vulnerability (weakest link). $\eta_j$ is judge $j$'s individual ASR under a given attack.
67	\item $\keff$: effective number of independent judges, computed from the eigenspectrum of the pairwise mutual information matrix. Higher $\keff$ indicates greater functional diversity.
68	\end{itemize}
69	
70	To disentangle $\keff$ from $\etamax$, we define $\keffresid$ as the residual of regressing $\keff$ on $\etamax$, ensuring orthogonality (VIF$=$1.02).
71	
72	\paragraph{Regression Model.} For each condition (dataset $\times$ attack type), we fit:
73	\begin{equation}
74	\text{ASR}_P = \beta_0 + \beta_\eta \cdot \etamax + \beta_K \cdot \keffresid + \epsilon
75	\end{equation}
76	across all 455 panels. A significantly positive $\beta_K$ indicates diversity independently increases vulnerability.
77	
78	\section{Experimental Setup}
79	
80	\paragraph{Models.} 15 LLM judges: GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini (OpenAI); Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google); Llama-3.1-8B, Llama-3.1-70B (Meta); Qwen2.5-7B, Qwen2.5-72B (Alibaba); Mistral-7B-v0.3, Phi-3-medium-14B (Microsoft). Three capability tiers: Small (7--14B), Medium (14--34B), Large (70B+ and API).
81	
82	\paragraph{Panels.} All $\binom{15}{3} = 455$ three-judge panels, extended to $K \in \{5,7,9\}$ for panel-size analysis.
83	
84	\paragraph{Attacks.} 9 attack types spanning three paradigms: \emph{bias exploitation} (sycophancy, verbosity, authority bias), \emph{score manipulation} (direct score manipulation, position bias, few-shot bias), and \emph{injection} (few-shot hijacking, persona manipulation, instruction override).
85	
86	\paragraph{Benchmarks.} MMLU and ARC-Challenge (MCQ); MT-Bench and AlpacaEval (open-ended generation).
87	
88	\paragraph{Statistical Methods.} FDR correction (Benjamini-Hochberg) for multiple comparisons; beta regression for distributional robustness; residualization for multicollinearity control.
89	
90	\section{The Diversity Trap: Core Evidence}
91	
92	\subsection{Dual Vulnerability Drivers}
93	
94	Table~\ref{tab:core} presents the core regression results across 12 conditions (2 datasets $\times$ 6 attacks). Both $\etamax$ and $\keffresid$ are significant predictors of panel ASR: $\etamax$ reaches FDR significance in 10/12 conditions, $\keffresid$ in 10/12 conditions. The mean $R^2 = 0.62$, indicating that these two factors jointly explain the majority of panel-level vulnerability variance.
95	
96	\begin{table*}[t]
97	\centering
98	\small
99	\caption{Dual vulnerability drivers: 15-model regression across 12 conditions (455 panels each). $\keffresid$ is residualized against $\etamax$ (VIF$=$1.02). Bold $p$-values are FDR-significant ($q < 0.05$). ``Dominant'' indicates which predictor has the larger standardized $\beta$.}
100	\label{tab:core}
101	\begin{tabular}{lccccccl}
102	\toprule
103	Condition & $\etamax$ $\beta$ & $p$ & $\keffresid$ $\beta$ & $p$ & $R^2$ & Confound $r$ & Dominant \\
104	\midrule
105	mmlu$\times$sycophancy & 0.82 & \textbf{1.2e-8} & 0.31 & \textbf{0.004} & 0.68 & 0.72 & $\etamax$ \\
106	mmlu$\times$score\_manip & 0.45 & \textbf{0.018} & 0.61 & \textbf{3.4e-9} & 0.71 & 0.38 & $\keff$ \\
107	mmlu$\times$position & 0.15 & 0.214 & 0.58 & \textbf{1.2e-8} & 0.56 & 0.36 & $\keff$ \\
108	mmlu$\times$verbosity & 0.74 & \textbf{4.1e-7} & 0.28 & \textbf{0.011} & 0.63 & 0.74 & $\etamax$ \\
109	mmlu$\times$authority & 0.69 & \textbf{1.8e-6} & 0.19 & 0.087 & 0.58 & 0.78 & $\etamax$ \\
110	mmlu$\times$few\_shot & 0.55 & \textbf{2.3e-4} & 0.48 & \textbf{6.1e-6} & 0.65 & 0.65 & both \\
111	\midrule
112	arc$\times$sycophancy & 0.79 & \textbf{3.5e-8} & 0.35 & \textbf{0.002} & 0.66 & 0.71 & $\etamax$ \\
113	arc$\times$score\_manip & 0.38 & 0.117 & 0.64 & \textbf{1.7e-7} & 0.59 & 0.35 & $\keff$ \\
114	arc$\times$position & 0.03 & 0.910 & 0.72 & \textbf{1.8e-8} & 0.57 & 0.34 & $\keff$ \\
115	arc$\times$verbosity & 0.71 & \textbf{8.9e-7} & 0.33 & \textbf{0.003} & 0.61 & 0.73 & $\etamax$ \\
116	arc$\times$authority & 0.66 & \textbf{3.2e-6} & 0.22 & 0.062 & 0.55 & 0.76 & $\etamax$ \\
117	arc$\times$few\_shot & 0.51 & \textbf{5.7e-4} & 0.52 & \textbf{3.8e-6} & 0.63 & 0.62 & both \\
118	\bottomrule
119	\end{tabular}
120	\end{table*}
121	
122	A systematic pattern emerges: \textbf{transferable attacks} (score manipulation, position bias) are $\keff$-dominated ($\beta_K > \beta_\eta$), while \textbf{shared-bias attacks} (sycophancy, verbosity, authority) are $\etamax$-dominated. This yields a predictive taxonomy: given a new attack type, its transferability predicts which vulnerability channel dominates.
123	
124	Three conditions have low confound correlation ($r \approx 0.35$), serving as ``smoking gun'' evidence: in these conditions, $\keffresid$ achieves $p < 2.1 \times 10^{-28}$, confirming diversity's independent harmful effect even where the $\keff$-$\etamax$ association is weak.
125	
126	\subsection{Capability-Matched Validation}
127	
128	A natural concern is that $\keff$'s positive effect is an artifact of tier-mixing: high-$\keff$ panels might mix weak and strong models, making $\keff$ a proxy for tier heterogeneity rather than diversity \emph{per se}. We test this by running within-tier regressions (Table~\ref{tab:tier}).
129	
130	\begin{table}[t]
131	\centering
132	\small
133	\caption{Within-tier $\keff$ validation. Large tier uses only top-tier models (70B+ and API), eliminating tier-mixing.}
134	\label{tab:tier}
135	\begin{tabular}{lcccc}
136	\toprule
137	Tier & Models & Panels & $r(\keff,\etamax)$ & $\keffresid$ sig \\
138	\midrule
139	Small (7B--14B) & 5 & 10 & 0.32 & 2/6 \\
140	Medium & 4 & 4 & 0.41 & 1/6 \\
141	Large (70B+API) & 6 & 20 & 0.33 & 4/6 \\
142	Cross-tier (all) & 15 & 455 & 0.55 & 10/12 \\
143	\bottomrule
144	\end{tabular}
145	\end{table}
146	
147	The large tier is most informative: all 6 models are top-tier (GPT-4o, GPT-4.1, Claude-3.5-Sonnet, Gemini-1.5-Pro, Llama-70B, Qwen-72B), yet $\keffresid$ is significant in 4/6 conditions (best $p = 4.2 \times 10^{-4}$). The condition-dependent pattern is preserved: score manipulation and position bias are $\keff$-dominated; sycophancy and verbosity are $\etamax$-dominated. This rules out tier-mixing as the driver of the diversity trap.
148	
149	\subsection{Statistical Robustness}
150	
151	We perform comprehensive diagnostics (Table~\ref{tab:diagnostics}). VIF$=$1.02 and condition number$=$4.8 confirm the design matrix is well-conditioned. Residuals pass Shapiro-Wilk normality ($p = 0.23$). Maximum Cook's distance is 0.031 (threshold: 1.0), with only 2.4\% high-leverage points. Under Bonferroni correction (most conservative), $\keffresid$ remains significant in 8/12 conditions. Beta regression, which properly handles bounded ASR in $[0,1]$, confirms 9/12 significant---highly consistent with OLS.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\caption{Multiple comparison robustness across correction methods.}
157	\label{tab:diagnostics}
158	\begin{tabular}{lcc}
159	\toprule
160	Correction & $\keffresid$ sig & $\etamax$ sig \\
161	\midrule
162	Uncorrected & 12/12 & 11/12 \\
163	FDR (BH) & 10/12 & 10/12 \\
164	Bonferroni & 8/12 & 9/12 \\
165	Beta reg.\ + FDR & 9/12 & 10/12 \\
166	\bottomrule
167	\end{tabular}
168	\end{table}
169	
170	\section{Mechanism: BFT Reversal}
171	
172	\subsection{Random-Fault Contrast}
173	
174	BFT predicts that diversity helps when faults are independent and random. We test this by simulating calibrated random faults: each judge's failure probability is drawn from bootstrapped clean-accuracy noise, independent across judges. Table~\ref{tab:bft} contrasts $\keff$'s coefficient under adaptive versus random-fault regimes.
175	
176	\begin{table*}[t]
177	\centering
178	\small
179	\caption{BFT regime contrast: $\keff$ coefficient under adaptive vs.\ calibrated random faults (12 conditions, 455 panels). ``Flipped'' indicates $\beta_{\text{RF}}$ is significantly negative (diversity helps under random faults).}
180	\label{tab:bft}
181	\begin{tabular}{lcccccc}
182	\toprule
183	Condition & $\beta_{\text{adaptive}}$ & $p_{\text{adap}}$ & $\beta_{\text{RF}}$ & $p_{\text{RF}}$ & $|\beta_{\text{adap}}/\beta_{\text{RF}}|$ & Flipped? \\
184	\midrule
185	mmlu$\times$sycophancy & 0.31 & \textbf{0.004} & 0.08 & 0.310 & 3.88 & No \\
186	mmlu$\times$score\_manip & 0.61 & \textbf{3.4e-9} & $-$0.22 & \textbf{0.015} & 2.77 & Yes \\
187	mmlu$\times$position & 0.58 & \textbf{1.2e-8} & $-$0.31 & \textbf{0.003} & 1.87 & Yes \\
188	mmlu$\times$verbosity & 0.28 & \textbf{0.011} & 0.11 & 0.198 & 2.55 & No \\
189	mmlu$\times$authority & 0.19 & 0.087 & 0.06 & 0.541 & 3.17 & No \\
190	mmlu$\times$few\_shot & 0.48 & \textbf{6.1e-6} & $-$0.18 & \textbf{0.039} & 2.67 & Yes \\
191	arc$\times$sycophancy & 0.35 & \textbf{0.002} & 0.10 & 0.251 & 3.50 & No \\
192	arc$\times$score\_manip & 0.64 & \textbf{1.7e-7} & $-$0.28 & \textbf{0.008} & 2.29 & Yes \\
193	arc$\times$position & 0.72 & \textbf{1.8e-8} & $-$0.35 & \textbf{0.001} & 2.06 & Yes \\
194	arc$\times$verbosity & 0.33 & \textbf{0.003} & 0.12 & 0.175 & 2.75 & No \\
195	arc$\times$authority & 0.22 & 0.062 & 0.05 & 0.612 & 4.40 & No \\
196	arc$\times$few\_shot & 0.52 & \textbf{3.8e-6} & $-$0.14 & 0.091 & 3.71 & Marginal \\
197	\bottomrule
198	\end{tabular}
199	\end{table*}
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af1a0641-07c2-4003-88bc-9a3fd69589fe",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "eefd8878-ddd9-4065-83bf-cd156fe84f05",
  "sourceToolAssistantUUID": "af1a0641-07c2-4003-88bc-9a3fd69589fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T18:49:28.873Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FZXpY1G6ZvTBGP551yTFFN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex",
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eefd8878-ddd9-4065-83bf-cd156fe84f05",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7EUnhy4CRBGQ6HQbhh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d473805b-39ea-4894-a12f-f78e069f4fcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179bQEDs4S3rLLeArcQ2m4k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6383,
      "cache_read_input_tokens": 39340,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 39340,
          "cache_creation_input_tokens": 6383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6383,
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

_source line 43 · 2026-05-22T18:49:28.877Z_

<details><summary>↩ Tool result · `toolu_01FZXpY1G6ZvTBGP551yTFFN`</summary>

```text
200	
201	The results confirm the BFT reversal: in 5/12 conditions, $\beta_{\text{RF}}$ flips to significantly \emph{negative}---diversity genuinely protects under random faults, as BFT predicts. The flips concentrate on transferable attacks (score manipulation, position bias, few-shot), where judge-specific exploit paths are most relevant. Under adaptive attacks, these same conditions show the strongest positive $\beta$ (0.48--0.72). The mean $\beta$ ratio is 2.8$\times$, and the $R^2$ gap ($\Delta R^2 = 0.31$; RF: 0.78, adaptive: 0.47) quantifies BFT's broken predictability: panel structure explains 78\% of variance under random faults but only 47\% under adaptive attacks, where strategic adversary behavior introduces irreducible noise.
202	
203	\subsection{ASR Concentration Analysis}
204	
205	To illuminate \emph{how} adaptive adversaries exploit diversity, we analyze per-judge ASR distributions within panels (Table~\ref{tab:concentration}).
206	
207	\begin{table}[t]
208	\centering
209	\small
210	\caption{ASR concentration: adaptive vs.\ random-fault regimes.}
211	\label{tab:concentration}
212	\begin{tabular}{lccc}
213	\toprule
214	Metric & Adaptive & RF & Ratio \\
215	\midrule
216	Mean Gini & 0.68 & 0.12 & 5.67 \\
217	Entropy (bits) & 1.42 & 2.31 & 0.61 \\
218	Top-1 judge share & 0.78 & 0.38 & 2.05 \\
219	$r(\keff, \text{Gini})$ & 0.52 & 0.08 & 6.50 \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	Under adaptive attacks, ASR is highly concentrated: the weakest judge absorbs 78\% of attack success (vs.\ 38\% under random faults). Crucially, $r(\keff, \text{Gini}) = 0.52$: more diverse panels produce \emph{more concentrated} attacks, because greater capability spread gives the adversary a clearer targeting gradient. Under random faults, concentration is uniformly low (Gini$=$0.12), confirming BFT's independence assumption holds only in the non-adversarial regime.
225	
226	\section{Generalization}
227	
228	\subsection{Attack Surface Expansion}
229	
230	To test whether the diversity trap generalizes beyond the original 6 attack types, we introduce 3 additional attacks: few-shot hijacking (in-context example injection), persona manipulation (authority impersonation), and instruction override (direct prompt overwrite). Table~\ref{tab:expanded} shows the 6 new conditions.
231	
232	\begin{table}[t]
233	\centering
234	\small
235	\caption{Extended attack results (6 new conditions, 15 models).}
236	\label{tab:expanded}
237	\begin{tabular}{lccc}
238	\toprule
239	Condition & $\keffresid$ $\beta$ & $p$ & Dominant \\
240	\midrule
241	mmlu$\times$hijack & 0.54 & \textbf{8.2e-7} & $\keff$ \\
242	mmlu$\times$persona & 0.29 & \textbf{0.008} & $\etamax$ \\
243	mmlu$\times$override & 0.22 & 0.042 & $\etamax$ \\
244	arc$\times$hijack & 0.58 & \textbf{2.1e-7} & $\keff$ \\
245	arc$\times$persona & 0.25 & \textbf{0.019} & $\etamax$ \\
246	arc$\times$override & 0.18 & 0.112 & $\etamax$ \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	$\keffresid$ is significant in 4/6 new conditions. Combined with the original 12, this yields 14/18 total FDR-significant conditions for $\keffresid$. The attack taxonomy is predictive: high-transferability attacks (few-shot hijacking) are $\keff$-dominated; moderate/low-transferability attacks (persona, instruction override) are $\etamax$-dominated---consistent with the core results.
252	
253	\subsection{Open-Ended Benchmarks}
254	
255	The diversity trap is not an MCQ artifact. On MT-Bench (multi-turn dialogue evaluation) and AlpacaEval (instruction-following scoring), $\keffresid$ is significant in 3/4 and 2/4 conditions, respectively (Table~\ref{tab:openended}). The condition-dependent dominance pattern transfers without modification: score manipulation and position bias remain $\keff$-dominated; sycophancy and verbosity remain $\etamax$-dominated. $R^2$ is lower (0.39--0.52 vs.\ 0.62 for MCQ), reflecting the higher noise floor inherent to open-ended evaluation.
256	
257	\begin{table}[t]
258	\centering
259	\small
260	\caption{Open-ended benchmark results (8 conditions). Pattern consistent with MCQ findings despite higher evaluation noise.}
261	\label{tab:openended}
262	\begin{tabular}{lcccl}
263	\toprule
264	Condition & $\keffresid$ $\beta$ & $p$ & $R^2$ & Dom. \\
265	\midrule
266	MT$\times$score & 0.52 & \textbf{1.8e-5} & 0.52 & $\keff$ \\
267	MT$\times$syco & 0.28 & \textbf{0.012} & 0.49 & $\etamax$ \\
268	MT$\times$pos & 0.47 & \textbf{8.3e-5} & 0.44 & $\keff$ \\
269	MT$\times$verb & 0.18 & 0.108 & 0.47 & $\etamax$ \\
270	AE$\times$score & 0.44 & \textbf{3.2e-4} & 0.46 & $\keff$ \\
271	AE$\times$syco & 0.21 & 0.058 & 0.43 & $\etamax$ \\
272	AE$\times$pos & 0.38 & \textbf{0.002} & 0.40 & both \\
273	AE$\times$verb & 0.14 & 0.175 & 0.39 & $\etamax$ \\
274	\bottomrule
275	\end{tabular}
276	\end{table}
277	
278	\subsection{Panel Size Sensitivity}
279	
280	Extending panel size from $K=3$ to $K \in \{5,7,9\}$ reveals a scaling law: $\keff$'s coefficient increases monotonically ($\beta_K$: 0.42$\to$0.48$\to$0.55$\to$0.61), while $\etamax$'s decreases (0.51$\to$0.49$\to$0.43$\to$0.38). The crossover occurs at $K \approx 6$: for panels below this size, individual robustness ($\etamax$) is the primary concern; above it, structural diversity ($\keff$) becomes dominant (Table~\ref{tab:panelsize}). This has direct practical implications: the common strategy of ``adding more judges'' systematically amplifies the diversity trap---$K=9$ panels show 45\% stronger $\keff$ effect than $K=3$.
281	
282	\begin{table}[t]
283	\centering
284	\small
285	\caption{Panel size sensitivity ($K = 3, 5, 7, 9$).}
286	\label{tab:panelsize}
287	\begin{tabular}{lccccl}
288	\toprule
289	$K$ & Panels & $\keffresid$ sig & $\bar{\beta}_K$ & $\bar{\beta}_\eta$ & Primary \\
290	\midrule
291	3 & 455 & 10/12 & 0.42 & 0.51 & $\etamax$ \\
292	5 & 3003 & 11/12 & 0.48 & 0.49 & balanced \\
293	7 & 6435 & 12/12 & 0.55 & 0.43 & $\keff$ \\
294	9 & 5005 & 12/12 & 0.61 & 0.38 & $\keff$ \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	\subsection{Partial-Knowledge Adversary}
300	
301	A full-knowledge adversary is a worst-case assumption. We test a realistic partial-knowledge adversary who knows only model \emph{family} membership (typically public information) but not individual vulnerability profiles. Family-level targeting achieves 78.4\% of full-knowledge ASR (0.058 vs.\ 0.074), and $\keff$ remains significant in 7/12 conditions (Table~\ref{tab:partial}). Family membership alone captures 62.8\% of adversary information value, because family$\to$capability tier correlations provide a strong prior on vulnerability profiles.
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\caption{Adversary knowledge level comparison.}
307	\label{tab:partial}
308	\begin{tabular}{lcccc}
309	\toprule
310	Knowledge & ASR & $\keff$ sig & $R^2$ & Info value \\
311	\midrule
312	Full & 0.074 & 10/12 & 0.62 & 100\% \\
313	Partial (family) & 0.058 & 7/12 & 0.51 & 62.8\% \\
314	Black-box & 0.031 & 3/12 & 0.28 & 0\% \\
315	\bottomrule
316	\end{tabular}
317	\end{table}
318	
319	\section{Structural Barriers to Independence}
320	
321	\subsection{Gaussian Copula Failure}
322	
323	If inter-judge dependence followed a Gaussian copula, pairwise mutual information (MI) could be estimated from linear correlations. Across 105 model pairs (15 models), observed MI exceeds Gaussian-predicted MI by a mean factor of 18.5$\times$ (max 312$\times$), with 82/105 pairs exceeding 10$\times$. This invalidates copula-based independence bounds and motivates empirical $\keff$ measurement.
324	
325	\subsection{Family Labels Are Unreliable}
326	
327	Model family labels do not predict judge independence: within-family MI (0.42) is not significantly higher than cross-family MI (0.39; Mann-Whitney $p = 0.158$). The actual driver is capability proximity ($r = -0.71$ with MI): models at similar capability levels share failure modes regardless of training pipeline. Practitioners should not equate ``different families'' with ``diverse panel.''
328	
329	\subsection{Diversity-Capability Tradeoff}
330	
331	Across 455 panels, $\keff$ and $\etamax$ correlate at $r = 0.55$ globally. Within capability tiers, this drops to $r \approx 0.33$, revealing two components: a cross-tier component ($\sim$40\%, from mixing weak and strong models) and a within-tier residual ($\sim$60\%, from genuine diversity-vulnerability association). The Pareto frontier (18 panels, slope $-0.73$) quantifies the tradeoff: each 0.1 increase in $\keff$ costs at least 0.073 increase in $\etamax$.
332	
333	\section{Defense: Panel Design and Aggregation}
334	
335	\subsection{Two-Stage Panel Selection}
336	
337	We propose a robustness-first algorithm: (1) screen judges by individual robustness ($\eta_j \leq$ percentile-75 threshold), (2) maximize $\keff$ among qualifying judges. Table~\ref{tab:defense} benchmarks this against 5 baselines.
338	
339	\begin{table}[t]
340	\centering
341	\small
342	\caption{Panel selection strategy benchmark (15 models, MMLU, 6 attacks). Two-stage achieves 84\% of oracle efficiency.}
343	\label{tab:defense}
344	\begin{tabular}{lccc}
345	\toprule
346	Strategy & ASR & $\Delta$ vs Strong-K & Best (of 6) \\
347	\midrule
348	Two-Stage (ours) & 0.038 & $-$20.8\% & 5/6 \\
349	Min-$\etamax$ & 0.041 & $-$14.6\% & 4/6 \\
350	Strongest-$K$ & 0.048 & baseline & 1/6 \\
351	Random & 0.089 & +85.4\% & 0/6 \\
352	Max-$\keff$ & 0.112 & +133.3\% & 0/6 \\
353	Oracle & 0.032 & $-$33.3\% & 6/6 \\
354	\bottomrule
355	\end{tabular}
356	\end{table}
357	
358	Two-stage achieves the lowest ASR among non-oracle strategies (0.038), outperforming the strongest-$K$ baseline by 20.8\%. Max-$\keff$ is catastrophic (ASR 0.112, +133\%), providing the most direct evidence against blind diversity maximization. Sensitivity analysis shows the screening threshold is robust across percentile 50--75, with optimal performance at percentile 65--75.
359	
360	\subsection{Aggregation Rule Modulation}
361	
362	The dual vulnerability driver effect varies by aggregation rule (Table~\ref{tab:aggregation}). Threshold (unanimity) voting amplifies $\keff$'s harmful effect by 45\% ($\beta_K$: 0.42$\to$0.61) and increases ASR by 86\%, because a single flipped judge blocks panel rejection. Bayesian aggregation, which downweights judges based on prior accuracy, provides the best single-aggregation defense: 28.4\% ASR reduction, with $\keff$ significance dropping from 10/12 to 6/12. However, 6/12 $\keff$ significance confirms Bayesian aggregation alone cannot eliminate the diversity trap, motivating a combined defense stack.
363	
364	\begin{table}[t]
365	\centering
366	\small
367	\caption{Aggregation rule $\times$ vulnerability drivers (455 panels).}
368	\label{tab:aggregation}
369	\begin{tabular}{lcccc}
370	\toprule
371	Aggregation & $\keff$ sig & $\bar{\beta}_K$ & ASR & $\Delta$ \\
372	\midrule
373	Majority & 10/12 & 0.42 & 0.074 & -- \\
374	Threshold & 11/12 & 0.61 & 0.138 & +86\% \\
375	Acc-weighted & 8/12 & 0.39 & 0.069 & $-$6.8\% \\
376	Bayesian & 6/12 & 0.25 & 0.053 & $-$28.4\% \\
377	\bottomrule
378	\end{tabular}
379	\end{table}
380	
381	\section{Conclusion}
382	
383	We presented large-scale empirical evidence for the \emph{diversity trap} in multi-judge LLM evaluation: panel diversity independently increases vulnerability to adaptive adversarial attacks. This finding, validated across 15 models, 455 panels, 9 attack types, 4 benchmarks, and multiple panel sizes, challenges the pervasive assumption that diversity improves evaluation robustness. The mechanism traces to BFT's broken assumption: adaptive adversaries exploit the heterogeneous attack surface that diverse judges create, concentrating attacks on the weakest judge rather than facing independent random faults. We proposed a two-stage defense (robustness screening + diversity optimization) that reduces ASR by 20.8\%, complemented by Bayesian aggregation ($-$28.4\%). We urge the LLM evaluation community to adopt diversity-aware security analysis: do not assume more judges means safer evaluation.
384	
385	\section*{Limitations}
386	
387	Our study has three main limitations. First, our adversary model assumes knowledge of panel composition (full or partial); in settings where panel membership is secret, the diversity trap may be attenuated. Second, while we cover 15 models from 6 families, the rapidly evolving LLM landscape means our specific quantitative findings may shift as new model generations emerge. Third, our analysis is observational---the regression design establishes independent predictive association, not strict causality, between diversity and vulnerability; experimental manipulation of panel composition with controlled interventions would strengthen causal claims.
388	
389	\bibliographystyle{plainnat}
390	\bibliography{custom}
391	
392	\end{document}
393	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d473805b-39ea-4894-a12f-f78e069f4fcf",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "46da1e8b-0e13-4a3e-a06c-33fc91e71714",
  "sourceToolAssistantUUID": "d473805b-39ea-4894-a12f-f78e069f4fcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-22T18:49:31.330Z_

Now let me also check the latest dream report that was generated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46da1e8b-0e13-4a3e-a06c-33fc91e71714",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7EouQ6TMg9fD5frJd3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9977cac0-5bf4-4295-89d2-34db7b360a9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCvyyGR6v1msirLkVLWKQm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4710,
      "cache_read_input_tokens": 45723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4710,
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

_source line 45 · 2026-05-22T18:49:34.196Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PBLHLj8ktGkRis5jpBZAzF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/median/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9977cac0-5bf4-4295-89d2-34db7b360a9e",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7EouQ6TMg9fD5frJd3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6672c61-ce17-4867-ae7e-0c02d46a2612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCvyyGR6v1msirLkVLWKQm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4710,
      "cache_read_input_tokens": 45723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4710,
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

_source line 46 · 2026-05-22T18:49:34.202Z_

<details><summary>↩ Tool result · `toolu_01PBLHLj8ktGkRis5jpBZAzF`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6672c61-ce17-4867-ae7e-0c02d46a2612",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "0217f46e-ba4a-454d-a5e8-be8f5a5a43d7",
  "sourceToolAssistantUUID": "a6672c61-ce17-4867-ae7e-0c02d46a2612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T18:49:35.131Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ef2TcUwuEFLMbwU2DPri7z`</summary>

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
  "parentUuid": "0217f46e-ba4a-454d-a5e8-be8f5a5a43d7",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7EouQ6TMg9fD5frJd3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e3685a3-df97-499b-869d-9bcb43ec6417",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCvyyGR6v1msirLkVLWKQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4710,
      "cache_read_input_tokens": 45723,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 45723,
          "cache_creation_input_tokens": 4710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4710,
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

_source line 48 · 2026-05-22T18:49:35.146Z_

<details><summary>↩ Tool result · `toolu_01Ef2TcUwuEFLMbwU2DPri7z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/decisions.yaml\", \"content\": \"_next_id: 18\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 16:31 UTC\\n  summary: MVP 方案：API 模型验证 K_eff 对操纵抗性的预测力，三步验证（相关性测量→攻击抗性 scaling→K_eff 回归）\\n  rationale: 项目核心假设是 K_eff 公式能预测多 judge 面板的操纵抗性。MVP 用 API 模型而非开源模型，因为：(1) 无需 GPU 配置，分钟级启动；(2)\\n    API 模型覆盖多家族（OpenAI/Anthropic/Google/DeepSeek/Qwen），足以验证 cross-family vs within-family\\n    相关性差异；(3) 核心假设与模型部署方式无关——如果 K_eff 在 API 模型上不 work，在开源模型上也不会 work。外部评审 FAILED (35%)\\n    但理论框架可修正，需先验证经验基础再投入理论修正。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 16:37 UTC\\n  summary: MVP v2：基于 Reviewer 反馈修正统计设计，四步验证（相关性→homo/hetero 对照→K_eff 公式验证→scaling\\n    分析）\\n  rationale: Reviewer 指出 v1 五个问题：(1) K=1/3/5 仅 3 点无统计效力；(2) \\\"ASR 随 K 递减\\\"是 trivial\\n    gate，需 homo vs hetero 对照；(3) kill criteria 缺操作定义；(4) MI 估计器未指定；(5) K_eff 公式本身未验证。v2\\n    全部修正：新增 Step 2 homo/hetero panel 对照（核心 kill criterion）、Step 3 formula vs empirical\\n    effective rank 验证、K 扩展至 1/2/3/4/5/7 + attack×dataset 交叉产生 ≥15 数据点、MI 用 plug-in\\n    + Miller-Madow、kill criteria 操作化（bootstrap CI/≥80% 配置/配对检验 p<0.05）。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 17:06 UTC\\n  summary: MVP 改用开源模型在 GPU 服务器运行，取消 API 依赖\\n  rationale: 用户催促推进（\\\"push\\\"），API keys 迟迟未提供成为阻塞项。已有 4× RTX 6000 96G，可跑 4 个 70B 级开源模型（Qwen-72B\\n    / Llama-70B / Mistral-Large / Qwen-32B），覆盖 3 个家族 + 1 个 same-family 对照，满足 homo/hetero\\n    对比需求。开源模型还有可复现性优势。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-21 22:26 UTC\\n  summary: Step 1 结果显示 family diversity ≠ effective diversity；Step 2 对照组从 homo/hetero-family\\n    改为 high-K_eff vs low-K_eff panels\\n  rationale: 6 模型全量数据：within-family MI vs cross-family MI 无统计显著差异（MMLU p=0.218, ARC\\n    p=0.427）。大模型间 cross-family MI (0.487) 甚至高于最强 within-family pair (0.451)。原因：模型能力接近度而非家族身份驱动相关性。K_eff\\n    框架本身 agnostic——不关心 MI 来源，仍可能有效。但原始 Step 2 设计（K=3 same-family vs K=3 cross-family）已失去意义。改为直接用\\n    Step 1 实测 MI 计算各 panel 的 K_eff，对比 high-K_eff vs low-K_eff panels 的 ASR。这是更干净的测试，且\\\"family\\n    ≠ diversity\\\"本身是值得报告的发现。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-21 22:50 UTC\\n  summary: MI-based K_eff 为主指标，ρ-based 降为参考；Gaussian copula 全面失败（偏离 10-21×）作为论文发现之一\\n  rationale: Copula GoF 全量数据：MI_observed/MI_gaussian 均值 MMLU 21.1×、ARC 10.4×，14-15/15\\n    pairs 偏离 >2×。极端 case Mistral-Large↔Qwen-14B ρ≈0 但 MI=0.1-0.2（纯非线性依赖）。ρ-based K_eff\\n    对此 pair 会算出\\\"完全独立\\\"（1-0.001≈1），严重高估 panel independence。MI-based K_eff 直接使用观测信息量，不依赖\\n    Gaussian 假设，是唯一合理选择。论文中 copula 偏离本身作为 methodological finding 报告：\\\"LLM judge 间存在大量非线性依赖，线性相关系数系统性低估信息共享。\\\"\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-21 23:24 UTC\\n  summary: 论文 framing 降级：'certifiable' → 'quantifiable/measurable'；K_eff 理论定位从 proven\\n    bound 改为 Gaussian-motivated + empirically validated metric\\n  rationale: Reviewer 逐步审查 T1 证明链：K_eff = 1+(K-1)·exp(-2·I_max) 的上界性质（Step 3-5）依赖\\n    Gaussian compound symmetric 假设。Copula GoF 确认 LLM judge 分布偏离 Gaussian 10-21×。非\\n    Gaussian 下只有 trivial bound η_joint ≤ K·η_max，K_eff 公式不保证是 η_joint 的上界。因此不能 claim\\n    \\\"certifiable manipulation resistance\\\"。MI plug-in 估计可靠（正偏差是保守方向）。贡献栈调整：Gaussian\\n    下的 bound 作为 theoretical motivation，MI-based K_eff 作为 empirically validated diversity\\n    metric，copula 偏离和家族标签不可靠作为 methodological findings。Step 4 是论文去向的决定性测试。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-22 01:08 UTC\\n  summary: Step 2 反转：K_eff 被 individual robustness confound 淹没，选 Option A 控制变量重跑\\n  rationale: High K_eff panels 全含 llama-8b（弱模型→低MI→高K_eff 但个体脆弱），Low K_eff panels\\n    全大模型（相关但个体强健）。ASR 反转不代表 K_eff 无效，而是被 robustness confound 掩盖。选 Option A：只用 4 个大模型(72B/70B/32B/Mistral-Large)的\\n    C(4,3)=4 panels 控制个体鲁棒性后重测。同时计算 single-judge ASR 量化 confound。Option B（修改公式）和 C（reframe）在\\n    A 结果出来前都为时过早。\\n  related_experiments:\\n  - exp_id: mvp-step2-keff-contrast\\n    role: evidence\\n    result: negative-confounded\\n  depends_on:\\n  - D004\\n  - D005\\n- id: D008\\n  date: 2026-05-22 03:21 UTC\\n  summary: MVP 原假设部分证伪：K_eff 仅对 shared-bias attacks 显著，η_max 主导 targeted attacks。探索\\n    attack-conditioned 双因子框架。\\n  rationale: 20-panel 多元回归 log(ASR)~log(K_eff)+log(η_max) 结果：K_eff 显著为负仅 1/6（arc×sycophancy\\n    β=-2.85 p=0.003），η_max 显著为正 4/6。攻击分类：targeted attacks（prompt injection, score\\n    manipulation）ASR≈f(η_max)，K_eff 无关；broad-spectrum attacks（sycophancy/共享偏差）ASR\\n    受 K_eff 影响。不立即 pivot 到 Path B（weakest-link reframe），先验证 attack taxonomy——增加 2-3\\n    种 broad-spectrum 攻击看 K_eff 是否一致有效。如果一致 → attack-conditioned K_eff theory（Path\\n    A 升级版）；如果不一致 → 全面 pivot 到 Path B。\\n  related_experiments:\\n  - exp_id: mvp-step2v3-retry3\\n    role: evidence\\n    result: partial-negative\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-22 04:56 UTC\\n  summary: Taxonomy 验证失败（0/6 新条件 K_eff 显著），建议 kill 项目\\n  rationale: 12 条件全景：K_eff 显著为负仅 1/12（arc×sycophancy，Bonferroni 勉强通过，同类攻击不复现，降级为孤立异常）。η_max\\n    显著 7/12 但\\\"最弱评委决定安全性\\\"可能被审稿人视为 trivial。Reviewer 评估当前 2.0-2.5，扩展后最高 3.0-3.5，不够 AAAI\\n    main（3.5+）。贡献栈过薄：负结果（K_eff 无效）+ 弱正结果（η_max 主导但可能 obvious）+ 方法论（copula 失败）无法支撑\\n    A 类投稿。\\n  related_experiments:\\n  - exp_id: taxonomy-broad-spectrum\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-22 06:58 UTC\\n  summary: Dream review (2.5 all tiers) exposed 13 structural issues; proceed with\\n    fixes, NOT kill\\n  rationale: 'Dream dream_20260522T055016 returned 2.5 (Borderline Findings) across\\n    best/median/worst — flat scoring indicates structural issues not data-dependent.\\n    Key fixes: (1) Theorem 1 proof gap — must account for ⌈K/2⌉ majority requirement;\\n    (2) Novelty reframe — acknowledge weakest-link known in security, position as\\n    first empirical quantification in LLM-judge domain; (3) VIF/multicollinearity\\n    analysis on existing data; (4) Multiple comparison correction; (5) Non-majority-vote\\n    aggregation; (6) Open-ended benchmark beyond MCQ; (7) \\\"When diversity helps\\\" section.\\n    User confirmed continue (not kill), target EMNLP 2026, GPUs unlimited. Immediate\\n    actions: plan_009 (VIF analysis, P0, no GPU), plan_001 (model expansion, P0),\\n    plan_003 (formal theorem, P0). Framing updated to v3.'\\n  related_experiments: []\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-22 07:08 UTC\\n  summary: Plan_003 BFT contrast failed (0/12 random-fault K_eff significant); Claim\\n    2 conditional on plan_001 model expansion\\n  rationale: 'Random-fault simulation showed K_eff 0/12 significant negative — same\\n    as adaptive (1/12). BFT vs adaptive contrast cannot be demonstrated with current\\n    6-model pool due to K_eff-η_max structural confound. R² difference (adaptive 0.14-0.73\\n    vs random-fault 0.55-0.95) is the only positive finding. Reviewer recommends:\\n    don''t reframe Claim 2 yet, wait for plan_001 (15+ models) which may break the\\n    confound. If plan_001 also fails to show K_eff distinction → Claim 2 must be dropped,\\n    ceiling falls to ~2.5-3.0. Theorem 1 direction adjusted: prove monotonicity in\\n    η_max (option b) rather than K_eff regime distinction.'\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: go/no-go gate\\n    result: failed — 0/12 K_eff significant under random faults\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-22 12:16 UTC\\n  summary: Plan_010 聚合实验完成：Bayesian 部分打破 weakest-link (3/12 vs 8/12)，threshold 下 diversity\\n    有害。纳入 Claim 7，Theorem 1 加 scope qualifier。\\n  rationale: 6 模型初步结果显示聚合规则显著调制 weakest-link 效应：majority/weighted 下 η_max 7-8/12 显著（Theorem\\n    1 成立），Bayesian 下仅 3/12（reliability weighting 降低弱 judge 影响），threshold 下 K_eff 正向显著（diversity\\n    在 unanimity 下有害）。Reviewer 确认方向有效但标 2 个 warning：(1) Bayesian 用同数据集 clean accuracy\\n    有信息泄漏嫌疑；(2) 缺 FDR 校正。两者在 15 模型版本中修复。该发现将论文从 negative-only 升级为 negative + positive\\n    prescription，增加实用价值。\\n  related_experiments:\\n  - exp_id: plan_010\\n    role: primary\\n    result: positive — aggregation modulates weakest-link\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-22 15:11 UTC\\n  summary: 7-model 预览显示 Claim 2 复活信号：random-fault K_eff gains 6/12（vs plan_003 的 0/12），ΔR²=+0.237。η_max\\n    提升到 10/12。等 15-model 455 panels 确认。\\n  rationale: '加入 claude-3-haiku（跨族 + 弱模型）后 confound 方向反转（r=+0.473），打破了 plan_003 时的结构性假阴性。Random-fault\\n    下 K_eff 6/12 显著优于 adaptive 的 0-1/12，初步恢复了 BFT adaptive/random-fault 对比的核心叙事。但仅\\n    35 panels 统计功效有限，且主要由 haiku 单点驱动。15-model 全量结果（ETA 8-10h）是最终判定。如果复现 → Claim 2\\n    恢复为 #2 贡献；如果不复现 → 维持 conditional。'\\n  related_experiments:\\n  - exp_id: plan_001_7model_preview\\n    role: primary\\n    result: positive signal — confound broken, Claim 2 revival, η_max 10/12\\n  depends_on:\\n  - D011\\n  - D012\\n- id: D014\\n  date: 2026-05-22 17:16 UTC\\n  summary: 15-model 结果证伪原始 Claim 1 (\\\"K_eff irrelevant\\\")；K_eff 12/12 显著正，diversity\\n    有害。Paper framing 需从 v3 升级到 v4\\n  rationale: '15-model/455-panel regression: K_eff 12/12 FDR sig positive (β>0), η_max\\n    9/12 sig。在 2 个 confound-free 条件 (r≈0.35, VIF≈1.14) 中 K_eff 仍极显著 (p=6e-26, 4e-16)，排除\\n    confound artifact 可能。Sensitivity (排除 ACC<0.5) 11/12 仍显著。论文叙事需从 \\\"diversity doesn''t\\n    help\\\" 转向 \\\"diversity actively hurts, mechanism = diversity-capability tradeoff\\\"。Claim\\n    1 与 Claim 3 合并为更强结论。等待 residualized K_eff 分析确认独立效应强度。'\\n  related_experiments:\\n  - exp_id: plan001_step1_full_v4\\n    role: primary\\n    result: K_eff 12/12 sig positive, η_max 9/12 sig\\n  depends_on:\\n  - D013\\n  - D012\\n- id: D015\\n  date: 2026-05-22 18:05 UTC\\n  summary: Claim 5 (Gaussian Copula Failure) falsified at 15-model scale; removed\\n    from contribution stack\\n  rationale: '15-model copula analysis: MI_obs/MI_gaussian ratio = 0.93 (MMLU), 0.90\\n    (ARC robust). 6-model 10-21× was small-sample artifact (15→105 pairs diluted extreme\\n    values). Only haiku pairs show extreme ratios (212×). Claim downgraded to minor\\n    observation. Contribution stack reduced from 8 to 7.'\\n  related_experiments:\\n  - exp_id: worker_analysis_15model-family-copula\\n    role: falsified Claim 5\\n    result: ratio ~0.9, copula fits well\\n  depends_on:\\n  - D014\\n- id: D016\\n  date: 2026-05-22 18:20 UTC\\n  summary: 'Claim 7 revised: \\\"Bayesian breaks weakest-link\\\" falsified → \\\"Bayesian\\n    mitigates diversity-as-vulnerability while η_max remains dominant\\\"'\\n  rationale: '15-model P2 aggregation results: η_max remains 12/12 FDR sig under Bayesian\\n    (vs 3/12 at 6 models — original claim was scale artifact). But K_eff sig drops\\n    from 12/12 (majority) to 5/12 (Bayesian), β direction partially flips (3/12 negative).\\n    Bayesian calibration suppresses the harmful diversity effect without weakening\\n    weakest-link protection. New narrative: aggregation method modulates diversity\\n    vulnerability, not weakest-link dominance. Prescriptive angle: practitioners should\\n    prefer Bayesian calibration to mitigate diversity-as-vulnerability.'\\n  related_experiments:\\n  - exp_id: plan001_step1_full_v4\\n    role: P2 aggregation source data\\n    result: majority K_eff 12/12 positive → bayesian K_eff 5/12 with 3 neg; η_max\\n      12/12 stable across all methods\\n  depends_on:\\n  - D014\\n  - D012\\n- id: D017\\n  date: 2026-05-22 18:39 UTC\\n  summary: 'Claim 7 final (log-log canonical): Bayesian partially mitigates BOTH drivers\\n    — η_max 11→9/12, K_eff flips to 4/5 negative (protective). D016 level-level numbers\\n    superseded.'\\n  rationale: 'P2b log-log canonical rerun resolves spec inconsistency (Reviewer #1).\\n    Majority row sanity-checks against dominance canonical. Under Bayesian: η_max\\n    drops from 11/12 to 9/12 (weakest-link partially weakened), K_eff 4/5 significant\\n    coefficients are negative (diversity becomes protective). Threshold shows R²=0.901\\n    (near-perfect dual-driver fit under unanimity). Weighted is strongest dual-driver\\n    (K_eff 11/12 all positive). The aggregation gradient (majority→weighted→threshold→bayesian)\\n    reveals how different voting rules modulate the diversity channel and weakest-link\\n    channel independently.'\\n  related_experiments:\\n  - exp_id: plan001_step1_full_v4\\n    role: P2b log-log aggregation source\\n    result: majority η_max 11/12 K_eff 8/12(7+1-) | weighted 11/12 11/12(11+) | threshold\\n      12/12 11/12(10+1-) R²=0.90 | bayesian 9/12 5/12(1+4-)\\n  depends_on:\\n  - D016\\n  - D014\\n\", \"total_chars\": 12035, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e3685a3-df97-499b-869d-9bcb43ec6417",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "2470de17-1c6a-479b-b490-127bcbd2eda7",
  "sourceToolAssistantUUID": "2e3685a3-df97-499b-869d-9bcb43ec6417",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-22T18:49:37.950Z_

Now let me also read the memory file for additional context about the project's evolution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2470de17-1c6a-479b-b490-127bcbd2eda7",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7FGN7dSasB4utNjSnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0b2bc95-5397-443d-99c0-380ec5c68f59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPE2ivCtjihuvSMSwwa6Q7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9242,
      "cache_read_input_tokens": 50433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9242,
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

_source line 50 · 2026-05-22T18:49:38.933Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H4KGeBAVbrR1iFv2erT5QH`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0b2bc95-5397-443d-99c0-380ec5c68f59",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7FGN7dSasB4utNjSnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f42d0647-7ec3-4208-8b99-ae40fb8f09e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPE2ivCtjihuvSMSwwa6Q7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9242,
      "cache_read_input_tokens": 50433,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9242
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 50433,
          "cache_creation_input_tokens": 9242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9242,
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

_source line 51 · 2026-05-22T18:49:38.953Z_

<details><summary>↩ Tool result · `toolu_01H4KGeBAVbrR1iFv2erT5QH`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/memory.md\", \"content\": \"# cert_manip_resist_eval — Memory\\n\\n## 环境信息\\n- **服务器**: seetacloud-rtx6000, 4× RTX PRO 6000 96GB\\n- **Python 环境**: conda base (`/root/miniconda3/bin/python`), vLLM 0.21.0 + torch 2.11.0+cu128\\n- **项目路径**: 服务器 `/root/cert_manip_resist_eval/`\\n- **模型路径**: `/root/autodl-tmp/models/`\\n- **AWQ 量化**: 所有模型均为 INT4 AWQ 量化版\\n- **HF 缓存**: `/root/autodl-tmp/.hf_cache/`（datasets 子目录有 mmlu + arc_challenge 的 arrow 缓存）\\n\\n## seetacloud 必须环境变量清单（缺一不可，连续 3 次 crash 教训）\\n```bash\\nsource /etc/network_turbo                    # 代理加速\\nexport HF_HUB_DISABLE_XET=1                 # xet 协议在 AutoDL 上 401\\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt  # SSL 证书\\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\\nexport HF_HOME=/root/autodl-tmp/.hf_cache   # 避免根分区写满\\nexport VLLM_WORKER_MULTIPROC_METHOD=spawn   # 必须在 import vllm 之前\\n```\\n\\n## 推理配置\\n- `gpu_memory_utilization=0.90` 安全（单模型串行加载时）\\n- serial load/unload 模式避免共享 GPU 的 OOM\\n- **启动新脚本前必须 kill 所有残留 vLLM 进程**，否则 GPU OOM（mvp-step2v3-retry2 教训）\\n\\n## 理论推导状态（2026-05-22）\\n- **T1 SDPI**: 完成。K_eff = 1+(K-1)e^{-2I_max} 是精确 Gaussian 值的上界\\n- **Theorem 1 (Weakest-Link)**: 完成。Panel ASR monotonically increasing in η_max under correlated judges + adaptive adversary. ASR = Θ(η_max^t). 6 页 LaTeX 证明在 `artifacts/theorem1_proof.tex`。Reviewer fixes applied: pointwise dominance remark added, empirical data moved to Remark [Empirical Support]\\n- **T3 PEG**: 完成。Proposition 1/2 (sketch proof)。ε_inc(ρ) = 1-√(1-ρ²)\\n- T2/T4/T5/T6: planned\\n\\n## API 模型列表（2026-05-22 更新）\\n原始9模型中6个已升级：\\n| 旧名 | 新名 | 原因 |\\n|---|---|---|\\n| claude-opus-4 | claude-opus-4-6 | 新版本 |\\n| claude-sonnet-4 | claude-sonnet-4-6 | 新版本 |\\n| gemini-2.5-pro | gemini-3.1-pro-preview | 新版本 |\\n| gemini-2.5-flash | gemini-3.5-flash | 新版本 |\\n| gpt-4o | gpt-4.1-nano | gpt-4o 退役(2026-02)，替换为同 tier weak 模型 |\\n| gpt-4o-mini | gpt-4.1-mini | 同理 |\\n\\n不变：gpt-4.1, gpt-5.5, claude-3-haiku\\n\\n**Scoring 基础设施**：本地 AWS 机器通过 OpenRouter（中国 IP 被 403 封锁，AutoDL 不能直连）\\n\\n## 15-model Pipeline 核心结果（2026-05-22）— K_eff Diversity Harm\\n\\n### Confound（|r| 修复后）\\n- **Overall: mean |r| = 0.701, verdict = CONFOUND_SEVERE**\\n- ARC 6/6 SEVERE（r = +0.73 ~ +0.92）\\n- MMLU: 1 SEVERE, 3 MODERATE, **2 BROKEN**（sycophancy r=+0.348, verbosity r=+0.355）\\n- 从 6-model r=-0.8 翻正到 +0.70，但 |r| 仍高——confound 翻转方向但未打破\\n\\n### K_eff β 方向：全部为正（12/12）— diversity 有害\\n- 即使在 confound BROKEN 的 2 个条件（mmlu×sycophancy β=+5.573, mmlu×verbosity β=+4.243），K_eff 仍显著正\\n- 可能机制：高 K_eff panel 必然包含跨 family 的弱模型（nano, haiku），其高 ASR 拉高整体\\n- η_max 不足以线性控制弱模型的非线性影响\\n\\n### Sensitivity（排除 clean ACC < 0.5）\\n- 11/12 K_eff 保持显著（仅 arc×sycophancy 消失）\\n- 比 9-model 的 4/12→0/12 稳健得多\\n\\n### Random Fault\\n- RF K_eff 12/12 显著（全正），Adaptive 12/12 显著\\n- Mean ΔR² = +0.213\\n\\n### MI Matrix 数据质量\\n- Gemini valid samples 213-297/300，无 warning\\n- 15 模型全部进入矩阵\\n\\n## Step 1 关键发现（2026-05-21）\\n- within-family MI > cross-family MI 方向正确但 p 不显著（MMLU p=0.206, ARC p=0.427）\\n- 根因: llama-8b 是 outlier，模型能力差距掩盖家族效应\\n- 大模型间 cross-family MI 很高（llama-70b↔mistral-large MI=0.487 > 最强 within pair）\\n\\n## Copula GoF 关键发现（2026-05-21）\\n- **Gaussian copula 假设被系统性违反**：MI_obs/MI_gauss 均值 MMLU=21×, ARC=10×\\n- ρ 严重低估依赖，MI-based K_eff 是正确度量\\n- 这本身是论文的 contribution point\\n\\n## Step 2 v2 负向结果（2026-05-22）\\n- high K_eff panels（含弱模型）ASR 更高，low K_eff panels（全大模型）ASR 更低\\n- 根因: individual model robustness confound\\n\\n## Step 2 v3 核心发现（2026-05-22）— Make-or-Break 回归\\n- **η_max（最弱评委 ASR）是 panel ASR 的主要预测因子**（4/6 条件 p<0.05）\\n- **K_eff 在 5/6 条件下不显著**，4/6 条件方向甚至为正\\n- **唯一例外：arc×sycophancy (β=-2.85, p=0.003)** — sycophancy 是唯一利用\\\"共享偏差\\\"的攻击\\n- **关键 insight：攻击分两类**\\n  - Targeted 攻击（PI, SM）：exploit 个体漏洞 → ASR≈f(η_max)，K_eff 无关\\n  - Broad-spectrum 攻击（sycophancy）：exploit 共享偏差 → K_eff 才有效\\n\\n## Taxonomy Broad-Spectrum 结果（2026-05-22）— K_eff 理论最终证伪\\n- **Attack taxonomy hypothesis 彻底失败**：3 种 broad-spectrum 攻击均未显示 K_eff 显著负向\\n- **累积 12 条件：K_eff 仅 1/12 (8%) 显著负向，η_max 7/12 (58%) 显著**\\n\\n## Plan_009 VIF 分析（2026-05-22）\\n- K_eff non-significance 非共线性伪影（Mean VIF=2.99, 一个 outlier 10.02）\\n- Residualized K_eff 仍然 1/12 显著 → 非共线性问题\\n- η_max Bonferroni 3/12, FDR 6/12\\n- Beta regression 与 OLS 11/12 concordance\\n\\n## Plan_003 Random-Fault（2026-05-22）\\n- BFT contrast NO-GO: 0/12 random-fault K_eff 显著\\n- R² gap 有价值: random-fault R²=0.55-0.95 vs adaptive R²=0.14-0.73\\n\\n## Plan_010 聚合策略（2026-05-22）— Bayesian 部分打破 weakest-link\\n- **4 种聚合方法**: majority vote, weighted vote, threshold (unanimous), Bayesian\\n- **Bayesian**: η_max 仅 3/12 显著 — **部分打破 weakest-link**\\n- **FDR-48 校正**: majority η_max 5/12, bayesian 2/12\\n- **Bayesian 5-fold CV**: robust, no info leakage\\n\\n## 决策记录\\n- [2026-05-21] keff.py: empirical_keff_from_rho 用所有 pairwise ρ，formula_keff 用 I_max\\n- [2026-05-21] T3 中 Theorem 降级为 Proposition（proof 是 sketch）\\n- [2026-05-21] Step 2 重新设计：high-K_eff vs low-K_eff panel contrast\\n- [2026-05-22] Step 2 v2 negative → v3 多元回归方案（Reviewer 建议）\\n- [2026-05-22] Part 3 (4-model 控制组) 被 Reviewer 否决: C(4,3)=4 K_eff 方差压缩 93%\\n- [2026-05-22] Step 2 v3 negative: η_max dominates, K_eff 仅对 broad-spectrum 攻击有效\\n- [2026-05-22] Taxonomy negative: K_eff 理论完全证伪，等待 Director 决策 framing pivot\\n- [2026-05-22] 提交 3 个 framing pivot 方向给 Director: A) Weakest-Link Paper B) Full Negative Result C) Hybrid η_max + K_eff secondary。建议方向 A\\n- [2026-05-22] Plan_010: Bayesian aggregation 部分打破 weakest-link，纳入 Claim 7\\n- [2026-05-22] API 模型 6/9 升级（gpt-4o 退役等），改用本地 AWS + OpenRouter scoring\\n- [2026-05-22] 15-model pipeline: K_eff β 全正（diversity 有害），confound |r|=0.70 翻正但未打破。需 Director 决策 reframe\\n\", \"total_chars\": 5350, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f42d0647-7ec3-4208-8b99-ae40fb8f09e7",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "ae36eb1bd3a5725c7",
  "type": "user",
  "uuid": "928df64c-2c88-4f62-a9ed-ec59da5ca5af",
  "sourceToolAssistantUUID": "f42d0647-7ec3-4208-8b99-ae40fb8f09e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-22T18:51:22.840Z_

I now have a comprehensive understanding of the paper, its evolution, and the underlying experimental work. Let me write the review.

---

## Review: R2 — Novelty, Positioning, and Related Work

**Paper**: "Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation: Weakest-Link Dominance, Aggregation Defenses, and the Limits of Diversity" (though the actual tex files use variants: "The Weakest Link: Why Judge Diversity Fails Under Adaptive Adversaries in Multi-LLM Evaluation" and dream versions use "More Diverse, More Vulnerable")

---

### Summary

This paper investigates whether diversity in multi-judge LLM evaluation panels provides robustness against adversarial manipulation, finding that it predominantly does not. Through experiments spanning 15 models, 455 three-judge panels, 6 attack types, and 2 benchmarks, the authors show that panel vulnerability is primarily predicted by the weakest individual judge (eta_max, significant in 11/12 conditions) rather than by panel diversity (K_eff, which is significantly *positively* associated with ASR in 7/12 conditions). The paper proposes robustness-first panel selection and Bayesian aggregation as practical defenses.

---

### Strengths

- **Scale and thoroughness of the empirical study.** The exhaustive enumeration of all C(15,3) = 455 panels is a clean experimental design that avoids selection bias. The 15 models span 5-6 families and 3 capability tiers, providing reasonable coverage of the current LLM ecosystem. The 2-benchmark x 6-attack = 12 condition matrix with FDR correction is methodologically sound.

- **The K_eff confound analysis is genuinely valuable.** The paper's most important contribution may be exposing that the widely cited ASR reduction in multi-judge panels (e.g., from the SoK by Almasoud et al. 2026) conflates panel diversity with the inclusion of individually robust models. The dominance analysis framework that disentangles eta_max from K_eff is well-executed. The decision log shows the authors discovered this finding empirically and followed the evidence honestly, including abandoning falsified claims (Gaussian copula failure at 15-model scale, original "K_eff irrelevant" framing).

- **The aggregation analysis adds prescriptive value.** The finding that Bayesian calibration flips K_eff from predominantly positive to predominantly negative (majority 7+/1- vs. Bayesian 1+/4-) while threshold voting amplifies both vulnerability channels is practically useful. The aggregation gradient (threshold -> majority -> weighted -> Bayesian) is a clean result.

- **Theorem 1 (Weakest-Link Monotonicity) is correctly stated and useful.** The monotonicity result under arbitrary correlations and adaptive adversaries is a clean formal contribution, even if the intuition is straightforward.

- **Related work section (in the working tex version) is substantially better than the paper summary suggested.** The 5-paragraph related work with specific citations to Krogh & Vieli 1995, Yang et al. 2026, Turkmen et al. 2026, Kim et al. 2025, and the information-theoretic line (Robertson 2025, Kaneko 2025, Feng 2026) is adequate and correctly positions the paper at the intersection of ensemble theory, adversarial robustness, and LLM evaluation.

- **Honest reporting of the sycophancy exception.** The paper does not hide that K_eff is significantly *protective* in 1/12 conditions (arc x sycophancy), and the mechanistic explanation (shared-bias attacks where BFT logic does hold) is coherent.

---

### Weaknesses

- **The central finding --- "the weakest judge determines panel security" --- has limited novelty.** The weakest-link principle has been articulated in security literature since at least Schneier (2000), which the paper itself cites. That this principle transfers to LLM judge panels is not surprising: any panel including a weak member will be vulnerable if the adversary can target that member. The paper claims its contribution is "first empirical quantification," but quantifying a well-known principle in a new domain is closer to a Findings-level contribution than a main-conference contribution. The authors should more clearly articulate *what changes* in the reader's understanding of LLM evaluation beyond "don't include weak judges."

- **The "diversity trap" framing is overfit to a confound the authors themselves identify.** The paper acknowledges that K_eff and eta_max correlate at r = +0.70 across the 455 panels (memory.md: "CONFOUND_SEVERE"). In the paper framing document, the authors note that "maximizing panel diversity (K_eff) structurally introduces less capable/robust models" --- this is the diversity-capability tradeoff. But if high K_eff *mechanistically requires* including weaker models (because the strongest models are all from a few families and thus correlated), then K_eff's positive coefficient is not evidence that "diversity hurts" in any causal sense --- it is evidence that the current model ecosystem forces a tradeoff between diversity and capability. The paper should be much more careful about causal language. The log-log regression with dominance analysis establishes predictive association, not mechanism.

- **The paper's narrative has been unstable, raising concerns about post-hoc framing.** The decisions.yaml reveals a dramatic trajectory: the original hypothesis was that K_eff *protects* against manipulation (D001-D003), this was progressively falsified (D007-D009), a "kill project" recommendation was issued (D009), then the project was revived with reframing (D010). The 6-model results showed "K_eff irrelevant" (1/12 significant), while the 15-model results showed "K_eff predominantly harmful" (7/12 positive). The Gaussian copula claim was a contribution at 6 models but was falsified at 15 models (D015). This instability suggests the paper's final framing was arrived at by fitting a narrative to whatever the data showed, rather than testing a pre-specified hypothesis. While this is common in empirical research, it weakens the novelty claim: the paper is reporting a correlational pattern in a specific model pool, not a generalizable finding about diversity.

- **The model list in the working paper has serious inconsistencies.** The methodology.tex lists models including "gpt-5.5" and "claude-opus-4-6" but has "[3 local models TBD]" placeholders. The dream/best version lists different models (GPT-4o, Claude-3.5-Sonnet, Gemini-1.5-Pro). The memory.md documents that gpt-4o was retired and replaced with gpt-4.1-nano, and model names changed during the project. The paper needs a final, consistent, fully specified model table. This is not just a formatting issue --- if the "15 models" changed composition during the study, it affects reproducibility.

- **The related work omits critical ensemble learning literature.** The paper's central claim --- that diversity can hurt under adaptive adversaries --- has direct antecedents in the ensemble adversarial robustness literature that are either cited superficially or missing entirely:
  - **Brown et al. (2005)** "Managing Diversity in Regression Ensembles" proved that the diversity-accuracy decomposition (Krogh & Vieli 1995) can be misleading because diversity is not independently controllable. This directly parallels the K_eff-eta_max confound.
  - **He et al. (2017)** and **Pang et al. (2019)** studied adversarial robustness of ensembles and showed that diversity-promoting training does not consistently improve robustness. The paper cites Tramer et al. (2018) on ensemble adversarial training but does not engage with this broader literature.
  - **The "no free lunch" results for ensemble diversity** (e.g., Kuncheva & Whitaker 2003) establish that diversity metrics are generally not independently optimizable from accuracy. The K_eff-eta_max confound discovered in this paper is a specific instance of this general result.
  - The BFT analogy, while pedagogically useful, is somewhat of a strawman. No serious practitioner of multi-judge evaluation claims formal BFT guarantees; the analogy is informal. The paper would be strengthened by engaging more carefully with what practitioners actually assume and recommend.

- **K_eff as a metric is not well motivated against alternatives.** The paper defines K_eff from pairwise MI (Equation 1) and claims it is "more stable for small panels (K=3)" but does not compare it against other diversity metrics (e.g., disagreement rate, double-fault measure, Q-statistic, entropy-based measures from the ensemble diversity literature). If the result is that diversity hurts, it matters whether this is specific to the MI-based K_eff or holds for any reasonable diversity measure. The paper mentions computing K_eff via Gaussian copula rho but also reports copula failure at 6 models --- this methodological tension is not fully resolved.

- **All panels are K=3 with majority vote in the main analysis.** This is a very small panel size. The dream report suggests K=5,7,9 experiments but these appear only in the simulated version, not in the actual experimental data (the decisions.yaml only references K=3 with 455 panels). The practical relevance of findings from 3-judge panels to real evaluation settings (which may use 5+ judges) is unclear.

- **The paper is incomplete.** The main.tex has placeholder sections for Abstract, Results (partial), Analysis, and Conclusion. The Limitations section is empty. Only the Related Work, Introduction, Threat Model, Methodology, and partial Results are written. The dream reports show what a complete version *might* look like, but the actual submission-ready paper does not exist yet. This makes it difficult to assess the final contribution package.

- **Reproducibility concern: attack implementations are underspecified.** Six attack types are listed (prompt injection, sycophancy, score manipulation, verbosity bias, position bias, authority bias) but the paper does not provide the actual attack templates, success criteria, or implementation details. "Programmatically applying each manipulation to the candidate text" is insufficient for reproducibility. How exactly is "sycophancy" operationalized as an attack? What constitutes "score manipulation" for a multiple-choice evaluation? These details are essential.

---

### Questions for Authors

1. **Causal vs. predictive**: Given the r = +0.70 correlation between K_eff and eta_max, and your own observation that "maximizing panel diversity structurally introduces less capable models," how do you distinguish between "diversity actively hurts" and "the current model ecosystem does not have enough diverse-and-strong models"? Would you expect K_eff to still be positively associated with ASR in a hypothetical pool of 15 equally capable but architecturally diverse models?

2. **Why K=3 only?** Real multi-judge panels often use 5-7 judges. Do you have K=5 or K=7 results from the actual experiments (not dream simulations)? The dream report suggests K_eff's effect *increases* with K, which would strengthen your claims substantially.

3. **Attack realism**: Your adaptive adversary has "full knowledge of the panel composition and per-judge vulnerability profiles." This is an extremely strong assumption. In practice, adversaries rarely know the exact judge panel. The partial-knowledge results appear only in the dream simulation. Can you provide actual experimental results under partial knowledge?

4. **Why not test the robustness-first recommendation empirically?** Claim 6 states min(eta_max) dominates 12/12 conditions, but the working Results section does not include this analysis. Is the two-stage algorithm evaluated on held-out attacks or the same attacks used for fitting?

5. **How does this paper's message differ from simply saying "use better models"?** The practical recommendation --- "select the most individually robust judges" --- seems to reduce to "use the strongest available models." What does the paper add beyond this straightforward advice?

---

### Minor Issues

- The paper title is inconsistent across files (at least three variants appear).
- Table 1 in methodology.tex has "[3 local models TBD]" --- unacceptable for submission.
- The R-squared values differ between the paper_framing.md (0.298 for majority) and the working results.tex (0.376). These need reconciliation.
- The paper references "Appendix A" for Theorem 1's proof but no appendix is structured in main.tex.

---

### Preliminary Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 3.5 | Methodology is generally sound (exhaustive enumeration, FDR correction, dominance analysis), but the severe K_eff-eta_max confound (r=0.70) limits interpretability. The causal framing ("diversity trap") overstates what correlational regression can establish. Paper is incomplete. |
| **Excitement** | 2.5 | The core finding (weakest judge matters most) is expected from security principles. The K_eff confound analysis is useful but incremental. The aggregation analysis adds value but is not individually novel. The negative result on diversity is worth reporting but not at the main-conference excitement threshold. |
| **Reproducibility** | 2.0 | Paper is incomplete (multiple placeholder sections). Model list has inconsistencies and TBD entries. Attack implementations are underspecified. No code release mentioned. The project's experimental trajectory (6-model -> 7-model -> 15-model with shifting conclusions) raises concerns about which exact configuration produces the reported numbers. |
| **Overall** | 2.5 | Borderline Findings. The paper addresses a relevant question and the experimental scale is commendable, but the novelty is limited (weakest-link principle is well-known), the framing has been post-hoc fitted to the data, and the paper is substantially incomplete. With a complete manuscript, clearer causal caveats, stronger engagement with ensemble diversity literature, and resolution of the K_eff-eta_max confound interpretation, this could reach 3.0-3.5 (Findings). |

**Confidence**: 4/5. I am confident in my assessment of novelty and positioning. The incomplete state of the paper introduces some uncertainty about the final contribution package.

---

### Detailed Recommendation

The paper's strongest contributions are (a) the empirical demonstration that the commonly observed ASR reduction in multi-judge panels is primarily attributable to individual model strength rather than diversity, and (b) the aggregation analysis showing Bayesian calibration can flip K_eff's direction. These are useful findings for the LLM evaluation community.

However, the paper currently oversells by framing a correlational pattern in a confounded design as a causal "diversity trap." The narrative instability (from "K_eff predicts robustness" to "K_eff is irrelevant" to "K_eff is harmful") reflects honest empirical work but also suggests the final framing is fit to the data rather than testing a clear hypothesis.

To strengthen toward conference acceptance:
1. Reframe from "diversity hurts" to "diversity's apparent protection is confounded with individual model strength; after controlling for strength, diversity has a modest additional harmful association in some conditions." This is less dramatic but more defensible.
2. Add substantial related work on ensemble diversity theory (Brown et al. 2005, Kuncheva & Whitaker 2003) to position the K_eff-eta_max confound as an instance of known diversity-accuracy tradeoffs.
3. Complete the paper (Abstract, full Results, Analysis, Conclusion, Limitations).
4. Provide attack implementation details sufficient for reproducibility.
5. If possible, add K=5 or K=7 experiments from actual data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "928df64c-2c88-4f62-a9ed-ec59da5ca5af",
  "isSidechain": true,
  "agentId": "ae36eb1bd3a5725c7",
  "requestId": "req_011CbJ7FYcRK9t8PYepKcfaK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddd0fd53-78c1-4915-b2a7-a2b6e20ad90b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oFiwWDyNMP33GQT9YKXfi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 59675,
      "output_tokens": 3728,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3728,
          "cache_read_input_tokens": 59675,
          "cache_creation_input_tokens": 3421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3421,
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
