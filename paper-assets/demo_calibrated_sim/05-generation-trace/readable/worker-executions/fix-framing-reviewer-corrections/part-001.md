# fix framing reviewer corrections — Part 1 of 2

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Worker execution logs

[Transcript overview](../fix-framing-reviewer-corrections.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/36/363cd7d243f187512321.json)

## Before a recorded user message

## Before a recorded user message

93 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl",
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
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
  "uuid": "57dc8a9e-1d24-42ab-928f-e23f6227c4d8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1778674800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "dced82bb-f013-48c7-b0ee-3f45c4a35331",
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the necessary files and registry data in parallel to gather all the information needed for the 5 corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "2d706c5d-9977-4441-9b27-7e19926d451a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWMExZbkDwtKRtqzaTjNAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12047,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12047
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


### Assistant

_source line 5_

读取 paper_framing.md、literature_map.yaml 和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "44633e2b-0a7b-4653-8910-6d22656b2ba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWMExZbkDwtKRtqzaTjNAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12047,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12047
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01APSqxHnS3q1RkFCu3Ct5sS`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
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
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "bde1d0ae-8fd9-476d-bd7c-70b0812467da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWMExZbkDwtKRtqzaTjNAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12047,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12047
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

_source line 7 · 2026-05-13T07:35:21.157Z_

<details><summary>↩ Tool result · `toolu_01APSqxHnS3q1RkFCu3Ct5sS`</summary>

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
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "49a11d62-ca69-473b-a417-ce8240399d44",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QczCjdVcTKNY2DyJtUzg2w`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "74a7d3fc-d6b6-45bd-b290-d168f9e2caa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZMgftnpwNo4cnxt8pNskV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1110,
      "cache_read_input_tokens": 23888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1110
      },
      "output_tokens": 70,
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

_source line 9 · 2026-05-13T07:35:28.183Z_

<details><summary>↩ Tool result · `toolu_01QczCjdVcTKNY2DyJtUzg2w`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\\n\\n> Plan B story — Director approved 2026-05-13\\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\\n\\n---\\n\\n## Title Candidates\\n\\n1. **\\\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\\\"**\\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\\n   - Con: 稍长\\n\\n2. **\\\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\\\"**\\n   - Pro: \\\"trap\\\" 吸引眼球，涵盖两种方法\\n   - Con: 可能暗示过于 negative\\n\\n3. **\\\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\\\"**\\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\\n   - Con: \\\"Considered Harmful\\\" 可能被认为 cliché\\n\\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\\n\\n---\\n\\n## Core Story\\n\\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\\n\\n**Attempted Solution**: We apply two complementary calibration strategies:\\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\\n\\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\\n\\n**Framing**: This is NOT \\\"we tried and failed.\\\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: BCP produces three systematic failure mechanisms\\n**Evidence strength**: Strong (single model, clean data)\\n\\n| Failure Mode | Description | Key Metric | exp_id |\\n|---|---|---|---|\\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |\\n\\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\\n- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)\\n\\n**External support**:\\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\\n- FM3: no direct external parallel — novel observation\\n\\n### C2: DPO+BCP interaction produces calibration reversal\\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\\n\\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\\n\\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\\n|---|---|---|\\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\\n| Variant×run checks with gap expansion | — | **10/12** |\\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\\n\\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\\n\\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\\n\\n### C3: Cross-scale validation\\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\\n\\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\\n\\n**Current auxiliary evidence**:\\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \\\"behavior shift observable at floor completion.\\\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\\n\\n**Hedging strategy**: If Qwen14B replicates → \\\"failure modes persist across model scales (7B, 14B).\\\" If not → limit scope to \\\"documented on Qwen2.5-7B; generalizability requires further investigation.\\\"\\n\\n### C4: Implications for future calibration research\\n**Evidence strength**: Analytical (grounded in C1-C3)\\n\\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \\\"attractor basin\\\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\\n\\n---\\n\\n## Reviewer Concerns (Pre-empted Attack Surfaces)\\n\\n### RC1: \\\"Single model — how do we know this generalizes?\\\"\\n**Status**: Partially mitigated\\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\\n- **Honest hedge**: \\\"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\\\"\\n\\n### RC2: \\\"n=20 tasks, high variance — statistical power?\\\"\\n**Response**:\\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\\n\\n### RC3: \\\"This is just negative results — where's the contribution?\\\"\\n**Response**:\\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\\n  3. **Actionable implications**: Concrete constraints for future calibration methods\\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\\n\\n### RC4: \\\"Why not try other calibration methods?\\\"\\n**Response**:\\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\\n\\n### RC5: \\\"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\\\"\\n**Response**:\\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\\n\\n---\\n\\n## Evidence Map\\n\\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\\n|---|---|---|---|---|---|\\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\\n\\n---\\n\\n## Contribution Statement\\n\\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\\n\\n---\\n\\n## Key Literature Anchors\\n\\n| Role in Paper | Paper | What It Provides |\\n|---|---|---|\\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\\n\\n---\\n\\n## Open Items\\n\\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\\n\", \"total_chars\": 12503, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "f73dfbb6-e1f5-484a-85d3-2ecd8e7ec674",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\\\\n\\\\n> Plan B story — Director approved 2026-05-13\\\\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\\\\n\\\\n---\\\\n\\\\n## Title Candidates\\\\n\\\\n1. **\\\\\\\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\\\\\\\"**\\\\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\\\\n   - Con: 稍长\\\\n\\\\n2. **\\\\\\\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\\\\\\\"**\\\\n   - Pro: \\\\\\\"trap\\\\\\\" 吸引眼球，涵盖两种方法\\\\n   - Con: 可能暗示过于 negative\\\\n\\\\n3. **\\\\\\\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\\\\\\\"**\\\\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\\\\n   - Con: \\\\\\\"Considered Harmful\\\\\\\" 可能被认为 cliché\\\\n\\\\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\\\\n\\\\n---\\\\n\\\\n## Core Story\\\\n\\\\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\\\\n\\\\n**Attempted Solution**: We apply two complementary calibration strategies:\\\\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\\\\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\\\\n\\\\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\\\\n\\\\n**Framing**: This is NOT \\\\\\\"we tried and failed.\\\\\\\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\\\\n\\\\n---\\\\n\\\\n## Core Claims\\\\n\\\\n### C1: BCP produces three systematic failure mechanisms\\\\n**Evidence strength**: Strong (single model, clean data)\\\\n\\\\n| Failure Mode | Description | Key Metric | exp_id |\\\\n|---|---|---|---|\\\\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\\\\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\\\\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |\\\\n\\\\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\\\\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\\\\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\\\\n- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)\\\\n\\\\n**External support**:\\\\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\\\\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\\\\n- FM3: no direct external parallel — novel observation\\\\n\\\\n### C2: DPO+BCP interaction produces calibration reversal\\\\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\\\\n\\\\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\\\\n\\\\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\\\\n|---|---|---|\\\\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\\\\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\\\\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\\\\n| Variant×run checks with gap expansion | — | **10/12** |\\\\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\\\\n\\\\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\\\\n\\\\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\\\\n\\\\n### C3: Cross-scale validation\\\\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\\\\n\\\\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\\\\n\\\\n**Current auxiliary evidence**:\\\\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \\\\\\\"behavior shift observable at floor completion.\\\\\\\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\\\\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\\\\n\\\\n**Hedging strategy**: If Qwen14B replicates → \\\\\\\"failure modes persist across model scales (7B, 14B).\\\\\\\" If not → limit scope to \\\\\\\"documented on Qwen2.5-7B; generalizability requires further investigation.\\\\\\\"\\\\n\\\\n### C4: Implications for future calibration research\\\\n**Evidence strength**: Analytical (grounded in C1-C3)\\\\n\\\\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\\\\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\\\\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\\\\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \\\\\\\"attractor basin\\\\\\\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\\\\n\\\\n---\\\\n\\\\n## Reviewer Concerns (Pre-empted Attack Surfaces)\\\\n\\\\n### RC1: \\\\\\\"Single model — how do we know this generalizes?\\\\\\\"\\\\n**Status**: Partially mitigated\\\\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\\\\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\\\\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\\\\n- **Honest hedge**: \\\\\\\"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\\\\\\\"\\\\n\\\\n### RC2: \\\\\\\"n=20 tasks, high variance — statistical power?\\\\\\\"\\\\n**Response**:\\\\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\\\\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\\\\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\\\\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\\\\n\\\\n### RC3: \\\\\\\"This is just negative results — where's the contribution?\\\\\\\"\\\\n**Response**:\\\\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\\\\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\\\\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\\\\n  3. **Actionable implications**: Concrete constraints for future calibration methods\\\\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\\\\n\\\\n### RC4: \\\\\\\"Why not try other calibration methods?\\\\\\\"\\\\n**Response**:\\\\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\\\\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\\\\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\\\\n\\\\n### RC5: \\\\\\\"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\\\\\\\"\\\\n**Response**:\\\\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\\\\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\\\\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\\\\n\\\\n---\\\\n\\\\n## Evidence Map\\\\n\\\\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\\\\n|---|---|---|---|---|---|\\\\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\\\\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\\\\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\\\\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\\\\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\\\\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\\\\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\\\\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\\\\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\\\\n\\\\n---\\\\n\\\\n## Contribution Statement\\\\n\\\\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\\\\n\\\\n---\\\\n\\\\n## Key Literature Anchors\\\\n\\\\n| Role in Paper | Paper | What It Provides |\\\\n|---|---|---|\\\\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\\\\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\\\\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\\\\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\\\\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\\\\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\\\\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\\\\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\\\\n\\\\n---\\\\n\\\\n## Open Items\\\\n\\\\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\\\\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\\\\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\\\\n\\\", \\\"total_chars\\\": 12503, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\\n\\n> Plan B story — Director approved 2026-05-13\\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\\n\\n---\\n\\n## Title Candidates\\n\\n1. **\\\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\\\"**\\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\\n   - Con: 稍长\\n\\n2. **\\\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\\\"**\\n   - Pro: \\\"trap\\\" 吸引眼球，涵盖两种方法\\n   - Con: 可能暗示过于 negative\\n\\n3. **\\\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\\\"**\\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\\n   - Con: \\\"Considered Harmful\\\" 可能被认为 cliché\\n\\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\\n\\n---\\n\\n## Core Story\\n\\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\\n\\n**Attempted Solution**: We apply two complementary calibration strategies:\\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\\n\\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\\n\\n**Framing**: This is NOT \\\"we tried and failed.\\\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: BCP produces three systematic failure mechanisms\\n**Evidence strength**: Strong (single model, clean data)\\n\\n| Failure Mode | Description | Key Metric | exp_id |\\n|---|---|---|---|\\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |\\n\\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\\n- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)\\n\\n**External support**:\\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\\n- FM3: no direct external parallel — novel observation\\n\\n### C2: DPO+BCP interaction produces calibration reversal\\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\\n\\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\\n\\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\\n|---|---|---|\\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\\n| Variant×run checks with gap expansion | — | **10/12** |\\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\\n\\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\\n\\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\\n\\n### C3: Cross-scale validation\\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\\n\\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\\n\\n**Current auxiliary evidence**:\\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \\\"behavior shift observable at floor completion.\\\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\\n\\n**Hedging strategy**: If Qwen14B replicates → \\\"failure modes persist across model scales (7B, 14B).\\\" If not → limit scope to \\\"documented on Qwen2.5-7B; generalizability requires further investigation.\\\"\\n\\n### C4: Implications for future calibration research\\n**Evidence strength**: Analytical (grounded in C1-C3)\\n\\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \\\"attractor basin\\\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\\n\\n---\\n\\n## Reviewer Concerns (Pre-empted Attack Surfaces)\\n\\n### RC1: \\\"Single model — how do we know this generalizes?\\\"\\n**Status**: Partially mitigated\\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\\n- **Honest hedge**: \\\"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\\\"\\n\\n### RC2: \\\"n=20 tasks, high variance — statistical power?\\\"\\n**Response**:\\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\\n\\n### RC3: \\\"This is just negative results — where's the contribution?\\\"\\n**Response**:\\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\\n  3. **Actionable implications**: Concrete constraints for future calibration methods\\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\\n\\n### RC4: \\\"Why not try other calibration methods?\\\"\\n**Response**:\\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\\n\\n### RC5: \\\"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\\\"\\n**Response**:\\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\\n\\n---\\n\\n## Evidence Map\\n\\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\\n|---|---|---|---|---|---|\\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\\n\\n---\\n\\n## Contribution Statement\\n\\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\\n\\n---\\n\\n## Key Literature Anchors\\n\\n| Role in Paper | Paper | What It Provides |\\n|---|---|---|\\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\\n\\n---\\n\\n## Open Items\\n\\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\\n\", \"total_chars\": 12503, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KmsZFSDoZvtLREwmxPNgg7`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "23147f58-647f-42e4-a3c4-d3f5d811782c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZMgftnpwNo4cnxt8pNskV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1110,
      "cache_read_input_tokens": 23888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1110
      },
      "output_tokens": 70,
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

_source line 11 · 2026-05-13T07:35:29.126Z_

<details><summary>↩ Tool result · `toolu_01KmsZFSDoZvtLREwmxPNgg7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT-COMPETITOR\\n  # ============================================================\\n  # 未找到直接竞品。没有现有工作专门做\\\"校准 LLM 用户模拟器的方言行为率偏差\\\"。\\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\\n  # 这验证了 DemoCalib 的新颖性。\\n\\n  # ============================================================\\n  # FOUNDATION\\n  # ============================================================\\n  - id: seshadri2026lost\\n    title: \\\"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\\\"\\n    authors: \\\"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\\\"\\n    venue: \\\"arXiv 2601.17087\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.17087\\\"\\n    category: foundation\\n    role: \\\"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Agent success rates vary up to 9pp across different user simulator LLMs\\\"\\n      - \\\"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\\\"\\n      - \\\"Simulated users introduce conversational artifacts absent from real human users\\\"\\n      - \\\"Disparities compound significantly with age for AAVE speakers\\\"\\n    how_we_differ: \\\"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\\\"\\n\\n  - id: yao2024taubench\\n    title: \\\"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\\\"\\n    authors: \\\"Yao et al.\\\"\\n    venue: \\\"arXiv 2406.12045\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2406.12045\\\"\\n    category: foundation\\n    role: \\\"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\\\"\\n      - \\\"Proposes pass^k metric measuring reliability over multiple trials\\\"\\n      - \\\"User simulator is LLM-based, enabling behavioral modification\\\"\\n    how_we_differ: \\\"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\\\"\\n\\n  - id: liu2024agentbench\\n    title: \\\"AgentBench: Evaluating LLMs as Agents\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2308.03688\\\"\\n    category: foundation\\n    role: \\\"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Significant performance gap between commercial and open-source LLMs as agents\\\"\\n      - \\\"Poor long-term reasoning and instruction following are main obstacles\\\"\\n    how_we_differ: \\\"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\\\"\\n\\n  - id: wang2024mint\\n    title: \\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\"\\n    authors: \\\"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.10691\\\"\\n    category: foundation\\n    role: \\\"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\\\"\\n      - \\\"Better single-turn performance does not guarantee better multi-turn performance\\\"\\n      - \\\"SIFT and RLHF generally hurt multi-turn capabilities\\\"\\n    how_we_differ: \\\"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\\\"\\n\\n  # ============================================================\\n  # METHOD-COMPONENT\\n  # ============================================================\\n  - id: rafailov2023dpo\\n    title: \\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\"\\n    authors: \\\"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    url: \\\"https://arxiv.org/abs/2305.18290\\\"\\n    category: method-component\\n    role: \\\"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO directly optimizes policy from preference pairs without explicit reward model\\\"\\n      - \\\"Computationally lightweight, stable alternative to PPO-based RLHF\\\"\\n      - \\\"Exceeds PPO-based RLHF in controlling sentiment of generations\\\"\\n    how_we_differ: \\\"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\\\"\\n\\n  - id: zhao2021calibrate\\n    title: \\\"Calibrate Before Use: Improving Few-Shot Performance of Language Models\\\"\\n    authors: \\\"Zhao, Wallace, Feng, Klein, Singh\\\"\\n    venue: \\\"ICML 2021\\\"\\n    year: 2021\\n    url: \\\"https://arxiv.org/abs/2102.09690\\\"\\n    category: method-component\\n    role: \\\"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\\\"\\n      - \\\"Identified majority label bias, recency bias, common token bias\\\"\\n      - \\\"Contextual calibration with content-free inputs improves accuracy up to 30%\\\"\\n    how_we_differ: \\\"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\\\"\\n\\n  - id: abdulhai2025consistent\\n    title: \\\"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\\\"\\n    authors: \\\"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2511.00222\\\"\\n    category: method-component\\n    role: \\\"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\\\"\\n      - \\\"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\\\"\\n      - \\\"Multi-turn RL reduces inconsistency by >55%\\\"\\n    how_we_differ: \\\"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\\\"\\n\\n  - id: naous2025flipping\\n    title: \\\"Flipping the Dialogue: Training and Evaluating User Language Models\\\"\\n    authors: \\\"Naous, Laban, Xu, Neville\\\"\\n    venue: \\\"arXiv 2510.06552\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.06552\\\"\\n    category: method-component\\n    role: \\\"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Better assistant LMs yield worse user simulators\\\"\\n      - \\\"UserLM-8b provides more realistic user simulation\\\"\\n      - \\\"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\\\"\\n    how_we_differ: \\\"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\\\"\\n\\n  - id: li2025persona\\n    title: \\\"LLM Generated Persona is a Promise with a Catch\\\"\\n    authors: \\\"Li, Chen et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.16527\\\"\\n    category: method-component\\n    role: \\\"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLM-generated personas systematically drift toward socially desirable traits\\\"\\n      - \\\"More LLM-generated content produces more left-leaning, less representative personas\\\"\\n      - \\\"Bias exists in the persona creation step itself, not just model responses\\\"\\n    how_we_differ: \\\"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\\\"\\n\\n  - id: wang2024alignment\\n    title: \\\"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\\\"\\n    authors: \\\"Wang, Bi, Pentyala et al.\\\"\\n    venue: \\\"arXiv 2407.16216\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2407.16216\\\"\\n    category: method-component\\n    role: \\\"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\\\"\\n      - \\\"DPO is stable and lightweight but sensitive to preference data quality\\\"\\n      - \\\"Detailed comparison of PPO vs GRPO vs DPO implementation details\\\"\\n    how_we_differ: \\\"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\\\"\\n\\n  # ============================================================\\n  # EVALUATION\\n  # ============================================================\\n  - id: lin2025redial\\n    title: \\\"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\\\"\\n    authors: \\\"Lin et al.\\\"\\n    venue: \\\"ACL 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.11005\\\"\\n    category: evaluation\\n    role: \\\"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\\\"\\n      - \\\"Almost all models show statistically significant performance drops on AAVE\\\"\\n      - \\\"AAVE performance gaps arise from morphosyntactic features and conversational norms\\\"\\n      - \\\"LLMs struggle more with AAVE than misspelled Standard English\\\"\\n    how_we_differ: \\\"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\\\"\\n\\n  - id: faisal2024dialectbench\\n    title: \\\"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\\\"\\n    authors: \\\"Faisal et al.\\\"\\n    venue: \\\"ACL 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2403.11009\\\"\\n    category: evaluation\\n    role: \\\"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"10 NLP tasks, 281 varieties, 40 language clusters\\\"\\n      - \\\"Substantial performance disparities between standard and non-standard varieties\\\"\\n      - \\\"Performance gap widens with fine-tuning due to uneven data availability\\\"\\n    how_we_differ: \\\"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\\\"\\n\\n  - id: gallegos2024bias\\n    title: \\\"Bias and Fairness in Large Language Models: A Survey\\\"\\n    authors: \\\"Gallegos, Rossi, Barrow et al.\\\"\\n    venue: \\\"Computational Linguistics, Vol. 50(3)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.00770\\\"\\n    category: evaluation\\n    role: \\\"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Taxonomy of bias metrics at embedding, probability, and generated text levels\\\"\\n      - \\\"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\\\"\\n      - \\\"Consolidated public datasets for bias evaluation\\\"\\n    how_we_differ: \\\"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\\\"\\n\\n  - id: parrish2022bbq\\n    title: \\\"BBQ: A Hand-Built Bias Benchmark for Question Answering\\\"\\n    authors: \\\"Parrish et al.\\\"\\n    venue: \\\"Findings of ACL 2022\\\"\\n    year: 2022\\n    url: \\\"https://aclanthology.org/2022.findings-acl.165/\\\"\\n    category: evaluation\\n    role: \\\"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\\\"\\n    relevance: low\\n    key_findings:\\n      - \\\"58,492 unique examples across multiple bias categories\\\"\\n      - \\\"Evaluates both individual and intersectional biases\\\"\\n      - \\\"Standard benchmark for LLM bias evaluation\\\"\\n    how_we_differ: \\\"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\\\"\\n\\n  - id: haq2026dialect\\n    title: \\\"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\\\"\\n    authors: \\\"Haq, Saldias\\\"\\n    venue: \\\"arXiv 2604.21152\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21152\\\"\\n    category: evaluation\\n    role: \\\"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\\\"\\n      - \\\"AAVE/Singlish users receive less sanitized content than SAE users\\\"\\n      - \\\"Safety alignment is brittle, over-indexed on explicit keywords\\\"\\n      - \\\"24,000+ responses analyzed across two LLMs\\\"\\n    how_we_differ: \\\"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\\\"\\n\\n  # ============================================================\\n  # BACKGROUND\\n  # ============================================================\\n  - id: joshi2025dialect_survey\\n    title: \\\"Natural Language Processing for Dialects of a Language: A Survey\\\"\\n    authors: \\\"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\\\"\\n    venue: \\\"ACM Computing Surveys, Vol. 57(6)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2401.05632\\\"\\n    category: background\\n    role: \\\"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"NLP models show systematic performance degradation on dialectal data\\\"\\n      - \\\"Covers NLU and NLG tasks including dialogue systems\\\"\\n      - \\\"Equity implications of language technology performance gaps\\\"\\n    how_we_differ: \\\"Survey provides broad context; we tackle a specific gap in user simulation fairness\\\"\\n\\n  - id: rickford1999aave\\n    title: \\\"African American Vernacular English: Features, Evolution, Educational Implications\\\"\\n    authors: \\\"Rickford, John Russell\\\"\\n    venue: \\\"Blackwell Publishers (Language in Society series)\\\"\\n    year: 1999\\n    url: \\\"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\\\"\\n    category: background\\n    role: \\\"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Systematic documentation of AAVE phonological and grammatical features\\\"\\n      - \\\"AAVE has distinct pragmatic conventions including directness patterns\\\"\\n      - \\\"AAVE is a fully systematic linguistic variety, not deficient English\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\\\"\\n\\n  - id: kachru2008cultures\\n    title: \\\"Cultures, Contexts, and World Englishes\\\"\\n    authors: \\\"Kachru, Yamuna; Smith, Cecil\\\"\\n    venue: \\\"Routledge\\\"\\n    year: 2008\\n    url: \\\"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\\\"\\n    category: background\\n    role: \\\"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Indian English has distinct politeness strategies rooted in face-saving norms\\\"\\n      - \\\"Requesting and disagreeing strategies differ from Inner Circle varieties\\\"\\n      - \\\"Three Circles model (Inner/Outer/Expanding) for understanding English variation\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\\\"\\n\\n  - id: sekulic2024daus\\n    title: \\\"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\\\"\\n    authors: \\\"Sekulic, Terragni, Guimaraes et al.\\\"\\n    venue: \\\"SCI-CHAT Workshop 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.13374\\\"\\n    category: background\\n    role: \\\"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\\\"\\n      - \\\"Mitigates hallucinations in simulator responses\\\"\\n      - \\\"Domain-aware approach outperforms generic prompting\\\"\\n    how_we_differ: \\\"DAUS optimizes task completion; we optimize demographic behavioral fidelity\\\"\\n\\n  - id: ahmad2025diversity\\n    title: \\\"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\\\"\\n    authors: \\\"Ahmad, Hillmann, Moller\\\"\\n    venue: \\\"arXiv 2502.12813\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.12813\\\"\\n    category: background\\n    role: \\\"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"GPT-o1 generates more heterogeneous user distributions than GPT-4o\\\"\\n      - \\\"82.46% task success across 57 dialogue sessions with diverse users\\\"\\n      - \\\"Captures variation in language styles, knowledge levels, and objectives\\\"\\n    how_we_differ: \\\"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\\\"\\n\\n  # ============================================================\\n  # NEW ADDITIONS (scan 2026-05-13)\\n  # ============================================================\\n\\n  # --- FOUNDATION (new) ---\\n  - id: sim2real2026gap\\n    title: \\\"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\\\"\\n    authors: \\\"Zhou, Sun, Xu, Chen, Radev\\\"\\n    venue: \\\"arXiv 2603.11245\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.11245\\\"\\n    category: foundation\\n    role: \\\"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\\\"\\n      - \\\"Simulated users create 'easy mode' that inflates agent success rates above human baseline\\\"\\n      - \\\"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\\\"\\n      - \\\"Higher model capability does not yield more faithful user simulation\\\"\\n    how_we_differ: \\\"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    note: \\\"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\\\"\\n\\n  # --- METHOD-COMPONENT (new) ---\\n  - id: khan2026decoding\\n    title: \\\"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\\\"\\n    authors: \\\"Khan, Muneeb Ur Raheem\\\"\\n    venue: \\\"arXiv 2605.02348\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2605.02348\\\"\\n    category: method-component\\n    role: \\\"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\\\"\\n      - \\\"No weight changes needed — debiasing happens at inference via PRM scoring\\\"\\n      - \\\"Gate calibration is model-dependent; no one-size-fits-all prompt works\\\"\\n    how_we_differ: \\\"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- EVALUATION (new) ---\\n  - id: gupta2025endive\\n    title: \\\"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\\\"\\n    authors: \\\"Gupta, Cheung et al.\\\"\\n    venue: \\\"Findings of EMNLP 2025 (arXiv 2504.07100)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2504.07100\\\"\\n    category: evaluation\\n    role: \\\"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\\\"\\n      - \\\"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\\\"\\n      - \\\"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\\\"\\n    how_we_differ: \\\"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\\n  - id: lee2024dpo_toxicity\\n    title: \\\"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\\\"\\n    authors: \\\"Lee, Panda, Yun, Bansal\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2401.01967\\\"\\n    category: method-component\\n    role: \\\"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO does not remove toxic capabilities, only bypasses them at inference\\\"\\n      - \\\"Simple un-alignment can revert model to pre-DPO behavior\\\"\\n      - \\\"Minimal parameter changes allow reversion — alignment is fragile\\\"\\n    how_we_differ: \\\"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM4 — explains why DPO training can reverse BCP calibration effect\\\"\\n\\n  - id: gupta2026intra_fairness\\n    title: \\\"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\\\"\\n    authors: \\\"Paraschou, Heiter, Iosifidis\\\"\\n    venue: \\\"arXiv 2602.16438\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16438\\\"\\n    category: method-component\\n    role: \\\"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Targeted debiasing can produce unintended negative consequences across other social axes\\\"\\n      - \\\"Bias spillover effect: altering behavior on one dimension when mitigating another\\\"\\n      - \\\"Multi-attribute fairness dynamics must be considered in alignment\\\"\\n    how_we_differ: \\\"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\\\"\\n\\n  - id: basil2025playing_pretend\\n    title: \\\"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\\\"\\n    authors: \\\"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\\\"\\n    venue: \\\"arXiv 2512.05858 (Wharton)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.05858\\\"\\n    category: method-component\\n    role: \\\"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Expert personas do not improve factual accuracy across benchmarks\\\"\\n      - \\\"Persona prompting activates instruction-following mode at expense of factual recall\\\"\\n      - \\\"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\\\"\\n    how_we_differ: \\\"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — explains mechanism behind global behavior suppression\\\"\\n\\n  - id: anonymous2026expert_persona\\n    title: \\\"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\\\"\\n    authors: \\\"Hu, Rostami, Thomason\\\"\\n    venue: \\\"arXiv 2603.18507\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.18507\\\"\\n    category: method-component\\n    role: \\\"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\\\"\\n      - \\\"Performance drops up to 30pp under persona modifications\\\"\\n      - \\\"More instruction-tuned models are more susceptible to persona-induced accuracy loss\\\"\\n    how_we_differ: \\\"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — strongest external evidence for global behavior suppression mechanism\\\"\\n\\n  # --- BACKGROUND (new) ---\\n  - id: nakash2026divert\\n    title: \\\"Efficient Agent Evaluation via Diversity-Guided User Simulation\\\"\\n    authors: \\\"Nakash, Kour, Anaby-Tavor\\\"\\n    venue: \\\"arXiv 2604.21480\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21480\\\"\\n    category: background\\n    role: \\\"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\\\"\\n      - \\\"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\\\"\\n    how_we_differ: \\\"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n# ============================================================\\n# SUMMARY\\n# ============================================================\\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\\n# - foundation: 5 (+sim2real2026gap)\\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +anonymous2026expert_persona)\\n# - evaluation: 6 (+gupta2025endive)\\n# - background: 6 (+nakash2026divert)\\n# - high relevance: 14, medium: 13, low: 1\\n#\\n# Plan B scan notes (2026-05-13):\\n# - 4 new papers added specifically for Plan B empirical analysis framing\\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\\n# - basil2025playing_pretend + anonymous2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\\n# - Also noted but not added:\\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\\n\", \"total_chars\": 26551, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "75dd0382-c311-493c-a47e-b27dbbc5302d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  # ============================================================\\\\n  # DIRECT-COMPETITOR\\\\n  # ============================================================\\\\n  # 未找到直接竞品。没有现有工作专门做\\\\\\\"校准 LLM 用户模拟器的方言行为率偏差\\\\\\\"。\\\\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\\\\n  # 这验证了 DemoCalib 的新颖性。\\\\n\\\\n  # ============================================================\\\\n  # FOUNDATION\\\\n  # ============================================================\\\\n  - id: seshadri2026lost\\\\n    title: \\\\\\\"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\\\\\\\"\\\\n    authors: \\\\\\\"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2601.17087\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.17087\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Agent success rates vary up to 9pp across different user simulator LLMs\\\\\\\"\\\\n      - \\\\\\\"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\\\\\\\"\\\\n      - \\\\\\\"Simulated users introduce conversational artifacts absent from real human users\\\\\\\"\\\\n      - \\\\\\\"Disparities compound significantly with age for AAVE speakers\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\\\\\\\"\\\\n\\\\n  - id: yao2024taubench\\\\n    title: \\\\\\\"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\\\\\\\"\\\\n    authors: \\\\\\\"Yao et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2406.12045\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.12045\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\\\\\\\"\\\\n      - \\\\\\\"Proposes pass^k metric measuring reliability over multiple trials\\\\\\\"\\\\n      - \\\\\\\"User simulator is LLM-based, enabling behavioral modification\\\\\\\"\\\\n    how_we_differ: \\\\\\\"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\\\\\\\"\\\\n\\\\n  - id: liu2024agentbench\\\\n    title: \\\\\\\"AgentBench: Evaluating LLMs as Agents\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2308.03688\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Significant performance gap between commercial and open-source LLMs as agents\\\\\\\"\\\\n      - \\\\\\\"Poor long-term reasoning and instruction following are main obstacles\\\\\\\"\\\\n    how_we_differ: \\\\\\\"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\\\\\\\"\\\\n\\\\n  - id: wang2024mint\\\\n    title: \\\\\\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\\\\\"\\\\n    authors: \\\\\\\"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2309.10691\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\\\\\\\"\\\\n      - \\\\\\\"Better single-turn performance does not guarantee better multi-turn performance\\\\\\\"\\\\n      - \\\\\\\"SIFT and RLHF generally hurt multi-turn capabilities\\\\\\\"\\\\n    how_we_differ: \\\\\\\"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # METHOD-COMPONENT\\\\n  # ============================================================\\\\n  - id: rafailov2023dpo\\\\n    title: \\\\\\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\\\\\"\\\\n    authors: \\\\\\\"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    year: 2023\\\\n    url: \\\\\\\"https://arxiv.org/abs/2305.18290\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"DPO directly optimizes policy from preference pairs without explicit reward model\\\\\\\"\\\\n      - \\\\\\\"Computationally lightweight, stable alternative to PPO-based RLHF\\\\\\\"\\\\n      - \\\\\\\"Exceeds PPO-based RLHF in controlling sentiment of generations\\\\\\\"\\\\n    how_we_differ: \\\\\\\"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\\\\\\\"\\\\n\\\\n  - id: zhao2021calibrate\\\\n    title: \\\\\\\"Calibrate Before Use: Improving Few-Shot Performance of Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhao, Wallace, Feng, Klein, Singh\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2021\\\\\\\"\\\\n    year: 2021\\\\n    url: \\\\\\\"https://arxiv.org/abs/2102.09690\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\\\\\\\"\\\\n      - \\\\\\\"Identified majority label bias, recency bias, common token bias\\\\\\\"\\\\n      - \\\\\\\"Contextual calibration with content-free inputs improves accuracy up to 30%\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\\\\\\\"\\\\n\\\\n  - id: abdulhai2025consistent\\\\n    title: \\\\\\\"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.00222\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\\\\\\\"\\\\n      - \\\\\\\"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\\\\\\\"\\\\n      - \\\\\\\"Multi-turn RL reduces inconsistency by >55%\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\\\\\\\"\\\\n\\\\n  - id: naous2025flipping\\\\n    title: \\\\\\\"Flipping the Dialogue: Training and Evaluating User Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Naous, Laban, Xu, Neville\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2510.06552\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.06552\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Better assistant LMs yield worse user simulators\\\\\\\"\\\\n      - \\\\\\\"UserLM-8b provides more realistic user simulation\\\\\\\"\\\\n      - \\\\\\\"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\\\\\\\"\\\\n\\\\n  - id: li2025persona\\\\n    title: \\\\\\\"LLM Generated Persona is a Promise with a Catch\\\\\\\"\\\\n    authors: \\\\\\\"Li, Chen et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.16527\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"LLM-generated personas systematically drift toward socially desirable traits\\\\\\\"\\\\n      - \\\\\\\"More LLM-generated content produces more left-leaning, less representative personas\\\\\\\"\\\\n      - \\\\\\\"Bias exists in the persona creation step itself, not just model responses\\\\\\\"\\\\n    how_we_differ: \\\\\\\"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\\\\\\\"\\\\n\\\\n  - id: wang2024alignment\\\\n    title: \\\\\\\"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\\\\\\\"\\\\n    authors: \\\\\\\"Wang, Bi, Pentyala et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2407.16216\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2407.16216\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\\\\\\\"\\\\n      - \\\\\\\"DPO is stable and lightweight but sensitive to preference data quality\\\\\\\"\\\\n      - \\\\\\\"Detailed comparison of PPO vs GRPO vs DPO implementation details\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # EVALUATION\\\\n  # ============================================================\\\\n  - id: lin2025redial\\\\n    title: \\\\\\\"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\\\\\\\"\\\\n    authors: \\\\\\\"Lin et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.11005\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\\\\\\\"\\\\n      - \\\\\\\"Almost all models show statistically significant performance drops on AAVE\\\\\\\"\\\\n      - \\\\\\\"AAVE performance gaps arise from morphosyntactic features and conversational norms\\\\\\\"\\\\n      - \\\\\\\"LLMs struggle more with AAVE than misspelled Standard English\\\\\\\"\\\\n    how_we_differ: \\\\\\\"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\\\\\\\"\\\\n\\\\n  - id: faisal2024dialectbench\\\\n    title: \\\\\\\"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\\\\\\\"\\\\n    authors: \\\\\\\"Faisal et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2403.11009\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"10 NLP tasks, 281 varieties, 40 language clusters\\\\\\\"\\\\n      - \\\\\\\"Substantial performance disparities between standard and non-standard varieties\\\\\\\"\\\\n      - \\\\\\\"Performance gap widens with fine-tuning due to uneven data availability\\\\\\\"\\\\n    how_we_differ: \\\\\\\"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\\\\\\\"\\\\n\\\\n  - id: gallegos2024bias\\\\n    title: \\\\\\\"Bias and Fairness in Large Language Models: A Survey\\\\\\\"\\\\n    authors: \\\\\\\"Gallegos, Rossi, Barrow et al.\\\\\\\"\\\\n    venue: \\\\\\\"Computational Linguistics, Vol. 50(3)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2309.00770\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Taxonomy of bias metrics at embedding, probability, and generated text levels\\\\\\\"\\\\n      - \\\\\\\"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\\\\\\\"\\\\n      - \\\\\\\"Consolidated public datasets for bias evaluation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\\\\\\\"\\\\n\\\\n  - id: parrish2022bbq\\\\n    title: \\\\\\\"BBQ: A Hand-Built Bias Benchmark for Question Answering\\\\\\\"\\\\n    authors: \\\\\\\"Parrish et al.\\\\\\\"\\\\n    venue: \\\\\\\"Findings of ACL 2022\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://aclanthology.org/2022.findings-acl.165/\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\\\\\\\"\\\\n    relevance: low\\\\n    key_findings:\\\\n      - \\\\\\\"58,492 unique examples across multiple bias categories\\\\\\\"\\\\n      - \\\\\\\"Evaluates both individual and intersectional biases\\\\\\\"\\\\n      - \\\\\\\"Standard benchmark for LLM bias evaluation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\\\\\\\"\\\\n\\\\n  - id: haq2026dialect\\\\n    title: \\\\\\\"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\\\\\\\"\\\\n    authors: \\\\\\\"Haq, Saldias\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2604.21152\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.21152\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\\\\\\\"\\\\n      - \\\\\\\"AAVE/Singlish users receive less sanitized content than SAE users\\\\\\\"\\\\n      - \\\\\\\"Safety alignment is brittle, over-indexed on explicit keywords\\\\\\\"\\\\n      - \\\\\\\"24,000+ responses analyzed across two LLMs\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # BACKGROUND\\\\n  # ============================================================\\\\n  - id: joshi2025dialect_survey\\\\n    title: \\\\\\\"Natural Language Processing for Dialects of a Language: A Survey\\\\\\\"\\\\n    authors: \\\\\\\"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\\\\\\\"\\\\n    venue: \\\\\\\"ACM Computing Surveys, Vol. 57(6)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2401.05632\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"NLP models show systematic performance degradation on dialectal data\\\\\\\"\\\\n      - \\\\\\\"Covers NLU and NLG tasks including dialogue systems\\\\\\\"\\\\n      - \\\\\\\"Equity implications of language technology performance gaps\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Survey provides broad context; we tackle a specific gap in user simulation fairness\\\\\\\"\\\\n\\\\n  - id: rickford1999aave\\\\n    title: \\\\\\\"African American Vernacular English: Features, Evolution, Educational Implications\\\\\\\"\\\\n    authors: \\\\\\\"Rickford, John Russell\\\\\\\"\\\\n    venue: \\\\\\\"Blackwell Publishers (Language in Society series)\\\\\\\"\\\\n    year: 1999\\\\n    url: \\\\\\\"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Systematic documentation of AAVE phonological and grammatical features\\\\\\\"\\\\n      - \\\\\\\"AAVE has distinct pragmatic conventions including directness patterns\\\\\\\"\\\\n      - \\\\\\\"AAVE is a fully systematic linguistic variety, not deficient English\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\\\\\\\"\\\\n\\\\n  - id: kachru2008cultures\\\\n    title: \\\\\\\"Cultures, Contexts, and World Englishes\\\\\\\"\\\\n    authors: \\\\\\\"Kachru, Yamuna; Smith, Cecil\\\\\\\"\\\\n    venue: \\\\\\\"Routledge\\\\\\\"\\\\n    year: 2008\\\\n    url: \\\\\\\"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Indian English has distinct politeness strategies rooted in face-saving norms\\\\\\\"\\\\n      - \\\\\\\"Requesting and disagreeing strategies differ from Inner Circle varieties\\\\\\\"\\\\n      - \\\\\\\"Three Circles model (Inner/Outer/Expanding) for understanding English variation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\\\\\\\"\\\\n\\\\n  - id: sekulic2024daus\\\\n    title: \\\\\\\"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\\\\\\\"\\\\n    authors: \\\\\\\"Sekulic, Terragni, Guimaraes et al.\\\\\\\"\\\\n    venue: \\\\\\\"SCI-CHAT Workshop 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2402.13374\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\\\\\\\"\\\\n      - \\\\\\\"Mitigates hallucinations in simulator responses\\\\\\\"\\\\n      - \\\\\\\"Domain-aware approach outperforms generic prompting\\\\\\\"\\\\n    how_we_differ: \\\\\\\"DAUS optimizes task completion; we optimize demographic behavioral fidelity\\\\\\\"\\\\n\\\\n  - id: ahmad2025diversity\\\\n    title: \\\\\\\"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Ahmad, Hillmann, Moller\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2502.12813\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.12813\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"GPT-o1 generates more heterogeneous user distributions than GPT-4o\\\\\\\"\\\\n      - \\\\\\\"82.46% task success across 57 dialogue sessions with diverse users\\\\\\\"\\\\n      - \\\\\\\"Captures variation in language styles, knowledge levels, and objectives\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # NEW ADDITIONS (scan 2026-05-13)\\\\n  # ============================================================\\\\n\\\\n  # --- FOUNDATION (new) ---\\\\n  - id: sim2real2026gap\\\\n    title: \\\\\\\"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\\\\\\\"\\\\n    authors: \\\\\\\"Zhou, Sun, Xu, Chen, Radev\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2603.11245\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.11245\\\\\\\"\\\\n    category: foundation\\\\n    role: \\\\\\\"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\\\\\\\"\\\\n      - \\\\\\\"Simulated users create 'easy mode' that inflates agent success rates above human baseline\\\\\\\"\\\\n      - \\\\\\\"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\\\\\\\"\\\\n      - \\\\\\\"Higher model capability does not yield more faithful user simulation\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    note: \\\\\\\"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\\\\\\\"\\\\n\\\\n  # --- METHOD-COMPONENT (new) ---\\\\n  - id: khan2026decoding\\\\n    title: \\\\\\\"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\\\\\\\"\\\\n    authors: \\\\\\\"Khan, Muneeb Ur Raheem\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2605.02348\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.02348\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\\\\\\\"\\\\n      - \\\\\\\"No weight changes needed — debiasing happens at inference via PRM scoring\\\\\\\"\\\\n      - \\\\\\\"Gate calibration is model-dependent; no one-size-fits-all prompt works\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n\\\\n  # --- EVALUATION (new) ---\\\\n  - id: gupta2025endive\\\\n    title: \\\\\\\"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Gupta, Cheung et al.\\\\\\\"\\\\n    venue: \\\\\\\"Findings of EMNLP 2025 (arXiv 2504.07100)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2504.07100\\\\\\\"\\\\n    category: evaluation\\\\n    role: \\\\\\\"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\\\\\\\"\\\\n      - \\\\\\\"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\\\\\\\"\\\\n      - \\\\\\\"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\\\\\\\"\\\\n    how_we_differ: \\\\\\\"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n\\\\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\\\\n  - id: lee2024dpo_toxicity\\\\n    title: \\\\\\\"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\\\\\\\"\\\\n    authors: \\\\\\\"Lee, Panda, Yun, Bansal\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2401.01967\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"DPO does not remove toxic capabilities, only bypasses them at inference\\\\\\\"\\\\n      - \\\\\\\"Simple un-alignment can revert model to pre-DPO behavior\\\\\\\"\\\\n      - \\\\\\\"Minimal parameter changes allow reversion — alignment is fragile\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM4 — explains why DPO training can reverse BCP calibration effect\\\\\\\"\\\\n\\\\n  - id: gupta2026intra_fairness\\\\n    title: \\\\\\\"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\\\\\\\"\\\\n    authors: \\\\\\\"Paraschou, Heiter, Iosifidis\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2602.16438\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.16438\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Targeted debiasing can produce unintended negative consequences across other social axes\\\\\\\"\\\\n      - \\\\\\\"Bias spillover effect: altering behavior on one dimension when mitigating another\\\\\\\"\\\\n      - \\\\\\\"Multi-attribute fairness dynamics must be considered in alignment\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\\\\\\\"\\\\n\\\\n  - id: basil2025playing_pretend\\\\n    title: \\\\\\\"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\\\\\\\"\\\\n    authors: \\\\\\\"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2512.05858 (Wharton)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.05858\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Expert personas do not improve factual accuracy across benchmarks\\\\\\\"\\\\n      - \\\\\\\"Persona prompting activates instruction-following mode at expense of factual recall\\\\\\\"\\\\n      - \\\\\\\"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM1 — explains mechanism behind global behavior suppression\\\\\\\"\\\\n\\\\n  - id: anonymous2026expert_persona\\\\n    title: \\\\\\\"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\\\\\\\"\\\\n    authors: \\\\\\\"Hu, Rostami, Thomason\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2603.18507\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.18507\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\\\\\\\"\\\\n    relevance: high\\\\n    key_findings:\\\\n      - \\\\\\\"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\\\\\\\"\\\\n      - \\\\\\\"Performance drops up to 30pp under persona modifications\\\\\\\"\\\\n      - \\\\\\\"More instruction-tuned models are more susceptible to persona-induced accuracy loss\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n    plan_b_relevance: \\\\\\\"FM1 — strongest external evidence for global behavior suppression mechanism\\\\\\\"\\\\n\\\\n  # --- BACKGROUND (new) ---\\\\n  - id: nakash2026divert\\\\n    title: \\\\\\\"Efficient Agent Evaluation via Diversity-Guided User Simulation\\\\\\\"\\\\n    authors: \\\\\\\"Nakash, Kour, Anaby-Tavor\\\\\\\"\\\\n    venue: \\\\\\\"arXiv 2604.21480\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.21480\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\\\\\\\"\\\\n    relevance: medium\\\\n    key_findings:\\\\n      - \\\\\\\"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\\\\\\\"\\\\n      - \\\\\\\"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\\\\\\\"\\\\n    how_we_differ: \\\\\\\"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\\\\\\\"\\\\n    scan_date: \\\\\\\"2026-05-13\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# SUMMARY\\\\n# ============================================================\\\\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\\\\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\\\\n# - foundation: 5 (+sim2real2026gap)\\\\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +anonymous2026expert_persona)\\\\n# - evaluation: 6 (+gupta2025endive)\\\\n# - background: 6 (+nakash2026divert)\\\\n# - high relevance: 14, medium: 13, low: 1\\\\n#\\\\n# Plan B scan notes (2026-05-13):\\\\n# - 4 new papers added specifically for Plan B empirical analysis framing\\\\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\\\\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\\\\n# - basil2025playing_pretend + anonymous2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\\\\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\\\\n# - Also noted but not added:\\\\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\\\\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\\\\n\\\", \\\"total_chars\\\": 26551, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT-COMPETITOR\\n  # ============================================================\\n  # 未找到直接竞品。没有现有工作专门做\\\"校准 LLM 用户模拟器的方言行为率偏差\\\"。\\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\\n  # 这验证了 DemoCalib 的新颖性。\\n\\n  # ============================================================\\n  # FOUNDATION\\n  # ============================================================\\n  - id: seshadri2026lost\\n    title: \\\"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\\\"\\n    authors: \\\"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\\\"\\n    venue: \\\"arXiv 2601.17087\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.17087\\\"\\n    category: foundation\\n    role: \\\"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Agent success rates vary up to 9pp across different user simulator LLMs\\\"\\n      - \\\"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\\\"\\n      - \\\"Simulated users introduce conversational artifacts absent from real human users\\\"\\n      - \\\"Disparities compound significantly with age for AAVE speakers\\\"\\n    how_we_differ: \\\"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\\\"\\n\\n  - id: yao2024taubench\\n    title: \\\"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\\\"\\n    authors: \\\"Yao et al.\\\"\\n    venue: \\\"arXiv 2406.12045\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2406.12045\\\"\\n    category: foundation\\n    role: \\\"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\\\"\\n      - \\\"Proposes pass^k metric measuring reliability over multiple trials\\\"\\n      - \\\"User simulator is LLM-based, enabling behavioral modification\\\"\\n    how_we_differ: \\\"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\\\"\\n\\n  - id: liu2024agentbench\\n    title: \\\"AgentBench: Evaluating LLMs as Agents\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2308.03688\\\"\\n    category: foundation\\n    role: \\\"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Significant performance gap between commercial and open-source LLMs as agents\\\"\\n      - \\\"Poor long-term reasoning and instruction following are main obstacles\\\"\\n    how_we_differ: \\\"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\\\"\\n\\n  - id: wang2024mint\\n    title: \\\"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\\\"\\n    authors: \\\"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.10691\\\"\\n    category: foundation\\n    role: \\\"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\\\"\\n      - \\\"Better single-turn performance does not guarantee better multi-turn performance\\\"\\n      - \\\"SIFT and RLHF generally hurt multi-turn capabilities\\\"\\n    how_we_differ: \\\"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\\\"\\n\\n  # ============================================================\\n  # METHOD-COMPONENT\\n  # ============================================================\\n  - id: rafailov2023dpo\\n    title: \\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\"\\n    authors: \\\"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    url: \\\"https://arxiv.org/abs/2305.18290\\\"\\n    category: method-component\\n    role: \\\"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO directly optimizes policy from preference pairs without explicit reward model\\\"\\n      - \\\"Computationally lightweight, stable alternative to PPO-based RLHF\\\"\\n      - \\\"Exceeds PPO-based RLHF in controlling sentiment of generations\\\"\\n    how_we_differ: \\\"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\\\"\\n\\n  - id: zhao2021calibrate\\n    title: \\\"Calibrate Before Use: Improving Few-Shot Performance of Language Models\\\"\\n    authors: \\\"Zhao, Wallace, Feng, Klein, Singh\\\"\\n    venue: \\\"ICML 2021\\\"\\n    year: 2021\\n    url: \\\"https://arxiv.org/abs/2102.09690\\\"\\n    category: method-component\\n    role: \\\"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\\\"\\n      - \\\"Identified majority label bias, recency bias, common token bias\\\"\\n      - \\\"Contextual calibration with content-free inputs improves accuracy up to 30%\\\"\\n    how_we_differ: \\\"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\\\"\\n\\n  - id: abdulhai2025consistent\\n    title: \\\"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\\\"\\n    authors: \\\"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2511.00222\\\"\\n    category: method-component\\n    role: \\\"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\\\"\\n      - \\\"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\\\"\\n      - \\\"Multi-turn RL reduces inconsistency by >55%\\\"\\n    how_we_differ: \\\"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\\\"\\n\\n  - id: naous2025flipping\\n    title: \\\"Flipping the Dialogue: Training and Evaluating User Language Models\\\"\\n    authors: \\\"Naous, Laban, Xu, Neville\\\"\\n    venue: \\\"arXiv 2510.06552\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.06552\\\"\\n    category: method-component\\n    role: \\\"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Better assistant LMs yield worse user simulators\\\"\\n      - \\\"UserLM-8b provides more realistic user simulation\\\"\\n      - \\\"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\\\"\\n    how_we_differ: \\\"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\\\"\\n\\n  - id: li2025persona\\n    title: \\\"LLM Generated Persona is a Promise with a Catch\\\"\\n    authors: \\\"Li, Chen et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.16527\\\"\\n    category: method-component\\n    role: \\\"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"LLM-generated personas systematically drift toward socially desirable traits\\\"\\n      - \\\"More LLM-generated content produces more left-leaning, less representative personas\\\"\\n      - \\\"Bias exists in the persona creation step itself, not just model responses\\\"\\n    how_we_differ: \\\"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\\\"\\n\\n  - id: wang2024alignment\\n    title: \\\"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\\\"\\n    authors: \\\"Wang, Bi, Pentyala et al.\\\"\\n    venue: \\\"arXiv 2407.16216\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2407.16216\\\"\\n    category: method-component\\n    role: \\\"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\\\"\\n      - \\\"DPO is stable and lightweight but sensitive to preference data quality\\\"\\n      - \\\"Detailed comparison of PPO vs GRPO vs DPO implementation details\\\"\\n    how_we_differ: \\\"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\\\"\\n\\n  # ============================================================\\n  # EVALUATION\\n  # ============================================================\\n  - id: lin2025redial\\n    title: \\\"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\\\"\\n    authors: \\\"Lin et al.\\\"\\n    venue: \\\"ACL 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.11005\\\"\\n    category: evaluation\\n    role: \\\"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\\\"\\n      - \\\"Almost all models show statistically significant performance drops on AAVE\\\"\\n      - \\\"AAVE performance gaps arise from morphosyntactic features and conversational norms\\\"\\n      - \\\"LLMs struggle more with AAVE than misspelled Standard English\\\"\\n    how_we_differ: \\\"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\\\"\\n\\n  - id: faisal2024dialectbench\\n    title: \\\"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\\\"\\n    authors: \\\"Faisal et al.\\\"\\n    venue: \\\"ACL 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2403.11009\\\"\\n    category: evaluation\\n    role: \\\"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"10 NLP tasks, 281 varieties, 40 language clusters\\\"\\n      - \\\"Substantial performance disparities between standard and non-standard varieties\\\"\\n      - \\\"Performance gap widens with fine-tuning due to uneven data availability\\\"\\n    how_we_differ: \\\"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\\\"\\n\\n  - id: gallegos2024bias\\n    title: \\\"Bias and Fairness in Large Language Models: A Survey\\\"\\n    authors: \\\"Gallegos, Rossi, Barrow et al.\\\"\\n    venue: \\\"Computational Linguistics, Vol. 50(3)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2309.00770\\\"\\n    category: evaluation\\n    role: \\\"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Taxonomy of bias metrics at embedding, probability, and generated text levels\\\"\\n      - \\\"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\\\"\\n      - \\\"Consolidated public datasets for bias evaluation\\\"\\n    how_we_differ: \\\"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\\\"\\n\\n  - id: parrish2022bbq\\n    title: \\\"BBQ: A Hand-Built Bias Benchmark for Question Answering\\\"\\n    authors: \\\"Parrish et al.\\\"\\n    venue: \\\"Findings of ACL 2022\\\"\\n    year: 2022\\n    url: \\\"https://aclanthology.org/2022.findings-acl.165/\\\"\\n    category: evaluation\\n    role: \\\"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\\\"\\n    relevance: low\\n    key_findings:\\n      - \\\"58,492 unique examples across multiple bias categories\\\"\\n      - \\\"Evaluates both individual and intersectional biases\\\"\\n      - \\\"Standard benchmark for LLM bias evaluation\\\"\\n    how_we_differ: \\\"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\\\"\\n\\n  - id: haq2026dialect\\n    title: \\\"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\\\"\\n    authors: \\\"Haq, Saldias\\\"\\n    venue: \\\"arXiv 2604.21152\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21152\\\"\\n    category: evaluation\\n    role: \\\"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\\\"\\n      - \\\"AAVE/Singlish users receive less sanitized content than SAE users\\\"\\n      - \\\"Safety alignment is brittle, over-indexed on explicit keywords\\\"\\n      - \\\"24,000+ responses analyzed across two LLMs\\\"\\n    how_we_differ: \\\"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\\\"\\n\\n  # ============================================================\\n  # BACKGROUND\\n  # ============================================================\\n  - id: joshi2025dialect_survey\\n    title: \\\"Natural Language Processing for Dialects of a Language: A Survey\\\"\\n    authors: \\\"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\\\"\\n    venue: \\\"ACM Computing Surveys, Vol. 57(6)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2401.05632\\\"\\n    category: background\\n    role: \\\"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"NLP models show systematic performance degradation on dialectal data\\\"\\n      - \\\"Covers NLU and NLG tasks including dialogue systems\\\"\\n      - \\\"Equity implications of language technology performance gaps\\\"\\n    how_we_differ: \\\"Survey provides broad context; we tackle a specific gap in user simulation fairness\\\"\\n\\n  - id: rickford1999aave\\n    title: \\\"African American Vernacular English: Features, Evolution, Educational Implications\\\"\\n    authors: \\\"Rickford, John Russell\\\"\\n    venue: \\\"Blackwell Publishers (Language in Society series)\\\"\\n    year: 1999\\n    url: \\\"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\\\"\\n    category: background\\n    role: \\\"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Systematic documentation of AAVE phonological and grammatical features\\\"\\n      - \\\"AAVE has distinct pragmatic conventions including directness patterns\\\"\\n      - \\\"AAVE is a fully systematic linguistic variety, not deficient English\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\\\"\\n\\n  - id: kachru2008cultures\\n    title: \\\"Cultures, Contexts, and World Englishes\\\"\\n    authors: \\\"Kachru, Yamuna; Smith, Cecil\\\"\\n    venue: \\\"Routledge\\\"\\n    year: 2008\\n    url: \\\"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\\\"\\n    category: background\\n    role: \\\"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Indian English has distinct politeness strategies rooted in face-saving norms\\\"\\n      - \\\"Requesting and disagreeing strategies differ from Inner Circle varieties\\\"\\n      - \\\"Three Circles model (Inner/Outer/Expanding) for understanding English variation\\\"\\n    how_we_differ: \\\"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\\\"\\n\\n  - id: sekulic2024daus\\n    title: \\\"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\\\"\\n    authors: \\\"Sekulic, Terragni, Guimaraes et al.\\\"\\n    venue: \\\"SCI-CHAT Workshop 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.13374\\\"\\n    category: background\\n    role: \\\"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\\\"\\n      - \\\"Mitigates hallucinations in simulator responses\\\"\\n      - \\\"Domain-aware approach outperforms generic prompting\\\"\\n    how_we_differ: \\\"DAUS optimizes task completion; we optimize demographic behavioral fidelity\\\"\\n\\n  - id: ahmad2025diversity\\n    title: \\\"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\\\"\\n    authors: \\\"Ahmad, Hillmann, Moller\\\"\\n    venue: \\\"arXiv 2502.12813\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.12813\\\"\\n    category: background\\n    role: \\\"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"GPT-o1 generates more heterogeneous user distributions than GPT-4o\\\"\\n      - \\\"82.46% task success across 57 dialogue sessions with diverse users\\\"\\n      - \\\"Captures variation in language styles, knowledge levels, and objectives\\\"\\n    how_we_differ: \\\"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\\\"\\n\\n  # ============================================================\\n  # NEW ADDITIONS (scan 2026-05-13)\\n  # ============================================================\\n\\n  # --- FOUNDATION (new) ---\\n  - id: sim2real2026gap\\n    title: \\\"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\\\"\\n    authors: \\\"Zhou, Sun, Xu, Chen, Radev\\\"\\n    venue: \\\"arXiv 2603.11245\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.11245\\\"\\n    category: foundation\\n    role: \\\"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\\\"\\n      - \\\"Simulated users create 'easy mode' that inflates agent success rates above human baseline\\\"\\n      - \\\"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\\\"\\n      - \\\"Higher model capability does not yield more faithful user simulation\\\"\\n    how_we_differ: \\\"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    note: \\\"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\\\"\\n\\n  # --- METHOD-COMPONENT (new) ---\\n  - id: khan2026decoding\\n    title: \\\"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\\\"\\n    authors: \\\"Khan, Muneeb Ur Raheem\\\"\\n    venue: \\\"arXiv 2605.02348\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2605.02348\\\"\\n    category: method-component\\n    role: \\\"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\\\"\\n      - \\\"No weight changes needed — debiasing happens at inference via PRM scoring\\\"\\n      - \\\"Gate calibration is model-dependent; no one-size-fits-all prompt works\\\"\\n    how_we_differ: \\\"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- EVALUATION (new) ---\\n  - id: gupta2025endive\\n    title: \\\"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\\\"\\n    authors: \\\"Gupta, Cheung et al.\\\"\\n    venue: \\\"Findings of EMNLP 2025 (arXiv 2504.07100)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2504.07100\\\"\\n    category: evaluation\\n    role: \\\"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\\\"\\n      - \\\"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\\\"\\n      - \\\"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\\\"\\n    how_we_differ: \\\"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\\n  - id: lee2024dpo_toxicity\\n    title: \\\"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\\\"\\n    authors: \\\"Lee, Panda, Yun, Bansal\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2401.01967\\\"\\n    category: method-component\\n    role: \\\"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"DPO does not remove toxic capabilities, only bypasses them at inference\\\"\\n      - \\\"Simple un-alignment can revert model to pre-DPO behavior\\\"\\n      - \\\"Minimal parameter changes allow reversion — alignment is fragile\\\"\\n    how_we_differ: \\\"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM4 — explains why DPO training can reverse BCP calibration effect\\\"\\n\\n  - id: gupta2026intra_fairness\\n    title: \\\"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\\\"\\n    authors: \\\"Paraschou, Heiter, Iosifidis\\\"\\n    venue: \\\"arXiv 2602.16438\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16438\\\"\\n    category: method-component\\n    role: \\\"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Targeted debiasing can produce unintended negative consequences across other social axes\\\"\\n      - \\\"Bias spillover effect: altering behavior on one dimension when mitigating another\\\"\\n      - \\\"Multi-attribute fairness dynamics must be considered in alignment\\\"\\n    how_we_differ: \\\"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\\\"\\n\\n  - id: basil2025playing_pretend\\n    title: \\\"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\\\"\\n    authors: \\\"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\\\"\\n    venue: \\\"arXiv 2512.05858 (Wharton)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.05858\\\"\\n    category: method-component\\n    role: \\\"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Expert personas do not improve factual accuracy across benchmarks\\\"\\n      - \\\"Persona prompting activates instruction-following mode at expense of factual recall\\\"\\n      - \\\"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\\\"\\n    how_we_differ: \\\"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — explains mechanism behind global behavior suppression\\\"\\n\\n  - id: anonymous2026expert_persona\\n    title: \\\"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\\\"\\n    authors: \\\"Hu, Rostami, Thomason\\\"\\n    venue: \\\"arXiv 2603.18507\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2603.18507\\\"\\n    category: method-component\\n    role: \\\"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\\\"\\n    relevance: high\\n    key_findings:\\n      - \\\"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\\\"\\n      - \\\"Performance drops up to 30pp under persona modifications\\\"\\n      - \\\"More instruction-tuned models are more susceptible to persona-induced accuracy loss\\\"\\n    how_we_differ: \\\"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n    plan_b_relevance: \\\"FM1 — strongest external evidence for global behavior suppression mechanism\\\"\\n\\n  # --- BACKGROUND (new) ---\\n  - id: nakash2026divert\\n    title: \\\"Efficient Agent Evaluation via Diversity-Guided User Simulation\\\"\\n    authors: \\\"Nakash, Kour, Anaby-Tavor\\\"\\n    venue: \\\"arXiv 2604.21480\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.21480\\\"\\n    category: background\\n    role: \\\"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\\\"\\n    relevance: medium\\n    key_findings:\\n      - \\\"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\\\"\\n      - \\\"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\\\"\\n    how_we_differ: \\\"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\\\"\\n    scan_date: \\\"2026-05-13\\\"\\n\\n# ============================================================\\n# SUMMARY\\n# ============================================================\\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\\n# - foundation: 5 (+sim2real2026gap)\\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +anonymous2026expert_persona)\\n# - evaluation: 6 (+gupta2025endive)\\n# - background: 6 (+nakash2026divert)\\n# - high relevance: 14, medium: 13, low: 1\\n#\\n# Plan B scan notes (2026-05-13):\\n# - 4 new papers added specifically for Plan B empirical analysis framing\\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\\n# - basil2025playing_pretend + anonymous2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\\n# - Also noted but not added:\\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\\n\", \"total_chars\": 26551, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BTwX7SNQdExFQdnV14ZSD3`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "filters": {
    "experiment_id": "hgate-dpo003-merged"
  },
  "fields": [
    "*"
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
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "2c2b0044-8f33-4efd-8b39-e6cbb3e925ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZMgftnpwNo4cnxt8pNskV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1110,
      "cache_read_input_tokens": 23888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1110
      },
      "output_tokens": 70,
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

_source line 13 · 2026-05-13T07:35:29.705Z_

<details><summary>↩ Tool result · `toolu_01BTwX7SNQdExFQdnV14ZSD3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0466}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "84d3de16-d70d-452e-9c7b-7197eb12a31f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0466}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0466}}"
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
The registry query for hgate-dpo003-merged returned 0 results. Let me try a broader query to find it. But I also have the data from the agent_context provided in the user message. Let me try to read the registry without filters first.

Actually, looking at the agent_context provided at the top, I already have the overcorrected data:

## hgate-dpo003-merged overcorrected 数据（from registry）
- run_1: overcorrected politeness=0.5693, baseline=0.4748 → +9.45pp


- run_2: overcorrected politeness=0.508, baseline=0.4657 → +4.23pp
- run_3: overcorrected politeness=0.581, baseline=0.5321 → +4.89pp
- run_4: overcorrected politeness=0.6371, baseline=0.5336 → +10.35pp

All four runs show overcorrection outperforming baseline with perfect consistency, and the mean improvement across runs is 7.23 percentage points. Now I'm looking at the mvp-004 overcorrected results to compare.

The single run shows a 4.6pp gain, but when I calculate the relative percentage change from the mean baseline of 0.5016, the 7.23pp absolute gap translates to about 14.4% relative improvement—which aligns with the 14.3% figure mentioned in the task. I should note that the paper_framing.md already references this hgate-dpo003-merged result at +14.3% in the evidence map. I'm verifying the numerical ranges across both models—hgate-dpo003-merged shows performance gains from +4.2pp to +10.4pp across four runs, while mvp-004 delivers a +4.6pp absolute improvement (which translates to the +8.2% relative figure already cited in the paper). The key distinction is that the paper frames results in relative percentages, so I need to align the evidence presentation accordingly.

Now I'm planning the five corrections needed: downgrading C1's evidence strength to account for the smaller sample size and single run, then reorganizing FM3 to position hgate-dpo003-merged as the primary finding with its more robust four-run consistency, while demoting mvp-004 to secondary evidence. I need to be precise with these numbers as I make the changes. I'm working through the metrics to understand how they're being reported. The range of +4.2% to +10.4% appears to be in percentage points when I check against the actual runs, while the mean of +14.3% is expressed as a relative percentage gain from baseline. It's an inconsistent way to present the data, but that's what the task specifies, so I'll stick with those numbers.

Now I need to update the FM3 overcorrection entry to use hgate-dpo003-merged as the primary evidence instead of mvp-004, and make sure those exact metrics appear in the supporting numbers and evidence map sections. I also need to replace all instances of `anonymous2026expert_persona` with `hu2026expert_persona` throughout both files, and then review the literature map to ensure everything is consistent.

Finally, I'm going through the `how_we_differ` fields to shift from Plan A language (proposing solutions like BCP + DPO calibration) to Plan B language (documenting why those approaches fail and providing a failure taxonomy instead). I'm working through how each paper relates to my approach, noting that most of my contributions involve documenting where calibration methods fail rather than claiming they succeed. The pattern is consistent across these comparisons—I'm positioning my work as identifying the limitations and failure modes of behavioral rate calibration techniques across different contexts, from dialect-specific user simulators to DPO applications, rather than proposing solutions that work. I'm refining how I frame these related work comparisons to avoid suggesting we're implementing calibration as a solution. For papers on dialect variation and behavioral simulation, I need to shift the language from "we add" or "we calibrate" toward "we investigate and document failure modes" — making clear that our contribution is understanding why these approaches don't work rather than proposing them as fixes. The key is keeping the framing neutral for background papers while being explicit about documenting limitations for papers that touch on our core problem space. I'm scanning through the entries to identify which ones use Plan A language—proposing or applying calibration methods. Most of these clearly fall into that category: they describe using BCP, DPO, or direct calibration approaches to fix behavioral rates, which is exactly the Plan A framing I need to replace with Plan B language that acknowledges why these methods fail instead. I'm noting that FM2's question_rate baseline is quite small at 0.044, so the absolute changes are modest. Now I need to update the paper_framing.md file with several corrections—starting with downgrading C1's evidence strength from Strong to Moderate since it's based on a single model run with limited samples, then reorganizing the FM3 findings to reflect the actual effect sizes more accurately. Now I'm updating the evidence map table to reflect the stronger hgate-dpo003-merged results as the primary finding, with mvp-004 as supporting evidence, and replacing the reference ID throughout the document.

For FM2, I need to add a base rate caveat to the supporting numbers section that contextualizes the question_rate baseline value. I'm reviewing the metrics and need to make sure the paper captures both absolute values and relative changes clearly. The C2 table comparison between the base and DPO versions looks good as is since it's showing the amplification effect.

Now I need to update the Evidence Map — the FM3 entry currently has hgate-dpo003-merged as secondary, but it should be primary. I'm also going to make edits to the paper_framing.md file and update literature_map.yaml. For the YAML file, I need to replace the `anonymous2026expert_persona` identifier throughout and update the `how_we_differ` fields to use the Plan B language instead.

Looking at the structure, the id field and all references need to change from `anonymous2026expert_persona` to `hu2026expert_persona`. I can see this identifier appears in FM1, RC1, C4, and the Key Literature Anchors table in paper_framing.md. I should verify which files I can actually save — the tool supports memory.md, writing_plan.yaml, and paper_framing.md, so I'll need to check if literature_map.yaml is writable. I need to decide between using the Edit tool for targeted changes versus save_project_file for the full file overwrite. Since I have multiple edits to make across both paper_framing.md and literature_map.yaml, the Edit tool is the safer approach to avoid introducing errors. Let me start making those changes now. I'll use the Read tool on both files first to satisfy the edit requirements, then make my changes—using save_project_file for paper_framing.md and the Edit tool for literature_map.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "51cb7306-849f-46a8-89f1-924a8a7b2282",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JWvTNW5yWXHLEqNdmYFJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13591,
      "cache_read_input_tokens": 24998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13591
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

Registry 查询 hgate-dpo003-merged 返回空，但 agent_context 已提供数据。两个文件都已读取完毕。现在读取文件路径以便直接编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "9857b9f0-2cf4-4399-a9fa-150c827959a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JWvTNW5yWXHLEqNdmYFJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13591,
      "cache_read_input_tokens": 24998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13591
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

<details open><summary>🔧 Tool call — Read · `toolu_01NAPXYzBvYySaBU8DhFc55s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "7acdde38-8f17-40de-96ce-24c21d257d4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JWvTNW5yWXHLEqNdmYFJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13591,
      "cache_read_input_tokens": 24998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13591
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

_source line 17 · 2026-05-13T07:37:24.511Z_

<details><summary>↩ Tool result · `toolu_01NAPXYzBvYySaBU8DhFc55s`</summary>

```text
1	# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators
2	
3	> Plan B story — Director approved 2026-05-13
4	> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)
5	
6	---
7	
8	## Title Candidates
9	
10	1. **"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation"**
11	   - Pro: 直接点明贡献（taxonomy），关键词覆盖好
12	   - Con: 稍长
13	
14	2. **"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators"**
15	   - Pro: "trap" 吸引眼球，涵盖两种方法
16	   - Con: 可能暗示过于 negative
17	
18	3. **"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation"**
19	   - Pro: Dijkstra 风格标题引发好奇，问号留余地
20	   - Con: "Considered Harmful" 可能被认为 cliché
21	
22	**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。
23	
24	---
25	
26	## Core Story
27	
28	**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.
29	
30	**Attempted Solution**: We apply two complementary calibration strategies:
31	- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates
32	- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs
33	
34	**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.
35	
36	**Framing**: This is NOT "we tried and failed." This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.
37	
38	---
39	
40	## Core Claims
41	
42	### C1: BCP produces three systematic failure mechanisms
43	**Evidence strength**: Strong (single model, clean data)
44	
45	| Failure Mode | Description | Key Metric | exp_id |
46	|---|---|---|---|
47	| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |
48	| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |
49	| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |
50	
51	**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:
52	- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193
53	- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)
54	- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)
55	
56	**External support**:
57	- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)
58	- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)
59	- FM3: no direct external parallel — novel observation
60	
61	### C2: DPO+BCP interaction produces calibration reversal
62	**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)
63	
64	DPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:
65	
66	| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |
67	|---|---|---|
68	| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |
69	| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |
70	| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |
71	| Variant×run checks with gap expansion | — | **10/12** |
72	| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |
73	
74	**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.
75	
76	**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)
77	
78	### C3: Cross-scale validation
79	**Evidence strength**: [PENDING: qwen14b-bcp-001]
80	
81	Qwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).
82	
83	**Current auxiliary evidence**:
84	- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports "behavior shift observable at floor completion." **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.
85	- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.
86	
87	**Hedging strategy**: If Qwen14B replicates → "failure modes persist across model scales (7B, 14B)." If not → limit scope to "documented on Qwen2.5-7B; generalizability requires further investigation."
88	
89	### C4: Implications for future calibration research
90	**Evidence strength**: Analytical (grounded in C1-C3)
91	
92	- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.
93	- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).
94	- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.
95	- **Implication 4**: Overcorrection rebound (FM3) suggests models have an "attractor basin" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.
96	
97	---
98	
99	## Reviewer Concerns (Pre-empted Attack Surfaces)
100	
101	### RC1: "Single model — how do we know this generalizes?"
102	**Status**: Partially mitigated
103	- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence
104	- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them
105	- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona
106	- **Honest hedge**: "We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work."
107	
108	### RC2: "n=20 tasks, high variance — statistical power?"
109	**Response**:
110	- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.
111	- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.
112	- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.
113	- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.
114	
115	### RC3: "This is just negative results — where's the contribution?"
116	**Response**:
117	- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:
118	  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)
119	  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass
120	  3. **Actionable implications**: Concrete constraints for future calibration methods
121	  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction
122	
123	### RC4: "Why not try other calibration methods?"
124	**Response**:
125	- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.
126	- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.
127	- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).
128	
129	### RC5: "The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?"
130	**Response**:
131	- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).
132	- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.
133	- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.
134	
135	---
136	
137	## Evidence Map
138	
139	| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |
140	|---|---|---|---|---|---|
141	| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |
142	| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |
143	| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |
144	| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |
145	| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |
146	| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |
147	| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |
148	| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |
149	| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |
150	
151	---
152	
153	## Contribution Statement
154	
155	We present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.
156	
157	---
158	
159	## Key Literature Anchors
160	
161	| Role in Paper | Paper | What It Provides |
162	|---|---|---|
163	| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |
164	| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |
165	| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |
166	| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |
167	| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |
168	| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |
169	| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |
170	| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |
171	
172	---
173	
174	## Open Items
175	
176	- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.
177	- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.
178	- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.
179	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "9b4ac877-d444-4bf1-92ad-914387c11337",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
      "content": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Strong (single model, clean data)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
      "numLines": 179,
      "startLine": 1,
      "totalLines": 179
    }
  }
}
```

</details>

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01HqguePhxYhKqWk6ovcQj34`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "fd0503eb-1a04-436f-a3bb-b64ca242402c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JWvTNW5yWXHLEqNdmYFJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13591,
      "cache_read_input_tokens": 24998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13591
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

_source line 19 · 2026-05-13T07:37:24.951Z_

<details><summary>↩ Tool result · `toolu_01HqguePhxYhKqWk6ovcQj34`</summary>

```text
1	papers:
2	  # ============================================================
3	  # DIRECT-COMPETITOR
4	  # ============================================================
5	  # 未找到直接竞品。没有现有工作专门做"校准 LLM 用户模拟器的方言行为率偏差"。
6	  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。
7	  # 这验证了 DemoCalib 的新颖性。
8	
9	  # ============================================================
10	  # FOUNDATION
11	  # ============================================================
12	  - id: seshadri2026lost
13	    title: "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations"
14	    authors: "Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant"
15	    venue: "arXiv 2601.17087"
16	    year: 2026
17	    url: "https://arxiv.org/abs/2601.17087"
18	    category: foundation
19	    role: "Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration"
20	    relevance: high
21	    key_findings:
22	      - "Agent success rates vary up to 9pp across different user simulator LLMs"
23	      - "AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers"
24	      - "Simulated users introduce conversational artifacts absent from real human users"
25	      - "Disparities compound significantly with age for AAVE speakers"
26	    how_we_differ: "They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps"
27	
28	  - id: yao2024taubench
29	    title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
30	    authors: "Yao et al."
31	    venue: "arXiv 2406.12045"
32	    year: 2024
33	    url: "https://arxiv.org/abs/2406.12045"
34	    category: foundation
35	    role: "The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric"
36	    relevance: high
37	    key_findings:
38	      - "Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail"
39	      - "Proposes pass^k metric measuring reliability over multiple trials"
40	      - "User simulator is LLM-based, enabling behavioral modification"
41	    how_we_differ: "We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates"
42	
43	  - id: liu2024agentbench
44	    title: "AgentBench: Evaluating LLMs as Agents"
45	    authors: "Liu et al."
46	    venue: "ICLR 2024"
47	    year: 2024
48	    url: "https://arxiv.org/abs/2308.03688"
49	    category: foundation
50	    role: "Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments"
51	    relevance: medium
52	    key_findings:
53	      - "Significant performance gap between commercial and open-source LLMs as agents"
54	      - "Poor long-term reasoning and instruction following are main obstacles"
55	    how_we_differ: "AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness"
56	
57	  - id: wang2024mint
58	    title: "MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback"
59	    authors: "Wang, Wang, Liu, Chen, Yuan, Peng, Ji"
60	    venue: "ICLR 2024"
61	    year: 2024
62	    url: "https://arxiv.org/abs/2309.10691"
63	    category: foundation
64	    role: "Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance"
65	    relevance: medium
66	    key_findings:
67	      - "LLMs benefit 1-8% per turn from tools, 2-17% from language feedback"
68	      - "Better single-turn performance does not guarantee better multi-turn performance"
69	      - "SIFT and RLHF generally hurt multi-turn capabilities"
70	    how_we_differ: "MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration"
71	
72	  # ============================================================
73	  # METHOD-COMPONENT
74	  # ============================================================
75	  - id: rafailov2023dpo
76	    title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
77	    authors: "Rafailov, Sharma, Mitchell, Manning, Ermon, Finn"
78	    venue: "NeurIPS 2023"
79	    year: 2023
80	    url: "https://arxiv.org/abs/2305.18290"
81	    category: method-component
82	    role: "Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training"
83	    relevance: high
84	    key_findings:
85	      - "DPO directly optimizes policy from preference pairs without explicit reward model"
86	      - "Computationally lightweight, stable alternative to PPO-based RLHF"
87	      - "Exceeds PPO-based RLHF in controlling sentiment of generations"
88	    how_we_differ: "We apply DPO specifically to align user simulator behavioral rates with target dialect distributions"
89	
90	  - id: zhao2021calibrate
91	    title: "Calibrate Before Use: Improving Few-Shot Performance of Language Models"
92	    authors: "Zhao, Wallace, Feng, Klein, Singh"
93	    venue: "ICML 2021"
94	    year: 2021
95	    url: "https://arxiv.org/abs/2102.09690"
96	    category: method-component
97	    role: "Foundational calibration method for LLMs; contextual calibration corrects output distribution biases"
98	    relevance: medium
99	    key_findings:
100	      - "Few-shot accuracy varies from near chance to near SOTA depending on prompt format"
101	      - "Identified majority label bias, recency bias, common token bias"
102	      - "Contextual calibration with content-free inputs improves accuracy up to 30%"
103	    how_we_differ: "They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation"
104	
105	  - id: abdulhai2025consistent
106	    title: "Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning"
107	    authors: "Abdulhai, Cheng, Clay, Althoff, Levine, Jaques"
108	    venue: "NeurIPS 2025"
109	    year: 2025
110	    url: "https://arxiv.org/abs/2511.00222"
111	    category: method-component
112	    role: "Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns"
113	    relevance: high
114	    key_findings:
115	      - "Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue"
116	      - "Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency"
117	      - "Multi-turn RL reduces inconsistency by >55%"
118	    how_we_differ: "They optimize persona consistency in general; we specifically target dialect behavioral rate calibration"
119	
120	  - id: naous2025flipping
121	    title: "Flipping the Dialogue: Training and Evaluating User Language Models"
122	    authors: "Naous, Laban, Xu, Neville"
123	    venue: "arXiv 2510.06552"
124	    year: 2025
125	    url: "https://arxiv.org/abs/2510.06552"
126	    category: method-component
127	    role: "Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models"
128	    relevance: high
129	    key_findings:
130	      - "Better assistant LMs yield worse user simulators"
131	      - "UserLM-8b provides more realistic user simulation"
132	      - "GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation"
133	    how_we_differ: "They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups"
134	
135	  - id: li2025persona
136	    title: "LLM Generated Persona is a Promise with a Catch"
137	    authors: "Li, Chen et al."
138	    venue: "NeurIPS 2025"
139	    year: 2025
140	    url: "https://arxiv.org/abs/2503.16527"
141	    category: method-component
142	    role: "Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation"
143	    relevance: medium
144	    key_findings:
145	      - "LLM-generated personas systematically drift toward socially desirable traits"
146	      - "More LLM-generated content produces more left-leaning, less representative personas"
147	      - "Bias exists in the persona creation step itself, not just model responses"
148	    how_we_differ: "We bypass persona generation biases by directly injecting behavioral rate targets via BCP"
149	
150	  - id: wang2024alignment
151	    title: "A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More"
152	    authors: "Wang, Bi, Pentyala et al."
153	    venue: "arXiv 2407.16216"
154	    year: 2024
155	    url: "https://arxiv.org/abs/2407.16216"
156	    category: method-component
157	    role: "Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology"
158	    relevance: medium
159	    key_findings:
160	      - "Unified policy gradient framework for pretraining, SFT, RLHF, RLVR"
161	      - "DPO is stable and lightweight but sensitive to preference data quality"
162	      - "Detailed comparison of PPO vs GRPO vs DPO implementation details"
163	    how_we_differ: "Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)"
164	
165	  # ============================================================
166	  # EVALUATION
167	  # ============================================================
168	  - id: lin2025redial
169	    title: "Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks"
170	    authors: "Lin et al."
171	    venue: "ACL 2025"
172	    year: 2025
173	    url: "https://arxiv.org/abs/2410.11005"
174	    category: evaluation
175	    role: "First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE"
176	    relevance: high
177	    key_findings:
178	      - "1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks"
179	      - "Almost all models show statistically significant performance drops on AAVE"
180	      - "AAVE performance gaps arise from morphosyntactic features and conversational norms"
181	      - "LLMs struggle more with AAVE than misspelled Standard English"
182	    how_we_differ: "ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation"
183	
184	  - id: faisal2024dialectbench
185	    title: "DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages"
186	    authors: "Faisal et al."
187	    venue: "ACL 2024"
188	    year: 2024
189	    url: "https://arxiv.org/abs/2403.11009"
190	    category: evaluation
191	    role: "Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties"
192	    relevance: medium
193	    key_findings:
194	      - "10 NLP tasks, 281 varieties, 40 language clusters"
195	      - "Substantial performance disparities between standard and non-standard varieties"
196	      - "Performance gap widens with fine-tuning due to uneven data availability"
197	    how_we_differ: "DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators"
198	
199	  - id: gallegos2024bias
200	    title: "Bias and Fairness in Large Language Models: A Survey"
201	    authors: "Gallegos, Rossi, Barrow et al."
202	    venue: "Computational Linguistics, Vol. 50(3)"
203	    year: 2024
204	    url: "https://arxiv.org/abs/2309.00770"
205	    category: evaluation
206	    role: "Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets"
207	    relevance: medium
208	    key_findings:
209	      - "Taxonomy of bias metrics at embedding, probability, and generated text levels"
210	      - "Mitigation methods categorized by intervention stage: pre/in/intra/post-processing"
211	      - "Consolidated public datasets for bias evaluation"
212	    how_we_differ: "Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)"
213	
214	  - id: parrish2022bbq
215	    title: "BBQ: A Hand-Built Bias Benchmark for Question Answering"
216	    authors: "Parrish et al."
217	    venue: "Findings of ACL 2022"
218	    year: 2022
219	    url: "https://aclanthology.org/2022.findings-acl.165/"
220	    category: evaluation
221	    role: "Established bias benchmark for QA; evaluates social biases across multiple demographic categories"
222	    relevance: low
223	    key_findings:
224	      - "58,492 unique examples across multiple bias categories"
225	      - "Evaluates both individual and intersectional biases"
226	      - "Standard benchmark for LLM bias evaluation"
227	    how_we_differ: "BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation"
228	
229	  - id: haq2026dialect
230	    title: "Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles"
231	    authors: "Haq, Saldias"
232	    venue: "arXiv 2604.21152"
233	    year: 2026
234	    url: "https://arxiv.org/abs/2604.21152"
235	    category: evaluation
236	    role: "Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior"
237	    relevance: high
238	    key_findings:
239	      - "Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero"
240	      - "AAVE/Singlish users receive less sanitized content than SAE users"
241	      - "Safety alignment is brittle, over-indexed on explicit keywords"
242	      - "24,000+ responses analyzed across two LLMs"
243	    how_we_differ: "They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates"
244	
245	  # ============================================================
246	  # BACKGROUND
247	  # ============================================================
248	  - id: joshi2025dialect_survey
249	    title: "Natural Language Processing for Dialects of a Language: A Survey"
250	    authors: "Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold"
251	    venue: "ACM Computing Surveys, Vol. 57(6)"
252	    year: 2025
253	    url: "https://arxiv.org/abs/2401.05632"
254	    category: background
255	    role: "Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties"
256	    relevance: medium
257	    key_findings:
258	      - "NLP models show systematic performance degradation on dialectal data"
259	      - "Covers NLU and NLG tasks including dialogue systems"
260	      - "Equity implications of language technology performance gaps"
261	    how_we_differ: "Survey provides broad context; we tackle a specific gap in user simulation fairness"
262	
263	  - id: rickford1999aave
264	    title: "African American Vernacular English: Features, Evolution, Educational Implications"
265	    authors: "Rickford, John Russell"
266	    venue: "Blackwell Publishers (Language in Society series)"
267	    year: 1999
268	    url: "https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450"
269	    category: background
270	    role: "Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets"
271	    relevance: medium
272	    key_findings:
273	      - "Systematic documentation of AAVE phonological and grammatical features"
274	      - "AAVE has distinct pragmatic conventions including directness patterns"
275	      - "AAVE is a fully systematic linguistic variety, not deficient English"
276	    how_we_differ: "Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward"
277	
278	  - id: kachru2008cultures
279	    title: "Cultures, Contexts, and World Englishes"
280	    authors: "Kachru, Yamuna; Smith, Cecil"
281	    venue: "Routledge"
282	    year: 2008
283	    url: "https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338"
284	    category: background
285	    role: "Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes"
286	    relevance: medium
287	    key_findings:
288	      - "Indian English has distinct politeness strategies rooted in face-saving norms"
289	      - "Requesting and disagreeing strategies differ from Inner Circle varieties"
290	      - "Three Circles model (Inner/Outer/Expanding) for understanding English variation"
291	    how_we_differ: "Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate"
292	
293	  - id: sekulic2024daus
294	    title: "Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems"
295	    authors: "Sekulic, Terragni, Guimaraes et al."
296	    venue: "SCI-CHAT Workshop 2024"
297	    year: 2024
298	    url: "https://arxiv.org/abs/2402.13374"
299	    category: background
300	    role: "DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination"
301	    relevance: medium
302	    key_findings:
303	      - "Fine-tuning LLMs on real dialogue examples improves user goal fulfillment"
304	      - "Mitigates hallucinations in simulator responses"
305	      - "Domain-aware approach outperforms generic prompting"
306	    how_we_differ: "DAUS optimizes task completion; we optimize demographic behavioral fidelity"
307	
308	  - id: ahmad2025diversity
309	    title: "Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models"
310	    authors: "Ahmad, Hillmann, Moller"
311	    venue: "arXiv 2502.12813"
312	    year: 2025
313	    url: "https://arxiv.org/abs/2502.12813"
314	    category: background
315	    role: "Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation"
316	    relevance: medium
317	    key_findings:
318	      - "GPT-o1 generates more heterogeneous user distributions than GPT-4o"
319	      - "82.46% task success across 57 dialogue sessions with diverse users"
320	      - "Captures variation in language styles, knowledge levels, and objectives"
321	    how_we_differ: "They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions"
322	
323	  # ============================================================
324	  # NEW ADDITIONS (scan 2026-05-13)
325	  # ============================================================
326	
327	  # --- FOUNDATION (new) ---
328	  - id: sim2real2026gap
329	    title: "Mind the Sim2Real Gap in User Simulation for Agentic Tasks"
330	    authors: "Zhou, Sun, Xu, Chen, Radev"
331	    venue: "arXiv 2603.11245"
332	    year: 2026
333	    url: "https://arxiv.org/abs/2603.11245"
334	    category: foundation
335	    role: "First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence"
336	    relevance: high
337	    key_findings:
338	      - "LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity"
339	      - "Simulated users create 'easy mode' that inflates agent success rates above human baseline"
340	      - "Simulated feedback is uniformly positive; humans express calibrated dissatisfaction"
341	      - "Higher model capability does not yield more faithful user simulation"
342	    how_we_differ: "They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups"
343	    scan_date: "2026-05-13"
344	    note: "Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix."
345	
346	  # --- METHOD-COMPONENT (new) ---
347	  - id: khan2026decoding
348	    title: "Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation"
349	    authors: "Khan, Muneeb Ur Raheem"
350	    venue: "arXiv 2605.02348"
351	    year: 2026
352	    url: "https://arxiv.org/abs/2605.02348"
353	    category: method-component
354	    role: "Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach"
355	    relevance: medium
356	    key_findings:
357	      - "Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency"
358	      - "No weight changes needed — debiasing happens at inference via PRM scoring"
359	      - "Gate calibration is model-dependent; no one-size-fits-all prompt works"
360	    how_we_differ: "They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions"
361	    scan_date: "2026-05-13"
362	
363	  # --- EVALUATION (new) ---
364	  - id: gupta2025endive
365	    title: "EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models"
366	    authors: "Gupta, Cheung et al."
367	    venue: "Findings of EMNLP 2025 (arXiv 2504.07100)"
368	    year: 2025
369	    url: "https://arxiv.org/abs/2504.07100"
370	    category: evaluation
371	    role: "Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects"
372	    relevance: high
373	    key_findings:
374	      - "Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English"
375	      - "Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)"
376	      - "LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic"
377	    how_we_differ: "EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups"
378	    scan_date: "2026-05-13"
379	
380	  # --- METHOD-COMPONENT (new, Plan B relevant) ---
381	  - id: lee2024dpo_toxicity
382	    title: "A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity"
383	    authors: "Lee, Panda, Yun, Bansal"
384	    venue: "ICML 2024"
385	    year: 2024
386	    url: "https://arxiv.org/abs/2401.01967"
387	    category: method-component
388	    role: "Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction"
389	    relevance: high
390	    key_findings:
391	      - "DPO does not remove toxic capabilities, only bypasses them at inference"
392	      - "Simple un-alignment can revert model to pre-DPO behavior"
393	      - "Minimal parameter changes allow reversion — alignment is fragile"
394	    how_we_differ: "They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode"
395	    scan_date: "2026-05-13"
396	    plan_b_relevance: "FM4 — explains why DPO training can reverse BCP calibration effect"
397	
398	  - id: gupta2026intra_fairness
399	    title: "Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment"
400	    authors: "Paraschou, Heiter, Iosifidis"
401	    venue: "arXiv 2602.16438"
402	    year: 2026
403	    url: "https://arxiv.org/abs/2602.16438"
404	    category: method-component
405	    role: "Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference"
406	    relevance: high
407	    key_findings:
408	      - "Targeted debiasing can produce unintended negative consequences across other social axes"
409	      - "Bias spillover effect: altering behavior on one dimension when mitigating another"
410	      - "Multi-attribute fairness dynamics must be considered in alignment"
411	    how_we_differ: "They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration"
412	    scan_date: "2026-05-13"
413	    plan_b_relevance: "FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims"
414	
415	  - id: basil2025playing_pretend
416	    title: "Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy"
417	    authors: "Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke"
418	    venue: "arXiv 2512.05858 (Wharton)"
419	    year: 2025
420	    url: "https://arxiv.org/abs/2512.05858"
421	    category: method-component
422	    role: "Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse"
423	    relevance: high
424	    key_findings:
425	      - "Expert personas do not improve factual accuracy across benchmarks"
426	      - "Persona prompting activates instruction-following mode at expense of factual recall"
427	      - "MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona"
428	    how_we_differ: "They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion"
429	    scan_date: "2026-05-13"
430	    plan_b_relevance: "FM1 — explains mechanism behind global behavior suppression"
431	
432	  - id: anonymous2026expert_persona
433	    title: "Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM"
434	    authors: "Hu, Rostami, Thomason"
435	    venue: "arXiv 2603.18507"
436	    year: 2026
437	    url: "https://arxiv.org/abs/2603.18507"
438	    category: method-component
439	    role: "Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse"
440	    relevance: high
441	    key_findings:
442	      - "Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks"
443	      - "Performance drops up to 30pp under persona modifications"
444	      - "More instruction-tuned models are more susceptible to persona-induced accuracy loss"
445	    how_we_differ: "They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts"
446	    scan_date: "2026-05-13"
447	    plan_b_relevance: "FM1 — strongest external evidence for global behavior suppression mechanism"
448	
449	  # --- BACKGROUND (new) ---
450	  - id: nakash2026divert
451	    title: "Efficient Agent Evaluation via Diversity-Guided User Simulation"
452	    authors: "Nakash, Kour, Anaby-Tavor"
453	    venue: "arXiv 2604.21480"
454	    year: 2026
455	    url: "https://arxiv.org/abs/2604.21480"
456	    category: background
457	    role: "DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation"
458	    relevance: medium
459	    key_findings:
460	      - "Snapshot-based branching avoids redundant regeneration of early conversation prefixes"
461	      - "Coverage-guided exploration uncovers deep failure modes from rare user behaviors"
462	    how_we_differ: "They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups"
463	    scan_date: "2026-05-13"
464	
465	# ============================================================
466	# SUMMARY
467	# ============================================================
468	# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)
469	# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)
470	# - foundation: 5 (+sim2real2026gap)
471	# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +anonymous2026expert_persona)
472	# - evaluation: 6 (+gupta2025endive)
473	# - background: 6 (+nakash2026divert)
474	# - high relevance: 14, medium: 13, low: 1
475	#
476	# Plan B scan notes (2026-05-13):
477	# - 4 new papers added specifically for Plan B empirical analysis framing
478	# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)
479	# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)
480	# - basil2025playing_pretend + anonymous2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)
481	# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed
482	# - Also noted but not added:
483	#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain
484	#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures
485	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "13e5f853-e674-4cbf-9b23-bcd8d8e35d88",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
      "content": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: anonymous2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +anonymous2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + anonymous2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
      "numLines": 485,
      "startLine": 1,
      "totalLines": 485
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
Now I have both files read. Let me execute all 5 corrections. I'll make the edits now.

Let me organize the edits:

**paper_framing.md edits:**

1. 修正1: C1 evidence strength
2. 修正2: FM3 table row, supporting numbers, evidence map
3. 修正3: anonymous2026expert_persona → hu2026expert_persona (multiple places)
4. 修正5: FM2 base rate annotation


5. **literature_map.yaml edits:**
   - 修正3: anonymous2026expert_persona → hu2026expert_persona (id and summary comment)
   - 修正4: how_we_differ updates for Plan B

Let me start making all the edits. I'll batch independent edits together.

For paper_framing.md, I'm updating the C1 evidence strength to reflect the more conservative assessment, then fixing the FM3 table row with the corrected numbers and evidence map reference. I'm also replacing all instances of the anonymous persona identifier with the hu2026 version, and updating the FM2 base rate annotation.

For literature_map.yaml, I'm making the same persona identifier swap and updating the Plan B differentiation points. I'm noting that the FM3 results show consistent overcorrection across all four runs with hgate-dpo003-merged, while mvp-004 only has a single run for comparison. For FM2, I need to flag that the 52.3% drop in question_rate is misleading without context—the baseline is already quite low at around 0.044 questions per task, so the absolute change is much smaller than the percentage suggests, and the paper should report both figures.

Now I'm moving through several edits: replacing the anonymous2026expert_persona references with hu2026expert_persona across the paper_framing.md and literature_map.yaml files, then continuing with edits 11 through 26.

I should batch the replace_all operations since they're independent, then handle the individual how_we_differ edits sequentially to avoid any overlap issues. I need to verify that each string I'm targeting appears uniquely in its file, since the edit tool will fail otherwise. Looking at the occurrences, `anonymous2026expert_persona` shows up multiple times in both files, so using replace_all=true will handle all of them at once. Let me compile all these edits into a single batch and execute them together.

Now I'm going through the how_we_differ section in literature_map.yaml and reframing each comparison to emphasize our contribution as documenting failure modes rather than proposing solutions. The changes shift the narrative from "we fix the problem" to "we expose why existing approaches don't work," starting with seshadri2026lost and moving through yao2024taubench, wang2024mint, and rafailov2023dpo. I'm continuing to revise how I frame each related work comparison, shifting from claiming novel contributions to documenting where the calibration approach breaks down. For the remaining papers, I'm applying the same pattern: acknowledging what prior work does, then emphasizing the failure modes and limitations we encounter when attempting behavioral rate calibration in user simulators. I'm documenting how training-time calibration approaches like BCP and DPO fail to correct behavioral rates across dialect groups, which motivates exploring decoding-time alternatives instead. I'm also systematizing how my work differs from related papers—showing that while prior work optimizes task completion or generates diverse profiles, I'm specifically documenting the failure modes when trying to calibrate user simulator behavioral fidelity to match real dialect distributions. I'm working through a large set of edits across multiple files to shift the framing from active claims to documented observations. Most of the literature map entries are already neutralized or don't need changes, and I've identified which ones require rewording. Now I need to organize these edits efficiently and tackle the paper_framing.md file systematically. I'm confident the parallel approach will work since all the edits target unique, non-overlapping strings—the replace_all of `anonymous2026expert_persona` won't interfere with the other edits since none of them reference that string. Let me batch and execute them all at once.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "208ee1d7-6372-48e8-9bea-ca13d5b35a79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 21_

两个文件都已读取。开始执行 5 项修正，并行提交所有编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "852f44de-18a6-434a-a7f4-3d4d42ccde25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01AhnAH4jZAaDmSu8p52BCtk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "old_string": "**Evidence strength**: Strong (single model, clean data)",
  "new_string": "**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "ebd7b528-f940-4971-855e-6684055cfb19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 23 · 2026-05-13T07:38:41.810Z_

<details><summary>↩ Tool result · `toolu_01AhnAH4jZAaDmSu8p52BCtk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "c08e529c-ffd7-4189-b8a1-48dbae22930e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
    "oldString": "**Evidence strength**: Strong (single model, clean data)",
    "newString": "**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)",
    "originalFile": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Strong (single model, clean data)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 7,
        "newStart": 40,
        "newLines": 7,
        "lines": [
          " ## Core Claims",
          " ",
          " ### C1: BCP produces three systematic failure mechanisms",
          "-**Evidence strength**: Strong (single model, clean data)",
          "+**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)",
          " ",
          " | Failure Mode | Description | Key Metric | exp_id |",
          " |---|---|---|---|"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01FVxQor4aSNWdQZYHzP9yrw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "old_string": "| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |",
  "new_string": "| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "2848e066-3816-42fb-a3b2-5fcacfbbeb74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 25 · 2026-05-13T07:38:43.842Z_

<details><summary>↩ Tool result · `toolu_01FVxQor4aSNWdQZYHzP9yrw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "333577a1-2b82-42d1-b6bd-82bcd18270bc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
    "oldString": "| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |",
    "newString": "| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |",
    "originalFile": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
    "structuredPatch": [
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 46,
        "newLines": 7,
        "lines": [
          " |---|---|---|---|",
          " | FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |",
          " | FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |",
          "-| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected variant politeness +8.2% above baseline | mvp-004 |",
          "+| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |",
          " ",
          " **Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:",
          " - FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01BmR9FHqnnwZTM3bxj2H8Uc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "old_string": "- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)",
  "new_string": "- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "d3710d0f-0b66-4105-90ea-4da65a83fa97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 27 · 2026-05-13T07:38:45.083Z_

<details><summary>↩ Tool result · `toolu_01BmR9FHqnnwZTM3bxj2H8Uc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "39db32d6-e154-440f-a16b-5091ae3fff02",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
    "oldString": "- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)",
    "newString": "- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)",
    "originalFile": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
    "structuredPatch": [
      {
        "oldStart": 51,
        "oldLines": 7,
        "newStart": 51,
        "newLines": 7,
        "lines": [
          " **Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:",
          " - FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193",
          " - FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)",
          "-- FM3: overcorrected politeness 0.605 vs baseline 0.559 (+8.2%)",
          "+- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)",
          " ",
          " **External support**:",
          " - FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_016XNxc2sne9bkJyp1j1MCBf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "old_string": "- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)",
  "new_string": "- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "053b0496-3953-41d9-90ba-41a0a5636acb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 29 · 2026-05-13T07:38:46.990Z_

<details><summary>↩ Tool result · `toolu_016XNxc2sne9bkJyp1j1MCBf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "ccbe40ea-e33b-457a-8ca5-1e7d5671830b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
    "oldString": "- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)",
    "newString": "- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.",
    "originalFile": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
    "structuredPatch": [
      {
        "oldStart": 51,
        "oldLines": 6,
        "newStart": 51,
        "newLines": 7,
        "lines": [
          " **Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:",
          " - FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193",
          " - FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)",
          "+  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.",
          " - FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)",
          " ",
          " **External support**:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01RL58a6AzmWnVgznXyzSLBW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "old_string": "| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |",
  "new_string": "| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "99994606-1fe0-4452-9210-2eb174bcf636",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 31 · 2026-05-13T07:38:48.877Z_

<details><summary>↩ Tool result · `toolu_01RL58a6AzmWnVgznXyzSLBW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "4ad2fad2-9178-46eb-a9fb-4fd0c8f96da2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
    "oldString": "| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |",
    "newString": "| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |",
    "originalFile": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
    "structuredPatch": [
      {
        "oldStart": 141,
        "oldLines": 7,
        "newStart": 141,
        "newLines": 7,
        "lines": [
          " |---|---|---|---|---|---|",
          " | C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |",
          " | C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |",
          "-| C1 | FM3: overcorrection rebound | mvp-004 | overcorrected pol vs baseline | +8.2% (+0.046 abs) | hgate-dpo003-merged (+14.3%, 4/4 runs) |",
          "+| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |",
          " | C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |",
          " | C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |",
          " | C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01CAYHLovkfVXoKDkrMXSEFk`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "old_string": "anonymous2026expert_persona",
  "new_string": "hu2026expert_persona"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "65aa8077-1747-4558-9320-dd436531d48b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 33 · 2026-05-13T07:38:49.818Z_

<details><summary>↩ Tool result · `toolu_01CAYHLovkfVXoKDkrMXSEFk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "c4d11f69-4349-4f98-a5a2-429bf2b8f1a2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
    "oldString": "anonymous2026expert_persona",
    "newString": "hu2026expert_persona",
    "originalFile": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
    "structuredPatch": [
      {
        "oldStart": 55,
        "oldLines": 7,
        "newStart": 55,
        "newLines": 7,
        "lines": [
          " - FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)",
          " ",
          " **External support**:",
          "-- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); anonymous2026expert_persona (accuracy degradation up to 30pp under persona)",
          "+- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)",
          " - FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)",
          " - FM3: no direct external parallel — novel observation",
          " "
        ]
      },
      {
        "oldStart": 90,
        "oldLines": 7,
        "newStart": 90,
        "newLines": 7,
        "lines": [
          " ### C4: Implications for future calibration research",
          " **Evidence strength**: Analytical (grounded in C1-C3)",
          " ",
          "-- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; anonymous2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.",
          "+- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.",
          " - **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).",
          " - **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.",
          " - **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets."
        ]
      },
      {
        "oldStart": 103,
        "oldLines": 7,
        "newStart": 103,
        "newLines": 7,
        "lines": [
          " **Status**: Partially mitigated",
          " - Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence",
          " - Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them",
          "-- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and anonymous2026expert_persona",
          "+- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona",
          " - **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"",
          " ",
          " ### RC2: \"n=20 tasks, high variance — statistical power?\""
        ]
      },
      {
        "oldStart": 163,
        "oldLines": 7,
        "newStart": 163,
        "newLines": 7,
        "lines": [
          " |---|---|---|",
          " | Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |",
          " | FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |",
          "-| FM1 mechanism | anonymous2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |",
          "+| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |",
          " | FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |",
          " | FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |",
          " | Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_016mPiMzH5xPahazyLYuTir5`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "anonymous2026expert_persona",
  "new_string": "hu2026expert_persona"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "6cc69b25-3ba4-44e1-aee0-c670236070c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 35 · 2026-05-13T07:38:50.730Z_

<details><summary>↩ Tool result · `toolu_016mPiMzH5xPahazyLYuTir5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "af61df00-c669-4e29-8dd8-8a966abd2799",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "anonymous2026expert_persona",
    "newString": "hu2026expert_persona",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: anonymous2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +anonymous2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + anonymous2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 429,
        "oldLines": 7,
        "newStart": 429,
        "newLines": 7,
        "lines": [
          "     scan_date: \"2026-05-13\"",
          "     plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"",
          " ",
          "-  - id: anonymous2026expert_persona",
          "+  - id: hu2026expert_persona",
          "     title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"",
          "     authors: \"Hu, Rostami, Thomason\"",
          "     venue: \"arXiv 2603.18507\""
        ]
      },
      {
        "oldStart": 468,
        "oldLines": 7,
        "newStart": 468,
        "newLines": 7,
        "lines": [
          " # Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)",
          " # - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)",
          " # - foundation: 5 (+sim2real2026gap)",
          "-# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +anonymous2026expert_persona)",
          "+# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)",
          " # - evaluation: 6 (+gupta2025endive)",
          " # - background: 6 (+nakash2026divert)",
          " # - high relevance: 14, medium: 13, low: 1"
        ]
      },
      {
        "oldStart": 477,
        "oldLines": 7,
        "newStart": 477,
        "newLines": 7,
        "lines": [
          " # - 4 new papers added specifically for Plan B empirical analysis framing",
          " # - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)",
          " # - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)",
          "-# - basil2025playing_pretend + anonymous2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)",
          "+# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)",
          " # - No direct competitor found for BCP failure mode analysis — novelty gap confirmed",
          " # - Also noted but not added:",
          " #   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_016Px4jXy1B5XFXgakjNoxiS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\"",
  "new_string": "how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "29ea92c8-1013-4eae-b4db-a6ba34680cce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 37 · 2026-05-13T07:38:52.234Z_

<details><summary>↩ Tool result · `toolu_016Px4jXy1B5XFXgakjNoxiS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "fedcd7ed-83ba-4c3d-a8af-a2cf23378c34",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\"",
    "newString": "how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          "       - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"",
          "       - \"Simulated users introduce conversational artifacts absent from real human users\"",
          "       - \"Disparities compound significantly with age for AAVE speakers\"",
          "-    how_we_differ: \"They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps\"",
          "+    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"",
          " ",
          "   - id: yao2024taubench",
          "     title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01MEvCAPq7PLWg35AUGhk4sD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\"",
  "new_string": "how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "84adf862-3ae3-4a38-bd76-b7618f8d3692",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 39 · 2026-05-13T07:38:53.653Z_

<details><summary>↩ Tool result · `toolu_01MEvCAPq7PLWg35AUGhk4sD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "360fc72f-1f84-4d2f-8bf3-075383ebe87c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\"",
    "newString": "how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 38,
        "oldLines": 7,
        "newStart": 38,
        "newLines": 7,
        "lines": [
          "       - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"",
          "       - \"Proposes pass^k metric measuring reliability over multiple trials\"",
          "       - \"User simulator is LLM-based, enabling behavioral modification\"",
          "-    how_we_differ: \"We extend tau-bench by calibrating the user simulator's dialect-specific behavioral rates\"",
          "+    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"",
          " ",
          "   - id: liu2024agentbench",
          "     title: \"AgentBench: Evaluating LLMs as Agents\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_019gCUCvc559eQ9Q6cfUfuN9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"",
  "new_string": "how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "618e3ccd-69eb-470b-b818-1f36008dc103",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 41 · 2026-05-13T07:38:55.052Z_

<details><summary>↩ Tool result · `toolu_019gCUCvc559eQ9Q6cfUfuN9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "e6f41da9-275f-4a3d-a054-8d7a845aa952",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"",
    "newString": "how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 67,
        "oldLines": 7,
        "newStart": 67,
        "newLines": 7,
        "lines": [
          "       - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"",
          "       - \"Better single-turn performance does not guarantee better multi-turn performance\"",
          "       - \"SIFT and RLHF generally hurt multi-turn capabilities\"",
          "-    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we add dialect-aware calibration\"",
          "+    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"",
          " ",
          "   # ============================================================",
          "   # METHOD-COMPONENT"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_019m7pAWphtqB7iytABk5axr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"",
  "new_string": "how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "2a4f5708-bffc-468d-953a-dde040e5597f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 43 · 2026-05-13T07:38:56.006Z_

<details><summary>↩ Tool result · `toolu_019m7pAWphtqB7iytABk5axr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "5ab61cf2-67ea-4598-8ec9-db031e71f479",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"",
    "newString": "how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 7,
        "newStart": 85,
        "newLines": 7,
        "lines": [
          "       - \"DPO directly optimizes policy from preference pairs without explicit reward model\"",
          "       - \"Computationally lightweight, stable alternative to PPO-based RLHF\"",
          "       - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"",
          "-    how_we_differ: \"We apply DPO specifically to align user simulator behavioral rates with target dialect distributions\"",
          "+    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"",
          " ",
          "   - id: zhao2021calibrate",
          "     title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_011JsKstyTR7pjYpRz9YZA7v`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"",
  "new_string": "how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "5b9925e4-7d61-4232-ab5c-795f1d6144c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 45 · 2026-05-13T07:38:57.421Z_

<details><summary>↩ Tool result · `toolu_011JsKstyTR7pjYpRz9YZA7v`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "cbab66f8-4f01-4e80-bcd4-939296e974b5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"",
    "newString": "how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 100,
        "oldLines": 7,
        "newStart": 100,
        "newLines": 7,
        "lines": [
          "       - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"",
          "       - \"Identified majority label bias, recency bias, common token bias\"",
          "       - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"",
          "-    how_we_differ: \"They calibrate classification outputs; we calibrate behavioral rates (question rate, politeness) in generation\"",
          "+    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"",
          " ",
          "   - id: abdulhai2025consistent",
          "     title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_018rYH7bPxGF6ff1MYiiBjqK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"",
  "new_string": "how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "4d9eee9c-db4c-420d-856e-df159a3831a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 47 · 2026-05-13T07:38:58.834Z_

<details><summary>↩ Tool result · `toolu_018rYH7bPxGF6ff1MYiiBjqK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "682b5ca3-b816-455a-a2d6-f006df53544a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"",
    "newString": "how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 115,
        "oldLines": 7,
        "newStart": 115,
        "newLines": 7,
        "lines": [
          "       - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"",
          "       - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"",
          "       - \"Multi-turn RL reduces inconsistency by >55%\"",
          "-    how_we_differ: \"They optimize persona consistency in general; we specifically target dialect behavioral rate calibration\"",
          "+    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"",
          " ",
          "   - id: naous2025flipping",
          "     title: \"Flipping the Dialogue: Training and Evaluating User Language Models\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01SHrx6EK2qmw3TJVRBeT9PZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"",
  "new_string": "how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "26d93f1c-a9aa-4996-9938-0b494ebd7638",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 49 · 2026-05-13T07:38:59.774Z_

<details><summary>↩ Tool result · `toolu_01SHrx6EK2qmw3TJVRBeT9PZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "d7cc675f-48c1-4189-88e8-bb364247de9e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"",
    "newString": "how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 130,
        "oldLines": 7,
        "newStart": 130,
        "newLines": 7,
        "lines": [
          "       - \"Better assistant LMs yield worse user simulators\"",
          "       - \"UserLM-8b provides more realistic user simulation\"",
          "       - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"",
          "-    how_we_differ: \"They train general User LMs; we calibrate user simulator behavioral rates for specific dialect groups\"",
          "+    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"",
          " ",
          "   - id: li2025persona",
          "     title: \"LLM Generated Persona is a Promise with a Catch\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_015MWmXKDyofzDkckXwvhZRN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"",
  "new_string": "how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "ac9480a4-fbf8-4bf4-96e3-412bac39aac4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 51 · 2026-05-13T07:39:01.194Z_

<details><summary>↩ Tool result · `toolu_015MWmXKDyofzDkckXwvhZRN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "38df03e6-2ed2-4b82-b661-d6f5c5df5015",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"",
    "newString": "how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 145,
        "oldLines": 7,
        "newStart": 145,
        "newLines": 7,
        "lines": [
          "       - \"LLM-generated personas systematically drift toward socially desirable traits\"",
          "       - \"More LLM-generated content produces more left-leaning, less representative personas\"",
          "       - \"Bias exists in the persona creation step itself, not just model responses\"",
          "-    how_we_differ: \"We bypass persona generation biases by directly injecting behavioral rate targets via BCP\"",
          "+    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"",
          " ",
          "   - id: wang2024alignment",
          "     title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01DemBz8aD4dDwNVXAqUU2N5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"",
  "new_string": "how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "b87eb410-9417-4272-af33-d1eaa309c5ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 53 · 2026-05-13T07:39:02.604Z_

<details><summary>↩ Tool result · `toolu_01DemBz8aD4dDwNVXAqUU2N5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "f25e66d2-0a07-47ce-ba32-6e2c133c032b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"",
    "newString": "how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 160,
        "oldLines": 7,
        "newStart": 160,
        "newLines": 7,
        "lines": [
          "       - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"",
          "       - \"DPO is stable and lightweight but sensitive to preference data quality\"",
          "       - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"",
          "-    how_we_differ: \"Survey provides methodology reference; we apply DPO to a novel domain (user simulator dialect calibration)\"",
          "+    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"",
          " ",
          "   # ============================================================",
          "   # EVALUATION"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_017aMQVNna17v9Hr3biSfZD8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"",
  "new_string": "how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "47fddaf5-8d5d-4d8a-a18b-dbf0a68ae420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 55 · 2026-05-13T07:39:03.542Z_

<details><summary>↩ Tool result · `toolu_017aMQVNna17v9Hr3biSfZD8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "e755bdeb-1ef3-4934-956e-16a8cb58ab81",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"",
    "newString": "how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 179,
        "oldLines": 7,
        "newStart": 179,
        "newLines": 7,
        "lines": [
          "       - \"Almost all models show statistically significant performance drops on AAVE\"",
          "       - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"",
          "       - \"LLMs struggle more with AAVE than misspelled Standard English\"",
          "-    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate and calibrate behavioral rates in user simulation\"",
          "+    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"",
          " ",
          "   - id: faisal2024dialectbench",
          "     title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01FeWquo49pFRq2vC8Ya1Su8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"",
  "new_string": "how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "b1fad469-ba86-4279-a086-9e72e01b8d81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 57 · 2026-05-13T07:39:04.954Z_

<details><summary>↩ Tool result · `toolu_01FeWquo49pFRq2vC8Ya1Su8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "7edca199-8786-4fd2-b972-bf0889191e75",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"",
    "newString": "how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 194,
        "oldLines": 7,
        "newStart": 194,
        "newLines": 7,
        "lines": [
          "       - \"10 NLP tasks, 281 varieties, 40 language clusters\"",
          "       - \"Substantial performance disparities between standard and non-standard varieties\"",
          "       - \"Performance gap widens with fine-tuning due to uneven data availability\"",
          "-    how_we_differ: \"DialectBench evaluates NLP task performance; we focus on behavioral calibration of user simulators\"",
          "+    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"",
          " ",
          "   - id: gallegos2024bias",
          "     title: \"Bias and Fairness in Large Language Models: A Survey\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ug34qQcVvQkQP2bM8fDgdu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"",
  "new_string": "how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "e16d95d0-f368-44c1-afd3-5c48af9bd8ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 59 · 2026-05-13T07:39:05.900Z_

<details><summary>↩ Tool result · `toolu_01Ug34qQcVvQkQP2bM8fDgdu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "77f388f7-1286-40c8-8a60-05c187c1dfc8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"",
    "newString": "how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 240,
        "oldLines": 7,
        "newStart": 240,
        "newLines": 7,
        "lines": [
          "       - \"AAVE/Singlish users receive less sanitized content than SAE users\"",
          "       - \"Safety alignment is brittle, over-indexed on explicit keywords\"",
          "       - \"24,000+ responses analyzed across two LLMs\"",
          "-    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we propose calibration methods to correct behavioral rates\"",
          "+    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"",
          " ",
          "   # ============================================================",
          "   # BACKGROUND"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_016puSUgMvpmqujfNyj1eKjs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"",
  "new_string": "how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "375baf65-59da-4a3d-8f5b-bfbe485fe88a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 61 · 2026-05-13T07:39:07.782Z_

<details><summary>↩ Tool result · `toolu_016puSUgMvpmqujfNyj1eKjs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "f43b1460-41ba-49f8-a7e6-8e6cee1a7071",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"",
    "newString": "how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 339,
        "oldLines": 7,
        "newStart": 339,
        "newLines": 7,
        "lines": [
          "       - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"",
          "       - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"",
          "       - \"Higher model capability does not yield more faithful user simulation\"",
          "-    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"",
          "+    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"",
          "     scan_date: \"2026-05-13\"",
          "     note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01SSevcesapaSnpkbGMKLwev`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"",
  "new_string": "how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "cfa49a63-f8f6-42ad-ab05-f81ee0a557f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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
