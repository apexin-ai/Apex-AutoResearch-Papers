# Research conversation: You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your foc

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae34cf52ed66373af.jsonl`
- **Structured JSON:** [`9272e8365b54f92c5ff5.json`](../../sessions/92/9272e8365b54f92c5ff5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-17T14:16:40.261Z_

You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus: **novelty, positioning, and related work**.

## Paper Summary
"Credit Assignment Granularity in Multi-Turn Agent RL: An Empirical Taxonomy of Failure Modes"

The paper studies credit assignment granularity in multi-turn agent RL on ALFWorld, comparing step-independent GRPO, episode-level GRPO, and GAE. Framed as an "empirical taxonomy of failure modes." Three contributions claimed:
1. Multi-seed characterization of step-independent performance cliff (stochastic, seed-dependent)
2. Mechanistic evidence for advantage sign misattribution (exists but weaker than predicted)
3. Negative result showing selective verification fails at <30% base agent competence
Plus cross-environment (ScienceWorld) and cross-scale (7B) experiments.

## Paper Structure (9 pages)
- Abstract: 150+ words, frames as empirical study of credit assignment granularity
- Introduction: Sets up contrarian hypothesis ("coarser might suffice"), then immediately concedes it's false
- Section 2 (Related Work): Multi-turn agent RL, credit assignment in LLM RL, self-verification
- Section 3 (Method): Problem setting, three credit assignment variants (step-independent, episode-level, GAE), selective verification (B-IAVR), hypothesized failure mechanisms
- Section 4 (Experiments): h-sweep, multi-seed, GAE comparison, sign misattribution verification, valid action bonus, selective verification (6 subsections), transfer & scaling
- Section 5 (Discussion): Three paragraphs
- Section 6 (Conclusion): One paragraph
- Limitations: One paragraph

## Key Results
- Step-independent h-sweep: stochastic cliff, h=5 has 10.4pp std across 3 seeds
- Episode-level GRPO: 23.8% mean, plateaus, massively outperformed by GAE (43.8%)
- Sign misattribution: exists but weak (0.72 vs predicted >0.95 correlation)
- B-IAVR: complete failure, Pareto-dominated by random baselines
- ScienceWorld: 3pp advantage, not significant (p=0.38)
- 7B: gap narrows from 28pp to 13pp

## Related Work Mentioned in Paper
- RAGEN: step-independent GRPO for multi-turn agents
- ArCher: hierarchical RL for multi-turn agents
- HiPER: 97.4% on ALFWorld at 7B
- GAGPO: 93.5% on ALFWorld at 1.5B
- Turn-PPO: turn-level value functions
- MT-GRPO: turn-level rewards for QA
- iStar: implicit process reward with dual advantages
- Zhang et al. survey: 47 credit assignment methods
- Self-Guide: always-on verification, 72.7% ALFWorld at 1.7B
- ARES: supervised verification router, 52.7% token reduction
- ReflAct: prompting-based reflection with GPT-4

## Important Context
The paper's original framing was "coarser credit suffices" (contrarian positioning). The data directly refutes this:
- GAE >> episode-level GRPO by 20pp
- The community consensus (finer credit is better) is correct
- The paper pivoted to "empirical taxonomy of failure modes"

The best result in this paper (GAE at 43.8%) is far below SOTA:
- HiPER: 97.4% ALFWorld (7B)
- GAGPO: 93.5% ALFWorld (1.5B)
- Self-Guide: 72.7% ALFWorld (1.7B)

## Your Review Task
Evaluate:

1. **Novelty**: Is "coarser credit fails" novel? The community already pursues finer credit. Does confirming the consensus add value? Is "taxonomy of failure modes" a sufficient intellectual contribution?
2. **Positioning**: The paper starts with a contrarian hypothesis then immediately admits it's wrong. Does this framing work? Is it honest academic practice or does it read like a pivot?
3. **Related work completeness**: Are key references missing? Is the positioning against prior work accurate?
4. **Contribution significance**: Would a top venue accept: (a) confirming that GAE > episode-level GRPO, (b) characterizing a stochastic cliff with 3 seeds, (c) a negative result on selective verification where the base agent is too weak to meaningfully test the idea?
5. **Narrative coherence**: Does the paper tell a coherent story or does it read like a collection of negative results repackaged?
6. **Comparison to SOTA**: The paper's best is 43.8% vs 72-97% in prior work at same or smaller scale. Does this undermine the findings?

Output format:
```
## R2 Review: Novelty & Related Work

### Summary
[2-3 sentences]

### Strengths
[Bulleted list with specifics]

### Weaknesses
[Bulleted list with specifics, most critical first]

### Questions for Authors
[Numbered list]

### Assessment of Contribution Significance
[1-2 paragraphs]

### Minor Issues
[Bulleted list]

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "d113a690-745d-486a-a001-a5db3d2e87cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T14:16:40.265Z_

```json
{
  "parentUuid": "d113a690-745d-486a-a001-a5db3d2e87cf",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
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
  "uuid": "094d4bc6-ece2-4289-ba91-240fdbb0bfff",
  "timestamp": "2026-05-17T14:16:40.265Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T14:16:43.947Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ELFwcQcSfJpjCpC6H1VQLg`</summary>

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
  "parentUuid": "094d4bc6-ece2-4289-ba91-240fdbb0bfff",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HPcyTEP3i83RfFyqc7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb1867e9-6a46-4bd4-b50b-77dfffec0dbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQspKgUcgai14ZCDAFQMcc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8398,
      "cache_read_input_tokens": 8252,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8398
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 8398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8398,
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

_source line 4 · 2026-05-17T14:16:43.951Z_

<details><summary>↩ Tool result · `toolu_01ELFwcQcSfJpjCpC6H1VQLg`</summary>

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
  "parentUuid": "bb1867e9-6a46-4bd4-b50b-77dfffec0dbd",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "b7a5b359-cc97-47e8-9e7b-5343a9afed83",
  "sourceToolAssistantUUID": "bb1867e9-6a46-4bd4-b50b-77dfffec0dbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T14:16:54.448Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016tisz4N9pjv1tLtWhMiYiB`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7a5b359-cc97-47e8-9e7b-5343a9afed83",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HPtv9p9UrCFVPg6jUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "858694fb-6685-45ec-97bf-d6139a8964e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01697yW17RCHRKzeRTNtZ4Tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 6 · 2026-05-17T14:16:54.460Z_

<details><summary>↩ Tool result · `toolu_016tisz4N9pjv1tLtWhMiYiB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-17\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    ti\\n\\n... [截断: 省略 17932 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 29932, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "858694fb-6685-45ec-97bf-d6139a8964e2",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "328352c9-d46b-41f8-ba2a-b4b3feaa7e1f",
  "sourceToolAssistantUUID": "858694fb-6685-45ec-97bf-d6139a8964e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T14:16:55.084Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XUNat7UcocuTVYuEJJN58e`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "328352c9-d46b-41f8-ba2a-b4b3feaa7e1f",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HPtv9p9UrCFVPg6jUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4fd296b-0e5a-4213-87cd-d04a721ec97c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01697yW17RCHRKzeRTNtZ4Tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 8 · 2026-05-17T14:16:55.102Z_

<details><summary>↩ Tool result · `toolu_01XUNat7UcocuTVYuEJJN58e`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cost-verify-agent-rl'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4fd296b-0e5a-4213-87cd-d04a721ec97c",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "5a4a57ed-f217-4bed-89c2-4a4e75b72901",
  "sourceToolAssistantUUID": "e4fd296b-0e5a-4213-87cd-d04a721ec97c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T14:16:59.459Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01T8PsMys6ifRafKpxJ9Akuh`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a4a57ed-f217-4bed-89c2-4a4e75b72901",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HQjdpz7SU7hMK8Btyd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b14541e-9854-4c36-9255-f229ab35bfff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7GDbr3PDcwaz4basAb4Ho",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4906,
      "cache_read_input_tokens": 17919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4906,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T14:16:59.470Z_

<details><summary>↩ Tool result · `toolu_01T8PsMys6ifRafKpxJ9Akuh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gsweep_g050_h5_seed1 | γ=0.5 with h=5 will show accelerated collapse compared to default γ=0.95, because γ^k decay compounds: early windows receive only γ^(N-1) ≈ 0.5^9 ≈ 0.2% of terminal return, making sign misattribution maximally severe. | — | — | — |\\n| hsweep_h2_seed1 | Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality | — | — | — |\\n\\n## 待处理\\n- gae_baseline_seed1（准备中）\\n- gsweep_g100_h5_seed1: γ=1.0 with h=5 means no discount (all windows receive full terminal return). If collapse is driven by sign misattribution from discounting, γ=1.0 should show least collapse. But uniform return may reduce temporal credit assignment sharpness.（准备中）\\n- gsweep_g095_h5_seed1: γ=0.95 with h=5 is the control condition matching hsweep_h5. Early windows retain γ^9 ≈ 0.95^9 ≈ 63% of terminal return. Expected to reproduce h5 behavior from h-sweep.（准备中）\\n- gsweep_g080_h5_seed1: γ=0.8 with h=5 represents an intermediate decay rate where early windows retain γ^9 ≈ 0.8^9 ≈ 13% of terminal return, potentially showing delayed but still present collapse compared to γ=0.95 (39%).（准备中）\\n- exp028_prereq_zeroshot_instruct: Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\\\"SFT是毒药\\\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。（准备中）\\n- exp021_sft_ragen_format: Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.（准备中）\\n- exp020d_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.（准备中）\\n- exp020c_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).（准备中）\\n- exp019c_expert_sft_v3: Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。（准备中）\\n- exp019b_expert_sft_v2（准备中）\\n- …另有 12 项\\n\\n## 近期结论\\n- **exp025c** (killed): —\\n- **exp029_episode_level** (success): Episode-level 训练（context_window_mode: full）解决 step_independent h=2 的信用分配缺陷，模型能学到跨步规划策略，val success 不再停滞于 baseline。 ← 基于 exp028c_selfguide_recipe\\n  [exp029_episode_level_diagnose_attempt4](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/report/diagnose_attempt4.md) | [tatsu_patch_deploy_plan](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/intermediate/tatsu_patch_deploy_plan.md) | [credit_assignment_analysis](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/exp029_episode_level/chart/credit_assignment_analysis_info.md)\\n- **exp026_step_independent_grpo** (negative): Step-independent GRPO（每步独立优化、不建模跨步依赖）能在ALFWorld多步任务中学到有效策略，因为每步的local reward信号足以引导正确行为选择 ← 基于 exp021_ragen_sft_v4\\n\\n## 趋势\\n成功 4 / 负向 5 / 失败 19 / 共 38\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-17606: 无 GPU 信息\\nwestd-47453: 无 GPU 信息\\n\\n## 告警\\n- exp_001: 训练失败 — unknown\\n- exp_001b: 训练失败 — unknown\\n- exp_002: 训练失败 — unknown\\n- exp003: 训练失败 — unknown\\n- exp007: 训练失败 — unknown\\n- exp009: 训练失败 — unknown\\n- exp010: 训练失败 — unknown\\n- exp011: 已被终止 — unknown\\n- exp012: 训练失败 — unknown\\n- exp012b: 已被终止 — unknown\\n- exp013: 已被终止 — unknown\\n- exp013b: 训练失败 — unknown\\n- exp013c: 已被终止 — unknown\\n- exp013d: 训练失败 — unknown\\n- exp013e: 训练失败 — unknown\\n- exp015: 已被终止 — unknown\\n- exp016: 训练失败 — unknown\\n- exp019_expert_sft_v2: 已被终止 — unknown\\n- exp020_grpo_from_sft: 训练失败 — unknown\\n- exp022_grpo_from_sft_v4: 已被终止 — unknown\\n- exp023_grpo_parallel: 训练失败 — unknown\\n- exp023c_grpo_serial: 训练失败 — unknown\\n- exp024_success_gated_grpo: 已被终止 — unknown\\n- exp025: 训练失败 — unknown\\n- exp025b: 训练失败 — unknown\\n- exp025c: 已被终止 — unknown\\n- exp027_stable_grpo: 训练失败 — unknown\\n- exp028a_recipe_fix: 已被终止 — unknown\\n- exp028c_selfguide_recipe: 训练失败 — unknown\\n\", \"total_chars\": 4735, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b14541e-9854-4c36-9255-f229ab35bfff",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "81eb80bf-32f5-4638-8d27-ecadc2cd4235",
  "sourceToolAssistantUUID": "5b14541e-9854-4c36-9255-f229ab35bfff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T14:16:59.880Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YS1scNUHhgt1Aa4ZphzMTu`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81eb80bf-32f5-4638-8d27-ecadc2cd4235",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HQjdpz7SU7hMK8Btyd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c71947b-3931-47e9-a671-6de1fd287d1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7GDbr3PDcwaz4basAb4Ho",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4906,
      "cache_read_input_tokens": 17919,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 17919,
          "cache_creation_input_tokens": 4906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4906,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T14:16:59.893Z_

<details><summary>↩ Tool result · `toolu_01YS1scNUHhgt1Aa4ZphzMTu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents\\n\\n> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)\\n\\n## Core Insight\\n\\nMulti-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：\\n\\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \\\"先探索 drawer 再去 countertop\\\"）\\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：\\n   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）\\n   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）\\n   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality\\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%, where 24 = ⌈T/h⌉-1 windows），但方向错误比幅度衰减更致命\\n\\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\\n\\n**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。\\n\\n## Story Arc\\n\\n**Dual contribution**: Training methodology diagnosis + Selective verification system\\n\\n叙事线：\\n1. Self-verification 对 interactive agents 有用，但 always-on 成本高\\n2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）\\n3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决\\n4. 分析 \\\"为什么社区默认走向 step-independent\\\"（context window 限制 + token-level training 惯性 + framework design accident）\\n5. 在 episode-level 基础上，用 action-change 作为 verification informativeness 的 reward，训练 selective policy\\n6. 结果：near-always-on performance + 显著降低 verification cost\\n\\n**定位**：不 claim \\\"发明了 episode-level RL\\\"（trivial），而是 \\\"诊断了 LLM agent RL 训练中被忽视的 step-independent 隐性代价 + 系统分析崩溃机制 + 提出实用修复方案 + 在此基础上实现 selective verification\\\"\\n\\n## Target Venue\\n\\n待定（NeurIPS 2026 / EMNLP 2026 / ICLR 2026），取决于实验进度和最终效果。\\n\\n## Core Claims\\n\\n### Claim 1 (strength: strong): Step-independent GRPO catastrophically fails for multi-turn agents due to dual mechanism\\n- 所需证据：episode-level vs step-independent 对比（多 seed），h-sweep ablation（3 seeds each），mechanistic analysis（gradient signal measurement），GAE baseline comparison\\n- 当前证据状态：**ESTABLISHED** (exp029 step5 val=25% vs exp028c step10 val=0%)\\n- 机制：(1) policy information loss (h-step context insufficient), (2) advantage sign misattribution (gradient direction reflects episode outcome, not window-local action quality; additionally γ^k magnitude decay for early windows)\\n- 技术细节：GRPO 算法无固有 γ，但 RAGEN step_independent 的 `compute_step_discounted_returns()` 引入 γ-discounted per-window returns → advantage 符号由 episode 成败决定。代码验证：`agent_trainer.py:271-340` + `core_algos.py:194-246`\\n\\n### Claim 2 (strength: moderate): Action-change is an effective intrinsic reward for verification informativeness\\n- 所需证据：selective verification 训练收敛 + action-change vs random/confidence baselines\\n- 当前证据状态：**not yet established**，依赖 Phase B 实验\\n- 前提：episode-level 训练的 agent 需达到 ≥40% success 才有意义\\n\\n### Claim 3 (strength: moderate): Learned selective policy matches always-on performance at reduced verification cost\\n- 所需证据：B-IAVR verification ↓40%+ 且 success delta < 3pp vs always-on\\n- 当前证据状态：**not yet established**，依赖 Phase B + C\\n- 前提：Claim 1 的 agent 需足够强\\n\\n## Contingency Plan\\n\\n如果 episode-level 训练收敛后 success 仍 < 40%（不足以支撑 cost-efficiency story）：\\n- **Plan A**：paper 变为 diagnostic + analysis contribution — \\\"Why Step-Independent RL Fails for LLM Multi-Turn Agents: Dual Mechanism Analysis\\\" (需更深 ablation + GAE comparison + community practice survey)\\n- **Plan B**：加 Self-Guide reward 到 episode-level（从 binary→dense reward），推高 performance 后再做 selective verification\\n- 不考虑 downgrade venue\\n- **注意**：Dream review 已证明 Plan A 纯 methodology paper 需要比预期更深的分析才能通过审稿（\\\"诊断社区默认实践的隐性代价\\\" > \\\"episode-level RL works\\\"）\\n\\n## Reviewer Attack Surface + Defense\\n\\n| # | Concern | Severity | Defense |\\n|---|---------|----------|---------|\\n| 1 | \\\"Episode-level RL is obvious / well-known\\\" | HIGH | h-sweep (3 seeds) 展示 non-trivial cliff + 双机制理论 + \\\"为什么社区默认 step-independent\\\" 分析 |\\n| 2 | \\\"Theory 与 GRPO 不匹配\\\" | HIGH | 精确区分：GRPO 算法无 γ，但 step_independent 实现引入 γ-discounted returns（代码引用）→ per-window advantage logging 实证 + 伪代码 |\\n| 3 | \\\"缺 GAE/标准 RL baselines\\\" | HIGH | 加 GAE(λ=0.95) + GAE(λ=1,γ=1) baseline，证明 episode-level GRPO 与 GAE 的差异 |\\n| 4 | \\\"Self-Guide 3x performance gap\\\" | HIGH | 正面回应：不同 paradigm (expert-guided vs from-scratch RL)，不同问题（Self-Guide 回避了训练问题） |\\n| 5 | Single environment (ALFWorld) | MEDIUM | ScienceWorld transfer (if resources permit) |\\n| 6 | Small model (1.7B) | MEDIUM | 定位 resource-constrained; 7B 验证 (conditional) |\\n| 7 | Action-change = noise vs signal | MEDIUM | Entropy-controlled analysis + causal intervention (Phase B) |\\n| 8 | 与 ARES 差异化不足 | LOW | Head-to-head 对比 + 方法论差异表 |\\n| 9 | \\\"Turn-PPO 已解决相同问题\\\" | HIGH | 精确区分：Turn-PPO 发现 uniform advantage（症状），我们发现 sign misattribution（根因机制 + 量化 γ^24≈29%）；解法相反 (finer vs coarser) |\\n\\n## Evidence Status Matrix\\n\\n| Claim | MVP Evidence | Research Evidence Needed | Priority |\\n|-------|-------------|--------------------------|----------|\\n| Claim 1 | exp029 vs exp028c (25% vs 0%) | h-value ablation, multi-seed, mechanism paper figure | P0 |\\n| Claim 2 | N/A | Phase B full implementation | P1 |\\n| Claim 3 | N/A | Phase B + C comparison suite | P1 |\\n\\n## Competitive Positioning\\n\\n| System | Method | Benchmark | Key Difference from Us |\\n|--------|--------|-----------|----------------------|\\n| Self-Guide (2026) | Always-on verification | ALFWorld 72.7% (1.7B) | We add selectivity via RL |\\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token reduction | SFT vs RL, continuous vs binary |\\n| Thinkless (NeurIPS'25) | RL control token | reasoning domain | Same RL philosophy, different domain |\\n| ReflAct (EMNLP'25) | Prompting GPT-4 | ALFWorld 93.3% | Different scale/approach |\\n| RAGEN (2025) | GRPO for agents | varies | Step-independent default, our baseline |\\n| **Turn-PPO (2512.17008)** | Turn-level MDP + value fn | reasoning tasks | \\\"Uniform advantage\\\" vs our \\\"sign misattribution\\\"; finer credit vs coarser |\\n| **GAGPO (2605.13217)** | Grouped value proxy, step-aligned | ALFWorld 93.5% (1.5B) | Finer-grained credit for performance; we diagnose mechanism failure |\\n| **MT-GRPO (2505.11821)** | Turn-level reward design | QA search tasks | Turn-level credit; we show coarser suffices |\\n| **iStar (ICLR'26)** | Implicit PRM + dual advantage | WebShop 86.5% | Learns step rewards; we show episode-level eliminates misattribution |\\n| **ArCHer (ICML'24)** | Hierarchical multi-turn RL | multi-turn agents | Foundational framework; establishes need for hierarchical structure |\\n| **HiPER (2602.16165)** | Hierarchical Plan-Execute RL | ALFWorld 97.4% (7B) | SOTA performance pursuit; we do mechanism diagnosis |\\n\\n### Positioning Strategy\\n\\n**核心差异化：Contrarian Solution。** 竞品（Turn-PPO, GAGPO, MT-GRPO, iStar, HiPER）一致认为 multi-turn RL 需要更细粒度的 credit assignment（turn-level, step-level, hierarchical），并用此提升性能。我们的贡献是诊断性的：\\n\\n1. **问题定义更精确**：Turn-PPO 发现 \\\"uniform advantage\\\" 问题（所有 turn 获得相同 advantage），我们发现更本质的 \\\"Advantage Sign Misattribution\\\"（advantage 符号由 episode outcome 决定而非 local action quality），并量化 γ^24 ≈ 29% 的 return 衰减。Uniform advantage 是症状，sign misattribution 是根因机制。\\n\\n2. **Contrarian solution**：所有竞品的解法都是引入更细的 credit（turn-level value, step-level PRM, hierarchical planner）。我们展示更粗的 episode-level credit 反而消除 sign misattribution，因为它避免了将 episode reward 错误分配到独立优化的子窗口。这挑战了 \\\"越细越好\\\" 的社区默认假设。\\n\\n3. **不同 contribution 维度**：GAGPO/HiPER 追求 ALFWorld 93-97% 的 SOTA performance（通过更好的 credit + 更复杂的架构）。我们不 compete on performance axis，而是回答 \\\"为什么社区默认的 step-independent 灾难性失败\\\" 这个诊断问题。两个 contribution 维度正交互补。\\n\\n4. **与 CA Survey 的关系**：Zhang (2604.09459) 系统化了 47 种 CA 方法，但未分析 CA 方法本身的 failure modes（何时更细粒度反而有害）。我们填补这一空白。\\n\\n## Research Phases\\n\\n1. **Phase A (DONE)**: Episode-level GRPO training — MVP passed, demonstrates Claim 1\\n2. **Phase A+**: Continue training to convergence (target ≥40% success), deploy tatsu parallel patch, multi-seed\\n3. **Phase B**: Implement selective verification with action-change reward — Claim 2 & 3\\n4. **Phase C**: Ablation suite — context window sweep, reward ablations, baseline comparisons\\n5. **Phase D**: (Conditional on resources) Multi-env / multi-model scaling\\n\", \"total_chars\": 8625, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c71947b-3931-47e9-a671-6de1fd287d1f",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "7337c581-5bf0-4a80-af08-ff8e5b03da42",
  "sourceToolAssistantUUID": "0c71947b-3931-47e9-a671-6de1fd287d1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T14:17:02.959Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HRWue1tWEcdKoovFfxHqpy`</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7337c581-5bf0-4a80-af08-ff8e5b03da42",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HR56cHJAZTr9JTHZzS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9ec0d17-18a1-4228-98ff-b5b5af5d47d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011n8mjhPDWWw5m5HGd9uUMB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6469,
      "cache_read_input_tokens": 22825,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6469
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 22825,
          "cache_creation_input_tokens": 6469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6469,
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

_source line 14 · 2026-05-17T14:17:02.982Z_

<details><summary>↩ Tool result · `toolu_01HRWue1tWEcdKoovFfxHqpy`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9ec0d17-18a1-4228-98ff-b5b5af5d47d6",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "4172948c-d5e4-4620-a2e0-b2a2de81b509",
  "sourceToolAssistantUUID": "a9ec0d17-18a1-4228-98ff-b5b5af5d47d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T14:17:06.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LEjHN2esunrFTQUmrZ9C5T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4172948c-d5e4-4620-a2e0-b2a2de81b509",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HRJCeYcFqX8ynQFb7r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b8abff5-8cb0-4133-bad2-6b651b93d7de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hw4nc9p8QrtFyqQUueMucG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 29294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 253,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 16 · 2026-05-17T14:17:06.069Z_

<details><summary>↩ Tool result · `toolu_01LEjHN2esunrFTQUmrZ9C5T`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL Training for LLM Agents.}
5	Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. WebAgent-R1~\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechanism itself as a source of systematic sign misattribution, which is the structural failure we identify and formalize.
6	
7	\paragraph{Credit Assignment in Reinforcement Learning.}
8	The temporal credit assignment problem has a long history. REINFORCE~\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\cite{schulman2017ppo} reduces variance through a learned value function and clipped surrogate objectives. Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} interpolates between one-step bootstrap and Monte Carlo returns via the $\lambda$ parameter, offering a continuous spectrum from TD(0) to full-episode credit. The TD($\lambda$) family~\cite{sutton1988td} established this interpolation in the tabular setting. In the LLM agent context, process reward models provide step-level supervision: AgentPRM~\cite{choudhury2025agentprm,xi2025agentprm} estimates per-step value through Monte Carlo rollouts or TD-based estimation with GAE. SkillMaster~\cite{skillmaster2026} proposes DualAdv-GRPO, which separately estimates advantages for task-solving and skill-editing decisions. Episode-level GRPO, as we advocate, is equivalent to GAE(1,1) without a critic: it assigns uniform advantage across all steps, forgoing per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard adaptation of GRPO (step-independent windowing) produces catastrophic sign errors in multi-turn settings.
9	
10	\paragraph{Selective Verification and Adaptive Computation.}
11	A growing body of work trains models to allocate computation adaptively rather than uniformly. In the reasoning domain, Thinkless~\cite{du2025thinkless} introduces an RL-trained control token that decides whether to invoke extended thinking for each query. AutoThink~\cite{tu2025autothink} uses multi-stage RL to shape when reasoning-capable models activate their chain-of-thought. SelfBudgeter~\cite{selfbudgeter2026} frames adaptive computation as token budget allocation trained via budget-guided GRPO. In the agent domain, ARES~\cite{yang2026ares} trains an SFT-initialized router that selects reasoning effort levels per step, refined via GRPO with a combined outcome and token-efficiency reward. Agent-Omit~\cite{agent-omit2026} learns to omit redundant thoughts and observations through agentic RL, reducing context length without sacrificing performance. Sherlock~\cite{sherlock2025} performs selective verification at the workflow level through offline counterfactual analysis and speculative execution. Derailer-Rerailer~\cite{wan2025derailer-rerailer} detects instability triggers in reasoning chains and invokes targeted verification. These approaches operate at the reasoning-token level (Thinkless, AutoThink, SelfBudgeter), workflow-DAG level (Sherlock), or use heuristic triggers (Derailer-Rerailer) and SFT-initialized routers (ARES). Our selective verification differs in scope and mechanism: it makes a binary verify-or-skip decision at each agent interaction step, trained end-to-end via RL with an action-change informativeness signal that requires no external annotations or heuristic design.
12	
13	\paragraph{Self-Verification and Self-Correction.}
14	Self-verification has received significant attention as a mechanism for improving LLM reliability. Kamoi et al.~\cite{kamoi2024self-correction-survey} survey self-correction in LLMs and establish that pure intrinsic self-correction (without external feedback) is unreliable across most settings. Long et al.~\cite{long2026selfverification} quantify the verification dilemma empirically: over 90\% of self-verification instances are confirmatory, with only approximately 2\% producing corrective changes. CorrectBench~\cite{tie2025correctbench} further demonstrates that uniform self-correction exhibits diminishing returns, as models repeatedly ``correct'' already-correct answers. VerifiAgent~\cite{verifiagent2025} proposes a unified verification framework with meta-verification and tool-based adaptive strategies, focusing on improving verification quality through better methods. These findings collectively establish two facts: verification quality is limited by confirmatory bias, and uniform application of verification wastes computation on uninformative instances. Our work addresses a complementary question: given that most verification is confirmatory, \textit{when} should an agent verify? The 90\% confirmatory rate reported by Long et al. directly motivates learning a selective policy that triggers verification only at steps where action change is likely.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b8abff5-8cb0-4133-bad2-6b651b93d7de",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "6c253dee-4e99-48a0-9d01-8d7ef30cd6ac",
  "sourceToolAssistantUUID": "0b8abff5-8cb0-4133-bad2-6b651b93d7de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T14:17:06.547Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GxYmpy1ybDomExcSZqFHQG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c253dee-4e99-48a0-9d01-8d7ef30cd6ac",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HRJCeYcFqX8ynQFb7r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dd5db1a-feb0-443d-aad5-9154b12d538c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hw4nc9p8QrtFyqQUueMucG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 29294,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 253
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 29294,
          "cache_creation_input_tokens": 253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 253,
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

_source line 18 · 2026-05-17T14:17:06.553Z_

<details><summary>↩ Tool result · `toolu_01GxYmpy1ybDomExcSZqFHQG`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training Large Language Model (LLM) agents for multi-turn interactive tasks poses a fundamental challenge: policies must compose actions across 30 to 50 interaction steps in environments such as household navigation~\cite{kim2025reflact}, web interaction~\cite{digiRL2024}, and scientific experimentation. Supervised fine-tuning (SFT) can teach action formatting but fails to instill compositional planning, because expert demonstrations do not expose the trial-and-error exploration through which effective multi-step strategies emerge. Reinforcement learning (RL) addresses this gap by optimizing policies through direct environment interaction, and Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} has become a preferred method due to its critic-free design and direct compatibility with language model architectures. Recent work applies RL-based training to interactive agents across diverse domains, from text-based games~\cite{ragen2025} and GUI interaction~\cite{digiRL2024} to tool use~\cite{spear2025} and instruction following~\cite{selfguide2026,feng2025gigpo}. These efforts share a common implementation pattern that has received little scrutiny: the multi-turn trajectory is decomposed into fixed-size windows, and each window is optimized as an independent training sample. This decomposition is the focus of our analysis.
5	
6	Current agent RL frameworks default to \textit{step-independent training}: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, each receiving a discounted return derived from the binary episode outcome and optimized independently via GRPO~\cite{ragen2025,selfguide2026}. This choice is motivated by practical considerations: it fits long trajectories within limited context windows, multiplies the effective batch size, and aligns with the token-level training paradigm of language models. However, the decomposition introduces a fundamental credit assignment pathology. When each window receives a group-normalized advantage, the sign of that advantage reflects whether the \textit{episode} succeeded or failed, not whether the \textit{window's actions} were locally correct. In our experiments, this pathology produces a striking failure pattern: step-independent training collapses to 0\% task success within 10 training steps, while action validity remains above 90\% (Section~\ref{sec:experiments}). The agent learns to produce well-formatted commands that satisfy syntactic constraints but loses the ability to complete tasks entirely. This collapse is not an artifact of a particular hyperparameter configuration. We observe the same failure across multiple learning rates, KL penalty strengths, and window sizes, consistent with a structural defect in the training paradigm rather than a tuning problem.
7	
8	Standard remedies do not resolve this collapse. Dense reward shaping, which provides per-step bonuses for intermediate goals such as valid action formatting, creates a different failure mode: the agent maximizes format-level rewards while task completion stays at zero. In our dense reward experiment, action validity increases from 60\% to 97.5\% while task success remains at 0\% (Section~\ref{sec:experiments}). Increasing the number of rollouts or adjusting the KL penalty delays the onset of collapse but does not prevent it. Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} and Proximal Policy Optimization (PPO)~\cite{schulman2017ppo} offer finer-grained temporal credit assignment through learned value functions, but they add model complexity and have not been applied with a diagnosis of \textit{why} step-independent training fails in the first place. The root cause is not the choice of RL algorithm. It is the step-independent windowing itself, which corrupts the credit assignment signal at its source.
9	
10	We trace the collapse to two mechanisms that operate jointly under step-independent training. The first, \textbf{policy information loss}, arises because each $h$-step window has no access to actions and outcomes from other windows, so cross-step strategies that require conditioning on earlier results become invisible to the optimization process. The second, \textbf{advantage sign misattribution}, is more damaging: under binary episode reward, the sign of each window's advantage $\hat{A}_k$ is determined by whether the episode succeeded or failed (Section~\ref{sec:m2_sign_misattribution}), not by the local quality of the window's actions. Good actions in failed episodes receive negative advantages and are actively suppressed, while bad actions in successful episodes are reinforced. Our formal analysis (Section~\ref{sec:formal_probability}) shows that at a baseline success rate of $p = 6.25\%$ with group size $K = 8$, approximately 84.5\% of gradient updates for locally correct windows point in the wrong direction. Sign misattribution is a directional error, fundamentally distinct from magnitude attenuation: it drives the policy away from correct behaviors rather than merely reducing convergence speed. Episode-level GRPO eliminates both mechanisms by treating the complete trajectory as a single optimization sample, consistent with GRPO's original design~\cite{shao2024deepseekmath}, so that all steps share one advantage and cross-step dependencies are preserved through the full interaction history. In our experiments, episode-level training achieves 28.1\% validation success (from a 12.5\% baseline), while step-independent training collapses to 0\%.
11	
12	Our contributions are as follows:
13	\begin{itemize}
14	    \item \textbf{Dual mechanism diagnosis.} We identify and formalize two mechanisms that cause catastrophic collapse under step-independent GRPO in multi-turn agent training: policy information loss and advantage sign misattribution. We show that sign misattribution is a directional error, with the probability of incorrect gradient direction approaching $1 - p$ as group size grows (Sections~\ref{sec:dual_mechanism},~\ref{sec:sign_fundamental},~\ref{sec:formal_probability}).
15	
16	    \item \textbf{Systematic empirical validation.} Through window-size ablation ($h \in \{2, 5, 10, 20, \text{full}\}$) and per-window advantage logging, we demonstrate a credit assignment cliff and provide direct empirical evidence for the sign misattribution mechanism (Section~\ref{sec:experiments}).
17	
18	    \item \textbf{Episode-level solution and analysis.} We show that episode-level GRPO simultaneously resolves both failure mechanisms, and we analyze its connection to GAE~\cite{schulman2016gae} and REINFORCE~\cite{williams1992reinforce}. We identify six factors that explain why the community has defaulted to the broken step-independent paradigm (Sections~\ref{sec:episode_level},~\ref{sec:classical_connection},~\ref{sec:why_defaults}).
19	\end{itemize}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dd5db1a-feb0-443d-aad5-9154b12d538c",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "37723cc6-4550-4e77-b7d4-b60c96de98a9",
  "sourceToolAssistantUUID": "2dd5db1a-feb0-443d-aad5-9154b12d538c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T14:17:10.435Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CWe1zn58oVbTqr4BT9GisG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37723cc6-4550-4e77-b7d4-b60c96de98a9",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HRZasNNBke5unvQAzK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5f8131d-151f-4e75-ae16-20dcfd91c5f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLkUtTo88LfWBWdxpgpy4P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3389,
      "cache_read_input_tokens": 29547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3389,
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

_source line 20 · 2026-05-17T14:17:10.442Z_

<details><summary>↩ Tool result · `toolu_01CWe1zn58oVbTqr4BT9GisG`</summary>

```text
1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\ref{sec:m2_sign_misattribution}?
7	
8	\subsection{Experimental Setup}
9	\label{sec:experimental_setup}
10	
11	\paragraph{Environment.}
12	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib
13	ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.
14	
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.
16	
17	\paragraph{Base model.}
18	We use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves approximately 6.25\% success rate on a held-out 32-episode validation set, providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.0625$ with group size $K = 8$, Proposition 2 (Section~\ref{sec:formal_probability}) predicts that approximately 84.5\% of gradient updates carry incorrect sign under step-independent training.
19	
20	\paragraph{RL training configuration.}
21	We train using the RAGEN framework~\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:
22	\begin{itemize}
23	    \item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)
24	    \item Learning rate: $1 \times 10^{-6}$
25	    \item KL penalty coefficient: $\beta = 0.01$ (low-variance KL)
26	    \item Discount factor: $\gamma = 0.95$ (applied in step-independent return computation via Equation~\ref{eq:step_return}; not applicable to episode-level mode)
27	    \item Invalid action penalty coefficient: 0.1
28	    \item Training data: 16 task instances per training step
29	    \item Training steps: 15 (early-stopped based on convergence)
30	\end{itemize}
31	
32	\paragraph{Evaluation protocol.}
33	We evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \in \{2, 4, 8\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.
34	
35	\subsection{Window-Size Ablation}
36	\label{sec:window_ablation}
37	
38	To disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.
39	
40	\paragraph{Conditions.}
41	We vary the step-independent history length $h \in \{2, 5, 10, 20\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \texttt{step\_independent} training mode with \texttt{step\_independent\_history\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.
42	
43	\paragraph{Design rationale.}
44	The five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.
45	
46	\paragraph{Controls.}
47	All conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. \placeholder{plan\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}
48	
49	\paragraph{Post-hoc evaluation.}
50	To isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).
51	
52	\subsection{Results}
53	\label{sec:results}
54	
55	\subsubsection{Episode-Level vs. Step-Independent Training}
56	\label{sec:results_main}
57	
58	The central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\% validation success at training step 15, a 4.5$\times$ improvement over the SFT baseline of approximately 6.25\%. Step-independent training with $h = 2$ collapses to 0\% validation success by step 10.
59	
60	\placeholder{tab1\_main\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\%), Action Valid (\%), Pass@8. Multi-seed mean$\pm$std from plan\_003.}
61	
62	\placeholder{fig6\_training\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}
63	
64	The collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), task success drops from 18.75\% to single digits while action validity remains high at approximately 89.3\%. The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), action validity itself collapses from 89.3\% to 43.1\%. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.
65	
66	Episode-level training exhibits no such collapse. Action validity remains above 95\% throughout training, and success rate increases monotonically. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.
67	
68	\subsubsection{Window-Size Ablation}
69	\label{sec:results_hsweep}
70	
71	\placeholder{tab2\_h\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \in \{2, 5, 10, 20, \text{full}\}$, 3 seeds per $h$.}
72	
73	\placeholder{fig5\_h\_sweep\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (6.25\%).}
74	
75	The ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.
76	
77	The dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.
78	
79	From the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Action validity at step 2 is 89.3\%, dropping to 43.1\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.
80	
81	\subsubsection{Dense Reward Baseline}
82	\label{sec:results_dense}
83	
84	A natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.
85	
86	The dense reward experiment (exp013f) produces a striking dissociation. Action validity increases from 60\% to 97.5\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, task success remains at 0\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.
87	
88	This result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.
89	
90	\subsection{Empirical Verification of Sign Misattribution}
91	\label{sec:sign_verification}
92	
93	The theoretical analysis of Section~\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions.
94	
95	\paragraph{Methodology.}
96	During step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\text{sign}(\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\text{episode}}^{(i)} \in \{0, 1\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:
97	\begin{itemize}
98	    \item \textbf{Sign-outcome correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and $R_{\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.
99	    \item \textbf{Sign-quality correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.
100	    \item \textbf{Correct sign fraction}: $P(\text{correct sign} \mid \text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\ref{sec:formal_probability}) predicts this equals approximately 15.5\% at $p = 6.25\%$, $K = 8$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5f8131d-151f-4e75-ae16-20dcfd91c5f1",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "da7d0621-306a-49f1-880f-e4de5d42640d",
  "sourceToolAssistantUUID": "e5f8131d-151f-4e75-ae16-20dcfd91c5f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T14:17:10.919Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pxd7sz8XPUrfdLQW7yLZnf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da7d0621-306a-49f1-880f-e4de5d42640d",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HRZasNNBke5unvQAzK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e626b24-e6fc-437b-92fa-a831d90dd247",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLkUtTo88LfWBWdxpgpy4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3389,
      "cache_read_input_tokens": 29547,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3389
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 29547,
          "cache_creation_input_tokens": 3389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3389,
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

_source line 22 · 2026-05-17T14:17:10.924Z_

<details><summary>↩ Tool result · `toolu_01Pxd7sz8XPUrfdLQW7yLZnf`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Generality of Sign Misattribution}
5	\label{sec:discussion_generality}
6	
7	The sign misattribution mechanism identified in Section~\ref{sec:m2_sign_misattribution} is not specific to RAGEN, ALFWorld, or GRPO. The failure arises from three structural properties that co-occur in any multi-turn agent RL setup: (a) step-level credit assignment via windowing, (b) sparse binary episode reward, and (c) group-relative advantage normalization. When these three conditions hold, the advantage sign for each window collapses to a proxy for episode outcome regardless of local action quality (Equation~\ref{eq:sign_correlation}). The environment details, the specific RL algorithm, and the model architecture are irrelevant to this structural argument.
8	
9	Consider the broader landscape of LLM agent training. Web agents operating in WebArena~\cite{zhou2024webarena} execute 20 to 40 interaction steps per episode with binary task completion rewards. Scientific experimentation agents in ScienceWorld~\cite{wang2022scienceworld} follow multi-step experimental protocols where success is determined only at the final measurement. GUI agents in mobile and desktop environments issue sequences of clicks and keystrokes with success defined by whether the target UI state is reached. Tool-use agents chain API calls where only the final output is evaluated. All of these settings combine long trajectories with sparse terminal rewards, and any framework that decomposes these trajectories into independently optimized windows will exhibit sign misattribution.
10	
11	Proposition~2 (Section~\ref{sec:formal_probability}) reveals a further implication: the severity of misattribution scales with task difficulty. As the baseline success rate $p$ decreases, $P(\text{correct} \mid \text{update}) \to p$ in the large-$K$ limit. Environments with longer horizons or more complex reasoning requirements tend to have lower baseline success rates, so sign misattribution becomes \textit{more} severe precisely where credit assignment is most needed. A web agent with $p = 5\%$ baseline success would experience correct gradient direction in only 5\% of updates, a regime where training cannot converge regardless of other hyperparameter choices.
12	
13	\subsection{Direction Correctness vs.\ Credit Granularity}
14	\label{sec:discussion_tradeoff}
15	
16	Episode-level GRPO eliminates sign misattribution by treating the full trajectory as a single optimization sample. The cost of this choice is that all tokens in the episode receive the same advantage. A correct action at step 3 and a redundant action at step 40 are reinforced with identical magnitude and sign. This represents a trade-off between two desiderata: direction correctness (whether the gradient sign is aligned with local action quality) and credit granularity (whether the gradient magnitude reflects per-step contribution to success).
17	
18	At the low success rates typical of early training ($p = 12.5\%$ in our experiments), direction correctness dominates. When 80.9\% of gradient updates point in the wrong direction, the optimization actively destroys good behaviors. Uniform reinforcement of all steps in a successful episode is imprecise but at least preserves correct sub-strategies within the trajectory. The asymmetry is stark: coarse-but-correct gradients produce slow convergence, while fine-but-wrong gradients produce divergence.
19	
20	As the policy improves and $p$ increases, the marginal value of per-step credit assignment grows. At $p = 50\%$, Proposition~2 predicts $P(\text{correct} \mid \text{update}) \approx 50\%$, meaning step-independent training would produce a roughly unbiased gradient in expectation (though with high variance). In this regime, the coarseness of episode-level training may become a binding constraint on sample efficiency. Methods that combine episode-level direction correctness with finer-grained credit represent a natural extension. GAE with episode-level correction (using a value function for magnitude estimation while constraining signs to be consistent with episode outcome) and GiGPO's nested group structure~\cite{feng2025gigpo} are two concrete approaches. The connection to GAE(1,1) established in Section~\ref{sec:classical_connection} suggests a principled interpolation: begin with $\lambda = 1$ (episode-level) during early training when direction correctness matters most, and anneal toward $\lambda < 1$ as the policy stabilizes and per-step credit becomes valuable.
21	
22	\subsection{Relationship to Classical Credit Assignment}
23	\label{sec:discussion_classical}
24	
25	Sign misattribution is a specific manifestation of the temporal credit assignment problem, adapted to the LLM agent setting. In classical RL, temporal credit assignment is addressed through value functions (TD learning), eligibility traces (TD($\lambda$)), or return decomposition methods. The solutions all share a common structure: they provide mechanisms for information to propagate across time steps within an episode, so that the contribution of each step to eventual reward can be estimated.
26	
27	Step-independent windowing violates this structure in a way that is unusual even within the classical RL literature. TD(0) assigns credit through one-step bootstrapped returns, which is local but connected: the value of state $s_t$ depends on $s_{t+1}$, creating a chain that propagates information across the episode over multiple training iterations. Monte Carlo methods assign credit through full-episode returns, providing direct (if noisy) temporal coupling. Step-independent training creates \textit{disconnected} windows that share no temporal coupling, neither through bootstrapping nor through shared returns. Each window is optimized as if it were an independent bandit arm that happens to receive a reward correlated with the episode outcome. This falls below the TD(0)-to-MC spectrum entirely.
28	
29	The multi-agent analogy from Section~\ref{sec:classical_connection} clarifies the structural novelty. In cooperative multi-agent RL, the credit assignment challenge of shared team reward is well-recognized, and solutions such as counterfactual baselines (COMA~\cite{foerster2018coma}) or value decomposition (QMIX~\cite{rashid2018qmix}) exist. In multi-turn LLM agent training, the same structural problem arises from an implementation choice rather than from the problem formulation itself. The multi-agent credit assignment problem is inherent to team games; the sign misattribution problem in agent RL is artificial, introduced by the windowing design and removable by episode-level training.
30	
31	\subsection{Dual Mechanism Interaction}
32	\label{sec:discussion_interaction}
33	
34	Information loss (Mechanism 1) and sign misattribution (Mechanism 2) are not independent. They interact through the success rate $p$, creating a feedback loop that accelerates collapse at small window sizes. Mechanism 1 restricts the representable strategy space, imposing a ceiling on achievable task success for a given $h$. This ceiling determines the maximum $p$ that the policy can sustain. Mechanism 2 then drives performance below this ceiling at a rate that depends on $p$ itself: lower $p$ produces more severe misattribution (Proposition~2), which further reduces $p$, which further increases misattribution severity.
35	
36	This interaction creates a vicious cycle. At $h = 2$, the information-loss ceiling is low, so the policy cannot achieve high $p$ even with perfect optimization. The low $p$ triggers severe sign misattribution ($\approx$80.9\% wrong-direction gradients at $p = 12.5\%$), which erodes whatever competence the model retains within its truncated context. The erosion reduces $p$ further, intensifying the misattribution. The two-phase collapse observed empirically (strategic failure followed by formatting failure) reflects this cascade: Mechanism 2 first destroys task-level strategies (reducing $p$ to near zero), then continues to corrupt lower-level action representations that were initially robust.
37	
38	At larger $h$ values, the ceiling is higher, sustaining a higher $p$ that partially mitigates misattribution severity. This predicts a more gradual degradation rather than catastrophic collapse. The h-sweep ablation (Section~\ref{sec:results_hsweep}) tests this prediction by examining whether larger $h$ values exhibit slower collapse trajectories. Episode-level training breaks the cycle entirely by eliminating both mechanisms simultaneously: the full context removes the information-loss ceiling, and the single episode-level advantage removes the opportunity for sign misattribution.
39	
40	
41	\subsection{Limitations}
42	\label{sec:limitations}
43	
44	\paragraph{Single environment.} Our experiments are conducted exclusively on ALFWorld, a text-based household environment. The dual mechanism analysis depends only on the training algorithm structure (windowing, binary reward, group normalization) and not on environment-specific properties, so the theoretical argument is environment-agnostic. However, empirical validation on additional multi-turn environments such as ScienceWorld~\cite{wang2022scienceworld} or WebShop~\cite{yao2022webshop} would strengthen the generality claim. Different environments may exhibit different baseline success rates, trajectory lengths, and dependency structures that modulate the practical severity of sign misattribution.
45	
46	\paragraph{Single model scale.} All experiments use Qwen3-1.7B. The severity of sign misattribution depends on $p$ (Proposition~2), which varies with model capacity. A 7B or 14B model may achieve a higher SFT baseline, reducing the fraction of wrong-sign updates. The misattribution mechanism does not disappear at higher $p$ (it persists as long as $p < 1$), but its practical impact may be less catastrophic if the model starts closer to the ceiling. Scaling experiments are needed to characterize the relationship between model capacity, baseline success rate, and collapse dynamics.
47	
48	\paragraph{Coarse credit in episode-level training.} Episode-level GRPO assigns uniform advantage to all tokens in an episode. For very long episodes ($T > 100$) or tasks with many independent sub-goals, this coarseness may limit learning efficiency even though it preserves direction correctness. The trade-off between direction correctness and credit granularity (Section~\ref{sec:discussion_tradeoff}) becomes increasingly relevant at higher success rates where the sign error is less severe but the efficiency cost of uniform reinforcement grows.
49	
50	\paragraph{Selective verification not implemented.} The selective verification component (Section~\ref{sec:selective_verification}) remains a design proposal. We present the training methodology diagnosis and episode-level solution, but the downstream application of training a selective verification policy has not been implemented or evaluated. The contribution of this paper is the credit assignment analysis and fix, not the verification application.
51	
52	\paragraph{Limited gradient analysis scope.} The empirical sign misattribution verification (Section~\ref{sec:sign_verification}) uses $h = 2$, representing the most extreme case of windowed training. Analysis across multiple $h$ values ($h \in \{5, 10, 20\}$) would reveal how misattribution severity varies with window size in practice and whether the theoretical predictions (which are $h$-independent for a given $p$) hold when different window sizes produce different effective $p$ values during training.
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e626b24-e6fc-437b-92fa-a831d90dd247",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "0714b090-6f0f-4c9e-9710-2bb197b5a588",
  "sourceToolAssistantUUID": "4e626b24-e6fc-437b-92fa-a831d90dd247",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T14:17:15.972Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UonfWysVUqL88j5hLUc4RN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "offset": 100,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0714b090-6f0f-4c9e-9710-2bb197b5a588",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HRtCo5BzRBq9cJzYoZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bf65c3f-0c25-4c77-a155-851290dcc17d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWSqwEvgFn5XcF1ywyjLNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6693,
      "cache_read_input_tokens": 32936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6693,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 24 · 2026-05-17T14:17:15.986Z_

<details><summary>↩ Tool result · `toolu_01UonfWysVUqL88j5hLUc4RN`</summary>

```text
100	    \item \textbf{Correct sign fraction}: $P(\text{correct sign} \mid \text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\ref{sec:formal_probability}) predicts this equals approximately 15.5\% at $p = 6.25\%$, $K = 8$.
101	\end{itemize}
102	
103	\paragraph{Predictions.}
104	The sign misattribution mechanism makes three testable predictions:
105	\begin{enumerate}
106	    \item Sign-outcome correlation $\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)
107	    \item Sign-quality correlation $\approx 0$ (advantage sign is independent of whether local actions were good)
108	    \item $P(\text{correct sign}) \approx 15.5\%$ (derived from Proposition 2 at the observed success rate)
109	\end{enumerate}
110	If all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.
111	
112	\placeholder{tab3\_mechanism\_verification: Sign misattribution empirical verification. Columns: Metric, Measured Value, Theoretical Prediction, Agreement. Rows: sign-outcome correlation, sign-quality correlation, $P(\text{correct sign})$. Data from plan\_004 per-window advantage logging.}
113	
114	\subsection{Additional Baselines}
115	\label{sec:additional_baselines}
116	
117	\paragraph{GAE baselines.}
118	To distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} under two configurations. GAE($\lambda = 0.95$, $\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\lambda = 1$, $\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \placeholder{plan\_003b: GAE baseline execution. Columns: Method, Val Success (\%), Action Valid (\%), Training Stability (variance across steps).}
119	
120	\paragraph{Selective verification.}
121	Building on the episode-level trained agent (Section~\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \placeholder{tab4\_selective\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\%), Verify Rate (\%), Cost Reduction (\%). Pending Phase B experiments.}
122	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bf65c3f-0c25-4c77-a155-851290dcc17d",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "b613c05d-9611-443a-8705-ca46a59897f1",
  "sourceToolAssistantUUID": "4bf65c3f-0c25-4c77-a155-851290dcc17d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T14:17:16.435Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ACjEYmd8iE1kh1mNR8JArK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b613c05d-9611-443a-8705-ca46a59897f1",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HRtCo5BzRBq9cJzYoZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d0846ac-9b31-4a23-8cb7-7e28bdf10a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWSqwEvgFn5XcF1ywyjLNs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6693,
      "cache_read_input_tokens": 32936,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6693
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 32936,
          "cache_creation_input_tokens": 6693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6693,
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

_source line 26 · 2026-05-17T14:17:16.446Z_

<details><summary>↩ Tool result · `toolu_01ACjEYmd8iE1kh1mNR8JArK`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Multi-turn agent RL requires credit assignment across long interaction trajectories, yet current frameworks default to step-independent windowing that decomposes trajectories into independently optimized windows. This default introduces a structural credit assignment pathology that no hyperparameter tuning can resolve.
5	
6	We diagnose a dual mechanism underlying this failure: policy information loss at the inference layer, which imposes a constant performance ceiling, and advantage sign misattribution at the training layer, which causes cumulative degradation. Formal analysis shows that at a baseline success rate of $p = 12.5\%$ with group size $K = 8$, approximately 80.9\% of gradient updates for locally correct windows point in the wrong direction. Our window-size ablation reveals a credit assignment cliff: as $h$ decreases, performance does not degrade smoothly but collapses in two phases, with action validity dropping from 89.3\% to 43.1\%. Episode-level GRPO, which treats the full trajectory as a single optimization sample, eliminates both mechanisms and achieves 28.1\% validation success where step-independent training collapses to 0\%.
7	
8	The central insight is that sign errors are more destructive than magnitude imprecision. Gradients that point in the wrong direction cause active divergence, while gradients with imprecise magnitude merely slow convergence. This distinction applies to any agent RL method that combines step-level windowing, sparse binary reward, and group-relative advantage normalization.
9	
10	Several directions extend this work. First, selective verification trains the agent to learn when self-verification is warranted during execution. Second, cross-environment validation on WebShop and ScienceWorld would test whether empirical severity matches our theoretical predictions across different trajectory lengths and success rates. Third, scaling experiments with 7B and 14B models will reveal how sign misattribution interacts with model capacity. Finally, $\lambda$-annealing from episode-level ($\lambda = 1$) to finer-grained credit ($\lambda < 1$) offers a principled interpolation between direction correctness and credit granularity as the policy improves.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d0846ac-9b31-4a23-8cb7-7e28bdf10a53",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "bcf67e8f-dc05-4c86-bfb7-370e41425258",
  "sourceToolAssistantUUID": "7d0846ac-9b31-4a23-8cb7-7e28bdf10a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T14:17:19.460Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BAkNoKJ43tEoZdaNPTCD5L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/theoretical_analysis.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcf67e8f-dc05-4c86-bfb7-370e41425258",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HSHsq7RKcvHgtBa8W9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70989b54-9180-4476-a57b-361ffd173499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuDQtAwb8L8wqnGnV4zWyk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 39629,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 39629,
          "cache_creation_input_tokens": 1529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1529,
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

_source line 28 · 2026-05-17T14:17:19.465Z_

<details><summary>↩ Tool result · `toolu_01BAkNoKJ43tEoZdaNPTCD5L`</summary>

```text
1	\section{Theoretical Analysis}
2	\label{sec:theory}
3	
4	Section~\ref{sec:dual_mechanism} identified two failure mechanisms of step-independent training: policy information loss and advantage sign misattribution. We now formalize why sign misattribution is the more fundamental failure, derive the probability of incorrect gradient direction as a function of task success rate, examine why the community has defaulted to step-independent training, and connect our findings to the classical credit assignment literature.
5	
6	\subsection{Why Sign Misattribution is Fundamental}
7	\label{sec:sign_fundamental}
8	
9	The two mechanisms identified in Section~\ref{sec:dual_mechanism} produce qualitatively different optimization errors. Policy information loss (Mechanism 1) reduces the information available to each window's policy, producing suboptimal but directionally reasonable gradient updates. Sign misattribution (Mechanism 2) corrupts the gradient direction itself. We formalize this distinction below.
10	
11	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $k$'s advantage $\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
12	
13	\textit{Argument.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\hat{A}_k$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $k$ is $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\mu > 0$, and all windows in the failed episode receive negative advantages after normalization via Equation~\ref{eq:grpo_advantage}. This includes windows where the agent took locally correct actions, such as correctly identifying a target object in an exploration step. Now consider a window with good local actions. In a successful episode (probability $p$), the window receives positive $\hat{A}_k$, which is the correct sign. In a failed episode (probability $1 - p$), the window receives negative $\hat{A}_k$ whenever $\mu > 0$, which is the wrong sign. The probability that $\mu = 0$ (all $K$ rollouts in the group failed) is $(1-p)^K$, which shrinks exponentially with $K$. As $K$ grows, nearly every failed episode produces a non-zero group mean, and the window receives the wrong sign with probability approaching $1-p$. The probability of correct sign therefore approaches $p$. \qed
14	
15	The distinction between sign error and magnitude error clarifies why Mechanism 2 is catastrophic while Mechanism 1 is merely suboptimal. The discount factor $\gamma^{(N-k)}$ in Equation~\ref{eq:step_return} introduces magnitude decay across window positions: for an episode with $T=50$ steps and $h=2$, the first window ($k=1$) retains $\gamma^{N-1} = 0.95^{24} \approx 0.29$ of the terminal window's return. This attenuation reduces the gradient magnitude for early windows but preserves the gradient direction. A gradient with correct sign and reduced magnitude produces slow convergence, a condition recoverable through longer training. A gradient with wrong sign produces active divergence: the optimization pushes the policy away from good behaviors and toward bad ones. Consider a navigation analogy. Magnitude error corresponds to a compass that points correctly but displays a dimmed needle; the traveler moves slowly toward the destination. Sign error corresponds to a compass pointing in the opposite direction; the traveler walks away from the destination with full confidence. The first error is correctable by patience. The second is correctable only by replacing the compass.
16	
17	\subsection{Formal Probability Analysis}
18	\label{sec:formal_probability}
19	
20	We derive a tighter bound on the probability of correct gradient direction as a function of task difficulty and group size.
21	
22	\textbf{Proposition 2.} \textit{Let $p$ denote the episode success rate and $K$ the number of rollouts per group. Under step-independent training with binary episode reward, the probability that a gradient update for a window with locally good actions has the correct sign satisfies:}
23	\begin{equation}
24	P(\text{correct sign or no update}) = p + (1-p)^{K}
25	\label{eq:correct_bound}
26	\end{equation}
27	\textit{Among gradient updates that occur (non-zero advantage), the fraction with correct sign is:}
28	\begin{equation}
29	P(\text{correct} \mid \text{update}) = \frac{p}{1 - (1-p)^{K}}
30	\label{eq:correct_conditional}
31	\end{equation}
32	
33	\textit{Derivation.} For a window with locally good actions, the gradient direction depends on $\text{sign}(\hat{A}_k)$, which depends on whether the episode succeeded and whether the group contains any successful rollouts. Three mutually exclusive cases arise.
34	
35	\textit{Case 1: Episode succeeded} (probability $p$). The window receives $R_k = \gamma^{(N-k)} \cdot r_+ > 0$. With at least one failed rollout in the group, $R_k > \mu$ after normalization, producing $\hat{A}_k > 0$. The gradient reinforces the window's actions. For a window with good local actions, this is the correct direction.
36	
37	\textit{Case 2: Episode failed, group contains at least one success} (probability $(1-p)[1 - (1-p)^{K-1}]$). The window receives $R_k = 0 < \mu$, producing $\hat{A}_k < 0$. The gradient suppresses the window's actions. For a window with good local actions, this is the wrong direction.
38	
39	\textit{Case 3: Episode failed, entire group failed} (probability $(1-p) \cdot (1-p)^{K-1} = (1-p)^{K}$). All returns are zero, so $\mu = 0$ and $\sigma = 0$. The advantage is zero, producing no gradient update.
40	
41	Summing Cases~1 and~3 yields Equation~\ref{eq:correct_bound}. Since only Cases~1 and~2 produce non-zero gradients, the conditional probability follows as Equation~\ref{eq:correct_conditional}.
42	
43	We evaluate these expressions at the empirical baseline of our experiments. At $p = 6.25\%$ (the pre-training success rate) and $K = 4$: $(1-p)^K = 0.9375^4 \approx 0.77$, giving $P(\text{correct or no update}) \approx 0.83$. Of the 23\% of cases that produce a gradient update, only $P(\text{correct} \mid \text{update}) = 0.0625 / 0.23 \approx 27\%$ have the correct sign. As $K$ increases to 16, $(1-p)^{K} \approx 0.36$, and $P(\text{correct} \mid \text{update}) \approx 9.8\%$. In the large-$K$ limit, $P(\text{correct} \mid \text{update}) \to p$, so approximately $1 - p \approx 94\%$ of all gradient updates for locally good windows point in the wrong direction. This is consistent with the empirical observation that step-independent training collapses to 0\% task success (exp026, exp028c) while episode-level training achieves stable improvement (exp029, 28.125\% validation success at step 15).
44	
45	\subsection{Why the Community Defaults to Step-Independent Training}
46	\label{sec:why_defaults}
47	
48	If step-independent training is fundamentally flawed for multi-turn agents, why has it become the default? We identify six contributing factors.
49	
50	\textbf{1. Context window constraints.} Smaller language models (1B to 4B parameters) typically support context windows of 2048 to 4096 tokens. Multi-turn episodes spanning 50 or more interaction steps easily exceed these limits. Step-independent windowing is a pragmatic response to a hardware constraint, not a deliberate algorithmic choice.
51	
52	\textbf{2. Token-level training inertia.} Language model training is organized around predicting the next token over fixed-length sequences. When multi-turn RL inherits this paradigm, the natural unit of optimization becomes a fixed-length window rather than a variable-length episode. The mismatch between token-level optimization and episode-level credit assignment goes unquestioned because it aligns with existing training infrastructure.
53	
54	\textbf{3. Framework design accident.} The RAGEN framework~\cite{ragen2025} implements step-independent mode as its default configuration, not as one option among alternatives. Users inherit this choice without an explicit decision point, and default configurations propagate silently through downstream projects.
55	
56	\textbf{4. Memory and compute constraints.} Episode-level training requires processing $O(T)$ tokens per sequence, incurring $O(T^2)$ attention cost with full self-attention. Step-independent training reduces this to $O(h)$ tokens and $O(h^2)$ attention cost per window. The computational savings are immediate and measurable, while the credit assignment failure is subtle and deferred until training collapse occurs.
57	
58	\textbf{5. Reward shaping as apparent fix.} Dense reward shaping (per-step bonuses for intermediate goals) appears to address sparse reward problems and has theoretical support in the single-agent RL literature. Our experiment with dense rewards under step-independent training (exp013f) reveals a different failure mode: the agent learns to maximize format-level rewards (action validity rises from 60\% to 97.5\%) while task success remains at 0\%. Reward shaping does not resolve sign misattribution; it creates new optimization targets that the agent can game without solving the underlying task.
59	
60	\textbf{6. Absence of negative results.} When step-independent training fails, practitioners attribute the failure to insufficient hyperparameter tuning or the inherent difficulty of sparse rewards. Without published analyses that isolate the credit assignment mechanism as the root cause, the community cannot distinguish between ``this problem is hard'' and ``this training paradigm is broken for this class of problems.''
61	
62	\subsection{Connection to Classical Credit Assignment}
63	\label{sec:classical_connection}
64	
65	Our findings connect to a long line of work on temporal credit assignment in reinforcement learning. We position the step-independent failure mode within this literature and clarify the contribution of our analysis.
66	
67	\textbf{Temporal difference learning and eligibility traces.} Sutton's TD($\lambda$)~\cite{sutton1988td} provides a spectrum of credit assignment strategies parameterized by $\lambda \in [0,1]$. At $\lambda = 0$, credit is assigned via one-step bootstrapped returns. At $\lambda = 1$, TD($\lambda$) reduces to Monte Carlo returns, where each state receives the full episode return. Step-independent training falls below this spectrum: windows are disconnected from each other, so temporal propagation of credit does not occur. Each window receives an independently computed advantage with no mechanism for information to flow across windows within the same episode.
68	
69	\textbf{Generalized Advantage Estimation.} GAE($\lambda, \gamma$)~\cite{schulman2016gae} extends TD($\lambda$) with a separate discount factor for the advantage estimator. GAE(0, $\gamma$) produces per-step advantages through a learned value function. GAE(1, 1) produces undiscounted Monte Carlo returns, and is equivalent to episode-level GRPO without a critic. The key difference is that GAE uses value function subtraction as the baseline for variance reduction, while GRPO uses group normalization. Episode-level GRPO can be viewed as GAE(1, 1) with a group-relative baseline replacing the learned value function. This substitution is effective when the group provides a representative reference distribution, but it does not address per-step credit assignment within an episode.
70	
71	\textbf{REINFORCE.} Williams' REINFORCE algorithm~\cite{williams1992reinforce} computes policy gradients from complete episode returns with a learned baseline $b(s)$. Episode-level GRPO is equivalent to REINFORCE where the group mean $\mu$ replaces $b(s)$ and the group standard deviation $\sigma$ provides normalization. The algorithmic structure is not new. Our contribution is the diagnosis: the community's standard adaptation of this algorithm for multi-turn LLM agents (step-independent windowing) silently breaks the credit assignment structure that REINFORCE assumes.
72	
73	\textbf{Multi-agent credit assignment analogy.} Step-independent windows can be understood through cooperative multi-agent games. Each window acts as an independent ``agent'' sharing a team reward (the episode outcome) but optimized without knowledge of other windows' actions. The sign misattribution problem parallels team reward credit assignment in cooperative multi-agent RL: when the team fails, all agents receive identical penalties regardless of individual contribution. In multi-agent RL, this is a recognized problem with known solutions such as counterfactual baselines. In multi-turn LLM agent training, the same structural problem arises from an implementation choice and has not been recognized as a credit assignment failure.
74	
75	To summarize our positioning: we do not propose a new credit assignment algorithm. Episode-level training is the standard approach, and GRPO was designed as an episode-level method. What we identify is that the community's adaptation of GRPO to multi-turn settings introduces a systematic sign error in gradient computation. This error is not a gradual performance degradation but a catastrophic failure mode, as confirmed by the contrast between step-independent collapse (exp026, exp028c: 0\% success) and episode-level stability (exp029: 28.125\% validation success from a 12.5\% baseline).
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70989b54-9180-4476-a57b-361ffd173499",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "a8236756-1e5b-4ff6-b64f-4e78a0f65791",
  "sourceToolAssistantUUID": "70989b54-9180-4476-a57b-361ffd173499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-17T14:17:23.618Z_

Now I have a comprehensive view of the paper. Let me also check what the paper summary mentions about cross-environment and scaling results, and the experiments file for more details on actual results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8236756-1e5b-4ff6-b64f-4e78a0f65791",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HSWnUNyCneyPXSCdJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6d9a1e2-9aa4-42e8-8dd1-c7f6f6fb1ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NkT55Pcu4FkF8HWdRBiWR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3655,
      "cache_read_input_tokens": 41158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3655,
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

_source line 30 · 2026-05-17T14:17:24.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DMRAVxYd5ppF3L2E6dWKT5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments_aa43d8.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6d9a1e2-9aa4-42e8-8dd1-c7f6f6fb1ae0",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HSWnUNyCneyPXSCdJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "303cde13-cd75-4023-8202-673035c5ab3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NkT55Pcu4FkF8HWdRBiWR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3655,
      "cache_read_input_tokens": 41158,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 41158,
          "cache_creation_input_tokens": 3655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3655,
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

_source line 31 · 2026-05-17T14:17:24.518Z_

<details><summary>↩ Tool result · `toolu_01DMRAVxYd5ppF3L2E6dWKT5`</summary>

```text
1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\ref{sec:m2_sign_misattribution}?
7	
8	\subsection{Experimental Setup}
9	\label{sec:experimental_setup}
10	
11	\paragraph{Environment.}
12	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib
13	ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.
14	
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.
16	
17	\paragraph{Base model.}
18	We use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves approximately 6.25\% success rate on a held-out 32-episode validation set, providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.0625$ with group size $K = 8$, Proposition 2 (Section~\ref{sec:formal_probability}) predicts that approximately 84.5\% of gradient updates carry incorrect sign under step-independent training.
19	
20	\paragraph{RL training configuration.}
21	We train using the RAGEN framework~\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:
22	\begin{itemize}
23	    \item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)
24	    \item Learning rate: $1 \times 10^{-6}$
25	    \item KL penalty coefficient: $\beta = 0.01$ (low-variance KL)
26	    \item Discount factor: $\gamma = 0.95$ (applied in step-independent return computation via Equation~\ref{eq:step_return}; not applicable to episode-level mode)
27	    \item Invalid action penalty coefficient: 0.1
28	    \item Training data: 16 task instances per training step
29	    \item Training steps: 15 (early-stopped based on convergence)
30	\end{itemize}
31	
32	\paragraph{Evaluation protocol.}
33	We evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \in \{2, 4, 8\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.
34	
35	\subsection{Window-Size Ablation}
36	\label{sec:window_ablation}
37	
38	To disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.
39	
40	\paragraph{Conditions.}
41	We vary the step-independent history length $h \in \{2, 5, 10, 20\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \texttt{step\_independent} training mode with \texttt{step\_independent\_history\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.
42	
43	\paragraph{Design rationale.}
44	The five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.
45	
46	\paragraph{Controls.}
47	All conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. \placeholder{plan\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}
48	
49	\paragraph{Post-hoc evaluation.}
50	To isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).
51	
52	\subsection{Results}
53	\label{sec:results}
54	
55	\subsubsection{Episode-Level vs. Step-Independent Training}
56	\label{sec:results_main}
57	
58	The central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\% validation success at training step 15, a 4.5$\times$ improvement over the SFT baseline of approximately 6.25\%. Step-independent training with $h = 2$ collapses to 0\% validation success by step 10.
59	
60	\placeholder{tab1\_main\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\%), Action Valid (\%), Pass@8. Multi-seed mean$\pm$std from plan\_003.}
61	
62	\placeholder{fig6\_training\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}
63	
64	The collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), task success drops from 18.75\% to single digits while action validity remains high at approximately 89.3\%. The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), action validity itself collapses from 89.3\% to 43.1\%. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.
65	
66	Episode-level training exhibits no such collapse. Action validity remains above 95\% throughout training, and success rate increases monotonically. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.
67	
68	\subsubsection{Window-Size Ablation}
69	\label{sec:results_hsweep}
70	
71	\placeholder{tab2\_h\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \in \{2, 5, 10, 20, \text{full}\}$, 3 seeds per $h$.}
72	
73	\placeholder{fig5\_h\_sweep\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (6.25\%).}
74	
75	The ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.
76	
77	The dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.
78	
79	From the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Action validity at step 2 is 89.3\%, dropping to 43.1\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.
80	
81	\subsubsection{Dense Reward Baseline}
82	\label{sec:results_dense}
83	
84	A natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.
85	
86	The dense reward experiment (exp013f) produces a striking dissociation. Action validity increases from 60\% to 97.5\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, task success remains at 0\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.
87	
88	This result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.
89	
90	\subsection{Empirical Verification of Sign Misattribution}
91	\label{sec:sign_verification}
92	
93	The theoretical analysis of Section~\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions.
94	
95	\paragraph{Methodology.}
96	During step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\text{sign}(\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\text{episode}}^{(i)} \in \{0, 1\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:
97	\begin{itemize}
98	    \item \textbf{Sign-outcome correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and $R_{\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.
99	    \item \textbf{Sign-quality correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.
100	    \item \textbf{Correct sign fraction}: $P(\text{correct sign} \mid \text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\ref{sec:formal_probability}) predicts this equals approximately 15.5\% at $p = 6.25\%$, $K = 8$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "303cde13-cd75-4023-8202-673035c5ab3c",
  "isSidechain": true,
  "promptId": "9ad9ec7f-893a-40c1-b4fa-3b5dfb894488",
  "agentId": "ae34cf52ed66373af",
  "type": "user",
  "uuid": "31ed8385-fc1c-4e11-8f40-c2947cef7082",
  "sourceToolAssistantUUID": "303cde13-cd75-4023-8202-673035c5ab3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-17T14:18:36.256Z_

Now I have sufficient information to write a thorough review. Let me synthesize my findings.

## R2 Review: Novelty & Related Work

### Summary
This paper diagnoses why step-independent windowed GRPO collapses in multi-turn agent RL, attributing failure to "advantage sign misattribution" and "policy information loss." It proposes episode-level GRPO as the fix (achieving 28.1% on ALFWorld vs. 0% for step-independent). The paper is framed as a diagnostic contribution with a "dual mechanism" taxonomy, but the core finding amounts to confirming that full-episode credit assignment outperforms artificially truncated credit assignment, a conclusion that the community has already operationalized through finer-grained methods (GAE, Turn-PPO, GiGPO, GAGPO) achieving 86-97% on the same benchmark.

### Strengths

- **Rigorous formalization of a specific failure mode.** Proposition 1 and 2 provide clean probabilistic statements about wrong-sign gradient fraction as a function of success rate and group size. The derivation is correct and the quantitative predictions are testable.

- **Useful community service observation.** Pointing out that RAGEN's default step-independent mode is a "framework design accident" that silently propagates a broken training paradigm has practical value. The six reasons for community adoption (Section 3.5/theory) are well-articulated.

- **Dense reward baseline is informative.** The experiment showing action validity rises to 97.5% while task success stays at 0% under dense reward shaping is a clean negative result that rules out a natural alternative hypothesis.

- **Clear writing with good structure.** The paper is well-organized, the theoretical analysis flows logically, and the two-phase collapse narrative (strategic failure then formatting failure) is compelling.

- **Honest limitations section.** The paper explicitly acknowledges single environment, single scale, and that selective verification is unimplemented.

### Weaknesses

- **The core finding confirms community consensus, not a novel insight.** The entire multi-turn agent RL community (Turn-PPO, GiGPO, GAGPO, iStar, HiPER, ArCher) already pursues finer-grained or episode-level credit because practitioners know step-independent windowing is problematic. The paper's "contrarian" framing (episode-level is coarser yet works) is misleading: episode-level GRPO is simply REINFORCE/GRPO as originally designed. The "broken" approach is the non-standard adaptation. This is diagnosing a bug in one framework's implementation, not discovering a new phenomenon.

- **Novelty relative to Turn-PPO is insufficiently differentiated.** Turn-PPO (cited in the paper) already identifies "uniform advantage" as the pathology of naive multi-turn GRPO. The paper claims their "sign misattribution" is deeper (root cause vs. symptom), but this distinction is subtle. Both papers identify the same structural problem: episode outcome dominates per-step credit signals. The proposed terminology ("sign misattribution") reframes the same issue rather than revealing something new.

- **Critical placeholders throughout the experiments section.** Tables 1, 2, 3, and Figures 5, 6 are all \placeholder{} entries. The h-sweep is described as "expected pattern; precise numbers await multi-seed completion." The sign misattribution verification section has no actual measured values. A paper whose central empirical contribution is "systematic empirical validation" cannot have placeholder results.

- **The paper's best result (28.1%) is catastrophically below SOTA.** HiPER achieves 97.4% (7B), GAGPO 93.5% (1.5B), PA-MoE 93.8% (1.5B), and Self-Guide 72.7% (1.7B) on the same environment at the same or smaller model scale. The 28.1% result demonstrates the proposed fix barely works, which undermines the practical significance of the diagnosis. If episode-level GRPO is the "correct" solution, why does it achieve only 28.1% when competitors at the same scale reach 72-94%?

- **Selective verification (the original motivation) is entirely absent.** The paper title references "Credit Assignment Granularity" and the paper_framing document reveals the original B-IAVR project was about selective verification. The selective verification section is explicitly described as "a design proposal" that "has not been implemented or evaluated." This makes the paper feel like Phase A of a larger project published prematurely.

- **Single-seed results presented as established findings.** The main comparison (episode-level 28.1% vs. step-independent 0%) is single-seed. The h-sweep is single-seed for h=2. For a paper whose core contribution is empirical diagnosis, this is insufficient. The paper acknowledges this but proceeds to draw strong conclusions anyway.

- **The "dual mechanism" decomposition is not rigorously validated.** The post-hoc evaluation protocol (train with h=2, evaluate with full context) to separate Mechanism 1 from Mechanism 2 is proposed but results are not reported. Without this decomposition, the claim that "sign misattribution is more fundamental than information loss" is theoretical assertion, not empirical fact.

- **Missing key related work and positioning gaps.** The paper does not cite or discuss:
  - PA-MoE (2026), which achieves 93.8% on ALFWorld at 1.5B, directly relevant as it shows the "step-independent + better credit" path works fine
  - HCAPO's hindsight credit assignment, which addresses precisely the same problem (step-level credit in long-horizon tasks) but achieves +13.8% on ALFWorld
  - The paper positions against "the community default" but this default is from a single framework (RAGEN). Other frameworks (e.g., those using PPO/GAE natively) never had this problem.

- **Circular framing.** The paper starts with "step-independent is the community default" then diagnoses why it fails. But is it actually the community default? RAGEN uses it. Other systems (ArCher, HiPER, GAGPO, GiGPO) do not. The paper inflates the importance of diagnosing RAGEN's specific implementation choice by presenting it as a community-wide problem.

### Questions for Authors

1. If episode-level GRPO is the correct approach (as argued), why does it achieve only 28.1% while Self-Guide at the same model scale achieves 72.7% and GAGPO at 1.5B achieves 93.5%? What additional mechanisms do those methods provide that episode-level GRPO lacks?

2. Beyond RAGEN, which other multi-turn agent RL frameworks actually use step-independent windowing as their default? The paper claims this is a "community default" but only provides evidence from one framework.

3. The sign misattribution mechanism depends on binary episode reward. Would the analysis change substantively with any form of intermediate reward signal (e.g., partial progress rewards, curriculum-based shaping)? If the failure is specific to binary reward + windowing, how broadly does it apply in practice?

4. Given that Turn-PPO already identified the "uniform advantage" problem in the same setting, what is the concrete additional insight from your "sign misattribution" framing beyond renaming the phenomenon and providing Propositions 1-2?

5. The paper has numerous \placeholder{} entries. What is the status of the multi-seed experiments, GAE baselines, and sign misattribution empirical verification that are claimed as contributions?

6. Why is the evaluation set only 32 episodes? With binary outcomes and stochastic policies, confidence intervals at n=32 are extremely wide (a 28.1% success rate has a 95% CI of roughly [14%, 46%] by binomial proportion).

### Assessment of Contribution Significance

The paper's intellectual contribution reduces to: (1) formalizing why a specific implementation choice in RAGEN breaks credit assignment, and (2) showing that removing this choice (using episode-level training) partially fixes the problem. The formalization (Propositions 1-2) is clean but mathematically straightforward: it amounts to showing that under binary reward, group-normalized advantages for windowed sub-episodes carry the sign of the episode outcome. This is arguably obvious from the definition of group-relative normalization.

For a top venue (25% acceptance rate), the contribution bar requires either novelty of insight, strength of empirical results, or significant practical impact. This paper's insight confirms what practitioners already know (full-episode credit is better than arbitrarily truncated credit). Its empirical results are incomplete (placeholders throughout) and far below SOTA (28% vs 72-97%). Its practical impact is limited to users of one specific framework (RAGEN) who happen to use the default configuration without understanding its implications.

The "taxonomy of failure modes" framing attempts to elevate the contribution beyond "episode-level beats step-independent," but the taxonomy has only two entries (information loss and sign misattribution), and their interaction/decomposition is not empirically validated. A taxonomy paper typically requires breadth (many methods, many environments, many failure modes) or depth (definitive mechanistic understanding with causal interventions). This paper has neither at present.

### Minor Issues

- The paper discusses GRPO as "episode-level by design" then diagnoses the "step-independent adaptation" as broken. This framing makes the contribution feel like a bug report for RAGEN rather than a scientific discovery.
- The evaluation protocol uses only 32 episodes, providing extremely noisy estimates. Standard ALFWorld evaluation uses 134 held-out tasks.
- The SFT baseline of 6.25% (2/32 episodes) is extremely low. At this level, the model barely functions, making it unclear whether observed failures are about credit assignment or simply about having an inadequate starting policy.
- Several experiments referenced in the text (exp013f, exp026, exp028c, exp029) use internal experiment IDs without providing accessible results.
- The discount factor gamma=0.95 in step-independent mode is presented as a code-level detail of RAGEN, yet the theoretical analysis heavily relies on it. This makes the contribution very implementation-specific.
- The "six reasons why community defaults to step-independent" section reads more like an opinion piece than scientific analysis.

### Preliminary Score: 3/6
### Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ed8385-fc1c-4e11-8f40-c2947cef7082",
  "isSidechain": true,
  "agentId": "ae34cf52ed66373af",
  "requestId": "req_011Cb8HStH3PfpmsvF1Pwfa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df9bbaa3-e1b0-4994-92d2-9f6a8d6b15b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "cbfaf1eb-86b3-4c62-a538-5d4d55066586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mdn5tyZbSdoTumFD1U2knc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3828,
      "cache_read_input_tokens": 44813,
      "output_tokens": 2407,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2407,
          "cache_read_input_tokens": 44813,
          "cache_creation_input_tokens": 3828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3828,
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
