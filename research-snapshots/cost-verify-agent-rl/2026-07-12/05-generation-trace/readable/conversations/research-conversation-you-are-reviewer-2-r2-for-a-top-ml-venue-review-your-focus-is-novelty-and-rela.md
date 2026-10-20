# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review the paper below us

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-adca5254a363aca6d.jsonl`
- **Structured JSON:** [`25c00e33bb2d944fea14.json`](../../sessions/25/25c00e33bb2d944fea14.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-17T12:55:43.757Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

Title: "Dissecting Credit Assignment Failure in Multi-Turn LLM Agent RL: A Dual-Mechanism Analysis"

This is a diagnostic/analysis paper studying why step-independent training fails for multi-turn LLM agents and characterizing failure modes. The paper:
- Identifies 4 failure mechanisms: advantage sign misattribution, policy information loss, entropy collapse, bandit-level credit insufficiency
- Shows episode-level GRPO achieves 23.4% (±6.2pp) vs 1% for step-independent on ALFWorld
- Shows GAE with value function reaches 41%, a 17.6pp gap over episode-level GRPO
- Provides mechanistic analysis showing sign misattribution is dominant (r=0.73) but not sole factor
- Tests across environments (ScienceWorld), scales (1.7B→7B), reward shaping, selective verification

## Full Paper Content (9 pages)

**Abstract**: RL for multi-turn LLM agents commonly adopts step-independent training (each context window as separate bandit arm). They show this fails due to advantage sign misattribution and policy information loss. Episode-level training eliminates sign misattribution but plateaus at 23.4% (±6.2pp) on ALFWorld. GAE reaches 41.0%. They decompose credit assignment failure into four factors, provide failure mode taxonomy, and derive design guidelines. Findings generalize across environments and model scales.

**Section 1 Introduction**: Sets up problem of step-independent optimization in LLM agent RL. On ALFWorld, step-independent GRPO collapses to ~1% while episode-level reaches 23.4%. Two mechanisms: sign misattribution and policy information loss. Episode-level exposes deeper bottleneck: bandit-style credit. GAE reaches 41%, 17.6pp improvement. Mechanistic analysis shows r=0.73 sign-outcome correlation with confounds.

Contributions:
1. Failure mode taxonomy with 4 mechanisms and quantified contributions
2. Empirical characterization of credit granularity spectrum (step-independent → episode-level → per-token GAE)
3. Actionable design guidelines

**Section 2 Background**: GRPO definition. Step-independent mode (trajectory split into h-token windows, each optimized independently). Episode-level mode (full trajectory as single sample). GAE with learned value function.

**Section 3 Failure Mode Taxonomy**: 4 mechanisms: sign misattribution, information loss, entropy collapse, bandit-level credit insufficiency. Each described with empirical indicators.

**Section 4 Experimental Setup**: ALFWorld environment, Qwen3-1.7B (primary) and 7B, GRPO with group size 8.

**Section 5 Results**: 10 subsections covering episode-level convergence, h-sweep, multi-seed, GAE comparison, mechanistic verification, task complexity, reward shaping, selective verification, ARES comparison, cross-environment and scaling.

**Section 6 Discussion**: 5 actionable guidelines. Why community defaults to step-independent. Limitations.

**Section 7 Conclusion**: Summary.

**References** (only 10 total):
[1] DeepSeekMath (2024)
[2] RAGEN (2025) 
[3] ALFWorld (ICLR 2021)
[4] ScienceWorld (EMNLP 2022)
[5] GAE / Schulman (ICLR 2016)
[6] Self-Guide (2026)
[7] ARES (2026)
[8] Thinkless (NeurIPS 2025)
[9] ReflAct (EMNLP 2025)
[10] PPO / Schulman (2017)

## Experiment Design Context

The paper was reframed as a diagnostic/analysis paper. Originally it aimed to propose selective verification (B-IAVR) as a method contribution, but experiments showed it fails: action-change reward signal is r=0.08 (p=0.12), B-IAVR is dominated by both ARES and a simple confidence heuristic. The paper pivoted to framing as failure mode analysis.

Key experimental facts:
- The h-sweep is not clean monotonic (non-monotonicity between seeds at adjacent h values)
- Mechanistic verification partially failed: many hypotheses only partially confirmed
- Multi-seed variance is very high (std=6.2pp, 95% CI [15.7%, 31.1%])
- Selective verification (B-IAVR) completely fails as a contribution
- GAE >> episode-level GRPO is the strongest finding (17.6pp gap)
- Only 10 references in the bibliography

## Your Review Task (R2: Novelty + Related Work)

Evaluate:
1. **Novelty**: How novel are the findings? Is the failure mode taxonomy genuinely new insight or well-known RL theory applied to a specific setting? Is credit assignment being a challenge in RL a new observation?
2. **Positioning**: Does the paper adequately position itself relative to prior work? Is the "analysis paper" framing convincing?
3. **Related work coverage**: Are key related works cited? The paper has only 10 references. Consider:
   - Classic credit assignment literature (temporal difference, eligibility traces)
   - Other LLM agent RL papers (AgentQ, Archer, WebAgent, etc.)
   - Multi-turn RL for LLMs (RLHF literature on reward modeling)
   - Step-level vs episode-level reward in RL (process reward models, outcome reward models)
   - Other analysis/diagnostic papers in ML
4. **Contribution significance**: For a top venue, are the contributions sufficient? An analysis paper needs very strong insights to compensate for lack of method contribution.
5. **Writing quality**: Is the paper well-written? Any AI-style writing artifacts?
6. **Reference adequacy**: With only 10 references, is the bibliography sufficient for a top venue submission?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: major/minor)
- Questions for authors
- Missing related work (specific papers/areas that should be cited)
- Score (1-6) and confidence (1-5)
- One-line recommendation

Be rigorous. This is a top venue review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "5a9e7c4d-62d8-4c29-ac12-408e7d20b751",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T12:55:43.760Z_

```json
{
  "parentUuid": "5a9e7c4d-62d8-4c29-ac12-408e7d20b751",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
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
  "uuid": "3026d0dc-697e-45a5-9d40-ead1b1cae646",
  "timestamp": "2026-05-17T12:55:43.760Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T12:55:46.871Z_



I'll start by reading the actual paper and any related project files to ground my review in the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3026d0dc-697e-45a5-9d40-ead1b1cae646",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BDdKZPeKBRs6dJ4MA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34c04c0c-8a2f-4098-820c-f78fd1179c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrEfCmJGBeVMirTDafXShv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8689,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8689,
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

_source line 4 · 2026-05-17T12:55:47.185Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011oCFe7obYKiusPDgW1eQcN`</summary>

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
  "parentUuid": "34c04c0c-8a2f-4098-820c-f78fd1179c29",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BDdKZPeKBRs6dJ4MA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da400315-6679-4e58-8b63-3d99986e4582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrEfCmJGBeVMirTDafXShv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8689,
      "cache_read_input_tokens": 8252,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 128,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 8689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8689,
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

_source line 5 · 2026-05-17T12:55:47.189Z_

<details><summary>↩ Tool result · `toolu_011oCFe7obYKiusPDgW1eQcN`</summary>

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
  "parentUuid": "da400315-6679-4e58-8b63-3d99986e4582",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "7688765b-930a-4490-8ef8-1756c71758a3",
  "sourceToolAssistantUUID": "da400315-6679-4e58-8b63-3d99986e4582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T12:55:50.569Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UpKDa7VddTSFhKKJNUJaU6`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7688765b-930a-4490-8ef8-1756c71758a3",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BDtLTJ1WJjiN7whRXR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40e5a572-ddec-440e-b15b-b107c2004f74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZanAZFkQfzfo5XGkvhSsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 7 · 2026-05-17T12:55:50.594Z_

<details><summary>↩ Tool result · `toolu_01UpKDa7VddTSFhKKJNUJaU6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-17\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    title: \\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.05842\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\n\\n  - id: skill0-2026\\n    title: \\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.02268\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\n\\n  - id: fission-grpo2026\\n    title: \\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2601.15625\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\n\\n  - id: selfbudgeter2026\\n    title: \\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"ICLR 2026 (under review)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11274\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\n      Parallel concept: SelfBudgeter allocates computation budget;\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\n\\n  - id: cove2026\\n    title: \\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\"\\n    authors: \\\"Chen et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.01940\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\n\\n  # ============================================================\\n  # Direction 3: Selective Verification / Adaptive Computation\\n  # ============================================================\\n\\n  - id: wan2025derailer-rerailer\\n    title: \\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\"\\n    authors: \\\"Wan et al.\\\"\\n    venue: \\\"ACL 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2408.13940\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Most directly related competitor. Both do selective verification with binary trigger.\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\n\\n  - id: sherlock2025\\n    title: \\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\"\\n    authors: \\\"Microsoft\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.00330\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\n\\n  - id: singhi2025when-to-verify\\n    title: \\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\"\\n    authors: \\\"Singhi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.01005\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\n      B-IAVR learns this allocation via RL rather than analytically.\\n\\n  - id: yang2026ares\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.07915\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\n      Reduces reasoning tokens by up to 52.7%.\\n\\n  - id: tu2025autothink\\n    title: \\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\"\\n    authors: \\\"Tu et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10832\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\n\\n  - id: du2025thinkless\\n    title: \\\"Thinkless: LLM Learns When to Think\\\"\\n    authors: \\\"Fang et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.13379\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained control token to decide when to invoke extended thinking.\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\n\\n  - id: wang2025efficient-agents\\n    title: \\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.02694\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\n\\n  - id: venktesh2025trust-but-verify\\n    title: \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\"\\n    authors: \\\"Venktesh et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.16665\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Survey of verification approaches for test-time compute scaling.\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\n\\n  - id: agent-omit2026\\n    title: \\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\"\\n    authors: \\\"Ning et al.\\\"\\n    venue: \\\"ICML 2026\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.04284\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\n\\n  - id: ava2026\\n    title: \\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\"\\n    authors: \\\"Patel\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\n      single-turn reasoning vs multi-turn agent trajectories.\\n\\n  - id: cast2026\\n    title: \\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\"\\n    authors: \\\"Pang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15041\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Historical execution cases calibrate reasoning depth for tool use.\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\n\\n  - id: marginal-token-allocators2026\\n    title: \\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\"\\n    authors: \\\"Zhu\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.01214\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\n      that verification decisions should reflect marginal cost-benefit analysis.\\n\\n  - id: argos2025\\n    title: \\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv (revised April 2026)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.03438\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\n\\n  # ============================================================\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\n  # ============================================================\\n\\n  - id: kim2025reflact\\n    title: \\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\"\\n    authors: \\\"Kim et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.15182\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\n\\n  - id: choudhury2025agentprm\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2502.10325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\n\\n  - id: xi2025agentprm\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Xi et al.\\\"\\n    venue: \\\"ACM Web Conference 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.08325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\n\\n  - id: xiang2024retrospex\\n    title: \\\"Retrospex: Language Agent Meets Offline RL Critic\\\"\\n    authors: \\\"Xiang et al.\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2505.11807\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\n      Similar architecture could inform B-IAVR's verification value estimation.\\n\\n  - id: cfgm2025\\n    title: \\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.15305\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Memory-augmented agent planning with episodic grounding.\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\n\\n  - id: respact2024\\n    title: \\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\"\\n    authors: \\\"Dongre et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2411.00927\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\n\\n  # ============================================================\\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\\n  # ============================================================\\n\\n  - id: turn-ppo2025\\n    title: \\\"Turn-Level Policy Optimization for Multi-Turn Agent Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.17008\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Most direct competitor. Identifies \\\"uniform advantage\\\" problem in\\n      step-independent GRPO (subset of our \\\"sign misattribution\\\"). Proposes turn-level\\n      MDP + learned value function. Our differences: (1) more precise formalization\\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\\n      (episode-level coarser credit vs their finer turn-level credit).\\n\\n  - id: gagpo2026\\n    title: \\\"GAGPO: Generalized Advantage Grouped Policy Optimization\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.13217\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\\n      Pursues finer-grained credit to improve performance; our work diagnoses why\\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\\n      Different contribution axis: performance optimization vs mechanism diagnosis.\\n\\n  - id: mt-grpo2025\\n    title: \\\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11821\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\\n      our contrarian shows coarser episode-level eliminates sign misattribution.\\n\\n  - id: istar2025\\n    title: \\\"Agentic Reinforcement Learning with Implicit Step Rewards\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.19199\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\\n      Learns step-level credit via implicit rewards without explicit labels;\\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\\n\\n  - id: archer2024\\n    title: \\\"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\\\"\\n    authors: \\\"Zhou, Zanette, Pan, Levine, Kumar\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2402.19446\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\\n      High-level off-policy value RL (utterance-level) + low-level token policy.\\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\\n      our work specifically diagnoses why flat step-independent approaches fail.\\n\\n  - id: ca-survey2026\\n    title: \\\"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\\\"\\n    authors: \\\"Zhang\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.09459\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\\n      sign misattribution diagnosis within the broader CA landscape.\\n\\n  - id: hiper2026\\n    title: \\\"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\\\"\\n    authors: \\\"Peng et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.16165\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\\n      Pursues SOTA performance via hierarchical plan-execute architecture;\\n      our work does mechanism diagnosis of why step-independent GRPO fails.\\n      Different contribution dimension: not comparable on performance axis.\\n\", \"total_chars\": 29915, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40e5a572-ddec-440e-b15b-b107c2004f74",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "82ba97c2-df87-4c2d-8a62-0973d67edd0f",
  "sourceToolAssistantUUID": "40e5a572-ddec-440e-b15b-b107c2004f74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T12:55:50.984Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017KHXQTmn2G6h8XYShBwxxL`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ba97c2-df87-4c2d-8a62-0973d67edd0f",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BDtLTJ1WJjiN7whRXR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5371fbb2-80b6-4f67-a80c-5e2548c5050e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZanAZFkQfzfo5XGkvhSsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 9 · 2026-05-17T12:55:50.996Z_

<details><summary>↩ Tool result · `toolu_017KHXQTmn2G6h8XYShBwxxL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\\n\\n> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)\\n\\n## Core Insight\\n\\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：\\n\\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \\\"先探索 drawer 再去 countertop\\\"）\\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：\\n   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）\\n   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）\\n   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality\\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命\\n\\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\\n\\n**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。\\n\\n## Story Arc\\n\\n**Dual contribution**: Training methodology diagnosis + Selective verification system\\n\\n叙事线：\\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\\n2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）\\n3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决\\n4. 分析 \\\"为什么社区默认走向 step-independent\\\"（context window 限制 + token-level training 惯性 + framework design accident）\\n5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\\n6. 结果：near-always-on performance + 显著降低 verification cost\\n\\n**定位**：不 claim \\\"发明了 episode-level RL\\\"（trivial），而是 \\\"诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification\\\"\\n\\n## Target Venue\\n\\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\\n\\n## Core Claims\\n\\n### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism\\n- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison\\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\\n- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)\\n- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`\\n\\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\\n\\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\\n- 当前证据状态：**not yet established**，依赖 Phase B + C\\n- 前提：Claim 1 的 agent 需足够强\\n\\n## Contingency Plan\\n\\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\\n- **Plan A**：paper 变为 diagnostic + analysis contribution — \\\"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\\\" (需更深 ablation + GAE comparison + community practice survey)\\n- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification\\n- 不考虑 downgrade venue\\n- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（\\\"诊断社区默认实践的隐性代价\\\" > \\\"episode-level RL works\\\"）\\n\\n## Reviewer Attack Surface + Defense\\n\\n| # | Concern | Severity | Defense |\\n|---|---------|----------|---------|\\n| 1 | \\\"Episode-level RL is obvious / well-known\\\" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + \\\"为什么社区默认 step-independent\\\" 分析 |\\n| 2 | \\\"Theory 与 GRPO 不匹配\\\" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |\\n| 3 | \\\"缺 GAE/标准 RL baselines\\\" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |\\n| 4 | \\\"Self-Guide 3x performance gap\\\" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |\\n| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |\\n| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |\\n| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\\n| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |\\n| 9 | \\\"Turn-PPO 已解决相同问题\\\" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage (subset)，我们发现 sign misattribution (superset + 量化 γ^24≈29%)；解法相反 (finer vs coarser) |\\n\\n## Evidence Status Matrix\\n\\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\\n|-------|-------------|--------------------------|----------|\\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\\n| Claim 2 | N/A | Phase B full implementation | P1 |\\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\\n\\n## Competitive Positioning\\n\\n| System | Method | Benchmark | Key Difference from Us |\\n|--------|--------|-----------|----------------------|\\n| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | We add selectivity via RL |\\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | SFT vs RL, continuous vs binary |\\n| Thinkless (NeurIPS'25) | RL control token | reasoning domain | Same RL philosophy, different domain |\\n| ReflAct (EMNLP'25) | Prompting GPT-4 | ALFWorld 93.3% | Different scale/approach |\\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default, our baseline |\\n| **Turn-PPO (2512.17008)** | Turn-level MDP + value fn | reasoning tasks | \\\"Uniform advantage\\\" vs our \\\"sign misattribution\\\"; finer credit vs coarser |\\n| **GAGPO (2605.13217)** | Grouped value proxy, step-aligned | ALFWorld 93.5% (1.5B) | Finer-grained credit for performance; we diagnose mechanism failure |\\n| **MT-GRPO (2505.11821)** | Turn-level reward design | QA search tasks | Turn-level credit; we show coarser suffices |\\n| **iStar (ICLR'26)** | Implicit PRM + dual advantage | WebShop 86.5% | Learns step rewards; we show episode-level eliminates misattribution |\\n| **ArCHer (ICML'24)** | Hierarchical multi-turn RL | multi-turn agents | Foundational framework; establishes need for hierarchical structure |\\n| **HiPER (2602.16165)** | Hierarchical Plan-Execute RL | ALFWorld 97.4% (7B) | SOTA performance pursuit; we do mechanism diagnosis |\\n\\n### Positioning Strategy\\n\\n**核心差异化：Contrarian Solution。** 竞品（Turn-PPO, GAGPO, MT-GRPO, iStar, HiPER）一致认为 multi-turn RL 需要更细粒度的 credit assignment（turn-level, step-level, hierarchical），并用此提升性能。我们的贡献是诊断性的：\\n\\n1. **问题定义更精确**：Turn-PPO 发现 \\\"uniform advantage\\\" 问题（所有 turn 获得相同 advantage），我们发现更本质的 \\\"Advantage Sign Misattribution\\\"（advantage 符号由 episode outcome 决定而非 local action quality），并量化 γ^24 ≈ 29% 的 return 衰减。Sign misattribution 是 uniform advantage 的超集。\\n\\n2. **Contrarian solution**：所有竞品的解法都是引入更细的 credit（turn-level value, step-level PRM, hierarchical planner）。我们展示更粗的 episode-level credit 反而消除 sign misattribution，因为它避免了将 episode reward 错误分配到独立优化的子窗口。这挑战了 \\\"越细越好\\\" 的社区默认假设。\\n\\n3. **不同 contribution 维度**：GAGPO/HiPER 追求 ALFWorld 93-97% 的 SOTA performance（通过更好的 credit + 更复杂的架构）。我们不 compete on performance axis，而是回答 \\\"为什么社区默认的 step-independent 灾难性失败\\\" 这个诊断问题。两个 contribution 维度正交互补。\\n\\n4. **与 CA Survey 的关系**：Zhang (2604.09459) 系统化了 47 种 CA 方法，但未分析 CA 方法本身的 failure modes（何时更细粒度反而有害）。我们填补这一空白。\\n\\n## Research Phases\\n\\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\\n\", \"total_chars\": 8631, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5371fbb2-80b6-4f67-a80c-5e2548c5050e",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "a452c257-e018-4017-be24-7cf277159720",
  "sourceToolAssistantUUID": "5371fbb2-80b6-4f67-a80c-5e2548c5050e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T12:55:52.106Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01P3Efgr1MgsBLFpjCM3SH54`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a452c257-e018-4017-be24-7cf277159720",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BDtLTJ1WJjiN7whRXR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "579dc430-3be4-4f41-a9f9-90d8e5f62ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZanAZFkQfzfo5XGkvhSsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 11 · 2026-05-17T12:55:52.115Z_

<details><summary>↩ Tool result · `toolu_01P3Efgr1MgsBLFpjCM3SH54`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cost-verify-agent-rl'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "579dc430-3be4-4f41-a9f9-90d8e5f62ea6",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "14f21eb2-7f81-4da4-b103-9013a2983354",
  "sourceToolAssistantUUID": "579dc430-3be4-4f41-a9f9-90d8e5f62ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T12:55:52.331Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01B41EQ4PRywV1oB8FuMuJD6`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f21eb2-7f81-4da4-b103-9013a2983354",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BDtLTJ1WJjiN7whRXR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0ac8870-6179-4a2c-92cc-c21835efd10d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZanAZFkQfzfo5XGkvhSsm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16941,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 391,
          "cache_read_input_tokens": 16941,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 13 · 2026-05-17T12:55:52.358Z_

<details><summary>↩ Tool result · `toolu_01B41EQ4PRywV1oB8FuMuJD6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| hsweep_h2_seed1 | Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality | — | — | — |\\n\\n## 待处理\\n- exp028_prereq_zeroshot_instruct: Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\\\"SFT是毒药\\\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。（准备中）\\n- exp021_sft_ragen_format: Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.（准备中）\\n- exp020d_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.（准备中）\\n- exp020c_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).（准备中）\\n- exp019c_expert_sft_v3: Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。（准备中）\\n- exp019b_expert_sft_v2（准备中）\\n- exp018_sft_grpo: Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），使 GRPO 有足够非零 reward group 产生有效梯度。LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, won=10.0, 无 bonus/penalty, GRPO 30 步。Pass: success ≥ 20%。（准备中）\\n- exp014b: 极低 Dense Reward: valid_action_bonus=0.01（1:1000 比例），测试极弱 bonus 能否防 collapse 又不引发 gaming。如果 bonus 弱到不影响 GRPO reward ranking，模型不会被诱导走捷径。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。（准备中）\\n- exp014a: Success-Gated Dense Reward: valid_action_bonus=0.15 只在 group 内至少一条 trajectory success 时才给。消除 reward gaming 的独立最大化路径——没有 success 就没有 bonus，模型必须探索 success。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。（准备中）\\n- exp014c: Success-gated valid_action_bonus：bonus 仅在 episode 成功时累加到 reward，消除独立最大化路径。valid_action_bonus=0.15, success_reward=10.0。解决 exp013f reward gaming（unconditional bonus 导致 agent 放弃 success 追求 valid action）。从 step 5 checkpoint 恢复 GRPO 30 步。（准备中）\\n- …另有 8 项\\n\\n## 近期结论\\n- **exp025c** (failed): —\\n- **exp029_episode_level** (success): Episode-level 训练（context_window_mode: full）解决 step_independent h=2 的信用分配缺陷，模型能学到跨步规划策略，val success 不再停滞于 baseline。 ← 基于 exp028c_selfguide_recipe\\n  [exp029_episode_level_diagnose_attempt4](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/report/diagnose_attempt4.md) | [tatsu_patch_deploy_plan](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/intermediate/tatsu_patch_deploy_plan.md) | [credit_assignment_analysis](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/chart/credit_assignment_analysis_info.md)\\n- **exp026_step_independent_grpo** (negative): Step-independent GRPO（每步独立优化、不建模跨步依赖）能在ALFWorld多步任务中学到有效策略，因为每步的local reward信号足以引导正确行为选择 ← 基于 exp021_ragen_sft_v4\\n\\n## 趋势\\n成功 4 / 负向 5 / 失败 20 / 共 38\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-17606: 无 GPU 信息\\n\\n## 告警\\n- exp_001: 训练失败 — unknown\\n- exp_001b: 训练失败 — unknown\\n- exp_002: 训练失败 — unknown\\n- exp003: 训练失败 — unknown\\n- exp007: 训练失败 — unknown\\n- exp009: 训练失败 — unknown\\n- exp010: 训练失败 — unknown\\n- exp011: 已被终止 — unknown\\n- exp012: 训练失败 — unknown\\n- exp012b: 已被终止 — unknown\\n- exp013: 已被终止 — unknown\\n- exp013b: 训练失败 — unknown\\n- exp013c: 已被终止 — unknown\\n- exp013d: 训练失败 — unknown\\n- exp013e: 训练失败 — unknown\\n- exp015: 已被终止 — unknown\\n- exp016: 训练失败 — unknown\\n- exp019_expert_sft_v2: 已被终止 — unknown\\n- exp020_grpo_from_sft: 训练失败 — unknown\\n- exp022_grpo_from_sft_v4: 已被终止 — unknown\\n- exp023_grpo_parallel: 训练失败 — unknown\\n- exp023c_grpo_serial: 训练失败 — unknown\\n- exp024_success_gated_grpo: 已被终止 — unknown\\n- exp025: 训练失败 — unknown\\n- exp025b: 训练失败 — unknown\\n- exp025c: 训练失败 — unknown\\n- exp027_stable_grpo: 训练失败 — unknown\\n- exp028a_recipe_fix: 已被终止 — unknown\\n- exp028c_selfguide_recipe: 训练失败 — unknown\\n\", \"total_chars\": 4728, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0ac8870-6179-4a2c-92cc-c21835efd10d",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "9fabce35-a63e-42bc-83df-111c94e4c9ca",
  "sourceToolAssistantUUID": "b0ac8870-6179-4a2c-92cc-c21835efd10d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-17T12:55:55.124Z_

Now let me look at the actual paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fabce35-a63e-42bc-83df-111c94e4c9ca",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BEGMX89m48ziMtSM5G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e2cacaa-9a2b-42fc-a58f-9734e4fc6d3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lxn9cqotxwwnsNUoAYyHyj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17777,
      "cache_read_input_tokens": 18392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17777,
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

_source line 15 · 2026-05-17T12:55:55.601Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CbhBX1JXDKfgpaixYQdUXy`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e2cacaa-9a2b-42fc-a58f-9734e4fc6d3d",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BEGMX89m48ziMtSM5G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f65aa29d-0785-4a69-9cf0-382f6a7401c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lxn9cqotxwwnsNUoAYyHyj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17777,
      "cache_read_input_tokens": 18392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17777,
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

_source line 16 · 2026-05-17T12:55:55.622Z_

<details><summary>↩ Tool result · `toolu_01CbhBX1JXDKfgpaixYQdUXy`</summary>

```text
artifacts/dream_reports/dream_20260516T235255/best/paper.tex
artifacts/dream_reports/dream_20260516T235255/median/paper.tex
artifacts/dream_reports/dream_20260516T235255/worst/paper.tex
artifacts/_project/paper/theoretical_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments_aa43d8.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/discussion.tex
docs/paper/experiments.tex
artifacts/_project/paper/conclusion.tex
docs/paper/discussion.tex
docs/paper/theoretical_analysis.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
artifacts/dream_reports/dream_20260517T121256/best/paper.tex
artifacts/dream_reports/dream_20260517T121256/median/paper.tex
artifacts/dream_reports/dream_20260517T121256/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f65aa29d-0785-4a69-9cf0-382f6a7401c9",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "5cd30e76-2216-406e-8d8e-87f512c65017",
  "sourceToolAssistantUUID": "f65aa29d-0785-4a69-9cf0-382f6a7401c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T12:55:56.015Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01X9SUCaBreXQoCqJo5i2YkB`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cd30e76-2216-406e-8d8e-87f512c65017",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BEGMX89m48ziMtSM5G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c41131fe-3eb0-413a-bd6a-d3e8993d1464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lxn9cqotxwwnsNUoAYyHyj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17777,
      "cache_read_input_tokens": 18392,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 18392,
          "cache_creation_input_tokens": 17777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17777,
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

_source line 18 · 2026-05-17T12:55:56.033Z_

<details><summary>↩ Tool result · `toolu_01X9SUCaBreXQoCqJo5i2YkB`</summary>

```text
artifacts/_project/paper/references.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c41131fe-3eb0-413a-bd6a-d3e8993d1464",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "62807d27-7519-4b38-af99-2b7e22cd4822",
  "sourceToolAssistantUUID": "c41131fe-3eb0-413a-bd6a-d3e8993d1464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T12:55:58.832Z_

<details open><summary>🔧 Tool call — Read · `toolu_018aHvmzn3EkT1hqBnL9k1LP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62807d27-7519-4b38-af99-2b7e22cd4822",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BEXvedSofuNpghC8FG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e3c2eb3-0ee9-4940-b374-b7ef6a399be9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPPYg6KZFF7rGUbbGPb1aJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 36169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 539,
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

_source line 20 · 2026-05-17T12:55:58.838Z_

<details><summary>↩ Tool result · `toolu_018aHvmzn3EkT1hqBnL9k1LP`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{subcaption}
10	
11	\title{Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents}
12	
13	\author{Anonymous}
14	
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Self-verification improves interactive agent performance but incurs substantial inference cost, with the majority of verification steps merely confirming existing decisions without changing behavior. We address the problem of training agents to selectively verify only when verification is likely to be informative. A prerequisite for this is effective Reinforcement Learning (RL) training of multi-turn agents, yet we find that the community-default step-independent training paradigm catastrophically fails in long-horizon settings. We diagnose a dual mechanism: (1) policy information loss from truncated context windows, and (2) advantage sign misattribution where per-window gradient direction reflects episode outcome rather than local action quality. Episode-level GRPO resolves both issues, achieving 46.8\% $\pm$ 2.4\% validation success on ALFWorld (5 seeds) compared to 0\% for step-independent training. Building on this foundation, we propose B-IAVR (Binary Informed Action-change Verification Routing), which uses action-change as an intrinsic reward signal for verification informativeness. B-IAVR reduces verification rate by 52\% while maintaining task success within 1.5 percentage points of always-on verification, and achieves the highest success-per-cost ratio (0.75) among all methods including an SFT-based baseline.
22	\end{abstract}
23	
24	\section{Introduction}
25	
26	Interactive agents that operate in multi-step environments face a fundamental tension between performance and efficiency. Self-verification, where an agent re-examines its proposed action before execution, consistently improves task success across environments. However, empirical analysis reveals that 77\% of verification steps are confirmatory, merely reaffirming the original action without behavioral change. This suggests that a large fraction of verification computation is wasted.
27	
28	Training an agent to learn \emph{when} to verify requires RL, since the value of verification at any step depends on the full trajectory context and cannot be determined by static rules. This requirement exposes a critical failure in current LLM agent training practice. The dominant paradigm, step-independent training as implemented in frameworks like RAGEN, processes each context window as an independent optimization unit. We demonstrate that this approach catastrophically collapses to 0\% task success in multi-turn settings.
29	
30	We identify a dual mechanism responsible for this collapse. First, \textbf{policy information loss}: when the policy observes only $h$ steps of history, it cannot learn cross-step strategies (e.g., ``explore drawer A before navigating to countertop B''). Second, \textbf{advantage sign misattribution}: in the step-independent regime, each window's advantage sign is determined by the episode outcome rather than local action quality. Good actions in failed episodes receive negative advantage (incorrect punishment), while poor actions in successful episodes receive positive advantage (incorrect reinforcement). Per-window advantage logging confirms this empirically: the correlation between advantage sign and episode outcome is $r = 0.97$, while the correlation with local action quality is merely $r = 0.04$.
31	
32	Episode-level GRPO resolves both mechanisms simultaneously. The policy observes complete episode history (resolving information loss), and all tokens share a single episode-level advantage, eliminating the need to distribute reward signals across independently-optimized windows (resolving sign misattribution). This is not a novel algorithm but a diagnostic insight: the community default is silently broken for multi-turn tasks, and the fix is straightforward.
33	
34	With effective RL training established, we address the original question: learning selective verification. We propose B-IAVR, which trains a binary verify/skip decision using action-change as the reward signal for verification informativeness. When the agent verifies and changes its action, this indicates the verification was informative; the reward function directly incentivizes verification at such decision points.
35	
36	Our contributions are:
37	\begin{enumerate}
38	\item A systematic diagnosis of why step-independent RL training fails for multi-turn LLM agents, identifying dual mechanisms (information loss and sign misattribution) with empirical verification across 3 seeds, 5 context-window sizes, and 2 environments.
39	\item Episode-level GRPO as a practical fix achieving 46.8\% $\pm$ 2.4\% success (5 seeds) on ALFWorld with Qwen3-1.7B, validated on ScienceWorld (32\% vs 8\% step-independent) and Qwen3-7B (58\% vs 5\%).
40	\item B-IAVR, a selective verification method that reduces verification cost by 52\% with only 1.5pp success degradation, outperforming ARES reproduction (+3.5pp success at 10pp lower cost) and achieving the best success-per-cost ratio among all baselines.
41	\end{enumerate}
42	
43	\section{Related Work}
44	
45	\paragraph{RL for LLM Agents.}
46	RAGEN introduced GRPO-based training for multi-turn LLM agents using a step-independent paradigm where each context window is treated as an independent optimization unit. While effective for short-horizon tasks, this paradigm's failure modes in long-horizon settings have not been systematically analyzed. Our work provides this analysis and demonstrates that episode-level training resolves the identified issues.
47	
48	\paragraph{Self-Verification in Agents.}
49	Self-Guide trains always-on self-verification using expert demonstrations, achieving 72.7\% on ALFWorld with Qwen-1.7B. ReflAct uses prompting-based reflection with GPT-4, reaching 93.3\%. These methods treat verification as always-on. ARES proposes adaptive effort allocation using an SFT-trained router with continuous effort levels, achieving 52.7\% token reduction. Our approach differs in using RL rather than SFT for the routing decision, and in using action-change as a direct reward signal rather than heuristic labels.
50	
51	\paragraph{Compute-Adaptive Inference.}
52	Thinkless trains RL control tokens to skip extended reasoning when unnecessary. Our work applies this philosophy to the verification domain in interactive agents, where the binary verify/skip decision has clear behavioral consequences (action change) that provide natural reward signals.
53	
54	\paragraph{Credit Assignment in RL.}
55	The advantage sign misattribution we identify relates to classical credit assignment problems in RL. GAE provides per-token credit via learned value functions. We show that for LLM agent training, correcting the sign (episode-level) captures most of the benefit (+3pp gap to GAE), suggesting that sign correctness is the primary bottleneck rather than per-token credit granularity.
56	
57	\section{Method}
58	
59	\subsection{Problem Setup}
60	
61	We consider an interactive agent operating in a text-based environment over $T$ steps. At each step $t$, the agent observes state $s_t$, generates action $a_t$, and optionally performs self-verification before committing. The episode terminates with binary reward $R \in \{0, 1\}$ (task success/failure).
62	
63	\subsection{Diagnosing Step-Independent Training Failure}
64	
65	In step-independent training, the episode is segmented into windows of $h$ steps, each optimized independently. For a window starting at step $t$, the per-window return is computed as $G_t = \gamma^{(T-t)/h} \cdot R$, and GRPO group normalization yields advantages:
66	\begin{equation}
67	A_t = \frac{G_t - \mu_G}{\sigma_G}
68	\end{equation}
69	where $\mu_G$ and $\sigma_G$ are computed across episodes in the batch.
70	
71	\textbf{Mechanism 1: Information Loss.} With window size $h$, the policy conditions on only $h$ steps of history. For tasks requiring coordinated multi-step strategies (average episode length 25 steps in ALFWorld), small $h$ prevents learning temporal dependencies.
72	
73	\textbf{Mechanism 2: Sign Misattribution.} Because $G_t \propto R$ for all windows within an episode, the sign of $A_t$ after group normalization is determined by whether the episode succeeded or failed, independent of the action quality within window $t$. Formally, for any window in a successful episode, $G_t > 0$; after normalization against a batch containing failures, $A_t > 0$. This means all actions in successful episodes are reinforced and all actions in failed episodes are suppressed, regardless of their local quality.
74	
75	\subsection{Episode-Level GRPO}
76	
77	Episode-level GRPO treats the entire trajectory as a single GRPO sample. All tokens in the episode share a common advantage:
78	\begin{equation}
79	A_{\text{episode}} = \frac{R - \mu_R}{\sigma_R}
80	\end{equation}
81	This eliminates information loss (full history visible) and sign misattribution (no per-window reward decomposition needed). While the per-token credit assignment is coarser than GAE, we show empirically that correcting the advantage sign is the dominant factor.
82	
83	\subsection{Selective Verification via B-IAVR}
84	
85	Given a converged episode-level agent, we train a selective verification policy. At each step, before action execution, the agent produces a binary token: \texttt{[VERIFY]} or \texttt{[SKIP]}.
86	
87	The reward function combines task success with verification informativeness:
88	\begin{equation}
89	r = R_{\text{task}} + \alpha \sum_{t: \text{verified}} \mathbb{1}[\text{action\_changed}_t] - \beta \sum_{t} \mathbb{1}[\text{verified}_t]
90	\end{equation}
91	where $\alpha = 0.3$ rewards informative verifications (those that change the action) and $\beta = 0.1$ penalizes verification cost. The ratio $\alpha/\beta = 3$ sets the break-even action-change probability at $1/3$, calibrated to the observed overall action-change rate of 0.23.
92	
93	Training uses episode-level GRPO, initialized from the converged always-on checkpoint. The selective policy learns to verify at high-uncertainty steps (early in the episode, unfamiliar states) and skip at confident steps (late, routine actions).
94	
95	\section{Experiments}
96	
97	\subsection{Setup}
98	
99	We train Qwen3-1.7B on ALFWorld (134 training tasks, 64 validation tasks) using the RAGEN framework. Episode-level GRPO uses full context windows. Hyperparameters: learning rate $5 \times 10^{-6}$, GRPO group size 4, KL coefficient 0.01. All results report validation success rate unless noted.
100	
101	\subsection{Episode-Level GRPO Convergence}
102	
103	Table~\ref{tab:convergence} shows the training trajectory. The model breaks through an initial plateau at step 25 (when action validity exceeds 70\%) and converges at step 50 with 48\% validation success. The plateau corresponds to the phase where the model learns action syntax; once valid actions exceed 70\%, the episode-level advantage signal becomes informative for strategic learning.
104	
105	\begin{table}[h]
106	\centering
107	\caption{Episode-level GRPO convergence trajectory on ALFWorld.}
108	\label{tab:convergence}
109	\begin{tabular}{cccccc}
110	\toprule
111	Step & Val Success & Action Valid & Train Success & Entropy & KL \\
112	\midrule
113	5  & 0.250 & 0.450 & 0.310 & 0.220 & 0.003 \\
114	10 & 0.250 & 0.500 & 0.380 & 0.190 & 0.005 \\
115	15 & 0.281 & 0.545 & 0.438 & 0.170 & 0.007 \\
116	20 & 0.300 & 0.610 & 0.480 & 0.150 & 0.009 \\
117	25 & 0.330 & 0.680 & 0.500 & 0.140 & 0.010 \\
118	30 & 0.380 & 0.730 & 0.530 & 0.130 & 0.011 \\
119	35 & 0.420 & 0.770 & 0.550 & 0.120 & 0.012 \\
120	40 & 0.450 & 0.800 & 0.570 & 0.120 & 0.012 \\
121	45 & 0.470 & 0.810 & 0.580 & 0.110 & 0.013 \\
122	50 & \textbf{0.480} & 0.820 & 0.580 & 0.110 & 0.013 \\
123	\bottomrule
124	\end{tabular}
125	\end{table}
126	
127	\subsection{Multi-Seed Replication}
128	
129	Five independent seeds confirm reproducibility (Table~\ref{tab:multiseed}). Mean converged success is 46.8\% $\pm$ 2.4\% (95\% CI: [43.8\%, 49.8\%]). All seeds exceed 40\%, and the CI excludes the pre-breakthrough plateau of 28\%.
130	
131	\begin{table}[h]
132	\centering
133	\caption{Multi-seed convergence results (5 seeds, episode-level GRPO).}
134	\label{tab:multiseed}
135	\begin{tabular}{ccccc}
136	\toprule
137	Seed & Converge Step & Val Success & Action Valid & Pass@8 \\
138	\midrule
139	1 & 50 & 0.480 & 0.82 & 0.95 \\
140	2 & 45 & 0.450 & 0.79 & 0.93 \\
141	3 & 42 & 0.500 & 0.84 & 0.96 \\
142	4 & 52 & 0.470 & 0.80 & 0.94 \\
143	5 & 48 & 0.440 & 0.78 & 0.92 \\
144	\midrule
145	Mean$\pm$Std & 47.4$\pm$3.8 & 0.468$\pm$0.024 & 0.81$\pm$0.03 & 0.94$\pm$0.02 \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\subsection{Context Window Ablation (h-Sweep)}
151	
152	Table~\ref{tab:hsweep} presents the critical h-sweep experiment (3 seeds per setting, 15 training steps). A catastrophic cliff appears at $h \leq 5$: all 3 seeds collapse to 0\% (h=2) or near-0\% (h=5). The transition from catastrophic failure to degraded learning occurs between h=5 and h=10. This is not a trivial ``more context is better'' result; the cliff's sharpness and the threshold effect at h=5 reveal the sign misattribution mechanism's non-linear impact.
153	
154	\begin{table}[h]
155	\centering
156	\caption{Context window h-sweep (step 15 validation success, 3 seeds each).}
157	\label{tab:hsweep}
158	\begin{tabular}{ccccccc}
159	\toprule
160	$h$ & Seed 1 & Seed 2 & Seed 3 & Mean & Std & Collapse Step \\
161	\midrule
162	2 & 0.000 & 0.000 & 0.000 & 0.000 & 0.000 & 4.3 \\
163	5 & 0.030 & 0.000 & 0.016 & 0.015 & 0.015 & 7.0 \\
164	10 & 0.078 & 0.110 & 0.063 & 0.084 & 0.024 & N/A \\
165	20 & 0.190 & 0.220 & 0.170 & 0.193 & 0.025 & N/A \\
166	full & 0.280 & 0.250 & 0.310 & \textbf{0.280} & 0.030 & N/A \\
167	\bottomrule
168	\end{tabular}
169	\end{table}
170	
171	\subsection{Empirical Verification of Sign Misattribution}
172	
173	Table~\ref{tab:sign} provides direct evidence of the sign misattribution mechanism. We log per-window advantages from step-independent training and correlate advantage sign with (a) episode outcome and (b) local action quality (proxied by action validity). The correlation between advantage sign and episode outcome is 0.97 ($p < 10^{-100}$), while the correlation with local quality is 0.04 ($p = 0.38$, not significant). In failed episodes, 94\% of good-action windows receive negative advantage; in successful episodes, 92\% of bad-action windows receive positive advantage.
174	
175	\begin{table}[h]
176	\centering
177	\caption{Sign attribution analysis ($n=3200$ windows from 256 episodes).}
178	\label{tab:sign}
179	\begin{tabular}{lccc}
180	\toprule
181	Condition & $n$ windows & Positive Adv \% & Negative Adv \% \\
182	\midrule
183	Success episode, good action & 420 & 0.98 & 0.02 \\
184	Success episode, bad action & 180 & 0.92 & 0.08 \\
185	Failure episode, good action & 850 & 0.03 & 0.97 \\
186	Failure episode, bad action & 1750 & 0.02 & 0.98 \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	\begin{table}[h]
192	\centering
193	\caption{Correlation between advantage properties and training signals.}
194	\label{tab:correlation}
195	\begin{tabular}{lccc}
196	\toprule
197	Pair & Correlation & $p$-value & Interpretation \\
198	\midrule
199	Sign $\times$ Episode Outcome & 0.97 & $<10^{-100}$ & Sign determined by outcome \\
200	Sign $\times$ Local Action Quality & 0.04 & 0.38 & Sign independent of local quality \\
201	Magnitude $\times$ Window Position & $-0.89$ & $<10^{-50}$ & $\gamma^k$ decay confirmed \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	\subsection{GAE Baseline Comparison}
207	
208	Table~\ref{tab:gae} compares episode-level GRPO against GAE variants and step-independent training. GAE($\lambda=0.95$) achieves 51\% at convergence, 3.2pp above episode-level GRPO (46.8\%). This modest gap confirms that correcting advantage sign is the primary bottleneck: episode-level information (sign correctness) accounts for the majority of improvement over step-independent, while per-token credit refinement via GAE provides secondary gains.
209	
210	\begin{table}[h]
211	\centering
212	\caption{Comparison of credit assignment methods.}
213	\label{tab:gae}
214	\begin{tabular}{lcccc}
215	\toprule
216	Method & Step 15 & Std & Converged & Per-token Adv. Var. \\
217	\midrule
218	Step-independent (h=2) & 0.000 & 0.000 & 0.000 & 0.85 \\
219	Episode-level GRPO & 0.280 & 0.030 & 0.468 & 0.00 \\
220	GAE($\lambda$=1.0, $\gamma$=1.0) & 0.287 & 0.015 & 0.490 & 0.18 \\
221	GAE($\lambda$=0.95, $\gamma$=1.0) & \textbf{0.307} & 0.025 & \textbf{0.510} & 0.42 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	
226	\subsection{Valid Action Bonus Variant}
227	
228	Adding a small valid-action bonus ($+0.05$ per valid action) to episode-level GRPO accelerates plateau breaking (step 12 vs step 25) and improves final success to 52\% (Table~\ref{tab:bonus}). Critically, the same dense reward causes catastrophic reward gaming under step-independent training (action validity reaches 97.5\% but success stays at 0\%), while under episode-level training it safely improves both metrics. This further confirms that the step-independent paradigm, not dense reward itself, is the failure mode.
229	
230	\begin{table}[h]
231	\centering
232	\caption{Episode-level GRPO with and without valid-action bonus.}
233	\label{tab:bonus}
234	\begin{tabular}{ccccc}
235	\toprule
236	Step & Base Success & +Bonus Success & Base Valid & +Bonus Valid \\
237	\midrule
238	5  & 0.250 & 0.300 & 0.450 & 0.550 \\
239	10 & 0.250 & 0.360 & 0.500 & 0.680 \\
240	15 & 0.280 & 0.410 & 0.550 & 0.780 \\
241	20 & 0.300 & 0.470 & 0.610 & 0.840 \\
242	25 & 0.330 & 0.500 & 0.680 & 0.870 \\
243	30 & 0.380 & \textbf{0.520} & 0.730 & 0.880 \\
244	\bottomrule
245	\end{tabular}
246	\end{table}
247	
248	\subsection{Selective Verification Results}
249	
250	\subsubsection{Action-Change Statistics}
251	
252	From the converged always-on agent (320 episodes, 7840 verification steps), 77\% of verifications are confirmatory (no action change). The action-change rate is higher in early steps (0.31) than late steps (0.17), reflecting decreasing uncertainty as episodes progress. Action changes correlate positively with task success (partial $r = 0.31$, $p = 0.003$ after controlling for policy entropy), confirming that action-change is a meaningful signal of verification informativeness rather than noise.
253	
254	\begin{table}[h]
255	\centering
256	\caption{Action-change rate by episode position and entropy stratum.}
257	\label{tab:actionchange}
258	\begin{tabular}{lcccc}
259	\toprule
260	Category & Change Rate & $n$ Steps & Corr. w/ Success & $p$-value \\
261	\midrule
262	Overall & 0.230 & 7840 & 0.28 & -- \\
263	Early (steps 1--8) & 0.310 & 2560 & 0.32 & -- \\
264	Mid (steps 9--16) & 0.220 & 2560 & 0.27 & -- \\
265	Late (steps 17--25) & 0.170 & 2720 & 0.21 & -- \\
266	\midrule
267	Low entropy ($<$0.1) & 0.140 & 105 ep. & 0.25 & 0.020 \\
268	Mid entropy (0.1--0.25) & 0.240 & 120 ep. & 0.33 & 0.005 \\
269	High entropy ($>$0.25) & 0.340 & 95 ep. & 0.29 & 0.010 \\
270	Partial (entropy-controlled) & 0.230 & 320 ep. & \textbf{0.31} & 0.003 \\
271	\bottomrule
272	\end{tabular}
273	\end{table}
274	
275	\subsubsection{Causal Intervention}
276	
277	To confirm that action-change captures verification value causally (not merely correlatively), we compare verification-triggered changes against random action replacement at matched rate (Table~\ref{tab:causal}). Verification-triggered changes achieve 48\% success, while random changes at the same 23\% rate yield only 35\% (below the 37\% no-verification baseline). The 13pp gap demonstrates that verification-triggered changes reflect informed correction, not arbitrary perturbation.
278	
279	\begin{table}[h]
280	\centering
281	\caption{Causal intervention: verification-triggered vs random action changes.}
282	\label{tab:causal}
283	\begin{tabular}{lccc}
284	\toprule
285	Condition & Success & Change Rate & $\Delta$ vs No-Change \\
286	\midrule
287	Verification-triggered & 0.480 & 0.23 & +11pp \\
288	Random at matched rate & 0.350 & 0.23 & $-$2pp \\
289	No change (no verification) & 0.370 & 0.00 & baseline \\
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	\subsubsection{B-IAVR Training and Comparison}
295	
296	Table~\ref{tab:biavr} presents the full comparison. B-IAVR achieves 46.5\% success at 48\% verification rate (62\% relative cost), yielding the highest success-per-cost ratio of 0.75. Compared to always-on verification (48\% success, 100\% cost), B-IAVR trades 1.5pp success for 38\% cost reduction. The learned policy verifies more at early steps (72\%) and less at late steps (28\%), matching the ground-truth action-change distribution. When B-IAVR does verify, 41\% of verifications change the action (vs 23\% for always-on), confirming that the model learned to verify selectively at informative decision points.
297	
298	\begin{table}[h]
299	\centering
300	\caption{Selective verification methods comparison.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e3c2eb3-0ee9-4940-b374-b7ef6a399be9",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "4cf4e1dd-61f7-407c-adf8-667f7eee8f19",
  "sourceToolAssistantUUID": "6e3c2eb3-0ee9-4940-b374-b7ef6a399be9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T12:55:59.412Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FaEysZtmMobqvjDMMaWUp3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf4e1dd-61f7-407c-adf8-667f7eee8f19",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BEXvedSofuNpghC8FG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "175b36a7-30e6-42c6-a5f2-1edf9714bd25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPPYg6KZFF7rGUbbGPb1aJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 36169,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 539
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 36169,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 539,
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

_source line 22 · 2026-05-17T12:55:59.419Z_

<details><summary>↩ Tool result · `toolu_01FaEysZtmMobqvjDMMaWUp3`</summary>

```text
1	@inproceedings{agent-omit2026,
2	  title     = {Agent-Omit: Training Efficient {LLM} Agents for Adaptive Thought and Observation Omission via Agentic {RL}},
3	  author    = {Ning, Yansong and Fang, Jun and Tan, Naiqiang and Liu, Hao},
4	  booktitle = {Proceedings of the International Conference on Machine Learning},
5	  year      = {2026},
6	}
7	
8	@article{choudhury2025agentprm,
9	  title   = {Process Reward Models for {LLM} Agents: Practical Framework and Directions},
10	  author  = {Choudhury, Sanjiban},
11	  journal = {arXiv preprint arXiv:2502.10325},
12	  year    = {2025},
13	}
14	
15	@article{dapo2025,
16	  title   = {{DAPO}: An Open-Source {LLM} Reinforcement Learning System at Scale},
17	  author  = {Yu, Qiying and Zhang, Zheng and Zhu, Ruofei and Yuan, Yufeng and Zuo, Xiaochen and Yue, Yu and Dai, Weinan and Fan, Tiantian and Liu, Gaohong and Liu, Lingjun and Liu, Xin and Lin, Haibin and Lin, Zhiqi and Ma, Bole and Sheng, Guangming and Tong, Yuxuan and Zhang, Chi and Zhang, Mofan and Zhang, Wang and Zhu, Hang and Zhu, Jinhua and Chen, Jiaze and Chen, Jiangjie and Wang, Chengyi and Yu, Hongli and Song, Yuxuan and Wei, Xiangpeng and Zhou, Hao and Liu, Jingjing and Ma, Wei-Ying and Zhang, Ya-Qin and Yan, Lin and Qiao, Mu and Wu, Yonghui and Wang, Mingxuan},
18	  journal = {arXiv preprint arXiv:2503.14476},
19	  year    = {2025},
20	}
21	
22	@inproceedings{digiRL2024,
23	  title     = {{DigiRL}: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning},
24	  author    = {Bai, Hao and Zhou, Yifei and Cemri, Mert and Pan, Jiayi and Suhr, Alane and Levine, Sergey and Kumar, Aviral},
25	  booktitle = {Advances in Neural Information Processing Systems},
26	  year      = {2024},
27	}
28	
29	@inproceedings{du2025thinkless,
30	  title     = {Thinkless: {LLM} Learns When to Think},
31	  author    = {Fang, Gongfan and Ma, Xinyin and Wang, Xinchao},
32	  booktitle = {Advances in Neural Information Processing Systems},
33	  year      = {2025},
34	}
35	
36	@inproceedings{feng2025gigpo,
37	  title     = {{GiGPO}: Group-in-Group Policy Optimization for {LLM} Agent Training},
38	  author    = {Feng, Lang and Xue, Zhenghai and Liu, Tingcong and An, Bo},
39	  booktitle = {Advances in Neural Information Processing Systems},
40	  year      = {2025},
41	}
42	
43	@article{hcapo2026,
44	  title   = {{HCAPO}: Hindsight Credit Assignment for Long-Horizon {LLM} Agents},
45	  author  = {Tan, Hui-Ze and Yang, Xiao-Wen and Chen, Hao and Shao, Jie-Jing and Wen, Yi and Shen, Yuteng and Luo, Weihong and Du, Xiku and Guo, Lan-Zhe and Li, Yu-Feng},
46	  journal = {arXiv preprint arXiv:2603.08754},
47	  year    = {2026},
48	}
49	
50	@article{kamoi2024self-correction-survey,
51	  title   = {When Can {LLMs} Actually Correct Their Own Mistakes? {A} Critical Survey of Self-Correction of {LLMs}},
52	  author  = {Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui},
53	  journal = {arXiv preprint arXiv:2406.01297},
54	  year    = {2024},
55	}
56	
57	@inproceedings{kim2025reflact,
58	  title     = {{ReflAct}: World-Grounded Decision Making in {LLM} Agents via Goal-State Reflection},
59	  author    = {Kim, Jeonghye and Rhee, Sojeong and Kim, Minbeom and Kim, Dohyung and Lee, Sangmook and Sung, Youngchul and Jung, Kyomin},
60	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
61	  year      = {2025},
62	}
63	
64	@article{li2025sorl,
65	  title   = {{SORL}: Stabilizing Off-Policy {RL} for Long-Horizon Agent Training},
66	  author  = {Li, Chenliang and Elmahdy, Adel and Boyd, Alex and Wang, Zhongruo and Zeng, Siliang and Garcia, Alfredo and Bhatia, Parminder and Kass-Hout, Taha and Xiao, Cao and Hong, Mingyi},
67	  journal = {arXiv preprint arXiv:2511.20718},
68	  year    = {2025},
69	}
70	
71	@article{long2026selfverification,
72	  title   = {Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in {LLM} Reasoning},
73	  author  = {Long, Quanyu and Jiang, Kai Jie and Chen, Jianda and Guo, Xu and Gan, Leilei and Wang, Wenya},
74	  journal = {arXiv preprint arXiv:2602.03485},
75	  year    = {2026},
76	}
77	
78	@article{ragen2025,
79	  title   = {{RAGEN}: Understanding Self-Evolution in {LLM} Agents via Multi-Turn Reinforcement Learning},
80	  author  = {Wang, Zihan and Wang, Kangrui and Wang, Qineng and Zhang, Pingyue and Li, Linjie and Yang, Zhengyuan and Jin, Xing and Yu, Kefan and Nguyen, Minh Nhat and Liu, Licheng and Gottlieb, Eli and Lu, Yiping and Cho, Kyunghyun and Wu, Jiajun and Li, Fei-Fei and Wang, Lijuan and Choi, Yejin and Li, Manling},
81	  journal = {arXiv preprint arXiv:2504.20073},
82	  year    = {2025},
83	}
84	
85	@inproceedings{schulman2016gae,
86	  title     = {High-Dimensional Continuous Control Using Generalized Advantage Estimation},
87	  author    = {Schulman, John and Moritz, Philipp and Levine, Sergey and Jordan, Michael and Abbeel, Pieter},
88	  booktitle = {Proceedings of the International Conference on Learning Representations},
89	  year      = {2016},
90	}
91	
92	@article{schulman2017ppo,
93	  title   = {Proximal Policy Optimization Algorithms},
94	  author  = {Schulman, John and Wolski, Filip and Dhariwal, Prafulla and Radford, Alec and Klimov, Oleg},
95	  journal = {arXiv preprint arXiv:1707.06347},
96	  year    = {2017},
97	}
98	
99	@article{selfbudgeter2026,
100	  title   = {{SelfBudgeter}: Adaptive Token Allocation for Efficient {LLM} Reasoning},
101	  author  = {Li, Zheng and Dong, Qingxiu and Ma, Jingyuan and Zhang, Di and Jia, Kai and Sui, Zhifang},
102	  journal = {arXiv preprint arXiv:2505.11274},
103	  year    = {2025},
104	}
105	
106	@article{selfguide2026,
107	  title   = {Co-Evolution of Policy and Internal Reward for Language Agents},
108	  author  = {Wang, Xinyu and Wu, Hanwei and Song, Jingwei and Zhang, Shuyuan and Zhang, Jiayi and Kong, Fanqi and Kwok, Tung Sum Thomas and Chang, Xiao-Wen and Luo, Yuyu and Wu, Chenglin and Liu, Bang},
109	  journal = {arXiv preprint arXiv:2604.03098},
110	  year    = {2026},
111	}
112	
113	@article{shao2024deepseekmath,
114	  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},
115	  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
116	  journal = {arXiv preprint arXiv:2402.03300},
117	  year    = {2024},
118	}
119	
120	@article{sherlock2025,
121	  title   = {Sherlock: Reliable and Efficient Agentic Workflow Execution},
122	  author  = {Ro, Yeonju and Qiu, Haoran and Goiri, {\'\I}{\~n}igo and Fonseca, Rodrigo and Bianchini, Ricardo and Akella, Aditya and Wang, Zhangyang and Erez, Mattan and Choukse, Esha},
123	  journal = {arXiv preprint arXiv:2511.00330},
124	  year    = {2025},
125	}
126	
127	@article{skillmaster2026,
128	  title   = {{SkillMaster}: Toward Autonomous Skill Mastery in {LLM} Agents},
129	  author  = {Yang, Min and Piao, Jinghua and Xia, Xu and Lan, Xiaochong and Chen, Jiaju and Gong, Yongshun and Li, Yong},
130	  journal = {arXiv preprint arXiv:2605.08693},
131	  year    = {2026},
132	}
133	
134	@inproceedings{spear2025,
135	  title     = {Learn the Ropes, Then Trust the Wins: Self-Imitation with Progressive Exploration for Agentic Reinforcement Learning},
136	  author    = {Qin, Yulei and Tan, Xiaoyu and He, Zhengbao and Li, Gang and Lin, Haojia and Li, Zongyi and Xu, Zihan and Shi, Yuchen and Cai, Siqi and Rui, Renting and Cai, Shaofei and Cai, Yuzheng and Zhang, Xuan and Ye, Sheng and Li, Ke and Sun, Xing},
137	  booktitle = {Proceedings of the International Conference on Learning Representations},
138	  year      = {2026},
139	}
140	
141	@article{sutton1988td,
142	  title   = {Learning to Predict by the Methods of Temporal Differences},
143	  author  = {Sutton, Richard S.},
144	  journal = {Machine Learning},
145	  volume  = {3},
146	  number  = {1},
147	  pages   = {9--44},
148	  year    = {1988},
149	}
150	
151	@inproceedings{tie2025correctbench,
152	  title     = {Can {LLMs} Correct Themselves? {A} Benchmark of Self-Correction in {LLMs}},
153	  author    = {Tie, Guiyao and Yuan, Zenghui and Zhao, Zeli and Hu, Chaoran and Gu, Tianhe and Zhang, Ruihang and Zhang, Sizhe and Wu, Junran and Tu, Xiaoyue and Jin, Ming and Wen, Qingsong and Chen, Lixing and Zhou, Pan and Sun, Lichao},
154	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
155	  year      = {2025},
156	}
157	
158	@inproceedings{tu2025autothink,
159	  title     = {Learning When to Think: Shaping Adaptive Reasoning in {R1}-Style Models via Multi-Stage {RL}},
160	  author    = {Tu, Songjun and Lin, Jiahao and Zhang, Qichao and Tian, Xiangyu and Li, Linjing and Lan, Xiangyuan and Zhao, Dongbin},
161	  booktitle = {Advances in Neural Information Processing Systems},
162	  year      = {2025},
163	}
164	
165	@inproceedings{verifiagent2025,
166	  title     = {{VerifiAgent}: A Unified Verification Agent in Language Model Reasoning},
167	  author    = {Han, Jiuzhou and Buntine, Wray and Shareghi, Ehsan},
168	  booktitle = {Findings of the Conference on Empirical Methods in Natural Language Processing},
169	  year      = {2025},
170	}
171	
172	@inproceedings{wan2025derailer-rerailer,
173	  title     = {Derailer-Rerailer: Adaptive Verification for Efficient and Reliable {LM} Reasoning},
174	  author    = {Wan, Guangya and Wu, Yuqi and Wang, Hao and Zhao, Shengming and Chen, Jie and Li, Sheng},
175	  booktitle = {Findings of the Annual Meeting of the Association for Computational Linguistics},
176	  year      = {2025},
177	}
178	
179	@inproceedings{wei2025webagent-r1,
180	  title     = {{WebAgent-R1}: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning},
181	  author    = {Wei, Zhepei and Yao, Wenlin and Liu, Yao and Zhang, Weizhi and Lu, Qin and Qiu, Liang and Yu, Changlong and Xu, Puyang and Zhang, Chao and Yin, Bing and Yun, Hyokun and Li, Lihong},
182	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
183	  year      = {2025},
184	}
185	
186	@article{williams1992reinforce,
187	  title   = {Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning},
188	  author  = {Williams, Ronald J.},
189	  journal = {Machine Learning},
190	  volume  = {8},
191	  number  = {3--4},
192	  pages   = {229--256},
193	  year    = {1992},
194	}
195	
196	@inproceedings{xi2025agentprm,
197	  title     = {{AgentPRM}: Process Reward Models for {LLM} Agents via Step-Wise Promise and Progress},
198	  author    = {Xi, Zhiheng and Liao, Chenyang and Li, Guanyu and Yang, Yajie and Chen, Wenxiang and Zhang, Zhihao and Wang, Binghai and Jin, Senjie and Zhou, Yuhao and Guan, Jian and Wu, Wei and Ji, Tao and Gui, Tao and Zhang, Qi and Huang, Xuanjing},
199	  booktitle = {Proceedings of the {ACM} Web Conference},
200	  year      = {2026},
201	}
202	
203	@article{yang2026ares,
204	  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},
205	  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},
206	  journal = {arXiv preprint arXiv:2603.07915},
207	  year    = {2026},
208	}
209	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "175b36a7-30e6-42c6-a5f2-1edf9714bd25",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "a70da2e0-c001-495a-acf8-00a2a078f562",
  "sourceToolAssistantUUID": "175b36a7-30e6-42c6-a5f2-1edf9714bd25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T12:56:03.987Z_

<details open><summary>🔧 Tool call — Read · `toolu_018U8Q14j4MxftmLsk7D8J9v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/best/paper.tex",
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a70da2e0-c001-495a-acf8-00a2a078f562",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BEnH6d3PKLSqRp1hd4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06ec83a9-5692-4759-ba80-e850c27f38a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJNHLC8ejEBzDkux1KyG5d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11932,
      "cache_read_input_tokens": 36708,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 36708,
          "cache_creation_input_tokens": 11932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11932,
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

_source line 24 · 2026-05-17T12:56:03.996Z_

<details><summary>↩ Tool result · `toolu_018U8Q14j4MxftmLsk7D8J9v`</summary>

```text
300	\caption{Selective verification methods comparison.}
301	\label{tab:biavr}
302	\begin{tabular}{lcccc}
303	\toprule
304	Method & Success & Verify Rate & Relative Cost & Success/Cost \\
305	\midrule
306	Always-on & 0.480 & 1.00 & 1.00 & 0.48 \\
307	\textbf{B-IAVR (ours)} & \underline{0.465} & 0.48 & 0.62 & \textbf{0.75} \\
308	Confidence-threshold & 0.440 & 0.55 & 0.67 & 0.66 \\
309	Random-0.5 & 0.430 & 0.50 & 0.63 & 0.68 \\
310	No-verify & 0.370 & 0.00 & 0.52 & 0.71 \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\subsubsection{Reward Signal Ablation}
316	
317	Table~\ref{tab:reward_ablation} ablates the reward signal for selective verification training. Action-change reward produces the best Pareto point. Confidence-based reward (using token entropy as verification trigger) underperforms because low entropy does not reliably indicate correct actions. Random-trigger reward lacks informative gradient for distinguishing useful from wasteful verification.
318	
319	\begin{table}[h]
320	\centering
321	\caption{Reward signal ablation for selective verification.}
322	\label{tab:reward_ablation}
323	\begin{tabular}{lcccc}
324	\toprule
325	Reward Signal & Success & Verify Rate & Cost & Success/Cost \\
326	\midrule
327	Action-change (ours) & \textbf{0.465} & 0.48 & 0.62 & \textbf{0.75} \\
328	Confidence-based & 0.440 & 0.53 & 0.65 & 0.68 \\
329	Random trigger & 0.420 & 0.51 & 0.64 & 0.66 \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	\subsubsection{Comparison with ARES}
335	
336	We reproduce ARES (SFT router with continuous effort allocation) on the same model and environment (Table~\ref{tab:ares}). B-IAVR achieves +3.5pp higher success at 10pp lower cost. ARES's SFT router is more conservative (60\% verify rate) because its training data biases toward ``verify when in doubt,'' leading to over-verification without commensurate success gains.
337	
338	\begin{table}[h]
339	\centering
340	\caption{Head-to-head comparison with ARES.}
341	\label{tab:ares}
342	\begin{tabular}{lcccc}
343	\toprule
344	Method & Success & Verify Rate & Relative Cost & Approach \\
345	\midrule
346	B-IAVR (ours) & \textbf{0.465} & 0.48 & \textbf{0.62} & RL, action-change reward \\
347	ARES (reproduced) & 0.430 & 0.60 & 0.72 & SFT router \\
348	Always-on & 0.480 & 1.00 & 1.00 & No selection \\
349	\bottomrule
350	\end{tabular}
351	\end{table}
352	
353	\subsection{Generalization}
354	
355	\subsubsection{Cross-Environment Transfer}
356	
357	Table~\ref{tab:transfer} validates the dual-mechanism finding on ScienceWorld. Episode-level GRPO achieves 32\% vs 8\% for step-independent (4$\times$ improvement). ScienceWorld's longer episodes (avg 35 steps) and larger action space make training harder overall, but the relative advantage of episode-level training is consistent.
358	
359	\begin{table}[h]
360	\centering
361	\caption{Cross-environment validation.}
362	\label{tab:transfer}
363	\begin{tabular}{lcccc}
364	\toprule
365	Environment & Episode-level & Step-independent & Ratio & Avg Steps \\
366	\midrule
367	ALFWorld & 0.480 & 0.000 & $\infty$ & 25 \\
368	ScienceWorld & 0.320 & 0.080 & 4.0$\times$ & 35 \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	\subsubsection{Model Scaling}
374	
375	Table~\ref{tab:scaling} shows results with Qwen3-7B. Episode-level GRPO reaches 58\% (vs 48\% at 1.7B, +10pp from stronger instruction following and larger capacity). Step-independent with 7B achieves only 5\%, confirming that the dual-mechanism failure is an algorithmic problem that model scale does not resolve.
376	
377	\begin{table}[h]
378	\centering
379	\caption{Model size scaling.}
380	\label{tab:scaling}
381	\begin{tabular}{lccc}
382	\toprule
383	Model & Episode-level & Step-independent & Ratio \\
384	\midrule
385	Qwen3-1.7B & 0.480 & 0.000 & $\infty$ \\
386	Qwen3-7B & \textbf{0.580} & 0.050 & 11.6$\times$ \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	\subsection{Per-Task Analysis}
392	
393	Table~\ref{tab:pertask} breaks down performance by ALFWorld task type. Success correlates strongly with task complexity (episode length; $r = -0.92$). Simpler tasks (pick, 18 steps) reach 58\%, while complex tasks (pick\_two, 32 steps) reach 33\%. Step-independent training collapses entirely on tasks requiring more than 20 steps, confirming the dual-mechanism's severity scales with horizon length.
394	
395	\begin{table}[h]
396	\centering
397	\caption{Per-task-type breakdown (episode-level GRPO, converged).}
398	\label{tab:pertask}
399	\begin{tabular}{lcccc}
400	\toprule
401	Task Type & $n$ Tasks & Success & Avg Steps & Step-indep. (est.) \\
402	\midrule
403	pick & 22 & \textbf{0.580} & 18 & 0.10 \\
404	clean & 18 & 0.520 & 22 & 0.03 \\
405	heat & 15 & 0.480 & 24 & 0.00 \\
406	cool & 14 & 0.450 & 25 & 0.00 \\
407	examine & 10 & 0.400 & 28 & 0.00 \\
408	pick\_two & 12 & 0.330 & 32 & 0.00 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	\section{Discussion}
414	
415	\paragraph{Why does the community default to step-independent training?}
416	Three factors explain this: (1) LLM context window limitations historically forced windowed processing; (2) token-level training (SFT, RLHF) established the convention of per-segment optimization; (3) framework implementations (RAGEN) made step-independent the path of least resistance. Our results suggest this default should be reconsidered for multi-turn agent training.
417	
418	\paragraph{Relationship to GAE.}
419	GAE provides finer-grained credit (per-token) via learned value functions and achieves +3.2pp over episode-level GRPO at convergence. However, episode-level GRPO requires no critic, no value function training, and achieves 92\% of GAE's performance. For practitioners, episode-level GRPO is a simple configuration change in existing frameworks.
420	
421	\paragraph{Limitations.}
422	Our evaluation uses two text-based environments (ALFWorld, ScienceWorld). The selective verification results apply to binary verify/skip decisions; extending to continuous effort allocation remains future work. The absolute performance (48\%) leaves a gap to methods using expert demonstrations (Self-Guide, 72.7\%), reflecting the from-scratch RL vs expert-guided paradigm difference.
423	
424	\section{Conclusion}
425	
426	We identified a dual mechanism (policy information loss and advantage sign misattribution) causing catastrophic failure of step-independent RL training for multi-turn LLM agents. Episode-level GRPO resolves both issues, enabling reliable training (46.8\% $\pm$ 2.4\%, 5 seeds). Building on this foundation, B-IAVR learns selective verification using action-change as an intrinsic reward, reducing verification cost by 52\% with minimal performance loss (1.5pp). The success-per-cost ratio of 0.75 represents the best efficiency among all compared methods. These results demonstrate that learning \emph{when} to verify is both feasible and practical for interactive agents operating under computational constraints.
427	
428	\bibliographystyle{plain}
429	\begin{thebibliography}{10}
430	
431	\bibitem{ragen2025}
432	RAGEN: Training agents with GRPO for multi-turn interactive tasks. 2025.
433	
434	\bibitem{selfguide2026}
435	Self-Guide: Self-verification training for interactive LLM agents via expert demonstrations. 2026.
436	
437	\bibitem{ares2026}
438	ARES: Adaptive reasoning effort scheduling with continuous compute allocation. arXiv:2603.07915, 2026.
439	
440	\bibitem{thinkless2025}
441	Thinkless: RL-trained control tokens for adaptive reasoning depth. NeurIPS, 2025.
442	
443	\bibitem{reflact2025}
444	ReflAct: Prompting-based reflection for LLM agents. EMNLP, 2025.
445	
446	\bibitem{grpo2024}
447	DeepSeekMath: Group relative policy optimization for mathematical reasoning. 2024.
448	
449	\bibitem{alfworld2021}
450	ALFWorld: Aligning text and embodied environments for interactive learning. ICLR, 2021.
451	
452	\bibitem{scienceworld2022}
453	ScienceWorld: Is your agent smarter than a 5th grader? EMNLP, 2022.
454	
455	\bibitem{gae2016}
456	Schulman et al. High-dimensional continuous control using generalized advantage estimation. ICLR, 2016.
457	
458	\bibitem{qwen2024}
459	Qwen2.5 technical report. 2024.
460	
461	\end{thebibliography}
462	
463	\end{document}
464	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06ec83a9-5692-4759-ba80-e850c27f38a1",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "0e7e7f06-d9bc-4696-ae97-178c01c235d4",
  "sourceToolAssistantUUID": "06ec83a9-5692-4759-ba80-e850c27f38a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-17T12:56:06.834Z_

Now let me also check the earlier dream review report to understand how reviewers previously evaluated this work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e7e7f06-d9bc-4696-ae97-178c01c235d4",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BF86TquKSzi5TqhxbN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "125114b2-da61-4a57-a5e8-ac697fd67b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BzP11tu8DozTGfWX9wXzR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3083,
      "cache_read_input_tokens": 48640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3083,
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

_source line 26 · 2026-05-17T12:56:08.230Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NDsMSCZA74houWF8DauZ9V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/median/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "125114b2-da61-4a57-a5e8-ac697fd67b97",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BF86TquKSzi5TqhxbN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc6870d9-035e-49b2-b879-16e747beae1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BzP11tu8DozTGfWX9wXzR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3083,
      "cache_read_input_tokens": 48640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3083,
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

_source line 27 · 2026-05-17T12:56:08.237Z_

<details><summary>↩ Tool result · `toolu_01NDsMSCZA74houWF8DauZ9V`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage{xcolor}
10	\usepackage{enumitem}
11	
12	\title{Diagnosing Step-Independent RL Failure in Multi-Turn LLM Agents:\\Sign Misattribution, Information Loss, and Selective Verification}
13	
14	\author{Anonymous}
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Training Large Language Model (LLM) agents with Reinforcement Learning (RL) for multi-turn interactive tasks remains challenging. We identify a dual failure mechanism in the widely adopted step-independent training paradigm: (1) policy information loss from truncated context windows prevents learning cross-step strategies, and (2) advantage sign misattribution causes per-window gradients to reflect episode outcomes rather than local action quality, with correlation $r=0.87$ between advantage sign and episode success. Through systematic ablation across context window sizes, we demonstrate a severe degradation zone below $h=5$ steps (success collapses from 18\% to 2\%) and show that episode-level GRPO eliminates both failure modes, achieving 30.6$\pm$5.9\% success versus 3$\pm$2\% for step-independent training on ALFWorld. We position episode-level training as a minimum viable fix rather than an optimal solution: GAE-based credit assignment further improves performance by 8 percentage points, confirming that finer-grained credit has additional value. As a preliminary downstream application, we train a selective verification policy using action-change as an intrinsic reward signal, achieving 28\% cost reduction with a modest 4 percentage point performance trade-off. Our diagnostic analysis generalizes across environments (ScienceWorld, 4.5$\times$ improvement) and model scales (1.7B to 7B parameters).
22	\end{abstract}
23	
24	\section{Introduction}
25	
26	LLM-based interactive agents that operate over multiple turns in grounded environments have become a central research direction. Training these agents with RL promises to improve their task completion without relying on expert demonstrations. However, the default training paradigm adopted by recent agent RL frameworks processes each episode as independent fixed-length windows of $h$ steps, optimizing each window separately with its own advantage estimate.
27	
28	This step-independent paradigm originates from practical constraints: transformer context windows are finite, and token-level training infrastructure naturally segments long trajectories. Yet its consequences for multi-turn agent training have not been systematically examined. We find that step-independent training catastrophically fails on tasks requiring more than a few coordinated decisions.
29	
30	We diagnose two mechanisms driving this failure. First, policy information loss: a window of $h$ steps cannot represent cross-step strategies such as ``explore drawer 1, then navigate to countertop.'' Second, and more critically, advantage sign misattribution: in step-independent training with discounted returns, the sign of each window's advantage is predominantly determined by overall episode success ($r=0.87$ with outcome) rather than local action quality ($r=0.12$). Good actions in failed episodes receive negative advantages and are suppressed; poor actions in successful episodes receive positive advantages and are reinforced.
31	
32	Episode-level training, where the entire trajectory is treated as a single GRPO sample with shared advantage, eliminates both pathologies. All tokens receive the same advantage sign (no cross-window misattribution), and the full episode context is available to the policy. We emphasize that this is a minimum viable fix: it resolves the sign problem but still assigns uniform credit across all tokens. GAE with a learned critic provides finer per-token credit and outperforms episode-level GRPO by 8 percentage points, confirming room for improvement.
33	
34	Building on the diagnostic foundation, we explore a preliminary application: training the agent to selectively verify its actions rather than always verifying. We use action-change rate (whether verification leads to a behavioral change) as an intrinsic reward signal for verification informativeness. The resulting policy reduces verification cost by 28\% with a 4 percentage point performance trade-off relative to always-on verification.
35	
36	Our contributions are:
37	\begin{itemize}[nosep]
38	\item A systematic diagnosis of dual failure mechanisms (sign misattribution + information loss) in step-independent RL for multi-turn LLM agents, supported by mechanistic measurements and controlled ablations.
39	\item Empirical characterization of the degradation boundary (context window $h$-sweep) and demonstration that episode-level GRPO serves as a zero-engineering-cost fix, with GAE providing an upper bound.
40	\item Preliminary evidence that learned selective verification, trained via action-change reward on top of episode-level agents, can reduce verification cost while maintaining most task performance.
41	\item Generalization evidence across environments (ALFWorld, ScienceWorld) and model scales (1.7B, 7B).
42	\end{itemize}
43	
44	\section{Related Work}
45	
46	\paragraph{RL for LLM Agents.}
47	RAGEN introduced GRPO-based training for interactive LLM agents, using a step-independent paradigm where episodes are segmented into fixed-length windows. DeepSeek-R1 and related work apply GRPO to single-turn reasoning tasks where the step-independent issue does not arise. Our work identifies why extending these methods to multi-turn settings fails and provides a diagnostic framework rather than a new algorithm.
48	
49	\paragraph{Credit Assignment in Long-Horizon RL.}
50	The tension between episode-level and step-level credit assignment is well-studied in classical RL. GAE provides a principled interpolation via the $\lambda$ parameter. In LLM agent training, this tension manifests differently because GRPO is inherently bandit-style (no explicit temporal discount), yet framework implementations introduce $\gamma$-discounted per-window returns. We connect this implementation detail to the observed sign misattribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc6870d9-035e-49b2-b879-16e747beae1c",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "cee43fc8-e6db-4192-bea8-74ac4bb49963",
  "sourceToolAssistantUUID": "bc6870d9-035e-49b2-b879-16e747beae1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T12:56:08.532Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MmcqW2bHgfWpcyQDUU6hit`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cee43fc8-e6db-4192-bea8-74ac4bb49963",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BF86TquKSzi5TqhxbN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cceffbf-00b0-4eae-8542-aa5439f4a4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BzP11tu8DozTGfWX9wXzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3083,
      "cache_read_input_tokens": 48640,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 48640,
          "cache_creation_input_tokens": 3083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3083,
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

_source line 29 · 2026-05-17T12:56:08.550Z_

<details><summary>↩ Tool result · `toolu_01MmcqW2bHgfWpcyQDUU6hit`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml\", \"content\": \"_next_id: 60\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:33 UTC\\n  summary: MVP 选择 ALFWorld + Qwen3-1.7B 单环境验证 B-IAVR 核心假设\\n  rationale: ALFWorld 离散动作空间使 action_changed 信号最清晰，semantic canonicalization 简单（verb,object,receptacle三元组）。Qwen3-1.7B\\n    有充分 headroom（+8.6pp on ALFWorld）。MVP 只需验证\\\"agent 能学会选择性验证\\\"这一核心假设，不需要跨环境/跨模型。2×GPU\\n    足够 1.7B+LoRA 训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 18:39 UTC\\n  summary: Phase A 使用全量微调（非 LoRA），匹配 Self-Guide 原始论文设置\\n  rationale: Self-Guide 原文用全量微调 GRPO。1.7B 模型在 94GB VRAM 下全量微调显存仅 38.5GB，完全可行。匹配 baseline\\n    设置确保公平对比。IDEA_BRIEF 提及 LoRA 是基于 H100 80GB 的资源估算，RTX PRO 6000 94GB 无需节省。\\n  related_experiments:\\n  - exp_id: exp_001\\n    role: Phase A baseline\\n    result: running\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 23:55 UTC\\n  summary: Kill exp003，Phase A bootstrap 失败确认，等待 invalid action 根因诊断后决定修复方向\\n  rationale: 'exp003 step 1: invalid_action=95.3%, pg_loss≈0, 每步 1.6h（100步=160h）。GRPO\\n    从 0.125% valid action 中无法获得有效学习信号。Qwen3 无独立 Instruct 版，Plan B 失效。需先诊断 invalid\\n    action 根因（格式冲突 / token 问题 / prompt 不兼容）再选修复路径。'\\n  related_experiments:\\n  - exp_id: exp003\\n    role: primary\\n    result: failed - bootstrap failure, 95% invalid actions, pg_loss≈0\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 00:10 UTC\\n  summary: 采用方案 A（修改解析器适配 Qwen3 格式）+ prompt 增强 + 速度优化，解决 bootstrap 失败\\n  rationale: 根因确认：Qwen3-1.7B 原生输出 &lt;think>...&lt;/think> 后直接跟自然语言，不生成 &lt;answer> 标签。RAGEN\\n    解析器正则要求 &lt;answer> 导致 95% invalid。方案 A 最快（1-2h 改代码）、最低风险（不换模型不加训练阶段），同时优化速度（关闭 collapse\\n    multi_turn 省 35% 步耗时 + 减 traj/step）。\\n  related_experiments:\\n  - exp_id: exp003\\n    role: diagnostic\\n    result: '32/32 samples confirm: no &lt;answer> tag in Qwen3 output'\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 02:56 UTC\\n  summary: exp007 borderline 但不 pivot SFT，提高 LR 到 5e-6 重跑 GRPO\\n  rationale: exp007 step 10 action_is_valid=8.35%，技术上触发预设 kill 条件（<10%），但：(1) 趋势明确上升\\n    4.01%→8.35%（+0.48pp/step），线性外推 ~step 14 即突破 10%；(2) success 从 0%→6.25%，GRPO 确实在学习；(3)\\n    manager_invalid 6.46%→1.56%，解析器修复有效；(4) 崩溃是 /tmp 磁盘满（基础设施），非算法失败；(5) SFT warmup\\n    需额外收集 expert trajectories + 训练周期，开销大。因此override kill 条件，选择提高 LR（1e-6→5e-6）重跑 GRPO\\n    30 步，save_freq=5，同时修复所有基础设施问题（RAY_TMPDIR、/tmp 清理）。新 kill 条件：step 10 action_is_valid\\n    < 15%（因 LR 提高 5x，预期收敛更快）。\\n  related_experiments:\\n  - exp_id: exp007\\n    role: evidence\\n    result: step 10 action_is_valid=8.35%, success=6.25%, 因磁盘满崩溃于 step 11, checkpoint\\n      全部丢失\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 03:02 UTC\\n  summary: 撤回 exp008 (LR 5e-6)，改用 SFT warmup 再接 GRPO\\n  rationale: Agent 正确指出 action_is_valid 低的根因不是 LR 不够高，而是 Qwen3-1.7B 缺乏 ALFWorld 命令语义知识——92%\\n    的动作语法正确但语义无效（不是合法 ALFWorld 命令）。提高 LR 只能加速已有信号的收敛，无法从根本解决命令词汇缺失。SFT warmup 直接教模型\\n    ALFWorld 命令格式和语义，GRPO 再优化策略，是更高效的路径。SFT 计划已就绪（artifacts/sft_warmup_plan.md），总成本\\n    ~8h（SFT 2h + GRPO 6h），可接受。\\n  related_experiments:\\n  - exp_id: exp007\\n    role: evidence\\n    result: 10 步 action_is_valid 仅 8.35%，语法正确但语义无效，指向命令知识缺失而非学习速度问题\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 05:40 UTC\\n  summary: Kill exp011，改 reward function（连续score+降format penalty+group_size 16），从\\n    step 5 checkpoint 恢复\\n  rationale: Reward 分析确认：format_penalty(-0.1/turn)在零成功 group 中劫持 GRPO 梯度，模型只学格式不学任务（action_is_valid\\n    68% + success 0%）。A1 连续 score 给部分完成的轨迹提供梯度信号；A2 降 format_penalty 到 -0.01 避免淹没任务信号；B1\\n    group_size 8→16 提高正信号 group 比例（32%→53%）。从 step 5 恢复因其仍有 1.6% success 残余。\\n  related_experiments:\\n  - exp_id: exp010\\n    role: evidence\\n    result: failed - reward analysis revealed format penalty hijacking GRPO gradient\\n  - exp_id: exp011\\n    role: killed\\n    result: same reward config as exp010, will repeat collapse pattern\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 05:41 UTC\\n  summary: Reviewer 确认 exp010 reward shaping 分析正确；A2(降 format_penalty)为 P0，A1(进度奖励)需先验证\\n    infos[\\\"score\\\"] 粒度\\n  rationale: Reviewer 独立验证了代码引用和根因诊断。新发现：env.py:137 未请求 score=True，AlfWorld 不同任务类型的\\n    score 粒度未知。A2（format_penalty→0 或 -0.01）风险最低——KL loss 已提供格式压力（SFT 模型 90% valid），penalty\\n    冗余且有害。exp011 从 step 10 恢复无 reward 修改=浪费算力，已在 D007 中 kill。\\n  related_experiments:\\n  - exp_id: exp010\\n    role: analysis_source\\n    result: failed\\n  - exp_id: exp011\\n    role: killed\\n    result: wasteful_resume_from_step10\\n  depends_on: []\\n- id: D009\\n  date: 2026-05-14 06:34 UTC\\n  summary: 强制 pre-flight checklist：每次实验提交前必须验证入口点、磁盘、参数兼容性、checkpoint 路径\\n  rationale: 18 个实验仅 1 成功，多数失败为可避免的工程问题（错误入口点、磁盘满、格式不兼容）。exp012 再次因用错入口点（agent_proxy\\n    vs train.py）失败。引入 pre-flight checklist 防止此类重复失败。\\n  related_experiments:\\n  - exp_id: exp012\\n    role: trigger\\n    result: failed - wrong entry point\\n  - exp_id: exp007\\n    role: prior failure\\n    result: failed - disk full\\n  - exp_id: exp003\\n    role: prior failure\\n    result: failed - format incompatibility\\n  depends_on:\\n  - D006\\n  - D008\\n- id: D010\\n  date: 2026-05-14 07:41 UTC\\n  summary: Kill exp012b（零梯度死锁），引入 dense reward shaping 设计 exp013，下调 MVP pass 标准至 success\\n    ≥ 20%\\n  rationale: 两位 Reviewer 独立确认：exp012b step 6-7 pg_loss=0, success=0%, pass@16=0%,\\n    advantages 全零。format_penalty=0 消除了组内 reward 方差，GRPO 无梯度信号。继续跑浪费 ~10.6 GPU-hours。核心问题是\\n    sparse binary reward + 弱基础模型 + GRPO 方差依赖 = 冷启动死锁。方向（SFT→GRPO）未被证伪，但需要 reward shaping\\n    打破死锁。76% MVP 标准不现实（Self-Guide 是非 RL 方法），下调至 20% 证明 GRPO 能学到有意义策略。\\n  related_experiments:\\n  - exp_id: exp012b\\n    role: trigger\\n    result: zero gradient deadlock - pg_loss=0, success=0%\\n  - exp_id: exp010\\n    role: comparison\\n    result: format_penalty=-0.1 had success=4.7% but gradient hijacking\\n  - exp_id: exp008_sft\\n    role: baseline\\n    result: SFT taught format compliance but not task strategy\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 07:41 UTC\\n  summary: Kill exp012b（零梯度死锁确认），引入 dense reward shaping，下调 MVP pass 标准至 success ≥\\n    20%\\n  rationale: Reviewer critical 确认：format_penalty=0 + binary reward + 0% success =\\n    零梯度死锁（pg_loss=0.0），模型完全不更新。exp010 的 format_penalty=-0.1 至少创造了 reward 方差但方向错误。根本问题是\\n    ALFWorld sparse binary reward + GRPO 在基础模型太弱时无法工作。解决方案：加 step-level dense reward\\n    shaping（子目标奖励），方向正确且创造梯度信号。76% 目标来自 Self-Guide 论文的非 RL 方法，30 步 GRPO 不可达，MVP pass\\n    下调至 success ≥ 20% + 明确上升趋势。\\n  related_experiments:\\n  - exp_id: exp012b\\n    role: trigger\\n    result: step 6-7 train success=0%, pg_loss=0.0, 零梯度\\n  - exp_id: exp010\\n    role: 对照\\n    result: format_penalty=-0.1 时 step 1 success=4.7% 但后续崩塌\\n  - exp_id: exp008_sft\\n    role: 基础\\n    result: SFT warmup 成功，action_is_valid 68-72%\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D012\\n  date: 2026-05-14 12:40 UTC\\n  summary: 'exp013f negative: dense reward gaming — 下一步 success-gated bonus + 降低 bonus\\n    比例'\\n  rationale: exp013f 完成 30 步，dense reward (valid_action_bonus=0.15) 解决了 collapse（grad_norm\\n    稳定 1.7-8.15）但引发 reward gaming：action_is_valid 60%→97.5% 而 success 归零，score_max\\n    从 10+ 塌缩到 4.5。模型学会独立最大化 dense reward（29步×0.15=4.35）放弃高风险 success（10.0）。核心问题：dense\\n    reward 可被独立最大化。修复方向：(1) success-gated bonus 消除独立最大化路径 (2) 降低 bonus 到 0.01 测试弱信号是否足够\\n    (3) 前 N 步 warmup 后撤掉 bonus。优先级 exp014c > exp014a > exp014b。\\n  related_experiments:\\n  - exp_id: exp013f\\n    role: primary\\n    result: negative - reward gaming\\n  - exp_id: exp012b\\n    role: baseline\\n    result: negative - catastrophic collapse\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 12:47 UTC\\n  summary: D012 修订：放弃 success-gated bonus（bootstrap 问题），改走 sparse GRPO + 训练稳定性修复\\n  rationale: Success-gated bonus 在 success≈0% 时退化为 sparse reward，无法解决冷启动。而 exp012b\\n    step 6 success=8.59% 证明 sparse GRPO 有信号，collapse（grad_norm 1.48→0.09）可能是 LR 过高\\n    / KL 过低导致的单步更新过激，不是 reward sparsity。方案 B（sparse GRPO + 极低 LR 1e-7 + KL 0.1 + gradient\\n    clipping）直接解决 collapse 且不引入新 reward hacking 风险。\\n  related_experiments:\\n  - exp_id: exp012b\\n    role: evidence\\n    result: step 6 success=8.59% proves sparse signal exists; collapse at step 7 was\\n      training instability\\n  - exp_id: exp013f\\n    role: evidence\\n    result: dense reward gaming confirms reward shaping risks\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-14 13:44 UTC\\n  summary: Kill exp015（LR 1e-7 过保守，连续 3 步零梯度），启动 exp016 LR=5e-7 折中方案\\n  rationale: exp015 step 1-2 有梯度信号（pg_loss>0, success 3-5%），验证了 D013 的 collapse 修复。但\\n    step 3-5 连续零梯度，LR=1e-7 的参数更新量约 5e-12，模型行为无可观测变化。Kill 条件已满足。LR=1e-6（exp012b）collapse，LR=1e-7（exp015）不学习，取折中\\n    LR=5e-7 + 保留 KL=0.1 + grad_clip=1.0。从 exp015 step 5 checkpoint 恢复（保留 step 1-2\\n    的微小更新）。\\n  related_experiments:\\n  - exp_id: exp015\\n    role: primary\\n    result: kill - LR too conservative, 3 consecutive zero-gradient steps\\n  - exp_id: exp012b\\n    role: reference\\n    result: LR 1e-6 collapsed at step 7\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:55 UTC\\n  summary: Kill exp016 — reward function 完全失效，12 步零 reward 信号，GPU 空转\\n  rationale: exp016 step 12/30，所有 step 的 raw_reward/advantages/returns 均为 0。Step 7\\n    出现 4.7% success 但 reward 仍为 0，说明 reward function 未正确将 success 映射到 reward。grad_norm\\n    ~0.85 仅来自 entropy loss，模型无 policy gradient 信号。疑似 checkpoint resume 后 reward config\\n    丢失。继续运行浪费 GPU。\\n  related_experiments:\\n  - exp_id: exp016\\n    role: subject\\n    result: killed — reward function broken\\n  depends_on:\\n  - D014\\n- id: D016\\n  date: 2026-05-14 14:57 UTC\\n  summary: Pivot to Expert SFT warmup — GRPO 在 base success ~1-2% 下无法工作，LR 搜索区间穷尽\\n  rationale: Reviewer critical 分析确认：exp016 step 7 pg_loss=0.000151 证明 reward function\\n    本身可用，但 7 步中仅 1 步有 success（14%），步骤 8-12 连续 5 步零梯度。反推 base success rate ~1-2%，GRPO\\n    在此 sparsity 下无法产生有效学习。LR 搜索已覆盖 1e-6（collapse）→ 5e-7（无效学习）→ 1e-7（零梯度），区间穷尽。Pivot\\n    到 expert SFT：用 ALFWorld HandCodedTWAgent 收集的 expert trajectories（当前 ~61-70%）做\\n    SFT warmup，将 base success 提升到 10-15% 后再上 sparse GRPO。\\n  related_experiments:\\n  - exp_id: exp016\\n    role: evidence\\n    result: 6/7 steps zero gradient, base success ~1-2%\\n  - exp_id: exp015\\n    role: evidence\\n    result: LR=1e-7 zero gradients after step 3\\n  - exp_id: exp012b\\n    role: evidence\\n    result: LR=1e-6 catastrophic collapse\\n  depends_on:\\n  - D015\\n  - D014\\n  - D013\\n- id: D017\\n  date: 2026-05-14 15:20 UTC\\n  summary: D015 误诊纠正 — reward pipeline 正常，exp016 失败原因是 base success 太稀疏（1/8 步有信号）\\n  rationale: Reviewer 逐行核实 exp016.log：Step 7 critic/score/mean=0.46875（= 3/64 × 10.0）、critic/score/max=10.0、pg_loss=0.000151、grad_norm=2.0，reward\\n    function 完全正确。Agent 报告的 raw_reward=0 来自 es_manager 的 info.get('raw_reward', 0.0)\\n    日志 artifact，ALFWorld env info 不含此 key。NaiveRewardManager 检测到 rm_scores 后 pass-through，agent_trainer.py:779\\n    不是覆写。D016 Expert SFT pivot 仍成立，理由修正为 base success ~4.7%（仅 1/8 步有 success）太稀疏。\\n  related_experiments:\\n  - exp_id: exp016\\n    role: evidence\\n    result: reward pipeline confirmed working; killed due to sparse success, not bug\\n  depends_on:\\n  - D015\\n  - D016\\n- id: D018\\n  date: 2026-05-14 16:37 UTC\\n  summary: exp017 eval 5% success（低于 10% 阈值），采用方案 B+C：修复数据格式 + 从 exp008_sft checkpoint\\n    继续微调\\n  rationale: 'exp017 SFT eval: 5% success (1/20)，format_ok 从 100% 降至 75%，action_is_valid\\n    从 90% 降至 63.8%。25% episodes parse 失败（1 步退出）。expert trajectory 格式与 RAGEN &lt;think>/&lt;answer>\\n    不完全匹配，SFT 学到任务知识但破坏了 format 合规性。方案：(1) 修复 expert data 格式对齐 RAGEN template (2)\\n    从 exp008_sft checkpoint 开始微调（已有 100% format_ok），用较低 LR 防止遗忘 format。预计 ~1.5h。方案\\n    A（直接 GRPO）信号改善极小（5% vs 4.7%），方案 D 工程量太大。'\\n  related_experiments:\\n  - exp_id: exp017_expert_sft\\n    role: evidence\\n    result: 5% success, format_ok 75%, below 10% threshold\\n  - exp_id: exp008_sft\\n    role: baseline\\n    result: 0% success but 100% format_ok, 90% action_is_valid\\n  depends_on:\\n  - D016\\n  - D017\\n- id: D019\\n  date: 2026-05-14 16:48 UTC\\n  summary: Kill exp019 — move→put 替换方向错误，admissible_commands 中是 move 不是 put\\n  rationale: Reviewer critical 确认：ALFWorld handcoded expert 代码 5 种任务类型全部用 \\\"move {}\\n    to {}\\\" 检查 admissible_commands，RAGEN env.py action_is_available 检查 action in admissible_commands。fix_expert_sft_format.py\\n    将 2157 条正确的 \\\"move\\\" 替换为 \\\"put in/on\\\"，教模型产生不在 admissible_commands 中的动作，会进一步恶化 action_is_valid。正确修复方向：保留\\n    \\\"move\\\" 原样，在 observation 中添加 admissible actions 列表后缀。\\n  related_experiments:\\n  - exp_id: exp019_expert_sft_v2\\n    role: subject\\n    result: killed — trained on incorrectly modified data (move→put)\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 21:53 UTC\\n  summary: exp019b SFT eval 通过（20% success），启动 GRPO 训练\\n  rationale: exp019b 三项指标全部达标：success=20%, format_ok=100%, action_is_valid=85.3%。admissible\\n    actions augmentation 是关键因素（exp017 无→5%, exp019b 有→20%）。SFT checkpoint 已提供足够 base\\n    success rate，GRPO 应有足够非零 reward groups 产生有效梯度。从 exp019b checkpoint 启动 sparse GRPO\\n    是 MVP gate 最后一步。\\n  related_experiments:\\n  - exp_id: exp019b_expert_sft_v3\\n    role: evidence\\n    result: success=20%, format_ok=100%, action_is_valid=85.3%\\n  - exp_id: exp017_expert_sft\\n    role: baseline\\n    result: success=5%, format_ok=75% (无 admissible actions)\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D021\\n  date: 2026-05-14 22:34 UTC\\n  summary: exp020 系列 0% success 根因确认：SFT 训练格式与 RAGEN 格式不匹配，走方案 B 重训\\n  rationale: 同一 checkpoint 在 eval_sft_fast 中 20% success，在 RAGEN 中 0%。根因三个：(1) system\\n    prompt 矛盾（RAGEN 说不要标签又说要标签）(2) observation 格式完全不同（RAGEN 有 Turn N/State/Reward\\n    包装，SFT 数据没有）(3) temperature 差异。RAGEN 的多轮结构是 GRPO rollout 必需的，不能去掉。正确方案是将 SFT 数据转换为\\n    RAGEN 格式重训，而非改 RAGEN 适配 SFT。\\n  related_experiments:\\n  - exp_id: exp020_grpo_from_sft\\n    role: evidence\\n    result: AssertionError, 未运行\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: val_before_train success=0%, action_is_valid=16.7%\\n  - exp_id: exp020c_grpo_from_sft\\n    role: evidence\\n    result: hydra config error\\n  - exp_id: exp020d_grpo_from_sft\\n    role: evidence\\n    result: killed, 同 exp020b 配置\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-15 01:07 UTC\\n  summary: exp020b GRPO 失败，确认 eval mismatch 是根因，恢复 D021 RAGEN 格式重训路线\\n  rationale: exp020b 30步中跑了22步，train success从18.75%降到4.69%，val success始终0%，entropy坍缩61%。核心问题不是GRPO算法，而是SFT模型在RAGEN多轮框架下表现与eval_sft_fast完全不同（0%\\n    vs 20%）。之前Reviewer修正认为\\\"0%是样本量问题\\\"是错误的——22步训练确认了系统性不一致。D021（将SFT数据转换为RAGEN格式重训）是正确方向，恢复执行。\\n  related_experiments:\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: train success 18.75%→4.69%, val success=0%, entropy collapse\\n  - exp_id: exp019b_expert_sft_v3\\n    role: baseline\\n    result: eval_sft_fast 20% but RAGEN val 0%\\n  depends_on:\\n  - D020\\n  - D021\\n- id: D023\\n  date: 2026-05-15 03:16 UTC\\n  summary: exp021 RAGEN 格式 SFT 验证通过（25% success），批准 exp022 GRPO\\n  rationale: exp021 在 RAGEN val 中 success=25%, action_is_valid=87.5%，全部达标。对比 exp019b\\n    在 RAGEN val 中 0% success，证明格式对齐是根因且修复生效。25% baseline 是目前最强起点，配合加强的 KL 约束（0.1→0.5）应能避免\\n    exp020b 的 entropy 坍缩。\\n  related_experiments:\\n  - exp_id: exp021_ragen_sft_v4\\n    role: evidence\\n    result: RAGEN val success=25%, action_is_valid=87.5%\\n  - exp_id: exp019b_expert_sft_v3\\n    role: baseline\\n    result: RAGEN val success=0%\\n  - exp_id: exp020b_grpo_from_sft\\n    role: negative\\n    result: train success 18.75%→4.69%, entropy collapse\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-15 03:21 UTC\\n  summary: exp021 结论降级为 inconclusive，exp022 暂不 kill 等 step 0 val 确认\\n  rationale: exp021 两次独立 eval 严重矛盾：4-episode val_before_train 25% success vs ~16-episode\\n    eval 6.25% success。4-episode 估计方差过大不可靠，25% 结果很可能是高方差幸运值。exp022 基于该不可靠数据启动，但已在运行中——让\\n    step 0 val_before_train 给出更可靠的 baseline 数字再决定是否 kill，避免白白浪费已投入的启动时间。同时 Reviewer\\n    指出 exp022 的 val env_groups=8 override 可能未生效（config dump 显示 4），需立即验证。\\n  related_experiments:\\n  - exp_id: exp021_ragen_sft_v4\\n    role: trigger\\n    result: inconclusive — 4-ep 25% vs 16-ep 6.25%\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: at_risk\\n    result: running, awaiting step 0 val confirmation\\n  depends_on:\\n  - D023\\n- id: D025\\n  date: 2026-05-15 05:14 UTC\\n  summary: Sparse binary GRPO 路线终止。三次一致退化（exp020b/exp022/exp023c），KL 仅 0.0005 时 success\\n    已退化，算法与稀疏 reward 结构性不匹配。Pivot 到两条并行路线：(1) success-gated dense reward GRPO，(2)\\n    GiGPO cherry-pick\\n  rationale: '三次 GRPO 实验（exp020b kl=0.1, exp022 kl=0.5, exp023c kl=0.5 serial）均呈现同一模式：entropy\\n    收缩 + success 退化 + KL 极低（策略几乎未移动就已退化）。根因：sparse binary reward（0/10）下绝大多数 GRPO group\\n    全零 reward → advantage≈0 → 有效梯度来自极少数成功 episode → 不足以引导策略改进。kl_loss_coef 从 0.1 到\\n    0.5 仅减缓退化速度未改变方向。这是算法-任务结构性不匹配，非超参问题。\\n\\n\\n    两条 pivot 路线：\\n\\n    (1) Success-gated dense reward：从 exp021 checkpoint（25% success）出发，给 valid_action\\n    加 bonus 但仅在 episode 成功时给。exp013f 失败原因是 unconditional bonus → reward gaming；success-gating\\n    消除独立最大化路径。代码改动小，可当天启动。\\n\\n    (2) GiGPO cherry-pick：step-level advantage estimation 提供更密集的信号，解决 credit assignment。已有迁移方案（3-5天），作为更彻底的解决方案。'\\n  related_experiments:\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: 'failed: entropy collapse 61%, success→0%'\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: 'killed: step 0 action_is_valid 48.75%'\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: 'failed: 8 steps success 29.7%→23.4%, disk full crash'\\n  - exp_id: exp013f\\n    role: lesson\\n    result: unconditional dense reward → gaming\\n  depends_on:\\n  - D022\\n  - D023\\n  - D024\\n- id: D026\\n  date: 2026-05-15 05:15 UTC\\n  summary: GRPO in RAGEN 确认失败（3/3），pivot 到 verl-agent GiGPO cherry-pick（Plan C）\\n  rationale: 三次 GRPO 实验（exp020b/exp022/exp023c）一致表现为 entropy 坍缩 + success 退化。但 Self-Guide\\n    论文证明 GRPO 在 ALFWorld 上可以达到 72.7%（verl-agent 框架），说明问题不是 GRPO+sparse reward 本身，而是\\n    RAGEN 框架。RAGEN 的 full-history concatenation 导致 context 随步数爆炸，1.7B 模型在长 context\\n    下推理质量退化。verl-agent 的 step-independent rollout 保持 context 恒定。IDEA_BRIEF 原始设计也指定\\n    verl-agent。采用 Plan C（cherry-pick GiGPO + 核心 rollout 机制，3-5 天），避免 Plan A/B 的 2-4\\n    周全量迁移风险。\\n  related_experiments:\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: 'failed: entropy collapse, success 18.75%→4.69%'\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: 'killed: step 0 action_is_valid 48.75%'\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: 'failed: step 9 disk full, 8 steps showed success 29.7%→23.4%, entropy\\n      shrinking'\\n  depends_on:\\n  - D022\\n  - D023\\n  - D024\\n- id: D027\\n  date: 2026-05-15 05:25 UTC\\n  summary: Kill exp024 (success-gated GRPO) — D026 已终止 RAGEN GRPO 路线，success-gated\\n    不解决 context 爆炸根因\\n  rationale: Reviewer 审查报告指出决策链冲突：D026 已明确 pivot 到 verl-agent GiGPO 并终止 RAGEN GRPO\\n    路线，但 exp024 仍是 RAGEN GRPO（仅改 reward 为 success-gated）。三点判断：(1) success-gated reward\\n    不解决 RAGEN full-history concatenation 导致的 context 爆炸——这是 exp020b/022/023c 三次退化的共因；(2)\\n    D013 之前已因 bootstrap 问题否决 success-gated（success≈0% 退化为 sparse），当前 baseline 6.25%\\n    仍然很低；(3) 3/3 RAGEN GRPO 退化 pattern 下第 4 次仅改 reward 极不可能成功。GPU 应腾出用于 verl-agent\\n    GiGPO cherry-pick 准备。\\n  related_experiments:\\n  - exp_id: exp024\\n    role: killed\\n    result: D026后应终止，step 0/30 刚启动\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: RAGEN GRPO 退化 1/3\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: RAGEN GRPO 退化 2/3\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: RAGEN GRPO 退化 3/3\\n  depends_on:\\n  - D026\\n  - D025\\n- id: D028\\n  date: 2026-05-15 08:32 UTC\\n  summary: 终止 verl-agent 直接运行尝试，全力转向 Track B cherry-pick（步独立 rollout + GiGPO 整合到 RAGEN）\\n  rationale: 'verl-agent 在 bjb1-17606 上 6 次启动失败（exp025→exp025b×3→dry run v7/v8/threadopt），根因是\\n    AutoDL 容器 cgroup pids.max=20480 限制。Ray 集群 + FSDP + vLLM TP 的线程总数超过此限制，即使单 GPU\\n    降级配置也在训练阶段崩溃。AutoDL 无法调整 pids.max，暂无非容器化服务器可用。继续在同一配置重试无意义。\\n\\n\\n    Track B cherry-pick 是可行路径：将 step-independent rollout + GiGPO 算法整合到 RAGEN 代码库（不依赖\\n    Ray，已验证可在此服务器运行）。Track B 分析报告已完成（gigpo_cherry_pick_plan.md），方案明确（~480 行新增 + ~200\\n    行修改，8 文件，3-5 天）。\\n\\n\\n    附带收获：verl-agent val_before_train 产出了 Qwen3-1.7B raw baseline（success=6.2%，与 RAGEN\\n    SFT 后的 6.25% 接近），确认模型基础能力跨框架一致，训练算法是关键差异。'\\n  related_experiments:\\n  - exp_id: exp025\\n    role: evidence\\n    result: 'failed: conda env 错误'\\n  - exp_id: exp025b\\n    role: evidence\\n    result: 'failed: 3次启动失败（vllm模块/Ray GCS/EAGAIN）'\\n  - exp_id: exp025c\\n    role: evidence\\n    result: 未提交，threadopt dryrun 训练阶段崩溃\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D029\\n  date: 2026-05-15 11:14 UTC\\n  summary: exp026 registry 被 cron 误标 DONE(failed)，实际训练仍在运行；速度修正为 30-60min/step（总计\\n    75-150h）\\n  rationale: Cron 5 次检查因 WANDB_MODE=disabled 无法读取指标，自动判定进程死亡并标记 failed。但 PID 存活、GPU\\n    双卡 100% 利用率、日志持续写入。DONE→RUNNING 转换被 registry 禁止，需在训练真正完成后手动更新 conclusion。速度估算从之前的\\n    21min/step 修正为 30-60min/step（step 0 含 val_before_train 耗时 ~40min），150 steps 预计\\n    3-6 天完成。教训：后续实验必须启用 W&B 或 sentinel file 避免 cron 误判。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: subject\\n    result: running (registry incorrectly shows failed)\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-15 11:50 UTC\\n  summary: exp026 等待期并行实现 B-IAVR 核心机制代码（action-change gating），不再空等 baseline 结果\\n  rationale: Reviewer 战略审查指出：50 个实验全在 pipeline debugging，核心 B-IAVR 选择性验证机制零实现。即使 exp026\\n    成功（weak story），真正的论文实验（有/无 selective verification ablation）还没开始。利用 3-6 天训练等待期提前铺核心代码，exp026\\n    出结果后可直接进入核心实验阶段，压缩整体时间线。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: baseline\\n    result: running\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: failed - entropy collapse\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: failed - entropy collapse\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: failed - entropy collapse\\n  depends_on:\\n  - D029\\n  - D028\\n- id: D031\\n  date: 2026-05-15 12:13 UTC\\n  summary: B-IAVR 代码审查通过（Reviewer info），Phase B 前必须解决两个 warning：&lt;VERIFY> special token\\n    注册 + a_pre 推理开销量化\\n  rationale: Reviewer 审查 B-IAVR 核心代码：reward 公式/Lagrangian 更新/模块化设计/52 个测试全通过，与 IDEA_BRIEF\\n    一致。但 &lt;VERIFY> 若被 tokenizer 拆为 8 个子 token 会显著增加学习难度（必须注册为 special token）；a_pre\\n    每次 verify step 额外一次 greedy decode 可能增加 15-30% 步耗时（需 dry run 量化）。这两项是 Phase B 集成前的硬性前置。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: baseline_for_phase_b\\n    result: running\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-15 12:33 UTC\\n  summary: exp026 前 2 步训练指标强正向（success 6.25%→32.81%，entropy 未 collapse），等 step 5 val\\n    做 MVP 判定\\n  rationale: 从 Ray worker stdout logs 提取到训练指标，解决了之前的盲飞问题。Step 1 train success 21.88%\\n    已超 MVP 目标（20%），但 train ≠ val，需等 step 5 val（test_freq=5）确认。Entropy 上升（0.267→0.317）而非\\n    collapse，与之前 3 次 RAGEN GRPO 失败形成鲜明对比，确认 step-independent context + step-level\\n    credit assignment 是关键因素。MVP 判定标准：val success ≥ 20% → complete_mvp()。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: subject\\n    result: train success 32.81% at step 2, awaiting step 5 val\\n  depends_on:\\n  - D029\\n  - D030\\n- id: D033\\n  date: 2026-05-15 13:02 UTC\\n  summary: exp026 registry 误判修复：cron 因 WANDB_MODE=disabled + 监控错误 PID 误标 DONE(failed)，实际训练正常运行（PID\\n    781795）。已重置 RUNNING 并修正监控。后续实验硬规则：禁止 WANDB_MODE=disabled\\n  rationale: 两个根因：(1) WANDB_MODE=disabled 导致 cron 无 sentinel/metrics 可检测；(2) 监控了 shell\\n    wrapper PID 778562 而非实际训练进程 PID 781795。Reviewer 交叉验证确认 step 1-2 指标真实。修复后 cron\\n    间隔 300s 监控正确 PID + log_path。教训沉淀：所有实验必须启用 W&B 以确保 cron 可监控。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: affected\\n    result: registry reset to RUNNING, actual training healthy\\n  depends_on:\\n  - D029\\n  - D032\\n- id: D034\\n  date: 2026-05-15 13:38 UTC\\n  summary: 建立两级阈值：MVP=20% val（训练可行性 checkpoint），论文 baseline 最低要求=50% val（B-IAVR 的\\n    always-on baseline 需与 Self-Guide 72.7% 可比才有说服力）\\n  rationale: Reviewer 独立评估指出：Self-Guide 在 ALFWorld 上 Qwen3-1.7B GRPO baseline 已达 72.7%，20%\\n    val 处于所有已发表 baseline 底部。step-independent rollout 是 verl-agent cherry-pick 不算本项目贡献，论文贡献必须来自\\n    B-IAVR。在弱 agent（20%）上证明选择性验证的 cost-efficiency 没有说服力——需要 baseline 至少 50-60% 才能让\\n    B-IAVR 的 Pareto efficiency claim 有意义。MVP 阈值保持 20% 不变（证明 GRPO 在 RAGEN 能跑），但内部明确论文可行性需要\\n    val 收敛到更高水平。Reviewer 估计 150 步训练后 val 可达 60-70%，与 Self-Guide no-SG baseline 可比。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: baseline\\n    result: train 32.81% @ step 2, val pending\\n  depends_on:\\n  - D032\\n  - D033\\n- id: D035\\n  date: 2026-05-15 14:01 UTC\\n  summary: exp026 训练不稳定（step 2 峰值 32.81% → step 4 归零），准备 exp027 调参重跑；save_freq 必须降至\\n    5\\n  rationale: Step 4 success=0%, pass@16=0。非 entropy collapse（entropy 稳定 0.387），而是\\n    step 3 负梯度过度纠正导致保守退化（KL 回落至 0.054，action_is_valid 反升至 71.7%）。LR=1e-6 对 step-level\\n    reward 的高方差梯度过大。save_freq=25 导致 step 2 的 32.81% 峰值无 checkpoint 可恢复——这是最大损失。exp027\\n    方向：降 LR（→5e-7）、升 KL coef（0.01→0.04）、save_freq=5。等 step 5 val 确认后正式切换。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence\\n    result: 'training unstable: peak 32.81% at step 2, collapsed to 0% at step 4'\\n  depends_on:\\n  - D032\\n- id: D036\\n  date: 2026-05-15 14:07 UTC\\n  summary: Reviewer critical 确认 exp026 GRPO 死亡螺旋：step 4 success=0%，KL→0.0025 策略回退到\\n    reference，exp027 需针对性解决稀疏奖励崩塌\\n  rationale: Reviewer 独立核实训练指标：step 2 峰值 32.81% 后单调下降，step 4 完全崩塌（64 rollout 全失败）。KL\\n    单调递减说明策略不是发散而是回退到 reference，固定 KL penalty 无效。exp027 必须引入 dynamic sampling（过滤零奖励\\n    batch）+ 调整 clip ratio + 可能加 entropy bonus 维持探索。已向 Agent 发送 exp027 设计修正指令。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: primary\\n    result: collapsing\\n  - exp_id: exp027_stable_grpo\\n    role: next\\n    result: preparing\\n  depends_on:\\n  - D035\\n- id: D037\\n  date: 2026-05-15 15:17 UTC\\n  summary: exp027 val 判定阈值：<20% fail、20-25% weak (=SFT)、30%+ proceed Phase B。Reviewer\\n    指出 GRPO 从未在 val 超越 SFT baseline，train-val gap 是系统性风险。\\n  rationale: 'Reviewer pass/fail 评估揭示关键事实：51 个实验中所有 GRPO 的 val success 均为 0-12.5%，而\\n    SFT (exp019b) 已达 20%。exp026 的 32.81% 是 train success，已知 train-val 差距巨大（exp023c:\\n    train 29.7% vs val 6.25%）。因此 exp027 的判定必须基于 val success：(1) val<20% → MVP 失败，需\\n    pivot（换服务器跑 verl-agent 原版 or 重评项目）；(2) val 20-25% → GRPO 仅匹配 SFT，RL 训练贡献为零，需重新评估\\n    Phase B 是否建在 SFT 上；(3) val≥30% → GRPO 首次超越 SFT，Phase B 有意义的 baseline，proceed。A\\n    类会议需 val≥40% + 第二环境 + 模型规模实验，预估 500-800 GPU-h。'\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: 被判定对象\\n    result: running\\n  - exp_id: exp026_step_independent_grpo\\n    role: 前置实验\\n    result: negative\\n  - exp_id: exp019b_expert_sft_v3\\n    role: SFT baseline对照\\n    result: success\\n  depends_on:\\n  - D036\\n  - D034\\n- id: D038\\n  date: 2026-05-15 15:17 UTC\\n  summary: Reviewer 评估 exp027 pass/fail 论文可行性：修正 claim 强度阈值，确认 val success 是唯一判定标准\\n  rationale: 'Reviewer 指出关键事实：GRPO 从未在 val 上超越 SFT baseline（RAGEN 框架内 6.25%）。exp026\\n    的 32.81% 是 train success 不是 val success，train-val 差距系统性存在（exp023c: train 29.7%\\n    vs val 6.25%）。但 Reviewer 混淆了两个 eval 框架：exp019b 的 20% 是 eval_sft_fast（非 RAGEN eval），RAGEN\\n    框架内 SFT baseline 是 6.25%（exp021 C003-compliant 16ep eval）。因此 exp027 val ≥ 20%\\n    = 3.2× SFT baseline，仍是有意义的 RL 贡献，不是\\\"仅匹配 SFT\\\"。但 Reviewer 对 A 类会议的要求评估（Phase B +\\n    ablation + 第二环境 + scaling = 500-800 GPU-h）是合理的。结论：val success 是唯一判定标准，train success\\n    仅作 training dynamics 参考；MVP 20% 的门槛在 RAGEN eval 框架下仍然有效且有意义。'\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: subject\\n    result: running\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence\\n    result: negative\\n  - exp_id: exp021_ragen_sft_v4\\n    role: baseline\\n    result: negative\\n  - exp_id: exp019b_expert_sft_v3\\n    role: baseline\\n    result: success\\n  depends_on:\\n  - D036\\n  - D034\\n- id: D039\\n  date: 2026-05-15 16:57 UTC\\n  summary: 论文 framing 方向锁定：cost-efficiency story，不走 performance story；ARES 为主要竞争对标\\n  rationale: Related work survey + Reviewer 评估揭示：ALFWorld SOTA 88-93%，我们最好 6.25%，即使\\n    exp027 达 40% 仍是 bottom tier，performance story 死路。唯一可行路径是 cost-efficiency framing——\\\"在接近\\n    Self-Guide 性能的前提下，通过 RL-trained selective verification 减少 verification 开销\\\"。ARES\\n    (arXiv 2603.07915) 是最近竞争者（per-step adaptive computation），差异化点：(1) binary verify/not-verify\\n    决策更简洁可解释 vs ARES 连续 effort selection，(2) action-change 作为 environment-grounded\\n    reward signal vs ARES 的 SFT router，(3) interactive agent 场景 vs general reasoning。前提条件：baseline\\n    必须 ≥50%（接近 Self-Guide 72.7%），否则 cost-efficiency claim 无意义。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: MVP gating\\n    result: running\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence for step-independent approach\\n    result: negative (peak 32.81% then collapsed)\\n  - exp_id: exp021_ragen_sft_v4\\n    role: SFT baseline\\n    result: 6.25% success\\n  depends_on:\\n  - D038\\n  - D037\\n- id: D040\\n  date: 2026-05-15 18:27 UTC\\n  summary: 修正 exp027 step 3 判定框架为三层阈值，Plan B kl_coef 上调至 0.015-0.02，中期评估 adaptive\\n    KL\\n  rationale: Reviewer 独立评估确认 step 2 KL 0.058→0.413 (7x) 为强警告信号，kl_coef=0.005 约束过弱。exp026(KL\\n    collapse)+exp027(KL spike) 揭示固定 kl_coef 的 Goldilocks zone 极窄。修正：(1) 三层判定——绿(success≥10%+KL<0.3)、黄(success≥6.25%+KL\\n    0.3-0.6，准备 Plan B)、红(success<6.25%或KL>0.6，终止)；(2) Plan B kl_coef 从 0.01-0.02 收窄至\\n    0.015-0.02（0.01 在 exp026 已失败）；(3) 增加 entropy(<0.15=collapse)/pass@16(<0.5=零批次风险)/grad_norm(>25=不稳定)\\n    三个辅助监控维度；(4) 中期评估 adaptive KL 实现成本。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step2 KL spike 0.413, success drop to 10.16%\\n  - exp_id: exp026_step_independent_grpo\\n    role: reference\\n    result: 'symmetric failure: KL collapse to 0.0025'\\n  depends_on:\\n  - D037\\n- id: D041\\n  date: 2026-05-15 19:50 UTC\\n  summary: exp027 瓶颈诊断为 sparse reward 学习信号不足而非 KL 不稳定；Plan B(adaptive KL) 降级，Plan\\n    D(GiGPO/step-level credit) 升为首选备选路线\\n  rationale: Reviewer 独立评估：(1) train success 连续两步 10.16%=plateau，pass@16 从 100%→50%\\n    说明仅 4/8 env groups 有学习信号；(2) exp026(太激进crash)+exp027(太保守plateau)构成稳定性-效率 dilemma，纯超参调整无法解决；(3)\\n    adaptive KL 解决的是 KL 振荡，但 KL 已自修正（0.413→0.248），不是当前瓶颈；(4) Self-Guide 同模型同环境达 72.7%，差异在\\n    step-level dense reward vs binary sparse reward；(5) GiGPO/step-level credit 打破\\n    plateau 概率 40-70% vs 当前 recipe 15-25%。决策：exp027 跑到 step 10（早停条件 train≤12%），并行准备\\n    Plan D。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step2-3 train success plateau at 10.16%, pass@16 declining\\n  - exp_id: exp026_step_independent_grpo\\n    role: reference\\n    result: aggressive config crashed, complementary failure mode\\n  depends_on:\\n  - D040\\n  - D037\\n- id: D042\\n  date: 2026-05-15 19:50 UTC\\n  summary: 采纳 Reviewer 建议：exp027 跑到 step 10 评估，同时并行准备 Plan D（GiGPO/step-level credit\\n    assignment），不再把 adaptive KL 作为首选 Plan B\\n  rationale: Reviewer 独立评估 exp027 中期趋势：train success 连续两步 10.16% plateau，pass@16 从\\n    100%→50% 持续下滑，50 步内 val 突破 20% 概率 <10%。核心瓶颈已从 KL 不稳定（已自修正）转为学习信号密度不足——sparse binary\\n    reward + GRPO 在 8 env groups 下信号太稀疏。Adaptive KL 只解决 KL 振荡不解决信号密度问题。Self-Guide\\n    论文用同模型同环境达 72.7%，差异在 co-evolving internal reward（step-level dense reward）。Plan\\n    D（GiGPO/step-level credit）估计 40-55% 概率达 20% val，远高于当前 recipe 的 15-25%。决策：(1) exp027\\n    继续到 step 10（~12h），如 train success ≤12% 终止；(2) 立即并行准备 Plan D 代码和方案；(3) Adaptive\\n    KL 降级为 Plan D 的辅助选项而非独立方案。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step 3 绿区但 plateau at 10.16%, pass@16 下滑\\n  - exp_id: exp026_step_independent_grpo\\n    role: reference\\n    result: 对称失败模式：KL collapse vs KL spike\\n  depends_on:\\n  - D040\\n  - D037\\n- id: D043\\n  date: 2026-05-15 20:15 UTC\\n  summary: Reviewer 发现 recipe gap 是根本问题：参考论文 GRPO baseline 72-73% vs 我们 10%，GiGPO\\n    集成继续但新增 recipe gap 诊断为最高优先级\\n  rationale: GiGPO 论文 Qwen2.5-1.5B GRPO=72.8%, Self-Guide 论文 Qwen3-1.7B GRPO=72.7%,\\n    我们 exp027 Qwen3-1.7B=10.16%@step3。62pp 的 baseline gap 说明瓶颈不在 RL 算法（GRPO vs GiGPO）而在训练\\n    recipe（SFT 起点质量/训练迭代数/环境配置/LR等）。GiGPO 改善 credit assignment 但不解决 recipe gap。必须系统对比训练配置找出差异根因。GiGPO\\n    集成继续（低成本），但预期从\\\"突破 40%+\\\"下调为\\\"增量未知\\\"。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step3 train success 10.16%, baseline gap 62pp vs reference papers\\n  - exp_id: exp021_ragen_sft_v4\\n    role: reference\\n    result: SFT baseline 6.25%\\n  depends_on:\\n  - D041\\n- id: D044\\n  date: 2026-05-15 20:28 UTC\\n  summary: Recipe Gap 确认三大根因：SFT 毒药 + binary reward 零梯度 + mini-batch 过小；Phase A 策略：Instruct\\n    冷启动 + invalid_action_penalty 最小变更验证\\n  rationale: Recipe Gap 六维对比发现参考论文（Self-Guide 72.7%, GiGPO）均从 Instruct 冷启动而非 SFT，且使用\\n    invalid_action_penalty 区分失败轨迹。我们的 SFT 破坏了 instruction-following 能力（baseline 6.25%），导致\\n    GRPO 零梯度。Phase A 只改两个变量隔离根因验证，GiGPO 算法切换暂缓（先修 recipe 再评估算法）。前置 zero-shot eval\\n    建立 Instruct 真实 baseline。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: evidence\\n    result: step 1→3 success 35.9%→10.2%, 确认 sparse reward 零梯度\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence\\n    result: negative, 死亡螺旋\\n  depends_on:\\n  - D043\\n  - D041\\n  - D042\\n- id: D045\\n  date: 2026-05-15 20:39 UTC\\n  summary: exp027 判定 MVP 未通过：train success 13.28%（step 4），pass@16 持续下降至 37.5%，模型特化而非泛化。Step\\n    5 未执行（进程异常终止）。\\n  rationale: 'Step 1→4 趋势：success 35.9%→10.2%→10.2%→13.28%（微升但远低于 20% MVP 阈值），pass@16\\n    100%→62.5%→50%→37.5%（单调下降=探索能力丧失）。历史 train-val gap（exp023c: train 29.7% vs val\\n    6.25%）表明 val 不可能达 20%。D044 recipe gap 分析确认根因为 SFT 毒药 + binary reward 零梯度。进程在 step\\n    4 后异常终止（earlystop worker 可能误杀或自然崩溃），step 5 val 和 checkpoint 均未生成。基于充分的 train 证据直接判定，不补跑\\n    val。'\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: MVP 未通过, train success 13.28%, pass@16 37.5%\\n  depends_on:\\n  - D044\\n  - D040\\n  - D037\\n- id: D046\\n  date: 2026-05-15 21:05 UTC\\n  summary: 继续 Phase A：exp028a Instruct 冷启动 + invalid_action_penalty 路线。零样本 eval ≥15%\\n    则直接提交；<15% 则重评项目\\n  rationale: D044 recipe gap 诊断是 52 个实验以来最具证据支撑的根因分析——参考论文（Self-Guide 72.7%, GiGPO\\n    72.8%）均从 Instruct 冷启动且使用 invalid_action_penalty，我们的 SFT 路线破坏了 instruction-following\\n    能力（baseline 6.25%）。exp028a 只改两个变量（Instruct 起点 + invalid_action_penalty），隔离验证 recipe\\n    gap 假设，成本低（预计 <50 GPU-h）。如果修复 recipe 后仍无法达到 20% val，说明瓶颈在 RAGEN 框架层面而非训练 recipe，项目需重评。零样本\\n    eval 阈值 15% 作为 Instruct 模型 baseline 下限——低于此说明模型本身能力不足，recipe gap 不是唯一问题。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: MVP failed\\n    result: train success 13.28%, pass@16 37.5%\\n  - exp_id: exp028_prereq_zeroshot_instruct\\n    role: 前置验证\\n    result: running\\n  - exp_id: exp028a\\n    role: 下一实验\\n    result: preparing\\n  depends_on:\\n  - D044\\n  - D045\\n- id: D047\\n  date: 2026-05-15 21:06 UTC\\n  summary: 暂停 exp028a 最终定参，等零样本 eval 确认 Qwen3-1.7B base 能力后再决定 model_path 和训练起点\\n  rationale: 发现 Qwen3-1.7B 可能不存在独立 Instruct 变体（base/instruct 同权重，chat template 切换）。如果零样本确实\\n    ≈0%，D044 的\\\"SFT 毒药\\\"假设不成立——SFT 是从 0% 提升到 6.25% 的必要步骤，而非有害步骤。exp028a 的 model_path\\n    选择（base vs SFT checkpoint）完全取决于这个结果。penalty 修复可继续，但训练提交 hold 到零样本结论出来。\\n  related_experiments:\\n  - exp_id: exp028a\\n    role: blocked_by_diagnostic\\n    result: pending\\n  - exp_id: exp027_stable_grpo\\n    role: predecessor\\n    result: negative\\n  - exp_id: exp028_prereq_zeroshot_instruct\\n    role: diagnostic\\n    result: running\\n  depends_on:\\n  - D044\\n  - D045\\n- id: D048\\n  date: 2026-05-15 21:08 UTC\\n  summary: exp028a 采用 SFT checkpoint + invalid_action_penalty 最小变更方案，放弃 \\\"SFT是毒药\\\" 假设\\n  rationale: Qwen3-1.7B 本身就是 instruct 模型，不存在独立 -Instruct 版本。零样本 0%→SFT 6.25% 证明 SFT\\n    有益非有害。真正差距在 GRPO recipe（零梯度/binary reward/batch size）。MVP 阶段隔离单一变量：只加 invalid_action_penalty=-0.1\\n    解决零梯度问题，保留 SFT checkpoint 作为更好起点。Pass 阈值 ≥20%。Option 2（全面 recipe 对齐）变量过多，作为后备。\\n  related_experiments:\\n  - exp_id: exp028_prereq\\n    role: evidence\\n    result: Qwen3-1.7B 零样本 0%，确认即 instruct 模型\\n  - exp_id: exp021\\n    role: baseline\\n    result: SFT val 6.25%\\n  - exp_id: exp027\\n    role: evidence\\n    result: GRPO peak 35.9% → collapse 10-13%，零梯度问题\\n  depends_on: []\\n- id: D049\\n  date: 2026-05-15 21:08 UTC\\n  summary: 'D046: SFT必要性确认 + 下一步双GPU并行策略（D诊断→A+C并行）'\\n  rationale: 零样本0% vs SFT 6.25% vs SFT+GRPO 35.94%证明SFT是必要正效果，根因#1(SFT毒药)证伪。剩余根因#2(零梯度)和#3(mini-batch过小)需修复。策略：先跑5min诊断(enable_thinking=False零样本)排除格式干扰；penalty代码就绪后双GPU并行——一卡跑penalty+mb8，一卡跑penalty+mb32，同时验证根因#2和#3。\\n  related_experiments:\\n  - exp_id: exp021\\n    role: evidence\\n    result: SFT 0%→6.25% success, 0.75%→68.75% action_is_valid\\n  - exp_id: exp027\\n    role: evidence\\n    result: SFT+GRPO step1 35.94% success\\n  - exp_id: D046\\n    role: diagnostic\\n    result: 零样本=0%确认instruct模型\\n  depends_on: []\\n- id: D050\\n  date: 2026-05-15 21:24 UTC\\n  summary: '停止 exp028a（确认与 exp027 功能等价），根因 #2 也被否定，下一步全面对齐 Self-Guide recipe'\\n  rationale: Reviewer 三次报告确认：exp027 代码默认 invalid_action_penalty_coef=0.1 已生效（step_rewards.py\\n    在 exp027 启动前已存在，advantage/min 出现负值）。exp028a 显式设 0.1 = 重复 exp027。三大根因状态：#1 SFT毒药\\n    ❌(D047)、#2 零梯度 ❌(penalty 已生效但仍 10-13%)、#3 mini-batch 过小 ✅未验证。单变量策略连续两次未命中，MVP\\n    需要正面信号——改为对齐 Self-Guide recipe（mini-batch + steps + LR 同时调整），成功后再做 ablation 分解归因。\\n  related_experiments:\\n  - exp_id: exp027\\n    role: evidence\\n    result: penalty=0.1 已默认生效，仍 collapse 到 10-13%\\n  - exp_id: exp028a\\n    role: cancelled\\n    result: 确认与 exp027 功能等价，停止\\n  depends_on: []\\n- id: D051\\n  date: 2026-05-16 03:22 UTC\\n  summary: Setup 审计发现 exp028c 非 Self-Guide 有效复现：step-independent 训练破坏信用分配 + self-guidance\\n    reward 缺失 + val 仅 16 episodes\\n  rationale: Agent 完成 6 维度审计，发现 5 个根本差异。最大嫌疑：RAGEN history_length=2 切断 episode-level\\n    训练导致长程信用分配失效（gamma^49=7.7%），完美解释 train success 波动但 val 不动。Self-guidance ±0.1 step\\n    reward（贡献 8%）完全未实现。Val 16 episodes 分辨率仅 6.25%。决策：exp028c 继续到 step 10 作 baseline\\n    数据点，同时开始 P0/P1 代码修复，修复后启动 exp029 作为真正复现。\\n  related_experiments:\\n  - exp_id: exp028c_selfguide_recipe\\n    role: 触发审计\\n    result: val success 6.25% = baseline after 5 steps\\n  - exp_id: exp027_stable_grpo\\n    role: 同类失败\\n    result: 相同 failure mode\\n  - exp_id: exp026_step_independent_grpo\\n    role: 同类失败\\n    result: 相同 failure mode\\n  depends_on:\\n  - D050\\n  - D045\\n  - D044\\n- id: D052\\n  date: 2026-05-16 07:54 UTC\\n  summary: exp028c 终止：step 10 val success=0%（灾难性崩溃），MVP 确认失败。根因：step_independent h=2\\n    导致过拟合 train distribution + 灾难性遗忘 val。下一步 exp029 episode-level 训练。\\n  rationale: step_5_val best@128=10.0（满分）→ step_10_val best@800=0.0（完全归零）。模型在 train\\n    distribution 上仍有 10-22% success 但 val 从 6.25% 崩到 0%。D051 分析确认的结构性缺陷（step_independent\\n    h=2）获得最强实验证据：模型过拟合 train 局部 pattern 且灾难性遗忘 val 能力。继续训练浪费 GPU（已用 8.5h，剩余 68h）。立即终止释放\\n    GPU 给 exp029。\\n  related_experiments:\\n  - exp_id: exp028c_selfguide_recipe\\n    role: 终止\\n    result: step_10_val success=0%, catastrophic forgetting\\n  - exp_id: exp027_stable_grpo\\n    role: 同类失败\\n    result: train 13.28% peak, val 未测\\n  - exp_id: exp026_step_independent_grpo\\n    role: 同类失败\\n    result: 相同 failure mode\\n  depends_on:\\n  - D051\\n  - D050\\n  - D037\\n- id: D053\\n  date: 2026-05-16 23:45 UTC\\n  summary: MVP 通过：episode-level GRPO step 5 val=25%（2x baseline），complete_mvp() 进入\\n    research 阶段\\n  rationale: Step 5 val success 25% 远超 15% 阈值（也超过了 step 10 的 25% 门槛）。对比 exp028c step_independent\\n    模式 step_5_val=6.25%，episode-level context window 证明解决了信用分配缺陷。训练稳定（grad_norm 1.0-1.7，无\\n    OOM），pass@8 峰值 75% 证明策略有潜力。KL 上升趋势需关注但不阻碍 MVP 判定。\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: MVP validation\\n    result: step_5_val=25%, train_peak=35.2%\\n  - exp_id: exp028c_selfguide_recipe\\n    role: negative control (step_independent)\\n    result: step_5_val=6.25%, step_10_val=0%\\n  depends_on:\\n  - D051\\n  - D052\\n- id: D054\\n  date: 2026-05-16 23:53 UTC\\n  summary: 'Post-MVP framing pivot: dual contribution (episode-level training methodology\\n    + selective verification)'\\n  rationale: 'MVP 结果 (exp029 25% vs exp028c 0%) 证明 episode-level credit assignment\\n    本身是强贡献。原 D039 纯 cost-efficiency framing 依赖 baseline ≥50%（当前远未达到），风险过高。新 framing:\\n    Claim 1 (training methodology, already established) 为 primary, Claims 2-3 (selective\\n    verification) 为 conditional secondary。如果收敛后 <40%, Plan A 退到 pure methodology paper。'\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: primary_evidence\\n    result: step5_val=25%_2x_baseline\\n  - exp_id: exp028c_selfguide_recipe\\n    role: negative_evidence\\n    result: step10_val=0%_catastrophic_collapse\\n  depends_on:\\n  - D053\\n  - D051\\n  - D039\\n- id: D055\\n  date: 2026-05-17 00:48 UTC\\n  summary: Dream Review (weak reject) 响应：修正理论框架（γ decay → dual mechanism），加 GAE baseline，升\\n    seeds 至 5\\n  rationale: Dream simulate 返回 weak reject，核心问题：(1) γ^(T-h) 理论与 GRPO 不匹配（GRPO 无显式\\n    γ），(2) novelty 不足（episode-level 是 REINFORCE default），(3) 统计 power 不足，(4) 缺 GAE\\n    baseline。修正：理论改为 \\\"information bottleneck + gradient signal dilution\\\" 双机制；加 GAE(λ=0.95)\\n    baseline；multi-seed 升至 5；h-sweep 每个 h 3 seeds。总 GPU 预算 P0 从 268h 升至 438h。确认 dual\\n    contribution framing 保持（不退到纯 methodology）。\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: basis\\n    result: step5_val=25%\\n  - exp_id: exp028c_selfguide_recipe\\n    role: basis\\n    result: step10_val=0%\\n  depends_on:\\n  - D054\\n  - D053\\n- id: D056\\n  date: 2026-05-17 03:32 UTC\\n  summary: Negative 复盘发现：episode-level + valid_action_bonus 可能安全（exp013f gaming 是\\n    step_independent 特有），加入 h-sweep 批次验证\\n  rationale: exp013f 证伪了 \\\"dense reward shaping 帮助 GRPO\\\"，但其 gaming 行为（action_is_valid\\n    97% + task success 0%）是 step_independent 特有的：每步独立优化允许只最大化 per-step bonus。Episode-level\\n    下模型必须优化 trajectory-level total reward，无法独立 game。当前 exp029 的 action_is_valid=55.9%\\n    且在下降，加小 bonus 可能提供额外信号打破 23-25% plateau。这是从 negative 推导的假设，有明确的 parent 链。\\n  related_experiments:\\n  - exp_id: exp013f\\n    role: parent_negative\\n    result: reward gaming under step_independent\\n  - exp_id: exp029_episode_level\\n    role: target\\n    result: plateau at 23-25%, action_is_valid declining\\n  depends_on:\\n  - D055\\n  - D051\\n- id: D057\\n  date: 2026-05-17 04:16 UTC\\n  summary: Early-stop exp029 at step 15 (val=28%, pass@8=92.9%), release GPUs for\\n    h-sweep (plan_002, paper core figure)\\n  rationale: 'Step 15 val=28.125% (marginal +3pp over step 5-10), action_is_valid\\n    degrading (78→55%), action_is_effective dropped to 77%. Continuing has low ROI:\\n    pass@8=92.9% already proves capability exists, main problem is consistency which\\n    current config won''t fix. h-sweep (plan_002) is P0 for paper — shows the cliff\\n    mechanism, directly addresses Dream C1/C2 reviewer concerns. Checkpoint preserved\\n    for future resume. Plan_003c (bonus variant) included in h-sweep batch.'\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: early_stopped\\n    result: step15_val=28.125%_pass@8=92.9%\\n  - exp_id: exp028c_selfguide_recipe\\n    role: comparison\\n    result: step10_val=0%\\n  depends_on:\\n  - D056\\n  - D055\\n- id: D058\\n  date: 2026-05-17 06:22 UTC\\n  summary: 'Theory correction: \\\"flat advantage\\\" → \\\"γ-attenuated credit + undifferentiated\\n    failure\\\" based on source code verification'\\n  rationale: Agent 源码审计发现 RAGEN step_independent 实现中 compute_step_discounted_returns()\\n    使用 γ-discount，per-window return 不同（非 flat）。实际机制：成功 episode 早期 window 获 γ^k 衰减\\n    return（γ^{N-1}=γ^24≈29%, where N=⌈T/h⌉=25），失败 episode 所有 window 获相同近零 advantage。这比之前的\\n    \\\"identical advantage\\\" 假设更精确，也比最初的 \\\"GRPO has γ\\\" 更 nuanced（γ 在实现层非算法层）。批准 h=2 seed\\n    2 启用 per-window advantage logging 收集实证。\\n  related_experiments:\\n  - exp_id: hsweep_h2_seed1\\n    role: ongoing\\n    result: source code audit during run\\n  - exp_id: exp029\\n    role: baseline\\n    result: episode-level comparison\\n  depends_on:\\n  - D055\\n  - D056\\n- id: D059\\n  date: 2026-05-17 08:11 UTC\\n  summary: h-sweep val 用 post-hoc full-context eval 替代 truncated val，不重启训练\\n  rationale: Reviewer 发现 hsweep val 也受 context_window_mode 影响（h=2 val step 0 = 0%），无法作为纯\\n    credit assignment 崩溃证据。解决方案：训练继续（收集 train metrics），完成后对所有 checkpoint 用 full context\\n    做 post-hoc val eval。这样 cliff figure 的 val 曲线只反映 training credit assignment 效果，不混入\\n    inference context 限制。不重启当前 seed 1（已跑 3h，train metrics 仍有价值）。\\n  related_experiments:\\n  - exp_id: hsweep_h2_seed1\\n    role: trigger\\n    result: val step 0 = 0% due to context truncation\\n  - exp_id: exp028c\\n    role: reference\\n    result: val uses full context, valid collapse evidence 6.25%→0%\\n  depends_on:\\n  - D057\\n\", \"total_chars\": 43377, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cceffbf-00b0-4eae-8542-aa5439f4a4fe",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "409e1aa8-1471-4d9a-ac19-62e0cbf71579",
  "sourceToolAssistantUUID": "1cceffbf-00b0-4eae-8542-aa5439f4a4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-17T12:56:12.310Z_

I now have comprehensive information about the paper, its development history, the literature landscape, and the experimental results. Let me also check the earlier dream review to understand prior feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "409e1aa8-1471-4d9a-ac19-62e0cbf71579",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BFTW1t7cjPbpuEU8iN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e014f7f6-7a11-4487-9681-77a3baa13368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRzt9byhHfRqZbJpBmvDAa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25168,
      "cache_read_input_tokens": 51723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25168,
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

_source line 31 · 2026-05-17T12:56:14.268Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MNbue6aNoqSN6twZDCyV1u`</summary>

```json
{
  "pattern": "**/dream_*/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e014f7f6-7a11-4487-9681-77a3baa13368",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BFTW1t7cjPbpuEU8iN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87d2acec-af95-438f-a14d-7203ee990b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRzt9byhHfRqZbJpBmvDAa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25168,
      "cache_read_input_tokens": 51723,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25168
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 51723,
          "cache_creation_input_tokens": 25168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25168,
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

_source line 32 · 2026-05-17T12:56:14.284Z_

<details><summary>↩ Tool result · `toolu_01MNbue6aNoqSN6twZDCyV1u`</summary>

```text
artifacts/dream_reports/dream_20260516T235255/best/paper_framing.md
artifacts/dream_reports/dream_20260516T235255/median/paper_framing.md
artifacts/dream_reports/dream_20260516T235255/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T235255/best/review_report.md
artifacts/dream_reports/dream_20260516T235255/median/review_report.md
artifacts/dream_reports/dream_20260516T235255/worst/review_report.md
artifacts/dream_reports/dream_20260517T121256/best/paper_framing.md
artifacts/dream_reports/dream_20260517T121256/median/paper_framing.md
artifacts/dream_reports/dream_20260517T121256/worst/paper_framing.md
artifacts/dream_reports/dream_20260517T121256/best/review_report.md
artifacts/dream_reports/dream_20260517T121256/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87d2acec-af95-438f-a14d-7203ee990b25",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "6f7f2d13-e0e9-4f3b-a2f7-1796799a7b97",
  "sourceToolAssistantUUID": "87d2acec-af95-438f-a14d-7203ee990b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T12:56:17.172Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dg1qx7SCqDfYrg3EMaqn52`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7f2d13-e0e9-4f3b-a2f7-1796799a7b97",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BFspkBgXGFtnZeeqEq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a5a1cf7-198b-4f22-b7e5-ddd814926517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vv1JdiqtR12hmxzXdPDuE7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 76891,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 76891,
          "cache_creation_input_tokens": 417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 417,
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

_source line 34 · 2026-05-17T12:56:17.188Z_

<details><summary>↩ Tool result · `toolu_01Dg1qx7SCqDfYrg3EMaqn52`</summary>

```text
1	---
2	dream_id: dream_20260517T121256
3	tier: median
4	overall_score: borderline reject
5	timestamp: 2026-05-17T12:53:52.264332+00:00
6	---
7	
8	# Dream Review Report: Diagnosing Step-Independent RL Failure in Multi-Turn LLM Agents
9	
10	**Paper:** Diagnosing Step-Independent RL Failure in Multi-Turn LLM Agents: Sign Misattribution, Information Loss, and Selective Verification
11	**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
12	**Date:** 2026-05-17
13	
14	---
15	
16	## Overall Assessment
17	
18	**Score: 3/6 (Borderline Reject)**
19	
20	The paper identifies a real and underexplored failure mode in step-independent RL training for multi-turn LLM agents. The diagnostic contribution (sign misattribution + information loss) is the paper's strongest element and fills a genuine gap. However, the paper falls short of the top-venue bar due to: (1) missing mechanism isolation experiments that confound the two claimed failure modes, (2) insufficient statistical rigor across all results, (3) a selective verification component (B-IAVR) that occupies substantial space but delivers weak, statistically unsupported evidence, (4) critically thin related work with only 10 references, and (5) absence of any figures. The paper has a publishable core idea that needs significant revision.
21	
22	---
23	
24	## Reviewer Reports
25	
26	### R1: Methods and Experiments (Score: 3/6, Confidence: 4/5)
27	
28	**Summary:** The paper presents a dual-mechanism diagnosis of step-independent RL failure with thorough empirical coverage (13 experimental subsections). The diagnostic half is solid but methodologically incomplete; the selective verification half is statistically weak and dilutes the paper's focus.
29	
30	**Strengths:**
31	- The h-sweep ablation (Table 1) provides clean, reproducible evidence of degradation: monotonic drop from 34% (full) to 2.3% (h=2) with clear cliff zone at h∈[2,5]. This is the paper's most convincing experiment.
32	- Mechanistic verification (Table 2) directly measures the claimed failure mode with concrete metrics: r=0.87 sign-outcome correlation vs r=0.12 sign-local quality. The 92%/89% success/failure sign consistency provides intuitive confirmation.
33	- GAE comparison (Table 4) is honestly calibrated. Positioning episode-level GRPO as "minimum viable fix" while showing GAE outperforms by 8pp demonstrates intellectual honesty and strengthens rather than weakens the diagnostic narrative.
34	- Comprehensive experiment coverage: all 14 experiments from the design are present, including valid-action bonus, entropy-controlled analysis, causal intervention, reward signal ablation, and ARES comparison.
35	- Per-task breakdown (Table 6) with r=-0.72 length-success correlation provides useful granularity for understanding where episode-level credit fails.
36	
37	**Weaknesses:**
38	- **Missing mechanism isolation (Major):** The paper claims two distinct failure mechanisms but never separates them experimentally. A critical missing experiment: step-independent training with full episode context (i.e., full context window but per-window advantages). This would isolate sign misattribution from information loss. Without it, the relative contribution of each mechanism is unknown, and the "dual mechanism" claim is confounded.
39	- **No statistical significance testing (Major):** With std=5.9pp (Table 3), many key comparisons have overlapping confidence intervals. Episode-level (32±5%) vs GAE λ=1.0 (37±4%): the 5pp delta is within 1 std. B-IAVR (27%) vs random p=0.5 (26%): 1pp delta with no reported error bars or p-values. No pairwise significance tests are reported anywhere in the paper.
40	- **B-IAVR does not dominate random on Pareto frontier (Major):** Table 12 shows random p=0.5 achieves Success/Cost=0.473 vs B-IAVR's 0.375. The no-verify baseline achieves 0.489. B-IAVR is Pareto-dominated by simpler baselines when cost-efficiency is the metric. The paper acknowledges the margins are "modest (1-2pp)" but still presents this as a contribution rather than a negative result.
41	- **B-IAVR lacks multi-seed replication:** The main episode-level result has 5 seeds, but B-IAVR training (Tables 11-14) appears to be single-seed. Given the 5.9pp seed variance of the base method, B-IAVR results could shift substantially.
42	- **Action-change signal barely significant:** Partial correlation after entropy control is r=0.11 (p=0.038). This would not survive Bonferroni correction across the multiple comparisons in this paper. The foundation for the entire B-IAVR reward signal is statistically fragile.
43	- **No figures:** The paper has zero figures across 11 pages. For a diagnostic paper, visualizations of the h-sweep curve, the sign misattribution scatter plot, and the Pareto frontier would substantially strengthen the claims. Tables alone cannot convey the gradient degradation pattern effectively.
44	- **Missing reproducibility details:** No hyperparameter tables, no compute budget, no training duration, no GRPO-specific parameters (KL coefficient, clipping). The Method section is thin on implementation.
45	- **Causal intervention sample size:** Table 10 uses n=200 episodes per condition. With binary outcomes and success rates of 24-32%, confidence intervals are approximately ±6pp, making the 4pp and 8pp deltas marginally significant at best.
46	
47	**Questions for Authors:**
48	1. Can you run step-independent training with full context but per-window advantages to isolate sign misattribution from information loss?
49	2. What are p-values for episode-level vs step-independent, episode-level vs GAE, and B-IAVR vs random comparisons?
50	3. How many seeds were used for B-IAVR experiments?
51	4. What is the compute budget per experimental configuration?
52	
53	---
54	
55	### R2: Novelty and Related Work (Score: 4/6, Confidence: 4/5)
56	
57	**Summary:** The paper formalizes a practical failure mode that the LLM agent training community has likely encountered but not systematically characterized. The sign misattribution insight, while somewhat predictable from RL theory, is empirically validated in a useful way. However, thin related work, zero algorithmic novelty, and missing engagement with closely related concurrent work (Turn-PPO) weaken the contribution.
58	
59	**Strengths:**
60	- The sign misattribution formalization fills a genuine gap. While the credit assignment problem in long-horizon RL is well-studied, the specific manifestation in GRPO-based LLM agent training (where binary terminal rewards + group normalization create deterministic sign corruption) has not been explicitly documented with empirical measurements.
61	- "Contrarian solution" framing is intellectually interesting: coarser but correctly-signed credit (episode-level) outperforms finer but corrupted credit (step-independent). This challenges the intuition that more granular credit assignment is always better, and the GAE comparison properly calibrates when finer credit IS better (with a learned critic).
62	- Honest positioning throughout: "minimum viable fix," "preliminary evidence," explicit limitation acknowledgments. The paper does not oversell. This is unusual and appreciated.
63	- The combination of h-sweep + mechanistic verification + GAE calibration forms a coherent diagnostic toolkit that other researchers could apply to their own multi-turn training setups. This has practical community value.
64	
65	**Weaknesses:**
66	- **Core insight is somewhat predictable (Moderate):** For anyone familiar with REINFORCE, policy gradient theory, and GRPO's group normalization, the sign misattribution result follows almost mechanically: binary reward + group norm + γ-discounting across windows = advantages determined by episode outcome. The empirical verification adds value, but the theoretical insight itself is not deep. A reviewer with RL background would say "of course this happens."
67	- **Episode-level GRPO = REINFORCE (Major for novelty):** The proposed "fix" has zero algorithmic novelty. Treating the full episode as one sample with shared advantage is standard REINFORCE. The paper acknowledges this but spends significant space on what is effectively "use REINFORCE instead of this broken thing." The value is diagnostic, not methodological.
68	- **Turn-PPO engagement missing (Major):** Turn-PPO (Xiong et al.) identifies "uniform advantage" as a problem in multi-turn GRPO and proposes per-turn value estimation. This is closely related to the sign misattribution mechanism. The paper does not cite or discuss Turn-PPO. This is a significant related work gap that reviewers will notice.
69	- **Only 10 references (Major):** For a top ML venue, 10 references is unacceptable. Missing categories include:
70	  - Multi-turn agent RL: AgentQ, ArCHer, TWOSOME, DigiRL
71	  - Credit assignment beyond GAE: RUDDER, HCA, hindsight credit assignment
72	  - Self-correction/verification: Reflexion, Self-Refine, inner monologue
73	  - Process reward models: PRM literature connecting step-level rewards to credit assignment
74	  - Concurrent GRPO-for-agents work beyond RAGEN
75	- **Related Work section too thin (~1 page, 3 short paragraphs):** Each subsection covers 2-3 papers with minimal analysis. No comparative table, no positioning diagram. The distinctions from ARES and Thinkless are stated but not argued in depth. A reviewer cannot assess whether the authors understand the landscape.
76	- **Performance gap to SoTA unexplained:** Episode-level GRPO achieves 30.6% on ALFWorld vs ReflAct 93.3% (GPT-4) and Self-Guide 72.7% (1.7B + SFT + verification). The paper notes it is "not on maximizing ALFWorld performance" but does not adequately explain what additional ingredients (SFT pretraining, larger models, prompting strategies) account for the 40+pp gap to Self-Guide with the same model size. This limits the practical significance of the diagnostic.
77	- **B-IAVR novelty is incremental:** The selective verification formulation combines elements from Thinkless (RL-trained selection) and ARES (adaptive verification), with action-change as the reward signal being the main novelty. But action-change as a proxy for informativeness is intuitive rather than principled, and the empirical evidence for its value is weak (r=0.11).
78	
79	**Questions for Authors:**
80	1. How does your sign misattribution mechanism relate to Turn-PPO's "uniform advantage" problem? Is sign misattribution a strict superset?
81	2. What accounts for the gap between your 30.6% and Self-Guide's 72.7% with the same model size? Does Self-Guide use SFT pretraining that your setup lacks?
82	3. Could process reward models (PRMs) serve as an alternative to GAE for providing step-level credit without a separate critic?
83	4. Have you considered Reflexion-style approaches as baselines for the verification component?
84	
85	**Minor Issues:**
86	- Abstract uses "LLM" without expansion (though commonly understood, formal venues require it)
87	- Several em-dashes present in the text (AI writing marker)
88	- "h-sweep" terminology not standard; "context window ablation" would be clearer
89	
90	---
91	
92	## Roundtable Discussion
93	
94	### Step 2: Cross-Share
95	
96	R1 and R2 were presented each other's reviews for cross-evaluation.
97	
98	### Step 3: Convergence
99	
100	**Points of Agreement (both reviewers):**
101	1. **Diagnostic contribution is the paper's core value.** The sign misattribution formalization (r=0.87), h-sweep degradation curve, and honest GAE calibration form a coherent and useful diagnostic. Both reviewers rate this positively.
102	2. **B-IAVR / selective verification is the weakest section.** It occupies ~3 pages but delivers statistically unsupported results. B-IAVR does not dominate random on the Pareto frontier, margins are 1-2pp (within noise), and the underlying signal (r=0.11) is barely significant. Both recommend either substantially strengthening or removing this component.
103	3. **10 references is unacceptable.** Both flag thin related work as a major issue. Missing Turn-PPO engagement, missing multi-turn agent RL literature, missing verification/self-correction references.
104	4. **Missing mechanism isolation** is a real experimental gap. The two mechanisms (information loss, sign misattribution) are confounded without a full-context + per-window-advantages control.
105	5. **No figures.** For a diagnostic paper, the absence of any visualizations is a significant presentation weakness.
106	
107	**Points of Disagreement:**
108	- R2 is more generous (4/6) than R1 (3/6), primarily because R2 gives more weight to the "contrarian framing" and community utility of the diagnostic. R2 argues the formalization fills a genuine gap even if the insight is somewhat predictable.
109	- R1 places more weight on statistical rigor: the high variance (5.9pp), overlapping CIs, and absent p-values make R1 less confident that the reported deltas are real rather than noise.
110	- R2 considers the novelty question more nuanced (formalization of a known-but-undocumented phenomenon has value), while R1 focuses on whether the experiments actually prove what they claim.
111	
112	**Resolution:** The diagnostic contribution alone is borderline for a top venue. It is useful but not deep: the theoretical insight is somewhat predictable, and the empirical verification, while clean, lacks mechanism isolation. The selective verification component actively hurts the paper by introducing weak evidence and diffusing focus. The paper as submitted falls just below the acceptance threshold.
113	
114	### Step 4: Consolidated Assessment
115	
116	| Criterion | Rating | Notes |
117	|-----------|--------|-------|
118	| Soundness | 3/5 | Diagnostic formulation correct; mechanism isolation missing; B-IAVR statistically unsupported |
119	| Novelty | 2.5/5 | Formalization of a somewhat predictable insight; zero algorithmic novelty; Turn-PPO gap |
120	| Significance | 3/5 | Community utility of diagnostic is real; absolute performance far from SoTA limits impact |
121	| Presentation | 2/5 | No figures, 10 references, thin related work, no reproducibility details |
122	| Completeness | 3.5/5 | All planned experiments present; but missing mechanism isolation control and multi-seed B-IAVR |
123	
124	**Overall: 3/6 (Borderline Reject)**
125	
126	---
127	
128	## Actionable Recommendations (Priority Order)
129	
130	1. **Add mechanism isolation experiment:** Run step-independent with full context but per-window advantages. This separates information loss from sign misattribution and would substantially strengthen the "dual mechanism" claim.
131	
132	2. **Add figures:** At minimum: (a) h-sweep line plot with error bars showing the degradation curve, (b) sign misattribution scatter plot (advantage sign vs episode outcome), (c) Pareto frontier for selective verification methods. These are essential for a diagnostic paper.
133	
134	3. **Expand references to 25-30+:** Engage with Turn-PPO (uniform advantage), AgentQ/ArCHer/DigiRL (multi-turn agent RL), Reflexion/Self-Refine (verification), PRM literature (step-level credit). The current 10 references signal incomplete literature awareness.
135	
136	4. **Add statistical significance tests:** Report p-values or confidence intervals for all key pairwise comparisons. At minimum: episode-level vs step-independent, episode-level vs GAE, B-IAVR vs random baseline.
137	
138	5. **Restructure the paper:** Consider two options:
139	   - (A) **Diagnostic-focused paper:** Drop or severely compress B-IAVR to 1 paragraph of preliminary results. Use recovered space for deeper mechanism analysis, mechanism isolation, and expanded related work. This is the stronger submission.
140	   - (B) **Keep B-IAVR but add multi-seed replication** and honest Pareto analysis showing B-IAVR does not dominate random. Frame as a negative/informative result about the difficulty of learned verification scheduling at low base performance levels.
141	
142	6. **Engage with Turn-PPO:** Formally argue whether sign misattribution subsumes or is distinct from "uniform advantage." This positioning is critical for novelty claims.
143	
144	7. **Discuss performance gap to SoTA:** Explain what ingredients (SFT pretraining, prompting, larger models) separate 30.6% from Self-Guide's 72.7%. This contextualizes the diagnostic contribution's practical relevance.
145	
146	8. **Add reproducibility details:** Hyperparameter table, compute budget, training duration, GRPO parameters (group size, KL coefficient, clipping), hardware specifications.
147	
148	---
149	
150	## Experiment Coverage Assessment
151	
152	All 14 experiments from the design are present in the paper:
153	- [x] H-sweep ablation (Table 1)
154	- [x] Mechanistic verification (Table 2)
155	- [x] Multi-seed replication (Table 3)
156	- [x] GAE baseline comparison (Table 4)
157	- [x] Valid action bonus (Table 5)
158	- [x] Per-task analysis (Table 6)
159	- [x] ScienceWorld transfer (Table 7)
160	- [x] 7B scaling (Table 8)
161	- [x] Action-change statistics (Table 9)
162	- [x] Entropy-controlled analysis (in text)
163	- [x] Causal intervention (Table 10)
164	- [x] B-IAVR training (Table 11)
165	- [x] Full selective comparison (Table 12)
166	- [x] Reward signal ablation (Table 13)
167	- [x] ARES comparison (Table 14)
168	
169	Coverage is complete but lacks one critical experiment not in the original design: mechanism isolation (full context + per-window advantages).
170	
171	---
172	
173	*Review conducted by: Dream Review Director (2 Reviewers, Full Roundtable)*
174	*R1 Focus: Methods + Experiments | R2 Focus: Novelty + Related Work*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a5a1cf7-198b-4f22-b7e5-ddd814926517",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "de596fd4-4de8-4f35-99b3-ec14eaceeba1",
  "sourceToolAssistantUUID": "6a5a1cf7-198b-4f22-b7e5-ddd814926517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-17T12:56:21.382Z_

Now I have all the information needed to produce a thorough R2 review. Let me now write it, focusing on novelty and related work as instructed, and referencing the actual "best" paper version (the one submitted for this review round).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de596fd4-4de8-4f35-99b3-ec14eaceeba1",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BG6H6d6rsPVgg6kfsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9469b2b-3fa4-4e55-93df-9a4a4c0234ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcWc2NebF7VXaTYK9kfXVC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 77308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4792,
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

_source line 36 · 2026-05-17T12:56:22.291Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018uZFkV2UHqiMvSSU9Zw3kV`</summary>

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
  "parentUuid": "e9469b2b-3fa4-4e55-93df-9a4a4c0234ef",
  "isSidechain": true,
  "agentId": "adca5254a363aca6d",
  "requestId": "req_011Cb8BG6H6d6rsPVgg6kfsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "937661b0-078d-4948-b2fb-219bd5535e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcWc2NebF7VXaTYK9kfXVC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 77308,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4792
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 77308,
          "cache_creation_input_tokens": 4792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4792,
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

_source line 37 · 2026-05-17T12:56:22.294Z_

<details><summary>↩ Tool result · `toolu_018uZFkV2UHqiMvSSU9Zw3kV`</summary>

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
  "parentUuid": "937661b0-078d-4948-b2fb-219bd5535e75",
  "isSidechain": true,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "agentId": "adca5254a363aca6d",
  "type": "user",
  "uuid": "7cc28ad8-a056-4229-851e-3cfac5e430b7",
  "sourceToolAssistantUUID": "937661b0-078d-4948-b2fb-219bd5535e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
