# writing abstract v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_writing_abstract-v1_20260515T102508.log`
- **Structured JSON:** [`cc920790984a4af269b3.json`](../../sessions/cc/cc920790984a4af269b3.json)

## Before a recorded user message

27 recorded events

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
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
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
  "uuid": "d07738e8-57ed-4c3d-a251-f248fe5e4195",
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
  "uuid": "f7644c23-5dc0-485d-bfc4-608921caba8d",
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me first read the project's existing files to understand the context better, then write the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "44a84dd3-4d37-4472-bcd6-d8e0d423d993",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar3XQ3NEAKFkmyv4SFEcBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11349,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11349
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

### Assistant

_source line 5_

Let me check existing project files for context before drafting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "d87f6826-e83c-4dab-8c37-bb23357bad5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar3XQ3NEAKFkmyv4SFEcBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11349,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11349
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012UkvTBebQFfUsFXaBPFCcJ`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "cc9fb699-7d2c-46a2-817b-1d6d5613db78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar3XQ3NEAKFkmyv4SFEcBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11349,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11349
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

_source line 7 · 2026-05-15T10:25:20.802Z_

<details><summary>↩ Tool result · `toolu_012UkvTBebQFfUsFXaBPFCcJ`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "550ab2da-6f61-4dce-ac17-e09acc08090e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01H6Ah5W1hd8NrGkFEobqep3`</summary>

```json
{
  "pattern": "artifacts/paper_drafts/**",
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
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "8379638f-b14f-4b46-90b6-6511f9305e43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar3XQ3NEAKFkmyv4SFEcBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11349,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11349
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

_source line 9 · 2026-05-15T10:25:21.123Z_

<details><summary>↩ Tool result · `toolu_01H6Ah5W1hd8NrGkFEobqep3`</summary>

```text
artifacts/paper_drafts/experimental_setup_k_checkpoint.md
artifacts/paper_drafts/figure_design_v1.md
artifacts/paper_drafts/claim2_wording_review.md
artifacts/paper_drafts/bm25_code_review.md
artifacts/paper_drafts/discussion_v2.md
artifacts/paper_drafts/introduction_v2.md
artifacts/paper_drafts/experiment_setup_v1.md
artifacts/paper_drafts/experiments_v1.md
artifacts/paper_drafts/related_work_supplement.md
artifacts/paper_drafts/checkpoint_criterion_table.tex
artifacts/paper_drafts/fixed_checkpoint_table.tex
artifacts/paper_drafts/discussion_valloss_divergence.md
artifacts/paper_drafts/introduction_v1.md
artifacts/paper_drafts/method_v1.md
artifacts/paper_drafts/related_work_v1.md
artifacts/paper_drafts/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "8a7f9a6e-61c1-4553-a932-ab98891887bc",
  "tool_use_result": {
    "filenames": [
      "artifacts/paper_drafts/experimental_setup_k_checkpoint.md",
      "artifacts/paper_drafts/figure_design_v1.md",
      "artifacts/paper_drafts/claim2_wording_review.md",
      "artifacts/paper_drafts/bm25_code_review.md",
      "artifacts/paper_drafts/discussion_v2.md",
      "artifacts/paper_drafts/introduction_v2.md",
      "artifacts/paper_drafts/experiment_setup_v1.md",
      "artifacts/paper_drafts/experiments_v1.md",
      "artifacts/paper_drafts/related_work_supplement.md",
      "artifacts/paper_drafts/checkpoint_criterion_table.tex",
      "artifacts/paper_drafts/fixed_checkpoint_table.tex",
      "artifacts/paper_drafts/discussion_valloss_divergence.md",
      "artifacts/paper_drafts/introduction_v1.md",
      "artifacts/paper_drafts/method_v1.md",
      "artifacts/paper_drafts/related_work_v1.md",
      "artifacts/paper_drafts/references.bib"
    ],
    "durationMs": 8,
    "numFiles": 16,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Let me read the paper_framing.md and some key existing drafts to ensure the abstract aligns with the project's framing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "cfa738a6-0af7-4f36-88d7-ceac94ee01e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AAKPCu6pDwUeiTGx85yLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 851
      },
      "output_tokens": 20,
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SafofnyPwUbKw72ASX4D5G`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "eab77b9b-fe30-423a-a348-aa979a9dfc52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AAKPCu6pDwUeiTGx85yLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 851
      },
      "output_tokens": 20,
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

_source line 12 · 2026-05-15T10:25:27.329Z_

<details><summary>↩ Tool result · `toolu_01SafofnyPwUbKw72ASX4D5G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results we\\n\\n... [截断: 省略 2424 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 14424, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "336e71da-3d9f-4f2a-87f0-b1e82db1b68d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — StructFuse\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3)\\\\n\\\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\\\\\"slow and ineffective\\\\\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\\\n\\\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\\\n\\\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\\\n\\\\n- **Existing approaches & gaps**:\\\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\\\n\\\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\\\n\\\\n- **Headline result template**: \\\\\\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\\\n\\\\n## Dual-Pillar Motivation\\\\n\\\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\\\n\\\\n## Formal Definition\\\\n\\\\nGiven retrieval domain D, structural graph G, query q:\\\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\\\n\\\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\\\n\\\\n## Title Options\\\\n\\\\n- Primary: \\\\\\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\\\\\"\\\\n- Alternative: \\\\\\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\\\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\\\n- Backup: \\\\\\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n\\\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\\\\\"Do Language Models...\\\\\\\" papers). Contribution is understanding, not just a new method.\\\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\\\n3. **Against \\\\\\\"incremental\\\\\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response | Evidence |\\\\n|---------|----------|----------|\\\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\\\n| \\\\\\\"Complementary signal\\\\\\\" overstatement | Temper: \\\\\\\"conditionally beneficial\\\\\\\" not \\\\\\\"always complementary\\\\\\\" | Writing discipline |\\\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\\\n\\\\n## Evidence Status\\\\n\\\\n### Confirmed findings (basis for claims):\\\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\\\n\\\\n### Evidence presentation strategy:\\\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\\\n\\\\n### In progress:\\\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\\\n\\\\n### Planned (priority order):\\\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\\\n- plan_014: Temperature ablation (Dream reviewer concern)\\\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\\\n- plan_015: Dynamic mining baseline\\\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\\\n- plan_007/008/009: Additional ablations\\\\n\\\\n## Limitations\\\\n\\\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\\\n\\\\n## Contingency (if full M2 results we\\\\n\\\\n... [截断: 省略 2424 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 14424, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results we\\n\\n... [截断: 省略 2424 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 14424, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01Uhpvo4BRUvAZXMDz4QQSNG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "c19706b0-72e6-46ba-8260-08f003c23111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AAKPCu6pDwUeiTGx85yLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 851
      },
      "output_tokens": 20,
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

_source line 14 · 2026-05-15T10:25:27.474Z_

<details><summary>↩ Tool result · `toolu_01Uhpvo4BRUvAZXMDz4QQSNG`</summary>

```text
1	# 1. Introduction
2	
3	Code retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \cite{liu2024repobench}, fault localization \cite{chen2025locagent}, and automated program repair \cite{jimenez2024swebench}.
4	Contrastive learning has become the dominant paradigm for training dense code retrievers \cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \cite{chen2020simclr,xiong2021ance}.
5	Despite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.
6	As retrieval scales to repository-level settings with hundreds of candidate files \cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.
7	
8	Existing negative selection approaches span a broad spectrum but leave a critical gap.
9	Random negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \cite{karpukhin2020dpr}.
10	Embedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.
11	CoCoHaNeRe \cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.
12	Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.
13	Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.
14	
15	We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
16	Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
17	We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.
18	All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.
19	
20	Our experiments on CodeSearchNet \cite{husain2019codesearchnet} yield three principal findings.
21	First, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \cite{fan2025cocohanere}.
22	Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).
23	Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.
24	
25	Our contributions are as follows:
26	\begin{enumerate}
27	\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.
28	\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
29	\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
30	\end{enumerate}
31	
32	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
33	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "cba4126f-b20a-4e44-bdbe-bb3ac611608d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
      "content": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper framing and introduction. Let me draft the abstract following the requirements:

- 200-250 words
- Structure: Problem → Method → Key findings → Significance
- Numbers as placeholders
- Follow the framing constraints (D049 softened claims)
- Title: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

Let me draft it now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "740f96ad-1b43-40f6-a413-2b137427c5d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbfNmX5D7WuADPqTt3j7i6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5021,
      "cache_read_input_tokens": 24041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5021
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

_source line 16_

Now I have enough context. Let me draft the abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "a6ee53ae-1f41-44ee-ba19-9f58aeaad9f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbfNmX5D7WuADPqTt3j7i6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5021,
      "cache_read_input_tokens": 24041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5021
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

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_019vD6aF4iZoGitpjci4aZMR`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/",
  "description": "Check paper_drafts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "09f72dc7-2380-4834-8faa-eebd8e930099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbfNmX5D7WuADPqTt3j7i6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5021,
      "cache_read_input_tokens": 24041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5021
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

_source line 18 · 2026-05-15T10:25:35.328Z_

<details><summary>↩ Tool result · `toolu_019vD6aF4iZoGitpjci4aZMR`</summary>

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
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "c85ab7d6-08d6-4de6-b7d8-a6d530912676",
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

_source line 19_

<details open><summary>🔧 Tool call — Write · `toolu_01XMVxw4f77bTY7NiMpBHDeg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/abstract_v1.md",
  "content": "# Abstract\n\n**What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry**\n\nHard negative mining is critical for training contrastive code retrievers, yet the field lacks systematic understanding of which mining strategies work and why. Prior work argues that non-differentiable embedding negatives are ineffective compared to gradient-based alternatives, but this claim has not been evaluated under controlled conditions in structural code retrieval settings. Meanwhile, code's rich structural properties—call graphs, data-flow dependencies—remain entirely unexploited for negative selection.\n\nWe conduct a controlled comparison of three hard negative mining strategies for repository-level code retrieval: random sampling, static embedding-distance mining, and dataflow-aware mining guided by inter-procedural data-flow analysis via CodeQL. All experiments use identical training pipelines across two decoder-only encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with X random seeds each, enabling analysis of strategy–encoder interactions.\n\nWe report three findings. First, static embedding-distance mining provides a reliable retrieval improvement over random baselines (+X.X pp Recall@1 averaged across encoders and seeds) at zero additional computational cost, establishing a strong baseline for future work. Second, as a preliminary observation, dataflow-aware negatives do not consistently outperform embedding mining but exhibit an encoder-dependent interaction pattern: negative difficulty margin analysis suggests that encoder representation geometry—specifically, the degree of embedding space saturation—may mediate strategy effectiveness. Third, our CodeQL-based pipeline scales to X repositories with 0% timeout rate, demonstrating that structure-grounded negative mining is practically feasible at scale. All improvements are training-time interventions with zero inference overhead, validated on downstream SWE-bench Lite evaluation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "7ac8c393-1371-4d0c-af67-eb2bb4684829",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KiKVm8NFbrJZrKrWkjhbzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 29062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
      },
      "output_tokens": 51,
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

_source line 20 · 2026-05-15T10:25:47.576Z_

<details><summary>↩ Tool result · `toolu_01XMVxw4f77bTY7NiMpBHDeg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/abstract_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "003db994-9ead-4347-a6cd-e5185fc81199",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/abstract_v1.md",
    "content": "# Abstract\n\n**What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry**\n\nHard negative mining is critical for training contrastive code retrievers, yet the field lacks systematic understanding of which mining strategies work and why. Prior work argues that non-differentiable embedding negatives are ineffective compared to gradient-based alternatives, but this claim has not been evaluated under controlled conditions in structural code retrieval settings. Meanwhile, code's rich structural properties—call graphs, data-flow dependencies—remain entirely unexploited for negative selection.\n\nWe conduct a controlled comparison of three hard negative mining strategies for repository-level code retrieval: random sampling, static embedding-distance mining, and dataflow-aware mining guided by inter-procedural data-flow analysis via CodeQL. All experiments use identical training pipelines across two decoder-only encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with X random seeds each, enabling analysis of strategy–encoder interactions.\n\nWe report three findings. First, static embedding-distance mining provides a reliable retrieval improvement over random baselines (+X.X pp Recall@1 averaged across encoders and seeds) at zero additional computational cost, establishing a strong baseline for future work. Second, as a preliminary observation, dataflow-aware negatives do not consistently outperform embedding mining but exhibit an encoder-dependent interaction pattern: negative difficulty margin analysis suggests that encoder representation geometry—specifically, the degree of embedding space saturation—may mediate strategy effectiveness. Third, our CodeQL-based pipeline scales to X repositories with 0% timeout rate, demonstrating that structure-grounded negative mining is practically feasible at scale. All improvements are training-time interventions with zero inference overhead, validated on downstream SWE-bench Lite evaluation.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01MYP5Nvg1NjLmnWoRQtfzHh`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/abstract_v1.md | awk '{print $1 - 2}'",
  "description": "Count words excluding title header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "f333acaf-9f26-4c65-bbe0-de2c0b438619",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJNBRfDQWYXUMupt92Aeia",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 562,
      "cache_read_input_tokens": 29447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 562
      },
      "output_tokens": 65,
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

_source line 22 · 2026-05-15T10:25:50.679Z_

<details><summary>↩ Tool result · `toolu_01MYP5Nvg1NjLmnWoRQtfzHh`</summary>

```text
244
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "6ef429c7-b684-42a4-b26a-35469e9f831e",
  "tool_use_result": {
    "stdout": "244",
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

_source line 23_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "8b6236ac-f23d-4a04-a3d8-1a9996b23b83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCPQXKkUCr34aRzVfnuc7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 142,
      "cache_read_input_tokens": 30009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 142
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

_source line 24_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BpVhLK6VvRaZzJ9X8bxwTH`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "0c4ce2af-8dce-48ba-b061-ed45389cab8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCPQXKkUCr34aRzVfnuc7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 142,
      "cache_read_input_tokens": 30009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 142
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

_source line 25 · 2026-05-15T10:25:56.528Z_

<details><summary>↩ Tool result · `toolu_01BpVhLK6VvRaZzJ9X8bxwTH`</summary>

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
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "51d5cfa3-2f87-46d0-a90f-e5fe355f1da2",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 26_

Abstract v1 已保存，244 词。结构：问题 → 方法 → 三条发现 → 意义。

要点确认：
- Claim 1 用 "reliable improvement at zero additional computational cost"，不用 "significant"
- Claim 2 用 "preliminary observation" + "may mediate"，exploratory 措辞
- Claim 3 定位为 practical pipeline，非 standalone contribution
- 数值全部占位符（+X.X pp, X repositories, X seeds）
- 末尾点明 training-time intervention + zero inference overhead + SWE-bench validation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "uuid": "52fa699e-fad6-4181-a8a1-46ecd152bd7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWZkuR4jKn98hw3VA9evvE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 30151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 473
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

### Task result

_source line 27_

Abstract v1 已保存，244 词。结构：问题 → 方法 → 三条发现 → 意义。

要点确认：
- Claim 1 用 "reliable improvement at zero additional computational cost"，不用 "significant"
- Claim 2 用 "preliminary observation" + "may mediate"，exploratory 措辞
- Claim 3 定位为 practical pipeline，非 standalone contribution
- 数值全部占位符（+X.X pp, X repositories, X seeds）
- 末尾点明 training-time intervention + zero inference overhead + SWE-bench validation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 48675,
  "duration_api_ms": 50328,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "22a0f8fc-e40b-4336-8a3e-df3e292e9b2b",
  "total_cost_usd": 0.24719524999999998,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 18783,
    "cache_read_input_tokens": 177741,
    "output_tokens": 1583,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18783,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 161,
        "cache_read_input_tokens": 30151,
        "cache_creation_input_tokens": 473,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 473
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1226,
      "outputTokens": 13,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001291,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 1583,
      "cacheReadInputTokens": 177741,
      "cacheCreationInputTokens": 18783,
      "webSearchRequests": 0,
      "costUSD": 0.24590425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b61ec818-2f44-4182-beeb-cb830df9e3c8"
}
```

</details>

---
