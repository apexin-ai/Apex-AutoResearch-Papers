# research crossing rate literature

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_research_crossing_rate_literature_20260520T045810.jsonl`
- **Structured JSON:** [`0a0216d2522c1087102a.json`](../../sessions/0a/0a0216d2522c1087102a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-20T05:09:47.882779+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T05:09:47.883130+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T05:09:47.883330+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Direction 1: CR in probe eval",
  "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers that use \"crossing rate\" or equivalent concepts (sign change rate, prediction flip rate, label oscillation) in the context of neural network probes or classifiers.\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"crossing rate\" safety probe\n2. \"sign change rate\" classifier prediction\n3. \"prediction flip\" neural network probe\n4. \"label oscillation\" hidden state probe\n5. \"crossing rate\" probing classifier\n6. \"prediction instability\" probe layer\n7. \"zero crossing rate\" signal processing classifier (this is a known signal processing concept - check if anyone applied it to ML probes)\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they use the concept\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2020-2026 papers. Be thorough - try at least 5-6 different keyword combinations.\n\nReturn a structured report with all findings, clearly separating:\n- Direct hits (exact \"crossing rate\" or equivalent in probe/classifier context)\n- Near hits (similar stability concepts applied to probes)\n- Related but different\n\nDo NOT fabricate any papers. Only report what you actually find in search results.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "tool_args": {
    "description": "Direction 1: CR in probe eval",
    "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers that use \"crossing rate\" or equivalent concepts (sign change rate, prediction flip rate, label oscillation) in the context of neural network probes or classifiers.\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"crossing rate\" safety probe\n2. \"sign change rate\" classifier prediction\n3. \"prediction flip\" neural network probe\n4. \"label oscillation\" hidden state probe\n5. \"crossing rate\" probing classifier\n6. \"prediction instability\" probe layer\n7. \"zero crossing rate\" signal processing classifier (this is a known signal processing concept - check if anyone applied it to ML probes)\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they use the concept\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2020-2026 papers. Be thorough - try at least 5-6 different keyword combinations.\n\nReturn a structured report with all findings, clearly separating:\n- Direct hits (exact \"crossing rate\" or equivalent in probe/classifier context)\n- Near hits (similar stability concepts applied to probes)\n- Related but different\n\nDo NOT fabricate any papers. Only report what you actually find in search results.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T05:09:47.883512+00:00_

Async agent launched successfully.
agentId: a1f190173f7faefc4 (internal ID - do not mention to user. Use SendMessage with to: 'a1f190173f7faefc4' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/9800489a-70d1-4b55-953c-73d78628b0a5/tasks/a1f190173f7faefc4.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T05:09:47.883688+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Direction 2: Composite metrics",
  "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers that use composite metrics combining accuracy and stability (like our \"CR-composite = Balanced Accuracy × Crossing Rate\") in safety monitoring or detection contexts.\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"composite metric\" safety monitoring online detection\n2. \"balanced accuracy\" \"prediction stability\" combination metric\n3. \"accuracy stability tradeoff\" safety classifier\n4. \"detection reliability\" \"prediction consistency\" metric\n5. \"accuracy\" \"stability\" composite score safety\n6. \"multi-criteria\" metric safety detection probe\n7. \"joint metric\" accuracy consistency classifier\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they combine accuracy with stability/consistency\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2020-2026 papers. Be thorough.\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "tool_args": {
    "description": "Direction 2: Composite metrics",
    "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers that use composite metrics combining accuracy and stability (like our \"CR-composite = Balanced Accuracy × Crossing Rate\") in safety monitoring or detection contexts.\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"composite metric\" safety monitoring online detection\n2. \"balanced accuracy\" \"prediction stability\" combination metric\n3. \"accuracy stability tradeoff\" safety classifier\n4. \"detection reliability\" \"prediction consistency\" metric\n5. \"accuracy\" \"stability\" composite score safety\n6. \"multi-criteria\" metric safety detection probe\n7. \"joint metric\" accuracy consistency classifier\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they combine accuracy with stability/consistency\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2020-2026 papers. Be thorough.\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T05:09:47.883871+00:00_

Async agent launched successfully.
agentId: ac69d20385a2e770a (internal ID - do not mention to user. Use SendMessage with to: 'ac69d20385a2e770a' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/9800489a-70d1-4b55-953c-73d78628b0a5/tasks/ac69d20385a2e770a.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T05:09:47.884029+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Direction 3: SafeSwitch + online safety",
  "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers about online/real-time safety detection systems that monitor LLM hidden states during generation, especially anything like \"SafeSwitch\".\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. SafeSwitch safety detection language model\n2. \"online safety monitoring\" language model probe\n3. \"real-time safety\" hidden state detection LLM\n4. \"safety classifier\" \"during generation\" reasoning\n5. \"latent safety\" monitor language model\n6. \"internal safety monitor\" LLM hidden states\n7. \"safety probe\" \"token by token\" OR \"step by step\" generation\n8. \"runtime safety\" probe hidden representation\n\nFor each search, note:\n- Paper title, authors, venue, year  \n- How they do online/runtime safety monitoring\n- Whether they discuss prediction stability or consistency across generation steps\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2023-2026 papers (this is a recent research direction). Be thorough.\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "tool_args": {
    "description": "Direction 3: SafeSwitch + online safety",
    "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers about online/real-time safety detection systems that monitor LLM hidden states during generation, especially anything like \"SafeSwitch\".\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. SafeSwitch safety detection language model\n2. \"online safety monitoring\" language model probe\n3. \"real-time safety\" hidden state detection LLM\n4. \"safety classifier\" \"during generation\" reasoning\n5. \"latent safety\" monitor language model\n6. \"internal safety monitor\" LLM hidden states\n7. \"safety probe\" \"token by token\" OR \"step by step\" generation\n8. \"runtime safety\" probe hidden representation\n\nFor each search, note:\n- Paper title, authors, venue, year  \n- How they do online/runtime safety monitoring\n- Whether they discuss prediction stability or consistency across generation steps\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2023-2026 papers (this is a recent research direction). Be thorough.\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T05:09:47.884190+00:00_

Async agent launched successfully.
agentId: aee73b0493242e7a7 (internal ID - do not mention to user. Use SendMessage with to: 'aee73b0493242e7a7' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/9800489a-70d1-4b55-953c-73d78628b0a5/tasks/aee73b0493242e7a7.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T05:09:47.884421+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Direction 4: Layer selection stability",
  "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers about layer selection for probing classifiers that use stability or consistency as a criterion (not just accuracy).\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"layer selection\" probing \"prediction stability\"\n2. \"optimal layer\" probe \"consistency\" neural network\n3. probing layer selection criterion stability robustness\n4. \"which layer\" probe evaluation robustness consistency\n5. \"layer-wise\" probing stability prediction\n6. \"probe accuracy\" varies across layers instability\n7. \"BERTology\" probing layer selection\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they select layers for probing\n- Whether they consider any stability/consistency metric beyond accuracy\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2019-2026 papers (probing has been studied since BERT era). Be thorough.\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "tool_args": {
    "description": "Direction 4: Layer selection stability",
    "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers about layer selection for probing classifiers that use stability or consistency as a criterion (not just accuracy).\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"layer selection\" probing \"prediction stability\"\n2. \"optimal layer\" probe \"consistency\" neural network\n3. probing layer selection criterion stability robustness\n4. \"which layer\" probe evaluation robustness consistency\n5. \"layer-wise\" probing stability prediction\n6. \"probe accuracy\" varies across layers instability\n7. \"BERTology\" probing layer selection\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they select layers for probing\n- Whether they consider any stability/consistency metric beyond accuracy\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2019-2026 papers (probing has been studied since BERT era). Be thorough.\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T05:09:47.884632+00:00_

Async agent launched successfully.
agentId: ac20f2fa62f0de4b4 (internal ID - do not mention to user. Use SendMessage with to: 'ac20f2fa62f0de4b4' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/9800489a-70d1-4b55-953c-73d78628b0a5/tasks/ac20f2fa62f0de4b4.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T05:09:47.884830+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Direction 5: Temporal consistency",
  "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers about prediction consistency / temporal consistency in sequential monitoring or classification, especially in safety-related contexts.\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"prediction consistency\" sequential monitoring classifier\n2. \"temporal consistency\" classifier safety detection\n3. \"prediction agreement\" across timesteps probe\n4. \"commitment detection\" language model safety\n5. \"prediction stability\" across tokens language model\n6. \"consistent prediction\" safety probe reasoning\n7. \"early exit\" \"prediction consistency\" neural network\n8. \"calibration\" \"safety probe\" prediction stability\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they measure prediction consistency over time/sequence\n- Whether they relate this to safety or reliability\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2020-2026 papers. Be thorough.\n\nAlso specifically search for:\n- \"early exit\" prediction confidence consistency (early exit literature often uses prediction consistency to decide when to stop)\n- \"calibration\" safety probe (calibration literature may discuss prediction stability)\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "tool_args": {
    "description": "Direction 5: Temporal consistency",
    "prompt": "You are conducting a literature survey for an ML safety paper. We need to find papers about prediction consistency / temporal consistency in sequential monitoring or classification, especially in safety-related contexts.\n\nUse WebSearch to search for papers, then WebFetch to verify findings. Search these keyword combinations:\n\n1. \"prediction consistency\" sequential monitoring classifier\n2. \"temporal consistency\" classifier safety detection\n3. \"prediction agreement\" across timesteps probe\n4. \"commitment detection\" language model safety\n5. \"prediction stability\" across tokens language model\n6. \"consistent prediction\" safety probe reasoning\n7. \"early exit\" \"prediction consistency\" neural network\n8. \"calibration\" \"safety probe\" prediction stability\n\nFor each search, note:\n- Paper title, authors, venue, year\n- How they measure prediction consistency over time/sequence\n- Whether they relate this to safety or reliability\n- Key quotes if available\n\nUse WebFetch on any promising arxiv/paper links to get abstracts and confirm relevance.\n\nFocus on 2020-2026 papers. Be thorough.\n\nAlso specifically search for:\n- \"early exit\" prediction confidence consistency (early exit literature often uses prediction consistency to decide when to stop)\n- \"calibration\" safety probe (calibration literature may discuss prediction stability)\n\nReturn a structured report with all findings. Do NOT fabricate any papers - only report what you actually find.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T05:09:47.885004+00:00_

Async agent launched successfully.
agentId: a9772788c4ea55d19 (internal ID - do not mention to user. Use SendMessage with to: 'a9772788c4ea55d19' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/9800489a-70d1-4b55-953c-73d78628b0a5/tasks/a9772788c4ea55d19.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T05:09:47.885199+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/ 2>/dev/null | head -20",
  "description": "Check existing artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/ 2>/dev/null | head -20",
    "description": "Check existing artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T05:09:47.885329+00:00_

E-R11-1
_project
advbench_preliminary
ai_writing_audit.md
api_key_fallback_eval.md
bib_author_fix.txt
camera_ready_precheck.md
citation_audit.md
citation_audit_round4.md
code_reusability_assessment.md
commitment_point_analysis.md
data_exploration_report.md
diag_d1_layer_sweep
diag_d2_pca_viz
dream_reports
e5_mistral_comparison
e5_mistral_comparison_v2
e5_mistral_comparison_v2_report.txt
exp-007
exp_001a

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:09:47.885512+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T05:09:47.885652+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:09:47.885859+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'in_progress', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'in_progress', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'in_progress', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'in_progress', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'in_progress', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'in_progress', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'in_progress', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'in_progress', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:09:47.886081+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:09:47.888107+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'in_progress', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'in_progress', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'in_progress', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'in_progress', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'in_progress', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'in_progress', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T05:09:47.888621+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T05:09:47.888886+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'in_progress', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'in_progress', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T05:09:47.889067+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T05:09:47.889291+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'in_progress', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'pending', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T05:09:47.889470+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:09:47.889654+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'completed', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'in_progress', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'completed', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'in_progress', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'pending', 'activeForm': 'Compiling final literature survey report'}]"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T05:09:47.889836+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:09:47.889981+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"zero crossing rate\" applied to neural network predictions classification stability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"zero crossing rate\" applied to neural network predictions classification stability"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T05:09:47.890108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"prediction flip rate\" OR \"decision flip rate\" neural network probe safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"prediction flip rate\" OR \"decision flip rate\" neural network probe safety"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T05:09:47.890234+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"overthinking\" early exit prediction changes intermediate layers transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"overthinking\" early exit prediction changes intermediate layers transformer"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T05:09:47.890377+00:00_

Web search results for query: ""zero crossing rate" applied to neural network predictions classification stability"

Links: [{"title":"Zero Crossing Rate - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/engineering/zero-crossing-rate"},{"title":"Zero-crossing rate method as an efficient tool for combustion instability diagnosis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0894177720308384"},{"title":"Stock Price Range Forecast via a Recurrent Neural Network Based on the Zero-Crossing Rate Approach | Request PDF","url":"https://www.researchgate.net/publication/334427641_Stock_Price_Range_Forecast_via_a_Recurrent_Neural_Network_Based_on_the_Zero-Crossing_Rate_Approach"},{"title":"Feature Selection Methods for Zero-Shot Learning of Neural Activity","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5481359/"},{"title":"Protein Mutation Stability Ternary Classification using Neural Networks   and Rigidity Analysis","url":"https://arxiv.org/pdf/1803.04659"},{"title":"Musical Instrument Recognition using Zero Crossing Rate ...","url":"https://research.ijais.org/volume1/number3/ijais12-450131.pdf"}]

Based on the web search results, I found information about zero crossing rate (ZCR) applications in various domains, though the results don't specifically focus on ZCR applied to neural network predictions for classification stability.

Here's what the search revealed:

**Zero Crossing Rate in General Applications:**

Zero-crossing rate (ZCR) denotes the ratio of changes in the sign within a specific time interval. This metric has been used across different fields:

1. **Medical Applications**: Zero crossing rate (ZCR) and Spectral roll off (SR) increase the diagnostic accuracy in diagnosis of Alzheimer's disease.

2. **Stock Market Prediction**: A Recurrent Neural Network (RNN) approach has been used to forecast stock prices, with emphasis on characteristics of the stock data such as the zero-crossing rate (Z
…[truncated 766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T05:09:47.890551+00:00_

Web search results for query: ""overthinking" early exit prediction changes intermediate layers transformer"

Links: [{"title":"Fast and Robust Vision Language Models with Early Exits","url":"https://aclanthology.org/2025.findings-acl.1209.pdf"},{"title":"ADEPT: ADAPTIVE DYNAMIC EARLY-EXIT PROCESS FOR TRANSFORMERS Sangmin Yoo∗","url":"https://www.arxiv.org/pdf/2601.03700"},{"title":"LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding","url":"https://arxiv.org/pdf/2404.16710"},{"title":"A transformer architecture alteration to incentivise externalised reasoning","url":"https://arxiv.org/pdf/2603.21376"},{"title":"ADEPT: Adaptive Dynamic Early-Exit Process for Transformers","url":"https://arxiv.org/html/2601.03700"},{"title":"The Diminishing Returns of Early-Exit Decoding in Modern LLMs","url":"https://arxiv.org/pdf/2603.23701"},{"title":"BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://cseweb.ucsd.edu/~jmcauley/pdfs/nips20.pdf"},{"title":"Early-Exit LLMs: Adaptive Inference","url":"https://www.emergentmind.com/topics/early-exit-large-language-models"}]

Based on the search results, I found relevant information about "overthinking" in transformers and how intermediate layers change predictions:

## Overthinking in Transformers

"Overthinking" (also called analysis paralysis) occurs during inference when early layers capture sufficient information for proper predictions, but the quality of information is only marginally improved throughout the following layers, resulting in poor cost-effectiveness.

## Intermediate Layers Changing Predictions

Intermediate layers are sometimes hesitant and "change their minds" - for example, a token was predicting one value as early as Layer 07, but changed its mind between Layer 22 and Layer 26, before settling again on the original prediction.

## Early-Exit Solutions

The search results reveal several approaches to address this issue:

1. **PABEE (Patience-based Early Exit)**: This me
…[truncated 838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T05:09:47.890753+00:00_

Web search results for query: ""prediction flip rate" OR "decision flip rate" neural network probe safety"

Links: [{"title":"Prediction for Future Yaw Rate Values of Vehicles Using Long Short-Term Memory Network","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10303885/"},{"title":"Predicting Safety Solutions via an Artificial Neural Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405896319326606"},{"title":"A Survey of Bit-Flip Attacks on Deep Neural Network and Corresponding Defense Methods","url":"https://www.mdpi.com/2079-9292/12/4/853"},{"title":"Reducing Flipping Errors in Deep Neural Networks","url":"https://arxiv.org/pdf/2203.08390"},{"title":"The neural consequences of flip flopping: The feedback related negativity and salience of reward prediction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8594627/"},{"title":"On the Estimation of Complex Circuits Functional Failure Rate by Machine   Learning Techniques","url":"https://arxiv.org/pdf/2002.09945"},{"title":"Auditing and Debugging Deep Learning Models via Flip Points: Individual-Level and Group-Level Analysis | La Matematica | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44007-021-00003-w"},{"title":"Non-linearity identification for construction workers'   personality-safety behaviour predictive relationship using neural network and   linear regression modelling","url":"https://arxiv.org/pdf/1912.05944"},{"title":"From Arithmetic to Logic: The Resilience of Logic and Lookup-Based Neural Networks Under Parameter Bit-Flips","url":"https://arxiv.org/pdf/2603.22770"}]

Based on the search results, I found some relevant information about prediction flipping in neural networks, though the results didn't specifically focus on "probe safety" in the AI safety context you may have been looking for.

The most relevant result discusses prediction flipping, where the vast majority of misclassified samples were previously classified correctly, 
…[truncated 1129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T05:09:47.890901+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kaya \"Shallow-Deep Networks\" overthinking confusion metric intermediate classifier ICML 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kaya \"Shallow-Deep Networks\" overthinking confusion metric intermediate classifier ICML 2019"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T05:09:47.891023+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Reducing Flipping Errors in Deep Neural Networks\" prediction consistency 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Reducing Flipping Errors in Deep Neural Networks\" prediction consistency 2022"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T05:09:47.891174+00:00_

Web search results for query: "Kaya "Shallow-Deep Networks" overthinking confusion metric intermediate classifier ICML 2019"

Links: [{"title":"Shallow-Deep-Networks/README.md at master · yigitcankaya/Shallow-Deep-Networks","url":"https://github.com/yigitcankaya/Shallow-Deep-Networks/blob/master/README.md"},{"title":"GitHub - yigitcankaya/Shallow-Deep-Networks: Source Code for ICML 2019 Paper \"Shallow-Deep Networks: Understanding and Mitigating Network Overthinking\" · GitHub","url":"https://github.com/yigitcankaya/Shallow-Deep-Networks"},{"title":"Shallow-Deep Networks: Understanding and Mitigating Network Overthinking - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181007052K/abstract"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Yigitcan+Kaya,+Sanghyun+Hong,+and+Tudor+Dumitras.+2019.+Shallow-deep+networks:+Understanding+and+mitigating+network+overthinking.+In+International+conference+on+machine+learning.+PMLR,+3301--3310."},{"title":"[1810.07052] Shallow-Deep Networks: Understanding and Mitigating Network Overthinking","url":"https://arxiv.org/abs/1810.07052"},{"title":"Shallow-Deep Networks: Understanding and Mitigating Network Overthinking","url":"https://proceedings.mlr.press/v97/kaya19a.html"},{"title":"BibSLEIGH — Shallow-Deep Networks: Understanding and Mitigating Network Overthinking","url":"https://bibtex.github.io/ICML-2019-KayaHD.html"},{"title":"Shallow-Deep Networks: Understanding and Mitigating Network Overthinking","url":"https://arxiv.org/pdf/1810.07052"},{"title":"Track: Deep Learning Architectures","url":"https://icml.cc/virtual/2019/session/4839"}]

Based on the search results, here's what I found about the paper:

The paper "Shallow-Deep Networks: Understanding and Mitigating Network Overthinking" was authored by Yigitcan Kaya, Sanghyun Hong, and Tudor Dumitras, and was published at the 36th International Conference on Machine Learning in 2019.

**Main Contributions:**

The paper characterizes network "overth
…[truncated 977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T05:09:47.891342+00:00_

Web search results for query: ""Reducing Flipping Errors in Deep Neural Networks" prediction consistency 2022"

Links: [{"title":"Reducing Flipping Errors in Deep Neural Networks - AAAI-2022","url":"https://aaai-2022.virtualchair.net/poster_aaai5945"},{"title":"[2203.08390] Reducing Flipping Errors in Deep Neural Networks","url":"https://arxiv.org/abs/2203.08390"},{"title":"Reducing Flipping Errors in Deep Neural Networks","url":"https://arxiv.org/pdf/2203.08390"},{"title":"Reducing Flipping Errors in Deep Neural Networks | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/20603"},{"title":"Reducing Flipping Errors in Deep Neural Networks","url":"https://www.connectedpapers.com/main/222f314912369fe7b660e343771710ae8d59882e/Reducing-Flipping-Errors-in-Deep-Neural-Networks/graph"},{"title":"No Data, No Optimization: A Lightweight Method To Disrupt Neural   Networks With Sign-Flips","url":"https://arxiv.org/pdf/2502.07408"}]

I found relevant information about "Reducing Flipping Errors in Deep Neural Networks" from 2022. Here are the results:

## Paper Overview

The paper investigates how many test samples that a DNN misclassifies in its final epoch were previously correctly classified in earlier epochs, finding that the vast majority of misclassified samples had their predictions flipped from "correct" to "wrong".

## Proposed Solution

The authors propose to restrict the behavior changes of a DNN on correctly-classified samples to maintain correct local boundaries and reduce flipping errors on unseen samples.

## Results

Extensive experiments on different benchmark datasets with various modern network architectures demonstrate that the proposed flipping error reduction (FER) approach substantially improves generalization, robustness, and transferability of DNNs without introducing additional network parameters or inference cost.

The paper was presented at AAAI-2022 and is available on arXiv (2203.
…[truncated 190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T05:09:47.891509+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Keoliya \"Stable Prediction\" adverse events medical time series oscillation penalty 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Keoliya \"Stable Prediction\" adverse events medical time series oscillation penalty 2025"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T05:09:47.891650+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Miller Blume \"Decision Flip Rate\" prediction instability clinical 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Miller Blume \"Decision Flip Rate\" prediction instability clinical 2026"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T05:09:47.891793+00:00_

Web search results for query: "Miller Blume "Decision Flip Rate" prediction instability clinical 2026"

Links: [{"title":"Diagnostics for Individual-Level Prediction Instability in Machine Learning for Healthcare","url":"https://arxiv.org/pdf/2603.00192"},{"title":"Clinical prediction models and the multiverse of madness","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10729337/"},{"title":"Bootstrapping-based Regularisation for Reducing Individual Prediction Instability in Clinical Risk Prediction Models","url":"https://arxiv.org/pdf/2602.11360"},{"title":"Stability of clinical prediction models developed using statistical or machine learning methods","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10952221/"},{"title":"Early trajectory of clinical global impression as a transdiagnostic predictor of psychiatric hospitalisation: a retrospective cohort study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10709150/"}]

Based on the search results, I found the most relevant information in the first result:

Elizabeth W. Miller and Jeffrey D. Blume from the School of Data Science at the University of Virginia have developed diagnostics for individual-level prediction instability in machine learning for healthcare.

Their evaluation framework quantifies individual-level prediction instability across repeated instantiations of a fixed learning pipeline, introducing two complementary diagnostics: empirical prediction interval width (ePIW) and empirical decision flip rate (eDFR), which measures instability in threshold-based clinical decisions.

Their research addresses how predictive models in healthcare increasingly inform patient-level decisions, yet little attention is paid to the variability in individual risk estimates and its impact on treatment decisions. For overparameterized models standard in machine learning, randomness introduced by optimization and initialization can lead to materially different risk estimates for the same patient, often going un
…[truncated 238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T05:09:47.891954+00:00_

Web search results for query: "Keoliya "Stable Prediction" adverse events medical time series oscillation penalty 2025"

Links: [{"title":"[2510.14286] Stable Prediction of Adverse Events in Medical Time-Series Data","url":"https://arxiv.org/abs/2510.14286"},{"title":"[2510.14286v1] Stable Prediction of Adverse Events in Medical Time-Series Data","url":"https://arxiv.org/abs/2510.14286v1"},{"title":"Stable Prediction of Adverse Events in Medical Time-Series Data","url":"https://arxiv.org/html/2510.14286v1"},{"title":"Stable Prediction of Adverse Events in Medical Time-Series Data","url":"https://www.seas.upenn.edu/~mkeoliya/assets/pdf/carebench.pdf"},{"title":"Stable Prediction of Adverse Events in Medical Time-Series Data","url":"https://arxiv.org/pdf/2510.14286"}]

I found relevant results for your search query. Here's what I found:

The paper "Stable Prediction of Adverse Events in Medical Time-Series Data" is authored by Mayank Keoliya, Seewon Choi, Rajeev Alur, Mayur Naik, and Eric Wong from the University of Pennsylvania.

The paper introduces CAREBench, an early event prediction (EEP) benchmark that evaluates deployability using multi-modal inputs—tabular EHR, ECG waveforms, and clinical text—and assesses temporal stability alongside predictive accuracy.

The authors propose a stability metric that quantifies short-term variability in per-patient risk and penalizes abrupt oscillations based on local-Lipschitz constants. CAREBench spans six prediction tasks such as sepsis onset and compares classical learners, deep sequence models, and zero-shot LLMs.

Across tasks, existing methods, especially LLMs, struggle to jointly optimize accuracy and stability, with notably poor recall at high-precision operating points.

The paper was published on October 16, 2025, and is available on arXiv (2510.14286).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T05:09:47.892122+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/1810.07052",
  "prompt": "Extract the exact definition of the \"confusion metric\" or \"confusion score\" from the paper. How is it computed? Does it count prediction changes/flips across layers? What is the mathematical formula?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/1810.07052",
    "prompt": "Extract the exact definition of the \"confusion metric\" or \"confusion score\" from the paper. How is it computed? Does it count prediction changes/flips across layers? What is the mathematical formula?"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T05:09:47.892249+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.14286",
  "prompt": "Extract the exact definition of the \"stability metric\" that penalizes oscillations. What is the mathematical formula? How does it relate to crossing rate or sign changes in predictions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.14286",
    "prompt": "Extract the exact definition of the \"stability metric\" that penalizes oscillations. What is the mathematical formula? How does it relate to crossing rate or sign changes in predictions?"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T05:09:47.892373+00:00_

# Response

Based on the provided web page content, I cannot extract the exact definition, computational method, or mathematical formula for the "confusion metric" mentioned in the paper.

The abstract only briefly references it: "we propose a new confusion metric to quantify the internal disagreements that will likely lead to misclassifications." However, no further technical details are provided on this page.

To obtain the specific definition and formula, you would need to access the full paper PDF, which is available at the link provided on the arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T05:09:47.892493+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2203.08390",
  "prompt": "Extract the definition of 'flipping errors' from this paper. How do they define and measure prediction flips? Is this about flips across training epochs or across layers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2203.08390",
    "prompt": "Extract the definition of 'flipping errors' from this paper. How do they define and measure prediction flips? Is this about flips across training epochs or across layers?"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T05:09:47.892670+00:00_

Based on the provided content, the specific mathematical formula for the stability metric is **not disclosed** in this abstract or webpage excerpt.

The abstract only states that the stability metric "quantifies short-term variability in per-patient risk and penalizes abrupt oscillations based on local-Lipschitz constants." However, no equations or precise mathematical definition are provided in the available text.

To obtain the exact formula and understand how it relates to crossing rates or sign changes, you would need to:

1. Access the full PDF paper (linked as "/pdf/2510.14286")
2. Review the HTML version at arxiv.org/html/2510.14286v1
3. Consult the accompanying code repository referenced in the abstract

The webpage does not contain the detailed mathematical specifications necessary to answer your question about the precise formulation or its relationship to prediction sign changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T05:09:47.892819+00:00_

# Flipping Errors Definition

Based on the provided content, **flipping errors refer to misclassifications where a deep neural network incorrectly predicts a sample in the final epoch, despite having classified it correctly in earlier epochs during training.**

The paper defines this as: "the predictions for these samples were flipped from 'correct' to 'wrong'."

## Key Characteristics:

**Temporal Scope**: Flipping errors occur across training epochs, not across network layers. The authors investigate "how many test samples that a DNN misclassifies in the last epoch were ever correctly classified by the DNN before the last epoch."

**Core Finding**: The research empirically demonstrates that "the vast majority of the misclassified samples in the last epoch were ever classified correctly before the last epoch."

## Measurement Approach:

The paper measures flipping errors by tracking whether samples correctly classified during earlier training epochs become misclassified in the final selected model. This temporal regression in prediction accuracy—where previously learned correct classifications deteriorate—represents the phenomenon they address through their Flipping Error Reduction (FER) approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T05:09:47.892951+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/1810.07052",
  "prompt": "Find the exact definition of the \"confusion metric\" or \"confusion score\". Look for the mathematical formula. How is it computed across internal classifiers at different layers? Does it measure disagreement or prediction changes across layers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/1810.07052",
    "prompt": "Find the exact definition of the \"confusion metric\" or \"confusion score\". Look for the mathematical formula. How is it computed across internal classifiers at different layers? Does it measure disagreement or prediction changes across layers?"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T05:09:47.893072+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2510.14286v1",
  "prompt": "Find the exact mathematical definition of the stability metric that penalizes oscillations. Look for formulas involving Lipschitz constants, oscillation penalty, or prediction variability. How is it defined mathematically?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2510.14286v1",
    "prompt": "Find the exact mathematical definition of the stability metric that penalizes oscillations. Look for formulas involving Lipschitz constants, oscillation penalty, or prediction variability. How is it defined mathematically?"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T05:09:47.893193+00:00_

I cannot find a specific definition of a "confusion metric" or "confusion score" in the provided PDF content. The document appears to be a technical paper with embedded images and compressed data streams, but the text is largely unreadable due to PDF encoding.

To locate the exact mathematical formula you're seeking, I would need:
1. A clearer, text-based version of the document
2. The specific section or page number where this metric is defined
3. The paper's title or authors for reference

If you can provide the document in a more accessible format or specify which section discusses this metric, I'd be happy to help identify how it's computed across internal classifiers and whether it measures disagreement or prediction changes.

[Binary content (application/pdf, 389.7KB) also saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/9800489a-70d1-4b55-953c-73d78628b0a5/tool-results/webfetch-1779253595811-9ysilc.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T05:09:47.893371+00:00_

# Stability Metric Definition

The paper defines temporal stability using a **local Lipschitz constant** approach. Here's the mathematical definition:

## Formula

"Lc = 1/|Tc| ∑(t,t'∈Tc) |f(xt)-f(xt')|/|t-t'|"

Where:
- **Lc** = stability score for a local window
- **Tc** = set of timestamp pairs (t, t') where t' - t ≤ c hours
- **f(xt)** = model's risk score at time t
- **c** = 10 minutes (the local pairing window for clinical plausibility)
- **b** = probe radius defining the evaluation window [T-b, T+b]

## Key Characteristics

**Lower values indicate more stable trajectories.** The metric quantifies short-term variability by measuring the average rate of change in predicted risk scores within a narrow time window. Higher values suggest "rapid, potentially erratic oscillations that undermine clinical trust."

The authors emphasize that this approach "penalizes abrupt oscillations" by measuring how much risk scores vary between nearby timesteps, effectively capturing prediction volatility without assuming knowledge of actual clinical condition changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T05:09:47.893540+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://proceedings.mlr.press/v97/kaya19a.html",
  "prompt": "Find information about the 'confusion metric' or 'confusion score' defined in this paper. What does it measure? How is it computed across internal classifiers at different layers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://proceedings.mlr.press/v97/kaya19a.html",
    "prompt": "Find information about the 'confusion metric' or 'confusion score' defined in this paper. What does it measure? How is it computed across internal classifiers at different layers?"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T05:09:47.893708+00:00_

Based on the provided webpage content, I cannot find specific details about how the confusion metric is computed or its exact technical definition.

The abstract only mentions that the authors "propose a new confusion metric to quantify the internal disagreements that will likely to lead to misclassifications." However, the webpage does not elaborate on:

- The mathematical formula or computation method
- How it operates across different internal classifier layers
- The specific measurement approach

To obtain this information, you would need to access the full PDF paper available at the link provided (http://proceedings.mlr.press/v97/kaya19a/kaya19a.pdf), which likely contains the detailed technical explanation in the methodology section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T05:09:47.893841+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kaya Hong Dumitras \"confusion metric\" \"internal classifiers\" overthinking definition formula disagreement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kaya Hong Dumitras \"confusion metric\" \"internal classifiers\" overthinking definition formula disagreement"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T05:09:47.893983+00:00_

Web search results for query: "Kaya Hong Dumitras "confusion metric" "internal classifiers" overthinking definition formula disagreement"

Links: [{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Yigitcan+Kaya,+Sanghyun+Hong,+and+Tudor+Dumitras.+2019.+Shallow-deep+networks:+Understanding+and+mitigating+network+overthinking.+In+International+conference+on+machine+learning.+PMLR,+3301--3310."},{"title":"Shallow-Deep Networks: Understanding and Mitigating Network Overthinking","url":"https://proceedings.mlr.press/v97/kaya19a.html"},{"title":"Yigitcan Kaya, Sanghyun Hong, Tudor Dumitras - UMIACS","url":"http://users.umiacs.umd.edu/~tudor/project_pages/shallowdeepnetwork/files/icml_sdn_poster.pdf"},{"title":"Classifier uncertainty: evidence, potential impact, and probabilistic treatment","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7959610/"},{"title":"Never mind the metrics -- what about the uncertainty? Visualising   confusion matrix metric distributions","url":"https://arxiv.org/pdf/2206.02157"},{"title":"Classifier uncertainty: evidence, potential impact, and probabilistic   treatment","url":"https://arxiv.org/pdf/2006.11105"},{"title":"Challenges in the real world use of classification accuracy metrics: From recall and precision to the Matthews correlation coefficient - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10550141/"}]

Based on the web search results, I found information about Kaya, Hong, and Dumitras's work on the confusion metric:

Kaya, Hong, and Dumitras proposed a new confusion metric to quantify the internal disagreements that will likely lead to misclassifications. 

Their work characterizes a prevalent weakness of deep neural networks called 'overthinking', which occurs when a DNN can reach correct predictions before its final layer. Overthinking is computationally wasteful, and it can also be destructive when, by the final layer, a correct prediction changes into a misclassification.

Detecting overthinking requi
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T05:09:47.894161+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'completed', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'completed', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'in_progress', 'activeForm': 'Compiling final literature survey report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'completed', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'completed', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'in_progress', 'activeForm': 'Compiling final literature survey report'}]"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T05:09:47.894330+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T05:09:47.894533+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/crossing_rate_literature_survey.md",
  "content": "# Crossing Rate / Prediction Stability Metric — Literature Survey\n\n**Date:** 2026-05-20  \n**Purpose:** Respond to red-team concern that CR / CR-composite is a \"straw man metric\"  \n**Method:** WebSearch + WebFetch across 5 directions, 30+ keyword combinations  \n\n---\n\n## 1. Direct Hits (Exact \"Crossing Rate\" or Equivalent in Probe/Classifier Context)\n\n**None found.** No paper defines a metric that counts how many times a probe's binary prediction (e.g., safe vs. unsafe) changes sign/flips as one traverses transformer layers from layer 0 to layer N.\n\nThe term \"crossing rate\" in ML literature maps exclusively to the signal processing concept of **zero-crossing rate (ZCR)**, used in audio/speech classification, and has never been applied to probe predictions across layers.\n\n**Searched keywords (all returned zero relevant results):**\n- \"crossing rate\" safety probe\n- \"crossing rate\" probing classifier\n- \"sign change rate\" classifier prediction\n- \"prediction flip rate\" neural network probe\n- \"label oscillation\" hidden state probe\n- \"zero crossing rate\" neural network predictions classification stability\n\n---\n\n## 2. Near Hits (Closely Related Concepts, Different Names)\n\n### 2.1 Kaya et al., \"Shallow-Deep Networks: Understanding and Mitigating Network Overthinking\" (ICML 2019)\n- **arXiv:** [1810.07052](https://arxiv.org/abs/1810.07052)\n- **Concept:** Defines a **\"confusion metric\"** that measures internal disagreements across layer-attached classifiers. Quantifies divergence between intermediate predictions and the final prediction.\n- **Overthinking:** When an intermediate layer produces a correct prediction but the final layer flips it to incorrect — essentially a destructive prediction flip across depth.\n- **Relation to CR:** Most conceptually proximate. Their confusion metric captures cross-layer disagreement (via L1 distance), while our CR counts discrete sign changes. Both measure prediction instability across the depth axis.\n\n### 2.2 Keoliya et al., \"Stable Prediction of Adverse Events in Medical Time-Series Data\" (arXiv 2025)\n- **arXiv:** [2510.14286](https://arxiv.org/abs/2510.14286)\n- **Concept:** Defines a **stability metric based on local Lipschitz constants** that penalizes abrupt oscillations in per-patient risk predictions: `Lc = 1/|Tc| Σ |f(x_t) - f(x_t')| / |t - t'|` where Tc pairs timestamps within c-hour windows.\n- **Key finding:** \"Existing methods, especially LLMs, struggle to jointly optimize accuracy and stability.\"\n- **Relation to CR:** Measures prediction oscillation over time (temporal axis), parallel to CR measuring oscillation over layers (depth axis). Lower Lc = more stable = analogous to lower CR.\n\n### 2.3 Miller & Blume, \"Diagnostics for Individual-Level Prediction Instability in ML for Healthcare\" (arXiv 2026)\n- **arXiv:** [2603.00192](https://arxiv.org/abs/2603.00192)\n- **Concept:** Defines **empirical Decision Flip Rate (eDFR)** — how often threshold-based clinical decisions change due to prediction variability across model instantiations.\n- **Relation to CR:** eDFR counts decision flips across model re-instantiations; CR counts prediction flips across layers. Both are discrete flip-counting metrics applied to binary decisions.\n\n### 2.4 Larsen, \"The Instability of Safety\" (arXiv 2025)\n- **arXiv:** [2512.12066](https://arxiv.org/abs/2512.12066)\n- **Concept:** Defines **Safety Stability Index (SSI)** measuring how consistently a model makes the same safety decision across sampling configurations. 18–28% of harmful prompts exhibit \"decision flips.\" SSI drops from 0.977 to 0.942 across temperatures.\n- **Relation to CR:** SSI measures behavioral stability of safety decisions; CR measures internal probe prediction stability. Both capture the \"how stable is the safety judgment\" question.\n\n### 2.5 PABEE: Zhou et al., \"BERT Loses Patience: Fast and Robust Inference with Early Exit\" (NeurIPS 2020)\n- **arXiv:** [2006.04152](https://arxiv.org/abs/2006.04152)\n- **Concept:** Exits when intermediate classifier predictions **remain unchanged for a pre-defined \"patience\" number of consecutive layers**. Cross-layer prediction agreement is the core confidence signal.\n- **Relation to CR:** PABEE's patience mechanism is the inverse of CR — it measures prediction *stability* (consecutive agreements) while CR measures *instability* (sign changes). Both operate on the same signal: whether probe predictions flip across layers.\n\n### 2.6 Xie et al., \"Calibrating Reasoning in Language Models with Internal Consistency\" (NeurIPS 2024)\n- **arXiv:** [2405.18711](https://arxiv.org/abs/2405.18711)\n- **Concept:** Defines **\"internal consistency\"** as agreement of latent predictions decoded from intermediate layers with the final prediction.\n- **Relation to CR:** Measures cross-layer agreement (binary), while CR counts the number of sign transitions.\n\n### 2.7 Wildi, \"Sign Accuracy, Mean-Squared Error and the Rate of Zero Crossings\" (arXiv 2026)\n- **arXiv:** [2601.06547](https://arxiv.org/abs/2601.06547)\n- **Concept:** Econometrics framework that explicitly connects **sign accuracy** with **zero-crossing frequency** via constrained optimization. Holding time `ht(y|b) = π/arccos(ρ(y))`.\n- **Relation to CR:** The mathematical framework linking sign accuracy (≈ BA) and zero-crossing rate (≈ CR) is exactly our CR-composite decomposition, but in econometrics.\n\n### 2.8 CCE: Zhong et al., \"Confidence-Consistency Evaluation for Time Series Anomaly Detection\" (arXiv 2025)\n- **arXiv:** [2509.01098](https://arxiv.org/abs/2509.01098)\n- **Concept:** Multiplicative composite: `S_anom = Conf(E_i) × Cons(E_i)`, combining confidence and consistency.\n- **Relation to CR-composite:** Closest methodological precedent for multiplicative accuracy × stability composites.\n\n### 2.9 Hemmati et al., \"Volatility in Certainty (VC)\" (arXiv 2025)\n- **arXiv:** [2511.11834](https://arxiv.org/abs/2511.11834)\n- **Concept:** Defines VC as \"the average squared log-ratio of adjacent certainty values\" in sorted softmax outputs. Strong negative correlation (ρ < −0.90) between accuracy and log(VC).\n- **Relation to CR:** VC measures prediction volatility; CR measures prediction sign changes. Both capture instability in classifier outputs.\n\n---\n\n## 3. Related but Different (Prediction Stability/Consistency, Not Crossing Rate)\n\n### 3.1 Layer Selection Criteria Beyond Accuracy\n\n| Paper | Venue | Criterion | Key Finding |\n|-------|-------|-----------|-------------|\n| Hewitt & Liang, \"Designing and Interpreting Probes with Control Tasks\" | EMNLP 2019 | Selectivity | Accuracy and selectivity disagree on optimal layer (ELMo layer 1 vs. 2) |\n| Voita & Titov, \"Information-Theoretic Probing with MDL\" | EMNLP 2020 | MDL | MDL methods \"are more informative and **stable** than standard probes\" |\n| Pimentel et al., \"Pareto Probing\" | EMNLP 2020 | Pareto complexity | Pareto criterion can reorder layer rankings vs. accuracy |\n| Vu et al., \"What Makes BERT Metrics Robust?\" | COLING 2022 | Robustness | Robustness-optimal layer differs from accuracy-optimal layer |\n| Choi et al., \"Probe Behaviors via MI Bounds\" | ICASSP 2024 | MI / linear margin | \"Interpreting layer-wise accuracy can be tricky\" |\n| Huang, \"Spectral Identifiability for Probe Geometry\" | arXiv 2025 | Spectral gap | Probe stability follows phase transitions in eigengap |\n\n### 3.2 Online/Runtime Safety Monitoring Systems\n\n| Paper | Venue | Mechanism |\n|-------|-------|-----------|\n| **SafeSwitch** (Han et al.) | EMNLP 2025 Findings | Prober on internal states → activates refusal head |\n| **TrajGuard** (Liu et al.) | ACL 2026 Findings | Streaming hidden-state trajectory with sliding window; states carry \"stronger and more stable risk signals\" |\n| **HiddenGuard/Prism** (Mei et al.) | arXiv 2024 | Token-level real-time detection via intermediate hidden states |\n| **ShieldHead** (Xuan et al.) | ACL 2025 Findings | Classification head parallel to LM head; <1ms latency |\n| **In-Decoding Probing** (Zhao et al.) | arXiv 2026 | Surfaces latent safety signals during decoding |\n| **AISA** (Song et al.) | arXiv 2026 | Spatiotemporal safety analysis + logits-level steering |\n| **Beyond Linear Probes** (Oldfield et al.) | ICLR 2026 | Truncated polynomial classifiers with \"safety dial\" cascade |\n\n### 3.3 Prediction Trajectory / Convergence\n\n| Paper | Venue | Concept |\n|-------|-------|---------|\n| Belrose et al., \"Tuned Lens\" | arXiv 2023 | Per-layer prediction trajectory; notes utility for malicious input detection |\n| Kongmanee, \"Token Prediction Refinement\" | arXiv 2025 | \"Depth of prediction refinement\" — layers needed to converge |\n| Long et al., \"When Truthful Representations Flip\" | EMNLP 2025 | Representational \"flips\" under deceptive instructions in early-to-mid layers |\n| Damirchi et al., \"Truth as a Trajectory\" | arXiv 2025 | Layer-wise geometric displacement distinguishes valid from spurious reasoning |\n| CircuitProbe (Panuganti) | arXiv 2025 | \"Stability zones\" via derivative of representation change |\n\n### 3.4 Early Prediction of Safety from CoT/Generation\n\n| Paper | Venue | Finding |\n|-------|-------|---------|\n| Chan et al., \"Predict Alignment Before Thinking Completes\" | arXiv 2025 | Probe on CoT activations predicts safety 50 sentences ahead |\n| Ashok & May, \"LMs Can Predict Own Behavior\" | NeurIPS 2025 | Input-token probes predict output safety; reduces jailbreaking 91% |\n| David, \"Temporal Predictors of Outcome\" | arXiv 2025 | Correctness highly predictable after few reasoning tokens |\n| Ruddell, \"Silent Commitment Failure\" | NIST CAISI 2026 | \"Governability\" = pre-commitment error detectability; 52× spike ratio between architectures |\n\n### 3.5 Probe Reliability and Failure Modes\n\n| Paper | Venue | Finding |\n|-------|-------|---------|\n| Wang et al., \"False Sense of Security\" | arXiv 2025 | Probes learn superficial patterns; n-gram methods achieve comparable performance |\n| Ravichander et al. | NeurIPS 2022 | \"Fundamental instability\" of probes for concept detection |\n| McGuinness et al., \"Neural Chameleons\" | arXiv 2025 | Models can be fine-tuned to evade activation monitors |\n| Belinkov, \"Probing Classifiers: Promises, Shortcomings\" | CL 2022 | Comprehensive survey of probing limitations |\n\n### 3.6 Representation Stability\n\n| Paper | Venue | Concept |\n|-------|-------|---------|\n| Bali et al., \"LLM Attention-Head Stability\" | arXiv 2026 | Middle-layer heads are least stable yet most representationally distinct |\n| Raju, \"Geometric Stability\" | arXiv 2026 | Stability and similarity have near-zero correlation (ρ ≈ 0.01) |\n| Khanmohammadi et al., \"CCPS\" | arXiv 2025 | Representation stability under perturbation for calibration |\n| Sadiekh et al., \"Polarity-Aware Probing (PA-CCS)\" | AAAI 2025 | Polar Consistency / Contradiction Index for semantic robustness |\n\n### 3.7 Composite Safety Evaluation Frameworks\n\n| Paper | Venue | Metric |\n|-------|-------|--------|\n| CUES (Alqudah et al.) | MDPI Math 2026 | `(C×U×E×S)^{1/4}` — geometric mean including stability |\n| Guerin et al. | IEEE ISSRE 2022 | Safety Gain + Residual Hazard + Availability Cost |\n| Teinemaa et al. | DMKD 2018 | Temporal stability for process mining classifiers |\n| Sahoo et al. | ICBINB@ICLR 2026 | Safety classifier collapse: 85%→50% AUC at σ=0.02 |\n\n### 3.8 Flipping Errors (Training Epoch Context)\n\n| Paper | Venue | Concept |\n|-------|-------|---------|\n| Yan et al., \"Reducing Flipping Errors in DNNs\" | AAAI 2022 | Prediction flips correct→wrong across training epochs; proposes FER regularization |\n\n---\n\n## 4. Gap Confirmation\n\nAfter searching 30+ keyword combinations across 5 directions:\n\n**The concept of measuring how many times a probe's binary prediction crosses the decision boundary as one scans across transformer layers is genuinely novel.** No existing paper defines this specific metric.\n\n### Why the gap exists\n\n1. **Probing literature** (2018–2024) focused on per-layer accuracy metrics; the question \"how stable is the prediction trajectory?\" was not asked because probing was evaluated layer-by-layer, not as a trajectory.\n\n2. **Early exit literature** (PABEE, CATs, etc.) uses cross-layer agreement as an *exit criterion* but never formalized it as an *evaluation metric* for probe quality.\n\n3. **Online safety monitoring** (SafeSwitch, TrajGuard, etc.) is a very recent field (2024–2026); the first papers focus on making it work at all, not on formalizing stability metrics for the monitoring signal itself.\n\n4. **The closest analogue** (ZCR from signal processing) is well-established in audio but the conceptual transfer to probe predictions across neural network depth has not been made.\n\n---\n\n## 5. Rebuttal Strategy\n\n### If reviewer says \"CR is a straw man metric you invented\":\n\n**Response A — CR addresses a documented gap:**\n> CR formalizes a phenomenon already observed but not quantified in the literature. Kaya et al. (ICML 2019) identified \"overthinking\" — where correct intermediate predictions flip to incorrect final predictions — and proposed a confusion metric measuring internal disagreement. PABEE (NeurIPS 2020) uses cross-layer prediction agreement as an exit criterion. Our crossing rate operationalizes this same intuition as an explicit evaluation metric: how often does the probe's binary decision flip across layers?\n\n**Response B — CR has direct analogues in other domains:**\n> The concept of counting sign changes in a sequential signal has established precedent:\n> - **Zero-crossing rate (ZCR)** is a standard signal processing metric (widely used in audio classification)\n> - **Decision Flip Rate (eDFR)** was independently proposed by Miller & Blume (2026) for clinical prediction instability\n> - **Wildi (2026)** explicitly connects sign accuracy with zero-crossing frequency in econometrics\n> - **Keoliya et al. (2025)** define an oscillation-penalizing stability metric for medical time series\n> \n> We transfer this well-motivated concept to the novel setting of cross-layer safety probe evaluation.\n\n**Response C — CR fills a practical need for online safety monitoring:**\n> The emerging field of online safety monitoring (SafeSwitch, EMNLP 2025; TrajGuard, ACL 2026; HiddenGuard, 2024; ShieldHead, ACL 2025) deploys probes that must make decisions at every layer or every token. A probe with high accuracy but high CR is unreliable for real-time deployment — it will oscillate between \"safe\" and \"unsafe\" across adjacent layers, making the monitoring signal noisy and the intervention policy unstable. CR captures exactly this failure mode.\n\n**Response D — CR-composite has methodological precedent:**\n> Multiplicative composites of accuracy and stability have been independently proposed:\n> - CCE (Zhong et al., 2025): `S = Conf × Cons` for anomaly detection\n> - CUES (Alqudah et al., 2026): geometric mean of accuracy, calibration, equity, and stability\n> - Keoliya et al. (2025): document that \"existing methods struggle to jointly optimize accuracy and stability\"\n> \n> CR-composite (BA × (1−CR)) follows this established pattern.\n\n### Recommended framing in paper:\n\nRather than claiming CR is a metric others already use, frame it as:\n\n1. **A formalization of an observed phenomenon** (overthinking, cross-layer disagreement) that lacked a dedicated metric\n2. **A natural metric for the online monitoring setting** — where prediction trajectory stability is operationally critical\n3. **An instance of a broader pattern** (ZCR, eDFR, Lipschitz stability) applied to a new domain\n\n### Key citations to add:\n\n| Citation | Purpose |\n|----------|---------|\n| Kaya et al. (ICML 2019) | Overthinking + confusion metric = prior recognition of cross-layer prediction instability |\n| Zhou et al. / PABEE (NeurIPS 2020) | Cross-layer prediction agreement as a practically useful signal |\n| Keoliya et al. (arXiv 2025) | Accuracy-stability joint optimization difficulty; oscillation-penalizing metric |\n| Miller & Blume (arXiv 2026) | Decision Flip Rate as a flip-counting instability diagnostic |\n| Larsen (arXiv 2025) | Safety Stability Index; 18–28% of prompts exhibit decision flips |\n| SafeSwitch (EMNLP 2025) | Online safety monitoring = the deployment context where CR matters |\n| TrajGuard (ACL 2026) | Hidden-state trajectories carry \"more stable risk signals\" |\n| Wildi (arXiv 2026) | Sign accuracy ↔ zero-crossing rate connection in optimization |\n\n---\n\n## 6. Search Coverage Log\n\n| Direction | Keywords Searched | Papers Examined | Verified via WebFetch |\n|-----------|------------------|-----------------|----------------------|\n| 1. CR / sign change in probes | 7 combinations | ~20 | 8 |\n| 2. Composite metrics | 7 combinations | ~22 | 6 |\n| 3. SafeSwitch / online safety | 8 combinations | ~25 | 10 |\n| 4. Layer selection stability | 7 combinations | ~20 | 8 |\n| 5. Temporal consistency | 8 combinations | ~20 | 7 |\n| Extra: ZCR, overthinking, FER | 5 combinations | ~10 | 4 |\n| **Total** | **42 combinations** | **~117 papers** | **43 verified** |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/crossing_rate_literature_survey.md",
    "content": "# Crossing Rate / Prediction Stability Metric — Literature Survey\n\n**Date:** 2026-05-20  \n**Purpose:** Respond to red-team concern that CR / CR-composite is a \"straw man metric\"  \n**Method:** WebSearch + WebFetch across 5 directions, 30+ keyword combinations  \n\n---\n\n## 1. Direct Hits (Exact \"Crossing Rate\" or Equivalent in Probe/Classifier Context)\n\n**None found.** No paper defines a metric that counts how many times a probe's binary prediction (e.g., safe vs. unsafe) changes sign/flips as one traverses transformer layers from layer 0 to layer N.\n\nThe term \"crossing rate\" in ML literature maps exclusively to the signal processing concept of **zero-crossing rate (ZCR)**, used in audio/speech classification, and has never been applied to probe predictions across layers.\n\n**Searched keywords (all returned zero relevant results):**\n- \"crossing rate\" safety probe\n- \"crossing rate\" probing classifier\n- \"sign change rate\" classifier prediction\n- \"prediction flip rate\" neural network probe\n- \"label oscillation\" hidden state probe\n- \"zero crossing rate\" neural network predictions classification stability\n\n---\n\n## 2. Near Hits (Closely Related Concepts, Different Names)\n\n### 2.1 Kaya et al., \"Shallow-Deep Networks: Understanding and Mitigating Network Overthinking\" (ICML 2019)\n- **arXiv:** [1810.07052](https://arxiv.org/abs/1810.07052)\n- **Concept:** Defines a **\"confusion metric\"** that measures internal disagreements across layer-attached classifiers. Quantifies divergence between intermediate predictions and the final prediction.\n- **Overthinking:** When an intermediate layer produces a correct prediction but the final layer flips it to incorrect — essentially a destructive prediction flip across depth.\n- **Relation to CR:** Most conceptually proximate. Their confusion metric captures cross-layer disagreement (via L1 distance), while our CR counts discrete sign changes. Both measure prediction instability across the depth axis.\n\n### 2.2 Keoliya et al., \"Stable Prediction of Adverse Events in Medical Time-Series Data\" (arXiv 2025)\n- **arXiv:** [2510.14286](https://arxiv.org/abs/2510.14286)\n- **Concept:** Defines a **stability metric based on local Lipschitz constants** that penalizes abrupt oscillations in per-patient risk predictions: `Lc = 1/|Tc| Σ |f(x_t) - f(x_t')| / |t - t'|` where Tc pairs timestamps within c-hour windows.\n- **Key finding:** \"Existing methods, especially LLMs, struggle to jointly optimize accuracy and stability.\"\n- **Relation to CR:** Measures prediction oscillation over time (temporal axis), parallel to CR measuring oscillation over layers (depth axis). Lower Lc = more stable = analogous to lower CR.\n\n### 2.3 Miller & Blume, \"Diagnostics for Individual-Level Prediction Instability in ML for Healthcare\" (arXiv 2026)\n- **arXiv:** [2603.00192](https://arxiv.org/abs/2603.00192)\n- **Concept:** Defines **empirical Decision Flip Rate (eDFR)** — how often threshold-based clinical decisions change due to prediction variability across model instantiations.\n- **Relation to CR:** eDFR counts decision flips across model re-instantiations; CR counts prediction flips across layers. Both are discrete flip-counting metrics applied to binary decisions.\n\n### 2.4 Larsen, \"The Instability of Safety\" (arXiv 2025)\n- **arXiv:** [2512.12066](https://arxiv.org/abs/2512.12066)\n- **Concept:** Defines **Safety Stability Index (SSI)** measuring how consistently a model makes the same safety decision across sampling configurations. 18–28% of harmful prompts exhibit \"decision flips.\" SSI drops from 0.977 to 0.942 across temperatures.\n- **Relation to CR:** SSI measures behavioral stability of safety decisions; CR measures internal probe prediction stability. Both capture the \"how stable is the safety judgment\" question.\n\n### 2.5 PABEE: Zhou et al., \"BERT Loses Patience: Fast and Robust Inference with Early Exit\" (NeurIPS 2020)\n- **arXiv:** [2006.04152](https://arxiv.org/abs/2006.04152)\n- **Concept:** Exits when intermediate classifier predictions **remain unchanged for a pre-defined \"patience\" number of consecutive layers**. Cross-layer prediction agreement is the core confidence signal.\n- **Relation to CR:** PABEE's patience mechanism is the inverse of CR — it measures prediction *stability* (consecutive agreements) while CR measures *instability* (sign changes). Both operate on the same signal: whether probe predictions flip across layers.\n\n### 2.6 Xie et al., \"Calibrating Reasoning in Language Models with Internal Consistency\" (NeurIPS 2024)\n- **arXiv:** [2405.18711](https://arxiv.org/abs/2405.18711)\n- **Concept:** Defines **\"internal consistency\"** as agreement of latent predictions decoded from intermediate layers with the final prediction.\n- **Relation to CR:** Measures cross-layer agreement (binary), while CR counts the number of sign transitions.\n\n### 2.7 Wildi, \"Sign Accuracy, Mean-Squared Error and the Rate of Zero Crossings\" (arXiv 2026)\n- **arXiv:** [2601.06547](https://arxiv.org/abs/2601.06547)\n- **Concept:** Econometrics framework that explicitly connects **sign accuracy** with **zero-crossing frequency** via constrained optimization. Holding time `ht(y|b) = π/arccos(ρ(y))`.\n- **Relation to CR:** The mathematical framework linking sign accuracy (≈ BA) and zero-crossing rate (≈ CR) is exactly our CR-composite decomposition, but in econometrics.\n\n### 2.8 CCE: Zhong et al., \"Confidence-Consistency Evaluation for Time Series Anomaly Detection\" (arXiv 2025)\n- **arXiv:** [2509.01098](https://arxiv.org/abs/2509.01098)\n- **Concept:** Multiplicative composite: `S_anom = Conf(E_i) × Cons(E_i)`, combining confidence and consistency.\n- **Relation to CR-composite:** Closest methodological precedent for multiplicative accuracy × stability composites.\n\n### 2.9 Hemmati et al., \"Volatility in Certainty (VC)\" (arXiv 2025)\n- **arXiv:** [2511.11834](https://arxiv.org/abs/2511.11834)\n- **Concept:** Defines VC as \"the average squared log-ratio of adjacent certainty values\" in sorted softmax outputs. Strong negative correlation (ρ < −0.90) between accuracy and log(VC).\n- **Relation to CR:** VC measures prediction volatility; CR measures prediction sign changes. Both capture instability in classifier outputs.\n\n---\n\n## 3. Related but Different (Prediction Stability/Consistency, Not Crossing Rate)\n\n### 3.1 Layer Selection Criteria Beyond Accuracy\n\n| Paper | Venue | Criterion | Key Finding |\n|-------|-------|-----------|-------------|\n| Hewitt & Liang, \"Designing and Interpreting Probes with Control Tasks\" | EMNLP 2019 | Selectivity | Accuracy and selectivity disagree on optimal layer (ELMo layer 1 vs. 2) |\n| Voita & Titov, \"Information-Theoretic Probing with MDL\" | EMNLP 2020 | MDL | MDL methods \"are more informative and **stable** than standard probes\" |\n| Pimentel et al., \"Pareto Probing\" | EMNLP 2020 | Pareto complexity | Pareto criterion can reorder layer rankings vs. accuracy |\n| Vu et al., \"What Makes BERT Metrics Robust?\" | COLING 2022 | Robustness | Robustness-optimal layer differs from accuracy-optimal layer |\n| Choi et al., \"Probe Behaviors via MI Bounds\" | ICASSP 2024 | MI / linear margin | \"Interpreting layer-wise accuracy can be tricky\" |\n| Huang, \"Spectral Identifiability for Probe Geometry\" | arXiv 2025 | Spectral gap | Probe stability follows phase transitions in eigengap |\n\n### 3.2 Online/Runtime Safety Monitoring Systems\n\n| Paper | Venue | Mechanism |\n|-------|-------|-----------|\n| **SafeSwitch** (Han et al.) | EMNLP 2025 Findings | Prober on internal states → activates refusal head |\n| **TrajGuard** (Liu et al.) | ACL 2026 Findings | Streaming hidden-state trajectory with sliding window; states carry \"stronger and more stable risk signals\" |\n| **HiddenGuard/Prism** (Mei et al.) | arXiv 2024 | Token-level real-time detection via intermediate hidden states |\n| **ShieldHead** (Xuan et al.) | ACL 2025 Findings | Classification head parallel to LM head; <1ms latency |\n| **In-Decoding Probing** (Zhao et al.) | arXiv 2026 | Surfaces latent safety signals during decoding |\n| **AISA** (Song et al.) | arXiv 2026 | Spatiotemporal safety analysis + logits-level steering |\n| **Beyond Linear Probes** (Oldfield et al.) | ICLR 2026 | Truncated polynomial classifiers with \"safety dial\" cascade |\n\n### 3.3 Prediction Trajectory / Convergence\n\n| Paper | Venue | Concept |\n|-------|-------|---------|\n| Belrose et al., \"Tuned Lens\" | arXiv 2023 | Per-layer prediction trajectory; notes utility for malicious input detection |\n| Kongmanee, \"Token Prediction Refinement\" | arXiv 2025 | \"Depth of prediction refinement\" — layers needed to converge |\n| Long et al., \"When Truthful Representations Flip\" | EMNLP 2025 | Representational \"flips\" under deceptive instructions in early-to-mid layers |\n| Damirchi et al., \"Truth as a Trajectory\" | arXiv 2025 | Layer-wise geometric displacement distinguishes valid from spurious reasoning |\n| CircuitProbe (Panuganti) | arXiv 2025 | \"Stability zones\" via derivative of representation change |\n\n### 3.4 Early Prediction of Safety from CoT/Generation\n\n| Paper | Venue | Finding |\n|-------|-------|---------|\n| Chan et al., \"Predict Alignment Before Thinking Completes\" | arXiv 2025 | Probe on CoT activations predicts safety 50 sentences ahead |\n| Ashok & May, \"LMs Can Predict Own Behavior\" | NeurIPS 2025 | Input-token probes predict output safety; reduces jailbreaking 91% |\n| David, \"Temporal Predictors of Outcome\" | arXiv 2025 | Correctness highly predictable after few reasoning tokens |\n| Ruddell, \"Silent Commitment Failure\" | NIST CAISI 2026 | \"Governability\" = pre-commitment error detectability; 52× spike ratio between architectures |\n\n### 3.5 Probe Reliability and Failure Modes\n\n| Paper | Venue | Finding |\n|-------|-------|---------|\n| Wang et al., \"False Sense of Security\" | arXiv 2025 | Probes learn superficial patterns; n-gram methods achieve comparable performance |\n| Ravichander et al. | NeurIPS 2022 | \"Fundamental instability\" of probes for concept detection |\n| McGuinness et al., \"Neural Chameleons\" | arXiv 2025 | Models can be fine-tuned to evade activation monitors |\n| Belinkov, \"Probing Classifiers: Promises, Shortcomings\" | CL 2022 | Comprehensive survey of probing limitations |\n\n### 3.6 Representation Stability\n\n| Paper | Venue | Concept |\n|-------|-------|---------|\n| Bali et al., \"LLM Attention-Head Stability\" | arXiv 2026 | Middle-layer heads are least stable yet most representationally distinct |\n| Raju, \"Geometric Stability\" | arXiv 2026 | Stability and similarity have near-zero correlation (ρ ≈ 0.01) |\n| Khanmohammadi et al., \"CCPS\" | arXiv 2025 | Representation stability under perturbation for calibration |\n| Sadiekh et al., \"Polarity-Aware Probing (PA-CCS)\" | AAAI 2025 | Polar Consistency / Contradiction Index for semantic robustness |\n\n### 3.7 Composite Safety Evaluation Frameworks\n\n| Paper | Venue | Metric |\n|-------|-------|--------|\n| CUES (Alqudah et al.) | MDPI Math 2026 | `(C×U×E×S)^{1/4}` — geometric mean including stability |\n| Guerin et al. | IEEE ISSRE 2022 | Safety Gain + Residual Hazard + Availability Cost |\n| Teinemaa et al. | DMKD 2018 | Temporal stability for process mining classifiers |\n| Sahoo et al. | ICBINB@ICLR 2026 | Safety classifier collapse: 85%→50% AUC at σ=0.02 |\n\n### 3.8 Flipping Errors (Training Epoch Context)\n\n| Paper | Venue | Concept |\n|-------|-------|---------|\n| Yan et al., \"Reducing Flipping Errors in DNNs\" | AAAI 2022 | Prediction flips correct→wrong across training epochs; proposes FER regularization |\n\n---\n\n## 4. Gap Confirmation\n\nAfter searching 30+ keyword combinations across 5 directions:\n\n**The concept of measuring how many times a probe's binary prediction crosses the decision boundary as one scans across transformer layers is genuinely novel.** No existing paper defines this specific metric.\n\n### Why the gap exists\n\n1. **Probing literature** (2018–2024) focused on per-layer accuracy metrics; the question \"how stable is the prediction trajectory?\" was not asked because probing was evaluated layer-by-layer, not as a trajectory.\n\n2. **Early exit literature** (PABEE, CATs, etc.) uses cross-layer agreement as an *exit criterion* but never formalized it as an *evaluation metric* for probe quality.\n\n3. **Online safety monitoring** (SafeSwitch, TrajGuard, etc.) is a very recent field (2024–2026); the first papers focus on making it work at all, not on formalizing stability metrics for the monitoring signal itself.\n\n4. **The closest analogue** (ZCR from signal processing) is well-established in audio but the conceptual transfer to probe predictions across neural network depth has not been made.\n\n---\n\n## 5. Rebuttal Strategy\n\n### If reviewer says \"CR is a straw man metric you invented\":\n\n**Response A — CR addresses a documented gap:**\n> CR formalizes a phenomenon already observed but not quantified in the literature. Kaya et al. (ICML 2019) identified \"overthinking\" — where correct intermediate predictions flip to incorrect final predictions — and proposed a confusion metric measuring internal disagreement. PABEE (NeurIPS 2020) uses cross-layer prediction agreement as an exit criterion. Our crossing rate operationalizes this same intuition as an explicit evaluation metric: how often does the probe's binary decision flip across layers?\n\n**Response B — CR has direct analogues in other domains:**\n> The concept of counting sign changes in a sequential signal has established precedent:\n> - **Zero-crossing rate (ZCR)** is a standard signal processing metric (widely used in audio classification)\n> - **Decision Flip Rate (eDFR)** was independently proposed by Miller & Blume (2026) for clinical prediction instability\n> - **Wildi (2026)** explicitly connects sign accuracy with zero-crossing frequency in econometrics\n> - **Keoliya et al. (2025)** define an oscillation-penalizing stability metric for medical time series\n> \n> We transfer this well-motivated concept to the novel setting of cross-layer safety probe evaluation.\n\n**Response C — CR fills a practical need for online safety monitoring:**\n> The emerging field of online safety monitoring (SafeSwitch, EMNLP 2025; TrajGuard, ACL 2026; HiddenGuard, 2024; ShieldHead, ACL 2025) deploys probes that must make decisions at every layer or every token. A probe with high accuracy but high CR is unreliable for real-time deployment — it will oscillate between \"safe\" and \"unsafe\" across adjacent layers, making the monitoring signal noisy and the intervention policy unstable. CR captures exactly this failure mode.\n\n**Response D — CR-composite has methodological precedent:**\n> Multiplicative composites of accuracy and stability have been independently proposed:\n> - CCE (Zhong et al., 2025): `S = Conf × Cons` for anomaly detection\n> - CUES (Alqudah et al., 2026): geometric mean of accuracy, calibration, equity, and stability\n> - Keoliya et al. (2025): document that \"existing methods struggle to jointly optimize accuracy and stability\"\n> \n> CR-composite (BA × (1−CR)) follows this established pattern.\n\n### Recommended framing in paper:\n\nRather than claiming CR is a metric others already use, frame it as:\n\n1. **A formalization of an observed phenomenon** (overthinking, cross-layer disagreement) that lacked a dedicated metric\n2. **A natural metric for the online monitoring setting** — where prediction trajectory stability is operationally critical\n3. **An instance of a broader pattern** (ZCR, eDFR, Lipschitz stability) applied to a new domain\n\n### Key citations to add:\n\n| Citation | Purpose |\n|----------|---------|\n| Kaya et al. (ICML 2019) | Overthinking + confusion metric = prior recognition of cross-layer prediction instability |\n| Zhou et al. / PABEE (NeurIPS 2020) | Cross-layer prediction agreement as a practically useful signal |\n| Keoliya et al. (arXiv 2025) | Accuracy-stability joint optimization difficulty; oscillation-penalizing metric |\n| Miller & Blume (arXiv 2026) | Decision Flip Rate as a flip-counting instability diagnostic |\n| Larsen (arXiv 2025) | Safety Stability Index; 18–28% of prompts exhibit decision flips |\n| SafeSwitch (EMNLP 2025) | Online safety monitoring = the deployment context where CR matters |\n| TrajGuard (ACL 2026) | Hidden-state trajectories carry \"more stable risk signals\" |\n| Wildi (arXiv 2026) | Sign accuracy ↔ zero-crossing rate connection in optimization |\n\n---\n\n## 6. Search Coverage Log\n\n| Direction | Keywords Searched | Papers Examined | Verified via WebFetch |\n|-----------|------------------|-----------------|----------------------|\n| 1. CR / sign change in probes | 7 combinations | ~20 | 8 |\n| 2. Composite metrics | 7 combinations | ~22 | 6 |\n| 3. SafeSwitch / online safety | 8 combinations | ~25 | 10 |\n| 4. Layer selection stability | 7 combinations | ~20 | 8 |\n| 5. Temporal consistency | 8 combinations | ~20 | 7 |\n| Extra: ZCR, overthinking, FER | 5 combinations | ~10 | 4 |\n| **Total** | **42 combinations** | **~117 papers** | **43 verified** |\n"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T05:09:47.894925+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/crossing_rate_literature_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T05:09:47.895074+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T05:09:47.895199+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T05:09:47.895319+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "crossing_rate_literature_survey",
  "type": "report",
  "description": "Literature survey on crossing rate / prediction stability metrics in safety detection literature. Covers 42 keyword combinations, ~117 papers examined, 43 verified. Confirms CR is novel; provides rebuttal strategy with 8 key citations.",
  "project": "contrastive_trace_safety",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/crossing_rate_literature_survey.md",
  "tags": "['literature-survey', 'crossing-rate', 'rebuttal', 'red-team']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "crossing_rate_literature_survey",
    "type": "report",
    "description": "Literature survey on crossing rate / prediction stability metrics in safety detection literature. Covers 42 keyword combinations, ~117 papers examined, 43 verified. Confirms CR is novel; provides rebuttal strategy with 8 key citations.",
    "project": "contrastive_trace_safety",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/crossing_rate_literature_survey.md",
    "tags": "['literature-survey', 'crossing-rate', 'rebuttal', 'red-team']"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T05:09:47.895462+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_8b4999\", \"name\": \"crossing_rate_literature_survey\", \"type\": \"report\", \"description\": \"Literature survey on crossing rate / prediction stability metrics in safety detection literature. Covers 42 keyword combinations, ~117 papers examined, 43 verified. Confirms CR is novel; provides rebuttal strategy with 8 key citations.\", \"path\": \"projects/contrastive_trace_safety/artifacts/_project/report/crossing_rate_literature_survey.md\", \"url\": null, \"project\": \"contrastive_trace_safety\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T05:09:20.614463+00:00\", \"tags\": [\"literature-survey\", \"crossing-rate\", \"rebuttal\", \"red-team\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T05:09:47.895596+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'completed', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'completed', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'completed', 'activeForm': 'Compiling final literature survey report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Direction 1: Crossing rate / sign change rate in probe evaluation', 'status': 'completed', 'activeForm': 'Searching for crossing rate in probe evaluation literature'}, {'content': 'Direction 2: Composite metrics (accuracy × stability) in safety monitoring', 'status': 'completed', 'activeForm': 'Searching for composite metrics in safety monitoring'}, {'content': 'Direction 3: SafeSwitch and online safety detection systems', 'status': 'completed', 'activeForm': 'Searching for online safety detection systems'}, {'content': 'Direction 4: Layer selection stability/consistency criteria', 'status': 'completed', 'activeForm': 'Searching for layer selection stability criteria'}, {'content': 'Direction 5: Prediction consistency / temporal consistency in sequential monitoring', 'status': 'completed', 'activeForm': 'Searching for temporal consistency in sequential monitoring'}, {'content': 'Extra searches: early exit, calibration, latent safety', 'status': 'completed', 'activeForm': 'Running extra keyword searches'}, {'content': 'Compile final report to artifacts/crossing_rate_literature_survey.md', 'status': 'completed', 'activeForm': 'Compiling final literature survey report'}]"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T05:09:47.895779+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_crossing_rate_literature_20260520T045810",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-20T05:09:47.895948+00:00_

报告已完成，保存在 `artifacts/crossing_rate_literature_survey.md`。

## 核心结论

**CR 作为精确定义的 metric 是新颖的**——42 组关键词、~117 篇论文中无人定义过 "跨层 probe 预测翻转计数"。但这不是 straw man，因为：

### 最强反驳证据

1. **Kaya et al. (ICML 2019)** — "overthinking" + confusion metric 已识别跨层预测翻转问题，但未形式化为评估指标
2. **PABEE (NeurIPS 2020)** — 直接用跨层预测一致性作为 early exit 判据，证明这个信号有实际价值
3. **Miller & Blume (2026)** — 独立提出 Decision Flip Rate (eDFR)，概念上等价于 CR（只是在不同轴上计数翻转）
4. **Keoliya et al. (2025)** — 提出惩罚振荡的 stability metric，发现 "existing methods struggle to jointly optimize accuracy and stability"
5. **Wildi (2026)** — 在计量经济学中显式连接 sign accuracy 和 zero-crossing rate，数学上与 CR-composite 分解完全平行

### 建议 framing

不要说 "别人也用 CR"，而是说：
- CR 形式化了已被观察到但未被量化的现象（overthinking, cross-layer disagreement）
- CR 是 online safety monitoring 场景的自然需求（SafeSwitch, TrajGuard 等系统需要稳定的监控信号）
- CR 是 ZCR / eDFR / Lipschitz stability 这类既有概念在新领域的实例化

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_crossing_rate_literature_20260520T045810"
}
```

</details>

---
