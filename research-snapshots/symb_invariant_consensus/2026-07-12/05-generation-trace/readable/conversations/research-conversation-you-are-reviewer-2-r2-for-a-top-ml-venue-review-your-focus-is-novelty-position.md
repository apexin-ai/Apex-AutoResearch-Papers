# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**. Review the 

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a06b1efba249b9d9e.jsonl`
- **Structured JSON:** [`e55d1bedfd518d51c841.json`](../../sessions/e5/e55d1bedfd518d51c841.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-15T07:49:52.917Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**. Review the paper below and provide your independent assessment. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target acceptance rate ~25%.

## Paper Summary

**Title:** Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors

The paper proposes Cross-Representation Disagreement Diagnosis (CRD), a framework that generates two executable formalizations of a reasoning problem (FOL+Z3 and Python), detects disagreements, classifies errors into a 4-type taxonomy (logic_error, negation_error, exec_crash, quantifier_error), localizes the faulty representation via stability testing, and optionally performs diagnosis-guided repair.

**Three Claims:**
1. Disagreement as high-precision diagnostic signal: 28–42% disagreement rates, 76–87% diagnostic precision, at 40% token cost of k=5 self-consistency
2. Structured error taxonomy with prescriptive value: 4-type taxonomy stable across models (κ=0.67), taxonomy-guided repair outperforms fixed-strategy by +5.0pp (p=0.042)
3. GT-label-dependent repair effect: helps Unknown (+22.1pp) and False (+10.4pp), hurts True (−11.2pp). Asymmetry reverses across domains (FOL-favored in logic 5.6:1, Code-favored in math 1.8:1)

## Related Work as Presented in Paper (Section 2)

The paper positions against 7 categories:

1. **Neurosymbolic Reasoning:** Logic-LM (Pan 2023), LINC (Olausson 2023), SatLM (Ye 2024) — translate NL to FOL. Single representation, no cross-representation comparison.

2. **Cross-Representation Filtering:** Liang et al. (2024) CoT-PoT disagreement for filtering. PROVE (2024) similarly filters. Paper claims to extend from binary filtering to structured diagnosis.

3. **Within-Representation Verification:** VeriCoT (Weng 2023), VERGE (Kang 2025), Roundtrip Verification (Zhong 2025) — verify within one paradigm. Paper extends to cross-representation.

4. **Self-Consistency and Ensemble:** Wang et al. (2023) k-sample majority vote. Multi-agent debate (Du 2023, Liang 2023). LEVER (Ni 2023). Paper claims CRD captures paradigm-level differences vs. generation variance.

5. **Self-Debugging:** Self-Debug (Chen 2023), Self-Refine (Madaan 2023), Faithful CoT (Lyu 2023) — single-representation iterative correction. CRD uses cross-paradigm disagreement as trigger.

6. **Adaptive Selection:** HybridMind (Li 2024), Sun et al. (2024) — choose representations. CRD diagnoses after both are generated.

7. **Correlated Failures:** Denisov-Blanch (2026) concerns about correlated failures in ensembles. Paper quantifies false agreement rate (12.3%).

## Key Novelty Claims

1. Extending cross-representation disagreement from binary filtering to structured diagnosis (error classification + localization + repair)
2. Error taxonomy with prescriptive value (κ=0.67 cross-model stability)
3. Discovery of GT-label-dependent repair effect and asymmetry reversal across domains
4. Empirical demonstration that disagreement patterns reflect domain-specific representation strengths, not fixed verifier hierarchies

## Experimental Scope
- 3 primary benchmarks: FOLIO (204), LogiQA (200), MATH Level 5 (200)
- 1 secondary benchmark: GPQA Diamond (150)
- 2 primary models: Qwen3-32B, DeepSeek V4 Pro
- 1 ablation model: Qwen3-8B
- 18 tables, comprehensive ablations
- All 13 planned experiments from the design document are covered

## Your Review Template

Provide your review in exactly this format:

### R2 Review: Novelty & Related Work

**Score:** X/6

**Summary:** (2-3 sentences)

**Strengths:**
- S1: ...
- S2: ...
- S3: ...

**Weaknesses:**
- W1: ...
- W2: ...
- W3: ...

**Questions for Authors:**
- Q1: ...
- Q2: ...

**Minor Issues:**
- ...

**Confidence:** X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "8b71d7c4-b472-4ded-b991-48cc4399e6e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T07:49:52.920Z_

```json
{
  "parentUuid": "8b71d7c4-b472-4ded-b991-48cc4399e6e4",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
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
  "uuid": "2f8d1061-d700-4c7a-bd18-2b5f31424a91",
  "timestamp": "2026-05-15T07:49:52.920Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T07:49:56.270Z_



I need to read the actual paper and related files to provide a thorough review. Let me start by finding the relevant materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f8d1061-d700-4c7a-bd18-2b5f31424a91",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zH5RV6uaKz3fBSdpd1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "273d8476-dd16-4b02-b8c4-9449fbc628b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2h3irYarkGuPzVPUbbJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7135,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7135,
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

_source line 4 · 2026-05-15T07:49:57.627Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013G2ppkMEQvCC9v5D4Ga66v`</summary>

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
  "parentUuid": "273d8476-dd16-4b02-b8c4-9449fbc628b5",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zH5RV6uaKz3fBSdpd1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "826903c1-579d-4cf2-b0cc-043fe0831793",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2h3irYarkGuPzVPUbbJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7135,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7135,
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

_source line 5 · 2026-05-15T07:49:57.631Z_

<details><summary>↩ Tool result · `toolu_013G2ppkMEQvCC9v5D4Ga66v`</summary>

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
  "parentUuid": "826903c1-579d-4cf2-b0cc-043fe0831793",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "d374996d-014a-4de4-90c7-03f6844ead0a",
  "sourceToolAssistantUUID": "826903c1-579d-4cf2-b0cc-043fe0831793",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T07:49:59.039Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01C4DrAgWxfpeNNiAz16YVXb`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d374996d-014a-4de4-90c7-03f6844ead0a",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zH5RV6uaKz3fBSdpd1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4ce438a-1a8f-4509-b142-e4aa933bf36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2h3irYarkGuPzVPUbbJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7135,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7135,
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

_source line 7 · 2026-05-15T07:49:59.085Z_

<details><summary>↩ Tool result · `toolu_01C4DrAgWxfpeNNiAz16YVXb`</summary>

```text
artifacts/.venv/lib/python3.14/site-packages/pyarrow/tests/data/orc/README.md
artifacts/.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/philox/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/idna-3.15.dist-info/licenses/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/httpcore-1.0.9.dist-info/licenses/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/httpx-0.28.1.dist-info/licenses/LICENSE.md
artifacts/.venv/lib/python3.14/site-packages/typer/.agents/skills/typer/SKILL.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/conversations/api.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/realtime/api.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/responses/api.md
artifacts/.venv/lib/python3.14/site-packages/openai/resources/webhooks/api.md
artifacts/.venv/lib/python3.14/site-packages/huggingface_hub/templates/datasetcard_template.md
artifacts/.venv/lib/python3.14/site-packages/huggingface_hub/templates/modelcard_template.md
task_context/history/reviewer/loop_1.md
task_context/history/agent/loop_1.md
task_context/history/director/loop_1.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2.md
artifacts/c1c5_audit.md
docs/proofwriter_survey.md
memory.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_3.md
task_context/history/agent/loop_2_1778793546.md
artifacts/c4_excl_unknown_analysis.md
artifacts/mvp_pipeline_004/report/c4_root_cause_analysis.md
artifacts/c4_decline_analysis.md
artifacts/mvp_pipeline_004/report/c4_decline_analysis.md
report.md
task_context/history/director/loop_3.md
task_context/history/reviewer/loop_3.md
task_context/history/agent/loop_4.md
task_context/history/agent/loop_3_1778804604.md
task_context/history/agent/loop_5.md
task_context/director.md
task_context/reviewer.md
task_context/agent.md
.claude/sessions/agent_2649041b/CLAUDE.md
.claude/sessions/agent_2649041b/AGENTS.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260515T060408/best/paper_framing.md
artifacts/dream_reports/dream_20260515T060408/median/paper_framing.md
artifacts/dream_reports/dream_20260515T060408/worst/paper_framing.md
.claude/sessions/briefer_e937439b/CLAUDE.md
.claude/sessions/briefer_e937439b/AGENTS.md
artifacts/dream_reports/dream_20260515T060408/median/review_report.md
artifacts/dream_reports/dream_20260515T060408/best/review_report.md
artifacts/dream_reports/dream_20260515T060408/worst/review_report.md
ROADMAP.md
paper_framing.md
.claude/sessions/reviewer_0fe76a8e/CLAUDE.md
.claude/sessions/reviewer_0fe76a8e/AGENTS.md
artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md
artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md
artifacts/dream_reports/dream_20260515T071730/worst/paper_framing.md
.claude/sessions/agent_4b4b70e8/CLAUDE.md
.claude/sessions/agent_4b4b70e8/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_551e3300/CLAUDE.md
.claude/sessions/director_551e3300/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4ce438a-1a8f-4509-b142-e4aa933bf36d",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "6ec681a0-a9f7-46c3-87b0-42d22a06e99a",
  "sourceToolAssistantUUID": "b4ce438a-1a8f-4509-b142-e4aa933bf36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T07:49:59.650Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BSfGBnSkrDYxzMeF3LybV5`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ec681a0-a9f7-46c3-87b0-42d22a06e99a",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zH5RV6uaKz3fBSdpd1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fcfb517-0e94-44d2-a784-e6a13ab8b08c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2h3irYarkGuPzVPUbbJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7135,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7135,
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

_source line 9 · 2026-05-15T07:49:59.685Z_

<details><summary>↩ Tool result · `toolu_01BSfGBnSkrDYxzMeF3LybV5`</summary>

```text
artifacts/dream_reports/dream_20260515T060408/best/paper.tex
artifacts/dream_reports/dream_20260515T060408/median/paper.tex
artifacts/dream_reports/dream_20260515T060408/worst/paper.tex
artifacts/dream_reports/dream_20260515T071730/best/paper.tex
artifacts/dream_reports/dream_20260515T071730/median/paper.tex
artifacts/dream_reports/dream_20260515T071730/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fcfb517-0e94-44d2-a784-e6a13ab8b08c",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "37f90f3f-0348-4588-88db-4f6adf1ba90b",
  "sourceToolAssistantUUID": "9fcfb517-0e94-44d2-a784-e6a13ab8b08c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T07:50:00.123Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01B8SoV3J75ZMPrUcZdYvPjk`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f90f3f-0348-4588-88db-4f6adf1ba90b",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zH5RV6uaKz3fBSdpd1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87b7b2e3-52c0-464a-b611-9bb5dd139441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2h3irYarkGuPzVPUbbJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7135,
      "cache_read_input_tokens": 8253,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 367,
          "cache_read_input_tokens": 8253,
          "cache_creation_input_tokens": 7135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7135,
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

_source line 11 · 2026-05-15T07:50:00.175Z_

<details><summary>↩ Tool result · `toolu_01B8SoV3J75ZMPrUcZdYvPjk`</summary>

```text
artifacts/dream_reports/dream_20260515T060408/best/paper.pdf
artifacts/dream_reports/dream_20260515T060408/median/paper.pdf
artifacts/dream_reports/dream_20260515T060408/worst/paper.pdf
artifacts/dream_reports/dream_20260515T071730/best/paper.pdf
artifacts/dream_reports/dream_20260515T071730/median/paper.pdf
artifacts/dream_reports/dream_20260515T071730/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87b7b2e3-52c0-464a-b611-9bb5dd139441",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "bff6cc5d-d663-45f1-ba80-e71617f56f49",
  "sourceToolAssistantUUID": "87b7b2e3-52c0-464a-b611-9bb5dd139441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T07:50:04.046Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bff6cc5d-d663-45f1-ba80-e71617f56f49",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zHcQZXcoyj6zyk1fxT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1441c9a0-fa39-4267-a40f-8faf9a61cb5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bpRwKD6JthUuG1wzLV73y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 15388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 13 · 2026-05-15T07:50:06.065Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JmJCe1Nk5ewGiTicvQEFHG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1441c9a0-fa39-4267-a40f-8faf9a61cb5b",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zHcQZXcoyj6zyk1fxT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41e222f6-ce7a-42bf-bcff-35f947ea2fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bpRwKD6JthUuG1wzLV73y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 15388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 14 · 2026-05-15T07:50:06.432Z_

<details><summary>↩ Tool result · `toolu_01JmJCe1Nk5ewGiTicvQEFHG`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{tabularx}
12	\usepackage[T1]{fontenc}
13	\usepackage[utf8]{inputenc}
14	\usepackage{microtype}
15	\usepackage{hyperref}
16	\usepackage{natbib}
17	\bibliographystyle{plainnat}
18	
19	\newcommand{\method}{CRD}
20	\newcommand{\pp}{\text{pp}}
21	
22	\title{Cross-Representation Disagreement as a Diagnostic Signal\\for LLM Reasoning Errors}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	% ============================================================
30	% ABSTRACT
31	% ============================================================
32	\begin{abstract}
33	When a large language model formalizes a reasoning problem into two distinct executable representations---first-order logic with Z3 verification and executable Python---disagreements between the outputs serve as a high-precision diagnostic signal. On three benchmarks (FOLIO, LogiQA, MATH Level~5) and two models (Qwen3-32B, DeepSeek~V4~Pro), we show that cross-representation disagreement (CRD) detects errors with 76--87\% diagnostic precision at 28--42\% disagreement rates, using only 40\% of the token cost of $k\!=\!5$ self-consistency. We contribute a four-type error taxonomy validated across models (Cohen's $\kappa\!=\!0.67$), reveal a GT-label-dependent repair effect where diagnosis helps for uncertain cases (+22.1\pp{} on GT=Unknown) but hurts for true cases ($-$11.2\pp{} overcorrection), and demonstrate that asymmetry direction reverses across domains---FOL-favored in logic (5.6:1), Code-favored in math (1.8:1)---indicating that disagreement patterns reflect domain-specific representation strengths rather than fixed verifier superiority.
34	\end{abstract}
35	
36	% ============================================================
37	% 1. INTRODUCTION
38	% ============================================================
39	\section{Introduction}
40	
41	Neurosymbolic reasoning pipelines increasingly rely on LLMs to translate natural language into formal executable representations~\cite{pan2023logiclm,ye2024satlm}. The dominant failure mode is not the symbolic solver but the LLM's formalization: subtle corruptions introduced during translation from natural language to formal representation~\cite{olausson2023linc}. Detecting these errors is difficult because the formal output is syntactically valid and the solver returns a definitive answer, masking upstream formalization errors.
42	
43	Current approaches to this problem fall into three categories: (1)~\emph{selection} methods that choose among representations based on confidence~\cite{li2024hybridmind,sun2024adaptive}, (2)~\emph{within-representation verification} that checks consistency within a single paradigm~\cite{weng2023vericot,kang2025verge,zhong2025roundtrip}, and (3)~\emph{cross-representation filtering} that discards samples where two formalizations disagree~\cite{liang2024cotpot,prove2024}. None of these exploit the diagnostic information \emph{within} the disagreement pattern itself---what type of error caused the disagreement, which representation is likely wrong, and how to repair it.
44	
45	We present \textbf{Cross-Representation Disagreement Diagnosis (\method{})}, an analysis framework and lightweight repair method that extends cross-representation disagreement from a binary filtering signal to a structured diagnostic tool. Given a reasoning problem, we generate two executable formalizations (FOL+Z3 and Python), execute both, and when they disagree, classify the error type, localize the faulty representation via stability testing, and optionally perform diagnosis-guided repair. Our three claims:
46	
47	\begin{enumerate}
48	\item \textbf{Disagreement as high-precision diagnostic signal.} Cross-representation disagreement occurs at 28--42\% rates across benchmarks and is diagnostically informative with 76--87\% precision---substantially higher than $k\!=\!5$ single-representation self-consistency (71--79\%) at 40\% of the token cost.
49	
50	\item \textbf{Structured error taxonomy with prescriptive value.} Disagreement patterns enable classification into four error types (logic\_error, negation\_error, exec\_crash, quantifier\_error). This taxonomy is stable across models ($\kappa\!=\!0.67$) and has prescriptive value: taxonomy-guided repair outperforms fixed-strategy repair by +5.0\pp{} ($p\!=\!0.042$).
51	
52	\item \textbf{GT-label-dependent repair effect.} Diagnosis-guided repair exhibits a striking asymmetry: it substantially helps for GT=Unknown (+22.1\pp{}) and GT=False (+10.4\pp{}) cases but \emph{hurts} for GT=True cases ($-$11.2\pp{}). The aggregate masks a three-way split that is the actual finding. We characterize this as a fundamental boundary of cross-representation diagnosis.
53	\end{enumerate}
54	
55	Our primary contribution is the systematic analysis of cross-representation disagreement as a diagnostic signal across domains and models. The repair framework demonstrates downstream utility but is secondary to the analytical findings. We release all experimental data and analysis code.
56	
57	% ============================================================
58	% 2. RELATED WORK
59	% ============================================================
60	\section{Related Work}
61	
62	\paragraph{Neurosymbolic Reasoning.}
63	Logic-LM~\cite{pan2023logiclm} and LINC~\cite{olausson2023linc} translate NL to FOL for symbolic solving. SatLM~\cite{ye2024satlm} uses SAT solvers. These methods use a single representation and cannot detect formalization errors through cross-representation comparison.
64	
65	\paragraph{Cross-Representation Filtering.}
66	Liang et al.~\cite{liang2024cotpot} showed CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements---no error categorization, no repair. PROVE~\cite{prove2024} similarly filters but does not diagnose. Our work extends filtering to structured diagnosis.
67	
68	\paragraph{Within-Representation Verification.}
69	VeriCoT~\cite{weng2023vericot} and VERGE~\cite{kang2025verge} verify reasoning chains within a single paradigm. Roundtrip Verification~\cite{zhong2025roundtrip} demonstrated diagnosis-guided repair within one representation on a narrow domain (150 traffic rules). We extend to cross-representation diagnosis across multiple domains.
70	
71	\paragraph{Self-Consistency and Ensemble Methods.}
72	Self-consistency~\cite{wang2023selfconsistency} uses $k$ samples from the same prompt for majority voting. Multi-agent debate~\cite{du2023debate,liang2023debate} and LEVER~\cite{ni2023lever} leverage multiple generation attempts. A key distinction: within-representation sampling captures generation variance, while CRD captures systematic paradigm-level differences between formal logic and imperative code.
73	
74	\paragraph{Self-Debugging and Refinement.}
75	Self-Debug~\cite{chen2023selfdebug} and Self-Refine~\cite{madaan2023selfrefine} use execution feedback for iterative correction within a single representation. Faithful CoT~\cite{lyu2023faithful} ensures reasoning chains are executable. These operate within one paradigm; CRD uses cross-paradigm disagreement as the diagnostic trigger.
76	
77	\paragraph{Adaptive Selection.}
78	HybridMind~\cite{li2024hybridmind} and adaptive selection methods~\cite{sun2024adaptive} choose between representations based on problem features. They select but do not diagnose or repair. CRD is complementary---it diagnoses \emph{after} both representations are generated.
79	
80	\paragraph{Correlated Failures.}
81	Denisov-Blanch~\cite{denisovblanch2026} raised concerns about correlated failures in ensemble methods. We explicitly quantify the false agreement rate (12.3\%) and show it varies by GT label, with the lowest correlation ($\phi\!=\!0.098$) on the subset where CRD is most effective (GT=Unknown).
82	
83	% ============================================================
84	% 3. METHOD
85	% ============================================================
86	\section{Method}
87	
88	\subsection{Overview}
89	
90	Given a reasoning problem $x$ with ground-truth label $y \in \{\text{True}, \text{False}, \text{Unknown}\}$, \method{} proceeds in four stages:
91	
92	\begin{enumerate}
93	\item \textbf{Dual formalization.} Prompt the LLM to produce two executable formalizations: $f_\text{FOL}(x)$ (first-order logic formula verified by Z3) and $f_\text{Code}(x)$ (Python program with execution).
94	\item \textbf{Disagreement detection.} Execute both formalizations and compare outputs. If $f_\text{FOL}(x) \neq f_\text{Code}(x)$, the sample enters the diagnostic pipeline.
95	\item \textbf{Error classification and localization.} Classify the disagreement into one of four error types using a rule-based taxonomy. Apply a stability test (re-execution with perturbed prompts) to localize the faulty representation.
96	\item \textbf{Diagnosis-guided repair} (optional). Generate a repair prompt incorporating the diagnosis (error type, suspected faulty side, disagreement pattern) and re-generate the faulty formalization.
97	\end{enumerate}
98	
99	For mathematical reasoning, we instantiate the dual representations as SymPy symbolic computation and Python numerical computation, maintaining the cross-executable-paradigm structure.
100	
101	\subsection{Error Taxonomy}
102	
103	We define four error types based on analysis of disagreement patterns:
104	
105	\begin{itemize}
106	\item \textbf{logic\_error}: Incorrect predicate definitions, flawed inference chains, or wrong logical connectives in the formalization.
107	\item \textbf{negation\_error}: Incorrect handling of negation---either missing negation or spurious double negation.
108	\item \textbf{exec\_crash}: Runtime errors in the executable path (syntax errors, undefined variables, solver timeouts).
109	\item \textbf{quantifier\_error}: Incorrect scope or type of quantifiers ($\forall$ vs.\ $\exists$) in FOL formalization.
110	\end{itemize}
111	
112	The taxonomy is deliberately rule-based for interpretability. We validate its cross-model stability in Section~\ref{sec:taxonomy_validation}.
113	
114	\subsection{Stability-Based Localization}
115	
116	To determine which representation contains the error, we apply a stability test: re-run each formalization $k\!=\!3$ times with temperature perturbation. If one representation produces consistent outputs while the other fluctuates, the unstable side is localized as the error source. When neither side is clearly unstable, the localization returns ``ambiguous.''
117	
118	This yields a high-precision / low-recall localization: when the stability test commits (53\% of diagnostic cases on FOLIO), accuracy is 94.6\%. The 47\% ambiguous rate is primarily driven by GT=Unknown samples where Code overclaiming creates systematically unstable predictions.
119	
120	\subsection{Multi-Round Repair}
121	
122	Repair proceeds for up to 3 rounds. Each round generates a repair prompt incorporating:
123	(1)~the error type from the taxonomy,
124	(2)~the localized faulty side (if available),
125	(3)~the outputs from both representations.
126	The repair prompt is type-specific: logic errors receive prompts targeting predicate and inference chain review; negation errors receive prompts checking polarity; exec\_crash triggers re-generation; quantifier errors receive prompts reviewing quantifier scope.
127	
128	\subsection{Cost Analysis}
129	
130	\method{} requires exactly 2 LLM calls for dual formalization (1 FOL + 1 Code), compared to $k\!=\!5$ calls for self-consistency. The repair pipeline adds 1--3 calls only for disagreeing samples. Overall token cost is approximately $2/5 = 0.40$ of SC-5, with additional diagnosis tokens for the disagreeing subset.
131	
132	% ============================================================
133	% 4. EXPERIMENTS
134	% ============================================================
135	\section{Experiments}
136	
137	\subsection{Setup}
138	
139	\paragraph{Models.} Qwen3-32B (primary), DeepSeek V4 Pro (cross-model validation), Qwen3-8B (scale ablation).
140	
141	\paragraph{Benchmarks.} (1)~FOLIO~\cite{han2022folio}: expert-annotated FOL problems, 204 samples, 3-class (True/False/Unknown). (2)~LogiQA~\cite{liu2021logiqa}: natural language logical reasoning from Chinese civil service exams, 200 samples, 4-way multiple choice. (3)~MATH Level~5~\cite{hendrycks2021math}: competition mathematics, 200 samples, using SymPy symbolic vs.\ Python numerical as dual representations. (4)~GPQA Diamond~\cite{rein2024gpqa}: graduate-level science questions, 150 samples (secondary benchmark).
142	
143	\paragraph{Metrics.} C1: disagreement rate. C2: diagnostic rate (fraction of disagreements where at least one side is wrong). C3: number of distinct error types observed. C4: repair delta (accuracy improvement over blind baseline). C5: localization accuracy (committed accuracy and coverage).
144	
145	% --------------------------------------------------------
146	% 4.2 FOLIO Core Analysis
147	% --------------------------------------------------------
148	\subsection{FOLIO Core Analysis}
149	\label{sec:folio_core}
150	
151	Table~\ref{tab:folio_core} presents the core metrics on FOLIO with Qwen3-32B (204 samples).
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\begin{tabular}{lccc}
157	\toprule
158	\textbf{Metric} & \textbf{Estimate} & \textbf{95\% CI} & \textbf{Gate} \\
159	\midrule
160	C1 (Disagree Rate) & 42.16\% & [35.3, 49.0] & $\geq$15\% \\
161	C2 (Diagnostic Rate) & 87.21\% & [81.3, 94.7] & $\geq$75\% \\
162	C3 (Error Types) & 4 & --- & $\geq$3 \\
163	C4 (Repair $\Delta$) & +4.65\pp{} & [$-$8.8, +18.1] & n.s. \\
164	C5 (Committed Acc) & 94.6\% & [86.1, 100] & --- \\
165	C5 (Coverage) & 53.0\% & [41.0, 65.1] & --- \\
166	\bottomrule
167	\end{tabular}
168	\caption{FOLIO C1--C5 metrics with bootstrap 95\% CI (Qwen3-32B, $n\!=\!204$). C2 lower bound 81.3\% exceeds the 75\% threshold, confirming high diagnostic precision.}
169	\label{tab:folio_core}
170	\end{table}
171	
172	The disagreement rate of 42.16\% indicates that a substantial fraction of problems elicit different answers from FOL+Z3 vs.\ Python execution. Of these disagreements, 87.21\% are diagnostically informative (at least one side is wrong). The error taxonomy identifies four types, dominated by logic\_error (25.5\%), followed by negation\_error (10.8\%), exec\_crash (5.4\%), and quantifier\_error (2.0\%) (Table~\ref{tab:error_taxonomy}).
173	
174	\begin{table}[t]
175	\centering
176	\small
177	\begin{tabular}{lcc}
178	\toprule
179	\textbf{Error Type} & \textbf{Count} & \textbf{Proportion} \\
180	\midrule
181	logic\_error & 52 & 25.5\% \\
182	negation\_error & 22 & 10.8\% \\
183	exec\_crash & 11 & 5.4\% \\
184	quantifier\_error & 4 & 2.0\% \\
185	\bottomrule
186	\end{tabular}
187	\caption{Error taxonomy distribution on FOLIO disagreement samples.}
188	\label{tab:error_taxonomy}
189	\end{table}
190	
191	The representation asymmetry is striking: FOL is correct in 56 disagreement cases vs.\ Code correct in 10 and both wrong in 10, yielding a 5.6:1 FOL-favored ratio. The phi coefficient between FOL and Code failures is 0.189 ($p\!=\!0.007$), indicating low but statistically significant correlation---the representations fail largely independently, with 75\% of errors being single-sided.
192	
193	% --------------------------------------------------------
194	% 4.3 GT-Label-Dependent Repair Effect
195	% --------------------------------------------------------
196	\subsection{GT-Label-Dependent Repair Effect}
197	\label{sec:repair_effect}
198	
199	The aggregate C4 of +4.65\pp{} (Fisher $p\!=\!0.626$) is not statistically significant. However, stratification by ground-truth label reveals a three-way split (Table~\ref{tab:gt_repair}).
200	
201	\begin{table}[t]
202	\centering
203	\small
204	\begin{tabular}{lccccl}
205	\toprule
206	\textbf{GT} & $n$ & \textbf{Targeted} & \textbf{Blind} & $\Delta$ & \textbf{Interp.} \\
207	\midrule
208	True & 72 & 63.6\% & 77.3\% & $-$13.6\pp{} & Overcorrect \\
209	False & 63 & 76.7\% & 70.0\% & +6.7\pp{} & Modest help \\
210	Unknown & 69 & 67.7\% & 52.9\% & +14.7\pp{} & Diagnosis helps \\
211	\bottomrule
212	\end{tabular}
213	\caption{GT-label-stratified repair effect on FOLIO (Round 1). Aggregate non-significance masks a three-way split.}
214	\label{tab:gt_repair}
215	\end{table}
216	
217	The GT=Unknown subset benefits most from diagnosis because Python's Code path lacks native three-valued logic and tends to overclaim True or False (78.3\% overclaiming rate). When CRD diagnosis reveals that FOL returned Unknown, the repair prompt helps the model recognize insufficient evidence. GT=True overcorrection occurs because when Code erroneously outputs False/Unknown, the diagnostic signal triggers the model to move away from True.
218	
219	% --------------------------------------------------------
220	% 4.4 Multi-Round Repair
221	% --------------------------------------------------------
222	\subsection{Multi-Round Repair}
223	\label{sec:multiround}
224	
225	Table~\ref{tab:multiround} shows how repair delta evolves across three rounds with error-type-specific prompts.
226	
227	\begin{table}[t]
228	\centering
229	\small
230	\begin{tabular}{lcccc}
231	\toprule
232	\textbf{GT Label} & $n$ & \textbf{Rd.~1 $\Delta$} & \textbf{Rd.~3 $\Delta$} & \textbf{Improv.} \\
233	\midrule
234	Unknown & 69 & +14.7\pp{} & +22.1\pp{} & +7.4\pp{} \\
235	False & 63 & +6.7\pp{} & +10.4\pp{} & +3.7\pp{} \\
236	True & 72 & $-$13.6\pp{} & $-$11.2\pp{} & +2.4\pp{} \\
237	\bottomrule
238	\end{tabular}
239	\caption{Multi-round repair results on FOLIO. GT=Unknown $\Delta$ rises from +14.7 to +22.1\pp{}; GT=True overcorrection partially mitigated but remains negative.}
240	\label{tab:multiround}
241	\end{table}
242	
243	Multi-round repair exhibits diminishing returns (Round~2: 8 additional fixes, Round~3: 3), confirming that type-specific strategies provide incremental value. Table~\ref{tab:repair_by_type} breaks down repair success by error type.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\begin{tabular}{lccc}
249	\toprule
250	\textbf{Error Type} & \textbf{Attempted} & \textbf{Fixed} & \textbf{Success} \\
251	\midrule
252	logic\_error & 41 & 28 & 68.3\% \\
253	negation\_error & 18 & 13 & 72.0\% \\
254	exec\_crash & 11 & 9 & 81.8\% \\
255	quantifier\_error & 4 & 2 & 50.0\% \\
256	\bottomrule
257	\end{tabular}
258	\caption{Repair success rate by error type (Round 3, FOLIO). exec\_crash is easiest to fix; quantifier\_error is hardest.}
259	\label{tab:repair_by_type}
260	\end{table}
261	
262	% --------------------------------------------------------
263	% 4.5 Cross-Model Ablation
264	% --------------------------------------------------------
265	\subsection{Cross-Model Ablation}
266	\label{sec:cross_model}
267	
268	To verify that CRD properties are not specific to Qwen3-32B, we test three conditions on FOLIO (Table~\ref{tab:cross_model}): (a)~Qwen3-32B within-model (MVP), (b)~DeepSeek V4 Pro within-model, and (c)~DeepSeek~FOL + Qwen~Code cross-model.
269	
270	\begin{table}[t]
271	\centering
272	\small
273	\begin{tabular}{lcccc}
274	\toprule
275	\textbf{Condition} & \textbf{C1} & \textbf{C2} & \textbf{C2 CI} & \textbf{Asym.} \\
276	\midrule
277	Qwen within & 42.2\% & 87.2\% & [81.3, 94.7] & 5.6:1 FOL \\
278	DeepSeek within & 38.7\% & 83.5\% & [74.2, 91.8] & 4.2:1 FOL \\
279	DS$\times$Qwen cross & 47.5\% & 80.9\% & [71.8, 89.1] & 3.8:1 FOL \\
280	\bottomrule
281	\end{tabular}
282	\caption{Cross-model ablation on FOLIO ($n\!=\!204$). C2 remains above 80\% across conditions. Asymmetry direction is consistently FOL-favored.}
283	\label{tab:cross_model}
284	\end{table}
285	
286	DeepSeek within-model C2 (83.5\%) falls within $\pm$8\pp{} of Qwen (87.2\%), confirming that diagnostic precision is a structural property of cross-representation disagreement rather than model-specific. The cross-model condition shows higher C1 (47.5\%) because different models' formalization biases increase disagreement probability, but slightly lower C2 (80.9\%) because some disagreement arises from capability differences rather than formalization errors. The GT-label-dependent repair effect replicates: DeepSeek shows +12.1\pp{} on GT=Unknown and $-$10.3\pp{} on GT=True.
287	
288	% --------------------------------------------------------
289	% 4.6 Cross-Benchmark Generalization
290	% --------------------------------------------------------
291	\subsection{Cross-Benchmark Generalization}
292	\label{sec:cross_benchmark}
293	
294	\paragraph{LogiQA.} We first piloted ProofWriter ($n\!=\!30$) but found only 6.7\% disagreement rate---synthetic data is too regular for CRD to be informative (both FOL and Code achieve $>$90\% accuracy). We switched to LogiQA, a natural-language logic benchmark derived from Chinese civil service exams. Table~\ref{tab:logiqa} compares LogiQA with FOLIO.
295	
296	\begin{table}[t]
297	\centering
298	\small
299	\begin{tabular}{lccc}
300	\toprule
301	\textbf{Metric} & \textbf{LogiQA} & \textbf{FOLIO} & $\Delta$ \\
302	\midrule
303	C1 (Disagree Rate) & 34.0\% & 42.2\% & $-$8.2\pp{} \\
304	C2 (Diagnostic Rate) & 81.5\% & 87.2\% & $-$5.7\pp{} \\
305	C3 (Error Types) & 4 & 4 & --- \\
306	C5 Committed Acc & 91.2\% & 94.6\% & $-$3.4\pp{} \\
307	Asymmetry & 3.2:1 FOL & 5.6:1 FOL & narrower \\
308	\bottomrule
309	\end{tabular}
310	\caption{LogiQA results ($n\!=\!200$, Qwen3-32B) vs.\ FOLIO reference. C2 remains above 80\%; the GT-stratified repair effect replicates.}
311	\label{tab:logiqa}
312	\end{table}
313	
314	LogiQA C2 of 81.5\% (CI: [73.8\%, 88.2\%]) confirms cross-benchmark stability. The narrower asymmetry (3.2:1 vs.\ 5.6:1) reflects LogiQA's propositional logic being less demanding than FOLIO's first-order logic, reducing FOL's relative advantage.
315	
316	\paragraph{ProofWriter pilot failure.} The 6.7\% pilot disagreement rate on ProofWriter (Table~\ref{tab:proofwriter_pilot}) is itself informative: CRD requires natural-language formalization challenges to produce a useful disagreement signal. Synthetic benchmarks with regular structure are well-handled by both representations, limiting CRD's applicability.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\begin{tabular}{lccc}
322	\toprule
323	\textbf{Metric} & \textbf{Value} & \textbf{Gate} & \textbf{Decision} \\
324	\midrule
325	Disagree Rate & 6.7\% & $\geq$10\% & FAIL \\
326	FOL Accuracy & 93.3\% & --- & --- \\
327	Code Accuracy & 90.0\% & --- & --- \\
328	\bottomrule
329	\end{tabular}
330	\caption{ProofWriter pilot ($n\!=\!30$). High accuracy on both paths yields insufficient disagreement for CRD.}
331	\label{tab:proofwriter_pilot}
332	\end{table}
333	
334	\paragraph{MATH Level 5.} We extend CRD to mathematical reasoning using SymPy symbolic computation vs.\ Python numerical computation as dual executable representations (Table~\ref{tab:math}).
335	
336	\begin{table}[t]
337	\centering
338	\small
339	\begin{tabular}{lccc}
340	\toprule
341	\textbf{Metric} & \textbf{MATH} & \textbf{FOLIO} & \textbf{LogiQA} \\
342	\midrule
343	C1 & 28.5\% & 42.2\% & 34.0\% \\
344	C2 & 76.0\% & 87.2\% & 81.5\% \\
345	C3 & 3 & 4 & 4 \\
346	Asymmetry & 1.8:1 Code & 5.6:1 FOL & 3.2:1 FOL \\
347	C5 Committed & 88.5\% & 94.6\% & 91.2\% \\
348	\bottomrule
349	\end{tabular}
350	\caption{MATH Level~5 results ($n\!=\!200$, Qwen3-32B). Asymmetry direction \emph{reverses}: Python numerical outperforms SymPy symbolic, contrasting with FOL-favored logic benchmarks.}
351	\label{tab:math}
352	\end{table}
353	
354	The asymmetry reversal is a key finding (Table~\ref{tab:asymmetry_direction}). In logic, FOL+Z3's formal verification guarantee gives it a systematic advantage. In mathematics, Python's flexible numerical methods are more robust than SymPy's symbolics (SymPy crash rate 12.5\% vs.\ Python 4.0\%). This proves that CRD captures \emph{domain-specific representation strengths}, not a fixed verifier hierarchy.
355	
356	\begin{table}[t]
357	\centering
358	\small
359	\begin{tabular}{llllc}
360	\toprule
361	\textbf{Domain} & \textbf{Rep.\ A} & \textbf{Rep.\ B} & \textbf{Favored} & \textbf{Ratio} \\
362	\midrule
363	Logic (FOLIO) & FOL+Z3 & Python & FOL & 5.6:1 \\
364	Logic (LogiQA) & FOL+Z3 & Python & FOL & 3.2:1 \\
365	Math (MATH) & SymPy & Python & Python & 1.8:1 \\
366	\bottomrule
367	\end{tabular}
368	\caption{Asymmetry direction across domains. The reversal from FOL-favored (logic) to Code-favored (math) reflects representation-task fit.}
369	\label{tab:asymmetry_direction}
370	\end{table}
371	
372	% --------------------------------------------------------
373	% 4.7 Correlated Failure Analysis
374	% --------------------------------------------------------
375	\subsection{Correlated Failure Analysis}
376	\label{sec:correlated}
377	
378	A natural concern is correlated failures: if both representations fail on the same samples, disagreement underestimates the true error rate. Table~\ref{tab:correlated} quantifies this.
379	
380	\begin{table}[t]
381	\centering
382	\small
383	\begin{tabular}{lcccc}
384	\toprule
385	\textbf{GT} & $n$ & $\phi$ & \textbf{False Agr.} & \textbf{Code Overcl.} \\
386	\midrule
387	True & 72 & 0.245 & 19.4\% & N/A \\
388	False & 63 & 0.162 & 11.1\% & N/A \\
389	Unknown & 69 & 0.098 & 5.8\% & 78.3\% \\
390	\midrule
391	Overall & 204 & 0.189 & 12.3\% & --- \\
392	\bottomrule
393	\end{tabular}
394	\caption{Correlated failure analysis by GT label. GT=Unknown has the lowest failure correlation ($\phi\!=\!0.098$) and highest Code overclaiming (78.3\%), explaining why CRD is most effective on this subset.}
395	\label{tab:correlated}
396	\end{table}
397	
398	The overall false agreement rate is 12.3\%---relatively low, and lowest on GT=Unknown (5.8\%) where CRD repair delta is highest. The phi coefficient is 0.189 overall ($p\!=\!0.007$), falling in the range where representations are independent enough to generate complementary signals but not so independent that disagreement is noise. Specification errors (ambiguity in the original problem) account for only 8.3\% of cases, confirming that most errors are formalization-specific.
399	
400	% --------------------------------------------------------
401	% 4.8 Selection vs Repair Ablation
402	% --------------------------------------------------------
403	\subsection{Selection vs.\ Repair Ablation}
404	\label{sec:selection_repair}
405	
406	After detecting disagreement and localizing the error side, should one simply \emph{select} the other side, or \emph{repair} the faulty one? Table~\ref{tab:selection_repair} compares on the GT$\neq$True subset ($n\!=\!132$), where diagnosis is beneficial.
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\setlength{\tabcolsep}{4pt}
412	\begin{tabular}{lccccc}
413	\toprule
414	\textbf{Method} & \textbf{All} & \textbf{logic} & \textbf{neg.} & \textbf{crash} & \textbf{quant.} \\
415	\midrule
416	Blind & 61.4 & 56.1 & 66.7 & 72.7 & 25.0 \\
417	Selection & 72.7 & 70.7 & 77.8 & 90.9 & 50.0 \\
418	Repair (Rd.~3) & 76.2 & 75.6 & 77.8 & 90.9 & 75.0 \\
419	\bottomrule
420	\end{tabular}
421	\caption{Selection vs.\ Repair on GT$\neq$True subset (FOLIO, $n\!=\!132$). All values are accuracy (\%). Selection already yields +11.3\pp{} over blind; repair adds +3.5\pp{}, concentrated on logic\_error and quantifier\_error.}
422	\label{tab:selection_repair}
423	\end{table}
424	
425	Selection alone provides +11.3\pp{} over blind baseline, demonstrating that CRD's diagnostic value is substantial even without repair. Repair adds +3.5\pp{} on top, with the advantage concentrated on logic\_error (+4.9\pp{}) and quantifier\_error (+25.0\pp{})---error types where both sides may be partially correct, making simple selection insufficient.
426	
427	% --------------------------------------------------------
428	% 4.9 Taxonomy Ablation
429	% --------------------------------------------------------
430	\subsection{Taxonomy-Guided vs.\ Fixed-Strategy Repair}
431	\label{sec:taxonomy_ablation}
432	
433	To test the prescriptive value of the error taxonomy, we compare taxonomy-guided repair (type-specific prompts) against a fixed strategy (uniform re-generation) in Table~\ref{tab:taxonomy_ablation}.
434	
435	\begin{table}[t]
436	\centering
437	\small
438	\begin{tabular}{lcccc}
439	\toprule
440	\textbf{Error Type} & $n$ & \textbf{Guided} & \textbf{Fixed} & $\Delta$ \\
441	\midrule
442	logic\_error & 41 & 75.6\% & 69.4\% & +6.2\pp{} \\
443	negation\_error & 18 & 77.8\% & 75.5\% & +2.3\pp{} \\
444	exec\_crash & 11 & 90.9\% & 90.9\% & +0.0\pp{} \\
445	quantifier\_error & 4 & 75.0\% & 57.0\% & +18.0\pp{} \\
446	\midrule
447	Overall & 74 & 76.2\% & 71.2\% & +5.0\pp{} \\
448	\bottomrule
449	\end{tabular}
450	\caption{Taxonomy-guided vs.\ fixed-strategy repair (FOLIO, GT$\neq$True). Overall $\Delta\!=\!$+5.0\pp{} (McNemar $p\!=\!0.042$). exec\_crash shows no difference (re-generation is already optimal); quantifier\_error shows the largest gap.}
451	\label{tab:taxonomy_ablation}
452	\end{table}
453	
454	The +5.0\pp{} overall advantage is statistically significant (McNemar $p\!=\!0.042$). The taxonomy's prescriptive value is concentrated on errors requiring targeted understanding: logic\_error (+6.2\pp{}, prompts targeting predicate and inference chain review) and quantifier\_error (+18.0\pp{}, prompts reviewing quantifier scope). exec\_crash shows zero difference because re-generation is inherently the correct strategy regardless of diagnosis.
455	
456	% --------------------------------------------------------
457	% 4.10 Cross-Model Taxonomy Validation
458	% --------------------------------------------------------
459	\subsection{Cross-Model Taxonomy Validation}
460	\label{sec:taxonomy_validation}
461	
462	To validate that the error taxonomy is not an artifact of a single model's classification, we have DeepSeek V4 Pro independently classify the same 75 diagnostic FOLIO samples (Table~\ref{tab:taxonomy_validation}).
463	
464	\begin{table}[t]
465	\centering
466	\small
467	\begin{tabular}{lcccc}
468	\toprule
469	\textbf{Error Type} & \textbf{Qwen} & \textbf{DS} & \textbf{Agree} & $\kappa$ \\
470	\midrule
471	logic\_error & 25.5\% & 28.0\% & 78.8\% & 0.71 \\
472	negation\_error & 10.8\% & 12.0\% & 72.7\% & 0.62 \\
473	exec\_crash & 5.4\% & 6.7\% & 90.9\% & 0.88 \\
474	quantifier\_error & 2.0\% & 1.3\% & 50.0\% & 0.45 \\
475	\midrule
476	Overall $\kappa$ & --- & --- & --- & 0.67 \\
477	\bottomrule
478	\end{tabular}
479	\caption{Cross-model taxonomy validation ($n\!=\!75$). Cohen's $\kappa\!=\!0.67$ (CI: [0.54, 0.80]) indicates substantial agreement. Rank order of error types is preserved across models.}
480	\label{tab:taxonomy_validation}
481	\end{table}
482	
483	Cohen's $\kappa\!=\!0.67$ (CI: [0.54, 0.80]) reaches ``substantial agreement.'' The rank order of error types is identical across models (logic $>$ negation $>$ crash $>$ quantifier), suggesting the taxonomy captures genuine structural failure modes rather than model-specific artifacts. exec\_crash achieves the highest agreement (90.9\%) due to its objective verifiability; quantifier\_error the lowest (50.0\%) due to small sample size ($n\!=\!4$).
484	
485	% --------------------------------------------------------
486	% 4.11 Self-Consistency Baseline
487	% --------------------------------------------------------
488	\subsection{CRD vs.\ Self-Consistency}
489	\label{sec:sc_baseline}
490	
491	We compare single-pass CRD against $k\!=\!5$ self-consistency (majority vote) within each representation (Table~\ref{tab:crd_vs_sc}).
492	
493	\begin{table}[t]
494	\centering
495	\small
496	\begin{tabular}{lccccc}
497	\toprule
498	\textbf{Bench.} & \textbf{SC5-FOL} & \textbf{SC5-Code} & \textbf{CRD} & $\Delta$ & \textbf{Cost} \\
499	\midrule
500	FOLIO & 79.3 & 72.1 & 87.2 & +7.9 & 0.40 \\
501	LogiQA & 75.8 & 69.4 & 81.5 & +5.7 & 0.40 \\
502	MATH & 71.2 & 74.8 & 76.0 & +1.2 & 0.40 \\
503	\midrule
504	Avg. & 75.4 & 72.1 & 81.6 & +4.9 & 0.40 \\
505	\bottomrule
506	\end{tabular}
507	\caption{CRD vs.\ $k\!=\!5$ self-consistency. All values are diagnostic precision (\%); $\Delta$ is CRD minus best SC5; Cost is CRD token ratio vs.\ SC5. CRD Pareto-dominates: higher precision at 40\% of the cost.}
508	\label{tab:crd_vs_sc}
509	\end{table}
510	
511	CRD Pareto-dominates $k\!=\!5$ self-consistency: +4.9\pp{} average precision at 40\% token cost. The advantage is largest on FOLIO (+7.9\pp{}), where FOL and Python represent maximally different paradigms, and smallest on MATH (+1.2\pp{}), where SymPy and Python numerical are both Python-ecosystem tools with smaller paradigm distance. On FOLIO, the precision gap is statistically significant (McNemar $p\!=\!0.031$). This result supports the thesis that cross-representation disagreement captures paradigm-level differences---fundamentally more informative than within-representation sampling variance.
512	
513	% --------------------------------------------------------
514	% 4.12 Model Scale Ablation
515	% --------------------------------------------------------
516	\subsection{Model Scale Ablation}
517	\label{sec:scale}
518	
519	Table~\ref{tab:scale} compares three models on FOLIO, forming a capability gradient.
520	
521	\begin{table}[t]
522	\centering
523	\small
524	\begin{tabular}{lccccc}
525	\toprule
526	\textbf{Model} & \textbf{C1} & \textbf{C2} & \textbf{Asym.} & \textbf{FOL} & \textbf{Code} \\
527	\midrule
528	Qwen3-8B & 55.4 & 74.5 & 2.8:1 & 58.3 & 47.1 \\
529	Qwen3-32B & 42.2 & 87.2 & 5.6:1 & 78.4 & 59.8 \\
530	DeepSeek Pro & 38.7 & 83.5 & 4.2:1 & 81.2 & 64.7 \\
531	\bottomrule
532	\end{tabular}
533	\caption{Model scale ablation on FOLIO. C1 and C2 show inverse scaling: weaker models produce more disagreements (C1$\uparrow$) but with lower diagnostic value (C2$\downarrow$). FOL and Code columns show individual path accuracy (\%).}
534	\label{tab:scale}
535	\end{table}
536	
537	Weaker models produce more disagreements (C1: 55.4\% for 8B vs.\ 42.2\% for 32B) but with lower diagnostic value (C2: 74.5\% vs.\ 87.2\%). The 8B model's C2 of 74.5\% approaches the lower bound of usefulness---below some capability threshold, correlated failures (both sides wrong) begin to dominate disagreement, eroding diagnostic precision. The asymmetry ratio compresses from 5.6:1 to 2.8:1 because FOL accuracy degrades faster with model scale (formal logic is more capability-sensitive), reducing the structural advantage.
538	
539	% --------------------------------------------------------
540	% 4.13 Cross-Domain Boundary (GPQA)
541	% --------------------------------------------------------
542	\subsection{Cross-Domain Boundary: GPQA Diamond}
543	\label{sec:gpqa}
544	
545	To characterize the boundary of CRD's applicability, we test on GPQA Diamond, a graduate-level science reasoning benchmark (Table~\ref{tab:cross_domain}).
546	
547	\begin{table}[t]
548	\centering
549	\small
550	\begin{tabular}{llccc}
551	\toprule
552	\textbf{Domain} & \textbf{Benchmark} & \textbf{C1} & \textbf{C2} & \textbf{Error Source} \\
553	\midrule
554	Logic & FOLIO & 42.2 & 87.2 & Formalization \\
555	Logic & LogiQA & 34.0 & 81.5 & Formalization \\
556	Math & MATH L5 & 28.5 & 76.0 & Computation \\
557	Science & GPQA & 22.0 & 72.7 & Knowledge gap \\
558	\bottomrule
559	\end{tabular}
560	\caption{CRD effectiveness across domains. C2 decreases monotonically as the primary error source shifts from formalization to knowledge gaps. CRD is most effective when errors arise from the translation to formal representation, not from missing domain knowledge.}
561	\label{tab:cross_domain}
562	\end{table}
563	
564	The four benchmarks form a clear domain gradient: C2 decreases from 87.2\% (pure logic) through 81.5\% and 76.0\% to 72.7\% (science) as the primary error source shifts from formalization errors to domain knowledge gaps. CRD's diagnostic power derives from detecting formalization-specific errors; when the model lacks the domain knowledge to formalize correctly in \emph{any} representation, disagreement provides weaker signal.
565	
566	% --------------------------------------------------------
567	% 4.14 Statistical Significance
568	% --------------------------------------------------------
569	\subsection{Statistical Significance}
570	\label{sec:significance}
571	
572	Table~\ref{tab:significance} summarizes significance tests across all benchmarks.
573	
574	\begin{table}[t]
575	\centering
576	\small
577	\setlength{\tabcolsep}{3pt}
578	\begin{tabular}{llllcl}
579	\toprule
580	\textbf{Test} & \textbf{Bench.} & \textbf{Metric} & \textbf{Effect} & $p$ & \textbf{Sig.} \\
581	\midrule
582	Fisher & FOLIO & C4 Unknown & +22.1\pp{} & .038 & Yes \\
583	Fisher & FOLIO & C4 True & $-$11.2\pp{} & .021 & Yes \\
584	Fisher & LogiQA & C4 pos.\ sub. & +11.3\pp{} & .045 & Yes \\
585	McNemar & FOLIO & CRD vs SC5 & +7.2\pp{} & .031 & Yes \\
586	McNemar & FOLIO & Tax.\ guided & +5.0\pp{} & .042 & Yes \\
587	Fisher & FOLIO & C4 aggregate & +4.65\pp{} & .626 & No \\
588	\bottomrule
589	\end{tabular}
590	\caption{Statistical significance summary. All stratified claims are significant; the aggregate C4 is not---confirming that stratified reporting is the correct granularity.}
591	\label{tab:significance}
592	\end{table}
593	
594	All primary claims at the stratified level reach statistical significance. The non-significant aggregate C4 reinforces our methodological argument: reporting aggregate repair delta masks the three-way split and produces a misleading null result. Bootstrap 95\% CIs for C2 across benchmarks are: FOLIO [81.3\%, 94.7\%], LogiQA [73.8\%, 88.2\%], MATH [66.1\%, 85.2\%].
595	
596	% ============================================================
597	% 5. DISCUSSION
598	% ============================================================
599	\section{Discussion}
600	
601	\paragraph{Paradigm distance modulates CRD effectiveness.}
602	The gradient from FOLIO (+7.9\pp{} over SC5) to MATH (+1.2\pp{}) suggests that CRD's advantage over within-representation self-consistency scales with the semantic distance between representations. FOL+Z3 and Python represent fundamentally different reasoning paradigms (declarative vs.\ imperative); SymPy and Python numerical are both imperative and Python-based, limiting paradigm-level diversity. This points to a design principle: maximize representation paradigm distance when deploying CRD.
603	
604	\paragraph{When NOT to use CRD.}
605	ProofWriter's 6.7\% disagreement rate and GPQA's 72.7\% C2 delineate the boundaries. CRD is most valuable when (1)~the task involves natural-language formalization challenges (not synthetic/regular data) and (2)~errors arise from the formalization process rather than missing domain knowledge. It provides diminishing returns on tasks where both representations achieve high accuracy or where knowledge gaps dominate.
606	
607	\paragraph{The GT=True overcorrection boundary.}
608	GT=True overcorrection ($-$11.2\pp{} after 3 rounds) is structural, not strategic. When Code erroneously outputs False/Unknown for a True problem, the diagnostic signal ``Code disagrees'' pushes the model away from the correct answer. Multi-round repair mitigates this (from $-$13.6 to $-$11.2\pp{}) but cannot eliminate it without access to ground truth. Practitioners should apply diagnosis-guided repair selectively, skipping it for high-confidence True predictions.
609	
610	\paragraph{Implications for representation design.}
611	The asymmetry reversal (FOL-favored in logic, Code-favored in math) suggests that representation choice should be domain-matched. FOL+Z3's formal verification provides guarantees in logic; Python's numerical flexibility is more robust for computation. A system could adaptively weight representations based on detected domain characteristics.
612	
613	% ============================================================
614	% 6. CONCLUSION
615	% ============================================================
616	\section{Conclusion}
617	
618	We presented Cross-Representation Disagreement Diagnosis (CRD), a framework that extends cross-representation disagreement from binary filtering to structured error diagnosis. Across three benchmarks and two models, CRD achieves 76--87\% diagnostic precision at 40\% of the cost of $k\!=\!5$ self-consistency. We identified three principal findings: (1)~disagreement between executable representations is a high-precision diagnostic signal that captures formalization-specific errors; (2)~a four-type error taxonomy validated across models ($\kappa\!=\!0.67$) provides prescriptive value for targeted repair (+5.0\pp{} over fixed strategy); (3)~diagnosis-guided repair exhibits a GT-label-dependent effect, with substantial benefit for Unknown/False cases but overcorrection for True cases. The asymmetry reversal across domains (FOL-favored in logic vs.\ Code-favored in math) reveals that disagreement patterns reflect domain-specific representation strengths, not fixed verifier hierarchies.
619	
620	\paragraph{Limitations.}
621	Our evaluation covers three reasoning domains with two primary models. The error taxonomy is rule-based and requires extension for new domains. Sample sizes (150--204) limit statistical power for fine-grained subgroup analyses. The GT=True overcorrection remains an open challenge.
622	
623	% ============================================================
624	% REFERENCES
625	% ============================================================
626	\begin{thebibliography}{25}
627	
628	\bibitem[Chen et al.(2023)]{chen2023selfdebug}
629	Xinyun Chen, Maxwell Lin, Nathanael Sch{\"a}rli, and Denny Zhou. 2023.
630	\newblock Teaching large language models to self-debug.
631	\newblock In \emph{Proc. ICLR}.
632	
633	\bibitem[Denisov-Blanch(2026)]{denisovblanch2026}
634	Daniel Denisov-Blanch. 2026.
635	\newblock On correlated failures in LLM ensemble methods.
636	\newblock \emph{arXiv preprint}.
637	
638	\bibitem[Du et al.(2023)]{du2023debate}
639	Yilun Du, Shuang Li, Antonio Torralba, Joshua~B. Tenenbaum, and Igor Mordatch. 2023.
640	\newblock Improving factuality and reasoning in language models through multiagent debate.
641	\newblock In \emph{Proc. ICML}.
642	
643	\bibitem[Han et al.(2022)]{han2022folio}
644	Simeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Luke Benson, Lucy Sun, Ekaterina Zubkova, Yun He, Matthew Kaber, Yuan Liu, Zhaoyi Hou, and Dragomir Radev. 2022.
645	\newblock {FOLIO}: Natural language reasoning with first-order logic.
646	\newblock \emph{arXiv:2209.00840}.
647	
648	\bibitem[Hendrycks et al.(2021)]{hendrycks2021math}
649	Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021.
650	\newblock Measuring mathematical problem solving with the {MATH} dataset.
651	\newblock In \emph{Proc. NeurIPS}.
652	
653	\bibitem[Kang et al.(2025)]{kang2025verge}
654	Kang et al. 2025.
655	\newblock {VERGE}: Verification-guided reasoning.
656	\newblock \emph{arXiv preprint}.
657	
658	\bibitem[Li et al.(2024)]{li2024hybridmind}
659	Li et al. 2024.
660	\newblock {HybridMind}: Adaptive selection of reasoning representations.
661	\newblock In \emph{Proc. ACL}.
662	
663	\bibitem[Liang et al.(2023)]{liang2023debate}
664	Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Zhaopeng Tu, and Shuming Shi. 2023.
665	\newblock Encouraging divergent thinking in large language models through multi-agent debate.
666	\newblock \emph{arXiv:2305.19118}.
667	
668	\bibitem[Liang et al.(2024)]{liang2024cotpot}
669	Liang et al. 2024.
670	\newblock {CoT}-{PoT} disagreement as an error detection signal.
671	\newblock \emph{arXiv preprint}.
672	
673	\bibitem[Liu et al.(2021)]{liu2021logiqa}
674	Jian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. 2021.
675	\newblock {LogiQA}: A challenge dataset for machine reading comprehension with logical reasoning.
676	\newblock In \emph{Proc. IJCAI}.
677	
678	\bibitem[Lyu et al.(2023)]{lyu2023faithful}
679	Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. 2023.
680	\newblock Faithful chain-of-thought reasoning.
681	\newblock In \emph{Proc. IJCNLP-AACL}.
682	
683	\bibitem[Madaan et al.(2023)]{madaan2023selfrefine}
684	Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa~Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. 2023.
685	\newblock Self-refine: Iterative refinement with self-feedback.
686	\newblock In \emph{Proc. NeurIPS}.
687	
688	\bibitem[Ni et al.(2023)]{ni2023lever}
689	Ansong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida~I. Wang, and Xi~Victoria Lin. 2023.
690	\newblock {LEVER}: Learning to verify language-to-code generation with execution.
691	\newblock In \emph{Proc. ICML}.
692	
693	\bibitem[Olausson et al.(2023)]{olausson2023linc}
694	Theo~X. Olausson, Alex Gu, Ben Lipkin, Cedegao~E. Zhang, Armando Solar-Lezama, Joshua~B. Tenenbaum, and Roger Levy. 2023.
695	\newblock {LINC}: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.
696	\newblock In \emph{Proc. EMNLP}.
697	
698	\bibitem[Pan et al.(2023)]{pan2023logiclm}
699	Liangming Pan, Alon Albalak, Xinyi Wang, and William~Yang Wang. 2023.
700	\newblock {Logic-LM}: Empowering large language models with symbolic solvers for faithful logical reasoning.
701	\newblock In \emph{Findings of EMNLP}.
702	
703	\bibitem[PROVE(2024)]{prove2024}
704	PROVE. 2024.
705	\newblock Program verification for error detection in reasoning.
706	\newblock \emph{arXiv preprint}.
707	
708	\bibitem[Rein et al.(2024)]{rein2024gpqa}
709	David Rein, Betty~Li Hou, Asa~Cooper Stickland, Jackson Petty, Richard~Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel~R. Bowman. 2024.
710	\newblock {GPQA}: A graduate-level Google-proof Q\&A benchmark.
711	\newblock In \emph{Proc. NAACL}.
712	
713	\bibitem[Sun et al.(2024)]{sun2024adaptive}
714	Sun et al. 2024.
715	\newblock Adaptive representation selection for reasoning.
716	\newblock \emph{arXiv preprint}.
717	
718	\bibitem[Wang et al.(2023)]{wang2023selfconsistency}
719	Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc~V. Le, Ed~H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.
720	\newblock Self-consistency improves chain of thought reasoning in language models.
721	\newblock In \emph{Proc. ICLR}.
722	
723	\bibitem[Weng et al.(2023)]{weng2023vericot}
724	Weng et al. 2023.
725	\newblock {VeriCoT}: Verification-based chain-of-thought.
726	\newblock \emph{arXiv preprint}.
727	
728	\bibitem[Ye et al.(2024)]{ye2024satlm}
729	Xi Ye, Qiaochu Chen, Isil Dillig, and Greg Durrett. 2024.
730	\newblock {SatLM}: Satisfiability-aided language models using declarative prompting.
731	\newblock In \emph{Proc. NeurIPS}.
732	
733	\bibitem[Zhong et al.(2025)]{zhong2025roundtrip}
734	Zhong et al. 2025.
735	\newblock Roundtrip verification for diagnosis-guided repair.
736	\newblock \emph{arXiv preprint}.
737	
738	\end{thebibliography}
739	
740	\end{document}
741	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41e222f6-ce7a-42bf-bcff-35f947ea2fad",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "c856d05e-d026-4331-b595-24ad8a52e90b",
  "sourceToolAssistantUUID": "41e222f6-ce7a-42bf-bcff-35f947ea2fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T07:50:06.877Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017QvwFZTQQ1ycgccYRqaTT2`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c856d05e-d026-4331-b595-24ad8a52e90b",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zHcQZXcoyj6zyk1fxT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "decba06b-6fc5-4551-9ba3-00d7ff2b7485",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bpRwKD6JthUuG1wzLV73y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 15388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 16 · 2026-05-15T07:50:06.893Z_

<details><summary>↩ Tool result · `toolu_017QvwFZTQQ1ycgccYRqaTT2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_pipeline_004 | v4 truncation detection + thinking-off retry, 204 samples | RUNNING (PID 47964, 127/204, ETA ~08:30 BJT) | All-mode 5/5 PASS @126样本 | — |\\n\\n## 126 样本 C1-C5 指标（evaluate_mvp.py 权威数据）\\n| 指标 | All-mode (N=117) | 阈值 | 状态 | Excl-Unknown (N=75) | 状态 |\\n|------|-----------------|------|------|-------------------|------|\\n| C1 disagree_rate | 35.9% (42/117) | ≥10% | PASS | 34.7% (26/75) | PASS |\\n| C2 diagnostic_rate | 88.1% (37/42) | ≥40% | PASS | 88.5% (23/26) | PASS |\\n| C3 error_types | 3 | ≥2 | PASS | 2 | PASS |\\n| C4 targeted_delta | +7.4pp (T:35/54 B:31/54) | >5pp | PASS | +0.0pp (T:22/35 B:22/35) | FAIL |\\n| C5 localization | 79.2% (19/24) | ≥60% | PASS | 87.5% (14/16) | PASS |\\n\\n## 已完成修复\\n- repair.py: repr_type 动态 prompt（C4 excl-unknown 根因修复）\\n- pipeline.py: streaming JSONL + gc.collect（内存泄漏修复）\\n- pipeline.py: JSON→JSONL in-place 转换（数据损坏 bug 修复）\\n- repair_only.py: repair-only 重跑脚本就绪\\n\\n## 待处理\\n- 等 204 全量完成 → evaluate_mvp.py 最终评估\\n- 204 完成后 → repair_only.py 重跑 repair+eval（用修复后的 prompt）\\n\\n## 近期结论\\n- **mvp_pipeline_004** (success, 127/204): All-mode 5/5 PASS，C4 趋势下滑需关注\\n- **mvp_pipeline_002** (negative): FOL crash 修复但 C4/C5 仍 FAIL\\n- **mvp_pipeline_001** (negative): 首轮 2/5 PASS\\n\\n## 趋势\\n成功 1 / 负向 2 / 失败 0 / 终止 2 / 共 6\\nMVP 指标持续改善: v1(2/5) → v2(2/5) → v4@80(4/5) → v4@126(5/5 all-mode)\\n\\n## 资源状态\\nautodl-rtx6000pro: cuda:0 pipeline (PID 47964) + vLLM serving 运行中\\n\", \"total_chars\": 1517, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "decba06b-6fc5-4551-9ba3-00d7ff2b7485",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "2b8baffd-d4e4-4998-90d5-26340f78aebf",
  "sourceToolAssistantUUID": "decba06b-6fc5-4551-9ba3-00d7ff2b7485",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T07:50:07.452Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Rx8tBJddeexs7urDEbMJzD`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b8baffd-d4e4-4998-90d5-26340f78aebf",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zHcQZXcoyj6zyk1fxT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ced3936b-c88e-4857-926d-15127468f16d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bpRwKD6JthUuG1wzLV73y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 15388,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 15388,
          "cache_creation_input_tokens": 3391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3391,
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

_source line 18 · 2026-05-15T07:50:07.463Z_

<details><summary>↩ Tool result · `toolu_01Rx8tBJddeexs7urDEbMJzD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/paper_framing.md\", \"content\": \"# Paper Framing — cross_representation_disagreement_diagno\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (10 days)\\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\\n\\n## Core Insight\\nWhen the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This \\\"disagreement as diagnostic\\\" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\\n\\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\\n\\n### Claim 2: Error Classification and Conditional Localization\\nDisagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is 94.6%. The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.\\n\\n**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return \\\"ambiguous\\\" (especially Unknown: 61%). C3=4 error types.\\n\\n**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.\\n\\n**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled \\\"the error.\\\"\\n\\n### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral\\nDiagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:\\n\\n| GT Label | n | Targeted | Blind | Delta | Interpretation |\\n|----------|---|----------|-------|-------|----------------|\\n| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |\\n| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |\\n| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |\\n\\nThis is NOT simply \\\"conditional advantage\\\" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal (\\\"Code disagrees with FOL\\\") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.\\n\\n**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.\\n\\n**Presentation strategy**: \\n1. Report C4 stratified by GT label as the PRIMARY result (table above)\\n2. Aggregate C4 only as context, with explicit caveat about non-significance\\n3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness\\n4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)\\n\\n## Story Spine\\n\\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\\n\\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\\n\\n- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).\\n\\n- **Headline result template**: \\\"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\\\"\\n\\n## Venue Fit\\n\\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| # | Concern | Response Strategy | Required Experiment |\\n|---|---------|-------------------|---------------------|\\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\\n| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |\\n| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |\\n| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as \\\"cross-representation\\\" is imprecise | Frame MATH domain as \\\"cross-executable-paradigm\\\" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |\\n| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |\\n\", \"total_chars\": 9217, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ced3936b-c88e-4857-926d-15127468f16d",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "784e1085-0ce1-478d-87b4-731404a21041",
  "sourceToolAssistantUUID": "ced3936b-c88e-4857-926d-15127468f16d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T07:50:13.648Z_

Now let me read the existing dream review reports for additional context, and the ideas/literature files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "784e1085-0ce1-478d-87b4-731404a21041",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zJD97B7ydrcgab4Qz7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44b2cb62-cbff-4e3c-876c-e6e93ac83c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEqoz7wJVNps1FvURLCZom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20116,
      "cache_read_input_tokens": 18779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20116,
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

_source line 20 · 2026-05-15T07:50:14.617Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W8xR9g9XbKAm9hzXmYT68x`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b2cb62-cbff-4e3c-876c-e6e93ac83c97",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zJD97B7ydrcgab4Qz7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c2ed729-1a18-41c4-8dfc-c37035e21f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEqoz7wJVNps1FvURLCZom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20116,
      "cache_read_input_tokens": 18779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20116,
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

_source line 21 · 2026-05-15T07:50:14.626Z_

<details><summary>↩ Tool result · `toolu_01W8xR9g9XbKAm9hzXmYT68x`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c2ed729-1a18-41c4-8dfc-c37035e21f8b",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "baf16b6e-36f4-4c2e-8c87-59536d1d3522",
  "sourceToolAssistantUUID": "3c2ed729-1a18-41c4-8dfc-c37035e21f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T07:50:16.970Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TDd6UrbL2qcncX2seRiH3C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baf16b6e-36f4-4c2e-8c87-59536d1d3522",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zJD97B7ydrcgab4Qz7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f769e73a-3478-446b-bcb0-a4c33b010025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEqoz7wJVNps1FvURLCZom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20116,
      "cache_read_input_tokens": 18779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20116,
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

_source line 23 · 2026-05-15T07:50:16.978Z_

<details><summary>↩ Tool result · reported error · `toolu_01TDd6UrbL2qcncX2seRiH3C`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f769e73a-3478-446b-bcb0-a4c33b010025",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "114bdeba-74b7-49e5-8951-f6938c4888d5",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno.",
  "sourceToolAssistantUUID": "f769e73a-3478-446b-bcb0-a4c33b010025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T07:50:17.686Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MgMGYaTwgmNxmv7vyAt7Gv`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "114bdeba-74b7-49e5-8951-f6938c4888d5",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zJD97B7ydrcgab4Qz7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "314f0e88-b915-4402-828a-9149b2bc3d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEqoz7wJVNps1FvURLCZom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20116,
      "cache_read_input_tokens": 18779,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20116
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 315,
          "cache_read_input_tokens": 18779,
          "cache_creation_input_tokens": 20116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20116,
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

_source line 25 · 2026-05-15T07:50:17.707Z_

<details><summary>↩ Tool result · `toolu_01MgMGYaTwgmNxmv7vyAt7Gv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "314f0e88-b915-4402-828a-9149b2bc3d02",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "426eca7d-7144-4e43-bb82-3c0f7423ea8f",
  "sourceToolAssistantUUID": "314f0e88-b915-4402-828a-9149b2bc3d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T07:50:19.906Z_

Let me check the existing dream review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "426eca7d-7144-4e43-bb82-3c0f7423ea8f",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zJubSuv5ebXFdGp98o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cef30679-1424-4399-a85d-5552507b903b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQZZrub9ZWniGn1oktY3sk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 38895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 666,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 27 · 2026-05-15T07:50:20.848Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TaPxLW9UKwPZJ3CpAHqXv5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cef30679-1424-4399-a85d-5552507b903b",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zJubSuv5ebXFdGp98o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d18e2d6f-5431-4ced-970e-c0cfa26064ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQZZrub9ZWniGn1oktY3sk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 38895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 666,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 28 · 2026-05-15T07:50:20.856Z_

<details><summary>↩ Tool result · `toolu_01TaPxLW9UKwPZJ3CpAHqXv5`</summary>

```text
1	---
2	dream_id: dream_20260515T060408
3	tier: best
4	overall_score: borderline reject
5	timestamp: 2026-05-15T06:52:42.017080+00:00
6	---
7	
8	## R2: Novelty and Related Work
9	
10	### Summary
11	This paper studies cross-representation disagreement (CRD) as a diagnostic signal for LLM formalization errors: when the same LLM formalizes a reasoning problem into FOL (verified by Z3) and executable Python, disagreements identify formalization errors with 81-87% precision across three benchmarks. The paper further proposes taxonomy-guided multi-round repair achieving +10.8pp over blind regeneration. While the empirical analysis is thorough on its primary benchmark (FOLIO), the claimed novelty -- using cross-representation disagreement for diagnosis rather than filtering -- is an incremental step beyond Liang et al. (2024), and several significant related works are missing.
12	
13	### Strengths
14	- S1: **Well-defined research question with honest framing.** The paper asks "when and why does CRD work?" rather than overclaiming a general framework. The boundary characterization (GPQA results showing degradation) is a genuine contribution that papers in this space rarely provide. The intellectual honesty of including negative/boundary results strengthens credibility.
15	
16	- S2: **The domain-dependent asymmetry finding is novel and interesting.** The observation that FOL dominates 7-9:1 in logic domains while code dominates 2.3:1 in mathematics is a non-obvious finding that reveals something meaningful about LLM formalization capabilities across paradigms. This has independent value as a diagnostic for understanding LLM strengths/weaknesses.
17	
18	- S3: **The Unknown confound analysis is the paper's strongest analytical contribution.** The decomposition showing that repair gains concentrate on GT=Unknown samples -- where Python structurally cannot implement three-valued logic while Z3 handles it natively -- is a genuine insight. This is not just a limitation disclosure; it reveals a fundamental asymmetry in representation expressiveness that the community should know about.
19	
20	- S4: **Reasonable experimental design with appropriate statistical rigor.** Bootstrap CIs, McNemar's test, and the inclusion of confidence intervals in all main tables meet the bar for statistical reporting. The cross-model ablation directly addresses the correlated failure concern from Denisov-Blanch (2026).
21	
22	- S5: **The selection vs. repair comparison (Table 8) is informative.** Showing that simple selection nearly matches repair at zero compute cost is a useful practical finding, and the analysis of repair's robustness to localization errors adds nuance.
23	
24	### Weaknesses
25	- W1: **Incremental novelty over Liang et al. (2024).** The core idea -- that cross-representation disagreement is informative -- was established by Liang et al. (2024) for CoT-PoT pairs. This paper's contribution is extending disagreement from "filtering" to "diagnosis + localization + repair." However, the diagnosis step is itself a straightforward LLM prompt (Section 3.3: ask the LLM which side is wrong and why), and the repair improvement is modest (+10.8pp best-case, and the worst-case scenario reveals this may be +5.2pp with p=0.078). The conceptual leap from "disagreement as filter" to "disagreement as diagnosis" is smaller than the paper suggests.
26	
27	- W2: **Significant related work omissions.** The paper cites only 17 references for a 12-page empirical analysis paper at a top venue. Notable omissions include:
28	  - **Self-consistency / universal self-consistency** (Wang et al. 2023, Chen et al. 2023): Multi-sample agreement as a signal is closely related to cross-representation agreement; the paper should discuss why cross-representation disagreement differs from self-consistency within a single representation.
29	  - **SatLM (Ye et al. 2024)** is cited but only in passing; its SAT-based verification approach is directly comparable to Z3-based verification.
30	  - **LEVER (Ni et al. 2023)**: Verification of LLM-generated programs via execution, directly relevant to the code-side verification.
31	  - **Faithful CoT (Lyu et al. 2023)**: Generates both NL reasoning and symbolic programs for verification -- essentially a dual-representation approach.
32	  - **Self-refine / self-debug / self-repair literature** (Madaan et al. 2023, Chen et al. 2024, Olausson et al. 2024): The taxonomy-guided repair is a form of self-repair; positioning against this literature is missing.
33	  - **Multi-agent debate / verification** (Du et al. 2023, Liang et al. 2024): Cross-representation can be viewed as a special case of multi-agent verification where the "agents" are different formalizations.
34	
35	- W3: **The "HybridMind" and "Adaptive Selection" references are incomplete/suspicious.** References [6] and [7] in the bibliography lack author names and appear to be placeholder entries (just titles with venue). "Prove (2024)" similarly lacks full bibliographic information. For a venue submission, incomplete references raise concerns about citation integrity. If these are real papers, they need proper attribution; if they are placeholders for papers the authors couldn't find exact references for, this is a serious issue.
36	
37	- W4: **Cross-benchmark consistency may be artifactual.** The remarkably consistent metrics across benchmarks (C1: 37-42%, C2: 81-87%, C5: 82-85%) are suspiciously uniform. Natural variation across fundamentally different benchmarks (deductive logic vs. competition math) would typically produce wider spreads. The Cochran's Q test claiming homogeneity (I^2=18.3%) further raises this concern -- one would expect domain-specific effects to produce heterogeneity, and the paper's own asymmetry analysis (Section 5.2) shows the representations behave very differently across domains, which should propagate to diagnostic metrics.
38	
39	- W5: **The error taxonomy is rule-based and not validated.** The taxonomy (Predicate Mapping, Quantifier Scope, Negation Handling for logic; Variable Mapping, Computation Error, Constraint Omission, Type Mismatch for math) is manually defined. No inter-annotator agreement is reported for the LLM-generated classifications. How reliable is the LLM at classifying its own errors? If the same model that made the error is classifying it, there's a circularity concern. The paper acknowledges this in limitations but doesn't quantify the impact.
40	
41	- W6: **The "first systematic study" claim is overclaimed.** The paper claims to present "the first systematic study of cross-representation disagreement as a diagnostic signal." Liang et al. (2024) already systematically studied cross-representation (CoT-PoT) agreement patterns. The novelty is in the specific FOL-vs-Code pairing and the diagnosis/repair extension, not in being the first to study cross-representation disagreement systematically.
42	
43	- W7: **Repair contribution is weak and acknowledged as secondary.** The best-case +10.8pp (p=0.008) after 3 rounds of type-specific repair is the optimistic scenario. The paper's own analysis notes that on single-round generic repair, the delta is only +5.2pp with Excl-Unknown at +0.0pp. If the multi-round type-specific repair doesn't deliver, the paper must rely on "diagnosis as analysis, not repair" -- a valid but narrower contribution that may not clear the main conference bar.
44	
45	### Questions for Authors
46	- Q1: How does cross-representation disagreement differ conceptually from self-consistency (Wang et al. 2023) applied across representation types? Is the key differentiator the use of formal verification (Z3) on one side, or the cross-representation structure itself? If it's Z3, then the contribution reduces to "using a verified representation as a reference standard," which is less novel.
47	
48	- Q2: For the error taxonomy validation: did you perform any human evaluation of the LLM-generated error classifications? What is the agreement rate between the LLM's error type labels and human expert judgment? Without this, the error type distribution tables (Tables 4, 5) have unknown reliability.
49	
50	- Q3: The cross-model ablation (Table 6) shows a 6.7pp reduction in false agreement rate. Is this statistically significant? How many of the 13 converted "both wrong, same answer" cases actually led to correct final answers after diagnosis?
51	
52	- Q4: The paper uses "approximately" (~) for many counts in Tables 4 and 5 (e.g., "~28", "~22"). Why are exact counts not available for completed experiments? This gives the impression of estimated rather than measured results.
53	
54	- Q5: Selection outperforms repair when localization is correct (Table 8). Given that localization accuracy is 82-85%, why not recommend selection as the primary strategy? The +1.5pp advantage of repair seems not worth the additional compute cost of 3 repair rounds.
55	
56	### Minor Issues
57	- The related work section (Section 2) is organized by paragraph headings that don't fully capture the landscape. A table comparing this work against prior cross-representation methods on key dimensions (filter vs. diagnose vs. repair, single vs. cross representation, # benchmarks, etc.) would strengthen positioning.
58	- Tables 4 and 5 use approximate counts (~) which is unusual for empirical results. Either report exact numbers or explain why approximation is necessary.
59	- The VeriCoT, VERGE, Roundtrip, HybridMind, Adaptive Selection, and Prove references need complete bibliographic entries with authors.
60	- "First-order logic" representations for MATH Level 5 (competition math) are described as "CoT" in Table 3 but "chain-of-thought" in Section 3.2 -- this is inconsistent with the FOL framing elsewhere. The paper should clarify that MATH uses CoT+SymPy rather than FOL+Code.
61	- The Cochran's Q homogeneity test in Section 5.1 is typically used for binary outcomes in meta-analysis; its application to diagnostic precision rates across three benchmarks from the same study is methodologically unusual and should be justified.
62	
63	### Scores
64	- Soundness: 3/5
65	- Contribution: 3/5
66	- Presentation: 4/5
67	- Overall: 3/6
68	- Confidence: 4/5
69	
70	### Meta-Assessment
71	Borderline reject. The paper has a well-defined question and honest framing, but the novelty increment over Liang et al. (2024) is modest, the related work coverage has significant gaps, several references appear incomplete or fabricated, and the strongest empirical contribution (repair) rests on potentially fragile results. The diagnostic analysis and boundary characterization have value, but whether they clear the bar for a top-venue main conference paper at ~25% acceptance rate is questionable. The Unknown confound discovery and domain-dependent asymmetry are the most publishable findings, but they may be better suited for Findings track.
72	
73	### Actionable Recommendations for Authors
74	1. **Add 10-15 missing references** (self-consistency, LEVER, Faithful CoT, self-refine/debug, multi-agent debate) and properly position against them. This is the single most impactful revision.
75	2. **Fix incomplete bibliography entries** for HybridMind, Adaptive Selection, Prove, VeriCoT, VERGE, Roundtrip. Every reference must have authors.
76	3. **Soften the "first systematic study" claim** to "first study of cross-representation disagreement for error diagnosis and targeted repair" -- Liang et al. already studied cross-representation disagreement systematically for filtering.
77	4. **Add human evaluation of error taxonomy** -- even a small-scale annotation (50 samples, 2 annotators) would address W5.
78	5. **If multi-round repair doesn't reach significance on non-Unknown samples**, pivot the paper to "diagnosis as analysis" and frame repair as a downstream application that works in specific conditions (GT=Unknown, high asymmetry). This is more defensible than claiming repair works generally.
79	6. **Explain the suspicious cross-benchmark uniformity** (W4) -- if the numbers are real, discuss why diagnostic precision is so consistent despite very different task structures. If projections, be explicit about which benchmarks have completed experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d18e2d6f-5431-4ced-970e-c0cfa26064ed",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "658a75fe-6b27-4d21-8681-74dfee1c9bc2",
  "sourceToolAssistantUUID": "d18e2d6f-5431-4ced-970e-c0cfa26064ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T07:50:21.531Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DNht1ghpPJK2FKRNM65pWJ`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260515T071730/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "658a75fe-6b27-4d21-8681-74dfee1c9bc2",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zJubSuv5ebXFdGp98o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a8f357a-7e07-4929-bdc4-a09f524d6276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQZZrub9ZWniGn1oktY3sk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 38895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 666,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 30 · 2026-05-15T07:50:21.570Z_

<details><summary>↩ Tool result · `toolu_01DNht1ghpPJK2FKRNM65pWJ`</summary>

```text
artifacts/dream_reports/dream_20260515T071730/best/review_context.yaml
artifacts/dream_reports/dream_20260515T071730/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a8f357a-7e07-4929-bdc4-a09f524d6276",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "63868240-d19d-468d-8505-8a28df237914",
  "sourceToolAssistantUUID": "2a8f357a-7e07-4929-bdc4-a09f524d6276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T07:50:25.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_018VUjpUK6phmCdVnuVq2yF4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63868240-d19d-468d-8505-8a28df237914",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zKCCqDqZHr4NQRyP7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "896b04bc-305e-474f-bb22-f305a01e1c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJPxNoyuNtTwmuroRYMUaE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3377,
      "cache_read_input_tokens": 39561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3377,
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

_source line 32 · 2026-05-15T07:50:25.554Z_

<details><summary>↩ Tool result · `toolu_018VUjpUK6phmCdVnuVq2yF4`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation
2	  self-consistency 更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定，
3	  C3 的 GT-label-dependent 效应在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。 Selection
4	  ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered boundary
5	  是加分项而非弱点。
6	
7	  '
8	imagined_experiments:
9	- name: FOLIO 完整分析（MVP 数据深度挖掘）
10	  plan_id: exp-001
11	  description: '基于 204 样本 MVP 数据的统计检验、错误分类、子集分层分析、不对称性 breakdown、 失败相关性定量分析和 cost-effectiveness
12	    分析。纯分析，无新实验运行。
13	
14	    '
15	  expected_results:
16	    C1_disagree_rate: 42.16% [35.3%, 49.0%]
17	    C2_diagnostic_rate: 87.21% [81.3%, 94.7%]
18	    C3_error_types: 4
19	    C4_targeted_delta_aggregate: +4.65pp (Fisher p=0.626, n.s.)
20	    C4_GT_True: -13.6pp
21	    C4_GT_False: +11.6pp
22	    C4_GT_Unknown: +14.7pp
23	    C5_committed_accuracy: 94.6% (35/37)
24	    C5_coverage: 53.0% (35/66)
25	    asymmetry_ratio: 5.6:1 (FOL=56, Code=10, Both=10)
26	    phi_coefficient: 0.189
27	    phi_p_value: 0.007
28	    complementary_error_rate: 75% (75/100)
29	    cost_multiplier_vs_code_only: 5.76x tokens
30	    accuracy_gain_over_code_only: +21.6pp
31	    dominant_error: logic_error 25.5%
32	  result_rationale: '这是已有 MVP 数据的深度挖掘，数值已固定。在 best 档位下，关键价值在于：(1) Bootstrap CI 对 C1/C2
33	    给出了紧致的区间，C2 下界 81.3% 远超 75% 阈值，为高精度诊断信号提供统计支撑； (2) phi=0.189 (p=0.007) 表明 FOL/Code
34	    失败相关性低但统计显著——恰好落在"足够独立以产生互补信号， 又不完全独立"的理想区间；(3) 75% 单侧失败率直接支撑 cross-representation
35	    的互补性叙事； (4) GT-stratified C4 揭示三路分裂是 Claim 3 的核心发现，aggregate 非显著反而强化了 "必须分层报告"的方法论贡献。cost_multiplier
36	    5.76x 看似高，但对比 k=5 self-consistency 的 5x 成本，CRD 以相近成本获得更丰富的诊断信息（错误类型 + 定位），而非仅
37	    majority vote。
38	
39	    '
40	  tables:
41	  - name: 'Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI'
42	    columns:
43	    - Metric
44	    - Point Estimate
45	    - 95% CI
46	    - MVP Gate
47	    rows:
48	    - - C1 (Disagree Rate)
49	      - 42.16%
50	      - '[35.3%, 49.0%]'
51	      - PASS (≥15%)
52	    - - C2 (Diagnostic Rate)
53	      - 87.21%
54	      - '[81.3%, 94.7%]'
55	      - PASS (≥75%)
56	    - - C3 (Error Types)
57	      - 4 types
58	      - —
59	      - PASS (≥3)
60	    - - C4 (Repair Delta)
61	      - +4.65pp
62	      - '[-8.8%, +18.1%]'
63	      - FAIL (CI includes 0)
64	    - - C5 (Localization)
65	      - 53.0%
66	      - '[41.0%, 65.1%]'
67	      - FAIL (<70%)
68	  - name: 'Table 2: GT-Label-Stratified Repair Effect'
69	    columns:
70	    - GT Label
71	    - n
72	    - Targeted Acc
73	    - Blind Acc
74	    - Delta
75	    - Interpretation
76	    rows:
77	    - - 'True'
78	      - 72
79	      - 63.6%
80	      - 77.3%
81	      - -13.6pp
82	      - Overcorrection
83	    - - 'False'
84	      - 63
85	      - 76.7%
86	      - 70.0%
87	      - +6.7pp
88	      - Modest help
89	    - - Unknown
90	      - 69
91	      - 67.7%
92	      - 52.9%
93	      - +14.7pp
94	      - Diagnosis helps
95	  - name: 'Table 3: Error Taxonomy Distribution'
96	    columns:
97	    - Error Type
98	    - Count
99	    - Proportion
100	    rows:
101	    - - logic_error
102	      - 52
103	      - 25.5%
104	    - - negation_error
105	      - 22
106	      - 10.8%
107	    - - exec_crash
108	      - 11
109	      - 5.4%
110	    - - quantifier_error
111	      - 4
112	      - 2.0%
113	  figures_description:
114	  - 'Fig 1: Confusion matrix heatmap — FOL correct/wrong × Code correct/wrong，标注 5.6:1
115	    不对称'
116	  - 'Fig 2: GT-stratified repair delta bar chart，三色柱状图显示三路分裂效应'
117	  - 'Fig 3: phi coefficient 按 GT label 分层的热图'
118	  analysis: 'exp-001 作为 anchor 实验，所有数值已确定。best 档位下的分析重点是将 C4 aggregate 非显著 和 C5 低覆盖率重新
119	    frame 为方法论发现而非失败：(1) aggregate 非显著正是因为 GT-label-dependent 效应相互抵消，分层报告是正确的分析粒度；(2)
120	    C5 coverage 53% 但 committed accuracy 94.6% 是高精度/低召回的 deliberate tradeoff，ambiguous
121	    标签中 61% 来自 GT=Unknown 驱动—— 这些样本恰好是 repair delta 最大的子集，说明即使定位不确定，disagreement pattern
122	    本身 就有修复价值。
123	
124	    '
125	- name: 跨模型消融（FOLIO）
126	  plan_id: exp-002
127	  description: '三组条件：(a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro
128	    within-model, (c) DeepSeek FOL + Qwen Code cross-model。区分分歧来源。
129	
130	    '
131	  expected_results:
132	    deepseek_within_C1: 38.7%
133	    deepseek_within_C2: 83.5%
134	    deepseek_within_C2_CI: '[74.2%, 91.8%]'
135	    deepseek_within_asymmetry: 4.2:1 (FOL-favored)
136	    deepseek_within_C4_GT_Unknown: +12.1pp
137	    deepseek_within_C4_GT_True: -10.3pp
138	    deepseek_within_C4_GT_False: +8.4pp
139	    cross_model_C1: 47.5%
140	    cross_model_C2: 80.9%
141	    cross_model_asymmetry: 3.8:1 (FOL-favored)
142	    C2_delta_vs_MVP: -3.7pp (within ±8pp gate)
143	    asymmetry_direction: consistent (FOL-favored in all 3 conditions)
144	  result_rationale: '在 best 档位下，DeepSeek within-model C2 落在 MVP ±8pp 内（83.5% vs 87.2%，delta=-3.7pp），
145	    证明诊断精度不是 Qwen3-32B 的特异性质，而是 cross-representation disagreement 的结构性属性。 DeepSeek
146	    C1 略低（38.7% vs 42.2%）合理——DeepSeek 作为更强模型，两条表征路径各自精度更高， 分歧率自然略低，但 C2 保持在 80%+ 说明分歧样本仍然高度诊断性。不对称方向一致（FOL-favored）
147	    是关键：这不是模型偶然，而是 FOL+Z3 的形式验证保证系统性地比 Python 执行更可靠。 Cross-model 条件 C1 更高（47.5%）因为两个不同模型的
148	    formalization bias 不同， 增加了分歧概率，但 C2 略降（80.9%）因为部分分歧来自模型差异而非 formalization 错误。
149	    这个分离正好支撑论文的核心论点：within-model cross-representation disagreement 更纯粹地反映 formalization
150	    错误，cross-model 混入了 capability 噪声。
151	
152	    '
153	  tables:
154	  - name: 'Table 4: Cross-Model Ablation Results on FOLIO (n=204)'
155	    columns:
156	    - Condition
157	    - C1
158	    - C2
159	    - C2 95% CI
160	    - Asymmetry
161	    - C4 (Unknown)
162	    - C4 (True)
163	    rows:
164	    - - Qwen3-32B within (MVP)
165	      - 42.2%
166	      - 87.2%
167	      - '[81.3%, 94.7%]'
168	      - 5.6:1 FOL
169	      - +14.7pp
170	      - -13.6pp
171	    - - DeepSeek within
172	      - 38.7%
173	      - 83.5%
174	      - '[74.2%, 91.8%]'
175	      - 4.2:1 FOL
176	      - +12.1pp
177	      - -10.3pp
178	    - - DeepSeek×Qwen cross
179	      - 47.5%
180	      - 80.9%
181	      - '[71.8%, 89.1%]'
182	      - 3.8:1 FOL
183	      - +9.8pp
184	      - -8.7pp
185	  figures_description:
186	  - 'Fig 4: 三条件 C1/C2 对比柱状图，带 error bars'
187	  - 'Fig 5: 不对称比例的 stacked bar，三条件均 FOL-favored'
188	  analysis: '三组数据形成清晰的叙事梯度：within-model(同模型) > cross-model(跨模型) 在 C2 上， 说明 within-model
189	    的诊断信号更纯净。DeepSeek GT-stratified 效应方向完全一致 （Unknown 正, True 负, False 正），证明 Claim
190	    3 的 GT-label-dependent 效应 是表征结构属性而非模型特异。C2 delta -3.7pp 在 ±8pp gate 内——这是 best
191	    档的 sweet spot，既证明泛化，又不大到暗示 MVP 是 outlier。
192	
193	    '
194	- name: ProofWriter / LogiQA 扩展
195	  plan_id: exp-003
196	  description: '第二逻辑推理基准。先 pilot 20-30 样本验证 disagree_rate ≥ 10%， 通过则全量跑 ProofWriter；失败则切换
197	    LogiQA。
198	
199	    '
200	  expected_results:
201	    dataset_used: LogiQA
202	    pilot_proofwriter_disagree_rate: 6.7% (2/30) — pilot FAIL
203	    pilot_switch_reason: ProofWriter 合成数据过于规则，FOL/Code 均高精度 (>93%)，分歧率不足
204	    logiqA_n: 200
205	    logiqA_C1: 34.0%
206	    logiqA_C2: 81.5%
207	    logiqA_C2_CI: '[73.8%, 88.2%]'
208	    logiqA_C3_error_types: 4
209	    logiqA_asymmetry: 3.2:1 (FOL-favored)
210	    logiqA_C4_GT_stratified_positive_subset: +11.3pp
211	    logiqA_C4_GT_stratified_negative_subset: -9.8pp
212	    logiqA_C5_committed: 91.2%
213	    logiqA_C5_coverage: 48.5%
214	  result_rationale: '在 best 档位下，ProofWriter pilot 失败是预期且合理的——合成数据的逻辑结构简单规则， 两条表征路径都能高精度处理，分歧率仅
215	    6.7%。这不是坏消息：切换到 LogiQA（自然语言逻辑， 4 选 1）反而更好，因为 NL 歧义性更高，更能展示 CRD 在真实场景中的价值。LogiQA
216	    C1=34% 略低于 FOLIO（42%）合理——选择题格式约束了输出空间，减少了 formalization 分歧；但 C2=81.5% 仍然高（≥75%
217	    gate），证明分歧样本跨基准稳定诊断。不对称比仍 FOL-favored（3.2:1）但比 FOLIO 的 5.6:1 低——LogiQA 的命题逻辑复杂度低于
218	    FOLIO 的一阶逻辑，FOL 路径的优势 相对缩小。GT-stratified 效应方向复现（正/负分裂），证明 Claim 3 跨基准泛化。 C5 committed
219	    91.2% 保持在 90%+ 高精度区间。
220	
221	    '
222	  tables:
223	  - name: 'Table 5: LogiQA Results (n=200, Qwen3-32B)'
224	    columns:
225	    - Metric
226	    - LogiQA
227	    - FOLIO (ref)
228	    - Delta
229	    rows:
230	    - - C1 (Disagree Rate)
231	      - 34.0%
232	      - 42.2%
233	      - -8.2pp
234	    - - C2 (Diagnostic Rate)
235	      - 81.5%
236	      - 87.2%
237	      - -5.7pp
238	    - - C3 (Error Types)
239	      - '4'
240	      - '4'
241	      - —
242	    - - C5 Committed Acc
243	      - 91.2%
244	      - 94.6%
245	      - -3.4pp
246	    - - Asymmetry (FOL:Code)
247	      - 3.2:1
248	      - 5.6:1
249	      - narrower
250	  - name: 'Table 5b: ProofWriter Pilot Results (n=30)'
251	    columns:
252	    - Metric
253	    - Value
254	    - Gate
255	    - Decision
256	    rows:
257	    - - Disagree Rate
258	      - 6.7%
259	      - ≥10%
260	      - FAIL → switch to LogiQA
261	    - - FOL Accuracy
262	      - 93.3%
263	      - —
264	      - —
265	    - - Code Accuracy
266	      - 90.0%
267	      - —
268	      - —
269	  figures_description:
270	  - 'Fig 6: FOLIO vs LogiQA C1/C2 并排对比，带 CI error bars'
271	  - 'Fig 7: LogiQA GT-stratified repair delta 复现 FOLIO 三路分裂模式'
272	  analysis: 'LogiQA 作为第二基准完美补充 FOLIO：不同数据源（中国公务员考试 vs 专家标注 FOL）， 不同任务格式（4 选 1 vs 3
273	    分类），C2 仍在 [75%, 92%] range 内。ProofWriter pilot 失败在论文中可以作为 1 段讨论："合成数据过于规则，分歧信号需要自然语言的
274	    formalization 挑战"——这反而强化了 CRD 适用场景的 characterization。
275	
276	    '
277	- name: MATH Level 5 双可执行表征扩展
278	  plan_id: exp-004
279	  description: 'MATH Level 5 使用 SymPy 符号推理 vs Python 数值计算两条可执行路径， 保持 cross-executable-representation
280	    框架一致性。
281	
282	    '
283	  expected_results:
284	    n: 200
285	    math_C1: 28.5%
286	    math_C2: 76.0%
287	    math_C2_CI: '[66.1%, 85.2%]'
288	    math_C3_error_types: 3
289	    math_asymmetry: 1.8:1 (Code-favored)
290	    math_asymmetry_direction: 反转——Python 数值计算在 MATH 上优于 SymPy 符号推理
291	    math_C4_GT_correct_delta: +3.2pp
292	    math_C4_GT_wrong_delta: +7.8pp
293	    math_C5_committed: 88.5%
294	    math_C5_coverage: 55.0%
295	    sympy_crash_rate: 12.5%
296	    python_crash_rate: 4.0%
297	  result_rationale: '在 best 档位下，MATH C1=28.5% 满足 ≥15% gate。C1 低于 FOLIO（42%）合理—— 数学问题有唯一正确答案，两条计算路径比逻辑推理的
298	    formalization 更容易达成一致。 C2=76% 刚好在 [70%, 85%] 范围内——数学分歧中更多是计算错误而非 formalization
299	    错误， 部分分歧来自数值精度问题（如浮点近似 vs 精确符号解），诊断性略低但仍超 70% gate。 关键发现：不对称方向反转（Code-favored
300	    1.8:1），与 FOLIO 的 FOL-favored 5.6:1 相反。 这是 best 档的 killer result——证明不对称性不是 FOL
301	    固有优势，而是表征-任务匹配： 在逻辑推理上 FOL+Z3 有形式验证优势，在数学计算上 Python 的灵活数值方法更鲁棒。 SymPy crash rate
302	    12.5% > Python 4% 因为 SymPy 对输入格式敏感（符号化简失败、 方程无解析解等），而 Python 数值方法更容错。这个反转直接回应
303	    R5（"不只是 FOL-as-verifier"）。
304	
305	    '
306	  tables:
307	  - name: 'Table 6: MATH Level 5 Results (n=200, Qwen3-32B)'
308	    columns:
309	    - Metric
310	    - MATH
311	    - FOLIO (ref)
312	    - LogiQA (ref)
313	    rows:
314	    - - C1 (Disagree Rate)
315	      - 28.5%
316	      - 42.2%
317	      - 34.0%
318	    - - C2 (Diagnostic Rate)
319	      - 76.0%
320	      - 87.2%
321	      - 81.5%
322	    - - C3 (Error Types)
323	      - '3'
324	      - '4'
325	      - '4'
326	    - - Asymmetry
327	      - 1.8:1 Code-fav
328	      - 5.6:1 FOL-fav
329	      - 3.2:1 FOL-fav
330	    - - C5 Committed
331	      - 88.5%
332	      - 94.6%
333	      - 91.2%
334	  - name: 'Table 7: Asymmetry Direction Across Domains'
335	    columns:
336	    - Domain
337	    - Representation A
338	    - Representation B
339	    - Favored
340	    - Ratio
341	    rows:
342	    - - Logic (FOLIO)
343	      - FOL+Z3
344	      - Python exec
345	      - FOL
346	      - 5.6:1
347	    - - Logic (LogiQA)
348	      - FOL+Z3
349	      - Python exec
350	      - FOL
351	      - 3.2:1
352	    - - Math (MATH)
353	      - SymPy symbolic
354	      - Python numerical
355	      - Python
356	      - 1.8:1
357	  figures_description:
358	  - 'Fig 8: 三基准 asymmetry direction 可视化——逻辑 vs 数学域的反转'
359	  - 'Fig 9: MATH 错误类型分布（computation_error, symbolic_failure, exec_crash）'
360	  analysis: 'MATH 的不对称反转是 best 档位的标志性结果。它将 paper 的 story 从 "FOL is better" 升级为 "cross-representation
361	    disagreement reveals domain-specific representation strengths"——更深层的洞察，更广的适用性。C2=76%
362	    虽然低于 FOLIO，但 CI 下界 66.1% 接近 70% gate，在 best 档位下 point estimate 通过。C3=3 types（少了
363	    quantifier_error， 因为数学域没有量词问题），但新增 computation_error（截断/精度）类型。
364	
365	    '
366	- name: Repair 机制改进（多轮修复）
367	  plan_id: exp-005
368	  description: '最多 3 轮 repair，加入错误类型特定修复策略，按 GT label 和 error_type 分层报告。 目标：Unknown
369	    子组 delta 从 +14.7pp 拉到 +20pp+。
370	
371	    '
372	  expected_results:
373	    repair_rounds_avg: 1.8
374	    GT_Unknown_delta_round1: +14.7pp
375	    GT_Unknown_delta_round3: +22.1pp
376	    GT_False_delta_round1: +6.7pp
377	    GT_False_delta_round3: +10.4pp
378	    GT_True_delta_round1: -13.6pp
379	    GT_True_delta_round3: -11.2pp
380	    C4_unknown_false_combined_delta: +15.8pp
381	    error_type_repair_success:
382	      logic_error: 68.3%
383	      negation_error: 72.0%
384	      exec_crash: 81.8%
385	      quantifier_error: 50.0%
386	    round2_additional_fixes: 8 samples
387	    round3_additional_fixes: 3 samples
388	  result_rationale: '在 best 档位下，多轮 repair 将 GT=Unknown delta 从 +14.7pp 拉到 +22.1pp（超过
389	    +20pp gate）。 机制：第一轮修复了大部分 Code overclaiming（Code 输出 True/False 但应为 Unknown）， 第二轮处理残余的
390	    logic_error（FOL 形式化中的量词/否定遗漏导致第一轮修复方向偏移）， 第三轮边际收益递减（仅 3 个 additional fix）。GT=True
391	    overcorrection 从 -13.6pp 改善到 -11.2pp——多轮 repair 的错误类型感知策略对 GT=True 的伤害略有缓解 （negation_error
392	    特定策略避免了盲目翻转），但仍然为负，证明 overcorrection boundary 是结构性的而非策略不足。exec_crash 81.8% 修复率最高因为这类错误最容易诊断和修复
393	    （语法/运行时错误，重新生成即可）。quantifier_error 50% 最低因为量词错误需要 深层理解全称/存在量词的语义。combined delta
394	    +15.8pp 落在 [8, 18] range 的偏高区域。
395	
396	    '
397	  tables:
398	  - name: 'Table 8: Multi-Round Repair Results (FOLIO, n=204)'
399	    columns:
400	    - GT Label
401	    - n
402	    - Round 1 Delta
403	    - Round 3 Delta
404	    - Improvement
405	    rows:
406	    - - Unknown
407	      - 69
408	      - +14.7pp
409	      - +22.1pp
410	      - +7.4pp
411	    - - 'False'
412	      - 63
413	      - +6.7pp
414	      - +10.4pp
415	      - +3.7pp
416	    - - 'True'
417	      - 72
418	      - -13.6pp
419	      - -11.2pp
420	      - +2.4pp (still negative)
421	  - name: 'Table 9: Repair Success Rate by Error Type (Round 3)'
422	    columns:
423	    - Error Type
424	    - Attempted
425	    - Fixed
426	    - Success Rate
427	    rows:
428	    - - logic_error
429	      - 41
430	      - 28
431	      - 68.3%
432	    - - negation_error
433	      - 18
434	      - 13
435	      - 72.0%
436	    - - exec_crash
437	      - 11
438	      - 9
439	      - 81.8%
440	    - - quantifier_error
441	      - 4
442	      - 2
443	      - 50.0%
444	  figures_description:
445	  - 'Fig 10: 多轮 repair 收益曲线（Round 1/2/3 delta 按 GT label）'
446	  - 'Fig 11: 错误类型特定修复成功率 bar chart'
447	  analysis: '多轮 repair 的递减收益模式（Round 1: +14.7→+22.1, Round 2: +5.2, Round 3: +2.2）
448	    是 best 档位的理想结果——证明错误类型特定策略有增量价值，但不是无限的。 GT=True 仍为负是论文的 honesty signal——不掩饰 boundary。错误类型分层报告
449	    为 exp-008（taxonomy ablation）提供了直接支撑。
450	
451	    '
452	- name: Unknown 样本深度分析 + correlated failure 定量
453	  plan_id: exp-006
454	  description: '分析 GT=Unknown 驱动 C4 delta 的机制，FOL/Code 相关系数按 GT 分层， false agreement
455	    rate，specification vs formalization 错误分类。
456	
457	    '
458	  expected_results:
459	    code_overclaiming_rate_unknown: 78.3% (54/69)
460	    code_overclaiming_mechanism: Code 路径倾向输出 True/False 而非 Unknown，因为 Python 缺乏三值逻辑原生支持
461	    fol_overclaiming_rate_unknown: 21.7% (15/69)
462	    phi_by_GT:
463	      'True': 0.245
464	      'False': 0.162
465	      Unknown: 0.098
466	    false_agreement_rate: 12.3% (25/204)
467	    false_agreement_breakdown: GT=True 14/72 (19.4%), GT=False 7/63 (11.1%), GT=Unknown
468	      4/69 (5.8%)
469	    specification_error_rate: 8.3% (17/204)
470	    formalization_specific_error_rate: 91.7% (187/204 non-spec-error)
471	  result_rationale: '在 best 档位下，Code overclaiming 78.3% 的高比率清晰解释了 GT=Unknown 子集的 repair
472	    delta 来源：Python 执行路径缺乏三值逻辑（True/False/Unknown）的原生表达能力， 倾向将 insufficient-information
473	    情况强制映射为 True 或 False。当 CRD 诊断出分歧后， repair prompt 包含"FOL 路径返回 Unknown"的信息，帮助模型认识到证据不足，修正
474	    Code 的 overclaiming。phi 按 GT 分层显示 Unknown 相关性最低（0.098），意味着 FOL/Code 在 Unknown
475	    上最不相关——互补信号最强，这直接解释了为什么 repair delta 最大。 False agreement rate 12.3% 相对低（Denisov-Blanch
476	    2026 担忧的 correlated failure 不严重），且 GT=Unknown 子集仅 5.8% false agreement——再次证明 Unknown
477	    是 CRD 的 最佳应用场景。specification error 仅 8.3% 说明绝大多数错误是 formalization-specific 而非原始问题歧义导致，支撑
478	    CRD 的诊断靶点合理性。
479	
480	    '
481	  tables:
482	  - name: 'Table 10: Correlated Failure Analysis'
483	    columns:
484	    - GT Label
485	    - n
486	    - phi
487	    - False Agreement Rate
488	    - Code Overclaiming
489	    rows:
490	    - - 'True'
491	      - 72
492	      - 0.245
493	      - 19.4%
494	      - N/A
495	    - - 'False'
496	      - 63
497	      - 0.162
498	      - 11.1%
499	      - N/A
500	    - - Unknown
501	      - 69
502	      - 0.098
503	      - 5.8%
504	      - 78.3%
505	    - - Overall
506	      - 204
507	      - 0.189
508	      - 12.3%
509	      - —
510	  figures_description:
511	  - 'Fig 12: Code overclaiming 机制图——Unknown→True/False 的映射路径'
512	  - 'Fig 13: phi coefficient 按 GT label 分层 + false agreement rate 联合可视化'
513	  analysis: '此分析为 Claim 3 提供了因果机制：不是 repair 策略差异导致 GT-dependent 效应， 而是 Code 表征的结构性局限（缺乏三值逻辑）×
514	    GT label 的交互作用。这使得 GT=True overcorrection 也有了合理解释——当 GT=True 但 Code 错误输出 False/Unknown
515	    时， 诊断信号误导 repair 认为应该远离 True，导致 overcorrection。
516	
517	    '
518	- name: Selection vs Repair 消融
519	  plan_id: exp-007
520	  description: '分歧检测+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层报告。
521	
522	    '
523	  expected_results:
524	    blind_baseline_acc_GT_not_true: 61.4%
525	    selection_acc_GT_not_true: 72.7%
526	    repair_acc_GT_not_true: 76.2%
527	    selection_vs_blind_delta: +11.3pp
528	    repair_vs_selection_delta: +3.5pp
529	    selection_by_error_type:
530	      logic_error: 70.7%
531	      negation_error: 77.8%
532	      exec_crash: 90.9%
533	      quantifier_error: 50.0%
534	    repair_by_error_type:
535	      logic_error: 75.6%
536	      negation_error: 77.8%
537	      exec_crash: 90.9%
538	      quantifier_error: 75.0%
539	    repair_advantage_concentrated_on: logic_error (+4.9pp) 和 quantifier_error (+25pp)
540	  result_rationale: '在 best 档位下，selection 已经大幅优于 blind baseline（+11.3pp，远超 +5pp gate），
541	    证明 CRD 诊断+定位的基本价值。repair 在 selection 之上再加 +3.5pp（刚超 +3pp gate）， 增量价值集中在 logic_error
542	    和 quantifier_error——这两类错误需要修正 formalization 而非简单选边，selection 无法解决因为两侧都可能部分正确（如
543	    FOL 量词正确但谓词错误， Code 谓词正确但逻辑流错误）。negation_error 和 exec_crash 上 repair ≈ selection，
544	    因为这两类错误通常有明确的"一侧对一侧错"模式，选正确侧就足够了。 这个分层结果支撑了论文的 nuanced claim：repair 不是全面优于 selection，
545	    而是在特定错误类型上有不可替代的价值——正是 taxonomy 驱动修复的意义。 限制在 GT≠True 子集报告（n=132），因为 GT=True overcorrection
546	    对 selection 和 repair 都适用，不影响二者的相对对比。
547	
548	    '
549	  tables:
550	  - name: 'Table 11: Selection vs Repair on GT≠True Subset (n=132)'
551	    columns:
552	    - Method
553	    - Overall Acc
554	    - logic_error
555	    - negation_error
556	    - exec_crash
557	    - quantifier_error
558	    rows:
559	    - - Blind Baseline
560	      - 61.4%
561	      - 56.1%
562	      - 66.7%
563	      - 72.7%
564	      - 25.0%
565	    - - Selection
566	      - 72.7%
567	      - 70.7%
568	      - 77.8%
569	      - 90.9%
570	      - 50.0%
571	    - - Repair (Round 3)
572	      - 76.2%
573	      - 75.6%
574	      - 77.8%
575	      - 90.9%
576	      - 75.0%
577	  figures_description:
578	  - 'Fig 14: 三方法对比 grouped bar chart，按 error_type 分层'
579	  - 'Fig 15: Repair 增量价值热图（repair - selection delta 按 error type）'
580	  analysis: 'Selection vs repair 的分层结果是 exp-007 的核心贡献：证明 taxonomy 不仅是分析工具， 还有规定性价值（prescriptive
581	    value）——知道错误类型决定了应该 select 还是 repair。 这直接回应 R3 并为 exp-008 铺路。selection_vs_blind
582	    +11.3pp 是强结果， 证明即使不 repair，CRD 诊断+定位已经有实用价值。
583	
584	    '
585	- name: Error Taxonomy 消融
586	  plan_id: exp-008
587	  description: '按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。
588	
589	    '
590	  expected_results:
591	    taxonomy_guided_acc: 76.2%
592	    fixed_strategy_acc: 71.2%
593	    taxonomy_delta: +5.0pp
594	    taxonomy_advantage_by_type:
595	      logic_error: +6.2pp
596	      negation_error: +2.3pp
597	      exec_crash: +0.0pp
598	      quantifier_error: +18.0pp
599	    mcnemar_p: 0.042
600	  result_rationale: '在 best 档位下，taxonomy-guided 策略整体优于 fixed strategy +5.0pp（McNemar
601	    p=0.042， 显著）。增量主要来自 logic_error（最大类，+6.2pp——targeted prompt 包含"检查谓词定义 和推理链"vs
602	    盲目重生成）和 quantifier_error（最小类但增幅最大 +18.0pp——targeted prompt 显式提示"检查全称/存在量词的作用域"，盲目重生成几乎无法修复这类细微错误）。
603	    exec_crash 无差异因为重生成本身就是最优策略（崩溃了就重新生成）。negation_error 增量小因为否定翻转相对简单，固定策略也能偶然修复。McNemar
604	    p=0.042 刚好显著， 反映样本量有限但效应真实。
605	
606	    '
607	  tables:
608	  - name: 'Table 12: Taxonomy-Guided vs Fixed Strategy Repair'
609	    columns:
610	    - Error Type
611	    - n
612	    - Taxonomy-Guided
613	    - Fixed (regen)
614	    - Delta
615	    rows:
616	    - - logic_error
617	      - 41
618	      - 75.6%
619	      - 69.4%
620	      - +6.2pp
621	    - - negation_error
622	      - 18
623	      - 77.8%
624	      - 75.5%
625	      - +2.3pp
626	    - - exec_crash
627	      - 11
628	      - 90.9%
629	      - 90.9%
630	      - +0.0pp
631	    - - quantifier_error
632	      - 4
633	      - 75.0%
634	      - 57.0%
635	      - +18.0pp
636	    - - Overall
637	      - 74
638	      - 76.2%
639	      - 71.2%
640	      - +5.0pp (p=0.042)
641	  figures_description:
642	  - 'Fig 16: Taxonomy-guided vs fixed strategy 按 error type 对比'
643	  analysis: 'Taxonomy ablation 证明 error classification 不只是 analysis contribution——
644	    它有 prescriptive value。这将 Claim 2 从纯分析升级为方法贡献， 增加论文的实用性维度。quantifier_error 的 +18pp
645	    虽然 n 太小（4 samples）不能 单独做统计检验，但方向明确。
646	
647	    '
648	- name: 统计显著性全面检验
649	  plan_id: exp-009
650	  description: '对所有 benchmark 的 C1-C5 指标做 Bootstrap 95% CI + Fisher exact / McNemar
651	    test。
652	
653	    '
654	  expected_results:
655	    FOLIO_C2_CI: '[81.3%, 94.7%]'
656	    LogiQA_C2_CI: '[73.8%, 88.2%]'
657	    MATH_C2_CI: '[66.1%, 85.2%]'
658	    cross_benchmark_C2_min_lower: 66.1%
659	    FOLIO_C4_unknown_fisher_p: 0.038
660	    FOLIO_C4_true_fisher_p: 0.021
661	    LogiQA_C4_positive_subset_fisher_p: 0.045
662	    CRD_vs_SC5_mcnemar_p: 0.031
663	    all_primary_claims_significant: true
664	    aggregate_C4_significant: false
665	  result_rationale: '在 best 档位下，所有主要 claim 的分层指标都达到统计显著：FOLIO GT=Unknown C4 delta
666	    Fisher p=0.038（n=69，+14.7pp→+22.1pp 多轮后更强），GT=True overcorrection p=0.021（负方向也显著，strengthens
667	    boundary characterization）。LogiQA 的正子集 p=0.045 复现效应。CRD vs SC5 McNemar p=0.031
668	    证明诊断精度差异显著。 关键：aggregate C4 仍然不显著——这在 best 档位下是 feature not bug， 因为分层报告是我们的 methodological
669	    contribution。CI 紧致度随样本量提高 （FOLIO n=204 > LogiQA n=200 > MATH n=200），MATH C2 下界
670	    66.1% 最低 但 point estimate 76% 仍超 70% gate。
671	
672	    '
673	  tables:
674	  - name: 'Table 13: Statistical Significance Summary Across Benchmarks'
675	    columns:
676	    - Test
677	    - Benchmark
678	    - Metric
679	    - Statistic
680	    - p-value
681	    - Significant?
682	    rows:
683	    - - Fisher
684	      - FOLIO
685	      - C4 GT=Unknown
686	      - +22.1pp
687	      - '0.038'
688	      - 'Yes'
689	    - - Fisher
690	      - FOLIO
691	      - C4 GT=True
692	      - -11.2pp
693	      - '0.021'
694	      - 'Yes'
695	    - - Fisher
696	      - LogiQA
697	      - C4 positive subset
698	      - +11.3pp
699	      - '0.045'
700	      - 'Yes'
701	    - - McNemar
702	      - FOLIO
703	      - CRD vs SC5 precision
704	      - +7.2pp
705	      - '0.031'
706	      - 'Yes'
707	    - - Fisher
708	      - FOLIO
709	      - C4 aggregate
710	      - +4.65pp
711	      - '0.626'
712	      - 'No'
713	    - - Bootstrap
714	      - All
715	      - C2 range
716	      - '[66.1%, 94.7%]'
717	      - —
718	      - —
719	  figures_description:
720	  - 'Fig 17: 跨基准 C2 Bootstrap CI 的 forest plot'
721	  analysis: '统计检验结果在 best 档位下完美支撑叙事：分层指标显著而 aggregate 不显著， 证明分层分析的必要性。Forest plot
722	    显示三基准 C2 CI 重叠但中心递减 （FOLIO > LogiQA > MATH），反映任务复杂度梯度。
723	
724	    '
725	- name: Self-Consistency Baseline 对比
726	  plan_id: exp-012
727	  description: 'FOLIO + LogiQA + MATH 上对比 k=5 FOL-only majority vote, k=5 Code-only
728	    majority vote, vs single-pass CRD。隔离 cross-representation 信号 vs 单表征 sampling diversity。
729	
730	    '
731	  expected_results:
732	    FOLIO:
733	      SC5_FOL_precision: 79.3%
734	      SC5_Code_precision: 72.1%
735	      CRD_precision: 87.2%
736	      CRD_vs_SC5_FOL_delta: +7.9pp
737	      SC5_FOL_cost_tokens: 5x baseline
738	      SC5_Code_cost_tokens: 5x baseline
739	      CRD_cost_tokens: 2x baseline
740	      CRD_vs_SC5_cost_ratio: '0.40'
741	    LogiQA:
742	      SC5_FOL_precision: 75.8%
743	      SC5_Code_precision: 69.4%
744	      CRD_precision: 81.5%
745	      CRD_vs_SC5_FOL_delta: +5.7pp
746	    MATH:
747	      SC5_SymPy_precision: 71.2%
748	      SC5_Python_precision: 74.8%
749	      CRD_precision: 76.0%
750	      CRD_vs_SC5_best_delta: +1.2pp
751	    overall_CRD_vs_SC5_precision_delta: +4.9pp (avg across benchmarks)
752	    overall_CRD_vs_SC5_cost_ratio: 0.4
753	  result_rationale: '在 best 档位下，CRD 在所有三个基准上诊断精度均优于 k=5 单表征 majority vote， 且 token
754	    成本仅为 40%（2 次生成 vs 5 次生成）。机制：k=5 同表征 sampling 捕获的是 generation variance（同一 prompt
755	    的随机性），而 CRD 捕获的是 paradigm-level difference （形式逻辑 vs 命令式代码的系统性差异）。前者在高温度下有效但容易被
756	    mode collapse 削弱 （LLM 倾向于收敛到同一错误模式），后者因为表征范式根本不同而产生更互补的错误信号。 FOLIO delta 最大（+7.9pp）因为
757	    FOL 和 Python 的范式差异最大；MATH delta 最小（+1.2pp） 因为 SymPy 和 Python numerical 都是 Python
758	    生态，范式差异较小。MATH 上 SC5_Python 甚至略优于 SC5_SymPy（74.8% vs 71.2%），与 exp-004 的不对称反转一致。
759	    CRD cost ratio 0.40 落在 [0.30, 0.45] range——2 次生成 vs 5 次生成 = 0.40， 考虑 CRD 额外的 diagnosis
760	    prompt 开销后正好 40%。
761	
762	    '
763	  tables:
764	  - name: 'Table 14: CRD vs Self-Consistency (k=5) Across Benchmarks'
765	    columns:
766	    - Benchmark
767	    - SC5-FOL Prec
768	    - SC5-Code Prec
769	    - CRD Prec
770	    - CRD-SC5 Δ
771	    - Cost Ratio
772	    rows:
773	    - - FOLIO
774	      - 79.3%
775	      - 72.1%
776	      - 87.2%
777	      - +7.9pp
778	      - '0.40'
779	    - - LogiQA
780	      - 75.8%
781	      - 69.4%
782	      - 81.5%
783	      - +5.7pp
784	      - '0.40'
785	    - - MATH
786	      - 71.2%
787	      - 74.8%
788	      - 76.0%
789	      - +1.2pp
790	      - '0.40'
791	    - - Average
792	      - 75.4%
793	      - 72.1%
794	      - 81.6%
795	      - +4.9pp
796	      - '0.40'
797	  figures_description:
798	  - 'Fig 18: CRD vs SC5 precision-cost Pareto 图——CRD 在 Pareto front 上'
799	  - 'Fig 19: 按基准的 CRD vs SC5 对比 grouped bar chart'
800	  analysis: 'exp-012 是回应 R8 的核心实验。best 档位下 CRD Pareto-dominates SC5（更高精度+更低成本）， headline
801	    变为"用 40% 的 token 成本获得平均 +4.9pp 的诊断精度提升"。 MATH 上 delta 仅 +1.2pp 是可接受的——因为 SymPy/Python
802	    范式差异较小， 但仍为正且 cost advantage 不变。论文可以讨论 "paradigm distance" 作为 CRD 效果的调节变量——范式差异越大，CRD
803	    相对于 SC5 的优势越大。
804	
805	    '
806	- name: Error Taxonomy 交叉验证
807	  plan_id: exp-013
808	  description: 'DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比， 计算 Cohen''s κ。验证
809	    taxonomy 跨模型稳定性。
810	
811	    '
812	  expected_results:
813	    n_classified: 75
814	    cohens_kappa: 0.67
815	    kappa_CI: '[0.54, 0.80]'
816	    agreement_by_type:
817	      logic_error: 78.8%
818	      negation_error: 72.7%
819	      exec_crash: 90.9%
820	      quantifier_error: 50.0%
821	    deepseek_type_distribution:
822	      logic_error: 28.0%
823	      negation_error: 12.0%
824	      exec_crash: 6.7%
825	      quantifier_error: 1.3%
826	      unclassified: 4.0%
827	    distribution_stability: rank order preserved (logic > negation > crash > quantifier)
828	  result_rationale: '在 best 档位下，Cohen''s κ=0.67 落在 [0.60, 0.80] range，达到 "substantial
829	    agreement" 标准。κ 不更高的原因合理：两个模型对 logic_error vs negation_error 的边界划分有 模糊区域（一些否定相关的逻辑错误可以归入任一类别），这是分类本身的固有模糊性而非
830	    taxonomy 设计缺陷。exec_crash 一致性最高（90.9%）因为执行崩溃是客观可验证的。 quantifier_error 一致性最低（50%）因为
831	    n 太小（仅 4 样本）且量词错误判断需要 深层语义理解。关键发现：两个模型的错误类型分布 rank order 完全一致 （logic > negation
832	    > crash > quantifier），说明 taxonomy 反映的是错误结构而非 模型偏好。DeepSeek 的 logic_error 比例略高（28%
833	    vs 25.5%）、unclassified 略低 （4% vs 0%），因为 DeepSeek 更倾向给出明确分类而非其他 catch-all。
834	
835	    '
836	  tables:
837	  - name: 'Table 15: Cross-Model Taxonomy Validation (n=75 diagnostic samples)'
838	    columns:
839	    - Error Type
840	    - Qwen3-32B %
841	    - DeepSeek %
842	    - Pairwise Agreement
843	    - κ contribution
844	    rows:
845	    - - logic_error
846	      - 25.5%
847	      - 28.0%
848	      - 78.8%
849	      - '0.71'
850	    - - negation_error
851	      - 10.8%
852	      - 12.0%
853	      - 72.7%
854	      - '0.62'
855	    - - exec_crash
856	      - 5.4%
857	      - 6.7%
858	      - 90.9%
859	      - '0.88'
860	    - - quantifier_error
861	      - 2.0%
862	      - 1.3%
863	      - 50.0%
864	      - '0.45'
865	    - - Overall κ
866	      - —
867	      - —
868	      - —
869	      - '0.67'
870	  figures_description:
871	  - 'Fig 20: 4×4 confusion matrix heatmap (Qwen classification vs DeepSeek classification)'
872	  - 'Fig 21: 两个模型的错误类型分布 side-by-side bar chart'
873	  analysis: 'κ=0.67 回应 R9 的 taxonomy validation 要求。substantial agreement 证明 taxonomy
874	    不是单模型的 artifact——不同 LLM 从同一组分歧样本中识别出一致的错误模式。 rank order 稳定性是更强的信号：即使个别样本分类不同，宏观分布结构跨模型复现，
875	    说明四类错误反映了 formalization 的真实失败模式。
876	
877	    '
878	- name: Qwen3-8B 消融
879	  plan_id: exp-010
880	  description: '低能力模型上的诊断率和分歧率变化。P2 优先级。
881	
882	    '
883	  expected_results:
884	    n: 204
885	    C1_disagree_rate: 55.4%
886	    C2_diagnostic_rate: 74.5%
887	    asymmetry: 2.8:1 (FOL-favored, compressed)
888	    fol_accuracy: 58.3%
889	    code_accuracy: 47.1%
890	    C4_aggregate: +2.1pp
891	  result_rationale: '在 best 档位下，8B 模型 C1 上升到 55.4%（更弱模型→更多 formalization 错误→更多分歧），
892	    但 C2 降至 74.5%（更多分歧来自"两侧都错"的 correlated failure，诊断性下降）。 这个 C1↑C2↓ 的 tradeoff 是
893	    model-capability 对 CRD 有效性的重要 characterization： 存在一个能力下限，低于此 CRD 的诊断价值被 correlated
894	    failure 侵蚀。 不对称比压缩到 2.8:1 因为 8B 的 FOL 能力下降更快（形式逻辑对模型能力更敏感）。 作为 P2 实验，这提供了有价值的
895	    scaling 分析但不影响核心 claim。
896	
897	    '
898	  tables:
899	  - name: 'Table 16: Model Scale Ablation on FOLIO'
900	    columns:
901	    - Model
902	    - C1
903	    - C2
904	    - Asymmetry
905	    - FOL Acc
906	    - Code Acc
907	    rows:
908	    - - Qwen3-32B
909	      - 42.2%
910	      - 87.2%
911	      - 5.6:1
912	      - 78.4%
913	      - 59.8%
914	    - - Qwen3-8B
915	      - 55.4%
916	      - 74.5%
917	      - 2.8:1
918	      - 58.3%
919	      - 47.1%
920	    - - DeepSeek V4 Pro
921	      - 38.7%
922	      - 83.5%
923	      - 4.2:1
924	      - 81.2%
925	      - 64.7%
926	  figures_description:
927	  - 'Fig 22: Model capability vs C1/C2 scatter plot (三模型)'
928	  analysis: '三个模型形成 capability 梯度（8B < 32B < DeepSeek Pro），C2 单调递增， C1 单调递减——完美的 scaling
929	    story。论文 1 段 discussion 即可，不需要更多。
930	
931	    '
932	- name: GPQA Diamond 扩展
933	  plan_id: exp-011
934	  description: '科学知识推理，SymPy/Python 双可执行表征。P2 优先级。
935	
936	    '
937	  expected_results:
938	    n: 150
939	    C1_disagree_rate: 22.0%
940	    C2_diagnostic_rate: 72.7%
941	    asymmetry: 1.4:1 (slight Python-favored)
942	    note: C2 略低于 70% gate——科学推理中 domain knowledge 错误占比高，CRD 对 knowledge gap 诊断力有限
943	  result_rationale: '在 best 档位下，GPQA C1=22% 较低（科学推理需要 domain knowledge 而非纯 formalization，
944	    两条路径的差异更多来自知识错误而非表征差异），C2=72.7% 在 70% gate 边缘。 这是 CRD 适用边界的有价值 characterization：cross-representation
945	    disagreement 对 formalization errors 诊断力强，对 domain knowledge errors 诊断力弱。 作为 P2
946	    可选实验，如果时间不够可以省略，核心三基准已足够。
947	
948	    '
949	  tables:
950	  - name: 'Table 17: Cross-Domain CRD Effectiveness'
951	    columns:
952	    - Domain
953	    - Benchmark
954	    - C1
955	    - C2
956	    - Primary Error Source
957	    rows:
958	    - - Logic
959	      - FOLIO
960	      - 42.2%
961	      - 87.2%
962	      - Formalization
963	    - - Logic
964	      - LogiQA
965	      - 34.0%
966	      - 81.5%
967	      - Formalization
968	    - - Math
969	      - MATH L5
970	      - 28.5%
971	      - 76.0%
972	      - Computation
973	    - - Science
974	      - GPQA
975	      - 22.0%
976	      - 72.7%
977	      - Knowledge gap
978	  figures_description:
979	  - 'Fig 23: Domain × C2 effectiveness 趋势图——formalization-heavy 域 CRD 最有效'
980	  analysis: 四基准形成清晰的域梯度：纯逻辑 > 数学 > 科学，C2 随 formalization 占比下降。 这是 best 档位的 bonus result——不是每个域都好用恰恰证明我们理解了
981	    CRD 的机制和边界。 但 GPQA 作为 P2 实验，若时间不足可省略，不影响核心结论。
982	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "896b04bc-305e-474f-bb22-f305a01e1c41",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "883033be-fc4b-4c50-8aed-d18abf000306",
  "sourceToolAssistantUUID": "896b04bc-305e-474f-bb22-f305a01e1c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T07:50:26.185Z_

<details open><summary>🔧 Tool call — Read · `toolu_016ez4yP9KaAiDnSpPinWqb8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "883033be-fc4b-4c50-8aed-d18abf000306",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zKCCqDqZHr4NQRyP7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c8ffa4f-ea5e-4ff8-8bcb-797ade0a4bf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJPxNoyuNtTwmuroRYMUaE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3377,
      "cache_read_input_tokens": 39561,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 39561,
          "cache_creation_input_tokens": 3377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3377,
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

_source line 34 · 2026-05-15T07:50:26.190Z_

<details><summary>↩ Tool result · `toolu_016ez4yP9KaAiDnSpPinWqb8`</summary>

```text
1	# Paper Framing — cross_representation_disagreement_diagno
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026 (10 days)
7	- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage
8	
9	## Core Insight
10	Cross-representation disagreement (FOL/Z3 vs Python Code) produced by the same LLM for the same reasoning problem is an underexploited diagnostic signal that detects formalization errors, enables error localization and classification, and guides targeted repair — going beyond existing approaches that only filter or verify within a single representation.
11	
12	## Core Claims (3 条)
13	
14	### Claim 1: Disagreement as High-Precision Diagnostic Signal
15	When the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.
16	
17	**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).
18	
19	### Claim 2: Accurate Error Localization and Classification
20	Disagreement patterns enable automatic error localization (identifying which representation contains the error) with high accuracy (~85%), and error type classification into a structured taxonomy (≥3 distinct types). The 9:1 asymmetry (FOL almost always correct, Code almost always erroneous) itself reveals fundamental differences in how LLMs handle formal logic vs. imperative code generation.
21	
22	**MVP evidence**: C5=85.4% localization accuracy, C3=3 error types. FOL:Code error ratio 9:1.
23	
24	### Claim 3: Characterizing the Boundary of Diagnosis-Guided Repair
25	We systematically characterize when cross-representation diagnosis enables effective targeted repair vs. when correlated failures limit repair gains. Targeted repair shows modest improvement over blind regeneration in All-mode (+5.2pp), but the advantage concentrates on specific sample subsets (GT=Unknown). This boundary characterization — distinguishing formalization-specific errors (catchable) from specification-level errors (producing false agreement) — is itself a contribution to understanding neurosymbolic failure modes.
26	
27	**MVP evidence**: C4 All-mode +5.2pp, Excl-Unknown +0.0pp. Unknown samples drive the repair delta.
28	
29	## Story Spine
30	
31	- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.
32	
33	- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.
34	
35	- **Our framing (dual-track)**: We present (1) the first systematic empirical analysis of cross-representation disagreement patterns in neurosymbolic reasoning — characterizing disagreement rates, error types, localization accuracy, and failure mode boundaries across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility.
36	
37	- **Headline result template**: "On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation."
38	
39	## Venue Fit
40	
41	- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.
42	- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.
43	- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.
44	
45	## Anticipated Reviewer Concerns & Responses
46	
47	| # | Concern | Response Strategy | Required Experiment |
48	|---|---------|-------------------|---------------------|
49	| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |
50	| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |
51	| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |
52	| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |
53	| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |
54	| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |
55	| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c8ffa4f-ea5e-4ff8-8bcb-797ade0a4bf6",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "210c472b-bd87-422c-b2f6-882c134c9fe2",
  "sourceToolAssistantUUID": "4c8ffa4f-ea5e-4ff8-8bcb-797ade0a4bf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-15T07:50:31.347Z_

Now I have thoroughly reviewed the paper, its framing documents, and a prior R2 review from the earlier dream report. Let me also check if there are any other relevant review context files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "210c472b-bd87-422c-b2f6-882c134c9fe2",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zKXyxgN6pnAKc9DvWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "854cdac0-4000-404a-922b-d966c988f6a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TxV924JieXYiwbN5sgXdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19044,
      "cache_read_input_tokens": 42938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19044,
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

_source line 36 · 2026-05-15T07:50:33.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TCZSyhbJT7F1mM1KJ8i8XS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "854cdac0-4000-404a-922b-d966c988f6a7",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zKXyxgN6pnAKc9DvWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa3df727-6faf-4d01-b3c5-02997254629f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TxV924JieXYiwbN5sgXdf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19044,
      "cache_read_input_tokens": 42938,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 42938,
          "cache_creation_input_tokens": 19044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19044,
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

_source line 37 · 2026-05-15T07:50:33.810Z_

<details><summary>↩ Tool result · `toolu_01TCZSyhbJT7F1mM1KJ8i8XS`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation
2	  self-consistency 更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定，
3	  C3 的 GT-label-dependent 效应在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。 Selection
4	  ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered boundary
5	  是加分项而非弱点。
6	
7	  '
8	imagined_experiments:
9	- name: FOLIO 完整分析（MVP 数据深度挖掘）
10	  plan_id: exp-001
11	  description: '基于 204 样本 MVP 数据的统计检验、错误分类、子集分层分析、不对称性 breakdown、 失败相关性定量分析和 cost-effectiveness
12	    分析。纯分析，无新实验运行。
13	
14	    '
15	  expected_results:
16	    C1_disagree_rate: 42.16% [35.3%, 49.0%]
17	    C2_diagnostic_rate: 87.21% [81.3%, 94.7%]
18	    C3_error_types: 4
19	    C4_targeted_delta_aggregate: +4.65pp (Fisher p=0.626, n.s.)
20	    C4_GT_True: -13.6pp
21	    C4_GT_False: +11.6pp
22	    C4_GT_Unknown: +14.7pp
23	    C5_committed_accuracy: 94.6% (35/37)
24	    C5_coverage: 53.0% (35/66)
25	    asymmetry_ratio: 5.6:1 (FOL=56, Code=10, Both=10)
26	    phi_coefficient: 0.189
27	    phi_p_value: 0.007
28	    complementary_error_rate: 75% (75/100)
29	    cost_multiplier_vs_code_only: 5.76x tokens
30	    accuracy_gain_over_code_only: +21.6pp
31	    dominant_error: logic_error 25.5%
32	  result_rationale: '这是已有 MVP 数据的深度挖掘，数值已固定。在 best 档位下，关键价值在于：(1) Bootstrap CI 对 C1/C2
33	    给出了紧致的区间，C2 下界 81.3% 远超 75% 阈值，为高精度诊断信号提供统计支撑； (2) phi=0.189 (p=0.007) 表明 FOL/Code
34	    失败相关性低但统计显著——恰好落在"足够独立以产生互补信号， 又不完全独立"的理想区间；(3) 75% 单侧失败率直接支撑 cross-representation
35	    的互补性叙事； (4) GT-stratified C4 揭示三路分裂是 Claim 3 的核心发现，aggregate 非显著反而强化了 "必须分层报告"的方法论贡献。cost_multiplier
36	    5.76x 看似高，但对比 k=5 self-consistency 的 5x 成本，CRD 以相近成本获得更丰富的诊断信息（错误类型 + 定位），而非仅
37	    majority vote。
38	
39	    '
40	  tables:
41	  - name: 'Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI'
42	    columns:
43	    - Metric
44	    - Point Estimate
45	    - 95% CI
46	    - MVP Gate
47	    rows:
48	    - - C1 (Disagree Rate)
49	      - 42.16%
50	      - '[35.3%, 49.0%]'
51	      - PASS (≥15%)
52	    - - C2 (Diagnostic Rate)
53	      - 87.21%
54	      - '[81.3%, 94.7%]'
55	      - PASS (≥75%)
56	    - - C3 (Error Types)
57	      - 4 types
58	      - —
59	      - PASS (≥3)
60	    - - C4 (Repair Delta)
61	      - +4.65pp
62	      - '[-8.8%, +18.1%]'
63	      - FAIL (CI includes 0)
64	    - - C5 (Localization)
65	      - 53.0%
66	      - '[41.0%, 65.1%]'
67	      - FAIL (<70%)
68	  - name: 'Table 2: GT-Label-Stratified Repair Effect'
69	    columns:
70	    - GT Label
71	    - n
72	    - Targeted Acc
73	    - Blind Acc
74	    - Delta
75	    - Interpretation
76	    rows:
77	    - - 'True'
78	      - 72
79	      - 63.6%
80	      - 77.3%
81	      - -13.6pp
82	      - Overcorrection
83	    - - 'False'
84	      - 63
85	      - 76.7%
86	      - 70.0%
87	      - +6.7pp
88	      - Modest help
89	    - - Unknown
90	      - 69
91	      - 67.7%
92	      - 52.9%
93	      - +14.7pp
94	      - Diagnosis helps
95	  - name: 'Table 3: Error Taxonomy Distribution'
96	    columns:
97	    - Error Type
98	    - Count
99	    - Proportion
100	    rows:
101	    - - logic_error
102	      - 52
103	      - 25.5%
104	    - - negation_error
105	      - 22
106	      - 10.8%
107	    - - exec_crash
108	      - 11
109	      - 5.4%
110	    - - quantifier_error
111	      - 4
112	      - 2.0%
113	  figures_description:
114	  - 'Fig 1: Confusion matrix heatmap — FOL correct/wrong × Code correct/wrong，标注 5.6:1
115	    不对称'
116	  - 'Fig 2: GT-stratified repair delta bar chart，三色柱状图显示三路分裂效应'
117	  - 'Fig 3: phi coefficient 按 GT label 分层的热图'
118	  analysis: 'exp-001 作为 anchor 实验，所有数值已确定。best 档位下的分析重点是将 C4 aggregate 非显著 和 C5 低覆盖率重新
119	    frame 为方法论发现而非失败：(1) aggregate 非显著正是因为 GT-label-dependent 效应相互抵消，分层报告是正确的分析粒度；(2)
120	    C5 coverage 53% 但 committed accuracy 94.6% 是高精度/低召回的 deliberate tradeoff，ambiguous
121	    标签中 61% 来自 GT=Unknown 驱动—— 这些样本恰好是 repair delta 最大的子集，说明即使定位不确定，disagreement pattern
122	    本身 就有修复价值。
123	
124	    '
125	- name: 跨模型消融（FOLIO）
126	  plan_id: exp-002
127	  description: '三组条件：(a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro
128	    within-model, (c) DeepSeek FOL + Qwen Code cross-model。区分分歧来源。
129	
130	    '
131	  expected_results:
132	    deepseek_within_C1: 38.7%
133	    deepseek_within_C2: 83.5%
134	    deepseek_within_C2_CI: '[74.2%, 91.8%]'
135	    deepseek_within_asymmetry: 4.2:1 (FOL-favored)
136	    deepseek_within_C4_GT_Unknown: +12.1pp
137	    deepseek_within_C4_GT_True: -10.3pp
138	    deepseek_within_C4_GT_False: +8.4pp
139	    cross_model_C1: 47.5%
140	    cross_model_C2: 80.9%
141	    cross_model_asymmetry: 3.8:1 (FOL-favored)
142	    C2_delta_vs_MVP: -3.7pp (within ±8pp gate)
143	    asymmetry_direction: consistent (FOL-favored in all 3 conditions)
144	  result_rationale: '在 best 档位下，DeepSeek within-model C2 落在 MVP ±8pp 内（83.5% vs 87.2%，delta=-3.7pp），
145	    证明诊断精度不是 Qwen3-32B 的特异性质，而是 cross-representation disagreement 的结构性属性。 DeepSeek
146	    C1 略低（38.7% vs 42.2%）合理——DeepSeek 作为更强模型，两条表征路径各自精度更高， 分歧率自然略低，但 C2 保持在 80%+ 说明分歧样本仍然高度诊断性。不对称方向一致（FOL-favored）
147	    是关键：这不是模型偶然，而是 FOL+Z3 的形式验证保证系统性地比 Python 执行更可靠。 Cross-model 条件 C1 更高（47.5%）因为两个不同模型的
148	    formalization bias 不同， 增加了分歧概率，但 C2 略降（80.9%）因为部分分歧来自模型差异而非 formalization 错误。
149	    这个分离正好支撑论文的核心论点：within-model cross-representation disagreement 更纯粹地反映 formalization
150	    错误，cross-model 混入了 capability 噪声。
151	
152	    '
153	  tables:
154	  - name: 'Table 4: Cross-Model Ablation Results on FOLIO (n=204)'
155	    columns:
156	    - Condition
157	    - C1
158	    - C2
159	    - C2 95% CI
160	    - Asymmetry
161	    - C4 (Unknown)
162	    - C4 (True)
163	    rows:
164	    - - Qwen3-32B within (MVP)
165	      - 42.2%
166	      - 87.2%
167	      - '[81.3%, 94.7%]'
168	      - 5.6:1 FOL
169	      - +14.7pp
170	      - -13.6pp
171	    - - DeepSeek within
172	      - 38.7%
173	      - 83.5%
174	      - '[74.2%, 91.8%]'
175	      - 4.2:1 FOL
176	      - +12.1pp
177	      - -10.3pp
178	    - - DeepSeek×Qwen cross
179	      - 47.5%
180	      - 80.9%
181	      - '[71.8%, 89.1%]'
182	      - 3.8:1 FOL
183	      - +9.8pp
184	      - -8.7pp
185	  figures_description:
186	  - 'Fig 4: 三条件 C1/C2 对比柱状图，带 error bars'
187	  - 'Fig 5: 不对称比例的 stacked bar，三条件均 FOL-favored'
188	  analysis: '三组数据形成清晰的叙事梯度：within-model(同模型) > cross-model(跨模型) 在 C2 上， 说明 within-model
189	    的诊断信号更纯净。DeepSeek GT-stratified 效应方向完全一致 （Unknown 正, True 负, False 正），证明 Claim
190	    3 的 GT-label-dependent 效应 是表征结构属性而非模型特异。C2 delta -3.7pp 在 ±8pp gate 内——这是 best
191	    档的 sweet spot，既证明泛化，又不大到暗示 MVP 是 outlier。
192	
193	    '
194	- name: ProofWriter / LogiQA 扩展
195	  plan_id: exp-003
196	  description: '第二逻辑推理基准。先 pilot 20-30 样本验证 disagree_rate ≥ 10%， 通过则全量跑 ProofWriter；失败则切换
197	    LogiQA。
198	
199	    '
200	  expected_results:
201	    dataset_used: LogiQA
202	    pilot_proofwriter_disagree_rate: 6.7% (2/30) — pilot FAIL
203	    pilot_switch_reason: ProofWriter 合成数据过于规则，FOL/Code 均高精度 (>93%)，分歧率不足
204	    logiqA_n: 200
205	    logiqA_C1: 34.0%
206	    logiqA_C2: 81.5%
207	    logiqA_C2_CI: '[73.8%, 88.2%]'
208	    logiqA_C3_error_types: 4
209	    logiqA_asymmetry: 3.2:1 (FOL-favored)
210	    logiqA_C4_GT_stratified_positive_subset: +11.3pp
211	    logiqA_C4_GT_stratified_negative_subset: -9.8pp
212	    logiqA_C5_committed: 91.2%
213	    logiqA_C5_coverage: 48.5%
214	  result_rationale: '在 best 档位下，ProofWriter pilot 失败是预期且合理的——合成数据的逻辑结构简单规则， 两条表征路径都能高精度处理，分歧率仅
215	    6.7%。这不是坏消息：切换到 LogiQA（自然语言逻辑， 4 选 1）反而更好，因为 NL 歧义性更高，更能展示 CRD 在真实场景中的价值。LogiQA
216	    C1=34% 略低于 FOLIO（42%）合理——选择题格式约束了输出空间，减少了 formalization 分歧；但 C2=81.5% 仍然高（≥75%
217	    gate），证明分歧样本跨基准稳定诊断。不对称比仍 FOL-favored（3.2:1）但比 FOLIO 的 5.6:1 低——LogiQA 的命题逻辑复杂度低于
218	    FOLIO 的一阶逻辑，FOL 路径的优势 相对缩小。GT-stratified 效应方向复现（正/负分裂），证明 Claim 3 跨基准泛化。 C5 committed
219	    91.2% 保持在 90%+ 高精度区间。
220	
221	    '
222	  tables:
223	  - name: 'Table 5: LogiQA Results (n=200, Qwen3-32B)'
224	    columns:
225	    - Metric
226	    - LogiQA
227	    - FOLIO (ref)
228	    - Delta
229	    rows:
230	    - - C1 (Disagree Rate)
231	      - 34.0%
232	      - 42.2%
233	      - -8.2pp
234	    - - C2 (Diagnostic Rate)
235	      - 81.5%
236	      - 87.2%
237	      - -5.7pp
238	    - - C3 (Error Types)
239	      - '4'
240	      - '4'
241	      - —
242	    - - C5 Committed Acc
243	      - 91.2%
244	      - 94.6%
245	      - -3.4pp
246	    - - Asymmetry (FOL:Code)
247	      - 3.2:1
248	      - 5.6:1
249	      - narrower
250	  - name: 'Table 5b: ProofWriter Pilot Results (n=30)'
251	    columns:
252	    - Metric
253	    - Value
254	    - Gate
255	    - Decision
256	    rows:
257	    - - Disagree Rate
258	      - 6.7%
259	      - ≥10%
260	      - FAIL → switch to LogiQA
261	    - - FOL Accuracy
262	      - 93.3%
263	      - —
264	      - —
265	    - - Code Accuracy
266	      - 90.0%
267	      - —
268	      - —
269	  figures_description:
270	  - 'Fig 6: FOLIO vs LogiQA C1/C2 并排对比，带 CI error bars'
271	  - 'Fig 7: LogiQA GT-stratified repair delta 复现 FOLIO 三路分裂模式'
272	  analysis: 'LogiQA 作为第二基准完美补充 FOLIO：不同数据源（中国公务员考试 vs 专家标注 FOL）， 不同任务格式（4 选 1 vs 3
273	    分类），C2 仍在 [75%, 92%] range 内。ProofWriter pilot 失败在论文中可以作为 1 段讨论："合成数据过于规则，分歧信号需要自然语言的
274	    formalization 挑战"——这反而强化了 CRD 适用场景的 characterization。
275	
276	    '
277	- name: MATH Level 5 双可执行表征扩展
278	  plan_id: exp-004
279	  description: 'MATH Level 5 使用 SymPy 符号推理 vs Python 数值计算两条可执行路径， 保持 cross-executable-representation
280	    框架一致性。
281	
282	    '
283	  expected_results:
284	    n: 200
285	    math_C1: 28.5%
286	    math_C2: 76.0%
287	    math_C2_CI: '[66.1%, 85.2%]'
288	    math_C3_error_types: 3
289	    math_asymmetry: 1.8:1 (Code-favored)
290	    math_asymmetry_direction: 反转——Python 数值计算在 MATH 上优于 SymPy 符号推理
291	    math_C4_GT_correct_delta: +3.2pp
292	    math_C4_GT_wrong_delta: +7.8pp
293	    math_C5_committed: 88.5%
294	    math_C5_coverage: 55.0%
295	    sympy_crash_rate: 12.5%
296	    python_crash_rate: 4.0%
297	  result_rationale: '在 best 档位下，MATH C1=28.5% 满足 ≥15% gate。C1 低于 FOLIO（42%）合理—— 数学问题有唯一正确答案，两条计算路径比逻辑推理的
298	    formalization 更容易达成一致。 C2=76% 刚好在 [70%, 85%] 范围内——数学分歧中更多是计算错误而非 formalization
299	    错误， 部分分歧来自数值精度问题（如浮点近似 vs 精确符号解），诊断性略低但仍超 70% gate。 关键发现：不对称方向反转（Code-favored
300	    1.8:1），与 FOLIO 的 FOL-favored 5.6:1 相反。 这是 best 档的 killer result——证明不对称性不是 FOL
301	    固有优势，而是表征-任务匹配： 在逻辑推理上 FOL+Z3 有形式验证优势，在数学计算上 Python 的灵活数值方法更鲁棒。 SymPy crash rate
302	    12.5% > Python 4% 因为 SymPy 对输入格式敏感（符号化简失败、 方程无解析解等），而 Python 数值方法更容错。这个反转直接回应
303	    R5（"不只是 FOL-as-verifier"）。
304	
305	    '
306	  tables:
307	  - name: 'Table 6: MATH Level 5 Results (n=200, Qwen3-32B)'
308	    columns:
309	    - Metric
310	    - MATH
311	    - FOLIO (ref)
312	    - LogiQA (ref)
313	    rows:
314	    - - C1 (Disagree Rate)
315	      - 28.5%
316	      - 42.2%
317	      - 34.0%
318	    - - C2 (Diagnostic Rate)
319	      - 76.0%
320	      - 87.2%
321	      - 81.5%
322	    - - C3 (Error Types)
323	      - '3'
324	      - '4'
325	      - '4'
326	    - - Asymmetry
327	      - 1.8:1 Code-fav
328	      - 5.6:1 FOL-fav
329	      - 3.2:1 FOL-fav
330	    - - C5 Committed
331	      - 88.5%
332	      - 94.6%
333	      - 91.2%
334	  - name: 'Table 7: Asymmetry Direction Across Domains'
335	    columns:
336	    - Domain
337	    - Representation A
338	    - Representation B
339	    - Favored
340	    - Ratio
341	    rows:
342	    - - Logic (FOLIO)
343	      - FOL+Z3
344	      - Python exec
345	      - FOL
346	      - 5.6:1
347	    - - Logic (LogiQA)
348	      - FOL+Z3
349	      - Python exec
350	      - FOL
351	      - 3.2:1
352	    - - Math (MATH)
353	      - SymPy symbolic
354	      - Python numerical
355	      - Python
356	      - 1.8:1
357	  figures_description:
358	  - 'Fig 8: 三基准 asymmetry direction 可视化——逻辑 vs 数学域的反转'
359	  - 'Fig 9: MATH 错误类型分布（computation_error, symbolic_failure, exec_crash）'
360	  analysis: 'MATH 的不对称反转是 best 档位的标志性结果。它将 paper 的 story 从 "FOL is better" 升级为 "cross-representation
361	    disagreement reveals domain-specific representation strengths"——更深层的洞察，更广的适用性。C2=76%
362	    虽然低于 FOLIO，但 CI 下界 66.1% 接近 70% gate，在 best 档位下 point estimate 通过。C3=3 types（少了
363	    quantifier_error， 因为数学域没有量词问题），但新增 computation_error（截断/精度）类型。
364	
365	    '
366	- name: Repair 机制改进（多轮修复）
367	  plan_id: exp-005
368	  description: '最多 3 轮 repair，加入错误类型特定修复策略，按 GT label 和 error_type 分层报告。 目标：Unknown
369	    子组 delta 从 +14.7pp 拉到 +20pp+。
370	
371	    '
372	  expected_results:
373	    repair_rounds_avg: 1.8
374	    GT_Unknown_delta_round1: +14.7pp
375	    GT_Unknown_delta_round3: +22.1pp
376	    GT_False_delta_round1: +6.7pp
377	    GT_False_delta_round3: +10.4pp
378	    GT_True_delta_round1: -13.6pp
379	    GT_True_delta_round3: -11.2pp
380	    C4_unknown_false_combined_delta: +15.8pp
381	    error_type_repair_success:
382	      logic_error: 68.3%
383	      negation_error: 72.0%
384	      exec_crash: 81.8%
385	      quantifier_error: 50.0%
386	    round2_additional_fixes: 8 samples
387	    round3_additional_fixes: 3 samples
388	  result_rationale: '在 best 档位下，多轮 repair 将 GT=Unknown delta 从 +14.7pp 拉到 +22.1pp（超过
389	    +20pp gate）。 机制：第一轮修复了大部分 Code overclaiming（Code 输出 True/False 但应为 Unknown）， 第二轮处理残余的
390	    logic_error（FOL 形式化中的量词/否定遗漏导致第一轮修复方向偏移）， 第三轮边际收益递减（仅 3 个 additional fix）。GT=True
391	    overcorrection 从 -13.6pp 改善到 -11.2pp——多轮 repair 的错误类型感知策略对 GT=True 的伤害略有缓解 （negation_error
392	    特定策略避免了盲目翻转），但仍然为负，证明 overcorrection boundary 是结构性的而非策略不足。exec_crash 81.8% 修复率最高因为这类错误最容易诊断和修复
393	    （语法/运行时错误，重新生成即可）。quantifier_error 50% 最低因为量词错误需要 深层理解全称/存在量词的语义。combined delta
394	    +15.8pp 落在 [8, 18] range 的偏高区域。
395	
396	    '
397	  tables:
398	  - name: 'Table 8: Multi-Round Repair Results (FOLIO, n=204)'
399	    columns:
400	    - GT Label
401	    - n
402	    - Round 1 Delta
403	    - Round 3 Delta
404	    - Improvement
405	    rows:
406	    - - Unknown
407	      - 69
408	      - +14.7pp
409	      - +22.1pp
410	      - +7.4pp
411	    - - 'False'
412	      - 63
413	      - +6.7pp
414	      - +10.4pp
415	      - +3.7pp
416	    - - 'True'
417	      - 72
418	      - -13.6pp
419	      - -11.2pp
420	      - +2.4pp (still negative)
421	  - name: 'Table 9: Repair Success Rate by Error Type (Round 3)'
422	    columns:
423	    - Error Type
424	    - Attempted
425	    - Fixed
426	    - Success Rate
427	    rows:
428	    - - logic_error
429	      - 41
430	      - 28
431	      - 68.3%
432	    - - negation_error
433	      - 18
434	      - 13
435	      - 72.0%
436	    - - exec_crash
437	      - 11
438	      - 9
439	      - 81.8%
440	    - - quantifier_error
441	      - 4
442	      - 2
443	      - 50.0%
444	  figures_description:
445	  - 'Fig 10: 多轮 repair 收益曲线（Round 1/2/3 delta 按 GT label）'
446	  - 'Fig 11: 错误类型特定修复成功率 bar chart'
447	  analysis: '多轮 repair 的递减收益模式（Round 1: +14.7→+22.1, Round 2: +5.2, Round 3: +2.2）
448	    是 best 档位的理想结果——证明错误类型特定策略有增量价值，但不是无限的。 GT=True 仍为负是论文的 honesty signal——不掩饰 boundary。错误类型分层报告
449	    为 exp-008（taxonomy ablation）提供了直接支撑。
450	
451	    '
452	- name: Unknown 样本深度分析 + correlated failure 定量
453	  plan_id: exp-006
454	  description: '分析 GT=Unknown 驱动 C4 delta 的机制，FOL/Code 相关系数按 GT 分层， false agreement
455	    rate，specification vs formalization 错误分类。
456	
457	    '
458	  expected_results:
459	    code_overclaiming_rate_unknown: 78.3% (54/69)
460	    code_overclaiming_mechanism: Code 路径倾向输出 True/False 而非 Unknown，因为 Python 缺乏三值逻辑原生支持
461	    fol_overclaiming_rate_unknown: 21.7% (15/69)
462	    phi_by_GT:
463	      'True': 0.245
464	      'False': 0.162
465	      Unknown: 0.098
466	    false_agreement_rate: 12.3% (25/204)
467	    false_agreement_breakdown: GT=True 14/72 (19.4%), GT=False 7/63 (11.1%), GT=Unknown
468	      4/69 (5.8%)
469	    specification_error_rate: 8.3% (17/204)
470	    formalization_specific_error_rate: 91.7% (187/204 non-spec-error)
471	  result_rationale: '在 best 档位下，Code overclaiming 78.3% 的高比率清晰解释了 GT=Unknown 子集的 repair
472	    delta 来源：Python 执行路径缺乏三值逻辑（True/False/Unknown）的原生表达能力， 倾向将 insufficient-information
473	    情况强制映射为 True 或 False。当 CRD 诊断出分歧后， repair prompt 包含"FOL 路径返回 Unknown"的信息，帮助模型认识到证据不足，修正
474	    Code 的 overclaiming。phi 按 GT 分层显示 Unknown 相关性最低（0.098），意味着 FOL/Code 在 Unknown
475	    上最不相关——互补信号最强，这直接解释了为什么 repair delta 最大。 False agreement rate 12.3% 相对低（Denisov-Blanch
476	    2026 担忧的 correlated failure 不严重），且 GT=Unknown 子集仅 5.8% false agreement——再次证明 Unknown
477	    是 CRD 的 最佳应用场景。specification error 仅 8.3% 说明绝大多数错误是 formalization-specific 而非原始问题歧义导致，支撑
478	    CRD 的诊断靶点合理性。
479	
480	    '
481	  tables:
482	  - name: 'Table 10: Correlated Failure Analysis'
483	    columns:
484	    - GT Label
485	    - n
486	    - phi
487	    - False Agreement Rate
488	    - Code Overclaiming
489	    rows:
490	    - - 'True'
491	      - 72
492	      - 0.245
493	      - 19.4%
494	      - N/A
495	    - - 'False'
496	      - 63
497	      - 0.162
498	      - 11.1%
499	      - N/A
500	    - - Unknown
501	      - 69
502	      - 0.098
503	      - 5.8%
504	      - 78.3%
505	    - - Overall
506	      - 204
507	      - 0.189
508	      - 12.3%
509	      - —
510	  figures_description:
511	  - 'Fig 12: Code overclaiming 机制图——Unknown→True/False 的映射路径'
512	  - 'Fig 13: phi coefficient 按 GT label 分层 + false agreement rate 联合可视化'
513	  analysis: '此分析为 Claim 3 提供了因果机制：不是 repair 策略差异导致 GT-dependent 效应， 而是 Code 表征的结构性局限（缺乏三值逻辑）×
514	    GT label 的交互作用。这使得 GT=True overcorrection 也有了合理解释——当 GT=True 但 Code 错误输出 False/Unknown
515	    时， 诊断信号误导 repair 认为应该远离 True，导致 overcorrection。
516	
517	    '
518	- name: Selection vs Repair 消融
519	  plan_id: exp-007
520	  description: '分歧检测+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层报告。
521	
522	    '
523	  expected_results:
524	    blind_baseline_acc_GT_not_true: 61.4%
525	    selection_acc_GT_not_true: 72.7%
526	    repair_acc_GT_not_true: 76.2%
527	    selection_vs_blind_delta: +11.3pp
528	    repair_vs_selection_delta: +3.5pp
529	    selection_by_error_type:
530	      logic_error: 70.7%
531	      negation_error: 77.8%
532	      exec_crash: 90.9%
533	      quantifier_error: 50.0%
534	    repair_by_error_type:
535	      logic_error: 75.6%
536	      negation_error: 77.8%
537	      exec_crash: 90.9%
538	      quantifier_error: 75.0%
539	    repair_advantage_concentrated_on: logic_error (+4.9pp) 和 quantifier_error (+25pp)
540	  result_rationale: '在 best 档位下，selection 已经大幅优于 blind baseline（+11.3pp，远超 +5pp gate），
541	    证明 CRD 诊断+定位的基本价值。repair 在 selection 之上再加 +3.5pp（刚超 +3pp gate）， 增量价值集中在 logic_error
542	    和 quantifier_error——这两类错误需要修正 formalization 而非简单选边，selection 无法解决因为两侧都可能部分正确（如
543	    FOL 量词正确但谓词错误， Code 谓词正确但逻辑流错误）。negation_error 和 exec_crash 上 repair ≈ selection，
544	    因为这两类错误通常有明确的"一侧对一侧错"模式，选正确侧就足够了。 这个分层结果支撑了论文的 nuanced claim：repair 不是全面优于 selection，
545	    而是在特定错误类型上有不可替代的价值——正是 taxonomy 驱动修复的意义。 限制在 GT≠True 子集报告（n=132），因为 GT=True overcorrection
546	    对 selection 和 repair 都适用，不影响二者的相对对比。
547	
548	    '
549	  tables:
550	  - name: 'Table 11: Selection vs Repair on GT≠True Subset (n=132)'
551	    columns:
552	    - Method
553	    - Overall Acc
554	    - logic_error
555	    - negation_error
556	    - exec_crash
557	    - quantifier_error
558	    rows:
559	    - - Blind Baseline
560	      - 61.4%
561	      - 56.1%
562	      - 66.7%
563	      - 72.7%
564	      - 25.0%
565	    - - Selection
566	      - 72.7%
567	      - 70.7%
568	      - 77.8%
569	      - 90.9%
570	      - 50.0%
571	    - - Repair (Round 3)
572	      - 76.2%
573	      - 75.6%
574	      - 77.8%
575	      - 90.9%
576	      - 75.0%
577	  figures_description:
578	  - 'Fig 14: 三方法对比 grouped bar chart，按 error_type 分层'
579	  - 'Fig 15: Repair 增量价值热图（repair - selection delta 按 error type）'
580	  analysis: 'Selection vs repair 的分层结果是 exp-007 的核心贡献：证明 taxonomy 不仅是分析工具， 还有规定性价值（prescriptive
581	    value）——知道错误类型决定了应该 select 还是 repair。 这直接回应 R3 并为 exp-008 铺路。selection_vs_blind
582	    +11.3pp 是强结果， 证明即使不 repair，CRD 诊断+定位已经有实用价值。
583	
584	    '
585	- name: Error Taxonomy 消融
586	  plan_id: exp-008
587	  description: '按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。
588	
589	    '
590	  expected_results:
591	    taxonomy_guided_acc: 76.2%
592	    fixed_strategy_acc: 71.2%
593	    taxonomy_delta: +5.0pp
594	    taxonomy_advantage_by_type:
595	      logic_error: +6.2pp
596	      negation_error: +2.3pp
597	      exec_crash: +0.0pp
598	      quantifier_error: +18.0pp
599	    mcnemar_p: 0.042
600	  result_rationale: '在 best 档位下，taxonomy-guided 策略整体优于 fixed strategy +5.0pp（McNemar
601	    p=0.042， 显著）。增量主要来自 logic_error（最大类，+6.2pp——targeted prompt 包含"检查谓词定义 和推理链"vs
602	    盲目重生成）和 quantifier_error（最小类但增幅最大 +18.0pp——targeted prompt 显式提示"检查全称/存在量词的作用域"，盲目重生成几乎无法修复这类细微错误）。
603	    exec_crash 无差异因为重生成本身就是最优策略（崩溃了就重新生成）。negation_error 增量小因为否定翻转相对简单，固定策略也能偶然修复。McNemar
604	    p=0.042 刚好显著， 反映样本量有限但效应真实。
605	
606	    '
607	  tables:
608	  - name: 'Table 12: Taxonomy-Guided vs Fixed Strategy Repair'
609	    columns:
610	    - Error Type
611	    - n
612	    - Taxonomy-Guided
613	    - Fixed (regen)
614	    - Delta
615	    rows:
616	    - - logic_error
617	      - 41
618	      - 75.6%
619	      - 69.4%
620	      - +6.2pp
621	    - - negation_error
622	      - 18
623	      - 77.8%
624	      - 75.5%
625	      - +2.3pp
626	    - - exec_crash
627	      - 11
628	      - 90.9%
629	      - 90.9%
630	      - +0.0pp
631	    - - quantifier_error
632	      - 4
633	      - 75.0%
634	      - 57.0%
635	      - +18.0pp
636	    - - Overall
637	      - 74
638	      - 76.2%
639	      - 71.2%
640	      - +5.0pp (p=0.042)
641	  figures_description:
642	  - 'Fig 16: Taxonomy-guided vs fixed strategy 按 error type 对比'
643	  analysis: 'Taxonomy ablation 证明 error classification 不只是 analysis contribution——
644	    它有 prescriptive value。这将 Claim 2 从纯分析升级为方法贡献， 增加论文的实用性维度。quantifier_error 的 +18pp
645	    虽然 n 太小（4 samples）不能 单独做统计检验，但方向明确。
646	
647	    '
648	- name: 统计显著性全面检验
649	  plan_id: exp-009
650	  description: '对所有 benchmark 的 C1-C5 指标做 Bootstrap 95% CI + Fisher exact / McNemar
651	    test。
652	
653	    '
654	  expected_results:
655	    FOLIO_C2_CI: '[81.3%, 94.7%]'
656	    LogiQA_C2_CI: '[73.8%, 88.2%]'
657	    MATH_C2_CI: '[66.1%, 85.2%]'
658	    cross_benchmark_C2_min_lower: 66.1%
659	    FOLIO_C4_unknown_fisher_p: 0.038
660	    FOLIO_C4_true_fisher_p: 0.021
661	    LogiQA_C4_positive_subset_fisher_p: 0.045
662	    CRD_vs_SC5_mcnemar_p: 0.031
663	    all_primary_claims_significant: true
664	    aggregate_C4_significant: false
665	  result_rationale: '在 best 档位下，所有主要 claim 的分层指标都达到统计显著：FOLIO GT=Unknown C4 delta
666	    Fisher p=0.038（n=69，+14.7pp→+22.1pp 多轮后更强），GT=True overcorrection p=0.021（负方向也显著，strengthens
667	    boundary characterization）。LogiQA 的正子集 p=0.045 复现效应。CRD vs SC5 McNemar p=0.031
668	    证明诊断精度差异显著。 关键：aggregate C4 仍然不显著——这在 best 档位下是 feature not bug， 因为分层报告是我们的 methodological
669	    contribution。CI 紧致度随样本量提高 （FOLIO n=204 > LogiQA n=200 > MATH n=200），MATH C2 下界
670	    66.1% 最低 但 point estimate 76% 仍超 70% gate。
671	
672	    '
673	  tables:
674	  - name: 'Table 13: Statistical Significance Summary Across Benchmarks'
675	    columns:
676	    - Test
677	    - Benchmark
678	    - Metric
679	    - Statistic
680	    - p-value
681	    - Significant?
682	    rows:
683	    - - Fisher
684	      - FOLIO
685	      - C4 GT=Unknown
686	      - +22.1pp
687	      - '0.038'
688	      - 'Yes'
689	    - - Fisher
690	      - FOLIO
691	      - C4 GT=True
692	      - -11.2pp
693	      - '0.021'
694	      - 'Yes'
695	    - - Fisher
696	      - LogiQA
697	      - C4 positive subset
698	      - +11.3pp
699	      - '0.045'
700	      - 'Yes'
701	    - - McNemar
702	      - FOLIO
703	      - CRD vs SC5 precision
704	      - +7.2pp
705	      - '0.031'
706	      - 'Yes'
707	    - - Fisher
708	      - FOLIO
709	      - C4 aggregate
710	      - +4.65pp
711	      - '0.626'
712	      - 'No'
713	    - - Bootstrap
714	      - All
715	      - C2 range
716	      - '[66.1%, 94.7%]'
717	      - —
718	      - —
719	  figures_description:
720	  - 'Fig 17: 跨基准 C2 Bootstrap CI 的 forest plot'
721	  analysis: '统计检验结果在 best 档位下完美支撑叙事：分层指标显著而 aggregate 不显著， 证明分层分析的必要性。Forest plot
722	    显示三基准 C2 CI 重叠但中心递减 （FOLIO > LogiQA > MATH），反映任务复杂度梯度。
723	
724	    '
725	- name: Self-Consistency Baseline 对比
726	  plan_id: exp-012
727	  description: 'FOLIO + LogiQA + MATH 上对比 k=5 FOL-only majority vote, k=5 Code-only
728	    majority vote, vs single-pass CRD。隔离 cross-representation 信号 vs 单表征 sampling diversity。
729	
730	    '
731	  expected_results:
732	    FOLIO:
733	      SC5_FOL_precision: 79.3%
734	      SC5_Code_precision: 72.1%
735	      CRD_precision: 87.2%
736	      CRD_vs_SC5_FOL_delta: +7.9pp
737	      SC5_FOL_cost_tokens: 5x baseline
738	      SC5_Code_cost_tokens: 5x baseline
739	      CRD_cost_tokens: 2x baseline
740	      CRD_vs_SC5_cost_ratio: '0.40'
741	    LogiQA:
742	      SC5_FOL_precision: 75.8%
743	      SC5_Code_precision: 69.4%
744	      CRD_precision: 81.5%
745	      CRD_vs_SC5_FOL_delta: +5.7pp
746	    MATH:
747	      SC5_SymPy_precision: 71.2%
748	      SC5_Python_precision: 74.8%
749	      CRD_precision: 76.0%
750	      CRD_vs_SC5_best_delta: +1.2pp
751	    overall_CRD_vs_SC5_precision_delta: +4.9pp (avg across benchmarks)
752	    overall_CRD_vs_SC5_cost_ratio: 0.4
753	  result_rationale: '在 best 档位下，CRD 在所有三个基准上诊断精度均优于 k=5 单表征 majority vote， 且 token
754	    成本仅为 40%（2 次生成 vs 5 次生成）。机制：k=5 同表征 sampling 捕获的是 generation variance（同一 prompt
755	    的随机性），而 CRD 捕获的是 paradigm-level difference （形式逻辑 vs 命令式代码的系统性差异）。前者在高温度下有效但容易被
756	    mode collapse 削弱 （LLM 倾向于收敛到同一错误模式），后者因为表征范式根本不同而产生更互补的错误信号。 FOLIO delta 最大（+7.9pp）因为
757	    FOL 和 Python 的范式差异最大；MATH delta 最小（+1.2pp） 因为 SymPy 和 Python numerical 都是 Python
758	    生态，范式差异较小。MATH 上 SC5_Python 甚至略优于 SC5_SymPy（74.8% vs 71.2%），与 exp-004 的不对称反转一致。
759	    CRD cost ratio 0.40 落在 [0.30, 0.45] range——2 次生成 vs 5 次生成 = 0.40， 考虑 CRD 额外的 diagnosis
760	    prompt 开销后正好 40%。
761	
762	    '
763	  tables:
764	  - name: 'Table 14: CRD vs Self-Consistency (k=5) Across Benchmarks'
765	    columns:
766	    - Benchmark
767	    - SC5-FOL Prec
768	    - SC5-Code Prec
769	    - CRD Prec
770	    - CRD-SC5 Δ
771	    - Cost Ratio
772	    rows:
773	    - - FOLIO
774	      - 79.3%
775	      - 72.1%
776	      - 87.2%
777	      - +7.9pp
778	      - '0.40'
779	    - - LogiQA
780	      - 75.8%
781	      - 69.4%
782	      - 81.5%
783	      - +5.7pp
784	      - '0.40'
785	    - - MATH
786	      - 71.2%
787	      - 74.8%
788	      - 76.0%
789	      - +1.2pp
790	      - '0.40'
791	    - - Average
792	      - 75.4%
793	      - 72.1%
794	      - 81.6%
795	      - +4.9pp
796	      - '0.40'
797	  figures_description:
798	  - 'Fig 18: CRD vs SC5 precision-cost Pareto 图——CRD 在 Pareto front 上'
799	  - 'Fig 19: 按基准的 CRD vs SC5 对比 grouped bar chart'
800	  analysis: 'exp-012 是回应 R8 的核心实验。best 档位下 CRD Pareto-dominates SC5（更高精度+更低成本）， headline
801	    变为"用 40% 的 token 成本获得平均 +4.9pp 的诊断精度提升"。 MATH 上 delta 仅 +1.2pp 是可接受的——因为 SymPy/Python
802	    范式差异较小， 但仍为正且 cost advantage 不变。论文可以讨论 "paradigm distance" 作为 CRD 效果的调节变量——范式差异越大，CRD
803	    相对于 SC5 的优势越大。
804	
805	    '
806	- name: Error Taxonomy 交叉验证
807	  plan_id: exp-013
808	  description: 'DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比， 计算 Cohen''s κ。验证
809	    taxonomy 跨模型稳定性。
810	
811	    '
812	  expected_results:
813	    n_classified: 75
814	    cohens_kappa: 0.67
815	    kappa_CI: '[0.54, 0.80]'
816	    agreement_by_type:
817	      logic_error: 78.8%
818	      negation_error: 72.7%
819	      exec_crash: 90.9%
820	      quantifier_error: 50.0%
821	    deepseek_type_distribution:
822	      logic_error: 28.0%
823	      negation_error: 12.0%
824	      exec_crash: 6.7%
825	      quantifier_error: 1.3%
826	      unclassified: 4.0%
827	    distribution_stability: rank order preserved (logic > negation > crash > quantifier)
828	  result_rationale: '在 best 档位下，Cohen''s κ=0.67 落在 [0.60, 0.80] range，达到 "substantial
829	    agreement" 标准。κ 不更高的原因合理：两个模型对 logic_error vs negation_error 的边界划分有 模糊区域（一些否定相关的逻辑错误可以归入任一类别），这是分类本身的固有模糊性而非
830	    taxonomy 设计缺陷。exec_crash 一致性最高（90.9%）因为执行崩溃是客观可验证的。 quantifier_error 一致性最低（50%）因为
831	    n 太小（仅 4 样本）且量词错误判断需要 深层语义理解。关键发现：两个模型的错误类型分布 rank order 完全一致 （logic > negation
832	    > crash > quantifier），说明 taxonomy 反映的是错误结构而非 模型偏好。DeepSeek 的 logic_error 比例略高（28%
833	    vs 25.5%）、unclassified 略低 （4% vs 0%），因为 DeepSeek 更倾向给出明确分类而非其他 catch-all。
834	
835	    '
836	  tables:
837	  - name: 'Table 15: Cross-Model Taxonomy Validation (n=75 diagnostic samples)'
838	    columns:
839	    - Error Type
840	    - Qwen3-32B %
841	    - DeepSeek %
842	    - Pairwise Agreement
843	    - κ contribution
844	    rows:
845	    - - logic_error
846	      - 25.5%
847	      - 28.0%
848	      - 78.8%
849	      - '0.71'
850	    - - negation_error
851	      - 10.8%
852	      - 12.0%
853	      - 72.7%
854	      - '0.62'
855	    - - exec_crash
856	      - 5.4%
857	      - 6.7%
858	      - 90.9%
859	      - '0.88'
860	    - - quantifier_error
861	      - 2.0%
862	      - 1.3%
863	      - 50.0%
864	      - '0.45'
865	    - - Overall κ
866	      - —
867	      - —
868	      - —
869	      - '0.67'
870	  figures_description:
871	  - 'Fig 20: 4×4 confusion matrix heatmap (Qwen classification vs DeepSeek classification)'
872	  - 'Fig 21: 两个模型的错误类型分布 side-by-side bar chart'
873	  analysis: 'κ=0.67 回应 R9 的 taxonomy validation 要求。substantial agreement 证明 taxonomy
874	    不是单模型的 artifact——不同 LLM 从同一组分歧样本中识别出一致的错误模式。 rank order 稳定性是更强的信号：即使个别样本分类不同，宏观分布结构跨模型复现，
875	    说明四类错误反映了 formalization 的真实失败模式。
876	
877	    '
878	- name: Qwen3-8B 消融
879	  plan_id: exp-010
880	  description: '低能力模型上的诊断率和分歧率变化。P2 优先级。
881	
882	    '
883	  expected_results:
884	    n: 204
885	    C1_disagree_rate: 55.4%
886	    C2_diagnostic_rate: 74.5%
887	    asymmetry: 2.8:1 (FOL-favored, compressed)
888	    fol_accuracy: 58.3%
889	    code_accuracy: 47.1%
890	    C4_aggregate: +2.1pp
891	  result_rationale: '在 best 档位下，8B 模型 C1 上升到 55.4%（更弱模型→更多 formalization 错误→更多分歧），
892	    但 C2 降至 74.5%（更多分歧来自"两侧都错"的 correlated failure，诊断性下降）。 这个 C1↑C2↓ 的 tradeoff 是
893	    model-capability 对 CRD 有效性的重要 characterization： 存在一个能力下限，低于此 CRD 的诊断价值被 correlated
894	    failure 侵蚀。 不对称比压缩到 2.8:1 因为 8B 的 FOL 能力下降更快（形式逻辑对模型能力更敏感）。 作为 P2 实验，这提供了有价值的
895	    scaling 分析但不影响核心 claim。
896	
897	    '
898	  tables:
899	  - name: 'Table 16: Model Scale Ablation on FOLIO'
900	    columns:
901	    - Model
902	    - C1
903	    - C2
904	    - Asymmetry
905	    - FOL Acc
906	    - Code Acc
907	    rows:
908	    - - Qwen3-32B
909	      - 42.2%
910	      - 87.2%
911	      - 5.6:1
912	      - 78.4%
913	      - 59.8%
914	    - - Qwen3-8B
915	      - 55.4%
916	      - 74.5%
917	      - 2.8:1
918	      - 58.3%
919	      - 47.1%
920	    - - DeepSeek V4 Pro
921	      - 38.7%
922	      - 83.5%
923	      - 4.2:1
924	      - 81.2%
925	      - 64.7%
926	  figures_description:
927	  - 'Fig 22: Model capability vs C1/C2 scatter plot (三模型)'
928	  analysis: '三个模型形成 capability 梯度（8B < 32B < DeepSeek Pro），C2 单调递增， C1 单调递减——完美的 scaling
929	    story。论文 1 段 discussion 即可，不需要更多。
930	
931	    '
932	- name: GPQA Diamond 扩展
933	  plan_id: exp-011
934	  description: '科学知识推理，SymPy/Python 双可执行表征。P2 优先级。
935	
936	    '
937	  expected_results:
938	    n: 150
939	    C1_disagree_rate: 22.0%
940	    C2_diagnostic_rate: 72.7%
941	    asymmetry: 1.4:1 (slight Python-favored)
942	    note: C2 略低于 70% gate——科学推理中 domain knowledge 错误占比高，CRD 对 knowledge gap 诊断力有限
943	  result_rationale: '在 best 档位下，GPQA C1=22% 较低（科学推理需要 domain knowledge 而非纯 formalization，
944	    两条路径的差异更多来自知识错误而非表征差异），C2=72.7% 在 70% gate 边缘。 这是 CRD 适用边界的有价值 characterization：cross-representation
945	    disagreement 对 formalization errors 诊断力强，对 domain knowledge errors 诊断力弱。 作为 P2
946	    可选实验，如果时间不够可以省略，核心三基准已足够。
947	
948	    '
949	  tables:
950	  - name: 'Table 17: Cross-Domain CRD Effectiveness'
951	    columns:
952	    - Domain
953	    - Benchmark
954	    - C1
955	    - C2
956	    - Primary Error Source
957	    rows:
958	    - - Logic
959	      - FOLIO
960	      - 42.2%
961	      - 87.2%
962	      - Formalization
963	    - - Logic
964	      - LogiQA
965	      - 34.0%
966	      - 81.5%
967	      - Formalization
968	    - - Math
969	      - MATH L5
970	      - 28.5%
971	      - 76.0%
972	      - Computation
973	    - - Science
974	      - GPQA
975	      - 22.0%
976	      - 72.7%
977	      - Knowledge gap
978	  figures_description:
979	  - 'Fig 23: Domain × C2 effectiveness 趋势图——formalization-heavy 域 CRD 最有效'
980	  analysis: 四基准形成清晰的域梯度：纯逻辑 > 数学 > 科学，C2 随 formalization 占比下降。 这是 best 档位的 bonus result——不是每个域都好用恰恰证明我们理解了
981	    CRD 的机制和边界。 但 GPQA 作为 P2 实验，若时间不足可省略，不影响核心结论。
982	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa3df727-6faf-4d01-b3c5-02997254629f",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "638b3fc9-1ba3-4e07-b3b7-22b43135db92",
  "sourceToolAssistantUUID": "aa3df727-6faf-4d01-b3c5-02997254629f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-15T07:50:37.847Z_

I now have a comprehensive understanding of the paper, the experimental design, the review context, and a prior R2 review. Let me now submit my independent review via the submit tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "638b3fc9-1ba3-4e07-b3b7-22b43135db92",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zL6FBThhtR3XNDtNj6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a31c058-eefc-47d2-a1fb-37595490bd25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEa2fBQuLjkDM15C4h5hNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17370,
      "cache_read_input_tokens": 61982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17370,
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

_source line 39 · 2026-05-15T07:50:38.903Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RxXxfhZn5Nd4KswzzMXy12`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a31c058-eefc-47d2-a1fb-37595490bd25",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zL6FBThhtR3XNDtNj6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfa92b06-8625-45d0-be6a-7cb704168934",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEa2fBQuLjkDM15C4h5hNe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17370,
      "cache_read_input_tokens": 61982,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 61982,
          "cache_creation_input_tokens": 17370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17370,
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

_source line 40 · 2026-05-15T07:50:38.908Z_

<details><summary>↩ Tool result · `toolu_01RxXxfhZn5Nd4KswzzMXy12`</summary>

````text
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
  "parentUuid": "bfa92b06-8625-45d0-be6a-7cb704168934",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "595d0d9a-f2ee-478c-b3af-abf94a97ecd8",
  "sourceToolAssistantUUID": "bfa92b06-8625-45d0-be6a-7cb704168934",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-15T07:50:46.059Z_



Now I have all the information needed to write a thorough, independent R2 review focused on novelty, positioning, and related work. Let me compose and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "595d0d9a-f2ee-478c-b3af-abf94a97ecd8",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zLUKUVPsoHKeqdAX4V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab2a3ca1-633e-4136-bc3a-1b27f31bf53d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fxFnquGwSBqATkGw2TUFY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 79352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 706,
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

_source line 42 · 2026-05-15T07:52:00.149Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01FWhBtGbLJhuxTrphZQyfXQ`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "tier": "best",
  "dream_id": "dream_20260515T071730",
  "overall_score": "weak reject",
  "report": "### R2 Review: Novelty & Related Work\n\n**Score:** 3/6\n\n**Summary:** This paper extends cross-representation disagreement from a binary filtering signal (as in Liang et al. 2024) to a structured diagnostic framework with error taxonomy, localization, and targeted repair. The most novel empirical findings are the GT-label-dependent repair asymmetry and the domain-dependent asymmetry reversal (FOL-favored in logic, Code-favored in math). However, the conceptual novelty increment over Liang et al. (2024) is modest -- the leap from \"disagreement as filter\" to \"disagreement as diagnosis\" is largely an engineering extension rather than a conceptual breakthrough -- and the related work coverage, while improved over earlier drafts, still has structural gaps that undermine the positioning claims.\n\n**Strengths:**\n- S1: **The domain-dependent asymmetry reversal is a genuinely novel finding.** The observation that FOL dominates 5.6:1 in logic but Code dominates 1.8:1 in math is non-obvious and has independent analytical value. This finding goes beyond what any prior work (including Liang et al. 2024) has demonstrated, and the mechanistic explanation (representation-task fit rather than fixed verifier hierarchy) is convincing. This is the paper's strongest novelty claim.\n\n- S2: **The GT-label-dependent repair effect is a well-characterized, honest contribution.** Rather than reporting only the aggregate non-significant C4 (+4.65pp, p=0.626) or cherry-picking the positive subsets, the paper explicitly presents the three-way split and frames GT=True overcorrection as a discovered boundary condition. This level of analytical honesty is rare and the finding itself -- that diagnosis actively hurts repair on GT=True cases -- is a useful cautionary insight for practitioners. The mechanistic explanation via Code overclaiming (78.3% on GT=Unknown) is well-supported.\n\n- S3: **Comprehensive ablation structure addresses most foreseeable objections.** The paper includes cross-model validation (Table 5), selection vs. repair comparison (Table 8), taxonomy-guided vs. fixed-strategy ablation (Table 9), self-consistency baseline (Table 11), model scale analysis (Table 12), and domain boundary characterization (Table 13). This is a thorough experimental design for an analysis-primary paper. The cross-model taxonomy validation (kappa=0.67) directly addresses the concern about LLM-classified error types being unreliable.\n\n- S4: **The CRD vs. self-consistency comparison (Table 11) establishes a clear practical advantage.** Pareto-dominating k=5 self-consistency at 40% token cost is a clean, memorable result. The observation that CRD's advantage scales with paradigm distance (FOLIO +7.9pp vs. MATH +1.2pp) provides a useful design principle.\n\n**Weaknesses:**\n- W1: **Incremental novelty over Liang et al. (2024) and the positioning overstates the gap.** The paper positions against Liang et al. (2024) as \"filtering vs. diagnosis,\" but the diagnostic step itself is straightforward: classify the disagreement pattern using rule-based heuristics, run a stability test (k=3 re-executions), and feed the diagnosis into a repair prompt. Each component is individually well-known (rule-based error classification, perturbation-based stability testing, diagnosis-informed prompting). The combination is sensible engineering but the paper reads as if the conceptual contribution is larger than it is. The \"extends from binary filtering to structured diagnosis\" framing makes it sound like a new paradigm when it is more accurately described as adding three standard modules on top of the Liang et al. observation.\n\n- W2: **Critical related work gaps remain.** Several highly relevant works are either missing or insufficiently discussed:\n  - **PAL (Gao et al., ICML 2023)** and **PoT (Chen et al., 2023)**: Program-of-Thought and Program-Aided Language Models generate code as reasoning traces -- the Code side of CRD is essentially PoT. The paper never acknowledges this lineage.\n  - **Universal Self-Consistency (Chen et al., 2024)**: Extends self-consistency to free-form text via LLM-based agreement checking, directly relevant to how CRD compares outputs across representations.\n  - **DIVERSE (Li et al., ICLR 2023)**: Uses diverse verifiers and voting strategies across reasoning paths -- conceptually related to cross-representation ensembling.\n  - **Zheng et al. (2024), \"Progressive Verification\"**: Uses multiple verification steps with different strategies, related to multi-round repair.\n  - The paper's discussion of Roundtrip Verification (Zhong et al. 2025) is too brief. That work demonstrated diagnosis-guided repair within one representation on 150 traffic rules -- CRD extends this cross-representationally but on similarly small sample sizes (150-204). The paper should explicitly discuss what the cross-representation extension buys over within-representation roundtrip verification, beyond the obvious \"different paradigms.\"\n\n- W3: **Several bibliography entries are incomplete or potentially unreliable.** References for PROVE (2024), Kang et al. (2025) VERGE, Weng et al. (2023) VeriCoT, Li et al. (2024) HybridMind, Sun et al. (2024) Adaptive Selection, and Zhong et al. (2025) Roundtrip Verification all lack full author lists or have suspiciously generic titles. \"PROVE (2024)\" is cited as just a title with no authors -- if this is a real published work, it needs proper attribution. If these references cannot be fully verified, this is a serious integrity concern for venue submission. At a top venue, every citation must be verifiable.\n\n- W4: **The MATH domain extension conflates different things under \"cross-representation.\"** In the logic domain, CRD compares FOL+Z3 (declarative, formally verified) vs. Python (imperative, executed). In the math domain, it compares SymPy symbolic vs. Python numerical -- both are Python libraries in the same ecosystem. The paper acknowledges this produces smaller paradigm distance (Section 5, Discussion), but the framing still treats both instantiations as equivalent demonstrations of \"cross-representation disagreement.\" This is imprecise. SymPy vs. Python numerical is more accurately \"cross-library\" or \"cross-computation-mode\" disagreement, lacking the declarative-vs-imperative paradigm gap that makes the logic domain compelling. The paper's own data confirms this: MATH shows the smallest CRD advantage over SC5 (+1.2pp), suggesting the cross-representation signal is weak when paradigm distance is small. The paper should be more explicit about this limitation rather than presenting MATH as equivalent evidence for the CRD thesis.\n\n- W5: **The error taxonomy's coverage and exclusivity are not validated.** The four types (logic_error, negation_error, exec_crash, quantifier_error) are presented as a complete taxonomy, but no analysis shows what fraction of disagreements fall outside these categories. The cross-model kappa of 0.67 validates inter-rater reliability but not coverage -- both models might consistently fail to capture a fifth error type. Additionally, negation_error is arguably a subtype of logic_error (incorrect logical connectives), and exec_crash is an operational failure rather than a reasoning error. The taxonomy mixes error granularity levels and error categories (reasoning errors vs. execution failures) without justification.\n\n- W6: **The paper does not adequately address the oracle information problem.** The GT-label-dependent repair analysis (Claim 3) relies on ground-truth labels for stratification. In deployment, GT labels are unknown. The paper discusses this briefly (\"practitioners should apply diagnosis-guided repair selectively, skipping it for high-confidence True predictions\") but does not provide a mechanism for predicting which GT-label bucket a sample falls into without access to GT. Without such a mechanism, the practical utility of the GT-dependent finding is limited to post-hoc analysis rather than actionable deployment guidance. This weakens Claim 3's contribution from \"prescriptive\" to \"descriptive.\"\n\n**Questions for Authors:**\n- Q1: How does CRD compare to a hybrid baseline that runs k=2 self-consistency within FOL and k=2 within Code (4 total calls, comparable cost to CRD's 2 calls + diagnosis overhead)? The current comparison against k=5 single-representation SC is favorable to CRD on cost, but a cross-representation k=2+2 baseline would test whether CRD's advantage comes from the cross-representation structure or simply from having both FOL and Code outputs available.\n\n- Q2: The stability test uses k=3 temperature perturbations for localization. How sensitive are the localization results to the choice of k and the temperature range? Was there any ablation on the stability test parameters? The 47% ambiguous rate is high -- could a higher k (e.g., k=5 or k=7) reduce ambiguity without proportional cost increase?\n\n**Minor Issues:**\n- The cost analysis claims 40% of SC5 cost, but this ignores the cost of the error classification, stability test (k=3 additional calls per representation = 6 calls for disagreeing samples), and repair (1-3 calls). For the 42% of samples that disagree, the actual cost is substantially higher than 2 calls. A more honest cost analysis would report expected cost per sample averaged over the full dataset.\n- Table 11 column header \"CRD\" reports diagnostic precision alongside SC5 diagnostic precision, but CRD is defined as the disagreement-based signal while SC5 uses majority vote inconsistency. The paper should clarify exactly what \"diagnostic precision\" means for each method to ensure fair comparison.\n- The Denisov-Blanch (2026) reference appears to be a future paper (the current date is May 2026). If this is a preprint, the citation should note this. If it does not yet exist, it should be removed.\n- quantifier_error has only n=4 samples throughout the paper. Reporting 50% or 75% accuracy on 4 samples is misleading -- these should be reported as raw counts (2/4, 3/4) rather than percentages, or flagged with explicit sample size warnings.\n- The paper lacks any qualitative error examples. Including 2-3 concrete examples of each error type (showing the original problem, the FOL formalization, the Python formalization, and the disagreement) would substantially improve the reader's understanding of what CRD actually detects.\n\n**Confidence:** 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab2a3ca1-633e-4136-bc3a-1b27f31bf53d",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zLUKUVPsoHKeqdAX4V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c956475a-4a41-4b62-8548-51cdf2652cec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fxFnquGwSBqATkGw2TUFY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 79352,
      "output_tokens": 2663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2663,
          "cache_read_input_tokens": 79352,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 706,
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

_source line 43 · 2026-05-15T07:52:03.838Z_

<details><summary>↩ Tool result · `toolu_01FWhBtGbLJhuxTrphZQyfXQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/review_report.md\", \"dream_id\": \"dream_20260515T071730\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c956475a-4a41-4b62-8548-51cdf2652cec",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a06b1efba249b9d9e",
  "type": "user",
  "uuid": "105ae7d5-02d3-4d12-a054-8a15469eaa11",
  "sourceToolAssistantUUID": "c956475a-4a41-4b62-8548-51cdf2652cec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-15T07:52:20.482Z_

Review submitted. Here is a summary of the R2 assessment:

**Score: 3/6 (Weak Reject)**

**Key findings from the novelty/positioning analysis:**

The paper's strongest novel contributions are (1) the domain-dependent asymmetry reversal (FOL-favored 5.6:1 in logic vs. Code-favored 1.8:1 in math) and (2) the GT-label-dependent repair effect with honest boundary characterization. These are genuinely interesting empirical findings not present in prior work.

However, the review identifies six weaknesses that prevent a positive recommendation at ~25% acceptance rate:

1. **Incremental over Liang et al. (2024)**: The "filtering to diagnosis" extension combines individually known techniques (rule-based classification, perturbation testing, diagnosis-informed prompting) rather than introducing a conceptual advance.

2. **Related work gaps**: Missing PAL/PoT (the Code side's lineage), Universal Self-Consistency, DIVERSE, and inadequate discussion of Roundtrip Verification.

3. **Incomplete/unverifiable bibliography entries**: PROVE, VERGE, VeriCoT, HybridMind, Adaptive Selection, and Roundtrip Verification references all lack full author lists.

4. **MATH domain conflation**: SymPy vs. Python numerical is "cross-library" not "cross-representation" in the paradigm-gap sense. The paper's own data (+1.2pp over SC5 on MATH) confirms weak signal when paradigm distance is small.

5. **Taxonomy coverage unvalidated**: No analysis of out-of-taxonomy errors; mixed granularity levels (negation_error as subtype of logic_error; exec_crash as operational rather than reasoning error).

6. **Oracle information problem**: GT-label-dependent findings (Claim 3) require ground truth for stratification, limiting practical deployment utility.

The review report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "105ae7d5-02d3-4d12-a054-8a15469eaa11",
  "isSidechain": true,
  "agentId": "a06b1efba249b9d9e",
  "requestId": "req_011Cb3zSjHJjmqYsrrFc1wd4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e58cfb4-c786-4f9f-849f-4bc15ef9a7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPpo6Lw546JRWqoDiQ8WgB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 80058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2900,
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
