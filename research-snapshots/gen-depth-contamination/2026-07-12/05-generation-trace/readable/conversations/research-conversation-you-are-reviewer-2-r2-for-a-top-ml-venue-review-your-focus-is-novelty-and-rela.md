# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty and Related Work**. Use a 6-point scale: 1=St

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7f5b69bb1b927267.jsonl`
- **Structured JSON:** [`cd1d569e50aba6b6434a.json`](../../sessions/cd/cd1d569e50aba6b6434a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-16T08:21:33.904Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty and Related Work**. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target acceptance rate ~25%.

## Paper Summary

**Title**: "The Discrimination Boundary of Recursive Text Generation: Measuring K* Across Architectures, Decoding Strategies, and Domains"

**Core idea**: The paper studies "generational depth" of text — how many successive model-generation steps separate a document from human-authored seed text. It formalizes recursive generation as an iterated lossy channel and uses the Data Processing Inequality (DPI) to prove existence of a finite discrimination boundary K*: the maximum depth at which adjacent depths remain statistically distinguishable. K* is defined operationally as the largest depth k where pairwise AUC (LightGBM on 15 statistical features) between depth k-1 and k exceeds θ=0.60 (bootstrap 95% CI lower bound).

**Contributions claimed**:
1. C1: Introduce OBD (Ordered Bag of Distributions) framework with 15 model-free statistical features for depth estimation; define K*
2. C2: First systematic measurement of K* across 6 model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B, Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B), 4 decoding strategies, 2 text domains (C4, Wikipedia), 3 text lengths. Under standard conditions (≥256 tokens, T≥0.9, compatible scorer), 14/14 conditions yield K*=2.
3. C3: Identify three principled boundary conditions (short text, low temperature, cross-architecture scorer mismatch) where K* degrades to 1, each explained by DPI
4. C4: K*=2 provides actionable curation guidance: binary filtering outperforms graduated depth-weighting (MMLU 0.5941 vs 0.5892, p=0.003 at 50% contamination)

**Related Work (as presented in paper §2)**:
- Machine-generated text detection: DetectGPT, watermarking, statistical tests — binary human-vs-synthetic, no depth estimation
- Model collapse and recursive training: work showing iterative training on self-generated data leads to distributional collapse; theoretical analyses of self-consuming generative processes — macro phenomenon, no individual document depth detection
- Data selection and curation: DSIR, D4, DoReMi — distribution-matched data selection without recursive depth estimation. One work applies binary MGT detection to importance resampling for preventing model collapse.

**Method summary**:
- Depth chains: D0 (human) → model continuation → D1 → ... → D5, 5K C4/Wikipedia docs
- 15D features: surprisal statistics (8), vocabulary distribution (5), structural (2). Surprisal computed by a "scorer" model (may differ from generator).
- LightGBM classifier per adjacent depth pair, 5-fold CV, 1000 bootstrap, permutation tests
- K* = largest k where 1v2 CI lower > θ=0.60 and perm p<0.05

**Experiments**: 
- Cross-architecture: 6 models, 4/6 clearly K*=2, Mistral K*=1 (boundary case)
- Cross-scorer 4×4 matrix: 12/16 K*=2
- Decoding: 4 configs on Pythia, 3/4 K*=2 (T=0.7 fails)
- Length: 128/256/512 tokens, K*=2 for ≥256
- Domain: C4 vs Wikipedia, both K*=2
- Ecological: retrain-chain with LoRA, K*=2
- Curation: binary vs graduated filtering at 10/30/50% doses, binary wins
- CC validation: 50K docs from CC 2025/2026, correlational only

**Paper structure**: 9 pages, 10 tables, anonymous submission.

## Your Review Task

Evaluate **novelty and related work** rigorously. Address:

1. **Novelty assessment**: How novel is the core contribution? Is the problem formulation (generational depth as a dimension, K* as discrimination boundary) genuinely new? Is the DPI-based theoretical framing original?
2. **Related work completeness**: Are there important missing references? Is the positioning against prior work fair and accurate?
3. **Incremental vs substantial**: Does this represent a substantial advance or is it incremental over existing MGT detection work?
4. **Significance and impact**: Will this influence future research or practice? Is the K*=2 finding surprising or expected?
5. **Writing quality**: Is the paper well-written? Clear? Well-organized?
6. **Presentation**: Are the results presented clearly? Any misleading framing?

Consider relevant areas:
- Model collapse literature (Shumailov et al., 2024; Alemohammad et al., 2023; Dohmatob et al., 2024)
- MGT detection (DetectGPT, Fast-DetectGPT, DNA-GPT, Binoculars, etc.)
- Data curation/selection (DSIR, D4, DoReMi, FineWeb)
- Information-theoretic analyses of language models
- Iterative/self-consuming generative processes

Output format:
```
## R2: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
- S1: ...
- S2: ...
...

### Weaknesses
- W1: ...
- W2: ...
...

### Questions for Authors
- Q1: ...
...

### Minor Issues
- ...

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "cfd7ee72-138c-40b9-8747-5d64974e9ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:21:33.912Z_

```json
{
  "parentUuid": "cfd7ee72-138c-40b9-8747-5d64974e9ea2",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
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
  "uuid": "0e9ebaab-81a3-42f1-aed0-da5d95435e19",
  "timestamp": "2026-05-16T08:21:33.912Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T08:21:37.222Z_



I need to read the paper and related project files to provide a thorough review. Let me start by loading the necessary tools and reading the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9ebaab-81a3-42f1-aed0-da5d95435e19",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vW8AbSAzbzCmVmFUWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2c9ddaf-2f00-47b7-83b1-6ae0c5c2e48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PaSnbcY959yFcTWn6QqAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7268,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7268,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-16T08:21:39.271Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NGC6NvsaPVMMJsN6ahQWpN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2c9ddaf-2f00-47b7-83b1-6ae0c5c2e48e",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vW8AbSAzbzCmVmFUWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd0c79da-340d-424e-bb4c-26c42d4d40a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PaSnbcY959yFcTWn6QqAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7268,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7268,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 5 · 2026-05-16T08:21:39.274Z_

<details><summary>↩ Tool result · `toolu_01NGC6NvsaPVMMJsN6ahQWpN`</summary>

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
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd0c79da-340d-424e-bb4c-26c42d4d40a0",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "91076cca-4c73-4d3e-a180-e231c87595c0",
  "sourceToolAssistantUUID": "bd0c79da-340d-424e-bb4c-26c42d4d40a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T08:21:41.069Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KkeWBHMhQqXzPGgjHhSKSM`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91076cca-4c73-4d3e-a180-e231c87595c0",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vW8AbSAzbzCmVmFUWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a82bc0a-cc66-43c9-b48c-5c9a0b4e4113",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PaSnbcY959yFcTWn6QqAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7268,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7268,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-16T08:21:41.113Z_

<details><summary>↩ Tool result · `toolu_01KkeWBHMhQqXzPGgjHhSKSM`</summary>

```text
artifacts/_project/report/related_work_structure.md
docs/claim_routes.md
artifacts/_project/report/claim_routes.md
docs/theory_framework.md
artifacts/_project/report/theory_framework.md
artifacts/_project/report/full_study_plan.md
task_context/history/reviewer/loop_1.md
artifacts/_project/report/methodology_draft.md
docs/figure_plan.md
artifacts/_project/report/figure_plan.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260512T200328/best/review_report.md
artifacts/dream_reports/dream_20260512T200328/median/review_report.md
artifacts/dream_reports/dream_20260512T200328/worst/review_report.md
artifacts/_project/report/literature_scan_2025_2026.md
artifacts/literature_scan_2025_2026.md
docs/methodology_draft.md
docs/related_work_structure.md
docs/full_study_plan.md
task_context/history/director/loop_1.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_1.md
artifacts/_project/report/literature_positioning_notes.md
artifacts/_project/report/literature_positioning_notes_d23bf4.md
artifacts/literature_positioning_notes.md
.claude/sessions/agent_35bd0e91/CLAUDE.md
.claude/sessions/agent_35bd0e91/AGENTS.md
artifacts/dream_reports/dream_20260513T080728/best/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/median/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/best/review_report.md
artifacts/dream_reports/dream_20260513T080728/median/review_report.md
artifacts/dream_reports/dream_20260513T080728/worst/review_report.md
artifacts/exp_003_decoding_ablation/report/exp003_analysis_report.md
task_context/history/agent/loop_2.md
artifacts/_project/paper/discussion_outline.md
artifacts/discussion_outline.md
artifacts/exp_015_neural_probe/intermediate/exp015_script_info.md
artifacts/exp_003_decoding_ablation/chart/exp003_figure_info.md
task_context/history/director/loop_2.md
task_context/history/reviewer/loop_3.md
artifacts/_project/paper/discussion_section_info.md
artifacts/_project/paper/conclusion_section_info.md
task_context/history/agent/loop_2_1778715887.md
task_context/history/agent/loop_3.md
task_context/history/reviewer/loop_4.md
task_context/history/director/loop_3.md
task_context/history/agent/loop_4.md
artifacts/exp-004/report/vram_assessment.md
artifacts/_project/paper/discussion_v2.md
artifacts/drafts/discussion_v2.md
artifacts/drafts/neural_probe_section.md
task_context/history/agent/loop_3_1778739204.md
artifacts/drafts/related_work_audit.md
artifacts/drafts/consistency_audit.md
artifacts/drafts/abstract_v2.md
artifacts/_project/paper/abstract_v2.md
task_context/history/agent/loop_5.md
artifacts/_project/report/reviewer_pass_round1.md
artifacts/drafts/reviewer_pass_round1.md
.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/philox/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_6.md
task_context/history/agent/loop_4_1778763765.md
artifacts/_project/report/paper_consistency_audit.md
artifacts/paper_consistency_audit.md
task_context/history/reviewer/loop_6.md
task_context/history/agent/loop_7.md
.claude/sessions/agent_21f01c55/CLAUDE.md
.claude/sessions/agent_21f01c55/AGENTS.md
artifacts/exp_006_graduated_filtering/intermediate/c3_fallback_outline.md
artifacts/c3_fallback_outline.md
task_context/history/agent/loop_8.md
task_context/history/reviewer/loop_7.md
task_context/history/agent/loop_8_1778819711.md
task_context/history/director/loop_4.md
task_context/history/agent/loop_9.md
.claude/sessions/agent_593954ae/CLAUDE.md
.claude/sessions/agent_593954ae/AGENTS.md
artifacts/review_reports/round_1.md
task_context/history/reviewer/loop_8.md
task_context/history/director/loop_5.md
task_context/history/agent/loop_10.md
task_context/history/agent/loop_10_1778859645.md
task_context/history/reviewer/loop_9.md
task_context/director.md
task_context/history/agent/loop_11.md
docs/paper/integration_templates.md
task_context/history/reviewer/loop_10.md
task_context/history/agent/loop_11_1778890108.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a82bc0a-cc66-43c9-b48c-5c9a0b4e4113",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "f70f7516-766f-4b5a-8331-c621c526a62e",
  "sourceToolAssistantUUID": "2a82bc0a-cc66-43c9-b48c-5c9a0b4e4113",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T08:21:41.267Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EX1PEGt5scdPsR9gPLg3t1`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f70f7516-766f-4b5a-8331-c621c526a62e",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vW8AbSAzbzCmVmFUWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3b8e371-509d-4aad-87d1-21995fa093ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PaSnbcY959yFcTWn6QqAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7268,
      "cache_read_input_tokens": 8250,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 315,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7268,
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

_source line 9 · 2026-05-16T08:21:41.321Z_

<details><summary>↩ Tool result · `toolu_01EX1PEGt5scdPsR9gPLg3t1`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex
artifacts/drafts/neural_probe_analysis.tex
artifacts/c3_contingency_versions.tex
artifacts/exp-006/paper/c3_contingency_versions.tex
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
docs/paper/related_work.tex
docs/paper/experiments_c3.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/experiments_c1.tex
docs/paper/introduction.tex
docs/paper/appendix_extended.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/discussion.tex
artifacts/dream_reports/dream_20260516T073047/best/paper.tex
artifacts/dream_reports/dream_20260516T073047/median/paper.tex
artifacts/dream_reports/dream_20260516T073047/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3b8e371-509d-4aad-87d1-21995fa093ea",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "68c4d417-4251-4bda-bf53-e4b329b8e5d3",
  "sourceToolAssistantUUID": "a3b8e371-509d-4aad-87d1-21995fa093ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-16T08:21:50.142Z_



Let me read the paper and key project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68c4d417-4251-4bda-bf53-e4b329b8e5d3",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vWfieFywMxRycsDYJS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb8d4439-289f-44dc-9a46-4487f9b990bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUqLmDnCNeaQrRvQMNVGbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4469,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 11 · 2026-05-16T08:21:51.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_014XcTQrVUpcSognrr9MryZL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb8d4439-289f-44dc-9a46-4487f9b990bb",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vWfieFywMxRycsDYJS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "120b8fc6-299f-4901-a2fb-94826832d903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUqLmDnCNeaQrRvQMNVGbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4469,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 12 · 2026-05-16T08:21:51.658Z_

<details><summary>↩ Tool result · `toolu_014XcTQrVUpcSognrr9MryZL`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$---the maximum depth at which adjacent generations remain distinguishable---using 15 statistical features and an OBD-LightGBM classifier.
36	Across 6 model configurations (1B--7B, base and instruct) and 4 decoding strategies, $\Kempirical{=}2$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$), consistent across all 10 tested conditions under self-scoring (most marginal: 0.2\,pp above $\theta$): a single generation step is reliably detectable, but the second renders text statistically indistinguishable from deeper synthetic content---a \emph{one-wash laundering} effect.
37	Model-free statistical features enable 80--92\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$), and cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model.
38	Both supervised classification and zero-shot frontier LLMs fail comparably at depths ${\geq}2$ (recall 14--22\% vs.\ 8--38\%), providing converging evidence consistent with $\Kempirical{=}2$ reflecting a data-intrinsic boundary rather than a method limitation.
39	Downstream, $\Kempirical{=}2$ correctly predicts that binary curation minimizes degradation most effectively among all tested strategies.
40	\end{abstract}
41	
42	% === Section 1: Introduction ===
43	\input{introduction}
44	
45	% === Section 2: Related Work ===
46	\input{related_work}
47	
48	% === Section 3: Method ===
49	\input{method}
50	
51	% === Section 4: Experiments ===
52	\input{experiments_c1}
53	
54	% === Section 5: K*-Aware Data Filtering ===
55	\input{experiments_c3}
56	
57	% === Section 6: Discussion ===
58	\input{discussion}
59	
60	% === Section 7: Conclusion ===
61	\input{conclusion}
62	
63	% === Limitations (ACL required, unnumbered) ===
64	\clearpage
65	\section*{Limitations}
66	
67	Our findings are bounded by (1)~model scale ($\leq$7B, with only one 7B configuration tested; a dedicated base-vs.-instruct ablation at 1.5B confirms $\Kempirical{=}2$ is independent of instruction tuning, but the 7B condition uses cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\Kempirical$ is a conservative upper bound on retrain-chain $\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; all ten conditions yield point-estimate $\Kempirical{=}2$ at $\theta{=}0.60$, with 9/10 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\Kempirical{=}1$, Section~\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\Kempirical^{\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\rho \geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\tau \approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\Kempirical$ from 2 to 1 for continuation-mode data (Table~\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\approx}$191 subword tokens after truncation) while depth~1+ are machine-generated (mean 193--256 tokens depending on model; Table~\ref{tab:token_length}); this length asymmetry makes 0v1 detection \emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (within-model range $\leq$ 6 tokens; EOS truncation rates stable across depths within each model), so the critical $\Kempirical{=}2$ finding---based on 1v2 vs.\ 2v3 comparisons---is unaffected by this confound (Section~\ref{sec:length_confound}).
68	Detailed analysis appears in Appendix~\ref{sec:extended_limitations}.
69	
70	% === Ethics Statement (ACL required, unnumbered) ===
71	\section*{Ethics Statement}
72	
73	Generational depth estimation is intended for data curation and corpus auditing---positive-sum applications that improve training data quality.
74	Our experiments use the publicly available C4 corpus and do not involve personally identifiable information.
75	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
76	
77	\bibliography{references}
78	
79	\input{appendix}
80	\input{appendix_extended}
81	
82	\end{document}
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "120b8fc6-299f-4901-a2fb-94826832d903",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "ce464cb7-6db3-42f7-a5bf-a2b215f455e2",
  "sourceToolAssistantUUID": "120b8fc6-299f-4901-a2fb-94826832d903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T08:21:52.091Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RYZfzaeJFWhRuk1jRdJZeZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce464cb7-6db3-42f7-a5bf-a2b215f455e2",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vWfieFywMxRycsDYJS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a479ebb5-f6d6-4aa2-a8ce-2ed2e117d47f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUqLmDnCNeaQrRvQMNVGbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4469,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 14 · 2026-05-16T08:21:52.120Z_

<details><summary>↩ Tool result · `toolu_01RYZfzaeJFWhRuk1jRdJZeZ`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, linguistic diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence dynamics~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
6	Our $\Kstar$ aligns with Schaeffer et al.'s Family~B (collapsing variance); our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro retrain-chain dynamics but provides no per-text depth estimation---the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation; CoDeC~\cite{zawalski2026codec} addresses data contamination via membership inference.
11	Robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}.
12	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}, but no method estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling---a special case of our framework when $\Kstar = 1$.
16	Without knowing $\Kempirical$, curation strategies cannot determine whether finer-grained depth weighting adds signal or noise.
17	
18	\paragraph{Ordinal classification and probing.}
19	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends the probing protocol~\cite{alain2017understanding, belinkov2022probing} to measure how representation choice affects the discrimination boundary.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a479ebb5-f6d6-4aa2-a8ce-2ed2e117d47f",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "9827e188-bd31-499e-ad05-0ae96283f9d6",
  "sourceToolAssistantUUID": "a479ebb5-f6d6-4aa2-a8ce-2ed2e117d47f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T08:21:52.960Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X6k1epxRfFeQUhHsgysRAK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9827e188-bd31-499e-ad05-0ae96283f9d6",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vWfieFywMxRycsDYJS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c61e2cba-f75c-4eab-bc1a-cd6554da7a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUqLmDnCNeaQrRvQMNVGbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 15518,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4469
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 15518,
          "cache_creation_input_tokens": 4469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4469,
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

_source line 16 · 2026-05-16T08:21:52.967Z_

<details><summary>↩ Tool result · `toolu_01X6k1epxRfFeQUhHsgysRAK`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	The gap cuts across three communities.
11	Binary detection methods~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate, and their confidence scores fail to discriminate beyond the binary boundary (Section~\ref{sec:binary_confidence}).
12	Data contamination detection via membership inference~\cite{zawalski2026codec} addresses a different question (whether specific texts appeared in training data) and likewise provides no depth signal.
13	The model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} characterizes recursive degradation at the macro level but provides no per-text depth estimation tool.
14	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
15	No existing method estimates how many rounds of recursive generation a text has undergone, nor quantifies the boundary beyond which such estimation becomes infeasible.
16	
17	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
18	We empirically measure $\Kempirical$---the maximum depth at which a classifier reliably distinguishes adjacent generations---using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
19	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the bootstrap 95\% CI for pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$.
20	
21	Our contributions center on two empirical findings:
22	\begin{enumerate}[label=(\alph*),nosep]
23	  \item \textbf{$\Kempirical = 2$ at $\theta{=}0.60$} (Cohen's $h{\approx}0.20$) across 6 model configurations (1B--7B, base and instruct) and 4 decoding strategies, with all 1v2 CI lower bounds exceeding $\theta$ and all 2v3 CI upper bounds below $\theta$ ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
24	  Generation mode appears to have a larger effect than model architecture ($+$8.4\,pp rewrite vs.\ continuation within Qwen; $3.9$\,pp spread across continuation-mode models), though formal interaction testing is beyond our current scope.
25	  This is independently corroborated: both supervised OBD and zero-shot frontier LLMs fail comparably at depths $\geq 2$ (McNemar $p > 0.05$), providing converging evidence consistent with $\Kempirical{=}2$ reflecting a data-intrinsic boundary (Section~\ref{sec:why_kstar}).
26	  \item \textbf{Model-free cross-model transfer}: 15 statistical features enable 80--92\% accuracy retention across continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$; Section~\ref{sec:transfer}), with surprisal-variance features dominating ($\rho \geq 0.85$).
27	  Cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model.
28	\end{enumerate}
29	
30	\noindent As a downstream validation, $\Kempirical = 2$ correctly predicts the strategy ordering in data filtering: binary curation at the $\Kempirical$ boundary minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$), while graduated ($0.5892$) and surprisal-based ($0.5894$) strategies provide no additional benefit (Section~\ref{sec:filtering}).
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c61e2cba-f75c-4eab-bc1a-cd6554da7a50",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "3531e81e-9d2d-4dd1-8c12-e30b6cc0ae1c",
  "sourceToolAssistantUUID": "c61e2cba-f75c-4eab-bc1a-cd6554da7a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T08:21:57.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_0139PsTbbEEBvNoAeiyMiSgD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3531e81e-9d2d-4dd1-8c12-e30b6cc0ae1c",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vXXjD3riAY2qNYyk1S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "490001a8-e2ea-4511-8236-caf449011473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dMmfiCWBtmw3bDJDG5hS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4285,
      "cache_read_input_tokens": 19987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 18 · 2026-05-16T08:21:57.113Z_

<details><summary>↩ Tool result · `toolu_0139PsTbbEEBvNoAeiyMiSgD`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this guarantees a finite $\Ktheory$ beyond which adjacent generations are indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ corresponds to Cohen's $h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.} (a conventional small-effect-size threshold), well above the permutation null (95th percentile $< 0.55$).
25	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	$\theta{=}0.60$ is justified independently by Cohen's $h \approx 0.20$ and a 10K permutation test ($p < 0.002$); the filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier as-is rather than re-optimizing $\theta$, avoiding circularity.
27	$\Kempirical$ varies with $\theta$: at $\theta{=}0.55$, $\Kempirical{=}2$--$3$ depending on configuration ($\Kempirical{=}3$ for Qwen variants, $\Kempirical{=}2$ for Pythia and OLMo); at $\theta{=}0.65$, continuation modes drop to $\Kempirical{=}1$; at $\theta{=}0.70$, $\Kempirical{=}1$ universally (Section~\ref{sec:kstar_boundary}).
28	
29	\subsection{Features and Classifier}
30	\label{sec:features}
31	
32	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
33	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
34	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
35	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
36	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
37	
38	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
39	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
40	
41	\subsection{Experimental Setup}
42	\label{sec:experimental_setup}
43	
44	We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
45	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
46	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
47	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
48	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{Experimental configurations.}
54	\label{tab:setup}
55	\begin{tabular}{llcc}
56	\toprule
57	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
58	\midrule
59	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
60	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
61	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
62	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
63	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
64	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "490001a8-e2ea-4511-8236-caf449011473",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "a8236223-565b-4457-9f65-6098f6c9d791",
  "sourceToolAssistantUUID": "490001a8-e2ea-4511-8236-caf449011473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T08:21:57.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_019qw12XeLYz3S1wuzRAPFnC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8236223-565b-4457-9f65-6098f6c9d791",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vXXjD3riAY2qNYyk1S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa4118e3-e6dd-4515-9bef-009a3dc9b569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dMmfiCWBtmw3bDJDG5hS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4285,
      "cache_read_input_tokens": 19987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 20 · 2026-05-16T08:21:57.940Z_

<details><summary>↩ Tool result · `toolu_019qw12XeLYz3S1wuzRAPFnC`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on six model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, Qwen2.5-1.5B-Instruct in both rewrite and continuation modes, Qwen2.5-1.5B (base) in continuation mode, and Qwen2.5-7B in continuation mode (cross-scale scoring with Qwen2.5-1.5B).
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical = 2$ Across All Configurations}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.}
17	\label{tab:kstar_ci}
18	\begin{tabular}{lcccccccccc}
19	\toprule
20	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
21	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
22	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
23	\midrule
24	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
25	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
26	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
27	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
28	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
29	\bottomrule
30	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all five 1v2 comparisons.} \\
31	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
32	\end{tabular}
33	\end{table*}
34	
35	\begin{figure}[t]
36	\centering
37	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
38	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
39	\label{fig:auc_decay}
40	\end{figure}
41	
42	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show a consistent pattern: 0v1 discrimination is near-perfect ($\auc \geq 0.96$), followed by a sharp drop at 1v2 ($\auc$: 0.6112--0.6955), with 2v3 falling below $\theta$ (0.5492--0.5893) and deeper pairs converging toward chance.
43	All five 1v2 point estimates exceed $\theta$, confirmed by bootstrap CIs (most marginal lower bound: Qwen-1.5B-continuation at 0.602); all five 2v3 point estimates and CI upper bounds fall below $\theta$ (permutation $p < 0.001$ for all boundary comparisons).
44	This establishes $\Kempirical = 2$ as consistent across all 10 tested conditions (6 independent model-mode configurations and 4 decoding-strategy ablation variants on the Qwen-rewrite configuration; Table~\ref{tab:s2_decoding}).
45	Under cross-model scoring, Qwen-continuation $\Kempirical$ drops to 1 (Section~\ref{sec:transfer}), indicating a model-specific component in the most marginal 1v2 boundary signal.
46	The sharp step-function pattern reflects the concentration of information loss: human text exhibits heavy-tailed, bursty surprisal patterns that are substantially altered by even a single autoregressive pass.
47	Subsequent generations operate on already-smoothed distributions, yielding progressively smaller marginal changes that fall below detectability within two steps.
48	
49	The 1v2 $\auc$ varies across models: Qwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\approx$ Qwen-continuation (0.6112).
50	The spread due to generation mode within a single model ($\Delta = 8.4$\,pp) exceeds the spread across models in the same mode ($\Delta = 3.9$\,pp), suggesting that generation mode appears to have a larger effect than model architecture, though formal interaction testing is beyond our current scope.
51	
52	\paragraph{Cross-scale validation.}
53	Qwen2.5-7B in continuation mode (scored by Qwen2.5-1.5B) confirms $\Kempirical = 2$: 1v2 $\auc = 0.6168$ $[0.608,\,0.626]$ (CI lower bound $> \theta$), 2v3 $\auc = 0.5492$ $[0.539,\,0.559]$ (Table~\ref{tab:kstar_ci}).
54	The 0v1 $\auc$ drops to 0.9638 (${\sim}$3\,pp below ${\leq}$1.5B models), consistent with larger models generating more human-like text; yet the $\Kempirical$ boundary remains unchanged, extending the invariance from 1.5B to 7B.
55	
56	\paragraph{Base-vs.-instruct ablation.}
57	Qwen2.5-1.5B (base) in continuation mode yields $\Kempirical = 2$: 0v1 $\auc = 0.987$, 1v2 $\auc = 0.626$, 2v3 $\auc = 0.550$ (Table~\ref{tab:setup}).
58	The 0v1 signal is slightly lower than the matched Instruct model ($0.987$ vs.\ $0.997$), consistent with base models producing less stylistically divergent text, but $\Kempirical$ is identical, confirming that the depth boundary is not an instruction-tuning artifact.
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
63	\caption{$\Kempirical$ as a function of $\theta$ across six model-mode configurations, computed using the 95\% CI lower bound criterion (Eq.~\ref{eq:kstar}). The dashed line marks the operational threshold $\theta{=}0.60$ used throughout, where all configurations yield $\Kempirical{=}2$. Qwen-rewrite yields the highest $\Kempirical$ at all $\theta$; at $\theta{=}0.70$, $\Kempirical{=}1$ universally.}
64	\label{fig:kstar_theta}
65	\end{figure}
66	
67	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$ (conservative CI-lower-bound variant): unanimous $\Kempirical = 2$ holds within $\theta \in [0.580, 0.600]$.
68	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite and Qwen-continuation while Pythia, OLMo, and Qwen-7B remain at $\Kempirical = 2$; at $\theta = 0.65$, all continuation modes drop to $\Kempirical = 1$ while rewrite retains $\Kempirical = 2$; at $\theta = 0.70$, $\Kempirical = 1$ universally.
69	All four decoding configurations (greedy, nucleus $p{=}0.9$, $T{=}0.70$, $T{=}1.2$) likewise yield $\Kempirical = 2$ at $\theta = 0.60$, with 1v2 $\auc$ in $[0.6866, 0.7039]$ (bootstrap CI lower bounds $\geq 0.677$, all ${>}\theta$; Table~\ref{tab:s2_decoding}).
70	Bootstrap CIs confirm 2v3 upper bounds below $\theta$ for 3/4 decoding variants; the nucleus $p{=}0.9$ condition (2v3 $\auc = 0.5917$, CI $[0.582, 0.601]$) has its upper bound marginally straddling $\theta$ by 0.001, consistent with measurement noise.
71	
72	%% ====================================================================
73	\subsection{Cross-Model Transfer}
74	\label{sec:transfer}
75	
76	\begin{figure}[t]
77	\centering
78	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
79	\caption{Cross-model transfer heatmap (6-class ordinal accuracy). Pythia$\leftrightarrow$OLMo achieves 90--92\% retention; Qwen-rewrite$\to$continuation-mode models: 61--63\%.}
80	\label{fig:transfer_heatmap}
81	\end{figure}
82	
83	The universality of $\Kempirical = 2$ raises a natural question: does the depth boundary reflect properties of the text itself, or generator-specific artifacts?
84	Cross-model transfer experiments address this directly.
85	
86	Figure~\ref{fig:transfer_heatmap} shows the transfer accuracy matrix (full matrix in Table~\ref{tab:s1_transfer}).
87	Continuation-mode transfer is high: Pythia$\leftrightarrow$OLMo retains 90--92\% of within-model accuracy, Qwen-cont$\leftrightarrow$Pythia 84--85\%, and Qwen-cont$\leftrightarrow$OLMo 80--85\%.
88	At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 for all pairs (range: 0.963--0.991).
89	These retention rates suggest that depth features transfer across generators when computed by a fixed scorer.
90	The high retention indicates that the relative importance of depth features is encoded in distributional text properties---surprisal variance, lexical diversity---rather than in generator-specific fingerprints, enabling generator-agnostic deployment when a consistent scorer is used.
91	
92	Qwen-rewrite classifiers transfer poorly (61--63\% retention to Pythia/OLMo), confirming reliance on mode-specific artifacts.
93	Cross-mode transfer is asymmetric: continuation$\to$rewrite retains 89\% while rewrite$\to$continuation retains 82\%, indicating that continuation-mode features form a generalizable subset.
94	
95	\paragraph{Cross-scorer validation.}
96	To test whether depth signals depend on the scorer model, we replace the Qwen self-scorer with two alternative scorers (Pythia-1.4B, OLMo-1B) for feature extraction on Qwen-generated text.
97	Feature rankings remain highly correlated across all scorer pairs (Spearman $\rho > 0.90$), confirming that feature ordering is text-intrinsic.
98	Absolute discriminability, however, is scorer-sensitive at the $\Kempirical$ boundary.
99	For Qwen-rewrite, $\Kempirical = 2$ is scorer-invariant: 1v2 $\auc$ remains stable under cross-scoring (Pythia: 0.7012, OLMo: 0.6947; self-scorer baseline: 0.6955; Table~\ref{tab:crossscorer}).
100	For Qwen-continuation---already the most marginal self-scorer condition (CI lower bound exceeds $\theta$ by only 0.2\,pp; Table~\ref{tab:kstar_ci})---$\Kempirical$ drops from 2 to 1 under both alternative scorers (1v2 $\auc$: $0.6112 \to 0.5923$ [Pythia], $0.5858$ [OLMo], both below $\theta$).
101	This dissociation---scorer-invariant feature rankings but scorer-sensitive boundary classification---indicates that cross-scoring preserves the relative importance structure of depth features while attenuating the absolute signal, with consequences only where the self-scorer margin is already thin.
102	Crucially, both alternative scorers agree on $\Kempirical$ for each generation mode ($\Kempirical = 2$ for rewrite, $1$ for continuation), indicating that $\Kempirical$ is determined by the generation process rather than the choice of scoring model.
103	
104	%% ====================================================================
105	\subsection{Feature Degradation Ordering}
106	\label{sec:feature_degradation}
107	
108	\begin{table*}[t]
109	\centering
110	\small
111	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
112	\label{tab:top_features}
113	\begin{tabular}{cllll}
114	\toprule
115	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
116	\midrule
117	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
118	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
119	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
120	\bottomrule
121	\end{tabular}
122	\end{table*}
123	
124	Having established that depth signals transfer across models, we next identify which specific features drive this transferable signal.
125	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
126	The top-3 features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---are shared across all three families, all measuring surprisal variability.
127	This shared ordering reveals a common mechanism: autoregressive generation progressively damps surprisal variability.
128	\texttt{surp\_d1\_std}---the standard deviation of token-to-token surprisal changes---decreases monotonically with depth as the irregular spikes characteristic of human writing are smoothed out, while \texttt{surp\_std} and \texttt{surp\_d2\_std} reflect the narrowing of the overall surprisal distribution.
129	Qwen-rewrite diverges, with \texttt{freq\_entropy} as its top feature---corroborating the cross-model transfer findings.
130	A limitation is that depth-pair-level agreement weakens ($\tau \approx 0.37$ at 1v2), indicating per-feature contributions at the boundary vary across models.
131	
132	%% ====================================================================
133	\subsection{Generation Mode}
134	\label{sec:generation_mode}
135	
136	The preceding analyses use continuation mode as the default; we now compare generation modes to validate this choice.
137	Within Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\auc = 0.6955$ versus continuation's $0.6112$ ($\Delta = +8.4$\,pp).
138	The amplified detectability reflects instruction-following artifacts that are discriminable but mode-specific rather than transferable across generators, as confirmed by the poor cross-model transfer of rewrite-mode classifiers (61--63\% vs.\ 80--92\% for continuation).
139	Continuation mode is therefore recommended as the canonical condition for cross-model comparisons.
140	
141	%% ====================================================================
142	\subsection{Neural Probe}
143	\label{sec:neural_probe}
144	
145	A natural question is whether $\Kempirical = 2$ is an artifact of our 15-dimensional feature set, or whether richer representations can push the boundary deeper.
146	Replacing hand-crafted features with frozen encoder hidden states (MLP probe; Table~\ref{tab:s7_neural_probe}), we evaluate $\Kempirical^{\text{neural}}$ across all three model families (Table~\ref{tab:neural_probe_crossmodel}).
147	Qwen-continuation achieves 2v3 $\auc = 0.6159$ $[0.610, 0.622]$, yielding $\Kempirical^{\text{neural}} = 3$.
148	However, Pythia ($\auc_{2v3} = 0.5963$ $[0.589, 0.603]$) and OLMo ($\auc_{2v3} = 0.5892$ $[0.582, 0.597]$) both fall below $\theta$, giving $\Kempirical^{\text{neural}} = 2$.
149	The Qwen-only elevation likely reflects self-familiarity: each model's frozen embeddings probe its own generations, and Qwen's instruction-tuned representations encode mode-specific artifacts that boost boundary discrimination---the same artifacts that transfer poorly across model families (Section~\ref{sec:transfer}).
150	The 15D model-free features yield $\Kempirical = 2$ universally (3/3 models), validating their choice for cross-model deployment.
151	
152	\begin{minipage}{\columnwidth}
153	\centering
154	\footnotesize
155	\captionof{table}{Neural probe pairwise $\auc$ with bootstrap 95\% CIs (frozen-encoder MLP). $\Kempirical^{\text{neural}} = 3$ for Qwen only; Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$.}
156	\label{tab:neural_probe_crossmodel}
157	\begin{tabular}{lccc}
158	\toprule
159	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
160	\midrule
161	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
162	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
163	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
164	\bottomrule
165	\end{tabular}
166	\end{minipage}
167	
168	%% ====================================================================
169	\subsection{Binary Detector Confidence and Depth}
170	\label{sec:binary_confidence}
171	
172	A natural question is whether binary detector confidence---even without ordinal training---implicitly encodes depth information.
173	We evaluate DivEye~\cite{basani2026diveye} (log-PPL) and Binoculars~\cite{hans2024binoculars} (cross-model PPL ratio; observer: Pythia-1.4B, performer: OLMo-1B) across all four model-mode configurations, reporting both Spearman $\rho$ with true depth and 6-class depth classification accuracy.
174	
175	Moderate rank correlations exist ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}), but these do not translate to practical depth discrimination: binary detectors effectively separate human from machine text (0v1 $\auc$: 0.54--0.85, depending on observer-generator matching), but confidence scores collapse to noise for depths $\geq 1$.
176	Six-class accuracy confirms this: most configurations fall at or below the random baseline of 0.167; only Qwen-rewrite (0.199) and Qwen-continuation (0.183) marginally exceed it, while Pythia (0.130) and OLMo (0.127) fall below.
177	Pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$ for most detector--generator pairs: all pairs $\geq$1v2 fall to 0.50--0.60, well below the OBD-15D baseline (0v1 $> 0.99$, 1v2: 0.61--0.70, $\Kempirical = 2$).
178	Multiple conditions exhibit non-monotonic AUC at deeper pairs (e.g., 2v3 $<$ 3v4 $<$ 4v5 for Qwen-continuation), violating the monotonic ordering required for depth interpretation.
179	The observed rank correlation is thus an artifact of 0v1 separation rather than fine-grained depth signal.
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa4118e3-e6dd-4515-9bef-009a3dc9b569",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "2a9bafde-9a1f-4dd5-bd80-ae1a57ec4ee0",
  "sourceToolAssistantUUID": "aa4118e3-e6dd-4515-9bef-009a3dc9b569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T08:21:58.426Z_

<details open><summary>🔧 Tool call — Read · `toolu_011o1A7rA6cq9DsHBXv224nV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a9bafde-9a1f-4dd5-bd80-ae1a57ec4ee0",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vXXjD3riAY2qNYyk1S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47e49f93-a643-43be-a104-6e12f138c865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dMmfiCWBtmw3bDJDG5hS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4285,
      "cache_read_input_tokens": 19987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 22 · 2026-05-16T08:21:58.443Z_

<details><summary>↩ Tool result · `toolu_011o1A7rA6cq9DsHBXv224nV`</summary>

```text
1	\section{Application: $\Kstar$-Aware Data Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
6	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{Downstream filtering performance (5 seeds). Full $\alpha$ sweep and significance tests in Appendix~\ref{sec:extended_limitations}.}
12	\label{tab:tab_filtering_main}
13	\input{tables/tab_filtering_main}
14	\end{table}
15	
16	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
17	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
18	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
19	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
20	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47e49f93-a643-43be-a104-6e12f138c865",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "db436142-7dfa-401b-ac87-f468bb35ba39",
  "sourceToolAssistantUUID": "47e49f93-a643-43be-a104-6e12f138c865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T08:21:58.648Z_

<details open><summary>🔧 Tool call — Read · `toolu_016EXdZkyPWxTGLLwWGm4eK8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db436142-7dfa-401b-ac87-f468bb35ba39",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vXXjD3riAY2qNYyk1S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa461713-3ac7-4920-98ce-7219c980801e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dMmfiCWBtmw3bDJDG5hS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4285,
      "cache_read_input_tokens": 19987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 24 · 2026-05-16T08:21:58.665Z_

<details><summary>↩ Tool result · `toolu_016EXdZkyPWxTGLLwWGm4eK8`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{The One-Wash Laundering Effect}
5	\label{sec:why_kstar}
6	\label{sec:one_wash}
7	
8	The shallowness of $\Kempirical = 2$ reflects the concentration of information loss: the 0v1 boundary is near-trivially separable ($\auc \geq 0.96$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$---the generation operator acts as a lossy channel with diminishing marginal information loss.
9	Consistency across four decoding strategies (Table~\ref{tab:s2_decoding}) reinforces that $\Kempirical$ is governed by the generation process rather than the sampling algorithm.
10	Even at the most marginal 1v2 condition (Qwen-continuation, CI lower bound exceeds $\theta$ by only 0.2\,pp), $\Kempirical = 2$ survives under self-scoring; on the 2v3 side, CI upper bounds confirm non-discrimination in 9/10 conditions, with the single borderline case (nucleus $p{=}0.9$, CI upper${} = 0.601$) consistent with measurement noise at near-threshold values.
11	Cross-scale validation at 7B (Section~\ref{sec:kstar_boundary}) extends this from 1.5B to 7B despite reduced 0v1 signal ($0.9638$ vs.\ $> 0.99$).
12	
13	The practical consequence is a three-tier taxonomy: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
14	A single generation pass suffices to render text statistically indistinguishable from multiply recycled content---a \emph{one-wash laundering} effect that limits depth-aware corpus curation to a binary boundary.
15	This connects to model collapse: Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations; our prompt-chain results show an analogous per-text pattern.
16	
17	Per-depth analysis provides the most direct evidence that this boundary is not methodological.
18	OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 69--77\% depth-0 recall and 8--38\% for depths 2--4 (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
19	This convergence across fundamentally different approaches---supervised statistical classification and zero-shot frontier LLMs---provides converging evidence that the saturation reflects a data-intrinsic boundary rather than a method limitation.
20	Binary detector confidence corroborates: despite moderate Spearman correlations ($|\rho|$ up to 0.46), 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), and Qwen-rewrite exhibits a sign reversal ($\rho > 0$), disqualifying confidence as a reliable depth proxy.
21	
22	\subsection{Why Graduated Filtering Fails}
23	\label{sec:negative_graduated}
24	
25	Since 2v3 $\auc < \theta$ for all configurations, depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise into importance weights, explaining the monotonic improvement with $\alpha$ as it converges toward binary thresholding (Appendix~\ref{sec:extended_limitations}).
26	DSIR fails for a different reason---bigram feature hashing captures domain shift but not depth-correlated distributional signatures.
27	
28	\subsection{Representation Dependence of the Boundary}
29	\label{sec:repr_dependence}
30	
31	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$ (Table~\ref{tab:neural_probe_crossmodel}).
32	The hierarchy $\Kempirical^{15\text{D}}{=}2 < \Kempirical^{\text{neural}} \in \{2,3\}$ reflects an interpretability--sensitivity tradeoff: learned representations recover additional depth signal sufficient to push $\Kempirical$ to 3 for one model (Qwen), but this gain is model-dependent---the 15D features trade one depth level of sensitivity for cross-model universality (10/10 conditions $\Kempirical{=}2$, 3/3 models identical), making them the preferred operational choice.
33	Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\Kempirical = 2$ to 1, while rewrite-mode $\Kempirical = 2$ is preserved---$\Kempirical$ is governed by the generation operator rather than the scoring model.
34	A base-vs.-instruct ablation at 1.5B confirms $\Kempirical{=}2$ is independent of instruction tuning (Section~\ref{sec:kstar_boundary}).
35	A potential length confound is also ruled out: in continuation mode the generation prompt is discarded so all depths $\geq 1$ are purely machine-generated, token counts are stable within depths 1--5 ($\leq$ 6-token range), and the length asymmetry (depth~0 ${\sim}$191 vs.\ depth~1+ 193--256 tokens) makes 0v1 detection more conservative, not inflated (Appendix~\ref{sec:extended_limitations}).
36	\label{sec:length_confound}
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa461713-3ac7-4920-98ce-7219c980801e",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "0ee9feb2-3a22-4b37-a3ac-54712e2bfd90",
  "sourceToolAssistantUUID": "aa461713-3ac7-4920-98ce-7219c980801e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T08:22:05.611Z_

<details open><summary>🔧 Tool call — Read · `toolu_018B9dwf5H3PJZ2GD61fdMCZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ee9feb2-3a22-4b37-a3ac-54712e2bfd90",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vXxdfa7eqPNhgSEJyq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d8dd695-c06a-4c45-9b38-29a794f9e8ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Bip7zYmTR1SMrLCC3L46v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10964,
      "cache_read_input_tokens": 24272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 26 · 2026-05-16T08:22:05.618Z_

<details><summary>↩ Tool result · `toolu_018B9dwf5H3PJZ2GD61fdMCZ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic measurement of the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	Two primary findings emerge:
6	(a)~$\Kempirical = 2$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$), consistent across all tested configurations from 1B to 7B under self-scoring ($p \leq 0.002$; most marginal: 0.2\,pp above $\theta$), implying a one-wash laundering effect.
7	Convergent failure of both supervised classifiers and frontier LLMs at depths $\geq 2$ (McNemar $p > 0.05$) provides converging evidence consistent with this reflecting a data-intrinsic boundary rather than a method limitation.
8	Generation mode appears to have a larger effect than model architecture ($\Delta = 8.4$\,pp), but rewrite-mode advantages are non-transferable (61--63\% vs.\ 80--92\%).
9	(b)~Model-free statistical features enable 80--92\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$), with surprisal-variance features dominating across model families ($\rho \geq 0.85$); cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model, enabling depth estimation for text from unknown generators without retraining.
10	As a downstream validation, $\Kempirical = 2$ correctly predicts the optimal curation granularity: binary filtering minimizes degradation most effectively; finer ordinal structure and depth-agnostic methods (DSIR) provide no benefit.
11	
12	Future work includes scaling beyond 7B, extending to naturalistic multi-domain corpora, and developing model-agnostic neural probes.
13	Our prompt-chain protocol isolates generation-level information loss in a controlled setting; establishing the retrain-chain $\Kstar$ relationship, where training dynamics introduce additional degradation, is a natural next step.
14	The 100\% synthetic filtering experiment characterizes an upper bound; mixed-corpus dose-response studies remain open.
15	Our base-vs.-instruct ablation confirms $\Kempirical{=}2$ is independent of instruction tuning, though broader architecture variation warrants further investigation.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d8dd695-c06a-4c45-9b38-29a794f9e8ab",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "a3beae5a-d72a-4ef6-b0d5-5f0a926fc5b8",
  "sourceToolAssistantUUID": "6d8dd695-c06a-4c45-9b38-29a794f9e8ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T08:22:06.633Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DvKPu5GXo2jN97DZVhuwAr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3beae5a-d72a-4ef6-b0d5-5f0a926fc5b8",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vXxdfa7eqPNhgSEJyq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f418f386-cab1-45bd-a563-7e7cd678741c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Bip7zYmTR1SMrLCC3L46v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10964,
      "cache_read_input_tokens": 24272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 28 · 2026-05-16T08:22:06.640Z_

<details><summary>↩ Tool result · `toolu_01DvKPu5GXo2jN97DZVhuwAr`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
21	\begin{table*}[t]
22	  \centering
23	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
24	  \label{tab:s1_transfer}
25	  \begin{tabular}{lcccc}
26	    \toprule
27	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
28	    \cmidrule(lr){2-5}
29	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
30	    \midrule
31	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
32	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
33	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
34	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
35	    \bottomrule
36	  \end{tabular}
37	  \vspace{4pt}
38	
39	  \footnotesize
40	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
41	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
42	\end{table*}
43	
44	%%% Table S2: Decoding Ablation AUC (exp-003)
45	\begin{table*}[t]
46	  \centering
47	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
48	  \label{tab:s2_decoding}
49	  \footnotesize
50	  \begin{tabular}{lcccc}
51	    \toprule
52	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
53	    \midrule
54	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
55	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
56	    \cmidrule(lr){1-5}
57	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
58	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
59	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
60	    \midrule
61	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
62	    \midrule
63	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
64	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
65	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
66	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
67	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
68	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
69	    \bottomrule
70	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
71	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
72	  \end{tabular}
73	\end{table*}
74	
75	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
76	\begin{table*}[t]
77	  \centering
78	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
79	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
80	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
81	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
82	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
83	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
84	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
85	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.
86	    Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}.}
87	  \label{tab:s3_llm_zeroshot}
88	
89	  \vspace{0.5em}
90	  \begin{subtable}{0.48\textwidth}
91	    \centering
92	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
93	    \label{tab:s3a_gpt55}
94	    \small
95	    \begin{tabular}{lcccccc}
96	      \toprule
97	      & \multicolumn{5}{c}{Predicted Depth} & \\
98	      \cmidrule(lr){2-6}
99	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
100	      \midrule
101	      0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
102	      1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
103	      2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
104	      3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
105	      4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
106	      \bottomrule
107	    \end{tabular}
108	  \end{subtable}
109	  \hfill
110	  \begin{subtable}{0.48\textwidth}
111	    \centering
112	    \caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}
113	    \label{tab:s3b_claude}
114	    \small
115	    \begin{tabular}{lcccccc}
116	      \toprule
117	      & \multicolumn{5}{c}{Predicted Depth} & \\
118	      \cmidrule(lr){2-6}
119	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
120	      \midrule
121	      0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
122	      1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
123	      2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
124	      3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
125	      4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
126	      \bottomrule
127	    \end{tabular}
128	  \end{subtable}
129	\end{table*}
130	
131	\begin{table}[t]
132	  \centering
133	  \small
134	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
135	  \label{tab:s3c_perdepth}
136	  \begin{tabular}{lccccc}
137	    \toprule
138	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
139	    \midrule
140	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
141	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
142	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
143	    \bottomrule
144	  \end{tabular}
145	\end{table}
146	
147	%%% Table: Token Length and EOS Truncation Analysis
148	\begin{table*}[t]
149	  \centering
150	  \small
151	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound} for discussion.}
152	  \label{tab:token_length}
153	  \begin{tabular}{lcccccccc}
154	    \toprule
155	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
156	    \cmidrule(lr){2-7}
157	    \textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \textbf{EOS Trunc.\ (\%)} & \textbf{Severity} \\
158	    \midrule
159	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
160	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
161	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\
162	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\
163	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
164	    \midrule
165	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
166	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
167	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
168	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
169	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
170	    \bottomrule
171	  \end{tabular}
172	
173	  \vspace{4pt}
174	  \footnotesize
175	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
176	\end{table*}
177	
178	\clearpage
179	\section{Supplementary Details}
180	
181	%%% Table S4: Dataset Statistics
182	\begin{table}[t]
183	  \centering
184	  \small
185	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
186	  \label{tab:s4_dataset_stats}
187	  \begin{tabular}{clrl}
188	    \toprule
189	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
190	    \midrule
191	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
192	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
193	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
194	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
195	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
196	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
197	    \midrule
198	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
199	    \bottomrule
200	  \end{tabular}
201	\end{table}
202	
203	%%% Table S5: Complete 15-D Feature Descriptions
204	\begin{table*}[t]
205	  \centering
206	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
207	  \label{tab:s5_features}
208	  \begin{tabular}{llp{0.45\textwidth}l}
209	    \toprule
210	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
211	    \midrule
212	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
213	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
214	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
215	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
216	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
217	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
218	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
219	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
220	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
221	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
222	    \midrule
223	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
224	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
225	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
226	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
227	    \midrule
228	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
229	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
230	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
231	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
232	    \bottomrule
233	  \end{tabular}
234	\end{table*}
235	
236	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
237	\begin{table*}[t]
238	\begin{minipage}[t]{0.45\textwidth}
239	  \centering
240	  \small
241	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
242	  \label{tab:s6_lgbm_params}
243	  \begin{tabular}{ll}
244	    \toprule
245	    \textbf{Parameter} & \textbf{Value} \\
246	    \midrule
247	    \texttt{n\_estimators}      & 200 \\
248	    \texttt{learning\_rate}     & 0.05 \\
249	    \texttt{max\_depth}         & 6 \\
250	    \texttt{num\_leaves}        & 31 \\
251	    \texttt{verbose}            & $-1$ \\
252	    \texttt{n\_jobs}            & $-1$ (all cores) \\
253	    Cross-validation            & 5-fold GroupKFold \\
254	    Grouping key                & \texttt{doc\_id} \\
255	    Objective                   & Binary (per depth pair) \\
256	    \bottomrule
257	  \end{tabular}
258	\end{minipage}\hfill
259	\begin{minipage}[t]{0.52\textwidth}
260	  \centering
261	  \small
262	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
263	  \label{tab:s7_neural_probe}
264	  \resizebox{\textwidth}{!}{%
265	  \begin{tabular}{ll}
266	    \toprule
267	    \textbf{Component} & \textbf{Details} \\
268	    \midrule
269	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
270	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
271	    Representation    & Last hidden state, attention-masked avg pool \\
272	    Embedding dim     & 1536 / 2048 / 2048 \\
273	    Max sequence len   & 512 tokens \\
274	    \midrule
275	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
276	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
277	    Activations       & ReLU \\
278	    Dropout           & 0.1 (after each hidden layer) \\
279	    Output            & 6-class softmax \\
280	    \midrule
281	    \multicolumn{2}{l}{\textit{Training}} \\
282	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
283	    Loss              & Cross-entropy \\
284	    Batch size        & 256 \\
285	    Max epochs        & 20 \\
286	    Early stopping    & Patience = 5 (validation loss) \\
287	    Cross-validation  & 5-fold GroupKFold \\
288	    \bottomrule
289	  \end{tabular}%
290	  }
291	\end{minipage}
292	\end{table*}
293	
294	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
295	\begin{table*}[t]
296	  \centering
297	  \footnotesize
298	  \caption{Pairwise AUC with bootstrap 95\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\theta = 0.60$. Permutation $p$-values test $H_0\colon \auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\,vs.\,4 ($p = 0.064$) and 4\,vs.\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}
299	  \label{tab:s8_cv_folds}
300	  \begin{tabular}{lcccc}
301	    \toprule
302	    \textbf{Depth Pair} & \textbf{Qwen-rewrite} & \textbf{Pythia-1.4B} & \textbf{OLMo-1B} & \textbf{Qwen-cont} \\
303	    \midrule
304	    0 vs.\ 1
305	      & $.996\;[.995,\,.997]$
306	      & $.993\;[.992,\,.994]$
307	      & $.997\;[.996,\,.998]$
308	      & $.997\;[.996,\,.998]$ \\
309	    1 vs.\ 2
310	      & $.696\;[.686,\,.704]$
311	      & $.654\;[.645,\,.663]$
312	      & $.615\;[.605,\,.625]$
313	      & $.611\;[.602,\,.621]$ \\
314	    \cmidrule(lr){1-5}
315	    2 vs.\ 3
316	      & $.589\;[.580,\,.599]$
317	      & $.551\;[.542,\,.563]$
318	      & $.550\;[.540,\,.560]$
319	      & $.561\;[.551,\,.571]$ \\
320	    3 vs.\ 4
321	      & $.544\;[.533,\,.555]$
322	      & $.515\;[.504,\,.526]$
323	      & $.509\;[.497,\,.520]^{\dagger}$
324	      & $.541\;[.531,\,.551]$ \\
325	    4 vs.\ 5
326	      & $.534\;[.524,\,.545]$
327	      & $.514\;[.502,\,.525]$
328	      & $.505\;[.493,\,.515]^{\ddagger}$
329	      & $.514\;[.504,\,.526]$ \\
330	    \bottomrule
331	  \end{tabular}
332	
333	  \vspace{4pt}
334	  \footnotesize
335	  Each cell: AUC $[95\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.
336	  ${}^{\dagger}$\,$p = 0.064$;\; ${}^{\ddagger}$\,$p = 0.232$;\; all other pairs $p < 0.01$.
337	\end{table*}
338	
339	%%% Table S9: Binary Detector Spearman ρ (exp-012)
340	\begin{table*}[t]
341	  \centering
342	  \small
343	  \caption{Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}
344	  \label{tab:s9_binary_spearman}
345	  \begin{tabular}{lcccc}
346	    \toprule
347	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
348	    \midrule
349	    \multicolumn{5}{l}{\textit{Spearman $\rho$ with true depth}} \\
350	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
351	    \quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
352	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
353	    \midrule
354	    \multicolumn{5}{l}{\textit{Classification}} \\
355	    \quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\
356	    \midrule
357	    \multicolumn{5}{l}{Random baseline: 0.167 \quad $\Kempirical^{\text{binary}} = 1$ \quad $\Kempirical^{\text{OBD}} = 2$} \\
358	    \bottomrule
359	  \end{tabular}
360	\end{table*}
361	
362	\clearpage
363	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f418f386-cab1-45bd-a563-7e7cd678741c",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "beb19c5b-e2c3-40cb-b0a5-973964f28869",
  "sourceToolAssistantUUID": "f418f386-cab1-45bd-a563-7e7cd678741c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T08:22:07.462Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019Y2dVLntkzXBco7sAyMDXG`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "literature_map.yaml",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beb19c5b-e2c3-40cb-b0a5-973964f28869",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vXxdfa7eqPNhgSEJyq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "536ed3f2-5750-435f-8839-58a715d6c476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Bip7zYmTR1SMrLCC3L46v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10964,
      "cache_read_input_tokens": 24272,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10964
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 24272,
          "cache_creation_input_tokens": 10964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10964,
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

_source line 30 · 2026-05-16T08:22:07.482Z_

<details><summary>↩ Tool result · `toolu_019Y2dVLntkzXBco7sAyMDXG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml\", \"content\": \"papers:\\n  # === Must-Cite ===\\n\\n  - id: drayson2025\\n    title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n    authors: \\\"Drayson, Yilmaz, Lampos\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n    code: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Binary MGT detection + importance resampling for collapse prevention; our depth estimator generalizes their binary detector to ordinal depth\\\"\\n    cited: false\\n    methodology: >\\n      Binary MGT detector (encoder-only transformer + classification head; best: ModernBERT-150M, AUC .986 in-dist, .943 OOD).\\n      Fine-tuned 5 epochs with label smoothing α=0.1 + temperature scaling.\\n      Sampling Importance Resampling (SIR): w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b, where q(x) = P(machine-generated), b≥1 bias term.\\n      Resample at k=1.5 (50% upsampling). Evaluated on GPT-2 and SmolLM2 (124M–1.7B).\\n    key_findings:\\n      - \\\"SIR filtering not only prevents collapse but improves over human-only training (perplexity -0.85% to -25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%)\\\"\\n      - \\\"ModernBERT achieves best detection (AUC .986 in-dist); optimal threshold 0.8674 on imbalanced data (29% human)\\\"\\n      - \\\"Curated synthetic data has positive value — outperforms oracle (perfect filter) in equal-ratio settings\\\"\\n      - \\\"Only evaluates fine-tuning (not pretraining), models ≤2B, open-ended generation only\\\"\\n    positioning_notes: >\\n      Closest prior work. Their SIR is a special case of our graduated filtering when K*=1 (binary: human vs all synthetic).\\n      We generalize binary→ordinal: estimate depth d∈{0,1,...,K*} and apply depth-graduated weights.\\n      K* tells when ordinal signal adds value over binary. They never discuss ordinal depth or multi-class estimation.\\n      Our C3 claim directly extends their framework: \\\"even coarse 3-class signal yields better calibration at decision boundaries.\\\"\\n\\n  - id: schaeffer2025position\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Schaeffer, Kazdan, Arulandu, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"framing-critical\\\"\\n    relevance: \\\"Identifies 8 definitions of model collapse across 3 families; forces us to position K* as discriminability saturation (distribution deformation), not test-loss collapse\\\"\\n    cited: false\\n    methodology: >\\n      Position paper. Surveys model collapse literature and identifies 8 distinct definitions organized in 3 families.\\n      Evaluates each definition against realistic deployment conditions. No experiments—purely analytical/argumentative.\\n    key_findings:\\n      - \\\"8 definitions in 3 families: (A) Population risk degrading [D1: catastrophic increase, D2: any increase, D3: asymptotic divergence]; (B) Distributions deforming [D4: collapsing variance, D5: scaling law change, D6: mode disappearance/entanglement, D7: tail data loss]; (C) Spurious generation [D8: hallucinated data]\\\"\\n      - \\\"Under realistic conditions (data accumulation, growing compute), catastrophic risk divergence (D1-D3) is avoidable\\\"\\n      - \\\"Real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention\\\"\\n      - \\\"Recommends researchers explicitly state which definition they study\\\"\\n    positioning_notes: >\\n      K* belongs to Family B (distributions deforming), specifically D4 (collapsing variance) + D6 (mode entanglement).\\n      K* measures when distribution deformation renders generations indistinguishable in feature space.\\n      K* is NOT about population risk (Family A). This distinction is critical for framing:\\n      we contribute a diagnostic for exactly the harms Schaeffer et al. identify as underexplored.\\n      Adopt their taxonomy explicitly in Related Work to anchor K* precisely.\\n\\n  - id: kazdan2025collapse\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Accumulate vs replace regimes affect contamination dynamics; in accumulate regime K* may shift upward\\\"\\n    cited: false\\n    methodology: >\\n      Formal comparison of 3 data regimes: Replace (train on latest synthetic only; Σ→0 a.s.),\\n      Accumulate (train on all historical data; real fraction→0 but stability holds),\\n      Accumulate-subsample (fixed budget from accumulated pool; intermediate degradation).\\n      Theory: Gaussian setting with closed-form limits. Experiments: multivariate Gaussian, KDE, LLM SFT (Gemma2-2B on HelpSteer2/TinyStories).\\n    key_findings:\\n      - \\\"Replace: covariance collapses to 0 (a.s.), W2 diverges. Collapse inevitable within 5-10 iterations\\\"\\n      - \\\"Accumulate: covariance stabilizes at σ₀²·sin(π/√n)/(π/√n). No collapse even as real data fraction→0\\\"\\n      - \\\"Accumulate-subsample: degradation plateaus rather than diverges\\\"\\n      - \\\"Cardinality of real data matters more than proportion (R²=0.59 vs 0.34)\\\"\\n    positioning_notes: >\\n      Our prompt-chain = replace regime (harshest setting). K*=2 measured under replace conditions.\\n      This makes K*=2 a conservative lower bound: under accumulate regime (more realistic), K* would shift upward.\\n      Strengthens our result: if depth estimation adds value at K*=2 under replace, it adds more under accumulate.\\n      Cite to justify experimental design and contextualize K* as regime-dependent.\\n\\n  - id: shi2025generalization\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shi, Wu, Zhang, Zhang, Tao, Qu\\\"\\n    venue: \\\"NeurIPS 2025 Spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    code: \\\"https://shilianghe007.github.io/model-collapse/\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Generalization-to-memorization transition in iterative retraining parallels our feature-space convergence; entropy decrease over iterations aligns with our depth-discriminative features\\\"\\n    cited: false\\n    methodology: >\\n      Study iterative retraining of diffusion models (DDPM) on CIFAR-10 subsets (1K–32K images).\\n      Generalization Score (GS): avg distance between generated and nearest training image.\\n      Entropy: Kozachenko-Leonenko estimator. Strong correlation: Pearson r=0.91 between entropy and log(GS).\\n      Mitigation: entropy-based data selection (greedy max-NN-distance + threshold-decay filter).\\n    key_findings:\\n      - \\\"GS drops approximately exponentially across iterations; collapse within 5-10 iterations for large datasets\\\"\\n      - \\\"Training data entropy is a direct predictor of generalization capability (r=0.91)\\\"\\n      - \\\"Entropy-based data selection mitigates memorization transition\\\"\\n      - \\\"Diffusion models only; no LLM experiments. No theoretical analysis of WHY entropy collapses\\\"\\n      - \\\"Generated images form tight local clusters while overall variance remains relatively stable\\\"\\n    positioning_notes: >\\n      Parallel phenomenon across modalities: their entropy decline ↔ our JSD decrease (0.27→0.004).\\n      Their \\\"GS drops exponentially\\\" ↔ our feature-space divergence vanishes rapidly → K*=2.\\n      Key distinction: they measure output-distribution entropy; we measure discriminability in feature space.\\n      K* complements their entropy metric: operationalizes \\\"at what depth does entropy decline = indistinguishability?\\\"\\n      Their clustering-while-variance-stable parallels our depth features converging before global statistics.\\n      Cite for cross-modal validation of convergence phenomenon.\\n\\n  # === Should-Cite ===\\n\\n  - id: basani2026diveye\\n    title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n    authors: \\\"Basani, Chen\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2509.18880\\\"\\n    code: \\\"https://github.com/IBM/diveye\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Surprisal diversity features as potential baseline for depth estimation; zero-shot detector outperforms prior work by 33.2%\\\"\\n    cited: false\\n\\n  - id: amin2025escaping\\n    title: \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\"\\n    authors: \\\"Amin et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.08924\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Boosting-inspired framework showing weak signal suffices for iterative training; motivates practical utility of imperfect depth estimators\\\"\\n    cited: false\\n\\n  - id: zawalski2026codec\\n    title: \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: \\\"Zawalski et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    category: \\\"contamination\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary contamination detection via ICL confidence shifts; complementary to our finer-grained depth estimation approach\\\"\\n    cited: false\\n\\n  - id: gambetta2025surplexity\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse\\\"\\n    authors: \\\"Gambetta et al.\\\"\\n    venue: \\\"arXiv preprint 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Surprise-based collapse metric; surplexity scores as potential feature for depth estimation pipeline and baseline comparison\\\"\\n    cited: false\\n\\n  - id: zhang2024minkpp\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang, Zheng, Gao, Miao\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary detection baseline; does not distinguish generational depth\\\"\\n    cited: false\\n\\n  - id: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal\\\"\\n    venue: \\\"Nature 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Seminal model collapse result; describes macro phenomenon but provides no detection tool for depth\\\"\\n    cited: false\\n\\n  - id: alemohammad2024selfconsuming\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Casco-Rodriguez, Luber, Babaei, Letizia, Bastani, Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Theoretical and empirical analysis of iterative generative training; complements Shumailov with formal convergence analysis\\\"\\n    cited: false\\n\\n  - id: dohmatob2024model\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Feng, Yang, Charton, Kempe\\\"\\n    venue: \\\"ICML 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Scaling law perspective on collapse; tail distribution loss aligns with our observed feature convergence\\\"\\n    cited: false\\n\\n  - id: xie2023dsir\\n    title: \\\"Data Selection with Importance Resampling\\\"\\n    authors: \\\"Xie, Santurkar, Ma, Liang\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Distribution-matching data selection baseline; does not estimate recursive depth\\\"\\n    cited: false\\n\\n  - id: tirumala2024d4\\n    title: \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\"\\n    authors: \\\"Tirumala, Markosyan, Zettlemoyer, Aghajanyan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Deduplication + diversification baseline for data curation; orthogonal to depth-based filtering\\\"\\n    cited: false\\n\\n  - id: xie2024doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Domain reweighting for pretraining; does not consider generational depth dimension\\\"\\n    cited: false\\n\\n  - id: kirchenbauer2023watermark\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: \\\"Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"watermarking\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Provenance tracking via watermarking; complementary approach to depth estimation when watermarks are available\\\"\\n    cited: false\\n\\n  - id: zellers2019grover\\n    title: \\\"Defending Against Neural Fake News\\\"\\n    authors: \\\"Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Early neural text detection; binary classification paradigm that our ordinal approach generalizes\\\"\\n    cited: false\\n\\n  - id: ippolito2020detection\\n    title: \\\"Automatic Detection of Generated Text is Easiest when Humans are Fooled\\\"\\n    authors: \\\"Ippolito, Duckworth, Callison-Burch, Eck\\\"\\n    venue: \\\"ACL 2020\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Binary detection difficulty analysis; does not consider multi-generational depth\\\"\\n    cited: false\\n\\n  # === New additions (scan 2026-04-28 to 2026-05-14) ===\\n\\n  - id: falahati2026curated\\n    title: \\\"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences\\\"\\n    authors: \\\"Falahati, Amiri, Larson, Golab\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2605.07724\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Proves pluralistic reward-based curation prevents collapse via Nash bargaining convergence; directly relevant to our graduated filtering—multi-reward curation is orthogonal to depth-based curation, potentially complementary\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Shows that curation strategy matters for collapse prevention: single-reward collapses, multi-reward stabilizes.\\n      Our depth estimator provides a different curation axis: instead of multiple rewards, we use generational depth.\\n      Potential synergy: combine their pluralistic rewards with our depth signal for even stronger filtering.\\n      Does NOT address generational depth or K*. No direct challenge to K*=2.\\n\\n  - id: mady2026feataugmented\\n    title: \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\"\\n    authors: \\\"Mady, Reschke, Schuller\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2605.03969\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Attention-based linguistic feature fusion for cross-domain/cross-generator binary detection; DeBERTa-v3-base+FeatAttn achieves 85.9% balanced accuracy under distribution shift on M4. Feature augmentation architecture applicable to depth estimation pipeline\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Binary detector (human vs AI) with strong cross-generator generalization via feature augmentation.\\n      Their FeatAttn module could be adapted for our ordinal depth classifier—fuse linguistic features with encoder representations.\\n      Key limitation: binary only, no depth awareness. In-domain 99.5% but brittle under shift.\\n      Our K* result implies even perfect binary detection hits diminishing returns past depth 2.\\n\\n  - id: pu2026generator\\n    title: \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\"\\n    authors: \\\"Pu, Cheng, Yuan, Wu, Bi\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2604.13692\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Generator-agnostic detection via disentangled representations (dual-bottleneck + cross-view regularization); up to 24.2% accuracy gain on MAGE benchmark (20 LLMs). Disentanglement of semantic vs generator artifacts is architecturally relevant for our depth estimator\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Key insight: separate semantic content from generator-specific artifacts parallels our need to isolate depth signal from generator identity.\\n      Dual-bottleneck architecture enforces compact, minimal latent codes; could inspire our depth encoder design.\\n      Tests on 20 LLMs across 7 categories but only binary classification. No multi-generation or depth estimation.\\n      Our depth estimator needs similar generator invariance: depth signal should hold across model families.\\n\", \"total_chars\": 16560, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "536ed3f2-5750-435f-8839-58a715d6c476",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "c17110ab-0246-42d4-a384-266ea9e76b6d",
  "sourceToolAssistantUUID": "536ed3f2-5750-435f-8839-58a715d6c476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T08:22:12.133Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CPJJddmev3W68nJTVdZbq3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c17110ab-0246-42d4-a384-266ea9e76b6d",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vYbqYJT42Euh4KV8Wv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f1f8006-73bf-4e68-9fe7-a5e1a1b449b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoCJ9vzztEKc1xtspPpEUG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15629,
      "cache_read_input_tokens": 35236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15629,
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

_source line 32 · 2026-05-16T08:22:12.146Z_

<details><summary>↩ Tool result · `toolu_01CPJJddmev3W68nJTVdZbq3`</summary>

```text
1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; our result establishes $\Kempirical = 2$ across all 10 conditions (1B--7B), aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\subsection{Feature Importance Across Decoding Strategies}
23	
24	Feature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\rho = 0.914$), while greedy vs.\ $T{=}1.2$ yields lower correlation ($\rho = 0.53$, nonsignificant after Bonferroni).
25	The depth boundary is robust but the optimal feature subset is strategy-dependent.
26	
27	\subsection{Scale and Neural Probe}
28	\label{sec:extended_neural_probe}
29	
30	Cross-scale validation confirms $\Kempirical = 2$ at 7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$, 2v3 $\auc = 0.5492$; Table~\ref{tab:kstar_ci}); the 7B 0v1 $\auc$ (0.9638) is ${\sim}$3\,pp lower than ${\leq}$1.5B models, consistent with larger models generating more human-like text. Scaling beyond 7B remains open.
31	
32	The neural probe yields model-dependent $\Kempirical^{\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.
33	The 15D model-free features yield $\Kempirical = 2$ universally, confirming their role as a robust lower bound across architectures.
34	
35	\subsection{LLM Zero-Shot Baseline}
36	\label{sec:extended_llm}
37	
38	GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\% (95\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\ref{tab:s3_llm_zeroshot}).
39	Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
40	When 6-class probabilities are marginalized to 5 classes ($P(d{\geq}4)$), accuracy rises to 44.4\% but concentrates in depth-4 (recall: 22\%$\to$80\%) while depths 2--3 collapse to 2--8\%; we report raw 6-class results.
41	
42	\subsection{Practical Considerations}
43	
44	All filtering strategies degrade general capabilities (MMLU: 0.6018 $\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\to$ 0.6638--0.6701); our 100\% synthetic setting is an upper bound---in mixed corpora, degradation scales with contamination fraction~\cite{shumailov2024collapse, dohmatob2024model}.
45	$\Kstar$-aware binary filtering reduces MMLU degradation by ${\sim}$50\% ($-$1.53\,pp $\to$ $-$0.77\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).
46	
47	\subsection{Extended Limitations}
48	\label{sec:extended_limitations}
49	
50	\emph{Prompt-chain versus retrain-chain.}
51	Under monotonic-degradation assumptions~\cite{shumailov2024collapse}, $\Kstar^{\text{retrain}} \leq \Kstar^{\text{prompt}}$, making $\Kempirical = 2$ a conservative estimate.
52	
53	\emph{Threshold sensitivity.}
54	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ universally (Figure~\ref{fig:kstar_theta}).
55	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
56	
57	\emph{Structural confound: token length.}
58	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
59	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
60	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
61	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
62	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
63	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
64	
65	\emph{Graduated filtering.}
66	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
67	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
68	\label{tab:pairwise_significance}
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f1f8006-73bf-4e68-9fe7-a5e1a1b449b7",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "b0787b19-d707-4a46-b500-c991ee149304",
  "sourceToolAssistantUUID": "8f1f8006-73bf-4e68-9fe7-a5e1a1b449b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T08:22:12.801Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0185iBHQaegUvEDeMAyjYdNZ`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0787b19-d707-4a46-b500-c991ee149304",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vYbqYJT42Euh4KV8Wv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6129a620-6bb2-4808-8a98-23a67317f6de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoCJ9vzztEKc1xtspPpEUG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15629,
      "cache_read_input_tokens": 35236,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15629
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 35236,
          "cache_creation_input_tokens": 15629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15629,
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

_source line 34 · 2026-05-16T08:22:12.812Z_

<details><summary>↩ Tool result · `toolu_0185iBHQaegUvEDeMAyjYdNZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6129a620-6bb2-4808-8a98-23a67317f6de",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "fa17c4a3-70de-4b46-9d19-91f9408660ef",
  "sourceToolAssistantUUID": "6129a620-6bb2-4808-8a98-23a67317f6de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T08:22:15.465Z_

Now let me check if there are previous review reports to understand how this paper has evolved.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa17c4a3-70de-4b46-9d19-91f9408660ef",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vYzezAs1Sxq8ALjygn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32e76214-9f04-4e81-960e-83f12692c4f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NVEUusSFtsJ4Kqk6Gzf4P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 50865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2576,
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

_source line 36 · 2026-05-16T08:22:17.884Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PrRDgs3kt4vcAAnYU2qN5w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260516T073047/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32e76214-9f04-4e81-960e-83f12692c4f7",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vYzezAs1Sxq8ALjygn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3070ae2b-4e83-4c02-807c-6fdc764441be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NVEUusSFtsJ4Kqk6Gzf4P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 50865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2576,
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

### Tool result

_source line 37 · 2026-05-16T08:22:17.889Z_

<details><summary>↩ Tool result · `toolu_01PrRDgs3kt4vcAAnYU2qN5w`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{natbib}
11	\usepackage{xcolor}
12	\usepackage{array}
13	
14	\newcommand{\Kstar}{K^{*}}
15	
16	\title{Recursive Generation Has a Universal Discrimination Boundary:\\
17	  $\Kstar\!=\!2$ Across Six Architecture Families at 1B--8B Scale}
18	
19	\author{
20	  Anonymous Authors
21	}
22	
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	% ============================================================
29	\begin{abstract}
30	Web-scale corpora are increasingly contaminated by recursively generated synthetic text, yet current detectors treat synthetic text as a binary category and cannot estimate how many rounds of recursive generation a passage has undergone.
31	We formalize recursive generation as an iterated lossy channel and derive, via the Data Processing Inequality (DPI), that a finite empirical discrimination boundary $\Kstar$ must exist beyond which successive generations become statistically indistinguishable.
32	Through a systematic experimental matrix spanning 18 conditions---6 model architecture families (Pythia, OLMo, Qwen, Qwen-7B, LLaMA-3.1-8B, Mistral-7B), 8 decoding configurations across 2 models, 3 text lengths, and a $4\!\times\!4$ cross-scorer matrix---we find that $\Kstar\!=\!2$ holds in 17 of 18 conditions (94\%).
33	The single exception arises in a degenerate self-scorer configuration and has a clear mechanistic explanation.
34	Two-way ANOVA confirms that the generator identity accounts for 68\% of variance in detection AUC while the scorer identity is not significant ($p\!=\!0.23$), establishing that depth signal is predominantly text-intrinsic and scorer-independent.
35	$\Kstar\!=\!2$ correctly predicts that binary filtering at the discrimination boundary outperforms graduated depth weighting, surprisal-based selection, and distribution matching for downstream task performance.
36	\end{abstract}
37	
38	% ============================================================
39	\section{Introduction}
40	\label{sec:intro}
41	
42	The proliferation of large language models (LLMs) has led to a growing concern: web-crawled training corpora increasingly contain synthetic text that was itself generated by LLMs, potentially trained on earlier synthetic outputs~\citep{shumailov2024model,alemohammad2024selfconsuming}.
43	This recursive contamination creates a \emph{generational depth} structure---generation~0 is human-written, generation~1 is model-generated from human prompts, generation~2 is model-generated from generation~1 outputs, and so on.
44	
45	Existing detection methods treat this as a binary problem: human versus machine~\citep{mitchell2023detectgpt,bao2024fastdetectgpt}.
46	Data selection methods such as DSIR~\citep{xie2023dsir} perform distribution matching without modeling recursive depth.
47	Model collapse literature~\citep{shumailov2024model,dohmatob2024tale} characterizes macro-level degradation but does not provide per-document depth estimation tools.
48	\citet{drayson2025contamination} applies binary machine-generated text detection to importance resampling, the closest prior work, but still makes binary judgments rather than estimating recursive depth.
49	
50	We ask: \emph{how many generations of recursive synthesis can a statistical detector reliably distinguish?}
51	We formalize this question through the Data Processing Inequality (DPI).
52	Treating each generation step as a noisy channel, DPI guarantees that mutual information between the original text and generation~$k$ is non-increasing in $k$.
53	This implies a finite \emph{discrimination boundary} $\Kstar_{\mathrm{theory}}$: the depth beyond which no detector can reliably separate adjacent generations.
54	We introduce $\Kstar_{\mathrm{empirical}}$, a conservative lower bound on $\Kstar_{\mathrm{theory}}$ measured using 15 hand-crafted statistical features and a LightGBM classifier with bootstrap confidence intervals.
55	
56	Our key finding is that $\Kstar\!=\!2$ is \emph{universal}: it holds across 6 architecture families (Pythia, OLMo, Qwen-1.5B, Qwen-7B, LLaMA-3.1-8B, Mistral-7B-v0.3), spanning 1B to 8B parameters, across 8 decoding configurations (greedy, nucleus $p\!\in\!\{0.9, 0.95\}$, temperature $T\!\in\!\{0.7, 1.0, 1.2\}$) tested on 2 model families, across text lengths from 128 to 512 tokens, and across a $4\!\times\!4$ generator$\times$scorer matrix.
57	In total, 17 of 18 tested conditions yield $\Kstar\!=\!2$, with the single exception attributable to a degenerate self-scorer configuration where the weakest-signal generator scores itself.
58	
59	\paragraph{Contributions.}
60	(1)~We formalize $\Kstar$ as an operational quantity derived from DPI and provide the first systematic empirical measurement.
61	(2)~We demonstrate $\Kstar\!=\!2$ universality across 6 architecture families at 1B--8B scale, 8 decoding configurations, 3 text lengths, and a $4\!\times\!4$ cross-scorer matrix (17/18 conditions).
62	(3)~We show that $\Kstar\!=\!2$ serves as an actionable data curation guideline: binary filtering at $\Kstar$ outperforms graduated weighting and alternative selection methods.
63	
64	% ============================================================
65	\section{Related Work}
66	\label{sec:related}
67	
68	\paragraph{Machine-generated text detection.}
69	Statistical detectors leverage perplexity~\citep{solaiman2019release}, log-rank perturbation~\citep{mitchell2023detectgpt}, and curvature-based metrics~\citep{bao2024fastdetectgpt} for binary classification.
70	These methods achieve high accuracy for generation-0 versus generation-1 but do not model recursive depth.
71	
72	\paragraph{Model collapse and iterative training.}
73	\citet{shumailov2024model} demonstrate that training on self-generated data leads to progressive quality degradation.
74	\citet{alemohammad2024selfconsuming} and \citet{dohmatob2024tale} provide theoretical frameworks for understanding this collapse.
75	Our work complements this line by characterizing the \emph{detection-side} boundary rather than the training-side dynamics.
76	
77	\paragraph{Data selection and curation.}
78	DSIR~\citep{xie2023dsir}, D4~\citep{tirumala2024d4}, and DoReMi~\citep{xie2024doremi} optimize training mixtures via distribution matching or domain reweighting.
79	\citet{drayson2025contamination} applies binary MGT detection to importance resampling for preventing model collapse.
80	None of these methods estimate recursive generation depth or provide a principled boundary for when depth-aware filtering adds value over binary detection.
81	
82	% ============================================================
83	\section{Method}
84	\label{sec:method}
85	
86	\subsection{Recursive Generation as an Iterated Lossy Channel}
87	\label{sec:dpi}
88	
89	Let $X_0$ denote human-written text drawn from distribution $P_0$.
90	A language model $M$ defines a stochastic channel that maps $X_k$ to $X_{k+1}$: the model reads $X_k$ (or a prompt derived from it) and generates a continuation or rewrite.
91	We consider continuation mode as our canonical condition, where $M$ is given the first $n$ tokens of $X_k$ and generates a completion.
92	
93	By the Data Processing Inequality, for any Markov chain $X_0 \to X_1 \to \cdots \to X_k$:
94	\begin{equation}
95	  I(X_0; X_k) \leq I(X_0; X_{k-1}) \leq \cdots \leq I(X_0; X_1)
96	  \label{eq:dpi}
97	\end{equation}
98	where $I(\cdot;\cdot)$ denotes mutual information.
99	Since each generation step is lossy (the model cannot perfectly reproduce its input distribution), the mutual information strictly decreases, implying the existence of a finite depth $\Kstar_{\mathrm{theory}}$ beyond which adjacent generations $X_k$ and $X_{k+1}$ are statistically indistinguishable by \emph{any} detector.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3070ae2b-4e83-4c02-807c-6fdc764441be",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "bf0b0cc5-8c6c-4377-88d9-92e5300524de",
  "sourceToolAssistantUUID": "3070ae2b-4e83-4c02-807c-6fdc764441be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T08:22:18.568Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LnUSoAESL1JKBt4Ue44QPw`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf0b0cc5-8c6c-4377-88d9-92e5300524de",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vYzezAs1Sxq8ALjygn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec78d1bb-e5e7-4ec3-a99e-ccb04470f0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NVEUusSFtsJ4Kqk6Gzf4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 50865,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 50865,
          "cache_creation_input_tokens": 2576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2576,
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

_source line 39 · 2026-05-16T08:22:18.596Z_

<details><summary>↩ Tool result · `toolu_01LnUSoAESL1JKBt4Ue44QPw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_021_length_ablation | 文本长度消融：128/256/512 tokens 下 K* 是否稳定？验证 K*=2 不依赖于 256-token 固定长度设定。Qwen2.5-1.5B (base) continuation, C4 5K, depth 0-5。 | — | — | — |\\n| exp_018_llama8b_depth | Cross-family K* 验证：LLaMA-3.1-8B continuation mode 的 K* 是否 = 2？首次超出 Qwen 家族，验证 K* universality 跨模型架构。C4 5K, depth 0-5, scorer=Qwen2.5-1.5B base。 | — | — | — |\\n| exp_019_mistral7b_depth | Cross-family K* 验证：Mistral-7B-v0.3 continuation mode 的 K* 是否 = 2？第二个非 Qwen 家族模型。C4 5K, depth 0-5, scorer=Mistral-7B-v0.3 (self-scorer)。与 exp-001/002/017 self-scoring 方法一致，exp_A_alt_scorer 已证明 scorer 不影响 K*。 | — | — | — |\\n\\n## 待处理\\n- exp_022_cross_scorer_matrix: 完整 4×4 cross-scorer 矩阵：4 generator (Qwen-rw/Qwen-cont/Pythia/OLMo) × 4 scorer (Qwen-Instruct/Qwen-base/Pythia/OLMo) 的 K* 和 pairwise AUC，量化 self-scoring advantage 并验证 scorer 独立性。（排队等待 GPU）\\n\\n## 近期结论\\n- **exp_016_base_vs_instruct** (success): Base vs Instruct K* 对比：Qwen2.5-1.5B (base) continuation mode 的 K* 是否与 exp-017 (Instruct continuation, K*=2) 一致？封堵 \\\"K*=2 是 instruct-tuning 副产物\\\" 攻击面。唯一变量 = base vs instruct。 ← 基于 exp_017_qwen_continuation\\n  [exp016_bootstrap_ci](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_016_base_vs_instruct/data/exp016_bootstrap_ci.json)\\n- **exp_003_decoding_ablation** (success): 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?）\\n  [exp003_config12_analysis](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_003_decoding_ablation/report/exp003_analysis_report.md) | [exp003_decoding_ablation_figure](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_003_decoding_ablation/chart/exp003_figure_info.md) | [exp003_bootstrap_ci](westc-26893:/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_bootstrap_ci.json)\\n- **exp_012_binary_confidence** (success): Binary detector confidence (DivEye log-PPL + Binoculars ratio) 与 true depth 的 Spearman correlation，验证 binary confidence ≠ depth。Binoculars: observer=Pythia-1.4b, performer=OLMo-1B-0724-hf。\\n\\n## 趋势\\n成功 21 / 负向 0 / 失败 0 / 共 21\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nwestc-26893: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2282, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec78d1bb-e5e7-4ec3-a99e-ccb04470f0f5",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "ead22807-4e37-4785-8236-1164e9a3c54d",
  "sourceToolAssistantUUID": "ec78d1bb-e5e7-4ec3-a99e-ccb04470f0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-16T08:22:22.027Z_

Now let me also look at previous dream review reports for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ead22807-4e37-4785-8236-1164e9a3c54d",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vZRG5hLKunTy9HqaJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b09c659-57d7-442c-8dec-c70f0256ad8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tPfZzJTQLMQTorA9ZEKYo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 53441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
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

_source line 41 · 2026-05-16T08:22:24.632Z_

<details open><summary>🔧 Tool call — Read · `toolu_016saQqMRtoUuk6qB61aGX3X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b09c659-57d7-442c-8dec-c70f0256ad8d",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vZRG5hLKunTy9HqaJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e8b17cd-440c-48fc-8c84-47e33ce0a7f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tPfZzJTQLMQTorA9ZEKYo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 53441,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 53441,
          "cache_creation_input_tokens": 3985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3985,
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

_source line 42 · 2026-05-16T08:22:24.647Z_

<details><summary>↩ Tool result · `toolu_016saQqMRtoUuk6qB61aGX3X`</summary>

```text
1	---
2	dream_id: dream_20260513T080728
3	tier: best
4	overall_score: weak accept
5	timestamp: 2026-05-13T08:53:20.291070+00:00
6	---
7	
8	# Dream Review Report: Generational Depth Contamination
9	
10	**Paper:** "Generational Depth Contamination: Measuring and Exploiting the Discrimination Boundary of Recursive Synthetic Text"
11	**Review mode:** full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)
12	**Date:** 2026-05-13
13	
14	---
15	
16	## Step 1: Independent Reviews
17	
18	### Reviewer 1 — Methods & Experiments
19	
20	**Score: 4/6 (Weak Accept) | Confidence: 4/5**
21	
22	**Strengths:**
23	- Well-structured problem formulation. The iterated lossy channel model and DPI-based argument for K*'s existence provide a clean conceptual foundation. The K*_theory vs K*_empirical distinction (Section 3.2) is correctly drawn.
24	- The decoding ablation (Table 1) establishing the greedy→standard→high-temp K* gradient (1→2→3) is the paper's most convincing finding — K* responds to a theoretically motivated control variable (effective decoding entropy), not classifier artifacts. Feature ordering consistency (ρ≥0.878, Table 2) reinforces this.
25	- Appropriate use of bootstrap 95% CIs with 10K resamples (Table 4). Transparent about the Qwen-cont instruct CI lower bound being only +0.15pp above θ.
26	- Fair graduated filtering design: binary-ours baseline isolates binary vs ordinal decision boundary with the same 15D features. Inclusion of DSIR and binary-Drayson provides additional context.
27	- Ecologically grounded validity checks: retrain-chain (Table 6-7), base vs instruct (Table 5), cross-model transfer all address natural objections.
28	- Hand-crafted features justified empirically (Table 14): 85% vs 62% cross-model transfer makes the design a structural advantage, not a compromise.
29	
30	**Weaknesses:**
31	- **θ=0.60 is unjustified.** This is the single most consequential design choice — it determines every K* value. AUC=0.60 is barely above chance (0.50). No principled derivation is provided. A different threshold (0.55 or 0.65) would produce substantially different K* values. At θ=0.55, greedy would reach K*=2; at θ=0.65, most 1.5B configs would drop to K*=1. The paper must report K* sensitivity to θ ∈ [0.55, 0.65].
32	- **DPI theory-to-practice gap wider than acknowledged.** DPI operates on the full joint distribution; empirical K* operates on 15D projections. The paper claims K* "captures genuine information-theoretic properties" but conflates classifier discriminability on a specific feature set with information-theoretic impossibility. The paper should state explicitly: K*_empirical is a lower bound determined by feature choice and threshold.
33	- **7B K*≥3 is statistically fragile.** The 2v3 CI lower=0.6015 exceeds θ=0.60 by 0.15pp on only 1K documents. A single unlucky bootstrap resample could flip this. The paper should acknowledge this fragility more prominently.
34	- **5-seed paired t-test (df=4) for graduated filtering.** The p-values (p=0.0043 MMLU) are surprisingly low for 4 degrees of freedom. Individual seed results should be reported; non-parametric alternatives or more seeds (10+) would strengthen the claim.
35	- **LoRA rank=16 retrain-chain has limited ecological validity.** Modifying <0.2% of parameters is a near-identity perturbation, far from full retraining. The result validates prompt-chain as a proxy for LoRA-level adaptation, not realistic contamination cycles.
36	- **Common Crawl validation is weak.** ρ=-0.288 and ρ=-0.342 explain <12% of variance, with no ground truth. Lower-quality web text would also correlate with lower AlignScore regardless of generational depth.
37	- **Domain sensitivity unexamined.** All experiments use C4 English web text. K* likely varies across domains (scientific, code, dialogue). No analysis provided.
38	- **Surprisal features use the same model family** that generated the text, creating a self-referential signal. The 85% cross-model transfer partially addresses this, but the 15% retention loss may reflect exactly this component.
39	
40	**Questions for Authors:**
41	1. What are K* values at θ = {0.55, 0.575, 0.625, 0.65}? Is the qualitative gradient preserved?
42	2. Have you tested intermediate injection rates (15%, 20%) to identify the exact significance transition point?
43	3. Have you considered a full fine-tuning retrain chain (even at small scale, e.g., Pythia-160M)?
44	4. If you remove all 5 surprisal features, what happens to K*?
45	5. Does optimal α shift with injection rate?
46	
47	---
48	
49	### Reviewer 2 — Novelty & Related Work
50	
51	**Score: 4/6 (Weak Accept) | Confidence: 4/5**
52	
53	**Strengths:**
54	- The shift from binary detection to ordinal depth estimation is a genuine reframing that opens new research directions. Framing depth as a measurable, controllable quantity (not just a binary label) is a real conceptual contribution.
55	- The K* controllability gradient is the paper's strongest novelty claim — two independent causal pathways (model scale, decoding entropy) demonstrate K* captures channel properties, not classifier artifacts. This goes beyond simply measuring K*=2.
56	- Comprehensive experimental coverage: 4 model configurations, decoding ablation, retrain-chain validation, cross-model transfer, LLM zero-shot baseline, binary detector comparison, learned vs hand-crafted features, Common Crawl validation. The breadth of supporting analyses is impressive for a single paper.
57	- The binary-ours comparison design is methodologically sound: same features, same classifier, only switching binary vs ordinal decision → clean causal identification of the ordinal signal's value.
58	
59	**Weaknesses:**
60	- **DPI application is textbook, not novel.** The iterated lossy channel + DPI argument is standard information theory. The contribution is the empirical measurement and exploitation of K*, not the theoretical framework. The paper oversells the information-theoretic framing relative to its actual novelty.
61	- **K*=2 has narrow practical utility.** Graduated filtering with a 3-class ordinal signal (human/gen-1/gen-2+) reduces to a single soft threshold on gen-1 data — close to "binary with a soft middle category." The gap between this and binary-Drayson's importance resampling is conceptual rather than dramatic.
62	- **Related work gaps.** Missing citations:
63	  - Watermarking literature (Kirchenbauer et al., 2023) — relevant because watermarking provides an alternative depth-tracking mechanism
64	  - Self-refinement / iterative generation literature — texts may undergo multiple LLM passes without being "recursive contamination"
65	  - Schaeffer et al. (2025) taxonomy of model collapse regimes — directly relevant to framing
66	  - Kazdan et al. (2025) accumulate/replace regimes — adjacent work on iterative training dynamics
67	  - Membership inference connections — depth estimation is related to membership inference across training stages
68	- **C1/C3 numbering gap.** The paper lists contributions as C1 and C3, skipping C2. The review context mentions "degradation ordering" as a contribution (C2) that was apparently demoted. The numbering artifact is confusing and suggests incomplete revision.
69	- **Drayson comparison not fully controlled.** Drayson et al. (2025) use soft importance resampling weights, not hard binary decisions. The graduated vs binary-Drayson comparison doesn't cleanly isolate ordinal signal from weighting scheme differences — Drayson also uses soft weights, just derived from binary confidence rather than ordinal depth.
70	- **"Model-agnostic" claim needs qualification.** The 15D features include 5 surprisal features computed using a reference model. If the reference model matches the generating model, the features are model-specific. Cross-model transfer (85%) shows partial but not full generalization. The claim should be qualified as "partially model-agnostic."
71	- **Writing quality.** The paper is generally well-written but references are broken (appearing as [?] throughout), and the C1/C3 numbering gap disrupts readability.
72	
73	**Questions for Authors:**
74	1. Why is C2 (degradation ordering) missing from the contribution list? Is Table 2 the remnant of a C2 claim?
75	2. How do you position this work against watermarking-based provenance tracking, which could in principle track generational depth?
76	3. If graduated filtering is applied on top of Drayson's importance resampling (rather than replacing it), do gains stack?
77	4. What reference model is used for surprisal computation in the cross-model transfer experiment?
78	5. How does K* behave for non-English text or code?
79	
80	---
81	
82	## Step 2: Cross-Sharing Observations
83	
84	**Points of agreement (both reviewers independently flagged):**
85	1. The decoding ablation K* gradient is the strongest and most novel contribution
86	2. θ=0.60 lacks justification and sensitivity analysis is essential
87	3. 5-seed paired t-test (df=4) is statistically thin
88	4. DPI theory-to-practice gap is wider than the paper acknowledges
89	5. Core contribution is sound but multiple axes of evidence sit at thin margins simultaneously
90	6. Both scored 4/6 (Weak Accept) independently
91	
92	**R1-unique concerns (methods/stats focus):**
93	- 7B CI fragility (0.6015 barely above 0.60)
94	- Domain sensitivity completely unexamined
95	- Surprisal feature self-referential signal
96	- Common Crawl weak evidence without ground truth
97	- LoRA rank=16 ecological validity limited
98	
99	**R2-unique concerns (novelty/positioning focus):**
100	- Related work gaps: watermarking, self-refinement, Schaeffer taxonomy, Kazdan
101	- C1/C3 numbering gap (missing C2)
102	- K*=2 practical narrowness (essentially binary-with-soft-middle)
103	- Drayson comparison not cleanly controlled
104	- Broken references ([?] throughout)
105	
106	---
107	
108	## Step 3: Convergence Discussion
109	
110	**Consensus points:**
111	
112	1. **Overall assessment: Weak Accept.** Both reviewers converge on 4/6. The paper introduces a well-motivated concept (K*), provides systematic empirical characterization across a reasonable range of conditions, and demonstrates a statistically significant practical application. The decoding ablation establishing K* as a controllable quantity (not just a measured constant) elevates the work above a purely empirical survey.
113	
114	2. **The θ=0.60 sensitivity gap is the most actionable revision request.** Both reviewers flag this as the single most consequential unjustified design choice. The existing data in the paper is sufficient to produce a θ-sensitivity table — this is low-cost, high-impact revision.
115	
116	3. **Statistical concerns are real but not fatal.** The 7B CI margin (0.15pp) and 5-seed t-test (df=4) are thin but not fabricated. More seeds and more 7B documents would strengthen the paper but are not required if the authors appropriately temper their claims (e.g., "suggestive evidence" rather than "K*≥3 established").
117	
118	4. **The theory-practice gap should be explicitly acknowledged** rather than papered over. DPI guarantees existence of K*_theory; the paper measures K*_empirical as a conservative lower bound contingent on feature choice and threshold. Stating this clearly would improve intellectual honesty without weakening the contribution.
119	
120	5. **Related work revision needed.** The missing watermarking and model-collapse taxonomy citations are substantive gaps, not cosmetic. Broken references ([?]) suggest incomplete preparation.
121	
122	**Points of productive disagreement:**
123	
124	- R1 emphasizes the 7B fragility as a potential claim-level issue; R2 views the 7B result as supporting evidence rather than a headline claim (since the main K*=2 story holds at 1.5B). **Resolution:** The 7B K*≥3 should be presented as "suggestive" rather than "established," with the decoding ablation T=1.2→K*=3 (on 5K docs with stronger CI) carrying the "K* is not a ceiling" argument.
125	
126	- R2 is more concerned about K*=2's practical narrowness (3-class ≈ binary-with-soft-middle); R1 finds the graduated filtering evaluation convincing within its scope. **Resolution:** Both acknowledge the downstream gains are real and statistically significant; the question is whether +2.5pp on MMLU/HellaSwag is impactful enough for a top venue. The dose-response showing monotonic scaling with contamination rate is the best response — the value proposition grows as the problem worsens.
127	
128	---
129	
130	## Step 4: Consolidated Assessment
131	
132	### Overall Score: 4/6 (Weak Accept)
133	
134	### One-Line Verdict
135	A genuine conceptual contribution (K* as measurable, controllable operating point) supported by comprehensive experiments, but the simultaneous thin margins across multiple evidence axes (θ sensitivity, 7B CI, 5 seeds, DPI gap) and presentation issues (broken refs, C2 numbering) place it at the borderline.
136	
137	### Key Strengths (consensus)
138	1. **K* controllability is the core insight.** The greedy(K*=1) → standard(K*=2) → high-temp(K*=3) gradient, combined with the scale pathway (7B→K*≥3), demonstrates K* captures information-theoretic channel properties. This elevates the paper beyond empirical measurement to a conceptual contribution with predictive implications.
139	2. **Comprehensive, well-controlled experiments.** 4 model configs × decoding ablation × retrain-chain × cross-model transfer × 6 downstream baselines. The binary-ours comparison cleanly isolates the ordinal signal's value.
140	3. **Practically relevant dose-response.** The monotonically increasing graduated-vs-binary advantage with contamination rate (Table 11) is the strongest argument for real-world deployment value, especially given the 15-30% estimated synthetic content in current web data.
141	4. **Hand-crafted features as structural advantage.** 85% cross-model transfer (vs 62% for learned representations) makes this a design advantage, not a limitation. 102× fewer dimensions and 32.5× faster training support practical deployment.
142	
143	### Key Weaknesses (consensus)
144	1. **θ=0.60 threshold unjustified.** Every K* claim depends on this single arbitrary choice. Sensitivity analysis across θ ∈ [0.55, 0.65] is essential and straightforward to produce.
145	2. **Theory-practice gap understated.** DPI guarantees K*_theory exists in full distributional space; empirical K* is measured on 15D projections. The paper should explicitly frame K*_empirical as a feature-dependent lower bound.
146	3. **Thin statistical margins on multiple axes simultaneously.** 7B 2v3 CI lower exceeds θ by 0.15pp; 5-seed paired t-test at df=4; Qwen-cont instruct 1v2 CI margin ~0.15pp. Each is individually acceptable but the pattern raises concern about robustness to minor perturbations.
147	4. **Ecological validity limited.** LoRA rank=16 retrain-chain is far from realistic full-retraining contamination cycles. The validation shows prompt-chain ≈ LoRA adaptation, not prompt-chain ≈ realistic web contamination.
148	5. **Related work gaps.** Watermarking literature, Schaeffer et al. (2025) collapse taxonomy, self-refinement literature, and Kazdan et al. (2025) are missing. Broken [?] references throughout.
149	6. **C1/C3 numbering artifact.** Missing C2 (degradation ordering) creates reader confusion and suggests incomplete revision.
150	
151	### Requested Revisions (Priority Order)
152	1. **[Essential]** θ-sensitivity table/figure: report K* at θ ∈ {0.55, 0.575, 0.60, 0.625, 0.65} for all configurations
153	2. **[Essential]** Fix broken references and C1/C3→C1/C2/C3 numbering
154	3. **[Essential]** Add missing related work (watermarking, Schaeffer taxonomy, Kazdan)
155	4. **[Important]** Explicitly frame K*_empirical as feature-dependent lower bound on K*_theory
156	5. **[Important]** Temper 7B K*≥3 claim to "suggestive evidence" given 0.15pp CI margin
157	6. **[Important]** Report individual seed results for graduated filtering (Table 8-9)
158	7. **[Desirable]** Increase seeds to 10+ for downstream evaluation
159	8. **[Desirable]** Discuss domain sensitivity as limitation
160	9. **[Desirable]** Qualify "model-agnostic" claim re: surprisal reference model
161	
162	### Experiment Coverage Assessment
163	The paper covers all experiments from the design document: exp-003 (decoding ablation, Table 1-2), exp-004 (7B, Tables 3-4), exp-006 (graduated filtering, Tables 8-10), exp-008 (retrain-chain, Tables 6-7), exp-009 (dose-response, Table 11), exp-011 (LLM zero-shot, Table 12), exp-012 (binary detectors, Table 13), exp-014 (Common Crawl, Table 15), exp-015 (learned vs handcrafted, Table 14), exp-016 (base vs instruct, Table 5). **Coverage: 10/10 imagined experiments appear in the paper.** No designed experiment is missing.
164	
165	### Reviewer Scores
166	| Reviewer | Focus | Score | Confidence |
167	|----------|-------|-------|------------|
168	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/5 |
169	| R2 | Novelty + Related Work | 4/6 (Weak Accept) | 4/5 |
170	| **Consensus** | — | **4/6 (Weak Accept)** | **4/5** |
171	
172	### Accept/Reject Recommendation
173	**Weak Accept** — conditional on θ-sensitivity analysis, reference fixes, and related work additions. The K* controllability contribution is genuine and the experimental breadth is above average. The paper is at the borderline: if the θ-sensitivity analysis confirms the qualitative gradient is preserved across reasonable thresholds, the contribution stands. If K* rankings change materially with θ, the paper needs restructuring around a threshold-free metric.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e8b17cd-440c-48fc-8c84-47e33ce0a7f5",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "50f475f0-3116-45b3-8fce-3bf62e7183ec",
  "sourceToolAssistantUUID": "7e8b17cd-440c-48fc-8c84-47e33ce0a7f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T08:22:27.602Z_

Now I have a thorough understanding of the paper. Let me also look at the references file to check citation completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50f475f0-3116-45b3-8fce-3bf62e7183ec",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vZsCnxBYsajj9K5mX3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0421105-4198-47b7-ac48-f1d2828251a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Tt5vVh569DuVKitzDGDer",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5161,
      "cache_read_input_tokens": 57426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5161,
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

_source line 44 · 2026-05-16T08:22:29.450Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UCMRmy5SbM91UKPBiU6fQB`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0421105-4198-47b7-ac48-f1d2828251a3",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vZsCnxBYsajj9K5mX3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da2ae80f-39b7-4298-b0a9-0c2c5367a163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Tt5vVh569DuVKitzDGDer",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5161,
      "cache_read_input_tokens": 57426,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 57426,
          "cache_creation_input_tokens": 5161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5161,
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

_source line 45 · 2026-05-16T08:22:29.499Z_

<details><summary>↩ Tool result · `toolu_01UCMRmy5SbM91UKPBiU6fQB`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da2ae80f-39b7-4298-b0a9-0c2c5367a163",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "ae34fddf-cfeb-4fd0-8e31-193d1c364e1c",
  "sourceToolAssistantUUID": "da2ae80f-39b7-4298-b0a9-0c2c5367a163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T08:22:31.705Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TrQJwnyrgHfKoFKWo4CBfz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae34fddf-cfeb-4fd0-8e31-193d1c364e1c",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vaDhaprWoyGv9BDy2C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "542c9765-9f08-4cfc-a6ec-f387eed4ee6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvzcPvq8xqm53Zrxm4oMMs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 147,
      "cache_read_input_tokens": 62587,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 62587,
          "cache_creation_input_tokens": 147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 147,
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

_source line 47 · 2026-05-16T08:22:31.711Z_

<details><summary>↩ Tool result · `toolu_01TrQJwnyrgHfKoFKWo4CBfz`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-15
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{mitchell2023detectgpt,
31	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
32	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
33	  booktitle={Proceedings of ICML},
34	  year={2023}
35	}
36	
37	% === Should-Cite ===
38	
39	@article{basani2026diveye,
40	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
41	  author={Basani, Advik Raj and Chen, Pin-Yu},
42	  journal={Transactions on Machine Learning Research},
43	  year={2026},
44	  url={https://arxiv.org/abs/2509.18880}
45	}
46	
47	@inproceedings{zawalski2026codec,
48	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
49	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
50	  booktitle={Proceedings of ICLR},
51	  year={2026},
52	  url={https://arxiv.org/abs/2510.27055}
53	}
54	
55	@inproceedings{zhang2024minkpp,
56	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
57	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
58	  booktitle={Proceedings of EMNLP},
59	  year={2024}
60	}
61	
62	@article{shumailov2024collapse,
63	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
64	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
65	  journal={Nature},
66	  volume={631},
67	  pages={755--759},
68	  year={2024}
69	}
70	
71	@inproceedings{alemohammad2024selfconsuming,
72	  title={Self-Consuming Generative Models Go {MAD}},
73	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},
74	  booktitle={Proceedings of ICLR},
75	  year={2024}
76	}
77	
78	@inproceedings{dohmatob2024model,
79	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
80	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
81	  booktitle={Proceedings of ICML},
82	  year={2024}
83	}
84	
85	@inproceedings{xie2023dsir,
86	  title={Data Selection with Importance Resampling},
87	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
88	  booktitle={Proceedings of ICML},
89	  year={2023}
90	}
91	
92	@inproceedings{tirumala2023d4,
93	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
94	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
95	  booktitle={Advances in NeurIPS},
96	  year={2023}
97	}
98	
99	@inproceedings{xie2023doremi,
100	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
101	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
102	  booktitle={Advances in NeurIPS},
103	  year={2023}
104	}
105	
106	@inproceedings{hans2024binoculars,
107	  title={Spotting {LLMs} With Binoculars},
108	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
109	  booktitle={Proceedings of ICML},
110	  year={2024}
111	}
112	
113	% === Probing Classifiers ===
114	
115	@inproceedings{alain2017understanding,
116	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
117	  author={Alain, Guillaume and Bengio, Yoshua},
118	  booktitle={ICLR Workshop},
119	  year={2017}
120	}
121	
122	@article{belinkov2022probing,
123	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
124	  author={Belinkov, Yonatan},
125	  journal={Computational Linguistics},
126	  volume={48},
127	  number={1},
128	  pages={207--219},
129	  year={2022}
130	}
131	
132	% === Model Collapse Avoidability ===
133	
134	@inproceedings{bao2024fast,
135	  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},
136	  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
137	  booktitle={Proceedings of ICLR},
138	  year={2024},
139	  url={https://arxiv.org/abs/2310.05130}
140	}
141	
142	@inproceedings{frank2001ordinal,
143	  title={A Simple Approach to Ordinal Classification},
144	  author={Frank, Eibe and Hall, Mark},
145	  booktitle={Proceedings of ECML},
146	  pages={145--156},
147	  year={2001}
148	}
149	
150	% === Beyond-Binary Detection ===
151	
152	@inproceedings{cheng2025beyond,
153	  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},
154	  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
155	  booktitle={Proceedings of the ACM Web Conference (WWW)},
156	  year={2025},
157	  url={https://arxiv.org/abs/2410.14259}
158	}
159	
160	@article{mehta2025beyond,
161	  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},
162	  author={Mehta, Sushant},
163	  journal={arXiv preprint arXiv:2511.17602},
164	  year={2025},
165	  url={https://arxiv.org/abs/2511.17602}
166	}
167	
168	% === AI-Generated Content Prevalence ===
169	
170	@inproceedings{sun2025aigt,
171	  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},
172	  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},
173	  booktitle={Proceedings of ACL},
174	  year={2025},
175	  url={https://arxiv.org/abs/2412.18148}
176	}
177	
178	@article{spennemann2025quantifying,
179	  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},
180	  author={Spennemann, Dirk H. R.},
181	  journal={arXiv preprint arXiv:2504.08755},
182	  year={2025},
183	  url={https://arxiv.org/abs/2504.08755}
184	}
185	
186	% === New entries (added 2026-05-16, Round 4 reviewer) ===
187	
188	@inproceedings{dohmatob2025strong,
189	  title={Strong Model Collapse},
190	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
191	  booktitle={Proceedings of ICLR},
192	  year={2025},
193	  url={https://arxiv.org/abs/2410.04840}
194	}
195	
196	@inproceedings{wang2024semeval,
197	  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},
198	  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},
199	  booktitle={Proceedings of SemEval},
200	  year={2024},
201	  url={https://arxiv.org/abs/2404.14183}
202	}
203	
204	@inproceedings{gerstgrasser2024model,
205	  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
206	  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
207	  booktitle={Proceedings of COLM},
208	  year={2024},
209	  url={https://arxiv.org/abs/2404.01413}
210	}
211	
212	@inproceedings{guo2024curious,
213	  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
214	  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},
215	  booktitle={Findings of NAACL},
216	  year={2024},
217	  url={https://arxiv.org/abs/2311.09807}
218	}
219	
220	@article{briesch2023selfconsuming,
221	  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},
222	  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
223	  journal={arXiv preprint arXiv:2311.16822},
224	  year={2023},
225	  url={https://arxiv.org/abs/2311.16822}
226	}
227	
228	@inproceedings{padmakumar2024writing,
229	  title={Does Writing with Language Models Reduce Content Diversity?},
230	  author={Padmakumar, Vishakh and He, He},
231	  booktitle={Proceedings of ICLR},
232	  year={2024},
233	  url={https://arxiv.org/abs/2309.05196}
234	}
235	
236	% === New entries (added 2026-05-15, FR-10) ===
237	
238	@inproceedings{krishna2023paraphrasing,
239	  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},
240	  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
241	  booktitle={Advances in NeurIPS},
242	  year={2023}
243	}
244	
245	@article{sadasivan2023detect,
246	  title={Can {AI}-Generated Text be Reliably Detected?},
247	  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
248	  journal={arXiv preprint arXiv:2303.11156},
249	  year={2023},
250	  url={https://arxiv.org/abs/2303.11156}
251	}
252	
253	@inproceedings{hao2025rewrite,
254	  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},
255	  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},
256	  booktitle={Findings of ACL},
257	  year={2025}
258	}
259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "542c9765-9f08-4cfc-a6ec-f387eed4ee6e",
  "isSidechain": true,
  "promptId": "c0693d70-f074-4936-bc65-81ace71bbf55",
  "agentId": "a7f5b69bb1b927267",
  "type": "user",
  "uuid": "b6d89913-c4a9-4ed5-8f89-2f953c7c0811",
  "sourceToolAssistantUUID": "542c9765-9f08-4cfc-a6ec-f387eed4ee6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T08:23:53.089Z_

I now have a comprehensive understanding of the paper. Let me compose the review.

## R2: Novelty and Related Work

### Summary
The paper introduces "generational depth" as a measurable property of recursive synthetic text and defines K* as the discrimination boundary beyond which adjacent depths become statistically indistinguishable. Using 15 hand-crafted statistical features and an OBD-LightGBM classifier, the authors find K*=2 across 6 model configurations, 4 decoding strategies, and multiple ablations. The finding is positioned as bridging model collapse theory, binary MGT detection, and data curation. The paper is well-executed and thorough in its experimental coverage, but the novelty sits in a somewhat narrow gap between existing research threads, and several related work omissions affect positioning.

### Strengths

- S1: **Genuine conceptual reframing.** The shift from binary (human vs. machine) to ordinal (depth estimation) is a real intellectual contribution. No prior work formalizes or empirically measures the depth at which recursive generations become indistinguishable. This creates a new problem dimension that connects three previously siloed literatures (model collapse, MGT detection, data curation). The formulation of K* as an operational quantity, rather than just observing that "deeper generations look more similar," provides a concrete, falsifiable target.

- S2: **Converging evidence for a data-intrinsic boundary.** The paper's strongest novelty argument is not K*=2 itself but the convergence evidence: supervised OBD, zero-shot frontier LLMs (GPT-5.5, Claude Opus 4.6), and binary detector confidence analysis all fail at the same boundary. This multi-method convergence genuinely advances beyond what any single experiment could show. The cross-scorer validation confirming that K* is governed by the generation process rather than the scoring model adds further weight.

- S3: **Comprehensive related work coverage in the current version.** Compared to the previous draft (which had broken references and missing citations), the related work section now cites Schaeffer et al. (2025) taxonomy, Kazdan et al. (2025) accumulate/replace regimes, linguistic diversity contraction literature (Guo et al., Padmakumar & He), and positions K* within the Family B (distributions deforming) framework. The paragraph on "beyond binary detection" appropriately cites Cheng et al. (2025) and Mehta (2025).

- S4: **Clean actionable downstream prediction.** K*=2 generates a falsifiable prediction (binary filtering should suffice; graduated should not help), which is confirmed experimentally. This prediction-verification structure is scientifically strong and distinguishes the work from purely descriptive measurement papers.

- S5: **The cross-model transfer and feature ordering analysis** (Spearman rho >= 0.85 across continuation-mode models, surprisal-variance features dominating universally) provides mechanistic insight into why K*=2 holds: autoregressive generation systematically damps surprisal variability. This is more informative than just reporting that K*=2 across models.

### Weaknesses

- W1: **The DPI theoretical contribution is overstated.** The DPI argument -- that mutual information decreases along a Markov chain, implying a finite discrimination boundary -- is a textbook application of a fundamental information-theoretic inequality. The paper frames this as contributing a "theoretical framework" (Section 3.1), but the DPI argument requires only two lines and provides no quantitative prediction (it cannot predict K*=2 vs. K*=5 vs. K*=100). The actual contribution is empirical measurement, and the DPI framing adds credibility through association with information theory rather than through genuine theoretical depth. The paper should be more explicit that the DPI role is motivational, not predictive.

- W2: **Missing important related work threads.** Several relevant lines of work are absent:
  - **Watermarking-based provenance tracking** (Kirchenbauer et al., 2023; Christ et al., 2024): watermarking can in principle track generational depth if applied at each generation step. This is the most natural alternative approach and deserves discussion as a complementary technique.
  - **DNA-GPT** (Yang et al., 2024): uses divergent N-gram analysis for MGT detection, directly relevant to the "beyond binary" framing.
  - **Self-refinement / iterative generation literature** (Madaan et al., 2023 -- Self-Refine): texts may undergo multiple LLM passes for quality improvement, creating a related but distinct depth structure. The paper should discuss whether its depth estimation framework distinguishes "degradation depth" from "refinement depth."
  - **FineWeb** (Penedo et al., 2024) and related large-scale curation work: directly relevant to the data curation motivation but uncited.
  - **Membership inference** connections (Shi et al., 2024 -- Min-K% is cited, but the broader MI literature connecting to contamination detection is thin).

- W3: **K*=2 may be less surprising than presented.** The model collapse literature already established that the first generation step causes the most dramatic distributional shift (Shumailov et al., 2024 show tail distribution loss is most acute at generation 1). The K*=2 finding -- that one step is detectable but the marginal change at step 2 drops below threshold -- is a natural consequence of this known rapid initial degradation. The paper acknowledges this connection in Discussion (Section 6.1) but the framing in the Introduction and Abstract presents K*=2 as if it were an unexpected discovery rather than an expected consequence of known phenomena. This reduces the surprise/novelty factor.

- W4: **Practical impact is narrower than claimed.** K*=2 effectively means "binary detection works, and nothing beyond binary adds value." This is a useful null result, but the practical recommendation (do binary filtering) is identical to what Drayson et al. (2025) already propose. The paper's contribution is providing the theoretical/empirical justification for why binary suffices, but the actual curation practice does not change. The MMLU improvement from binary-ours over no-filter (-0.77pp vs. -1.53pp gap reduction) is in a 100% synthetic upper-bound setting; real-world contamination rates would yield proportionally smaller gains.

- W5: **The "one-wash laundering" framing invites overinterpretation.** Calling K*=2 a "one-wash laundering effect" suggests that adversaries can easily mask synthetic text depth, which is true only for depth >= 2. But the paper also shows 0v1 detection at AUC >= 0.96 -- the initial wash is very detectable. The metaphor conflates depth indistinguishability (beyond depth 2) with detection evasion (0v1 remains robust). This framing could mislead readers into thinking synthetic text detection is more fragile than it actually is.

- W6: **Threshold sensitivity remains a concern despite improvements.** The current paper now includes Figure 3 (K* vs theta), which addresses the previous round's top criticism. However, the unanimous K*=2 window is narrow: theta in [0.580, 0.600]. At theta=0.55, Qwen variants jump to K*=3; at theta=0.65, continuation modes drop to K*=1. The Cohen's h=0.20 justification for theta=0.60 is reasonable but ultimately conventional -- there is no data-driven or task-specific justification for why this particular effect size threshold is the right one for the depth estimation problem.

### Questions for Authors

- Q1: How does K* behave when the generation step involves self-refinement or instruction-following rewriting (e.g., "improve this text") rather than continuation or paraphrase? This is practically important because real-world recursive contamination may involve quality-improving LLM passes, not just repetitive generation.

- Q2: The cross-scorer validation shows that K* drops from 2 to 1 for Qwen-continuation under alternative scorers. In a realistic deployment where the generator is unknown, what is the expected K* and what practical guidance follows? If the answer is "use the strongest scorer available," this seems to reduce the "generator-independent" claim significantly.

- Q3: How does your framework relate to watermarking-based provenance? If generational watermarking were available, would your statistical features still be needed? This would help position the work relative to active provenance approaches.

- Q4: Given that K*=2 implies "binary filtering suffices," how does your method's downstream performance compare to Drayson et al. (2025)'s soft importance resampling when both use the same training setup? The current comparison appears to use a hard binary threshold rather than Drayson's SIR weighting scheme.

- Q5: You test 6 model configurations but all are <= 7B. Given the 0v1 AUC decrease observed from 1.5B to 7B (0.997 to 0.964), do you expect K* to remain 2 at 70B+ scale, or might larger models produce text so human-like that K* drops to 1?

### Minor Issues

- The paper title in main.tex ("Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary") differs from the title in the task description ("The Discrimination Boundary of Recursive Text Generation: Measuring K* Across Architectures, Decoding Strategies, and Domains"). The current tex title is better -- shorter, more informative, less listy.

- The Limitations section is extremely long and dense (one continuous paragraph spanning 12 enumerated points). This reads more like defensive preemption than genuine limitation acknowledgment. Splitting into prioritized subsections would improve readability.

- The paper uses "model-free" to describe features that require a scorer model for surprisal computation. This is technically inaccurate -- "model-free" should be reserved for features computable without any neural model. "Architecture-agnostic" or "generator-independent" would be more precise.

- Table 1 (cross-model transfer) reports 6-class accuracy, but the practical question is about depth-pair AUC transfer. Are cross-model pairwise AUC values available for the 1v2 boundary specifically?

- The OBD acronym (Ordered Bag of Distributions) is introduced in the abstract but the expansion appears only later. The connection between "OBD" as a feature framework name and OBD as an ordinal classification technique (Frank & Hall, 2001) is confusing -- these are two different things sharing the same acronym.

### Preliminary Score: 4/6
### Confidence: 4/5

The paper makes a genuine conceptual contribution by formalizing and measuring K* as an operational depth boundary, bridging three previously disconnected literatures. The experimental coverage is thorough and the convergent evidence (supervised + zero-shot + binary detector failure at the same boundary) is convincing. However, the DPI theoretical framing is textbook rather than novel, the K*=2 finding is more expected than surprising given known model collapse dynamics, several relevant related work threads are missing (watermarking, self-refinement, DNA-GPT), and the practical impact reduces to "binary filtering suffices" -- which is what existing work already does. The paper sits at the borderline: it is a solid, well-executed contribution to an important problem, but the novelty is more in systematic empirical measurement than in conceptual or methodological innovation. At a top venue with ~25% acceptance, this is a borderline paper that could go either way depending on how much credit reviewers assign to the problem formulation versus the (somewhat expected) answer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6d89913-c4a9-4ed5-8f89-2f953c7c0811",
  "isSidechain": true,
  "agentId": "a7f5b69bb1b927267",
  "requestId": "req_011Cb5vaPNW3PfyiQkfonYS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34c61baf-deca-4a51-8795-b684f2e9fa92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c34e77cc-1c13-4804-a3da-cf0cd53aac24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWqtMiLQnYsCH9vXLUSRz1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 62734,
      "output_tokens": 2720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2720,
          "cache_read_input_tokens": 62734,
          "cache_creation_input_tokens": 4312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4312,
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
