# paper writing conclusion

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_writing_conclusion_20260514T112339.log`
- **Structured JSON:** [`7918d30a358bb1b8d4db.json`](../../sessions/79/7918d30a358bb1b8d4db.json)

## Before a recorded user message

31 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "67597bde-9368-4a4d-b913-34775702af24",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779303600,
    "rateLimitType": "seven_day",
    "utilization": 0.33,
    "isUsingOverage": false
  },
  "uuid": "da834e61-c40e-481d-820a-db6f381b97dc",
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by gathering all the necessary information to write the Conclusion section. I need to:

1. Read paper_framing.md
2. List artifacts to find existing paper sections
3. Read the registry for key data

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "2331e986-0a73-4f88-a93d-080344f4349f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvUJ3NXH6Aq3baGcbJc1t6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11533,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11533
      },
      "output_tokens": 32,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UEjhznGCpq5DVZ4ijebi9e`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
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
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "92122273-d8f8-4333-88d0-e43131f7eac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvUJ3NXH6Aq3baGcbJc1t6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11533,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11533
      },
      "output_tokens": 32,
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

_source line 6 · 2026-05-14T11:23:50.455Z_

<details><summary>↩ Tool result · `toolu_01UEjhznGCpq5DVZ4ijebi9e`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "215f64b2-a20d-4fa6-973e-fe1c7610d2a1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch all the necessary data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "4acd20be-9a62-4ca6-ab25-7c06ed87476c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsRcuvyoBHN1RwSSQ6VPmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 23374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1467
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JdAWNuypJDSrm6TPUqNsSe`</summary>

```json
{
  "project": "simgate-modular-routing",
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
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "abb21a0e-b161-4810-abf3-37bb077e1109",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsRcuvyoBHN1RwSSQ6VPmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 23374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1467
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

_source line 9 · 2026-05-14T11:23:54.657Z_

<details><summary>↩ Tool result · `toolu_01JdAWNuypJDSrm6TPUqNsSe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (11 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\\n\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\n\\n**D013 note**: C1 no longer claims \\\"selective > unconditional.\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\n\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\n\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\n\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\"we built a better tool selector\\\" papers.\\n\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\n\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\n\\n- **Headline result template**: \\\"Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just always use deterministic\\\"**\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\n\\n5. **\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\n\\n6. **\\\"ScienceWorld's -100 penalty inflates gains\\\"** (Dream all 3 tiers)\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\n\\n7. **\\\"Missing tool-use literature — this is just Toolformer\\\"** (Dream all 3 tiers, CRITICAL)\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\n\\n8. **\\\"Rule-based routing baseline missing\\\"** (Dream median + worst)\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\"structural failure analysis\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Death avoidance is the only signal\\\" may seem like a limited finding — mitigate by framing as \\\"this IS the insight\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\"structural failure analysis\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\\n## Robustness Check (30-task prescreening, appendix only)\\n\\nA broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.\\n\\n## 数据源权威声明\\n\\n- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用\\n- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix\\n- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）\\n- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）\\n\", \"total_chars\": 13390, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "a6f6990e-971f-4a52-9abd-d30faf2014fd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — simgate-modular-routing\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026 (11 days remaining)\\\\n\\\\n## Core Insight\\\\n\\\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\\\n\\\\n## Core Claims (2 claims for short paper)\\\\n\\\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\\\\n\\\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\\\n\\\\n**D013 note**: C1 no longer claims \\\\\\\"selective > unconditional.\\\\\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\\\n\\\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\\\n\\\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\\\n\\\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\\\\\"we built a better tool selector\\\\\\\" papers.\\\\n\\\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\\\n\\\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\\\n\\\\n- **Headline result template**: \\\\\\\"Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\\\\\"\\\\n\\\\n## Paper Structure (4-page short paper)\\\\n\\\\n| Section | Pages | Content |\\\\n|---------|-------|---------|\\\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\\\n| References | ~0.5 | Not counted in 4-page limit |\\\\n\\\\n## Anticipated Reviewer Concerns & Mitigations\\\\n\\\\n1. **\\\\\\\"Novelty is incremental — just SFT a small model to classify\\\\\\\"**\\\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\\\n\\\\n2. **\\\\\\\"Only one benchmark (ScienceWorld)\\\\\\\"**\\\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\\\n\\\\n3. **\\\\\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\\\\\"**\\\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\\\n\\\\n4. **\\\\\\\"Death avoidance is trivial — just always use deterministic\\\\\\\"**\\\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\\\n\\\\n5. **\\\\\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\\\\\"**\\\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\\\n\\\\n6. **\\\\\\\"ScienceWorld's -100 penalty inflates gains\\\\\\\"** (Dream all 3 tiers)\\\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\\\n\\\\n7. **\\\\\\\"Missing tool-use literature — this is just Toolformer\\\\\\\"** (Dream all 3 tiers, CRITICAL)\\\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\\\n\\\\n8. **\\\\\\\"Rule-based routing baseline missing\\\\\\\"** (Dream median + worst)\\\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\\\\\"structural failure analysis\\\\\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\\\n- Short paper format matches focused contribution scope\\\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\\\\\"Scope & Future Work\\\\\\\" paragraph\\\\n- Risk: \\\\\\\"Death avoidance is the only signal\\\\\\\" may seem like a limited finding — mitigate by framing as \\\\\\\"this IS the insight\\\\\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\\\\\"structural failure analysis\\\\\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\\\n\\\\n## Key Differences from IDEA_BRIEF\\\\n\\\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\\\n2. **Framing shifted**: From \\\\\\\"general routing to deterministic computation\\\\\\\" to \\\\\\\"safety-aware routing\\\\\\\" based on MVP death avoidance finding.\\\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\\\n4. **\\\\\\\"ANY form\\\\\\\" softened**: Per Human Review Note #4, \\\\\\\"across multiple forms\\\\\\\" instead of \\\\\\\"ANY form\\\\\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\\\n\\\\n## Robustness Check (30-task prescreening, appendix only)\\\\n\\\\nA broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.\\\\n\\\\n## 数据源权威声明\\\\n\\\\n- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用\\\\n- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix\\\\n- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）\\\\n- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）\\\\n\\\", \\\"total_chars\\\": 13390, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (11 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\\n\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\n\\n**D013 note**: C1 no longer claims \\\"selective > unconditional.\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\n\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\n\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\n\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\"we built a better tool selector\\\" papers.\\n\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\n\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\n\\n- **Headline result template**: \\\"Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just always use deterministic\\\"**\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\n\\n5. **\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\n\\n6. **\\\"ScienceWorld's -100 penalty inflates gains\\\"** (Dream all 3 tiers)\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\n\\n7. **\\\"Missing tool-use literature — this is just Toolformer\\\"** (Dream all 3 tiers, CRITICAL)\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\n\\n8. **\\\"Rule-based routing baseline missing\\\"** (Dream median + worst)\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\"structural failure analysis\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Death avoidance is the only signal\\\" may seem like a limited finding — mitigate by framing as \\\"this IS the insight\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\"structural failure analysis\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\\n## Robustness Check (30-task prescreening, appendix only)\\n\\nA broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.\\n\\n## 数据源权威声明\\n\\n- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用\\n- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix\\n- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）\\n- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）\\n\", \"total_chars\": 13390, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019SJVaguUbh1guF8sQDG7vZ`</summary>

```json
{
  "project": "simgate-modular-routing",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "31f68f67-746b-4f44-9bd8-a83eab47e299",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsRcuvyoBHN1RwSSQ6VPmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 23374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1467
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

_source line 11 · 2026-05-14T11:23:55.391Z_

<details><summary>↩ Tool result · `toolu_019SJVaguUbh1guF8sQDG7vZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan-004-ablation-b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:36:59.120Z\", \"updated_at\": \"2026-05-14T09:42:34.996Z\", \"hypothesis\": \"Plan-004 条件 (b) implicit router SFT：Qwen3-1.7B + LoRA, [SIMULATE] token 隐式路由。与 plan-002 (explicit router) 对比，验证路由 signal 是否需要显式分类器还是可通过 token 嵌入隐式学习。同样使用 upsample_minority 处理类别不平衡。\", \"parent\": \"plan-002-formal-v2\", \"conclusion\": \"success\", \"notes\": \"**训练实验 SUCCESS（非退化 router，internal_recall=51.52% > 30% 判定线）。e2e 部署效果 NEGATIVE 记录在 plan-003-e2e-ablation-b-correct。**\\n\\n4-seed generation-level 汇总（ga=8, upsample_minority）：\\n| Seed | balanced_acc | internal_recall | det_recall | accuracy |\\n|------|-------------|-----------------|------------|----------|\\n| 42   | 59.27%      | 51.52%          | 67.03%     | 65.36%   |\\n| 123  | 57.36%      | 57.58%          | 57.14%     | 57.19%   |\\n| 456  | 57.48%      | 75.76%          | 39.19%     | 43.14%   |\\n| 789  | 58.31%      | 81.82%          | 34.80%     | 39.87%   |\\n\\nbalanced_acc 均值 58.1±0.8%（仅比随机高 8pp）。internal_recall 波动（51-82%）是阈值效应。\\n\\n**论文定位（D033）**：Router near-random IS the finding → 强化 C1（death avoidance 主导到 router 无法从 episode-level labels 学到其他有效 signal）。\\n\\n原始 eval: accuracy=65.36%, balanced_acc=59.27%, zero logit-generation gap。Eval 脚本: eval_ablation_b_gen.py。\", \"metrics\": {\"logit_level\": {\"eval_accuracy\": 0.6536, \"eval_f1_macro\": 0.5091, \"eval_balanced_accuracy\": 0.5927, \"internal_recall\": 0.5152, \"per_class\": {\"deterministic\": {\"precision\": 0.9196, \"recall\": 0.6703, \"f1\": 0.7754, \"support\": 273}, \"internal\": {\"precision\": 0.1589, \"recall\": 0.5152, \"f1\": 0.2429, \"support\": 33}}, \"confusion\": {\"true_int_pred_int\": 17, \"true_int_pred_det\": 16, \"true_det_pred_det\": 183, \"true_det_pred_int\": 90}, \"training_loss_curve\": {\"epoch1\": 0.7151, \"epoch2\": 0.3928, \"epoch3\": 0.3609}}, \"generation_level\": {\"accuracy\": 0.6536, \"balanced_accuracy\": 0.5927, \"internal_recall\": 0.5152, \"internal_precision\": 0.1589, \"internal_f1\": 0.2429, \"det_recall\": 0.6703, \"det_precision\": 0.9196, \"det_f1\": 0.7754, \"confusion_matrix\": [[17, 16], [90, 183]], \"confusion_labels\": [\"internal\", \"deterministic\"], \"n_val\": 306, \"val_label_dist\": {\"internal\": 33, \"deterministic\": 273}, \"pred_dist\": {\"deterministic\": 199, \"internal\": 107}, \"enable_thinking\": false, \"logit_generation_gap\": 0, \"note\": \"Generation-level eval IDENTICAL to logit-level. Zero gap. Only model in project without logit-generation gap.\"}, \"is_degenerate\": false}}, \"plan-003-implicit-eval-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:27:09.398Z\", \"updated_at\": \"2026-05-14T09:27:37.907Z\", \"conclusion\": \"negative\", \"hypothesis\": \"Step-level implicit routing eval of ablation-b (plan-004-implicit/final_adapter) on 245 episodes / 11 tasks via eval_implicit_router.py. Score -12.84 worse than always-det baseline -9.47.\", \"metrics\": {\"continuous_score\": -12.84, \"ci_low\": -17.52, \"ci_high\": -8.45, \"success_rate\": 0.22, \"catastrophic_failure_rate\": 0.192, \"sim_invocation_ratio\": 0.941, \"step_routing_accuracy\": 0.602, \"episode_routing_accuracy\": 0.821, \"internal_recall\": 0.444, \"det_recall\": 0.86, \"routing_det\": 229, \"routing_internal\": 16, \"n_episodes\": 245, \"n_tasks\": 11, \"n_steps\": 2160, \"oracle_internal_preferred\": 9, \"oracle_det_preferred\": 86, \"oracle_no_preference\": 150}}, \"plan-003-e2e-ablation-b-correct\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:21:57.921Z\", \"updated_at\": \"2026-05-14T09:24:39.892Z\", \"metrics\": {\"continuous_score_mean\": -10.7, \"continuous_score_ci_low\": -15.25, \"continuous_score_ci_high\": -6.38, \"success_rate\": 0.2367, \"death_rate\": 0.1755, \"sim_ratio\": 0.9703, \"fallback_rate\": 0.7061, \"fallback_count\": 173, \"n_episodes\": 245, \"n_tasks\": 11, \"estimated_llm_tokens\": 1464400, \"baseline_always_det\": -9.47, \"baseline_oracle\": -6.58, \"delta_vs_always_det\": -1.23}, \"conclusion\": \"negative\", \"hypothesis\": \"End-to-end eval of ablation-b (correct checkpoint: plan-004-implicit/final_adapter, internal_recall=51.52%) on 245 episodes / 11 tasks. Test C1: trained-router > always-det (-9.47).\", \"notes\": \"**NEGATIVE: trained-router (-10.70) worse than always-det (-9.47) by 1.23 pts.**\\n\\n正确 checkpoint: checkpoints/plan-004-implicit/final_adapter (ablation-b seed42)。\\nCI [-15.25, -6.38] 包含 -9.47，差异不显著但 point estimate 更差。\\n\\n关键指标：\\n- sim_ratio=97.0% — router 几乎全部路由到 deterministic\\n- fallback_rate=70.6% — 173/245 episodes 无 step data，直接 fallback 到 deterministic\\n- death_rate=17.6%\\n- 唯一正分 task: find-non-living-thing (+28.68, 62.5% success, 0% death)\\n\\n**论文意义**：即使项目内判别力最高的 router (balanced_acc=58.1%)，e2e 表现仍 ≤ always-det。强力支撑 C1：death avoidance 主导下 router 无法学到有效 signal，trained routing 不如简单 always-deterministic。\"}, \"plan-004-ablation-b-seed789\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:57.342Z\", \"updated_at\": \"2026-05-14T09:22:41.133Z\", \"hypothesis\": \"ablation-b seed 变体 (seed=789)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\", \"conclusion\": \"negative\", \"metrics\": {\"generation_level\": {\"balanced_accuracy\": 0.5831, \"internal_recall\": 0.8182, \"det_recall\": 0.348, \"accuracy\": 0.3987}, \"parent\": \"plan-004-ablation-b\", \"note\": \"Seed 变体。balanced_acc ~58% 恒定，accuracy=39.87% 最低因最偏 internal。确认阈值效应。\"}}, \"plan-004-ablation-b-seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:56.275Z\", \"updated_at\": \"2026-05-14T09:22:39.105Z\", \"hypothesis\": \"ablation-b seed 变体 (seed=456)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\", \"conclusion\": \"negative\", \"metrics\": {\"generation_level\": {\"balanced_accuracy\": 0.5748, \"internal_recall\": 0.7576, \"det_recall\": 0.3919, \"accuracy\": 0.4314}, \"parent\": \"plan-004-ablation-b\", \"note\": \"Seed 变体。balanced_acc ~58% 恒定，accuracy=43.14% 低是因为偏 internal 预测。阈值效应。\"}}, \"plan-004-ablation-b-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:54.935Z\", \"updated_at\": \"2026-05-14T09:22:36.972Z\", \"hypothesis\": \"ablation-b seed 变体 (seed=123)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\", \"conclusion\": \"negative\", \"metrics\": {\"generation_level\": {\"balanced_accuracy\": 0.5736, \"internal_recall\": 0.5758, \"det_recall\": 0.5714, \"accuracy\": 0.5719}, \"parent\": \"plan-004-ablation-b\", \"note\": \"Seed 变体。balanced_acc ~58% 恒定，internal_recall 波动是阈值效应。Router 判别力接近随机。\"}}, \"plan-003-eval-implicit\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:11:52.155Z\", \"updated_at\": \"2026-05-14T09:12:15.517Z\", \"conclusion\": \"negative\", \"metrics\": {\"continuous_score\": {\"mean\": -12.84, \"ci_low\": -17.52, \"ci_high\": -8.45, \"n\": 245}, \"success_rate\": {\"mean\": 0.2204, \"ci_low\": 0.1796, \"ci_high\": 0.2653}, \"catastrophic_failure_rate\": {\"mean\": 0.1918, \"ci_low\": 0.151, \"ci_high\": 0.2327}, \"simulator_invocation_ratio\": 0.9411, \"step_routing_accuracy\": {\"accuracy\": 0.6023, \"correct\": 1301, \"total\": 2160}, \"episode_routing_accuracy\": {\"accuracy\": 0.8211, \"correct\": 78, \"total\": 95}, \"routing_distribution\": {\"deterministic\": 229, \"internal\": 16}, \"baselines\": {\"always_internal\": -39.07, \"always_det\": -9.47, \"oracle\": -6.58, \"random\": -22.38}, \"WARNING\": \"trained router (-12.84) worse than always-det (-9.47) by 3.37 points\"}}, \"plan-003-e2e-ablation-b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:02:31.160Z\", \"updated_at\": \"2026-05-14T09:10:14.831Z\", \"conclusion\": \"failed\", \"metrics\": {\"score_mean\": -11.11, \"score_ci_low\": -15.93, \"score_ci_high\": -6.7, \"death_rate\": 0.1796, \"success_rate\": 0.2367, \"sim_ratio\": 0.9607, \"fallback_rate\": 0.706, \"n_episodes\": 245, \"n_tasks\": 11, \"baseline_always_det\": -9.47, \"baseline_oracle\": -6.58, \"delta_vs_always_det\": -1.64}, \"hypothesis\": \"End-to-end eval of trained generative router (plan-002-generative-v1, internal_recall=51.5%) on 245 episodes / 11 tasks. Test C1: trained-router > always-det.\", \"notes\": \"⚠️ INVALID: 加载了错误的 checkpoint (checkpoints/plan-002-generative-v1/final_adapter = gen-v1 失败模型)，不是 ablation-b 的 checkpoints/plan-004-implicit/final_adapter。所有结果 (score=-11.11, delta_vs_always_det=-1.64) 反映的是 gen-v1 的 e2e 表现，不是 ablation-b。Reviewer 2026-05-14 发现。结果已废弃，用正确 checkpoint 重跑。\"}, \"plan-002-generative-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:24:07.881Z\", \"updated_at\": \"2026-05-14T08:44:34.766Z\", \"hypothesis\": \"Generative router SFT: 基于 ablation-b 成功经验（internal_recall=51.5%），用修正数据 data/plan-004-implicit/（2040 samples, 11 tasks, no-preference 已丢弃），upsample_minority=true 平衡类别（internal 180→1560），generative token prediction 而非 classification head。Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4, grad_accum=8。目标: internal_recall > 30% 且不退化。\", \"notes\": \"重新评估路由指标（generation-based eval, enable_thinking=False）。结果：accuracy=70.67%（偏高因多数类偏向），balanced_accuracy=46.67%，internal_recall=16.67%（5/30），det_recall=76.67%（207/270）。两种 thinking 模式对比：thinking_on+strip 在50 samples 上 internal_recall=0/5, thinking_off 同样 0/5。模型输出两种类别（pred: 232 det / 68 internal），但路由预测与真实标签不相关。vs ablation-b internal_recall=51.5%，generative-v1 显著退步。此前 notes 声称 internal_recall=51.85% 可能来自 logit-level eval（非 generation），不能反映实际推理行为。结论改为 negative。\", \"metrics\": {\"routing_accuracy\": 0.7067, \"balanced_accuracy\": 0.4667, \"internal_recall\": 0.1667, \"internal_precision\": 0.0735, \"internal_f1\": 0.102, \"det_recall\": 0.7667, \"det_precision\": 0.8922, \"det_f1\": 0.8247, \"val_size\": 300, \"val_label_dist\": {\"internal\": 30, \"deterministic\": 270}, \"pred_dist\": {\"deterministic\": 232, \"internal\": 68}, \"confusion_matrix\": [[5, 25], [63, 207]], \"train_final_loss\": 0.2, \"train_eval_loss\": 0.26, \"note\": \"enable_thinking=False required for Qwen3 inference; with thinking mode, model outputs &lt;think> tags causing all-internal parsing failure\"}, \"conclusion\": \"negative\"}, \"plan-004-v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:02:08.110Z\", \"updated_at\": \"2026-05-14T08:29:36.639Z\", \"hypothesis\": \"Implicit router SFT v5：严格复现 ablation-b 成功条件——data/plan-004-implicit/ + upsample_minority + gradient_accumulation_steps=1（有效 batch=4）。与 v3 区别：(1) 正确数据路径（非 results/plan_c_test_labels/），(2) 加 upsample，(3) ga=1 而非 ga=8。目标：复现 ablation-b 的 internal recall ~51.5%，确认 upsample + 小 batch 是成功关键。\", \"metrics\": {\"logit_level\": {\"accuracy\": 0.7451, \"balanced_accuracy\": 0.7905, \"internal_recall\": 0.8485, \"eval_loss\": 0.2382, \"note\": \"From Trainer eval during training (logit-level, not generation)\"}, \"generation_eval\": {\"accuracy\": 0.5333, \"balanced_accuracy\": 0.4148, \"internal_recall\": 0.2667, \"internal_precision\": 0.0635, \"internal_f1\": 0.0941, \"det_recall\": 0.563, \"det_precision\": 0.8736, \"det_f1\": 0.6862, \"confusion_matrix\": [[152, 118], [22, 8]], \"confusion_labels\": [\"deterministic\", \"internal\"], \"n_val\": 300, \"val_label_dist\": {\"internal\": 30, \"deterministic\": 270}, \"pred_dist\": {\"deterministic\": 174, \"internal\": 126}, \"enable_thinking\": \"identical results for thinking_on, thinking_off, and thinking_on+strip\"}}, \"conclusion\": \"negative\", \"notes\": \"Generation-based routing eval 推翻了此前 logit-level 的 success 结论。\\n\\n**Logit-level (Trainer eval, 训练时)**: accuracy=74.5%, balanced_acc=79.1%, internal_recall=84.9% — 看起来成功。\\n**Generation-based eval**: accuracy=53.3%, balanced_acc=41.5%, internal_recall=26.7% — 实际失败。\\n\\ninternal_recall=26.7% < 30% 判定线 → conclusion 改为 negative。\\n\\n三种 thinking 模式（thinking_on, thinking_off, thinking_on+strip）结果完全一致，说明 thinking mode 不是根因。\\n\\n与 ablation-b 对比: accuracy 53.3% vs 65.4%, balanced_acc 41.5% vs 59.3%, internal_recall 26.7% vs 51.5%。全面落后。\\n\\n与 plan-002-generative-v1 同样的问题模式：logit-level 指标与 generation-level 指标严重不一致。模型在 next-token prediction (loss) 层面学会了区分路由，但在自回归生成时无法可靠地输出 [SIMULATE] 前缀。\\n\\n根因推测：causal LM 的 generation 和 teacher-forcing eval 是不同的推理模式。训练时看到完整序列可以区分路由，但生成时第一个 token 的选择（是否输出 \\\"[\\\" 开始 [SIMULATE]）不够确定。\"}, \"plan-003-baseline-245eps\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:11:02.369Z\", \"updated_at\": \"2026-05-14T08:11:34.208Z\", \"conclusion\": \"success\", \"notes\": \"245 eps baseline results: always-int=-39.07 [-44.89,-33.37] death=42.9%; always-det=-9.47 [-13.66,-5.11] death=16.3%; oracle=-6.58 [-10.65,-2.43] death=14.3% sim=96.2%; random=-22.38 [-27.75,-17.09] death=27.8%. episode_summary.jsonl rebuilt from episodes.jsonl (old 194-ep backups saved as .bak194).\"}, \"plan-002-generative-v1-ga1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:59:30.209Z\", \"updated_at\": \"2026-05-14T08:03:02.054Z\", \"hypothesis\": \"Generative router SFT 对照组：与 plan-002-generative-v1 完全一致（Qwen3-1.7B + LoRA r=16, 3 epochs, upsample_minority=true, data/plan-004-implicit/），唯一区别 gradient_accumulation_steps=1（有效 batch_size=4 而非 32）。隔离 upsample + grad_accum confound：ablation-b 成功用 ga=1，v3/v4 失败用 ga=8。目标：如果 ga1 复现 ablation-b 的 internal recall ~51.5%，确认 grad_accum=8 是 v3/v4 退化的 confound。\", \"notes\": \"cuda:1 暂让给 plan-004-v5（Director 优先指令）。v5 ~3min 完成后立即提交 v1-ga1。\", \"conclusion\": \"killed\"}, \"plan-004-v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:16:04.007Z\", \"updated_at\": \"2026-05-14T07:38:54.065Z\", \"parent\": \"plan-004-v3\", \"conclusion\": \"negative\", \"notes\": \"## 状态报告 (2026-05-14)\\n\\n### 训练完成\\n- 状态: DONE (EXIT_CODE=0)\\n- 运行时长: 150.3s (~2.5min)\\n- 进度: 147/147 steps, 3 epochs\\n- Adapter 保存: checkpoints/plan-004-v4/final_adapter\\n\\n### 数据\\n- 文件: results/plan_c_test_labels/implicit_sft.jsonl (1814行)\\n- 与 v2/v3 使用同一数据文件\\n- Split: 53 train / 10 val episodes → 1558 train / 256 val steps\\n- Route labels (train): internal=1048, deterministic=510\\n\\n### Loss 曲线\\n| Epoch | Train Loss | Grad Norm |\\n|-------|-----------|-----------|\\n| 0.21  | 48.1538   | 122.03    |\\n| 0.41  | 42.0474   | 131.02    |\\n| 0.62  | 26.1077   | 94.05     |\\n| 0.82  | 13.7082   | 51.81     |\\n| 1.02  | 8.463     | 36.91     |\\n| 1.23  | 6.8562    | 27.10     |\\n| 1.43  | 6.0505    | 15.74     |\\n| 1.64  | 5.9014    | 15.58     |\\n| 1.84  | 5.0414    | 10.27     |\\n| 2.04  | 4.5778    | 10.58     |\\n| 2.25  | 4.4344    | 16.18     |\\n| 2.45  | 4.153     | 14.26     |\\n| 2.66  | 4.4794    | 11.85     |\\n| 2.86  | 4.3672    | 14.33     |\\n\\n平均 train_loss: 12.74\\n\\n### Eval Loss\\n- Epoch 1: 0.9549\\n- Epoch 2: 0.5524\\n- Epoch 3: 0.4922\\n\\n### Checkpoints\\ncheckpoint-49, checkpoint-98, final_adapter\\n\\n### 与 v2/v3 对比（关键发现）\\n- **v4 step 10 loss = 48.1538，与 v2/v3 的 48.15 完全一致**\\n- 三个版本使用同一数据文件 (results/plan_c_test_labels/implicit_sft.jsonl)\\n- ablation-b 用不同数据 (data/plan-004-implicit/)，loss 正常 (0.36-0.71)\\n- **结论：数据文件是初始 loss 异常高的根因，非 class_weights**\\n\\n### 异常：train loss vs eval loss 巨大差距\\n- Train loss 终态 ~4.4 vs eval loss 0.49\\n- 可能原因: 训练 loss 含 class_weights 加权，eval loss 是原始 CE；或数据格式/标签问题导致训练目标与评估目标不一致\"}, \"plan-003-baseline\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T07:29:43.220Z\", \"updated_at\": \"2026-05-14T07:30:27.429Z\", \"hypothesis\": \"End-to-end evaluation baselines: always-internal, always-deterministic, oracle, random, trained-router (degenerate v6). 194 episodes / 11 tasks. 建立论文 Table 1 的 baseline 数据。\", \"conclusion\": \"success\", \"metrics\": {\"always_internal\": {\"score\": -37.16, \"ci_90\": [-43.39, -31.43], \"success_rate\": 0.1237, \"death_rate\": 0.4072, \"sim_ratio\": 0}, \"always_deterministic\": {\"score\": -11.64, \"ci_90\": [-17.39, -6.55], \"success_rate\": 0.2371, \"death_rate\": 0.1856, \"sim_ratio\": 1}, \"oracle\": {\"score\": -9.03, \"ci_90\": [-14.14, -4.15], \"success_rate\": 0.2423, \"death_rate\": 0.1649, \"sim_ratio\": 0.9623}, \"random\": {\"score\": -23.75, \"ci_90\": [-29.6, -18.11], \"success_rate\": 0.1649, \"death_rate\": 0.2835, \"sim_ratio\": 0.5027}, \"trained_router_v6\": {\"score\": -11.64, \"ci_90\": [-17.39, -6.55], \"success_rate\": 0.2371, \"death_rate\": 0.1856, \"sim_ratio\": 1, \"note\": \"degenerate - identical to always-deterministic\"}, \"episodes\": 194, \"tasks\": 11}, \"notes\": \"Retrospectively registered. Eval ran on server by worker_code_plan-003-eval-script. Output: results/plan_003_eval/. trained-router = plan-002-formal-v6 (degenerate, all-deterministic). 需用 plan-002-generative-v1 的非退化 router 重跑 trained-router 条件。\"}, \"plan-002-formal-v6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:57:27.371Z\", \"updated_at\": \"2026-05-14T07:28:12.694Z\", \"notes\": \"初次启动 OOM（GPU0 内存争抢，step 30/153 被杀），自动重启 PID 240633。Epoch 1 eval: accuracy=0.929, f1_macro=0.481, f1_internal=0.0, recall_internal=0.0。去掉 class_weights 后模型在 89.7%/10.3% 不平衡数据上仍退化为全 deterministic 预测。dtype 实际为 fp32（启动早于 torch_dtype 修正）。\", \"conclusion\": \"negative\"}, \"plan-004-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:06:51.091Z\", \"updated_at\": \"2026-05-14T07:24:34.751Z\", \"hypothesis\": \"Implicit router SFT v3：修复两个 bug——(1) 去掉 class_weights auto（D023 根因），(2) 用 plan_c/ 11 task 重生成数据修复 no-preference→internal 映射 bug。与 plan-002-formal-v6（explicit classification head, 同样无 class_weights）对照。2040 samples from 11 tasks, no-preference 已丢弃。\", \"parent\": \"plan-004-v2\", \"conclusion\": \"negative\", \"notes\": \"## 数据文件差异分析 (2026-05-14)\\n\\n### 三个数据文件确认\\n| | ablation-b | v2 | v3 |\\n|---|---|---|---|\\n| 路径 | data/plan-004-implicit/implicit_sft.jsonl | results/plan_c_test_labels/implicit_sft.jsonl | data/plan-004-v3/implicit_sft.jsonl |\\n| MD5 | c9b59e04de78... | eb9daacc7f97... | **c9b59e04de78... (=ablation-b)** |\\n| 样本数 | 2040 | 1814 | 2040 |\\n| 文件大小 | 1,578,366 bytes | 1,398,021 bytes | 1,578,366 bytes |\\n\\n**v3 和 ablation-b 的数据文件 100% 相同（MD5 一致）。**\\n\\n### Schema（三个文件一致）\\nfields: messages, task_type, variation, step_idx, route_label\\n\\n### 标签分布\\n- ablation-b / v3: **deterministic 1830 (89.7%), internal 210 (10.3%)**\\n- v2: **internal 1214 (66.9%), deterministic 600 (33.1%)** ← 标签比例完全反转！\\n\\n### Task Type 分布\\n- ablation-b / v3: 11 个 task_type，以 find-non-living-thing(510), chemistry-mix(240) 为主\\n- v2: **仅 4 个 task_type**：find-non-living-thing(600), find-animal(554), grow-fruit(390), identify-life-stages-1(270)\\n\\n### 文本长度\\n- ablation-b / v3: n=2040, min=52, max=166, mean=87 words\\n- v2: n=1814, min=52, max=200, mean=90 words\\n\\n### 前 3 条样本对比\\nablation-b/v3 首条: chemistry-mix/variation 0/step 0, [SIMULATE] connect agent to door to kitchen, route=deterministic\\nv2 首条: find-non-living-thing/variation 0/step 0, [SIMULATE] connect agent to art studio door, route=deterministic\\n\\n### 训练配置对比（真正变量）\\n| | ablation-b (正常) | v2 (异常) | v3 (异常) |\\n|---|---|---|---|\\n| 脚本 | training/implicit_router_sft.py | 同左 | 同左 |\\n| 数据 | data/plan-004-implicit (2040) | results/plan_c_test_labels (1814) | data/plan-004-v3 (2040, **=ablation-b**) |\\n| upsample_minority | **true** | false | false |\\n| class_weights | 无 | \\\"auto\\\" | null |\\n| gradient_accumulation | 1 (默认) | 8 | 8 |\\n| batch_size | 4 | 4 | 4 |\\n| 有效batch | 4 | 32 | 32 |\\n\\n### 训练曲线对比\\n| | ablation-b | v2 | v3 |\\n|---|---|---|---|\\n| Step 10 loss | 5.25 | 48.15 | 48.15 (用户报告) |\\n| Epoch 1 eval_loss | ~0.68 | 0.95 | [无 train.log] |\\n| Epoch 3 eval_loss | 0.36 | **0.49 (收敛了!)** | [无 train.log] |\\n| 平均 train_loss | 1.26 | 12.74 | [无数据] |\\n\\n**重要发现: v2 虽然起步 loss=48，但最终 eval_loss 收敛到 0.49，模型实际上学到了。**\\n\\n### class_weights 代码分析\\nclass_weights 在 WeightedTrainer.compute_loss() 中正确实现：\\n- sample_idx 由 ImplicitSFTDataset.__getitem__() 返回 (line 85)\\n- PaddingCollator.__call__() 正确传递 (line 128-136)\\n- compute_loss() 中 `inputs.pop(\\\"sample_idx\\\")` 获取，条件 `self._class_weights is not None and sample_indices is not None` 控制 (line 227)\\n- v2 (class_weights=\\\"auto\\\"): 权重 internal=0.743, det=1.527，正确计算并应用\\n- v3 (class_weights=null): 无权重，`loss = per_sample_loss.mean()`\\n\\n**class_weights 代码本身没有 bug。v2 和 v3 的 step 10 loss 一致（48.15），证明 class_weights 不是 loss 差异的主因。** class_weights 只是对 per-sample loss 的乘法缩放（0.74x~1.53x），不会改变 loss 的数量级。\\n\\n### plan-002-formal-v6 数据路径\\n- 数据来源: `results/plan_c/` 目录（11 个 task_type 子目录的 labeled_steps.jsonl）\\n- 加载: 2040 samples from 11 files\\n- 标签分布: deterministic 1830 (89.7%), internal 210 (10.3%)\\n- 与 ablation-b 的 implicit 数据是**同源数据，但格式不同**（explicit router 用 observation+action_history+label 格式，implicit 用 messages chat 格式）\\n- **plan-002-formal-v6 也退化了**: 全预测 deterministic (internal: 0/30, deterministic: 390/390)\\n\\n### 结论：根因判定\\n\\n**\\\"数据文件不同\\\"假说被证伪（对 v3）**：v3 使用和 ablation-b 完全相同的数据（MD5 一致），但仍然异常。\\n\\n**真正的变量是训练策略的组合**：\\n1. **`upsample_minority: true`**（ablation-b 独有）：在 89.7% deterministic 的极端不平衡数据上，WeightedRandomSampler 确保 internal 样本被充分采样。没有它，模型每 batch 几乎只看到 deterministic 样本。\\n2. **`gradient_accumulation_steps: 1 vs 8`**：有效 batch 4 vs 32。较大 batch + 无上采样 = 每步看到的 internal 样本更少。\\n\\n**v2 的数据确实不同**（标签比例反转：internal 67% vs 10%，只有 4 个 task_type），但 v2 依然收敛了（eval_loss 0.49）。这说明数据差异导致训练行为不同，但不是致命问题。\\n\\n**建议下一步**：\\n- 用 ablation-b 的配置（upsample_minority=true, gradient_accumulation=1）重跑 v3 数据，验证是否恢复正常 loss\\n- 对 v2 跑 eval 看是否也退化\"}, \"plan-004-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:41:13.286Z\", \"updated_at\": \"2026-05-14T07:08:59.680Z\", \"conclusion\": \"failed\", \"metrics\": {\"train_loss_avg\": 12.74, \"train_loss_epoch1\": [48.15, 42.05, 26.14, 13.71], \"train_loss_epoch3\": [4.58, 4.42, 4.15, 4.46, 4.36], \"eval_loss_epoch2\": 0.5509, \"eval_loss_epoch3\": 0.4905, \"train_runtime_sec\": 150.74, \"note\": \"no accuracy/balanced_accuracy computed\"}, \"notes\": \"Training completed normally (3 epochs, 147 steps). TRAINING_COMPLETE sentinel present. final_adapter + checkpoint-98/147 saved. train_loss=12.74 (abnormally high due to class_weights auto), eval_loss=0.490 at epoch 3. Process exited normally after completion, not OOM/crash.\"}, \"plan-002-formal-v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:37:37.792Z\", \"updated_at\": \"2026-05-14T07:08:19.782Z\", \"hypothesis\": \"Router SFT v5：pad_token_id fix。v3/v4 loss 异常根因确认为 model.config.pad_token_id=None（ModelScope 下载的 Qwen3-1.7B 未设置 pad_token_id，导致分类头 loss 计算错误）。Fix：模型加载后立即设 model.config.pad_token_id = tokenizer.pad_token_id (151643)。其余配置与 v4 相同：stratified split + 无 upsample + class_weights auto + 互斥检查。Qwen3-1.7B + LoRA r=16 (0.37% trainable), 3 epochs, batch_size=4 + grad_accum=8, 2040 samples (1830 det / 210 internal)。\", \"parent\": \"plan-002-formal-v4\", \"conclusion\": \"negative\", \"metrics\": {\"train_loss_avg\": 5.59, \"eval_loss_epoch1\": 0.79, \"eval_loss_epoch2\": 0.78, \"eval_accuracy\": 0.9167, \"eval_balanced_accuracy\": 0.4936, \"eval_f1_macro\": 0.47, \"per_class\": {\"deterministic\": {\"precision\": 0.928, \"recall\": 0.987, \"f1\": 0.938}, \"internal\": {\"precision\": 0, \"recall\": 0, \"f1\": 0}}, \"class_weights\": {\"internal\": 4.5, \"deterministic\": 0.5625}, \"grad_norm_range\": \"70-604\", \"is_degenerate\": true, \"note\": \"Metrics corrected per eval_report.json (D023 Reviewer audit). class_weights auto inflates train loss (4-11) and destabilizes training (grad_norm 604). Model degenerates to all-deterministic.\"}, \"notes\": \"D021 确认：class_weights auto [4.5, 0.5625] 是 v3/v4/v5 loss 异常的根因。train_loss 4-11 (正常应 0.5-0.7)，grad_norm 604，internal recall=0。pad_token_id fix 无效（代码中已存在）。v6 对照实验：移除 class_weights，验证 loss 是否恢复正常。\"}, \"plan-002-formal-v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:22:49.207Z\", \"updated_at\": \"2026-05-14T07:03:55.761Z\", \"hypothesis\": \"Router SFT v4：三项修复——(1) stratified val split (sklearn train_test_split stratify=labels, val 有 30 internal + 390 det), (2) 移除 upsample_minority 只保留 class_weights auto [4.50, 0.5625], (3) 互斥检查防止过补偿。Qwen3-1.7B + LoRA r=16 (0.37% trainable), 3 epochs, batch_size=4 + grad_accum=8, 2040 samples (1830 det / 210 internal)。\", \"conclusion\": \"negative\", \"notes\": \"【更正 D023】v4 实际完整训练完毕（有 TRAINING_COMPLETE + checkpoint-153 + eval_report.json），之前误标 killed。accuracy=91.9% 但 internal_recall=0%（退化为全 deterministic）。根因：class_weights [4.5, 0.5625] 使含 internal 微批次 loss 爆炸(5-11)、grad_norm 100-600，被 max_grad_norm=1.0 裁剪后 internal 有效学习率≈lr×1/600≈3e-8（等于零）。dryrun 无 class_weights 时 loss 正常(0.17-1.03)。\", \"metrics\": {\"eval_accuracy\": 0.919, \"eval_balanced_accuracy\": 0.5, \"internal_recall\": 0, \"internal_precision\": 0, \"is_degenerate\": true, \"class_weights\": {\"internal\": 4.5, \"deterministic\": 0.5625}, \"note\": \"训练完整完成（TRAINING_COMPLETE + checkpoint-153 + eval_report.json），但退化为全部预测 deterministic。之前误标 killed。真正问题：class_weights [4.5, 0.5625] + max_grad_norm=1.0 交互导致 internal 有效学习率≈0\"}}, \"plan-002-formal-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:46:07.817Z\", \"updated_at\": \"2026-05-14T06:09:51.858Z\", \"hypothesis\": \"Router SFT v3（本地 Qwen3-1.7B + HF_HUB_OFFLINE=1）。v1/v2 因网络不可达崩溃。v3 改用 ModelScope 本地模型 /root/autodl-tmp/models/Qwen/Qwen3-1.7B。结果：accuracy=0, f1=0, 完全失效。正在排查根因（模型 config 差异 / label mapping 问题）。\", \"parent\": \"plan-002-formal-v2\", \"conclusion\": \"failed\"}, \"plan-012-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:02:42.659Z\", \"updated_at\": \"2026-05-14T06:04:07.731Z\", \"hypothesis\": \"Death decomposition 全量分析：11 tasks / 245 episodes。plan-001b 完整数据上的最终版。核心发现：death avoidance fraction=90.41%, Δ_full=29.60, Δ_nd=2.84, r=0.9698 (p=8.12e-07)。\", \"conclusion\": \"success\", \"metrics\": {\"delta_full\": 29.6, \"delta_nd\": 2.84, \"death_avoidance_fraction\": 0.9041, \"pearson_r\": 0.9698, \"pearson_p\": 8.12e-07, \"tasks\": 11, \"episodes\": 245, \"death_rate_int\": 0.429, \"death_rate_det\": 0.163, \"label_dist\": {\"det_preferred\": 86, \"internal_preferred\": 9, \"no_preference\": 150}}}, \"plan-012-decomposition\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:50:01.170Z\", \"updated_at\": \"2026-05-14T05:44:02.255Z\", \"hypothesis\": \"Death decomposition 中间分析：30 tasks / 249 episodes 上验证 death avoidance 占 ~99% routing signal（预分析，plan-001b 完整数据后将重跑最终版）\", \"conclusion\": \"success\", \"metrics\": {\"full_11tasks\": {\"delta_full\": 29.6, \"delta_nd\": 2.84, \"death_avoidance_fraction\": 0.9041, \"pearson_r\": 0.9698, \"pearson_p\": 8.12e-07, \"tasks\": 11, \"episodes\": 245, \"death_rate_int\": 0.429, \"death_rate_det\": 0.163, \"label_dist\": {\"det_preferred\": 86, \"internal_preferred\": 9, \"no_preference\": 150}}, \"prescreening_30tasks\": {\"delta_full\": 37.9, \"delta_nd\": 0.2, \"death_avoidance_fraction\": 0.99, \"pearson_r\": 0.989, \"pearson_p\": \"<0.0001\", \"tasks\": 30, \"episodes\": 249}, \"key_tasks\": {\"find_non_living_thing\": {\"n\": 40, \"dr_int\": 0, \"dr_det\": 0, \"delta_full\": 9.58, \"delta_nd\": 9.58, \"note\": \"唯一零死亡 task, Δ_full 全部来自 non-death 性能差异\"}, \"measure_melting_point\": {\"n\": 20, \"dr_int\": 0.55, \"dr_det\": 0.25, \"delta_full\": 30.05, \"delta_pr\": 0.05, \"note\": \"高死亡率, 性能差距几乎完全由 death avoidance 解释\"}}}}, \"plan-002-formal-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:35:54.371Z\", \"updated_at\": \"2026-05-14T05:42:36.829Z\", \"hypothesis\": \"Router SFT 正式训练 v2（WANDB_MODE=offline 修复网络问题）：Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4 + grad_accum=8, class_weights auto + WeightedRandomSampler。v1 因 W&B 网络不可达崩溃。\", \"parent\": \"plan-002-formal\", \"conclusion\": \"failed\", \"notes\": \"第二次失败，根因与 v1 相同：AutoTokenizer.from_pretrained(\\\"Qwen/Qwen3-1.7B\\\") 网络不可达 (OSError: [Errno 101] Network is unreachable)。WANDB_MODE=offline 只修了 W&B 上报，没修模型加载。Qwen3-1.7B 不在本地 HF cache。训练从未开始，wall_clock 256s 全为 HTTP retry/backoff。| 修复方案: 先用 network_turbo 或 ModelScope 下载 Qwen3-1.7B 到本地，再用 --model_name /local/path 重新提交 v3。\"}, \"plan-002-formal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:28:33.051Z\", \"updated_at\": \"2026-05-14T05:37:19.272Z\", \"hypothesis\": \"Router SFT 正式训练：Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4 + grad_accum=8 (有效 batch=32), class_weights auto + WeightedRandomSampler。诊断性 probe——验证 learned router 能否从 episode-level counterfactual labels 学到 routing signal（尤其 internal-preferred minority class）。Dryrun 确认 pipeline 通但 1 epoch 退化，3 epochs 应足以收敛。\", \"conclusion\": \"failed\", \"notes\": \"失败原因: AutoTokenizer.from_pretrained(\\\"Qwen/Qwen3-1.7B\\\") 在初始化阶段崩溃——HuggingFace Hub 网络不可达 (OSError: [Errno 101] Network is unreachable) 且本地 HF cache 无此模型。训练从未开始，无 checkpoint，无任何进度。wall_clock 258s 全为 HTTP retry/backoff。| 已有成果: 无 | 建议: 找到 Qwen3-1.7B 本地路径或下载后，用 --model_name /local/path 重新提交\"}, \"plan-001b-gpu1-freeze-chem\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:08:29.425Z\", \"updated_at\": \"2026-05-14T05:36:34.576Z\", \"hypothesis\": \"GPU1 拆分任务：freeze 20 eps + chemistry-mix 20 eps。find-non-living-thing 完成后立即启动，与 GPU0 (lifespan-longest-lived + measure-melting-point) 并行。\", \"conclusion\": \"success\"}, \"plan-002-dryrun\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:03:05.854Z\", \"updated_at\": \"2026-05-14T05:26:39.798Z\", \"hypothesis\": \"Pipeline validation on partial data (10/11 tasks). NOT for results — verify data loading, model init, training loop, checkpoint save, eval. Will retrain on full data after chemistry-mix completes.\", \"notes\": \"dryrun-passed. Checkpoint saved: checkpoint-383 + final_adapter + eval_report.json. LoRA r=16 (0.37% trainable), 5880 samples, 1163 steps, batch_size=4. Cron 误标 failed（PID 变更导致 5× dead check），实际训练成功完成。【修正】class_weights=[11.07, 0.52] 和 WeightedRandomSampler 均已生效（WeightedCETrainer.compute_loss 覆盖 + get_train_dataloader 覆盖）。退化原因：1 epoch 不足以收敛（loss 仍在下降 0.6307→0.4762），非 class_weights 未启用。\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6307, \"eval_loss\": 0.4762, \"eval_accuracy\": 0.923, \"eval_f1_macro\": 0.48, \"eval_balanced_accuracy\": 0.5, \"per_class\": {\"deterministic\": {\"precision\": 0.923, \"recall\": 1, \"f1\": 0.96}, \"internal\": {\"precision\": 0, \"recall\": 0, \"f1\": 0}}, \"confusion\": {\"true_internal_pred_internal\": 0, \"true_internal_pred_det\": 30, \"true_det_pred_det\": 360, \"true_det_pred_internal\": 0}, \"per_task_eval\": {\"chemistry-mix\": {\"accuracy\": 0, \"n_samples\": 30}, \"find-animal\": {\"accuracy\": 1, \"n_samples\": 30}, \"find-non-living-thing\": {\"accuracy\": 1, \"n_samples\": 90}, \"freeze\": {\"accuracy\": 1, \"n_samples\": 30}, \"grow-fruit\": {\"accuracy\": 1, \"n_samples\": 30}, \"identify-life-stages-1\": {\"accuracy\": 1, \"n_samples\": 30}, \"identify-life-stages-2\": {\"accuracy\": 1, \"n_samples\": 30}, \"inclined-plane-determine-angle\": {\"accuracy\": 1, \"n_samples\": 30}, \"lifespan-longest-lived\": {\"accuracy\": 1, \"n_samples\": 30}, \"lifespan-longest-lived-then-shortest-lived\": {\"accuracy\": 1, \"n_samples\": 30}, \"measure-melting-point-unknown-substance\": {\"accuracy\": 1, \"n_samples\": 30}}, \"samples\": 1920, \"total_steps\": 383, \"runtime_s\": 303.8, \"note\": \"DEGENERATE: 全部预测 deterministic, internal recall=0. chemistry-mix 是唯一 internal-preferred task (30 samples 全错). 正在审计 class_weights 是否真正生效。\"}}, \"gpu0-v6-lifespan\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:19:08.846Z\", \"updated_at\": \"2026-05-14T04:52:49.472Z\", \"hypothesis\": \"GPU0 干净重收 lifespan-longest-lived 全量 20 eps（SLIM_EPISODES=1，从 ep0 开始）。之前数据文件损坏（150GB），已删除后重启。plan-001b 最后 3 个未完成 task 之一。\", \"conclusion\": \"killed\", \"notes\": \"Director 指令主动终止。lifespan-longest-lived 已收 23 eps（超额3），数据充足。GPU0 释放给 plan-002 dry-run。\"}, \"plan-001b-gpu0-v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:47:32.668Z\", \"updated_at\": \"2026-05-14T04:19:43.102Z\", \"hypothesis\": \"GPU0 修正重启：measure-melting-point-unknown-substance 20 eps + lifespan-longest-lived 补 1 ep (ep19)。去重后重启，使用 --reuse_dirs 防止重复。\", \"conclusion\": \"killed\", \"notes\": \"Director 指令主动终止。原因：measure-melting-point 已有完整 20 eps（冗余），lifespan-longest-lived 文件损坏（150GB）。GPU0 重启做 lifespan-longest-lived 全量 20 eps 干净重收 (v6)。\"}, \"plan-001b-fnlt-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:05:13.793Z\", \"updated_at\": \"2026-05-14T03:12:10.756Z\", \"hypothesis\": \"find-non-living-thing 追加收集 ep 21-39 (19 eps)，补齐到 40 eps 总量。唯一 0% 死亡率 task，是 ~99% death avoidance claim 的关键 counter-example。\", \"conclusion\": \"success\", \"metrics\": {\"find-non-living-thing\": {\"total_episodes\": 40, \"ep_range\": \"0-39\", \"no_duplicates\": true, \"no_missing\": true, \"det_pref\": 8, \"int_pref\": 0, \"no_pref\": 11, \"avg_score_gap_non_tie\": 40.5, \"note\": \"19 new eps (ep 21-39) collected. Combined with prior 21 eps. 0% death rate confirmed at 40 ep scale.\"}}}, \"plan-001b-gpu0-v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:06:59.924Z\", \"updated_at\": \"2026-05-14T02:47:30.101Z\", \"hypothesis\": \"GPU0 拆分任务：lifespan-longest-lived 补 4 eps (已有 16, 目标 20) + measure-melting-point-unknown-substance 全量 20 eps。与 GPU1 freeze+chemistry-mix 并行，加速 plan-001b 完成。\", \"conclusion\": \"killed\", \"notes\": \"v4 崩溃（GPU0 第三次进程异常终止）。v2: vLLM EngineCore crash, v3: cleanup worker 误杀, v4: 崩溃原因待确认。数据重复已清理（lifespan-longest-lived ep 0-6 重复删除）。\"}, \"plan-001b-gpu0-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:50:46.913Z\", \"updated_at\": \"2026-05-14T02:02:40.577Z\", \"hypothesis\": \"GPU0 vLLM崩溃后重启收集：lifespan-longest-lived补5eps(ep15-19) + measure-melting-point-unknown-substance 20eps + freeze 20eps + chemistry-mix 20eps。与v2相同配置，数据可合并。\", \"notes\": \"脚本 run_gpu0_v3.sh 已创建但从未启动。GPU0 被 v2 崩溃残留的僵尸 vLLM 进程（PID 544942, 28GB VRAM）占用。4 个 task 全部未开始。需清理僵尸后重新拆分到双卡。\", \"conclusion\": \"failed\"}, \"plan-001b-gpu1-extra\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:46:54.844Z\", \"updated_at\": \"2026-05-14T02:02:28.988Z\", \"hypothesis\": \"find-non-living-thing 追加 19 eps（ep 21-39），补齐到 40 eps 总量。ep1-20 已收集（delta=-0.05, tied），21 eps 因 cleanup worker 误杀 SIGHUP 中断（仅完成 ep21）。唯一 0% 死亡率 task，C1 \\\"~99% death avoidance\\\" claim 的关键 counter-example。\", \"conclusion\": \"failed\"}, \"plan-001b-gpu1-rebalance\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T01:48:05.077Z\", \"updated_at\": \"2026-05-14T01:56:27.532Z\", \"hypothesis\": \"GPU 负载均衡：GPU1 接管 find-non-living-thing extra 20 eps + GPU0 未开始的 freeze/chemistry-mix 各 20 eps，加速 plan-001b 完成\", \"conclusion\": \"killed\", \"notes\": \"已废弃：GPU0-v3 已接管 freeze/chemistry-mix 数据收集。find-non-living-thing extra 20 eps 由 plan-001b-gpu1-extra 独立处理。\"}, \"plan-001b-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:10:04.310Z\", \"updated_at\": \"2026-05-14T01:56:22.485Z\", \"hypothesis\": \"Episode-level data collection for 4 tasks (1 internal-pref: find-non-living-thing + 3 death-dom: grow-fruit, inclined-plane-determine-angle, identify-life-stages-2), 20 eps/task, reusing prescreening 5 eps. find-non-living-thing needs follow-up to reach 40 eps total.\", \"notes\": \"Part of plan-001b approved by Director. Tasks: find-non-living-thing (20 eps first pass, needs extra 20 to reach 40 target), grow-fruit, inclined-plane-determine-angle, identify-life-stages-2. 80 new eps this run. Follow-up needed for find-non-living extra 20 eps.\", \"conclusion\": \"success\", \"metrics\": {\"find-non-living-thing\": {\"episodes\": 20, \"internal_mean\": 24.9, \"det_mean\": 24.95, \"delta_int_minus_det\": -0.05, \"int_deaths\": 0, \"det_deaths\": 0, \"both_deaths\": 0, \"int_only_death\": 0, \"det_only_death\": 0, \"labels\": {\"det-pref\": 7, \"int-pref\": 4, \"no-pref\": 9}, \"alive_int_mean\": 24.9, \"alive_det_mean\": 24.95, \"note\": \"Prescreening 5eps showed internal-preferred, but 20eps shows essentially TIED (delta=-0.05). Direction did NOT hold. det-pref=7 vs int-pref=4 by episode count.\"}, \"grow-fruit\": {\"episodes\": 20, \"internal_mean\": -43.65, \"det_mean\": -18.55, \"delta_int_minus_det\": -25.1, \"int_deaths\": 9, \"det_deaths\": 4, \"both_deaths\": 3, \"int_only_death\": 6, \"det_only_death\": 1, \"labels\": {\"det-pref\": 6, \"int-pref\": 1, \"no-pref\": 13}, \"alive_int_mean\": 2.45, \"alive_det_mean\": 1.81, \"note\": \"Death-dominated confirmed. Internal dies 6x exclusively vs det 1x. Alive scores low and similar.\"}, \"inclined-plane-determine-angle\": {\"episodes\": 20, \"internal_mean\": -55, \"det_mean\": -19, \"delta_int_minus_det\": -36, \"int_deaths\": 11, \"det_deaths\": 4, \"both_deaths\": 4, \"int_only_death\": 7, \"det_only_death\": 0, \"labels\": {\"det-pref\": 7, \"int-pref\": 0, \"no-pref\": 13}, \"alive_int_mean\": 0, \"alive_det_mean\": 1.25, \"note\": \"Most extreme death-dominated. Internal dies 7x exclusively, det never dies alone. Internal NEVER preferred (0/20). Alive scores near zero.\"}, \"identify-life-stages-2\": {\"episodes\": 20, \"internal_mean\": -48.4, \"det_mean\": -18.4, \"delta_int_minus_det\": -30, \"int_deaths\": 10, \"det_deaths\": 4, \"both_deaths\": 4, \"int_only_death\": 6, \"det_only_death\": 0, \"labels\": {\"det-pref\": 6, \"int-pref\": 0, \"no-pref\": 14}, \"alive_int_mean\": 3.2, \"alive_det_mean\": 2, \"note\": \"Death-dominated confirmed. Internal dies 6x exclusively, det never alone. Internal NEVER preferred (0/20).\"}, \"summary\": {\"total_episodes\": 80, \"all_tasks_complete\": true, \"death_dominated_tasks\": [\"grow-fruit\", \"inclined-plane-determine-angle\", \"identify-life-stages-2\"], \"internal_preferred_tasks\": [], \"key_finding\": \"find-non-living-thing prescreening signal (internal>det) did NOT replicate at 20 eps — essentially tied. All 3 death-dom tasks confirmed: internal router causes significantly more deaths than deterministic.\"}}}, \"plan-001b-gpu0-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:31:47.627Z\", \"updated_at\": \"2026-05-14T01:51:26.200Z\", \"hypothesis\": \"Episode-level data collection for 7 tasks (5 genuine-det + 2 death-dom), 20 eps/task. v2: added cleanup_gpu_processes() to prevent orphan vLLM processes.\", \"conclusion\": \"failed\", \"notes\": \"GPU0 第二次失败。根因：vLLM EngineCore 在 Episode 15 deterministic 模式中意外死亡 (EngineDeadError)。v2 的 cleanup_gpu_processes() 只清理启动前孤儿，未防运行中崩溃。诊断 Worker: worker_diagnose_plan-001b-gpu0-v2_20260514T015111\"}, \"plan-011-rule-based\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:51:12.911Z\", \"updated_at\": \"2026-05-14T01:00:59.327Z\", \"hypothesis\": \"Rule-based keyword routing baseline：测试 keyword heuristic 能否捕获 episode-level routing signal。三版 keyword list 均结构性失效——v1 (含 connect) ≈ always-det, v2 (科学词) ≈ always-internal, v3 (状态变化动词) ≈ always-internal。\", \"conclusion\": \"success\", \"metrics\": {\"v1_match_rate\": \"85.8%\", \"v1_result\": \"degenerate → always-det\", \"v2_match_rate\": \"4.9%\", \"v2_result\": \"degenerate → always-internal\", \"v3_match_rate\": \"2.8%\", \"v3_episode_accuracy\": \"1.5%\", \"v3_result\": \"degenerate → always-internal\", \"conclusion\": \"Keyword heuristic structurally fails on ScienceWorld — ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords. No keyword list provides meaningful routing signal.\", \"note\": \"D014: structural failure analysis, paper positions as evidence for learned/observation-based approaches\"}, \"notes\": \"v1 204 vs v2 203 episode 差异原因：竞态条件——v2 报告在 lifespan-shortest-lived/episodes.jsonl 创建前 15 秒生成。非方法论问题。当前重跑两版均为 233 episodes。论文统一引用最终 plan-001b 完整数据的 episode 基数。\"}, \"plan-001b-gpu0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:10:02.679Z\", \"updated_at\": \"2026-05-13T22:33:15.743Z\", \"hypothesis\": \"Episode-level data collection for 7 tasks (5 genuine-det: find-animal, identify-life-stages-1, lifespan-longest-lived-then-shortest, lifespan-longest-lived, measure-melting-point-unknown + 2 death-dom: freeze, chemistry-mix), 20 eps/task, reusing prescreening 5 eps\", \"notes\": \"Part of plan-001b approved by Director. Tasks: find-animal, identify-life-stages-1, lifespan-longest-lived-then-shortest-lived, lifespan-longest-lived, measure-melting-point-unknown-substance, freeze, chemistry-mix. 105 new eps (15 each × 7 tasks). Watch measure-melting-point-unknown death_avoidance_fraction=0.38 outlier per Reviewer note.\", \"conclusion\": \"failed\"}, \"research-prescreening-gpu0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:20:17.197Z\", \"updated_at\": \"2026-05-13T22:09:59.200Z\", \"hypothesis\": \"Fork-based deterministic evaluation 在 ScienceWorld 30 个 task types 中广泛有效（预筛 25 个未测 task，5 ep/task，识别 signal 方向）\", \"conclusion\": \"killed\"}, \"research-prescreening-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:53:28.002Z\", \"updated_at\": \"2026-05-13T22:08:01.696Z\", \"hypothesis\": \"GPU1 加入 plan-001a 预筛，跑剩余 8 个 task types（measure-melting-point-unknown-substance, mendelian-genetics-known/unknown-plant, power-component x2, test-conductivity x2, use-thermometer），加速完成全部 25 tasks\", \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"8/8\", \"all_direction\": \"POSITIVE\", \"results\": {\"measure-melting-point-unknown-substance\": {\"int_mean\": -58.6, \"det_mean\": -32, \"delta\": 26.6, \"signal\": \"death-dominated\"}, \"mendelian-genetics-known-plant\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"mendelian-genetics-unknown-plant\": {\"int_mean\": -60, \"det_mean\": -40, \"delta\": 20, \"signal\": \"death-dominated\"}, \"power-component\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"power-component-renewable-vs-nonrenewable-energy\": {\"int_mean\": -60, \"det_mean\": 0, \"delta\": 60, \"signal\": \"death-dominated\"}, \"test-conductivity\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"test-conductivity-of-unknown-substances\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"use-thermometer\": {\"int_mean\": -59.4, \"det_mean\": -19.4, \"delta\": 40, \"signal\": \"death-dominated\"}}, \"summary\": \"All 8 tasks death-dominated: internal mode hits -100 (lethal) in 3/5 episodes; deterministic mode avoids most deaths but scores remain ~0 (no genuine task progress). Delta driven by death avoidance, not task solving.\"}}, \"mvp-p1-signal\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T04:50:06.546Z\", \"updated_at\": \"2026-05-13T21:46:23.662Z\", \"conclusion\": \"killed\"}, \"research-boil-v3-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:20:17.657Z\", \"updated_at\": \"2026-05-13T19:50:37.666Z\", \"hypothesis\": \"用统一 v3 代码（> tie-break + death filter 仅 det/oracle）重跑 boil 20ep，获得与其他 4 个 task 一致的代码版本数据\", \"parent\": \"mvp-p1-gpu0\", \"notes\": \"Registry 状态 ANALYZING 但 cron reconcile 确认 PID 650421 仍存活（16/20 episodes 完成）。实际仍在 RUNNING。状态机不允许回退 ANALYZING→RUNNING，等完成后直接转 DONE。\", \"metrics\": {\"boil_v3_20ep\": {\"internal_mean\": -44.7, \"internal_std\": 50, \"det_mean\": -9.3, \"det_std\": 30.3, \"oracle_mean\": 3.8, \"oracle_std\": 15.2, \"oracle_minus_internal\": 48.5, \"oracle_minus_det\": 13.1, \"det_minus_internal\": 35.4}, \"death_distribution\": {\"internal_deaths\": 9, \"internal_total\": 20, \"internal_death_pct\": 45, \"det_deaths\": 2, \"det_total\": 20, \"det_death_pct\": 10, \"oracle_deaths\": 0, \"oracle_total\": 20, \"oracle_death_pct\": 0}, \"note\": \"v3 code (> tie-break, death filter det/oracle only). Oracle大幅优于两个baseline, 但绝对分低(3.8), 仅1/20 episode拿到70分. Death avoidance is primary mechanism.\"}, \"conclusion\": \"success\"}, \"research-cf-pilot-gpu1\": {\"status\": \"PENDING\", \"created_at\": \"2026-05-13T17:15:37.908Z\", \"updated_at\": \"2026-05-13T17:17:23.652Z\", \"hypothesis\": \"Episode-terminal counterfactual labeling (K=10) 在 melt/change-state/mix-paint 上产生 >30% non-tie rate，为 router 训练提供有效信号\", \"conclusion\": \"killed\"}, \"mvp-p1-gpu1-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T08:00:51.836Z\", \"updated_at\": \"2026-05-13T15:41:04.061Z\", \"conclusion\": \"success\", \"metrics\": {\"mix_paint\": {\"internal_mean\": -41, \"det_mean\": -5.5, \"oracle_mean\": 4.5, \"det_minus_internal\": 35.5, \"bootstrap_90ci\": [20, 55]}, \"grow_plant\": {\"internal_mean\": 0.5, \"det_mean\": 0.5, \"oracle_mean\": 0.5, \"det_minus_internal\": 0, \"bootstrap_90ci\": [0, 0]}, \"n_episodes_per_task\": 20, \"tasks_significant\": \"1/2\", \"note\": \"grow-plant: NO_EFFECT (三种模式完全相同); mix-paint: 显著正向\"}}, \"mvp-p1-gpu0-vllm\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T09:18:47.128Z\", \"updated_at\": \"2026-05-13T15:17:57.586Z\", \"conclusion\": \"success\", \"metrics\": {\"melt\": {\"internal_mean\": -54.7, \"det_mean\": -14.55, \"oracle_mean\": 2.15, \"det_minus_internal\": 40.15, \"bootstrap_90ci\": [25, 60.15]}, \"change_state\": {\"internal_mean\": -54.7, \"det_mean\": -14.5, \"oracle_mean\": 0.45, \"det_minus_internal\": 40.2, \"bootstrap_90ci\": [25, 60.15]}, \"pooled\": {\"det_minus_internal\": 40.17, \"bootstrap_90ci\": [27.6, 52.77]}, \"n_episodes_per_task\": 20, \"ci_lower_gt_0\": true, \"tasks_significant\": \"2/2\"}}, \"mvp-p1-gpu0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T05:45:22.030Z\", \"updated_at\": \"2026-05-13T09:22:26.294Z\", \"conclusion\": \"killed\", \"metrics\": {\"boil_20ep\": {\"internal_mean\": -49.8, \"det_mean\": -19.7, \"oracle_mean\": -29.7}, \"note\": \"旧代码 (>= tie-break, 无 death filter), boil 20/20 完成, melt/change-state 未跑\"}}, \"mvp-p1-gpu1-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T07:44:48.498Z\", \"updated_at\": \"2026-05-13T08:00:14.773Z\", \"conclusion\": \"killed\"}, \"mvp-p1-gpu1-vllm\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T07:10:07.454Z\", \"updated_at\": \"2026-05-13T07:43:34.463Z\", \"conclusion\": \"killed\"}, \"mvp-p1-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T05:45:20.053Z\", \"updated_at\": \"2026-05-13T07:09:59.347Z\", \"conclusion\": \"killed\"}, \"mvp-p0-forking\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T04:50:05.057Z\", \"updated_at\": \"2026-05-13T05:10:18.587Z\", \"conclusion\": \"success\", \"metrics\": {\"fork_success_rate\": 1, \"avg_latency_s\": 1.67, \"p50_latency_s\": 1.53, \"p95_latency_s\": 2.37, \"max_memory_mb\": 20, \"gate\": \"PASS\"}}}, \"count\": 49, \"total\": 49, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1831}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "f3e6f50b-7e73-4743-a8d3-9c2e91a0f8b8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan-004-ablation-b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T05:36:59.120Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:42:34.996Z\\\", \\\"hypothesis\\\": \\\"Plan-004 条件 (b) implicit router SFT：Qwen3-1.7B + LoRA, [SIMULATE] token 隐式路由。与 plan-002 (explicit router) 对比，验证路由 signal 是否需要显式分类器还是可通过 token 嵌入隐式学习。同样使用 upsample_minority 处理类别不平衡。\\\", \\\"parent\\\": \\\"plan-002-formal-v2\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"**训练实验 SUCCESS（非退化 router，internal_recall=51.52% > 30% 判定线）。e2e 部署效果 NEGATIVE 记录在 plan-003-e2e-ablation-b-correct。**\\\\n\\\\n4-seed generation-level 汇总（ga=8, upsample_minority）：\\\\n| Seed | balanced_acc | internal_recall | det_recall | accuracy |\\\\n|------|-------------|-----------------|------------|----------|\\\\n| 42   | 59.27%      | 51.52%          | 67.03%     | 65.36%   |\\\\n| 123  | 57.36%      | 57.58%          | 57.14%     | 57.19%   |\\\\n| 456  | 57.48%      | 75.76%          | 39.19%     | 43.14%   |\\\\n| 789  | 58.31%      | 81.82%          | 34.80%     | 39.87%   |\\\\n\\\\nbalanced_acc 均值 58.1±0.8%（仅比随机高 8pp）。internal_recall 波动（51-82%）是阈值效应。\\\\n\\\\n**论文定位（D033）**：Router near-random IS the finding → 强化 C1（death avoidance 主导到 router 无法从 episode-level labels 学到其他有效 signal）。\\\\n\\\\n原始 eval: accuracy=65.36%, balanced_acc=59.27%, zero logit-generation gap。Eval 脚本: eval_ablation_b_gen.py。\\\", \\\"metrics\\\": {\\\"logit_level\\\": {\\\"eval_accuracy\\\": 0.6536, \\\"eval_f1_macro\\\": 0.5091, \\\"eval_balanced_accuracy\\\": 0.5927, \\\"internal_recall\\\": 0.5152, \\\"per_class\\\": {\\\"deterministic\\\": {\\\"precision\\\": 0.9196, \\\"recall\\\": 0.6703, \\\"f1\\\": 0.7754, \\\"support\\\": 273}, \\\"internal\\\": {\\\"precision\\\": 0.1589, \\\"recall\\\": 0.5152, \\\"f1\\\": 0.2429, \\\"support\\\": 33}}, \\\"confusion\\\": {\\\"true_int_pred_int\\\": 17, \\\"true_int_pred_det\\\": 16, \\\"true_det_pred_det\\\": 183, \\\"true_det_pred_int\\\": 90}, \\\"training_loss_curve\\\": {\\\"epoch1\\\": 0.7151, \\\"epoch2\\\": 0.3928, \\\"epoch3\\\": 0.3609}}, \\\"generation_level\\\": {\\\"accuracy\\\": 0.6536, \\\"balanced_accuracy\\\": 0.5927, \\\"internal_recall\\\": 0.5152, \\\"internal_precision\\\": 0.1589, \\\"internal_f1\\\": 0.2429, \\\"det_recall\\\": 0.6703, \\\"det_precision\\\": 0.9196, \\\"det_f1\\\": 0.7754, \\\"confusion_matrix\\\": [[17, 16], [90, 183]], \\\"confusion_labels\\\": [\\\"internal\\\", \\\"deterministic\\\"], \\\"n_val\\\": 306, \\\"val_label_dist\\\": {\\\"internal\\\": 33, \\\"deterministic\\\": 273}, \\\"pred_dist\\\": {\\\"deterministic\\\": 199, \\\"internal\\\": 107}, \\\"enable_thinking\\\": false, \\\"logit_generation_gap\\\": 0, \\\"note\\\": \\\"Generation-level eval IDENTICAL to logit-level. Zero gap. Only model in project without logit-generation gap.\\\"}, \\\"is_degenerate\\\": false}}, \\\"plan-003-implicit-eval-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:27:09.398Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:27:37.907Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"Step-level implicit routing eval of ablation-b (plan-004-implicit/final_adapter) on 245 episodes / 11 tasks via eval_implicit_router.py. Score -12.84 worse than always-det baseline -9.47.\\\", \\\"metrics\\\": {\\\"continuous_score\\\": -12.84, \\\"ci_low\\\": -17.52, \\\"ci_high\\\": -8.45, \\\"success_rate\\\": 0.22, \\\"catastrophic_failure_rate\\\": 0.192, \\\"sim_invocation_ratio\\\": 0.941, \\\"step_routing_accuracy\\\": 0.602, \\\"episode_routing_accuracy\\\": 0.821, \\\"internal_recall\\\": 0.444, \\\"det_recall\\\": 0.86, \\\"routing_det\\\": 229, \\\"routing_internal\\\": 16, \\\"n_episodes\\\": 245, \\\"n_tasks\\\": 11, \\\"n_steps\\\": 2160, \\\"oracle_internal_preferred\\\": 9, \\\"oracle_det_preferred\\\": 86, \\\"oracle_no_preference\\\": 150}}, \\\"plan-003-e2e-ablation-b-correct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:21:57.921Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:24:39.892Z\\\", \\\"metrics\\\": {\\\"continuous_score_mean\\\": -10.7, \\\"continuous_score_ci_low\\\": -15.25, \\\"continuous_score_ci_high\\\": -6.38, \\\"success_rate\\\": 0.2367, \\\"death_rate\\\": 0.1755, \\\"sim_ratio\\\": 0.9703, \\\"fallback_rate\\\": 0.7061, \\\"fallback_count\\\": 173, \\\"n_episodes\\\": 245, \\\"n_tasks\\\": 11, \\\"estimated_llm_tokens\\\": 1464400, \\\"baseline_always_det\\\": -9.47, \\\"baseline_oracle\\\": -6.58, \\\"delta_vs_always_det\\\": -1.23}, \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"End-to-end eval of ablation-b (correct checkpoint: plan-004-implicit/final_adapter, internal_recall=51.52%) on 245 episodes / 11 tasks. Test C1: trained-router > always-det (-9.47).\\\", \\\"notes\\\": \\\"**NEGATIVE: trained-router (-10.70) worse than always-det (-9.47) by 1.23 pts.**\\\\n\\\\n正确 checkpoint: checkpoints/plan-004-implicit/final_adapter (ablation-b seed42)。\\\\nCI [-15.25, -6.38] 包含 -9.47，差异不显著但 point estimate 更差。\\\\n\\\\n关键指标：\\\\n- sim_ratio=97.0% — router 几乎全部路由到 deterministic\\\\n- fallback_rate=70.6% — 173/245 episodes 无 step data，直接 fallback 到 deterministic\\\\n- death_rate=17.6%\\\\n- 唯一正分 task: find-non-living-thing (+28.68, 62.5% success, 0% death)\\\\n\\\\n**论文意义**：即使项目内判别力最高的 router (balanced_acc=58.1%)，e2e 表现仍 ≤ always-det。强力支撑 C1：death avoidance 主导下 router 无法学到有效 signal，trained routing 不如简单 always-deterministic。\\\"}, \\\"plan-004-ablation-b-seed789\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:19:57.342Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:22:41.133Z\\\", \\\"hypothesis\\\": \\\"ablation-b seed 变体 (seed=789)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"generation_level\\\": {\\\"balanced_accuracy\\\": 0.5831, \\\"internal_recall\\\": 0.8182, \\\"det_recall\\\": 0.348, \\\"accuracy\\\": 0.3987}, \\\"parent\\\": \\\"plan-004-ablation-b\\\", \\\"note\\\": \\\"Seed 变体。balanced_acc ~58% 恒定，accuracy=39.87% 最低因最偏 internal。确认阈值效应。\\\"}}, \\\"plan-004-ablation-b-seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:19:56.275Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:22:39.105Z\\\", \\\"hypothesis\\\": \\\"ablation-b seed 变体 (seed=456)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"generation_level\\\": {\\\"balanced_accuracy\\\": 0.5748, \\\"internal_recall\\\": 0.7576, \\\"det_recall\\\": 0.3919, \\\"accuracy\\\": 0.4314}, \\\"parent\\\": \\\"plan-004-ablation-b\\\", \\\"note\\\": \\\"Seed 变体。balanced_acc ~58% 恒定，accuracy=43.14% 低是因为偏 internal 预测。阈值效应。\\\"}}, \\\"plan-004-ablation-b-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:19:54.935Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:22:36.972Z\\\", \\\"hypothesis\\\": \\\"ablation-b seed 变体 (seed=123)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"generation_level\\\": {\\\"balanced_accuracy\\\": 0.5736, \\\"internal_recall\\\": 0.5758, \\\"det_recall\\\": 0.5714, \\\"accuracy\\\": 0.5719}, \\\"parent\\\": \\\"plan-004-ablation-b\\\", \\\"note\\\": \\\"Seed 变体。balanced_acc ~58% 恒定，internal_recall 波动是阈值效应。Router 判别力接近随机。\\\"}}, \\\"plan-003-eval-implicit\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:11:52.155Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:12:15.517Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"continuous_score\\\": {\\\"mean\\\": -12.84, \\\"ci_low\\\": -17.52, \\\"ci_high\\\": -8.45, \\\"n\\\": 245}, \\\"success_rate\\\": {\\\"mean\\\": 0.2204, \\\"ci_low\\\": 0.1796, \\\"ci_high\\\": 0.2653}, \\\"catastrophic_failure_rate\\\": {\\\"mean\\\": 0.1918, \\\"ci_low\\\": 0.151, \\\"ci_high\\\": 0.2327}, \\\"simulator_invocation_ratio\\\": 0.9411, \\\"step_routing_accuracy\\\": {\\\"accuracy\\\": 0.6023, \\\"correct\\\": 1301, \\\"total\\\": 2160}, \\\"episode_routing_accuracy\\\": {\\\"accuracy\\\": 0.8211, \\\"correct\\\": 78, \\\"total\\\": 95}, \\\"routing_distribution\\\": {\\\"deterministic\\\": 229, \\\"internal\\\": 16}, \\\"baselines\\\": {\\\"always_internal\\\": -39.07, \\\"always_det\\\": -9.47, \\\"oracle\\\": -6.58, \\\"random\\\": -22.38}, \\\"WARNING\\\": \\\"trained router (-12.84) worse than always-det (-9.47) by 3.37 points\\\"}}, \\\"plan-003-e2e-ablation-b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:02:31.160Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:10:14.831Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"score_mean\\\": -11.11, \\\"score_ci_low\\\": -15.93, \\\"score_ci_high\\\": -6.7, \\\"death_rate\\\": 0.1796, \\\"success_rate\\\": 0.2367, \\\"sim_ratio\\\": 0.9607, \\\"fallback_rate\\\": 0.706, \\\"n_episodes\\\": 245, \\\"n_tasks\\\": 11, \\\"baseline_always_det\\\": -9.47, \\\"baseline_oracle\\\": -6.58, \\\"delta_vs_always_det\\\": -1.64}, \\\"hypothesis\\\": \\\"End-to-end eval of trained generative router (plan-002-generative-v1, internal_recall=51.5%) on 245 episodes / 11 tasks. Test C1: trained-router > always-det.\\\", \\\"notes\\\": \\\"⚠️ INVALID: 加载了错误的 checkpoint (checkpoints/plan-002-generative-v1/final_adapter = gen-v1 失败模型)，不是 ablation-b 的 checkpoints/plan-004-implicit/final_adapter。所有结果 (score=-11.11, delta_vs_always_det=-1.64) 反映的是 gen-v1 的 e2e 表现，不是 ablation-b。Reviewer 2026-05-14 发现。结果已废弃，用正确 checkpoint 重跑。\\\"}, \\\"plan-002-generative-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T07:24:07.881Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:44:34.766Z\\\", \\\"hypothesis\\\": \\\"Generative router SFT: 基于 ablation-b 成功经验（internal_recall=51.5%），用修正数据 data/plan-004-implicit/（2040 samples, 11 tasks, no-preference 已丢弃），upsample_minority=true 平衡类别（internal 180→1560），generative token prediction 而非 classification head。Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4, grad_accum=8。目标: internal_recall > 30% 且不退化。\\\", \\\"notes\\\": \\\"重新评估路由指标（generation-based eval, enable_thinking=False）。结果：accuracy=70.67%（偏高因多数类偏向），balanced_accuracy=46.67%，internal_recall=16.67%（5/30），det_recall=76.67%（207/270）。两种 thinking 模式对比：thinking_on+strip 在50 samples 上 internal_recall=0/5, thinking_off 同样 0/5。模型输出两种类别（pred: 232 det / 68 internal），但路由预测与真实标签不相关。vs ablation-b internal_recall=51.5%，generative-v1 显著退步。此前 notes 声称 internal_recall=51.85% 可能来自 logit-level eval（非 generation），不能反映实际推理行为。结论改为 negative。\\\", \\\"metrics\\\": {\\\"routing_accuracy\\\": 0.7067, \\\"balanced_accuracy\\\": 0.4667, \\\"internal_recall\\\": 0.1667, \\\"internal_precision\\\": 0.0735, \\\"internal_f1\\\": 0.102, \\\"det_recall\\\": 0.7667, \\\"det_precision\\\": 0.8922, \\\"det_f1\\\": 0.8247, \\\"val_size\\\": 300, \\\"val_label_dist\\\": {\\\"internal\\\": 30, \\\"deterministic\\\": 270}, \\\"pred_dist\\\": {\\\"deterministic\\\": 232, \\\"internal\\\": 68}, \\\"confusion_matrix\\\": [[5, 25], [63, 207]], \\\"train_final_loss\\\": 0.2, \\\"train_eval_loss\\\": 0.26, \\\"note\\\": \\\"enable_thinking=False required for Qwen3 inference; with thinking mode, model outputs &lt;think> tags causing all-internal parsing failure\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan-004-v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:02:08.110Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:29:36.639Z\\\", \\\"hypothesis\\\": \\\"Implicit router SFT v5：严格复现 ablation-b 成功条件——data/plan-004-implicit/ + upsample_minority + gradient_accumulation_steps=1（有效 batch=4）。与 v3 区别：(1) 正确数据路径（非 results/plan_c_test_labels/），(2) 加 upsample，(3) ga=1 而非 ga=8。目标：复现 ablation-b 的 internal recall ~51.5%，确认 upsample + 小 batch 是成功关键。\\\", \\\"metrics\\\": {\\\"logit_level\\\": {\\\"accuracy\\\": 0.7451, \\\"balanced_accuracy\\\": 0.7905, \\\"internal_recall\\\": 0.8485, \\\"eval_loss\\\": 0.2382, \\\"note\\\": \\\"From Trainer eval during training (logit-level, not generation)\\\"}, \\\"generation_eval\\\": {\\\"accuracy\\\": 0.5333, \\\"balanced_accuracy\\\": 0.4148, \\\"internal_recall\\\": 0.2667, \\\"internal_precision\\\": 0.0635, \\\"internal_f1\\\": 0.0941, \\\"det_recall\\\": 0.563, \\\"det_precision\\\": 0.8736, \\\"det_f1\\\": 0.6862, \\\"confusion_matrix\\\": [[152, 118], [22, 8]], \\\"confusion_labels\\\": [\\\"deterministic\\\", \\\"internal\\\"], \\\"n_val\\\": 300, \\\"val_label_dist\\\": {\\\"internal\\\": 30, \\\"deterministic\\\": 270}, \\\"pred_dist\\\": {\\\"deterministic\\\": 174, \\\"internal\\\": 126}, \\\"enable_thinking\\\": \\\"identical results for thinking_on, thinking_off, and thinking_on+strip\\\"}}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"Generation-based routing eval 推翻了此前 logit-level 的 success 结论。\\\\n\\\\n**Logit-level (Trainer eval, 训练时)**: accuracy=74.5%, balanced_acc=79.1%, internal_recall=84.9% — 看起来成功。\\\\n**Generation-based eval**: accuracy=53.3%, balanced_acc=41.5%, internal_recall=26.7% — 实际失败。\\\\n\\\\ninternal_recall=26.7% < 30% 判定线 → conclusion 改为 negative。\\\\n\\\\n三种 thinking 模式（thinking_on, thinking_off, thinking_on+strip）结果完全一致，说明 thinking mode 不是根因。\\\\n\\\\n与 ablation-b 对比: accuracy 53.3% vs 65.4%, balanced_acc 41.5% vs 59.3%, internal_recall 26.7% vs 51.5%。全面落后。\\\\n\\\\n与 plan-002-generative-v1 同样的问题模式：logit-level 指标与 generation-level 指标严重不一致。模型在 next-token prediction (loss) 层面学会了区分路由，但在自回归生成时无法可靠地输出 [SIMULATE] 前缀。\\\\n\\\\n根因推测：causal LM 的 generation 和 teacher-forcing eval 是不同的推理模式。训练时看到完整序列可以区分路由，但生成时第一个 token 的选择（是否输出 \\\\\\\"[\\\\\\\" 开始 [SIMULATE]）不够确定。\\\"}, \\\"plan-003-baseline-245eps\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:11:02.369Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:11:34.208Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"245 eps baseline results: always-int=-39.07 [-44.89,-33.37] death=42.9%; always-det=-9.47 [-13.66,-5.11] death=16.3%; oracle=-6.58 [-10.65,-2.43] death=14.3% sim=96.2%; random=-22.38 [-27.75,-17.09] death=27.8%. episode_summary.jsonl rebuilt from episodes.jsonl (old 194-ep backups saved as .bak194).\\\"}, \\\"plan-002-generative-v1-ga1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T07:59:30.209Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:03:02.054Z\\\", \\\"hypothesis\\\": \\\"Generative router SFT 对照组：与 plan-002-generative-v1 完全一致（Qwen3-1.7B + LoRA r=16, 3 epochs, upsample_minority=true, data/plan-004-implicit/），唯一区别 gradient_accumulation_steps=1（有效 batch_size=4 而非 32）。隔离 upsample + grad_accum confound：ablation-b 成功用 ga=1，v3/v4 失败用 ga=8。目标：如果 ga1 复现 ablation-b 的 internal recall ~51.5%，确认 grad_accum=8 是 v3/v4 退化的 confound。\\\", \\\"notes\\\": \\\"cuda:1 暂让给 plan-004-v5（Director 优先指令）。v5 ~3min 完成后立即提交 v1-ga1。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan-004-v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T07:16:04.007Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:38:54.065Z\\\", \\\"parent\\\": \\\"plan-004-v3\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"## 状态报告 (2026-05-14)\\\\n\\\\n### 训练完成\\\\n- 状态: DONE (EXIT_CODE=0)\\\\n- 运行时长: 150.3s (~2.5min)\\\\n- 进度: 147/147 steps, 3 epochs\\\\n- Adapter 保存: checkpoints/plan-004-v4/final_adapter\\\\n\\\\n### 数据\\\\n- 文件: results/plan_c_test_labels/implicit_sft.jsonl (1814行)\\\\n- 与 v2/v3 使用同一数据文件\\\\n- Split: 53 train / 10 val episodes → 1558 train / 256 val steps\\\\n- Route labels (train): internal=1048, deterministic=510\\\\n\\\\n### Loss 曲线\\\\n| Epoch | Train Loss | Grad Norm |\\\\n|-------|-----------|-----------|\\\\n| 0.21  | 48.1538   | 122.03    |\\\\n| 0.41  | 42.0474   | 131.02    |\\\\n| 0.62  | 26.1077   | 94.05     |\\\\n| 0.82  | 13.7082   | 51.81     |\\\\n| 1.02  | 8.463     | 36.91     |\\\\n| 1.23  | 6.8562    | 27.10     |\\\\n| 1.43  | 6.0505    | 15.74     |\\\\n| 1.64  | 5.9014    | 15.58     |\\\\n| 1.84  | 5.0414    | 10.27     |\\\\n| 2.04  | 4.5778    | 10.58     |\\\\n| 2.25  | 4.4344    | 16.18     |\\\\n| 2.45  | 4.153     | 14.26     |\\\\n| 2.66  | 4.4794    | 11.85     |\\\\n| 2.86  | 4.3672    | 14.33     |\\\\n\\\\n平均 train_loss: 12.74\\\\n\\\\n### Eval Loss\\\\n- Epoch 1: 0.9549\\\\n- Epoch 2: 0.5524\\\\n- Epoch 3: 0.4922\\\\n\\\\n### Checkpoints\\\\ncheckpoint-49, checkpoint-98, final_adapter\\\\n\\\\n### 与 v2/v3 对比（关键发现）\\\\n- **v4 step 10 loss = 48.1538，与 v2/v3 的 48.15 完全一致**\\\\n- 三个版本使用同一数据文件 (results/plan_c_test_labels/implicit_sft.jsonl)\\\\n- ablation-b 用不同数据 (data/plan-004-implicit/)，loss 正常 (0.36-0.71)\\\\n- **结论：数据文件是初始 loss 异常高的根因，非 class_weights**\\\\n\\\\n### 异常：train loss vs eval loss 巨大差距\\\\n- Train loss 终态 ~4.4 vs eval loss 0.49\\\\n- 可能原因: 训练 loss 含 class_weights 加权，eval loss 是原始 CE；或数据格式/标签问题导致训练目标与评估目标不一致\\\"}, \\\"plan-003-baseline\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T07:29:43.220Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:30:27.429Z\\\", \\\"hypothesis\\\": \\\"End-to-end evaluation baselines: always-internal, always-deterministic, oracle, random, trained-router (degenerate v6). 194 episodes / 11 tasks. 建立论文 Table 1 的 baseline 数据。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"always_internal\\\": {\\\"score\\\": -37.16, \\\"ci_90\\\": [-43.39, -31.43], \\\"success_rate\\\": 0.1237, \\\"death_rate\\\": 0.4072, \\\"sim_ratio\\\": 0}, \\\"always_deterministic\\\": {\\\"score\\\": -11.64, \\\"ci_90\\\": [-17.39, -6.55], \\\"success_rate\\\": 0.2371, \\\"death_rate\\\": 0.1856, \\\"sim_ratio\\\": 1}, \\\"oracle\\\": {\\\"score\\\": -9.03, \\\"ci_90\\\": [-14.14, -4.15], \\\"success_rate\\\": 0.2423, \\\"death_rate\\\": 0.1649, \\\"sim_ratio\\\": 0.9623}, \\\"random\\\": {\\\"score\\\": -23.75, \\\"ci_90\\\": [-29.6, -18.11], \\\"success_rate\\\": 0.1649, \\\"death_rate\\\": 0.2835, \\\"sim_ratio\\\": 0.5027}, \\\"trained_router_v6\\\": {\\\"score\\\": -11.64, \\\"ci_90\\\": [-17.39, -6.55], \\\"success_rate\\\": 0.2371, \\\"death_rate\\\": 0.1856, \\\"sim_ratio\\\": 1, \\\"note\\\": \\\"degenerate - identical to always-deterministic\\\"}, \\\"episodes\\\": 194, \\\"tasks\\\": 11}, \\\"notes\\\": \\\"Retrospectively registered. Eval ran on server by worker_code_plan-003-eval-script. Output: results/plan_003_eval/. trained-router = plan-002-formal-v6 (degenerate, all-deterministic). 需用 plan-002-generative-v1 的非退化 router 重跑 trained-router 条件。\\\"}, \\\"plan-002-formal-v6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T06:57:27.371Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:28:12.694Z\\\", \\\"notes\\\": \\\"初次启动 OOM（GPU0 内存争抢，step 30/153 被杀），自动重启 PID 240633。Epoch 1 eval: accuracy=0.929, f1_macro=0.481, f1_internal=0.0, recall_internal=0.0。去掉 class_weights 后模型在 89.7%/10.3% 不平衡数据上仍退化为全 deterministic 预测。dtype 实际为 fp32（启动早于 torch_dtype 修正）。\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan-004-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T07:06:51.091Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:24:34.751Z\\\", \\\"hypothesis\\\": \\\"Implicit router SFT v3：修复两个 bug——(1) 去掉 class_weights auto（D023 根因），(2) 用 plan_c/ 11 task 重生成数据修复 no-preference→internal 映射 bug。与 plan-002-formal-v6（explicit classification head, 同样无 class_weights）对照。2040 samples from 11 tasks, no-preference 已丢弃。\\\", \\\"parent\\\": \\\"plan-004-v2\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"## 数据文件差异分析 (2026-05-14)\\\\n\\\\n### 三个数据文件确认\\\\n| | ablation-b | v2 | v3 |\\\\n|---|---|---|---|\\\\n| 路径 | data/plan-004-implicit/implicit_sft.jsonl | results/plan_c_test_labels/implicit_sft.jsonl | data/plan-004-v3/implicit_sft.jsonl |\\\\n| MD5 | c9b59e04de78... | eb9daacc7f97... | **c9b59e04de78... (=ablation-b)** |\\\\n| 样本数 | 2040 | 1814 | 2040 |\\\\n| 文件大小 | 1,578,366 bytes | 1,398,021 bytes | 1,578,366 bytes |\\\\n\\\\n**v3 和 ablation-b 的数据文件 100% 相同（MD5 一致）。**\\\\n\\\\n### Schema（三个文件一致）\\\\nfields: messages, task_type, variation, step_idx, route_label\\\\n\\\\n### 标签分布\\\\n- ablation-b / v3: **deterministic 1830 (89.7%), internal 210 (10.3%)**\\\\n- v2: **internal 1214 (66.9%), deterministic 600 (33.1%)** ← 标签比例完全反转！\\\\n\\\\n### Task Type 分布\\\\n- ablation-b / v3: 11 个 task_type，以 find-non-living-thing(510), chemistry-mix(240) 为主\\\\n- v2: **仅 4 个 task_type**：find-non-living-thing(600), find-animal(554), grow-fruit(390), identify-life-stages-1(270)\\\\n\\\\n### 文本长度\\\\n- ablation-b / v3: n=2040, min=52, max=166, mean=87 words\\\\n- v2: n=1814, min=52, max=200, mean=90 words\\\\n\\\\n### 前 3 条样本对比\\\\nablation-b/v3 首条: chemistry-mix/variation 0/step 0, [SIMULATE] connect agent to door to kitchen, route=deterministic\\\\nv2 首条: find-non-living-thing/variation 0/step 0, [SIMULATE] connect agent to art studio door, route=deterministic\\\\n\\\\n### 训练配置对比（真正变量）\\\\n| | ablation-b (正常) | v2 (异常) | v3 (异常) |\\\\n|---|---|---|---|\\\\n| 脚本 | training/implicit_router_sft.py | 同左 | 同左 |\\\\n| 数据 | data/plan-004-implicit (2040) | results/plan_c_test_labels (1814) | data/plan-004-v3 (2040, **=ablation-b**) |\\\\n| upsample_minority | **true** | false | false |\\\\n| class_weights | 无 | \\\\\\\"auto\\\\\\\" | null |\\\\n| gradient_accumulation | 1 (默认) | 8 | 8 |\\\\n| batch_size | 4 | 4 | 4 |\\\\n| 有效batch | 4 | 32 | 32 |\\\\n\\\\n### 训练曲线对比\\\\n| | ablation-b | v2 | v3 |\\\\n|---|---|---|---|\\\\n| Step 10 loss | 5.25 | 48.15 | 48.15 (用户报告) |\\\\n| Epoch 1 eval_loss | ~0.68 | 0.95 | [无 train.log] |\\\\n| Epoch 3 eval_loss | 0.36 | **0.49 (收敛了!)** | [无 train.log] |\\\\n| 平均 train_loss | 1.26 | 12.74 | [无数据] |\\\\n\\\\n**重要发现: v2 虽然起步 loss=48，但最终 eval_loss 收敛到 0.49，模型实际上学到了。**\\\\n\\\\n### class_weights 代码分析\\\\nclass_weights 在 WeightedTrainer.compute_loss() 中正确实现：\\\\n- sample_idx 由 ImplicitSFTDataset.__getitem__() 返回 (line 85)\\\\n- PaddingCollator.__call__() 正确传递 (line 128-136)\\\\n- compute_loss() 中 `inputs.pop(\\\\\\\"sample_idx\\\\\\\")` 获取，条件 `self._class_weights is not None and sample_indices is not None` 控制 (line 227)\\\\n- v2 (class_weights=\\\\\\\"auto\\\\\\\"): 权重 internal=0.743, det=1.527，正确计算并应用\\\\n- v3 (class_weights=null): 无权重，`loss = per_sample_loss.mean()`\\\\n\\\\n**class_weights 代码本身没有 bug。v2 和 v3 的 step 10 loss 一致（48.15），证明 class_weights 不是 loss 差异的主因。** class_weights 只是对 per-sample loss 的乘法缩放（0.74x~1.53x），不会改变 loss 的数量级。\\\\n\\\\n### plan-002-formal-v6 数据路径\\\\n- 数据来源: `results/plan_c/` 目录（11 个 task_type 子目录的 labeled_steps.jsonl）\\\\n- 加载: 2040 samples from 11 files\\\\n- 标签分布: deterministic 1830 (89.7%), internal 210 (10.3%)\\\\n- 与 ablation-b 的 implicit 数据是**同源数据，但格式不同**（explicit router 用 observation+action_history+label 格式，implicit 用 messages chat 格式）\\\\n- **plan-002-formal-v6 也退化了**: 全预测 deterministic (internal: 0/30, deterministic: 390/390)\\\\n\\\\n### 结论：根因判定\\\\n\\\\n**\\\\\\\"数据文件不同\\\\\\\"假说被证伪（对 v3）**：v3 使用和 ablation-b 完全相同的数据（MD5 一致），但仍然异常。\\\\n\\\\n**真正的变量是训练策略的组合**：\\\\n1. **`upsample_minority: true`**（ablation-b 独有）：在 89.7% deterministic 的极端不平衡数据上，WeightedRandomSampler 确保 internal 样本被充分采样。没有它，模型每 batch 几乎只看到 deterministic 样本。\\\\n2. **`gradient_accumulation_steps: 1 vs 8`**：有效 batch 4 vs 32。较大 batch + 无上采样 = 每步看到的 internal 样本更少。\\\\n\\\\n**v2 的数据确实不同**（标签比例反转：internal 67% vs 10%，只有 4 个 task_type），但 v2 依然收敛了（eval_loss 0.49）。这说明数据差异导致训练行为不同，但不是致命问题。\\\\n\\\\n**建议下一步**：\\\\n- 用 ablation-b 的配置（upsample_minority=true, gradient_accumulation=1）重跑 v3 数据，验证是否恢复正常 loss\\\\n- 对 v2 跑 eval 看是否也退化\\\"}, \\\"plan-004-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T06:41:13.286Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:08:59.680Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"train_loss_avg\\\": 12.74, \\\"train_loss_epoch1\\\": [48.15, 42.05, 26.14, 13.71], \\\"train_loss_epoch3\\\": [4.58, 4.42, 4.15, 4.46, 4.36], \\\"eval_loss_epoch2\\\": 0.5509, \\\"eval_loss_epoch3\\\": 0.4905, \\\"train_runtime_sec\\\": 150.74, \\\"note\\\": \\\"no accuracy/balanced_accuracy computed\\\"}, \\\"notes\\\": \\\"Training completed normally (3 epochs, 147 steps). TRAINING_COMPLETE sentinel present. final_adapter + checkpoint-98/147 saved. train_loss=12.74 (abnormally high due to class_weights auto), eval_loss=0.490 at epoch 3. Process exited normally after completion, not OOM/crash.\\\"}, \\\"plan-002-formal-v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T06:37:37.792Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:08:19.782Z\\\", \\\"hypothesis\\\": \\\"Router SFT v5：pad_token_id fix。v3/v4 loss 异常根因确认为 model.config.pad_token_id=None（ModelScope 下载的 Qwen3-1.7B 未设置 pad_token_id，导致分类头 loss 计算错误）。Fix：模型加载后立即设 model.config.pad_token_id = tokenizer.pad_token_id (151643)。其余配置与 v4 相同：stratified split + 无 upsample + class_weights auto + 互斥检查。Qwen3-1.7B + LoRA r=16 (0.37% trainable), 3 epochs, batch_size=4 + grad_accum=8, 2040 samples (1830 det / 210 internal)。\\\", \\\"parent\\\": \\\"plan-002-formal-v4\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"train_loss_avg\\\": 5.59, \\\"eval_loss_epoch1\\\": 0.79, \\\"eval_loss_epoch2\\\": 0.78, \\\"eval_accuracy\\\": 0.9167, \\\"eval_balanced_accuracy\\\": 0.4936, \\\"eval_f1_macro\\\": 0.47, \\\"per_class\\\": {\\\"deterministic\\\": {\\\"precision\\\": 0.928, \\\"recall\\\": 0.987, \\\"f1\\\": 0.938}, \\\"internal\\\": {\\\"precision\\\": 0, \\\"recall\\\": 0, \\\"f1\\\": 0}}, \\\"class_weights\\\": {\\\"internal\\\": 4.5, \\\"deterministic\\\": 0.5625}, \\\"grad_norm_range\\\": \\\"70-604\\\", \\\"is_degenerate\\\": true, \\\"note\\\": \\\"Metrics corrected per eval_report.json (D023 Reviewer audit). class_weights auto inflates train loss (4-11) and destabilizes training (grad_norm 604). Model degenerates to all-deterministic.\\\"}, \\\"notes\\\": \\\"D021 确认：class_weights auto [4.5, 0.5625] 是 v3/v4/v5 loss 异常的根因。train_loss 4-11 (正常应 0.5-0.7)，grad_norm 604，internal recall=0。pad_token_id fix 无效（代码中已存在）。v6 对照实验：移除 class_weights，验证 loss 是否恢复正常。\\\"}, \\\"plan-002-formal-v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T06:22:49.207Z\\\", \\\"updated_at\\\": \\\"2026-05-14T07:03:55.761Z\\\", \\\"hypothesis\\\": \\\"Router SFT v4：三项修复——(1) stratified val split (sklearn train_test_split stratify=labels, val 有 30 internal + 390 det), (2) 移除 upsample_minority 只保留 class_weights auto [4.50, 0.5625], (3) 互斥检查防止过补偿。Qwen3-1.7B + LoRA r=16 (0.37% trainable), 3 epochs, batch_size=4 + grad_accum=8, 2040 samples (1830 det / 210 internal)。\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"【更正 D023】v4 实际完整训练完毕（有 TRAINING_COMPLETE + checkpoint-153 + eval_report.json），之前误标 killed。accuracy=91.9% 但 internal_recall=0%（退化为全 deterministic）。根因：class_weights [4.5, 0.5625] 使含 internal 微批次 loss 爆炸(5-11)、grad_norm 100-600，被 max_grad_norm=1.0 裁剪后 internal 有效学习率≈lr×1/600≈3e-8（等于零）。dryrun 无 class_weights 时 loss 正常(0.17-1.03)。\\\", \\\"metrics\\\": {\\\"eval_accuracy\\\": 0.919, \\\"eval_balanced_accuracy\\\": 0.5, \\\"internal_recall\\\": 0, \\\"internal_precision\\\": 0, \\\"is_degenerate\\\": true, \\\"class_weights\\\": {\\\"internal\\\": 4.5, \\\"deterministic\\\": 0.5625}, \\\"note\\\": \\\"训练完整完成（TRAINING_COMPLETE + checkpoint-153 + eval_report.json），但退化为全部预测 deterministic。之前误标 killed。真正问题：class_weights [4.5, 0.5625] + max_grad_norm=1.0 交互导致 internal 有效学习率≈0\\\"}}, \\\"plan-002-formal-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T05:46:07.817Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:09:51.858Z\\\", \\\"hypothesis\\\": \\\"Router SFT v3（本地 Qwen3-1.7B + HF_HUB_OFFLINE=1）。v1/v2 因网络不可达崩溃。v3 改用 ModelScope 本地模型 /root/autodl-tmp/models/Qwen/Qwen3-1.7B。结果：accuracy=0, f1=0, 完全失效。正在排查根因（模型 config 差异 / label mapping 问题）。\\\", \\\"parent\\\": \\\"plan-002-formal-v2\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan-012-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T06:02:42.659Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:04:07.731Z\\\", \\\"hypothesis\\\": \\\"Death decomposition 全量分析：11 tasks / 245 episodes。plan-001b 完整数据上的最终版。核心发现：death avoidance fraction=90.41%, Δ_full=29.60, Δ_nd=2.84, r=0.9698 (p=8.12e-07)。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"delta_full\\\": 29.6, \\\"delta_nd\\\": 2.84, \\\"death_avoidance_fraction\\\": 0.9041, \\\"pearson_r\\\": 0.9698, \\\"pearson_p\\\": 8.12e-07, \\\"tasks\\\": 11, \\\"episodes\\\": 245, \\\"death_rate_int\\\": 0.429, \\\"death_rate_det\\\": 0.163, \\\"label_dist\\\": {\\\"det_preferred\\\": 86, \\\"internal_preferred\\\": 9, \\\"no_preference\\\": 150}}}, \\\"plan-012-decomposition\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T00:50:01.170Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:44:02.255Z\\\", \\\"hypothesis\\\": \\\"Death decomposition 中间分析：30 tasks / 249 episodes 上验证 death avoidance 占 ~99% routing signal（预分析，plan-001b 完整数据后将重跑最终版）\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"full_11tasks\\\": {\\\"delta_full\\\": 29.6, \\\"delta_nd\\\": 2.84, \\\"death_avoidance_fraction\\\": 0.9041, \\\"pearson_r\\\": 0.9698, \\\"pearson_p\\\": 8.12e-07, \\\"tasks\\\": 11, \\\"episodes\\\": 245, \\\"death_rate_int\\\": 0.429, \\\"death_rate_det\\\": 0.163, \\\"label_dist\\\": {\\\"det_preferred\\\": 86, \\\"internal_preferred\\\": 9, \\\"no_preference\\\": 150}}, \\\"prescreening_30tasks\\\": {\\\"delta_full\\\": 37.9, \\\"delta_nd\\\": 0.2, \\\"death_avoidance_fraction\\\": 0.99, \\\"pearson_r\\\": 0.989, \\\"pearson_p\\\": \\\"<0.0001\\\", \\\"tasks\\\": 30, \\\"episodes\\\": 249}, \\\"key_tasks\\\": {\\\"find_non_living_thing\\\": {\\\"n\\\": 40, \\\"dr_int\\\": 0, \\\"dr_det\\\": 0, \\\"delta_full\\\": 9.58, \\\"delta_nd\\\": 9.58, \\\"note\\\": \\\"唯一零死亡 task, Δ_full 全部来自 non-death 性能差异\\\"}, \\\"measure_melting_point\\\": {\\\"n\\\": 20, \\\"dr_int\\\": 0.55, \\\"dr_det\\\": 0.25, \\\"delta_full\\\": 30.05, \\\"delta_pr\\\": 0.05, \\\"note\\\": \\\"高死亡率, 性能差距几乎完全由 death avoidance 解释\\\"}}}}, \\\"plan-002-formal-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T05:35:54.371Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:42:36.829Z\\\", \\\"hypothesis\\\": \\\"Router SFT 正式训练 v2（WANDB_MODE=offline 修复网络问题）：Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4 + grad_accum=8, class_weights auto + WeightedRandomSampler。v1 因 W&B 网络不可达崩溃。\\\", \\\"parent\\\": \\\"plan-002-formal\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"第二次失败，根因与 v1 相同：AutoTokenizer.from_pretrained(\\\\\\\"Qwen/Qwen3-1.7B\\\\\\\") 网络不可达 (OSError: [Errno 101] Network is unreachable)。WANDB_MODE=offline 只修了 W&B 上报，没修模型加载。Qwen3-1.7B 不在本地 HF cache。训练从未开始，wall_clock 256s 全为 HTTP retry/backoff。| 修复方案: 先用 network_turbo 或 ModelScope 下载 Qwen3-1.7B 到本地，再用 --model_name /local/path 重新提交 v3。\\\"}, \\\"plan-002-formal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T05:28:33.051Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:37:19.272Z\\\", \\\"hypothesis\\\": \\\"Router SFT 正式训练：Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4 + grad_accum=8 (有效 batch=32), class_weights auto + WeightedRandomSampler。诊断性 probe——验证 learned router 能否从 episode-level counterfactual labels 学到 routing signal（尤其 internal-preferred minority class）。Dryrun 确认 pipeline 通但 1 epoch 退化，3 epochs 应足以收敛。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: AutoTokenizer.from_pretrained(\\\\\\\"Qwen/Qwen3-1.7B\\\\\\\") 在初始化阶段崩溃——HuggingFace Hub 网络不可达 (OSError: [Errno 101] Network is unreachable) 且本地 HF cache 无此模型。训练从未开始，无 checkpoint，无任何进度。wall_clock 258s 全为 HTTP retry/backoff。| 已有成果: 无 | 建议: 找到 Qwen3-1.7B 本地路径或下载后，用 --model_name /local/path 重新提交\\\"}, \\\"plan-001b-gpu1-freeze-chem\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T02:08:29.425Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:36:34.576Z\\\", \\\"hypothesis\\\": \\\"GPU1 拆分任务：freeze 20 eps + chemistry-mix 20 eps。find-non-living-thing 完成后立即启动，与 GPU0 (lifespan-longest-lived + measure-melting-point) 并行。\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan-002-dryrun\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T05:03:05.854Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:26:39.798Z\\\", \\\"hypothesis\\\": \\\"Pipeline validation on partial data (10/11 tasks). NOT for results — verify data loading, model init, training loop, checkpoint save, eval. Will retrain on full data after chemistry-mix completes.\\\", \\\"notes\\\": \\\"dryrun-passed. Checkpoint saved: checkpoint-383 + final_adapter + eval_report.json. LoRA r=16 (0.37% trainable), 5880 samples, 1163 steps, batch_size=4. Cron 误标 failed（PID 变更导致 5× dead check），实际训练成功完成。【修正】class_weights=[11.07, 0.52] 和 WeightedRandomSampler 均已生效（WeightedCETrainer.compute_loss 覆盖 + get_train_dataloader 覆盖）。退化原因：1 epoch 不足以收敛（loss 仍在下降 0.6307→0.4762），非 class_weights 未启用。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.6307, \\\"eval_loss\\\": 0.4762, \\\"eval_accuracy\\\": 0.923, \\\"eval_f1_macro\\\": 0.48, \\\"eval_balanced_accuracy\\\": 0.5, \\\"per_class\\\": {\\\"deterministic\\\": {\\\"precision\\\": 0.923, \\\"recall\\\": 1, \\\"f1\\\": 0.96}, \\\"internal\\\": {\\\"precision\\\": 0, \\\"recall\\\": 0, \\\"f1\\\": 0}}, \\\"confusion\\\": {\\\"true_internal_pred_internal\\\": 0, \\\"true_internal_pred_det\\\": 30, \\\"true_det_pred_det\\\": 360, \\\"true_det_pred_internal\\\": 0}, \\\"per_task_eval\\\": {\\\"chemistry-mix\\\": {\\\"accuracy\\\": 0, \\\"n_samples\\\": 30}, \\\"find-animal\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"find-non-living-thing\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 90}, \\\"freeze\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"grow-fruit\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"identify-life-stages-1\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"identify-life-stages-2\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"inclined-plane-determine-angle\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"lifespan-longest-lived\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"lifespan-longest-lived-then-shortest-lived\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}, \\\"measure-melting-point-unknown-substance\\\": {\\\"accuracy\\\": 1, \\\"n_samples\\\": 30}}, \\\"samples\\\": 1920, \\\"total_steps\\\": 383, \\\"runtime_s\\\": 303.8, \\\"note\\\": \\\"DEGENERATE: 全部预测 deterministic, internal recall=0. chemistry-mix 是唯一 internal-preferred task (30 samples 全错). 正在审计 class_weights 是否真正生效。\\\"}}, \\\"gpu0-v6-lifespan\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T04:19:08.846Z\\\", \\\"updated_at\\\": \\\"2026-05-14T04:52:49.472Z\\\", \\\"hypothesis\\\": \\\"GPU0 干净重收 lifespan-longest-lived 全量 20 eps（SLIM_EPISODES=1，从 ep0 开始）。之前数据文件损坏（150GB），已删除后重启。plan-001b 最后 3 个未完成 task 之一。\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"Director 指令主动终止。lifespan-longest-lived 已收 23 eps（超额3），数据充足。GPU0 释放给 plan-002 dry-run。\\\"}, \\\"plan-001b-gpu0-v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T02:47:32.668Z\\\", \\\"updated_at\\\": \\\"2026-05-14T04:19:43.102Z\\\", \\\"hypothesis\\\": \\\"GPU0 修正重启：measure-melting-point-unknown-substance 20 eps + lifespan-longest-lived 补 1 ep (ep19)。去重后重启，使用 --reuse_dirs 防止重复。\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"Director 指令主动终止。原因：measure-melting-point 已有完整 20 eps（冗余），lifespan-longest-lived 文件损坏（150GB）。GPU0 重启做 lifespan-longest-lived 全量 20 eps 干净重收 (v6)。\\\"}, \\\"plan-001b-fnlt-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T02:05:13.793Z\\\", \\\"updated_at\\\": \\\"2026-05-14T03:12:10.756Z\\\", \\\"hypothesis\\\": \\\"find-non-living-thing 追加收集 ep 21-39 (19 eps)，补齐到 40 eps 总量。唯一 0% 死亡率 task，是 ~99% death avoidance claim 的关键 counter-example。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"find-non-living-thing\\\": {\\\"total_episodes\\\": 40, \\\"ep_range\\\": \\\"0-39\\\", \\\"no_duplicates\\\": true, \\\"no_missing\\\": true, \\\"det_pref\\\": 8, \\\"int_pref\\\": 0, \\\"no_pref\\\": 11, \\\"avg_score_gap_non_tie\\\": 40.5, \\\"note\\\": \\\"19 new eps (ep 21-39) collected. Combined with prior 21 eps. 0% death rate confirmed at 40 ep scale.\\\"}}}, \\\"plan-001b-gpu0-v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T02:06:59.924Z\\\", \\\"updated_at\\\": \\\"2026-05-14T02:47:30.101Z\\\", \\\"hypothesis\\\": \\\"GPU0 拆分任务：lifespan-longest-lived 补 4 eps (已有 16, 目标 20) + measure-melting-point-unknown-substance 全量 20 eps。与 GPU1 freeze+chemistry-mix 并行，加速 plan-001b 完成。\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"v4 崩溃（GPU0 第三次进程异常终止）。v2: vLLM EngineCore crash, v3: cleanup worker 误杀, v4: 崩溃原因待确认。数据重复已清理（lifespan-longest-lived ep 0-6 重复删除）。\\\"}, \\\"plan-001b-gpu0-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:50:46.913Z\\\", \\\"updated_at\\\": \\\"2026-05-14T02:02:40.577Z\\\", \\\"hypothesis\\\": \\\"GPU0 vLLM崩溃后重启收集：lifespan-longest-lived补5eps(ep15-19) + measure-melting-point-unknown-substance 20eps + freeze 20eps + chemistry-mix 20eps。与v2相同配置，数据可合并。\\\", \\\"notes\\\": \\\"脚本 run_gpu0_v3.sh 已创建但从未启动。GPU0 被 v2 崩溃残留的僵尸 vLLM 进程（PID 544942, 28GB VRAM）占用。4 个 task 全部未开始。需清理僵尸后重新拆分到双卡。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan-001b-gpu1-extra\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T01:46:54.844Z\\\", \\\"updated_at\\\": \\\"2026-05-14T02:02:28.988Z\\\", \\\"hypothesis\\\": \\\"find-non-living-thing 追加 19 eps（ep 21-39），补齐到 40 eps 总量。ep1-20 已收集（delta=-0.05, tied），21 eps 因 cleanup worker 误杀 SIGHUP 中断（仅完成 ep21）。唯一 0% 死亡率 task，C1 \\\\\\\"~99% death avoidance\\\\\\\" claim 的关键 counter-example。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan-001b-gpu1-rebalance\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T01:48:05.077Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:56:27.532Z\\\", \\\"hypothesis\\\": \\\"GPU 负载均衡：GPU1 接管 find-non-living-thing extra 20 eps + GPU0 未开始的 freeze/chemistry-mix 各 20 eps，加速 plan-001b 完成\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"已废弃：GPU0-v3 已接管 freeze/chemistry-mix 数据收集。find-non-living-thing extra 20 eps 由 plan-001b-gpu1-extra 独立处理。\\\"}, \\\"plan-001b-gpu1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:10:04.310Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:56:22.485Z\\\", \\\"hypothesis\\\": \\\"Episode-level data collection for 4 tasks (1 internal-pref: find-non-living-thing + 3 death-dom: grow-fruit, inclined-plane-determine-angle, identify-life-stages-2), 20 eps/task, reusing prescreening 5 eps. find-non-living-thing needs follow-up to reach 40 eps total.\\\", \\\"notes\\\": \\\"Part of plan-001b approved by Director. Tasks: find-non-living-thing (20 eps first pass, needs extra 20 to reach 40 target), grow-fruit, inclined-plane-determine-angle, identify-life-stages-2. 80 new eps this run. Follow-up needed for find-non-living extra 20 eps.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"find-non-living-thing\\\": {\\\"episodes\\\": 20, \\\"internal_mean\\\": 24.9, \\\"det_mean\\\": 24.95, \\\"delta_int_minus_det\\\": -0.05, \\\"int_deaths\\\": 0, \\\"det_deaths\\\": 0, \\\"both_deaths\\\": 0, \\\"int_only_death\\\": 0, \\\"det_only_death\\\": 0, \\\"labels\\\": {\\\"det-pref\\\": 7, \\\"int-pref\\\": 4, \\\"no-pref\\\": 9}, \\\"alive_int_mean\\\": 24.9, \\\"alive_det_mean\\\": 24.95, \\\"note\\\": \\\"Prescreening 5eps showed internal-preferred, but 20eps shows essentially TIED (delta=-0.05). Direction did NOT hold. det-pref=7 vs int-pref=4 by episode count.\\\"}, \\\"grow-fruit\\\": {\\\"episodes\\\": 20, \\\"internal_mean\\\": -43.65, \\\"det_mean\\\": -18.55, \\\"delta_int_minus_det\\\": -25.1, \\\"int_deaths\\\": 9, \\\"det_deaths\\\": 4, \\\"both_deaths\\\": 3, \\\"int_only_death\\\": 6, \\\"det_only_death\\\": 1, \\\"labels\\\": {\\\"det-pref\\\": 6, \\\"int-pref\\\": 1, \\\"no-pref\\\": 13}, \\\"alive_int_mean\\\": 2.45, \\\"alive_det_mean\\\": 1.81, \\\"note\\\": \\\"Death-dominated confirmed. Internal dies 6x exclusively vs det 1x. Alive scores low and similar.\\\"}, \\\"inclined-plane-determine-angle\\\": {\\\"episodes\\\": 20, \\\"internal_mean\\\": -55, \\\"det_mean\\\": -19, \\\"delta_int_minus_det\\\": -36, \\\"int_deaths\\\": 11, \\\"det_deaths\\\": 4, \\\"both_deaths\\\": 4, \\\"int_only_death\\\": 7, \\\"det_only_death\\\": 0, \\\"labels\\\": {\\\"det-pref\\\": 7, \\\"int-pref\\\": 0, \\\"no-pref\\\": 13}, \\\"alive_int_mean\\\": 0, \\\"alive_det_mean\\\": 1.25, \\\"note\\\": \\\"Most extreme death-dominated. Internal dies 7x exclusively, det never dies alone. Internal NEVER preferred (0/20). Alive scores near zero.\\\"}, \\\"identify-life-stages-2\\\": {\\\"episodes\\\": 20, \\\"internal_mean\\\": -48.4, \\\"det_mean\\\": -18.4, \\\"delta_int_minus_det\\\": -30, \\\"int_deaths\\\": 10, \\\"det_deaths\\\": 4, \\\"both_deaths\\\": 4, \\\"int_only_death\\\": 6, \\\"det_only_death\\\": 0, \\\"labels\\\": {\\\"det-pref\\\": 6, \\\"int-pref\\\": 0, \\\"no-pref\\\": 14}, \\\"alive_int_mean\\\": 3.2, \\\"alive_det_mean\\\": 2, \\\"note\\\": \\\"Death-dominated confirmed. Internal dies 6x exclusively, det never alone. Internal NEVER preferred (0/20).\\\"}, \\\"summary\\\": {\\\"total_episodes\\\": 80, \\\"all_tasks_complete\\\": true, \\\"death_dominated_tasks\\\": [\\\"grow-fruit\\\", \\\"inclined-plane-determine-angle\\\", \\\"identify-life-stages-2\\\"], \\\"internal_preferred_tasks\\\": [], \\\"key_finding\\\": \\\"find-non-living-thing prescreening signal (internal>det) did NOT replicate at 20 eps — essentially tied. All 3 death-dom tasks confirmed: internal router causes significantly more deaths than deterministic.\\\"}}}, \\\"plan-001b-gpu0-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:31:47.627Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:51:26.200Z\\\", \\\"hypothesis\\\": \\\"Episode-level data collection for 7 tasks (5 genuine-det + 2 death-dom), 20 eps/task. v2: added cleanup_gpu_processes() to prevent orphan vLLM processes.\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"GPU0 第二次失败。根因：vLLM EngineCore 在 Episode 15 deterministic 模式中意外死亡 (EngineDeadError)。v2 的 cleanup_gpu_processes() 只清理启动前孤儿，未防运行中崩溃。诊断 Worker: worker_diagnose_plan-001b-gpu0-v2_20260514T015111\\\"}, \\\"plan-011-rule-based\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T00:51:12.911Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:00:59.327Z\\\", \\\"hypothesis\\\": \\\"Rule-based keyword routing baseline：测试 keyword heuristic 能否捕获 episode-level routing signal。三版 keyword list 均结构性失效——v1 (含 connect) ≈ always-det, v2 (科学词) ≈ always-internal, v3 (状态变化动词) ≈ always-internal。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"v1_match_rate\\\": \\\"85.8%\\\", \\\"v1_result\\\": \\\"degenerate → always-det\\\", \\\"v2_match_rate\\\": \\\"4.9%\\\", \\\"v2_result\\\": \\\"degenerate → always-internal\\\", \\\"v3_match_rate\\\": \\\"2.8%\\\", \\\"v3_episode_accuracy\\\": \\\"1.5%\\\", \\\"v3_result\\\": \\\"degenerate → always-internal\\\", \\\"conclusion\\\": \\\"Keyword heuristic structurally fails on ScienceWorld — ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords. No keyword list provides meaningful routing signal.\\\", \\\"note\\\": \\\"D014: structural failure analysis, paper positions as evidence for learned/observation-based approaches\\\"}, \\\"notes\\\": \\\"v1 204 vs v2 203 episode 差异原因：竞态条件——v2 报告在 lifespan-shortest-lived/episodes.jsonl 创建前 15 秒生成。非方法论问题。当前重跑两版均为 233 episodes。论文统一引用最终 plan-001b 完整数据的 episode 基数。\\\"}, \\\"plan-001b-gpu0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T22:10:02.679Z\\\", \\\"updated_at\\\": \\\"2026-05-13T22:33:15.743Z\\\", \\\"hypothesis\\\": \\\"Episode-level data collection for 7 tasks (5 genuine-det: find-animal, identify-life-stages-1, lifespan-longest-lived-then-shortest, lifespan-longest-lived, measure-melting-point-unknown + 2 death-dom: freeze, chemistry-mix), 20 eps/task, reusing prescreening 5 eps\\\", \\\"notes\\\": \\\"Part of plan-001b approved by Director. Tasks: find-animal, identify-life-stages-1, lifespan-longest-lived-then-shortest-lived, lifespan-longest-lived, measure-melting-point-unknown-substance, freeze, chemistry-mix. 105 new eps (15 each × 7 tasks). Watch measure-melting-point-unknown death_avoidance_fraction=0.38 outlier per Reviewer note.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"research-prescreening-gpu0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T16:20:17.197Z\\\", \\\"updated_at\\\": \\\"2026-05-13T22:09:59.200Z\\\", \\\"hypothesis\\\": \\\"Fork-based deterministic evaluation 在 ScienceWorld 30 个 task types 中广泛有效（预筛 25 个未测 task，5 ep/task，识别 signal 方向）\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"research-prescreening-gpu1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T19:53:28.002Z\\\", \\\"updated_at\\\": \\\"2026-05-13T22:08:01.696Z\\\", \\\"hypothesis\\\": \\\"GPU1 加入 plan-001a 预筛，跑剩余 8 个 task types（measure-melting-point-unknown-substance, mendelian-genetics-known/unknown-plant, power-component x2, test-conductivity x2, use-thermometer），加速完成全部 25 tasks\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tasks_completed\\\": \\\"8/8\\\", \\\"all_direction\\\": \\\"POSITIVE\\\", \\\"results\\\": {\\\"measure-melting-point-unknown-substance\\\": {\\\"int_mean\\\": -58.6, \\\"det_mean\\\": -32, \\\"delta\\\": 26.6, \\\"signal\\\": \\\"death-dominated\\\"}, \\\"mendelian-genetics-known-plant\\\": {\\\"int_mean\\\": -60, \\\"det_mean\\\": -20, \\\"delta\\\": 40, \\\"signal\\\": \\\"death-dominated\\\"}, \\\"mendelian-genetics-unknown-plant\\\": {\\\"int_mean\\\": -60, \\\"det_mean\\\": -40, \\\"delta\\\": 20, \\\"signal\\\": \\\"death-dominated\\\"}, \\\"power-component\\\": {\\\"int_mean\\\": -60, \\\"det_mean\\\": -20, \\\"delta\\\": 40, \\\"signal\\\": \\\"death-dominated\\\"}, \\\"power-component-renewable-vs-nonrenewable-energy\\\": {\\\"int_mean\\\": -60, \\\"det_mean\\\": 0, \\\"delta\\\": 60, \\\"signal\\\": \\\"death-dominated\\\"}, \\\"test-conductivity\\\": {\\\"int_mean\\\": -60, \\\"det_mean\\\": -20, \\\"delta\\\": 40, \\\"signal\\\": \\\"death-dominated\\\"}, \\\"test-conductivity-of-unknown-substances\\\": {\\\"int_mean\\\": -60, \\\"det_mean\\\": -20, \\\"delta\\\": 40, \\\"signal\\\": \\\"death-dominated\\\"}, \\\"use-thermometer\\\": {\\\"int_mean\\\": -59.4, \\\"det_mean\\\": -19.4, \\\"delta\\\": 40, \\\"signal\\\": \\\"death-dominated\\\"}}, \\\"summary\\\": \\\"All 8 tasks death-dominated: internal mode hits -100 (lethal) in 3/5 episodes; deterministic mode avoids most deaths but scores remain ~0 (no genuine task progress). Delta driven by death avoidance, not task solving.\\\"}}, \\\"mvp-p1-signal\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-13T04:50:06.546Z\\\", \\\"updated_at\\\": \\\"2026-05-13T21:46:23.662Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"research-boil-v3-gpu1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T16:20:17.657Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:50:37.666Z\\\", \\\"hypothesis\\\": \\\"用统一 v3 代码（> tie-break + death filter 仅 det/oracle）重跑 boil 20ep，获得与其他 4 个 task 一致的代码版本数据\\\", \\\"parent\\\": \\\"mvp-p1-gpu0\\\", \\\"notes\\\": \\\"Registry 状态 ANALYZING 但 cron reconcile 确认 PID 650421 仍存活（16/20 episodes 完成）。实际仍在 RUNNING。状态机不允许回退 ANALYZING→RUNNING，等完成后直接转 DONE。\\\", \\\"metrics\\\": {\\\"boil_v3_20ep\\\": {\\\"internal_mean\\\": -44.7, \\\"internal_std\\\": 50, \\\"det_mean\\\": -9.3, \\\"det_std\\\": 30.3, \\\"oracle_mean\\\": 3.8, \\\"oracle_std\\\": 15.2, \\\"oracle_minus_internal\\\": 48.5, \\\"oracle_minus_det\\\": 13.1, \\\"det_minus_internal\\\": 35.4}, \\\"death_distribution\\\": {\\\"internal_deaths\\\": 9, \\\"internal_total\\\": 20, \\\"internal_death_pct\\\": 45, \\\"det_deaths\\\": 2, \\\"det_total\\\": 20, \\\"det_death_pct\\\": 10, \\\"oracle_deaths\\\": 0, \\\"oracle_total\\\": 20, \\\"oracle_death_pct\\\": 0}, \\\"note\\\": \\\"v3 code (> tie-break, death filter det/oracle only). Oracle大幅优于两个baseline, 但绝对分低(3.8), 仅1/20 episode拿到70分. Death avoidance is primary mechanism.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"research-cf-pilot-gpu1\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"created_at\\\": \\\"2026-05-13T17:15:37.908Z\\\", \\\"updated_at\\\": \\\"2026-05-13T17:17:23.652Z\\\", \\\"hypothesis\\\": \\\"Episode-terminal counterfactual labeling (K=10) 在 melt/change-state/mix-paint 上产生 >30% non-tie rate，为 router 训练提供有效信号\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp-p1-gpu1-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T08:00:51.836Z\\\", \\\"updated_at\\\": \\\"2026-05-13T15:41:04.061Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mix_paint\\\": {\\\"internal_mean\\\": -41, \\\"det_mean\\\": -5.5, \\\"oracle_mean\\\": 4.5, \\\"det_minus_internal\\\": 35.5, \\\"bootstrap_90ci\\\": [20, 55]}, \\\"grow_plant\\\": {\\\"internal_mean\\\": 0.5, \\\"det_mean\\\": 0.5, \\\"oracle_mean\\\": 0.5, \\\"det_minus_internal\\\": 0, \\\"bootstrap_90ci\\\": [0, 0]}, \\\"n_episodes_per_task\\\": 20, \\\"tasks_significant\\\": \\\"1/2\\\", \\\"note\\\": \\\"grow-plant: NO_EFFECT (三种模式完全相同); mix-paint: 显著正向\\\"}}, \\\"mvp-p1-gpu0-vllm\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T09:18:47.128Z\\\", \\\"updated_at\\\": \\\"2026-05-13T15:17:57.586Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"melt\\\": {\\\"internal_mean\\\": -54.7, \\\"det_mean\\\": -14.55, \\\"oracle_mean\\\": 2.15, \\\"det_minus_internal\\\": 40.15, \\\"bootstrap_90ci\\\": [25, 60.15]}, \\\"change_state\\\": {\\\"internal_mean\\\": -54.7, \\\"det_mean\\\": -14.5, \\\"oracle_mean\\\": 0.45, \\\"det_minus_internal\\\": 40.2, \\\"bootstrap_90ci\\\": [25, 60.15]}, \\\"pooled\\\": {\\\"det_minus_internal\\\": 40.17, \\\"bootstrap_90ci\\\": [27.6, 52.77]}, \\\"n_episodes_per_task\\\": 20, \\\"ci_lower_gt_0\\\": true, \\\"tasks_significant\\\": \\\"2/2\\\"}}, \\\"mvp-p1-gpu0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T05:45:22.030Z\\\", \\\"updated_at\\\": \\\"2026-05-13T09:22:26.294Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"boil_20ep\\\": {\\\"internal_mean\\\": -49.8, \\\"det_mean\\\": -19.7, \\\"oracle_mean\\\": -29.7}, \\\"note\\\": \\\"旧代码 (>= tie-break, 无 death filter), boil 20/20 完成, melt/change-state 未跑\\\"}}, \\\"mvp-p1-gpu1-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T07:44:48.498Z\\\", \\\"updated_at\\\": \\\"2026-05-13T08:00:14.773Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp-p1-gpu1-vllm\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T07:10:07.454Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:43:34.463Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp-p1-gpu1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T05:45:20.053Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:09:59.347Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp-p0-forking\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-13T04:50:05.057Z\\\", \\\"updated_at\\\": \\\"2026-05-13T05:10:18.587Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"fork_success_rate\\\": 1, \\\"avg_latency_s\\\": 1.67, \\\"p50_latency_s\\\": 1.53, \\\"p95_latency_s\\\": 2.37, \\\"max_memory_mb\\\": 20, \\\"gate\\\": \\\"PASS\\\"}}}, \\\"count\\\": 49, \\\"total\\\": 49, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1831}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan-004-ablation-b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:36:59.120Z\", \"updated_at\": \"2026-05-14T09:42:34.996Z\", \"hypothesis\": \"Plan-004 条件 (b) implicit router SFT：Qwen3-1.7B + LoRA, [SIMULATE] token 隐式路由。与 plan-002 (explicit router) 对比，验证路由 signal 是否需要显式分类器还是可通过 token 嵌入隐式学习。同样使用 upsample_minority 处理类别不平衡。\", \"parent\": \"plan-002-formal-v2\", \"conclusion\": \"success\", \"notes\": \"**训练实验 SUCCESS（非退化 router，internal_recall=51.52% > 30% 判定线）。e2e 部署效果 NEGATIVE 记录在 plan-003-e2e-ablation-b-correct。**\\n\\n4-seed generation-level 汇总（ga=8, upsample_minority）：\\n| Seed | balanced_acc | internal_recall | det_recall | accuracy |\\n|------|-------------|-----------------|------------|----------|\\n| 42   | 59.27%      | 51.52%          | 67.03%     | 65.36%   |\\n| 123  | 57.36%      | 57.58%          | 57.14%     | 57.19%   |\\n| 456  | 57.48%      | 75.76%          | 39.19%     | 43.14%   |\\n| 789  | 58.31%      | 81.82%          | 34.80%     | 39.87%   |\\n\\nbalanced_acc 均值 58.1±0.8%（仅比随机高 8pp）。internal_recall 波动（51-82%）是阈值效应。\\n\\n**论文定位（D033）**：Router near-random IS the finding → 强化 C1（death avoidance 主导到 router 无法从 episode-level labels 学到其他有效 signal）。\\n\\n原始 eval: accuracy=65.36%, balanced_acc=59.27%, zero logit-generation gap。Eval 脚本: eval_ablation_b_gen.py。\", \"metrics\": {\"logit_level\": {\"eval_accuracy\": 0.6536, \"eval_f1_macro\": 0.5091, \"eval_balanced_accuracy\": 0.5927, \"internal_recall\": 0.5152, \"per_class\": {\"deterministic\": {\"precision\": 0.9196, \"recall\": 0.6703, \"f1\": 0.7754, \"support\": 273}, \"internal\": {\"precision\": 0.1589, \"recall\": 0.5152, \"f1\": 0.2429, \"support\": 33}}, \"confusion\": {\"true_int_pred_int\": 17, \"true_int_pred_det\": 16, \"true_det_pred_det\": 183, \"true_det_pred_int\": 90}, \"training_loss_curve\": {\"epoch1\": 0.7151, \"epoch2\": 0.3928, \"epoch3\": 0.3609}}, \"generation_level\": {\"accuracy\": 0.6536, \"balanced_accuracy\": 0.5927, \"internal_recall\": 0.5152, \"internal_precision\": 0.1589, \"internal_f1\": 0.2429, \"det_recall\": 0.6703, \"det_precision\": 0.9196, \"det_f1\": 0.7754, \"confusion_matrix\": [[17, 16], [90, 183]], \"confusion_labels\": [\"internal\", \"deterministic\"], \"n_val\": 306, \"val_label_dist\": {\"internal\": 33, \"deterministic\": 273}, \"pred_dist\": {\"deterministic\": 199, \"internal\": 107}, \"enable_thinking\": false, \"logit_generation_gap\": 0, \"note\": \"Generation-level eval IDENTICAL to logit-level. Zero gap. Only model in project without logit-generation gap.\"}, \"is_degenerate\": false}}, \"plan-003-implicit-eval-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:27:09.398Z\", \"updated_at\": \"2026-05-14T09:27:37.907Z\", \"conclusion\": \"negative\", \"hypothesis\": \"Step-level implicit routing eval of ablation-b (plan-004-implicit/final_adapter) on 245 episodes / 11 tasks via eval_implicit_router.py. Score -12.84 worse than always-det baseline -9.47.\", \"metrics\": {\"continuous_score\": -12.84, \"ci_low\": -17.52, \"ci_high\": -8.45, \"success_rate\": 0.22, \"catastrophic_failure_rate\": 0.192, \"sim_invocation_ratio\": 0.941, \"step_routing_accuracy\": 0.602, \"episode_routing_accuracy\": 0.821, \"internal_recall\": 0.444, \"det_recall\": 0.86, \"routing_det\": 229, \"routing_internal\": 16, \"n_episodes\": 245, \"n_tasks\": 11, \"n_steps\": 2160, \"oracle_internal_preferred\": 9, \"oracle_det_preferred\": 86, \"oracle_no_preference\": 150}}, \"plan-003-e2e-ablation-b-correct\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:21:57.921Z\", \"updated_at\": \"2026-05-14T09:24:39.892Z\", \"metrics\": {\"continuous_score_mean\": -10.7, \"continuous_score_ci_low\": -15.25, \"continuous_score_ci_high\": -6.38, \"success_rate\": 0.2367, \"death_rate\": 0.1755, \"sim_ratio\": 0.9703, \"fallback_rate\": 0.7061, \"fallback_count\": 173, \"n_episodes\": 245, \"n_tasks\": 11, \"estimated_llm_tokens\": 1464400, \"baseline_always_det\": -9.47, \"baseline_oracle\": -6.58, \"delta_vs_always_det\": -1.23}, \"conclusion\": \"negative\", \"hypothesis\": \"End-to-end eval of ablation-b (correct checkpoint: plan-004-implicit/final_adapter, internal_recall=51.52%) on 245 episodes / 11 tasks. Test C1: trained-router > always-det (-9.47).\", \"notes\": \"**NEGATIVE: trained-router (-10.70) worse than always-det (-9.47) by 1.23 pts.**\\n\\n正确 checkpoint: checkpoints/plan-004-implicit/final_adapter (ablation-b seed42)。\\nCI [-15.25, -6.38] 包含 -9.47，差异不显著但 point estimate 更差。\\n\\n关键指标：\\n- sim_ratio=97.0% — router 几乎全部路由到 deterministic\\n- fallback_rate=70.6% — 173/245 episodes 无 step data，直接 fallback 到 deterministic\\n- death_rate=17.6%\\n- 唯一正分 task: find-non-living-thing (+28.68, 62.5% success, 0% death)\\n\\n**论文意义**：即使项目内判别力最高的 router (balanced_acc=58.1%)，e2e 表现仍 ≤ always-det。强力支撑 C1：death avoidance 主导下 router 无法学到有效 signal，trained routing 不如简单 always-deterministic。\"}, \"plan-004-ablation-b-seed789\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:57.342Z\", \"updated_at\": \"2026-05-14T09:22:41.133Z\", \"hypothesis\": \"ablation-b seed 变体 (seed=789)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\", \"conclusion\": \"negative\", \"metrics\": {\"generation_level\": {\"balanced_accuracy\": 0.5831, \"internal_recall\": 0.8182, \"det_recall\": 0.348, \"accuracy\": 0.3987}, \"parent\": \"plan-004-ablation-b\", \"note\": \"Seed 变体。balanced_acc ~58% 恒定，accuracy=39.87% 最低因最偏 internal。确认阈值效应。\"}}, \"plan-004-ablation-b-seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:56.275Z\", \"updated_at\": \"2026-05-14T09:22:39.105Z\", \"hypothesis\": \"ablation-b seed 变体 (seed=456)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\", \"conclusion\": \"negative\", \"metrics\": {\"generation_level\": {\"balanced_accuracy\": 0.5748, \"internal_recall\": 0.7576, \"det_recall\": 0.3919, \"accuracy\": 0.4314}, \"parent\": \"plan-004-ablation-b\", \"note\": \"Seed 变体。balanced_acc ~58% 恒定，accuracy=43.14% 低是因为偏 internal 预测。阈值效应。\"}}, \"plan-004-ablation-b-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:54.935Z\", \"updated_at\": \"2026-05-14T09:22:36.972Z\", \"hypothesis\": \"ablation-b seed 变体 (seed=123)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。\", \"conclusion\": \"negative\", \"metrics\": {\"generation_level\": {\"balanced_accuracy\": 0.5736, \"internal_recall\": 0.5758, \"det_recall\": 0.5714, \"accuracy\": 0.5719}, \"parent\": \"plan-004-ablation-b\", \"note\": \"Seed 变体。balanced_acc ~58% 恒定，internal_recall 波动是阈值效应。Router 判别力接近随机。\"}}, \"plan-003-eval-implicit\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:11:52.155Z\", \"updated_at\": \"2026-05-14T09:12:15.517Z\", \"conclusion\": \"negative\", \"metrics\": {\"continuous_score\": {\"mean\": -12.84, \"ci_low\": -17.52, \"ci_high\": -8.45, \"n\": 245}, \"success_rate\": {\"mean\": 0.2204, \"ci_low\": 0.1796, \"ci_high\": 0.2653}, \"catastrophic_failure_rate\": {\"mean\": 0.1918, \"ci_low\": 0.151, \"ci_high\": 0.2327}, \"simulator_invocation_ratio\": 0.9411, \"step_routing_accuracy\": {\"accuracy\": 0.6023, \"correct\": 1301, \"total\": 2160}, \"episode_routing_accuracy\": {\"accuracy\": 0.8211, \"correct\": 78, \"total\": 95}, \"routing_distribution\": {\"deterministic\": 229, \"internal\": 16}, \"baselines\": {\"always_internal\": -39.07, \"always_det\": -9.47, \"oracle\": -6.58, \"random\": -22.38}, \"WARNING\": \"trained router (-12.84) worse than always-det (-9.47) by 3.37 points\"}}, \"plan-003-e2e-ablation-b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:02:31.160Z\", \"updated_at\": \"2026-05-14T09:10:14.831Z\", \"conclusion\": \"failed\", \"metrics\": {\"score_mean\": -11.11, \"score_ci_low\": -15.93, \"score_ci_high\": -6.7, \"death_rate\": 0.1796, \"success_rate\": 0.2367, \"sim_ratio\": 0.9607, \"fallback_rate\": 0.706, \"n_episodes\": 245, \"n_tasks\": 11, \"baseline_always_det\": -9.47, \"baseline_oracle\": -6.58, \"delta_vs_always_det\": -1.64}, \"hypothesis\": \"End-to-end eval of trained generative router (plan-002-generative-v1, internal_recall=51.5%) on 245 episodes / 11 tasks. Test C1: trained-router > always-det.\", \"notes\": \"⚠️ INVALID: 加载了错误的 checkpoint (checkpoints/plan-002-generative-v1/final_adapter = gen-v1 失败模型)，不是 ablation-b 的 checkpoints/plan-004-implicit/final_adapter。所有结果 (score=-11.11, delta_vs_always_det=-1.64) 反映的是 gen-v1 的 e2e 表现，不是 ablation-b。Reviewer 2026-05-14 发现。结果已废弃，用正确 checkpoint 重跑。\"}, \"plan-002-generative-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:24:07.881Z\", \"updated_at\": \"2026-05-14T08:44:34.766Z\", \"hypothesis\": \"Generative router SFT: 基于 ablation-b 成功经验（internal_recall=51.5%），用修正数据 data/plan-004-implicit/（2040 samples, 11 tasks, no-preference 已丢弃），upsample_minority=true 平衡类别（internal 180→1560），generative token prediction 而非 classification head。Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4, grad_accum=8。目标: internal_recall > 30% 且不退化。\", \"notes\": \"重新评估路由指标（generation-based eval, enable_thinking=False）。结果：accuracy=70.67%（偏高因多数类偏向），balanced_accuracy=46.67%，internal_recall=16.67%（5/30），det_recall=76.67%（207/270）。两种 thinking 模式对比：thinking_on+strip 在50 samples 上 internal_recall=0/5, thinking_off 同样 0/5。模型输出两种类别（pred: 232 det / 68 internal），但路由预测与真实标签不相关。vs ablation-b internal_recall=51.5%，generative-v1 显著退步。此前 notes 声称 internal_recall=51.85% 可能来自 logit-level eval（非 generation），不能反映实际推理行为。结论改为 negative。\", \"metrics\": {\"routing_accuracy\": 0.7067, \"balanced_accuracy\": 0.4667, \"internal_recall\": 0.1667, \"internal_precision\": 0.0735, \"internal_f1\": 0.102, \"det_recall\": 0.7667, \"det_precision\": 0.8922, \"det_f1\": 0.8247, \"val_size\": 300, \"val_label_dist\": {\"internal\": 30, \"deterministic\": 270}, \"pred_dist\": {\"deterministic\": 232, \"internal\": 68}, \"confusion_matrix\": [[5, 25], [63, 207]], \"train_final_loss\": 0.2, \"train_eval_loss\": 0.26, \"note\": \"enable_thinking=False required for Qwen3 inference; with thinking mode, model outputs &lt;think> tags causing all-internal parsing failure\"}, \"conclusion\": \"negative\"}, \"plan-004-v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:02:08.110Z\", \"updated_at\": \"2026-05-14T08:29:36.639Z\", \"hypothesis\": \"Implicit router SFT v5：严格复现 ablation-b 成功条件——data/plan-004-implicit/ + upsample_minority + gradient_accumulation_steps=1（有效 batch=4）。与 v3 区别：(1) 正确数据路径（非 results/plan_c_test_labels/），(2) 加 upsample，(3) ga=1 而非 ga=8。目标：复现 ablation-b 的 internal recall ~51.5%，确认 upsample + 小 batch 是成功关键。\", \"metrics\": {\"logit_level\": {\"accuracy\": 0.7451, \"balanced_accuracy\": 0.7905, \"internal_recall\": 0.8485, \"eval_loss\": 0.2382, \"note\": \"From Trainer eval during training (logit-level, not generation)\"}, \"generation_eval\": {\"accuracy\": 0.5333, \"balanced_accuracy\": 0.4148, \"internal_recall\": 0.2667, \"internal_precision\": 0.0635, \"internal_f1\": 0.0941, \"det_recall\": 0.563, \"det_precision\": 0.8736, \"det_f1\": 0.6862, \"confusion_matrix\": [[152, 118], [22, 8]], \"confusion_labels\": [\"deterministic\", \"internal\"], \"n_val\": 300, \"val_label_dist\": {\"internal\": 30, \"deterministic\": 270}, \"pred_dist\": {\"deterministic\": 174, \"internal\": 126}, \"enable_thinking\": \"identical results for thinking_on, thinking_off, and thinking_on+strip\"}}, \"conclusion\": \"negative\", \"notes\": \"Generation-based routing eval 推翻了此前 logit-level 的 success 结论。\\n\\n**Logit-level (Trainer eval, 训练时)**: accuracy=74.5%, balanced_acc=79.1%, internal_recall=84.9% — 看起来成功。\\n**Generation-based eval**: accuracy=53.3%, balanced_acc=41.5%, internal_recall=26.7% — 实际失败。\\n\\ninternal_recall=26.7% < 30% 判定线 → conclusion 改为 negative。\\n\\n三种 thinking 模式（thinking_on, thinking_off, thinking_on+strip）结果完全一致，说明 thinking mode 不是根因。\\n\\n与 ablation-b 对比: accuracy 53.3% vs 65.4%, balanced_acc 41.5% vs 59.3%, internal_recall 26.7% vs 51.5%。全面落后。\\n\\n与 plan-002-generative-v1 同样的问题模式：logit-level 指标与 generation-level 指标严重不一致。模型在 next-token prediction (loss) 层面学会了区分路由，但在自回归生成时无法可靠地输出 [SIMULATE] 前缀。\\n\\n根因推测：causal LM 的 generation 和 teacher-forcing eval 是不同的推理模式。训练时看到完整序列可以区分路由，但生成时第一个 token 的选择（是否输出 \\\"[\\\" 开始 [SIMULATE]）不够确定。\"}, \"plan-003-baseline-245eps\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:11:02.369Z\", \"updated_at\": \"2026-05-14T08:11:34.208Z\", \"conclusion\": \"success\", \"notes\": \"245 eps baseline results: always-int=-39.07 [-44.89,-33.37] death=42.9%; always-det=-9.47 [-13.66,-5.11] death=16.3%; oracle=-6.58 [-10.65,-2.43] death=14.3% sim=96.2%; random=-22.38 [-27.75,-17.09] death=27.8%. episode_summary.jsonl rebuilt from episodes.jsonl (old 194-ep backups saved as .bak194).\"}, \"plan-002-generative-v1-ga1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:59:30.209Z\", \"updated_at\": \"2026-05-14T08:03:02.054Z\", \"hypothesis\": \"Generative router SFT 对照组：与 plan-002-generative-v1 完全一致（Qwen3-1.7B + LoRA r=16, 3 epochs, upsample_minority=true, data/plan-004-implicit/），唯一区别 gradient_accumulation_steps=1（有效 batch_size=4 而非 32）。隔离 upsample + grad_accum confound：ablation-b 成功用 ga=1，v3/v4 失败用 ga=8。目标：如果 ga1 复现 ablation-b 的 internal recall ~51.5%，确认 grad_accum=8 是 v3/v4 退化的 confound。\", \"notes\": \"cuda:1 暂让给 plan-004-v5（Director 优先指令）。v5 ~3min 完成后立即提交 v1-ga1。\", \"conclusion\": \"killed\"}, \"plan-004-v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:16:04.007Z\", \"updated_at\": \"2026-05-14T07:38:54.065Z\", \"parent\": \"plan-004-v3\", \"conclusion\": \"negative\", \"notes\": \"## 状态报告 (2026-05-14)\\n\\n### 训练完成\\n- 状态: DONE (EXIT_CODE=0)\\n- 运行时长: 150.3s (~2.5min)\\n- 进度: 147/147 steps, 3 epochs\\n- Adapter 保存: checkpoints/plan-004-v4/final_adapter\\n\\n### 数据\\n- 文件: results/plan_c_test_labels/implicit_sft.jsonl (1814行)\\n- 与 v2/v3 使用同一数据文件\\n- Split: 53 train / 10 val episodes → 1558 train / 256 val steps\\n- Route labels (train): internal=1048, deterministic=510\\n\\n### Loss 曲线\\n| Epoch | Train Loss | Grad Norm |\\n|-------|-----------|-----------|\\n| 0.21  | 48.1538   | 122.03    |\\n| 0.41  | 42.0474   | 131.02    |\\n| 0.62  | 26.1077   | 94.05     |\\n| 0.82  | 13.7082   | 51.81     |\\n| 1.02  | 8.463     | 36.91     |\\n| 1.23  | 6.8562    | 27.10     |\\n| 1.43  | 6.0505    | 15.74     |\\n| 1.64  | 5.9014    | 15.58     |\\n| 1.84  | 5.0414    | 10.27     |\\n| 2.04  | 4.5778    | 10.58     |\\n| 2.25  | 4.4344    | 16.18     |\\n| 2.45  | 4.153     | 14.26     |\\n| 2.66  | 4.4794    | 11.85     |\\n| 2.86  | 4.3672    | 14.33     |\\n\\n平均 train_loss: 12.74\\n\\n### Eval Loss\\n- Epoch 1: 0.9549\\n- Epoch 2: 0.5524\\n- Epoch 3: 0.4922\\n\\n### Checkpoints\\ncheckpoint-49, checkpoint-98, final_adapter\\n\\n### 与 v2/v3 对比（关键发现）\\n- **v4 step 10 loss = 48.1538，与 v2/v3 的 48.15 完全一致**\\n- 三个版本使用同一数据文件 (results/plan_c_test_labels/implicit_sft.jsonl)\\n- ablation-b 用不同数据 (data/plan-004-implicit/)，loss 正常 (0.36-0.71)\\n- **结论：数据文件是初始 loss 异常高的根因，非 class_weights**\\n\\n### 异常：train loss vs eval loss 巨大差距\\n- Train loss 终态 ~4.4 vs eval loss 0.49\\n- 可能原因: 训练 loss 含 class_weights 加权，eval loss 是原始 CE；或数据格式/标签问题导致训练目标与评估目标不一致\"}, \"plan-003-baseline\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T07:29:43.220Z\", \"updated_at\": \"2026-05-14T07:30:27.429Z\", \"hypothesis\": \"End-to-end evaluation baselines: always-internal, always-deterministic, oracle, random, trained-router (degenerate v6). 194 episodes / 11 tasks. 建立论文 Table 1 的 baseline 数据。\", \"conclusion\": \"success\", \"metrics\": {\"always_internal\": {\"score\": -37.16, \"ci_90\": [-43.39, -31.43], \"success_rate\": 0.1237, \"death_rate\": 0.4072, \"sim_ratio\": 0}, \"always_deterministic\": {\"score\": -11.64, \"ci_90\": [-17.39, -6.55], \"success_rate\": 0.2371, \"death_rate\": 0.1856, \"sim_ratio\": 1}, \"oracle\": {\"score\": -9.03, \"ci_90\": [-14.14, -4.15], \"success_rate\": 0.2423, \"death_rate\": 0.1649, \"sim_ratio\": 0.9623}, \"random\": {\"score\": -23.75, \"ci_90\": [-29.6, -18.11], \"success_rate\": 0.1649, \"death_rate\": 0.2835, \"sim_ratio\": 0.5027}, \"trained_router_v6\": {\"score\": -11.64, \"ci_90\": [-17.39, -6.55], \"success_rate\": 0.2371, \"death_rate\": 0.1856, \"sim_ratio\": 1, \"note\": \"degenerate - identical to always-deterministic\"}, \"episodes\": 194, \"tasks\": 11}, \"notes\": \"Retrospectively registered. Eval ran on server by worker_code_plan-003-eval-script. Output: results/plan_003_eval/. trained-router = plan-002-formal-v6 (degenerate, all-deterministic). 需用 plan-002-generative-v1 的非退化 router 重跑 trained-router 条件。\"}, \"plan-002-formal-v6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:57:27.371Z\", \"updated_at\": \"2026-05-14T07:28:12.694Z\", \"notes\": \"初次启动 OOM（GPU0 内存争抢，step 30/153 被杀），自动重启 PID 240633。Epoch 1 eval: accuracy=0.929, f1_macro=0.481, f1_internal=0.0, recall_internal=0.0。去掉 class_weights 后模型在 89.7%/10.3% 不平衡数据上仍退化为全 deterministic 预测。dtype 实际为 fp32（启动早于 torch_dtype 修正）。\", \"conclusion\": \"negative\"}, \"plan-004-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:06:51.091Z\", \"updated_at\": \"2026-05-14T07:24:34.751Z\", \"hypothesis\": \"Implicit router SFT v3：修复两个 bug——(1) 去掉 class_weights auto（D023 根因），(2) 用 plan_c/ 11 task 重生成数据修复 no-preference→internal 映射 bug。与 plan-002-formal-v6（explicit classification head, 同样无 class_weights）对照。2040 samples from 11 tasks, no-preference 已丢弃。\", \"parent\": \"plan-004-v2\", \"conclusion\": \"negative\", \"notes\": \"## 数据文件差异分析 (2026-05-14)\\n\\n### 三个数据文件确认\\n| | ablation-b | v2 | v3 |\\n|---|---|---|---|\\n| 路径 | data/plan-004-implicit/implicit_sft.jsonl | results/plan_c_test_labels/implicit_sft.jsonl | data/plan-004-v3/implicit_sft.jsonl |\\n| MD5 | c9b59e04de78... | eb9daacc7f97... | **c9b59e04de78... (=ablation-b)** |\\n| 样本数 | 2040 | 1814 | 2040 |\\n| 文件大小 | 1,578,366 bytes | 1,398,021 bytes | 1,578,366 bytes |\\n\\n**v3 和 ablation-b 的数据文件 100% 相同（MD5 一致）。**\\n\\n### Schema（三个文件一致）\\nfields: messages, task_type, variation, step_idx, route_label\\n\\n### 标签分布\\n- ablation-b / v3: **deterministic 1830 (89.7%), internal 210 (10.3%)**\\n- v2: **internal 1214 (66.9%), deterministic 600 (33.1%)** ← 标签比例完全反转！\\n\\n### Task Type 分布\\n- ablation-b / v3: 11 个 task_type，以 find-non-living-thing(510), chemistry-mix(240) 为主\\n- v2: **仅 4 个 task_type**：find-non-living-thing(600), find-animal(554), grow-fruit(390), identify-life-stages-1(270)\\n\\n### 文本长度\\n- ablation-b / v3: n=2040, min=52, max=166, mean=87 words\\n- v2: n=1814, min=52, max=200, mean=90 words\\n\\n### 前 3 条样本对比\\nablation-b/v3 首条: chemistry-mix/variation 0/step 0, [SIMULATE] connect agent to door to kitchen, route=deterministic\\nv2 首条: find-non-living-thing/variation 0/step 0, [SIMULATE] connect agent to art studio door, route=deterministic\\n\\n### 训练配置对比（真正变量）\\n| | ablation-b (正常) | v2 (异常) | v3 (异常) |\\n|---|---|---|---|\\n| 脚本 | training/implicit_router_sft.py | 同左 | 同左 |\\n| 数据 | data/plan-004-implicit (2040) | results/plan_c_test_labels (1814) | data/plan-004-v3 (2040, **=ablation-b**) |\\n| upsample_minority | **true** | false | false |\\n| class_weights | 无 | \\\"auto\\\" | null |\\n| gradient_accumulation | 1 (默认) | 8 | 8 |\\n| batch_size | 4 | 4 | 4 |\\n| 有效batch | 4 | 32 | 32 |\\n\\n### 训练曲线对比\\n| | ablation-b | v2 | v3 |\\n|---|---|---|---|\\n| Step 10 loss | 5.25 | 48.15 | 48.15 (用户报告) |\\n| Epoch 1 eval_loss | ~0.68 | 0.95 | [无 train.log] |\\n| Epoch 3 eval_loss | 0.36 | **0.49 (收敛了!)** | [无 train.log] |\\n| 平均 train_loss | 1.26 | 12.74 | [无数据] |\\n\\n**重要发现: v2 虽然起步 loss=48，但最终 eval_loss 收敛到 0.49，模型实际上学到了。**\\n\\n### class_weights 代码分析\\nclass_weights 在 WeightedTrainer.compute_loss() 中正确实现：\\n- sample_idx 由 ImplicitSFTDataset.__getitem__() 返回 (line 85)\\n- PaddingCollator.__call__() 正确传递 (line 128-136)\\n- compute_loss() 中 `inputs.pop(\\\"sample_idx\\\")` 获取，条件 `self._class_weights is not None and sample_indices is not None` 控制 (line 227)\\n- v2 (class_weights=\\\"auto\\\"): 权重 internal=0.743, det=1.527，正确计算并应用\\n- v3 (class_weights=null): 无权重，`loss = per_sample_loss.mean()`\\n\\n**class_weights 代码本身没有 bug。v2 和 v3 的 step 10 loss 一致（48.15），证明 class_weights 不是 loss 差异的主因。** class_weights 只是对 per-sample loss 的乘法缩放（0.74x~1.53x），不会改变 loss 的数量级。\\n\\n### plan-002-formal-v6 数据路径\\n- 数据来源: `results/plan_c/` 目录（11 个 task_type 子目录的 labeled_steps.jsonl）\\n- 加载: 2040 samples from 11 files\\n- 标签分布: deterministic 1830 (89.7%), internal 210 (10.3%)\\n- 与 ablation-b 的 implicit 数据是**同源数据，但格式不同**（explicit router 用 observation+action_history+label 格式，implicit 用 messages chat 格式）\\n- **plan-002-formal-v6 也退化了**: 全预测 deterministic (internal: 0/30, deterministic: 390/390)\\n\\n### 结论：根因判定\\n\\n**\\\"数据文件不同\\\"假说被证伪（对 v3）**：v3 使用和 ablation-b 完全相同的数据（MD5 一致），但仍然异常。\\n\\n**真正的变量是训练策略的组合**：\\n1. **`upsample_minority: true`**（ablation-b 独有）：在 89.7% deterministic 的极端不平衡数据上，WeightedRandomSampler 确保 internal 样本被充分采样。没有它，模型每 batch 几乎只看到 deterministic 样本。\\n2. **`gradient_accumulation_steps: 1 vs 8`**：有效 batch 4 vs 32。较大 batch + 无上采样 = 每步看到的 internal 样本更少。\\n\\n**v2 的数据确实不同**（标签比例反转：internal 67% vs 10%，只有 4 个 task_type），但 v2 依然收敛了（eval_loss 0.49）。这说明数据差异导致训练行为不同，但不是致命问题。\\n\\n**建议下一步**：\\n- 用 ablation-b 的配置（upsample_minority=true, gradient_accumulation=1）重跑 v3 数据，验证是否恢复正常 loss\\n- 对 v2 跑 eval 看是否也退化\"}, \"plan-004-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:41:13.286Z\", \"updated_at\": \"2026-05-14T07:08:59.680Z\", \"conclusion\": \"failed\", \"metrics\": {\"train_loss_avg\": 12.74, \"train_loss_epoch1\": [48.15, 42.05, 26.14, 13.71], \"train_loss_epoch3\": [4.58, 4.42, 4.15, 4.46, 4.36], \"eval_loss_epoch2\": 0.5509, \"eval_loss_epoch3\": 0.4905, \"train_runtime_sec\": 150.74, \"note\": \"no accuracy/balanced_accuracy computed\"}, \"notes\": \"Training completed normally (3 epochs, 147 steps). TRAINING_COMPLETE sentinel present. final_adapter + checkpoint-98/147 saved. train_loss=12.74 (abnormally high due to class_weights auto), eval_loss=0.490 at epoch 3. Process exited normally after completion, not OOM/crash.\"}, \"plan-002-formal-v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:37:37.792Z\", \"updated_at\": \"2026-05-14T07:08:19.782Z\", \"hypothesis\": \"Router SFT v5：pad_token_id fix。v3/v4 loss 异常根因确认为 model.config.pad_token_id=None（ModelScope 下载的 Qwen3-1.7B 未设置 pad_token_id，导致分类头 loss 计算错误）。Fix：模型加载后立即设 model.config.pad_token_id = tokenizer.pad_token_id (151643)。其余配置与 v4 相同：stratified split + 无 upsample + class_weights auto + 互斥检查。Qwen3-1.7B + LoRA r=16 (0.37% trainable), 3 epochs, batch_size=4 + grad_accum=8, 2040 samples (1830 det / 210 internal)。\", \"parent\": \"plan-002-formal-v4\", \"conclusion\": \"negative\", \"metrics\": {\"train_loss_avg\": 5.59, \"eval_loss_epoch1\": 0.79, \"eval_loss_epoch2\": 0.78, \"eval_accuracy\": 0.9167, \"eval_balanced_accuracy\": 0.4936, \"eval_f1_macro\": 0.47, \"per_class\": {\"deterministic\": {\"precision\": 0.928, \"recall\": 0.987, \"f1\": 0.938}, \"internal\": {\"precision\": 0, \"recall\": 0, \"f1\": 0}}, \"class_weights\": {\"internal\": 4.5, \"deterministic\": 0.5625}, \"grad_norm_range\": \"70-604\", \"is_degenerate\": true, \"note\": \"Metrics corrected per eval_report.json (D023 Reviewer audit). class_weights auto inflates train loss (4-11) and destabilizes training (grad_norm 604). Model degenerates to all-deterministic.\"}, \"notes\": \"D021 确认：class_weights auto [4.5, 0.5625] 是 v3/v4/v5 loss 异常的根因。train_loss 4-11 (正常应 0.5-0.7)，grad_norm 604，internal recall=0。pad_token_id fix 无效（代码中已存在）。v6 对照实验：移除 class_weights，验证 loss 是否恢复正常。\"}, \"plan-002-formal-v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:22:49.207Z\", \"updated_at\": \"2026-05-14T07:03:55.761Z\", \"hypothesis\": \"Router SFT v4：三项修复——(1) stratified val split (sklearn train_test_split stratify=labels, val 有 30 internal + 390 det), (2) 移除 upsample_minority 只保留 class_weights auto [4.50, 0.5625], (3) 互斥检查防止过补偿。Qwen3-1.7B + LoRA r=16 (0.37% trainable), 3 epochs, batch_size=4 + grad_accum=8, 2040 samples (1830 det / 210 internal)。\", \"conclusion\": \"negative\", \"notes\": \"【更正 D023】v4 实际完整训练完毕（有 TRAINING_COMPLETE + checkpoint-153 + eval_report.json），之前误标 killed。accuracy=91.9% 但 internal_recall=0%（退化为全 deterministic）。根因：class_weights [4.5, 0.5625] 使含 internal 微批次 loss 爆炸(5-11)、grad_norm 100-600，被 max_grad_norm=1.0 裁剪后 internal 有效学习率≈lr×1/600≈3e-8（等于零）。dryrun 无 class_weights 时 loss 正常(0.17-1.03)。\", \"metrics\": {\"eval_accuracy\": 0.919, \"eval_balanced_accuracy\": 0.5, \"internal_recall\": 0, \"internal_precision\": 0, \"is_degenerate\": true, \"class_weights\": {\"internal\": 4.5, \"deterministic\": 0.5625}, \"note\": \"训练完整完成（TRAINING_COMPLETE + checkpoint-153 + eval_report.json），但退化为全部预测 deterministic。之前误标 killed。真正问题：class_weights [4.5, 0.5625] + max_grad_norm=1.0 交互导致 internal 有效学习率≈0\"}}, \"plan-002-formal-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:46:07.817Z\", \"updated_at\": \"2026-05-14T06:09:51.858Z\", \"hypothesis\": \"Router SFT v3（本地 Qwen3-1.7B + HF_HUB_OFFLINE=1）。v1/v2 因网络不可达崩溃。v3 改用 ModelScope 本地模型 /root/autodl-tmp/models/Qwen/Qwen3-1.7B。结果：accuracy=0, f1=0, 完全失效。正在排查根因（模型 config 差异 / label mapping 问题）。\", \"parent\": \"plan-002-formal-v2\", \"conclusion\": \"failed\"}, \"plan-012-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:02:42.659Z\", \"updated_at\": \"2026-05-14T06:04:07.731Z\", \"hypothesis\": \"Death decomposition 全量分析：11 tasks / 245 episodes。plan-001b 完整数据上的最终版。核心发现：death avoidance fraction=90.41%, Δ_full=29.60, Δ_nd=2.84, r=0.9698 (p=8.12e-07)。\", \"conclusion\": \"success\", \"metrics\": {\"delta_full\": 29.6, \"delta_nd\": 2.84, \"death_avoidance_fraction\": 0.9041, \"pearson_r\": 0.9698, \"pearson_p\": 8.12e-07, \"tasks\": 11, \"episodes\": 245, \"death_rate_int\": 0.429, \"death_rate_det\": 0.163, \"label_dist\": {\"det_preferred\": 86, \"internal_preferred\": 9, \"no_preference\": 150}}}, \"plan-012-decomposition\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:50:01.170Z\", \"updated_at\": \"2026-05-14T05:44:02.255Z\", \"hypothesis\": \"Death decomposition 中间分析：30 tasks / 249 episodes 上验证 death avoidance 占 ~99% routing signal（预分析，plan-001b 完整数据后将重跑最终版）\", \"conclusion\": \"success\", \"metrics\": {\"full_11tasks\": {\"delta_full\": 29.6, \"delta_nd\": 2.84, \"death_avoidance_fraction\": 0.9041, \"pearson_r\": 0.9698, \"pearson_p\": 8.12e-07, \"tasks\": 11, \"episodes\": 245, \"death_rate_int\": 0.429, \"death_rate_det\": 0.163, \"label_dist\": {\"det_preferred\": 86, \"internal_preferred\": 9, \"no_preference\": 150}}, \"prescreening_30tasks\": {\"delta_full\": 37.9, \"delta_nd\": 0.2, \"death_avoidance_fraction\": 0.99, \"pearson_r\": 0.989, \"pearson_p\": \"<0.0001\", \"tasks\": 30, \"episodes\": 249}, \"key_tasks\": {\"find_non_living_thing\": {\"n\": 40, \"dr_int\": 0, \"dr_det\": 0, \"delta_full\": 9.58, \"delta_nd\": 9.58, \"note\": \"唯一零死亡 task, Δ_full 全部来自 non-death 性能差异\"}, \"measure_melting_point\": {\"n\": 20, \"dr_int\": 0.55, \"dr_det\": 0.25, \"delta_full\": 30.05, \"delta_pr\": 0.05, \"note\": \"高死亡率, 性能差距几乎完全由 death avoidance 解释\"}}}}, \"plan-002-formal-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:35:54.371Z\", \"updated_at\": \"2026-05-14T05:42:36.829Z\", \"hypothesis\": \"Router SFT 正式训练 v2（WANDB_MODE=offline 修复网络问题）：Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4 + grad_accum=8, class_weights auto + WeightedRandomSampler。v1 因 W&B 网络不可达崩溃。\", \"parent\": \"plan-002-formal\", \"conclusion\": \"failed\", \"notes\": \"第二次失败，根因与 v1 相同：AutoTokenizer.from_pretrained(\\\"Qwen/Qwen3-1.7B\\\") 网络不可达 (OSError: [Errno 101] Network is unreachable)。WANDB_MODE=offline 只修了 W&B 上报，没修模型加载。Qwen3-1.7B 不在本地 HF cache。训练从未开始，wall_clock 256s 全为 HTTP retry/backoff。| 修复方案: 先用 network_turbo 或 ModelScope 下载 Qwen3-1.7B 到本地，再用 --model_name /local/path 重新提交 v3。\"}, \"plan-002-formal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:28:33.051Z\", \"updated_at\": \"2026-05-14T05:37:19.272Z\", \"hypothesis\": \"Router SFT 正式训练：Qwen3-1.7B + LoRA r=16, 3 epochs, batch_size=4 + grad_accum=8 (有效 batch=32), class_weights auto + WeightedRandomSampler。诊断性 probe——验证 learned router 能否从 episode-level counterfactual labels 学到 routing signal（尤其 internal-preferred minority class）。Dryrun 确认 pipeline 通但 1 epoch 退化，3 epochs 应足以收敛。\", \"conclusion\": \"failed\", \"notes\": \"失败原因: AutoTokenizer.from_pretrained(\\\"Qwen/Qwen3-1.7B\\\") 在初始化阶段崩溃——HuggingFace Hub 网络不可达 (OSError: [Errno 101] Network is unreachable) 且本地 HF cache 无此模型。训练从未开始，无 checkpoint，无任何进度。wall_clock 258s 全为 HTTP retry/backoff。| 已有成果: 无 | 建议: 找到 Qwen3-1.7B 本地路径或下载后，用 --model_name /local/path 重新提交\"}, \"plan-001b-gpu1-freeze-chem\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:08:29.425Z\", \"updated_at\": \"2026-05-14T05:36:34.576Z\", \"hypothesis\": \"GPU1 拆分任务：freeze 20 eps + chemistry-mix 20 eps。find-non-living-thing 完成后立即启动，与 GPU0 (lifespan-longest-lived + measure-melting-point) 并行。\", \"conclusion\": \"success\"}, \"plan-002-dryrun\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:03:05.854Z\", \"updated_at\": \"2026-05-14T05:26:39.798Z\", \"hypothesis\": \"Pipeline validation on partial data (10/11 tasks). NOT for results — verify data loading, model init, training loop, checkpoint save, eval. Will retrain on full data after chemistry-mix completes.\", \"notes\": \"dryrun-passed. Checkpoint saved: checkpoint-383 + final_adapter + eval_report.json. LoRA r=16 (0.37% trainable), 5880 samples, 1163 steps, batch_size=4. Cron 误标 failed（PID 变更导致 5× dead check），实际训练成功完成。【修正】class_weights=[11.07, 0.52] 和 WeightedRandomSampler 均已生效（WeightedCETrainer.compute_loss 覆盖 + get_train_dataloader 覆盖）。退化原因：1 epoch 不足以收敛（loss 仍在下降 0.6307→0.4762），非 class_weights 未启用。\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6307, \"eval_loss\": 0.4762, \"eval_accuracy\": 0.923, \"eval_f1_macro\": 0.48, \"eval_balanced_accuracy\": 0.5, \"per_class\": {\"deterministic\": {\"precision\": 0.923, \"recall\": 1, \"f1\": 0.96}, \"internal\": {\"precision\": 0, \"recall\": 0, \"f1\": 0}}, \"confusion\": {\"true_internal_pred_internal\": 0, \"true_internal_pred_det\": 30, \"true_det_pred_det\": 360, \"true_det_pred_internal\": 0}, \"per_task_eval\": {\"chemistry-mix\": {\"accuracy\": 0, \"n_samples\": 30}, \"find-animal\": {\"accuracy\": 1, \"n_samples\": 30}, \"find-non-living-thing\": {\"accuracy\": 1, \"n_samples\": 90}, \"freeze\": {\"accuracy\": 1, \"n_samples\": 30}, \"grow-fruit\": {\"accuracy\": 1, \"n_samples\": 30}, \"identify-life-stages-1\": {\"accuracy\": 1, \"n_samples\": 30}, \"identify-life-stages-2\": {\"accuracy\": 1, \"n_samples\": 30}, \"inclined-plane-determine-angle\": {\"accuracy\": 1, \"n_samples\": 30}, \"lifespan-longest-lived\": {\"accuracy\": 1, \"n_samples\": 30}, \"lifespan-longest-lived-then-shortest-lived\": {\"accuracy\": 1, \"n_samples\": 30}, \"measure-melting-point-unknown-substance\": {\"accuracy\": 1, \"n_samples\": 30}}, \"samples\": 1920, \"total_steps\": 383, \"runtime_s\": 303.8, \"note\": \"DEGENERATE: 全部预测 deterministic, internal recall=0. chemistry-mix 是唯一 internal-preferred task (30 samples 全错). 正在审计 class_weights 是否真正生效。\"}}, \"gpu0-v6-lifespan\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:19:08.846Z\", \"updated_at\": \"2026-05-14T04:52:49.472Z\", \"hypothesis\": \"GPU0 干净重收 lifespan-longest-lived 全量 20 eps（SLIM_EPISODES=1，从 ep0 开始）。之前数据文件损坏（150GB），已删除后重启。plan-001b 最后 3 个未完成 task 之一。\", \"conclusion\": \"killed\", \"notes\": \"Director 指令主动终止。lifespan-longest-lived 已收 23 eps（超额3），数据充足。GPU0 释放给 plan-002 dry-run。\"}, \"plan-001b-gpu0-v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:47:32.668Z\", \"updated_at\": \"2026-05-14T04:19:43.102Z\", \"hypothesis\": \"GPU0 修正重启：measure-melting-point-unknown-substance 20 eps + lifespan-longest-lived 补 1 ep (ep19)。去重后重启，使用 --reuse_dirs 防止重复。\", \"conclusion\": \"killed\", \"notes\": \"Director 指令主动终止。原因：measure-melting-point 已有完整 20 eps（冗余），lifespan-longest-lived 文件损坏（150GB）。GPU0 重启做 lifespan-longest-lived 全量 20 eps 干净重收 (v6)。\"}, \"plan-001b-fnlt-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:05:13.793Z\", \"updated_at\": \"2026-05-14T03:12:10.756Z\", \"hypothesis\": \"find-non-living-thing 追加收集 ep 21-39 (19 eps)，补齐到 40 eps 总量。唯一 0% 死亡率 task，是 ~99% death avoidance claim 的关键 counter-example。\", \"conclusion\": \"success\", \"metrics\": {\"find-non-living-thing\": {\"total_episodes\": 40, \"ep_range\": \"0-39\", \"no_duplicates\": true, \"no_missing\": true, \"det_pref\": 8, \"int_pref\": 0, \"no_pref\": 11, \"avg_score_gap_non_tie\": 40.5, \"note\": \"19 new eps (ep 21-39) collected. Combined with prior 21 eps. 0% death rate confirmed at 40 ep scale.\"}}}, \"plan-001b-gpu0-v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T02:06:59.924Z\", \"updated_at\": \"2026-05-14T02:47:30.101Z\", \"hypothesis\": \"GPU0 拆分任务：lifespan-longest-lived 补 4 eps (已有 16, 目标 20) + measure-melting-point-unknown-substance 全量 20 eps。与 GPU1 freeze+chemistry-mix 并行，加速 plan-001b 完成。\", \"conclusion\": \"killed\", \"notes\": \"v4 崩溃（GPU0 第三次进程异常终止）。v2: vLLM EngineCore crash, v3: cleanup worker 误杀, v4: 崩溃原因待确认。数据重复已清理（lifespan-longest-lived ep 0-6 重复删除）。\"}, \"plan-001b-gpu0-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:50:46.913Z\", \"updated_at\": \"2026-05-14T02:02:40.577Z\", \"hypothesis\": \"GPU0 vLLM崩溃后重启收集：lifespan-longest-lived补5eps(ep15-19) + measure-melting-point-unknown-substance 20eps + freeze 20eps + chemistry-mix 20eps。与v2相同配置，数据可合并。\", \"notes\": \"脚本 run_gpu0_v3.sh 已创建但从未启动。GPU0 被 v2 崩溃残留的僵尸 vLLM 进程（PID 544942, 28GB VRAM）占用。4 个 task 全部未开始。需清理僵尸后重新拆分到双卡。\", \"conclusion\": \"failed\"}, \"plan-001b-gpu1-extra\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:46:54.844Z\", \"updated_at\": \"2026-05-14T02:02:28.988Z\", \"hypothesis\": \"find-non-living-thing 追加 19 eps（ep 21-39），补齐到 40 eps 总量。ep1-20 已收集（delta=-0.05, tied），21 eps 因 cleanup worker 误杀 SIGHUP 中断（仅完成 ep21）。唯一 0% 死亡率 task，C1 \\\"~99% death avoidance\\\" claim 的关键 counter-example。\", \"conclusion\": \"failed\"}, \"plan-001b-gpu1-rebalance\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T01:48:05.077Z\", \"updated_at\": \"2026-05-14T01:56:27.532Z\", \"hypothesis\": \"GPU 负载均衡：GPU1 接管 find-non-living-thing extra 20 eps + GPU0 未开始的 freeze/chemistry-mix 各 20 eps，加速 plan-001b 完成\", \"conclusion\": \"killed\", \"notes\": \"已废弃：GPU0-v3 已接管 freeze/chemistry-mix 数据收集。find-non-living-thing extra 20 eps 由 plan-001b-gpu1-extra 独立处理。\"}, \"plan-001b-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:10:04.310Z\", \"updated_at\": \"2026-05-14T01:56:22.485Z\", \"hypothesis\": \"Episode-level data collection for 4 tasks (1 internal-pref: find-non-living-thing + 3 death-dom: grow-fruit, inclined-plane-determine-angle, identify-life-stages-2), 20 eps/task, reusing prescreening 5 eps. find-non-living-thing needs follow-up to reach 40 eps total.\", \"notes\": \"Part of plan-001b approved by Director. Tasks: find-non-living-thing (20 eps first pass, needs extra 20 to reach 40 target), grow-fruit, inclined-plane-determine-angle, identify-life-stages-2. 80 new eps this run. Follow-up needed for find-non-living extra 20 eps.\", \"conclusion\": \"success\", \"metrics\": {\"find-non-living-thing\": {\"episodes\": 20, \"internal_mean\": 24.9, \"det_mean\": 24.95, \"delta_int_minus_det\": -0.05, \"int_deaths\": 0, \"det_deaths\": 0, \"both_deaths\": 0, \"int_only_death\": 0, \"det_only_death\": 0, \"labels\": {\"det-pref\": 7, \"int-pref\": 4, \"no-pref\": 9}, \"alive_int_mean\": 24.9, \"alive_det_mean\": 24.95, \"note\": \"Prescreening 5eps showed internal-preferred, but 20eps shows essentially TIED (delta=-0.05). Direction did NOT hold. det-pref=7 vs int-pref=4 by episode count.\"}, \"grow-fruit\": {\"episodes\": 20, \"internal_mean\": -43.65, \"det_mean\": -18.55, \"delta_int_minus_det\": -25.1, \"int_deaths\": 9, \"det_deaths\": 4, \"both_deaths\": 3, \"int_only_death\": 6, \"det_only_death\": 1, \"labels\": {\"det-pref\": 6, \"int-pref\": 1, \"no-pref\": 13}, \"alive_int_mean\": 2.45, \"alive_det_mean\": 1.81, \"note\": \"Death-dominated confirmed. Internal dies 6x exclusively vs det 1x. Alive scores low and similar.\"}, \"inclined-plane-determine-angle\": {\"episodes\": 20, \"internal_mean\": -55, \"det_mean\": -19, \"delta_int_minus_det\": -36, \"int_deaths\": 11, \"det_deaths\": 4, \"both_deaths\": 4, \"int_only_death\": 7, \"det_only_death\": 0, \"labels\": {\"det-pref\": 7, \"int-pref\": 0, \"no-pref\": 13}, \"alive_int_mean\": 0, \"alive_det_mean\": 1.25, \"note\": \"Most extreme death-dominated. Internal dies 7x exclusively, det never dies alone. Internal NEVER preferred (0/20). Alive scores near zero.\"}, \"identify-life-stages-2\": {\"episodes\": 20, \"internal_mean\": -48.4, \"det_mean\": -18.4, \"delta_int_minus_det\": -30, \"int_deaths\": 10, \"det_deaths\": 4, \"both_deaths\": 4, \"int_only_death\": 6, \"det_only_death\": 0, \"labels\": {\"det-pref\": 6, \"int-pref\": 0, \"no-pref\": 14}, \"alive_int_mean\": 3.2, \"alive_det_mean\": 2, \"note\": \"Death-dominated confirmed. Internal dies 6x exclusively, det never alone. Internal NEVER preferred (0/20).\"}, \"summary\": {\"total_episodes\": 80, \"all_tasks_complete\": true, \"death_dominated_tasks\": [\"grow-fruit\", \"inclined-plane-determine-angle\", \"identify-life-stages-2\"], \"internal_preferred_tasks\": [], \"key_finding\": \"find-non-living-thing prescreening signal (internal>det) did NOT replicate at 20 eps — essentially tied. All 3 death-dom tasks confirmed: internal router causes significantly more deaths than deterministic.\"}}}, \"plan-001b-gpu0-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:31:47.627Z\", \"updated_at\": \"2026-05-14T01:51:26.200Z\", \"hypothesis\": \"Episode-level data collection for 7 tasks (5 genuine-det + 2 death-dom), 20 eps/task. v2: added cleanup_gpu_processes() to prevent orphan vLLM processes.\", \"conclusion\": \"failed\", \"notes\": \"GPU0 第二次失败。根因：vLLM EngineCore 在 Episode 15 deterministic 模式中意外死亡 (EngineDeadError)。v2 的 cleanup_gpu_processes() 只清理启动前孤儿，未防运行中崩溃。诊断 Worker: worker_diagnose_plan-001b-gpu0-v2_20260514T015111\"}, \"plan-011-rule-based\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:51:12.911Z\", \"updated_at\": \"2026-05-14T01:00:59.327Z\", \"hypothesis\": \"Rule-based keyword routing baseline：测试 keyword heuristic 能否捕获 episode-level routing signal。三版 keyword list 均结构性失效——v1 (含 connect) ≈ always-det, v2 (科学词) ≈ always-internal, v3 (状态变化动词) ≈ always-internal。\", \"conclusion\": \"success\", \"metrics\": {\"v1_match_rate\": \"85.8%\", \"v1_result\": \"degenerate → always-det\", \"v2_match_rate\": \"4.9%\", \"v2_result\": \"degenerate → always-internal\", \"v3_match_rate\": \"2.8%\", \"v3_episode_accuracy\": \"1.5%\", \"v3_result\": \"degenerate → always-internal\", \"conclusion\": \"Keyword heuristic structurally fails on ScienceWorld — ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords. No keyword list provides meaningful routing signal.\", \"note\": \"D014: structural failure analysis, paper positions as evidence for learned/observation-based approaches\"}, \"notes\": \"v1 204 vs v2 203 episode 差异原因：竞态条件——v2 报告在 lifespan-shortest-lived/episodes.jsonl 创建前 15 秒生成。非方法论问题。当前重跑两版均为 233 episodes。论文统一引用最终 plan-001b 完整数据的 episode 基数。\"}, \"plan-001b-gpu0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:10:02.679Z\", \"updated_at\": \"2026-05-13T22:33:15.743Z\", \"hypothesis\": \"Episode-level data collection for 7 tasks (5 genuine-det: find-animal, identify-life-stages-1, lifespan-longest-lived-then-shortest, lifespan-longest-lived, measure-melting-point-unknown + 2 death-dom: freeze, chemistry-mix), 20 eps/task, reusing prescreening 5 eps\", \"notes\": \"Part of plan-001b approved by Director. Tasks: find-animal, identify-life-stages-1, lifespan-longest-lived-then-shortest-lived, lifespan-longest-lived, measure-melting-point-unknown-substance, freeze, chemistry-mix. 105 new eps (15 each × 7 tasks). Watch measure-melting-point-unknown death_avoidance_fraction=0.38 outlier per Reviewer note.\", \"conclusion\": \"failed\"}, \"research-prescreening-gpu0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:20:17.197Z\", \"updated_at\": \"2026-05-13T22:09:59.200Z\", \"hypothesis\": \"Fork-based deterministic evaluation 在 ScienceWorld 30 个 task types 中广泛有效（预筛 25 个未测 task，5 ep/task，识别 signal 方向）\", \"conclusion\": \"killed\"}, \"research-prescreening-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:53:28.002Z\", \"updated_at\": \"2026-05-13T22:08:01.696Z\", \"hypothesis\": \"GPU1 加入 plan-001a 预筛，跑剩余 8 个 task types（measure-melting-point-unknown-substance, mendelian-genetics-known/unknown-plant, power-component x2, test-conductivity x2, use-thermometer），加速完成全部 25 tasks\", \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"8/8\", \"all_direction\": \"POSITIVE\", \"results\": {\"measure-melting-point-unknown-substance\": {\"int_mean\": -58.6, \"det_mean\": -32, \"delta\": 26.6, \"signal\": \"death-dominated\"}, \"mendelian-genetics-known-plant\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"mendelian-genetics-unknown-plant\": {\"int_mean\": -60, \"det_mean\": -40, \"delta\": 20, \"signal\": \"death-dominated\"}, \"power-component\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"power-component-renewable-vs-nonrenewable-energy\": {\"int_mean\": -60, \"det_mean\": 0, \"delta\": 60, \"signal\": \"death-dominated\"}, \"test-conductivity\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"test-conductivity-of-unknown-substances\": {\"int_mean\": -60, \"det_mean\": -20, \"delta\": 40, \"signal\": \"death-dominated\"}, \"use-thermometer\": {\"int_mean\": -59.4, \"det_mean\": -19.4, \"delta\": 40, \"signal\": \"death-dominated\"}}, \"summary\": \"All 8 tasks death-dominated: internal mode hits -100 (lethal) in 3/5 episodes; deterministic mode avoids most deaths but scores remain ~0 (no genuine task progress). Delta driven by death avoidance, not task solving.\"}}, \"mvp-p1-signal\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T04:50:06.546Z\", \"updated_at\": \"2026-05-13T21:46:23.662Z\", \"conclusion\": \"killed\"}, \"research-boil-v3-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:20:17.657Z\", \"updated_at\": \"2026-05-13T19:50:37.666Z\", \"hypothesis\": \"用统一 v3 代码（> tie-break + death filter 仅 det/oracle）重跑 boil 20ep，获得与其他 4 个 task 一致的代码版本数据\", \"parent\": \"mvp-p1-gpu0\", \"notes\": \"Registry 状态 ANALYZING 但 cron reconcile 确认 PID 650421 仍存活（16/20 episodes 完成）。实际仍在 RUNNING。状态机不允许回退 ANALYZING→RUNNING，等完成后直接转 DONE。\", \"metrics\": {\"boil_v3_20ep\": {\"internal_mean\": -44.7, \"internal_std\": 50, \"det_mean\": -9.3, \"det_std\": 30.3, \"oracle_mean\": 3.8, \"oracle_std\": 15.2, \"oracle_minus_internal\": 48.5, \"oracle_minus_det\": 13.1, \"det_minus_internal\": 35.4}, \"death_distribution\": {\"internal_deaths\": 9, \"internal_total\": 20, \"internal_death_pct\": 45, \"det_deaths\": 2, \"det_total\": 20, \"det_death_pct\": 10, \"oracle_deaths\": 0, \"oracle_total\": 20, \"oracle_death_pct\": 0}, \"note\": \"v3 code (> tie-break, death filter det/oracle only). Oracle大幅优于两个baseline, 但绝对分低(3.8), 仅1/20 episode拿到70分. Death avoidance is primary mechanism.\"}, \"conclusion\": \"success\"}, \"research-cf-pilot-gpu1\": {\"status\": \"PENDING\", \"created_at\": \"2026-05-13T17:15:37.908Z\", \"updated_at\": \"2026-05-13T17:17:23.652Z\", \"hypothesis\": \"Episode-terminal counterfactual labeling (K=10) 在 melt/change-state/mix-paint 上产生 >30% non-tie rate，为 router 训练提供有效信号\", \"conclusion\": \"killed\"}, \"mvp-p1-gpu1-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T08:00:51.836Z\", \"updated_at\": \"2026-05-13T15:41:04.061Z\", \"conclusion\": \"success\", \"metrics\": {\"mix_paint\": {\"internal_mean\": -41, \"det_mean\": -5.5, \"oracle_mean\": 4.5, \"det_minus_internal\": 35.5, \"bootstrap_90ci\": [20, 55]}, \"grow_plant\": {\"internal_mean\": 0.5, \"det_mean\": 0.5, \"oracle_mean\": 0.5, \"det_minus_internal\": 0, \"bootstrap_90ci\": [0, 0]}, \"n_episodes_per_task\": 20, \"tasks_significant\": \"1/2\", \"note\": \"grow-plant: NO_EFFECT (三种模式完全相同); mix-paint: 显著正向\"}}, \"mvp-p1-gpu0-vllm\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T09:18:47.128Z\", \"updated_at\": \"2026-05-13T15:17:57.586Z\", \"conclusion\": \"success\", \"metrics\": {\"melt\": {\"internal_mean\": -54.7, \"det_mean\": -14.55, \"oracle_mean\": 2.15, \"det_minus_internal\": 40.15, \"bootstrap_90ci\": [25, 60.15]}, \"change_state\": {\"internal_mean\": -54.7, \"det_mean\": -14.5, \"oracle_mean\": 0.45, \"det_minus_internal\": 40.2, \"bootstrap_90ci\": [25, 60.15]}, \"pooled\": {\"det_minus_internal\": 40.17, \"bootstrap_90ci\": [27.6, 52.77]}, \"n_episodes_per_task\": 20, \"ci_lower_gt_0\": true, \"tasks_significant\": \"2/2\"}}, \"mvp-p1-gpu0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T05:45:22.030Z\", \"updated_at\": \"2026-05-13T09:22:26.294Z\", \"conclusion\": \"killed\", \"metrics\": {\"boil_20ep\": {\"internal_mean\": -49.8, \"det_mean\": -19.7, \"oracle_mean\": -29.7}, \"note\": \"旧代码 (>= tie-break, 无 death filter), boil 20/20 完成, melt/change-state 未跑\"}}, \"mvp-p1-gpu1-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T07:44:48.498Z\", \"updated_at\": \"2026-05-13T08:00:14.773Z\", \"conclusion\": \"killed\"}, \"mvp-p1-gpu1-vllm\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T07:10:07.454Z\", \"updated_at\": \"2026-05-13T07:43:34.463Z\", \"conclusion\": \"killed\"}, \"mvp-p1-gpu1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T05:45:20.053Z\", \"updated_at\": \"2026-05-13T07:09:59.347Z\", \"conclusion\": \"killed\"}, \"mvp-p0-forking\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T04:50:05.057Z\", \"updated_at\": \"2026-05-13T05:10:18.587Z\", \"conclusion\": \"success\", \"metrics\": {\"fork_success_rate\": 1, \"avg_latency_s\": 1.67, \"p50_latency_s\": 1.53, \"p95_latency_s\": 2.37, \"max_memory_mb\": 20, \"gate\": \"PASS\"}}}, \"count\": 49, \"total\": 49, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1831}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_016shiw6VTARzHqHF6pJ8tLa`</summary>

```json
{
  "pattern": "**/artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "d6ec2e5f-20da-42d1-9ed2-d97c9097d68f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsRcuvyoBHN1RwSSQ6VPmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 23374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1467
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

_source line 13 · 2026-05-14T11:23:56.660Z_

<details><summary>↩ Tool result · `toolu_016shiw6VTARzHqHF6pJ8tLa`</summary>

```text
artifacts/phase1_progress_report.md
artifacts/diagnosis_mvp-p1-gpu1-v2.md
artifacts/dream_reports/dream_20260513T153257/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T153257/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T153257/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T153257/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T153257/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/best/experiment_data.json
artifacts/dream_reports/dream_20260513T153257/best/paper_framing.md
artifacts/dream_reports/dream_20260513T153257/best/paper.tex
artifacts/dream_reports/dream_20260513T153257/best/paper.aux
artifacts/dream_reports/dream_20260513T153257/best/paper.out
artifacts/dream_reports/dream_20260513T153257/best/paper.pdf
artifacts/dream_reports/dream_20260513T153257/best/paper.log
artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T153257/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/median/experiment_data.json
artifacts/dream_reports/dream_20260513T153257/median/paper_framing.md
artifacts/dream_reports/dream_20260513T153257/median/paper.tex
artifacts/dream_reports/dream_20260513T153257/median/paper.aux
artifacts/dream_reports/dream_20260513T153257/median/paper.out
artifacts/dream_reports/dream_20260513T153257/median/paper.pdf
artifacts/dream_reports/dream_20260513T153257/median/paper.log
artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T153257/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T153257/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T153257/worst/paper.tex
artifacts/dream_reports/dream_20260513T153257/worst/paper.aux
artifacts/dream_reports/dream_20260513T153257/worst/paper.out
artifacts/dream_reports/dream_20260513T153257/worst/paper.pdf
artifacts/dream_reports/dream_20260513T153257/worst/paper.log
artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T153257/best/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T153257/best/review_report.md
artifacts/dream_reports/dream_20260513T153257/logs/review_best.log
artifacts/dream_reports/dream_20260513T153257/median/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/median/review_report.md
artifacts/dream_reports/dream_20260513T153257/logs/review_median.log
artifacts/dream_reports/dream_20260513T153257/worst/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/worst/review_report.md
artifacts/dream_reports/dream_20260513T153257/logs/review_worst.log
artifacts/dream_reports/dream_20260513T153257/meta.yaml
artifacts/router_sft_train.py
artifacts/plan_001b_task_selection.md
artifacts/death_aware_labeling.py
artifacts/literature_survey_death_avoidance.md
artifacts/_project/report/keywords_v2_comparison.txt
artifacts/_project/report/plan012_preliminary_decomposition.txt
artifacts/_project/data/prescreening_final_summary.json
artifacts/prescreening_final_summary.json
artifacts/plan_001b_revised_proposal.md
artifacts/_project/chart/plan012_dryrun_summary.txt
artifacts/_project/chart/plan005_routing_pattern_summary.txt
artifacts/_project/report/c1_claim_impact_analysis.txt
artifacts/_project/paper/related_work_draft.md
artifacts/related_work_draft.md
artifacts/plan005_routing_analysis.md
artifacts/plan-012-decomposition/data/plan005_routing_analysis_summary.txt
artifacts/_project/paper/introduction_draft.md
artifacts/_project/paper/introduction_draft_d860d5.md
artifacts/_project/paper/experiment_tables.md
artifacts/_project/report/experiment_tables.md
artifacts/experiment_tables.md
artifacts/_project/paper/method_draft_e328fe.md
artifacts/_project/paper/method_draft.md
artifacts/_project/report/paper_data_tables.md
artifacts/paper_data_tables.md
artifacts/plan-012-full/data/death_decomposition_preliminary.csv
artifacts/_project/data/heatmap_data.csv
artifacts/_project/report/number_consistency_audit.md
artifacts/plan-002-generative-v1-analysis.md
artifacts/_project/paper/paper_outline.md
artifacts/plan-004-v5/report/routing_eval_v5.txt
artifacts/plan-004-ablation-b/data/ablation_b_gen_eval.txt
artifacts/_project/paper/experiments_draft_dd9866.md
artifacts/_project/paper/experiments_draft.md
artifacts/plan-003-e2e-ablation-b/data/plan-003-e2e-ablation-b-results.md
artifacts/_project/report/ablation_b_multiseed_report.md
artifacts/plan-003-eval-implicit/data/plan-003-eval-implicit-results.txt
artifacts/_project/paper/method_v2_draft.md
artifacts/_project/paper/method_v2_draft_875550.md
artifacts/_project/paper/introduction_v2_draft.md
artifacts/_project/paper/introduction_v2_draft_32f156.md
artifacts/manifest.yaml
artifacts/_project/paper/related_work_v2_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "39a00d3e-95eb-42bb-b051-b77c18e44341",
  "tool_use_result": {
    "filenames": [
      "artifacts/phase1_progress_report.md",
      "artifacts/diagnosis_mvp-p1-gpu1-v2.md",
      "artifacts/dream_reports/dream_20260513T153257/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260513T153257/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260513T153257/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260513T153257/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260513T153257/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260513T153257/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T153257/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T153257/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T153257/best/paper.aux",
      "artifacts/dream_reports/dream_20260513T153257/best/paper.out",
      "artifacts/dream_reports/dream_20260513T153257/best/paper.pdf",
      "artifacts/dream_reports/dream_20260513T153257/best/paper.log",
      "artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260513T153257/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260513T153257/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T153257/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T153257/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T153257/median/paper.aux",
      "artifacts/dream_reports/dream_20260513T153257/median/paper.out",
      "artifacts/dream_reports/dream_20260513T153257/median/paper.pdf",
      "artifacts/dream_reports/dream_20260513T153257/median/paper.log",
      "artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260513T153257/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260513T153257/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T153257/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T153257/worst/paper.tex",
      "artifacts/dream_reports/dream_20260513T153257/worst/paper.aux",
      "artifacts/dream_reports/dream_20260513T153257/worst/paper.out",
      "artifacts/dream_reports/dream_20260513T153257/worst/paper.pdf",
      "artifacts/dream_reports/dream_20260513T153257/worst/paper.log",
      "artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260513T153257/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260513T153257/logs/orchestrator.log",
      "artifacts/dream_reports/dream_20260513T153257/best/review_report.md",
      "artifacts/dream_reports/dream_20260513T153257/logs/review_best.log",
      "artifacts/dream_reports/dream_20260513T153257/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260513T153257/median/review_report.md",
      "artifacts/dream_reports/dream_20260513T153257/logs/review_median.log",
      "artifacts/dream_reports/dream_20260513T153257/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260513T153257/worst/review_report.md",
      "artifacts/dream_reports/dream_20260513T153257/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260513T153257/meta.yaml",
      "artifacts/router_sft_train.py",
      "artifacts/plan_001b_task_selection.md",
      "artifacts/death_aware_labeling.py",
      "artifacts/literature_survey_death_avoidance.md",
      "artifacts/_project/report/keywords_v2_comparison.txt",
      "artifacts/_project/report/plan012_preliminary_decomposition.txt",
      "artifacts/_project/data/prescreening_final_summary.json",
      "artifacts/prescreening_final_summary.json",
      "artifacts/plan_001b_revised_proposal.md",
      "artifacts/_project/chart/plan012_dryrun_summary.txt",
      "artifacts/_project/chart/plan005_routing_pattern_summary.txt",
      "artifacts/_project/report/c1_claim_impact_analysis.txt",
      "artifacts/_project/paper/related_work_draft.md",
      "artifacts/related_work_draft.md",
      "artifacts/plan005_routing_analysis.md",
      "artifacts/plan-012-decomposition/data/plan005_routing_analysis_summary.txt",
      "artifacts/_project/paper/introduction_draft.md",
      "artifacts/_project/paper/introduction_draft_d860d5.md",
      "artifacts/_project/paper/experiment_tables.md",
      "artifacts/_project/report/experiment_tables.md",
      "artifacts/experiment_tables.md",
      "artifacts/_project/paper/method_draft_e328fe.md",
      "artifacts/_project/paper/method_draft.md",
      "artifacts/_project/report/paper_data_tables.md",
      "artifacts/paper_data_tables.md",
      "artifacts/plan-012-full/data/death_decomposition_preliminary.csv",
      "artifacts/_project/data/heatmap_data.csv",
      "artifacts/_project/report/number_consistency_audit.md",
      "artifacts/plan-002-generative-v1-analysis.md",
      "artifacts/_project/paper/paper_outline.md",
      "artifacts/plan-004-v5/report/routing_eval_v5.txt",
      "artifacts/plan-004-ablation-b/data/ablation_b_gen_eval.txt",
      "artifacts/_project/paper/experiments_draft_dd9866.md",
      "artifacts/_project/paper/experiments_draft.md",
      "artifacts/plan-003-e2e-ablation-b/data/plan-003-e2e-ablation-b-results.md",
      "artifacts/_project/report/ablation_b_multiseed_report.md",
      "artifacts/plan-003-eval-implicit/data/plan-003-eval-implicit-results.txt",
      "artifacts/_project/paper/method_v2_draft.md",
      "artifacts/_project/paper/method_v2_draft_875550.md",
      "artifacts/_project/paper/introduction_v2_draft.md",
      "artifacts/_project/paper/introduction_v2_draft_32f156.md",
      "artifacts/manifest.yaml",
      "artifacts/_project/paper/related_work_v2_draft.md"
    ],
    "durationMs": 46,
    "numFiles": 87,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
I have the paper_framing.md and registry data. Now I need to read the existing paper sections for narrative consistency. Let me read the key drafts: introduction_v2, method_v2, and experiments_draft.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "b563053f-b2e5-44aa-9f81-201f0c66ba48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNmvZYsD4Lom3qzjhC412C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27333,
      "cache_read_input_tokens": 24841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27333
      },
      "output_tokens": 10,
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

Reading existing paper sections for narrative consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "09800c04-cbca-4017-b4fd-9b1957db6698",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNmvZYsD4Lom3qzjhC412C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27333,
      "cache_read_input_tokens": 24841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27333
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — Read · `toolu_01FL8vnM1GWR7kfT9htsdZVH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "06a9c730-e5c0-493b-a73c-c9ba89234654",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNmvZYsD4Lom3qzjhC412C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27333,
      "cache_read_input_tokens": 24841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27333
      },
      "output_tokens": 10,
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

_source line 17 · 2026-05-14T11:24:03.419Z_

<details><summary>↩ Tool result · `toolu_01FL8vnM1GWR7kfT9htsdZVH`</summary>

```text
1	# Introduction — Draft v2 (A-source: plan-012-full, 11 tasks / 245 episodes)
2	
3	\section{Introduction}
4	
5	When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated, or failing to model that metal conducts heat differently than glass---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?
6	
7	Existing routing approaches \cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 98.2\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\S\ref{sec:collection}). Keyword-based heuristics (\S\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\texttt{pour}, \texttt{move}, \texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.
8	
9	We propose \emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\S\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\Delta_{\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\Delta_{\text{no\_death}} = +2.84$---a Death Avoidance Factor (DAF; \S\ref{sec:daf}) of 90.41\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), confirming that death avoidance is the primary mechanism across task types (\S\ref{sec:death-decomp}). Death rates differ sharply: 42.9\% for internal reasoning versus 16.3\% for deterministic computation. Episode-level labels reflect this asymmetry: of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.2\% of oracle routing decisions match an unconditional always-deterministic strategy (\S\ref{sec:baselines}).
10	
11	Our contributions:
12	\begin{enumerate}
13	\item \textbf{Episode-level counterfactual methodology with death avoidance decomposition.} We introduce a framework that generates routing labels from episode-level outcome comparisons and decomposes the routing signal via the DAF metric and death-aware labeling (\S\ref{sec:collection}, \S\ref{sec:daf}). This overcomes per-step oracle degeneracy (98.2\% tie rate) in sparse-reward environments.
14	\item \textbf{Death avoidance dominates routing signal on ScienceWorld.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation. Non-death differences are small ($\Delta_{\text{no\_death}} = +2.84$, 9.6\% of $\Delta_{\text{full}}$) but reveal residual routing value---e.g., \texttt{find-non-living-thing} has zero deaths yet $\Delta_{\text{full}} = +9.58$ (\S\ref{sec:death-decomp}). Router training as a diagnostic probe shows counterfactual labels encode learnable patterns at the representation level (logit accuracy 74.5\%, balanced accuracy 79\%) despite a generation-level expression gap (\S\ref{sec:router-diagnostic}).
15	\end{enumerate}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "6704c0a3-c70b-448a-bb22-facc7560b672",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft.md",
      "content": "# Introduction — Draft v2 (A-source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Introduction}\n\nWhen a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated, or failing to model that metal conducts heat differently than glass---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n\nExisting routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 98.2\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\S\\ref{sec:collection}). Keyword-based heuristics (\\S\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\texttt{pour}, \\texttt{move}, \\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\n\nWe propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming that death avoidance is the primary mechanism across task types (\\S\\ref{sec:death-decomp}). Death rates differ sharply: 42.9\\% for internal reasoning versus 16.3\\% for deterministic computation. Episode-level labels reflect this asymmetry: of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.2\\% of oracle routing decisions match an unconditional always-deterministic strategy (\\S\\ref{sec:baselines}).\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Episode-level counterfactual methodology with death avoidance decomposition.} We introduce a framework that generates routing labels from episode-level outcome comparisons and decomposes the routing signal via the DAF metric and death-aware labeling (\\S\\ref{sec:collection}, \\S\\ref{sec:daf}). This overcomes per-step oracle degeneracy (98.2\\% tie rate) in sparse-reward environments.\n\\item \\textbf{Death avoidance dominates routing signal on ScienceWorld.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation. Non-death differences are small ($\\Delta_{\\text{no\\_death}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$) but reveal residual routing value---e.g., \\texttt{find-non-living-thing} has zero deaths yet $\\Delta_{\\text{full}} = +9.58$ (\\S\\ref{sec:death-decomp}). Router training as a diagnostic probe shows counterfactual labels encode learnable patterns at the representation level (logit accuracy 74.5\\%, balanced accuracy 79\\%) despite a generation-level expression gap (\\S\\ref{sec:router-diagnostic}).\n\\end{enumerate}\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_013cWqoHuGyscGBmrRPEPhsa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "761d306f-9601-40d2-acd7-a392a48b44ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNmvZYsD4Lom3qzjhC412C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27333,
      "cache_read_input_tokens": 24841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27333
      },
      "output_tokens": 10,
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

_source line 19 · 2026-05-14T11:24:03.787Z_

<details><summary>↩ Tool result · `toolu_013cWqoHuGyscGBmrRPEPhsa`</summary>

```text
1	# Method Section — Draft v2 (A-Source: plan-012-full, 11 tasks / 245 episodes)
2	
3	\section{Method}
4	
5	\subsection{Counterfactual Episode Collection}
6	\label{sec:collection}
7	
8	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 98.2\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
9	
10	For each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \emph{pure-internal} episode follows the ReAct paradigm \cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.
11	
12	Each episode pair produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes the terminal score and $d \in \{0,1\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. We evaluate on ScienceWorld \cite{scienceworld-2022}, which spans 30 task types covering physical and chemical reasoning with a $-100$ penalty upon agent death. After prescreening (5 episodes per type for signal estimation), we perform targeted full collection on 11 task types, yielding 245 episode pairs (20--40 per type).
13	
14	\subsection{Death-Aware Labeling}
15	\label{sec:labeling}
16	
17	Each counterfactual pair receives an episode-level routing label based on $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:
18	
19	\begin{enumerate}
20	    \item \textbf{Death asymmetry}: $d^{\text{int}} \neq d^{\text{det}}$ $\rightarrow$ the surviving strategy is preferred.
21	    \item \textbf{Both dead}: $d^{\text{int}} = d^{\text{det}} = 1$ $\rightarrow$ \texttt{no\_preference}.
22	    \item \textbf{Score comparison}: both survive and $s^{\text{det}} \neq s^{\text{int}}$ $\rightarrow$ the higher-scoring strategy is preferred.
23	    \item \textbf{Tied alive}: both survive and $s^{\text{det}} = s^{\text{int}}$ $\rightarrow$ \texttt{no\_preference}.
24	\end{enumerate}
25	
26	Across 245 episodes, this yields 86 (35.1\%) \texttt{det\_preferred}, 9 (3.7\%) \texttt{internal\_preferred}, and 150 (61.2\%) \texttt{no\_preference}. The near-absence of \texttt{internal\_preferred} labels combined with the dominance of \texttt{no\_preference} indicates that the deterministic strategy's advantage is concentrated in death avoidance rather than superior task performance when both agents survive.
27	
28	\subsection{Death Avoidance Factor}
29	\label{sec:daf}
30	
31	To quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):
32	\begin{equation}
33	    \text{DAF} = 1 - \frac{\Delta_{\text{no\_death}}}{\Delta_{\text{full}}}
34	\end{equation}
35	where $\Delta_{\text{full}}$ is the mean score gap ($s^{\text{det}} - s^{\text{int}}$) across all episodes and $\Delta_{\text{no\_death}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\Delta_{\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\Delta_{\text{full}}| > 0$.
36	
37	On 245 episodes across 11 task types: $\Delta_{\text{full}} = +29.60$, $\Delta_{\text{no\_death}} = +2.84$, yielding DAF $= 90.41\%$. The cross-task consistency is strong: the Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$) across 11 task types, indicating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.
38	
39	\subsection{Rule-Based Baseline}
40	\label{sec:rule}
41	
42	As a simple routing heuristic, we test keyword-based rules that route to deterministic computation when the action contains science-related verbs. We evaluate three keyword lists of decreasing breadth:
43	
44	\begin{itemize}
45	    \item \textbf{v1} (20 generic verbs including \emph{connect}, \emph{move}): matches 85.8\% of actions, degenerating to always-deterministic.
46	    \item \textbf{v2} (17 science-specific verbs: \emph{heat}, \emph{boil}, \emph{melt}, \emph{freeze}, \ldots): matches 4.9\%, degenerating to always-internal.
47	    \item \textbf{v3} (12 state-change verbs): matches 2.8\%, degenerating to always-internal.
48	\end{itemize}
49	
50	The structural cause is that ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms. No keyword granularity bridges the gap between near-total and negligible match rates, precluding meaningful routing discrimination. This structural failure motivates observation-based approaches that use environment observations and agent state as routing features rather than action keywords.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "4dc1852e-3cf5-4348-b256-f91d5630cc10",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
      "content": "# Method Section — Draft v2 (A-Source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Method}\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 98.2\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n\nFor each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.\n\nEach episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. We evaluate on ScienceWorld \\cite{scienceworld-2022}, which spans 30 task types covering physical and chemical reasoning with a $-100$ penalty upon agent death. After prescreening (5 episodes per type for signal estimation), we perform targeted full collection on 11 task types, yielding 245 episode pairs (20--40 per type).\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nEach counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ the surviving strategy is preferred.\n    \\item \\textbf{Both dead}: $d^{\\text{int}} = d^{\\text{det}} = 1$ $\\rightarrow$ \\texttt{no\\_preference}.\n    \\item \\textbf{Score comparison}: both survive and $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n    \\item \\textbf{Tied alive}: both survive and $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n\\end{enumerate}\n\nAcross 245 episodes, this yields 86 (35.1\\%) \\texttt{det\\_preferred}, 9 (3.7\\%) \\texttt{internal\\_preferred}, and 150 (61.2\\%) \\texttt{no\\_preference}. The near-absence of \\texttt{internal\\_preferred} labels combined with the dominance of \\texttt{no\\_preference} indicates that the deterministic strategy's advantage is concentrated in death avoidance rather than superior task performance when both agents survive.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{no\\_death}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nwhere $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{no\\_death}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\\Delta_{\\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\\Delta_{\\text{full}}| > 0$.\n\nOn 245 episodes across 11 task types: $\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{no\\_death}} = +2.84$, yielding DAF $= 90.41\\%$. The cross-task consistency is strong: the Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$) across 11 task types, indicating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.\n\n\\subsection{Rule-Based Baseline}\n\\label{sec:rule}\n\nAs a simple routing heuristic, we test keyword-based rules that route to deterministic computation when the action contains science-related verbs. We evaluate three keyword lists of decreasing breadth:\n\n\\begin{itemize}\n    \\item \\textbf{v1} (20 generic verbs including \\emph{connect}, \\emph{move}): matches 85.8\\% of actions, degenerating to always-deterministic.\n    \\item \\textbf{v2} (17 science-specific verbs: \\emph{heat}, \\emph{boil}, \\emph{melt}, \\emph{freeze}, \\ldots): matches 4.9\\%, degenerating to always-internal.\n    \\item \\textbf{v3} (12 state-change verbs): matches 2.8\\%, degenerating to always-internal.\n\\end{itemize}\n\nThe structural cause is that ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms. No keyword granularity bridges the gap between near-total and negligible match rates, precluding meaningful routing discrimination. This structural failure motivates observation-based approaches that use environment observations and agent state as routing features rather than action keywords.\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01U5uDnq1SmvCjDUxizWhyQB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "e256b4c4-440e-492f-ab26-8bd60c850747",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNmvZYsD4Lom3qzjhC412C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27333,
      "cache_read_input_tokens": 24841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27333
      },
      "output_tokens": 10,
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

_source line 21 · 2026-05-14T11:24:04.185Z_

<details><summary>↩ Tool result · `toolu_01U5uDnq1SmvCjDUxizWhyQB`</summary>

```text
1	# Experiments — Draft v1
2	
3	\section{Experiments}
4	
5	\subsection{Setup}
6	\label{sec:exp-setup}
7	
8	We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.
9	
10	\subsection{Death Avoidance Decomposition}
11	\label{sec:death-decomp}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{no\_death}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
14	
15	This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.
16	
17	The episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \texttt{det\_preferred}, only 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.
18	
19	One task reveals the residual non-death signal. \texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\Delta_{\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\% (internal) and 25\% (deterministic), producing $\Delta_{\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.
20	
21	When both modalities survive, their task performance is near-equivalent ($\Delta_{\text{no\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.
22	
23	\subsection{Baselines}
24	\label{sec:baselines}
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\begin{tabular}{@{}lccc@{}}
30	\toprule
31	Strategy & Score & 95\% CI & Death \% \\
32	\midrule
33	Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\
34	Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\
35	Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\
36	Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\
37	\midrule
38	Implicit Router & \multicolumn{3}{c}{[PLACEHOLDER]} \\
39	\bottomrule
40	\end{tabular}
41	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\% of its decisions match the always-deterministic strategy.}
42	\label{tab:baselines}
43	\end{table}
44	
45	Table~\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\% of its routing decisions matching always-deterministic. This \emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\%) proportional to its 50/50 allocation.
46	
47	Keyword-based routing (\S\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\%, degenerating to always-deterministic) or negligible (v2: 4.9\%, v3: 2.8\%, both degenerating to always-internal). No keyword granularity bridges this gap.
48	
49	\subsection{Router Training as Diagnostic}
50	\label{sec:router-diagnostic}
51	
52	A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.
53	
54	\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.
55	
56	\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\% with balanced accuracy of 79\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\% with internal recall of 51.5\%, revealing a gap between logit-level pattern recognition and generation-level expression. [PLACEHOLDER: ablation-b end-to-end evaluation results for Table~\ref{tab:baselines}.]
57	
58	These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.
59	
60	\subsection{Limitations}
61	\label{sec:limitations}
62	
63	Our analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "85f5249e-7bf8-4e38-ab26-f10aba5c1305",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft.md",
      "content": "# Experiments — Draft v1\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n\\midrule\nImplicit Router & \\multicolumn{3}{c}{[PLACEHOLDER]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match the always-deterministic strategy.}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap.\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\\% with balanced accuracy of 79\\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\\% with internal recall of 51.5\\%, revealing a gap between logit-level pattern recognition and generation-level expression. [PLACEHOLDER: ablation-b end-to-end evaluation results for Table~\\ref{tab:baselines}.]\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the Conclusion section, making sure to:

1. Match the narrative established in intro/method/experiments
2. Use only registry-verified numbers (from plan-012-full)
3. Structure: Summary (2-3 sentences) + Limitations (2-3 sentences) + Future Work (2-3 sentences)
4. LaTeX format
5. ~0.3 pages
6. No new claims
7. Appropriate strength words (single benchmark → no "consistently"/"broadly")

Key numbers from registry (plan-012-full):
- DAF = 90.41%


- Δ_full = +29.60
- Δ_nd = +2.84
- r = 0.9698, p = 8.12e-07
- 11 tasks / 245 episodes
- Death rate: internal 42.9%, deterministic 16.3%
- Label dist: det_preferred 86, internal_preferred 9, no_preference 150

The router diagnostic from the ablation study shows it's performing near chance level at 58%, which is an important limitation to note. I notice the experiments section already has a \subsection{ started, so I need to be careful about the structure here.

The experiments draft already includes a Limitations subsection, so for the Conclusion I should keep the limitations discussion brief and complementary rather than redundant — summarizing the key constraints without duplicating what's already there. The task specifies that Conclusion should cover Summary, Limitations, and Future Work, so I'll weave those together concisely.

Now I'm drafting the LaTeX for the Conclusion section, which will present the main findings about episode-level counterfactual analysis and the dominance of death avoidance in routing decisions, along with the router performance results.

The analysis has clear limitations—it's validated only on ScienceWorld with Qwen2.5-7B-Instruct, and the harsh death penalty might overstate how much death avoidance matters compared to environments with softer failure costs. Episode-level labels can't capture step-by-step routing dynamics, and the gap between router training performance at the episode level versus actual generation suggests we'd need finer-grained step-level labels to train more effective routers. Future directions should focus on step-level counterfactual labeling to unlock better router learning, and testing whether death avoidance dominance holds across other tool-augmented domains like mathematical reasoning or API-mediated tasks. I'm cross-checking the performance metrics across different experimental runs. The router achieves around 58% balanced accuracy at the generation level (averaging 59.27%, 57.36%, 57.48%, and 58.31% across four seeds), while logit-level performance reaches 79% balanced accuracy—a substantial gap that suggests the learned patterns exist in the representation space but struggle to manifest in actual generation. This near-random generation-level performance strengthens the counterfactual decomposition argument for C1.

Now I'm refining the Conclusion section to include the key limitations: the episode-level granularity prevents us from revealing step-by-step routing decisions, we're limited to a single benchmark (ScienceWorld) when broader environments would strengthen the findings, and the dataset itself is relatively constrained at 245 episodes across 11 task types. I'm drafting the conclusion to weave in the death avoidance finding as the core result while acknowledging these boundaries. son $r = 0.9698$, $p = 8.12 \times 10^{-7}$). A diagnostic router trained on these labels achieves near-random balanced accuracy ($\approx$58\% across four seeds), reinforcing that the episode-level signal is dominated by a single mechanism---catastrophic failure prevention---rather than diverse step-level routing patterns.

Our analysis is limited to a single benchmark (ScienceWorld) with one LLM backbone (Qwen2.5-7B-Instruct) and 245 episodes across 11 task types; generalization to other environments and model scales remains to be established. Episode-level labeling cannot reveal step-level routing dynamics, and ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal relative to environments with milder failure costs.

Future work should pursue step-level counterfactual labeling to overcome the granularity bottleneck and enable finer-grained router training. Extending this framework to other tool-augmented domains like mathematical reasoning or API-mediated tasks would clarify whether death avoidance dominance is unique to catastrophic-failure settings or a more general pattern in LLM behavior. The same decomposition approach could also help diagnose other systematic failure modes beyond hallucinated state transitions.

Now I'm verifying all the numbers against the registry to ensure accuracy before writing and registering the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "04dbfff9-4217-4d5b-8e9c-152486adbf51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRUwPk4WsTPgV3VCexMBGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5584,
      "cache_read_input_tokens": 52174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5584
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

_source line 23_

Now I have all context. Writing the Conclusion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "e29d4cbc-5e29-4a95-b98a-cc2728c729d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRUwPk4WsTPgV3VCexMBGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5584,
      "cache_read_input_tokens": 52174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5584
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01DXxZzUynnnrB7Bch6YojcK`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/",
  "description": "List existing paper artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "1ea1b89d-6fc7-44a4-b014-ffbdfc2a11d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRUwPk4WsTPgV3VCexMBGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5584,
      "cache_read_input_tokens": 52174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5584
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

_source line 25 · 2026-05-14T11:24:55.709Z_

<details><summary>↩ Tool result · `toolu_01DXxZzUynnnrB7Bch6YojcK`</summary>

```text
experiment_tables.md
experiments_draft.md
experiments_draft_dd9866.md
introduction_draft.md
introduction_draft_d860d5.md
introduction_v2_draft.md
introduction_v2_draft_32f156.md
method_draft.md
method_draft_e328fe.md
method_v2_draft.md
method_v2_draft_875550.md
paper_outline.md
related_work_draft.md
related_work_v2_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "94380ea0-d416-4061-af75-f9b81199dd66",
  "tool_use_result": {
    "stdout": "experiment_tables.md\nexperiments_draft.md\nexperiments_draft_dd9866.md\nintroduction_draft.md\nintroduction_draft_d860d5.md\nintroduction_v2_draft.md\nintroduction_v2_draft_32f156.md\nmethod_draft.md\nmethod_draft_e328fe.md\nmethod_v2_draft.md\nmethod_v2_draft_875550.md\npaper_outline.md\nrelated_work_draft.md\nrelated_work_v2_draft.md",
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

_source line 26_

<details open><summary>🔧 Tool call — Write · `toolu_01CpkxAm6Zf994Dvh3zXgq5w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/conclusion_draft.md",
  "content": "# Conclusion — Draft v1 (A-Source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Conclusion}\n\nWe introduced episode-level counterfactual analysis as a diagnostic methodology for understanding what routing learns in LLM agents operating on interactive environments. Across 11 ScienceWorld task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal between internal LLM reasoning and deterministic computation ($\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{no\\_death}} = +2.84$; Pearson $r = 0.9698$, $p = 8.12 \\times 10^{-7}$). A diagnostic router trained on these labels achieves near-random balanced accuracy ($\\approx$58\\% across four seeds), reinforcing that the episode-level signal is dominated by a single mechanism---catastrophic failure prevention---rather than diverse step-level routing patterns.\n\nOur analysis is limited to a single benchmark (ScienceWorld) with one LLM backbone (Qwen2.5-7B-Instruct) and 245 episodes across 11 task types; generalization to other environments and model scales remains to be established. Episode-level labeling cannot reveal step-level routing dynamics, and ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal relative to environments with milder failure costs.\n\nFuture work should pursue step-level counterfactual labeling to overcome the granularity bottleneck and enable finer-grained router training. Extending the methodology to other tool-augmented domains---mathematical reasoning with code interpreters, API-mediated tasks---would test whether death avoidance dominance is specific to catastrophic-failure environments or a broader phenomenon. The counterfactual decomposition framework can also serve as a diagnostic lens for other systematic LLM failure modes beyond hallucinated state transitions.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "9be85624-aee2-4fe6-91b2-d9ee00fa2916",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DShHM8yj9DdebJAV5JcyFr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 57758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
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

_source line 27 · 2026-05-14T11:25:04.745Z_

<details><summary>↩ Tool result · `toolu_01CpkxAm6Zf994Dvh3zXgq5w`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/conclusion_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "499d7da5-b2f3-4c4b-8e1a-d3eaf57e7dd7",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/conclusion_draft.md",
    "content": "# Conclusion — Draft v1 (A-Source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Conclusion}\n\nWe introduced episode-level counterfactual analysis as a diagnostic methodology for understanding what routing learns in LLM agents operating on interactive environments. Across 11 ScienceWorld task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal between internal LLM reasoning and deterministic computation ($\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{no\\_death}} = +2.84$; Pearson $r = 0.9698$, $p = 8.12 \\times 10^{-7}$). A diagnostic router trained on these labels achieves near-random balanced accuracy ($\\approx$58\\% across four seeds), reinforcing that the episode-level signal is dominated by a single mechanism---catastrophic failure prevention---rather than diverse step-level routing patterns.\n\nOur analysis is limited to a single benchmark (ScienceWorld) with one LLM backbone (Qwen2.5-7B-Instruct) and 245 episodes across 11 task types; generalization to other environments and model scales remains to be established. Episode-level labeling cannot reveal step-level routing dynamics, and ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal relative to environments with milder failure costs.\n\nFuture work should pursue step-level counterfactual labeling to overcome the granularity bottleneck and enable finer-grained router training. Extending the methodology to other tool-augmented domains---mathematical reasoning with code interpreters, API-mediated tasks---would test whether death avoidance dominance is specific to catastrophic-failure environments or a broader phenomenon. The counterfactual decomposition framework can also serve as a diagnostic lens for other systematic LLM failure modes beyond hallucinated state transitions.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_019dUwDgdqn8ZC3nHX4ErDUQ`</summary>

```json
{
  "name": "conclusion_draft",
  "type": "paper",
  "description": "EMNLP 2026 short paper Conclusion section draft v1 — Summary + Limitations + Future Work, all numbers from plan-012-full (A-source)",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/conclusion_draft.md",
  "tags": [
    "paper",
    "conclusion",
    "v1"
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
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "467818b1-a859-4658-b7b7-c38a33817372",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvNQQzwU66M7WVSFiC7pas",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 612,
      "cache_read_input_tokens": 60284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 612
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

_source line 29 · 2026-05-14T11:25:10.263Z_

<details><summary>↩ Tool result · `toolu_019dUwDgdqn8ZC3nHX4ErDUQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_49608d\", \"name\": \"conclusion_draft\", \"type\": \"paper\", \"description\": \"EMNLP 2026 short paper Conclusion section draft v1 — Summary + Limitations + Future Work, all numbers from plan-012-full (A-source)\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/conclusion_draft_49608d.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T11:25:10.024749+00:00\", \"tags\": [\"paper\", \"conclusion\", \"v1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "3a977e7f-7895-4ac0-8c34-4bd21dddcacd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_49608d\\\", \\\"name\\\": \\\"conclusion_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"EMNLP 2026 short paper Conclusion section draft v1 — Summary + Limitations + Future Work, all numbers from plan-012-full (A-source)\\\", \\\"path\\\": \\\"projects/simgate-modular-routing/artifacts/_project/paper/conclusion_draft_49608d.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"simgate-modular-routing\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T11:25:10.024749+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"conclusion\\\", \\\"v1\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_49608d\", \"name\": \"conclusion_draft\", \"type\": \"paper\", \"description\": \"EMNLP 2026 short paper Conclusion section draft v1 — Summary + Limitations + Future Work, all numbers from plan-012-full (A-source)\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/conclusion_draft_49608d.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T11:25:10.024749+00:00\", \"tags\": [\"paper\", \"conclusion\", \"v1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

Conclusion section 已写入并注册 (`art_20260514_49608d`)。

**结构**：
- **Summary**（3 句）：episode-level counterfactual methodology + DAF=90.41% 核心发现 + router near-random (balanced_acc≈58%, 4 seeds) 强化 C1
- **Limitations**（2 句）：单 benchmark/单 backbone/245 eps 数据量 + episode-level 粒度限制 + -100 penalty 可能放大 signal
- **Future Work**（3 句）：step-level labeling → 克服粒度瓶颈 + 扩展到 MATH/code 等 tool-augmented 域 + counterfactual decomposition 作为通用 LLM failure mode 诊断工具

所有数字均来自 plan-012-full (A-source)；router balanced_acc 来自 plan-004-ablation-b 4-seed 汇总。无新 claim，强度词与单 benchmark evidence 匹配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "uuid": "d38acd18-311a-4841-ae36-8a4f00e665bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019okzNNEqRbwN6fe4hyCqRa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 60896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
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

_source line 31_

Conclusion section 已写入并注册 (`art_20260514_49608d`)。

**结构**：
- **Summary**（3 句）：episode-level counterfactual methodology + DAF=90.41% 核心发现 + router near-random (balanced_acc≈58%, 4 seeds) 强化 C1
- **Limitations**（2 句）：单 benchmark/单 backbone/245 eps 数据量 + episode-level 粒度限制 + -100 penalty 可能放大 signal
- **Future Work**（3 句）：step-level labeling → 克服粒度瓶颈 + 扩展到 MATH/code 等 tool-augmented 域 + counterfactual decomposition 作为通用 LLM failure mode 诊断工具

所有数字均来自 plan-012-full (A-source)；router balanced_acc 来自 plan-004-ablation-b 4-seed 汇总。无新 claim，强度词与单 benchmark evidence 匹配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 93445,
  "duration_api_ms": 93527,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "07279fa8-ee46-4045-89ea-e8aed7904d80",
  "total_cost_usd": 0.5612097500000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 49579,
    "cache_read_input_tokens": 291168,
    "output_tokens": 4170,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49579,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 278,
        "cache_read_input_tokens": 60896,
        "cache_creation_input_tokens": 524,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 524
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1352,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001452,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 4170,
      "cacheReadInputTokens": 291168,
      "cacheCreationInputTokens": 49579,
      "webSearchRequests": 0,
      "costUSD": 0.55975775,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b13f0f53-eca0-4f07-91e7-4bbfe022a28b"
}
```

</details>

---
