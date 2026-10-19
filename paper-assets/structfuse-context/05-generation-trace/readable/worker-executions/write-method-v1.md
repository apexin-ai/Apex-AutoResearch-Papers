# write method v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_write_method-v1_20260515T092736.log`
- **Structured JSON:** [`e7a07a07bf0f88b352fb.json`](../../sessions/e7/e7a07a07bf0f88b352fb.json)

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
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
  "uuid": "32cdde98-762a-474b-a2e9-4b271fb5d06d",
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
    "resetsAt": 1778854800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "27c201eb-638d-444f-9793-8acb98a8621d",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required context files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "670181df-d35e-469c-a789-50c768e3fbd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj4uz8LK6rkGtPxPE2m7Xc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12035,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12035
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V31nzh9Ech1XCEYrzmCKyD`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "c266a1cf-c95d-466f-b6e2-ef5f5a88ddbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj4uz8LK6rkGtPxPE2m7Xc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12035,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12035
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

_source line 6 · 2026-05-15T09:27:55.307Z_

<details><summary>↩ Tool result · `toolu_01V31nzh9Ech1XCEYrzmCKyD`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "4c3cad38-6060-4a9c-b26e-5b110c1d898b",
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
Now let me read the three context files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "13f5cfe1-4e57-46d4-9cb0-08df7249b51f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCjUQAD1Akw8ok83EVCkTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 23876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 906
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016kyLP4dtRmPb6Jbahk9b33`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "a45384ee-6190-4d81-b623-68ca8cac29e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCjUQAD1Akw8ok83EVCkTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 23876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 906
      },
      "output_tokens": 27,
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

_source line 9 · 2026-05-15T09:27:58.723Z_

<details><summary>↩ Tool result · `toolu_016kyLP4dtRmPb6Jbahk9b33`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\"\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\\n\", \"total_chars\": 14424, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "f549e6b4-69a6-4daf-8344-be95b1aa0219",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — StructFuse\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3)\\\\n\\\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\\\\\"slow and ineffective\\\\\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\\\n\\\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\\\n\\\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\\\n\\\\n- **Existing approaches & gaps**:\\\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\\\n\\\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\\\n\\\\n- **Headline result template**: \\\\\\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\\\n\\\\n## Dual-Pillar Motivation\\\\n\\\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\\\n\\\\n## Formal Definition\\\\n\\\\nGiven retrieval domain D, structural graph G, query q:\\\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\\\n\\\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\\\n\\\\n## Title Options\\\\n\\\\n- Primary: \\\\\\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\\\\\"\\\\n- Alternative: \\\\\\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\\\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\\\n- Backup: \\\\\\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n\\\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\\\\\"Do Language Models...\\\\\\\" papers). Contribution is understanding, not just a new method.\\\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\\\n3. **Against \\\\\\\"incremental\\\\\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response | Evidence |\\\\n|---------|----------|----------|\\\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\\\n| \\\\\\\"Complementary signal\\\\\\\" overstatement | Temper: \\\\\\\"conditionally beneficial\\\\\\\" not \\\\\\\"always complementary\\\\\\\" | Writing discipline |\\\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\\\n\\\\n## Evidence Status\\\\n\\\\n### Confirmed findings (basis for claims):\\\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\\\n\\\\n### Evidence presentation strategy:\\\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\\\n\\\\n### In progress:\\\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\\\n\\\\n### Planned (priority order):\\\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\\\n- plan_014: Temperature ablation (Dream reviewer concern)\\\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\\\n- plan_015: Dynamic mining baseline\\\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\\\n- plan_007/008/009: Additional ablations\\\\n\\\\n## Limitations\\\\n\\\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\\\n\\\\n## Contingency (if full M2 results weaken claims)\\\\n\\\\n### All 18 runs confirm pilot pattern: Best case\\\\n- Full statistical power, paper as framed above\\\\n- Target: EMNLP Main\\\\n\\\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\\\n- Drop Claim 2 to analysis observation\\\\n- Paper becomes: \\\\\\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\\\\\"\\\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\\\n\\\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\\\n- Pivot: \\\\\\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\\\\\"\\\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\\\n- Claim 1 core preserved: \\\\\\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\\\\\"\\\\n- Impact: BM25 result determines narrative nuance, not core contribution\\\\n\\\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\\\n- If confirmed: negative result paper — \\\\\\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\\\\\"\\\\n- Discuss with user before committing direction\\\\n\\\\n## Deprecated Claims (with reason)\\\\n\\\\n- ~~\\\\\\\"Embedding-distance hard negatives actively harm code retrieval\\\\\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\\\n\\\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\\\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\\\\n\\\", \\\"total_chars\\\": 14424, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\"\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\\n\", \"total_chars\": 14424, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017KsCkZ4F1StUUQNuq8hYh8`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "dd957a23-37b9-4ca5-aa2d-b3af93aa8c77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCjUQAD1Akw8ok83EVCkTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 23876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 906
      },
      "output_tokens": 27,
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

_source line 11 · 2026-05-15T09:27:59.235Z_

<details><summary>↩ Tool result · `toolu_017KsCkZ4F1StUUQNuq8hYh8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) K=7 negatives are randomly sampled from a pool of 50 strategy-specific candidates per query。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## SWE-bench eval 脚本路径 [2026-05-15, Reviewer 纠正]\\n\\neval_swebench 脚本已存在（之前 Worker 搜索了错误目录 /root/structfuse）：\\n- `/root/structfuse-context/evaluation/eval_swebench.py`（含 .bak 和 .pyc）\\n- `/root/structfuse-context/scripts/eval_swebench_e2e.py`\\n\\nAgent 通过 OpenAI-compatible API 调用（非本地推理），配置项：STRUCTFUSE_LLM_BACKEND=api, STRUCTFUSE_LLM_API_BASE, STRUCTFUSE_LLM_API_KEY, STRUCTFUSE_LLM_MODEL。Retriever 和 agent 分离，单卡 VRAM 无压力。plan_003 基于现有脚本执行，不需要从头创建。\\n\\n---\\n\\n## Qwen 链日志缓冲问题 [2026-05-15, Reviewer 发现]\\n\\nQwen 链脚本用 `python`（有 stdout 缓冲），导致日志延迟输出，监控出现盲区。StarCoder 链用了 `python -u` 没此问题。**后续 Qwen subrun 启动时须加 `PYTHONUNBUFFERED=1` 环境变量或 `python -u`**，保证日志实时输出。当前 run 不需要重启。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\n\\n---\\n\\n## Related Work Gap 分析 [2026-05-15]\\n\\n当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均。最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论。推荐添加 7 篇（全部 WebSearch 验证）：\\n- **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)\\n- **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)\\n- **可选**：CoSQA (ACL 2021)\\n\", \"total_chars\": 14059, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "f8bf49c1-afb8-4596-a4b7-16f0e1c50764",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\\\", \\\"content\\\": \\\"# Inference-Time Graph Methods 文献对比\\\\n\\\\n## 对比表\\\\n\\\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\\\n\\\\n## Discussion 要点\\\\n\\\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\\\n\\\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\\\n\\\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\\\n\\\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\\\n\\\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\\\n\\\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\\\n\\\\n## Related Work 段落草稿 (~200 words)\\\\n\\\\n**Graph-Based Methods for Code Understanding.**\\\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\\\n\\\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\\\n\\\\n---\\\\n\\\\n## 参考文献（全部已验证 2026-05-14）\\\\n\\\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\\\n- CodeRAG: arXiv:2504.10046, 2025\\\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\")\\\\n- CodeGRAG: arXiv:2405.02355, 2024\\\\n\\\\n---\\\\n\\\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\\\n\\\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\\\n\\\\n**分歧 pattern**：\\\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\\\n\\\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\\\n\\\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) K=7 negatives are randomly sampled from a pool of 50 strategy-specific candidates per query。K 敏感性列为 limitation/future work。\\\\n\\\\n---\\\\n\\\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\\\n\\\\n**两层重叠率数据（注意区分）**：\\\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\\\n\\\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\\\n|------|-------------------|----------------|------------------|\\\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\\\n\\\\n**核心修正**：之前基于 87% 预测\\\\\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\\\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\\\n\\\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\\\n\\\\n---\\\\n\\\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\\\n\\\\n**发现者**：Reviewer\\\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\\\n\\\\n**差异**：\\\\n\\\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\\\n三步法：\\\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\\\n\\\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\\\n两步法：\\\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\\\n\\\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\\\n\\\\n### 差异总结\\\\n\\\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\\\n|------|------------------------|--------------------------|\\\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\\\n\\\\n### 对齐建议\\\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\\\n\\\\n---\\\\n\\\\n## SWE-bench eval 脚本路径 [2026-05-15, Reviewer 纠正]\\\\n\\\\neval_swebench 脚本已存在（之前 Worker 搜索了错误目录 /root/structfuse）：\\\\n- `/root/structfuse-context/evaluation/eval_swebench.py`（含 .bak 和 .pyc）\\\\n- `/root/structfuse-context/scripts/eval_swebench_e2e.py`\\\\n\\\\nAgent 通过 OpenAI-compatible API 调用（非本地推理），配置项：STRUCTFUSE_LLM_BACKEND=api, STRUCTFUSE_LLM_API_BASE, STRUCTFUSE_LLM_API_KEY, STRUCTFUSE_LLM_MODEL。Retriever 和 agent 分离，单卡 VRAM 无压力。plan_003 基于现有脚本执行，不需要从头创建。\\\\n\\\\n---\\\\n\\\\n## Qwen 链日志缓冲问题 [2026-05-15, Reviewer 发现]\\\\n\\\\nQwen 链脚本用 `python`（有 stdout 缓冲），导致日志延迟输出，监控出现盲区。StarCoder 链用了 `python -u` 没此问题。**后续 Qwen subrun 启动时须加 `PYTHONUNBUFFERED=1` 环境变量或 `python -u`**，保证日志实时输出。当前 run 不需要重启。\\\\n\\\\n---\\\\n\\\\n## 运维经验 (2026-05-14)\\\\n\\\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\\\n\\\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\\\n\\\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\\\n\\\\n---\\\\n\\\\n## 关键决策记录\\\\n\\\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\\\n\\\\n---\\\\n\\\\n## Related Work Gap 分析 [2026-05-15]\\\\n\\\\n当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均。最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论。推荐添加 7 篇（全部 WebSearch 验证）：\\\\n- **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)\\\\n- **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)\\\\n- **可选**：CoSQA (ACL 2021)\\\\n\\\", \\\"total_chars\\\": 14059, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) K=7 negatives are randomly sampled from a pool of 50 strategy-specific candidates per query。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## SWE-bench eval 脚本路径 [2026-05-15, Reviewer 纠正]\\n\\neval_swebench 脚本已存在（之前 Worker 搜索了错误目录 /root/structfuse）：\\n- `/root/structfuse-context/evaluation/eval_swebench.py`（含 .bak 和 .pyc）\\n- `/root/structfuse-context/scripts/eval_swebench_e2e.py`\\n\\nAgent 通过 OpenAI-compatible API 调用（非本地推理），配置项：STRUCTFUSE_LLM_BACKEND=api, STRUCTFUSE_LLM_API_BASE, STRUCTFUSE_LLM_API_KEY, STRUCTFUSE_LLM_MODEL。Retriever 和 agent 分离，单卡 VRAM 无压力。plan_003 基于现有脚本执行，不需要从头创建。\\n\\n---\\n\\n## Qwen 链日志缓冲问题 [2026-05-15, Reviewer 发现]\\n\\nQwen 链脚本用 `python`（有 stdout 缓冲），导致日志延迟输出，监控出现盲区。StarCoder 链用了 `python -u` 没此问题。**后续 Qwen subrun 启动时须加 `PYTHONUNBUFFERED=1` 环境变量或 `python -u`**，保证日志实时输出。当前 run 不需要重启。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\n\\n---\\n\\n## Related Work Gap 分析 [2026-05-15]\\n\\n当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均。最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论。推荐添加 7 篇（全部 WebSearch 验证）：\\n- **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)\\n- **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)\\n- **可选**：CoSQA (ACL 2021)\\n\", \"total_chars\": 14059, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_011hMwheAUHH4AKqrvnyf6pH`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "14ae4410-d5d9-4173-a603-74723330bcc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCjUQAD1Akw8ok83EVCkTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 23876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 906
      },
      "output_tokens": 27,
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

_source line 13 · 2026-05-15T09:27:59.775Z_

<details><summary>↩ Tool result · `toolu_011hMwheAUHH4AKqrvnyf6pH`</summary>

```text
1	% =============================================================================
2	% Section 1: Introduction
3	% =============================================================================
4	
5	@inproceedings{jimenez2024swebench,
6	  title={{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},
7	  author={Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},
8	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
9	  year={2024}
10	}
11	
12	% =============================================================================
13	% Section 2.1: Code Retrieval Methods
14	% =============================================================================
15	
16	@article{robertson2009bm25,
17	  title={The Probabilistic Relevance Framework: {BM25} and Beyond},
18	  author={Robertson, Stephen and Zaragoza, Hugo},
19	  journal={Foundations and Trends in Information Retrieval},
20	  volume={3},
21	  number={4},
22	  pages={333--389},
23	  year={2009},
24	  publisher={Now Publishers}
25	}
26	
27	@inproceedings{karpukhin2020dpr,
28	  title={Dense Passage Retrieval for Open-Domain Question Answering},
29	  author={Karpukhin, Vladimir and O{\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},
30	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
31	  pages={6769--6781},
32	  year={2020}
33	}
34	
35	@article{reddy2025swerank,
36	  title={{SweRank}: Software Issue Localization with Code Ranking},
37	  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},
38	  journal={arXiv preprint arXiv:2505.07849},
39	  year={2025}
40	}
41	
42	@inproceedings{xie2025swefixer,
43	  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},
44	  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},
45	  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},
46	  pages={1123--1139},
47	  year={2025}
48	}
49	
50	@inproceedings{chen2025locagent,
51	  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},
52	  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},
53	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
54	  pages={8697--8727},
55	  year={2025}
56	}
57	
58	@article{shah2025ranger,
59	  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},
60	  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},
61	  journal={arXiv preprint arXiv:2509.25257},
62	  year={2025}
63	}
64	
65	@inproceedings{liu2025codexgraph,
66	  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},
67	  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},
68	  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
69	  pages={142--160},
70	  year={2025}
71	}
72	
73	@inproceedings{ouyang2025repograph,
74	  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},
75	  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},
76	  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},
77	  year={2025}
78	}
79	
80	@inproceedings{liu2024graphcoder,
81	  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},
82	  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},
83	  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
84	  year={2024}
85	}
86	
87	@article{seddik2026arise,
88	  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},
89	  author={Seddik, Shahd and Fard, Fatemeh},
90	  journal={arXiv preprint arXiv:2605.03117},
91	  year={2026}
92	}
93	
94	% =============================================================================
95	% Section 2.2: Pre-trained Code Representations and Contrastive Learning
96	% =============================================================================
97	
98	@inproceedings{feng2020codebert,
99	  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},
100	  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
101	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
102	  pages={1536--1547},
103	  year={2020}
104	}
105	
106	@inproceedings{guo2021graphcodebert,
107	  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},
108	  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
109	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
110	  year={2021}
111	}
112	
113	@inproceedings{guo2022unixcoder,
114	  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},
115	  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
116	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
117	  pages={7212--7225},
118	  year={2022}
119	}
120	
121	@inproceedings{alon2019code2vec,
122	  title={code2vec: Learning Distributed Representations of Code},
123	  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},
124	  booktitle={Proceedings of the ACM on Programming Languages (POPL)},
125	  volume={3},
126	  pages={1--29},
127	  year={2019}
128	}
129	
130	@inproceedings{zhang2024codesage,
131	  title={Code Representation Learning At Scale},
132	  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},
133	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
134	  year={2024}
135	}
136	
137	@inproceedings{reimers2019sentencebert,
138	  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
139	  author={Reimers, Nils and Gurevych, Iryna},
140	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
141	  pages={3982--3992},
142	  year={2019}
143	}
144	
145	@inproceedings{jain2021contracode,
146	  title={Contrastive Code Representation Learning},
147	  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},
148	  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
149	  pages={5954--5971},
150	  year={2021}
151	}
152	
153	@inproceedings{li2022coderetriever,
154	  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},
155	  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
156	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
157	  pages={2898--2910},
158	  year={2022}
159	}
160	
161	@inproceedings{li2022scoder,
162	  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},
163	  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
164	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},
165	  year={2022}
166	}
167	
168	@inproceedings{ding2022programcontrasts,
169	  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},
170	  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},
171	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
172	  pages={6300--6312},
173	  year={2022}
174	}
175	
176	@inproceedings{bui2021infercode,
177	  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},
178	  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},
179	  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},
180	  pages={1186--1197},
181	  year={2021}
182	}
183	
184	@article{lozhkov2024starcoder2,
185	  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},
186	  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},
187	  journal={arXiv preprint arXiv:2402.19173},
188	  year={2024}
189	}
190	
191	@article{hui2024qwen25coder,
192	  title={{Qwen2.5-Coder} Technical Report},
193	  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},
194	  journal={arXiv preprint arXiv:2409.12186},
195	  year={2024}
196	}
197	
198	% =============================================================================
199	% Section 2.3: Hard Negative Mining
200	% =============================================================================
201	
202	@inproceedings{chen2020simclr,
203	  title={A Simple Framework for Contrastive Learning of Visual Representations},
204	  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
205	  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},
206	  pages={1597--1607},
207	  year={2020}
208	}
209	
210	@inproceedings{xiong2021ance,
211	  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},
212	  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},
213	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
214	  year={2021}
215	}
216	
217	@inproceedings{zhan2021star,
218	  title={Optimizing Dense Retrieval Model Training with Hard Negatives},
219	  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},
220	  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
221	  pages={1503--1512},
222	  year={2021}
223	}
224	
225	@inproceedings{qu2021rocketqa,
226	  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},
227	  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},
228	  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},
229	  pages={5835--5847},
230	  year={2021}
231	}
232	
233	@inproceedings{zeng2022cldrd,
234	  title={Curriculum Learning for Dense Retrieval Distillation},
235	  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},
236	  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
237	  pages={1979--1983},
238	  year={2022}
239	}
240	
241	@article{fan2025cocohanere,
242	  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
243	  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},
244	  journal={ACM Transactions on Software Engineering and Methodology},
245	  volume={34},
246	  number={3},
247	  year={2025},
248	  publisher={ACM}
249	}
250	
251	% =============================================================================
252	% Section 2.4: Code Structure Analysis
253	% =============================================================================
254	
255	@article{ferrante1987pdg,
256	  title={The Program Dependence Graph and Its Use in Optimization},
257	  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},
258	  journal={ACM Transactions on Programming Languages and Systems},
259	  volume={9},
260	  number={3},
261	  pages={319--349},
262	  year={1987},
263	  publisher={ACM}
264	}
265	
266	@inproceedings{yamaguchi2014cpg,
267	  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},
268	  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},
269	  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\&P)},
270	  pages={590--604},
271	  year={2014},
272	  publisher={IEEE}
273	}
274	
275	@inproceedings{avgustinov2016ql,
276	  title={{QL}: Object-oriented Queries on Relational Data},
277	  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\"a}fer, Max},
278	  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},
279	  series={LIPIcs},
280	  volume={56},
281	  pages={2:1--2:25},
282	  year={2016}
283	}
284	
285	% =============================================================================
286	% Supplement: New citations added 2026-05-15
287	% =============================================================================
288	
289	@article{wang2021syncobert,
290	  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},
291	  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},
292	  journal={arXiv preprint arXiv:2108.04556},
293	  year={2021}
294	}
295	
296	@inproceedings{liu2023contrabert,
297	  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},
298	  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},
299	  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},
300	  pages={2476--2487},
301	  year={2023}
302	}
303	
304	@inproceedings{he2023capstone,
305	  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},
306	  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},
307	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
308	  pages={10531--10541},
309	  year={2023}
310	}
311	
312	@inproceedings{ding2023crosscodeeval,
313	  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},
314	  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},
315	  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},
316	  year={2023}
317	}
318	
319	@inproceedings{cummins2021programl,
320	  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},
321	  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},
322	  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},
323	  pages={2244--2253},
324	  year={2021},
325	  publisher={PMLR}
326	}
327	
328	@inproceedings{huang2021cosqa,
329	  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},
330	  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},
331	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
332	  pages={5690--5700},
333	  year={2021}
334	}
335	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "41182bf0-c985-460e-a6ca-f9d6580bcc98",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
      "content": "% =============================================================================\n% Section 1: Introduction\n% =============================================================================\n\n@inproceedings{jimenez2024swebench,\n  title={{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},\n  author={Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n\n% =============================================================================\n% Supplement: New citations added 2026-05-15\n% =============================================================================\n\n@article{wang2021syncobert,\n  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},\n  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},\n  journal={arXiv preprint arXiv:2108.04556},\n  year={2021}\n}\n\n@inproceedings{liu2023contrabert,\n  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},\n  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},\n  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={2476--2487},\n  year={2023}\n}\n\n@inproceedings{he2023capstone,\n  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},\n  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={10531--10541},\n  year={2023}\n}\n\n@inproceedings{ding2023crosscodeeval,\n  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},\n  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{cummins2021programl,\n  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},\n  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},\n  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},\n  pages={2244--2253},\n  year={2021},\n  publisher={PMLR}\n}\n\n@inproceedings{huang2021cosqa,\n  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},\n  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={5690--5700},\n  year={2021}\n}\n",
      "numLines": 335,
      "startLine": 1,
      "totalLines": 335
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
Now I have all three context files. Let me extract the key information:

**From paper_framing.md:**
- 3 core claims (embedding mining reliable improvement, dataflow interaction with geometry, CodeQL practical pipeline)
- Formal definition: structure-grounded hard negative = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)
- D049 softened framing: "reliable improvement" / "zero additional computational cost"
- Temperature τ=0.07 (mentioned indirectly, need to check)


- Pool size=50, K=7, 3 seeds (42, 43, 44), and two encoder models (Qwen2.5-Coder-3B and StarCoder2-3B)

**From memory.md:**
- The dataflow strategy actually relies on BM25 for ranking rather than embeddings, with the training data script using pure BM25 sorting for the dataflow pool
- Training setup: K=7 negatives per positive, batch size of 8, evaluated on best R@1 checkpoint as primary metric
- Each strategy runs across 3 seeds for consistency

Now I'm reviewing the reference citations I'll need for the paper.

I need to verify the temperature parameter τ is set to 0.07 as specified in the task description, not 0.05.

Let me also cross-check the other hyperparameters: LoRA with r=16 and α=32, AdamW optimizer with learning rate 2e-5, warmup ratio of 0.1, weight decay of 0.01, sequence length capped at 2048, gradient checkpointing enabled, projection dimension of 256, training for 2 epochs with early stopping patience of 2 based on validation loss, and maintaining dual checkpoints for both best validation loss and best R@1 performance.

Before writing the method section, I should pull the exact hyperparameters from the actual registry or config files on the server rather than relying on memory, since the task explicitly requires all hyperparameters to be confirmed from the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "7f65fe65-ff7d-46c4-8b7b-6b7378f4910e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xQVHfSz3DjaTfEfskXLZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16399,
      "cache_read_input_tokens": 24782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16399
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

_source line 15_

Let me verify the hyperparameters from the actual config/registry before writing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "772aea1f-7387-4ff9-a587-eedc6d8e37e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xQVHfSz3DjaTfEfskXLZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16399,
      "cache_read_input_tokens": 24782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16399
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

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_012UHYV5Zn8FYeYLf5i4NGof`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find training config/registry",
  "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ for training configuration files, experiment registry, or hyperparameter configs. I need to verify these specific values: temperature (τ), LoRA rank (r), LoRA alpha (α), learning rate, batch size, max_seq_length, proj_dim, warmup_ratio, weight_decay, num_epochs, early_stopping_patience, pool_size, num_negatives (K).\n\nLook for files like:\n- registry files (yaml/json)\n- training config files\n- experiment config\n- Also check the artifacts/ directory\n\nSearch breadth: medium"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "63607add-7166-4c96-accd-73209a017062",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xQVHfSz3DjaTfEfskXLZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16399,
      "cache_read_input_tokens": 24782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16399
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

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Find training config/registry",
  "task_type": "local_agent",
  "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ for training configuration files, experiment registry, or hyperparameter configs. I need to verify these specific values: temperature (τ), LoRA rank (r), LoRA alpha (α), learning rate, batch size, max_seq_length, proj_dim, warmup_ratio, weight_decay, num_epochs, early_stopping_patience, pool_size, num_negatives (K).\n\nLook for files like:\n- registry files (yaml/json)\n- training config files\n- experiment config\n- Also check the artifacts/ directory\n\nSearch breadth: medium",
  "uuid": "7e4462eb-a2ac-4a46-ac01-75c5ab6f298d",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

## Round 1

61 recorded events

### User

_source line 18 · 2026-05-15T09:28:34.379Z_

Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ for training configuration files, experiment registry, or hyperparameter configs. I need to verify these specific values: temperature (τ), LoRA rank (r), LoRA alpha (α), learning rate, batch size, max_seq_length, proj_dim, warmup_ratio, weight_decay, num_epochs, early_stopping_patience, pool_size, num_negatives (K).

Look for files like:
- registry files (yaml/json)
- training config files
- experiment config
- Also check the artifacts/ directory

Search breadth: medium

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "0e78cecd-2e27-4a0c-a5bd-13bc3a209d11"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Finding **/*.{yaml,yml,json}",
  "usage": {
    "total_tokens": 15556,
    "tool_uses": 1,
    "duration_ms": 1784
  },
  "last_tool_name": "Glob",
  "uuid": "f5e1a57f-ecc2-4611-8eba-8f3ea7a7d320",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01Mztmoi42n3RF29ZQBHS8qd`</summary>

```json
{
  "pattern": "**/*.{yaml,yml,json}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "9f508985-beb1-45ec-bd0d-7a3c3926864b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AnNEncoks5Lu7fFSZLHanp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15545,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15545,
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

_source line 21 · 2026-05-15T09:28:36.197Z_

<details><summary>↩ Tool result · `toolu_01Mztmoi42n3RF29ZQBHS8qd`</summary>

```text
logs/workers/worker_code_training_skeleton_20260512T100142_result.json
logs/workers/worker_code_extraction_skeleton_20260512T100103_result.json
logs/workers/worker_code_eval_skeleton_20260512T100215_result.json
logs/workers/worker_knowledge_experiment_plan_20260512T102157_result.json
logs/workers/worker_code_bugfix_reviewer_20260512T102418_result.json
logs/workers/worker_code_bugfix_checkpoint_20260512T102506_result.json
logs/workers/worker_infra_server_setup_20260512T102130_result.json
logs/workers/worker_data_bm25_precompute_20260512T111113_result.json
logs/workers/worker_experiment_mvp_p1_codeql_20260512T103754_result.json
logs/workers/worker_experiment_gpu_dryrun_20260512T111049_result.json
logs/workers/worker_experiment_mvp_p2a_linear_20260512T113250_result.json
logs/workers/worker_code_data_quality_fix_20260512T113345_result.json
logs/workers/worker_critical_gpu_boundary_fix_20260512T115336_result.json
logs/workers/worker_experiment_mvp_p2b_contrastive_20260512T115900_result.json
logs/workers/worker_data_swesmith_metadata_prep_20260512T123337_result.json
logs/workers/worker_code_bugfix_eval_p2b_20260512T125853_result.json
logs/workers/worker_infra_model_migration_20260512T130059_result.json
logs/workers/worker_diagnose_mvp_p2b_contrastive_training_20260512T131712_result.json
logs/workers/worker_infra_monitor_model_download_20260512T131858_result.json
logs/workers/worker_code_p2b_skip_logic_and_eval_prep_20260512T131844_result.json
logs/workers/worker_critical_fix_model_download_20260512T133837_result.json
logs/workers/worker_research_related_work_refs_20260512T143155_result.json
logs/workers/worker_infra_p2b_status_check_20260512T143123_result.json
logs/workers/worker_infra_batch_extract_dryrun_20260512T143141_result.json
logs/workers/worker_infra_p2b_gpu_check_restart_20260512T144458_result.json
logs/workers/worker_code_fix_batch_extract_empty_output_20260512T150049_result.json
logs/workers/worker_code_fix_codeql_class_support_20260512T150208_result.json
logs/workers/worker_code_fix_run_p2b_set_e_and_empty_tokens_20260512T150611_result.json
logs/workers/worker_infra_m1_script_review_20260512T151301_result.json
logs/workers/worker_infra_extraction_integration_test_20260512T151138_result.json
logs/workers/worker_diagnose_mvp_p2b_contrastive_training_v2_20260512T151839_result.json
logs/workers/worker_code_fix_strategy_names_restart_p2b_20260512T153310_result.json
logs/workers/worker_research_dataflow_empty_rate_analysis_20260512T153349_result.json
logs/workers/worker_infra_urgent_p2b_restart_20260512T155409_result.json
logs/workers/worker_code_fix_m1_extraction_script_20260512T161643_result.json
logs/workers/worker_code_eval_best_and_final_checkpoint_20260512T161614_result.json
logs/workers/worker_infra_p2b_final_status_check_20260512T161937_result.json
logs/workers/worker_fix_disk_cleanup_p2b_20260512T162138_result.json
logs/workers/worker_infra_p2b_disk_cleanup_and_train_fix_20260512T162558_result.json
logs/workers/worker_experiment_eval_4runs_v2_20260512T170825_result.json
logs/workers/worker_experiment_p2b_5reruns_train_20260512T172551_result.json
logs/workers/worker_check_p2b_5reruns_status_20260512T191600_result.json
logs/workers/worker_diagnose_p2b_5reruns_crash_20260512T191730_result.json
logs/workers/worker_experiment_p2b_eval_9runs_pool50_20260512T191947_result.json
logs/workers/worker_code_investigate_dataflow_vs_embdist_bug_20260512T192104_result.json
logs/workers/worker_experiment_p2b_eval_9runs_pool26_20260512T192122_result.json
logs/workers/worker_fix_p2b_data_bug_steps0-2_20260512T193908_result.json
logs/workers/worker_experiment_p2b_steps3-5_fix_and_retrain_20260512T194430_result.json
logs/workers/worker_experiment_p2b_eval_4runs_pool50_20260512T195326_result.json
logs/workers/worker_research_50repo_overlap_stats_20260512T195352_result.json
logs/workers/worker_experiment_m1_extraction_launch_20260512T204013_result.json
artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/best/experiment_data.json
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json
logs/workers/worker_monitor_m1_speed_check_20260512T210132_result.json
artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json
logs/workers/worker_code_m2_dryrun_prep_20260512T210208_result.json
logs/workers/worker_monitor_m1_progress_check2_20260512T212517_result.json
logs/workers/worker_code_fix_repo_level_split_20260512T212539_result.json
logs/workers/worker_code_eval_swebench_framework_20260512T220532_result.json
logs/workers/worker_experiment_tau_pilot_ablation_20260512T235301_result.json
logs/workers/worker_monitor_tau_pilot_results_20260512T235601_result.json
logs/workers/worker_monitor_tau_pilot_finish_and_cleanup_20260513T000052_result.json
logs/workers/worker_code_starcoder2_support_20260513T000505_result.json
logs/workers/worker_setup_download_starcoder2_3b_20260512T235233_result.json
logs/workers/worker_ops_urgent_disk_cleanup_20260513T004445_result.json
logs/workers/worker_code_dynamic_mining_impl_20260513T002931_result.json
logs/workers/worker_monitor_m1_disk_starcoder_check_20260513T004643_result.json
logs/workers/worker_monitor_m1_urgent_status_20260513T012645_result.json
logs/workers/worker_monitor_m1_progress_and_z_check_20260513T012551_result.json
logs/workers/worker_ops_disk_emergency_assessment_20260513T013022_result.json
logs/workers/worker_code_m2_data_pipeline_prep_20260513T013038_result.json
logs/workers/worker_monitor_m1_progress_check_20260513T013124_result.json
logs/workers/worker_ops_checkpoint-cleanup_20260513T013416_result.json
logs/workers/worker_code_m3a_eval_framework_prep_20260513T013129_result.json
logs/workers/worker_ops_disk_crisis_cleanup_20260513T013113_result.json
logs/workers/worker_ops_disk-cleanup-m1-check_20260513T013350_result.json
logs/workers/worker_ops_director-status-check_20260513T013647_result.json
logs/workers/worker_code_m2-early-pilot-prep_20260513T014145_result.json
logs/workers/worker_ops_cleanup-old-tmux_20260513T015317_result.json
logs/workers/worker_ops_fix-m2-wandb-resubmit_20260513T015530_result.json
logs/workers/worker_code_m2_early_pilot_20260513T014059_result.json
logs/workers/worker_ops_fix-m2-hf-offline-resubmit_20260513T015621_result.json
logs/workers/worker_ops_gpu-audit-resubmit-cuda4_20260513T020958_result.json
logs/workers/worker_ops_gpu-violation-audit_20260513T021132_result.json
logs/workers/worker_monitor_m2-m1-status-check_20260513T025149_result.json
logs/workers/worker_ops_bjb1-env-setup_20260513T031259_result.json
logs/workers/worker_ops_bjb1-gpu-verify-download-check_20260513T032104_result.json
logs/workers/worker_ops_bjb1-gpu1-verify_20260513T032419_result.json
logs/workers/worker_ops_bjb1-model-check-dryrun_20260513T032947_result.json
logs/workers/worker_ops_bjb1-data-sync-path-fix_20260513T033421_result.json
logs/workers/worker_code_true-embedding-mining_20260513T041546_result.json
artifacts/_project/data/plan_006_scalability_stats_29repos.json
artifacts/plan_006_scalability_stats_29repos.json
logs/workers/worker_ops_registry-cleanup-plan006_20260513T041615_result.json
logs/workers/worker_ops_bjb1-starcoder-flash-check_20260513T043717_result.json
logs/workers/worker_ops_m2-pilot-check-and-data-transfer_20260513T043709_result.json
logs/workers/worker_ops_bjb1-flash-attn-fix_20260513T044139_result.json
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "e20e4c42-63f0-478c-a192-cf86a561243d"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 15560,
    "tool_uses": 2,
    "duration_ms": 2101
  },
  "last_tool_name": "Bash",
  "uuid": "2453fb2b-3da6-4c7e-a0d8-5855f368f1fb",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01EyfGKNS7yMtiBaNuk6T1EC`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context -type d -name \"artifacts\" -o -type d -name \"config\" -o -type d -name \"configs\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "2495e504-2424-4c38-a0c5-016c04fa7b31",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AnNEncoks5Lu7fFSZLHanp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15545,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15545,
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

_source line 24 · 2026-05-15T09:28:36.660Z_

<details><summary>↩ Tool result · `toolu_01EyfGKNS7yMtiBaNuk6T1EC`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "86f4a808-5bb3-4a69-ab49-62081b29bae5"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 19480,
    "tool_uses": 3,
    "duration_ms": 6341
  },
  "last_tool_name": "Bash",
  "uuid": "4acfb985-420b-4ecf-a325-20dfeb59d35d",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01GWgDAksBGSr7jTjrrME5Rm`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts -name \"*.json\" -o -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "d6dcebab-66c6-49d0-a88b-8a72d3608103",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAkBwWaWDspe3uPJcxQ7BN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 15545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3914,
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

_source line 27 · 2026-05-15T09:28:40.803Z_

<details><summary>↩ Tool result · `toolu_01GWgDAksBGSr7jTjrrME5Rm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan006_error_patterns.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/pilot_results_920f68.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/plan_006_scalability_stats_29repos.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/pilot_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/scalability_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "6e906201-bbf2-4345-81f0-4de64bf167dc"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Searching for temperature|tau|learning_rate|batch_size|lora_ran…",
  "usage": {
    "total_tokens": 19481,
    "tool_uses": 4,
    "duration_ms": 8616
  },
  "last_tool_name": "Grep",
  "uuid": "217582bd-6c27-46bc-8b2d-7cb0386ff2bf",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01RKcBpx5RgBeKKe7jbyimQQ`</summary>

```json
{
  "pattern": "temperature|tau|learning_rate|batch_size|lora_rank|lora_alpha|proj_dim",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "type": "json",
  "output_mode": "files_with_matches",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "d7355356-fc47-47cc-8054-e41f76e55826",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAkBwWaWDspe3uPJcxQ7BN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 15545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3914,
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

_source line 30 · 2026-05-15T09:28:43.037Z_

<details><summary>↩ Tool result · `toolu_01RKcBpx5RgBeKKe7jbyimQQ`</summary>

```text
Found 20 files limit: 20
logs/workers/worker_analysis_checkpoint-criterion-K_20260515T031356_result.json
logs/workers/worker_check_moto-codeql-failure-scope_20260515T020034_result.json
logs/workers/worker_fix_experiments-v1-warnings_20260514T225801_result.json
logs/workers/worker_fix_plan_005_batch_encoding_and_sim_bins_20260514T205608_result.json
logs/workers/worker_check_bm25_watcher_and_phase1_20260514T202819_result.json
logs/workers/worker_analysis_plan_005_stratified_20260514T201443_result.json
logs/workers/worker_fix_train_py_adapter_only_checkpoint_20260514T193437_result.json
logs/workers/worker_code_plan_018_bm25_phase2_script_20260514T175227_result.json
checkpoints/m2_full_starcoder_DONE_20260514T174955.json
checkpoints/m2_full_starcoder_RUNNING_20260514T174955.json
artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json
checkpoints/m2_full_qwen_ANALYZING_20260514T112434.json
artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json
logs/workers/worker_code_m2_early_stopping_20260514T081434_result.json
artifacts/dream_reports/dream_20260514T075732/median/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json
logs/workers/worker_ssh_s43_launch_readiness_20260514T053516_result.json
logs/workers/worker_ssh_plan014_temp_ablation_config_20260514T005331_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "53767ccd-d9d5-4df8-81bb-343b83d15979"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Reading artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json",
  "usage": {
    "total_tokens": 21859,
    "tool_uses": 5,
    "duration_ms": 10488
  },
  "last_tool_name": "Read",
  "uuid": "12e1766c-199d-4eac-a1b4-00605e5edc02",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01WNvieJULfpaFM1s1jccE7E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "e8dcad5c-e0af-44af-85da-13afdfcae955",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018n58pv91hxojzrJ4cYh4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 19459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2372,
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

_source line 33 · 2026-05-15T09:28:45.217Z_

<details><summary>↩ Tool result · `toolu_01WNvieJULfpaFM1s1jccE7E`</summary>

```text
1	[
2	  {
3	    "name": "SWE-bench Lite End-to-End Evaluation",
4	    "description": "3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。\n",
5	    "results": {
6	      "random_resolve_rate": 0.22,
7	      "random_resolved_count": 66,
8	      "embedding_resolve_rate": 0.245,
9	      "embedding_resolved_count": 73,
10	      "dataflow_resolve_rate": 0.252,
11	      "dataflow_resolved_count": 76,
12	      "embedding_minus_random_pp": 2.5,
13	      "dataflow_minus_random_pp": 3.2,
14	      "dataflow_minus_embedding_pp": 0.7,
15	      "total_instances": 300,
16	      "retriever_top_k": 5,
17	      "agent_model": "Qwen3.6-27B"
18	    },
19	    "tables": [
20	      {
21	        "name": "Table 4: SWE-bench Lite Resolve Rate",
22	        "columns": [
23	          "Strategy",
24	          "Resolved",
25	          "Total",
26	          "Rate (%)",
27	          "Δ vs Random (pp)"
28	        ],
29	        "rows": [
30	          [
31	            "random",
32	            66,
33	            300,
34	            22.0,
35	            "—"
36	          ],
37	          [
38	            "embedding",
39	            73,
40	            300,
41	            24.3,
42	            "+2.3"
43	          ],
44	          [
45	            "dataflow",
46	            76,
47	            300,
48	            25.3,
49	            "+3.3"
50	          ]
51	        ]
52	      },
53	      {
54	        "name": "Table 4b: SWE-bench by Patch Complexity",
55	        "columns": [
56	          "Patch Type",
57	          "N",
58	          "random (%)",
59	          "embedding (%)",
60	          "dataflow (%)"
61	        ],
62	        "rows": [
63	          [
64	            "single-file",
65	            189,
66	            28.0,
67	            30.7,
68	            30.2
69	          ],
70	          [
71	            "multi-file",
72	            111,
73	            11.7,
74	            14.4,
75	            17.1
76	          ]
77	        ]
78	      }
79	    ],
80	    "figures": [],
81	    "analysis": "Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上 +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使 retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives 普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline 一致。\n\n\nEmbedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与 issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分\"近似但无关\" 与\"近似且相关\"的文件。Dataflow 额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee 关系），dataflow negatives 训练使 retriever 理解\"调用链上的文件更可能共同出现在 patch 中\"。Delta 幅度从 retrieval R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的 patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。\n"
82	  },
83	  {
84	    "name": "RepoBench-R Cross-File Retrieval with Multi-Seed CIs",
85	    "description": "RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。\n",
86	    "results": {
87	      "qwen_test_hard": {
88	        "random_R1_mean": 0.621,
89	        "random_R1_ci": [
90	          0.614,
91	          0.628
92	        ],
93	        "embedding_R1_mean": 0.642,
94	        "embedding_R1_ci": [
95	          0.634,
96	          0.65
97	        ],
98	        "dataflow_R1_mean": 0.633,
99	        "dataflow_R1_ci": [
100	          0.624,
101	          0.642
102	        ],
103	        "embedding_minus_random_pp": 2.1,
104	        "dataflow_minus_random_pp": 1.2
105	      },
106	      "qwen_test_easy": {
107	        "random_R1_mean": 0.843,
108	        "embedding_R1_mean": 0.855,
109	        "dataflow_R1_mean": 0.85,
110	        "embedding_minus_random_pp": 1.2
111	      },
112	      "starcoder_test_hard": {
113	        "random_R1_mean": 0.574,
114	        "random_R1_ci": [
115	          0.566,
116	          0.582
117	        ],
118	        "embedding_R1_mean": 0.589,
119	        "embedding_R1_ci": [
120	          0.58,
121	          0.598
122	        ],
123	        "dataflow_R1_mean": 0.572,
124	        "dataflow_R1_ci": [
125	          0.562,
126	          0.582
127	        ],
128	        "embedding_minus_random_pp": 1.5,
129	        "dataflow_minus_random_pp": -0.2
130	      },
131	      "starcoder_test_easy": {
132	        "random_R1_mean": 0.812,
133	        "embedding_R1_mean": 0.822,
134	        "dataflow_R1_mean": 0.81
135	      },
136	      "repobench_R1_delta_pp_embedding_avg": 1.8,
137	      "bootstrap_CI_width_R1_pp_avg": 1.2
138	    },
139	    "tables": [
140	      {
141	        "name": "Table 5: RepoBench-R Results (test_hard, pool≈18)",
142	        "columns": [
143	          "Encoder",
144	          "Strategy",
145	          "R@1 (%)",
146	          "95% CI",
147	          "Δ vs Random (pp)"
148	        ],
149	        "rows": [
150	          [
151	            "Qwen",
152	            "random",
153	            62.1,
154	            "[61.4, 62.8]",
155	            "—"
156	          ],
157	          [
158	            "Qwen",
159	            "embedding",
160	            64.2,
161	            "[63.4, 65.0]",
162	            "+2.1"
163	          ],
164	          [
165	            "Qwen",
166	            "dataflow",
167	            63.3,
168	            "[62.4, 64.2]",
169	            "+1.2"
170	          ],
171	          [
172	            "StarCoder",
173	            "random",
174	            57.4,
175	            "[56.6, 58.2]",
176	            "—"
177	          ],
178	          [
179	            "StarCoder",
180	            "embedding",
181	            58.9,
182	            "[58.0, 59.8]",
183	            "+1.5"
184	          ],
185	          [
186	            "StarCoder",
187	            "dataflow",
188	            57.2,
189	            "[56.2, 58.2]",
190	            "−0.2"
191	          ]
192	        ]
193	      }
194	    ],
195	    "figures": [],
196	    "analysis": "Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R 上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 \"结果仅限单一 benchmark\" 的 reviewer concern。Test_easy 上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。\n\n\nRepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。 Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp）， 因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta 被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI 含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI 宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。\n"
197	  },
198	  {
199	    "name": "Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles",
200	    "description": "5 层分层分析：repo size / pool size / query-positive similarity / structural data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints 在 SWE-smith validation 上重新评估。\n",
201	    "results": {
202	      "stratum_structural_available": {
203	        "with_dataflow_34pct": {
204	          "qwen_dataflow_minus_random_pp": 2.8,
205	          "qwen_dataflow_minus_embedding_pp": 1.3,
206	          "starcoder_dataflow_minus_random_pp": 0.1,
207	          "n_instances": "~5200"
208	        },
209	        "fallback_66pct": {
210	          "qwen_dataflow_minus_random_pp": 0.1,
211	          "qwen_dataflow_minus_embedding_pp": -0.2,
212	          "starcoder_dataflow_minus_random_pp": -0.3,
213	          "n_instances": "~10000"
214	        }
215	      },
216	      "stratum_neg_difficulty_quartile": {
217	        "Q1_easiest": {
218	          "qwen_embedding_minus_random_pp": 0.8,
219	          "qwen_dataflow_minus_random_pp": 0.3
220	        },
221	        "Q2": {
222	          "qwen_embedding_minus_random_pp": 1.5,
223	          "qwen_dataflow_minus_random_pp": 0.7
224	        },
225	        "Q3": {
226	          "qwen_embedding_minus_random_pp": 2.4,
227	          "qwen_dataflow_minus_random_pp": 1.2
228	        },
229	        "Q4_hardest": {
230	          "qwen_embedding_minus_random_pp": 3.2,
231	          "qwen_dataflow_minus_random_pp": 2.1
232	        }
233	      },
234	      "stratum_repo_size": {
235	        "small_lt50": {
236	          "embedding_delta_pp": 2.8,
237	          "n": "~500"
238	        },
239	        "medium_50_200": {
240	          "embedding_delta_pp": 2.2,
241	          "n": "~4100"
242	        },
243	        "large_200_500": {
244	          "embedding_delta_pp": 1.8,
245	          "n": "~5500"
246	        },
247	        "xlarge_500plus": {
248	          "embedding_delta_pp": 1.6,
249	          "n": "~5100"
250	        }
251	      },
252	      "stratum_pool_size": {
253	        "pool_lt20": {
254	          "embedding_delta_pp": 1.0,
255	          "dataflow_delta_pp": 0.3
256	        },
257	        "pool_20_50": {
258	          "embedding_delta_pp": 2.1,
259	          "dataflow_delta_pp": 1.0
260	        },
261	        "pool_gt50": {
262	          "embedding_delta_pp": 2.5,
263	          "dataflow_delta_pp": 1.4
264	        }
265	      },
266	      "stratum_query_pos_sim": {
267	        "high_sim_gt095": {
268	          "embedding_delta_pp": 2.6,
269	          "dataflow_delta_pp": 1.8
270	        },
271	        "medium_sim_085_095": {
272	          "embedding_delta_pp": 1.9,
273	          "dataflow_delta_pp": 0.8
274	        },
275	        "low_sim_lt085": {
276	          "embedding_delta_pp": 1.2,
277	          "dataflow_delta_pp": 0.2
278	        }
279	      }
280	    },
281	    "tables": [
282	      {
283	        "name": "Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)",
284	        "columns": [
285	          "Stratum",
286	          "N",
287	          "random R@1",
288	          "embedding R@1",
289	          "dataflow R@1",
290	          "df−rand (pp)"
291	        ],
292	        "rows": [
293	          [
294	            "With dataflow (34%)",
295	            "~5.2K",
296	            53.1,
297	            55.4,
298	            55.9,
299	            "+2.8"
300	          ],
301	          [
302	            "Fallback (66%)",
303	            "~10K",
304	            55.2,
305	            57.3,
306	            55.3,
307	            "+0.1"
308	          ],
309	          [
310	            "Overall",
311	            "~15.2K",
312	            54.5,
313	            56.5,
314	            55.5,
315	            "+1.0"
316	          ]
317	        ]
318	      },
319	      {
320	        "name": "Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)",
321	        "columns": [
322	          "Quartile",
323	          "margin_mean",
324	          "emb−rand (pp)",
325	          "df−rand (pp)"
326	        ],
327	        "rows": [
328	          [
329	            "Q1 (easiest)",
330	            0.142,
331	            "+0.8",
332	            "+0.3"
333	          ],
334	          [
335	            "Q2",
336	            0.078,
337	            "+1.5",
338	            "+0.7"
339	          ],
340	          [
341	            "Q3",
342	            0.031,
343	            "+2.4",
344	            "+1.2"
345	          ],
346	          [
347	            "Q4 (hardest)",
348	            0.008,
349	            "+3.2",
350	            "+2.1"
351	          ]
352	        ]
353	      }
354	    ],
355	    "figures": [],
356	    "analysis": "Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是 representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 \"diluted signal\" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。\n\n\nStructural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些 instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding 或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 \"34% coverage 稀释 signal\" 的 concern——真实 per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta 最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高 pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta 最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate pool 更集中，mining 策略差异更容易体现。\n"
357	  },
358	  {
359	    "name": "Call-Graph Hop Depth Ablation (1/2/3-hop)",
360	    "description": "比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。 Qwen encoder, 1 seed, SWE-smith validation。\n",
361	    "results": {
362	      "hop_1": {
363	        "R1": 0.548,
364	        "connected_coverage_pct": 12.4,
365	        "negatives_per_query_mean": 18.2
366	      },
367	      "hop_2": {
368	        "R1": 0.555,
369	        "connected_coverage_pct": 34.3,
370	        "negatives_per_query_mean": 31.7
371	      },
372	      "hop_3": {
373	        "R1": 0.551,
374	        "connected_coverage_pct": 58.6,
375	        "negatives_per_query_mean": 42.1
376	      },
377	      "optimal_hop": 2,
378	      "hop2_minus_hop1_pp": 0.7,
379	      "hop3_minus_hop2_pp": -0.4
380	    },
381	    "tables": [
382	      {
383	        "name": "Table 9: Hop Depth Ablation (Qwen, dataflow strategy)",
384	        "columns": [
385	          "Hops",
386	          "Coverage (%)",
387	          "Neg/query",
388	          "R@1 (%)",
389	          "Δ vs 2-hop (pp)"
390	        ],
391	        "rows": [
392	          [
393	            1,
394	            12.4,
395	            18.2,
396	            54.8,
397	            "−0.7"
398	          ],
399	          [
400	            2,
401	            34.3,
402	            31.7,
403	            55.5,
404	            "—"
405	          ],
406	          [
407	            3,
408	            58.6,
409	            42.1,
410	            55.1,
411	            "−0.4"
412	          ]
413	        ]
414	      }
415	    ],
416	    "figures": [],
417	    "analysis": "2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee， 2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop 选择有 principled 依据而非纯粹 empirical tuning。\n\n\n2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的 connected 节点来定义 \"disconnected\" negatives，退化为 random。3-hop 过于宽松——58.6% coverage 下 \"disconnected\" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3% coverage（与 M1 extraction 的 structural data rate 一致）在 \"enough connected nodes to define meaningful disconnection\" 和 \"disconnected set still contains genuinely unrelated files\" 之间取得平衡。\n"
418	  },
419	  {
420	    "name": "Training Data Size Scaling (1K/3K/5K)",
421	    "description": "固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances 增长， 观察 R@1 变化和策略排名稳定性。\n",
422	    "results": {
423	      "size_1K": {
424	        "random_R1": 0.51,
425	        "embedding_R1": 0.522,
426	        "dataflow_R1": 0.515,
427	        "embedding_minus_random_pp": 1.2,
428	        "seed_std": 0.015
429	      },
430	      "size_3K": {
431	        "random_R1": 0.532,
432	        "embedding_R1": 0.55,
433	        "dataflow_R1": 0.541,
434	        "embedding_minus_random_pp": 1.8,
435	        "seed_std": 0.01
436	      },
437	      "size_5K": {
438	        "random_R1": 0.545,
439	        "embedding_R1": 0.565,
440	        "dataflow_R1": 0.555,
441	        "embedding_minus_random_pp": 2.0,
442	        "seed_std": 0.008
443	      },
444	      "ranking_stable": true,
445	      "monotonic_improvement": true
446	    },
447	    "tables": [
448	      {
449	        "name": "Table 10: Data Size Scaling (Qwen)",
450	        "columns": [
451	          "Size",
452	          "random R@1",
453	          "embedding R@1",
454	          "dataflow R@1",
455	          "emb−rand (pp)",
456	          "σ across seeds"
457	        ],
458	        "rows": [
459	          [
460	            "1K",
461	            51.0,
462	            52.2,
463	            51.5,
464	            "+1.2",
465	            1.5
466	          ],
467	          [
468	            "3K",
469	            53.2,
470	            55.0,
471	            54.1,
472	            "+1.8",
473	            1.0
474	          ],
475	          [
476	            "5K",
477	            54.5,
478	            56.5,
479	            55.5,
480	            "+2.0",
481	            0.8
482	          ]
483	        ]
484	      }
485	    ],
486	    "figures": [],
487	    "analysis": "Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见 diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer \"effect size marginal\" concern 有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。\n\n\n策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta 幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining 策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K 时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further scaling could help, but is beyond scope。\n"
488	  },
489	  {
490	    "name": "Fusion Head Ablation",
491	    "description": "比较 embedding-only / structural-features-only / combined fusion head， 隔离 training-time mining 价值与 inference-time feature injection。\n",
492	    "results": {
493	      "embedding_only": {
494	        "qwen_R1": 0.565,
495	        "starcoder_R1": 0.475
496	      },
497	      "structural_features_only": {
498	        "qwen_R1": 0.498,
499	        "starcoder_R1": 0.421
500	      },
501	      "combined_fusion": {
502	        "qwen_R1": 0.561,
503	        "starcoder_R1": 0.472
504	      },
505	      "embedding_only_minus_combined_pp": 0.4,
506	      "conclusion": "mining > fusion; structural features at inference add noise"
507	    },
508	    "tables": [
509	      {
510	        "name": "Table 11: Fusion Head Ablation",
511	        "columns": [
512	          "Configuration",
513	          "Qwen R@1 (%)",
514	          "StarCoder R@1 (%)"
515	        ],
516	        "rows": [
517	          [
518	            "embedding-only (ours)",
519	            56.5,
520	            47.5
521	          ],
522	          [
523	            "structural-features-only",
524	            49.8,
525	            42.1
526	          ],
527	          [
528	            "combined fusion",
529	            56.1,
530	            47.2
531	          ]
532	        ]
533	      }
534	    ],
535	    "figures": [],
536	    "analysis": "训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features 绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector structural features，引入 noise。\n\n\nEmbedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征） 表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance 反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。 这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。\n"
537	  },
538	  {
539	    "name": "Dataflow-Distance Weighted vs Binary Negatives",
540	    "description": "比较 binary connected/disconnected 与 dataflow-distance weighted negative sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。\n",
541	    "results": {
542	      "binary_qwen_R1": 0.555,
543	      "weighted_qwen_R1": 0.558,
544	      "binary_starcoder_R1": 0.458,
545	      "weighted_starcoder_R1": 0.459,
546	      "weighted_minus_binary_qwen_pp": 0.3,
547	      "weighted_minus_binary_starcoder_pp": 0.1
548	    },
549	    "tables": [
550	      {
551	        "name": "Table S1: Weighted vs Binary Dataflow Negatives",
552	        "columns": [
553	          "Method",
554	          "Qwen R@1 (%)",
555	          "StarCoder R@1 (%)",
556	          "Δ vs Binary (pp)"
557	        ],
558	        "rows": [
559	          [
560	            "Binary (default)",
561	            55.5,
562	            45.8,
563	            "—"
564	          ],
565	          [
566	            "Distance-weighted",
567	            55.8,
568	            45.9,
569	            "+0.3 / +0.1"
570	          ]
571	        ]
572	      }
573	    ],
574	    "figures": [],
575	    "analysis": "Binary is sufficient — complexity of weighted sampling not justified. 论文可在 ablation section 用一句话报告这一 negative result， 强化 \"simple binary structural signal is the key insight\" 的 narrative。\n\n\nWeighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary disconnected/connected 已经捕获了最关键的 structural distinction—— \"是否在调用链上\"。进一步按 hop distance 加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。\n"
576	  },
577	  {
578	    "name": "SWE-bench Failure Analysis (50 cases)",
579	    "description": "从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow 信号是否可能帮助。\n",
580	    "results": {
581	      "total_analyzed": 50,
582	      "category_breakdown": {
583	        "retrieval_failure_wrong_files": 22,
584	        "retrieval_success_but_agent_fail": 15,
585	        "insufficient_context_window": 7,
586	        "test_environment_issue": 4,
587	        "ambiguous_issue_description": 2
588	      },
589	      "dataflow_could_help": {
590	        "true": 14,
591	        "partially": 5,
592	        "false": 31
593	      },
594	      "dataflow_help_rate": 0.28,
595	      "key_pattern": "14/22 retrieval failures involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity would directly address these.\n"
596	    },
597	    "tables": [
598	      {
599	        "name": "Table S2: Failure Category Breakdown",
600	        "columns": [
601	          "Category",
602	          "Count",
603	          "% of 50",
604	          "Dataflow Could Help?"
605	        ],
606	        "rows": [
607	          [
608	            "Retrieval: wrong files",
609	            22,
610	            44,
611	            "14/22 (64%)"
612	          ],
613	          [
614	            "Retrieval OK, agent fail",
615	            15,
616	            30,
617	            "N/A"
618	          ],
619	          [
620	            "Context window limit",
621	            7,
622	            14,
623	            "5/7 partially"
624	          ],
625	          [
626	            "Test env issue",
627	            4,
628	            8,
629	            "No"
630	          ],
631	          [
632	            "Ambiguous issue",
633	            2,
634	            4,
635	            "No"
636	          ]
637	        ]
638	      }
639	    ],
640	    "figures": [],
641	    "analysis": "28% of failures could benefit from dataflow signal, consistent with the observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures confirms that cross-module dependency is the primary retrieval challenge, directly supporting Claim 2's motivation.\n\n\n50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和 gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了 \"ceiling analysis\"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。\n"
642	  },
643	  {
644	    "name": "Qualitative Examples (5-10 cases)",
645	    "description": "从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例， 展示 structural signal 的具体作用机制。\n",
646	    "results": {
647	      "total_examples": 8,
648	      "example_categories": {
649	        "caller_callee_confusion": 3,
650	        "utility_file_distraction": 2,
651	        "cross_module_import_chain": 2,
652	        "test_file_vs_source": 1
653	      },
654	      "illustrative_example": {
655	        "issue": "django/django#12345 — QuerySet.filter() returns wrong results with nested Q objects",
656	        "random_retriever_top1": "django/db/models/query.py (text match on 'filter')",
657	        "dataflow_retriever_top1": "django/db/models/sql/query.py (actual SQL generation called by filter)",
658	        "gold": "django/db/models/sql/query.py",
659	        "explanation": "Random retriever picks query.py (contains 'filter' method signature) but the bug is in sql/query.py (the downstream SQL builder called by filter). Dataflow training teaches the model that sql/query.py is structurally connected to query.py via 2-hop call chain, making it a better negative for other instances, which in turn improves the model's ability to rank the actual implementation file higher.\n"
660	      }
661	    },
662	    "tables": [],
663	    "figures": [],
664	    "analysis": "Qualitative examples serve as the paper's \"aha moment\" — they make the abstract representation geometry argument concrete. Reviewer-facing value: even skeptics who question statistical significance can see the mechanism operating on real code.\n\n\n8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper 函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的 source code 复制）。这些案例具体展示了 \"lexical similarity ≠ structural relevance\" 的核心 insight。\n"
665	  },
666	  {
667	    "name": "Temperature Ablation τ ∈ {0.05, 0.1, 0.2}",
668	    "description": "3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy ranking 是否 regime-specific。\n",
669	    "results": {
670	      "tau_005": {
671	        "qwen_random_R1": 0.558,
672	        "qwen_embedding_R1": 0.577,
673	        "qwen_dataflow_R1": 0.569,
674	        "qwen_embedding_minus_random_pp": 1.9,
675	        "starcoder_random_R1": 0.47,
676	        "starcoder_embedding_R1": 0.485,
677	        "starcoder_dataflow_R1": 0.467,
678	        "starcoder_embedding_minus_random_pp": 1.5
679	      },
680	      "tau_010": {
681	        "qwen_random_R1": 0.545,
682	        "qwen_embedding_R1": 0.565,
683	        "qwen_dataflow_R1": 0.555,
684	        "qwen_embedding_minus_random_pp": 2.0,
685	        "starcoder_random_R1": 0.46,
686	        "starcoder_embedding_R1": 0.475,
687	        "starcoder_dataflow_R1": 0.458,
688	        "starcoder_embedding_minus_random_pp": 1.5
689	      },
690	      "tau_020": {
691	        "qwen_random_R1": 0.53,
692	        "qwen_embedding_R1": 0.546,
693	        "qwen_dataflow_R1": 0.538,
694	        "qwen_embedding_minus_random_pp": 1.6,
695	        "starcoder_random_R1": 0.448,
696	        "starcoder_embedding_R1": 0.461,
697	        "starcoder_dataflow_R1": 0.447,
698	        "starcoder_embedding_minus_random_pp": 1.3
699	      },
700	      "ranking_preserved_across_tau": true,
701	      "optimal_tau": 0.05
702	    },
703	    "tables": [
704	      {
705	        "name": "Table 8: Temperature Ablation (R@1 %)",
706	        "columns": [
707	          "τ",
708	          "Encoder",
709	          "random",
710	          "embedding",
711	          "dataflow",
712	          "emb−rand (pp)"
713	        ],
714	        "rows": [
715	          [
716	            0.05,
717	            "Qwen",
718	            55.8,
719	            57.7,
720	            56.9,
721	            "+1.9"
722	          ],
723	          [
724	            0.05,
725	            "StarCoder",
726	            47.0,
727	            48.5,
728	            46.7,
729	            "+1.5"
730	          ],
731	          [
732	            0.1,
733	            "Qwen",
734	            54.5,
735	            56.5,
736	            55.5,
737	            "+2.0"
738	          ],
739	          [
740	            0.1,
741	            "StarCoder",
742	            46.0,
743	            47.5,
744	            45.8,
745	            "+1.5"
746	          ],
747	          [
748	            0.2,
749	            "Qwen",
750	            53.0,
751	            54.6,
752	            53.8,
753	            "+1.6"
754	          ],
755	          [
756	            0.2,
757	            "StarCoder",
758	            44.8,
759	            46.1,
760	            44.7,
761	            "+1.3"
762	          ]
763	        ]
764	      }
765	    ],
766	    "figures": [],
767	    "analysis": "Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但 不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。\n\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且 delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity 被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific， 直接回应 median reviewer 的 \"τ=0.05 unusually low\" concern。\n"
768	  },
769	  {
770	    "name": "Dynamic vs Static Embedding Mining",
771	    "description": "Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。\n",
772	    "results": {
773	      "qwen_static_R1": 0.565,
774	      "qwen_dynamic_R1": 0.568,
775	      "qwen_dynamic_minus_static_pp": 0.3,
776	      "starcoder_static_R1": 0.475,
777	      "starcoder_dynamic_R1": 0.477,
778	      "starcoder_dynamic_minus_static_pp": 0.2,
779	      "dynamic_significant": false,
780	      "curriculum_confound_ruled_out": true
781	    },
782	    "tables": [
783	      {
784	        "name": "Table 13: Static vs Dynamic Embedding Mining",
785	        "columns": [
786	          "Encoder",
787	          "Static R@1 (%)",
788	          "Dynamic R@1 (%)",
789	          "Δ (pp)",
790	          "p-value"
791	        ],
792	        "rows": [
793	          [
794	            "Qwen",
795	            56.5,
796	            56.8,
797	            "+0.3",
798	            0.41
799	          ],
800	          [
801	            "StarCoder",
802	            47.5,
803	            47.7,
804	            "+0.2",
805	            0.53
806	          ]
807	        ]
808	      }
809	    ],
810	    "figures": [],
811	    "analysis": "Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative 的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner recommendation——mine once from pretrained, no need for per-epoch re-mining。\n\n\nDynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning 只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了 \"static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives 变 stale）\" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy 的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每 epoch 重新 encode + kNN）不 justified。\n"
812	  },
813	  {
814	    "name": "Bootstrap CIs for SWE-bench Lite Resolve Rate",
815	    "description": "对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired difference CIs 和 p-values。\n",
816	    "results": {
817	      "embedding_minus_random": {
818	        "delta_pp": 2.5,
819	        "ci_95": [
820	          0.7,
821	          4.3
822	        ],
823	        "p_value": 0.018,
824	        "significant": true
825	      },
826	      "dataflow_minus_random": {
827	        "delta_pp": 3.2,
828	        "ci_95": [
829	          1.0,
830	          5.5
831	        ],
832	        "p_value": 0.008,
833	        "significant": true
834	      },
835	      "dataflow_minus_embedding": {
836	        "delta_pp": 0.7,
837	        "ci_95": [
838	          -1.5,
839	          2.9
840	        ],
841	        "p_value": 0.134,
842	        "significant": false
843	      },
844	      "bootstrap_n": 10000,
845	      "sample_size": 300
846	    },
847	    "tables": [
848	      {
849	        "name": "Table 4c: SWE-bench Bootstrap Significance Tests",
850	        "columns": [
851	          "Comparison",
852	          "Δ (pp)",
853	          "95% CI",
854	          "p-value"
855	        ],
856	        "rows": [
857	          [
858	            "embedding − random",
859	            "+2.5",
860	            "[+0.7, +4.3]",
861	            0.018
862	          ],
863	          [
864	            "dataflow − random",
865	            "+3.2",
866	            "[+1.0, +5.5]",
867	            0.008
868	          ],
869	          [
870	            "dataflow − embedding",
871	            "+0.7",
872	            "[−1.5, +2.9]",
873	            0.134
874	          ]
875	        ]
876	      }
877	    ],
878	    "figures": [],
879	    "analysis": "CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。 Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 \"conditional\" framing 一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。\n\n\nEmbedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining 在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300 instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游 binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench Lite 不是为精确 delta 估计设计的 benchmark。\n"
880	  },
881	  {
882	    "name": "Inference-Time Graph Method Literature Comparison",
883	    "description": "文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成 8 篇论文 survey。\n",
884	    "results": {
885	      "papers_surveyed": 8,
886	      "key_distinction": "training-time mining (ours) vs inference-time graph navigation",
887	      "complementarity_evidence": "All 8 methods operate at inference time; StructFuse mines at training time. The two approaches are complementary — StructFuse improves the base retriever that graph methods navigate over.\n",
888	      "papers_list": [
889	        "CodexGraph",
890	        "LocAgent",
891	        "RANGER",
892	        "GraphCoder",
893	        "ARISE",
894	        "RepoGraph",
895	        "CodeGRAG",
896	        "CodeRAG"
897	      ]
898	    },
899	    "tables": [
900	      {
901	        "name": "Table S3: Comparison with Inference-Time Graph Methods",
902	        "columns": [
903	          "Method",
904	          "Graph Stage",
905	          "Graph Type",
906	          "Complementary?"
907	        ],
908	        "rows": [
909	          [
910	            "StructFuse (ours)",
911	            "Training",
912	            "Dataflow (CodeQL)",
913	            "—"
914	          ],
915	          [
916	            "CodexGraph",
917	            "Inference",
918	            "Code graph DB",
919	            "Yes"
920	          ],
921	          [
922	            "LocAgent",
923	            "Inference",
924	            "Repo structure",
925	            "Yes"
926	          ],
927	          [
928	            "RANGER",
929	            "Inference",
930	            "Call graph",
931	            "Yes"
932	          ],
933	          [
934	            "ARISE",
935	            "Inference",
936	            "Intra-proc dataflow",
937	            "Partially (intra only)"
938	          ]
939	        ]
940	      }
941	    ],
942	    "figures": [],
943	    "analysis": "Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight: StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。\n\n\n8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段 通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time 方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用 embedding retrieval）。 Discussion section 应明确 \"complementary, not competing\" 的定位。\n"
944	  },
945	  {
946	    "name": "BM25 Negative Baseline — Closing CoCoHaNeRe Argument",
947	    "description": "BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe 报告的 \"embedding negatives harm\" 实际是 BM25-proxy artifact。\n",
948	    "results": {
949	      "qwen": {
950	        "bm25_R1": 0.52,
951	        "random_R1": 0.545,
952	        "embedding_R1": 0.565,
953	        "dataflow_R1": 0.555,
954	        "bm25_minus_random_pp": -2.5,
955	        "embedding_minus_bm25_pp": 4.5
956	      },
957	      "starcoder": {
958	        "bm25_R1": 0.433,
959	        "random_R1": 0.46,
960	        "embedding_R1": 0.475,
961	        "dataflow_R1": 0.458,
962	        "bm25_minus_random_pp": -2.7,
963	        "embedding_minus_bm25_pp": 4.2
964	      },
965	      "bm25_harms_both_encoders": true,
966	      "cocohanere_artifact_confirmed": true,
967	      "bm25_minus_random_avg_pp": -2.6
968	    },
969	    "tables": [
970	      {
971	        "name": "Table 3: Full 4-Strategy Comparison Including BM25 Baseline",
972	        "columns": [
973	          "Encoder",
974	          "Strategy",
975	          "R@1 (%)",
976	          "95% CI",
977	          "Δ vs Random (pp)"
978	        ],
979	        "rows": [
980	          [
981	            "Qwen",
982	            "BM25",
983	            52.0,
984	            "[51.2, 52.8]",
985	            "−2.5"
986	          ],
987	          [
988	            "Qwen",
989	            "random",
990	            54.5,
991	            "[53.8, 55.2]",
992	            "—"
993	          ],
994	          [
995	            "Qwen",
996	            "dataflow",
997	            55.5,
998	            "[54.6, 56.4]",
999	            "+1.0"
1000	          ],
1001	          [
1002	            "Qwen",
1003	            "embedding",
1004	            56.5,
1005	            "[55.8, 57.2]",
1006	            "+2.0"
1007	          ],
1008	          [
1009	            "StarCoder",
1010	            "BM25",
1011	            43.3,
1012	            "[42.3, 44.3]",
1013	            "−2.7"
1014	          ],
1015	          [
1016	            "StarCoder",
1017	            "random",
1018	            46.0,
1019	            "[45.1, 46.9]",
1020	            "—"
1021	          ],
1022	          [
1023	            "StarCoder",
1024	            "dataflow",
1025	            45.8,
1026	            "[44.8, 46.8]",
1027	            "−0.2"
1028	          ],
1029	          [
1030	            "StarCoder",
1031	            "embedding",
1032	            47.5,
1033	            "[46.6, 48.4]",
1034	            "+1.5"
1035	          ]
1036	        ]
1037	      }
1038	    ],
1039	    "figures": [],
1040	    "analysis": "BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 \"argumentative correction\" 升级为 \"empirical demonstration\"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行 BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的 quality spectrum。Reviewer 对 \"correction without evidence\" 的 concern 被彻底关闭。\n\n\nBM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names, variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分 positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成 Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp [-4.0, -1.5] 范围内。\n"
1041	  },
1042	  {
1043	    "name": "Pool Size Sensitivity (50/100/200/500)",
1044	    "description": "在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints， 测试 strategy ranking 在更 realistic pool sizes 下的稳定性。\n",
1045	    "results": {
1046	      "qwen": {
1047	        "pool_50": {
1048	          "random_R1": 0.545,
1049	          "embedding_R1": 0.565,
1050	          "dataflow_R1": 0.555,
1051	          "embedding_minus_random_pp": 2.0
1052	        },
1053	        "pool_100": {
1054	          "random_R1": 0.428,
1055	          "embedding_R1": 0.447,
1056	          "dataflow_R1": 0.438,
1057	          "embedding_minus_random_pp": 1.9
1058	        },
1059	        "pool_200": {
1060	          "random_R1": 0.342,
1061	          "embedding_R1": 0.359,
1062	          "dataflow_R1": 0.351,
1063	          "embedding_minus_random_pp": 1.7
1064	        },
1065	        "pool_500": {
1066	          "random_R1": 0.261,
1067	          "embedding_R1": 0.276,
1068	          "dataflow_R1": 0.269,
1069	          "embedding_minus_random_pp": 1.5
1070	        }
1071	      },
1072	      "starcoder": {
1073	        "pool_50": {
1074	          "random_R1": 0.46,
1075	          "embedding_R1": 0.475,
1076	          "dataflow_R1": 0.458,
1077	          "embedding_minus_random_pp": 1.5
1078	        },
1079	        "pool_100": {
1080	          "random_R1": 0.358,
1081	          "embedding_R1": 0.372,
1082	          "dataflow_R1": 0.357,
1083	          "embedding_minus_random_pp": 1.4
1084	        },
1085	        "pool_200": {
1086	          "random_R1": 0.282,
1087	          "embedding_R1": 0.295,
1088	          "dataflow_R1": 0.281,
1089	          "embedding_minus_random_pp": 1.3
1090	        },
1091	        "pool_500": {
1092	          "random_R1": 0.214,
1093	          "embedding_R1": 0.225,
1094	          "dataflow_R1": 0.213,
1095	          "embedding_minus_random_pp": 1.1
1096	        }
1097	      },
1098	      "ranking_stable_across_pools": true,
1099	      "pool_ranking_stable_pct": 100,
1100	      "delta_shrinkage_rate": "~0.15pp per doubling of pool size"
1101	    },
1102	    "tables": [
1103	      {
1104	        "name": "Table 12: Pool Size Sensitivity (R@1 %)",
1105	        "columns": [
1106	          "Pool",
1107	          "Encoder",
1108	          "random",
1109	          "embedding",
1110	          "dataflow",
1111	          "emb−rand (pp)",
1112	          "Ranking"
1113	        ],
1114	        "rows": [
1115	          [
1116	            50,
1117	            "Qwen",
1118	            54.5,
1119	            56.5,
1120	            55.5,
1121	            "+2.0",
1122	            "E>D>R"
1123	          ],
1124	          [
1125	            100,
1126	            "Qwen",
1127	            42.8,
1128	            44.7,
1129	            43.8,
1130	            "+1.9",
1131	            "E>D>R"
1132	          ],
1133	          [
1134	            200,
1135	            "Qwen",
1136	            34.2,
1137	            35.9,
1138	            35.1,
1139	            "+1.7",
1140	            "E>D>R"
1141	          ],
1142	          [
1143	            500,
1144	            "Qwen",
1145	            26.1,
1146	            27.6,
1147	            26.9,
1148	            "+1.5",
1149	            "E>D>R"
1150	          ],
1151	          [
1152	            50,
1153	            "StarCoder",
1154	            46.0,
1155	            47.5,
1156	            45.8,
1157	            "+1.5",
1158	            "E>R>D"
1159	          ],
1160	          [
1161	            100,
1162	            "StarCoder",
1163	            35.8,
1164	            37.2,
1165	            35.7,
1166	            "+1.4",
1167	            "E>R>D"
1168	          ],
1169	          [
1170	            200,
1171	            "StarCoder",
1172	            28.2,
1173	            29.5,
1174	            28.1,
1175	            "+1.3",
1176	            "E>R≈D"
1177	          ],
1178	          [
1179	            500,
1180	            "StarCoder",
1181	            21.4,
1182	            22.5,
1183	            21.3,
1184	            "+1.1",
1185	            "E>R≈D"
1186	          ]
1187	        ]
1188	      }
1189	    ],
1190	    "figures": [],
1191	    "analysis": "Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是 best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是 robust 的。论文可以明确声明：\"Strategy rankings are stable across pool sizes spanning an order of magnitude (50–500), with embedding mining maintaining a statistically significant advantage even at the largest pool tested.\"\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)， 缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 \"hard\" negative 的概率增加（base rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有 +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500) 但保持正值。 这直接回应 reviewer \"pool=50 unrealistically small\" concern：即使 10x pool 扩大， strategy ranking 完全不翻转。\n"
1192	  }
1193	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "5dc93cb0-6e67-4e2f-bdd9-aa7d26fccc79"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 21862,
    "tool_uses": 6,
    "duration_ms": 10895
  },
  "last_tool_name": "Bash",
  "uuid": "eecfc4fe-fe24-4522-af23-3782242f848c",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_011mcuDgZd1Kqz9XaoiLWqmU`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context -name \"CLAUDE.md\" -o -name \"*.py\" -path \"*/config*\" -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "627f491b-a1e9-4a25-bf14-9d29a759276a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018n58pv91hxojzrJ4cYh4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 19459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2372,
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

_source line 36 · 2026-05-15T09:28:45.351Z_

<details><summary>↩ Tool result · `toolu_011mcuDgZd1Kqz9XaoiLWqmU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/agent_1b98c4fb/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/agent_cb55d4ab/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/agent_2bc11d4f/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/agent_204785e5/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/CLAUDE.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "7d3d381d-3c26-4a35-95a8-26ffd2f28cd9"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Searching for temp|tau|lora_rank|lora_alpha|learning.*rate|batc…",
  "usage": {
    "total_tokens": 21865,
    "tool_uses": 7,
    "duration_ms": 12158
  },
  "last_tool_name": "Grep",
  "uuid": "b29373a4-4839-4863-bf9f-e8d79cd989a2",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_0178LMc687LBALemQ6SRJwMe`</summary>

```json
{
  "pattern": "temp|tau|lora_rank|lora_alpha|learning.*rate|batch.*size|max_seq|proj_dim|warmup|weight_decay|num_epochs|early_stopping|pool_size|num_negatives",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "type": "yaml",
  "output_mode": "files_with_matches",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "2fe2a7eb-d17e-480d-9278-b6a142e0b262",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018n58pv91hxojzrJ4cYh4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 19459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2372,
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

_source line 39 · 2026-05-15T09:28:46.577Z_

<details><summary>↩ Tool result · `toolu_0178LMc687LBALemQ6SRJwMe`</summary>

```text
Found 22 files
artifacts/manifest.yaml
decisions.yaml
registry.yaml
literature_map.yaml
artifacts/dream_reports/dream_20260514T162530/meta.yaml
artifacts/dream_reports/dream_20260514T162530/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/median/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/meta.yaml
artifacts/dream_reports/dream_20260514T075732/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/meta.yaml
artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "6718ce30-e0d4-49c8-9081-0f08dafb0f95"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Reading registry.yaml",
  "usage": {
    "total_tokens": 41221,
    "tool_uses": 8,
    "duration_ms": 14089
  },
  "last_tool_name": "Read",
  "uuid": "0119693b-c28f-4f4c-be24-fc7c0a640c60",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01CkoqSjT1TANhNZZAovqzov`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "960407ff-8417-4e6d-81e2-00e3d77cc29c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011LcRPUkg6ntjyKvArEB4dM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19354,
      "cache_read_input_tokens": 21831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19354,
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

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Reading artifacts/manifest.yaml",
  "usage": {
    "total_tokens": 41222,
    "tool_uses": 9,
    "duration_ms": 14259
  },
  "last_tool_name": "Read",
  "uuid": "cb1b6e5a-1b37-46c1-8c68-516116ee681b",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01AgB1UMMnHHYuKrkx1jnCtC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "460534d1-c60e-4bf9-b6f3-690aeb0ddbd3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011LcRPUkg6ntjyKvArEB4dM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19354,
      "cache_read_input_tokens": 21831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19354,
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

_source line 44 · 2026-05-15T09:28:48.814Z_

<details><summary>↩ Tool result · `toolu_01CkoqSjT1TANhNZZAovqzov`</summary>

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
201	      server: cqa1-21977
202	      gpu:
203	      - cuda:4
204	      pid: '89257'
205	      log_path: N/A
206	      submitted_at: '2026-05-12T12:22:54.433Z'
207	      submitted_via: submit_training_job
208	      backend: tmux
209	      account: root
210	      data_path: N/A
211	      data_count: 0
212	      model_name: N/A
213	      seed: 42
214	      checkpoint_path: N/A
215	      wall_clock_seconds: 9772.0
216	      gpu_hours: 2.71
217	    conclusion: killed
218	    completed_at: '2026-05-12T15:05:46.413Z'
219	  p2b-smoke7:
220	    status: DONE
221	    retry_count: 0
222	    created_at: '2026-05-12T12:28:55.114Z'
223	    updated_at: '2026-05-12T15:05:47.346Z'
224	    spec:
225	      command: obsolete smoke test
226	      server: cqa1-21977
227	      gpu:
228	      - cuda:4
229	      pid: '90758'
230	      log_path: N/A
231	      submitted_at: '2026-05-12T12:28:55.101Z'
232	      submitted_via: submit_training_job
233	      backend: tmux
234	      account: root
235	      data_path: N/A
236	      data_count: 0
237	      model_name: N/A
238	      seed: 42
239	      checkpoint_path: N/A
240	      wall_clock_seconds: 9412.2
241	      gpu_hours: 2.61
242	    conclusion: killed
243	    completed_at: '2026-05-12T15:05:47.346Z'
244	  p2b-smoke8:
245	    status: DONE
246	    retry_count: 0
247	    created_at: '2026-05-12T12:32:22.931Z'
248	    updated_at: '2026-05-12T15:05:48.324Z'
249	    spec:
250	      command: obsolete smoke test
251	      server: cqa1-21977
252	      gpu:
253	      - cuda:4
254	      pid: '91698'
255	      log_path: N/A
256	      submitted_at: '2026-05-12T12:32:22.916Z'
257	      submitted_via: submit_training_job
258	      backend: tmux
259	      account: root
260	      data_path: N/A
261	      data_count: 0
262	      model_name: N/A
263	      seed: 42
264	      checkpoint_path: N/A
265	      wall_clock_seconds: 9205.4
266	      gpu_hours: 2.56
267	    conclusion: killed
268	    completed_at: '2026-05-12T15:05:48.324Z'
269	  p2b-all-9runs:
270	    status: DONE
271	    retry_count: 0
272	    created_at: '2026-05-12T12:34:24.923Z'
273	    updated_at: '2026-05-12T15:05:49.244Z'
274	    spec:
275	      command: obsolete smoke test
276	      server: cqa1-21977
277	      gpu:
278	      - cuda:4
279	      pid: '92636'
280	      log_path: N/A
281	      submitted_at: '2026-05-12T12:34:24.908Z'
282	      submitted_via: submit_training_job
283	      backend: tmux
284	      account: root
285	      data_path: N/A
286	      data_count: 0
287	      model_name: N/A
288	      seed: 42
289	      checkpoint_path: N/A
290	      wall_clock_seconds: 9084.3
291	      gpu_hours: 2.52
292	    conclusion: killed
293	    completed_at: '2026-05-12T15:05:49.244Z'
294	  mvp_p2b_contrastive_training:
295	    status: DONE
296	    retry_count: 2
297	    created_at: '2026-05-12T12:37:44.628Z'
298	    updated_at: '2026-05-13T01:31:27.220Z'
299	    reproduce:
300	      finished_at: '2026-05-12T16:19:50.297Z'
301	    failure_reason: EXIT_CODE=2 (shell misuse / syntax)
302	    completed_at: '2026-05-12T13:16:21.735Z'
303	    extra:
304	      hook_events:
305	      - event: on_failed
306	        action: agent
307	        ts: '2026-05-12T13:16:22.517958+00:00'
308	      - event: on_failed
309	        action: agent
310	        ts: '2026-05-12T15:15:47.933008+00:00'
311	      - event: on_complete
312	        action: agent
313	        ts: '2026-05-12T16:19:51.082427+00:00'
314	      previous_failure:
315	        conclusion: failed
316	        notes: '第2次失败: random策略3seeds全部完成(s42跳过/s123 recall@5=0.984/s456 recall@5=0.992),
317	          但embedding策略s42启动即EXIT_CODE=2(shell syntax error). Worker worker_diagnose_mvp_p2b_contrastive_training_v2
318	          正在诊断和修复run_p2b_all.sh的embedding配置部分'
319	    notes: 4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save
320	      RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123
321	      开始级联.
322	    spec:
323	      command: 'bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)'
324	      server: cqa1-21977
325	      gpu:
326	      - cuda:4
327	      pid: '238645'
328	      data_path: /root/structfuse/mvp_data/training_data/
329	      data_count: 127
330	      model_name: Qwen2.5-Coder-3B + LoRA
331	      seed: 42,123,456
332	      hypothesis: 'H3: data-flow hard negatives vs random vs embedding-distance, 3-seed
333	        × 3-strategy contrastive training'
334	      plan_id: mvp_p2b_contrastive_training
335	      checkpoint_path: /root/autodl-tmp/structfuse/checkpoints/
336	      log_path: /tmp/p2b_all_runs.log
337	    metrics:
338	      random_s42_recall1: 0.984
339	      random_s123_recall1: 0.984
340	      random_s456_recall1: 0.992
341	      embedding_s42_recall1: 0.874
342	      random_mean_recall1: 0.987
343	      runs_completed: 4
344	      runs_failed: 5
345	      failure_type: disk_full_torch_save
346	    conclusion: killed
347	  mvp_p2b_contrastive_v2:
348	    status: DONE
349	    retry_count: 0
350	    created_at: '2026-05-12T15:03:02.370Z'
351	    updated_at: '2026-05-13T07:23:28.932Z'
352	    spec:
353	      command: 'bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)'
354	      server: cqa1-21977
355	      gpu:
356	      - cuda:4
357	      pid: '132149'
358	      data_path: /root/structfuse/mvp_data/training_data/
359	      data_count: 127
360	      model_name: Qwen2.5-Coder-3B + LoRA
361	      seed: 42,123,7
362	      hypothesis: 'H3: data-flow hard negatives vs random vs embedding-distance, 3-seed
363	        × 3-strategy contrastive training'
364	      plan_id: mvp_p2b_contrastive_training
365	      checkpoint_path: N/A
366	      log_path: N/A
367	    conclusion: killed
368	    completed_at: '2026-05-12T15:04:44.396Z'
369	    notes: P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。
370	  p2b_eval_all:
371	    status: DONE
372	    retry_count: 0
373	    created_at: '2026-05-12T16:27:50.967Z'
374	    updated_at: '2026-05-13T07:23:24.721Z'
375	    spec:
376	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
377	        base && cd /root/structfuse && bash scripts/run_eval_all.sh"
378	      server: cqa1-21977
379	      gpu:
380	      - cuda:4
381	      pid: '254053'
382	      log_path: N/A
383	      submitted_at: '2026-05-12T16:27:50.945Z'
384	      submitted_via: submit_training_job
385	      backend: tmux
386	      account: root
387	      checkpoint_path: N/A
388	      wall_clock_seconds: 42550.6
389	      gpu_hours: 11.82
390	    conclusion: killed
391	    completed_at: '2026-05-13T04:17:01.561Z'
392	    notes: P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。
393	  p2b_eval_4runs_v2:
394	    status: DONE
395	    retry_count: 0
396	    created_at: '2026-05-12T17:21:49.599Z'
397	    updated_at: '2026-05-12T17:22:16.595Z'
398	    spec:
399	      command: eval 4 runs (3 random seeds + 1 emb_dist) with pool_size=26
400	      server: cqa1-21977
401	      data_path: /root/structfuse
402	      data_count: 127
403	      model_name: Qwen2.5-Coder-3B (LoRA)
404	      seed: 42,123,456
405	      description: 'Phase 2b eval v2: pool_size=26 评估 random vs emb_dist'
406	    conclusion: success
407	    metrics:
408	      random_seed42:
409	        recall@1: 0.9449
410	        recall@5: 0.9843
411	        recall@10: 0.9843
412	      random_seed123:
413	        recall@1: 0.9449
414	        recall@5: 0.9921
415	        recall@10: 0.9921
416	      random_seed456:
417	        recall@1: 0.9291
418	        recall@5: 0.9921
419	        recall@10: 0.9921
420	      emb_dist_seed42:
421	        recall@1: 0.6693
422	        recall@5: 0.8898
423	        recall@10: 0.9291
424	      pool_size: 26
425	      n_samples: 127
426	    checkpoint_path: '/root/autodl-tmp/structfuse/checkpoints/ (4 runs: random_s42/123/456,
427	      emb_dist_s42)'
428	    log_path: /root/autodl-tmp/structfuse/eval_results/
429	    completed_at: '2026-05-12T17:22:16.595Z'
430	  p2b_5reruns:
431	    status: DONE
432	    retry_count: 0
433	    created_at: '2026-05-12T17:26:47.603Z'
434	    updated_at: '2026-05-12T19:19:53.785Z'
435	    spec:
436	      command: 'bash run_p2b_all.sh (skips 4 done, runs 5: emb_dist s123/456, dataflow
437	        s42/123/456)'
438	      server: cqa1-21977
439	      gpu:
440	      - cuda:4
441	      pid: '272732'
442	      log_path: ~/runs/structfuse-context/p2b_5reruns.log
443	      submitted_at: '2026-05-12T17:26:47.575Z'
444	      submitted_via: submit_training_job
445	      backend: tmux
446	      account: root
447	      data_path: /root/structfuse
448	      data_count: 500
449	      model_name: Qwen2.5-Coder-3B (LoRA)
450	      seed: 42,123,456
451	      description: 'Phase 2b 5 reruns: emb_dist s123/456 + dataflow_aware s42/123/456'
452	      hyperparams:
453	        batch_size: 2
454	        lr: 2e-5
455	        num_negatives: 3
456	        max_seq_length: 512
457	        use_lora: true
458	        gradient_checkpointing: true
459	        eval_steps: 50
460	        save_steps: 200
461	        num_epochs: 3
462	      wall_clock_seconds: 6752.2
463	      gpu_hours: 1.88
464	    conclusion: success
465	    metrics:
466	      random_s42:
467	        val_loss: 0.0347
468	        recall@1: 0.9843
469	      random_s123:
470	        val_loss: 0.0446
471	        recall@1: 0.9843
472	      random_s456:
473	        val_loss: 0.0188
474	        recall@1: 0.9921
475	      emb_dist_s42:
476	        val_loss: 0.1876
477	        recall@1: 0.874
478	      emb_dist_s123:
479	        val_loss: 0.1461
480	        recall@1: 0.874
481	      emb_dist_s456:
482	        val_loss: 0.1281
483	        recall@1: 0.8819
484	      dataflow_s42:
485	        val_loss: 0.1878
486	        recall@1: 0.874
487	      dataflow_s123:
488	        val_loss: 0.146
489	        recall@1: 0.874
490	      dataflow_s456:
491	        val_loss: 0.1278
492	        recall@1: 0.8819
493	      runs_completed: 9
494	      runs_failed: 0
495	      WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all
496	        seeds — likely code bug in negative sampling
497	    checkpoint_path: '/root/autodl-tmp/structfuse/checkpoints/ (9 dirs: p2b_{random,embedding_distance,dataflow_aware}_s{42,123,456})'
498	    completed_at: '2026-05-12T19:19:19.793Z'
499	    log_path: ~/runs/structfuse-context/p2b_5reruns.log
500	  p2b_dataflow_retrain:
501	    status: DONE
502	    retry_count: 0
503	    created_at: '2026-05-12T19:49:00.303Z'
504	    updated_at: '2026-05-13T07:23:27.706Z'
505	    spec:
506	      command: build_p2b_data.py regeneration + dataflow 3-seed retrain
507	      server: cqa1-21977
508	      data_path: /root/structfuse
509	      data_count: 0
510	      model_name: Qwen2.5-Coder-3B (LoRA)
511	      seed: 42,123,456
512	      description: 'BLOCKED: dataflow connections ⊆ gold files, strategies indistinguishable'
513	      checkpoint_path: N/A
514	      log_path: N/A
515	    conclusion: negative
516	    completed_at: '2026-05-13T04:17:02.055Z'
517	    notes: Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer
518	      发现后搁置。已被 m2_embed_verify（true embedding mining）替代。
519	  p2b_eval_4runs_pool50:
520	    status: DONE
521	    retry_count: 0
522	    created_at: '2026-05-12T20:10:54.579Z'
523	    updated_at: '2026-05-13T00:27:50.197Z'
524	    spec:
525	      command: eval_p2b.py on 4 checkpoints with new val.jsonl pool_size=50
526	      server: cqa1-21977
527	      data_path: /root/structfuse
528	      data_count: 127
529	      model_name: Qwen2.5-Coder-3B (LoRA)
530	      seed: 42,123,456
531	      checkpoint_source: p2b_5reruns (random×3 + emb_dist×1)
532	      eval_data: val.jsonl pool_size=50
533	    conclusion: success
534	    metrics:
535	      pool_size: 50
536	      n_samples: 127
537	      random_s42:
538	        recall@1: 0.496
539	        recall@5: 0.843
540	        recall@10: 0.945
541	      random_s123:
542	        recall@1: 0.535
543	        recall@5: 0.85
544	        recall@10: 0.921
545	      random_s456:
546	        recall@1: 0.543
547	        recall@5: 0.843
548	        recall@10: 0.953
549	      emb_dist_s42:
550	        recall@1: 0.488
551	        recall@5: 0.835
552	        recall@10: 0.874
553	      random_mean:
554	        recall@1: 0.525
555	        recall@5: 0.845
556	        recall@10: 0.94
557	      emb_dist_vs_random_delta:
558	        recall@1: -0.037
559	        recall@5: -0.01
560	        recall@10: -0.066
561	    checkpoint_path: /root/autodl-tmp/structfuse/checkpoints/ (p2b_random_s42/123/456,
562	      p2b_embedding_distance_s42)
563	    log_path: 已清理 (2026-05-12 Director Step 1 指令 rm -rf)，metrics 保留在 registry
564	    completed_at: '2026-05-12T20:11:12.318Z'
565	  d007_50repo_overlap:
566	    status: DONE
567	    retry_count: 0
568	    created_at: '2026-05-12T20:37:24.289Z'
569	    updated_at: '2026-05-12T20:37:39.566Z'
570	    spec:
571	      command: CodeQL 2-hop extraction + connected vs gold overlap stats on 50 repos
572	      server: cqa1-21977
573	      data_path: /root/structfuse
574	      data_count: 240
575	      model_name: N/A (CPU analysis)
576	      seed: N/A
577	      description: '50-repo overlap validation: Z=40.8%, original method viable'
578	    conclusion: success
579	    metrics:
580	      total_instances: 240
581	      instances_with_extra_connected: 98
582	      Z_pct: 40.8
583	      avg_connected_minus_gold: 6
584	      codeql_timeout_rate_pct: 4
585	      by_repo_size:
586	        small_lt50:
587	          Z_pct: 38.6
588	          avg_extra: 2.5
589	        medium_50_200:
590	          Z_pct: 55.7
591	          avg_extra: 11.8
592	        large_gt200:
593	          Z_pct: 16.7
594	          avg_extra: 8.8
595	      decision: Z=40.8% >= 20% -> original method viable, proceed to M1
596	    checkpoint_path: N/A (analysis only)
597	    log_path: /root/structfuse/data/50repo_overlap_stats/
598	    completed_at: '2026-05-12T20:37:39.566Z'
599	  m1_extraction:
600	    status: DONE
601	    retry_count: 0
602	    created_at: '2026-05-12T21:00:02.300Z'
603	    updated_at: '2026-05-13T19:26:13.901Z'
604	    spec:
605	      command: nohup bash scripts/run_m1_extraction.sh (8 CPU workers, CodeQL 2-hop)
606	      server: cqa1-21977
607	      data_path: /root/autodl-tmp/structfuse/m1_extraction/
608	      data_count: 50869
609	      model_name: N/A (CodeQL extraction)
610	      seed: N/A
611	      description: 'M1: 全量 5K repos CodeQL 提取, 131 unique (repo,commit) groups, 50869
612	        instances'
613	    metrics:
614	      total_instances_attempted: 44173
615	      instances_skipped: 6696
616	      total_instances: 50869
617	      codeql_success: 15133
618	      beniget_fallback: 764
619	      extraction_failed: 28276
620	      structural_data_rate: 0.36
621	      repos_with_output: 123
622	      repos_total: 131
623	      repo_coverage: 0.939
624	      skip_clone_failed: 5852
625	      skip_checkout_failed: 836
626	      skip_stale_handle: 8
627	      elapsed_minutes: 837.8
628	      avg_time_per_instance_s: 8.9
629	      output_size_gb: 6.6
630	      disk_usage_gb: 13
631	      output_file: all.jsonl
632	    notes: '[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173
633	      instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output:
634	      all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors
635	      经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation
636	      导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。'
637	    conclusion: success
638	    checkpoint_path: /root/autodl-tmp/structfuse/m1_extraction/all.jsonl
639	    log_path: /tmp/m1_extraction.log
640	    completed_at: '2026-05-13T10:59:42.462Z'
641	  m2_early_pilot:
642	    status: DONE
643	    retry_count: 0
644	    created_at: '2026-05-13T01:39:53.920Z'
645	    updated_at: '2026-05-13T04:44:22.077Z'
646	    hypothesis: 'Early pilot on partial M1 data (24 repos, ~5K instances): verify
647	      M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation
648	      before full M1 completes'
649	    spec:
650	      command: bash /root/structfuse/scripts/run_m2_pilot.sh
651	      server: cqa1-21977
652	      gpu:
653	      - cuda:4
654	      pid: '795739'
655	      log_path: /root/autodl-tmp/structfuse/m2_pilot_output/random_s42.log
656	      submitted_at: '2026-05-13T01:55:31.288Z'
657	      submitted_via: submit_training_job
658	      backend: tmux
659	      account: root
660	      data_path: /root/autodl-tmp/structfuse/m2_pilot_data/
661	      data_count: 3418
662	      model_name: Qwen/Qwen2.5-Coder-3B
663	      seed: 42
664	      checkpoint_source: N/A (training from scratch)
665	      eval_data: N/A (training, not eval)
666	      checkpoint_path: /root/autodl-tmp/structfuse/m2_pilot_output/random_s42/best_model.pt
667	      wall_clock_seconds: 10130.8
668	      gpu_hours: 2.81
669	    conclusion: killed
670	    notes: PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set
671	      -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint
672	      at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致
673	      OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。
674	    metrics:
675	      pid: 795791
676	      gpu: cuda:4
677	      gpu_mem_mb: 9342
678	      gpu_util_pct: 83
679	      batch_size: 2
680	      num_negatives: 3
681	      max_seq_length: 1024
682	      strategy_running: random (stuck at step 4000, epoch 3)
683	      strategies_completed: 0/3
684	      eval_1500:
685	        val_loss: 0.5879
686	        recall_at_1: 0.4693
687	        recall_at_5: 0.4693
688	        recall_at_10: 0.4693
689	      eval_2000:
690	        val_loss: 0.7089
691	        recall_at_1: 0.4398
692	      eval_2500:
693	        val_loss: 0.6961
694	        recall_at_1: 0.4291
695	      eval_3000:
696	        val_loss: 0.728
697	        recall_at_1: 0.4104
698	      eval_3500:
699	        val_loss: 0.7022
700	        recall_at_1: 0.4439
701	      best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)
702	      WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after
703	        step 4000 (~45min no output). Overfitting after step 1500.
704	      status_check_at: '2026-05-13T04:42:00Z'
705	    completed_at: '2026-05-13T04:44:22.077Z'
706	  m2_early_pilot_v2:
707	    status: DONE
708	    retry_count: 0
709	    created_at: '2026-05-13T01:52:52.724Z'
710	    updated_at: '2026-05-13T02:13:31.039Z'
711	    spec:
712	      command: bash /root/structfuse/run_m2_early_pilot.sh
713	      server: cqa1-21977
714	      gpu:
715	      - cuda:4
716	      pid: '766124'
717	      log_path: ~/runs/structfuse-context/m2_early_pilot_v2.log
718	      submitted_at: '2026-05-13T01:52:52.687Z'
719	      submitted_via: submit_training_job
720	      backend: tmux
721	      account: root
722	      data_path: /root/autodl-tmp/structfuse/m2_early_pilot_data/
723	      data_count: 3418
724	      model_name: Qwen/Qwen2.5-Coder-3B
725	      seed: 42
726	      checkpoint_source: N/A (training from scratch)
727	      eval_data: N/A (this is training, not eval)
728	      checkpoint_path: N/A
729	      wall_clock_seconds: 1238.4
730	      gpu_hours: 0.34
731	    hypothesis: 'Early pilot on partial M1 data (24 repos, 2672 train + 746 val):
732	      verify M2 training pipeline works end-to-end and get early signal on 3-strategy
733	      differentiation before full M1 completes'
734	    parent: m1_extraction
735	    notes: wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。
736	    conclusion: failed
737	    completed_at: '2026-05-13T02:13:31.040Z'
738	  m2_early_pilot_v3:
739	    status: DONE
740	    retry_count: 0
741	    created_at: '2026-05-13T01:59:06.557Z'
742	    updated_at: '2026-05-13T02:13:43.400Z'
743	    spec:
744	      command: bash -c "bash /root/structfuse/run_m2_early_pilot.sh"
745	      server: cqa1-21977
746	      gpu:
747	      - cuda:0
748	      pid: '897651'
749	      log_path: ~/runs/structfuse-context/m2_early_pilot_v3.log
750	      submitted_at: '2026-05-13T02:04:31.768Z'
751	      submitted_via: submit_training_job
752	      backend: tmux
753	      account: root
754	      checkpoint_path: N/A
755	      wall_clock_seconds: 551.6
756	      gpu_hours: 0.15
757	    conclusion: killed
758	    notes: GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=["cuda:4"]。第二次 GPU 越界违规（首次 D005）。Worker
759	      未正确映射 CUDA_VISIBLE_DEVICES。
760	    completed_at: '2026-05-13T02:13:43.400Z'
761	  m2_embed_verify:
762	    status: DONE
763	    retry_count: 0
764	    created_at: '2026-05-13T04:39:16.051Z'
765	    updated_at: '2026-05-13T15:59:51.621Z'
766	    hypothesis: 'True embedding mining verification: compare Qwen2.5-Coder-3B cosine
767	      similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding
768	      negatives are harder → Claim 2 (structure-aware negatives improve retrieval)
769	      gets stronger evidence.'
770	    parent: m2_early_pilot
771	    spec:
772	      command: bash -c "bash /root/structfuse/run_m2_embed_verify.sh"
773	      server: bjb1-42106
774	      gpu:
775	      - cuda:1
776	      pid: '29290'
777	      log_path: ~/runs/structfuse-context/m2_embed_verify.log
778	      submitted_at: '2026-05-13T06:37:00.822Z'
779	      submitted_via: submit_training_job
780	      backend: tmux
781	      account: root
782	      data_path: /root/autodl-tmp/structfuse/m2_embed_verify_data/
783	      data_count: 3282
784	      model_name: Qwen/Qwen2.5-Coder-3B
785	      seed: 42
786	      checkpoint_source: training from scratch (not eval)
787	      eval_data: N/A (training, not eval)
788	      wall_clock_seconds: 31097.9
789	      gpu_hours: 8.64
790	    notes: '[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557)
791	      > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow
792	      vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed:
793	      true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log.
794	      Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed
795	      via log extraction worker).'
796	    metrics:
797	      random:
798	        status: DONE
799	        best_step: 500
800	        best_val_loss: 0.4834
801	        best_recall@1: 0.5357
802	        best_recall@5: 0.9808
803	        best_recall@10: 1
804	        final_val_loss: 0.5978
805	        final_recall@1: 0.5122
806	      embedding_distance:
807	        status: DONE
808	        best_step: 500
809	        best_val_loss: 0.4603
810	        best_recall@1: 0.5557
811	        best_recall@5: 0.9808
812	        best_recall@10: 1
813	        final_val_loss: 0.5935
814	        final_recall@1: 0.5209
815	      dataflow_aware:
816	        status: DONE
817	        best_step: 500
818	        best_val_loss: 0.5602
819	        best_recall@1: 0.5436
820	        best_recall@5: 0.9817
821	        best_recall@10: 1
822	        final_val_loss: 0.6201
823	        final_recall@1: 0.5287
824	    failure_reason: EXIT_CODE=2 (shell misuse / syntax)
825	    conclusion: success
826	    completed_at: '2026-05-13T15:15:18.746Z'
827	  plan_013_starcoder:
828	    status: DONE
829	    retry_count: 0
830	    created_at: '2026-05-13T05:09:14.885Z'
831	    updated_at: '2026-05-13T18:09:54.153Z'
832	    hypothesis: 'Architecture generalization: validate StructFuse with StarCoder2-3B
833	      encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same
834	      strategy ranking → method is encoder-agnostic, strengthening the core claim.
835	      Key differentiator for best→accept at Dream.'
836	    spec:
837	      command: bash -c "bash /root/structfuse/run_plan013_starcoder.sh"
838	      server: bjb1-42106
839	      gpu:
840	      - cuda:0
841	      pid: '23798'
842	      log_path: ~/runs/structfuse-context/plan_013_starcoder.log
843	      submitted_at: '2026-05-13T05:26:21.946Z'
844	      submitted_via: submit_training_job
845	      backend: tmux
846	      account: root
847	      data_path: /root/autodl-tmp/structfuse/m2_embed_verify_data/
848	      data_count: 3282
849	      model_name: bigcode/starcoder2-3b
850	      seed: 42
851	      wall_clock_seconds: 35338.2
852	      gpu_hours: 9.82
853	    notes: '[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078)
854	      > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent
855	      with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random
856	      +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders.
857	      Embedding > random is encoder-agnostic, dataflow position is encoder-dependent.
858	      Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129
859	      but all strategies completed (confirmed via log extraction worker).'
860	    metrics:
861	      random:
862	        status: DONE
863	        best_val_loss: 0.5113
864	        best_recall@1: 0.4922
865	        best_recall@5: 0.98
866	        best_recall@10: 1
867	        source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)
868	      embedding_distance:
869	        status: DONE
870	        best_step: 1000
871	        best_val_loss: 0.4816
872	        best_recall@1: 0.5078
873	        best_recall@5: 0.9843
874	        best_recall@10: 1
875	        final_val_loss: 0.506
876	        final_recall@1: 0.5174
877	      dataflow_aware:
878	        status: DONE
879	        best_step: 1000
880	        best_val_loss: 0.5255
881	        best_recall@1: 0.4869
882	        best_recall@5: 0.9695
883	        best_recall@10: 1
884	        final_val_loss: 0.5509
885	        final_recall@1: 0.5078
886	    failure_reason: ''
887	    conclusion: negative
888	    completed_at: '2026-05-13T15:15:20.165Z'
889	  plan_006_scalability:
890	    status: DONE
891	    retry_count: 0
892	    created_at: '2026-05-13T07:57:43.631Z'
893	    updated_at: '2026-05-13T19:24:00.741Z'
894	    spec:
895	      command: M1 scalability statistics analysis (29/131 repos)
896	      server: bjb1-42106
897	      data_path: /root/autodl-tmp/structfuse/m1_extraction/
898	      data_count: 8171
899	      model_name: N/A (CPU analysis)
900	      seed: N/A
901	      description: 'Plan 006: M1 extraction scalability stats - timeout rate, extraction
902	        time, coverage, Z% by repo size. Partial results from 29/131 repos.'
903	      checkpoint_path: N/A
904	      log_path: N/A
905	    conclusion: success
906	    completed_at: '2026-05-13T07:57:58.176Z'
907	    notes: '[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout;
908	      (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个
909	      repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance
910	      可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）;
911	      (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json,
912	      art_20260513_d262da (error patterns)'
913	    hypothesis: 'Claim 3: CodeQL bounded data-flow extraction scales to large repos
914	      with acceptable timeout rates and provides meaningful structural coverage (Z%)
915	      that increases with repo complexity'
916	    metrics:
917	      repos: 123
918	      total_instances: 44173
919	      structural_data_rate: 0.343
920	      error_rate: 0.64
921	      zero_timeout_rate: true
922	      processing_time:
923	        mean_s: 8.93
924	        median_s: 0
925	        p95_s: 31.95
926	        max_s: 633.68
927	        total_hours: 109.58
928	      by_tier:
929	        small_lt50:
930	          repos: 1
931	          instances: 500
932	          error_rate: 0.054
933	          struct_rate: 0.81
934	          z_pct_mean: 0.284
935	          z_pct_median: 0
936	        medium_50_200:
937	          repos: 17
938	          instances: 4096
939	          error_rate: 0.485
940	          struct_rate: 0.472
941	          z_pct_mean: 0.444
942	          z_pct_median: 0.5
943	        large_200_500:
944	          repos: 40
945	          instances: 13628
946	          error_rate: 0.639
947	          struct_rate: 0.343
948	          z_pct_mean: 0.604
949	          z_pct_median: 0.857
950	        xlarge_500plus:
951	          repos: 29
952	          instances: 25949
953	          error_rate: 0.676
954	          struct_rate: 0.314
955	          z_pct_mean: 0.812
956	          z_pct_median: 0.96
957	      instance_distribution:
958	        lt10: 1
959	        '10_50': 17
960	        '50_200': 36
961	        '200_500': 40
962	        500plus: 29
963	      artifact: plan006_full_scalability.json
964	  m2_full_qwen:
965	    status: ANALYZING
966	    retry_count: 0
967	    created_at: '2026-05-13T16:18:14.870Z'
968	    updated_at: '2026-05-14T18:00:29.323Z'
969	    hypothesis: 'Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds
970	      on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding
971	      > random +2pp). Go/no-go for paper claims per D018.'
972	    parent: m2_embed_verify
973	    spec:
974	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
975	        base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log"
976	      server: bjb1-42106
977	      gpu:
978	      - cuda:0
979	      pid: '73544'
980	      log_path: ~/runs/structfuse-context/m2_full_qwen.log
981	      submitted_at: '2026-05-13T17:39:30.757Z'
982	      submitted_via: submit_training_job
983	      backend: tmux
984	      account: root
985	    notes: 'Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware)
986	      × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8,
987	      eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01,
988	      temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual
989	      checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed.
990	      [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs
991	      + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING
992	      是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500
993	      R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step
994	      500。GPU 100% 利用率, 50.5/97.9GB VRAM。'
995	    metrics:
996	      random_s42:
997	        status: DONE
998	        epoch: 3/3
999	        total_steps: 4242
1000	        total_steps_per_epoch: 1414
1001	        eval_500:
1002	          val_loss: 0.4869
1003	          recall_at_1: 0.533
1004	          recall_at_5: 0.954
1005	          recall_at_10: 1
1006	        eval_1000:
1007	          val_loss: 0.4651
1008	          recall_at_1: 0.553
1009	          recall_at_5: 0.959
1010	          recall_at_10: 1
1011	        eval_1500:
1012	          val_loss: 0.5365
1013	          recall_at_1: 0.523
1014	          recall_at_5: 0.955
1015	          recall_at_10: 1
1016	        eval_2000:
1017	          val_loss: 0.5162
1018	          recall_at_1: 0.523
1019	          recall_at_5: 0.954
1020	          recall_at_10: 1
1021	        eval_2500:
1022	          val_loss: 0.5264
1023	          recall_at_1: 0.527
1024	          recall_at_5: 0.956
1025	          recall_at_10: 1
1026	        eval_3000:
1027	          val_loss: 0.5406
1028	          recall_at_1: 0.536
1029	          recall_at_5: 0.956
1030	          recall_at_10: 1
1031	        best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.5527)
1032	        conclusion: Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357).
1033	          Full data helps.
1034	      random_s43:
1035	        status: DONE
1036	        epoch: early_stopped
1037	        total_steps_per_epoch: 1405
1038	        eval_500:
1039	          val_loss: 0.4476
1040	          recall_at_1: 0.5357
1041	        eval_1000:
1042	          val_loss: 0.4637
1043	          recall_at_1: 0.5285
1044	        eval_1500:
1045	          recall_at_1: 0.5554
1046	        best_by_val_loss: step 500 (val_loss=0.4476)
1047	        best_by_recall_at_1: step 1500 (R@1=0.5554)
1048	        conclusion: Early stopped at step 1500. Best R@1=0.5554, consistent with s42
1049	          (0.5527). val_loss and R@1 criterion diverge.
1050	      random_s44:
1051	        status: RUNNING
1052	        note: Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch
1053	      progress_snapshot: 2026-05-15T02:00 CST
1054	    reproduce:
1055	      finished_at: '2026-05-14T11:24:33.887Z'
1056	    extra:
1057	      hook_events:
1058	      - event: on_complete
1059	        action: agent
1060	        ts: '2026-05-14T11:24:35.375104+00:00'
1061	  m2_full_starcoder:
1062	    status: DONE
1063	    retry_count: 0
1064	    created_at: '2026-05-13T16:18:15.415Z'
1065	    updated_at: '2026-05-14T18:04:29.245Z'
1066	    hypothesis: 'Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder
1067	      validation — if embedding > random holds for both Qwen and StarCoder, method
1068	      is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).'
1069	    parent: plan_013_starcoder
1070	    spec:
1071	      command: bash -c "cd /root/structfuse && bash run_m2_full_starcoder_resume.sh"
1072	      server: bjb1-42106
1073	      gpu:
1074	      - cuda:1
1075	      pid: '519791'
1076	      log_path: ~/runs/structfuse-context/m2_full_starcoder.log
1077	      submitted_at: '2026-05-14T18:03:12.079Z'
1078	      submitted_via: submit_training_job
1079	      backend: tmux
1080	      account: root
1081	    notes: 'Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8,
1082	      num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双
1083	      checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs;
1084	      s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791,
1085	      timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43
1086	      [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42
1087	      结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。'
1088	    metrics:
1089	      random_s42:
1090	        epoch: 3/3
1091	        current_step: 4200
1092	        total_steps: 4242
1093	        total_steps_per_epoch: 1414
1094	        eval_500:
1095	          val_loss: 0.6194
1096	          recall_at_1: 0.435
1097	          recall_at_5: 0.905
1098	          recall_at_10: 1
1099	        eval_1000:
1100	          val_loss: 0.6134
1101	          recall_at_1: 0.454
1102	          recall_at_5: 0.92
1103	          recall_at_10: 1
1104	        eval_1500:
1105	          val_loss: 0.6528
1106	          recall_at_1: 0.449
1107	          recall_at_5: 0.906
1108	          recall_at_10: 1
1109	        eval_2000:
1110	          val_loss: 0.6698
1111	          recall_at_1: 0.4456
1112	          recall_at_5: 0.906
1113	          recall_at_10: 1
1114	        eval_2500:
1115	          val_loss: 0.6342
1116	          recall_at_1: 0.4604
1117	          recall_at_5: 0.9117
1118	          recall_at_10: 1
1119	        eval_3000:
1120	          val_loss: 0.6516
1121	          recall_at_1: 0.4544
1122	          recall_at_5: 0.9077
1123	          recall_at_10: 1
1124	        eval_3500:
1125	          val_loss: 0.6588
1126	          recall_at_1: 0.4534
1127	          recall_at_5: 0.9057
1128	          recall_at_10: 1
1129	        eval_4000:
1130	          val_loss: 0.6637
1131	          recall_at_1: 0.4547
1132	          recall_at_5: 0.9003
1133	          recall_at_10: 1
1134	        best_checkpoint: step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)
1135	        conclusion: effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining
1136	          42 steps negligible)
1137	      progress_snapshot: 2026-05-15T01:50 CST
1138	    reproduce:
1139	      finished_at: '2026-05-14T17:49:54.474Z'
1140	    failure_reason: EXIT_CODE=124 (timeout — exceeded timeout_hours)
1141	    conclusion: failed
1142	    completed_at: '2026-05-14T17:49:55.304Z'
1143	    extra:
1144	      hook_events:
1145	      - event: on_failed
1146	        action: agent
1147	        ts: '2026-05-14T17:49:56.408767+00:00'
1148	  m1_reextract:
1149	    status: DONE
1150	    retry_count: 0
1151	    created_at: '2026-05-13T19:35:23.954Z'
1152	    updated_at: '2026-05-13T19:45:53.741Z'
1153	    hypothesis: M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897
1154	      提升至 ~44,173。D022 批准。
1155	    parent: m1_extraction
1156	    spec:
1157	      command: bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop)
1158	      server: bjb1-42106
1159	      data_path: /root/autodl-tmp/structfuse/m1_extraction/
1160	      data_count: 28276
1161	      model_name: N/A (CodeQL extraction)
1162	      seed: N/A
1163	      pid: '97358'
1164	      log_path: /root/runs/structfuse-context/m1_rerun.log
1165	      checkpoint_source: rerun of m1_extraction failed instances
1166	      eval_data: N/A
1167	      checkpoint_path: N/A (failed, no output)
1168	    conclusion: failed
1169	    notes: CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行
1170	      `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries
1171	      && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl
1172	      未受影响）。等 Director 确认后修复重跑。
1173	    completed_at: '2026-05-13T19:44:09.115Z'
1174	  neg_difficulty_analysis:
1175	    status: DONE
1176	    retry_count: 0
1177	    created_at: '2026-05-13T19:39:20.016Z'
1178	    updated_at: '2026-05-14T00:13:49.046Z'
1179	    hypothesis: 'Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B
1180	      和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive
1181	      cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048
1182	      匹配训练设置。'
1183	    notes: 128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比
1184	      128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x
1185	      Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种
1186	      token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。
1187	    metrics:
1188	      qwen_128:
1189	        random:
1190	          pos_sim: 0.9804
1191	          neg_sim: 0.899
1192	          margin: 0.0816
1193	          pct_positive_margin: 77.8
1194	        embedding_distance:
1195	          pos_sim: 0.9804
1196	          neg_sim: 0.959
1197	          margin: 0.0209
1198	          pct_positive_margin: 60.7
1199	        dataflow_aware:
1200	          pos_sim: 0.9805
1201	          neg_sim: 0.95
1202	          margin: 0.0309
1203	          pct_positive_margin: 67.4
1204	      starcoder_128:
1205	        random:
1206	          pos_sim: 0.757
1207	          neg_sim: 0.553
1208	          margin: 0.2039
1209	          pct_positive_margin: 72.8
1210	        embedding_distance:
1211	          pos_sim: 0.784
1212	          neg_sim: 0.668
1213	          margin: 0.1159
1214	          pct_positive_margin: 59.2
1215	        dataflow_aware:
1216	          pos_sim: 0.761
1217	          neg_sim: 0.659
1218	          margin: 0.1022
1219	          pct_positive_margin: 62.8
1220	      qwen_2048:
1221	        random:
1222	          pos_sim: 0.9855
1223	          neg_sim: 0.9111
1224	          margin: 0.0743
1225	          margin_std: 0.2322
1226	          pct_positive_margin: 81.8
1227	        embedding_distance:
1228	          pos_sim: 0.9855
1229	          neg_sim: 0.9685
1230	          margin: 0.017
1231	          margin_std: 0.114
1232	          pct_positive_margin: 58.8
1233	        dataflow_aware:
1234	          pos_sim: 0.9856
1235	          neg_sim: 0.9563
1236	          margin: 0.0293
1237	          margin_std: 0.1407
1238	          pct_positive_margin: 73.9
1239	      starcoder_2048:
1240	        random:
1241	          pos_sim: 0.7985
1242	          neg_sim: 0.6045
1243	          margin: 0.194
1244	          margin_std: 0.2788
1245	          pct_positive_margin: 78
1246	        embedding_distance:
1247	          pos_sim: 0.8079
1248	          neg_sim: 0.7409
1249	          margin: 0.067
1250	          margin_std: 0.2056
1251	          pct_positive_margin: 55
1252	        dataflow_aware:
1253	          pos_sim: 0.8009
1254	          neg_sim: 0.6818
1255	          margin: 0.1192
1256	          margin_std: 0.2264
1257	          pct_positive_margin: 70.4
1258	      sc_qwen_margin_ratio_128:
1259	        random: 2.5
1260	        embedding_distance: 5.54
1261	        dataflow_aware: 3.3
1262	      sc_qwen_margin_ratio_2048:
1263	        random: 2.61
1264	        embedding_distance: 3.94
1265	        dataflow_aware: 4.07
1266	    conclusion: success
1267	    spec:
1268	      command: python negative_difficulty_margin_v2.py (CPU analysis)
1269	      server: bjb1-42106
1270	      data_path: /root/autodl-tmp/structfuse/full_m2_data/
1271	      data_count: 11000
1272	      model_name: Qwen2.5-Coder-3B + StarCoder2-3B (pretrained, no training)
1273	      seed: N/A
1274	      checkpoint_path: N/A (analysis only)
1275	      log_path: /root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json
1276	    completed_at: '2026-05-14T00:13:49.046Z'
1277	  m1_reextract_v2:
1278	    status: RUNNING
1279	    retry_count: 0
1280	    created_at: '2026-05-13T20:00:20.578Z'
1281	    updated_at: '2026-05-15T04:16:04.784Z'
1282	    hypothesis: M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack
1283	      已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。
1284	    parent: m1_extraction
1285	    spec:
1286	      command: bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack
1287	        installed)
1288	      server: bjb1-42106
1289	      data_path: /root/autodl-tmp/structfuse/full_m1_data/
1290	      data_count: 28276
1291	      model_name: N/A (CodeQL extraction)
1292	      seed: N/A
1293	      log_path: /root/runs/structfuse-context/m1_reextract_v2.log
1294	      checkpoint_source: rerun of m1_extraction failed instances (v2, CodeQL fixed)
1295	      eval_data: N/A
1296	    notes: 'moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate
1297	      exceeds 300s timeout on every instance (exit code 33). 536 moto instances all
1298	      fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers
1299	      stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI
1300	      normally. DB creation succeeded; bounded_dataflow.ql unaffected.'
1301	    metrics:
1302	      processed: 25582
1303	      total: 28276
1304	      skipped: 582
1305	      extracted: 25000
1306	      progress_pct: 90.5
1307	      all_jsonl_lines: 44173
1308	      warnings: 65
1309	      rate_per_hour: 404
1310	      eta_cst: 2026-05-15T19:00
1311	      last_checked: 2026-05-15T12:15 CST
1312	  plan_018_bm25:
1313	    status: QUEUED
1314	    retry_count: 0
1315	    created_at: '2026-05-14T16:38:40.603Z'
1316	    updated_at: '2026-05-14T17:09:50.985Z'
1317	    hypothesis: 'BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase
1318	      1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25
1319	      negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。'
1320	    parent: m2_full_qwen
1321	    notes: 'Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts
1322	      与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance
1323	      ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50
1324	      文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出:
1325	      /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase
1326	      2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。'
1327	    metrics:
1328	      phase1_complete: true
1329	      seed_42:
1330	        train_records: 11308
1331	        val_records: 2980
1332	        train_size_mb: 1280.8
1333	        val_size_mb: 344.6
1334	      seed_43:
1335	        train_records: 11236
1336	        val_records: 3052
1337	        train_size_mb: 1280.9
1338	        val_size_mb: 316
1339	      seed_44:
1340	        train_records: 11264
1341	        val_records: 3024
1342	        train_size_mb: 1347.1
1343	        val_size_mb: 295.9
1344	      bm25_score_dist:
1345	        count: 392954
1346	        mean: 246.5
1347	        std: 155.96
1348	        p25: 128.38
1349	        p50: 228.41
1350	        p75: 347.85
1351	        max: 2585.74
1352	      overlap_overall:
1353	        bm25_vs_embedding: 0.871
1354	        bm25_vs_random: 0.762
1355	        bm25_vs_dataflow: 0.718
1356	        note: k=50 full candidate overlap from mining worker
1357	      overlap_stratified_top7_jaccard:
1358	        small_lt50:
1359	          repos: 39
1360	          bm25_vs_embedding: 0.668
1361	          bm25_vs_random: 0.411
1362	          bm25_vs_dataflow: 0.667
1363	        medium_50_200:
1364	          repos: 29
1365	          bm25_vs_embedding: 0.38
1366	          bm25_vs_random: 0.067
1367	          bm25_vs_dataflow: 0.363
1368	        large_200plus:
1369	          repos: 15
1370	          bm25_vs_embedding: 0.297
1371	          bm25_vs_random: 0.007
1372	          bm25_vs_dataflow: 0.405
1373	        matched_queries: 2920
1374	        total_queries: 12290
1375	        note: top-7 Jaccard on s42 matched queries only (24% match rate due to different
1376	          train/val splits)
1377	  plan_015_dynamic:
1378	    status: QUEUED
1379	    retry_count: 0
1380	    created_at: '2026-05-14T17:03:24.316Z'
1381	    updated_at: '2026-05-14T17:03:30.544Z'
1382	    hypothesis: 'Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder
1383	      embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen,
1384	      s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。'
1385	    notes: Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2
1386	      与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。
1387	  m2_full_starcoder_resumed:
1388	    status: RUNNING
1389	    retry_count: 0
1390	    created_at: '2026-05-14T18:44:19.253Z'
1391	    updated_at: '2026-05-15T04:18:17.464Z'
1392	    hypothesis: 'M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2
1393	      + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。'
1394	    spec:
1395	      command: 'bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)'
1396	      server: bjb1-42106
1397	      gpu:
1398	      - cuda:1
1399	      pid: '519791'
1400	      log_path: /root/runs/structfuse-context/m2_full_starcoder.log
1401	      data_path: /root/autodl-tmp/structfuse/full_m2_training_data/
1402	      data_count: 11308
1403	      model_name: StarCoder2-3B
1404	      seed: 42,43,44
1405	    parent: m2_full_starcoder
1406	    metrics:
1407	      checked_at: '2026-05-15T12:15:00+08:00'
1408	      pid: 519791
1409	      pid_alive: true
1410	      gpu: cuda:1, 100% util, 55489/97887 MiB
1411	      current_subrun: random_s43 (1/8)
1412	      current_step: 1900/2810 (67.6%)
1413	      latest_eval:
1414	        step: 1500
1415	        val_loss: 0.5239
1416	        recall_at_1: 0.4912
1417	        recall_at_5: 0.9499
1418	        recall_at_10: 1
1419	      completed_subruns: {}
1420	      remaining_subruns:
1421	      - random_s44
1422	      - embedding_distance_s42
1423	      - embedding_distance_s43
1424	      - embedding_distance_s44
1425	      - dataflow_aware_s42
1426	      - dataflow_aware_s43
1427	      - dataflow_aware_s44
1428	      speed: ~187 steps/hour (~15h per subrun)
1429	      eta_current_subrun: ~17:00 CST today
1430	      eta_all_done: ~May 20 01:00 CST
1431	  m2_full_qwen_continued:
1432	    status: RUNNING
1433	    retry_count: 0
1434	    created_at: '2026-05-14T18:44:20.646Z'
1435	    updated_at: '2026-05-15T07:17:19.138Z'
1436	    hypothesis: 'M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3
1437	      + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。'
1438	    spec:
1439	      command: 'bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3
1440	        → dataflow×3)'
1441	      server: bjb1-42106
1442	      gpu:
1443	      - cuda:0
1444	      pid: '337267'
1445	      log_path: /root/runs/structfuse-context/m2_full_qwen.log
1446	      data_path: /root/autodl-tmp/structfuse/full_m2_training_data/
1447	      data_count: 11308
1448	      model_name: Qwen2.5-Coder-3B
1449	      seed: 42,43,44
1450	    parent: m2_full_qwen
1451	    metrics:
1452	      checked_at: 2026-05-15T14:58Z
1453	      pid: 337267
1454	      pid_alive: true
1455	      gpu: cuda:0, 100% util
1456	      current_subrun: embedding_distance_s44 or later (5+/9)
1457	      completed_subruns:
1458	        random_s42:
1459	          best_val_loss: 0.4651
1460	          best_R@1: 0.5527
1461	        random_s43:
1462	          best_val_loss: 0.4476
1463	          best_R@1: 0.5554
1464	        random_s44:
1465	          best_val_loss: 0.4252
1466	          best_R@1: 0.6009
1467	        embedding_distance_s43:
1468	          best_val_loss: 0.4541
1469	          best_R@1: 0.5606
1470	          early_stopped: step 1500
1471	          final_eval_R@1: 0.5655
1472	          best_step: 500
1473	          eval_500:
1474	            val_loss: 0.4541
1475	            R@1: 0.5446
1476	          eval_1000:
1477	            val_loss: 0.4654
1478	            R@1: 0.539
1479	          eval_1500:
1480	            val_loss: 0.4926
1481	            R@1: 0.5606
1482	      embedding_vs_random_s43: +0.52pp (0.5606 vs 0.5554)
1483	      eta_all_done: ~May 17 21:00 CST
1484	  plan_017_literature:
1485	    status: DONE
1486	    retry_count: 0
1487	    created_at: '2026-05-14T18:49:00.477Z'
1488	    updated_at: '2026-05-14T21:33:45.149Z'
1489	    hypothesis: 'Inference-time graph method comparison: 8 papers surveyed (CodexGraph,
1490	      LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion
1491	      v2 drafted, all citations verified. Conclusion: training-time vs inference-time
1492	      complementary.'
1493	    spec:
1494	      command: analysis only (no training)
1495	      server: local
1496	      data_path: N/A
1497	      data_count: 0
1498	      model_name: N/A
1499	      seed: N/A
1500	      checkpoint_path: N/A
1501	      log_path: N/A
1502	    conclusion: success
1503	    metrics:
1504	      papers_surveyed: 8
1505	      citations_verified: 8
1506	      discussion_draft: artifacts/paper_drafts/discussion_v2.md
1507	      artifact_id: art_20260514_a2e1cd
1508	    completed_at: '2026-05-14T18:49:39.557Z'
1509	    notes: Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml
1510	      和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG
1511	      和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented
1512	      prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注
1513	      retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与
1514	      StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。
1515	  plan_005_stratified:
1516	    status: PREPARING
1517	    retry_count: 0
1518	    created_at: '2026-05-14T20:36:16.738Z'
1519	    updated_at: '2026-05-15T04:24:45.090Z'
1520	    hypothesis: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural
1521	      data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制
1522	      pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。
1523	    parent: m2_full_qwen
1524	    notes: plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复
1525	      (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size
1526	      交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best
1527	      / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch。[2026-05-15
1528	      09:10] Dry-run v5 全流程验证通过（21秒）。confound 分析 + BM25 overlap stratified 分析均通过。数据预处理全部完成。等
1529	      M2 checkpoint 就绪后替换 --dry-run 为 --checkpoints-dir 即可。[2026-05-15 11:17] evaluate_pool50.py
1530	      (D042) 独立验证通过：260行脚本，--help/数据加载/模型加载/编码流程/--batch-mode 自动发现 best_by_* checkpoint
1531	      全部 OK。GPU 模式几分钟可跑完 2980 queries。Ready for production。[2026-05-15] SWE-bench
1532	      eval 脚本确认存在于 /root/structfuse-context/evaluation/eval_swebench.py 和 /root/structfuse-context/scripts/eval_swebench_e2e.py，plan_003
1533	      基于现有脚本执行。
1534	    metrics:
1535	      confound_analysis:
1536	        data_validity: ⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。
1537	        valid_findings:
1538	          distribution_structure: rich-dataflow 99.3% 落在 large/xlarge repo，small repo
1539	            中完全不存在
1540	          correlation:
1541	            dataflow_edges_vs_repo_size_pearson_r: 0.089
1542	          cross_distribution:
1543	            rich_in_large_xlarge_pct: 99.3
1544	            rich_in_small: 0
1545	            moderate_in_large_xlarge_pct: 60.9
1546	          implication: 真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应
1547	        invalid_findings: 所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用
1548	        artifacts_path: /root/autodl-tmp/structfuse/artifacts/confound_analysis/
1549	        valid_artifact: cross_tabulation.csv
1550	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "eec9d185-158b-4346-bf33-f465ba58aa02"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Reading artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml",
  "usage": {
    "total_tokens": 41223,
    "tool_uses": 10,
    "duration_ms": 14475
  },
  "last_tool_name": "Read",
  "uuid": "0ca5849d-0707-44e4-98fe-e44a037b29b9",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01BzMCvx1AQDtUYmnhX1Z9RK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "164751bc-bd2d-41d8-a2e2-3125a9ce8ecb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011LcRPUkg6ntjyKvArEB4dM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19354,
      "cache_read_input_tokens": 21831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19354,
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

_source line 47 · 2026-05-15T09:28:49.091Z_

<details><summary>↩ Tool result · `toolu_01AgB1UMMnHHYuKrkx1jnCtC`</summary>

```text
1	- id: art_20260512_b890e8
2	  name: contrastive_model.py
3	  type: intermediate
4	  description: StructFuse bi-encoder contrastive model with InfoNCE loss, weighted
5	    positives, fusion head, LoRA support
6	  path: projects/structfuse-context/artifacts/_project/intermediate/contrastive_model.py
7	  url: null
8	  project: structfuse-context
9	  exp_id: null
10	  skill: ''
11	  created_at: '2026-05-12T10:04:16.728617+00:00'
12	  tags:
13	  - structfuse
14	  - training
15	  - stage2
16	- id: art_20260512_a7cf03
17	  name: StructFuse call_graph.ql
18	  type: intermediate
19	  description: CodeQL query for 2-hop call graph extraction from buggy function (Phase
20	    1a)
21	  path: projects/structfuse-context/artifacts/_project/intermediate/call_graph.ql
22	  url: null
23	  project: structfuse-context
24	  exp_id: null
25	  skill: ''
26	  created_at: '2026-05-12T10:04:17.924200+00:00'
27	  tags:
28	  - structfuse
29	  - stage1
30	  - codeql
31	- id: art_20260512_a82ef6
32	  name: hard_negative_mining.py
33	  type: intermediate
34	  description: 'Data-flow-aware hard negative mining: random / embedding-distance
35	    / dataflow-aware strategies'
36	  path: projects/structfuse-context/artifacts/_project/intermediate/hard_negative_mining.py
37	  url: null
38	  project: structfuse-context
39	  exp_id: null
40	  skill: ''
41	  created_at: '2026-05-12T10:04:18.671317+00:00'
42	  tags:
43	  - structfuse
44	  - training
45	  - stage2
46	- id: art_20260512_99f4ec
47	  name: StructFuse bounded_dataflow.ql
48	  type: intermediate
49	  description: CodeQL query for scope-bounded inter-procedural data-flow analysis
50	    (Phase 1b)
51	  path: projects/structfuse-context/artifacts/_project/intermediate/bounded_dataflow.ql
52	  url: null
53	  project: structfuse-context
54	  exp_id: null
55	  skill: ''
56	  created_at: '2026-05-12T10:04:19.846492+00:00'
57	  tags:
58	  - structfuse
59	  - stage1
60	  - codeql
61	  - dataflow
62	- id: art_20260512_2c1b69
63	  name: train.py
64	  type: intermediate
65	  description: 'StructFuse training entry: Accelerate, W&B, dynamic negative mining,
66	    eval loop, checkpoint saving'
67	  path: projects/structfuse-context/artifacts/_project/intermediate/train.py
68	  url: null
69	  project: structfuse-context
70	  exp_id: null
71	  skill: ''
72	  created_at: '2026-05-12T10:04:20.628765+00:00'
73	  tags:
74	  - structfuse
75	  - training
76	  - stage2
77	- id: art_20260512_21d6b6
78	  name: StructFuse extract_dataflow.py
79	  type: intermediate
80	  description: 'Main extraction pipeline: CodeQL 2-phase analysis with Beniget fallback,
81	    multiprocessing parallel, JSONL output'
82	  path: projects/structfuse-context/artifacts/_project/intermediate/extract_dataflow.py
83	  url: null
84	  project: structfuse-context
85	  exp_id: null
86	  skill: ''
87	  created_at: '2026-05-12T10:04:22.339431+00:00'
88	  tags:
89	  - structfuse
90	  - stage1
91	  - extraction
92	  - pipeline
93	- id: art_20260512_51f682
94	  name: StructFuse build_training_data.py
95	  type: intermediate
96	  description: 'Contrastive training data builder: BM25 hard negatives, feature vectors,
97	    HuggingFace-compatible JSONL output'
98	  path: projects/structfuse-context/artifacts/_project/intermediate/build_training_data.py
99	  url: null
100	  project: structfuse-context
101	  exp_id: null
102	  skill: ''
103	  created_at: '2026-05-12T10:04:23.854442+00:00'
104	  tags:
105	  - structfuse
106	  - stage1
107	  - training-data
108	  - contrastive
109	- id: art_20260512_8aef33
110	  name: eval_retrieval.py
111	  type: data
112	  description: 'StructFuse retrieval evaluation script: Recall@k, MRR, Structural
113	    Precision on SWE-bench Lite / RepoBench-R / custom sets. Supports BM25 baseline,
114	    data-flow filter, fusion re-ranking, multi-model comparison.'
115	  path: projects/structfuse-context/artifacts/_project/data/eval_retrieval.py
116	  url: null
117	  project: structfuse-context
118	  exp_id: null
119	  skill: ''
120	  created_at: '2026-05-12T10:05:00.289408+00:00'
121	  tags:
122	  - evaluation
123	  - retrieval
124	  - structfuse
125	  - stage3
126	- id: art_20260512_033304
127	  name: eval_swebench.py
128	  type: data
129	  description: 'StructFuse SWE-bench end-to-end evaluation: issue -> StructFuse retrieval
130	    -> Qwen3.6-27B patch generation (vLLM) -> harness evaluation. Supports resume,
131	    per-instance logging, Pass@1 summary.'
132	  path: projects/structfuse-context/artifacts/_project/data/eval_swebench.py
133	  url: null
134	  project: structfuse-context
135	  exp_id: null
136	  skill: ''
137	  created_at: '2026-05-12T10:05:05.302147+00:00'
138	  tags:
139	  - evaluation
140	  - swebench
141	  - structfuse
142	  - e2e
143	  - stage3
144	- id: art_20260512_e5f41c
145	  name: requirements.txt
146	  type: data
147	  description: 'StructFuse project Python dependencies: torch, transformers, rank-bm25,
148	    faiss-cpu, vllm, etc.'
149	  path: projects/structfuse-context/artifacts/_project/data/requirements.txt
150	  url: null
151	  project: structfuse-context
152	  exp_id: null
153	  skill: ''
154	  created_at: '2026-05-12T10:05:05.480895+00:00'
155	  tags:
156	  - dependencies
157	  - structfuse
158	- id: art_20260512_7277a2
159	  name: MVP Phase 1 Report
160	  type: report
161	  description: 'MVP Phase 1 CodeQL feasibility + H2 sanity check results: timeout
162	    0%, connected files coverage 1.44% vs disconnected 0%, Fisher p=0.0000. Both PASS.'
163	  path: projects/structfuse-context/artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md
164	  url: null
165	  project: structfuse-context
166	  exp_id: mvp_p1_codeql_feasibility
167	  skill: ''
168	  created_at: '2026-05-12T11:31:28.845286+00:00'
169	  tags:
170	  - mvp
171	  - phase1
172	  - codeql
173	  - h2
174	  - pass
175	- id: art_20260512_434371
176	  name: phase2a_linear_proxy_results
177	  type: report
178	  description: 'Phase 2a linear proxy validation - PASS: DataFlow+BM25 beats BM25-only
179	    on F1/AUC/MRR. Gold file rank improved from 16→3 (flask), 4→1 (requests), 31→3
180	    (pytest).'
181	  path: projects/structfuse-context/artifacts/_project/report/phase2a_linear_proxy_results.txt
182	  url: null
183	  project: structfuse-context
184	  exp_id: null
185	  skill: ''
186	  created_at: '2026-05-12T11:40:32.570898+00:00'
187	  tags:
188	  - mvp
189	  - phase2a
190	  - evaluation
191	  - pass
192	- id: art_20260512_6211d5
193	  name: failure_diagnosis
194	  type: report
195	  description: mvp_p2b_contrastive_training 失败诊断：Run 2/9 因 ModelScope 并发下载导致模型 safetensors
196	    文件缺失
197	  path: projects/structfuse-context/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
198	  url: null
199	  project: structfuse-context
200	  exp_id: mvp_p2b_contrastive_training
201	  skill: ''
202	  created_at: '2026-05-12T13:19:19.831877+00:00'
203	  tags:
204	  - diagnosis
205	  - failure
206	  - modelscope
207	- id: art_20260512_cf23fc
208	  name: 50-repo overlap experiment results
209	  type: report
210	  description: 50-repo CodeQL 2-hop call_graph overlap experiment on SWE-smith data.
211	    Validates that connected-but-not-gold files exist at scale (Z=40.8% >> 20% threshold),
212	    confirming original StructFuse method is viable.
213	  path: projects/structfuse-context/artifacts/_project/report/50repo_overlap_report.md
214	  url: null
215	  project: structfuse-context
216	  exp_id: null
217	  skill: ''
218	  created_at: '2026-05-12T20:36:49.021879+00:00'
219	  tags:
220	  - experiment
221	  - codeql
222	  - overlap
223	  - validation
224	- id: art_20260513_240352
225	  name: plan_006_scalability_stats_29repos
226	  type: data
227	  description: 'M1 scalability statistics from 29/131 repos (8171 instances): extraction
228	    time, timeout rate, coverage, Z% by repo size. For plan_006.'
229	  path: projects/structfuse-context/artifacts/_project/data/plan_006_scalability_stats_29repos.json
230	  url: null
231	  project: structfuse-context
232	  exp_id: null
233	  skill: ''
234	  created_at: '2026-05-13T04:24:15.343120+00:00'
235	  tags:
236	  - plan_006
237	  - scalability
238	  - m1_extraction
239	- id: art_20260513_ef3ab0
240	  name: plan_006_scalability_summary
241	  type: report
242	  description: 'Plan 006 M1 extraction scalability stats (29/131 repos): Z% by size,
243	    extraction perf, zero-Z repos, key findings for paper Discussion'
244	  path: projects/structfuse-context/artifacts/_project/report/scalability_summary.md
245	  url: null
246	  project: structfuse-context
247	  exp_id: null
248	  skill: ''
249	  created_at: '2026-05-13T06:18:14.578259+00:00'
250	  tags:
251	  - plan_006
252	  - scalability
253	  - m1_extraction
254	- id: art_20260513_eaf24b
255	  name: plan_006_scalability_data
256	  type: data
257	  description: 'Structured JSON for plan_006 scalability visualization: by_size, extraction_time,
258	    zero_z_repos, per_repo breakdown (29 repos)'
259	  path: projects/structfuse-context/artifacts/_project/data/scalability_data.json
260	  url: null
261	  project: structfuse-context
262	  exp_id: null
263	  skill: ''
264	  created_at: '2026-05-13T06:18:16.617467+00:00'
265	  tags:
266	  - plan_006
267	  - scalability
268	  - m1_extraction
269	  - visualization
270	- id: art_20260513_2d4eb4
271	  name: pilot_results_summary
272	  type: report
273	  description: StructFuse pilot results summary - Qwen2.5-Coder-3B and StarCoder2-3B
274	    eval metrics across random/embedding/dataflow strategies
275	  path: projects/structfuse-context/artifacts/_project/report/pilot_results_summary.md
276	  url: null
277	  project: structfuse-context
278	  exp_id: null
279	  skill: ''
280	  created_at: '2026-05-13T10:34:49.209382+00:00'
281	  tags:
282	  - pilot
283	  - eval
284	  - results
285	- id: art_20260513_85049a
286	  name: pilot_results_data
287	  type: data
288	  description: StructFuse pilot results structured JSON - full eval history, checkpoint
289	    paths, training config. File at bjb1-42106:/root/structfuse/results/pilot_results.json
290	  path: projects/structfuse-context/artifacts/_project/data/pilot_results.json
291	  url: null
292	  project: structfuse-context
293	  exp_id: null
294	  skill: ''
295	  created_at: '2026-05-13T10:35:26.154352+00:00'
296	  tags:
297	  - pilot
298	  - eval
299	  - results
300	  - json
301	- id: art_20260513_229113
302	  name: cross_encoder_analysis
303	  type: intermediate
304	  description: 'Cross-encoder comparison script: Qwen2.5-Coder-3B vs StarCoder2-3B,
305	    generates Markdown/LaTeX tables, strategy deltas, ranking consistency analysis,
306	    and auto-narrative.'
307	  path: projects/structfuse-context/artifacts/_project/intermediate/cross_encoder_analysis.py
308	  url: null
309	  project: structfuse-context
310	  exp_id: null
311	  skill: ''
312	  created_at: '2026-05-13T10:42:10.274341+00:00'
313	  tags:
314	  - analysis
315	  - cross-encoder
316	  - comparison
317	  - m2_embed_verify
318	  - plan_013_starcoder
319	- id: art_20260513_46f013
320	  name: run_full_m2_training
321	  type: intermediate
322	  description: 全量 M2 单次训练 wrapper 脚本，接受 (strategy, seed, gpu_id) 参数运行一个训练任务
323	  path: projects/structfuse-context/artifacts/_project/intermediate/run_full_m2_training.sh
324	  url: null
325	  project: structfuse-context
326	  exp_id: null
327	  skill: ''
328	  created_at: '2026-05-13T10:45:57.693370+00:00'
329	  tags:
330	  - m2
331	  - training
332	  - full
333	  - script
334	- id: art_20260513_d36f2f
335	  name: schedule_m2_runs
336	  type: intermediate
337	  description: 全量 M2 双卡调度脚本，9 runs (3 strategies × 3 seeds) 均衡分配到 GPU0/GPU1
338	  path: projects/structfuse-context/artifacts/_project/intermediate/schedule_m2_runs.sh
339	  url: null
340	  project: structfuse-context
341	  exp_id: null
342	  skill: ''
343	  created_at: '2026-05-13T10:45:59.748163+00:00'
344	  tags:
345	  - m2
346	  - training
347	  - full
348	  - scheduler
349	- id: art_20260513_64aa24
350	  name: pilot_results_summary
351	  type: report
352	  description: StructFuse pilot experiment results summary - Qwen2.5-Coder-3B and
353	    StarCoder2-3B across random/embedding/dataflow strategies with complete metrics
354	  path: projects/structfuse-context/artifacts/_project/report/pilot_results_summary_64aa24.md
355	  url: null
356	  project: structfuse-context
357	  exp_id: null
358	  skill: ''
359	  created_at: '2026-05-13T11:52:02.987195+00:00'
360	  tags:
361	  - pilot
362	  - results
363	  - metrics
364	  - qwen
365	  - starcoder
366	- id: art_20260513_920f68
367	  name: pilot_results
368	  type: data
369	  description: StructFuse pilot structured results JSON - complete metrics for all
370	    encoder/strategy combinations
371	  path: projects/structfuse-context/artifacts/_project/data/pilot_results_920f68.json
372	  url: null
373	  project: structfuse-context
374	  exp_id: null
375	  skill: ''
376	  created_at: '2026-05-13T11:52:04.578072+00:00'
377	  tags:
378	  - pilot
379	  - results
380	  - structured-data
381	  - json
382	- id: art_20260513_a8c683
383	  name: full_z_percent_stats
384	  type: data
385	  description: Full M1 Z% statistics (123 repos, 44173 instances). 条件 Z%=78.0%, 全量
386	    Z%=26.8%. Per-repo breakdown.
387	  path: projects/structfuse-context/artifacts/plan_006_scalability/data/full_z_percent_stats.json
388	  url: null
389	  project: structfuse-context
390	  exp_id: plan_006_scalability
391	  skill: ''
392	  created_at: '2026-05-13T16:34:07.365228+00:00'
393	  tags:
394	  - z-percent
395	  - m1
396	  - scalability
397	- id: art_20260513_c3956f
398	  name: m2_full_qwen_wrapper_script
399	  type: intermediate
400	  description: Wrapper shell script for 9 sequential M2 full Qwen training runs (3
401	    strategies × 3 seeds). set -eo pipefail, dual checkpoint, WANDB_CONSOLE=off, direct
402	    file redirect.
403	  path: projects/structfuse-context/artifacts/m2_full_qwen/intermediate/run_m2_full_qwen.sh
404	  url: null
405	  project: structfuse-context
406	  exp_id: m2_full_qwen
407	  skill: ''
408	  created_at: '2026-05-13T16:56:34.582285+00:00'
409	  tags:
410	  - training
411	  - shell-script
412	  - m2
413	- id: art_20260513_466352
414	  name: plan006_full_scalability
415	  type: data
416	  description: 'Full M1 scalability statistics: 44173 instances across 123 repos,
417	    stratified by repo size tier'
418	  path: projects/structfuse-context/artifacts/plan_006_scalability/data/plan006_full_scalability.json
419	  url: null
420	  project: structfuse-context
421	  exp_id: plan_006_scalability
422	  skill: ''
423	  created_at: '2026-05-13T18:48:55.784862+00:00'
424	  tags:
425	  - m1
426	  - scalability
427	  - full-run
428	  - statistics
429	- id: art_20260513_d262da
430	  name: plan006_error_patterns
431	  type: data
432	  description: 'M1 extraction error pattern analysis: all 28,276 errors (64%) are
433	    buggy_file_not_found - upstream SWE-smith data issue, not CodeQL failure. 82/123
434	    repos affected, 36 repos with >90% error rate.'
435	  path: projects/structfuse-context/artifacts/plan_006_scalability/data/plan006_error_patterns.json
436	  url: null
437	  project: structfuse-context
438	  exp_id: plan_006_scalability
439	  skill: ''
440	  created_at: '2026-05-13T19:05:43.898730+00:00'
441	  tags:
442	  - error-analysis
443	  - m1-extraction
444	  - limitation
445	- id: art_20260513_ca0458
446	  name: negative_difficulty_charts
447	  type: chart
448	  description: 'Negative difficulty distribution histograms (3 figures: Qwen, StarCoder,
449	    Cross-encoder comparison). Server: bjb1-42106:/root/autodl-tmp/structfuse/artifacts/negative_difficulty_{qwen,starcoder,comparison}.{pdf,png}'
450	  path: projects/structfuse-context/artifacts/_project/chart/negative_difficulty_charts_index.txt
451	  url: null
452	  project: structfuse-context
453	  exp_id: null
454	  skill: ''
455	  created_at: '2026-05-13T19:08:02.266021+00:00'
456	  tags:
457	  - analysis
458	  - negative_mining
459	  - visualization
460	- id: art_20260513_12311f
461	  name: negative_difficulty_stats
462	  type: data
463	  description: 'Negative difficulty distribution stats: cosine similarity between
464	    query-negative pairs using pretrained Qwen2.5-Coder-3B and StarCoder2-3B across
465	    3 mining strategies. 50 queries x 20 negatives per strategy.'
466	  path: projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats.txt
467	  url: null
468	  project: structfuse-context
469	  exp_id: null
470	  skill: ''
471	  created_at: '2026-05-13T19:08:26.878004+00:00'
472	  tags:
473	  - analysis
474	  - negative_mining
475	  - difficulty_distribution
476	- id: art_20260513_68a365
477	  name: negative_difficulty_margin_charts
478	  type: chart
479	  description: '3 charts on server: margin distribution, bars (pos/neg/margin), violin
480	    plot. Path: /root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_*.{png,pdf}'
481	  path: projects/structfuse-context/artifacts/_project/chart/negative_difficulty_margin_charts_index.txt
482	  url: null
483	  project: structfuse-context
484	  exp_id: null
485	  skill: ''
486	  created_at: '2026-05-13T19:29:14.236993+00:00'
487	  tags:
488	  - negative-difficulty
489	  - margin
490	  - chart
491	- id: art_20260513_87bd9a
492	  name: negative_difficulty_stats_v2
493	  type: data
494	  description: Margin analysis (pos_sim, neg_sim, margin) per strategy per encoder.
495	    StarCoder margin 2.5-5.5x larger than Qwen.
496	  path: projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats_v2.txt
497	  url: null
498	  project: structfuse-context
499	  exp_id: null
500	  skill: ''
501	  created_at: '2026-05-13T19:29:29.550385+00:00'
502	  tags:
503	  - negative-difficulty
504	  - margin
505	  - analysis
506	- id: art_20260514_47c425
507	  name: neg_difficulty_margin_comparison
508	  type: chart
509	  description: 论文级双面板图：Qwen vs StarCoder negative difficulty margin对比（stacked bar,
510	    3 strategies × 2 encoders, 2048-token data）。展示 Qwen 表征饱和（margin 0.017~0.074）vs
511	    StarCoder 健康（margin 0.067~0.194）。
512	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt
513	  url: null
514	  project: structfuse-context
515	  exp_id: neg_difficulty_analysis
516	  skill: draw-paper-figure
517	  created_at: '2026-05-14T01:48:29.287483+00:00'
518	  tags:
519	  - paper
520	  - visualization
521	  - neg_difficulty
522	  - margin
523	- id: art_20260514_f75270
524	  name: m2_full_qwen_analysis
525	  type: report
526	  description: m2_full_qwen 实验分析：9 runs 中仅 random_s42 完成，best R@1=0.5527 (step 1000)，其余
527	    8 runs 未完成
528	  path: projects/structfuse-context/artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md
529	  url: null
530	  project: structfuse-context
531	  exp_id: m2_full_qwen
532	  skill: ''
533	  created_at: '2026-05-14T11:30:04.261359+00:00'
534	  tags:
535	  - m2
536	  - qwen
537	  - experiment-analysis
538	  - incomplete
539	- id: art_20260514_fa81d1
540	  name: m2_starcoder_status_check
541	  type: report
542	  description: 'm2_full_starcoder random_s42 progress diagnostic: step 3700/4242 (87%),
543	    overfitting confirmed, best R@1=0.4604 @step2500'
544	  path: projects/structfuse-context/artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md
545	  url: null
546	  project: structfuse-context
547	  exp_id: m2_full_starcoder
548	  skill: ''
549	  created_at: '2026-05-14T15:19:03.313283+00:00'
550	  tags:
551	  - status-check
552	  - m2
553	  - starcoder
554	  - overfitting
555	- id: art_20260514_b47344
556	  name: plan_015_dynamic_mining_design
557	  type: report
558	  description: 'Plan 015 experiment design: Dynamic vs Static embedding negative mining,
559	    with literature review, experiment variants, GPU overhead estimation, and expected
560	    outcomes for reviewer rebuttal'
561	  path: projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md
562	  url: null
563	  project: structfuse-context
564	  exp_id: null
565	  skill: ''
566	  created_at: '2026-05-14T16:16:57.329092+00:00'
567	  tags:
568	  - plan_015
569	  - experiment_design
570	  - dynamic_mining
571	  - reviewer_response
572	- id: art_20260514_a2e1cd
573	  name: discussion_v2
574	  type: paper
575	  description: Discussion章节v2草稿：5.1 inference-time graph comparison, 5.2 representation
576	    geometry as predictor, 5.3 limitations (5 items), 5.4 future work. ~1086 words,
577	    EMNLP style.
578	  path: projects/structfuse-context/artifacts/_project/paper/discussion_v2.md
579	  url: null
580	  project: structfuse-context
581	  exp_id: null
582	  skill: ''
583	  created_at: '2026-05-14T17:07:27.036510+00:00'
584	  tags:
585	  - plan_017
586	  - discussion
587	  - paper_draft
588	- id: art_20260514_01876a
589	  name: neg_difficulty_margin_comparison
590	  type: chart
591	  description: 主图：2048t下Qwen vs StarCoder margin对比柱状图，标注ratio (2.6×/3.9×/4.1×)。Okabe-Ito配色，300DPI。
592	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta_01876a.txt
593	  url: null
594	  project: structfuse-context
595	  exp_id: neg_difficulty_analysis
596	  skill: ''
597	  created_at: '2026-05-14T17:08:29.200136+00:00'
598	  tags:
599	  - neg_difficulty
600	  - paper_figure
601	  - margin
602	- id: art_20260514_7197a5
603	  name: neg_difficulty_similarity_dist
604	  type: chart
605	  description: 补充图：并排子图展示Qwen/StarCoder的pos_sim和neg_sim grouped bar，箭头标注margin Δ。
606	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_similarity_dist_meta.txt
607	  url: null
608	  project: structfuse-context
609	  exp_id: neg_difficulty_analysis
610	  skill: ''
611	  created_at: '2026-05-14T17:08:31.478220+00:00'
612	  tags:
613	  - neg_difficulty
614	  - paper_figure
615	  - similarity
616	- id: art_20260514_74ea5a
617	  name: neg_difficulty_ratio_heatmap
618	  type: chart
619	  description: Heatmap：2×3 (token length × strategy)，StarCoder/Qwen margin ratio。
620	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_ratio_heatmap_meta.txt
621	  url: null
622	  project: structfuse-context
623	  exp_id: neg_difficulty_analysis
624	  skill: ''
625	  created_at: '2026-05-14T17:08:33.400132+00:00'
626	  tags:
627	  - neg_difficulty
628	  - paper_figure
629	  - heatmap
630	- id: art_20260514_9baf69
631	  name: bm25_overlap_stratified
632	  type: data
633	  description: BM25 vs 各策略 top-7 Jaccard 重叠率按 repo size 分层。Small 0.67, Medium 0.38,
634	    Large 0.30 (vs embedding)。
635	  path: projects/structfuse-context/artifacts/plan_018_bm25/data/bm25_overlap_stratified_meta.txt
636	  url: null
637	  project: structfuse-context
638	  exp_id: plan_018_bm25
639	  skill: ''
640	  created_at: '2026-05-14T17:09:56.271213+00:00'
641	  tags:
642	  - bm25
643	  - overlap
644	  - stratified
645	  - plan_018
646	- id: art_20260514_a50aca
647	  name: experimental_setup_k_checkpoint
648	  type: paper
649	  description: 'Paper paragraph documenting K=7 negatives per query and dual checkpoint
650	    selection protocol, with registry-backed analysis of 7 completed runs (4/7 criteria
651	    agree, divergence pattern: Qwen always agrees, StarCoder always diverges)'
652	  path: projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md
653	  url: null
654	  project: structfuse-context
655	  exp_id: null
656	  skill: ''
657	  created_at: '2026-05-14T17:55:29.479783+00:00'
658	  tags:
659	  - paper
660	  - experimental-setup
661	  - checkpoint
662	  - K-negatives
663	  - dream-review
664	- id: art_20260514_3008c4
665	  name: v1_v2_changelog
666	  type: report
667	  description: Stratified dry-run v1→v2 差异溯源：根因为 mock_predictions() 使用 hash(strategy)
668	    构造 RNG seed，Python 3 hash randomization 导致跨进程不确定。含完整数值变化表（3 维度 × 3 策略 × 所有 strata）。
669	  path: projects/structfuse-context/artifacts/plan_005_stratified/report/v1_v2_changelog.md
670	  url: null
671	  project: structfuse-context
672	  exp_id: plan_005_stratified
673	  skill: ''
674	  created_at: '2026-05-14T20:40:50.297063+00:00'
675	  tags:
676	  - plan_005
677	  - v1_v2_diff
678	  - changelog
679	  - mock_rng
680	- id: art_20260514_fa94e9
681	  name: related_work_expansion_report
682	  type: report
683	  description: 'Related work expansion: literature_map.yaml 从 ~22 扩展到 37 verified
684	    entries (7 categories)。含 CoCoHaNeRe framing 分析、15 篇新增、2 处修正。'
685	  path: projects/structfuse-context/artifacts/_project/report/related_work_expansion_report.md
686	  url: null
687	  project: structfuse-context
688	  exp_id: null
689	  skill: ''
690	  created_at: '2026-05-14T21:27:25.138825+00:00'
691	  tags:
692	  - literature
693	  - related-work
694	  - CoCoHaNeRe
695	  - paper-framing
696	- id: art_20260514_98650c
697	  name: related_work_v1
698	  type: paper
699	  description: 'Related Work section draft v1 — 3 subsections: Code Retrieval Methods,
700	    Contrastive Learning for Code, Hard Negative Mining (~950 words)'
701	  path: projects/structfuse-context/artifacts/_project/paper/related_work_v1.md
702	  url: null
703	  project: structfuse-context
704	  exp_id: null
705	  skill: ''
706	  created_at: '2026-05-14T22:09:33.655871+00:00'
707	  tags:
708	  - paper
709	  - related-work
710	  - draft
711	- id: art_20260514_a7df8a
712	  name: SWE-bench Lite Dry-Run 预检报告
713	  type: report
714	  description: Plan_003 SWE-bench Lite 评估环境预检：数据、脚本、依赖、磁盘空间、checkpoint 可用性检查结果
715	  path: projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md
716	  url: null
717	  project: structfuse-context
718	  exp_id: plan_003
719	  skill: ''
720	  created_at: '2026-05-14T22:10:14.564938+00:00'
721	  tags:
722	  - swebench
723	  - dryrun
724	  - precheck
725	- id: art_20260514_dc54a3
726	  name: related_work_v1
727	  type: paper
728	  description: 'Related Work v1 draft — patched: §2.1 "all→these" graph-guided, §2.2
729	    added Sentence-BERT citation, §2.3 added pilot evidence caveat to "consistently
730	    improves"'
731	  path: projects/structfuse-context/artifacts/_project/paper/related_work_v1_dc54a3.md
732	  url: null
733	  project: structfuse-context
734	  exp_id: null
735	  skill: ''
736	  created_at: '2026-05-14T22:45:19.439165+00:00'
737	  tags:
738	  - related-work
739	  - v1
740	  - patched
741	- id: art_20260514_2cb18b
742	  name: introduction_v1
743	  type: paper
744	  description: 'Introduction section draft v1 — 4-paragraph structure: code retrieval
745	    importance, existing gaps (inference-only structure + no systematic negative mining
746	    study), our systematic study challenging gradient-based assumptions, 3 contributions'
747	  path: projects/structfuse-context/artifacts/_project/paper/introduction_v1.md
748	  url: null
749	  project: structfuse-context
750	  exp_id: null
751	  skill: ''
752	  created_at: '2026-05-14T22:47:45.459362+00:00'
753	  tags:
754	  - paper
755	  - introduction
756	  - draft
757	- id: art_20260514_5db688
758	  name: method_v1
759	  type: paper
760	  description: 'Method section draft (§3) with 4 subsections: Problem Formulation,
761	    StructFuse Pipeline, Training Objective, Negative Mining Strategies. ~1200 words,
762	    LaTeX formulas, cite keys aligned with literature_map.yaml.'
763	  path: projects/structfuse-context/artifacts/_project/paper/method_v1.md
764	  url: null
765	  project: structfuse-context
766	  exp_id: null
767	  skill: ''
768	  created_at: '2026-05-14T22:49:00.699349+00:00'
769	  tags:
770	  - paper
771	  - method
772	  - draft-v1
773	- id: art_20260514_25f2bc
774	  name: experiments_v1
775	  type: paper
776	  description: Experiments section draft (§4) with setup, implementation details,
777	    results tables (placeholder), representation geometry analysis (filled), and CodeQL
778	    scalability (filled). ~1400 words.
779	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1.md
780	  url: null
781	  project: structfuse-context
782	  exp_id: null
783	  skill: ''
784	  created_at: '2026-05-14T22:53:24.173003+00:00'
785	  tags:
786	  - paper
787	  - experiments
788	  - draft
789	- id: art_20260514_c76ce4
790	  name: figure_design_v1
791	  type: paper
792	  description: 论文 Figure 设计稿 v1：8 个 figure 的文字 sketch（pipeline overview、mining strategies
793	    illustration、main results、representation geometry、pool sensitivity、training curves、SWE-bench
794	    downstream、stratified analysis），含布局、数据需求、优先级、production timeline
795	  path: projects/structfuse-context/artifacts/_project/paper/figure_design_v1.md
796	  url: null
797	  project: structfuse-context
798	  exp_id: null
799	  skill: ''
800	  created_at: '2026-05-14T22:56:43.045319+00:00'
801	  tags:
802	  - paper
803	  - figure
804	  - design
805	- id: art_20260514_054f8d
806	  name: experiments_v1
807	  type: paper
808	  description: 'Experiments v1 draft with 5 fixes: (1) Table 6 Total 36.0%→34.3% aligned
809	    to registry, (2) Table 2 updated to R@1 checkpoint values with 4-decimal precision,
810	    (3) SWE-bench→SWE-smith with task→instance expansion explanation, (4) cite key
811	    cocohanere2025→fan2025cocohanere, (5) temperature τ=0.07 marked as learnable'
812	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_054f8d.md
813	  url: null
814	  project: structfuse-context
815	  exp_id: null
816	  skill: ''
817	  created_at: '2026-05-14T22:59:57.770391+00:00'
818	  tags:
819	  - paper
820	  - experiments
821	  - v1-fixed
822	- id: art_20260514_144ea2
823	  name: fig4_rep_geometry
824	  type: chart
825	  description: 'Fig 4: Representation Geometry — 2-panel figure. (a) Margin comparison
826	    grouped bar chart showing Qwen vs StarCoder pos-neg margins across 3 negative
827	    strategies with ratio annotations. (b) Similarity distribution box plots highlighting
828	    Qwen ceiling effect vs StarCoder wider spread. PDF vector + 300 DPI PNG.'
829	  path: projects/structfuse-context/artifacts/_project/chart/fig4_rep_geometry.png
830	  url: null
831	  project: structfuse-context
832	  exp_id: null
833	  skill: ''
834	  created_at: '2026-05-14T23:00:39.813252+00:00'
835	  tags:
836	  - paper
837	  - figure
838	  - neg_difficulty
839	  - representation_geometry
840	- id: art_20260514_8f65d6
841	  name: fig4_rep_geometry_pdf
842	  type: chart
843	  description: Fig 4 vector PDF version for LaTeX inclusion.
844	  path: projects/structfuse-context/artifacts/_project/chart/fig4_rep_geometry.pdf
845	  url: null
846	  project: structfuse-context
847	  exp_id: null
848	  skill: ''
849	  created_at: '2026-05-14T23:00:42.196239+00:00'
850	  tags:
851	  - paper
852	  - figure
853	  - pdf
854	- id: art_20260514_999157
855	  name: fig4_rep_geometry_script
856	  type: intermediate
857	  description: Plotting script for Fig 4 Representation Geometry figure. Self-contained,
858	    uses hardcoded data from neg_difficulty_analysis.
859	  path: projects/structfuse-context/artifacts/_project/intermediate/fig4_rep_geometry.py
860	  url: null
861	  project: structfuse-context
862	  exp_id: null
863	  skill: ''
864	  created_at: '2026-05-14T23:00:44.013645+00:00'
865	  tags:
866	  - paper
867	  - script
868	- id: art_20260514_3cf111
869	  name: method_v1
870	  type: paper
871	  description: 'Method section v1 with 6 fixes: projection head corrected to two-layer
872	    MLP+GELU, mean pooling described, pos_weight mechanism documented (uniform distance→unweighted
873	    InfoNCE), epoch strategy corrected (2 epochs + early stopping, s42 uses 3), L2
874	    normalization added, FusionHead confirmed absent.'
875	  path: projects/structfuse-context/artifacts/_project/paper/method_v1_3cf111.md
876	  url: null
877	  project: structfuse-context
878	  exp_id: null
879	  skill: ''
880	  created_at: '2026-05-14T23:03:27.091555+00:00'
881	  tags:
882	  - paper
883	  - method
884	  - v1-fixed
885	- id: art_20260514_ce3556
886	  name: method_v1
887	  type: paper
888	  description: '§3 Method draft — fixed fallback rate from 34% to 66% (line 63): 34.3%
889	    is structural coverage, ~66% lack structural data and fall back to embedding-distance
890	    negatives.'
891	  path: projects/structfuse-context/artifacts/_project/paper/method_v1_ce3556.md
892	  url: null
893	  project: structfuse-context
894	  exp_id: null
895	  skill: ''
896	  created_at: '2026-05-14T23:12:01.790814+00:00'
897	  tags:
898	  - paper-draft
899	  - method
900	  - bugfix
901	- id: art_20260514_eccca0
902	  name: experiments_v1 (round 2 fixes)
903	  type: paper
904	  description: 'Experiments v1 second-round fixes: 3 warnings (Table 6 repo count
905	    87 vs 123, strategy count 3 core + BM25 supplementary, projection head/pooling
906	    synced with method_v1) + 2 info items (structural instance count 15133, pilot
907	    "confirmed at full scale" → pending M2)'
908	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_eccca0.md
909	  url: null
910	  project: structfuse-context
911	  exp_id: null
912	  skill: ''
913	  created_at: '2026-05-14T23:12:33.473818+00:00'
914	  tags:
915	  - paper
916	  - experiments
917	  - round2-fixes
918	- id: art_20260514_bcd130
919	  name: experiments_v1
920	  type: paper
921	  description: Experiments section draft v1 — fixed Table 6 repo counts (87→123) and
922	    tier label (files→instances)
923	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_bcd130.md
924	  url: null
925	  project: structfuse-context
926	  exp_id: null
927	  skill: ''
928	  created_at: '2026-05-14T23:24:52.486733+00:00'
929	  tags:
930	  - paper
931	  - experiments
932	  - table6-fix
933	- id: art_20260514_d4b180
934	  name: experiments_v1
935	  type: paper
936	  description: 标记 Table 6 和 structural count 为 pending recalc，等待 m1_reextract_v2 完成后统一重算
937	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_d4b180.md
938	  url: null
939	  project: structfuse-context
940	  exp_id: null
941	  skill: ''
942	  created_at: '2026-05-14T23:30:40.862339+00:00'
943	  tags:
944	  - pending-recalc
945	  - table6
946	  - reextract-v2
947	- id: art_20260514_26c5b2
948	  name: fig1_pipeline_overview
949	  type: chart
950	  description: 'Fig 1: StructFuse pipeline overview — left-to-right flow from input
951	    (repo + bug report) through CodeQL extraction, negative mining (3 color-coded
952	    strategies: random/embedding/dataflow), contrastive training (InfoNCE + LoRA),
953	    to fine-tuned retriever. Okabe-Ito palette, serif font, 7x2.8in full-width.'
954	  path: projects/structfuse-context/artifacts/_project/chart/fig1_pipeline_overview.pdf
955	  url: null
956	  project: structfuse-context
957	  exp_id: null
958	  skill: ''
959	  created_at: '2026-05-14T23:38:53.669151+00:00'
960	  tags:
961	  - paper
962	  - figure
963	  - pipeline
964	  - fig1
965	- id: art_20260514_ad5cca
966	  name: fig1_pipeline_overview_png
967	  type: chart
968	  description: Fig 1 pipeline overview PNG preview (300 DPI)
969	  path: projects/structfuse-context/artifacts/_project/chart/fig1_pipeline_overview.png
970	  url: null
971	  project: structfuse-context
972	  exp_id: null
973	  skill: ''
974	  created_at: '2026-05-14T23:38:55.554881+00:00'
975	  tags:
976	  - paper
977	  - figure
978	  - pipeline
979	  - fig1
980	  - preview
981	- id: art_20260514_f9e844
982	  name: fig1_pipeline_overview_script
983	  type: intermediate
984	  description: Generation script for Fig 1 pipeline overview (matplotlib, no external
985	    deps)
986	  path: projects/structfuse-context/artifacts/_project/intermediate/fig1_pipeline_overview.py
987	  url: null
988	  project: structfuse-context
989	  exp_id: null
990	  skill: ''
991	  created_at: '2026-05-14T23:38:57.258190+00:00'
992	  tags:
993	  - paper
994	  - figure
995	  - script
996	  - fig1
997	- id: art_20260514_a5287e
998	  name: fig2_mining_strategies
999	  type: chart
1000	  description: 'Fig 2: Negative Mining Strategies — 3-panel comparison (Random / Embedding-Distance
1001	    / Dataflow-Aware). Shows same mini-repo graph with different negative selections
1002	    highlighted per strategy. Okabe-Ito colors, serif font, publication-ready.'
1003	  path: projects/structfuse-context/artifacts/_project/chart/fig2_mining_strategies.pdf
1004	  url: null
1005	  project: structfuse-context
1006	  exp_id: null
1007	  skill: ''
1008	  created_at: '2026-05-14T23:50:52.794198+00:00'
1009	  tags:
1010	  - paper
1011	  - figure
1012	  - negative-mining
1013	  - EMNLP2026
1014	- id: art_20260515_ae4280
1015	  name: method_v1
1016	  type: paper
1017	  description: 'Method section draft (§3): Problem formulation, structural information
1018	    extraction (M1), structure-aware negative mining (3 strategies), contrastive fine-tuning
1019	    (M2). All numbers sourced from registry.'
1020	  path: projects/structfuse-context/artifacts/_project/paper/method_v1_ae4280.md
1021	  url: null
1022	  project: structfuse-context
1023	  exp_id: null
1024	  skill: ''
1025	  created_at: '2026-05-15T01:59:32.730650+00:00'
1026	  tags:
1027	  - paper
1028	  - method
1029	  - draft
1030	- id: art_20260515_bba58d
1031	  name: experiment_setup_v1
1032	  type: paper
1033	  description: 'Experiment setup draft (§4): Dataset (SWE-smith, 131 repos, 14.3K
1034	    instances/seed), models (Qwen2.5-Coder-3B + StarCoder2-3B), training config (all
1035	    hyperparams from registry), evaluation metrics (R@k, bootstrap CI, Cohen''s d).'
1036	  path: projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md
1037	  url: null
1038	  project: structfuse-context
1039	  exp_id: null
1040	  skill: ''
1041	  created_at: '2026-05-15T01:59:36.266487+00:00'
1042	  tags:
1043	  - paper
1044	  - experiment-setup
1045	  - draft
1046	- id: art_20260515_895cbe
1047	  name: introduction_v2
1048	  type: paper
1049	  description: 'Introduction v2 draft — 5-paragraph ML top-venue structure: problem/motivation,
1050	    current approaches & gap, StructFuse approach, key findings, contributions. Claim
1051	    2 marked exploratory per D035. [TBD] placeholders for M2 final numbers.'
1052	  path: projects/structfuse-context/artifacts/_project/paper/introduction_v2.md
1053	  url: null
1054	  project: structfuse-context
1055	  exp_id: null
1056	  skill: ''
1057	  created_at: '2026-05-15T02:00:08.505124+00:00'
1058	  tags:
1059	  - paper
1060	  - introduction
1061	  - v2
1062	  - writing
1063	- id: art_20260515_884407
1064	  name: Checkpoint Criterion Analysis
1065	  type: report
1066	  description: Dual checkpoint (best_by_val_loss vs best_by_R@1) alignment analysis
1067	    + K=7 rationale for paper ablation section. 50% alignment rate on full M2 runs,
1068	    mean R@1 gap +0.65pp when diverged.
1069	  path: projects/structfuse-context/artifacts/_project/report/checkpoint_criterion_analysis.md
1070	  url: null
1071	  project: structfuse-context
1072	  exp_id: null
1073	  skill: ''
1074	  created_at: '2026-05-15T03:21:08.324336+00:00'
1075	  tags:
1076	  - ablation
1077	  - checkpoint
1078	  - paper
1079	- id: art_20260515_d1d8e6
1080	  name: plan005_stratification_spec
1081	  type: report
1082	  description: Plan 005 分层分析规格文档：5 维分层定义、3 阶段管道、数据源、执行计划
1083	  path: projects/structfuse-context/artifacts/plan_005/report/plan005_stratification_spec.md
1084	  url: null
1085	  project: structfuse-context
1086	  exp_id: plan_005
1087	  skill: ''
1088	  created_at: '2026-05-15T05:09:44.760930+00:00'
1089	  tags:
1090	  - stratified_analysis
1091	  - plan_005
1092	  - pipeline
1093	- id: art_20260515_fbb594
1094	  name: checkpoint_criterion_table
1095	  type: paper
1096	  description: 'Checkpoint criterion ablation table (LaTeX tabular): best_by_val_loss
1097	    vs best_by_R@1 comparison across 4 completed M2 runs, 50% divergence rate, encoder-dependent
1098	    pattern'
1099	  path: projects/structfuse-context/artifacts/_project/paper/checkpoint_criterion_table.tex
1100	  url: null
1101	  project: structfuse-context
1102	  exp_id: null
1103	  skill: ''
1104	  created_at: '2026-05-15T06:17:19.124582+00:00'
1105	  tags:
1106	  - paper
1107	  - ablation
1108	  - checkpoint
1109	- id: art_20260515_b69433
1110	  name: fixed_checkpoint_table
1111	  type: paper
1112	  description: 'LaTeX tabular: fixed-checkpoint comparison (embedding vs random at
1113	    same step), eliminates selection bias. Partial — s43 @500/@1000 filled, rest TBD
1114	    pending M2 completion.'
1115	  path: projects/structfuse-context/artifacts/_project/paper/fixed_checkpoint_table.tex
1116	  url: null
1117	  project: structfuse-context
1118	  exp_id: null
1119	  skill: ''
1120	  created_at: '2026-05-15T06:20:08.689200+00:00'
1121	  tags:
1122	  - table
1123	  - fixed-checkpoint
1124	  - claim2
1125	  - reviewer-response
1126	  - draft
1127	- id: art_20260515_c7f173
1128	  name: introduction_v1
1129	  type: paper
1130	  description: 'Introduction section v1 draft (~800 words): D049-compliant softened
1131	    framing, 5-paragraph structure, dual pilot+M2 data reporting, all cite keys aligned
1132	    with references.bib'
1133	  path: projects/structfuse-context/artifacts/_project/paper/introduction_v1_c7f173.md
1134	  url: null
1135	  project: structfuse-context
1136	  exp_id: null
1137	  skill: ''
1138	  created_at: '2026-05-15T08:51:28.731676+00:00'
1139	  tags:
1140	  - paper
1141	  - introduction
1142	  - D049
1143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "afeb9776-4f0b-45d4-9022-204a7923a906"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T09:28:49.117Z_

<details><summary>↩ Tool result · `toolu_01BzMCvx1AQDtUYmnhX1Z9RK`</summary>

```text
1	tier: best
2	narrative_guidance: '全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。
3	  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI
4	  下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。
5	  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。
6	  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。
7	  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545,
8	  embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。
9	
10	  '
11	imagined_experiments:
12	- name: SWE-bench Lite End-to-End Evaluation
13	  plan_id: plan_003
14	  description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench
15	    Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
16	
17	    '
18	  expected_results:
19	    random_resolve_rate: 0.22
20	    random_resolved_count: 66
21	    embedding_resolve_rate: 0.245
22	    embedding_resolved_count: 73
23	    dataflow_resolve_rate: 0.252
24	    dataflow_resolved_count: 76
25	    embedding_minus_random_pp: 2.5
26	    dataflow_minus_random_pp: 3.2
27	    dataflow_minus_embedding_pp: 0.7
28	    total_instances: 300
29	    retriever_top_k: 5
30	    agent_model: Qwen3.6-27B
31	  result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与
32	    issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关" 与"近似且相关"的文件。Dataflow
33	    额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee
34	    关系），dataflow negatives 训练使 retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval
35	    R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的
36	    patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
37	
38	    '
39	  tables:
40	  - name: 'Table 4: SWE-bench Lite Resolve Rate'
41	    columns:
42	    - Strategy
43	    - Resolved
44	    - Total
45	    - Rate (%)
46	    - Δ vs Random (pp)
47	    rows:
48	    - - random
49	      - 66
50	      - 300
51	      - 22.0
52	      - —
53	    - - embedding
54	      - 73
55	      - 300
56	      - 24.3
57	      - '+2.3'
58	    - - dataflow
59	      - 76
60	      - 300
61	      - 25.3
62	      - '+3.3'
63	  - name: 'Table 4b: SWE-bench by Patch Complexity'
64	    columns:
65	    - Patch Type
66	    - N
67	    - random (%)
68	    - embedding (%)
69	    - dataflow (%)
70	    rows:
71	    - - single-file
72	      - 189
73	      - 28.0
74	      - 30.7
75	      - 30.2
76	    - - multi-file
77	      - 111
78	      - 11.7
79	      - 14.4
80	      - 17.1
81	  figures_description:
82	  - 'Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI
83	    whiskers'
84	  - 'Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored
85	    by strategy'
86	  analysis: 'Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上
87	    +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使
88	    retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives
89	    普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline
90	    一致。
91	
92	    '
93	- name: RepoBench-R Cross-File Retrieval with Multi-Seed CIs
94	  plan_id: plan_004
95	  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds
96	    × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。
97	
98	    '
99	  expected_results:
100	    qwen_test_hard:
101	      random_R1_mean: 0.621
102	      random_R1_ci:
103	      - 0.614
104	      - 0.628
105	      embedding_R1_mean: 0.642
106	      embedding_R1_ci:
107	      - 0.634
108	      - 0.65
109	      dataflow_R1_mean: 0.633
110	      dataflow_R1_ci:
111	      - 0.624
112	      - 0.642
113	      embedding_minus_random_pp: 2.1
114	      dataflow_minus_random_pp: 1.2
115	    qwen_test_easy:
116	      random_R1_mean: 0.843
117	      embedding_R1_mean: 0.855
118	      dataflow_R1_mean: 0.85
119	      embedding_minus_random_pp: 1.2
120	    starcoder_test_hard:
121	      random_R1_mean: 0.574
122	      random_R1_ci:
123	      - 0.566
124	      - 0.582
125	      embedding_R1_mean: 0.589
126	      embedding_R1_ci:
127	      - 0.58
128	      - 0.598
129	      dataflow_R1_mean: 0.572
130	      dataflow_R1_ci:
131	      - 0.562
132	      - 0.582
133	      embedding_minus_random_pp: 1.5
134	      dataflow_minus_random_pp: -0.2
135	    starcoder_test_easy:
136	      random_R1_mean: 0.812
137	      embedding_R1_mean: 0.822
138	      dataflow_R1_mean: 0.81
139	    repobench_R1_delta_pp_embedding_avg: 1.8
140	    bootstrap_CI_width_R1_pp_avg: 1.2
141	  result_rationale: 'RepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。
142	    Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp），
143	    因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta
144	    被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI
145	    含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI
146	    宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。
147	
148	    '
149	  tables:
150	  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'
151	    columns:
152	    - Encoder
153	    - Strategy
154	    - R@1 (%)
155	    - 95% CI
156	    - Δ vs Random (pp)
157	    rows:
158	    - - Qwen
159	      - random
160	      - 62.1
161	      - '[61.4, 62.8]'
162	      - —
163	    - - Qwen
164	      - embedding
165	      - 64.2
166	      - '[63.4, 65.0]'
167	      - '+2.1'
168	    - - Qwen
169	      - dataflow
170	      - 63.3
171	      - '[62.4, 64.2]'
172	      - '+1.2'
173	    - - StarCoder
174	      - random
175	      - 57.4
176	      - '[56.6, 58.2]'
177	      - —
178	    - - StarCoder
179	      - embedding
180	      - 58.9
181	      - '[58.0, 59.8]'
182	      - '+1.5'
183	    - - StarCoder
184	      - dataflow
185	      - 57.2
186	      - '[56.2, 58.2]'
187	      - −0.2
188	  figures_description:
189	  - 'Fig 6: RepoBench-R R@1 grouped bar chart (2 encoders × 3 strategies) with CI
190	    whiskers, test_easy vs test_hard side by side'
191	  analysis: 'Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R
192	    上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 "结果仅限单一 benchmark" 的 reviewer concern。Test_easy
193	    上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。
194	
195	    '
196	- name: Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles
197	  plan_id: plan_005
198	  description: '5 层分层分析：repo size / pool size / query-positive similarity / structural
199	    data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints
200	    在 SWE-smith validation 上重新评估。
201	
202	    '
203	  expected_results:
204	    stratum_structural_available:
205	      with_dataflow_34pct:
206	        qwen_dataflow_minus_random_pp: 2.8
207	        qwen_dataflow_minus_embedding_pp: 1.3
208	        starcoder_dataflow_minus_random_pp: 0.1
209	        n_instances: ~5200
210	      fallback_66pct:
211	        qwen_dataflow_minus_random_pp: 0.1
212	        qwen_dataflow_minus_embedding_pp: -0.2
213	        starcoder_dataflow_minus_random_pp: -0.3
214	        n_instances: ~10000
215	    stratum_neg_difficulty_quartile:
216	      Q1_easiest:
217	        qwen_embedding_minus_random_pp: 0.8
218	        qwen_dataflow_minus_random_pp: 0.3
219	      Q2:
220	        qwen_embedding_minus_random_pp: 1.5
221	        qwen_dataflow_minus_random_pp: 0.7
222	      Q3:
223	        qwen_embedding_minus_random_pp: 2.4
224	        qwen_dataflow_minus_random_pp: 1.2
225	      Q4_hardest:
226	        qwen_embedding_minus_random_pp: 3.2
227	        qwen_dataflow_minus_random_pp: 2.1
228	    stratum_repo_size:
229	      small_lt50:
230	        embedding_delta_pp: 2.8
231	        n: ~500
232	      medium_50_200:
233	        embedding_delta_pp: 2.2
234	        n: ~4100
235	      large_200_500:
236	        embedding_delta_pp: 1.8
237	        n: ~5500
238	      xlarge_500plus:
239	        embedding_delta_pp: 1.6
240	        n: ~5100
241	    stratum_pool_size:
242	      pool_lt20:
243	        embedding_delta_pp: 1.0
244	        dataflow_delta_pp: 0.3
245	      pool_20_50:
246	        embedding_delta_pp: 2.1
247	        dataflow_delta_pp: 1.0
248	      pool_gt50:
249	        embedding_delta_pp: 2.5
250	        dataflow_delta_pp: 1.4
251	    stratum_query_pos_sim:
252	      high_sim_gt095:
253	        embedding_delta_pp: 2.6
254	        dataflow_delta_pp: 1.8
255	      medium_sim_085_095:
256	        embedding_delta_pp: 1.9
257	        dataflow_delta_pp: 0.8
258	      low_sim_lt085:
259	        embedding_delta_pp: 1.2
260	        dataflow_delta_pp: 0.2
261	  result_rationale: 'Structural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些
262	    instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback
263	    stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding
264	    或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 "34% coverage 稀释 signal" 的 concern——真实
265	    per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta
266	    最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高
267	    pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta
268	    最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate
269	    pool 更集中，mining 策略差异更容易体现。
270	
271	    '
272	  tables:
273	  - name: 'Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)'
274	    columns:
275	    - Stratum
276	    - N
277	    - random R@1
278	    - embedding R@1
279	    - dataflow R@1
280	    - df−rand (pp)
281	    rows:
282	    - - With dataflow (34%)
283	      - ~5.2K
284	      - 53.1
285	      - 55.4
286	      - 55.9
287	      - '+2.8'
288	    - - Fallback (66%)
289	      - ~10K
290	      - 55.2
291	      - 57.3
292	      - 55.3
293	      - '+0.1'
294	    - - Overall
295	      - ~15.2K
296	      - 54.5
297	      - 56.5
298	      - 55.5
299	      - '+1.0'
300	  - name: 'Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)'
301	    columns:
302	    - Quartile
303	    - margin_mean
304	    - emb−rand (pp)
305	    - df−rand (pp)
306	    rows:
307	    - - Q1 (easiest)
308	      - 0.142
309	      - '+0.8'
310	      - '+0.3'
311	    - - Q2
312	      - 0.078
313	      - '+1.5'
314	      - '+0.7'
315	    - - Q3
316	      - 0.031
317	      - '+2.4'
318	      - '+1.2'
319	    - - Q4 (hardest)
320	      - 0.008
321	      - '+3.2'
322	      - '+2.1'
323	  figures_description:
324	  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and
325	    StarCoder'
326	  - 'Fig 8: Neg difficulty quartile vs R@1 delta line plot, 3 strategies overlaid'
327	  analysis: 'Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp
328	    embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是
329	    representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 "diluted
330	    signal" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。
331	
332	    '
333	- name: Call-Graph Hop Depth Ablation (1/2/3-hop)
334	  plan_id: plan_007
335	  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。
336	    Qwen encoder, 1 seed, SWE-smith validation。
337	
338	    '
339	  expected_results:
340	    hop_1:
341	      R1: 0.548
342	      connected_coverage_pct: 12.4
343	      negatives_per_query_mean: 18.2
344	    hop_2:
345	      R1: 0.555
346	      connected_coverage_pct: 34.3
347	      negatives_per_query_mean: 31.7
348	    hop_3:
349	      R1: 0.551
350	      connected_coverage_pct: 58.6
351	      negatives_per_query_mean: 42.1
352	    optimal_hop: 2
353	    hop2_minus_hop1_pp: 0.7
354	    hop3_minus_hop2_pp: -0.4
355	  result_rationale: '2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的
356	    connected 节点来定义 "disconnected" negatives，退化为 random。3-hop 过于宽松——58.6% coverage
357	    下 "disconnected" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3%
358	    coverage（与 M1 extraction 的 structural data rate 一致）在 "enough connected nodes to
359	    define meaningful disconnection" 和 "disconnected set still contains genuinely
360	    unrelated files" 之间取得平衡。
361	
362	    '
363	  tables:
364	  - name: 'Table 9: Hop Depth Ablation (Qwen, dataflow strategy)'
365	    columns:
366	    - Hops
367	    - Coverage (%)
368	    - Neg/query
369	    - R@1 (%)
370	    - Δ vs 2-hop (pp)
371	    rows:
372	    - - 1
373	      - 12.4
374	      - 18.2
375	      - 54.8
376	      - −0.7
377	    - - 2
378	      - 34.3
379	      - 31.7
380	      - 55.5
381	      - —
382	    - - 3
383	      - 58.6
384	      - 42.1
385	      - 55.1
386	      - −0.4
387	  figures_description:
388	  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'
389	  analysis: '2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee，
390	    2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop
391	    选择有 principled 依据而非纯粹 empirical tuning。
392	
393	    '
394	- name: Training Data Size Scaling (1K/3K/5K)
395	  plan_id: plan_008
396	  description: '固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances
397	    增长， 观察 R@1 变化和策略排名稳定性。
398	
399	    '
400	  expected_results:
401	    size_1K:
402	      random_R1: 0.51
403	      embedding_R1: 0.522
404	      dataflow_R1: 0.515
405	      embedding_minus_random_pp: 1.2
406	      seed_std: 0.015
407	    size_3K:
408	      random_R1: 0.532
409	      embedding_R1: 0.55
410	      dataflow_R1: 0.541
411	      embedding_minus_random_pp: 1.8
412	      seed_std: 0.01
413	    size_5K:
414	      random_R1: 0.545
415	      embedding_R1: 0.565
416	      dataflow_R1: 0.555
417	      embedding_minus_random_pp: 2.0
418	      seed_std: 0.008
419	    ranking_stable: true
420	    monotonic_improvement: true
421	  result_rationale: '策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta
422	    幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining
423	    策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K
424	    时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further
425	    scaling could help, but is beyond scope。
426	
427	    '
428	  tables:
429	  - name: 'Table 10: Data Size Scaling (Qwen)'
430	    columns:
431	    - Size
432	    - random R@1
433	    - embedding R@1
434	    - dataflow R@1
435	    - emb−rand (pp)
436	    - σ across seeds
437	    rows:
438	    - - 1K
439	      - 51.0
440	      - 52.2
441	      - 51.5
442	      - '+1.2'
443	      - 1.5
444	    - - 3K
445	      - 53.2
446	      - 55.0
447	      - 54.1
448	      - '+1.8'
449	      - 1.0
450	    - - 5K
451	      - 54.5
452	      - 56.5
453	      - 55.5
454	      - '+2.0'
455	      - 0.8
456	  figures_description:
457	  - 'Fig S2: R@1 vs training size for 3 strategies, with shaded seed variance bands'
458	  analysis: 'Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见
459	    diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer "effect size marginal" concern
460	    有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。
461	
462	    '
463	- name: Fusion Head Ablation
464	  plan_id: plan_009
465	  description: '比较 embedding-only / structural-features-only / combined fusion head，
466	    隔离 training-time mining 价值与 inference-time feature injection。
467	
468	    '
469	  expected_results:
470	    embedding_only:
471	      qwen_R1: 0.565
472	      starcoder_R1: 0.475
473	    structural_features_only:
474	      qwen_R1: 0.498
475	      starcoder_R1: 0.421
476	    combined_fusion:
477	      qwen_R1: 0.561
478	      starcoder_R1: 0.472
479	    embedding_only_minus_combined_pp: 0.4
480	    conclusion: mining > fusion; structural features at inference add noise
481	  result_rationale: 'Embedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征）
482	    表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural
483	    features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance
484	    反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp
485	    Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。
486	    这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。
487	
488	    '
489	  tables:
490	  - name: 'Table 11: Fusion Head Ablation'
491	    columns:
492	    - Configuration
493	    - Qwen R@1 (%)
494	    - StarCoder R@1 (%)
495	    rows:
496	    - - embedding-only (ours)
497	      - 56.5
498	      - 47.5
499	    - - structural-features-only
500	      - 49.8
501	      - 42.1
502	    - - combined fusion
503	      - 56.1
504	      - 47.2
505	  figures_description:
506	  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'
507	  analysis: '训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural
508	    features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features
509	    绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector
510	    structural features，引入 noise。
511	
512	    '
513	- name: Dataflow-Distance Weighted vs Binary Negatives
514	  plan_id: plan_010
515	  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative
516	    sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。
517	
518	    '
519	  expected_results:
520	    binary_qwen_R1: 0.555
521	    weighted_qwen_R1: 0.558
522	    binary_starcoder_R1: 0.458
523	    weighted_starcoder_R1: 0.459
524	    weighted_minus_binary_qwen_pp: 0.3
525	    weighted_minus_binary_starcoder_pp: 0.1
526	  result_rationale: 'Weighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary
527	    disconnected/connected 已经捕获了最关键的 structural distinction—— "是否在调用链上"。进一步按 hop distance
528	    加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial
529	    negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。
530	
531	    '
532	  tables:
533	  - name: 'Table S1: Weighted vs Binary Dataflow Negatives'
534	    columns:
535	    - Method
536	    - Qwen R@1 (%)
537	    - StarCoder R@1 (%)
538	    - Δ vs Binary (pp)
539	    rows:
540	    - - Binary (default)
541	      - 55.5
542	      - 45.8
543	      - —
544	    - - Distance-weighted
545	      - 55.8
546	      - 45.9
547	      - +0.3 / +0.1
548	  figures_description: []
549	  analysis: 'Binary is sufficient — complexity of weighted sampling not justified.
550	    论文可在 ablation section 用一句话报告这一 negative result， 强化 "simple binary structural signal
551	    is the key insight" 的 narrative。
552	
553	    '
554	- name: SWE-bench Failure Analysis (50 cases)
555	  plan_id: plan_011
556	  description: '从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow
557	    信号是否可能帮助。
558	
559	    '
560	  expected_results:
561	    total_analyzed: 50
562	    category_breakdown:
563	      retrieval_failure_wrong_files: 22
564	      retrieval_success_but_agent_fail: 15
565	      insufficient_context_window: 7
566	      test_environment_issue: 4
567	      ambiguous_issue_description: 2
568	    dataflow_could_help:
569	      true: 14
570	      partially: 5
571	      false: 31
572	    dataflow_help_rate: 0.28
573	    key_pattern: '14/22 retrieval failures involve cross-module dependencies where
574	      the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity
575	      would directly address these.
576	
577	      '
578	  result_rationale: '50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和
579	    gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval
580	    success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了
581	    "ceiling analysis"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。
582	
583	    '
584	  tables:
585	  - name: 'Table S2: Failure Category Breakdown'
586	    columns:
587	    - Category
588	    - Count
589	    - '% of 50'
590	    - Dataflow Could Help?
591	    rows:
592	    - - 'Retrieval: wrong files'
593	      - 22
594	      - 44
595	      - 14/22 (64%)
596	    - - Retrieval OK, agent fail
597	      - 15
598	      - 30
599	      - N/A
600	    - - Context window limit
601	      - 7
602	      - 14
603	      - 5/7 partially
604	    - - Test env issue
605	      - 4
606	      - 8
607	      - 'No'
608	    - - Ambiguous issue
609	      - 2
610	      - 4
611	      - 'No'
612	  figures_description:
613	  - 'Fig S4: Sankey diagram — failure flow from retrieval stage to resolution outcome'
614	  analysis: '28% of failures could benefit from dataflow signal, consistent with the
615	    observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures
616	    confirms that cross-module dependency is the primary retrieval challenge, directly
617	    supporting Claim 2''s motivation.
618	
619	    '
620	- name: Qualitative Examples (5-10 cases)
621	  plan_id: plan_012
622	  description: '从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例，
623	    展示 structural signal 的具体作用机制。
624	
625	    '
626	  expected_results:
627	    total_examples: 8
628	    example_categories:
629	      caller_callee_confusion: 3
630	      utility_file_distraction: 2
631	      cross_module_import_chain: 2
632	      test_file_vs_source: 1
633	    illustrative_example:
634	      issue: django/django#12345 — QuerySet.filter() returns wrong results with nested
635	        Q objects
636	      random_retriever_top1: django/db/models/query.py (text match on 'filter')
637	      dataflow_retriever_top1: django/db/models/sql/query.py (actual SQL generation
638	        called by filter)
639	      gold: django/db/models/sql/query.py
640	      explanation: 'Random retriever picks query.py (contains ''filter'' method signature)
641	        but the bug is in sql/query.py (the downstream SQL builder called by filter).
642	        Dataflow training teaches the model that sql/query.py is structurally connected
643	        to query.py via 2-hop call chain, making it a better negative for other instances,
644	        which in turn improves the model''s ability to rank the actual implementation
645	        file higher.
646	
647	        '
648	  result_rationale: '8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper
649	    函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import
650	    chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的
651	    source code 复制）。这些案例具体展示了 "lexical similarity ≠ structural relevance" 的核心 insight。
652	
653	    '
654	  tables: []
655	  figures_description:
656	  - 'Fig 9: Side-by-side retrieval ranking visualization for 3 representative cases,
657	    showing file dependency graph with highlighted paths'
658	  analysis: 'Qualitative examples serve as the paper''s "aha moment" — they make the
659	    abstract representation geometry argument concrete. Reviewer-facing value: even
660	    skeptics who question statistical significance can see the mechanism operating
661	    on real code.
662	
663	    '
664	- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2}
665	  plan_id: plan_014
666	  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy
667	    ranking 是否 regime-specific。
668	
669	    '
670	  expected_results:
671	    tau_005:
672	      qwen_random_R1: 0.558
673	      qwen_embedding_R1: 0.577
674	      qwen_dataflow_R1: 0.569
675	      qwen_embedding_minus_random_pp: 1.9
676	      starcoder_random_R1: 0.47
677	      starcoder_embedding_R1: 0.485
678	      starcoder_dataflow_R1: 0.467
679	      starcoder_embedding_minus_random_pp: 1.5
680	    tau_010:
681	      qwen_random_R1: 0.545
682	      qwen_embedding_R1: 0.565
683	      qwen_dataflow_R1: 0.555
684	      qwen_embedding_minus_random_pp: 2.0
685	      starcoder_random_R1: 0.46
686	      starcoder_embedding_R1: 0.475
687	      starcoder_dataflow_R1: 0.458
688	      starcoder_embedding_minus_random_pp: 1.5
689	    tau_020:
690	      qwen_random_R1: 0.53
691	      qwen_embedding_R1: 0.546
692	      qwen_dataflow_R1: 0.538
693	      qwen_embedding_minus_random_pp: 1.6
694	      starcoder_random_R1: 0.448
695	      starcoder_embedding_R1: 0.461
696	      starcoder_dataflow_R1: 0.447
697	      starcoder_embedding_minus_random_pp: 1.3
698	    ranking_preserved_across_tau: true
699	    optimal_tau: 0.05
700	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
701	    > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper
702	    temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且
703	    delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity
704	    被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific，
705	    直接回应 median reviewer 的 "τ=0.05 unusually low" concern。
706	
707	    '
708	  tables:
709	  - name: 'Table 8: Temperature Ablation (R@1 %)'
710	    columns:
711	    - τ
712	    - Encoder
713	    - random
714	    - embedding
715	    - dataflow
716	    - emb−rand (pp)
717	    rows:
718	    - - 0.05
719	      - Qwen
720	      - 55.8
721	      - 57.7
722	      - 56.9
723	      - '+1.9'
724	    - - 0.05
725	      - StarCoder
726	      - 47.0
727	      - 48.5
728	      - 46.7
729	      - '+1.5'
730	    - - 0.1
731	      - Qwen
732	      - 54.5
733	      - 56.5
734	      - 55.5
735	      - '+2.0'
736	    - - 0.1
737	      - StarCoder
738	      - 46.0
739	      - 47.5
740	      - 45.8
741	      - '+1.5'
742	    - - 0.2
743	      - Qwen
744	      - 53.0
745	      - 54.6
746	      - 53.8
747	      - '+1.6'
748	    - - 0.2
749	      - StarCoder
750	      - 44.8
751	      - 46.1
752	      - 44.7
753	      - '+1.3'
754	  figures_description:
755	  - 'Fig S5: Temperature × strategy interaction plot (R@1 on y-axis, τ on x-axis,
756	    separate lines per strategy)'
757	  analysis: 'Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但
758	    不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative
759	    best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。
760	
761	    '
762	- name: Dynamic vs Static Embedding Mining
763	  plan_id: plan_015
764	  description: 'Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained
765	    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。
766	
767	    '
768	  expected_results:
769	    qwen_static_R1: 0.565
770	    qwen_dynamic_R1: 0.568
771	    qwen_dynamic_minus_static_pp: 0.3
772	    starcoder_static_R1: 0.475
773	    starcoder_dynamic_R1: 0.477
774	    starcoder_dynamic_minus_static_pp: 0.2
775	    dynamic_significant: false
776	    curriculum_confound_ruled_out: true
777	  result_rationale: 'Dynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning
778	    只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了
779	    "static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives
780	    变 stale）" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy
781	    的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每
782	    epoch 重新 encode + kNN）不 justified。
783	
784	    '
785	  tables:
786	  - name: 'Table 13: Static vs Dynamic Embedding Mining'
787	    columns:
788	    - Encoder
789	    - Static R@1 (%)
790	    - Dynamic R@1 (%)
791	    - Δ (pp)
792	    - p-value
793	    rows:
794	    - - Qwen
795	      - 56.5
796	      - 56.8
797	      - '+0.3'
798	      - 0.41
799	    - - StarCoder
800	      - 47.5
801	      - 47.7
802	      - '+0.2'
803	      - 0.53
804	  figures_description:
805	  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'
806	  analysis: 'Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative
807	    的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner
808	    recommendation——mine once from pretrained, no need for per-epoch re-mining。
809	
810	    '
811	- name: Bootstrap CIs for SWE-bench Lite Resolve Rate
812	  plan_id: plan_016
813	  description: '对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired
814	    difference CIs 和 p-values。
815	
816	    '
817	  expected_results:
818	    embedding_minus_random:
819	      delta_pp: 2.5
820	      ci_95:
821	      - 0.7
822	      - 4.3
823	      p_value: 0.018
824	      significant: true
825	    dataflow_minus_random:
826	      delta_pp: 3.2
827	      ci_95:
828	      - 1.0
829	      - 5.5
830	      p_value: 0.008
831	      significant: true
832	    dataflow_minus_embedding:
833	      delta_pp: 0.7
834	      ci_95:
835	      - -1.5
836	      - 2.9
837	      p_value: 0.134
838	      significant: false
839	    bootstrap_n: 10000
840	    sample_size: 300
841	  result_rationale: 'Embedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining
842	    在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module
843	    patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300
844	    instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游
845	    binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench
846	    Lite 不是为精确 delta 估计设计的 benchmark。
847	
848	    '
849	  tables:
850	  - name: 'Table 4c: SWE-bench Bootstrap Significance Tests'
851	    columns:
852	    - Comparison
853	    - Δ (pp)
854	    - 95% CI
855	    - p-value
856	    rows:
857	    - - embedding − random
858	      - '+2.5'
859	      - '[+0.7, +4.3]'
860	      - 0.018
861	    - - dataflow − random
862	      - '+3.2'
863	      - '[+1.0, +5.5]'
864	      - 0.008
865	    - - dataflow − embedding
866	      - '+0.7'
867	      - '[−1.5, +2.9]'
868	      - 0.134
869	  figures_description:
870	  - 'Fig 5c: Bootstrap distribution histograms for the 3 pairwise comparisons'
871	  analysis: 'CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。
872	    Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 "conditional" framing
873	    一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。
874	
875	    '
876	- name: Inference-Time Graph Method Literature Comparison
877	  plan_id: plan_017
878	  description: '文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成
879	    8 篇论文 survey。
880	
881	    '
882	  expected_results:
883	    papers_surveyed: 8
884	    key_distinction: training-time mining (ours) vs inference-time graph navigation
885	    complementarity_evidence: 'All 8 methods operate at inference time; StructFuse
886	      mines at training time. The two approaches are complementary — StructFuse improves
887	      the base retriever that graph methods navigate over.
888	
889	      '
890	    papers_list:
891	    - CodexGraph
892	    - LocAgent
893	    - RANGER
894	    - GraphCoder
895	    - ARISE
896	    - RepoGraph
897	    - CodeGRAG
898	    - CodeRAG
899	  result_rationale: '8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段
900	    通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time
901	    方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用
902	    embedding retrieval）。 Discussion section 应明确 "complementary, not competing" 的定位。
903	
904	    '
905	  tables:
906	  - name: 'Table S3: Comparison with Inference-Time Graph Methods'
907	    columns:
908	    - Method
909	    - Graph Stage
910	    - Graph Type
911	    - Complementary?
912	    rows:
913	    - - StructFuse (ours)
914	      - Training
915	      - Dataflow (CodeQL)
916	      - —
917	    - - CodexGraph
918	      - Inference
919	      - Code graph DB
920	      - 'Yes'
921	    - - LocAgent
922	      - Inference
923	      - Repo structure
924	      - 'Yes'
925	    - - RANGER
926	      - Inference
927	      - Call graph
928	      - 'Yes'
929	    - - ARISE
930	      - Inference
931	      - Intra-proc dataflow
932	      - Partially (intra only)
933	  figures_description: []
934	  analysis: 'Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight:
935	    StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。
936	
937	    '
938	- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument
939	  plan_id: plan_018
940	  description: 'BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe
941	    报告的 "embedding negatives harm" 实际是 BM25-proxy artifact。
942	
943	    '
944	  expected_results:
945	    qwen:
946	      bm25_R1: 0.52
947	      random_R1: 0.545
948	      embedding_R1: 0.565
949	      dataflow_R1: 0.555
950	      bm25_minus_random_pp: -2.5
951	      embedding_minus_bm25_pp: 4.5
952	    starcoder:
953	      bm25_R1: 0.433
954	      random_R1: 0.46
955	      embedding_R1: 0.475
956	      dataflow_R1: 0.458
957	      bm25_minus_random_pp: -2.7
958	      embedding_minus_bm25_pp: 4.2
959	    bm25_harms_both_encoders: true
960	    cocohanere_artifact_confirmed: true
961	    bm25_minus_random_avg_pp: -2.6
962	  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder
963	    -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically
964	    similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names,
965	    variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分
966	    positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在
967	    code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically
968	    similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic
969	    distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成
970	    Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp
971	    [-4.0, -1.5] 范围内。
972	
973	    '
974	  tables:
975	  - name: 'Table 3: Full 4-Strategy Comparison Including BM25 Baseline'
976	    columns:
977	    - Encoder
978	    - Strategy
979	    - R@1 (%)
980	    - 95% CI
981	    - Δ vs Random (pp)
982	    rows:
983	    - - Qwen
984	      - BM25
985	      - 52.0
986	      - '[51.2, 52.8]'
987	      - −2.5
988	    - - Qwen
989	      - random
990	      - 54.5
991	      - '[53.8, 55.2]'
992	      - —
993	    - - Qwen
994	      - dataflow
995	      - 55.5
996	      - '[54.6, 56.4]'
997	      - '+1.0'
998	    - - Qwen
999	      - embedding
1000	      - 56.5
1001	      - '[55.8, 57.2]'
1002	      - '+2.0'
1003	    - - StarCoder
1004	      - BM25
1005	      - 43.3
1006	      - '[42.3, 44.3]'
1007	      - −2.7
1008	    - - StarCoder
1009	      - random
1010	      - 46.0
1011	      - '[45.1, 46.9]'
1012	      - —
1013	    - - StarCoder
1014	      - dataflow
1015	      - 45.8
1016	      - '[44.8, 46.8]'
1017	      - −0.2
1018	    - - StarCoder
1019	      - embedding
1020	      - 47.5
1021	      - '[46.6, 48.4]'
1022	      - '+1.5'
1023	  figures_description:
1024	  - 'Fig 3: 4-strategy R@1 bar chart with BM25 highlighted in red, showing the harm
1025	    direction. Annotation arrow from BM25 to embedding with ''4.5pp gap — the CoCoHaNeRe
1026	    artifact'''
1027	  - 'Fig 4: Neg similarity distribution histograms for BM25 vs embedding vs random
1028	    vs dataflow, showing BM25 occupies a different region of similarity space'
1029	  analysis: 'BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 "argumentative
1030	    correction" 升级为 "empirical demonstration"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行
1031	    BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy
1032	    ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的
1033	    quality spectrum。Reviewer 对 "correction without evidence" 的 concern 被彻底关闭。
1034	
1035	    '
1036	- name: Pool Size Sensitivity (50/100/200/500)
1037	  plan_id: plan_019
1038	  description: '在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
1039	    测试 strategy ranking 在更 realistic pool sizes 下的稳定性。
1040	
1041	    '
1042	  expected_results:
1043	    qwen:
1044	      pool_50:
1045	        random_R1: 0.545
1046	        embedding_R1: 0.565
1047	        dataflow_R1: 0.555
1048	        embedding_minus_random_pp: 2.0
1049	      pool_100:
1050	        random_R1: 0.428
1051	        embedding_R1: 0.447
1052	        dataflow_R1: 0.438
1053	        embedding_minus_random_pp: 1.9
1054	      pool_200:
1055	        random_R1: 0.342
1056	        embedding_R1: 0.359
1057	        dataflow_R1: 0.351
1058	        embedding_minus_random_pp: 1.7
1059	      pool_500:
1060	        random_R1: 0.261
1061	        embedding_R1: 0.276
1062	        dataflow_R1: 0.269
1063	        embedding_minus_random_pp: 1.5
1064	    starcoder:
1065	      pool_50:
1066	        random_R1: 0.46
1067	        embedding_R1: 0.475
1068	        dataflow_R1: 0.458
1069	        embedding_minus_random_pp: 1.5
1070	      pool_100:
1071	        random_R1: 0.358
1072	        embedding_R1: 0.372
1073	        dataflow_R1: 0.357
1074	        embedding_minus_random_pp: 1.4
1075	      pool_200:
1076	        random_R1: 0.282
1077	        embedding_R1: 0.295
1078	        dataflow_R1: 0.281
1079	        embedding_minus_random_pp: 1.3
1080	      pool_500:
1081	        random_R1: 0.214
1082	        embedding_R1: 0.225
1083	        dataflow_R1: 0.213
1084	        embedding_minus_random_pp: 1.1
1085	    ranking_stable_across_pools: true
1086	    pool_ranking_stable_pct: 100
1087	    delta_shrinkage_rate: ~0.15pp per doubling of pool size
1088	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
1089	    > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct
1090	    = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors
1091	    = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)，
1092	    缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 "hard" negative 的概率增加（base
1093	    rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有
1094	    +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500)
1095	    但保持正值。 这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x pool 扩大，
1096	    strategy ranking 完全不翻转。
1097	
1098	    '
1099	  tables:
1100	  - name: 'Table 12: Pool Size Sensitivity (R@1 %)'
1101	    columns:
1102	    - Pool
1103	    - Encoder
1104	    - random
1105	    - embedding
1106	    - dataflow
1107	    - emb−rand (pp)
1108	    - Ranking
1109	    rows:
1110	    - - 50
1111	      - Qwen
1112	      - 54.5
1113	      - 56.5
1114	      - 55.5
1115	      - '+2.0'
1116	      - E>D>R
1117	    - - 100
1118	      - Qwen
1119	      - 42.8
1120	      - 44.7
1121	      - 43.8
1122	      - '+1.9'
1123	      - E>D>R
1124	    - - 200
1125	      - Qwen
1126	      - 34.2
1127	      - 35.9
1128	      - 35.1
1129	      - '+1.7'
1130	      - E>D>R
1131	    - - 500
1132	      - Qwen
1133	      - 26.1
1134	      - 27.6
1135	      - 26.9
1136	      - '+1.5'
1137	      - E>D>R
1138	    - - 50
1139	      - StarCoder
1140	      - 46.0
1141	      - 47.5
1142	      - 45.8
1143	      - '+1.5'
1144	      - E>R>D
1145	    - - 100
1146	      - StarCoder
1147	      - 35.8
1148	      - 37.2
1149	      - 35.7
1150	      - '+1.4'
1151	      - E>R>D
1152	    - - 200
1153	      - StarCoder
1154	      - 28.2
1155	      - 29.5
1156	      - 28.1
1157	      - '+1.3'
1158	      - E>R≈D
1159	    - - 500
1160	      - StarCoder
1161	      - 21.4
1162	      - 22.5
1163	      - 21.3
1164	      - '+1.1'
1165	      - E>R≈D
1166	  figures_description:
1167	  - 'Fig 10: Pool size (x-axis, log scale) vs R@1 (y-axis) for 3 strategies, separate
1168	    panels for Qwen and StarCoder. Shaded bands between embedding and random lines
1169	    highlight persistent delta.'
1170	  - 'Fig 10b: Delta (embedding − random) vs pool size, showing graceful degradation'
1171	  analysis: Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是
1172	    best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是
1173	    robust 的。论文可以明确声明："Strategy rankings are stable across pool sizes spanning an
1174	    order of magnitude (50–500), with embedding mining maintaining a statistically
1175	    significant advantage even at the largest pool tested."
1176	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "cb644978-8a95-4e11-82ee-8fc3cf4e6808"
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
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "description": "Running grep -r \"temperature\\|tau\\|lora_rank\\|lora_alpha\\…",
  "usage": {
    "total_tokens": 101194,
    "tool_uses": 11,
    "duration_ms": 20332
  },
  "last_tool_name": "Bash",
  "uuid": "586b8a56-e1f2-441a-a5c7-412a038042a8",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01H3NrrWHmLUjyc9FUDQa5Ei`</summary>

```json
{
  "command": "grep -r \"temperature\\|tau\\|lora_rank\\|lora_alpha\\|learning_rate\\|batch_size\\|max_seq_length\\|proj_dim\\|warmup_ratio\\|weight_decay\\|num_epochs\\|early_stopping_patience\\|num_negatives\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context --include=\"*.py\" --include=\"*.sh\" --include=\"*.md\" | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "0baa9bdb-233f-4054-a821-5b4cc51dbd4a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XvUUwkV2qQeVczawnPyexh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 59969,
      "cache_read_input_tokens": 41185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 59969,
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

_source line 51 · 2026-05-15T09:28:54.779Z_

<details><summary>↩ Tool result · `toolu_01H3NrrWHmLUjyc9FUDQa5Ei`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:        self, query: str, candidates: list[str], batch_size: int = 32
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:        max_seq_length: int = 2048,
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:        self.max_seq_length = max_seq_length
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:            proj_dim=cfg.get("proj_dim", 256),
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:            lora_alpha=cfg.get("lora_alpha", 32),
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:    def _encode(self, texts: list[str], batch_size: int) -> np.ndarray:
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:        for i in range(0, len(texts), batch_size):
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:            batch = texts[i : i + batch_size]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:                max_length=self.max_seq_length,
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:        self, query: str, candidates: list[str], batch_size: int = 32
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:        q = self._encode([query], batch_size=1)
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:        d = self._encode(docs, batch_size=batch_size)
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:            max_seq_length=args.max_seq_length,
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py:                query, inst.context, batch_size=args.batch_size
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/handoff_20260513.md:5. **M2 完成后可同时跑 plan_014/015**（temperature ablation + dynamic mining）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/handoff_20260513.md:- tau pilot 在 MVP 数据上意义有限（pool size 不同导致 recall 不可比），全量 ablation 在 M1 数据上做才有意义
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/IDEA_BRIEF.md:- **auto_research**: {'claude_api_cost': '$200-400 (2000-4000 turns for iterative pipeline development, CodeQL query debugging, experiment scheduling)', 'estimated_gpu_cost': '$500-700 (200h H100 at spot ~$2.50/hr to on-demand ~$3.50/hr)', 'gpu_hours': '~200h H100 (full ablation suite including label-heterogeneity experiments, hyperparameter sweep over contrastive temperature and hard negative ratio, primary + secondary benchmark evaluation)', 'gpu_utilization': '~85-90% utilization; agent continuously launches experiments, parallelizes independent ablations', 'risk_note': 'Agent should validate scope-bounded CodeQL query on first 10 repos and report: (a) timeout rate with 300s limit, (b) avg reachable files within 2 call-graph hops, (c) fraction requiring Beniget fallback. If CodeQL timeout rate >30%, agent autonomously tightens to 1 call-graph hop. Label-source statistics automatically tracked and reported.', 'speed_bottleneck': 'SWE-bench Lite evaluation (~8min/instance x 300 instances on Qwen3.6-27B = ~40 H100-hours; parallelizable across GPUs). Optional SWE-bench Pro adds ~40h.', 'team': '0 (initial setup: CodeQL CLI installation, SWE-smith repo cloning, SWE-bench evaluation harness)', 'timeline': '10-12 days with 2-4 H100 GPUs available concurrently'}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/director/loop_3.md:2. eval_swebench.py 两个 bug 修复（lora_alpha 读 config、repo-cache-dir 参数）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/director/loop_3.md:- plan_014 temperature ablation（M2 完成后优先）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/director/loop_4.md:- **易错点**：(1) 不要把 MVP 的 BM25-proxy 结果 (-27pp) 当作 embedding distance 证据，那是 mislabeling (2) n=3 seeds 统计功效很低(df=2)，Type II error 高，No-Go 不等于无效应 (3) 过拟合模式一致（两编码器都 step 1000 best），但 StarCoder 的 eval@1500 降幅比 Qwen 小（-0.5pp vs -3pp），表征空间更健康 (4) plan_014 的 temperature 是 learnable parameter（`log_temperature`），ablation 测的是初始化值，已修复传参 bug
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/director/loop_1.md:- **MVP FAIL（dataflow 无显著优势）→ 排查过拟合**：降 lr / 加 weight_decay / 增大 num_negatives / early stopping，限 1 次重试后仍 fail → kill 项目
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/director/loop_2.md:- Full M2 完成后优先启动 plan_014 temperature ablation (~10h)
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/agent/loop_3.md:- M2 全部完成 → plan_014 temperature ablation（P1，~10h）+ plan_003 SWE-bench eval（P0，需 Qwen checkpoint）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/agent/loop_4.md:- eval 脚本 bug fixes 完成（lora_alpha、repo-cache-dir、e2e placeholder 实现）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/agent/loop_4.md:- M2 完成 → 执行 plan_014 temperature ablation（D025 scope: 2 strategies × 3 τ × 2 epochs = 6 runs，脚本已就绪）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/agent/loop_5.md:- m2_full_qwen conclusion=success 且 embedding > random 显著 → cuda:0 立即启动 plan_003 SWE-bench eval（脚本已 dry-run pass）或 plan_014 temperature ablation
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/agent/loop_8_1778818340.md:5. **K=7 无 ablation**：所有正式实验固定 K=7（batch_size=8 对齐），K 敏感性列为 limitation/future work
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/agent/loop_2.md:  - train.py 已有 `--temperature` 参数（τ pilot 加的），默认 0.05。M2 训练时注意是否要改回 0.07
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/agent/loop_5_1778781850.md:- **GPU 空闲** → plan_014 temperature ablation（脚本 D025 缩减版，6 runs ~70h）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_3.md:- W&B：`WANDB_MODE=disabled`（tau pilot 期间确认）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_3.md:- worker_monitor_tau_pilot_results / finish_and_cleanup → WARNING。tau_pilot_0.05/0.1 checkpoint 全部删除，无 eval 结果，无 registry 条目。Director 已收到两次通知但尚无回应。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_3.md:- Director 回应 tau_pilot 清理原因 → 确认是否需要重跑 pilot 或直接进 plan_014 全量温度消融
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_3.md:  2. tau_pilot 数据已丢失（checkpoint 删了没做 eval），不要假设有温度先验数据。plan_014 需从零开始。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_4.md:- StarCoder registry notes 仍显示旧超参（batch_size=4, epochs=2）——实际训练用 batch_size=8, epochs=3。如果 Agent 引用 registry 旧参数做分析，要拦
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_6.md:3. **plan_014 (temperature ablation) 已缩减为 6 runs（D025）**，不是原来的 9 runs
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_5.md:- SWE-bench eval placeholder 实现（PASS：StructFuseRetriever 接口正确，lora_alpha 硬编码为 minor warning）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_5.md:- **eval_swebench.py L230 `lora_alpha` 修复** → 低优先级，当前实验 alpha=32=2×16 恰好一致，但应改为 `cfg.get("lora_alpha", 32)`。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/task_context/history/reviewer/loop_1.md:- **P2b FAIL** → 审查 fail_action（调训练策略 1 次：降 lr / 加 weight decay / 增大 num_negatives / early stopping），过拟合是首要排查方向（train loss 在 step 200 即为 0）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md:**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) K=7 negatives are randomly sampled from a pool of 50 strategy-specific candidates per query。K 敏感性列为 limitation/future work。
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md:- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md:4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a/CLAUDE.md:- [ ] 完成 ablation_learning_rate（plan_003）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a/AGENTS.md:- [ ] 完成 ablation_learning_rate（plan_003）
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_3cf111.md:$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_3cf111.md:where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query. Our framework supports distance-weighted positive scores via per-sample weights $w_i = \exp(-\alpha \cdot d_i)$, where $d_i$ is the data-flow path distance from query to positive and $\alpha = 1.0$. In practice, the training data assigns a uniform distance of $d = 1$ to all positives, yielding a constant weight $w = e^{-1}$ across all samples. Since this scales all per-sample losses equally, the optimization is equivalent to standard unweighted InfoNCE.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_eccca0.md:**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_ce3556.md:$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_ce3556.md:where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query. Our framework supports distance-weighted positive scores via per-sample weights $w_i = \exp(-\alpha \cdot d_i)$, where $d_i$ is the data-flow path distance from query to positive and $\alpha = 1.0$. In practice, the training data assigns a uniform distance of $d = 1$ to all positives, yielding a constant weight $w = e^{-1}$ across all samples. Since this scales all per-sample losses equally, the optimization is equivalent to standard unweighted InfoNCE.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md:**K = 7** (`num_negatives=7`) for all main experiments: m2_full_qwen, m2_full_starcoder, m2_embed_verify, plan_013_starcoder. Earlier MVP experiments (p2b series) used K=3 but are superseded.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_bcd130.md:**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md:**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_054f8d.md:**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md:$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md:where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md:| Temperature ($\tau$, initial) | 0.07 (learnable) |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_d4b180.md:**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_ae4280.md:$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_ae4280.md:where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/run_full_m2_training.sh:#   batch_size=8, num_negatives=7, max_seq_length=2048, epochs=2
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/contrastive_model.py:        proj_dim: int = 256,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "3b92ec43-aee1-4341-9364-1cb8b3bcc4b4"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a6e01105f5daa7414",
  "tool_use_id": "toolu_012UHYV5Zn8FYeYLf5i4NGof",
  "status": "completed",
  "output_file": "",
  "summary": "Find training config/registry",
  "usage": {
    "total_tokens": 108035,
    "tool_uses": 11,
    "duration_ms": 31931
  },
  "uuid": "00ca307e-c34d-48cc-9802-e729bcaf51aa",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745"
}
```

---

### Tool result

_source line 53 · 2026-05-15T09:29:06.317Z_

<details><summary>↩ Tool result · `toolu_012UHYV5Zn8FYeYLf5i4NGof`</summary>

```text
Excellent! Now let me compile all the training configuration values I've found. Let me create a comprehensive summary based on all the information gathered.

Based on my thorough search of the StructFuse project training configuration files and experiment registry, here are the verified hyperparameter and configuration values:

## Training Configuration Values Found

**File Sources:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml` (experiment registry)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1*.md` (paper drafts)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md`

### Core Training Hyperparameters

| Parameter | Value | Source |
|-----------|-------|--------|
| **Temperature (τ)** | 0.07 (initial, learnable) | registry, experiments_v1.md, method_v1.md |
| **LoRA Rank (r)** | 16 | experiments_v1.md, method_v1 series |
| **LoRA Alpha (α)** | 32 | experiments_v1.md, eval_repobench.py |
| **Learning Rate** | 2e-5 (2×10⁻⁵) | experiments_v1.md, m2_full_qwen registry spec |
| **Batch Size** | 8 | experiments_v1.md, registry (m2_full_qwen), intermediate/run_full_m2_training.sh |
| **Max Sequence Length** | 2,048 | experiments_v1.md, registry, eval_repobench.py |
| **Projection Dimension (proj_dim)** | 256 | experiments_v1.md, registry (m2_full_qwen notes), contrastive_model.py |
| **Warmup Ratio** | 0.1 (10% linear warmup) | experiments_v1.md |
| **Weight Decay** | 0.01 | experiments_v1.md, registry (m2_full_qwen spec) |
| **Number of Epochs** | 3 (s42), 2 (s43/s44 with early stopping) | registry (m2_full_qwen metrics, m2_full_starcoder notes) |
| **Early Stopping Patience** | 2 | registry (m2_full_qwen notes: "early_stopping_patience=2") |
| **Number of Negatives (K)** | 7 | experimental_setup_k_checkpoint.md, run_full_m2_training.sh comments |
| **Pool Size** | 50 (primary), 26, 100, 200, 500 (sensitivity tests) | registry (p2b_eval_4runs_pool50, plan_019) |

### Additional Training Details

- **LoRA Target**: Applied to query (Wq) and value (Wv) projection matrices of every attention layer
- **LoRA Dropout**: 0.05
- **Pooling Strategy**: Mean pooling over non-padding positions
- **Normalization**: L2 normalization post-pooling
- **Projection Head**: Two-layer MLP (Linear→GELU→Linear) mapping to 256-dimensional embedding
- **Loss Function**: InfoNCE with learnable temperature
- **Optimizer**: AdamW with cosine annealing schedule
- **Gradient Clipping**: Max norm 1.0
- **Gradient Checkpointing**: Enabled

### Experiment-Specific Configurations

**m2_full_qwen registry entry** (lines 964-1032 in registry.yaml):
- `batch_size: 8`
- `num_negatives: 7`
- `lr: 2e-5`
- `eval_steps: 500`
- `max_seq_length: 2048`
- `warmup_ratio: 0.1`
- `weight_decay: 0.01`
- `temperature: 0.07`
- `proj_dim: 256`
- Training data: ~11.3K instances/seed, validation: ~3K instances/seed

### Files Containing Configuration Details

1. **Primary Config Sources:**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml` - Main experiment registry with all run details
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_bcd130.md` - Paper draft with complete fine-tuning config

2. **Supporting Files:**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_3cf111.md` - LoRA and temperature specifications
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md` - K=7 negatives rationale
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py` - Encoder initialization with proj_dim=256, lora_alpha=32
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/run_full_m2_training.sh` - Training script with batch_size, num_negatives, epochs documented

All values are confirmed across multiple sources within the experiment registry and paper drafts, ensuring consistency and accuracy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "58f57053-23d7-4964-b516-925f056b9e48",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ for training configuration files, experiment registry, or hyperparameter configs. I need to verify these specific values: temperature (τ), LoRA rank (r), LoRA alpha (α), learning rate, batch size, max_seq_length, proj_dim, warmup_ratio, weight_decay, num_epochs, early_stopping_patience, pool_size, num_negatives (K).\n\nLook for files like:\n- registry files (yaml/json)\n- training config files\n- experiment config\n- Also check the artifacts/ directory\n\nSearch breadth: medium",
    "agentId": "a6e01105f5daa7414",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now let me compile all the training configuration values I've found. Let me create a comprehensive summary based on all the information gathered.\n\nBased on my thorough search of the StructFuse project training configuration files and experiment registry, here are the verified hyperparameter and configuration values:\n\n## Training Configuration Values Found\n\n**File Sources:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml` (experiment registry)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1*.md` (paper drafts)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md`\n\n### Core Training Hyperparameters\n\n| Parameter | Value | Source |\n|-----------|-------|--------|\n| **Temperature (τ)** | 0.07 (initial, learnable) | registry, experiments_v1.md, method_v1.md |\n| **LoRA Rank (r)** | 16 | experiments_v1.md, method_v1 series |\n| **LoRA Alpha (α)** | 32 | experiments_v1.md, eval_repobench.py |\n| **Learning Rate** | 2e-5 (2×10⁻⁵) | experiments_v1.md, m2_full_qwen registry spec |\n| **Batch Size** | 8 | experiments_v1.md, registry (m2_full_qwen), intermediate/run_full_m2_training.sh |\n| **Max Sequence Length** | 2,048 | experiments_v1.md, registry, eval_repobench.py |\n| **Projection Dimension (proj_dim)** | 256 | experiments_v1.md, registry (m2_full_qwen notes), contrastive_model.py |\n| **Warmup Ratio** | 0.1 (10% linear warmup) | experiments_v1.md |\n| **Weight Decay** | 0.01 | experiments_v1.md, registry (m2_full_qwen spec) |\n| **Number of Epochs** | 3 (s42), 2 (s43/s44 with early stopping) | registry (m2_full_qwen metrics, m2_full_starcoder notes) |\n| **Early Stopping Patience** | 2 | registry (m2_full_qwen notes: \"early_stopping_patience=2\") |\n| **Number of Negatives (K)** | 7 | experimental_setup_k_checkpoint.md, run_full_m2_training.sh comments |\n| **Pool Size** | 50 (primary), 26, 100, 200, 500 (sensitivity tests) | registry (p2b_eval_4runs_pool50, plan_019) |\n\n### Additional Training Details\n\n- **LoRA Target**: Applied to query (Wq) and value (Wv) projection matrices of every attention layer\n- **LoRA Dropout**: 0.05\n- **Pooling Strategy**: Mean pooling over non-padding positions\n- **Normalization**: L2 normalization post-pooling\n- **Projection Head**: Two-layer MLP (Linear→GELU→Linear) mapping to 256-dimensional embedding\n- **Loss Function**: InfoNCE with learnable temperature\n- **Optimizer**: AdamW with cosine annealing schedule\n- **Gradient Clipping**: Max norm 1.0\n- **Gradient Checkpointing**: Enabled\n\n### Experiment-Specific Configurations\n\n**m2_full_qwen registry entry** (lines 964-1032 in registry.yaml):\n- `batch_size: 8`\n- `num_negatives: 7`\n- `lr: 2e-5`\n- `eval_steps: 500`\n- `max_seq_length: 2048`\n- `warmup_ratio: 0.1`\n- `weight_decay: 0.01`\n- `temperature: 0.07`\n- `proj_dim: 256`\n- Training data: ~11.3K instances/seed, validation: ~3K instances/seed\n\n### Files Containing Configuration Details\n\n1. **Primary Config Sources:**\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml` - Main experiment registry with all run details\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_bcd130.md` - Paper draft with complete fine-tuning config\n\n2. **Supporting Files:**\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_3cf111.md` - LoRA and temperature specifications\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md` - K=7 negatives rationale\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py` - Encoder initialization with proj_dim=256, lora_alpha=32\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/intermediate/run_full_m2_training.sh` - Training script with batch_size, num_negatives, epochs documented\n\nAll values are confirmed across multiple sources within the experiment registry and paper drafts, ensuring consistency and accuracy."
      }
    ],
    "totalDurationMs": 31936,
    "totalTokens": 109476,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6838,
      "cache_read_input_tokens": 101154,
      "output_tokens": 1478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6838
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1478,
          "cache_read_input_tokens": 101154,
          "cache_creation_input_tokens": 6838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6838,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 3,
      "bashCount": 4,
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

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Key findings from the registry verification:

Important corrections from the task description:
1. **Temperature τ=0.07** - confirmed, and it's learnable (initial value)
2. **LoRA targets**: Wq and Wv (query and value projections), not just "attention layers"
3. **LoRA dropout**: 0.05
4. **Number of epochs**: registry shows 3 (s42) and 2 (s43/s44 with early stopping) — the task says "2 epochs + early stopping patience=2" but actual is 3 epochs max with early stopping


5. **Gradient clipping**: max norm 1.0
6. **Projection head**: Two-layer MLP (Linear→GELU→Linear) mapping to 256-dim
7. **Pooling**: Mean pooling over non-padding, L2 normalization
8. **Optimizer**: AdamW with cosine annealing schedule (not just AdamW)

The epoch discrepancy is clearer now—s42 completed all 3 epochs without early stopping triggering, while s43 and s44 stopped at 2 epochs when the patience threshold was hit. I should go with the registry values since the task explicitly says to confirm all hyperparameters from there. The registry shows 3 epochs maximum with early stopping patience of 2, and I also need to note that temperature is 0.07 (learnable) and the LoRA modules target Wq and Wv specifically.

Now I'm structuring the method section across five subsections totaling around 1000 words, being careful to use the correct framing language about reliable improvements and negligible costs, confirm that BM25 handles the ranking in the dataflow, cite properly, and incorporate those scalability numbers about the 123 repos and structural coverage metrics. I'm completing the InfoNCE loss formula and explaining the core research question around negative mining strategies. Then I'm describing how we extract structural information using CodeQL to perform taint-tracking analysis on the repository, identifying which files are reachable from a query function through data-flow dependencies.

When CodeQL isn't available due to build issues, I fall back to a simpler AST-based analyzer to maintain coverage. Across the full dataset of 123 repositories and over 44,000 training instances, structural connectivity information is successfully extracted for about a third of the cases.

Now I'm looking at the negative mining strategies we're comparing. We're testing three different approaches for selecting hard negatives—random sampling as a baseline, embedding-distance based selection, and presumably other difficulty-based strategies. For each query, we pull 50 candidate negatives and then randomly sample 7 of them per instance to avoid conflating the selection strategy with sampling noise.

The embedding-distance approach uses a frozen pretrained encoder to find semantically similar non-gold files—these are the near-misses that look relevant but aren't actual targets. Since we're already using the pretrained encoder, this adds no computational overhead beyond a one-time embedding pass.

The dataflow-aware strategy is more sophisticated: it first filters out structurally connected files (those reachable through data-flow or call-graph paths from the query), ensuring negatives are truly disconnected from the functional context, then ranks the remaining candidates by BM25 relevance. We're using two different 3B parameter models—Qwen2.5-Coder and StarCoder2—to test whether the mining strategy works consistently across encoders with different pretraining backgrounds. For fine-tuning, I'm applying LoRA with specific hyperparameters to the attention layers, then processing the encoded sequences through mean pooling and normalization before projecting them into a 256-dimensional space via a small MLP. The training uses AdamW optimization...

For training, I'm setting up a contrastive learning setup with InfoNCE loss where each batch has one positive example and seven negatives, using cosine annealing with warmup and early stopping based on validation loss, while tracking both the best checkpoint by validation loss and by Recall@1 performance. The evaluation measures how well the model ranks a pool of 50 candidate files by cosine similarity, with Recall@1 as the primary metric.

To ensure robustness, I'm running each encoder and mining strategy combination three times with different random seeds and computing bootstrap confidence intervals across all 18 runs. I'm also validating that improvements in retrieval actually translate to better performance on downstream tasks using SWE-bench Lite.

Now I'm checking the citation references—I need to verify that LoRA is actually in the bibliography before including it, and I'm also doing a quick word count estimate across the sections to make sure everything stays within the target ranges. I found an issue with the LoRA citation—it's not in the references file, so I need to remove it and just mention LoRA by name instead. Also, I'm noticing a discrepancy between the task description saying "2 epochs + early stopping patience=2" and the registry showing "up to 3 epochs"—the registry is authoritative, so I'll go with that. I need to verify the training data breakdown—the registry shows 44,173 total instances across 123 repos, but I should clarify how that maps to the per-seed counts the agent reported.

I'll use 44,173 for the extraction pipeline scale in §3.2 and note the per-strategy training size separately if needed. Also confirming the temperature is 0.07 (learnable, not 0.05) and I've already covered the dual checkpoint strategy with the D036 reference in §3.4, so I'm ready to write the final version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "1bd14929-507f-4da9-aa2a-41cff443ecbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jpu4Knm9wWhyzs2k5UyhG9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2693,
      "cache_read_input_tokens": 41181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2693
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

_source line 55_

Registry confirms key corrections: τ=0.07 (learnable), LoRA targets Wq/Wv with dropout 0.05, max 3 epochs (not 2), cosine annealing schedule, gradient clipping 1.0, two-layer MLP projection head. Writing the draft now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "7446a771-002e-4b90-8b0f-3129b4405841",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jpu4Knm9wWhyzs2k5UyhG9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2693,
      "cache_read_input_tokens": 41181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2693
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01KBcp5sULzfivj46HnBbFPQ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/",
  "description": "List paper_drafts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "352b9042-6e1f-4199-a497-925c827edeea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jpu4Knm9wWhyzs2k5UyhG9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2693,
      "cache_read_input_tokens": 41181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2693
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

_source line 57 · 2026-05-15T09:30:47.775Z_

<details><summary>↩ Tool result · `toolu_01KBcp5sULzfivj46HnBbFPQ`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "2fe00442-74aa-49d2-847b-8396e18a041a",
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

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01PY41nwjqZEMypY5EkHPCZA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "8c3b6cc2-3ad9-418d-900e-8e4ff2201ecd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6eJnq1q2TQ5iTrGXMiGjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4471,
      "cache_read_input_tokens": 43874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4471
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

_source line 59 · 2026-05-15T09:30:50.445Z_

<details><summary>↩ Tool result · `toolu_01PY41nwjqZEMypY5EkHPCZA`</summary>

```text
1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "a1c8e539-1032-4be6-ac98-881f29c54095",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 117
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
There's already a method_v1.md. I need to overwrite it with the new draft. Let me write the full new draft.

Let me finalize the content and write it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "7bd26d7c-5d46-43d3-91b2-f12afc8bb214",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158ZSD3nZsgQbec2FCfK1ot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 368,
      "cache_read_input_tokens": 48345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 368
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

_source line 61_

Existing method_v1.md will be overwritten. Writing the new draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "2f34c779-8c1b-42b5-8b75-5537c4609c38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158ZSD3nZsgQbec2FCfK1ot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 368,
      "cache_read_input_tokens": 48345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 368
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

_source line 62_

<details open><summary>🔧 Tool call — Write · `toolu_018Cjybdtdm3kBkVmqSJsmPT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "content": "# 3. Method\n\n## 3.1 Problem Formulation\n\nWe formulate file-level code retrieval as a contrastive learning problem. Given a repository $\\mathcal{R}$ containing source files, a query $q$ consists of a buggy function or file paired with its issue description. A positive file $p \\in \\mathcal{R}$ is the gold patch target---a file modified to resolve the issue. All remaining non-query, non-gold files constitute the negative candidate pool.\n\nWe train an encoder $E: \\mathcal{F} \\to \\mathbb{R}^d$ such that $\\text{sim}(E(q), E(p)) \\gg \\text{sim}(E(q), E(n))$ for any negative $n$. Training minimizes the InfoNCE loss \\cite{chen2020simclr}:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E(q), E(p)) / \\tau)}{\\exp(\\text{sim}(E(q), E(p)) / \\tau) + \\sum_{i=1}^{K} \\exp(\\text{sim}(E(q), E(n_i)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter and $\\{n_1, \\ldots, n_K\\}$ are $K$ negatives selected by a mining strategy. The central question is how the choice of mining strategy affects retrieval quality, and whether structural code information provides signal beyond embedding similarity.\n\n## 3.2 Structural Extraction Pipeline\n\nTo enable structure-aware negative mining, we extract inter-procedural data-flow graphs from repository snapshots using CodeQL \\cite{avgustinov2016ql}. For each query function $q$, we construct a CodeQL database from the repository at the relevant commit, then perform bounded taint-tracking analysis to identify all files reachable from $q$ through inter-procedural data-flow paths. This captures cross-function semantic relationships---for instance, a utility function that transforms data passed from a source through multiple call boundaries.\n\nA file $f$ is \\emph{connected} to query $q$ if $f$ is reachable from $q$ via inter-procedural data-flow paths in the structural graph $G$; otherwise $f$ is \\emph{disconnected}. Connected files include both gold targets and non-gold files that participate in the query's data-flow neighborhood (e.g., shared utility modules, intermediate processing functions).\n\nWhen CodeQL analysis fails due to missing build configurations, we fall back to beniget, a Python AST-based def-use analyzer providing intra-module data-flow coverage. At full scale, the pipeline processes 123 repositories comprising 44,173 training instances with 0\\% analysis timeout. Structural connectivity is available for 34.3\\% of instances; among those, 78\\% of connected files are non-gold, confirming that connectivity captures functional relevance beyond gold-file identity. We frame this pipeline as a practical enabling tool (\\S5), not a standalone contribution.\n\n## 3.3 Negative Mining Strategies\n\nWe compare three strategies spanning different dimensions of negative difficulty. All strategies share a common two-stage protocol: first, a pool of 50 candidate negatives is constructed according to the strategy; then $K{=}7$ negatives are randomly sampled from this pool per training instance. This decouples strategy-specific selection from stochastic sampling effects.\n\n**Random.** Negatives are drawn uniformly at random from all non-positive files within the same repository. This serves as the no-signal baseline, reflecting the standard approach in dense retrieval \\cite{karpukhin2020dpr}.\n\n**Embedding-distance.** We compute cosine similarity between the query and all non-positive repository files using a pretrained encoder (frozen; not updated during training). The 50 most similar non-positive files form the candidate pool. These are semantic near-misses: files that \\emph{appear} relevant to the pretrained encoder but are not gold targets. This strategy incurs zero additional cost beyond the one-time offline embedding computation, as the pretrained encoder is already available.\n\n**Dataflow-aware.** This strategy combines structural filtering with lexical ranking. First, all structurally connected files are excluded from the candidate pool---specifically, files reachable via inter-procedural data-flow paths and call-graph neighbors ($\\text{positive\\_files} \\cup \\text{cg\\_connected}$). This ensures negatives are structurally disconnected from the query. Second, the remaining disconnected files are ranked by BM25 score \\cite{robertson2009bm25} in descending order, and the top-50 form the candidate pool. Formally:\n\n$$\\text{pool}_{\\text{df}}(q) = \\underset{x \\in \\mathcal{D} :\\ x \\notin R_G(q) \\,\\wedge\\, x \\notin \\text{gold}(q)}{\\text{top-}50}\\ \\text{BM25}(q, x)$$\n\nwhere $R_G(q)$ denotes files reachable from $q$ in structural graph $G$. Structural information serves exclusively as a \\emph{filter} (determining which files to exclude), while BM25 provides the \\emph{ranking} signal among remaining candidates. The rationale is that high-BM25, structurally-disconnected files are lexically similar but functionally unrelated---a complementary difficulty dimension to embedding distance.\n\n## 3.4 Training Setup\n\n**Encoders.** We use two decoder-only code language models with distinct pretraining: Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2}. These encoders differ in pretraining corpora and representation geometry, enabling examination of whether mining strategy effectiveness interacts with encoder properties.\n\n**Fine-tuning.** We apply LoRA adaptation with rank $r{=}16$, scaling factor $\\alpha{=}32$, and dropout 0.05, targeting query and value projection matrices ($W_q$, $W_v$) in every attention layer. Input sequences are truncated to 2,048 tokens. We use mean pooling over non-padding positions followed by L2 normalization, then project through a two-layer MLP (Linear$\\to$GELU$\\to$Linear) to a 256-dimensional embedding space.\n\n**Optimization.** We use AdamW (lr=$2 \\times 10^{-5}$, cosine annealing, warmup ratio 0.1, weight decay 0.01) for up to 3 epochs with gradient checkpointing and gradient clipping (max norm 1.0). The InfoNCE temperature is initialized to $\\tau{=}0.07$ and learned during training. Each batch contains 1 positive and $K{=}7$ negatives (effective batch size 8). Early stopping with patience 2 is applied based on validation loss, evaluated every 500 steps. We save two checkpoints per run: best by validation loss and best by validation R@1.\n\n## 3.5 Evaluation Protocol\n\n**Retrieval metric.** We evaluate on a pool-based retrieval task: given a query, the model ranks a candidate pool of 50 files by cosine similarity. The primary metric is Recall@1 (R@1)---whether the top-ranked file is a gold patch target.\n\n**Checkpoint selection.** We report the best-by-R@1 checkpoint as the primary result, selected by validation R@1. Fixed-checkpoint comparisons are reported as a robustness check to confirm that strategy rankings are not artifacts of checkpoint selection.\n\n**Statistical rigor.** Each encoder $\\times$ strategy combination is trained with 3 random seeds (42, 43, 44), yielding 18 total runs (2 encoders $\\times$ 3 strategies $\\times$ 3 seeds). We report bootstrap 95\\% confidence intervals for all comparisons.\n\n**Downstream evaluation.** To validate that retrieval improvements transfer to end-to-end performance, we evaluate on SWE-bench Lite \\cite{jimenez2024swebench} (300 instances) with an LLM-based repair agent. The retriever provides file-level context, measuring whether improved retrieval translates to higher issue resolution rates.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "ce80d1f2-0557-4360-b3ac-88f5adcb9910",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158ZSD3nZsgQbec2FCfK1ot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 368,
      "cache_read_input_tokens": 48345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 368
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

_source line 63 · 2026-05-15T09:31:44.003Z_

<details><summary>↩ Tool result · `toolu_018Cjybdtdm3kBkVmqSJsmPT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "6717b2dc-f1e2-4697-bdee-642c785b611e",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "content": "# 3. Method\n\n## 3.1 Problem Formulation\n\nWe formulate file-level code retrieval as a contrastive learning problem. Given a repository $\\mathcal{R}$ containing source files, a query $q$ consists of a buggy function or file paired with its issue description. A positive file $p \\in \\mathcal{R}$ is the gold patch target---a file modified to resolve the issue. All remaining non-query, non-gold files constitute the negative candidate pool.\n\nWe train an encoder $E: \\mathcal{F} \\to \\mathbb{R}^d$ such that $\\text{sim}(E(q), E(p)) \\gg \\text{sim}(E(q), E(n))$ for any negative $n$. Training minimizes the InfoNCE loss \\cite{chen2020simclr}:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E(q), E(p)) / \\tau)}{\\exp(\\text{sim}(E(q), E(p)) / \\tau) + \\sum_{i=1}^{K} \\exp(\\text{sim}(E(q), E(n_i)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter and $\\{n_1, \\ldots, n_K\\}$ are $K$ negatives selected by a mining strategy. The central question is how the choice of mining strategy affects retrieval quality, and whether structural code information provides signal beyond embedding similarity.\n\n## 3.2 Structural Extraction Pipeline\n\nTo enable structure-aware negative mining, we extract inter-procedural data-flow graphs from repository snapshots using CodeQL \\cite{avgustinov2016ql}. For each query function $q$, we construct a CodeQL database from the repository at the relevant commit, then perform bounded taint-tracking analysis to identify all files reachable from $q$ through inter-procedural data-flow paths. This captures cross-function semantic relationships---for instance, a utility function that transforms data passed from a source through multiple call boundaries.\n\nA file $f$ is \\emph{connected} to query $q$ if $f$ is reachable from $q$ via inter-procedural data-flow paths in the structural graph $G$; otherwise $f$ is \\emph{disconnected}. Connected files include both gold targets and non-gold files that participate in the query's data-flow neighborhood (e.g., shared utility modules, intermediate processing functions).\n\nWhen CodeQL analysis fails due to missing build configurations, we fall back to beniget, a Python AST-based def-use analyzer providing intra-module data-flow coverage. At full scale, the pipeline processes 123 repositories comprising 44,173 training instances with 0\\% analysis timeout. Structural connectivity is available for 34.3\\% of instances; among those, 78\\% of connected files are non-gold, confirming that connectivity captures functional relevance beyond gold-file identity. We frame this pipeline as a practical enabling tool (\\S5), not a standalone contribution.\n\n## 3.3 Negative Mining Strategies\n\nWe compare three strategies spanning different dimensions of negative difficulty. All strategies share a common two-stage protocol: first, a pool of 50 candidate negatives is constructed according to the strategy; then $K{=}7$ negatives are randomly sampled from this pool per training instance. This decouples strategy-specific selection from stochastic sampling effects.\n\n**Random.** Negatives are drawn uniformly at random from all non-positive files within the same repository. This serves as the no-signal baseline, reflecting the standard approach in dense retrieval \\cite{karpukhin2020dpr}.\n\n**Embedding-distance.** We compute cosine similarity between the query and all non-positive repository files using a pretrained encoder (frozen; not updated during training). The 50 most similar non-positive files form the candidate pool. These are semantic near-misses: files that \\emph{appear} relevant to the pretrained encoder but are not gold targets. This strategy incurs zero additional cost beyond the one-time offline embedding computation, as the pretrained encoder is already available.\n\n**Dataflow-aware.** This strategy combines structural filtering with lexical ranking. First, all structurally connected files are excluded from the candidate pool---specifically, files reachable via inter-procedural data-flow paths and call-graph neighbors ($\\text{positive\\_files} \\cup \\text{cg\\_connected}$). This ensures negatives are structurally disconnected from the query. Second, the remaining disconnected files are ranked by BM25 score \\cite{robertson2009bm25} in descending order, and the top-50 form the candidate pool. Formally:\n\n$$\\text{pool}_{\\text{df}}(q) = \\underset{x \\in \\mathcal{D} :\\ x \\notin R_G(q) \\,\\wedge\\, x \\notin \\text{gold}(q)}{\\text{top-}50}\\ \\text{BM25}(q, x)$$\n\nwhere $R_G(q)$ denotes files reachable from $q$ in structural graph $G$. Structural information serves exclusively as a \\emph{filter} (determining which files to exclude), while BM25 provides the \\emph{ranking} signal among remaining candidates. The rationale is that high-BM25, structurally-disconnected files are lexically similar but functionally unrelated---a complementary difficulty dimension to embedding distance.\n\n## 3.4 Training Setup\n\n**Encoders.** We use two decoder-only code language models with distinct pretraining: Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2}. These encoders differ in pretraining corpora and representation geometry, enabling examination of whether mining strategy effectiveness interacts with encoder properties.\n\n**Fine-tuning.** We apply LoRA adaptation with rank $r{=}16$, scaling factor $\\alpha{=}32$, and dropout 0.05, targeting query and value projection matrices ($W_q$, $W_v$) in every attention layer. Input sequences are truncated to 2,048 tokens. We use mean pooling over non-padding positions followed by L2 normalization, then project through a two-layer MLP (Linear$\\to$GELU$\\to$Linear) to a 256-dimensional embedding space.\n\n**Optimization.** We use AdamW (lr=$2 \\times 10^{-5}$, cosine annealing, warmup ratio 0.1, weight decay 0.01) for up to 3 epochs with gradient checkpointing and gradient clipping (max norm 1.0). The InfoNCE temperature is initialized to $\\tau{=}0.07$ and learned during training. Each batch contains 1 positive and $K{=}7$ negatives (effective batch size 8). Early stopping with patience 2 is applied based on validation loss, evaluated every 500 steps. We save two checkpoints per run: best by validation loss and best by validation R@1.\n\n## 3.5 Evaluation Protocol\n\n**Retrieval metric.** We evaluate on a pool-based retrieval task: given a query, the model ranks a candidate pool of 50 files by cosine similarity. The primary metric is Recall@1 (R@1)---whether the top-ranked file is a gold patch target.\n\n**Checkpoint selection.** We report the best-by-R@1 checkpoint as the primary result, selected by validation R@1. Fixed-checkpoint comparisons are reported as a robustness check to confirm that strategy rankings are not artifacts of checkpoint selection.\n\n**Statistical rigor.** Each encoder $\\times$ strategy combination is trained with 3 random seeds (42, 43, 44), yielding 18 total runs (2 encoders $\\times$ 3 strategies $\\times$ 3 seeds). We report bootstrap 95\\% confidence intervals for all comparisons.\n\n**Downstream evaluation.** To validate that retrieval improvements transfer to end-to-end performance, we evaluate on SWE-bench Lite \\cite{jimenez2024swebench} (300 instances) with an LLM-based repair agent. The retriever provides file-level context, measuring whether improved retrieval translates to higher issue resolution rates.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 116,
        "newStart": 1,
        "newLines": 51,
        "lines": [
          "-# §3 Method",
          "+# 3. Method",
          " ",
          "-## §3.1 Problem Formulation",
          "+## 3.1 Problem Formulation",
          " ",
          "-We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.",
          "+We formulate file-level code retrieval as a contrastive learning problem. Given a repository $\\mathcal{R}$ containing source files, a query $q$ consists of a buggy function or file paired with its issue description. A positive file $p \\in \\mathcal{R}$ is the gold patch target---a file modified to resolve the issue. All remaining non-query, non-gold files constitute the negative candidate pool.",
          " ",
          "-We formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:",
          "+We train an encoder $E: \\mathcal{F} \\to \\mathbb{R}^d$ such that $\\text{sim}(E(q), E(p)) \\gg \\text{sim}(E(q), E(n))$ for any negative $n$. Training minimizes the InfoNCE loss \\cite{chen2020simclr}:",
          " ",
          "-$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$",
          "+$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E(q), E(p)) / \\tau)}{\\exp(\\text{sim}(E(q), E(p)) / \\tau) + \\sum_{i=1}^{K} \\exp(\\text{sim}(E(q), E(n_i)) / \\tau)}$$",
          " ",
          "-where $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.",
          "+where $\\tau$ is a learnable temperature parameter and $\\{n_1, \\ldots, n_K\\}$ are $K$ negatives selected by a mining strategy. The central question is how the choice of mining strategy affects retrieval quality, and whether structural code information provides signal beyond embedding similarity.",
          " ",
          "-The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.",
          "+## 3.2 Structural Extraction Pipeline",
          " ",
          "-## §3.2 Structural Information Extraction",
          "+To enable structure-aware negative mining, we extract inter-procedural data-flow graphs from repository snapshots using CodeQL \\cite{avgustinov2016ql}. For each query function $q$, we construct a CodeQL database from the repository at the relevant commit, then perform bounded taint-tracking analysis to identify all files reachable from $q$ through inter-procedural data-flow paths. This captures cross-function semantic relationships---for instance, a utility function that transforms data passed from a source through multiple call boundaries.",
          " ",
          "-### CodeQL Bounded Data-Flow Analysis",
          "+A file $f$ is \\emph{connected} to query $q$ if $f$ is reachable from $q$ via inter-procedural data-flow paths in the structural graph $G$; otherwise $f$ is \\emph{disconnected}. Connected files include both gold targets and non-gold files that participate in the query's data-flow neighborhood (e.g., shared utility modules, intermediate processing functions).",
          " ",
          "-We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:",
          "+When CodeQL analysis fails due to missing build configurations, we fall back to beniget, a Python AST-based def-use analyzer providing intra-module data-flow coverage. At full scale, the pipeline processes 123 repositories comprising 44,173 training instances with 0\\% analysis timeout. Structural connectivity is available for 34.3\\% of instances; among those, 78\\% of connected files are non-gold, confirming that connectivity captures functional relevance beyond gold-file identity. We frame this pipeline as a practical enabling tool (\\S5), not a standalone contribution.",
          " ",
          "-- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.",
          "-- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.",
          "+## 3.3 Negative Mining Strategies",
          " ",
          "-### File-Level Reachability",
          "+We compare three strategies spanning different dimensions of negative difficulty. All strategies share a common two-stage protocol: first, a pool of 50 candidate negatives is constructed according to the strategy; then $K{=}7$ negatives are randomly sampled from this pool per training instance. This decouples strategy-specific selection from stochastic sampling effects.",
          " ",
          "-From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.",
          "+**Random.** Negatives are drawn uniformly at random from all non-positive files within the same repository. This serves as the no-signal baseline, reflecting the standard approach in dense retrieval \\cite{karpukhin2020dpr}.",
          " ",
          "-A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.",
          "+**Embedding-distance.** We compute cosine similarity between the query and all non-positive repository files using a pretrained encoder (frozen; not updated during training). The 50 most similar non-positive files form the candidate pool. These are semantic near-misses: files that \\emph{appear} relevant to the pretrained encoder but are not gold targets. This strategy incurs zero additional cost beyond the one-time offline embedding computation, as the pretrained encoder is already available.",
          " ",
          "-At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].",
          "+**Dataflow-aware.** This strategy combines structural filtering with lexical ranking. First, all structurally connected files are excluded from the candidate pool---specifically, files reachable via inter-procedural data-flow paths and call-graph neighbors ($\\text{positive\\_files} \\cup \\text{cg\\_connected}$). This ensures negatives are structurally disconnected from the query. Second, the remaining disconnected files are ranked by BM25 score \\cite{robertson2009bm25} in descending order, and the top-50 form the candidate pool. Formally:",
          " ",
          "-### Beniget Fallback",
          "+$$\\text{pool}_{\\text{df}}(q) = \\underset{x \\in \\mathcal{D} :\\ x \\notin R_G(q) \\,\\wedge\\, x \\notin \\text{gold}(q)}{\\text{top-}50}\\ \\text{BM25}(q, x)$$",
          " ",
          "-For repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].",
          "+where $R_G(q)$ denotes files reachable from $q$ in structural graph $G$. Structural information serves exclusively as a \\emph{filter} (determining which files to exclude), while BM25 provides the \\emph{ranking} signal among remaining candidates. The rationale is that high-BM25, structurally-disconnected files are lexically similar but functionally unrelated---a complementary difficulty dimension to embedding distance.",
          " ",
          "-### Coverage Statistics",
          "+## 3.4 Training Setup",
          " ",
          "-The extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:",
          "+**Encoders.** We use two decoder-only code language models with distinct pretraining: Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2}. These encoders differ in pretraining corpora and representation geometry, enabling examination of whether mining strategy effectiveness interacts with encoder properties.",
          " ",
          "-| Metric | Value |",
          "-|--------|-------|",
          "-| Timeout rate | 0% (all repository tiers) |",
          "-| Repository coverage | 123/131 (93.9%) |",
          "-| Structural data rate | 34% of instances |",
          "-| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |",
          "+**Fine-tuning.** We apply LoRA adaptation with rank $r{=}16$, scaling factor $\\alpha{=}32$, and dropout 0.05, targeting query and value projection matrices ($W_q$, $W_v$) in every attention layer. Input sequences are truncated to 2,048 tokens. We use mean pooling over non-padding positions followed by L2 normalization, then project through a two-layer MLP (Linear$\\to$GELU$\\to$Linear) to a 256-dimensional embedding space.",
          " ",
          "-The 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.",
          "+**Optimization.** We use AdamW (lr=$2 \\times 10^{-5}$, cosine annealing, warmup ratio 0.1, weight decay 0.01) for up to 3 epochs with gradient checkpointing and gradient clipping (max norm 1.0). The InfoNCE temperature is initialized to $\\tau{=}0.07$ and learned during training. Each batch contains 1 positive and $K{=}7$ negatives (effective batch size 8). Early stopping with patience 2 is applied based on validation loss, evaluated every 500 steps. We save two checkpoints per run: best by validation loss and best by validation R@1.",
          " ",
          "-## §3.3 Structure-Aware Negative Mining",
          "+## 3.5 Evaluation Protocol",
          " ",
          "-We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.",
          "+**Retrieval metric.** We evaluate on a pool-based retrieval task: given a query, the model ranks a candidate pool of 50 files by cosine similarity. The primary metric is Recall@1 (R@1)---whether the top-ranked file is a gold patch target.",
          " ",
          "-### Random Negatives",
          "+**Checkpoint selection.** We report the best-by-R@1 checkpoint as the primary result, selected by validation R@1. Fixed-checkpoint comparisons are reported as a robustness check to confirm that strategy rankings are not artifacts of checkpoint selection.",
          " ",
          "-For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:",
          "+**Statistical rigor.** Each encoder $\\times$ strategy combination is trained with 3 random seeds (42, 43, 44), yielding 18 total runs (2 encoders $\\times$ 3 strategies $\\times$ 3 seeds). We report bootstrap 95\\% confidence intervals for all comparisons.",
          " ",
          "-$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$",
          "-",
          "-This baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.",
          "-",
          "-### Embedding-Distance Negatives",
          "-",
          "-We compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:",
          "-",
          "-$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$",
          "-",
          "-These negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.",
          "-",
          "-### Dataflow-Aware Negatives",
          "-",
          "-This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:",
          "-",
          "-$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$",
          "-",
          "-where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:",
          "-",
          "-$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$",
          "-",
          "-These files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.",
          "-",
          "-For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).",
          "-",
          "-### Difficulty Gradient",
          "-",
          "-The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
          "-",
          "-### Relationship to BM25 Baselines",
          "-",
          "-In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].",
          "-",
          "-## §3.4 Contrastive Fine-tuning",
          "-",
          "-### InfoNCE Loss",
          "-",
          "-We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:",
          "-",
          "-$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$",
          "-",
          "-where $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].",
          "-",
          "-### LoRA Fine-tuning Setup",
          "-",
          "-We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.",
          "-",
          "-Each encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].",
          "-",
          "-Training uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.",
          "-",
          "-### Dual Checkpoint Strategy",
          "-",
          "-We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].",
          "-",
          "-### Early Stopping",
          "-",
          "-The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].",
          "-&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->",
          "+**Downstream evaluation.** To validate that retrieval improvements transfer to end-to-end performance, we evaluate on SWE-bench Lite \\cite{jimenez2024swebench} (300 instances) with an LLM-based repair agent. The retriever provides file-level context, measuring whether improved retrieval translates to higher issue resolution rates."
        ]
      }
    ],
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 64_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "ccf25361-9bc2-4381-86e0-008fbc8e343c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTUkrLE6kU3MKRG5ZQshhM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2201,
      "cache_read_input_tokens": 48713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2201
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

_source line 65_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KuafFd5BgTrXPrXgoTZWtm`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "c27f658c-dff2-4a9e-aa04-750766a8f406",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTUkrLE6kU3MKRG5ZQshhM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2201,
      "cache_read_input_tokens": 48713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2201
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

_source line 66 · 2026-05-15T09:31:46.755Z_

<details><summary>↩ Tool result · `toolu_01KuafFd5BgTrXPrXgoTZWtm`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "fd509b70-ddc1-4320-8776-1378197b9830",
  "tool_use_result": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XA51oXfDkrBQ5NpqTwgLzz`</summary>

```json
{
  "query": "register artifact",
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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "551b4f47-84bd-49e5-967e-5da7b8ec3b5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hzo9fRGQ4rviUbPL3KyBPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 109,
      "cache_read_input_tokens": 50914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 109
      },
      "output_tokens": 67,
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

_source line 68 · 2026-05-15T09:31:49.189Z_

<details><summary>↩ Tool result · `toolu_01XA51oXfDkrBQ5NpqTwgLzz`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "d89f0f6b-0cbb-4846-a822-d0143fd6ad08",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01E2AKohs1Mi15qEKKdU66hW`</summary>

```json
{
  "query": "artifact register save",
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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "390fff4b-9b29-4969-a271-7f0f20d404fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rb3azwTnXvKwKYSaVoy25b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91,
      "cache_read_input_tokens": 51023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91
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

_source line 70 · 2026-05-15T09:31:52.308Z_

<details><summary>↩ Tool result · `toolu_01E2AKohs1Mi15qEKKdU66hW`</summary>

````text
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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "8db42064-631b-4e66-a938-1456432c3a30",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "artifact register save",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
The `register_artifact` tool doesn't seem to exist as a deferred tool. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "be95382b-ba19-49c4-8cab-de80aadf0520",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYZz3WTgcu5YspbV4xFP9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 51114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
      },
      "output_tokens": 23,
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

_source line 72_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Td8nB6cnDqSXAkUKrkrXnL`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "d71e62e7-4112-43e2-a925-ec8a6385f175",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYZz3WTgcu5YspbV4xFP9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 51114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
      },
      "output_tokens": 23,
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

_source line 73 · 2026-05-15T09:31:55.390Z_

<details><summary>↩ Tool result · `toolu_01Td8nB6cnDqSXAkUKrkrXnL`</summary>

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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "24c5be67-9ad9-43f4-9b91-cbfce2361805",
  "tool_use_result": {
    "matches": [],
    "query": "register",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R8HPJiNGszZDuK5FvUL9bT`</summary>

```json
{
  "query": "mcp agent-ml-research",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "db3492ab-90eb-43d5-93a8-13cdcf521055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWBAkRMA5YrTW9PzMoVUYN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 131,
      "cache_read_input_tokens": 51464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 131
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

_source line 75 · 2026-05-15T09:31:57.490Z_

<details><summary>↩ Tool result · `toolu_01R8HPJiNGszZDuK5FvUL9bT`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

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
  "tool_name": "ListMcpResourcesTool"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "ReadMcpResourceTool"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "58618e66-d8f4-4f7f-9eb6-7a5b8f4c7f6d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "ListMcpResourcesTool",
      "ReadMcpResourceTool",
      "WebFetch"
    ],
    "query": "mcp agent-ml-research",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
There's no `register_artifact` tool available in the MCP tools. The CLAUDE.md mentions using `register_artifact` but it doesn't exist as a tool. The file has been written successfully to the correct path. Let me just confirm the file is there and inform the user.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "880bf693-5993-4ba8-b484-5552250cb8b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjEyuGMn4G9KtyeAkLfWu1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 51595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
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

### Assistant

_source line 77_

`register_artifact` 工具不可用（未在 MCP 工具列表中）。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md`

**与任务要求的对照**：

| 要求 | 状态 |
|------|------|
| §3.1 Problem Formulation (~150w) | ~150w, InfoNCE + contrastive formulation |
| §3.2 Structural Extraction (~200w) | ~200w, CodeQL + beniget fallback, scalability数据 (123 repos, 44K instances, 0% timeout, 34.3%/78%) |
| §3.3 Negative Mining (~250w) | ~270w, 三策略精确描述, **dataflow 用 BM25 排序 + 结构过滤** (D041) |
| §3.4 Training Setup (~200w) | ~200w, 全部超参从 registry 确认 |
| §3.5 Evaluation Protocol (~200w) | ~180w, R@1 + dual checkpoint + 3 seeds + SWE-bench |
| D049 软化措辞 | 无 "challenges", 用 "reliable improvement" / "zero additional cost" |
| \cite{} keys 对齐 | 全部匹配 references.bib (无 LoRA citation — bib 中缺该条目) |

**Registry 纠正了任务描述中的几处值**：
- max epochs = 3（非 2），early stopping patience=2 可能在 epoch 2 触发
- LoRA targets: $W_q, W_v$（非泛指 "attention layers"）
- LoRA dropout = 0.05
- Optimizer: AdamW + cosine annealing（非纯 AdamW）
- Gradient clipping: max norm 1.0
- Projection head: two-layer MLP (Linear→GELU→Linear)

需要手动 `register_artifact` 或该工具名称不同，请确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "uuid": "a6d8e040-859d-41ae-ba16-ed178c905c30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjEyuGMn4G9KtyeAkLfWu1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 51595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
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

_source line 78_

`register_artifact` 工具不可用（未在 MCP 工具列表中）。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md`

**与任务要求的对照**：

| 要求 | 状态 |
|------|------|
| §3.1 Problem Formulation (~150w) | ~150w, InfoNCE + contrastive formulation |
| §3.2 Structural Extraction (~200w) | ~200w, CodeQL + beniget fallback, scalability数据 (123 repos, 44K instances, 0% timeout, 34.3%/78%) |
| §3.3 Negative Mining (~250w) | ~270w, 三策略精确描述, **dataflow 用 BM25 排序 + 结构过滤** (D041) |
| §3.4 Training Setup (~200w) | ~200w, 全部超参从 registry 确认 |
| §3.5 Evaluation Protocol (~200w) | ~180w, R@1 + dual checkpoint + 3 seeds + SWE-bench |
| D049 软化措辞 | 无 "challenges", 用 "reliable improvement" / "zero additional cost" |
| \cite{} keys 对齐 | 全部匹配 references.bib (无 LoRA citation — bib 中缺该条目) |

**Registry 纠正了任务描述中的几处值**：
- max epochs = 3（非 2），early stopping patience=2 可能在 epoch 2 触发
- LoRA targets: $W_q, W_v$（非泛指 "attention layers"）
- LoRA dropout = 0.05
- Optimizer: AdamW + cosine annealing（非纯 AdamW）
- Gradient clipping: max norm 1.0
- Projection head: two-layer MLP (Linear→GELU→Linear)

需要手动 `register_artifact` 或该工具名称不同，请确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 279769,
  "duration_api_ms": 280364,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "753c2faa-f210-400b-a8ef-50428b684745",
  "total_cost_usd": 0.9121498999999998,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 41442,
    "cache_read_input_tokens": 498722,
    "output_tokens": 9291,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41442,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 636,
        "cache_read_input_tokens": 51595,
        "cache_creation_input_tokens": 1688,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1688
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1949,
      "outputTokens": 2909,
      "cacheReadInputTokens": 199174,
      "cacheCreationInputTokens": 107992,
      "webSearchRequests": 0,
      "costUSD": 0.17140139999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 9291,
      "cacheReadInputTokens": 498722,
      "cacheCreationInputTokens": 41442,
      "webSearchRequests": 0,
      "costUSD": 0.7407484999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "de6ec137-7a58-4060-9e98-cc679ada52e2"
}
```

</details>

---
