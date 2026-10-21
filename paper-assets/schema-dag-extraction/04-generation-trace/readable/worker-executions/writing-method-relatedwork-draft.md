# writing method relatedwork draft

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_writing_method-relatedwork-draft_20260515T035316.log`
- **Structured JSON:** [`4e2ac159da5d52cc4250.json`](../../sessions/4e/4e2ac159da5d52cc4250.json)

## Before a recorded user message

34 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
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
  "uuid": "8fbd8ae9-54be-424d-8a32-4ee6297e6949",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1778817600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "19e66eaa-59f2-4538-9394-5f4b661798b8",
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9"
}
```

---

### Assistant

_source line 4_

I'll start by reading the necessary source files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "84ba04ed-4de8-4fba-b582-ad5498492d77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbmTQsDVpUfpf73FzrRY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11607,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11607
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016rxpso8fUhoU8BXRip4A34`</summary>

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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "8d95101d-9ad9-4995-90c9-f2eee493b6f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbmTQsDVpUfpf73FzrRY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11607,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11607
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

_source line 6 · 2026-05-15T03:53:29.088Z_

<details><summary>↩ Tool result · `toolu_016rxpso8fUhoU8BXRip4A34`</summary>

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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "93524832-3945-4529-964a-428b8d93c1e4",
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
Now let me read all the source files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "e7e4fe64-a948-4c09-ae01-267e36a57910",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sdSpiomy3ofQ7o7NipWYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 23448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1324
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NAxj8hsCtSPL891ZALn9hB`</summary>

```json
{
  "project": "schema-dag-extraction",
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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "12e415c9-36fb-4c0e-84d1-de245952f04e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sdSpiomy3ofQ7o7NipWYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 23448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1324
      },
      "output_tokens": 19,
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

_source line 9 · 2026-05-15T03:53:37.336Z_

<details><summary>↩ Tool result · `toolu_01NAxj8hsCtSPL891ZALn9hB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (3 conditions)\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion (precision decline via mislabeling). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\\n\\n## Story Spine\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.\\n\\n- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.\\n\\n- **Headline result template**: \\\"Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost.\\\"\\n\\n## Core Insight (Narrative A -- Multi-Channel Degradation)\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Correlated with pairwise type similarity. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal (partial correlation significant after controlling for count) and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024) methodology.\\n- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.\\n- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.\\n- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | Add >=1 more model | exp-012 |\\n| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |\\n| No practical method | SDGD framework | exp-008 to exp-011 |\\n| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |\\n| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |\\n| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |\\n| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 5604, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "12313958-ce9e-4b04-8cb7-f3e13903276f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — schema-dag-extraction\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\\\n- Commitment deadline: August 2, 2026\\\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\\\n- Deadline: ARR May 25, 2026 (10 days from today)\\\\n\\\\n## Core Claims (3 conditions)\\\\n\\\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.\\\\n\\\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion (precision decline via mislabeling). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\\\n\\\\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\\\n\\\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.\\\\n\\\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.\\\\n\\\\n- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.\\\\n\\\\n- **Headline result template**: \\\\\\\"Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost.\\\\\\\"\\\\n\\\\n## Core Insight (Narrative A -- Multi-Channel Degradation)\\\\n\\\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\\\n- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Correlated with pairwise type similarity. Addressable by separating confusable types into different batches.\\\\n\\\\nThese channels are orthogonal (partial correlation significant after controlling for count) and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **\\\\\\\"Just an empirical study\\\\\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\\\\\"Lost in the Middle\\\\\\\" (TACL 2024) methodology.\\\\n- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.\\\\n- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.\\\\n- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response Strategy | Experiment |\\\\n|---------|------------------|------------|\\\\n| Only one model | Add >=1 more model | exp-012 |\\\\n| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |\\\\n| No practical method | SDGD framework | exp-008 to exp-011 |\\\\n| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |\\\\n| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |\\\\n| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |\\\\n| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |\\\\n\\\", \\\"total_chars\\\": 5604, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (3 conditions)\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion (precision decline via mislabeling). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\\n\\n## Story Spine\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.\\n\\n- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.\\n\\n- **Headline result template**: \\\"Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost.\\\"\\n\\n## Core Insight (Narrative A -- Multi-Channel Degradation)\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Correlated with pairwise type similarity. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal (partial correlation significant after controlling for count) and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024) methodology.\\n- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.\\n- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.\\n- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | Add >=1 more model | exp-012 |\\n| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |\\n| No practical method | SDGD framework | exp-008 to exp-011 |\\n| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |\\n| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |\\n| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |\\n| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 5604, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MpruDFiBm6abomRGcd1Zgm`</summary>

```json
{
  "project": "schema-dag-extraction",
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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "6f51d2d6-7b29-4fd3-8a93-52e66594061c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sdSpiomy3ofQ7o7NipWYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 23448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1324
      },
      "output_tokens": 19,
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

_source line 11 · 2026-05-15T03:53:37.598Z_

<details><summary>↩ Tool result · `toolu_01MpruDFiBm6abomRGcd1Zgm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large Language Models\\\"\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\n  role: background\\n  relevance_note: >\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\n\\n# =============================================================================\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\n# =============================================================================\\n#\\n# 1. \\\"Type count vs type confusability\\\" disentangling:\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\n#\\n# 2. Schema decomposition baselines to compare:\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\n#    - DEE (task-level decomposition) — discuss in related work\\n#    - SPT (schema as tools) — discuss in related work\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\n#\\n# 3. \\\"Lost in the Middle\\\" for IE:\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\n#    We can be first to connect positional bias to schema prompt design.\\n#\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\n#\\n# 5. Overall novelty position:\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\n\", \"total_chars\": 13967, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "ed7c56c0-5eb8-44ce-a522-b7d5e79e320d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for schema-dag-extraction\\\\n# Updated: 2026-05-15\\\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\\\n\\\\n# =============================================================================\\\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\\\n# =============================================================================\\\\n\\\\n- id: llm-pee-2025\\\\n  title: \\\\\\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2503.02628\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\\\n    Divides candidate types into partitions to reduce prompt length.\\\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\\\n\\\\n- id: parse-2025\\\\n  title: \\\\\\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\\\\\"\\\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Industry\\\\n  url: https://arxiv.org/abs/2510.08623\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\\\n    Does NOT model type confusability explicitly.\\\\n\\\\n- id: dee-2024\\\\n  title: \\\\\\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\\\\\"\\\\n  year: 2024\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2406.01045\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Decomposes event extraction into detection + argument extraction.\\\\n    Dynamic schema-aware RAG for augmented prompts.\\\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\\\n\\\\n- id: crossagentie-2025\\\\n  title: \\\\\\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\\\\\"\\\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.718/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\\\n    Must clearly differentiate in paper.\\\\n\\\\n- id: dlisc-2025\\\\n  title: \\\\\\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (May 2025)\\\\n  url: https://arxiv.org/abs/2505.14992\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Dual-LoRA with Incremental Schema Caching.\\\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\\\n\\\\n- id: spt-2025\\\\n  title: \\\\\\\"Schema as Parameterized Tools for Universal Information Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (June 2025)\\\\n  url: https://arxiv.org/abs/2506.01276\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Treats schemas as parameterized tools for LLM tool-calling.\\\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\\\n    Does not address type confusability.\\\\n\\\\n- id: zeroner-2025\\\\n  title: \\\\\\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\\\\\"\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.805/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Description-driven: LLM supervision → BERT student for unseen types.\\\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\\\n    Related to how schema semantics affect extraction quality.\\\\n\\\\n- id: cmas-ner-2025\\\\n  title: \\\\\\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: TheWebConf 2025\\\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent collective intelligence for zero-shot NER.\\\\n    Addresses context correlation and indiscriminate demonstration problems.\\\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\\\n\\\\n# =============================================================================\\\\n# METHOD COMPONENTS — techniques we build upon or relate to\\\\n# =============================================================================\\\\n\\\\n- id: uniner-2024\\\\n  title: \\\\\\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\\\\\"\\\\n  authors: [Wenxuan Zhou et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://arxiv.org/abs/2308.03279\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\\\n    Important baseline for universal NER and schema-at-scale challenges.\\\\n\\\\n- id: gollie-2024\\\\n  title: \\\\\\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\\\\\"\\\\n  authors: [Oscar Sainz et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Code-style schema definitions + annotation guideline following.\\\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\\\n    Baseline for guideline-driven schema representation.\\\\n\\\\n- id: gliner-2024\\\\n  title: \\\\\\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08526\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\\\n\\\\n- id: gliner2-2025\\\\n  title: \\\\\\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Demo\\\\n  url: https://arxiv.org/abs/2507.18546\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\\\n\\\\n- id: kggen-2025\\\\n  title: \\\\\\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\\\\\"\\\\n  authors: [Mo et al.]\\\\n  year: 2025\\\\n  venue: NeurIPS 2025\\\\n  url: https://arxiv.org/abs/2502.09956\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Two-stage decomposition: entities first, then relations.\\\\n    Entity clustering/deduplication to reduce graph sparsity.\\\\n    Schema decomposition approach for KG construction.\\\\n\\\\n- id: code4uie-2024\\\\n  title: \\\\\\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\\\\\"\\\\n  authors: [Yucan Guo et al.]\\\\n  year: 2024\\\\n  venue: NeurIPS 2024 Workshop\\\\n  url: https://arxiv.org/abs/2311.02962\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Python class-based schema definitions + RAG for code generation.\\\\n    Unified code-style schema for all IE tasks.\\\\n\\\\n- id: iepile-2024\\\\n  title: \\\\\\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\\\\\"\\\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2402.14710\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\\\n    semantically proximate schemas to train type discrimination.\\\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\\\n\\\\n- id: lost-in-middle-2024\\\\n  title: \\\\\\\"Lost in the Middle: How Language Models Use Long Contexts\\\\\\\"\\\\n  authors: [Nelson F. Liu et al.]\\\\n  year: 2024\\\\n  venue: TACL 2024\\\\n  url: https://arxiv.org/abs/2307.03172\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\\\n    Motivates schema decomposition to reduce prompt length.\\\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\\\n\\\\n# =============================================================================\\\\n# ZERO-SHOT NER / RE BASELINES\\\\n# =============================================================================\\\\n\\\\n- id: self-improve-ner-2024\\\\n  title: \\\\\\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\\\\\"\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08921\\\\n  role: background\\\\n  relevance_note: >\\\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\\\n\\\\n- id: self-prompting-re-2024\\\\n  title: \\\\\\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\\\\\"\\\\n  year: 2024\\\\n  venue: EMNLP 2024 Findings\\\\n  url: https://arxiv.org/abs/2410.01154\\\\n  role: background\\\\n  relevance_note: >\\\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\\\n    Training-free RE baseline.\\\\n\\\\n- id: reasoning-ner-2025\\\\n  title: \\\\\\\"A Reasoning Paradigm for Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (Nov 2025)\\\\n  url: https://arxiv.org/abs/2511.11978\\\\n  role: background\\\\n  relevance_note: >\\\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\\\n\\\\n- id: nuner-2024\\\\n  title: \\\\\\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\\\\\"\\\\n  authors: [Sergei Bogdanov et al., NuMind]\\\\n  year: 2024\\\\n  venue: EMNLP 2024\\\\n  url: https://arxiv.org/abs/2402.15343\\\\n  role: background\\\\n  relevance_note: >\\\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\\\n\\\\n# =============================================================================\\\\n# EVALUATION / BENCHMARKING\\\\n# =============================================================================\\\\n\\\\n- id: familiarity-2025\\\\n  title: \\\\\\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\\\\\"\\\\n  year: 2025\\\\n  venue: NAACL 2025\\\\n  url: https://arxiv.org/abs/2412.10121\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    \\\\\\\"Familiarity\\\\\\\" metric for label shift in synthetic NER data.\\\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\\\n    Quantifies semantic similarity between entity types — related to type confusability.\\\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\\\n\\\\n- id: guidex-2025\\\\n  title: \\\\\\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\\\\\"\\\\n  authors: [Neil Deshpande et al.]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://arxiv.org/abs/2506.00649\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\\\n\\\\n# =============================================================================\\\\n# SURVEYS\\\\n# =============================================================================\\\\n\\\\n- id: llm4ie-survey-2024\\\\n  title: \\\\\\\"Large Language Models for Generative Information Extraction: A Survey\\\\\\\"\\\\n  authors: [Derong Xu et al.]\\\\n  year: 2024\\\\n  venue: Frontiers of Computer Science\\\\n  url: https://arxiv.org/abs/2312.17617\\\\n  role: background\\\\n  relevance_note: >\\\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\\\n\\\\n- id: knowcoder-2024\\\\n  title: \\\\\\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\\\\\"\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2403.07969\\\\n  role: background\\\\n  relevance_note: >\\\\n    Encodes schema knowledge via code structures into LLM.\\\\n    Related to code-based schema representation.\\\\n\\\\n- id: slot-2025\\\\n  title: \\\\\\\"SLOT: Structuring the Output of Large Language Models\\\\\\\"\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Industry\\\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\\\n  role: background\\\\n  relevance_note: >\\\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\\\n\\\\n# =============================================================================\\\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\\\n# =============================================================================\\\\n#\\\\n# 1. \\\\\\\"Type count vs type confusability\\\\\\\" disentangling:\\\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\\\n#\\\\n# 2. Schema decomposition baselines to compare:\\\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\\\n#    - DEE (task-level decomposition) — discuss in related work\\\\n#    - SPT (schema as tools) — discuss in related work\\\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\\\n#\\\\n# 3. \\\\\\\"Lost in the Middle\\\\\\\" for IE:\\\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\\\n#    We can be first to connect positional bias to schema prompt design.\\\\n#\\\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\\\n#\\\\n# 5. Overall novelty position:\\\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\\\n\\\", \\\"total_chars\\\": 13967, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large Language Models\\\"\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\n  role: background\\n  relevance_note: >\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\n\\n# =============================================================================\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\n# =============================================================================\\n#\\n# 1. \\\"Type count vs type confusability\\\" disentangling:\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\n#\\n# 2. Schema decomposition baselines to compare:\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\n#    - DEE (task-level decomposition) — discuss in related work\\n#    - SPT (schema as tools) — discuss in related work\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\n#\\n# 3. \\\"Lost in the Middle\\\" for IE:\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\n#    We can be first to connect positional bias to schema prompt design.\\n#\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\n#\\n# 5. Overall novelty position:\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\n\", \"total_chars\": 13967, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_018fkkKAE781wyEK7QHM6VMA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/sdgd_design_doc.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "8467084a-5593-4c45-bfa3-cd8c830feffd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sdSpiomy3ofQ7o7NipWYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 23448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1324
      },
      "output_tokens": 19,
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

_source line 13 · 2026-05-15T03:53:37.819Z_

<details><summary>↩ Tool result · `toolu_018fkkKAE781wyEK7QHM6VMA`</summary>

````text
1	# SDGD Framework — Algorithm Design & Code Skeleton
2	
3	## 1. Algorithm Flow
4	
5	### Input
6	- `types: Dict[str, str]` — type name → description (e.g., `configs/few_nerd_types.json`, 66 entries)
7	- `embeddings: Tensor[N, D]` — type embeddings from Qwen3-32B mean-pool (N=66, D=5120), loaded from `artifacts/type_embeddings.pt`
8	- `τ: float` — confusability threshold (from Contribution A: θ* where degradation becomes significant)
9	- `model: LLM` — vLLM engine (Qwen3-32B-FP8)
10	- `samples: List[Dict]` — test samples with `text` field
11	- `confusion_matrix: Optional[Tensor[N, N]]` — empirical confusion counts from calibration (SDGD-cal only)
12	
13	### Output
14	- `predictions: List[Dict]` — merged predictions across all batches, format: `[{"sample_id": int, "predictions": [{"text": str, "type": str}]}]`
15	
16	### Pseudocode
17	
18	```
19	function SDGD(types, embeddings, τ, model, samples, confusion_matrix=None):
20	    # Step 1: Pairwise confusability matrix
21	    if confusion_matrix is not None:                      # SDGD-cal
22	        C = normalize_confusion(confusion_matrix)         # symmetric, [0,1]
23	    else:                                                 # SDGD-zero
24	        C = cosine_similarity(embeddings, embeddings)     # [N, N]
25	
26	    # Step 2: Thresholded adjacency graph
27	    A = (C > τ) & ~eye(N)                                # binary adjacency
28	    G = Graph(nodes=types.keys(), edges=A.nonzero())
29	
30	    # Step 3: Greedy graph coloring → type batches
31	    coloring = greedy_color(G, strategy="largest_first")  # {type: color_id}
32	    batches = group_by_color(coloring)                    # {color_id: [type_names]}
33	
34	    # Step 4: Per-batch extraction
35	    all_predictions = []
36	    for batch_id, batch_types in batches.items():
37	        prompts = [build_prompt(s["text"], types, batch_types) for s in samples]
38	        schema = build_json_schema(batch_types)
39	        outputs = model.generate(prompts, guided_decoding=schema)
40	        preds = parse_outputs(outputs, batch_id, batch_types)
41	        all_predictions.append(preds)
42	
43	    # Step 5: Merge across batches
44	    merged = merge_predictions(all_predictions)
45	    return merged
46	```
47	
48	## 2. Key Design Decisions
49	
50	### 2.1 SDGD-zero vs SDGD-cal
51	
52	| | SDGD-zero | SDGD-cal |
53	|---|---|---|
54	| Confusability source | Embedding cosine similarity | Empirical confusion matrix from k calibration examples |
55	| Data requirement | None (zero-shot) | 5-10 labeled examples per type |
56	| Quality | Proxy — embedding similarity ≈ semantic confusability | Ground truth — measures actual model confusion |
57	| Cost | Free (embeddings precomputed) | k × N_types extraction calls for calibration |
58	| When to use | No labeled data; rapid schema adaptation | Labeled data available; maximum accuracy |
59	
60	**Calibration procedure (SDGD-cal)**:
61	```
62	function compute_empirical_confusion(types, model, calibration_samples):
63	    # Run single-pass extraction with ALL types on calibration set
64	    preds = extract(model, calibration_samples, all_types=types)
65	    
66	    # Build confusion matrix: C[i,j] = count of gold type-i predicted as type-j
67	    C = zeros(N, N)
68	    for sample in calibration_samples:
69	        for gold_entity in sample.entities:
70	            matched_pred = find_best_match(gold_entity, preds[sample.id])
71	            if matched_pred:
72	                i = type_index[gold_entity.type]
73	                j = type_index[matched_pred.type]
74	                C[i, j] += 1
75	    
76	    # Symmetrize and normalize
77	    C_sym = (C + C.T) / 2
78	    row_sums = C_sym.sum(dim=1, keepdim=True).clamp(min=1)
79	    return C_sym / row_sums
80	```
81	
82	### 2.2 Threshold τ Selection
83	
84	**Primary method: Adaptive threshold（数据集无关）**
85	
86	`τ = mean(C_upper_tri) + k · std(C_upper_tri)`，k 是唯一超参数。
87	
88	- 自适应于不同 schema 的 embedding 分布，避免循环性问题（不从目标数据集推导阈值）
89	- Few-NERD Qwen3 embeddings: mean=0.7837, std=0.0653 → k=1.0 时 τ ≈ 0.85
90	- 默认 k=1.0，通过 k sweep 消融确定最优值
91	
92	**Oracle threshold baseline（上界对比用）**:
93	- 从 Few-NERD BCS-quality curve 推导的固定 τ∈[0.82, 0.88]
94	- 仅用于 Few-NERD 上的上界对比实验，**不可用于跨域验证**（exp-009 等）
95	- 论文中明确标注为 "oracle" 以区分
96	
97	**跨域验证要求**:
98	- exp-009（ACE05/MAVEN）等跨域实验 **必须** 使用 adaptive threshold
99	- 不同数据集的 embedding 分布不同，固定 τ 无意义
100	
101	**消融计划**: k sweep {0.5, 1.0, 1.5, 2.0}，在 adaptive framework 内做。报告每个 k 下的：τ 值、batch 数量、F1、vs single-pass Δ。
102	
103	### 2.3 Graph Coloring Algorithm
104	
105	**选择: Greedy (largest_first)**
106	
107	理由：
108	- IE schema 图很小（Few-NERD 66 nodes, ACE05 58 nodes, 最大 MAVEN 168 nodes）
109	- Greedy coloring 时间复杂度 O(V²)，对 168 nodes 微秒级
110	- Optimal coloring 是 NP-hard，但 greedy 在稀疏图（τ 控制密度）上接近最优
111	- NetworkX `greedy_color` 直接可用，strategy="largest_first" 优先处理高度节点
112	
113	**Batch 数量预估** (Few-NERD, τ=0.85):
114	- 同 coarse category 内 subtypes 基本都 > 0.85（如 person-* 8 个 subtypes 互相 BCS > 0.88）
115	- 预计 chromatic number ≈ 8-10（≈ max clique size in thresholded graph）
116	- 对比 single-pass (1 batch, 66 types) 和 per-type (66 batches)
117	
118	### 2.4 Merge Strategy
119	
120	**Primary: Simple union**（适用于 NER）
121	```
122	function merge_predictions(batch_predictions):
123	    merged = defaultdict(list)
124	    for batch_preds in batch_predictions:
125	        for pred in batch_preds:
126	            merged[pred.sample_id].extend(pred.predictions)
127	    return merged
128	```
129	
130	NER batch 之间 type 集合不重叠（graph coloring 保证），所以不存在同一 span 被不同 batch 提取为不同 type 的冲突。唯一可能的重复：同一 span 被提取为同一 type（hallucination）。
131	
132	**Conflict resolution（RE/EE 跨层时需要）**:
133	- 同一 (text, type) pair 出现在多个 batch → deduplicate
134	- 同一 span 不同 type → 保留 confidence 最高的（如果 model 提供 logprob）或保留全部（交给 evaluator）
135	
136	当前 NER-only 阶段用 simple union 即可。
137	
138	## 3. Module Structure
139	
140	```
141	src/sdgd/
142	  __init__.py           # Public API: sdgd_extract()
143	  similarity.py         # Pairwise confusability computation
144	  graph.py              # Threshold graph construction + coloring
145	  decompose.py          # Main decomposition orchestrator
146	  merge.py              # Result merging across batches
147	  evaluate.py           # SDGD-specific evaluation & comparison
148	```
149	
150	### 3.1 `similarity.py`
151	
152	```python
153	"""Pairwise confusability matrix computation."""
154	import torch
155	import torch.nn.functional as F
156	from typing import Dict, Optional, Tuple, List
157	
158	def load_type_embeddings(path: str) -> Tuple[torch.Tensor, List[str]]:
159	    """Load precomputed type embeddings.
160	    
161	    Returns:
162	        embeddings: [N, D] tensor (N=66, D=5120 for Qwen3)
163	        type_names: ordered list of type names matching embedding rows
164	    """
165	    ...
166	
167	def cosine_similarity_matrix(embeddings: torch.Tensor) -> torch.Tensor:
168	    """Compute pairwise cosine similarity. Returns [N, N] matrix in [0, 1]."""
169	    normed = F.normalize(embeddings, dim=1)
170	    return normed @ normed.T
171	
172	def normalize_confusion_matrix(C: torch.Tensor) -> torch.Tensor:
173	    """Symmetrize and normalize raw confusion counts to [0, 1].
174	    
175	    C[i,j] = count of gold type-i predicted as type-j.
176	    Output: symmetric matrix, diagonal zeroed, max-normalized.
177	    """
178	    ...
179	
180	def compute_confusability(
181	    embeddings: torch.Tensor,
182	    confusion_matrix: Optional[torch.Tensor] = None,
183	) -> torch.Tensor:
184	    """Unified confusability computation.
185	    
186	    SDGD-zero: uses embedding cosine similarity.
187	    SDGD-cal: uses normalized empirical confusion matrix.
188	    """
189	    if confusion_matrix is not None:
190	        return normalize_confusion_matrix(confusion_matrix)
191	    return cosine_similarity_matrix(embeddings)
192	```
193	
194	### 3.2 `graph.py`
195	
196	```python
197	"""Confusability graph construction and coloring."""
198	import networkx as nx
199	import torch
200	from typing import Dict, List, Tuple
201	
202	def build_confusability_graph(
203	    conf_matrix: torch.Tensor,
204	    type_names: List[str],
205	    threshold: float,
206	) -> nx.Graph:
207	    """Build thresholded undirected graph.
208	    
209	    Edge (i, j) exists iff conf_matrix[i, j] > threshold and i != j.
210	    Edge weight = conf_matrix[i, j].
211	    """
212	    ...
213	
214	def color_graph(
215	    G: nx.Graph,
216	    strategy: str = "largest_first",
217	) -> Dict[str, int]:
218	    """Greedy graph coloring. Returns {type_name: color_id}."""
219	    return nx.coloring.greedy_color(G, strategy=strategy)
220	
221	def coloring_to_batches(coloring: Dict[str, int]) -> Dict[int, List[str]]:
222	    """Convert coloring assignment to batch groups. Returns {batch_id: [type_names]}."""
223	    batches = {}
224	    for type_name, color_id in coloring.items():
225	        batches.setdefault(color_id, []).append(type_name)
226	    return batches
227	
228	def compute_batch_bcs(
229	    batches: Dict[int, List[str]],
230	    conf_matrix: torch.Tensor,
231	    type_names: List[str],
232	) -> Dict[int, float]:
233	    """Compute BCS (max pairwise confusability) for each batch."""
234	    ...
235	
236	def graph_stats(G: nx.Graph, batches: Dict[int, List[str]]) -> Dict:
237	    """Summary stats: num_batches, avg_batch_size, max_bcs, edge_density."""
238	    ...
239	```
240	
241	### 3.3 `decompose.py`
242	
243	```python
244	"""Main SDGD decomposition orchestrator."""
245	from typing import Dict, List, Optional
246	from .similarity import load_type_embeddings, compute_confusability
247	from .graph import build_confusability_graph, color_graph, coloring_to_batches
248	
249	class SDGDDecomposer:
250	    def __init__(
251	        self,
252	        type_definitions: Dict[str, str],
253	        embedding_path: str,
254	        threshold: float,
255	        confusion_matrix: Optional[torch.Tensor] = None,
256	    ):
257	        self.type_definitions = type_definitions
258	        self.embeddings, self.type_names = load_type_embeddings(embedding_path)
259	        self.threshold = threshold
260	        self.conf_matrix = compute_confusability(
261	            self.embeddings, confusion_matrix
262	        )
263	        self._build_batches()
264	
265	    def _build_batches(self):
266	        """Construct confusability graph and compute coloring."""
267	        self.graph = build_confusability_graph(
268	            self.conf_matrix, self.type_names, self.threshold
269	        )
270	        coloring = color_graph(self.graph)
271	        self.batches = coloring_to_batches(coloring)
272	
273	    @property
274	    def num_batches(self) -> int:
275	        return len(self.batches)
276	
277	    def get_batch_types(self, batch_id: int) -> List[str]:
278	        return self.batches[batch_id]
279	
280	    def get_batch_definitions(self, batch_id: int) -> Dict[str, str]:
281	        """Return {type_name: description} for a batch, ready for prompt construction."""
282	        return {t: self.type_definitions[t] for t in self.batches[batch_id]}
283	```
284	
285	**Integration with existing `run_extraction.py`**:
286	
287	```python
288	# In the extraction loop — replaces fixed batch composition
289	from sdgd.decompose import SDGDDecomposer
290	
291	decomposer = SDGDDecomposer(
292	    type_definitions=load_json("configs/few_nerd_types.json"),
293	    embedding_path="artifacts/type_embeddings.pt",
294	    threshold=0.85,
295	)
296	
297	all_predictions = []
298	for batch_id in range(decomposer.num_batches):
299	    batch_types = decomposer.get_batch_types(batch_id)
300	    batch_schema = build_json_schema(batch_types)       # existing function
301	    prompts = [build_prompt(s["text"], type_definitions, batch_types) 
302	               for s in samples]                         # existing function
303	    outputs = llm.generate(prompts, SamplingParams(
304	        max_tokens=1024, temperature=0.0,
305	        guided_decoding=GuidedDecodingParams(json=batch_schema),
306	    ))
307	    preds = parse_outputs(outputs, batch_id, batch_types) # existing function
308	    all_predictions.extend(preds)
309	
310	merged = merge_predictions(all_predictions)               # new: sdgd.merge
311	```
312	
313	### 3.4 `merge.py`
314	
315	```python
316	"""Result merging across batches."""
317	from collections import defaultdict
318	from typing import Dict, List
319	
320	def merge_predictions(
321	    batch_predictions: List[List[Dict]],
322	    strategy: str = "union",
323	) -> List[Dict]:
324	    """Merge predictions from multiple batches.
325	    
326	    Strategies:
327	      - "union": simple concatenation (NER, types don't overlap across batches)
328	      - "dedup": union + remove exact (text, type) duplicates per sample
329	    
330	    Input format per batch: [{"sample_id": int, "predictions": [{"text": str, "type": str}]}]
331	    Output: same format, one entry per sample_id with all predictions merged.
332	    """
333	    merged = defaultdict(list)
334	    for batch_preds in batch_predictions:
335	        for entry in batch_preds:
336	            merged[entry["sample_id"]].extend(entry["predictions"])
337	
338	    if strategy == "dedup":
339	        for sid in merged:
340	            seen = set()
341	            deduped = []
342	            for p in merged[sid]:
343	                key = (p["text"], p["type"])
344	                if key not in seen:
345	                    seen.add(key)
346	                    deduped.append(p)
347	            merged[sid] = deduped
348	
349	    return [{"sample_id": sid, "predictions": preds} 
350	            for sid, preds in sorted(merged.items())]
351	```
352	
353	### 3.5 `evaluate.py`
354	
355	```python
356	"""SDGD-specific evaluation and comparison."""
357	from typing import Dict, List, Tuple
358	
359	def evaluate_sdgd(
360	    predictions: List[Dict],
361	    samples: List[Dict],
362	    batches: Dict[int, List[str]],
363	) -> Dict:
364	    """Evaluate SDGD extraction using text_match_eval.
365	    
366	    Returns:
367	      - overall: micro P/R/F1 across all types
368	      - per_batch: P/R/F1 per batch (with BCS annotation)
369	      - per_type: P/R/F1 per type
370	    """
371	    # Reuses text_match_eval from src/text_match_reeval.py
372	    ...
373	
374	def compare_methods(
375	    results: Dict[str, Dict],
376	    method_names: List[str] = None,
377	) -> Dict:
378	    """Compare SDGD against baselines.
379	    
380	    Expected keys in results:
381	      - "single_pass": all 66 types in one batch
382	      - "per_type": 66 separate calls (UniNER-style)
383	      - "random_k": random batching, same k as SDGD
384	      - "sdgd_zero": SDGD with embedding similarity
385	      - "sdgd_cal": SDGD with empirical confusion matrix
386	    
387	    Returns: comparison table with F1, API calls, latency.
388	    """
389	    ...
390	
391	def compute_api_cost(
392	    num_batches: int,
393	    num_samples: int,
394	    avg_prompt_tokens: int,
395	    avg_completion_tokens: int,
396	) -> Dict:
397	    """Estimate API cost / vLLM throughput for different methods."""
398	    ...
399	```
400	
401	## 4. Interfaces with Existing Code
402	
403	### 4.1 Prompt Construction (from `run_extraction.py`)
404	
405	SDGD 不修改 prompt 构建逻辑，只控制传入的 `type_subset` 参数：
406	
407	```python
408	# Existing interface — unchanged
409	build_prompt(input_text: str, type_definitions: Dict[str, str], type_subset: List[str]) -> str
410	build_json_schema(batch_types: List[str]) -> dict
411	```
412	
413	SDGD 通过 `decomposer.get_batch_types(batch_id)` 提供 `type_subset`。
414	
415	### 4.2 vLLM Inference (from `run_extraction.py`)
416	
417	复用现有 vLLM 初始化和调用逻辑。SDGD 只是在外层循环 batch：
418	
419	```python
420	# Existing: single batch, all types
421	outputs = llm.generate(prompts, sampling_params)
422	
423	# SDGD: loop over batches, each with subset types + constrained schema
424	for batch_id in range(decomposer.num_batches):
425	    batch_schema = build_json_schema(decomposer.get_batch_types(batch_id))
426	    outputs = llm.generate(prompts, SamplingParams(..., guided_decoding=GuidedDecodingParams(json=batch_schema)))
427	```
428	
429	关键：vLLM engine 只初始化一次，batch 间复用。每个 batch 的 JSON schema 不同（type enum 不同）。
430	
431	### 4.3 Evaluation (from `text_match_reeval.py`)
432	
433	```python
434	# Existing interface
435	text_match_eval(pred_entries, samples, batch_types) -> (prf_dict, per_type_dict)
436	```
437	
438	SDGD evaluate 调用方式：
439	- **Per-batch evaluation**: 每个 SDGD batch 独立调用 `text_match_eval`，得到 per-batch metrics（可与 BCS 做相关分析）
440	- **Overall evaluation**: merge 后对全部 types 调用一次 `text_match_eval`，得到 SDGD 总体 F1
441	
442	### 4.4 Type Embeddings
443	
444	```
445	/root/schema-dag-extraction/artifacts/type_embeddings.pt
446	```
447	- Format: `{"embeddings": Tensor[66, 5120], "type_names": List[str]}`（需确认实际格式）
448	- Qwen3-32B mean-pooled last hidden states
449	- 已验证：BCS range 0.5309, mean=0.7837, std=0.0653
450	
451	## 5. Baseline Methods for Comparison
452	
453	| Method | Batches | Types/Batch | BCS Control | API Calls |
454	|--------|---------|-------------|-------------|-----------|
455	| Single-pass | 1 | 66 | None (max BCS) | N |
456	| Per-type (UniNER) | 66 | 1 | 0 (trivially) | 66N |
457	| Random-k | k (= SDGD's k) | ~66/k | Random | kN |
458	| SDGD-zero | k (from coloring) | Variable | ≤ τ | kN |
459	| SDGD-cal | k' (from coloring) | Variable | ≤ τ | k'N + calibration |
460	
461	Random-k 是关键消融——与 SDGD 相同 batch 数量但随机分组。F1 差异直接量化 confusability-aware grouping 的价值。
462	
463	## 6. Implementation Notes
464	
465	1. **Graph coloring 确定性**: `nx.greedy_color` 受节点遍历顺序影响。固定 `type_names` 排序以保证可复现。
466	
467	2. **Threshold sensitivity**: τ 轻微变化可能改变 batch 数量（图密度突变）。评估时报告 τ vs num_batches 曲线。
468	
469	3. **vLLM batch 效率**: 每个 SDGD batch 对全部 1000 samples 做推理。总推理次数 = k × 1000。对比 per-type 的 66 × 1000 = 66k 次。SDGD 如果 k ≈ 10，则 10k 次，6.6x speedup over per-type。
470	
471	4. **Prompt v2**: SDGD 必须使用 exp003a 的 prompt v2（text-only, anti-hallucination instruction），不要用 v1（含 char offset 要求）。
472	
473	5. **Empty batch handling**: 某些 batch 可能只包含低频 type（测试集中无 gold entity）。仍需执行推理（可能提取到 entity），但评估时 gold=0 的 batch 不参与 F1 计算。
474	
475	6. **Dependency on exp003a**: 实际代码编写等 exp003a 完成确认数据干净后再开始。当前 document 为设计阶段。
476	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "3b68905f-53b3-4245-a9d1-dcddd21643bf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/sdgd_design_doc.md",
      "content": "# SDGD Framework — Algorithm Design & Code Skeleton\n\n## 1. Algorithm Flow\n\n### Input\n- `types: Dict[str, str]` — type name → description (e.g., `configs/few_nerd_types.json`, 66 entries)\n- `embeddings: Tensor[N, D]` — type embeddings from Qwen3-32B mean-pool (N=66, D=5120), loaded from `artifacts/type_embeddings.pt`\n- `τ: float` — confusability threshold (from Contribution A: θ* where degradation becomes significant)\n- `model: LLM` — vLLM engine (Qwen3-32B-FP8)\n- `samples: List[Dict]` — test samples with `text` field\n- `confusion_matrix: Optional[Tensor[N, N]]` — empirical confusion counts from calibration (SDGD-cal only)\n\n### Output\n- `predictions: List[Dict]` — merged predictions across all batches, format: `[{\"sample_id\": int, \"predictions\": [{\"text\": str, \"type\": str}]}]`\n\n### Pseudocode\n\n```\nfunction SDGD(types, embeddings, τ, model, samples, confusion_matrix=None):\n    # Step 1: Pairwise confusability matrix\n    if confusion_matrix is not None:                      # SDGD-cal\n        C = normalize_confusion(confusion_matrix)         # symmetric, [0,1]\n    else:                                                 # SDGD-zero\n        C = cosine_similarity(embeddings, embeddings)     # [N, N]\n\n    # Step 2: Thresholded adjacency graph\n    A = (C > τ) & ~eye(N)                                # binary adjacency\n    G = Graph(nodes=types.keys(), edges=A.nonzero())\n\n    # Step 3: Greedy graph coloring → type batches\n    coloring = greedy_color(G, strategy=\"largest_first\")  # {type: color_id}\n    batches = group_by_color(coloring)                    # {color_id: [type_names]}\n\n    # Step 4: Per-batch extraction\n    all_predictions = []\n    for batch_id, batch_types in batches.items():\n        prompts = [build_prompt(s[\"text\"], types, batch_types) for s in samples]\n        schema = build_json_schema(batch_types)\n        outputs = model.generate(prompts, guided_decoding=schema)\n        preds = parse_outputs(outputs, batch_id, batch_types)\n        all_predictions.append(preds)\n\n    # Step 5: Merge across batches\n    merged = merge_predictions(all_predictions)\n    return merged\n```\n\n## 2. Key Design Decisions\n\n### 2.1 SDGD-zero vs SDGD-cal\n\n| | SDGD-zero | SDGD-cal |\n|---|---|---|\n| Confusability source | Embedding cosine similarity | Empirical confusion matrix from k calibration examples |\n| Data requirement | None (zero-shot) | 5-10 labeled examples per type |\n| Quality | Proxy — embedding similarity ≈ semantic confusability | Ground truth — measures actual model confusion |\n| Cost | Free (embeddings precomputed) | k × N_types extraction calls for calibration |\n| When to use | No labeled data; rapid schema adaptation | Labeled data available; maximum accuracy |\n\n**Calibration procedure (SDGD-cal)**:\n```\nfunction compute_empirical_confusion(types, model, calibration_samples):\n    # Run single-pass extraction with ALL types on calibration set\n    preds = extract(model, calibration_samples, all_types=types)\n    \n    # Build confusion matrix: C[i,j] = count of gold type-i predicted as type-j\n    C = zeros(N, N)\n    for sample in calibration_samples:\n        for gold_entity in sample.entities:\n            matched_pred = find_best_match(gold_entity, preds[sample.id])\n            if matched_pred:\n                i = type_index[gold_entity.type]\n                j = type_index[matched_pred.type]\n                C[i, j] += 1\n    \n    # Symmetrize and normalize\n    C_sym = (C + C.T) / 2\n    row_sums = C_sym.sum(dim=1, keepdim=True).clamp(min=1)\n    return C_sym / row_sums\n```\n\n### 2.2 Threshold τ Selection\n\n**Primary method: Adaptive threshold（数据集无关）**\n\n`τ = mean(C_upper_tri) + k · std(C_upper_tri)`，k 是唯一超参数。\n\n- 自适应于不同 schema 的 embedding 分布，避免循环性问题（不从目标数据集推导阈值）\n- Few-NERD Qwen3 embeddings: mean=0.7837, std=0.0653 → k=1.0 时 τ ≈ 0.85\n- 默认 k=1.0，通过 k sweep 消融确定最优值\n\n**Oracle threshold baseline（上界对比用）**:\n- 从 Few-NERD BCS-quality curve 推导的固定 τ∈[0.82, 0.88]\n- 仅用于 Few-NERD 上的上界对比实验，**不可用于跨域验证**（exp-009 等）\n- 论文中明确标注为 \"oracle\" 以区分\n\n**跨域验证要求**:\n- exp-009（ACE05/MAVEN）等跨域实验 **必须** 使用 adaptive threshold\n- 不同数据集的 embedding 分布不同，固定 τ 无意义\n\n**消融计划**: k sweep {0.5, 1.0, 1.5, 2.0}，在 adaptive framework 内做。报告每个 k 下的：τ 值、batch 数量、F1、vs single-pass Δ。\n\n### 2.3 Graph Coloring Algorithm\n\n**选择: Greedy (largest_first)**\n\n理由：\n- IE schema 图很小（Few-NERD 66 nodes, ACE05 58 nodes, 最大 MAVEN 168 nodes）\n- Greedy coloring 时间复杂度 O(V²)，对 168 nodes 微秒级\n- Optimal coloring 是 NP-hard，但 greedy 在稀疏图（τ 控制密度）上接近最优\n- NetworkX `greedy_color` 直接可用，strategy=\"largest_first\" 优先处理高度节点\n\n**Batch 数量预估** (Few-NERD, τ=0.85):\n- 同 coarse category 内 subtypes 基本都 > 0.85（如 person-* 8 个 subtypes 互相 BCS > 0.88）\n- 预计 chromatic number ≈ 8-10（≈ max clique size in thresholded graph）\n- 对比 single-pass (1 batch, 66 types) 和 per-type (66 batches)\n\n### 2.4 Merge Strategy\n\n**Primary: Simple union**（适用于 NER）\n```\nfunction merge_predictions(batch_predictions):\n    merged = defaultdict(list)\n    for batch_preds in batch_predictions:\n        for pred in batch_preds:\n            merged[pred.sample_id].extend(pred.predictions)\n    return merged\n```\n\nNER batch 之间 type 集合不重叠（graph coloring 保证），所以不存在同一 span 被不同 batch 提取为不同 type 的冲突。唯一可能的重复：同一 span 被提取为同一 type（hallucination）。\n\n**Conflict resolution（RE/EE 跨层时需要）**:\n- 同一 (text, type) pair 出现在多个 batch → deduplicate\n- 同一 span 不同 type → 保留 confidence 最高的（如果 model 提供 logprob）或保留全部（交给 evaluator）\n\n当前 NER-only 阶段用 simple union 即可。\n\n## 3. Module Structure\n\n```\nsrc/sdgd/\n  __init__.py           # Public API: sdgd_extract()\n  similarity.py         # Pairwise confusability computation\n  graph.py              # Threshold graph construction + coloring\n  decompose.py          # Main decomposition orchestrator\n  merge.py              # Result merging across batches\n  evaluate.py           # SDGD-specific evaluation & comparison\n```\n\n### 3.1 `similarity.py`\n\n```python\n\"\"\"Pairwise confusability matrix computation.\"\"\"\nimport torch\nimport torch.nn.functional as F\nfrom typing import Dict, Optional, Tuple, List\n\ndef load_type_embeddings(path: str) -> Tuple[torch.Tensor, List[str]]:\n    \"\"\"Load precomputed type embeddings.\n    \n    Returns:\n        embeddings: [N, D] tensor (N=66, D=5120 for Qwen3)\n        type_names: ordered list of type names matching embedding rows\n    \"\"\"\n    ...\n\ndef cosine_similarity_matrix(embeddings: torch.Tensor) -> torch.Tensor:\n    \"\"\"Compute pairwise cosine similarity. Returns [N, N] matrix in [0, 1].\"\"\"\n    normed = F.normalize(embeddings, dim=1)\n    return normed @ normed.T\n\ndef normalize_confusion_matrix(C: torch.Tensor) -> torch.Tensor:\n    \"\"\"Symmetrize and normalize raw confusion counts to [0, 1].\n    \n    C[i,j] = count of gold type-i predicted as type-j.\n    Output: symmetric matrix, diagonal zeroed, max-normalized.\n    \"\"\"\n    ...\n\ndef compute_confusability(\n    embeddings: torch.Tensor,\n    confusion_matrix: Optional[torch.Tensor] = None,\n) -> torch.Tensor:\n    \"\"\"Unified confusability computation.\n    \n    SDGD-zero: uses embedding cosine similarity.\n    SDGD-cal: uses normalized empirical confusion matrix.\n    \"\"\"\n    if confusion_matrix is not None:\n        return normalize_confusion_matrix(confusion_matrix)\n    return cosine_similarity_matrix(embeddings)\n```\n\n### 3.2 `graph.py`\n\n```python\n\"\"\"Confusability graph construction and coloring.\"\"\"\nimport networkx as nx\nimport torch\nfrom typing import Dict, List, Tuple\n\ndef build_confusability_graph(\n    conf_matrix: torch.Tensor,\n    type_names: List[str],\n    threshold: float,\n) -> nx.Graph:\n    \"\"\"Build thresholded undirected graph.\n    \n    Edge (i, j) exists iff conf_matrix[i, j] > threshold and i != j.\n    Edge weight = conf_matrix[i, j].\n    \"\"\"\n    ...\n\ndef color_graph(\n    G: nx.Graph,\n    strategy: str = \"largest_first\",\n) -> Dict[str, int]:\n    \"\"\"Greedy graph coloring. Returns {type_name: color_id}.\"\"\"\n    return nx.coloring.greedy_color(G, strategy=strategy)\n\ndef coloring_to_batches(coloring: Dict[str, int]) -> Dict[int, List[str]]:\n    \"\"\"Convert coloring assignment to batch groups. Returns {batch_id: [type_names]}.\"\"\"\n    batches = {}\n    for type_name, color_id in coloring.items():\n        batches.setdefault(color_id, []).append(type_name)\n    return batches\n\ndef compute_batch_bcs(\n    batches: Dict[int, List[str]],\n    conf_matrix: torch.Tensor,\n    type_names: List[str],\n) -> Dict[int, float]:\n    \"\"\"Compute BCS (max pairwise confusability) for each batch.\"\"\"\n    ...\n\ndef graph_stats(G: nx.Graph, batches: Dict[int, List[str]]) -> Dict:\n    \"\"\"Summary stats: num_batches, avg_batch_size, max_bcs, edge_density.\"\"\"\n    ...\n```\n\n### 3.3 `decompose.py`\n\n```python\n\"\"\"Main SDGD decomposition orchestrator.\"\"\"\nfrom typing import Dict, List, Optional\nfrom .similarity import load_type_embeddings, compute_confusability\nfrom .graph import build_confusability_graph, color_graph, coloring_to_batches\n\nclass SDGDDecomposer:\n    def __init__(\n        self,\n        type_definitions: Dict[str, str],\n        embedding_path: str,\n        threshold: float,\n        confusion_matrix: Optional[torch.Tensor] = None,\n    ):\n        self.type_definitions = type_definitions\n        self.embeddings, self.type_names = load_type_embeddings(embedding_path)\n        self.threshold = threshold\n        self.conf_matrix = compute_confusability(\n            self.embeddings, confusion_matrix\n        )\n        self._build_batches()\n\n    def _build_batches(self):\n        \"\"\"Construct confusability graph and compute coloring.\"\"\"\n        self.graph = build_confusability_graph(\n            self.conf_matrix, self.type_names, self.threshold\n        )\n        coloring = color_graph(self.graph)\n        self.batches = coloring_to_batches(coloring)\n\n    @property\n    def num_batches(self) -> int:\n        return len(self.batches)\n\n    def get_batch_types(self, batch_id: int) -> List[str]:\n        return self.batches[batch_id]\n\n    def get_batch_definitions(self, batch_id: int) -> Dict[str, str]:\n        \"\"\"Return {type_name: description} for a batch, ready for prompt construction.\"\"\"\n        return {t: self.type_definitions[t] for t in self.batches[batch_id]}\n```\n\n**Integration with existing `run_extraction.py`**:\n\n```python\n# In the extraction loop — replaces fixed batch composition\nfrom sdgd.decompose import SDGDDecomposer\n\ndecomposer = SDGDDecomposer(\n    type_definitions=load_json(\"configs/few_nerd_types.json\"),\n    embedding_path=\"artifacts/type_embeddings.pt\",\n    threshold=0.85,\n)\n\nall_predictions = []\nfor batch_id in range(decomposer.num_batches):\n    batch_types = decomposer.get_batch_types(batch_id)\n    batch_schema = build_json_schema(batch_types)       # existing function\n    prompts = [build_prompt(s[\"text\"], type_definitions, batch_types) \n               for s in samples]                         # existing function\n    outputs = llm.generate(prompts, SamplingParams(\n        max_tokens=1024, temperature=0.0,\n        guided_decoding=GuidedDecodingParams(json=batch_schema),\n    ))\n    preds = parse_outputs(outputs, batch_id, batch_types) # existing function\n    all_predictions.extend(preds)\n\nmerged = merge_predictions(all_predictions)               # new: sdgd.merge\n```\n\n### 3.4 `merge.py`\n\n```python\n\"\"\"Result merging across batches.\"\"\"\nfrom collections import defaultdict\nfrom typing import Dict, List\n\ndef merge_predictions(\n    batch_predictions: List[List[Dict]],\n    strategy: str = \"union\",\n) -> List[Dict]:\n    \"\"\"Merge predictions from multiple batches.\n    \n    Strategies:\n      - \"union\": simple concatenation (NER, types don't overlap across batches)\n      - \"dedup\": union + remove exact (text, type) duplicates per sample\n    \n    Input format per batch: [{\"sample_id\": int, \"predictions\": [{\"text\": str, \"type\": str}]}]\n    Output: same format, one entry per sample_id with all predictions merged.\n    \"\"\"\n    merged = defaultdict(list)\n    for batch_preds in batch_predictions:\n        for entry in batch_preds:\n            merged[entry[\"sample_id\"]].extend(entry[\"predictions\"])\n\n    if strategy == \"dedup\":\n        for sid in merged:\n            seen = set()\n            deduped = []\n            for p in merged[sid]:\n                key = (p[\"text\"], p[\"type\"])\n                if key not in seen:\n                    seen.add(key)\n                    deduped.append(p)\n            merged[sid] = deduped\n\n    return [{\"sample_id\": sid, \"predictions\": preds} \n            for sid, preds in sorted(merged.items())]\n```\n\n### 3.5 `evaluate.py`\n\n```python\n\"\"\"SDGD-specific evaluation and comparison.\"\"\"\nfrom typing import Dict, List, Tuple\n\ndef evaluate_sdgd(\n    predictions: List[Dict],\n    samples: List[Dict],\n    batches: Dict[int, List[str]],\n) -> Dict:\n    \"\"\"Evaluate SDGD extraction using text_match_eval.\n    \n    Returns:\n      - overall: micro P/R/F1 across all types\n      - per_batch: P/R/F1 per batch (with BCS annotation)\n      - per_type: P/R/F1 per type\n    \"\"\"\n    # Reuses text_match_eval from src/text_match_reeval.py\n    ...\n\ndef compare_methods(\n    results: Dict[str, Dict],\n    method_names: List[str] = None,\n) -> Dict:\n    \"\"\"Compare SDGD against baselines.\n    \n    Expected keys in results:\n      - \"single_pass\": all 66 types in one batch\n      - \"per_type\": 66 separate calls (UniNER-style)\n      - \"random_k\": random batching, same k as SDGD\n      - \"sdgd_zero\": SDGD with embedding similarity\n      - \"sdgd_cal\": SDGD with empirical confusion matrix\n    \n    Returns: comparison table with F1, API calls, latency.\n    \"\"\"\n    ...\n\ndef compute_api_cost(\n    num_batches: int,\n    num_samples: int,\n    avg_prompt_tokens: int,\n    avg_completion_tokens: int,\n) -> Dict:\n    \"\"\"Estimate API cost / vLLM throughput for different methods.\"\"\"\n    ...\n```\n\n## 4. Interfaces with Existing Code\n\n### 4.1 Prompt Construction (from `run_extraction.py`)\n\nSDGD 不修改 prompt 构建逻辑，只控制传入的 `type_subset` 参数：\n\n```python\n# Existing interface — unchanged\nbuild_prompt(input_text: str, type_definitions: Dict[str, str], type_subset: List[str]) -> str\nbuild_json_schema(batch_types: List[str]) -> dict\n```\n\nSDGD 通过 `decomposer.get_batch_types(batch_id)` 提供 `type_subset`。\n\n### 4.2 vLLM Inference (from `run_extraction.py`)\n\n复用现有 vLLM 初始化和调用逻辑。SDGD 只是在外层循环 batch：\n\n```python\n# Existing: single batch, all types\noutputs = llm.generate(prompts, sampling_params)\n\n# SDGD: loop over batches, each with subset types + constrained schema\nfor batch_id in range(decomposer.num_batches):\n    batch_schema = build_json_schema(decomposer.get_batch_types(batch_id))\n    outputs = llm.generate(prompts, SamplingParams(..., guided_decoding=GuidedDecodingParams(json=batch_schema)))\n```\n\n关键：vLLM engine 只初始化一次，batch 间复用。每个 batch 的 JSON schema 不同（type enum 不同）。\n\n### 4.3 Evaluation (from `text_match_reeval.py`)\n\n```python\n# Existing interface\ntext_match_eval(pred_entries, samples, batch_types) -> (prf_dict, per_type_dict)\n```\n\nSDGD evaluate 调用方式：\n- **Per-batch evaluation**: 每个 SDGD batch 独立调用 `text_match_eval`，得到 per-batch metrics（可与 BCS 做相关分析）\n- **Overall evaluation**: merge 后对全部 types 调用一次 `text_match_eval`，得到 SDGD 总体 F1\n\n### 4.4 Type Embeddings\n\n```\n/root/schema-dag-extraction/artifacts/type_embeddings.pt\n```\n- Format: `{\"embeddings\": Tensor[66, 5120], \"type_names\": List[str]}`（需确认实际格式）\n- Qwen3-32B mean-pooled last hidden states\n- 已验证：BCS range 0.5309, mean=0.7837, std=0.0653\n\n## 5. Baseline Methods for Comparison\n\n| Method | Batches | Types/Batch | BCS Control | API Calls |\n|--------|---------|-------------|-------------|-----------|\n| Single-pass | 1 | 66 | None (max BCS) | N |\n| Per-type (UniNER) | 66 | 1 | 0 (trivially) | 66N |\n| Random-k | k (= SDGD's k) | ~66/k | Random | kN |\n| SDGD-zero | k (from coloring) | Variable | ≤ τ | kN |\n| SDGD-cal | k' (from coloring) | Variable | ≤ τ | k'N + calibration |\n\nRandom-k 是关键消融——与 SDGD 相同 batch 数量但随机分组。F1 差异直接量化 confusability-aware grouping 的价值。\n\n## 6. Implementation Notes\n\n1. **Graph coloring 确定性**: `nx.greedy_color` 受节点遍历顺序影响。固定 `type_names` 排序以保证可复现。\n\n2. **Threshold sensitivity**: τ 轻微变化可能改变 batch 数量（图密度突变）。评估时报告 τ vs num_batches 曲线。\n\n3. **vLLM batch 效率**: 每个 SDGD batch 对全部 1000 samples 做推理。总推理次数 = k × 1000。对比 per-type 的 66 × 1000 = 66k 次。SDGD 如果 k ≈ 10，则 10k 次，6.6x speedup over per-type。\n\n4. **Prompt v2**: SDGD 必须使用 exp003a 的 prompt v2（text-only, anti-hallucination instruction），不要用 v1（含 char offset 要求）。\n\n5. **Empty batch handling**: 某些 batch 可能只包含低频 type（测试集中无 gold entity）。仍需执行推理（可能提取到 entity），但评估时 gold=0 的 batch 不参与 F1 计算。\n\n6. **Dependency on exp003a**: 实际代码编写等 exp003a 完成确认数据干净后再开始。当前 document 为设计阶段。\n",
      "numLines": 476,
      "startLine": 1,
      "totalLines": 476
    }
  }
}
````

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
I now have all the source materials. Let me create the three output files:

1. `method_framework.md` - Method Section framework
2. `related_work_draft.md` - Related Work draft
3. `maven_description.md` - MAVEN dataset description

Let me also check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "83836799-aaf0-4883-80a3-b32f6772b184",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8bLEEPYYV13iAgVtkR77T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13901,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13901
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

All source materials loaded. Now writing the three drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "a88d94ab-1419-4038-865d-1e770dfdfb87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8bLEEPYYV13iAgVtkR77T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13901,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13901
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

<details open><summary>🔧 Tool call — Bash · `toolu_01WBzJ3CGqXsrbkA4PPLEXzS`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "1d0e8008-0809-4d44-8ed6-f2f891ada0db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8bLEEPYYV13iAgVtkR77T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13901,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13901
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

_source line 17 · 2026-05-15T03:53:45.943Z_

<details><summary>↩ Tool result · `toolu_01WBzJ3CGqXsrbkA4PPLEXzS`</summary>

```text
DIR_NOT_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "12f1eda8-7c88-4b73-8728-e055a22f8494",
  "tool_use_result": {
    "stdout": "DIR_NOT_FOUND",
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pw6CSp2yXtm12k1PGXDPUo`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts",
  "description": "Create paper_drafts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "df13eb2e-3065-427a-acc6-7f09149ebf58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxKpVUziunkuifXsibkab1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 38673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 19 · 2026-05-15T03:53:48.473Z_

<details><summary>↩ Tool result · `toolu_01Pw6CSp2yXtm12k1PGXDPUo`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "bf3f3198-c8e7-439b-ba14-69ff9212b9ba",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_01BnWtCesMcpzE41MMoSo1qK`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/method_framework.md",
  "content": "# Section 3: Method\n\n## 3.1 Problem Formulation\n\n### Schema Complexity in Training-Free LLM IE\n\nWe consider training-free information extraction where an LLM $\\mathcal{M}$ extracts typed mentions from input text $x$ given a schema $\\mathcal{S} = \\{(t_i, d_i)\\}_{i=1}^{N}$, where $t_i$ is a type name and $d_i$ its natural language description. The LLM receives $\\mathcal{S}$ (or a subset) in its prompt and produces structured predictions $\\hat{Y} = \\{(m_j, t_j)\\}$, each a mention span $m_j$ paired with a type $t_j \\in \\mathcal{S}$.\n\n**Type count** $N = |\\mathcal{S}|$ is the number of types presented simultaneously. Prior work implicitly treats $N$ as the sole driver of schema complexity.\n\n**Pairwise type confusability.** We define the *Schema Confusability Score* (SCS) between types $t_i$ and $t_j$ as:\n\n$$\\text{SCS}(t_i, t_j) = \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$$\n\nwhere $\\mathbf{e}_i \\in \\mathbb{R}^D$ is the mean-pooled hidden state of $\\mathcal{M}$ when encoding type $t_i$'s definition. SCS captures the degree to which two types occupy overlapping regions in the model's representation space.\n\n**Batch Confusability Score (BCS).** For a batch $B \\subseteq \\mathcal{S}$, we define:\n\n$$\\text{BCS}(B) = \\max_{t_i, t_j \\in B, \\, i \\neq j} \\text{SCS}(t_i, t_j)$$\n\nBCS measures the worst-case confusability within a batch --- the pair of types most likely to be confused by the model when co-presented.\n\n**Schema complexity** is thus characterized by two independent factors: the *count* $N$ and the *confusability structure* of $\\mathcal{S}$, as captured by the pairwise SCS matrix $\\mathbf{C} \\in [0,1]^{N \\times N}$.\n\n\n## 3.2 Controlled Experiment Design\n\nTo disentangle the effects of type count and type confusability on extraction quality, we design a controlled experimental protocol with two complementary analyses.\n\n### Count Curve Analysis\n\nWe construct type subsets of increasing size $n \\in \\{5, 10, 15, \\ldots, N\\}$ by sampling from $\\mathcal{S}$, extract on fixed evaluation samples, and measure micro-F1, precision, and recall as functions of $n$. Multiple random draws per count level reduce sampling variance. This establishes the *marginal* effect of count on extraction performance.\n\n### Within-Count BCS Correlation\n\nAt each count level $n$, multiple batches with the same number of types but *different* confusability profiles are constructed. We compute:\n\n$$r = \\text{Pearson}(\\text{BCS}(B_1), \\ldots, \\text{BCS}(B_m); \\; F_1(B_1), \\ldots, F_1(B_m)) \\quad \\text{at fixed } n$$\n\nA significant negative correlation at fixed $n$ demonstrates that confusability predicts quality degradation *beyond* what count alone explains. We further compute partial correlations $r(\\text{F1}, \\text{BCS} \\mid n)$ pooled across all count levels to quantify confusability's independent contribution.\n\n### Multi-Channel Degradation Model\n\nThe controlled analysis reveals two orthogonal degradation channels:\n\n- **Channel 1 (Count $\\to$ Recall decline):** Increasing $N$ causes the model to *omit* entities. Manifests as monotonic recall degradation, consistent with attention capacity limits.\n- **Channel 2 (Confusability $\\to$ Precision decline):** Co-presenting confusable types causes *type confusion* --- entities are detected but assigned the wrong type. Manifests as precision degradation correlated with BCS.\n\nError taxonomy analysis confirms the two channels produce distinct error types: *omission errors* (false negatives from capacity limits) vs. *type confusion errors* (correct span, wrong type).\n\n\n## 3.3 SDGD Framework\n\nBased on the multi-channel degradation model, we propose **Schema-Decomposed Graph-Driven (SDGD) extraction**, a framework that partitions the schema into low-confusability batches to neutralize Channel 2 degradation.\n\n### Algorithm Overview\n\n**Input:** Type schema $\\mathcal{S} = \\{(t_i, d_i)\\}_{i=1}^N$; type embeddings $\\mathbf{E} \\in \\mathbb{R}^{N \\times D}$; confusability threshold $\\tau$; LLM $\\mathcal{M}$; evaluation samples $\\mathcal{X}$. Optionally: empirical confusion matrix $\\mathbf{C}_{\\text{emp}}$ (for SDGD-cal).\n\n**Output:** Merged predictions $\\hat{Y}$ over all types.\n\n**Step 1 --- Confusability matrix computation.** Compute pairwise confusability $\\mathbf{C} \\in [0,1]^{N \\times N}$. In the zero-shot variant (SDGD-zero), $\\mathbf{C}_{ij} = \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$. In the calibrated variant (SDGD-cal), $\\mathbf{C}$ is derived from an empirical confusion matrix obtained on a small calibration set (\\S3.4).\n\n**Step 2 --- Thresholded confusability graph.** Construct undirected graph $G = (V, E)$ where $V = \\mathcal{S}$ and edge $(t_i, t_j) \\in E$ iff $\\mathbf{C}_{ij} > \\tau$ and $i \\neq j$. Two types are adjacent iff they are \"too confusable\" to co-exist in a single batch.\n\n**Step 3 --- Greedy graph coloring.** Compute a proper vertex coloring of $G$ using greedy coloring with the \\texttt{largest\\_first} strategy. The coloring assigns each type to a color (batch) such that no two adjacent (highly confusable) types share a batch. The number of colors $k$ equals the chromatic number approximation.\n\n**Step 4 --- Per-batch extraction.** For each color group $B_c$ ($c = 1, \\ldots, k$), construct a prompt containing only the type definitions in $B_c$, and extract mentions from all samples $\\mathcal{X}$ using $\\mathcal{M}$ with constrained decoding (JSON schema restricting outputs to types in $B_c$).\n\n**Step 5 --- Cross-batch merge.** Since graph coloring guarantees non-overlapping type sets across batches, predictions are merged by simple union. For each sample, the final prediction set is the concatenation of predictions from all $k$ batches.\n\n### LaTeX Pseudocode\n\n```latex\n\\begin{algorithm}[t]\n\\caption{SDGD: Schema-Decomposed Graph-Driven Extraction}\n\\label{alg:sdgd}\n\\begin{algorithmic}[1]\n\\REQUIRE Schema $\\mathcal{S} = \\{(t_i, d_i)\\}_{i=1}^N$, embeddings $\\mathbf{E} \\in \\mathbb{R}^{N \\times D}$, threshold $\\tau$, LLM $\\mathcal{M}$, samples $\\mathcal{X}$\n\\ENSURE Predictions $\\hat{Y}$\n\n\\STATE \\textbf{// Step 1: Confusability matrix}\n\\STATE $\\mathbf{C}_{ij} \\leftarrow \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$ for all $i, j \\in [N]$\n\\COMMENT{SDGD-zero; SDGD-cal uses empirical confusion}\n\n\\STATE \\textbf{// Step 2: Thresholded confusability graph}\n\\STATE $V \\leftarrow \\mathcal{S}$\n\\STATE $E \\leftarrow \\{(t_i, t_j) \\mid \\mathbf{C}_{ij} > \\tau,\\ i \\neq j\\}$\n\\STATE $G \\leftarrow (V, E)$\n\n\\STATE \\textbf{// Step 3: Graph coloring}\n\\STATE $\\phi \\leftarrow \\textsc{GreedyColor}(G, \\text{largest\\_first})$\n\\COMMENT{$\\phi: V \\to \\{1, \\ldots, k\\}$}\n\\STATE $\\{B_1, \\ldots, B_k\\} \\leftarrow \\textsc{GroupByColor}(\\phi)$\n\n\\STATE \\textbf{// Step 4: Per-batch extraction}\n\\STATE $\\hat{Y} \\leftarrow \\emptyset$\n\\FOR{$c = 1$ \\TO $k$}\n    \\STATE $\\hat{Y}_c \\leftarrow \\mathcal{M}.\\text{extract}(\\mathcal{X}, B_c)$\n    \\COMMENT{Constrained to types in $B_c$}\n    \\STATE $\\hat{Y} \\leftarrow \\hat{Y} \\cup \\hat{Y}_c$\n    \\COMMENT{Union merge}\n\\ENDFOR\n\n\\RETURN $\\hat{Y}$\n\\end{algorithmic}\n\\end{algorithm}\n```\n\n### Threshold Selection\n\nThe threshold $\\tau$ controls graph density and hence the number of batches $k$. We adopt an **adaptive threshold** strategy that is schema-agnostic:\n\n$$\\tau = \\mu(\\mathbf{C}_{\\text{upper}}) + k_\\sigma \\cdot \\sigma(\\mathbf{C}_{\\text{upper}})$$\n\nwhere $\\mathbf{C}_{\\text{upper}}$ denotes the upper-triangular entries of $\\mathbf{C}$ (excluding the diagonal), $\\mu$ and $\\sigma$ are the mean and standard deviation, and $k_\\sigma$ is the sole hyperparameter. The adaptive threshold adjusts to the embedding distribution of each schema, avoiding reliance on dataset-specific tuning. We set $k_\\sigma = 1.0$ by default and conduct ablations over $k_\\sigma \\in \\{0.5, 1.0, 1.5, 2.0\\}$.\n\nFor analysis purposes, we also report an **oracle threshold** derived from the BCS--quality degradation curve on the development set. The oracle serves as an upper bound and is clearly distinguished from the adaptive method in all results.\n\n### Complexity\n\nGraph coloring on $N$ types is $O(N^2)$ with greedy heuristics. For the schemas in our experiments ($N \\leq 168$), decomposition completes in milliseconds. The dominant cost is LLM inference: SDGD requires $k \\times |\\mathcal{X}|$ generation calls, compared to $1 \\times |\\mathcal{X}|$ for single-pass and $N \\times |\\mathcal{X}|$ for per-type splitting. With $k \\approx 8\\text{--}12$, SDGD achieves $5\\text{--}8\\times$ fewer calls than per-type splitting.\n\n\n## 3.4 SDGD-zero and SDGD-cal Variants\n\nWe instantiate two variants of the SDGD framework, differing in how the confusability matrix $\\mathbf{C}$ is obtained:\n\n### SDGD-zero (Zero-Shot)\n\nThe confusability matrix is computed from type embeddings alone, with no labeled data. We encode each type definition $d_i$ through $\\mathcal{M}$ and extract the mean-pooled last hidden state $\\mathbf{e}_i \\in \\mathbb{R}^D$. Pairwise cosine similarity serves as the confusability proxy:\n\n$$\\mathbf{C}_{ij}^{\\text{zero}} = \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$$\n\n**Advantages:** Fully zero-shot; no labeled data required; embeddings are precomputed once per schema. Suitable for rapid deployment on new schemas.\n\n**Limitation:** Embedding similarity is a *proxy* for confusability. Two types may be semantically similar yet easily distinguished in context (e.g., \\textit{person-artist} and \\textit{person-actor} share embedding space but have distinct contextual cues).\n\n### SDGD-cal (Calibrated)\n\nThe confusability matrix is derived from empirical extraction errors on a small calibration set of $m$ labeled examples per type:\n\n1. Run single-pass extraction with all $N$ types on the calibration set.\n2. Construct a raw confusion matrix $\\mathbf{C}_{\\text{raw}} \\in \\mathbb{R}^{N \\times N}$, where $\\mathbf{C}_{\\text{raw}}[i,j]$ counts gold type-$i$ entities predicted as type-$j$.\n3. Symmetrize: $\\mathbf{C}_{\\text{sym}} = (\\mathbf{C}_{\\text{raw}} + \\mathbf{C}_{\\text{raw}}^\\top) / 2$.\n4. Normalize: $\\mathbf{C}_{ij}^{\\text{cal}} = \\mathbf{C}_{\\text{sym}}[i,j] / \\sum_j \\mathbf{C}_{\\text{sym}}[i,j]$.\n\n**Advantages:** Measures *actual* model confusion rather than semantic proximity. Captures model-specific and context-dependent confusability patterns.\n\n**Cost:** Requires $m$ labeled examples per type for calibration ($m = 5\\text{--}10$ in our experiments). Total calibration cost: one extraction pass over the calibration set.\n\n### Comparison\n\n| | SDGD-zero | SDGD-cal |\n|---|---|---|\n| Data requirement | None | $m$ labeled examples/type |\n| Confusability signal | Semantic proximity | Empirical model errors |\n| Schema adaptability | Instant | Requires calibration pass |\n| Expected quality | Good (proxy) | Best (ground-truth confusion) |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "e898fffa-6e48-4874-84f6-380bbf5a9cee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MLWbU4BGDu6u2zHLtWf9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 128,
      "cache_read_input_tokens": 38919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 128
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

_source line 21 · 2026-05-15T03:55:00.022Z_

<details><summary>↩ Tool result · `toolu_01BnWtCesMcpzE41MMoSo1qK`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/method_framework.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "a6b1a7d9-8f77-4945-8c31-7594f2301ef0",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/method_framework.md",
    "content": "# Section 3: Method\n\n## 3.1 Problem Formulation\n\n### Schema Complexity in Training-Free LLM IE\n\nWe consider training-free information extraction where an LLM $\\mathcal{M}$ extracts typed mentions from input text $x$ given a schema $\\mathcal{S} = \\{(t_i, d_i)\\}_{i=1}^{N}$, where $t_i$ is a type name and $d_i$ its natural language description. The LLM receives $\\mathcal{S}$ (or a subset) in its prompt and produces structured predictions $\\hat{Y} = \\{(m_j, t_j)\\}$, each a mention span $m_j$ paired with a type $t_j \\in \\mathcal{S}$.\n\n**Type count** $N = |\\mathcal{S}|$ is the number of types presented simultaneously. Prior work implicitly treats $N$ as the sole driver of schema complexity.\n\n**Pairwise type confusability.** We define the *Schema Confusability Score* (SCS) between types $t_i$ and $t_j$ as:\n\n$$\\text{SCS}(t_i, t_j) = \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$$\n\nwhere $\\mathbf{e}_i \\in \\mathbb{R}^D$ is the mean-pooled hidden state of $\\mathcal{M}$ when encoding type $t_i$'s definition. SCS captures the degree to which two types occupy overlapping regions in the model's representation space.\n\n**Batch Confusability Score (BCS).** For a batch $B \\subseteq \\mathcal{S}$, we define:\n\n$$\\text{BCS}(B) = \\max_{t_i, t_j \\in B, \\, i \\neq j} \\text{SCS}(t_i, t_j)$$\n\nBCS measures the worst-case confusability within a batch --- the pair of types most likely to be confused by the model when co-presented.\n\n**Schema complexity** is thus characterized by two independent factors: the *count* $N$ and the *confusability structure* of $\\mathcal{S}$, as captured by the pairwise SCS matrix $\\mathbf{C} \\in [0,1]^{N \\times N}$.\n\n\n## 3.2 Controlled Experiment Design\n\nTo disentangle the effects of type count and type confusability on extraction quality, we design a controlled experimental protocol with two complementary analyses.\n\n### Count Curve Analysis\n\nWe construct type subsets of increasing size $n \\in \\{5, 10, 15, \\ldots, N\\}$ by sampling from $\\mathcal{S}$, extract on fixed evaluation samples, and measure micro-F1, precision, and recall as functions of $n$. Multiple random draws per count level reduce sampling variance. This establishes the *marginal* effect of count on extraction performance.\n\n### Within-Count BCS Correlation\n\nAt each count level $n$, multiple batches with the same number of types but *different* confusability profiles are constructed. We compute:\n\n$$r = \\text{Pearson}(\\text{BCS}(B_1), \\ldots, \\text{BCS}(B_m); \\; F_1(B_1), \\ldots, F_1(B_m)) \\quad \\text{at fixed } n$$\n\nA significant negative correlation at fixed $n$ demonstrates that confusability predicts quality degradation *beyond* what count alone explains. We further compute partial correlations $r(\\text{F1}, \\text{BCS} \\mid n)$ pooled across all count levels to quantify confusability's independent contribution.\n\n### Multi-Channel Degradation Model\n\nThe controlled analysis reveals two orthogonal degradation channels:\n\n- **Channel 1 (Count $\\to$ Recall decline):** Increasing $N$ causes the model to *omit* entities. Manifests as monotonic recall degradation, consistent with attention capacity limits.\n- **Channel 2 (Confusability $\\to$ Precision decline):** Co-presenting confusable types causes *type confusion* --- entities are detected but assigned the wrong type. Manifests as precision degradation correlated with BCS.\n\nError taxonomy analysis confirms the two channels produce distinct error types: *omission errors* (false negatives from capacity limits) vs. *type confusion errors* (correct span, wrong type).\n\n\n## 3.3 SDGD Framework\n\nBased on the multi-channel degradation model, we propose **Schema-Decomposed Graph-Driven (SDGD) extraction**, a framework that partitions the schema into low-confusability batches to neutralize Channel 2 degradation.\n\n### Algorithm Overview\n\n**Input:** Type schema $\\mathcal{S} = \\{(t_i, d_i)\\}_{i=1}^N$; type embeddings $\\mathbf{E} \\in \\mathbb{R}^{N \\times D}$; confusability threshold $\\tau$; LLM $\\mathcal{M}$; evaluation samples $\\mathcal{X}$. Optionally: empirical confusion matrix $\\mathbf{C}_{\\text{emp}}$ (for SDGD-cal).\n\n**Output:** Merged predictions $\\hat{Y}$ over all types.\n\n**Step 1 --- Confusability matrix computation.** Compute pairwise confusability $\\mathbf{C} \\in [0,1]^{N \\times N}$. In the zero-shot variant (SDGD-zero), $\\mathbf{C}_{ij} = \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$. In the calibrated variant (SDGD-cal), $\\mathbf{C}$ is derived from an empirical confusion matrix obtained on a small calibration set (\\S3.4).\n\n**Step 2 --- Thresholded confusability graph.** Construct undirected graph $G = (V, E)$ where $V = \\mathcal{S}$ and edge $(t_i, t_j) \\in E$ iff $\\mathbf{C}_{ij} > \\tau$ and $i \\neq j$. Two types are adjacent iff they are \"too confusable\" to co-exist in a single batch.\n\n**Step 3 --- Greedy graph coloring.** Compute a proper vertex coloring of $G$ using greedy coloring with the \\texttt{largest\\_first} strategy. The coloring assigns each type to a color (batch) such that no two adjacent (highly confusable) types share a batch. The number of colors $k$ equals the chromatic number approximation.\n\n**Step 4 --- Per-batch extraction.** For each color group $B_c$ ($c = 1, \\ldots, k$), construct a prompt containing only the type definitions in $B_c$, and extract mentions from all samples $\\mathcal{X}$ using $\\mathcal{M}$ with constrained decoding (JSON schema restricting outputs to types in $B_c$).\n\n**Step 5 --- Cross-batch merge.** Since graph coloring guarantees non-overlapping type sets across batches, predictions are merged by simple union. For each sample, the final prediction set is the concatenation of predictions from all $k$ batches.\n\n### LaTeX Pseudocode\n\n```latex\n\\begin{algorithm}[t]\n\\caption{SDGD: Schema-Decomposed Graph-Driven Extraction}\n\\label{alg:sdgd}\n\\begin{algorithmic}[1]\n\\REQUIRE Schema $\\mathcal{S} = \\{(t_i, d_i)\\}_{i=1}^N$, embeddings $\\mathbf{E} \\in \\mathbb{R}^{N \\times D}$, threshold $\\tau$, LLM $\\mathcal{M}$, samples $\\mathcal{X}$\n\\ENSURE Predictions $\\hat{Y}$\n\n\\STATE \\textbf{// Step 1: Confusability matrix}\n\\STATE $\\mathbf{C}_{ij} \\leftarrow \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$ for all $i, j \\in [N]$\n\\COMMENT{SDGD-zero; SDGD-cal uses empirical confusion}\n\n\\STATE \\textbf{// Step 2: Thresholded confusability graph}\n\\STATE $V \\leftarrow \\mathcal{S}$\n\\STATE $E \\leftarrow \\{(t_i, t_j) \\mid \\mathbf{C}_{ij} > \\tau,\\ i \\neq j\\}$\n\\STATE $G \\leftarrow (V, E)$\n\n\\STATE \\textbf{// Step 3: Graph coloring}\n\\STATE $\\phi \\leftarrow \\textsc{GreedyColor}(G, \\text{largest\\_first})$\n\\COMMENT{$\\phi: V \\to \\{1, \\ldots, k\\}$}\n\\STATE $\\{B_1, \\ldots, B_k\\} \\leftarrow \\textsc{GroupByColor}(\\phi)$\n\n\\STATE \\textbf{// Step 4: Per-batch extraction}\n\\STATE $\\hat{Y} \\leftarrow \\emptyset$\n\\FOR{$c = 1$ \\TO $k$}\n    \\STATE $\\hat{Y}_c \\leftarrow \\mathcal{M}.\\text{extract}(\\mathcal{X}, B_c)$\n    \\COMMENT{Constrained to types in $B_c$}\n    \\STATE $\\hat{Y} \\leftarrow \\hat{Y} \\cup \\hat{Y}_c$\n    \\COMMENT{Union merge}\n\\ENDFOR\n\n\\RETURN $\\hat{Y}$\n\\end{algorithmic}\n\\end{algorithm}\n```\n\n### Threshold Selection\n\nThe threshold $\\tau$ controls graph density and hence the number of batches $k$. We adopt an **adaptive threshold** strategy that is schema-agnostic:\n\n$$\\tau = \\mu(\\mathbf{C}_{\\text{upper}}) + k_\\sigma \\cdot \\sigma(\\mathbf{C}_{\\text{upper}})$$\n\nwhere $\\mathbf{C}_{\\text{upper}}$ denotes the upper-triangular entries of $\\mathbf{C}$ (excluding the diagonal), $\\mu$ and $\\sigma$ are the mean and standard deviation, and $k_\\sigma$ is the sole hyperparameter. The adaptive threshold adjusts to the embedding distribution of each schema, avoiding reliance on dataset-specific tuning. We set $k_\\sigma = 1.0$ by default and conduct ablations over $k_\\sigma \\in \\{0.5, 1.0, 1.5, 2.0\\}$.\n\nFor analysis purposes, we also report an **oracle threshold** derived from the BCS--quality degradation curve on the development set. The oracle serves as an upper bound and is clearly distinguished from the adaptive method in all results.\n\n### Complexity\n\nGraph coloring on $N$ types is $O(N^2)$ with greedy heuristics. For the schemas in our experiments ($N \\leq 168$), decomposition completes in milliseconds. The dominant cost is LLM inference: SDGD requires $k \\times |\\mathcal{X}|$ generation calls, compared to $1 \\times |\\mathcal{X}|$ for single-pass and $N \\times |\\mathcal{X}|$ for per-type splitting. With $k \\approx 8\\text{--}12$, SDGD achieves $5\\text{--}8\\times$ fewer calls than per-type splitting.\n\n\n## 3.4 SDGD-zero and SDGD-cal Variants\n\nWe instantiate two variants of the SDGD framework, differing in how the confusability matrix $\\mathbf{C}$ is obtained:\n\n### SDGD-zero (Zero-Shot)\n\nThe confusability matrix is computed from type embeddings alone, with no labeled data. We encode each type definition $d_i$ through $\\mathcal{M}$ and extract the mean-pooled last hidden state $\\mathbf{e}_i \\in \\mathbb{R}^D$. Pairwise cosine similarity serves as the confusability proxy:\n\n$$\\mathbf{C}_{ij}^{\\text{zero}} = \\text{cosine}(\\mathbf{e}_i, \\mathbf{e}_j)$$\n\n**Advantages:** Fully zero-shot; no labeled data required; embeddings are precomputed once per schema. Suitable for rapid deployment on new schemas.\n\n**Limitation:** Embedding similarity is a *proxy* for confusability. Two types may be semantically similar yet easily distinguished in context (e.g., \\textit{person-artist} and \\textit{person-actor} share embedding space but have distinct contextual cues).\n\n### SDGD-cal (Calibrated)\n\nThe confusability matrix is derived from empirical extraction errors on a small calibration set of $m$ labeled examples per type:\n\n1. Run single-pass extraction with all $N$ types on the calibration set.\n2. Construct a raw confusion matrix $\\mathbf{C}_{\\text{raw}} \\in \\mathbb{R}^{N \\times N}$, where $\\mathbf{C}_{\\text{raw}}[i,j]$ counts gold type-$i$ entities predicted as type-$j$.\n3. Symmetrize: $\\mathbf{C}_{\\text{sym}} = (\\mathbf{C}_{\\text{raw}} + \\mathbf{C}_{\\text{raw}}^\\top) / 2$.\n4. Normalize: $\\mathbf{C}_{ij}^{\\text{cal}} = \\mathbf{C}_{\\text{sym}}[i,j] / \\sum_j \\mathbf{C}_{\\text{sym}}[i,j]$.\n\n**Advantages:** Measures *actual* model confusion rather than semantic proximity. Captures model-specific and context-dependent confusability patterns.\n\n**Cost:** Requires $m$ labeled examples per type for calibration ($m = 5\\text{--}10$ in our experiments). Total calibration cost: one extraction pass over the calibration set.\n\n### Comparison\n\n| | SDGD-zero | SDGD-cal |\n|---|---|---|\n| Data requirement | None | $m$ labeled examples/type |\n| Confusability signal | Semantic proximity | Empirical model errors |\n| Schema adaptability | Instant | Requires calibration pass |\n| Expected quality | Good (proxy) | Best (ground-truth confusion) |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Write · `toolu_019jcCFoSJLag58su3VWKJZm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/related_work_draft.md",
  "content": "# Section 2: Related Work\n\n## 2.1 Schema Decomposition for Information Extraction\n\nHandling large type schemas has emerged as a key challenge for LLM-based IE. Several strategies have been proposed to reduce schema complexity at inference time.\n\n**Per-type and fixed decomposition.** UniversalNER \\cite{uniner-2024} distills ChatGPT into a compact model by targeting one entity type per extraction call, reporting +7 F1 over ChatGPT on 43 datasets. While effective, per-type splitting sacrifices cross-type context and incurs $O(N)$ inference cost, with no principled criterion for when decomposition is necessary. KGGen \\cite{kggen-2025} employs a two-stage pipeline --- entity extraction followed by relation extraction --- which decomposes at the *task* level rather than within the type schema. Similarly, DEE \\cite{dee-2024} separates event detection from argument extraction with dynamic schema-aware retrieval, but does not address intra-task type partitioning.\n\n**Similarity-based partitioning.** LLM-PEE \\cite{llm-pee-2025} partitions massive event type schemas via similarity-based recall, assigning types to groups that reduce prompt length. This achieves +5.4\\% event detection F1 over zero-shot baselines. However, LLM-PEE uses type similarity as an implicit proxy without empirically validating that similarity drives extraction errors --- the partition criterion optimizes for coverage, not confusability reduction.\n\n**Schema rewriting and tool-based approaches.** PARSE \\cite{parse-2025} uses an LLM to autonomously rewrite JSON schemas for better LLM consumption (+64.7\\% on SWDE), treating schema optimization as a black-box process without modeling type interactions. SPT \\cite{spt-2025} reframes schemas as parameterized tools for LLM tool-calling, offering a novel interface but not addressing why certain type configurations degrade extraction. DLISC \\cite{dlisc-2025} introduces dual-LoRA with incremental schema caching for on-device efficiency, orthogonal to our focus on type confusability.\n\n**Our distinction.** Unlike all prior decomposition methods, SDGD is grounded in an empirically validated degradation model: we first demonstrate that type confusability independently predicts extraction failure (controlling for count), then operationalize this finding into a graph-coloring-based decomposition that *provably* separates highly confusable types. No prior work explicitly isolates confusability from count as a degradation factor, nor optimizes decomposition to minimize it.\n\n\n## 2.2 Confusability-Aware Approaches in NLP\n\nThe notion that semantically similar labels cause classification errors has appeared across NLP, though not in the context of training-free LLM IE schema design.\n\n**Label confusion in training.** IEPile \\cite{iepile-2024} constructs hard negative schemas --- semantically proximate type sets --- during *training* to improve a model's type discrimination ability. This confirms that confusable schemas are harder, but the intervention is at training time. Our work addresses *inference-time* confusability for training-free systems where model weights are frozen. The Familiarity metric \\cite{familiarity-2025} quantifies label shift between synthetic training data and evaluation sets, revealing that zero-shot NER scores are overestimated when training labels overlap with evaluation labels. This measures *evaluation bias* from label similarity, not extraction-time confusion --- but supports our premise that type similarity is a meaningful confound.\n\n**Multi-agent debate for type resolution.** CROSSAGENTIE \\cite{crossagentie-2025} deploys cross-type debate within multi-agent systems to resolve entity-label conflicts: when an entity is assigned conflicting types by different agents, intra-group debate adjudicates. This *reactively* addresses type confusion after it occurs. CMAS-NER \\cite{cmas-ner-2025} similarly uses cooperative multi-agent collective intelligence to overcome context correlation and indiscriminate demonstration problems in zero-shot NER. Our approach is *proactive*: we prevent type confusion by ensuring highly confusable types never co-occur in a single extraction call. The two strategies are complementary --- SDGD decomposition could serve as a pre-processing stage for multi-agent systems.\n\n**Positional and attention effects.** Liu et al. \\cite{lost-in-middle-2024} demonstrate that LLMs degrade when relevant information appears in the middle of long contexts, exhibiting U-shaped attention patterns. While not IE-specific, this provides additional motivation for schema decomposition: shorter prompts with fewer types reduce the risk of attention-related information loss. To our knowledge, no prior work has connected positional attention biases to IE schema prompt design.\n\n\n## 2.3 LLM-Based Information Extraction\n\nTraining-free LLM IE has progressed rapidly, establishing both the opportunity and the challenge that motivate our work.\n\n**Instruction-tuned IE models.** GoLLIE \\cite{gollie-2024} demonstrates that code-style schema definitions with annotation guideline following enable strong zero-shot IE from a Code-LLaMA backbone. Code4UIE \\cite{code4uie-2024} extends this to retrieval-augmented code generation for universal IE. KnowCoder \\cite{knowcoder-2024} encodes schema knowledge via code structures into LLMs. These models internalize schema understanding through fine-tuning, sidestepping inference-time schema complexity. However, they require task-specific training, limiting deployment flexibility.\n\n**Zero-shot extraction methods.** Self-improving NER \\cite{self-improve-ner-2024} generates synthetic examples via LLM self-prompting, while ReasoningNER \\cite{reasoning-ner-2025} applies chain-of-thought reasoning to achieve +12.3 F1 over GPT-4 in zero-shot settings. ZeroNER \\cite{zeroner-2025} leverages entity type descriptions to produce LLM supervision for a BERT student model (+16\\% F1 over LLMs on hard zero-shot). These methods improve extraction within a fixed schema presentation, but do not address how schema *structure* --- the composition and similarity of co-presented types --- affects quality.\n\n**Compact and efficient models.** GLiNER \\cite{gliner-2024} achieves competitive zero-shot NER with a bidirectional encoder via parallel entity extraction, and GLiNER2 \\cite{gliner2-2025} extends this to multi-task IE. NuNER \\cite{nuner-2024} uses contrastive pre-training on LLM-annotated data for strong few-shot performance. These non-LLM alternatives avoid schema complexity issues by design (parallel per-type extraction), but sacrifice the generality and zero-shot flexibility of LLM-based approaches.\n\n**Surveys.** Xu et al. \\cite{llm4ie-survey-2024} provide a comprehensive survey of LLM-based generative IE, covering prompting strategies, fine-tuning paradigms, and benchmarks. Our work contributes to the prompting strategy dimension by showing that *what types are co-presented* matters as much as *how they are presented*.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "ff11fac8-009f-4762-acca-38ac903466c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MLWbU4BGDu6u2zHLtWf9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 128,
      "cache_read_input_tokens": 38919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 128
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

_source line 23 · 2026-05-15T03:55:47.275Z_

<details><summary>↩ Tool result · `toolu_019jcCFoSJLag58su3VWKJZm`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/related_work_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "46da8801-1a9c-4f3b-9cc8-239a438c6439",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/related_work_draft.md",
    "content": "# Section 2: Related Work\n\n## 2.1 Schema Decomposition for Information Extraction\n\nHandling large type schemas has emerged as a key challenge for LLM-based IE. Several strategies have been proposed to reduce schema complexity at inference time.\n\n**Per-type and fixed decomposition.** UniversalNER \\cite{uniner-2024} distills ChatGPT into a compact model by targeting one entity type per extraction call, reporting +7 F1 over ChatGPT on 43 datasets. While effective, per-type splitting sacrifices cross-type context and incurs $O(N)$ inference cost, with no principled criterion for when decomposition is necessary. KGGen \\cite{kggen-2025} employs a two-stage pipeline --- entity extraction followed by relation extraction --- which decomposes at the *task* level rather than within the type schema. Similarly, DEE \\cite{dee-2024} separates event detection from argument extraction with dynamic schema-aware retrieval, but does not address intra-task type partitioning.\n\n**Similarity-based partitioning.** LLM-PEE \\cite{llm-pee-2025} partitions massive event type schemas via similarity-based recall, assigning types to groups that reduce prompt length. This achieves +5.4\\% event detection F1 over zero-shot baselines. However, LLM-PEE uses type similarity as an implicit proxy without empirically validating that similarity drives extraction errors --- the partition criterion optimizes for coverage, not confusability reduction.\n\n**Schema rewriting and tool-based approaches.** PARSE \\cite{parse-2025} uses an LLM to autonomously rewrite JSON schemas for better LLM consumption (+64.7\\% on SWDE), treating schema optimization as a black-box process without modeling type interactions. SPT \\cite{spt-2025} reframes schemas as parameterized tools for LLM tool-calling, offering a novel interface but not addressing why certain type configurations degrade extraction. DLISC \\cite{dlisc-2025} introduces dual-LoRA with incremental schema caching for on-device efficiency, orthogonal to our focus on type confusability.\n\n**Our distinction.** Unlike all prior decomposition methods, SDGD is grounded in an empirically validated degradation model: we first demonstrate that type confusability independently predicts extraction failure (controlling for count), then operationalize this finding into a graph-coloring-based decomposition that *provably* separates highly confusable types. No prior work explicitly isolates confusability from count as a degradation factor, nor optimizes decomposition to minimize it.\n\n\n## 2.2 Confusability-Aware Approaches in NLP\n\nThe notion that semantically similar labels cause classification errors has appeared across NLP, though not in the context of training-free LLM IE schema design.\n\n**Label confusion in training.** IEPile \\cite{iepile-2024} constructs hard negative schemas --- semantically proximate type sets --- during *training* to improve a model's type discrimination ability. This confirms that confusable schemas are harder, but the intervention is at training time. Our work addresses *inference-time* confusability for training-free systems where model weights are frozen. The Familiarity metric \\cite{familiarity-2025} quantifies label shift between synthetic training data and evaluation sets, revealing that zero-shot NER scores are overestimated when training labels overlap with evaluation labels. This measures *evaluation bias* from label similarity, not extraction-time confusion --- but supports our premise that type similarity is a meaningful confound.\n\n**Multi-agent debate for type resolution.** CROSSAGENTIE \\cite{crossagentie-2025} deploys cross-type debate within multi-agent systems to resolve entity-label conflicts: when an entity is assigned conflicting types by different agents, intra-group debate adjudicates. This *reactively* addresses type confusion after it occurs. CMAS-NER \\cite{cmas-ner-2025} similarly uses cooperative multi-agent collective intelligence to overcome context correlation and indiscriminate demonstration problems in zero-shot NER. Our approach is *proactive*: we prevent type confusion by ensuring highly confusable types never co-occur in a single extraction call. The two strategies are complementary --- SDGD decomposition could serve as a pre-processing stage for multi-agent systems.\n\n**Positional and attention effects.** Liu et al. \\cite{lost-in-middle-2024} demonstrate that LLMs degrade when relevant information appears in the middle of long contexts, exhibiting U-shaped attention patterns. While not IE-specific, this provides additional motivation for schema decomposition: shorter prompts with fewer types reduce the risk of attention-related information loss. To our knowledge, no prior work has connected positional attention biases to IE schema prompt design.\n\n\n## 2.3 LLM-Based Information Extraction\n\nTraining-free LLM IE has progressed rapidly, establishing both the opportunity and the challenge that motivate our work.\n\n**Instruction-tuned IE models.** GoLLIE \\cite{gollie-2024} demonstrates that code-style schema definitions with annotation guideline following enable strong zero-shot IE from a Code-LLaMA backbone. Code4UIE \\cite{code4uie-2024} extends this to retrieval-augmented code generation for universal IE. KnowCoder \\cite{knowcoder-2024} encodes schema knowledge via code structures into LLMs. These models internalize schema understanding through fine-tuning, sidestepping inference-time schema complexity. However, they require task-specific training, limiting deployment flexibility.\n\n**Zero-shot extraction methods.** Self-improving NER \\cite{self-improve-ner-2024} generates synthetic examples via LLM self-prompting, while ReasoningNER \\cite{reasoning-ner-2025} applies chain-of-thought reasoning to achieve +12.3 F1 over GPT-4 in zero-shot settings. ZeroNER \\cite{zeroner-2025} leverages entity type descriptions to produce LLM supervision for a BERT student model (+16\\% F1 over LLMs on hard zero-shot). These methods improve extraction within a fixed schema presentation, but do not address how schema *structure* --- the composition and similarity of co-presented types --- affects quality.\n\n**Compact and efficient models.** GLiNER \\cite{gliner-2024} achieves competitive zero-shot NER with a bidirectional encoder via parallel entity extraction, and GLiNER2 \\cite{gliner2-2025} extends this to multi-task IE. NuNER \\cite{nuner-2024} uses contrastive pre-training on LLM-annotated data for strong few-shot performance. These non-LLM alternatives avoid schema complexity issues by design (parallel per-type extraction), but sacrifice the generality and zero-shot flexibility of LLM-based approaches.\n\n**Surveys.** Xu et al. \\cite{llm4ie-survey-2024} provide a comprehensive survey of LLM-based generative IE, covering prompting strategies, fine-tuning paradigms, and benchmarks. Our work contributes to the prompting strategy dimension by showing that *what types are co-presented* matters as much as *how they are presented*.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Write · `toolu_01XrEfLaMXGgrVjqMaUTyrYo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/maven_description.md",
  "content": "# MAVEN Dataset Description\n\n*(For inclusion in Section 4: Experimental Setup, dataset description subsection)*\n\n**MAVEN** \\cite{wang-etal-2020-maven} is a large-scale event detection benchmark constructed from 4,480 English Wikipedia documents. It defines 168 event types organized in a hierarchical taxonomy derived from FrameNet, with 118,732 annotated event mention instances. The type space is substantially larger than prior event detection datasets (e.g., ACE05 with 33 types) and exhibits pronounced sibling-type confusability: Wang et al. report that 14.6--19.8\\% of inter-annotator disagreements involve sibling types in the hierarchy (Table 7 of the original paper), confirming that structurally adjacent event types are inherently difficult to distinguish even for human annotators. We select MAVEN for cross-task validation for three reasons: (1) it provides a *different IE task* (event detection vs. NER), testing whether confusability-aware decomposition generalizes beyond entity extraction; (2) its 168-type schema is 2.5$\\times$ larger than Few-NERD's 66 fine-grained types, stress-testing SDGD on a more complex schema; and (3) independently documented confusability evidence (sibling confusion rates) enables external validation of our Schema Confusability Score against human judgment.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "1d721002-fb6c-4f37-a6e3-85e3aa221d9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MLWbU4BGDu6u2zHLtWf9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 128,
      "cache_read_input_tokens": 38919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 128
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

_source line 25 · 2026-05-15T03:55:56.761Z_

<details><summary>↩ Tool result · `toolu_01XrEfLaMXGgrVjqMaUTyrYo`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/maven_description.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "76891b9a-63e0-4234-98b7-594aaa6ca46e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/maven_description.md",
    "content": "# MAVEN Dataset Description\n\n*(For inclusion in Section 4: Experimental Setup, dataset description subsection)*\n\n**MAVEN** \\cite{wang-etal-2020-maven} is a large-scale event detection benchmark constructed from 4,480 English Wikipedia documents. It defines 168 event types organized in a hierarchical taxonomy derived from FrameNet, with 118,732 annotated event mention instances. The type space is substantially larger than prior event detection datasets (e.g., ACE05 with 33 types) and exhibits pronounced sibling-type confusability: Wang et al. report that 14.6--19.8\\% of inter-annotator disagreements involve sibling types in the hierarchy (Table 7 of the original paper), confirming that structurally adjacent event types are inherently difficult to distinguish even for human annotators. We select MAVEN for cross-task validation for three reasons: (1) it provides a *different IE task* (event detection vs. NER), testing whether confusability-aware decomposition generalizes beyond entity extraction; (2) its 168-type schema is 2.5$\\times$ larger than Few-NERD's 66 fine-grained types, stress-testing SDGD on a more complex schema; and (3) independently documented confusability evidence (sibling confusion rates) enables external validation of our Schema Confusability Score against human judgment.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 26_

三个文件已写入。注册 artifacts。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "6c93e439-2339-462a-bc4c-58606b9dd811",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNThVjW1P8gHduwJVfEstk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6205,
      "cache_read_input_tokens": 39047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6205
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01HWcK1jhr6CAKcvsyz1yej6`</summary>

```json
{
  "name": "Method Section Framework",
  "type": "paper",
  "description": "Paper Section 3 (Method) draft: Problem Formulation, Controlled Experiment Design, SDGD Framework with LaTeX pseudocode, SDGD-zero vs SDGD-cal variants, adaptive threshold strategy",
  "project": "schema-dag-extraction",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/method_framework.md",
  "tags": [
    "paper",
    "method",
    "EMNLP2026"
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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "9b94e920-3fc3-4f57-a3db-fe4d737e2773",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNThVjW1P8gHduwJVfEstk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6205,
      "cache_read_input_tokens": 39047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6205
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

_source line 28 · 2026-05-15T03:56:04.403Z_

<details><summary>↩ Tool result · `toolu_01HWcK1jhr6CAKcvsyz1yej6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_bf91f7\", \"name\": \"Method Section Framework\", \"type\": \"paper\", \"description\": \"Paper Section 3 (Method) draft: Problem Formulation, Controlled Experiment Design, SDGD Framework with LaTeX pseudocode, SDGD-zero vs SDGD-cal variants, adaptive threshold strategy\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/paper/method_framework.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T03:56:04.372109+00:00\", \"tags\": [\"paper\", \"method\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "0c00a57d-ae17-456a-ae82-90171261da96",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_bf91f7\\\", \\\"name\\\": \\\"Method Section Framework\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Paper Section 3 (Method) draft: Problem Formulation, Controlled Experiment Design, SDGD Framework with LaTeX pseudocode, SDGD-zero vs SDGD-cal variants, adaptive threshold strategy\\\", \\\"path\\\": \\\"projects/schema-dag-extraction/artifacts/_project/paper/method_framework.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema-dag-extraction\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T03:56:04.372109+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"EMNLP2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_bf91f7\", \"name\": \"Method Section Framework\", \"type\": \"paper\", \"description\": \"Paper Section 3 (Method) draft: Problem Formulation, Controlled Experiment Design, SDGD Framework with LaTeX pseudocode, SDGD-zero vs SDGD-cal variants, adaptive threshold strategy\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/paper/method_framework.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T03:56:04.372109+00:00\", \"tags\": [\"paper\", \"method\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_018MStp3YwcQdHCN78eeFHG4`</summary>

```json
{
  "name": "Related Work Draft",
  "type": "paper",
  "description": "Paper Section 2 (Related Work) draft: Schema Decomposition for IE, Confusability-Aware NLP, LLM-Based IE — covers 25 papers across 3 dimensions",
  "project": "schema-dag-extraction",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/related_work_draft.md",
  "tags": [
    "paper",
    "related-work",
    "EMNLP2026"
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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "3e76ae59-82fe-48df-b73e-56806ee3ab16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNThVjW1P8gHduwJVfEstk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6205,
      "cache_read_input_tokens": 39047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6205
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

_source line 30 · 2026-05-15T03:56:06.760Z_

<details><summary>↩ Tool result · `toolu_018MStp3YwcQdHCN78eeFHG4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_4f948b\", \"name\": \"Related Work Draft\", \"type\": \"paper\", \"description\": \"Paper Section 2 (Related Work) draft: Schema Decomposition for IE, Confusability-Aware NLP, LLM-Based IE — covers 25 papers across 3 dimensions\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/paper/related_work_draft.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T03:56:06.727328+00:00\", \"tags\": [\"paper\", \"related-work\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "940321dd-d7b7-4932-b38e-b720aaea2e78",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_4f948b\\\", \\\"name\\\": \\\"Related Work Draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Paper Section 2 (Related Work) draft: Schema Decomposition for IE, Confusability-Aware NLP, LLM-Based IE — covers 25 papers across 3 dimensions\\\", \\\"path\\\": \\\"projects/schema-dag-extraction/artifacts/_project/paper/related_work_draft.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema-dag-extraction\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T03:56:06.727328+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"EMNLP2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_4f948b\", \"name\": \"Related Work Draft\", \"type\": \"paper\", \"description\": \"Paper Section 2 (Related Work) draft: Schema Decomposition for IE, Confusability-Aware NLP, LLM-Based IE — covers 25 papers across 3 dimensions\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/paper/related_work_draft.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T03:56:06.727328+00:00\", \"tags\": [\"paper\", \"related-work\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01AFN1kbHpi35qvY8gLxUGyL`</summary>

```json
{
  "name": "MAVEN Dataset Description",
  "type": "paper",
  "description": "MAVEN dataset description paragraph (~150 words) for Experimental Setup section: 168 event types, 4480 docs, sibling confusion evidence, cross-task validation rationale",
  "project": "schema-dag-extraction",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/paper_drafts/maven_description.md",
  "tags": [
    "paper",
    "dataset",
    "MAVEN",
    "EMNLP2026"
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
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "aa9b12f3-a18e-4b4a-8300-d2bee4084c2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNThVjW1P8gHduwJVfEstk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6205,
      "cache_read_input_tokens": 39047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6205
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

_source line 32 · 2026-05-15T03:56:09.381Z_

<details><summary>↩ Tool result · `toolu_01AFN1kbHpi35qvY8gLxUGyL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_b7191f\", \"name\": \"MAVEN Dataset Description\", \"type\": \"paper\", \"description\": \"MAVEN dataset description paragraph (~150 words) for Experimental Setup section: 168 event types, 4480 docs, sibling confusion evidence, cross-task validation rationale\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/paper/maven_description.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T03:56:09.350124+00:00\", \"tags\": [\"paper\", \"dataset\", \"MAVEN\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "4cfdb44c-9ac2-4e16-a238-da106d238a57",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_b7191f\\\", \\\"name\\\": \\\"MAVEN Dataset Description\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"MAVEN dataset description paragraph (~150 words) for Experimental Setup section: 168 event types, 4480 docs, sibling confusion evidence, cross-task validation rationale\\\", \\\"path\\\": \\\"projects/schema-dag-extraction/artifacts/_project/paper/maven_description.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema-dag-extraction\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T03:56:09.350124+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"dataset\\\", \\\"MAVEN\\\", \\\"EMNLP2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_b7191f\", \"name\": \"MAVEN Dataset Description\", \"type\": \"paper\", \"description\": \"MAVEN dataset description paragraph (~150 words) for Experimental Setup section: 168 event types, 4480 docs, sibling confusion evidence, cross-task validation rationale\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/paper/maven_description.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T03:56:09.350124+00:00\", \"tags\": [\"paper\", \"dataset\", \"MAVEN\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

三个文件已完成并注册：

**`method_framework.md`** — Section 3 完整框架：
- 3.1 Problem Formulation: 定义 SCS、BCS、schema complexity 双因子模型
- 3.2 Controlled Experiment Design: count curve + within-count BCS correlation + multi-channel degradation模型（count→recall, confusability→precision）
- 3.3 SDGD Framework: 5 步算法描述 + `\begin{algorithm}` 格式伪代码 + adaptive threshold（$\tau = \mu + k_\sigma \cdot \sigma$）+ oracle baseline 区分 + 复杂度分析
- 3.4 SDGD-zero vs SDGD-cal: 两个变体的数据需求、信号来源、校准流程、对比表

**`related_work_draft.md`** — Section 2 三维度组织：
- 2.1 Schema Decomposition for IE: UniNER, LLM-PEE, PARSE, KGGen, DEE, SPT, DLISC（7篇），明确 SDGD 与每个方法的区别
- 2.2 Confusability-Aware NLP: IEPile（训练时 vs 推理时）、Familiarity（评估偏差 vs 提取混淆）、CROSSAGENTIE/CMAS（reactive debate vs proactive decomposition）、Lost-in-the-Middle
- 2.3 LLM-Based IE: GoLLIE, Code4UIE, KnowCoder, Self-improving NER, ReasoningNER, ZeroNER, GLiNER/GLiNER2, NuNER, survey

**`maven_description.md`** — 1 段约 150 words：168 types、FrameNet hierarchy、4480 docs、118K mentions、sibling confusion 14.6-19.8%、三个选择理由（cross-task, larger schema, external confusability evidence）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "uuid": "e6ada282-a897-41bb-9c3a-b9fb12c185df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBX8CWepczBdABEhgQh5jV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 45252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 34_

三个文件已完成并注册：

**`method_framework.md`** — Section 3 完整框架：
- 3.1 Problem Formulation: 定义 SCS、BCS、schema complexity 双因子模型
- 3.2 Controlled Experiment Design: count curve + within-count BCS correlation + multi-channel degradation模型（count→recall, confusability→precision）
- 3.3 SDGD Framework: 5 步算法描述 + `\begin{algorithm}` 格式伪代码 + adaptive threshold（$\tau = \mu + k_\sigma \cdot \sigma$）+ oracle baseline 区分 + 复杂度分析
- 3.4 SDGD-zero vs SDGD-cal: 两个变体的数据需求、信号来源、校准流程、对比表

**`related_work_draft.md`** — Section 2 三维度组织：
- 2.1 Schema Decomposition for IE: UniNER, LLM-PEE, PARSE, KGGen, DEE, SPT, DLISC（7篇），明确 SDGD 与每个方法的区别
- 2.2 Confusability-Aware NLP: IEPile（训练时 vs 推理时）、Familiarity（评估偏差 vs 提取混淆）、CROSSAGENTIE/CMAS（reactive debate vs proactive decomposition）、Lost-in-the-Middle
- 2.3 LLM-Based IE: GoLLIE, Code4UIE, KnowCoder, Self-improving NER, ReasoningNER, ZeroNER, GLiNER/GLiNER2, NuNER, survey

**`maven_description.md`** — 1 段约 150 words：168 types、FrameNet hierarchy、4480 docs、118K mentions、sibling confusion 14.6-19.8%、三个选择理由（cross-task, larger schema, external confusability evidence）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 183789,
  "duration_api_ms": 184674,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "99d96655-9a5b-476e-8601-5e375e4657c9",
  "total_cost_usd": 0.53000175,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 35091,
    "cache_read_input_tokens": 221952,
    "output_tokens": 7924,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35091,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 529,
        "cache_read_input_tokens": 45252,
        "cache_creation_input_tokens": 1680,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1680
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1462,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001557,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 7924,
      "cacheReadInputTokens": 221952,
      "cacheCreationInputTokens": 35091,
      "webSearchRequests": 0,
      "costUSD": 0.52844475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d98a08be-0933-4ccd-9ac2-8ef9be32b2ee"
}
```

</details>

---
