# write introduction v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_write_introduction-v1_20260515T083143.log`
- **Structured JSON:** [`054f564e05f5bd8adb7f.json`](../../sessions/05/054f564e05f5bd8adb7f.json)

## Before a recorded user message

40 recorded events

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
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
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
  "uuid": "23da62ee-e296-4302-946c-a900bcd90b3f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778836200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cd1a3f72-5c77-40ae-beae-ea6d236b90b3",
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required source files to gather context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "448b6ede-53ff-4605-acab-a0592b0804bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKhT1f8W7jvDPavQZRWycs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11794,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11794
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014jT2ojvSeHpgr2sG9EU6kZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
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
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "f6240835-d7c6-40e9-85d0-fcd203175604",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKhT1f8W7jvDPavQZRWycs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11794,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11794
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

_source line 6 · 2026-05-15T08:31:55.565Z_

<details><summary>↩ Tool result · `toolu_014jT2ojvSeHpgr2sG9EU6kZ`</summary>

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
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "b3502f17-ea1a-450b-bd0d-9bb7e2d99d76",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the required files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "bdaeb79b-559f-4ea6-b02c-1eb8ccaf98a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VDhqBDqPbBB5qC9rW9F1e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 23635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
      },
      "output_tokens": 56,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PEfZYtNbwWiCzLf48CnWSZ`</summary>

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
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "b4b9fd9f-0b63-40de-8544-33a71d31f785",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VDhqBDqPbBB5qC9rW9F1e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 23635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
      },
      "output_tokens": 56,
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

_source line 9 · 2026-05-15T08:31:59.100Z_

<details><summary>↩ Tool result · `toolu_01PEfZYtNbwWiCzLf48CnWSZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\"\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\n\", \"total_chars\": 14238, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "2402a279-79e0-4562-a860-4756a5b18076",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — StructFuse\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3)\\\\n\\\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\\\\\"slow and ineffective\\\\\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\\\n\\\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\\\n\\\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\\\n\\\\n- **Existing approaches & gaps**:\\\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\\\n\\\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\\\n\\\\n- **Headline result template**: \\\\\\\"Simple static embedding-distance mining consistently improves code retrieval (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\\\n\\\\n## Dual-Pillar Motivation\\\\n\\\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\\\n\\\\n## Formal Definition\\\\n\\\\nGiven retrieval domain D, structural graph G, query q:\\\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\\\n\\\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\\\n\\\\n## Title Options\\\\n\\\\n- Primary: \\\\\\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\\\\\"\\\\n- Alternative: \\\\\\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\\\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\\\n- Backup: \\\\\\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n\\\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\\\\\"Do Language Models...\\\\\\\" papers). Contribution is understanding, not just a new method.\\\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\\\n3. **Against \\\\\\\"incremental\\\\\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response | Evidence |\\\\n|---------|----------|----------|\\\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\\\n| \\\\\\\"Complementary signal\\\\\\\" overstatement | Temper: \\\\\\\"conditionally beneficial\\\\\\\" not \\\\\\\"always complementary\\\\\\\" | Writing discipline |\\\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\\\n\\\\n## Evidence Status\\\\n\\\\n### Confirmed findings (basis for claims):\\\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\\\n\\\\n### Evidence presentation strategy:\\\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\\\n\\\\n### In progress:\\\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\\\n\\\\n### Planned (priority order):\\\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\\\n- plan_014: Temperature ablation (Dream reviewer concern)\\\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\\\n- plan_015: Dynamic mining baseline\\\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\\\n- plan_007/008/009: Additional ablations\\\\n\\\\n## Limitations\\\\n\\\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\\\n\\\\n## Contingency (if full M2 results weaken claims)\\\\n\\\\n### All 18 runs confirm pilot pattern: Best case\\\\n- Full statistical power, paper as framed above\\\\n- Target: EMNLP Main\\\\n\\\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\\\n- Drop Claim 2 to analysis observation\\\\n- Paper becomes: \\\\\\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\\\\\"\\\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\\\n\\\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\\\n- Pivot: \\\\\\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\\\\\"\\\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\\\n- Claim 1 core preserved: \\\\\\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\\\\\"\\\\n- Impact: BM25 result determines narrative nuance, not core contribution\\\\n\\\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\\\n- If confirmed: negative result paper — \\\\\\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\\\\\"\\\\n- Discuss with user before committing direction\\\\n\\\\n## Deprecated Claims (with reason)\\\\n\\\\n- ~~\\\\\\\"Embedding-distance hard negatives actively harm code retrieval\\\\\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\\\n\\\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\\\n\\\", \\\"total_chars\\\": 14238, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\"\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\n\", \"total_chars\": 14238, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018zcFSkNxYyX7fvnercZSFD`</summary>

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
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "b27c8cd5-2f33-4a1b-b7ee-eca86b9075ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VDhqBDqPbBB5qC9rW9F1e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 23635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
      },
      "output_tokens": 56,
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

_source line 11 · 2026-05-15T08:31:59.635Z_

<details><summary>↩ Tool result · `toolu_018zcFSkNxYyX7fvnercZSFD`</summary>

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
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "e5f03626-920d-4f61-a0a8-deb0d2f8fe05",
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

<details open><summary>🔧 Tool call — Read · `toolu_016py5y7VoYBCedqjKBCpucm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "4f17c3cc-8422-4640-8367-07cff3e52a4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VDhqBDqPbBB5qC9rW9F1e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 23635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
      },
      "output_tokens": 56,
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

_source line 13 · 2026-05-15T08:32:00.053Z_

<details><summary>↩ Tool result · `toolu_016py5y7VoYBCedqjKBCpucm`</summary>

```text
1	# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas
2	
3	> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.
4	> Six new papers added; RocketQA already cited in v1.
5	> Generated: 2026-05-15
6	
7	---
8	
9	## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)
10	
11	Beyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.
12	
13	## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)
14	
15	The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.
16	
17	## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)
18	
19	The importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.
20	
21	---
22	
23	## Summary of New Citations
24	
25	| Paper | Venue | Year | Area | Relation to StructFuse |
26	|-------|-------|------|------|----------------------|
27	| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |
28	| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |
29	| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |
30	| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |
31	| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |
32	| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "264d3029-5574-415a-9eab-0f0b6b45638e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
      "content": "# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas\n\n> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.\n> Six new papers added; RocketQA already cited in v1.\n> Generated: 2026-05-15\n\n---\n\n## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)\n\nBeyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.\n\n## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)\n\nThe curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.\n\n## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)\n\nThe importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \\cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \\cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \\cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.\n\n---\n\n## Summary of New Citations\n\n| Paper | Venue | Year | Area | Relation to StructFuse |\n|-------|-------|------|------|----------------------|\n| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |\n| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |\n| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |\n| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |\n| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |\n| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
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
Now let me also check if there's a references.bib file to get the citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "13ae1c8b-485a-4589-ad29-9a7aa0004264",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LaG1HkWibVt7SWiDssSLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12579,
      "cache_read_input_tokens": 24542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12579
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

Let me check if there's a references.bib for citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "ff523fa3-c653-48e6-b475-435b5b60d9b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LaG1HkWibVt7SWiDssSLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12579,
      "cache_read_input_tokens": 24542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12579
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

<details open><summary>🔧 Tool call — Glob · `toolu_01JNMJr3UPRuXxuiq21ZiubA`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "4ce7de58-ed61-46f6-bf81-c8a2cc183490",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LaG1HkWibVt7SWiDssSLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12579,
      "cache_read_input_tokens": 24542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12579
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

_source line 17 · 2026-05-15T08:32:04.830Z_

<details><summary>↩ Tool result · `toolu_01JNMJr3UPRuXxuiq21ZiubA`</summary>

```text
artifacts/paper_drafts/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "aa4211cc-3a79-4e05-b05f-0d3ba0a607b1",
  "tool_use_result": {
    "filenames": [
      "artifacts/paper_drafts/references.bib"
    ],
    "durationMs": 12,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01CrjWqeN2aMoU6iniZaWeNB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "1b2a85bb-6a82-4b72-a443-ef64fcae37fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaK4KMPFFnoyD6u7WCu1qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 172,
      "cache_read_input_tokens": 37121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 172
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

_source line 19 · 2026-05-15T08:32:07.527Z_

<details><summary>↩ Tool result · `toolu_01CrjWqeN2aMoU6iniZaWeNB`</summary>

```text
1	% =============================================================================
2	% Section 2.1: Code Retrieval Methods
3	% =============================================================================
4	
5	@article{robertson2009bm25,
6	  title={The Probabilistic Relevance Framework: {BM25} and Beyond},
7	  author={Robertson, Stephen and Zaragoza, Hugo},
8	  journal={Foundations and Trends in Information Retrieval},
9	  volume={3},
10	  number={4},
11	  pages={333--389},
12	  year={2009},
13	  publisher={Now Publishers}
14	}
15	
16	@inproceedings{karpukhin2020dpr,
17	  title={Dense Passage Retrieval for Open-Domain Question Answering},
18	  author={Karpukhin, Vladimir and O{\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},
19	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
20	  pages={6769--6781},
21	  year={2020}
22	}
23	
24	@article{reddy2025swerank,
25	  title={{SweRank}: Software Issue Localization with Code Ranking},
26	  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},
27	  journal={arXiv preprint arXiv:2505.07849},
28	  year={2025}
29	}
30	
31	@inproceedings{xie2025swefixer,
32	  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},
33	  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},
34	  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},
35	  pages={1123--1139},
36	  year={2025}
37	}
38	
39	@inproceedings{chen2025locagent,
40	  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},
41	  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},
42	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
43	  pages={8697--8727},
44	  year={2025}
45	}
46	
47	@article{shah2025ranger,
48	  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},
49	  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},
50	  journal={arXiv preprint arXiv:2509.25257},
51	  year={2025}
52	}
53	
54	@inproceedings{liu2025codexgraph,
55	  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},
56	  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},
57	  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
58	  pages={142--160},
59	  year={2025}
60	}
61	
62	@inproceedings{ouyang2025repograph,
63	  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},
64	  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},
65	  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},
66	  year={2025}
67	}
68	
69	@inproceedings{liu2024graphcoder,
70	  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},
71	  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},
72	  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
73	  year={2024}
74	}
75	
76	@article{seddik2026arise,
77	  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},
78	  author={Seddik, Shahd and Fard, Fatemeh},
79	  journal={arXiv preprint arXiv:2605.03117},
80	  year={2026}
81	}
82	
83	% =============================================================================
84	% Section 2.2: Pre-trained Code Representations and Contrastive Learning
85	% =============================================================================
86	
87	@inproceedings{feng2020codebert,
88	  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},
89	  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
90	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
91	  pages={1536--1547},
92	  year={2020}
93	}
94	
95	@inproceedings{guo2021graphcodebert,
96	  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},
97	  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
98	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
99	  year={2021}
100	}
101	
102	@inproceedings{guo2022unixcoder,
103	  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},
104	  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
105	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
106	  pages={7212--7225},
107	  year={2022}
108	}
109	
110	@inproceedings{alon2019code2vec,
111	  title={code2vec: Learning Distributed Representations of Code},
112	  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},
113	  booktitle={Proceedings of the ACM on Programming Languages (POPL)},
114	  volume={3},
115	  pages={1--29},
116	  year={2019}
117	}
118	
119	@inproceedings{zhang2024codesage,
120	  title={Code Representation Learning At Scale},
121	  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},
122	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
123	  year={2024}
124	}
125	
126	@inproceedings{reimers2019sentencebert,
127	  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
128	  author={Reimers, Nils and Gurevych, Iryna},
129	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
130	  pages={3982--3992},
131	  year={2019}
132	}
133	
134	@inproceedings{jain2021contracode,
135	  title={Contrastive Code Representation Learning},
136	  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},
137	  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
138	  pages={5954--5971},
139	  year={2021}
140	}
141	
142	@inproceedings{li2022coderetriever,
143	  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},
144	  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
145	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
146	  pages={2898--2910},
147	  year={2022}
148	}
149	
150	@inproceedings{li2022scoder,
151	  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},
152	  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
153	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},
154	  year={2022}
155	}
156	
157	@inproceedings{ding2022programcontrasts,
158	  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},
159	  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},
160	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
161	  pages={6300--6312},
162	  year={2022}
163	}
164	
165	@inproceedings{bui2021infercode,
166	  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},
167	  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},
168	  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},
169	  pages={1186--1197},
170	  year={2021}
171	}
172	
173	@article{lozhkov2024starcoder2,
174	  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},
175	  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},
176	  journal={arXiv preprint arXiv:2402.19173},
177	  year={2024}
178	}
179	
180	@article{hui2024qwen25coder,
181	  title={{Qwen2.5-Coder} Technical Report},
182	  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},
183	  journal={arXiv preprint arXiv:2409.12186},
184	  year={2024}
185	}
186	
187	% =============================================================================
188	% Section 2.3: Hard Negative Mining
189	% =============================================================================
190	
191	@inproceedings{chen2020simclr,
192	  title={A Simple Framework for Contrastive Learning of Visual Representations},
193	  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
194	  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},
195	  pages={1597--1607},
196	  year={2020}
197	}
198	
199	@inproceedings{xiong2021ance,
200	  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},
201	  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},
202	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
203	  year={2021}
204	}
205	
206	@inproceedings{zhan2021star,
207	  title={Optimizing Dense Retrieval Model Training with Hard Negatives},
208	  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},
209	  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
210	  pages={1503--1512},
211	  year={2021}
212	}
213	
214	@inproceedings{qu2021rocketqa,
215	  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},
216	  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},
217	  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},
218	  pages={5835--5847},
219	  year={2021}
220	}
221	
222	@inproceedings{zeng2022cldrd,
223	  title={Curriculum Learning for Dense Retrieval Distillation},
224	  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},
225	  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
226	  pages={1979--1983},
227	  year={2022}
228	}
229	
230	@article{fan2025cocohanere,
231	  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
232	  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},
233	  journal={ACM Transactions on Software Engineering and Methodology},
234	  volume={34},
235	  number={3},
236	  year={2025},
237	  publisher={ACM}
238	}
239	
240	% =============================================================================
241	% Section 2.4: Code Structure Analysis
242	% =============================================================================
243	
244	@article{ferrante1987pdg,
245	  title={The Program Dependence Graph and Its Use in Optimization},
246	  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},
247	  journal={ACM Transactions on Programming Languages and Systems},
248	  volume={9},
249	  number={3},
250	  pages={319--349},
251	  year={1987},
252	  publisher={ACM}
253	}
254	
255	@inproceedings{yamaguchi2014cpg,
256	  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},
257	  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},
258	  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\&P)},
259	  pages={590--604},
260	  year={2014},
261	  publisher={IEEE}
262	}
263	
264	@inproceedings{avgustinov2016ql,
265	  title={{QL}: Object-oriented Queries on Relational Data},
266	  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\"a}fer, Max},
267	  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},
268	  series={LIPIcs},
269	  volume={56},
270	  pages={2:1--2:25},
271	  year={2016}
272	}
273	
274	% =============================================================================
275	% Supplement: New citations added 2026-05-15
276	% =============================================================================
277	
278	@article{wang2021syncobert,
279	  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},
280	  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},
281	  journal={arXiv preprint arXiv:2108.04556},
282	  year={2021}
283	}
284	
285	@inproceedings{liu2023contrabert,
286	  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},
287	  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},
288	  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},
289	  pages={2476--2487},
290	  year={2023}
291	}
292	
293	@inproceedings{he2023capstone,
294	  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},
295	  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},
296	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
297	  pages={10531--10541},
298	  year={2023}
299	}
300	
301	@inproceedings{ding2023crosscodeeval,
302	  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},
303	  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},
304	  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},
305	  year={2023}
306	}
307	
308	@inproceedings{cummins2021programl,
309	  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},
310	  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},
311	  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},
312	  pages={2244--2253},
313	  year={2021},
314	  publisher={PMLR}
315	}
316	
317	@inproceedings{huang2021cosqa,
318	  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},
319	  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},
320	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
321	  pages={5690--5700},
322	  year={2021}
323	}
324	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "271301fb-158e-427f-8aa5-185a6266a440",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
      "content": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n\n% =============================================================================\n% Supplement: New citations added 2026-05-15\n% =============================================================================\n\n@article{wang2021syncobert,\n  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},\n  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},\n  journal={arXiv preprint arXiv:2108.04556},\n  year={2021}\n}\n\n@inproceedings{liu2023contrabert,\n  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},\n  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},\n  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={2476--2487},\n  year={2023}\n}\n\n@inproceedings{he2023capstone,\n  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},\n  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={10531--10541},\n  year={2023}\n}\n\n@inproceedings{ding2023crosscodeeval,\n  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},\n  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{cummins2021programl,\n  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},\n  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},\n  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},\n  pages={2244--2253},\n  year={2021},\n  publisher={PMLR}\n}\n\n@inproceedings{huang2021cosqa,\n  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},\n  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={5690--5700},\n  year={2021}\n}\n",
      "numLines": 324,
      "startLine": 1,
      "totalLines": 324
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context needed. Let me also check if there are existing paper drafts to understand the output directory structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "9d623284-4b8f-4f4c-a104-2577505cffdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQeRSWFsMq1bvMph7RxcHA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6046,
      "cache_read_input_tokens": 37293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6046
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

### Assistant

_source line 21_

Now let me check the output directory exists and look for any existing drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "3eef4df0-bef4-44b7-8bd3-304ae2f0bf6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQeRSWFsMq1bvMph7RxcHA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6046,
      "cache_read_input_tokens": 37293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6046
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

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01GYzks6q3FRuqYu2c7pYptm`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/",
  "description": "List paper drafts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "5b459ed5-685c-4d9e-ba2d-8c9382a48328",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQeRSWFsMq1bvMph7RxcHA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6046,
      "cache_read_input_tokens": 37293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6046
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

_source line 23 · 2026-05-15T08:32:13.324Z_

<details><summary>↩ Tool result · `toolu_01GYzks6q3FRuqYu2c7pYptm`</summary>

```text
bm25_code_review.md
checkpoint_criterion_table.tex
claim2_wording_review.md
discussion_v2.md
discussion_valloss_divergence.md
experiment_setup_v1.md
experimental_setup_k_checkpoint.md
experiments_v1.md
figure_design_v1.md
fixed_checkpoint_table.tex
introduction_v1.md
introduction_v2.md
method_v1.md
references.bib
related_work_supplement.md
related_work_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "c7021ffa-ed90-4701-a47d-671cf704ba55",
  "tool_use_result": {
    "stdout": "bm25_code_review.md\ncheckpoint_criterion_table.tex\nclaim2_wording_review.md\ndiscussion_v2.md\ndiscussion_valloss_divergence.md\nexperiment_setup_v1.md\nexperimental_setup_k_checkpoint.md\nexperiments_v1.md\nfigure_design_v1.md\nfixed_checkpoint_table.tex\nintroduction_v1.md\nintroduction_v2.md\nmethod_v1.md\nreferences.bib\nrelated_work_supplement.md\nrelated_work_v1.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
There's already an introduction_v1.md and introduction_v2.md. Let me read introduction_v1.md to see what's there, since the task says to write to introduction_v1.md. Actually, the task says to write to introduction_v1.md. Let me read the existing one first to see if it's there and what it contains, since I'm going to overwrite it.

Wait, actually the user explicitly asked me to write to introduction_v1.md. The file already exists. Let me read it to understand what's there, and then I'll write the new version. Actually, the task says "论文 Introduction 初稿（~800 words）" so this is generating the introduction draft. 

Now I'm pulling together the framing document to understand the key narrative. The paper has three main claims: embedding-distance mining as a reliable baseline, an exploratory observation about structure-grounded negatives and encoder geometry, and the CodeQL pipeline. I need to weave these together with the softened language from the framing—avoiding "challenges" and "we demonstrate"—while incorporating the specific performance numbers from the pilot and M2 experiments.

I'm organizing the introduction around a 5-paragraph structure and gathering the citation keys I'll need to ground the work in prior research on code retrieval, contrastive learning, and graph-based representations. I'm checking the bibliography for a few missing citations — SWE-bench, SWE-smith, and RepoFusion all appear in the literature map but aren't in the bib file yet, so I'll use placeholder citations for now. Now I'm moving into drafting the introduction with specific constraints: around 800 words across 5 paragraphs, softened language avoiding "challenges" and "we demonstrate," exploratory framing for the second claim, and reporting both pilot and M2 results in LaTeX citation format. I'll structure this as code retrieval importance and dense retrieval trends, then hard negative mining success in NLP and its application to code, followed by our core insight. I'm establishing that while dense retrieval has become standard for code localization, the role of negative example selection in training these models hasn't been thoroughly investigated, despite its proven importance in text retrieval systems. Now I'm tracing how hard negative mining evolved across different retrieval approaches—from BM25-based strategies to dynamic mining and cross-encoder filtering—to set up why this matters for code.

The key tension I'm identifying is that recent work like CoCoHaNeRe claims embedding-based hard negatives are ineffective for code search, but this conclusion might be premature given that code has structural properties—call graphs, data dependencies, taint flows—that natural language lacks and could make simpler mining strategies more viable than previously thought.

I'm proposing to leverage CodeQL's inter-procedural analysis to identify structurally disconnected files that are still lexically similar, creating negatives grounded in program semantics rather than surface patterns. This mining happens only during training with no inference overhead, making it orthogonal to graph-guided retrieval methods that operate at test time.

Now I'm comparing four negative mining strategies across two 3B-parameter models. Embedding-distance mining alone delivers consistent gains of 0.5–2.0 percentage points in recall without extra computational cost, establishing it as a solid baseline. Structure-aware negatives from dataflow analysis show promise but the results are still being evaluated. I'm finishing up the contributions section, laying out the three main points: the practical pipeline for mining structural negatives using CodeQL, the systematic comparison across different negative mining strategies and two distinct encoders, and the mechanistic analysis of how representation geometry influences which strategies work best. I'm also doing a final word count check to make sure each paragraph hits around 150-200 words and the total stays close to 800.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "0905bcd3-53e0-4676-954d-fe238ac7f497",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Khxi4uSB6sC3EcTY2cFwpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 43339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 25_

Writing the introduction draft now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "ea538df1-c6e3-420c-9ad3-28f0052d53a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Khxi4uSB6sC3EcTY2cFwpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 43339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01GnZf5sDcLd41bGn4o4W8Ae`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "ed9a766c-a0cf-4dc8-a29e-370a84cd69d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Khxi4uSB6sC3EcTY2cFwpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 43339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 27 · 2026-05-15T08:33:14.696Z_

<details><summary>↩ Tool result · `toolu_01GnZf5sDcLd41bGn4o4W8Ae`</summary>

```text
1	# 1. Introduction
2	
3	Large-scale software maintenance increasingly depends on automatically identifying which source files require modification given a bug report or issue description.
4	Benchmarks such as SWE-bench \cite{jimenez2024swebench} formalize this as a retrieval problem over repositories containing hundreds or thousands of files, and recent systems tackle it through text-based retrieval \cite{reddy2025swerank,xie2025swefixer}, agent-based interactive localization \cite{yang2024sweagent,xia2024agentless}, or combinations thereof.
5	A common assumption underlying these approaches is that textual similarity between an issue description and a source file signals relevance.
6	In practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.
7	This mismatch is particularly acute in large repositories where naming conventions are reused across unrelated modules, making retrieval that relies solely on text vulnerable to systematic false positives.
8	
9	Two largely independent lines of work have sought to address this limitation, each with a significant gap.
10	First, a growing body of methods leverages code structure graphs at inference time.
11	LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ LLM agents to navigate repository-level graphs during fault localization; CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} provide graph database interfaces for structural code navigation; GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate control-flow or data-dependence edges—though both remain intra-procedural in scope.
12	These methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.
13	Second, hard negative mining—selecting challenging negative examples for contrastive training—is known to substantially impact dense retrieval quality \cite{karpukhin2020dpr,xiong2021ance}, yet has received limited systematic study in the code domain.
14	CoCoHaNeRe \cite{fan2025cocohanere} proposes a gradient-based differentiable hard negative mechanism for code search contrastive learning, arguing that non-differentiable embedding-based negatives are ``slow and ineffective'' compared to gradient-based alternatives.
15	However, CoCoHaNeRe's comparison does not evaluate simple static embedding-distance mining—selecting negatives by nearest-neighbor lookup in a frozen embedding space—in structural code retrieval settings.
16	This leaves open whether the complexity of gradient-based methods is truly necessary, and more broadly, how different negative mining strategies interact with the properties of the encoder being trained.
17	
18	We present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.
19	Our central finding challenges the prevailing assumption that expensive gradient-based methods are required: simple static embedding-distance mining consistently improves retrieval (pilot evidence; pending M2 full confirmation), yielding +1.6--2.0 percentage points in Recall@1 over random baselines across two decoder-only encoders with distinct pretraining paradigms and representation geometries—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}.
20	These gains are achieved without gradient-based mechanisms, providing a direct counter-example to CoCoHaNeRe's premise in the structural code retrieval setting we study.
21	We note that CoCoHaNeRe's original argument targets the comparison between gradient-based and non-differentiable embedding negatives broadly; our counter-evidence is specific to structural code retrieval, where static embedding-distance mining proves sufficient.
22	Beyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.
23	
24	Our contributions are as follows:
25	
26	1. We demonstrate that simple static embedding-distance hard negative mining consistently improves (pilot evidence; pending M2 full confirmation) contrastive code retrieval across two decoder-only encoders with distinct representation geometries, challenging the assumption that gradient-based hard negative methods \cite{fan2025cocohanere} are necessary for effective code search.
27	
28	2. **[Exploratory observation]** We report that structure-grounded (dataflow) negatives interact with encoder representation geometry: negative difficulty margin analysis (+17% for Qwen2.5-Coder-3B, +28% for StarCoder2-3B) provides mechanistic evidence that the pretrained embedding space's degree of saturation mediates strategy effectiveness. Pilot data shows dataflow negatives underperform embedding mining on both encoders, with the gap modulated by representation geometry. This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.
29	
30	3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "69e98bb5-165c-4be0-b652-b5f2109f6837",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
      "content": "# 1. Introduction\n\nLarge-scale software maintenance increasingly depends on automatically identifying which source files require modification given a bug report or issue description.\nBenchmarks such as SWE-bench \\cite{jimenez2024swebench} formalize this as a retrieval problem over repositories containing hundreds or thousands of files, and recent systems tackle it through text-based retrieval \\cite{reddy2025swerank,xie2025swefixer}, agent-based interactive localization \\cite{yang2024sweagent,xia2024agentless}, or combinations thereof.\nA common assumption underlying these approaches is that textual similarity between an issue description and a source file signals relevance.\nIn practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.\nThis mismatch is particularly acute in large repositories where naming conventions are reused across unrelated modules, making retrieval that relies solely on text vulnerable to systematic false positives.\n\nTwo largely independent lines of work have sought to address this limitation, each with a significant gap.\nFirst, a growing body of methods leverages code structure graphs at inference time.\nLocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ LLM agents to navigate repository-level graphs during fault localization; CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} provide graph database interfaces for structural code navigation; GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate control-flow or data-dependence edges—though both remain intra-procedural in scope.\nThese methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.\nSecond, hard negative mining—selecting challenging negative examples for contrastive training—is known to substantially impact dense retrieval quality \\cite{karpukhin2020dpr,xiong2021ance}, yet has received limited systematic study in the code domain.\nCoCoHaNeRe \\cite{fan2025cocohanere} proposes a gradient-based differentiable hard negative mechanism for code search contrastive learning, arguing that non-differentiable embedding-based negatives are ``slow and ineffective'' compared to gradient-based alternatives.\nHowever, CoCoHaNeRe's comparison does not evaluate simple static embedding-distance mining—selecting negatives by nearest-neighbor lookup in a frozen embedding space—in structural code retrieval settings.\nThis leaves open whether the complexity of gradient-based methods is truly necessary, and more broadly, how different negative mining strategies interact with the properties of the encoder being trained.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.\nOur central finding challenges the prevailing assumption that expensive gradient-based methods are required: simple static embedding-distance mining consistently improves retrieval (pilot evidence; pending M2 full confirmation), yielding +1.6--2.0 percentage points in Recall@1 over random baselines across two decoder-only encoders with distinct pretraining paradigms and representation geometries—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}.\nThese gains are achieved without gradient-based mechanisms, providing a direct counter-example to CoCoHaNeRe's premise in the structural code retrieval setting we study.\nWe note that CoCoHaNeRe's original argument targets the comparison between gradient-based and non-differentiable embedding negatives broadly; our counter-evidence is specific to structural code retrieval, where static embedding-distance mining proves sufficient.\nBeyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.\n\nOur contributions are as follows:\n\n1. We demonstrate that simple static embedding-distance hard negative mining consistently improves (pilot evidence; pending M2 full confirmation) contrastive code retrieval across two decoder-only encoders with distinct representation geometries, challenging the assumption that gradient-based hard negative methods \\cite{fan2025cocohanere} are necessary for effective code search.\n\n2. **[Exploratory observation]** We report that structure-grounded (dataflow) negatives interact with encoder representation geometry: negative difficulty margin analysis (+17% for Qwen2.5-Coder-3B, +28% for StarCoder2-3B) provides mechanistic evidence that the pretrained embedding space's degree of saturation mediates strategy effectiveness. Pilot data shows dataflow negatives underperform embedding mining on both encoders, with the gap modulated by representation geometry. This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.\n\n3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \\cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
OK, the existing introduction_v1.md has the old framing that uses "challenges" and "we demonstrate" which violates D049 constraints. I need to rewrite it completely with the softened D049 framing. Let me write the new version.

Let me draft the full content now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "ac1b782a-17bb-48a8-80bc-e309b0686716",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146XQML7yXFUiyDXVgf34Lv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3928,
      "cache_read_input_tokens": 43750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3928
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

_source line 29_

Existing v1 uses pre-D049 language ("challenges the prevailing assumption", "we demonstrate"). Rewriting with D049-compliant framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "b63057df-aa5b-4758-b5fe-59ba3331930f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146XQML7yXFUiyDXVgf34Lv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3928,
      "cache_read_input_tokens": 43750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3928
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

_source line 30_

<details open><summary>🔧 Tool call — Write · `toolu_01AweLTEKkU29aiMoqCd3dVy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
  "content": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by BM25 similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "7ec5e302-4edb-493e-8bb9-55a8397da537",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146XQML7yXFUiyDXVgf34Lv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3928,
      "cache_read_input_tokens": 43750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3928
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

_source line 31 · 2026-05-15T08:33:31.263Z_

<details><summary>↩ Tool result · `toolu_01AweLTEKkU29aiMoqCd3dVy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "29eb3b92-4019-4029-9696-ce3cf0485fb3",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
    "content": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by BM25 similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 30,
        "newStart": 1,
        "newLines": 34,
        "lines": [
          " # 1. Introduction",
          " ",
          "-Large-scale software maintenance increasingly depends on automatically identifying which source files require modification given a bug report or issue description.",
          "-Benchmarks such as SWE-bench \\cite{jimenez2024swebench} formalize this as a retrieval problem over repositories containing hundreds or thousands of files, and recent systems tackle it through text-based retrieval \\cite{reddy2025swerank,xie2025swefixer}, agent-based interactive localization \\cite{yang2024sweagent,xia2024agentless}, or combinations thereof.",
          "-A common assumption underlying these approaches is that textual similarity between an issue description and a source file signals relevance.",
          "-In practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.",
          "-This mismatch is particularly acute in large repositories where naming conventions are reused across unrelated modules, making retrieval that relies solely on text vulnerable to systematic false positives.",
          "+Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.",
          "+Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.",
          "+These approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.",
          "+Yet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.",
          "+Despite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.",
          " ",
          "-Two largely independent lines of work have sought to address this limitation, each with a significant gap.",
          "-First, a growing body of methods leverages code structure graphs at inference time.",
          "-LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ LLM agents to navigate repository-level graphs during fault localization; CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} provide graph database interfaces for structural code navigation; GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate control-flow or data-dependence edges—though both remain intra-procedural in scope.",
          "-These methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.",
          "-Second, hard negative mining—selecting challenging negative examples for contrastive training—is known to substantially impact dense retrieval quality \\cite{karpukhin2020dpr,xiong2021ance}, yet has received limited systematic study in the code domain.",
          "-CoCoHaNeRe \\cite{fan2025cocohanere} proposes a gradient-based differentiable hard negative mechanism for code search contrastive learning, arguing that non-differentiable embedding-based negatives are ``slow and ineffective'' compared to gradient-based alternatives.",
          "-However, CoCoHaNeRe's comparison does not evaluate simple static embedding-distance mining—selecting negatives by nearest-neighbor lookup in a frozen embedding space—in structural code retrieval settings.",
          "-This leaves open whether the complexity of gradient-based methods is truly necessary, and more broadly, how different negative mining strategies interact with the properties of the encoder being trained.",
          "+In open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.",
          "+DPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.",
          "+These methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.",
          "+In the code domain, however, the picture is less clear.",
          "+CoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''",
          "+This finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?",
          " ",
          "-We present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.",
          "-Our central finding challenges the prevailing assumption that expensive gradient-based methods are required: simple static embedding-distance mining consistently improves retrieval (pilot evidence; pending M2 full confirmation), yielding +1.6--2.0 percentage points in Recall@1 over random baselines across two decoder-only encoders with distinct pretraining paradigms and representation geometries—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}.",
          "-These gains are achieved without gradient-based mechanisms, providing a direct counter-example to CoCoHaNeRe's premise in the structural code retrieval setting we study.",
          "-We note that CoCoHaNeRe's original argument targets the comparison between gradient-based and non-differentiable embedding negatives broadly; our counter-evidence is specific to structural code retrieval, where static embedding-distance mining proves sufficient.",
          "-Beyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.",
          "+We observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.",
          "+This structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.",
          "+We operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by BM25 similarity.",
          "+Crucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.",
          "+This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.",
          " ",
          "+Our systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.",
          "+First, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.",
          "+This establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.",
          "+Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.",
          "+We report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.",
          "+",
          " Our contributions are as follows:",
          " ",
          "-1. We demonstrate that simple static embedding-distance hard negative mining consistently improves (pilot evidence; pending M2 full confirmation) contrastive code retrieval across two decoder-only encoders with distinct representation geometries, challenging the assumption that gradient-based hard negative methods \\cite{fan2025cocohanere} are necessary for effective code search.",
          "+1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.",
          " ",
          "-2. **[Exploratory observation]** We report that structure-grounded (dataflow) negatives interact with encoder representation geometry: negative difficulty margin analysis (+17% for Qwen2.5-Coder-3B, +28% for StarCoder2-3B) provides mechanistic evidence that the pretrained embedding space's degree of saturation mediates strategy effectiveness. Pilot data shows dataflow negatives underperform embedding mining on both encoders, with the gap modulated by representation geometry. This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.",
          "+2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.",
          " ",
          "-3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \\cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.",
          "+3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation."
        ]
      }
    ],
    "originalFile": "# 1. Introduction\n\nLarge-scale software maintenance increasingly depends on automatically identifying which source files require modification given a bug report or issue description.\nBenchmarks such as SWE-bench \\cite{jimenez2024swebench} formalize this as a retrieval problem over repositories containing hundreds or thousands of files, and recent systems tackle it through text-based retrieval \\cite{reddy2025swerank,xie2025swefixer}, agent-based interactive localization \\cite{yang2024sweagent,xia2024agentless}, or combinations thereof.\nA common assumption underlying these approaches is that textual similarity between an issue description and a source file signals relevance.\nIn practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.\nThis mismatch is particularly acute in large repositories where naming conventions are reused across unrelated modules, making retrieval that relies solely on text vulnerable to systematic false positives.\n\nTwo largely independent lines of work have sought to address this limitation, each with a significant gap.\nFirst, a growing body of methods leverages code structure graphs at inference time.\nLocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ LLM agents to navigate repository-level graphs during fault localization; CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} provide graph database interfaces for structural code navigation; GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate control-flow or data-dependence edges—though both remain intra-procedural in scope.\nThese methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.\nSecond, hard negative mining—selecting challenging negative examples for contrastive training—is known to substantially impact dense retrieval quality \\cite{karpukhin2020dpr,xiong2021ance}, yet has received limited systematic study in the code domain.\nCoCoHaNeRe \\cite{fan2025cocohanere} proposes a gradient-based differentiable hard negative mechanism for code search contrastive learning, arguing that non-differentiable embedding-based negatives are ``slow and ineffective'' compared to gradient-based alternatives.\nHowever, CoCoHaNeRe's comparison does not evaluate simple static embedding-distance mining—selecting negatives by nearest-neighbor lookup in a frozen embedding space—in structural code retrieval settings.\nThis leaves open whether the complexity of gradient-based methods is truly necessary, and more broadly, how different negative mining strategies interact with the properties of the encoder being trained.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.\nOur central finding challenges the prevailing assumption that expensive gradient-based methods are required: simple static embedding-distance mining consistently improves retrieval (pilot evidence; pending M2 full confirmation), yielding +1.6--2.0 percentage points in Recall@1 over random baselines across two decoder-only encoders with distinct pretraining paradigms and representation geometries—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}.\nThese gains are achieved without gradient-based mechanisms, providing a direct counter-example to CoCoHaNeRe's premise in the structural code retrieval setting we study.\nWe note that CoCoHaNeRe's original argument targets the comparison between gradient-based and non-differentiable embedding negatives broadly; our counter-evidence is specific to structural code retrieval, where static embedding-distance mining proves sufficient.\nBeyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.\n\nOur contributions are as follows:\n\n1. We demonstrate that simple static embedding-distance hard negative mining consistently improves (pilot evidence; pending M2 full confirmation) contrastive code retrieval across two decoder-only encoders with distinct representation geometries, challenging the assumption that gradient-based hard negative methods \\cite{fan2025cocohanere} are necessary for effective code search.\n\n2. **[Exploratory observation]** We report that structure-grounded (dataflow) negatives interact with encoder representation geometry: negative difficulty margin analysis (+17% for Qwen2.5-Coder-3B, +28% for StarCoder2-3B) provides mechanistic evidence that the pretrained embedding space's degree of saturation mediates strategy effectiveness. Pilot data shows dataflow negatives underperform embedding mining on both encoders, with the gap modulated by representation geometry. This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.\n\n3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \\cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 32_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "877bc12e-5ff3-4ee4-a21e-d0811fa3fd6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ci9yiT5NUxWoF7e8adwF5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 47678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LWTeMayrwQXXFCNFv1UCto`</summary>

```json
{
  "query": "register_artifact",
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
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "30de6c4f-b02f-4275-962c-0d0eaa6ff6a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ci9yiT5NUxWoF7e8adwF5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 47678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 34 · 2026-05-15T08:33:34.450Z_

<details><summary>↩ Tool result · `toolu_01LWTeMayrwQXXFCNFv1UCto`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "6f168336-5ed0-49e7-8f8c-59f91c017d26",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LNvqyxVJZGG6dmGULb3stz`</summary>

```json
{
  "query": "artifact register",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "10d18c7d-3b29-49b4-af70-feeed107e278",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqksapM4SoLRPiGG59AT4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 98,
      "cache_read_input_tokens": 49323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 98
      },
      "output_tokens": 64,
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

_source line 36 · 2026-05-15T08:33:36.737Z_

<details><summary>↩ Tool result · `toolu_01LNvqyxVJZGG6dmGULb3stz`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "4b40ecc9-186e-4815-b7a5-4e13dcea10bc",
  "tool_use_result": {
    "matches": [],
    "query": "artifact register",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016HVRNUoZdxUww2WkKQALZs`</summary>

```json
{
  "query": "register",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "45e2affa-f7f3-46ef-998f-a5e1d6554074",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PVuqFhQC58H9vF3EmVect",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91,
      "cache_read_input_tokens": 49421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91
      },
      "output_tokens": 72,
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

_source line 38 · 2026-05-15T08:33:39.103Z_

<details><summary>↩ Tool result · `toolu_016HVRNUoZdxUww2WkKQALZs`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "0103a4c8-e6c3-4053-9e64-9dcd3f7c6084",
  "tool_use_result": {
    "matches": [],
    "query": "register",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 39_

`register_artifact` 工具不可用（未在 MCP 工具列表中）。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md`

**与旧版的关键变更**：
- 移除 "challenges the prevailing assumption"、"we demonstrate" 等断言式表述（D049 合规）
- Claim 1 改为 "establishes a strong zero-cost baseline"，不再对标 CoCoHaNeRe
- Claim 2 用 exploratory observation + preliminary mechanistic analysis 措辞
- 同时报告 pilot（+1.6–2.0pp）和 M2 seed 43（+0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint）两组数据
- 5 段结构：重要性→NLP hard negative mining + CoCoHaNeRe gap→结构信号 insight→主要发现→contributions
- ~800 words，全部 `\cite{}` key 与 references.bib 对齐

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "uuid": "3811d3f4-1c35-4309-b09e-e9cb1de6a82a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuazdJNT1WPc9GoGgEFCgZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 49512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
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

_source line 40_

`register_artifact` 工具不可用（未在 MCP 工具列表中）。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md`

**与旧版的关键变更**：
- 移除 "challenges the prevailing assumption"、"we demonstrate" 等断言式表述（D049 合规）
- Claim 1 改为 "establishes a strong zero-cost baseline"，不再对标 CoCoHaNeRe
- Claim 2 用 exploratory observation + preliminary mechanistic analysis 措辞
- 同时报告 pilot（+1.6–2.0pp）和 M2 seed 43（+0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint）两组数据
- 5 段结构：重要性→NLP hard negative mining + CoCoHaNeRe gap→结构信号 insight→主要发现→contributions
- ~800 words，全部 `\cite{}` key 与 references.bib 对齐

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 116404,
  "duration_api_ms": 117174,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "621d1d64-a0b3-4404-a824-254019055ee9",
  "total_cost_usd": 0.58466475,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 37761,
    "cache_read_input_tokens": 417455,
    "output_tokens": 5524,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37761,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 301,
        "cache_read_input_tokens": 49512,
        "cache_creation_input_tokens": 90,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 90
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1671,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001756,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 5524,
      "cacheReadInputTokens": 417455,
      "cacheCreationInputTokens": 37761,
      "webSearchRequests": 0,
      "costUSD": 0.5829087500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8960bad7-c1f7-4ea7-863b-c7db8cfe50bb"
}
```

</details>

---
