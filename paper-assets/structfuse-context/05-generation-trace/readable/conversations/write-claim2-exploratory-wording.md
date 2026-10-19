# write claim2 exploratory wording

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_write_claim2-exploratory-wording_20260515T055558.jsonl`
- **Structured JSON:** [`2e0fc999f5d0358eed00.json`](../../sessions/2e/2e0fc999f5d0358eed00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-15T05:59:28.436587+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T05:59:28.436956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T05:59:28.437123+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T05:59:28.437381+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, n
…[truncated 11467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T05:59:28.437623+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes",
  "new_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes",
    "new_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T05:59:28.437786+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T05:59:28.437922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T05:59:28.438115+00:00_

1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, 
…[truncated 11273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T05:59:28.438289+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes",
  "new_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes",
    "new_string": "(2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T05:59:28.438455+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T05:59:28.438584+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison",
  "new_string": "neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison",
    "new_string": "neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T05:59:28.438775+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T05:59:28.438901+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "margin differential explains strategy interaction",
  "new_string": "margin differential is consistent with hypothesized strategy interaction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "margin differential explains strategy interaction",
    "new_string": "margin differential is consistent with hypothesized strategy interaction"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T05:59:28.439055+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T05:59:28.439173+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)",
  "new_string": "m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)",
    "new_string": "m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T05:59:28.439325+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T05:59:28.439447+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only",
  "new_string": "plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only",
    "new_string": "plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T05:59:28.439616+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T05:59:28.439749+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "representation geometry analysis explains prior contradictions\"",
  "new_string": "representation geometry analysis may help explain prior contradictions\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "representation geometry analysis explains prior contradictions\"",
    "new_string": "representation geometry analysis may help explain prior contradictions\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T05:59:28.439901+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T05:59:28.440038+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "provides mechanistic explanation for strategy × encoder interaction",
  "new_string": "offers preliminary mechanistic analysis of strategy × encoder interaction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "provides mechanistic explanation for strategy × encoder interaction",
    "new_string": "offers preliminary mechanistic analysis of strategy × encoder interaction"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T05:59:28.440206+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T05:59:28.440344+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "provides mechanistic evidence for this interaction",
  "new_string": "offers preliminary mechanistic evidence for this interaction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "provides mechanistic evidence for this interaction",
    "new_string": "offers preliminary mechanistic evidence for this interaction"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T05:59:28.440501+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T05:59:28.440669+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T05:59:28.440793+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T05:59:28.440906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T05:59:28.441087+00:00_

1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables t
…[truncated 11377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T05:59:28.441276+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective.",
  "new_string": "representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "old_string": "representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective.",
    "new_string": "representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T05:59:28.441441+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T05:59:28.441577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T05:59:28.441779+00:00_

1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables t
…[truncated 11375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T05:59:28.441958+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper challenges a prevalent assumption + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\"\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \"challenging gradient-based assumption\" narrative needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "paper_framing.md",
    "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper challenges a prevalent assumption + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\"\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \"challenging gradient-based assumption\" narrative needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T05:59:28.442225+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-15T05:59:28.442392+00:00_

完成。共修改 9 处 Claim 2 相关断言式表述：

| 位置 | 原文 | 修改后 |
|------|------|--------|
| Core Claims #2 | provides mechanistic evidence | offers preliminary mechanistic evidence |
| Story Spine - Our contribution | provide mechanistic analysis ... yield different outcomes | offer preliminary mechanistic analysis ... may yield different outcomes |
| Headline result template | provides a candidate mechanistic explanation | offers a candidate mechanistic explanation |
| Dual-Pillar Secondary | provides explanatory depth | offers preliminary explanatory depth |
| Venue Fit #3 | provides mechanistic explanation | offers preliminary mechanistic analysis |
| Evidence - D021 | explains strategy interaction | is consistent with hypothesized strategy interaction |
| Evidence - m2_embed_verify | confirms ranking | is consistent with pilot ranking |
| Evidence - plan_013 | Confirms cross-encoder pattern ... dataflow helps Qwen only | Consistent with cross-encoder pattern ... dataflow appears to help Qwen only |
| Contingency | explains prior contradictions | may help explain prior contradictions |

Claim 1、Claim 3 的断言式表述均未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_write_claim2-exploratory-wording_20260515T055558"
}
```

</details>

---
