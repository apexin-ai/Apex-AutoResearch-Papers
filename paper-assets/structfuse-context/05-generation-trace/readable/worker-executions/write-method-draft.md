# write method draft

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 108
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_write_method-draft_20260514T224613.log`
- **Structured JSON:** [`7b3d89e741a0c402877f.json`](../../sessions/7b/7b3d89e741a0c402877f.json)

## Before a recorded user message

17 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "b969bf2a-2b90-4ee7-97eb-abc1c8fe8731",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

I'll read the three input files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "3e154198-d5f2-4007-a77b-49443f82a8bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmNVcFB75p2BvYhCc8f8tP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12080
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Runtime record

_source line 4_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778807400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1bf1c156-7576-455c-830c-fa8084fdec11",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01S8RsZ3cKN2TVz9oeYf32Hv`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "da77da52-8328-407e-b4cd-121e52b0a4c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmNVcFB75p2BvYhCc8f8tP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12080,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12080
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T22:46:25.283Z_

<details><summary>↩ Tool result · `toolu_01S8RsZ3cKN2TVz9oeYf32Hv`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "96224bd7-ec5a-4e27-81c8-c8c68ce11364",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read all three input files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "4a892761-c36c-42e6-b66a-b9dd5194f27c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtP4EADj5REb5m2YVKQ7io",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 23527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1322
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014BS7LJnSraYdTkXPzqVNdo`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "b746ef21-1ce6-4bdc-a7bf-4b7859363672",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtP4EADj5REb5m2YVKQ7io",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 23527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1322
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T22:46:29.138Z_

<details><summary>↩ Tool result · `toolu_014BS7LJnSraYdTkXPzqVNdo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"challenging gradient-based assumption\\\" narrative needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 12022, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "c14509dc-4817-40f9-889f-24bec4008f99",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — StructFuse\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3)\\\\n\\\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\\\\\"slow and ineffective\\\\\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\\\n\\\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\\\n\\\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\\\n\\\\n- **Existing approaches & gaps**:\\\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\\\n\\\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\\\n\\\\n- **Headline result template**: \\\\\\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\\\n\\\\n## Dual-Pillar Motivation\\\\n\\\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\\\n\\\\n## Formal Definition\\\\n\\\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\\\n\\\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\\\n\\\\n## Title Options\\\\n\\\\n- Primary: \\\\\\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\\\\\"\\\\n- Alternative: \\\\\\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\\\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\\\n- Backup: \\\\\\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n\\\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\\\\\"Do Language Models...\\\\\\\" papers). Contribution is understanding, not just a new method.\\\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\\\n3. **Against \\\\\\\"incremental\\\\\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response | Evidence |\\\\n|---------|----------|----------|\\\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\\\n| \\\\\\\"Complementary signal\\\\\\\" overstatement | Temper: \\\\\\\"conditionally beneficial\\\\\\\" not \\\\\\\"always complementary\\\\\\\" | Writing discipline |\\\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\\\n\\\\n## Evidence Status\\\\n\\\\n### Confirmed findings (basis for claims):\\\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\\\n\\\\n### In progress:\\\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\\\n\\\\n### Planned (priority order):\\\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\\\n- plan_014: Temperature ablation (Dream reviewer concern)\\\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\\\n- plan_015: Dynamic mining baseline\\\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\\\n- plan_007/008/009: Additional ablations\\\\n\\\\n## Contingency (if full M2 results weaken claims)\\\\n\\\\n### All 18 runs confirm pilot pattern: Best case\\\\n- Full statistical power, paper as framed above\\\\n- Target: EMNLP Main\\\\n\\\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\\\n- Drop Claim 2 to analysis observation\\\\n- Paper becomes: \\\\\\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\\\\\"\\\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\\\n\\\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\\\\\"challenging gradient-based assumption\\\\\\\" narrative needs adjustment\\\\n- Pivot: \\\\\\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\\\\\"\\\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\\\n- Claim 1 core preserved: \\\\\\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\\\\\"\\\\n- Impact: BM25 result determines narrative nuance, not core contribution\\\\n\\\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\\\n- If confirmed: negative result paper — \\\\\\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\\\\\"\\\\n- Discuss with user before committing direction\\\\n\\\\n## Deprecated Claims (with reason)\\\\n\\\\n- ~~\\\\\\\"Embedding-distance hard negatives actively harm code retrieval\\\\\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\\\n\\\", \\\"total_chars\\\": 12022, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"challenging gradient-based assumption\\\" narrative needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 12022, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UJXa5uz4N3tbMRjdh78pBv`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a46b475a-7780-4a5f-a225-690e1962ceb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtP4EADj5REb5m2YVKQ7io",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 23527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1322
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T22:46:30.082Z_

<details><summary>↩ Tool result · `toolu_01UJXa5uz4N3tbMRjdh78pBv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15999, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "d9b8779e-f864-4788-bd2d-6868c4817922",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\\\", \\\"content\\\": \\\"# StructFuse — Related Work Literature Map\\\\n# 最后更新: 2026-05-14\\\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\\\n# 总计: 39 entries (含 2 个软件工具引用)\\\\n\\\\ncategories:\\\\n\\\\n  # ==========================================================================\\\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\\\n  # ==========================================================================\\\\n  code_retrieval_bug_fixing:\\\\n    description: \\\\\\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\\\\\"\\\\n        authors: \\\\\\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"AutoCodeRover: Autonomous Program Improvement\\\\\\\"\\\\n        authors: \\\\\\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\\\\\"\\\\n        venue: ISSTA\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-smith: Scaling Data for Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\\\\\"\\\\n        venue: \\\\\\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\\\\\"\\\\n        year: 2025\\\\n        relation: building-block\\\\n        summary: \\\\\\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\\\\\"\\\\n        authors: \\\\\\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SweRank: Software Issue Localization with Code Ranking\\\\\\\"\\\\n        authors: \\\\\\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\\\\\"\\\\n        authors: \\\\\\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Findings)\\\\\\\"\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\\\n  # ==========================================================================\\\\n  hard_negative_mining:\\\\n    description: \\\\\\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Dense Passage Retrieval for Open-Domain Question Answering\\\\\\\"\\\\n        authors: \\\\\\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"A Simple Framework for Contrastive Learning of Visual Representations\\\\\\\"\\\\n        authors: \\\\\\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\\\\\"\\\\n        authors: \\\\\\\"Nils Reimers, Iryna Gurevych\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Curriculum Learning for Dense Retrieval Distillation\\\\\\\"\\\\n        authors: \\\\\\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\\\\\"\\\\n        venue: \\\\\\\"SIGIR (Best Short Paper)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\\\\\"\\\\n        venue: \\\\\\\"ACM TOSEM\\\\\\\"\\\\n        year: 2025\\\\n        relation: contrast-target\\\\n        summary: \\\\\\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\\\\\"\\\\n        note: \\\\\\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 3: Contrastive Learning for Code\\\\n  # ==========================================================================\\\\n  contrastive_code_learning:\\\\n    description: \\\\\\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Contrastive Code Representation Learning\\\\\\\"\\\\n        authors: \\\\\\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\\\\\"\\\\n        authors: \\\\\\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Long Papers)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 4: Program Analysis for ML\\\\n  # ==========================================================================\\\\n  program_analysis_for_ml:\\\\n    description: \\\\\\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeQL: Semantic Code Analysis Engine\\\\\\\"\\\\n        authors: \\\\\\\"GitHub / Semmle\\\\\\\"\\\\n        venue: \\\\\\\"Tool (open-source)\\\\\\\"\\\\n        year: 2019\\\\n        relation: building-block\\\\n        summary: \\\\\\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2vec: Learning Distributed Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: POPL\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2seq: Generating Sequences from Structured Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\\\\\"\\\\n        authors: \\\\\\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\\\\\"\\\\n        venue: SANER\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\"\\\\n        authors: \\\\\\\"Shahd Seddik, Fatemeh Fard\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2026\\\\n        relation: contrast\\\\n        summary: \\\\\\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 5: Code Embeddings / Code Search\\\\n  # ==========================================================================\\\\n  code_embeddings_search:\\\\n    description: \\\\\\\"代码嵌入模型和代码搜索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\\\\\"\\\\n        authors: \\\\\\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: \\\\\\\"EMNLP (Findings)\\\\\\\"\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"StarCoder: May the Source Be with You!\\\\\\\"\\\\n        authors: \\\\\\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\\\\\"\\\\n        venue: TMLR\\\\n        year: 2023\\\\n        relation: building-block\\\\n        summary: \\\\\\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Code Llama: Open Foundation Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Qwen2.5-Coder Technical Report\\\\\\\"\\\\n        authors: \\\\\\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: building-block\\\\n        summary: \\\\\\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: background\\\\n        summary: \\\\\\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoFusion: Training Code Models to Understand Your Repository\\\\\\\"\\\\n        authors: \\\\\\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"BM25\\\\\\\"\\\\n        authors: \\\\\\\"Stephen Robertson, Hugo Zaragoza\\\\\\\"\\\\n        venue: \\\\\\\"Foundations and Trends in Information Retrieval\\\\\\\"\\\\n        year: 2009\\\\n        relation: baseline\\\\n        summary: \\\\\\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\\\n  # ==========================================================================\\\\n  graph_guided_inference:\\\\n    description: \\\\\\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\\\\\"\\\\n        authors: \\\\\\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\\\\\"\\\\n        authors: \\\\\\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\\\\\"\\\\n        venue: NAACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\\\\\"\\\\n        authors: \\\\\\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\\\\\"\\\\n        authors: \\\\\\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\\\\\"\\\\n        venue: ASE\\\\n        year: 2024\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 7: Infrastructure / Tools\\\\n  # ==========================================================================\\\\n  infrastructure:\\\\n    description: \\\\\\\"StructFuse 依赖的核心基础设施和工具\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Billion-Scale Similarity Search with GPUs\\\\\\\"\\\\n        authors: \\\\\\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\\\\\"\\\\n        venue: \\\\\\\"IEEE Transactions on Big Data\\\\\\\"\\\\n        year: 2021\\\\n        relation: building-block\\\\n        summary: \\\\\\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\\\\\"\\\\n        authors: \\\\\\\"Max Brunsfeld et al.\\\\\\\"\\\\n        venue: \\\\\\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\\\\\"\\\\n        year: 2018\\\\n        relation: building-block\\\\n        summary: \\\\\\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\\\\\"\\\\n        note: \\\\\\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 15999, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15999, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FnVMNmN6KQQ4M8fm59dwCy`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a32c3b88-a428-47f6-b711-3b9095e2f634",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtP4EADj5REb5m2YVKQ7io",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 23527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1322
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T22:46:30.494Z_

<details><summary>↩ Tool result · `toolu_01FnVMNmN6KQQ4M8fm59dwCy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 10174, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "ae28db8f-8430-4586-aa40-6d8c84161143",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\\\", \\\"content\\\": \\\"# Inference-Time Graph Methods 文献对比\\\\n\\\\n## 对比表\\\\n\\\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\\\n\\\\n## Discussion 要点\\\\n\\\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\\\n\\\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\\\n\\\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\\\n\\\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\\\n\\\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\\\n\\\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\\\n\\\\n## Related Work 段落草稿 (~200 words)\\\\n\\\\n**Graph-Based Methods for Code Understanding.**\\\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\\\n\\\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\\\n\\\\n---\\\\n\\\\n## 参考文献（全部已验证 2026-05-14）\\\\n\\\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\\\n- CodeRAG: arXiv:2504.10046, 2025\\\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\")\\\\n- CodeGRAG: arXiv:2405.02355, 2024\\\\n\\\\n---\\\\n\\\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\\\n\\\\n**两层重叠率数据（注意区分）**：\\\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\\\n\\\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\\\n|------|-------------------|----------------|------------------|\\\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\\\n\\\\n**核心修正**：之前基于 87% 预测\\\\\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\\\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\\\n\\\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\\\n\\\\n---\\\\n\\\\n## 运维经验 (2026-05-14)\\\\n\\\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\\\n\\\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\\\n\\\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\\\n\\\\n---\\\\n\\\\n## 关键决策记录\\\\n\\\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\\", \\\"total_chars\\\": 10174, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 10174, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check if there are any existing training config details I should look at - the memory.md mentions training parameters but I should check if there are more specific config details. Let me also check if there are existing artifacts or code that have the training configuration.

From the materials I have:

**paper_framing.md** key info:
- Formal definition: structure-grounded hard negative = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
- Core claims about embedding-distance mining vs gradient-based


- Dataflow negatives interaction with encoder geometry
- CodeQL pipeline as the structural grounding mechanism

**literature_map.yaml** key info:
- Citation keys for all referenced papers
- CoCoHaNeRe as contrast target
- DPR, ANCE, SimCLR as background
- CodeQL as building block
- SWE-bench ecosystem

**memory.md** key info:
- Training setup uses two encoders: Qwen2.5-Coder-3B and StarCoder2-3B
- InfoNCE contrastive loss with temperature τ
- Training config: lr=2e-5, batch_size=8, num_negatives=7, max_seq_length=2048, LoRA r

=16, proj_dim=256
- BM25 negative mining analysis and infrastructure details

I need to track down the temperature value and verify any additional config parameters in the codebase.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "eb62a44d-1b60-4092-b986-fddb92cb0a57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLdZygnkV26VLaF1Pf66cQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14281,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14281
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 15_

Let me check the codebase for the exact temperature and other training hyperparameters.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a36c0a76-254d-420e-b542-68ae6ecfd1bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLdZygnkV26VLaF1Pf66cQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14281,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14281
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_018Soyx3Dz88YTL3xAkgnwMJ`</summary>

```json
{
  "description": "Find training config params",
  "subagent_type": "Explore",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find the training configuration parameters - specifically the temperature value for contrastive loss, LoRA configuration (r, alpha, target_modules), learning rate, batch size, num_negatives, max_seq_length, projection dimension, number of epochs, optimizer details, and the dual checkpoint strategy details.\n\nSearch breadth: medium. Look in config files, training scripts, YAML configs, and any experiment config files. Also check the artifacts directory for any experiment reports that mention these values. Check any code repo paths that might be referenced."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "533687e2-b4fc-494d-a814-9d0f4d462e76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLdZygnkV26VLaF1Pf66cQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14281,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14281
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Find training config params",
  "task_type": "local_agent",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find the training configuration parameters - specifically the temperature value for contrastive loss, LoRA configuration (r, alpha, target_modules), learning rate, batch size, num_negatives, max_seq_length, projection dimension, number of epochs, optimizer details, and the dual checkpoint strategy details.\n\nSearch breadth: medium. Look in config files, training scripts, YAML configs, and any experiment config files. Also check the artifacts directory for any experiment reports that mention these values. Check any code repo paths that might be referenced.",
  "uuid": "afddf70b-a546-4e7c-ae99-0b208fd51489",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

## Round 1

91 recorded events

### User

_source line 18 · 2026-05-14T22:46:51.650Z_

In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find the training configuration parameters - specifically the temperature value for contrastive loss, LoRA configuration (r, alpha, target_modules), learning rate, batch size, num_negatives, max_seq_length, projection dimension, number of epochs, optimizer details, and the dual checkpoint strategy details.

Search breadth: medium. Look in config files, training scripts, YAML configs, and any experiment config files. Also check the artifacts directory for any experiment reports that mention these values. Check any code repo paths that might be referenced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "89bc7b45-71c0-4ab5-bad8-0bbae6ed306f"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 18504,
    "tool_uses": 1,
    "duration_ms": 1775
  },
  "last_tool_name": "Bash",
  "uuid": "52189625-7fc3-4d4f-bfb5-98a66489abd3",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_017Vg66NYevHjaDph9Vg3K6T`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context -type f -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.py\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "0db42280-c9c6-4e77-b94e-1eac34f048ed",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019zZ32gZwmowCXBwWxTM79f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18495,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T22:46:53.619Z_

<details><summary>↩ Tool result · `toolu_017Vg66NYevHjaDph9Vg3K6T`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_dual-gpu-verify_20260513T090837_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_plan017_review_fixes_20260514T092605_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_m2_full_qwen_20260514T112525_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_framing_analysis_20260513T184429_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_setup_download_starcoder2_3b_20260512T235233_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_fix-m2-hf-offline-resubmit_20260513T015621_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_m1-progress-check-v2_20260513T082755_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ssh_eval2000_urgent_check_20260514T025319_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_train_m2_full_qwen_20260513T162011_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_50repo_overlap_stats_20260512T195352_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_bjb1-gpu-fix-v2_20260513T052414_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_disk_emergency_assessment_20260513T013022_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_training_skeleton_20260512T100142_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix_repo_level_split_20260512T212539_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_dynamic_mining_impl_20260513T002931_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_starcoder_padtoken_hyperparams_20260513T163817_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_monitor_m1_progress_check_20260513T013124_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_extraction_skeleton_20260512T100103_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_m1-progress-check-v3_20260513T103626_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_bjb1-model-check-dryrun_20260513T032947_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_infra_p2b_gpu_check_restart_20260512T144458_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_plan013-dataflow-auto-start_20260513T090427_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_plan_017_graph_methods_20260513T212612_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_citation-integrity_20260514T213133_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ssh_rename_safety_eval_20260513T204556_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_starcoder2_support_20260513T000505_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_dataflow_empty_rate_analysis_20260512T153349_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_k_and_checkpoint_doc_20260514T175242_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ssh_m1_reextract_launch_20260513T193609_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_pilot-final-results-prep_20260513T114711_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_training_status_check_20260515_20260514T162453_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_plan-registry-association_20260513T075624_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_m2-embed-verify-fix-resubmit_20260513T051144_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_experiment_p2b_5reruns_train_20260512T172551_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_p0_log_extraction_20260513T153711_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_eval_skeleton_20260512T100215_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_infra_p2b_disk_cleanup_and_train_fix_20260512T162558_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_bjb1-gpu-verify-download-check_20260513T032104_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_data_bm25_precompute_20260512T111113_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ssh_neg_difficulty_2048_actual_run_20260513T224719_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_monitor_m1_progress_and_z_check_20260513T012551_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_monitor_tau_pilot_finish_and_cleanup_20260513T000052_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_bjb1-data-sync-path-fix_20260513T033421_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_wandb_m2_training_progress_20260513T215030_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_starcoder-random-data-fix_20260513T112208_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_experiment_p2b_steps3-5_fix_and_retrain_20260512T194430_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_registry-cleanup-plan006_20260513T041615_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_check_training_progress_0514_20260514T080329_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "f0050ec6-1496-41b2-853f-c18a3dc8e62e"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 22244,
    "tool_uses": 2,
    "duration_ms": 5826
  },
  "last_tool_name": "Bash",
  "uuid": "af0fd4bb-bfe6-4249-948f-28f4ab46d773",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01MZTjxgYzqSUKoiw5U6JykZ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "0d66e0e9-3511-4644-8edc-cb4b3071701f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0155QTbTZBjYBWnLdafx5LX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 18495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3736,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T22:46:57.531Z_

<details><summary>↩ Tool result · `toolu_01MZTjxgYzqSUKoiw5U6JykZ`</summary>

```text
total 260
drwxr-xr-x  9 ubuntu ubuntu  4096 May 14 22:09 .
drwxrwxr-x  4 ubuntu ubuntu  4096 May 13 12:16 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 13 12:16 .claude
-rw-r--r--  1 ubuntu ubuntu 12778 May 14 22:45 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 12 09:57 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  4971 May 14 21:27 ROADMAP.md
drwxr-xr-x 20 ubuntu ubuntu  4096 May 14 22:09 artifacts
drwxr-xr-x  2 ubuntu ubuntu 20480 May 14 20:36 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 12 09:57 decisions.lock
-rw-------  1 ubuntu ubuntu 40717 May 14 21:27 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 13 02:35 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 10:46 dream_registry.lock
-rw-------  1 ubuntu ubuntu  3641 May 14 17:20 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  3646 May 14 17:20 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 18366 May 14 08:28 eval_repobench.py
drwxr-xr-x  2 ubuntu ubuntu  4096 May 14 10:26 evaluation
-rw-r--r--  1 ubuntu ubuntu     0 May 12 12:58 experiment_plan.lock
-rw-------  1 ubuntu ubuntu  7371 May 14 18:50 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu 18221 May 14 21:33 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 12 10:01 logs
-rw-r--r--  1 ubuntu ubuntu 11148 May 14 21:08 memory.md
-rw-r--r--  1 ubuntu ubuntu 12082 May 14 22:09 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 12 11:30 registry.lock
-rw-------  1 ubuntu ubuntu 56802 May 14 21:33 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  4303 May 14 20:36 report.md
-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 09:56 study_status.lock
drwxr-xr-x  3 ubuntu ubuntu  4096 May 14 21:12 task_context
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "2babbd37-8955-4518-809f-6d88fd7b0ea8"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Finding **/config*.yaml",
  "usage": {
    "total_tokens": 23142,
    "tool_uses": 3,
    "duration_ms": 7532
  },
  "last_tool_name": "Glob",
  "uuid": "74427c01-0ff5-4d95-9efc-70cf71c163a8",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Glob · `toolu_016Zi83pE6R2LkVidA9d1KBq`</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a21e820d-e5de-4bb5-8408-0c5d5dd95f6c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018K8WvALhQwDCb7zKvYLhjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 22231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T22:46:59.208Z_

<details><summary>↩ Tool result · `toolu_016Zi83pE6R2LkVidA9d1KBq`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "9c7bcad6-6bc5-4e4c-9505-157214c72893"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Finding **/config*.py",
  "usage": {
    "total_tokens": 23143,
    "tool_uses": 4,
    "duration_ms": 7742
  },
  "last_tool_name": "Glob",
  "uuid": "736f58e6-7ca5-455a-95b2-0b81be4fc1f3",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Glob · `toolu_01VJFW2Jo1ufahKm1wSctj4b`</summary>

```json
{
  "pattern": "**/config*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "c5d38517-2af4-47a1-bb89-edb27ebd755a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018K8WvALhQwDCb7zKvYLhjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 22231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T22:46:59.405Z_

<details><summary>↩ Tool result · `toolu_01VJFW2Jo1ufahKm1wSctj4b`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "c3ce2a68-32b9-4b25-9b90-50b31e901e2e"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Finding **/train*.py",
  "usage": {
    "total_tokens": 23144,
    "tool_uses": 5,
    "duration_ms": 7978
  },
  "last_tool_name": "Glob",
  "uuid": "f2bcf39b-490f-4d86-b0f5-b7d567990e30",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Glob · `toolu_017YHxj3CU5VhUhaVVW8YYzq`</summary>

```json
{
  "pattern": "**/train*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "14de6a4e-53a9-4752-ae58-ba64d4fb2581",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018K8WvALhQwDCb7zKvYLhjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 22231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T22:46:59.650Z_

<details><summary>↩ Tool result · `toolu_017YHxj3CU5VhUhaVVW8YYzq`</summary>

```text
artifacts/code/training/train.py
artifacts/_project/intermediate/train.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a4ea03c4-d235-4c29-9fdb-1966868b1152"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Finding **/experiment*.yaml",
  "usage": {
    "total_tokens": 23145,
    "tool_uses": 6,
    "duration_ms": 8268
  },
  "last_tool_name": "Glob",
  "uuid": "7d644e4e-aeea-40da-a4cc-fb66f992524d",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Glob · `toolu_017zN19Wme9c3kwpUpjDDMsk`</summary>

```json
{
  "pattern": "**/experiment*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "35a8fd97-4b3d-4707-a167-d70d3ffbceac",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018K8WvALhQwDCb7zKvYLhjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 22231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T22:46:59.936Z_

<details><summary>↩ Tool result · `toolu_017zN19Wme9c3kwpUpjDDMsk`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "cf0b8cfa-bcf6-40db-8484-e72737a9b427"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading artifacts/code/training/train.py",
  "usage": {
    "total_tokens": 23665,
    "tool_uses": 7,
    "duration_ms": 9859
  },
  "last_tool_name": "Read",
  "uuid": "efa381ec-cea6-499f-9086-98e75a3c8a39",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01QKeNnt8Xoa2LSUJ2feMD6h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "fbd39263-2747-4d32-8fc8-7a1b52f51fb0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmELeLnhxztrB1bkHWogX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 23127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 503,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T22:47:01.519Z_

<details><summary>↩ Tool result · `toolu_01QKeNnt8Xoa2LSUJ2feMD6h`</summary>

```text
1	import os
2	os.environ["CUDA_VISIBLE_DEVICES"] = "4"
3	
4	"""StructFuse contrastive training entry point.
5	
6	Trains a bi-encoder (Qwen2.5-Coder-3B) with InfoNCE loss, data-flow-weighted
7	positives, and configurable hard-negative mining.  Supports single/multi-GPU
8	via HuggingFace Accelerate, LoRA, gradient checkpointing, and W&B logging.
9	"""
10	
11	from __future__ import annotations
12	
13	import argparse
14	import json
15	import math
16	import os
17	import random
18	from pathlib import Path
19	from typing import Any, Dict, List
20	
21	import numpy as np
22	import torch
23	from torch.utils.data import DataLoader, Dataset
24	from transformers import AutoTokenizer, get_cosine_schedule_with_warmup
25	
26	from accelerate import Accelerator
27	from accelerate.utils import set_seed
28	
29	from contrastive_model import StructFuseEncoder
30	from hard_negative_mining import build_miner, mine_batch
31	
32	
33	# ── Dataset ──────────────────────────────────────────────────────────
34	
35	class ContrastiveDataset(Dataset):
36	    """
37	    Each sample: {query, positive, negatives[], pos_weight, features[]}.
38	
39	    The raw data file is JSONL with fields:
40	        query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance,
41	        neg_candidates (list of file ids), features (dict per candidate).
42	
43	    Negatives are mined dynamically per epoch via `refresh_negatives()`.
44	    """
45	
46	    def __init__(
47	        self,
48	        data_path: str,
49	        tokenizer: AutoTokenizer,
50	        max_seq_length: int,
51	        num_negatives: int,
52	        pos_weight_alpha: float,
53	        use_fusion_head: bool,
54	    ):
55	        self.tokenizer = tokenizer
56	        self.max_seq_length = max_seq_length
57	        self.num_negatives = num_negatives
58	        self.alpha = pos_weight_alpha
59	        self.use_fusion_head = use_fusion_head
60	
61	        self.samples: List[Dict[str, Any]] = []
62	        with open(data_path) as f:
63	            for line in f:
64	                if line.strip():
65	                    self.samples.append(json.loads(line))
66	
67	        # mined negatives, refreshed each epoch
68	        self._negatives: Dict[int, List[Dict[str, Any]]] = {}
69	
70	    def refresh_negatives(self, mined: Dict[str, List[tuple]]):
71	        """Update negatives after an epoch-level mining pass."""
72	        self._negatives = {}
73	        for idx, sample in enumerate(self.samples):
74	            qid = sample["query_id"]
75	            negs = mined.get(qid, [])
76	            self._negatives[idx] = negs
77	
78	    def __len__(self):
79	        return len(self.samples)
80	
81	    def __getitem__(self, idx):
82	        s = self.samples[idx]
83	
84	        query_enc = self.tokenizer(
85	            s["query_tokens"], truncation=True, max_length=self.max_seq_length,
86	            padding=False, return_tensors=None,
87	        )
88	        pos_enc = self.tokenizer(
89	            s["pos_tokens"], truncation=True, max_length=self.max_seq_length,
90	            padding=False, return_tensors=None,
91	        )
92	
93	        # positive weight from data-flow distance
94	        dist = s.get("pos_dataflow_distance", 1.0)
95	        pos_weight = math.exp(-self.alpha * dist)
96	
97	        # negatives
98	        neg_pool = self._negatives.get(idx, [])
99	        if len(neg_pool) < self.num_negatives:
100	            # fallback: use candidates from the sample itself
101	            fallback = s.get("neg_candidates", [])
102	            random.shuffle(fallback)
103	            while len(neg_pool) < self.num_negatives and fallback:
104	                cid = fallback.pop()
105	                neg_pool.append({"id": cid, "tokens": s.get("candidate_tokens", {}).get(cid, "")})
106	
107	        neg_encs = []
108	        for ni in range(self.num_negatives):
109	            if ni < len(neg_pool):
110	                neg_item = neg_pool[ni]
111	                tokens = neg_item.get("tokens", neg_item.get("id", ""))
112	            else:
113	                tokens = ""
114	            neg_encs.append(self.tokenizer(
115	                tokens, truncation=True, max_length=self.max_seq_length,
116	                padding=False, return_tensors=None,
117	            ))
118	
119	        # features for fusion head
120	        features = None
121	        if self.use_fusion_head:
122	            features = self._extract_features(s, neg_pool)
123	
124	        return {
125	            "query_ids": query_enc["input_ids"],
126	            "query_mask": query_enc["attention_mask"],
127	            "pos_ids": pos_enc["input_ids"],
128	            "pos_mask": pos_enc["attention_mask"],
129	            "neg_ids": [ne["input_ids"] for ne in neg_encs],
130	            "neg_mask": [ne["attention_mask"] for ne in neg_encs],
131	            "pos_weight": pos_weight,
132	            "features": features,
133	        }
134	
135	    def _extract_features(self, sample, neg_pool) -> List[List[float]]:
136	        """Build (1+K, NUM_FEATURES) feature matrix for pos + negatives."""
137	        feat_keys = ["dataflow_distance", "bm25_score", "co_change_freq",
138	                      "inter_procedural_flag", "path_count"]
139	        all_feats = []
140	        # positive features
141	        pos_feat = [float(sample.get(f"pos_{k}", 0.0)) for k in feat_keys]
142	        all_feats.append(pos_feat)
143	        # negative features
144	        for ni in range(self.num_negatives):
145	            if ni < len(neg_pool):
146	                neg_item = neg_pool[ni]
147	                nf = [float(neg_item.get(k, 0.0)) for k in feat_keys]
148	            else:
149	                nf = [0.0] * len(feat_keys)
150	            all_feats.append(nf)
151	        return all_feats
152	
153	
154	def collate_fn(batch: List[Dict]) -> Dict[str, torch.Tensor]:
155	    """Pad variable-length sequences and stack into tensors."""
156	
157	    def _pad_1d(seqs, pad_value=0):
158	        max_len = max(len(s) for s in seqs)
159	        padded = [s + [pad_value] * (max_len - len(s)) for s in seqs]
160	        return torch.tensor(padded, dtype=torch.long)
161	
162	    def _pad_2d(batch_seqs, pad_value=0):
163	        """batch_seqs: list of list-of-seqs (B x K x varying L)."""
164	        max_len = max(len(s) for seqs in batch_seqs for s in seqs)
165	        result = []
166	        for seqs in batch_seqs:
167	            padded = [s + [pad_value] * (max_len - len(s)) for s in seqs]
168	            result.append(padded)
169	        return torch.tensor(result, dtype=torch.long)
170	
171	    query_ids = _pad_1d([b["query_ids"] for b in batch])
172	    query_mask = _pad_1d([b["query_mask"] for b in batch])
173	    pos_ids = _pad_1d([b["pos_ids"] for b in batch])
174	    pos_mask = _pad_1d([b["pos_mask"] for b in batch])
175	    neg_ids = _pad_2d([b["neg_ids"] for b in batch])
176	    neg_mask = _pad_2d([b["neg_mask"] for b in batch])
177	    pos_weights = torch.tensor([b["pos_weight"] for b in batch], dtype=torch.float32)
178	
179	    out = {
180	        "query_ids": query_ids,
181	        "query_mask": query_mask,
182	        "pos_ids": pos_ids,
183	        "pos_mask": pos_mask,
184	        "neg_ids": neg_ids,
185	        "neg_mask": neg_mask,
186	        "pos_weights": pos_weights,
187	    }
188	
189	    if batch[0]["features"] is not None:
190	        out["features"] = torch.tensor(
191	            [b["features"] for b in batch], dtype=torch.float32
192	        )
193	
194	    return out
195	
196	
197	# ── Evaluation ───────────────────────────────────────────────────────
198	
199	@torch.no_grad()
200	def evaluate(model: StructFuseEncoder, val_loader: DataLoader, accelerator: Accelerator) -> Dict[str, float]:
201	    """Compute recall@1/5/10 and average loss on the validation set."""
202	    model.eval()
203	    total_loss = 0.0
204	    total_correct = {1: 0, 5: 0, 10: 0}
205	    total_samples = 0
206	
207	    for batch in val_loader:
208	        kwargs = {
209	            "query_ids": batch["query_ids"],
210	            "query_mask": batch["query_mask"],
211	            "pos_ids": batch["pos_ids"],
212	            "pos_mask": batch["pos_mask"],
213	            "neg_ids": batch["neg_ids"],
214	            "neg_mask": batch["neg_mask"],
215	            "pos_weights": batch["pos_weights"],
216	            "features": batch.get("features"),
217	        }
218	        loss, logits = model(**kwargs)
219	
220	        total_loss += loss.item() * logits.size(0)
221	        total_samples += logits.size(0)
222	
223	        for k in [1, 5, 10]:
224	            if logits.size(1) >= k:
225	                topk = logits.topk(min(k, logits.size(1)), dim=1).indices
226	                total_correct[k] += (topk == 0).any(dim=1).sum().item()
227	            else:
228	                total_correct[k] += (logits.argmax(dim=1) == 0).sum().item()
229	
230	    # Aggregate across all processes for multi-GPU correctness
231	    stats = torch.tensor(
232	        [total_loss, total_samples] + [total_correct[k] for k in [1, 5, 10]],
233	        device=accelerator.device, dtype=torch.float64,
234	    )
235	    stats = accelerator.reduce(stats, reduction="sum")
236	    total_loss = stats[0].item()
237	    total_samples = stats[1].item()
238	    for i, k in enumerate([1, 5, 10]):
239	        total_correct[k] = stats[2 + i].item()
240	
241	    model.train()
242	    metrics = {"val_loss": total_loss / max(total_samples, 1)}
243	    for k in [1, 5, 10]:
244	        metrics[f"recall@{k}"] = total_correct[k] / max(total_samples, 1)
245	    return metrics
246	
247	
248	# ── Training ─────────────────────────────────────────────────────────
249	
250	def train(args):
251	    set_seed(args.seed)
252	    accelerator = Accelerator(log_with="wandb" if args.wandb_project else None)
253	
254	    if args.wandb_project and accelerator.is_main_process:
255	        accelerator.init_trackers(
256	            project_name=args.wandb_project,
257	            config=vars(args),
258	            init_kwargs={"wandb": {"name": args.wandb_run_name}},
259	        )
260	
261	    # tokenizer
262	    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
263	    if tokenizer.pad_token is None:
264	        tokenizer.pad_token = tokenizer.eos_token
265	
266	    # model
267	    model = StructFuseEncoder(
268	        model_name=args.model_name,
269	        proj_dim=args.proj_dim,
270	        use_projection=True,
271	        use_lora=args.use_lora,
272	        lora_r=args.lora_r,
273	        lora_alpha=args.lora_r * 2,
274	        use_fusion_head=args.use_fusion_head,
275	    )
276	    if args.gradient_checkpointing:
277	        model.enable_gradient_checkpointing()
278	
279	    # datasets
280	    train_ds = ContrastiveDataset(
281	        args.train_file, tokenizer, args.max_seq_length,
282	        args.num_negatives, args.pos_weight_alpha, args.use_fusion_head,
283	    )
284	    val_ds = ContrastiveDataset(
285	        args.val_file, tokenizer, args.max_seq_length,
286	        args.num_negatives, args.pos_weight_alpha, args.use_fusion_head,
287	    )
288	
289	    train_loader = DataLoader(
290	        train_ds, batch_size=args.batch_size, shuffle=True,
291	        collate_fn=collate_fn, num_workers=4, pin_memory=True,
292	    )
293	    val_loader = DataLoader(
294	        val_ds, batch_size=args.batch_size, shuffle=False,
295	        collate_fn=collate_fn, num_workers=2, pin_memory=True,
296	    )
297	
298	    # hard-negative miner
299	    dataflow_graph = _load_json_as_sets(args.dataflow_graph_file) if args.dataflow_graph_file else None
300	    embeddings = _load_embeddings(args.embeddings_file) if args.embeddings_file else None
301	    miner = build_miner(
302	        strategy=args.hard_negative_strategy,
303	        dataflow_graph=dataflow_graph,
304	        embeddings=embeddings,
305	    )
306	
307	    # optimizer & scheduler
308	    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=0.01)
309	    total_steps = len(train_loader) * args.num_epochs
310	    warmup_steps = int(total_steps * args.warmup_ratio)
311	    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)
312	
313	    # accelerate prepare
314	    model, optimizer, train_loader, val_loader, scheduler = accelerator.prepare(
315	        model, optimizer, train_loader, val_loader, scheduler
316	    )
317	
318	    # ── training loop ────────────────────────────────────────────
319	    global_step = 0
320	    output_dir = Path(args.output_dir)
321	    output_dir.mkdir(parents=True, exist_ok=True)
322	
323	    for epoch in range(args.num_epochs):
324	        # epoch-level negative mining
325	        if accelerator.is_main_process:
326	            accelerator.print(f"[Epoch {epoch+1}] Mining hard negatives ({args.hard_negative_strategy})...")
327	            queries = [s["query_id"] for s in train_ds.samples]
328	            pos_map = {s["query_id"]: [s["pos_id"]] for s in train_ds.samples}
329	            all_cands = list({s["query_id"] for s in train_ds.samples}
330	                            | {s["pos_id"] for s in train_ds.samples})
331	            mined = mine_batch(miner, queries, pos_map, all_cands, args.num_negatives)
332	            train_ds.refresh_negatives(mined)
333	
334	        accelerator.wait_for_everyone()
335	        model.train()
336	
337	        for batch in train_loader:
338	            kwargs = {
339	                "query_ids": batch["query_ids"],
340	                "query_mask": batch["query_mask"],
341	                "pos_ids": batch["pos_ids"],
342	                "pos_mask": batch["pos_mask"],
343	                "neg_ids": batch["neg_ids"],
344	                "neg_mask": batch["neg_mask"],
345	                "pos_weights": batch["pos_weights"],
346	                "features": batch.get("features"),
347	            }
348	            loss, logits = model(**kwargs)
349	
350	            accelerator.backward(loss)
351	            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
352	            optimizer.step()
353	            scheduler.step()
354	            optimizer.zero_grad()
355	
356	            global_step += 1
357	
358	            if accelerator.is_main_process and global_step % 50 == 0:
359	                lr = scheduler.get_last_lr()[0]
360	                accelerator.print(f"  step {global_step}  loss={loss.item():.4f}  lr={lr:.2e}")
361	                if args.wandb_project:
362	                    accelerator.log({"train_loss": loss.item(), "learning_rate": lr}, step=global_step)
363	
364	            if global_step % args.eval_steps == 0:
365	                metrics = evaluate(
366	                    accelerator.unwrap_model(model), val_loader, accelerator
367	                )
368	                if accelerator.is_main_process:
369	                    accelerator.print(f"  [eval@{global_step}] {metrics}")
370	                    if args.wandb_project:
371	                        accelerator.log(metrics, step=global_step)
372	
373	            if global_step % args.save_steps == 0 and accelerator.is_main_process:
374	                ckpt_dir = output_dir / f"checkpoint-{global_step}"
375	                _save_checkpoint(accelerator.unwrap_model(model), tokenizer, ckpt_dir, args)
376	
377	    # ── final save ───────────────────────────────────────────────
378	    if accelerator.is_main_process:
379	        final_metrics = evaluate(accelerator.unwrap_model(model), val_loader, accelerator)
380	        accelerator.print(f"[Final eval] {final_metrics}")
381	        if args.wandb_project:
382	            accelerator.log(final_metrics, step=global_step)
383	        _save_checkpoint(accelerator.unwrap_model(model), tokenizer, output_dir / "final", args)
384	        accelerator.print(f"Training complete. Model saved to {output_dir / 'final'}")
385	
386	    if args.wandb_project:
387	        accelerator.end_training()
388	
389	
390	# ── helpers ──────────────────────────────────────────────────────────
391	
392	def _save_checkpoint(model, tokenizer, path, args):
393	    path = Path(path)
394	    path.mkdir(parents=True, exist_ok=True)
395	    torch.save(model.state_dict(), path / "model.pt")
396	    tokenizer.save_pretrained(path)
397	    with open(path / "training_config.json", "w") as f:
398	        json.dump(vars(args), f, indent=2)
399	
400	
401	def _load_json_as_sets(path: str) -> Dict[str, set]:
402	    with open(path) as f:
403	        raw = json.load(f)
404	    return {k: set(v) for k, v in raw.items()}
405	
406	
407	def _load_embeddings(path: str) -> Dict[str, np.ndarray]:
408	    data = np.load(path, allow_pickle=True)
409	    return {str(k): data[k] for k in data.files}
410	
411	
412	# ── CLI ──────────────────────────────────────────────────────────────
413	
414	def parse_args():
415	    p = argparse.ArgumentParser(description="StructFuse contrastive training")
416	    p.add_argument("--model-name", default="Qwen/Qwen2.5-Coder-3B")
417	    p.add_argument("--train-file", required=True)
418	    p.add_argument("--val-file", required=True)
419	    p.add_argument("--output-dir", required=True)
420	    p.add_argument("--batch-size", type=int, default=8)
421	    p.add_argument("--learning-rate", type=float, default=2e-5)
422	    p.add_argument("--num-epochs", type=int, default=3)
423	    p.add_argument("--warmup-ratio", type=float, default=0.1)
424	    p.add_argument("--num-negatives", type=int, default=7)
425	    p.add_argument("--hard-negative-strategy", choices=["random", "embedding_distance", "dataflow_aware"], default="dataflow_aware")
426	    p.add_argument("--hard-negative-ratio", type=float, default=0.5)
427	    p.add_argument("--temperature", type=float, default=0.07)
428	    p.add_argument("--pos-weight-alpha", type=float, default=1.0)
429	    p.add_argument("--use-fusion-head", action="store_true")
430	    p.add_argument("--use-lora", action="store_true")
431	    p.add_argument("--lora-r", type=int, default=16)
432	    p.add_argument("--proj-dim", type=int, default=256)
433	    p.add_argument("--gradient-checkpointing", action="store_true")
434	    p.add_argument("--eval-steps", type=int, default=500)
435	    p.add_argument("--save-steps", type=int, default=1000)
436	    p.add_argument("--max-seq-length", type=int, default=2048)
437	    p.add_argument("--seed", type=int, default=42)
438	    p.add_argument("--wandb-project", default="structfuse")
439	    p.add_argument("--wandb-run-name", default=None)
440	    p.add_argument("--dataflow-graph-file", default=None, help="JSON file: {file_id: [reachable_ids]}")
441	    p.add_argument("--embeddings-file", default=None, help=".npz file with pre-computed embeddings")
442	    return p.parse_args()
443	
444	
445	if __name__ == "__main__":
446	    train(parse_args())
447	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "e46faa21-1ad8-4a0b-85ff-7f372e11e0ba"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading experiment_plan.yaml",
  "usage": {
    "total_tokens": 23673,
    "tool_uses": 8,
    "duration_ms": 10279
  },
  "last_tool_name": "Read",
  "uuid": "88d7b795-ea98-4926-8d92-e2184b50ee25",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01VMJ2iJsmhMr7HQtqjECPHo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "28df38cd-5340-45d2-9532-f539602d581a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmELeLnhxztrB1bkHWogX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 23127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 503,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T22:47:01.938Z_

<details><summary>↩ Tool result · `toolu_01VMJ2iJsmhMr7HQtqjECPHo`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected
5	    vs gold statistics'
6	  priority: P0
7	  gpu_budget_hours: 0
8	  deps: []
9	  registry_id: m1_extraction
10	  mvp_registry_id: mvp_p1_codeql_feasibility
11	- id: plan_002
12	  claim: 1
13	  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,
14	    3 seeds each, Qwen2.5-Coder-3B LoRA'
15	  priority: P0
16	  gpu_budget_hours: 200
17	  deps:
18	  - plan_001
19	  registry_id: m2_embed_verify
20	  mvp_registry_id: mvp_p2b_contrastive_training
21	  full_registry_ids: ["m2_full_qwen", "m2_full_starcoder"]
22	- id: plan_003
23	  claim: 1
24	  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best
25	    checkpoint, Qwen3.6-27B agent'
26	  priority: P0
27	  gpu_budget_hours: 40
28	  deps:
29	  - plan_002
30	  notes: 'eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos
31	    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.'
32	- id: plan_004
33	  claim: 1
34	  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no
35	    LLM agent'
36	  priority: P1
37	  gpu_budget_hours: 15
38	  deps:
39	  - plan_002
40	  notes: 'eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via
41	    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting
42	    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs —
43	    dream reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but
44	    not RepoBench-R) across all 3 tiers.'
45	- id: plan_005
46	  claim: 2
47	  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding
48	    negatives 何时最有害'
49	  priority: P1
50	  gpu_budget_hours: 5
51	  deps:
52	  - plan_002
53	  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:
54	    repo size / pool size / query-positive similarity. Outputs stratified_results.json
55	    + plots PDF. Awaiting M2 checkpoints for re-eval. [Dream fix] Must add 2 more
56	    strata: (a) structural data availability (34% with dataflow vs 66% fallback) per
57	    [B][M][W] all tiers, (b) neg_difficulty quartile analysis per [W] tier. Total 5
58	    strata.'
59	- id: plan_006
60	  claim: 3
61	  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,
62	    connected-but-not-gold ratio by repo size'
63	  priority: P0
64	  gpu_budget_hours: 0
65	  deps:
66	  - plan_001
67	  registry_id: plan_006_scalability
68	- id: plan_007
69	  claim: 1
70	  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'
71	  priority: P1
72	  gpu_budget_hours: 20
73	  deps:
74	  - plan_001
75	- id: plan_008
76	  claim: 1
77	  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'
78	  priority: P1
79	  gpu_budget_hours: 15
80	  deps:
81	  - plan_001
82	- id: plan_009
83	  claim: 1
84	  description: 'Ablation: fusion head (embedding-only vs structural-features-only
85	    vs combined)'
86	  priority: P1
87	  gpu_budget_hours: 10
88	  deps:
89	  - plan_002
90	- id: plan_010
91	  claim: 1
92	  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'
93	  priority: P2
94	  gpu_budget_hours: 10
95	  deps:
96	  - plan_001
97	- id: plan_011
98	  claim: 1
99	  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether
100	    data-flow helps'
101	  priority: P1
102	  gpu_budget_hours: 5
103	  deps:
104	  - plan_003
105	- id: plan_012
106	  claim: 1
107	  description: 'Qualitative examples: 5-10 cases where structural negatives changed
108	    retrieval outcome'
109	  priority: P2
110	  gpu_budget_hours: 0
111	  deps:
112	  - plan_003
113	- id: plan_013
114	  claim: 1
115	  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,
116	    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'
117	  priority: P0
118	  gpu_budget_hours: 15
119	  deps:
120	  - plan_001
121	  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.
122	    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'
123	  registry_id: plan_013_starcoder
124	  full_registry_id: "m2_full_starcoder"
125	- id: plan_014
126	  claim: 2
127	  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test
128	    regime-specificity of embedding harm'
129	  priority: P1
130	  gpu_budget_hours: 70
131	  deps:
132	  - plan_002
133	  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'
134	- id: plan_015
135	  claim: 2
136	  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per
137	    epoch vs static (mine once from pretrained). Isolate selection criterion from
138	    curriculum shift.'
139	  priority: P1
140	  gpu_budget_hours: 10
141	  deps:
142	  - plan_002
143	  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound
144	    for Claim 2'
145	- id: plan_016
146	  claim: 1
147	  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals
148	    to end-to-end resolve rate evaluation'
149	  priority: P0
150	  gpu_budget_hours: 0
151	  deps:
152	  - plan_003
153	  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical
154	    significance test'
155	- id: plan_017
156	  claim: 1
157	  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,
158	    LocAgent — is StructFuse complementary or alternative? Analysis complete, document
159	    in artifacts/analysis/plan017_literature_comparison.md. Discussion draft in
160	    artifacts/paper_drafts/discussion_draft.md.'
161	  priority: P1
162	  gpu_budget_hours: 0
163	  deps:
164	  - plan_002
165	  registry_id: plan_017_literature
166	  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'
167	  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,
168	    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.
169	    Conclusion: training-time vs inference-time are complementary, not competing.'
170	- id: plan_018
171	  claim: 1
172	  description: 'BM25 negative baseline: mine BM25-based hard negatives as 4th strategy,
173	    train ≥1 seed × 2 encoders, compare R@1 with random/embedding/dataflow. Empirically
174	    verify CoCoHaNeRe BM25-proxy caused the reported harm.'
175	  priority: P0
176	  gpu_budget_hours: 15
177	  deps:
178	  - plan_001
179	  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers identify missing BM25
180	    baseline as #1 structural gap. CoCoHaNeRe correction claim requires empirical
181	    verification — without it the paper motivation is asserted but unverified.'
182	  notes: 'Phase 1 (CPU, can start now): build BM25 index over training corpus, mine
183	    top-k BM25 negatives per query using same protocol as other strategies, produce
184	    bm25_training_data.jsonl. Phase 2 (GPU, after M2 frees up): train 1 seed × 2
185	    encoders with BM25 negatives (~7.5h each). 3 seeds preferred if GPU budget allows.
186	    Expected result: BM25 negatives harm → confirms CoCoHaNeRe artifact → closes argument.'
187	- id: plan_019
188	  claim: 1
189	  description: 'Pool size sensitivity analysis: test strategy ranking stability at
190	    pool={50, 100, 200, 500} candidates per query on SWE-smith validation.'
191	  priority: P1
192	  gpu_budget_hours: 5
193	  deps:
194	  - plan_002
195	  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers flag pool=50 as
196	    unrealistically small. Strategy differences may not preserve at realistic pool sizes.'
197	  notes: 'Requires M2 best checkpoints. Re-evaluate on expanded candidate pools.
198	    If strategy ranking changes at pool>200, must discuss in paper.'
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "2de76d80-6e67-4991-8e5b-968f0321274b"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 23681,
    "tool_uses": 9,
    "duration_ms": 10363
  },
  "last_tool_name": "Read",
  "uuid": "8e1ffbac-27af-432d-88d1-02ec137bce4c",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01RnjUACLNzUeeqYxeFcPB9j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a0e2acfa-8475-488b-be91-c0b1e82123be",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VmELeLnhxztrB1bkHWogX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 23127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 503,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T22:47:02.018Z_

<details><summary>↩ Tool result · `toolu_01RnjUACLNzUeeqYxeFcPB9j`</summary>

```text
1	# Inference-Time Graph Methods 文献对比
2	
3	## 对比表
4	
5	| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |
6	|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|
7	| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |
8	| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |
9	| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |
10	| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |
11	| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |
12	| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |
13	| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |
14	| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |
15	| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |
16	
17	## Discussion 要点
18	
19	### StructFuse vs Inference-Time Graph Methods: 互补性与差异性
20	
21	1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.
22	
23	2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.
24	
25	3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.
26	
27	4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.
28	
29	5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.
30	
31	## Related Work 段落草稿 (~200 words)
32	
33	**Graph-Based Methods for Code Understanding.**
34	Recent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.
35	
36	These methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.
37	
38	---
39	
40	## 参考文献（全部已验证 2026-05-14）
41	
42	- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025
43	- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025
44	- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified
45	- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025
46	- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024
47	- CodeRAG: arXiv:2504.10046, 2025
48	- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair")
49	- CodeGRAG: arXiv:2405.02355, 2024
50	
51	---
52	
53	## BM25 Negative Mining 策略洞察 (2026-05-14, updated)
54	
55	**两层重叠率数据（注意区分）**：
56	- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%
57	- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选
58	
59	**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：
60	| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |
61	|------|-------------------|----------------|------------------|
62	| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |
63	| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |
64	| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |
65	
66	**核心修正**：之前基于 87% 预测"Phase 2 中 BM25 R@1 很可能接近 embedding"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。
67	
68	**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。
69	
70	---
71	
72	## 运维经验 (2026-05-14)
73	
74	**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。
75	
76	**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。
77	
78	**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。
79	
80	---
81	
82	## 关键决策记录
83	
84	**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "4fb4941c-d3b4-4744-8987-baaeeceb4684"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Searching for temperature|lora_r|lora_alpha|learning_rate|batch…",
  "usage": {
    "total_tokens": 37155,
    "tool_uses": 10,
    "duration_ms": 13162
  },
  "last_tool_name": "Grep",
  "uuid": "4e0c443b-b38f-4982-b16c-50ed2f4ced82",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_015pXuQmgAQp652iSvy66zbu`</summary>

```json
{
  "pattern": "temperature|lora_r|lora_alpha|learning_rate|batch.size|num_negatives|max_seq_length|proj_dim|num_epochs|checkpoint",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "d960af5e-41ca-41e2-ab9d-4381da1df157",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XTtzRR364ejP4QawH4fMP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13472,
      "cache_read_input_tokens": 23630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13472,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T22:47:04.885Z_

<details><summary>↩ Tool result · `toolu_015pXuQmgAQp652iSvy66zbu`</summary>

```text
Found 250 files limit: 250
logs/workers/worker_write_method-draft_20260514T224613.log
logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39.jsonl
logs/workers/worker_write_introduction-draft_20260514T224556.log
logs/chats/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director.jsonl
logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer.jsonl
.claude/sessions/director_3a5c0d9a/AGENTS.md
.claude/sessions/director_3a5c0d9a/CLAUDE.md
.claude/sessions/agent_204785e5/AGENTS.md
.claude/sessions/agent_204785e5/CLAUDE.md
.claude/sessions/reviewer_65cfe724/AGENTS.md
.claude/sessions/reviewer_65cfe724/CLAUDE.md
logs/workers/worker_fix_related-work-info_20260514T224433.log
artifacts/manifest.yaml
artifacts/_project/paper/related_work_v1_dc54a3.md
artifacts/paper_drafts/related_work_v1.md
logs/workers/worker_prep_swebench-dryrun_20260514T220727_result.json
logs/workers/worker_prep_swebench-dryrun_20260514T220727.log
artifacts/plan_003/report/swebench_dryrun_report.md
artifacts/plan_003/swebench_dryrun_report.md
logs/workers/worker_write_related-work-draft_20260514T220708.log
artifacts/_project/paper/related_work_v1.md
logs/workers/worker_fix_citation-integrity_20260514T213133.log
registry.yaml
literature_map.yaml
logs/chats/cron_hook_m2_full_starcoder.jsonl
logs/ralph_loop_timeline.jsonl
logs/chats/cron_hook_m2_full_qwen.jsonl
ROADMAP.md
decisions.yaml
logs/chats/worker_research_related-work-expansion_20260514T211428.jsonl
logs/workers/worker_research_related-work-expansion_20260514T211428.log
logs/chats/worker_monitor_progress_check_may15_20260514T211439.jsonl
logs/workers/worker_monitor_progress_check_may15_20260514T211439.log
.claude/sessions/agent_1b98c4fb/AGENTS.md
.claude/sessions/agent_1b98c4fb/CLAUDE.md
task_context/agent.md
logs/chats/archive/cron_hook_m2_full_starcoder_20260514T211229_415925.jsonl
.claude/sessions/agent_2bc11d4f/AGENTS.md
.claude/sessions/agent_2bc11d4f/CLAUDE.md
task_context/history/agent/loop_7.md
logs/chats/archive/cron_hook_m2_full_qwen_20260514T211211_559646.jsonl
memory.md
logs/workers/worker_fix_plan_005_batch_encoding_and_sim_bins_20260514T205608_result.json
logs/workers/worker_fix_plan_005_batch_encoding_and_sim_bins_20260514T205608.log
task_context/history/agent/loop_6_1778793131.md
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260514T210244_527647.jsonl
logs/workers/worker_code_plan_005_real_eval_script_20260514T204618_result.json
logs/workers/worker_code_plan_005_real_eval_script_20260514T204618.log
logs/chats/worker_check_m2_progress_20260514_v3_20260514T204214.jsonl
logs/workers/worker_check_m2_progress_20260514_v3_20260514T204214.log
logs/workers/worker_analysis_plan_005_v1v2_diff_20260514T203611.log
logs/workers/worker_analysis_dataflow_reposize_confound_20260514T203328.log
logs/workers/worker_analysis_plan_005_stratified_v2_20260514T202757_result.json
logs/workers/worker_analysis_plan_005_stratified_v2_20260514T202757.log
logs/workers/worker_check_bm25_watcher_and_phase1_20260514T202819_result.json
logs/workers/worker_check_bm25_watcher_and_phase1_20260514T202819.log
logs/workers/worker_analysis_plan_005_stratified_20260514T201443_result.json
logs/chats/worker_analysis_plan_005_stratified_20260514T201443.jsonl
logs/workers/worker_analysis_plan_005_stratified_20260514T201443.log
artifacts/plan005_stratified_analysis_report.md
logs/workers/worker_fix_train_py_adapter_only_checkpoint_20260514T193437_result.json
logs/workers/worker_fix_train_py_adapter_only_checkpoint_20260514T193437.log
logs/workers/worker_fix_starcoder_checkpoint_cleanup_bug_20260514T193339_result.json
logs/workers/worker_fix_starcoder_checkpoint_cleanup_bug_20260514T193339.log
logs/workers/worker_fix_plan_003_repo_clone_20260514T190217.log
logs/chats/worker_fix_disk_cleanup_immediate_20260514T191433.jsonl
logs/workers/worker_fix_disk_cleanup_immediate_20260514T191433.log
logs/workers/worker_fix_disk_cleanup_step1_20260514T191344_result.json
logs/chats/worker_fix_disk_cleanup_step1_20260514T191344.jsonl
logs/workers/worker_fix_disk_cleanup_step1_20260514T191344.log
logs/workers/worker_check_urgent_3issues_20260514_20260514T190956_result.json
logs/workers/worker_check_urgent_3issues_20260514_20260514T190956.log
logs/workers/worker_check_m2_status_20260514_v2_20260514T190621_result.json
logs/workers/worker_check_m2_status_20260514_v2_20260514T190621.log
task_context/director.md
logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260514T190505_661342.jsonl
task_context/reviewer.md
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260514T190436_913882.jsonl
logs/workers/worker_code_plan_003_swebench_dryrun_20260514T185034.log
artifacts/plan003_swebench_dryrun_report.md
experiment_plan.yaml
checkpoints/plan_017_literature_DONE_20260514T184939.json
checkpoints/plan_017_literature_ANALYZING_20260514T184923.json
checkpoints/plan_017_literature_ANALYZING_20260514T184920.json
checkpoints/plan_017_literature_RUNNING_20260514T184916.json
logs/workers/worker_fix_bm25_watcher_setup_20260514T181354.log
artifacts/paper_drafts/experimental_setup_k_checkpoint.md
logs/workers/worker_fix_insert_bm25_into_resume_20260514T180458.log
logs/workers/worker_check_gpu_status_20260514_20260514T180700.log
logs/workers/worker_fix_gpu_resume_with_bm25_20260514T175853_result.json
logs/workers/worker_fix_gpu_resume_with_bm25_20260514T175853.log
task_context/history/agent/loop_6.md
logs/chats/archive/cron_hook_m2_full_qwen_20260514T180410_292393.jsonl
logs/workers/worker_fix_cuda1_conflict_emergency_20260514T180110.log
logs/chats/worker_fix_qwen_cuda0_check_resume_20260514T175730.jsonl
logs/workers/worker_fix_qwen_cuda0_check_resume_20260514T175730.log
logs/workers/worker_code_plan_018_bm25_phase2_script_20260514T175227_result.json
logs/workers/worker_code_plan_018_bm25_phase2_script_20260514T175227.log
logs/workers/worker_writing_k_and_checkpoint_doc_20260514T175242_result.json
logs/workers/worker_writing_k_and_checkpoint_doc_20260514T175242.log
artifacts/_project/paper/experimental_setup_k_checkpoint.md
logs/workers/worker_fix_m2_full_starcoder_resume_20260514T175326_result.json
logs/chats/worker_fix_m2_full_starcoder_resume_20260514T175326.jsonl
logs/workers/worker_fix_m2_full_starcoder_resume_20260514T175326.log
checkpoints/m2_full_starcoder_DONE_20260514T174955.json
checkpoints/m2_full_starcoder_RUNNING_20260514T174955.json
artifacts/dream_reports/dream_20260514T162530/meta.yaml
artifacts/dream_reports/dream_20260514T162530/logs/review_worst.log
logs/workers/worker_code_plan_018_bm25_mining_20260514T163941.log
artifacts/dream_reports/dream_20260514T162530/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/logs/review_median.log
artifacts/dream_reports/dream_20260514T162530/median/review_report.md
artifacts/dream_reports/dream_20260514T162530/best/review_report.md
logs/workers/worker_writing_plan_017_discussion_20260514T170421.log
artifacts/dream_reports/dream_20260514T162530/median/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/logs/review_best.log
artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T162530/worst/paper.aux
logs/workers/worker_code_plan_018_bm25_phase1_20260514T163821.log
artifacts/dream_reports/dream_20260514T162530/worst/paper.tex
artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T162530/median/paper.aux
artifacts/dream_reports/dream_20260514T162530/median/paper.tex
artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T162530/best/paper.aux
artifacts/dream_reports/dream_20260514T162530/best/paper.tex
artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T162530/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T162530/logs/phase2_best_attempt0.log
logs/chats/worker_ops_training_status_check_20260515_20260514T162453.jsonl
logs/workers/worker_ops_training_status_check_20260515_20260514T162453.log
logs/chats/worker_ops_urgent_status_check_20260514T161829.jsonl
logs/workers/worker_ops_urgent_status_check_20260514T161829.log
logs/workers/worker_research_plan015_design_20260514T161215_result.json
logs/workers/worker_research_plan015_design_20260514T161215.log
artifacts/_project/report/plan_015_dynamic_mining_design.md
task_context/history/director/loop_5.md
logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260514T161625_042063.jsonl
logs/workers/worker_knowledge_update_roadmap_20260514T161154.log
logs/workers/worker_code_chain_s42_supplement_20260514T152851.log
logs/workers/worker_code_fix_qwen_unbuffered_20260514T153002.log
logs/workers/worker_code_fix_s42_gap_20260514T151836_result.json
logs/workers/worker_code_fix_s42_gap_20260514T151836.log
logs/chats/worker_code_prepare_stat_analysis_20260514T150704.jsonl
logs/workers/worker_code_prepare_stat_analysis_20260514T150704.log
logs/chats/worker_check_training_status_loop6_20260514T150013.jsonl
logs/workers/worker_check_training_status_loop6_20260514T150013.log
artifacts/status_check_loop6.md
logs/workers/worker_diagnose_m2_starcoder_progress_20260514T150040.log
artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md
artifacts/m2_starcoder_status_check.md
logs/chats/worker_diagnose_m2_qwen_cuda0_status_20260514T145916.jsonl
logs/workers/worker_diagnose_m2_qwen_cuda0_status_20260514T145916.log
artifacts/m2_qwen_status_check.md
task_context/history/reviewer/loop_7.md
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260514T145712_162723.jsonl
task_context/history/agent/loop_5_1778781850.md
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260514T145710_491440.jsonl
task_context/history/agent/loop_5.md
logs/chats/archive/cron_hook_m2_full_qwen_20260514T145707_652625.jsonl
logs/workers/worker_diagnose_qwen_s43_crash_20260514T113103.log
logs/workers/worker_analysis_m2_full_qwen_20260514T112525.log
artifacts/m2_full_qwen_analysis.md
artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md
checkpoints/m2_full_qwen_ANALYZING_20260514T112434.json
logs/chats/worker_urgent_kill_and_restart_m2_loops_20260514T111500.jsonl
logs/workers/worker_urgent_kill_and_restart_m2_loops_20260514T111500.log
logs/workers/worker_viz_neg_difficulty_figure_v2_20260514T103252.log
logs/workers/worker_viz_neg_difficulty_figure_20260514T101839.log
logs/chats/worker_fix_plan017_review_fixes_20260514T092605.jsonl
logs/workers/worker_fix_plan017_review_fixes_20260514T092605.log
logs/workers/worker_code_plan005_stratified_analysis_20260514T092057_result.json
logs/workers/worker_code_plan005_stratified_analysis_20260514T092057.log
artifacts/dream_reports/dream_20260514T075732/meta.yaml
artifacts/dream_reports/dream_20260514T075732/logs/review_worst.log
artifacts/dream_reports/dream_20260514T075732/worst/review_report.md
artifacts/dream_reports/dream_20260514T075732/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/logs/review_median.log
artifacts/dream_reports/dream_20260514T075732/median/review_report.md
artifacts/dream_reports/dream_20260514T075732/best/review_report.md
logs/workers/worker_code_eval_repobench_20260514T082145_result.json
logs/chats/worker_code_eval_repobench_20260514T082145.jsonl
logs/workers/worker_code_eval_repobench_20260514T082145.log
artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/logs/review_best.log
eval_repobench.py
logs/workers/worker_prep_swebench_repo_clone_20260514T081920.log
artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T075732/worst/paper.aux
artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T075732/median/paper.aux
artifacts/dream_reports/dream_20260514T075732/median/paper.tex
logs/workers/worker_code_m2_early_stopping_20260514T081434_result.json
logs/workers/worker_prep_swebench_dryrun_random_s42_20260514T080904_result.json
logs/workers/worker_code_m2_early_stopping_20260514T081434.log
logs/workers/worker_prep_swebench_dryrun_random_s42_20260514T080904.log
artifacts/dream_reports/dream_20260514T075732/median/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T075732/best/paper.aux
artifacts/dream_reports/dream_20260514T075732/best/paper.tex
logs/workers/worker_fix_log_script_and_verify_s43_20260514T080736.log
artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase2_median_attempt0.log
logs/workers/worker_check_training_progress_0514_20260514T080329.log
logs/workers/worker_prep_swebench_eval_readiness_20260514T080045_result.json
logs/chats/worker_prep_swebench_eval_readiness_20260514T080045.jsonl
logs/workers/worker_prep_swebench_eval_readiness_20260514T080045.log
artifacts/swebench_eval_readiness.md
logs/workers/worker_check_training_progress_loop5_20260514T080030_result.json
logs/chats/worker_check_training_progress_loop5_20260514T080030.jsonl
logs/workers/worker_check_training_progress_loop5_20260514T080030.log
artifacts/training_status_snapshot.md
artifacts/dream_reports/dream_20260514T075732/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase1_attempt0.log
task_context/history/agent/loop_4.md
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260514T075842_714317.jsonl
task_context/history/reviewer/loop_6.md
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260514T075838_386698.jsonl
task_context/history/director/loop_4.md
logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260514T075833_559307.jsonl
logs/workers/worker_ssh_starcoder_eval1500_check_20260514T053507.log
logs/workers/worker_ssh_training_progress_check_d026_20260514T053459_result.json
logs/workers/worker_ssh_training_progress_check_d026_20260514T053459.log
logs/workers/worker_ssh_s43_launch_readiness_20260514T053516_result.json
logs/workers/worker_ssh_s43_launch_readiness_20260514T053516.log
logs/workers/worker_ssh_eval2000_urgent_check_20260514T025319_result.json
logs/workers/worker_ssh_eval2000_urgent_check_20260514T025319.log
logs/workers/worker_knowledge_update_experiment_plan_20260514T025324.log
logs/workers/worker_ssh_eval2000_check_v2_20260514T014910_result.json
logs/workers/worker_ssh_eval2000_check_v2_20260514T014910.log
logs/workers/worker_ssh_m2_training_progress_latest_20260514T014638_result.json
logs/chats/worker_ssh_m2_training_progress_latest_20260514T014638.jsonl
logs/workers/worker_ssh_m2_training_progress_latest_20260514T014638.log
logs/chats/worker_ssh_m2_qwen_eval2000_check_20260514T014332.jsonl
logs/workers/worker_ssh_m2_qwen_eval2000_check_20260514T014332.log
logs/workers/worker_ssh_plan003_dryrun_v2_verify_20260514T010818_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "1a61e6fe-c596-4c8c-a1e1-4270bf9ef941"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 37156,
    "tool_uses": 11,
    "duration_ms": 13507
  },
  "last_tool_name": "Read",
  "uuid": "780c563f-a149-478d-8ca5-66700b515836",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01LR1cLo6Emzg8EodT1e44jk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "5315ff55-0af7-4848-9905-33516f5c2ecd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XTtzRR364ejP4QawH4fMP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13472,
      "cache_read_input_tokens": 23630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13472,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T22:47:05.170Z_

<details><summary>↩ Tool result · `toolu_01LR1cLo6Emzg8EodT1e44jk`</summary>

```text
1	baseline: null
2	experiments:
3	  mvp_p1_codeql_feasibility:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-12T11:30:45.938Z'
7	    updated_at: '2026-05-12T11:58:06.197Z'
8	    spec:
9	      command: python extraction/extract_dataflow.py + codeql query run (call_graph.ql
10	        + bounded_dataflow.ql)
11	      server: cqa1-21977
12	      data_path: '/root/structfuse/mvp_data/repos (8 SWE-smith instances: flask, requests,
13	        pytest, pylint, xarray, astropy, sphinx, matplotlib)'
14	      data_count: 8
15	      model_name: N/A (CPU pipeline)
16	      seed: null
17	      hypothesis: 'H1: CodeQL 2-hop bounded data-flow timeout <30%; H2: connected
18	        files gold patch coverage significantly > disconnected'
19	      plan_id: mvp_p1_codeql_feasibility
20	    conclusion: success
21	    metrics:
22	      timeout_rate: 0
23	      repos_processed: 8
24	      repos_skipped: 2
25	      cg_mean_s: 29.6
26	      cg_max_s: 119.8
27	      df_mean_s: 43.4
28	      df_max_s: 167.1
29	      h2_connected_coverage: 0.014815
30	      h2_disconnected_coverage: 0
31	      h2_fisher_p: 6.5e-09
32	      h2_gold_in_connected_ratio: 1
33	      h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'
34	    log_path: /root/autodl-tmp/mvp_results/mvp_phase1_report.json
35	    checkpoint_path: N/A (CPU pipeline, no model checkpoint)
36	    completed_at: '2026-05-12T11:31:16.335Z'
37	  mvp_p2a_linear_proxy:
38	    status: DONE
39	    retry_count: 0
40	    created_at: '2026-05-12T11:53:42.223Z'
41	    updated_at: '2026-05-12T11:58:15.436Z'
42	    spec:
43	      command: python evaluation/linear_proxy.py (logistic regression on data-flow
44	        features + BM25)
45	      server: cqa1-21977
46	      data_path: /root/autodl-tmp/mvp_results/ + /root/structfuse/mvp_data/bm25/
47	      data_count: 8
48	      model_name: LogisticRegression (scikit-learn)
49	      seed: null
50	      hypothesis: 'H2-confirm: data-flow features 的线性分类器预测 bug-relevant 文件优于纯 BM25
51	        baseline'
52	      plan_id: mvp_p2a_linear_proxy
53	    conclusion: success
54	    metrics:
55	      df_bm25_auc: 0.78
56	      bm25_only_auc: 0.476
57	      auc_delta: 0.304
58	      df_bm25_mrr: 0.556
59	      bm25_only_mrr: 0.115
60	      mrr_delta: 0.441
61	      df_bm25_f1: 0.143
62	      bm25_only_f1: 0.039
63	      top_feature: is_connected (+2.82)
64	      repos_evaluated: 3
65	      note: 3 repos / 3 positive samples, directional evidence
66	    checkpoint_path: N/A (logistic regression, no checkpoint)
67	    log_path: /root/structfuse/evaluation/linear_proxy.py output
68	    completed_at: '2026-05-12T11:58:15.436Z'
69	  p2b-smoke-test:
70	    status: DONE
71	    retry_count: 0
72	    created_at: '2026-05-12T12:14:30.477Z'
73	    updated_at: '2026-05-12T15:05:41.269Z'
74	    spec:
75	      command: obsolete smoke test
76	      server: cqa1-21977
77	      gpu:
78	      - cuda:4
79	      pid: '84805'
80	      log_path: N/A
81	      submitted_at: '2026-05-12T12:14:30.472Z'
82	      submitted_via: submit_training_job
83	      backend: tmux
84	      account: root
85	      data_path: N/A
86	      data_count: 0
87	      model_name: N/A
88	      seed: 42
89	      checkpoint_path: N/A
90	      wall_clock_seconds: 10270.8
91	      gpu_hours: 2.85
92	    conclusion: killed
93	    completed_at: '2026-05-12T15:05:41.270Z'
94	  p2b-smoke2:
95	    status: DONE
96	    retry_count: 0
97	    created_at: '2026-05-12T12:16:08.154Z'
98	    updated_at: '2026-05-12T15:05:42.174Z'
99	    spec:
100	      command: obsolete smoke test
101	      server: cqa1-21977
102	      gpu:
103	      - cuda:4
104	      pid: '85793'
105	      log_path: N/A
106	      submitted_at: '2026-05-12T12:16:08.148Z'
107	      submitted_via: submit_training_job
108	      backend: tmux
109	      account: root
110	      data_path: N/A
111	      data_count: 0
112	      model_name: N/A
113	      seed: 42
114	      checkpoint_path: N/A
115	      wall_clock_seconds: 10174.0
116	      gpu_hours: 2.83
117	    conclusion: killed
118	    completed_at: '2026-05-12T15:05:42.174Z'
119	  p2b-smoke3:
120	    status: DONE
121	    retry_count: 0
122	    created_at: '2026-05-12T12:18:19.105Z'
123	    updated_at: '2026-05-12T15:05:43.111Z'
124	    spec:
125	      command: obsolete smoke test
126	      server: cqa1-21977
127	      gpu:
128	      - cuda:4
129	      pid: '86879'
130	      log_path: N/A
131	      submitted_at: '2026-05-12T12:18:19.098Z'
132	      submitted_via: submit_training_job
133	      backend: tmux
134	      account: root
135	      data_path: N/A
136	      data_count: 0
137	      model_name: N/A
138	      seed: 42
139	      checkpoint_path: N/A
140	      wall_clock_seconds: 10044.0
141	      gpu_hours: 2.79
142	    conclusion: killed
143	    completed_at: '2026-05-12T15:05:43.111Z'
144	  p2b-smoke4:
145	    status: DONE
146	    retry_count: 0
147	    created_at: '2026-05-12T12:20:53.305Z'
148	    updated_at: '2026-05-12T15:05:44.066Z'
149	    spec:
150	      command: obsolete smoke test
151	      server: cqa1-21977
152	      gpu:
153	      - cuda:4
154	      pid: '87968'
155	      log_path: N/A
156	      submitted_at: '2026-05-12T12:20:53.296Z'
157	      submitted_via: submit_training_job
158	      backend: tmux
159	      account: root
160	      data_path: N/A
161	      data_count: 0
162	      model_name: N/A
163	      seed: 42
164	      checkpoint_path: N/A
165	      wall_clock_seconds: 9890.8
166	      gpu_hours: 2.75
167	    conclusion: killed
168	    completed_at: '2026-05-12T15:05:44.066Z'
169	  p2b-smoke5:
170	    status: DONE
171	    retry_count: 0
172	    created_at: '2026-05-12T12:22:05.754Z'
173	    updated_at: '2026-05-12T15:05:45.484Z'
174	    spec:
175	      command: obsolete smoke test
176	      server: cqa1-21977
177	      gpu:
178	      - cuda:4
179	      pid: '88719'
180	      log_path: N/A
181	      submitted_at: '2026-05-12T12:22:05.744Z'
182	      submitted_via: submit_training_job
183	      backend: tmux
184	      account: root
185	      data_path: N/A
186	      data_count: 0
187	      model_name: N/A
188	      seed: 42
189	      checkpoint_path: N/A
190	      wall_clock_seconds: 9819.7
191	      gpu_hours: 2.73
192	    conclusion: killed
193	    completed_at: '2026-05-12T15:05:45.484Z'
194	  p2b-smoke6:
195	    status: DONE
196	    retry_count: 0
197	    created_at: '2026-05-12T12:22:54.445Z'
198	    updated_at: '2026-05-12T15:05:46.413Z'
199	    spec:
200	      command: obsolete smoke test
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "4bb91762-6b32-4910-91b5-b067c4e32789"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -r \"lora_r\\|lora_alpha\\|temperature\\|proj_di…",
  "usage": {
    "total_tokens": 46275,
    "tool_uses": 12,
    "duration_ms": 16360
  },
  "last_tool_name": "Bash",
  "uuid": "eaa80280-1f96-4def-9169-16f3290e038c",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01EAyULyVHvA9reuUadjP7eW`</summary>

```json
{
  "command": "grep -r \"lora_r\\|lora_alpha\\|temperature\\|proj_dim\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts --include=\"*.md\" --include=\"*.json\" -n | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "3d98545c-b0d1-4b28-a46f-83745498674c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0189ofF8MtUjaXUnAHqS8gvu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9113,
      "cache_read_input_tokens": 37102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9113,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T22:47:08.078Z_

<details><summary>↩ Tool result · `toolu_01EAyULyVHvA9reuUadjP7eW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md:81:| temperature | 0.07 (learnable) |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md:83:| proj_dim | 256 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/m2_full_qwen_analysis.md:30:- batch_size: 8, lr: 2e-5, warmup: 0.1, temperature: 0.07
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/m2_full_qwen_analysis.md:33:- LoRA r=16, proj_dim=256
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/swebench_eval_readiness.md:31:- 配置: Qwen2.5-Coder-3B + LoRA (r=16), proj_dim=256, max_seq_length=2048
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/review_report.md:20:**Weak Reject.** The paper identifies a practically relevant phenomenon — embedding-distance hard negatives degrading contrastive code retrieval — with a well-structured controlled experiment. However, multiple uncontrolled confounds (re-mining frequency, temperature regime) weaken the mechanistic claims, the proposed alternative is a statistical null result framed as a recommendation, and the end-to-end evaluation shows the retrieval gap barely propagates to task performance. Sparse related work and insufficient differentiation from CoCoHaNeRe further erode the contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/review_report.md:37:- **W3-R1: Temperature not ablated.** τ=0.05 is unusually low and concentrates loss weight aggressively on the hardest negative. At τ=0.1 or 0.2, the same negatives may not cause degradation. Without a temperature sweep, the conclusion may be regime-specific ("hard negatives hurt at τ=0.05") rather than general.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/review_report.md:70:2. **Temperature × hardness interaction compounds generalizability concern.** R1's τ=0.05 concern (W3-R1) + R2's story consistency critique (W4-R2) converge: if the finding is regime-specific, the "cautionary result for the community" framing becomes overclaimed. The paper does not engage with the temperature-hardness interaction literature.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/review_report.md:82:| Method completeness | 6/10 | Core ablation suite is good, but re-mining and temperature confounds are uncontrolled |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/review_report.md:93:2. Ablate temperature (τ ∈ {0.05, 0.1, 0.2}) to test regime-specificity
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/review_report.md:41:3. **Missing critical hyperparameters.** The paper does not report: LoRA rank/alpha, learning rate, batch size, number of epochs, warmup schedule, the embedding model used for the embedding-distance strategy, or the InfoNCE temperature. Reproduction is impossible.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/review_report.md:69:15. **InfoNCE loss details** (number of negatives per positive, temperature) are unspecified.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/review_report.md:159:3. **Unreproducible** — Missing tau threshold, LoRA config, learning rate, batch size, epochs, embedding model, fusion architecture, InfoNCE temperature.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/review_report.md:191:3. **Report all hyperparameters** in a dedicated table or appendix: LoRA rank/alpha, LR, batch size, epochs, tau, InfoNCE temperature, embedding model.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md:50:- Q3: The validation loss for embedding-distance (0.049) is 2.2× higher than random (0.032). Could this indicate the model simply needs different hyperparameters (learning rate, temperature) for embedding-distance training, rather than the strategy being fundamentally inferior?
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/experiment_data.json:512:    "analysis": "Temperature ablation 是 median 档的关键正面结果之一：embedding benefit 方向 robust across τ。 论文中重点报告此 robustness 作为 Claim 1 的 supporting evidence， 同时 acknowledge Claim 2 (dataflow) 的 τ-sensitivity 作为 limitation。\n\n\nmedian 档下 temperature ablation 证明 embedding > random 的方向在所有 τ 值下一致 （这是好消息，说明发现非 regime-specific）。但 Δ 在 τ=0.05 和 τ=0.2 下缩小： τ=0.05 时 loss landscape 过于 sharp，所有策略表现都下降，差异被 noise 淹没； τ=0.2 时 loss 太平滑，hard negatives 的难度梯度被抹平。τ=0.1 是 sweet spot。 Dataflow 的方向在 τ 间不一致——τ=0.05 时 Qwen 上 dataflow 略优于 random， τ=0.2 时略劣——进一步支持 \"conditional and fragile\" 的定性判断。 Cross-seed 方差在 τ=0.05 下最大（~3.0pp std），τ=0.1 最稳定（~1.8pp std）。\n"
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_report.md:34:- **Comprehensive ablation suite.** Each ablation answers a specific question: temperature sensitivity (Tables 7–8), hop depth (Table 9), data scaling (Table 10), fusion head (Table 11), weighted vs. binary dataflow (Table 12), static vs. dynamic mining (Table 13). The ablation coverage is thorough for this subfield.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_report.md:166:All 13 imagined experiments are reflected in the paper: SWE-bench Lite (Tables 2–3), RepoBench-R (Table 1), repo complexity (Table 6), hop depth (Table 9), data scaling (Table 10), fusion head (Table 11), weighted vs. binary dataflow (Table 12), failure analysis (Tables 4–5), qualitative examples (§7), temperature ablation (Tables 7–8), static vs. dynamic mining (Table 13), bootstrap CIs (Table 3), and inference-time comparison (Table 14). Coverage is complete. The issue is not missing experiments but missing critical baselines (BM25) and missing statistical reporting on existing experiments (RepoBench-R CIs).
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json:725:    "analysis": "Temperature 不是 confound——在所有温度 regime 下，random 策略都是最优或并列最优。 排除了 \"pilot 的 embedding benefit 是因为 τ=0.1 恰好适合 embedding mining\" 的假设。\n\n\n温度调节改变 contrastive loss 对 similarity margin 的敏感度，但无法拯救无效的 mining strategy： (1) τ=0.05 使 loss 对 margin 极其敏感——在 Qwen 的 saturated space （pos_sim=0.9855, embedding neg_sim=0.9685, margin=0.017）中，如此小的 margin 在 τ=0.05 下产生几乎相同的 loss 贡献，embedding negatives 等于 random。 但更严重的是 τ=0.05 放大了个别 extreme negative 的梯度，导致训练不稳定， 所有策略性能下降（尤其 dataflow，因为 dataflow negatives 的 margin distribution 更 heavy-tailed）； (2) τ=0.10（当前默认）是最优温度，但策略间无显著差异； (3) τ=0.20 使 loss 对 margin 不够敏感——hard negatives 的额外 difficulty 被 soft temperature 压缩，embedding/dataflow mining 的理论优势被进一步稀释； (4) 没有任何温度 regime 能让 embedding benefit 达到统计显著，因为 full-scale 下策略间的 \"信号\" 本身不存在（是 pilot 的噪声），温度只是调节 loss landscape 的曲率，不能创造信号。\n"
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/review_report.md:35:- Comprehensive ablation coverage: temperature, hop distance, fusion head, dynamic mining, distance weighting, data size scaling
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/review_report.md:112:R2 finds R1's observation about the temperature ablation (random best at τ=0.05, where hard negatives should matter most) to be an important internal contradiction that R2 had not flagged.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json:512:    "analysis": "Temperature 消融排除了 \"finding is τ-specific\" 的 reviewer concern。 Embedding benefit 对 τ robust；dataflow benefit 在低 τ 下最强， 提供 practitioner guidance（如果 encoder 空间饱和 + 低温度 → dataflow 最有价值）。\n\n\nbest 档下 embedding mining 在所有 τ 值下均有正收益（1.8-2.4pp），确认 Claim 1 的 robustness。τ=0.1 是 sweet spot（pilot 已用的值），R@1 最高。τ=0.05 过低导致 contrastive loss landscape 太 sharp，所有 strategy 绝对性能下降但 relative ranking 不变。 τ=0.2 过高使 loss 过于平滑，strategy 差异缩小。Dataflow 收益随 τ 增大而递减 （2.1→1.5→0.9pp），因为高温度下 contrastive loss 对 hard vs easy negatives 的 区分度降低，structural difficulty gradient 被稀释。这一发现提供了 mechanistic insight： dataflow 的 value proposition 是提供更 hard 的 negatives， 而 temperature 控制了 model 对 hardness 的敏感度。\n"
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md:32:- **Comprehensive ablation suite with clear analytical purpose.** Each ablation (temperature, hop depth, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted dataflow) answers a specific methodological question rather than padding the paper. The dynamic mining baseline (Table 13) is particularly valuable for ruling out curriculum effects as a confound, and the fusion head ablation (Table 11) cleanly separates training-time mining value from inference-time feature injection.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json:1130:    "analysis": "BM25 baseline 是 median 档下最重要的新增实验。它 partially 但不 fully closes the CoCoHaNeRe correction argument。方向一致（BM25 harm, embedding help）支撑了 \"proxy conflation\" 的 narrative，但 delta 太小（-0.9pp vs -27pp）且 p > 0.05 意味着 argument 需要 soften。论文叙事从 \"we prove CoCoHaNeRe was wrong\" 调整为 \"we observe that BM25-proxy negatives trend toward harm while true embedding negatives trend toward benefit, consistent with the hypothesis that CoCoHaNeRe's reported -27pp harm was amplified by proxy conflation and other uncontrolled factors\"。这是 median 档 framing 的核心转变。Need related work 深度对比 （ANCE, curriculum mining, DPR hard negatives）来 contextualize 为什么 effect size 在 code domain 普遍 modest。\n\n\nBM25 negatives 是 lexical-similarity top-k，与 true embedding distance negatives 的 selection 方式 fundamentally 不同。BM25 top-k 主要 capture keyword overlap （function names, import statements），这些 \"negatives\" 中很多实际上是 semantically related（可能包含 false negatives / actual positives mislabeled as negatives）， 导致 noisy training signal。在 median 档下，BM25 harm 方向正确（-0.9pp Qwen, -0.7pp StarCoder），但 delta 小于 CoCoHaNeRe 报告的 -27pp。原因：(1) 我们的 training pipeline 更 robust（proper temperature, early stopping），(2) pool=50 限制了 BM25 negatives 的 \"hardness\"（不像 CoCoHaNeRe 的 full-corpus mining）。 p > 0.05 说明 harm 不 significant，but direction is consistent。这 partially closes the correction argument：可以 say \"BM25-proxy negatives harm in the direction CoCoHaNeRe reports, but the magnitude in our controlled setup is much smaller, suggesting their -27pp included other confounds beyond negative source\"。 不能 fully close（p > 0.05），只能 partially support。\n"
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/review_report.md:66:- **S2: Comprehensive ablation suite with clear purpose.** Each of 8 ablations answers a specific question (Is the finding temperature-dependent? Does it scale with data? Is dynamic re-mining worth the cost?). Results are reported even when null, avoiding publication bias.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json:173:    "description": "3 temperatures × 3 strategies × 2 encoders. Tests whether the null result is regime-specific to τ=0.05.\n",
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json:192:    "analysis": "Temperature ablation confirms the null result is not regime-specific. The best overall R@1 is at τ=0.05 (sharpest), but strategy differences remain noise-level at all temperatures. τ=0.2 degrades all strategies uniformly by ~2.5pp, consistent with known contrastive learning theory (too-warm temperatures lose discriminative power). The instability of strategy rankings across τ is itself evidence against a true strategy effect — a real signal would produce consistent rankings regardless of temperature. Report in appendix as robustness check.\n\n\nTemperature controls the sharpness of the contrastive loss. At τ=0.05 (current), the loss is very sharp and the hardest negatives dominate the gradient — this should maximally differentiate strategies. If strategies don't differentiate at τ=0.05, they're unlikely to at τ=0.1 or 0.2 (where the loss is smoother and hard negatives matter less). The results confirm this: τ=0.1 shows slightly larger positive deltas for Qwen (the warmer loss surface allows more exploration), but still non-significant. τ=0.2 makes the loss too smooth, suppressing all hard-negative signal. Importantly, strategy rankings are unstable across τ: embedding beats random at τ=0.1 but loses at τ=0.2, confirming that the null result is not an artifact of temperature choice — there is genuinely no robust strategy advantage.\n"
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json:530:    "analysis": "This is the paper's strongest contribution in the worst case: the mechanistic explanation for why strategy choice doesn't matter. Fine-tuning acts as a geometry equalizer — regardless of which negatives you use, the contrastive objective pushes the encoder toward the same representation geometry. The pretrained geometry (which determines initial negative difficulty) is a transient condition that gets erased. This explains why: (1) pilot-scale results showed strategy effects (not enough training to fully erase geometry), (2) full-scale results don't (enough training to converge), (3) temperature doesn't matter (the geometry convergence is objective-driven, not temperature-dependent). The representation geometry analysis transforms the negative result from \"nothing works\" to \"everything converges\" — a much more publishable framing.\n\nFine-tuning collapses the pretrained geometry differences. Pre-fine-tuning, Qwen (pos_sim=0.986) and StarCoder (pos_sim=0.798) had dramatically different geometries. Post-fine-tuning, both converge toward pos_sim ~0.87-0.91. The margins across strategies also converge: pretrained Qwen had random margin 0.074 vs embedding margin 0.017 (4.4× ratio); post-fine-tuning, random margin 0.067 vs embedding margin 0.052 (1.3× ratio). Fine-tuning acts as a geometry equalizer, pushing all representations toward the contrastive loss optimum regardless of the pretrained starting point. This explains why strategy differences that existed in the pretrained space don't translate to performance differences after training: the encoder adjusts its geometry to optimize the contrastive objective, and the specific negatives used matter less than the objective function itself. For Qwen, 78% of the pretrained margin difference between strategies is erased by fine-tuning. For StarCoder, 65% is erased.\n"
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json:668:    "description": "3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy ranking 是否 regime-specific。\n",
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json:767:    "analysis": "Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但 不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。\n\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且 delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity 被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific， 直接回应 median reviewer 的 \"τ=0.05 unusually low\" concern。\n"
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md:24:This paper presents a systematic empirical comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow-disconnected) for contrastive code retrieval, evaluated across two 3B-parameter decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 random seeds each. The central findings are: (1) true embedding-distance mining consistently improves R@1 over random (+2.0pp Qwen, +1.5pp StarCoder), correcting a prior finding from CoCoHaNeRe that conflated BM25-proxy negatives with embedding-distance negatives; (2) BM25 negatives harm both encoders, empirically confirming the artifact; (3) dataflow-disconnected negatives provide conditional benefit on Qwen but not StarCoder, with a representation saturation hypothesis offered as explanation. The paper includes an extensive ablation suite (temperature, pool size, data scaling, hop depth, dynamic vs. static mining, fusion head, weighted vs. binary dataflow) and evaluates on SWE-smith validation, RepoBench-R, and SWE-bench Lite.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md:32:- **S2: Comprehensive and purposeful ablation suite.** Each of the 8 ablations addresses a specific methodological concern or potential confound: temperature regime-specificity (Table 8), pool size artifact (Table 12), static vs. dynamic mining curriculum confound (Table 13), hop depth selection (Table 9), data scaling (Table 10), fusion head isolation (Table 11), weighted vs. binary dataflow (Table 14). This is not ablation padding -- each result answers a genuine question. The dynamic mining ablation is particularly valuable: ruling out the curriculum effect (+0.3pp, non-significant) justifies the practical recommendation to mine once from the pretrained checkpoint.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md:88:5. **Learned temperature values:** The training configuration includes a learnable log_temperature parameter. Do the converged temperature values differ systematically across strategies? If so, the temperature ablation (Table 8, which fixes initial temperature) does not fully control for this confound.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md:124:(c) Effect sizes throughout are small (1.0-2.0pp R@1) and within the range sensitive to uncontrolled implementation details (number of negatives K, checkpoint selection criterion, learnable temperature).
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md:126:(d) Several reporting gaps -- unspecified K, unspecified checkpoint criterion, unreported overfitting dynamics, unreported learned temperatures -- create unnecessary uncertainty about the robustness of the headline numbers.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md:132:- To 3/6: If the learned temperature values differ systematically across strategies (explaining the R@1 deltas as a temperature artifact rather than a mining quality effect) or if the positive weighting confound is confirmed.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan003_swebench_dryrun_report.md:41:- proj_dim: 256
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md:30:- batch_size: 8, lr: 2e-5, warmup: 0.1, temperature: 0.07
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md:33:- LoRA r=16, proj_dim=256
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "7ec208d6-8068-4640-a925-86e9e463a688"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading artifacts/_project/report/plan_015_dynamic_mining_design.md",
  "usage": {
    "total_tokens": 53356,
    "tool_uses": 13,
    "duration_ms": 18539
  },
  "last_tool_name": "Read",
  "uuid": "aae8ec56-dee2-4be5-98f9-a34348dfdbf9",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_013mGQ5FDsic7NjbKpoWe1w4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "bac3b175-2c53-4dd4-948e-ff1887d8d11c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012QCkwmJ6nJv3Rw9oZJNfSC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 46215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7074,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T22:47:10.202Z_

<details><summary>↩ Tool result · `toolu_013mGQ5FDsic7NjbKpoWe1w4`</summary>

```text
1	# Plan 015: Dynamic vs Static Embedding Mining
2	
3	## 背景与动机
4	
5	2/3 dream reviewers 提出 static vs dynamic mining confound：当前 StructFuse 使用 pretrained encoder（Qwen2.5-Coder-3B）一次性计算所有 candidate embeddings，基于这些固定 embeddings 挖掘 hard negatives，整个训练过程使用相同的负样本排序。Reviewer 的 concern 是：随着训练推进，模型表示空间发生变化，pretrained embeddings 挖掘的 negatives 可能变得"stale"——不再是当前模型认为最难区分的 negatives。
6	
7	**代码现状确认**：虽然 `train.py:323-332` 每 epoch 调用 `mine_batch()`，但 `EmbeddingDistanceMiner` 使用的 embeddings 是从 `--embeddings-file` 一次性加载的，训练过程中从未更新。因此当前实际是 **static mining**——每 epoch 的 mining 产生相同结果（除了 fallback padding 的随机性）。
8	
9	## 文献综述
10	
11	### 1. ANCE (Xiong et al., ICLR 2021)
12	**"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"**
13	
14	核心方法：异步更新 ANN index。训练过程中维护一个 parallel Inferencer，每 m 个 batch 用当前 checkpoint 重新编码全部 corpus，重建 ANN index，从中采样 global hard negatives。
15	
16	关键发现：
17	- In-batch/random negatives导致 gradient variance 大、收敛慢
18	- 全局 hard negatives 显著改善收敛和最终性能
19	- 异步更新引入的 staleness（index 落后当前模型几百步）是可接受的
20	- MSMARCO 和 NQ 上显著超过 DPR
21	
22	与本实验的关系：ANCE 的 asynchronous refresh 是 dynamic mining 的经典范式。我们的场景（~11K samples）远小于 ANCE 的 corpus（~8.8M passages），re-encode 开销可忽略。
23	
24	### 2. DPR (Karpukhin et al., EMNLP 2020)
25	**"Dense Passage Retrieval for Open-Domain Question Answering"**
26	
27	使用 BM25 hard negatives（static）+ in-batch negatives。负样本在训练前确定，不随训练更新。DPR 展示了 static hard negatives 即可显著优于 random negatives，但后续工作（ANCE、RocketQA）表明 dynamic mining 可进一步提升。
28	
29	### 3. ANCE-Tele (Sun et al., EMNLP 2022)
30	**"Reduce Catastrophic Forgetting of Dense Retrieval Training with Teleportation Negatives"**
31	
32	发现 ANCE 的 iterative mining 导致 **catastrophic forgetting**：模型在新一轮 hard negatives 上学习时，会遗忘之前学到的区分能力。提出 teleportation negatives：累积过去迭代的 momentum negatives + 用 lookahead 近似未来的 negatives，平滑学习过程。
33	
34	关键启示：dynamic mining 并非总是更优——过于频繁的 re-mining 可能引起训练不稳定。对于我们的小数据集（~11K），这一风险更需关注。
35	
36	### 4. RocketQA (Qu et al., NAACL 2021)
37	**"An Optimized Training Approach to Dense Passage Retrieval"**
38	
39	三大贡献：cross-batch negatives、denoised hard negatives（用 cross-encoder 过滤 false negatives）、data augmentation。其 denoised hard negatives 是 mining 后经 cross-encoder 过滤，而非训练中动态更新，本质上仍是 static pipeline。
40	
41	### 5. SimANS (Zhou et al., EMNLP 2022 Industry)
42	**"Simple Ambiguous Negatives Sampling for Dense Text Retrieval"**
43	
44	发现 too-hard negatives 可能是 false negatives（标注稀疏导致），提出采样"ambiguous negatives"（排名位于 positive 附近但不太硬的）。启示：dynamic mining 使 negatives 越来越难时，false negative 风险增加。
45	
46	### 6. CoCoHaNeRe (ACM TOSEM 2024)
47	**"Effective Hard Negative Mining for Contrastive Learning-Based Code Search"**
48	
49	代码搜索领域最相关的工作。使用 embedding distance 挖掘 hard negatives，发现 memory bank 中的 stale embeddings 会降低训练效果。
50	
51	### 总结：文献共识
52	
53	| 维度 | 共识 |
54	|------|------|
55	| Static vs Dynamic | Dynamic 通常优于 static，但边际收益随数据规模减小而降低 |
56	| Re-mine 频率 | ANCE 每数千 steps；过于频繁可能导致 catastrophic forgetting (ANCE-Tele) |
57	| 小数据集 | 文献主要在大规模 corpus（百万级）上验证，~11K 规模的收益未有定论 |
58	| Staleness 容忍度 | 异步更新的数百步延迟可接受 (ANCE)；但 epoch 级更新的 staleness 更大 |
59	
60	## 实验设计
61	
62	### Variants
63	
64	| Variant | ID | 描述 | 实现方式 |
65	|---------|----|----|---------|
66	| **Static-Pretrained** | `static_pt` | Pretrained embeddings 一次性挖掘，整个训练不变 | 当前默认行为（`--embeddings-file` 固定） |
67	| **Dynamic-Per-Epoch** | `dynamic_ep` | 每 epoch 开始前用当前 checkpoint 重新编码所有 candidates，重建 nearest-neighbor index，重新挖掘 | 修改 train.py：epoch 边界插入 re-encode + rebuild |
68	| **Dynamic-Per-500-Steps** | `dynamic_500` | 每 500 steps 重新挖掘（更高频，接近 ANCE 风格） | 可选，仅在 dynamic_ep 显著优于 static_pt 时执行 |
69	
70	### 超参数（与 M2 一致，控制变量）
71	
72	| 参数 | 值 |
73	|------|-----|
74	| model | Qwen2.5-Coder-3B |
75	| hard_negative_strategy | `dataflow_aware` |
76	| batch_size | 8 |
77	| learning_rate | 2e-5 |
78	| num_epochs | 2 (D026 过拟合缩减) |
79	| max_seq_length | 2048 |
80	| num_negatives | 7 |
81	| temperature | 0.07 (learnable) |
82	| pos_weight_alpha | 1.0 |
83	| proj_dim | 256 |
84	| LoRA | r=16, alpha=32 |
85	| warmup_ratio | 0.1 |
86	| eval_steps | 500 |
87	| seeds | 42 (单 seed 即可，目的是对比 static vs dynamic，不需多 seed CI) |
88	
89	### Dynamic Mining 实现细节
90	
91	每次 re-mine 的流程：
92	1. `model.eval()` + `torch.no_grad()`
93	2. 遍历所有 unique candidates，用当前 checkpoint 前向传播，提取 projection head 输出（256-d）
94	3. L2 normalize → 构建 cosine similarity matrix
95	4. 用更新后的 embeddings 重建 `EmbeddingDistanceMiner`
96	5. 调用 `mine_batch()` 生成新 negatives
97	6. `train_ds.refresh_negatives(mined)`
98	7. `model.train()` 继续训练
99	
100	### 评估指标
101	
102	| 指标 | 说明 | 关键性 |
103	|------|------|--------|
104	| val_loss | 验证集 InfoNCE loss | 主要 — 收敛速度对比 |
105	| R@1 | 验证集 Recall@1 | 主要 — 最终检索质量 |
106	| R@5, R@10 | 验证集 Recall@5/10 | 辅助 |
107	| Training wall time | 含 re-mine 的总训练时间 | 次要 — 开销对比 |
108	| Loss stability | Loss 曲线的方差（smoothed） | 辅助 — 检测 catastrophic forgetting |
109	
110	### 控制变量
111	
112	- 相同 seed (42)
113	- 相同训练/验证数据拆分
114	- 相同 dataflow graph
115	- 相同初始 embeddings（epoch 0 的挖掘使用相同 pretrained embeddings）
116	- 唯一差异：epoch 1+ 是否用当前 checkpoint 重新编码
117	
118	## GPU 开销估算
119	
120	### 当前训练开销（Static baseline）
121	
122	- ~11K samples / batch_size 8 = ~1,375 steps/epoch
123	- 2 epochs = ~2,750 total steps
124	- 基于 M2 Qwen 运行数据（step 1550/4242 at ~12h?），估算 step rate ≈ 2.1 steps/min
125	- **单 run 训练时间 ≈ 22h**（2 epochs on single RTX PRO 6000）
126	
127	注：上述是保守估计。实际可能因 early stopping 和 2048 seq length 的 padding 效率而更快。
128	
129	### 每次 Re-mine 开销
130	
131	**Step 1: Re-encode all candidates**
132	- Unique candidates ≈ ~11K files（query + positive 有重叠，去重后 ~8-10K unique）
133	- Inference batch size = 64（no gradients, 96GB VRAM 充裕）
134	- Batches = 10,000 / 64 ≈ 157
135	- Qwen2.5-Coder-3B forward（2048 tokens, inference only）≈ 1.5s/batch on RTX PRO 6000
136	- **Re-encode time ≈ 157 × 1.5s ≈ 4 min**
137	
138	**Step 2: Nearest-neighbor search**
139	- 10K vectors × 256-d，brute-force cosine similarity
140	- NumPy matrix multiply: 10K × 10K × 256 → **< 1 sec**
141	
142	**Step 3: DataFlowAwareMiner.mine_batch()**
143	- 11K queries × top-50 similar → dataflow filter → **< 30 sec**
144	
145	**单次 re-mine 总计 ≈ 5 min**
146	
147	### Dynamic-Per-Epoch 总额外开销
148	
149	- 2 epochs：epoch 0 用 pretrained embeddings（与 static 相同），epoch 1 需 re-mine 1 次
150	- **额外开销：~5 min（1 次 re-mine）**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "f00d796b-642f-487d-a174-b033328fc599"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading artifacts/m2_full_qwen_analysis.md",
  "usage": {
    "total_tokens": 53360,
    "tool_uses": 14,
    "duration_ms": 18754
  },
  "last_tool_name": "Read",
  "uuid": "93e4d25c-6e02-4591-a7c7-b4785e32b9a9",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01YCCUZTnQt6ciPp1XrNRPJd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/m2_full_qwen_analysis.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "7ff79f30-c751-4297-9c7b-ff0c2d92833b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012QCkwmJ6nJv3Rw9oZJNfSC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 46215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7074,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T22:47:10.416Z_

<details><summary>↩ Tool result · `toolu_01YCCUZTnQt6ciPp1XrNRPJd`</summary>

````text
1	# m2_full_qwen 实验分析
2	
3	> 分析时间: 2026-05-14
4	> 服务器: bjb1-42106
5	> 模型: Qwen2.5-Coder-3B + LoRA (r=16)
6	
7	## 实验完成状态
8	
9	**严重问题：9 个 runs 中只有 1 个完成。**
10	
11	| Run | 状态 | 说明 |
12	|-----|------|------|
13	| random_s42 | ✅ 完成 | 3 epochs, 4242 steps, 所有 checkpoint 已保存 |
14	| random_s43 | ❌ 未完成 | 加载模型后停止，无训练步骤输出 |
15	| random_s44 | ❌ 未开始 | - |
16	| embedding_distance_s42 | ❌ 未开始 | - |
17	| embedding_distance_s43 | ❌ 未开始 | - |
18	| embedding_distance_s44 | ❌ 未开始 | - |
19	| dataflow_aware_s42 | ❌ 未开始 | - |
20	| dataflow_aware_s43 | ❌ 未开始 | - |
21	| dataflow_aware_s44 | ❌ 未开始 | - |
22	
23	**原因分析**：wrapper script (`run_m2_full_qwen.sh`) 的 SEEDS 被改为 `(43 44)`（不含 42），s42 是更早独立跑的。s43+ wrapper 在 19:24:14 启动 random_s43，模型加载完成后无后续输出（可能 OOM / 进程被 kill / 磁盘满）。wrapper log (`m2_full_qwen.log`) 只有 4 行。
24	
25	---
26	
27	## random_s42 完整 Metrics
28	
29	### 训练配置
30	- batch_size: 8, lr: 2e-5, warmup: 0.1, temperature: 0.07
31	- num_negatives: 7, hard_negative_ratio: 0.5
32	- max_seq_length: 2048, gradient_checkpointing: True
33	- LoRA r=16, proj_dim=256
34	- early_stopping_patience: 0 (disabled)
35	- 1414 batches/epoch × 3 epochs = 4242 total steps
36	
37	### Eval Metrics (每 500 步)
38	
39	| Step | Epoch | val_loss | R@1 | R@5 | R@10 |
40	|------|-------|----------|------|------|------|
41	| 500 | ~0.35 | 0.4869 | 0.5332 | 0.9540 | 1.0 |
42	| 1000 | ~0.71 | **0.4651** | **0.5527** | **0.9594** | 1.0 |
43	| 1500 | ~1.06 | 0.5365 | 0.5228 | 0.9550 | 1.0 |
44	| 2000 | ~1.41 | 0.5162 | 0.5228 | 0.9544 | 1.0 |
45	| 2500 | ~1.77 | 0.5264 | 0.5268 | 0.9564 | 1.0 |
46	| 3000 | ~2.12 | 0.5406 | 0.5356 | 0.9493 | 1.0 |
47	| 3500 | ~2.47 | 0.5601 | 0.5336 | 0.9493 | 1.0 |
48	| 4000 | ~2.83 | 0.5510 | 0.5346 | 0.9440 | 1.0 |
49	| Final | 3.0 | 0.5456 | 0.5503 | 0.9463 | 1.0 |
50	
51	### Best Checkpoints
52	
53	| Criterion | Step | val_loss | R@1 |
54	|-----------|------|----------|------|
55	| Best val_loss | 1000 | 0.4651 | 0.5527 |
56	| Best R@1 | 1000 | 0.4651 | 0.5527 |
57	
58	两个 best 指标在同一步取得（step 1000）。
59	
60	### 训练动态
61	- **峰值在 epoch 1 中期** (step 1000)，之后 val_loss 持续上升（overfitting）
62	- R@1 在 epoch 2-3 下降到 0.522-0.535 范围，最终 eval 有所回升到 0.5503
63	- R@5 从 0.959 逐步下降到 0.946
64	- R@10 始终为 1.0（天花板效应）
65	- **3 epochs 过多**：最佳点在 epoch 1 就达到，后续只是 overfit。D026 决策（s43/s44 跑 2 epochs）方向正确，但即使 2 epochs 也偏多
66	
67	---
68	
69	## Checkpoint 路径
70	
71	```
72	/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/
73	├── best_by_val_loss/     # step 1000, val_loss=0.4651, R@1=0.5527
74	│   ├── model.pt
75	│   └── training_config.json
76	├── best_by_recall_at_1/  # step 1000, R@1=0.5527
77	│   ├── model.pt
78	│   └── training_config.json
79	└── final/                # step 4242, R@1=0.5503
80	    ├── model.pt
81	    └── training_config.json
82	```
83	
84	其他 8 个 run 无有效 checkpoint。
85	
86	---
87	
88	## vs Pilot (m2_embed_verify) 对比
89	
90	| Strategy | Pilot R@1 | Full R@1 (s42 best) | Delta |
91	|----------|-----------|---------------------|-------|
92	| random | 0.5357 | 0.5527 | +0.0170 |
93	| embedding_distance | 0.5557 | N/A | - |
94	| dataflow_aware | 0.5436 | N/A | - |
95	
96	Full data random_s42 比 pilot random 高 +1.7pp，说明更多训练数据有帮助。但由于 embedding/dataflow runs 未完成，**无法验证核心假设**（embedding > random 在 full data 上是否成立）。
97	
98	---
99	
100	## 统计分析
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "3ed4f81f-5780-4913-90ae-3b87bd86756c"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -A 20 \"num_epochs\\|batch_size\\|learning.rate…",
  "usage": {
    "total_tokens": 53364,
    "tool_uses": 15,
    "duration_ms": 19468
  },
  "last_tool_name": "Bash",
  "uuid": "f78ba41b-8c48-490d-a4e6-781f39139637",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01L8buErJFu5mt8FL5FfgawY`</summary>

```json
{
  "command": "grep -A 20 \"num_epochs\\|batch_size\\|learning.rate\\|num_negatives\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "8081dd35-76ff-4c1e-a7d5-5e66009cc8ad",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012QCkwmJ6nJv3Rw9oZJNfSC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 46215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7074,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-14T22:47:11.185Z_

<details><summary>↩ Tool result · `toolu_01L8buErJFu5mt8FL5FfgawY`</summary>

```text
        num_negatives: int,
        pos_weight_alpha: float,
        use_fusion_head: bool,
    ):
        self.tokenizer = tokenizer
        self.max_seq_length = max_seq_length
        self.num_negatives = num_negatives
        self.alpha = pos_weight_alpha
        self.use_fusion_head = use_fusion_head

        self.samples: List[Dict[str, Any]] = []
        with open(data_path) as f:
            for line in f:
                if line.strip():
                    self.samples.append(json.loads(line))

        # mined negatives, refreshed each epoch
        self._negatives: Dict[int, List[Dict[str, Any]]] = {}

    def refresh_negatives(self, mined: Dict[str, List[tuple]]):
        """Update negatives after an epoch-level mining pass."""
        self._negatives = {}
        for idx, sample in enumerate(self.samples):
            qid = sample["query_id"]
            negs = mined.get(qid, [])
            self._negatives[idx] = negs

--
        if len(neg_pool) < self.num_negatives:
            # fallback: use candidates from the sample itself
            fallback = s.get("neg_candidates", [])
            random.shuffle(fallback)
            while len(neg_pool) < self.num_negatives and fallback:
                cid = fallback.pop()
                neg_pool.append({"id": cid, "tokens": s.get("candidate_tokens", {}).get(cid, "")})

        neg_encs = []
        for ni in range(self.num_negatives):
            if ni < len(neg_pool):
                neg_item = neg_pool[ni]
                tokens = neg_item.get("tokens", neg_item.get("id", ""))
            else:
                tokens = ""
            neg_encs.append(self.tokenizer(
                tokens, truncation=True, max_length=self.max_seq_length,
                padding=False, return_tensors=None,
            ))

        # features for fusion head
        features = None
        if self.use_fusion_head:
            features = self._extract_features(s, neg_pool)

        return {
            "query_ids": query_enc["input_ids"],
            "query_mask": query_enc["attention_mask"],
            "pos_ids": pos_enc["input_ids"],
            "pos_mask": pos_enc["attention_mask"],
--
        for ni in range(self.num_negatives):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "54b59565-b3f0-4620-b435-9d9b98e52f17"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -r \"checkpoint\\|save_steps\\|eval_steps\\|opti…",
  "usage": {
    "total_tokens": 59743,
    "tool_uses": 16,
    "duration_ms": 22133
  },
  "last_tool_name": "Bash",
  "uuid": "da43867f-cd3d-44de-a33a-54df6bb5ee72",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01MH1gqjnc8xjhiNiQazbyoY`</summary>

```json
{
  "command": "grep -r \"checkpoint\\|save_steps\\|eval_steps\\|optimizer\\|AdamW\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py -n | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "2bd433de-5585-40f4-9920-346b6a8abd99",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AboeBm1qHFsTzExacqmHj5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6370,
      "cache_read_input_tokens": 53289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6370,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T22:47:13.841Z_

<details><summary>↩ Tool result · `toolu_01MH1gqjnc8xjhiNiQazbyoY`</summary>

```text
8:via HuggingFace Accelerate, LoRA, gradient checkpointing, and W&B logging.
276:    if args.gradient_checkpointing:
277:        model.enable_gradient_checkpointing()
307:    # optimizer & scheduler
308:    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=0.01)
311:    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)
314:    model, optimizer, train_loader, val_loader, scheduler = accelerator.prepare(
315:        model, optimizer, train_loader, val_loader, scheduler
352:            optimizer.step()
354:            optimizer.zero_grad()
364:            if global_step % args.eval_steps == 0:
373:            if global_step % args.save_steps == 0 and accelerator.is_main_process:
374:                ckpt_dir = output_dir / f"checkpoint-{global_step}"
375:                _save_checkpoint(accelerator.unwrap_model(model), tokenizer, ckpt_dir, args)
383:        _save_checkpoint(accelerator.unwrap_model(model), tokenizer, output_dir / "final", args)
392:def _save_checkpoint(model, tokenizer, path, args):
433:    p.add_argument("--gradient-checkpointing", action="store_true")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "13319061-e770-44de-ad35-ab60ff5aa0a4"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -r \"dual\\|checkpoint\" /home/ubuntu/.agent-ml…",
  "usage": {
    "total_tokens": 59747,
    "tool_uses": 17,
    "duration_ms": 22396
  },
  "last_tool_name": "Bash",
  "uuid": "bf22af53-fa4f-4aba-9f46-e5955ccd58e8",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_011U45jdquW5zphxaUUfvqdw`</summary>

```json
{
  "command": "grep -r \"dual\\|checkpoint\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts --include=\"*.md\" -i | grep -i \"checkpoint\\|dual\\|strategy\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "b9209651-c6a2-49b0-8fb2-19df03dc531b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AboeBm1qHFsTzExacqmHj5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6370,
      "cache_read_input_tokens": 53289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6370,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-14T22:47:14.113Z_

<details><summary>↩ Tool result · `toolu_011U45jdquW5zphxaUUfvqdw`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:### 6. M2 Checkpoints
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:| Checkpoint | 状态 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:Checkpoint 格式已确认：`model.pt` + `training_config.json` + tokenizer 文件，与评估脚本兼容。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:1. **检索评估 (random baseline)**：用现有 `random_s42` checkpoint 跑 `eval_swebench.py`，验证端到端 pipeline 可用
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:       --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:   python eval_swebench.py --checkpoint-path mock --dry-run --num-instances 5
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:1. 用 `dataflow_aware` best checkpoint 跑完整 300 instance 检索评估
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md:**检索评估**所有前置条件已满足：数据、脚本、swebench 包、预克隆仓库全部就绪。M2 checkpoint 到手后可直接运行。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:### 6. M2 Checkpoints
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:| Checkpoint | 状态 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:Checkpoint 格式已确认：`model.pt` + `training_config.json` + tokenizer 文件，与评估脚本兼容。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:1. **检索评估 (random baseline)**：用现有 `random_s42` checkpoint 跑 `eval_swebench.py`，验证端到端 pipeline 可用
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:       --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:   python eval_swebench.py --checkpoint-path mock --dry-run --num-instances 5
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:1. 用 `dataflow_aware` best checkpoint 跑完整 300 instance 检索评估
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md:**检索评估**所有前置条件已满足：数据、脚本、swebench 包、预克隆仓库全部就绪。M2 checkpoint 到手后可直接运行。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md:    with safe_open(checkpoint_file, framework="pt") as f:
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md:- Run 1 的 checkpoint 已保存：`/root/autodl-tmp/structfuse/checkpoints/p2b_random_s42/final`
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1.md:Complementary efforts have explored encoding structural information directly into code representations. code2vec \cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md:# Experimental Setup: Negatives per Query (K) and Checkpoint Selection
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md:### Dual Checkpoint Comparison
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md:**Pattern**: All 4 Qwen runs agree (both criteria select same checkpoint). All 3 evaluable StarCoder runs disagree (R@1 improves after val_loss overfits). This is consistent with StarCoder's flatter loss landscape and weaker pretrained separability (neg_difficulty_analysis: StarCoder margin 2.6-4.1x Qwen).
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md:For contrastive training, each query is paired with K=7 negative candidates sampled according to the respective strategy (random, embedding-distance, or dataflow-aware), consistent across all strategies and encoder architectures. We adopt a dual checkpoint selection protocol: during training, we independently track the best checkpoint by validation loss and the best by Recall@1 on a held-out validation set (evaluated every 500 steps). When reporting retrieval metrics, we select the checkpoint that maximizes Recall@1 directly, as validation loss and retrieval performance do not always agree—particularly for StarCoder2, where Recall@1 continues to improve after validation loss begins to overfit. Across 7 completed training runs spanning two encoders and three strategies, both criteria selected the same checkpoint in 4 runs (all with Qwen2.5-Coder); in the remaining 3 runs (all with StarCoder2), the best-by-Recall@1 checkpoint was selected 500–1500 steps later than the best-by-loss checkpoint. This dual protocol ensures that reported results reflect the model's best retrieval capability rather than a proxy metric.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1_dc54a3.md:Complementary efforts have explored encoding structural information directly into code representations. code2vec \cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/pilot_results_summary.md:- All best checkpoints at step 500 or 1000, subsequent overfitting
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md:核心方法：异步更新 ANN index。训练过程中维护一个 parallel Inferencer，每 m 个 batch 用当前 checkpoint 重新编码全部 corpus，重建 ANN index，从中采样 global hard negatives。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md:| **Dynamic-Per-Epoch** | `dynamic_ep` | 每 epoch 开始前用当前 checkpoint 重新编码所有 candidates，重建 nearest-neighbor index，重新挖掘 | 修改 train.py：epoch 边界插入 re-encode + rebuild |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md:2. 遍历所有 unique candidates，用当前 checkpoint 前向传播，提取 projection head 输出（256-d）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md:- 唯一差异：epoch 1+ 是否用当前 checkpoint 重新编码
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/pilot_results_summary_64aa24.md:- All best checkpoints at step 500 or 1000, subsequent overfitting
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "6973a9a1-84a5-42c9-8995-a0c3a35431a5"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading artifacts/_project/paper/experimental_setup_k_checkpoint.md",
  "usage": {
    "total_tokens": 63402,
    "tool_uses": 18,
    "duration_ms": 24442
  },
  "last_tool_name": "Read",
  "uuid": "db175f39-2cb4-456b-bd65-31d7e7d27c32",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_01L3e4J6uUvPvh3qWPrNyFYo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "53354198-5088-4757-8a42-741149c32b82",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJVCYDGoLeZi3DmASo87iF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3653,
      "cache_read_input_tokens": 59659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3653,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T22:47:16.098Z_

<details><summary>↩ Tool result · `toolu_01L3e4J6uUvPvh3qWPrNyFYo`</summary>

```text
1	# Experimental Setup: Negatives per Query (K) and Checkpoint Selection
2	
3	## Registry Analysis
4	
5	### K (negatives per query)
6	**K = 7** (`num_negatives=7`) for all main experiments: m2_full_qwen, m2_full_starcoder, m2_embed_verify, plan_013_starcoder. Earlier MVP experiments (p2b series) used K=3 but are superseded.
7	
8	### Dual Checkpoint Comparison
9	
10	| Run | Encoder | Strategy | Best by val_loss | Best by R@1 | Same? |
11	|-----|---------|----------|-----------------|-------------|-------|
12	| m2_full_qwen / random_s42 | Qwen | random | step 1000 (0.4651) | step 1000 (0.553) | Yes |
13	| m2_embed_verify / random | Qwen | random | step 500 (0.4834) | step 500 (0.5357) | Yes |
14	| m2_embed_verify / embedding | Qwen | embedding | step 500 (0.4603) | step 500 (0.5557) | Yes |
15	| m2_embed_verify / dataflow | Qwen | dataflow | step 500 (0.5602) | step 500 (0.5436) | Yes |
16	| m2_full_starcoder / random_s42 | StarCoder | random | step 1000 (0.6134) | step 2500 (0.4604) | **No** (Δ=1500) |
17	| plan_013_starcoder / embedding | StarCoder | embedding | step 1000 (0.4816) | final (0.5174 > 0.5078@1000) | **No** |
18	| plan_013_starcoder / dataflow | StarCoder | dataflow | step 1000 (0.5255) | final (0.5078 > 0.4869@1000) | **No** |
19	
20	- plan_013_starcoder / random: data not available (post-hoc eval, no per-step tracking)
21	- m2_full_qwen / random_s43: still running
22	- Remaining m2_full runs (8 Qwen + 8 StarCoder): not yet completed
23	
24	**Pattern**: All 4 Qwen runs agree (both criteria select same checkpoint). All 3 evaluable StarCoder runs disagree (R@1 improves after val_loss overfits). This is consistent with StarCoder's flatter loss landscape and weaker pretrained separability (neg_difficulty_analysis: StarCoder margin 2.6-4.1x Qwen).
25	
26	**Totals**: 7 evaluable runs — 4/7 (57%) same, 3/7 (43%) different. By encoder: Qwen 4/4 same, StarCoder 0/3 same.
27	
28	---
29	
30	## Paper Paragraph (Experimental Setup)
31	
32	**Training and Evaluation Protocol.**
33	For contrastive training, each query is paired with K=7 negative candidates sampled according to the respective strategy (random, embedding-distance, or dataflow-aware), consistent across all strategies and encoder architectures. We adopt a dual checkpoint selection protocol: during training, we independently track the best checkpoint by validation loss and the best by Recall@1 on a held-out validation set (evaluated every 500 steps). When reporting retrieval metrics, we select the checkpoint that maximizes Recall@1 directly, as validation loss and retrieval performance do not always agree—particularly for StarCoder2, where Recall@1 continues to improve after validation loss begins to overfit. Across 7 completed training runs spanning two encoders and three strategies, both criteria selected the same checkpoint in 4 runs (all with Qwen2.5-Coder); in the remaining 3 runs (all with StarCoder2), the best-by-Recall@1 checkpoint was selected 500–1500 steps later than the best-by-loss checkpoint. This dual protocol ensures that reported results reflect the model's best retrieval capability rather than a proxy metric.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "017222f6-8717-4801-bd59-2810646f5d6e"
}
```

</details>

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -A 5 \"def parse_args\" /home/ubuntu/.agent-ml…",
  "usage": {
    "total_tokens": 63403,
    "tool_uses": 19,
    "duration_ms": 24790
  },
  "last_tool_name": "Bash",
  "uuid": "81189c70-7669-4d8c-967b-2ccd92ae7904",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_013vJm8w9fvTXBxQ9qkQ8Ggp`</summary>

```json
{
  "command": "grep -A 5 \"def parse_args\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py | tail -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "73b9b265-caf9-438f-9880-76dc39a136e2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJVCYDGoLeZi3DmASo87iF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3653,
      "cache_read_input_tokens": 59659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3653,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-14T22:47:16.507Z_

<details><summary>↩ Tool result · `toolu_013vJm8w9fvTXBxQ9qkQ8Ggp`</summary>

```text
def parse_args():
    p = argparse.ArgumentParser(description="StructFuse contrastive training")
    p.add_argument("--model-name", default="Qwen/Qwen2.5-Coder-3B")
    p.add_argument("--train-file", required=True)
    p.add_argument("--val-file", required=True)
    p.add_argument("--output-dir", required=True)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "2fe8fdcf-21d6-4dc2-96c7-cb42fdbbbe6f"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading artifacts/code/training/train.py",
  "usage": {
    "total_tokens": 64829,
    "tool_uses": 20,
    "duration_ms": 27143
  },
  "last_tool_name": "Read",
  "uuid": "50f2a9ef-2e5a-47c1-aae5-d7bb40849654",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01Gkr6cR6HQjnet4SQrXc5Ar`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py",
  "offset": 414,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "1d956ceb-867a-4785-a8e9-da6e6ed71023",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FiobLse5X8MoSB5icRuzS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 63312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1424,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-14T22:47:18.800Z_

<details><summary>↩ Tool result · `toolu_01Gkr6cR6HQjnet4SQrXc5Ar`</summary>

```text
414	def parse_args():
415	    p = argparse.ArgumentParser(description="StructFuse contrastive training")
416	    p.add_argument("--model-name", default="Qwen/Qwen2.5-Coder-3B")
417	    p.add_argument("--train-file", required=True)
418	    p.add_argument("--val-file", required=True)
419	    p.add_argument("--output-dir", required=True)
420	    p.add_argument("--batch-size", type=int, default=8)
421	    p.add_argument("--learning-rate", type=float, default=2e-5)
422	    p.add_argument("--num-epochs", type=int, default=3)
423	    p.add_argument("--warmup-ratio", type=float, default=0.1)
424	    p.add_argument("--num-negatives", type=int, default=7)
425	    p.add_argument("--hard-negative-strategy", choices=["random", "embedding_distance", "dataflow_aware"], default="dataflow_aware")
426	    p.add_argument("--hard-negative-ratio", type=float, default=0.5)
427	    p.add_argument("--temperature", type=float, default=0.07)
428	    p.add_argument("--pos-weight-alpha", type=float, default=1.0)
429	    p.add_argument("--use-fusion-head", action="store_true")
430	    p.add_argument("--use-lora", action="store_true")
431	    p.add_argument("--lora-r", type=int, default=16)
432	    p.add_argument("--proj-dim", type=int, default=256)
433	    p.add_argument("--gradient-checkpointing", action="store_true")
434	    p.add_argument("--eval-steps", type=int, default=500)
435	    p.add_argument("--save-steps", type=int, default=1000)
436	    p.add_argument("--max-seq-length", type=int, default=2048)
437	    p.add_argument("--seed", type=int, default=42)
438	    p.add_argument("--wandb-project", default="structfuse")
439	    p.add_argument("--wandb-run-name", default=None)
440	    p.add_argument("--dataflow-graph-file", default=None, help="JSON file: {file_id: [reachable_ids]}")
441	    p.add_argument("--embeddings-file", default=None, help=".npz file with pre-computed embeddings")
442	    return p.parse_args()
443	
444	
445	if __name__ == "__main__":
446	    train(parse_args())
447	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "ff8d096e-3383-4d68-bab4-eefae249fdb2"
}
```

</details>

---

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Reading artifacts/code/training/train.py",
  "usage": {
    "total_tokens": 65710,
    "tool_uses": 21,
    "duration_ms": 28894
  },
  "last_tool_name": "Read",
  "uuid": "7b6e3e70-8590-489b-881c-0c3be887415a",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_0131yNP163DydPWiRo7jYY76`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py",
  "offset": 267,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "06e4bd8b-ddb2-4563-a391-3779e9670085",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013w2ywwTSi3xLxmj6LvFaQR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 64736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 880,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-14T22:47:20.551Z_

<details><summary>↩ Tool result · `toolu_0131yNP163DydPWiRo7jYY76`</summary>

```text
267	    model = StructFuseEncoder(
268	        model_name=args.model_name,
269	        proj_dim=args.proj_dim,
270	        use_projection=True,
271	        use_lora=args.use_lora,
272	        lora_r=args.lora_r,
273	        lora_alpha=args.lora_r * 2,
274	        use_fusion_head=args.use_fusion_head,
275	    )
276	    if args.gradient_checkpointing:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "304c46ad-e95a-4d40-a3aa-890816a06c58"
}
```

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 66008,
    "tool_uses": 22,
    "duration_ms": 30816
  },
  "last_tool_name": "Bash",
  "uuid": "ae356e14-9d3d-4d78-90c4-d540b6891026",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01WDXJBuowv5jMBmiVW55fZP`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context -name \"contrastive_model.py\" -o -name \"*encoder*.py\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "b266f467-3532-4556-b44e-d8247d8cf4fe",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011NcXCDaV2LAN86bkPH63hT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 65616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 289,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-14T22:47:22.537Z_

<details><summary>↩ Tool result · `toolu_01WDXJBuowv5jMBmiVW55fZP`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/contrastive_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/cross_encoder_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/contrastive_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/analysis/cross_encoder_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "0bb2eec8-621e-4832-aee3-dbfd40988d09"
}
```

</details>

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 66013,
    "tool_uses": 23,
    "duration_ms": 31064
  },
  "last_tool_name": "Bash",
  "uuid": "f643a181-cc5f-452d-a741-74545ab3fdc3",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01EokmnXgUAA9c7PmRxAXrpa`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts -name \"*.py\" -type f | grep -E \"(model|encoder|contrastive)\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "8b36fa5f-b3e3-4ba9-b6c0-ba63f6df92bc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011NcXCDaV2LAN86bkPH63hT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 65616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 289,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-14T22:47:22.782Z_

<details><summary>↩ Tool result · `toolu_01EokmnXgUAA9c7PmRxAXrpa`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/contrastive_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/cross_encoder_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/contrastive_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/analysis/cross_encoder_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "47db8d7b-1812-4bf1-b659-517510f1ac86"
}
```

</details>

---

### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -n \"LoRA\\|lora\\|target_modules\" /home/ubuntu…",
  "usage": {
    "total_tokens": 66768,
    "tool_uses": 24,
    "duration_ms": 32712
  },
  "last_tool_name": "Bash",
  "uuid": "aa46c6cb-a193-4486-96cb-32f0540535ce",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_0194KJnxcpDfDCCtZ5AsYA96`</summary>

```json
{
  "command": "grep -n \"LoRA\\|lora\\|target_modules\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/contrastive_model.py | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "f29a9d28-8b85-4e1f-bd7a-07ca1eb59d39",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SHNkjz4ZMrFht1wsLqhnZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 65905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 702,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-14T22:47:24.425Z_

<details><summary>↩ Tool result · `toolu_0194KJnxcpDfDCCtZ5AsYA96`</summary>

```text
55:    """Bi-encoder with shared Qwen backbone, optional projection & LoRA."""
62:        use_lora: bool = False,
63:        lora_r: int = 16,
64:        lora_alpha: int = 32,
91:        if use_lora:
92:            self._apply_lora(lora_r, lora_alpha)
94:    def _apply_lora(self, r: int, alpha: int):
97:        lora_cfg = LoraConfig(
99:            lora_alpha=alpha,
100:            target_modules=["q_proj", "v_proj"],
101:            lora_dropout=0.05,
105:        self.backbone = get_peft_model(self.backbone, lora_cfg)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "d4925c05-ee68-42cf-9ec7-9cbc14f7f90e"
}
```

</details>

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -n \"weight_decay\\|warmup\\|schedule\" /home/ub…",
  "usage": {
    "total_tokens": 67089,
    "tool_uses": 25,
    "duration_ms": 34709
  },
  "last_tool_name": "Bash",
  "uuid": "af1ad42a-0ced-4ca7-834b-92f5a21ba924",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Bash · `toolu_011B7g1vh71sG84AVxUff2mF`</summary>

```json
{
  "command": "grep -n \"weight_decay\\|warmup\\|schedule\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "7904fb51-85bd-4027-be4b-1459789f8689",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JsUmfYmJGfF9EqqcpB7WFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 66607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 321,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-14T22:47:26.410Z_

<details><summary>↩ Tool result · `toolu_011B7g1vh71sG84AVxUff2mF`</summary>

```text
24:from transformers import AutoTokenizer, get_cosine_schedule_with_warmup
307:    # optimizer & scheduler
308:    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=0.01)
310:    warmup_steps = int(total_steps * args.warmup_ratio)
311:    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)
314:    model, optimizer, train_loader, val_loader, scheduler = accelerator.prepare(
315:        model, optimizer, train_loader, val_loader, scheduler
353:            scheduler.step()
359:                lr = scheduler.get_last_lr()[0]
423:    p.add_argument("--warmup-ratio", type=float, default=0.1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "036974e2-e5f8-45e9-931b-798ec6bdb3df"
}
```

</details>

---

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "description": "Running grep -A 30 \"m2_full_qwen:\" /home/ubuntu/.agent-ml…",
  "usage": {
    "total_tokens": 67448,
    "tool_uses": 26,
    "duration_ms": 36593
  },
  "last_tool_name": "Bash",
  "uuid": "16ff4f62-9399-424e-942f-a5e9551f0d07",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Bash · `toolu_013XcqJZ1Byx3GDFPmuuDwF5`</summary>

```json
{
  "command": "grep -A 30 \"m2_full_qwen:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "c5bf2fb9-0e2a-492b-8e4f-ca81449ee9e9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UVsyDWM4stL6pvRN9rk3xX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 342,
      "cache_read_input_tokens": 66928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 342,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-14T22:47:28.304Z_

<details><summary>↩ Tool result · `toolu_013XcqJZ1Byx3GDFPmuuDwF5`</summary>

```text
  m2_full_qwen:
    status: ANALYZING
    retry_count: 0
    created_at: '2026-05-13T16:18:14.870Z'
    updated_at: '2026-05-14T18:00:29.323Z'
    hypothesis: 'Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds
      on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding
      > random +2pp). Go/no-go for paper claims per D018.'
    parent: m2_embed_verify
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log"
      server: bjb1-42106
      gpu:
      - cuda:0
      pid: '73544'
      log_path: ~/runs/structfuse-context/m2_full_qwen.log
      submitted_at: '2026-05-13T17:39:30.757Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
    notes: 'Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware)
      × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8,
      eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01,
      temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual
      checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed.
      [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs
      + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING
      是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500
      R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step
      500。GPU 100% 利用率, 50.5/97.9GB VRAM。'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a5a7c3c7-454c-40d2-811b-1a24e42705c5"
}
```

</details>

---

### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a9cbefeeed0e6e6a8",
  "tool_use_id": "toolu_018Soyx3Dz88YTL3xAkgnwMJ",
  "status": "completed",
  "output_file": "",
  "summary": "Find training config params",
  "usage": {
    "total_tokens": 68334,
    "tool_uses": 26,
    "duration_ms": 49130
  },
  "uuid": "0c6f9c25-d7f4-41d9-b0c8-81b6ca27980a",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04"
}
```

---

### Tool result

_source line 98 · 2026-05-14T22:47:40.784Z_

<details><summary>↩ Tool result · `toolu_018Soyx3Dz88YTL3xAkgnwMJ`</summary>

```text
Perfect! Now I have all the information needed. Let me compile a comprehensive report.

## Summary of Training Configuration Parameters

Based on my thorough search through the StructFuse project, here are all the training configuration parameters you requested:

### Core Training Hyperparameters

**Learning Rate & Batch Size:**
- **Learning Rate:** 2e-5
- **Batch Size:** 8

**Temperature (Contrastive Loss):**
- **Temperature (τ):** 0.07 (learnable parameter)
- This is unusually low (reviewers noted τ=0.05 is at the sharp end of the spectrum); paper includes temperature ablation with values {0.05, 0.1, 0.2}

**Number of Negatives & Sequence Length:**
- **num_negatives:** 7 (negatives per query)
- **max_seq_length:** 2048 tokens

**Training Duration:**
- **num_epochs:** 3 (for initial seed 42 to capture overfitting curve); later seeds reduced to 2 epochs with early_stopping_patience=2
- **eval_steps:** 500 (validation evaluation interval)
- **save_steps:** 1000 (checkpoint save interval)

**Projection & Model Configuration:**
- **proj_dim:** 256 (projection dimension for embedding space)
- **Model Base:** Qwen2.5-Coder-3B (decoder-only architecture)

### LoRA Configuration

- **LoRA Enabled:** Yes (--use-lora flag)
- **LoRA rank (r):** 16
- **LoRA alpha (α):** 32 (calculated as lora_r × 2, i.e., 16 × 2)
- **target_modules:** ["q_proj", "v_proj"] (query and value projections in attention)
- **LoRA dropout:** 0.05

### Optimizer Details

- **Optimizer:** AdamW (torch.optim.AdamW)
- **Weight Decay:** 0.01

### Learning Rate Schedule

- **Scheduler:** Cosine annealing with warmup (get_cosine_schedule_with_warmup)
- **Warmup Ratio:** 0.1 (10% of total steps used for linear warmup)
- **Total Steps:** len(train_loader) × num_epochs

### Positive Weight Configuration

- **pos_weight_alpha:** 1.0 (exponential decay factor for positive weight based on dataflow distance)
- Weight formula: exp(-alpha × dataflow_distance)

### Gradient & Computation

- **Gradient Checkpointing:** Enabled (--gradient-checkpointing flag)
- **Gradient Clipping:** max_norm=1.0

### Dual Checkpoint Strategy

The project uses a **dual checkpoint selection protocol** to handle the disagreement between validation loss and retrieval metrics (especially on StarCoder2):

1. **Best by Validation Loss:** Tracks the checkpoint with minimum val_loss (evaluated every 500 steps)
2. **Best by Recall@1:** Tracks the checkpoint with maximum R@1 on held-out validation set (evaluated every 500 steps)

**Selection Pattern:**
- For Qwen2.5-Coder-3B: Both criteria agree in 4/4 runs tested (select same checkpoint)
- For StarCoder2-3B: Both criteria disagree in 3/3 evaluable runs (best-by-R@1 checkpoint is 500-1500 steps later than best-by-loss)
- **Final Selection:** Reports use the checkpoint that maximizes Recall@1 directly (example: step 1000 for Qwen random_s42, vs step 2500 for StarCoder random_s42)

### Data Configuration

- **Train Data:** ~11.3K samples per seed
- **Validation Data:** ~3K samples per seed
- **num_workers:** 4 (for training DataLoader), 2 (for validation DataLoader)
- **pin_memory:** True

### Hard Negative Mining Strategy

- **Default Strategy:** dataflow_aware (also tested: random, embedding_distance)
- **hard_negative_ratio:** 0.5 (ratio of hard negatives vs easy negatives)
- Re-mining occurs each epoch at the epoch boundary using updated miner state

### Additional Configuration Details

- **seed:** 42 (primary), 43, 44 (additional seeds for statistical validation)
- **W&B Logging:** Enabled (wandb_project="structfuse")
- **Gradient Accumulation:** Not explicitly used; synchronous updates per batch
- **Mixed Precision:** Managed by Accelerate framework (not explicitly configured in train.py)

### File Locations

All configuration parameters are implemented in:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py` (main training script with argument parser)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/contrastive_model.py` (LoRA configuration in StructFuseEncoder)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md` (dual checkpoint strategy documentation)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "5400ff82-ded5-4313-a8cc-5f4871ebe741",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/, find the training configuration parameters - specifically the temperature value for contrastive loss, LoRA configuration (r, alpha, target_modules), learning rate, batch size, num_negatives, max_seq_length, projection dimension, number of epochs, optimizer details, and the dual checkpoint strategy details.\n\nSearch breadth: medium. Look in config files, training scripts, YAML configs, and any experiment config files. Also check the artifacts directory for any experiment reports that mention these values. Check any code repo paths that might be referenced.",
    "agentId": "a9cbefeeed0e6e6a8",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me compile a comprehensive report.\n\n## Summary of Training Configuration Parameters\n\nBased on my thorough search through the StructFuse project, here are all the training configuration parameters you requested:\n\n### Core Training Hyperparameters\n\n**Learning Rate & Batch Size:**\n- **Learning Rate:** 2e-5\n- **Batch Size:** 8\n\n**Temperature (Contrastive Loss):**\n- **Temperature (τ):** 0.07 (learnable parameter)\n- This is unusually low (reviewers noted τ=0.05 is at the sharp end of the spectrum); paper includes temperature ablation with values {0.05, 0.1, 0.2}\n\n**Number of Negatives & Sequence Length:**\n- **num_negatives:** 7 (negatives per query)\n- **max_seq_length:** 2048 tokens\n\n**Training Duration:**\n- **num_epochs:** 3 (for initial seed 42 to capture overfitting curve); later seeds reduced to 2 epochs with early_stopping_patience=2\n- **eval_steps:** 500 (validation evaluation interval)\n- **save_steps:** 1000 (checkpoint save interval)\n\n**Projection & Model Configuration:**\n- **proj_dim:** 256 (projection dimension for embedding space)\n- **Model Base:** Qwen2.5-Coder-3B (decoder-only architecture)\n\n### LoRA Configuration\n\n- **LoRA Enabled:** Yes (--use-lora flag)\n- **LoRA rank (r):** 16\n- **LoRA alpha (α):** 32 (calculated as lora_r × 2, i.e., 16 × 2)\n- **target_modules:** [\"q_proj\", \"v_proj\"] (query and value projections in attention)\n- **LoRA dropout:** 0.05\n\n### Optimizer Details\n\n- **Optimizer:** AdamW (torch.optim.AdamW)\n- **Weight Decay:** 0.01\n\n### Learning Rate Schedule\n\n- **Scheduler:** Cosine annealing with warmup (get_cosine_schedule_with_warmup)\n- **Warmup Ratio:** 0.1 (10% of total steps used for linear warmup)\n- **Total Steps:** len(train_loader) × num_epochs\n\n### Positive Weight Configuration\n\n- **pos_weight_alpha:** 1.0 (exponential decay factor for positive weight based on dataflow distance)\n- Weight formula: exp(-alpha × dataflow_distance)\n\n### Gradient & Computation\n\n- **Gradient Checkpointing:** Enabled (--gradient-checkpointing flag)\n- **Gradient Clipping:** max_norm=1.0\n\n### Dual Checkpoint Strategy\n\nThe project uses a **dual checkpoint selection protocol** to handle the disagreement between validation loss and retrieval metrics (especially on StarCoder2):\n\n1. **Best by Validation Loss:** Tracks the checkpoint with minimum val_loss (evaluated every 500 steps)\n2. **Best by Recall@1:** Tracks the checkpoint with maximum R@1 on held-out validation set (evaluated every 500 steps)\n\n**Selection Pattern:**\n- For Qwen2.5-Coder-3B: Both criteria agree in 4/4 runs tested (select same checkpoint)\n- For StarCoder2-3B: Both criteria disagree in 3/3 evaluable runs (best-by-R@1 checkpoint is 500-1500 steps later than best-by-loss)\n- **Final Selection:** Reports use the checkpoint that maximizes Recall@1 directly (example: step 1000 for Qwen random_s42, vs step 2500 for StarCoder random_s42)\n\n### Data Configuration\n\n- **Train Data:** ~11.3K samples per seed\n- **Validation Data:** ~3K samples per seed\n- **num_workers:** 4 (for training DataLoader), 2 (for validation DataLoader)\n- **pin_memory:** True\n\n### Hard Negative Mining Strategy\n\n- **Default Strategy:** dataflow_aware (also tested: random, embedding_distance)\n- **hard_negative_ratio:** 0.5 (ratio of hard negatives vs easy negatives)\n- Re-mining occurs each epoch at the epoch boundary using updated miner state\n\n### Additional Configuration Details\n\n- **seed:** 42 (primary), 43, 44 (additional seeds for statistical validation)\n- **W&B Logging:** Enabled (wandb_project=\"structfuse\")\n- **Gradient Accumulation:** Not explicitly used; synchronous updates per batch\n- **Mixed Precision:** Managed by Accelerate framework (not explicitly configured in train.py)\n\n### File Locations\n\nAll configuration parameters are implemented in:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py` (main training script with argument parser)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/contrastive_model.py` (LoRA configuration in StructFuseEncoder)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md` (dual checkpoint strategy documentation)"
      }
    ],
    "totalDurationMs": 49133,
    "totalTokens": 69441,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 67270,
      "output_tokens": 1284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1284,
          "cache_read_input_tokens": 67270,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 885,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 5,
      "bashCount": 12,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the Method section draft.

Key parameters:
- Temperature τ: 0.07 (learnable)
- lr: 2e-5
- batch_size: 8
- num_negatives: 7
- max_seq_length: 2048
- LoRA r: 16, alpha: 32, target_modules: q_proj, v_proj, dropout: 0.05
- proj_dim: 256
- num_epochs: 3 (initial), 2 (later seeds with early stopping patience=2)


- eval_steps: 500
- optimizer: AdamW with weight decay of 0.01
- scheduler: cosine annealing with warmup over 10% of training
- gradient checkpointing and clipping at norm 1.0
- dual checkpoint strategy tracking both validation loss and recall@1
- two encoder architectures: Qwen2.5-Coder-3B and StarCoder2-3B

Now I'm drafting the method section with four subsections, being precise and academic about the setup.

For the formal definition, I'm establishing the retrieval domain D with a structural graph G and similarity function s. The key innovation is defining structure-grounded hard negatives as examples that are similar to the query but structurally unreachable in the graph—these are selected by maximizing similarity while respecting the structural constraint. The graph itself is externally fixed to ensure the approach remains robust to distribution shifts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "3b097e06-1cad-4784-971e-8c3af6355125",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2Vwtn2zxGpNhdqr4YsT7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2006,
      "cache_read_input_tokens": 39130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2006
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 100_

Now I have all materials. Let me write the method section draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "350d2078-deb5-43c5-af94-a727c6d4621b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2Vwtn2zxGpNhdqr4YsT7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2006,
      "cache_read_input_tokens": 39130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2006
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Bash · `toolu_01HDqxzhiK3RszrJD1CtADbC`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if paper_drafts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "50e87430-4555-4e42-8c0d-9351085fbd70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2Vwtn2zxGpNhdqr4YsT7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2006,
      "cache_read_input_tokens": 39130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2006
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-14T22:47:53.440Z_

<details><summary>↩ Tool result · `toolu_01HDqxzhiK3RszrJD1CtADbC`</summary>

```text
discussion_v2.md
experimental_setup_k_checkpoint.md
introduction_v1.md
related_work_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "1ce5e5f7-ec8d-40d2-afc9-e06133da3138",
  "tool_use_result": {
    "stdout": "discussion_v2.md\nexperimental_setup_k_checkpoint.md\nintroduction_v1.md\nrelated_work_v1.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Write · `toolu_01RHp1FfjxPitxa6NzgEnfdv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 StructFuse Pipeline\n\nOur pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n\n**CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n\nWe set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n\n**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\n**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n\n## §3.3 Training Objective\n\n**Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.\n\n**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.\n\n**Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.\n\n**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n\n## §3.4 Negative Mining Strategies\n\nWe compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n\n**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThis selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n\n**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThat is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\n**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n\nFor repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "1048944d-af64-4aa4-a385-35360c05bfaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKTTuxtEAbMNWgsZF6RUzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 41136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
      },
      "output_tokens": 53,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-14T22:48:54.870Z_

<details><summary>↩ Tool result · `toolu_01RHp1FfjxPitxa6NzgEnfdv`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "088be5c3-4916-4dde-a377-0480532956cd",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 StructFuse Pipeline\n\nOur pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n\n**CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n\nWe set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n\n**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\n**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n\n## §3.3 Training Objective\n\n**Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.\n\n**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.\n\n**Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.\n\n**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n\n## §3.4 Negative Mining Strategies\n\nWe compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n\n**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThis selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n\n**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThat is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\n**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n\nFor repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 105_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_012R8aWrWLeL4WPfyknkXadv`</summary>

```json
{
  "name": "method_v1",
  "type": "paper",
  "description": "Method section draft (§3) with 4 subsections: Problem Formulation, StructFuse Pipeline, Training Objective, Negative Mining Strategies. ~1200 words, LaTeX formulas, cite keys aligned with literature_map.yaml.",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "tags": [
    "paper",
    "method",
    "draft-v1"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "a69d2192-bfc7-49e9-a7e4-6679860f9f1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018r2ZSvD2hGKJu7ZdxJSMwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2802,
      "cache_read_input_tokens": 41714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2802
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-14T22:49:00.818Z_

<details><summary>↩ Tool result · `toolu_012R8aWrWLeL4WPfyknkXadv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_5db688\", \"name\": \"method_v1\", \"type\": \"paper\", \"description\": \"Method section draft (§3) with 4 subsections: Problem Formulation, StructFuse Pipeline, Training Objective, Negative Mining Strategies. ~1200 words, LaTeX formulas, cite keys aligned with literature_map.yaml.\", \"path\": \"projects/structfuse-context/artifacts/_project/paper/method_v1.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:49:00.699349+00:00\", \"tags\": [\"paper\", \"method\", \"draft-v1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "9c25bdd6-4a68-44d8-ad48-86acc15eef29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_5db688\\\", \\\"name\\\": \\\"method_v1\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Method section draft (§3) with 4 subsections: Problem Formulation, StructFuse Pipeline, Training Objective, Negative Mining Strategies. ~1200 words, LaTeX formulas, cite keys aligned with literature_map.yaml.\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/paper/method_v1.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T22:49:00.699349+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"draft-v1\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_5db688\", \"name\": \"method_v1\", \"type\": \"paper\", \"description\": \"Method section draft (§3) with 4 subsections: Problem Formulation, StructFuse Pipeline, Training Objective, Negative Mining Strategies. ~1200 words, LaTeX formulas, cite keys aligned with literature_map.yaml.\", \"path\": \"projects/structfuse-context/artifacts/_project/paper/method_v1.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:49:00.699349+00:00\", \"tags\": [\"paper\", \"method\", \"draft-v1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 107_

已写入 `artifacts/paper_drafts/method_v1.md` 并注册。

四个 subsection 覆盖内容：

- **§3.1 Problem Formulation** — repo-level retrieval 形式化定义，contrastive learning 框架
- **§3.2 StructFuse Pipeline** — CodeQL inter-procedural data-flow extraction → file-level structural graph → drift-immune 设计
- **§3.3 Training Objective** — InfoNCE 公式（τ=0.07 learnable），LoRA 配置（r=16, α=32, q_proj/v_proj），AdamW lr=2e-5，dual checkpoint 策略
- **§3.4 Negative Mining Strategies** — random / embedding-distance / dataflow-aware 三策略定义与公式，含 difficulty gradient 讨论和 34% fallback 说明

引用与 `literature_map.yaml` 对齐（SimCLR、DPR、ANCE、FAISS、CodeQL、Qwen2.5-Coder、StarCoder 等）。约 1200 词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "uuid": "0e8c27dd-965c-4787-8344-b1f815840647",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VyqCVkgFeec1ZVfey7w2J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 44516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 551
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 108_

已写入 `artifacts/paper_drafts/method_v1.md` 并注册。

四个 subsection 覆盖内容：

- **§3.1 Problem Formulation** — repo-level retrieval 形式化定义，contrastive learning 框架
- **§3.2 StructFuse Pipeline** — CodeQL inter-procedural data-flow extraction → file-level structural graph → drift-immune 设计
- **§3.3 Training Objective** — InfoNCE 公式（τ=0.07 learnable），LoRA 配置（r=16, α=32, q_proj/v_proj），AdamW lr=2e-5，dual checkpoint 策略
- **§3.4 Negative Mining Strategies** — random / embedding-distance / dataflow-aware 三策略定义与公式，含 difficulty gradient 讨论和 34% fallback 说明

引用与 `literature_map.yaml` 对齐（SimCLR、DPR、ANCE、FAISS、CodeQL、Qwen2.5-Coder、StarCoder 等）。约 1200 词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 170469,
  "duration_api_ms": 174268,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "c36d698d-d2e8-4560-8a39-71da24135a04",
  "total_cost_usd": 0.6275674499999999,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 33620,
    "cache_read_input_tokens": 226319,
    "output_tokens": 4888,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33620,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 294,
        "cache_read_input_tokens": 44516,
        "cache_creation_input_tokens": 551,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 551
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1612,
      "outputTokens": 4162,
      "cacheReadInputTokens": 744122,
      "cacheCreationInputTokens": 68155,
      "webSearchRequests": 0,
      "costUSD": 0.18202795,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 4888,
      "cacheReadInputTokens": 226319,
      "cacheCreationInputTokens": 33620,
      "webSearchRequests": 0,
      "costUSD": 0.44553950000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "46522e61-c02f-4230-a47d-ab86626bd42e"
}
```

</details>

---
