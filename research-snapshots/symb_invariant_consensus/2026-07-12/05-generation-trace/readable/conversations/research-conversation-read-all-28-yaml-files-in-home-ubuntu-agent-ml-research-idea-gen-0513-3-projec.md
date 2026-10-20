# Research conversation: Read ALL 28 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad9e4baebe5f13e88.jsonl`
- **Structured JSON:** [`f1e831c3d45979d3deca.json`](../../sessions/f1/f1e831c3d45979d3deca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-21T07:44:25.718Z_

Read ALL 28 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/ and return their COMPLETE contents verbatim. The files are:

du2023improving.yaml, chen2024usc.yaml, taubenfeld2025cisc.yaml, dsc2025.yaml, fover2025.yaml, constraintllm2025.yaml, llm_meets_cp2025.yaml, satbench2025.yaml, logicagent2025.yaml, xu2026dylos.yaml, aristotle2025.yaml, qi2025symbolic_provers.yaml, dissecting2025.yaml, crest2025.yaml, khan2024debating.yaml, olausson2023linc.yaml, pan2023logiclm.yaml, snell2025scaling_tts.yaml, multi_path_plan2025.yaml, wang2024mathshepherd.yaml, hosseini2024vstar.yaml, huang2024selfcorrect.yaml, wang2023sc.yaml, li2023diverse.yaml, rc2025.yaml, ye2024satlm.yaml, xu2024symbcot.yaml, xiong2024uncertainty.yaml

I need EVERY field from every YAML. Do not summarize or truncate. Return the full text of each file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "d9f3aa77-f57f-434f-b0d1-8f80fcbf580c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T07:44:27.214Z_

I'll read all 28 YAML files from the specified directory. Let me start by fetching them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f3aa77-f57f-434f-b0d1-8f80fcbf580c",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf1103a6-a379-48f8-9ed5-06597a0211b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-21T07:44:27.477Z_

<details open><summary>🔧 Tool call — Read · `toolu_0169U2tEWgKv8ak9UTm6sv2k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/du2023improving.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf1103a6-a379-48f8-9ed5-06597a0211b8",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6cb7eece-9a44-47eb-97f1-0831b2a3a63a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-21T07:44:27.493Z_

<details><summary>↩ Tool result · `toolu_0169U2tEWgKv8ak9UTm6sv2k`</summary>

```text
1	paper_key: "du2023improving"
2	title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
3	venue: "ICML 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["single-agent CoT", "self-consistency", "self-verification"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "factual validity", direction: "higher_better"}
11	  datasets:
12	    - {name: "GSM8K", size: "N/A"}
13	    - {name: "math reasoning benchmarks", size: "N/A"}
14	    - {name: "biographical QA", size: "N/A"}
15	  ablation_dimensions: ["number of agents", "number of debate rounds"]
16	  training_recipe: {info: "black-box prompting, no training"}
17	  method_family: "multi-agent debate"
18	
19	positioning:
20	  core_claim: "Multiple LLM instances debating over multiple rounds significantly enhances mathematical/strategic reasoning and factual validity compared to single-agent approaches"
21	  key_results: "Significant improvements in mathematical and strategic reasoning; reduced hallucinations and fallacious answers"
22	  limitations: ["N/A"]
23	  relation_to_us: "foundation"
24	
25	narrative: "N/A"
26	figures: "N/A"
27	tables: "N/A"
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cb7eece-9a44-47eb-97f1-0831b2a3a63a",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "6588acc5-aa3e-4ca7-bcfb-77938d7bfa71",
  "sourceToolAssistantUUID": "6cb7eece-9a44-47eb-97f1-0831b2a3a63a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T07:44:27.639Z_

<details open><summary>🔧 Tool call — Read · `toolu_0187QaKK871pi7b5qvWBnurC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/chen2024usc.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6588acc5-aa3e-4ca7-bcfb-77938d7bfa71",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99cf590f-23ee-4e35-a71c-bdb15f7b085f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 6 · 2026-05-21T07:44:27.647Z_

<details><summary>↩ Tool result · `toolu_0187QaKK871pi7b5qvWBnurC`</summary>

```text
1	paper_key: "chen2024usc"
2	title: "Universal Self-Consistency for Large Language Model Generation"
3	venue: "ICML 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard self-consistency (majority voting)", "execution-based voting"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "consistency", direction: "higher_better"}
11	  datasets:
12	    - {name: "mathematical reasoning benchmarks", size: "N/A"}
13	    - {name: "code generation benchmarks", size: "N/A"}
14	    - {name: "long-context summarization", size: "N/A"}
15	    - {name: "open-ended QA", size: "N/A"}
16	  ablation_dimensions: ["task type", "number of samples"]
17	  training_recipe: {info: "prompting-based, no training"}
18	  method_family: "self-consistency"
19	
20	positioning:
21	  core_claim: "LLMs themselves can select the most consistent answer among multiple candidates, extending self-consistency to free-form generation tasks where majority voting is inapplicable"
22	  key_results: "Matches standard self-consistency on math; matches execution-based voting on code generation without execution access"
23	  limitations: ["N/A"]
24	  relation_to_us: "foundation"
25	
26	narrative: "N/A"
27	figures: "N/A"
28	tables: "N/A"
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99cf590f-23ee-4e35-a71c-bdb15f7b085f",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "05de8b72-3694-46de-a577-e6d5fcc3352b",
  "sourceToolAssistantUUID": "99cf590f-23ee-4e35-a71c-bdb15f7b085f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T07:44:28.076Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pmjdns8o1J4KbBvMnTZTEo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/taubenfeld2025cisc.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05de8b72-3694-46de-a577-e6d5fcc3352b",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d786c67-7011-4225-b6fd-8ce38b19a9f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 8 · 2026-05-21T07:44:28.082Z_

<details><summary>↩ Tool result · `toolu_01Pmjdns8o1J4KbBvMnTZTEo`</summary>

```text
1	paper_key: "taubenfeld2025cisc"
2	title: "Confidence Improves Self-Consistency in LLMs"
3	venue: "ACL Findings 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard self-consistency (unweighted majority voting)"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "sample efficiency (paths needed)", direction: "lower_better"}
11	  datasets:
12	    - {name: "4 reasoning datasets (unspecified)", size: "N/A"}
13	  ablation_dimensions: ["confidence scoring method", "number of sampled paths", "model choice"]
14	  training_recipe: {info: "prompting-based, no training; confidence scores from model logits"}
15	  method_family: "confidence-weighted self-consistency"
16	
17	positioning:
18	  core_claim: "Weighted majority voting using model confidence scores (CISC) identifies correct answers with >40% fewer reasoning paths than standard self-consistency across 9 models and 4 datasets"
19	  key_results: ">40% reduction in sampled paths on average; outperforms standard self-consistency across 9 models and 4 datasets"
20	  limitations: ["N/A"]
21	  relation_to_us: "competitor"
22	
23	narrative: "N/A"
24	figures: "N/A"
25	tables: "N/A"
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d786c67-7011-4225-b6fd-8ce38b19a9f2",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "fcb18387-62f0-4541-925a-e484afc63ba6",
  "sourceToolAssistantUUID": "0d786c67-7011-4225-b6fd-8ce38b19a9f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T07:44:28.288Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KriuJQoT1icSgaoGovGZq4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dsc2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcb18387-62f0-4541-925a-e484afc63ba6",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "974e23aa-0eb0-46bb-acae-7acd7d1a7b23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 10 · 2026-05-21T07:44:28.294Z_

<details><summary>↩ Tool result · `toolu_01KriuJQoT1icSgaoGovGZq4`</summary>

```text
1	paper_key: "dsc2025"
2	title: "Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning"
3	venue: "NAACL Findings 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["Adaptive Self-Consistency (ASC)", "Early-stopping Self-Consistency (ESC)", "standard self-consistency"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "inference cost (number of samples)", direction: "lower_better"}
11	  datasets:
12	    - {name: "arithmetic reasoning benchmarks", size: "N/A"}
13	    - {name: "commonsense reasoning benchmarks", size: "N/A"}
14	    - {name: "symbolic reasoning benchmarks", size: "N/A"}
15	  ablation_dimensions: ["prior vs posterior difficulty estimation", "batch-level vs instance-level allocation"]
16	  training_recipe: {info: "prompting-based, no training; difficulty estimation from batch statistics"}
17	  method_family: "adaptive self-consistency"
18	
19	positioning:
20	  core_claim: "Leveraging both prior and posterior difficulty information at the batch level enables adaptive inference resource allocation that significantly reduces self-consistency cost while maintaining comparable performance"
21	  key_results: "Consistently surpasses ASC and ESC in cost efficiency by a significant margin with comparable accuracy across 6 benchmarks"
22	  limitations: ["N/A"]
23	  relation_to_us: "competitor"
24	
25	narrative: "N/A"
26	figures: "N/A"
27	tables: "N/A"
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "974e23aa-0eb0-46bb-acae-7acd7d1a7b23",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "be27bb0f-436f-4662-a0d7-43ff6ee69f26",
  "sourceToolAssistantUUID": "974e23aa-0eb0-46bb-acae-7acd7d1a7b23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T07:44:28.498Z_

<details open><summary>🔧 Tool call — Read · `toolu_012MheA9praX2PWQPArvfKP1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/fover2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be27bb0f-436f-4662-a0d7-43ff6ee69f26",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c5cfe70-1484-4c5f-89c8-8309740d9cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 12 · 2026-05-21T07:44:28.505Z_

<details><summary>↩ Tool result · `toolu_012MheA9praX2PWQPArvfKP1`</summary>

```text
1	paper_key: "fover2025"
2	title: "FoVer: Efficient PRM Training Data Synthesis via Formal Verification"
3	venue: "ACL Findings 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["PRMs trained on human-annotated data", "PRMs trained on LLM-generated labels"]
8	  metrics:
9	    - {name: "accuracy on reasoning benchmarks", direction: "higher_better"}
10	    - {name: "step-level error detection", direction: "higher_better"}
11	  datasets:
12	    - {name: "12 reasoning benchmarks (math, logic, NLI, BBH)", size: "N/A"}
13	    - {name: "formal logic tasks", size: "N/A"}
14	    - {name: "theorem proving tasks", size: "N/A"}
15	  ablation_dimensions: ["formal verification tool (Z3 vs Isabelle)", "training data domain"]
16	  training_recipe: {info: "fine-tuning PRMs on synthesized step-level labels from Z3/Isabelle formal verification"}
17	  method_family: "formal verification for process reward models"
18	
19	positioning:
20	  core_claim: "Formal verification tools (Z3, Isabelle) can automatically synthesize high-quality PRM training data with step-level error labels, improving reasoning across both formal and informal tasks without human annotation"
21	  key_results: "Improves PRMs on math, logic, NLI, and BBH benchmarks; generalizes from formal to informal reasoning"
22	  limitations: ["N/A"]
23	  relation_to_us: "complementary"
24	
25	narrative: "N/A"
26	figures: "N/A"
27	tables: "N/A"
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c5cfe70-1484-4c5f-89c8-8309740d9cbc",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "dadda91c-7d73-405b-8492-84b3c84dc860",
  "sourceToolAssistantUUID": "9c5cfe70-1484-4c5f-89c8-8309740d9cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T07:44:28.711Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RLuNxExzEhi3MNs6bcLppQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/constraintllm2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dadda91c-7d73-405b-8492-84b3c84dc860",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1d49964a-4b72-4ee1-956d-157e7c609f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 14 · 2026-05-21T07:44:28.717Z_

<details><summary>↩ Tool result · `toolu_01RLuNxExzEhi3MNs6bcLppQ`</summary>

```text
1	paper_key: "constraintllm2025"
2	title: "ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming"
3	venue: "EMNLP 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["general-purpose LLMs on CP tasks"]
8	  metrics:
9	    - {name: "solving accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "IndusCP", size: "140 industrial-level tasks"}
12	    - {name: "existing CP benchmarks", size: "N/A"}
13	  ablation_dimensions: ["Constraint-Aware Retrieval Module", "Tree-of-Thoughts framework", "guided self-correction"]
14	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", info: "multi-instruction supervised fine-tuning on open-source LLM"}
15	  method_family: "neuro-symbolic constraint programming"
16	
17	positioning:
18	  core_claim: "First LLM specifically designed for CP modeling, combining constraint-aware retrieval with Tree-of-Thoughts and self-correction to achieve 2x improvement over baselines on industrial-level CP tasks"
19	  key_results: "State-of-the-art solving accuracy across multiple benchmarks; 2x improvement over baselines on IndusCP"
20	  limitations: ["N/A"]
21	  relation_to_us: "complementary"
22	
23	narrative: "N/A"
24	figures: "N/A"
25	tables: "N/A"
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d49964a-4b72-4ee1-956d-157e7c609f7d",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "897eef72-41a7-4ef7-ba25-494f066f0b21",
  "sourceToolAssistantUUID": "1d49964a-4b72-4ee1-956d-157e7c609f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T07:44:29.140Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2aaCK2Ce6nMNNZhyniQg3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/llm_meets_cp2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "897eef72-41a7-4ef7-ba25-494f066f0b21",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1da8cf92-f7c2-47de-bdfc-58233cf46b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 16 · 2026-05-21T07:44:29.160Z_

<details><summary>↩ Tool result · `toolu_01Y2aaCK2Ce6nMNNZhyniQg3`</summary>

```text
1	paper_key: "llm_meets_cp2025"
2	title: "Large Language Model Meets Constraint Propagation"
3	venue: "IJCAI 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard LLM text generation", "original GenCP"]
8	  metrics:
9	    - {name: "constraint satisfaction rate", direction: "higher_better"}
10	    - {name: "generation feasibility", direction: "higher_better"}
11	    - {name: "LLM inference efficiency", direction: "higher_better"}
12	  datasets:
13	    - {name: "COLLIE benchmarks", size: "N/A"}
14	  ablation_dimensions: ["MLM integration for domain preview", "bidirectional vs unidirectional propagation"]
15	  training_recipe: {info: "no training; inference-time constraint satisfaction via Masked Language Models"}
16	  method_family: "constraint programming + language models"
17	
18	positioning:
19	  core_claim: "Formulating constrained text generation as a CSP and integrating Masked Language Models for bidirectional constraint propagation significantly improves generation quality under strict content constraints"
20	  key_results: "Significant improvement on COLLIE benchmarks; more efficient LLM inference usage for constrained generation"
21	  limitations: ["N/A"]
22	  relation_to_us: "complementary"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1da8cf92-f7c2-47de-bdfc-58233cf46b60",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "500e51d5-2c97-4e60-ab25-b1d6cb5a2fa1",
  "sourceToolAssistantUUID": "1da8cf92-f7c2-47de-bdfc-58233cf46b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T07:44:29.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X8nA7McBdtsci9JPk3sdyT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/satbench2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "500e51d5-2c97-4e60-ab25-b1d6cb5a2fa1",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "555de7a9-cb46-4665-82a9-2eea948b539c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 18 · 2026-05-21T07:44:29.368Z_

<details><summary>↩ Tool result · `toolu_01X8nA7McBdtsci9JPk3sdyT`</summary>

```text
1	paper_key: "satbench2025"
2	title: "SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas"
3	venue: "EMNLP 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["o4-mini", "other frontier LLMs"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "SATBench", size: "2100 puzzles with adjustable difficulty"}
12	  ablation_dimensions: ["number of clauses (difficulty)", "SAT vs UNSAT problems"]
13	  training_recipe: {info: "evaluation benchmark, no training; automated puzzle generation from SAT formulas + LLM translation"}
14	  method_family: "SAT-based reasoning benchmark"
15	
16	positioning:
17	  core_claim: "LLMs have systematic failures in search-based logical reasoning: even the strongest model (o4-mini) achieves only 65% on hard UNSAT problems (near 50% random baseline), exhibiting satisfiability bias, context inconsistency, and condition omission"
18	  key_results: "o4-mini: 65.0% on hard UNSAT (random baseline: 50%); systematic failures in satisfiability bias, context inconsistency, condition omission"
19	  limitations: ["N/A"]
20	  relation_to_us: "complementary"
21	
22	narrative: "N/A"
23	figures: "N/A"
24	tables: "N/A"
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "555de7a9-cb46-4665-82a9-2eea948b539c",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "26a96276-487a-495d-8584-130772a1d369",
  "sourceToolAssistantUUID": "555de7a9-cb46-4665-82a9-2eea948b539c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T07:44:29.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SgcmnA7AK81LnkgD4PzBSe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/logicagent2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26a96276-487a-495d-8584-130772a1d369",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7a213c07-6347-4eb8-b3fe-bc39e71589ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 20 · 2026-05-21T07:44:29.564Z_

<details><summary>↩ Tool result · `toolu_01SgcmnA7AK81LnkgD4PzBSe`</summary>

```text
1	paper_key: "logicagent2025"
2	title: "From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)"
3	venue: "ACL 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard CoT prompting", "other reasoning agents"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "RepublicQA", size: "N/A (college-level, Flesch-Kincaid Grade 11.94)"}
12	    - {name: "ProntoQA", size: "N/A"}
13	    - {name: "ProofWriter", size: "N/A"}
14	    - {name: "FOLIO", size: "N/A"}
15	    - {name: "ProverQA", size: "N/A"}
16	  ablation_dimensions: ["semiotic square components", "automated deduction vs reflective verification"]
17	  training_recipe: {info: "agent-based prompting framework, no training"}
18	  method_family: "multi-perspective reasoning agent"
19	
20	positioning:
21	  core_claim: "Semiotic-square-guided multi-perspective reasoning jointly addresses logical and semantic complexity, achieving 6.25% improvement on RepublicQA and 7.05% on mainstream logic benchmarks"
22	  key_results: "+6.25% average on RepublicQA; +7.05% average on ProntoQA, ProofWriter, FOLIO, ProverQA"
23	  limitations: ["N/A"]
24	  relation_to_us: "competitor"
25	
26	narrative: "N/A"
27	figures: "N/A"
28	tables: "N/A"
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a213c07-6347-4eb8-b3fe-bc39e71589ee",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "93c65a05-a7a6-4bc7-9d41-1135f3e29bb5",
  "sourceToolAssistantUUID": "7a213c07-6347-4eb8-b3fe-bc39e71589ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T07:44:29.765Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S6LAfLTs1dvSxQzqMwqNeh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2026dylos.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93c65a05-a7a6-4bc7-9d41-1135f3e29bb5",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c5e5e1ef-5de2-4963-9ece-25719c65d89d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 22 · 2026-05-21T07:44:29.771Z_

<details><summary>↩ Tool result · `toolu_01S6LAfLTs1dvSxQzqMwqNeh`</summary>

```text
1	paper_key: "xu2026dylos"
2	title: "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)"
3	venue: "EACL 2026"
4	full_text_available: true
5	
6	research:
7	  baselines: ["Zero-shot", "CoT", "Logic-LM", "LINC", "SymbCoT", "Aristotle"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "routing_accuracy", direction: "higher_better"}
11	  datasets:
12	    - {name: "PrOntoQA", size: "500"}
13	    - {name: "ProofWriter", size: "600"}
14	    - {name: "FOLIO", size: "204"}
15	    - {name: "LogicalDeduction", size: "300"}
16	    - {name: "AR-LSAT", size: "230"}
17	  ablation_dimensions: ["solver_type", "routing_strategy", "model_scale", "LoRA_finetuning"]
18	  training_recipe: {optimizer: "LoRA", lr: "N/A", hardware: "N/A"}
19	  method_family: "LLM-symbolic hybrid with dynamic solver routing"
20	
21	positioning:
22	  core_claim: "Dynamic composition of multiple symbolic solvers (Pyke/Prover9/Z3/MiniZinc) via LLM-based routing achieves robust logical reasoning across heterogeneous problem types"
23	  key_results: "92.1% mixed reasoning (GPT-4o), +27% over zero-shot; 7B models: 8-26% baseline → 41-59.6% with LoRA"
24	  limitations:
25	    - "Model scale dependency — small models struggle with formalization"
26	    - "Formalization bottleneck: 60-80% of small-model errors from formalization"
27	    - "Limited solver coverage: no probabilistic/temporal/mathematical reasoning"
28	  relation_to_us: "competitor"
29	
30	narrative:
31	  story_type: "统一框架型"
32	  hook: "Material vs formal inference dichotomy — LLMs handle material, symbolic solvers handle formal, but no system integrates both dynamically"
33	  tension: "Existing hybrid methods are locked to a single solver type, failing on problems requiring different logical paradigms"
34	  key_insight: "Revealed in Section 3 — a router that classifies reasoning type enables dynamic solver dispatch with >98% accuracy"
35	  argument_chain: "heterogeneous logical tasks → single-solver limitation → classify-then-route → multi-solver composition → validated on mixed benchmarks"
36	  contribution_framing: "3 contributions each with quantitative evidence in the intro"
37	  intro_structure: "5 paragraphs: (1) material-formal dichotomy hook, (2) existing hybrid limitations, (3) DyLoS overview, (4) contributions with numbers, (5) paper structure"
38	  notable_technique: "Every contribution claim includes specific quantitative results; material-formal inference dichotomy used as recurring anchor"
39	
40	figures:
41	  figure_count: 5
42	  figure1:
43	    type: "method_overview"
44	    description: "3-stage pipeline: decompose → route → solve, showing 4 solver types"
45	    narrative_role: "Establishes the system architecture immediately after the problem statement"
46	    design_elements: ["flow diagram", "solver icons", "color-coded stages"]
47	    visual_style: "Left-to-right pipeline with branching at routing stage"
48	  result_figures:
49	    - figure_id: "Figure 3"
50	      viz_type: "bar_chart"
51	      what_compared: "Accuracy across datasets with different solvers"
52	      how_gain_highlighted: "DyLoS bar consistently highest"
53	      design_note: "Grouped by dataset, color by method"
54	  ablation_figures:
55	    - figure_id: "Figure 4"
56	      viz_type: "bar_chart"
57	      dimensions_varied: ["model_scale", "with/without_LoRA"]
58	      design_note: "Shows scaling behavior and LoRA impact"
59	  figure_narrative_role: "Fig1(architecture) → Fig2(routing) → Fig3(main results) → Fig4(scaling) → Fig5(error analysis)"
60	
61	tables:
62	  table_count: 4
63	  main_result_table:
64	    table_id: "Table 1"
65	    row_axis: "methods"
66	    col_axis: "datasets × accuracy"
67	    row_organization: "by_category"
68	    col_organization: "grouped_by_dataset"
69	    highlight_strategy: "bold_best"
70	    statistical_reporting: "single run"
71	    num_baselines: 6
72	    design_note: "Separates LLM-only vs hybrid methods"
73	  ablation_tables:
74	    - table_id: "Table 3"
75	      what_varied: ["solver_selection", "routing_strategy"]
76	      variation_style: "full_numbers"
77	      design_note: "Shows each solver's standalone vs combined performance"
78	  supplementary_tables:
79	    in_appendix: true
80	    content: "Prompt templates, additional model results"
81	    reason: "Space constraints"
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5e5e1ef-5de2-4963-9ece-25719c65d89d",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "aaf8c89c-bae6-45d3-bcb2-4d1c00453884",
  "sourceToolAssistantUUID": "c5e5e1ef-5de2-4963-9ece-25719c65d89d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T07:44:29.975Z_

<details open><summary>🔧 Tool call — Read · `toolu_016LgeEn8J1fa5wPHkMWfjRe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/aristotle2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaf8c89c-bae6-45d3-bcb2-4d1c00453884",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04fe1559-3a4b-40d1-8bba-ecfbbb1cd6fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 24 · 2026-05-21T07:44:29.981Z_

<details><summary>↩ Tool result · `toolu_016LgeEn8J1fa5wPHkMWfjRe`</summary>

```text
1	paper_key: "aristotle2025"
2	title: "Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework"
3	venue: "ACL 2025"
4	full_text_available: true
5	
6	research:
7	  baselines: ["CoT", "ToT", "CR", "SymbCoT", "Logic-LM", "LINC"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "one_step_inference_accuracy", direction: "higher_better"}
11	    - {name: "visited_nodes", direction: "lower_better"}
12	  datasets:
13	    - {name: "PrOntoQA", size: "500"}
14	    - {name: "ProofWriter", size: "600"}
15	    - {name: "FOLIO", size: "204"}
16	    - {name: "LogiQA", size: "651"}
17	  ablation_dimensions: ["CNF_decomposition", "search_strategy", "resolution_principle", "Prolog_translation"]
18	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
19	  method_family: "symbolic logic pipeline (Prolog + CNF + resolution)"
20	
21	positioning:
22	  core_claim: "A logic-complete framework integrating Prolog translation, CNF decomposition, and resolution principle into LLM reasoning achieves 99.7% one-step accuracy while reducing search by 52.6%"
23	  key_results: "+4.5% avg over SymbCoT (GPT-4), +5.4% (GPT-4o), +12.1% (Llama-3.1-405B); 99.7% one-step accuracy vs ToT's 74.0%"
24	  limitations:
25	    - "Requires all premises explicitly stated — fails on implicit knowledge (LogiQA: 31.2% vs CoT's 65.6%)"
26	    - "Computationally expensive multi-step search"
27	  relation_to_us: "competitor"
28	
29	narrative:
30	  story_type: "突破局限型"
31	  hook: "Figure 1 teaser showing accuracy gap — quantifies the problem before explaining the solution"
32	  tension: "Existing neurosymbolic methods suffer from incomplete logical operations, leading to error accumulation in multi-step proofs"
33	  key_insight: "Sec 3.2 — replacing LLM self-evaluation with deterministic resolution principle eliminates the weakest link in the reasoning chain"
34	  argument_chain: "multi-step errors → incomplete symbolic integration → full Prolog pipeline → deterministic search → validated accuracy + efficiency"
35	  contribution_framing: "3 contributions: framework, logic-completeness proof, empirical validation"
36	  intro_structure: "6 paragraphs: (1) LLM reasoning importance, (2) existing method failures with Figure 1, (3) root cause analysis, (4) Aristotle overview, (5) contributions, (6) paper structure"
37	  notable_technique: "Teaser result figure in intro paragraph 2 — immediately quantifies the gap before any method description"
38	
39	figures:
40	  figure_count: 8
41	  figure1:
42	    type: "teaser_result"
43	    description: "Bar chart comparing accuracy of existing methods showing performance gap"
44	    narrative_role: "Quantifies the problem in the intro before solution is described"
45	    design_elements: ["grouped bars", "accuracy numbers", "method labels"]
46	    visual_style: "Clean bar chart with clear performance gap visualization"
47	  result_figures:
48	    - figure_id: "Figure 4"
49	      viz_type: "scatter"
50	      what_compared: "Accuracy vs efficiency tradeoff across methods"
51	      how_gain_highlighted: "Aristotle in upper-left (high accuracy, low nodes)"
52	      design_note: "Dual-axis: accuracy vs search efficiency"
53	    - figure_id: "Figure 5"
54	      viz_type: "line_plot"
55	      what_compared: "Accuracy across reasoning depths"
56	      how_gain_highlighted: "Aristotle maintains accuracy at higher depths"
57	      design_note: "Shows robustness to depth"
58	  ablation_figures:
59	    - figure_id: "Figure 3"
60	      viz_type: "grouped_bar"
61	      dimensions_varied: ["CNF", "resolution", "search_strategy"]
62	      design_note: "Red gradient coloring for ablation variants"
63	  figure_narrative_role: "Fig1(teaser gap) → Fig2(method) → Fig3(ablation) → Fig4(efficiency) → Fig5(depth) → Fig6-7(case studies) → Fig8(error analysis)"
64	
65	tables:
66	  table_count: 4
67	  main_result_table:
68	    table_id: "Table 1"
69	    row_axis: "methods"
70	    col_axis: "datasets × accuracy"
71	    row_organization: "by_category"
72	    col_organization: "grouped_by_dataset"
73	    highlight_strategy: "bold_best + underline_second"
74	    statistical_reporting: "single run"
75	    num_baselines: 6
76	    design_note: "Categorizes methods into LLM-only, symbolic-augmented, and Aristotle"
77	  ablation_tables:
78	    - table_id: "Table 2"
79	      what_varied: ["CNF", "resolution", "Prolog_translation", "search"]
80	      variation_style: "checkmark_grid"
81	      design_note: "Systematic component removal showing each module's contribution"
82	  supplementary_tables:
83	    in_appendix: true
84	    content: "Extended results, additional models, case studies"
85	    reason: "Main paper focuses on core 4 datasets"
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04fe1559-3a4b-40d1-8bba-ecfbbb1cd6fe",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "5929bf82-0234-416e-a560-1952b73a8a8a",
  "sourceToolAssistantUUID": "04fe1559-3a4b-40d1-8bba-ecfbbb1cd6fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T07:44:30.396Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DDUQEHFLH4iaR2yjAXxfbj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/qi2025symbolic_provers.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5929bf82-0234-416e-a560-1952b73a8a8a",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "590752ad-20e8-4db4-a8f2-be98f8ea3837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 26 · 2026-05-21T07:44:30.404Z_

<details><summary>↩ Tool result · `toolu_01DDUQEHFLH4iaR2yjAXxfbj`</summary>

```text
1	paper_key: "qi2025symbolic_provers"
2	title: "Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation"
3	venue: "ICLR 2025"
4	full_text_available: true
5	
6	research:
7	  baselines: ["GPT-4o", "Claude-3.5-Sonnet", "Llama3.1-8B/70B", "Gemma2-9B/27B", "Mistral-7B/Large", "Qwen2.5-7B/32B/72B"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "ID_accuracy", direction: "higher_better"}
11	    - {name: "OOD_accuracy", direction: "higher_better"}
12	  datasets:
13	    - {name: "ProverQA", size: "1500 instances, 3 difficulty levels"}
14	    - {name: "ProofWriter", size: "for transfer eval"}
15	    - {name: "FOLIO", size: "for transfer eval"}
16	  ablation_dimensions: ["difficulty_level", "CoT_vs_direct", "finetuning_data_source", "ID_vs_OOD"]
17	  training_recipe: {optimizer: "SFT", lr: "N/A", hardware: "N/A"}
18	  method_family: "LLM + symbolic prover (Prover9) for benchmark generation"
19	
20	positioning:
21	  core_claim: "Top-down generation combining LLM diversity with Prover9 rigor creates ProverQA benchmark that reveals even SOTA models barely exceed chance on hard FOL problems"
22	  key_results: "GPT-4o: 50.0%, Claude-3.5: 56.4% on hard; finetuning Llama3.1-8B on ProverQA: +34.6% ID, +7.5% OOD (vs -2.0% ProofWriter, -11.4% FOLIO)"
23	  limitations:
24	    - "Benchmark limited to FOL reasoning"
25	    - "Top-down generation may not cover all reasoning patterns"
26	  relation_to_us: "foundation"
27	
28	narrative:
29	  story_type: "统一框架型"
30	  hook: "Existing benchmarks lack reliable ground truth labels and controllable difficulty"
31	  tension: "Bottom-up benchmark construction introduces label noise and uncontrolled complexity"
32	  key_insight: "Section 3 — top-down generation (goal → backward to premises) ensures logical coherence by construction"
33	  argument_chain: "benchmark limitations → top-down generation idea → Prover9 guarantees → difficulty control → model evaluation reveals gaps → finetuning transfer validates quality"
34	  contribution_framing: "3 contributions: generation framework, benchmark, comprehensive evaluation"
35	  intro_structure: "4 paragraphs: (1) importance of logical reasoning, (2) criteria for good benchmarks, (3) ProverGen framework, (4) contributions"
36	  notable_technique: "Table 1 checkmark grid as early positioning device — shows no existing benchmark meets all criteria"
37	
38	figures:
39	  figure_count: 2
40	  figure1:
41	    type: "method_overview"
42	    description: "ProverGen pipeline: top-down generation with Prover9"
43	    narrative_role: "Establishes the generation framework"
44	    design_elements: ["pipeline flow", "Prover9 integration point"]
45	    visual_style: "Schematic flow diagram"
46	  result_figures:
47	    - figure_id: "Figure 2"
48	      viz_type: "bar_chart"
49	      what_compared: "Model accuracy across difficulty levels"
50	      how_gain_highlighted: "Performance drop at higher difficulty"
51	      design_note: "Grouped by difficulty, showing model capability gap"
52	  ablation_figures: []
53	  figure_narrative_role: "Fig1(method) → Fig2(results) — minimal figures, table-heavy paper"
54	
55	tables:
56	  table_count: 6
57	  main_result_table:
58	    table_id: "Table 2"
59	    row_axis: "methods"
60	    col_axis: "difficulty levels × accuracy"
61	    row_organization: "by_category"
62	    col_organization: "grouped_by_difficulty"
63	    highlight_strategy: "bold_best"
64	    statistical_reporting: "single run"
65	    num_baselines: 10
66	    design_note: "Comprehensive model comparison across 3 difficulty levels"
67	  ablation_tables:
68	    - table_id: "Table 3"
69	      what_varied: ["finetuning_data_source", "ID_vs_OOD"]
70	      variation_style: "full_numbers"
71	      design_note: "Transfer learning comparison showing ProverQA's superiority"
72	  supplementary_tables:
73	    in_appendix: true
74	    content: "Additional model results, generation statistics"
75	    reason: "Main paper focuses on key comparisons"
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "590752ad-20e8-4db4-a8f2-be98f8ea3837",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "abf2772b-6b2c-4d8b-9151-71a41cda2df1",
  "sourceToolAssistantUUID": "590752ad-20e8-4db4-a8f2-be98f8ea3837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T07:44:30.609Z_

<details open><summary>🔧 Tool call — Read · `toolu_015fCGQc94ECnfdEkLgApZtj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dissecting2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abf2772b-6b2c-4d8b-9151-71a41cda2df1",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f4e558d0-46bf-4a59-bb4a-bfdc56c48294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 28 · 2026-05-21T07:44:30.614Z_

<details><summary>↩ Tool result · `toolu_015fCGQc94ECnfdEkLgApZtj`</summary>

```text
1	paper_key: "dissecting2025"
2	title: "Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation"
3	venue: "EMNLP Findings 2025"
4	full_text_available: true
5	
6	research:
7	  baselines: ["LLaMA-3.1-8B", "Gemma-2-9B", "Mistral-v0.3-7B", "CoT", "SFT-NL", "SFT-Symbolic"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "atomicity", direction: "higher_better"}
11	    - {name: "CSS", direction: "higher_better"}
12	    - {name: "NSD", direction: "higher_better"}
13	    - {name: "RFI", direction: "higher_better"}
14	  datasets:
15	    - {name: "FLD", size: "multi-depth"}
16	    - {name: "FOLIO", size: "204"}
17	    - {name: "ProntoQA", size: "500"}
18	  ablation_dimensions: ["supervision_type_NL_vs_symbolic", "reasoning_depth", "model_family"]
19	  training_recipe: {optimizer: "AdamW", lr: "1e-6", hardware: "4xA100, ~2h per model"}
20	  method_family: "evaluation framework (accuracy + soundness + probing)"
21	
22	positioning:
23	  core_claim: "Three-dimensional evaluation (accuracy + stepwise soundness + representation probing) reveals NL supervision generalizes better but symbolic supervision produces more structurally sound reasoning chains"
24	  key_results: "SFT-NL: 67.5% on FLD (from 31.7%); symbolic has higher atomicity (24.7% vs 13.0%); probing shows SFT improves generation but not internalized understanding"
25	  limitations:
26	    - "Limited to propositional/FOL reasoning"
27	    - "Probing only captures linear representations"
28	  relation_to_us: "foundation"
29	
30	narrative:
31	  story_type: "化繁为简型"
32	  hook: "LLMs show improved reasoning but we lack tools to understand what exactly improves"
33	  tension: "Single-metric evaluation (accuracy) masks critical differences in reasoning quality"
34	  key_insight: "Section 4 — decomposing evaluation into accuracy/soundness/probing reveals a fundamental NL-vs-symbolic tradeoff"
35	  argument_chain: "opaque evaluation → 3-dimensional framework → NL vs symbolic comparison → surprising probing results → implications for training design"
36	  contribution_framing: "3 contributions: evaluation framework, NL-vs-symbolic findings, probing insights"
37	  intro_structure: "5 paragraphs: (1) LLM reasoning progress, (2) evaluation limitations, (3) proposed framework, (4) key findings preview, (5) paper structure"
38	  notable_technique: "Previewing surprising findings in intro to create anticipation for the full analysis"
39	
40	figures:
41	  figure_count: 5
42	  figure1:
43	    type: "method_overview"
44	    description: "Three-dimensional evaluation framework: accuracy, soundness, probing"
45	    narrative_role: "Establishes the evaluation methodology upfront"
46	    design_elements: ["three parallel tracks", "metric labels", "color coding"]
47	    visual_style: "Schematic diagram with three evaluation dimensions"
48	  result_figures:
49	    - figure_id: "Figure 3"
50	      viz_type: "line_plot"
51	      what_compared: "Accuracy across reasoning depths for NL vs symbolic supervision"
52	      how_gain_highlighted: "Symbolic degrades more gracefully at higher depths"
53	      design_note: "Depth-accuracy curves are the strongest evidence"
54	    - figure_id: "Figure 4"
55	      viz_type: "heatmap"
56	      what_compared: "Probing results (CSS, NSD, RFI) across models and training types"
57	      how_gain_highlighted: "Color intensity shows where SFT helps vs doesn't"
58	      design_note: "Compact visualization of multi-dimensional probing results"
59	  ablation_figures:
60	    - figure_id: "Figure 5"
61	      viz_type: "bar_chart"
62	      dimensions_varied: ["model_family", "supervision_type"]
63	      design_note: "Cross-model consistency check"
64	  figure_narrative_role: "Fig1(framework) → Fig2(accuracy overview) → Fig3(depth analysis) → Fig4(probing) → Fig5(cross-model)"
65	
66	tables:
67	  table_count: 5
68	  main_result_table:
69	    table_id: "Table 1"
70	    row_axis: "methods"
71	    col_axis: "datasets × metrics (accuracy + soundness)"
72	    row_organization: "by_category"
73	    col_organization: "grouped_by_dataset"
74	    highlight_strategy: "bold_best"
75	    statistical_reporting: "single run"
76	    num_baselines: 6
77	    design_note: "Dual-metric reporting (accuracy and soundness side-by-side)"
78	  ablation_tables:
79	    - table_id: "Table 3"
80	      what_varied: ["supervision_type", "reasoning_depth"]
81	      variation_style: "full_numbers"
82	      design_note: "Depth-stratified comparison"
83	  supplementary_tables:
84	    in_appendix: true
85	    content: "Full probing results, additional model comparisons"
86	    reason: "Probing methodology details too extensive for main text"
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4e558d0-46bf-4a59-bb4a-bfdc56c48294",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "ca0e77a9-36b7-4dfd-9b28-d9dcd7c0ee3f",
  "sourceToolAssistantUUID": "f4e558d0-46bf-4a59-bb4a-bfdc56c48294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T07:44:30.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KMZw93wUbUh45bMSjLiYBQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/crest2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca0e77a9-36b7-4dfd-9b28-d9dcd7c0ee3f",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57cf98c4-1710-433a-bd15-c3857d13e6af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 30 · 2026-05-21T07:44:30.834Z_

<details><summary>↩ Tool result · `toolu_01KMZw93wUbUh45bMSjLiYBQ`</summary>

```text
1	paper_key: "crest2025"
2	title: "Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)"
3	venue: "NAACL 2025"
4	full_text_available: true
5	
6	research:
7	  baselines: ["SFT", "RFT", "STaR", "REST-EM", "V-STaR", "DPO-vanilla"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "ReClor", size: "~6k"}
12	    - {name: "ARC-Challenge", size: "2590"}
13	    - {name: "CSQA", size: "~12k"}
14	  ablation_dimensions: ["follow_up_questions", "tolerance_parameter_t", "DPO_lambda", "sample_count_N"]
15	  training_recipe: {optimizer: "AdamW", lr: "5e-6", hardware: "4xA100"}
16	  method_family: "consistency-driven self-training"
17	
18	positioning:
19	  core_claim: "Follow-up question consistency provides richer signal than binary answer correctness for filtering self-training rationales, enabling better SFT+DPO training"
20	  key_results: "+1.7-1.8% over best baseline on ReClor; consistent gains on ARC-C and CSQA across Llama-3-8B, Gemma-7B, Phi-2"
21	  limitations:
22	    - "Restricted to MCQ format"
23	    - "All follow-up questions weighted equally"
24	    - "No teacher-student setting explored"
25	  relation_to_us: "foundation"
26	
27	narrative:
28	  story_type: "突破局限型"
29	  hook: "Self-training with LLM-generated rationales is promising but suffers from false positive rationales"
30	  tension: "Binary correctness filtering passes rationales with right answers but wrong reasoning"
31	  key_insight: "Section 3.2 — follow-up questions stress-test rationale quality beyond just checking the final answer"
32	  argument_chain: "self-training promise → false positive problem → follow-up question consistency → filtered SFT + DPO → multi-model validation"
33	  contribution_framing: "3 contributions: consistency evaluation method, 4-stage training pipeline, empirical validation"
34	  intro_structure: "4 paragraphs: (1) self-training promise, (2) false positive problem, (3) CREST solution, (4) contributions"
35	  notable_technique: "Concrete example of a false positive rationale in intro to make the problem viscerally clear"
36	
37	figures:
38	  figure_count: 4
39	  figure1:
40	    type: "problem_illustration"
41	    description: "Example showing a rationale that gets the right answer through wrong reasoning, and how follow-up questions expose it"
42	    narrative_role: "Makes the false positive problem concrete and motivates the solution"
43	    design_elements: ["correct vs incorrect rationale comparison", "follow-up question examples", "red/green highlighting"]
44	    visual_style: "Two-column comparison with text examples"
45	  result_figures:
46	    - figure_id: "Figure 3"
47	      viz_type: "bar_chart"
48	      what_compared: "Methods across 3 datasets × 3 models"
49	      how_gain_highlighted: "CREST consistently highest or tied"
50	      design_note: "3×3 grid layout for comprehensive comparison"
51	  ablation_figures:
52	    - figure_id: "Figure 4"
53	      viz_type: "line_plot"
54	      dimensions_varied: ["tolerance_t", "DPO_lambda", "sample_N"]
55	      design_note: "Sensitivity analysis with clear optimal ranges"
56	  figure_narrative_role: "Fig1(problem example) → Fig2(method pipeline) → Fig3(main results) → Fig4(sensitivity)"
57	
58	tables:
59	  table_count: 4
60	  main_result_table:
61	    table_id: "Table 1"
62	    row_axis: "methods"
63	    col_axis: "datasets × models"
64	    row_organization: "by_category"
65	    col_organization: "grouped_by_dataset"
66	    highlight_strategy: "bold_best + underline_second"
67	    statistical_reporting: "mean across 3 seeds"
68	    num_baselines: 6
69	    design_note: "Separate sections for each model family"
70	  ablation_tables:
71	    - table_id: "Table 2"
72	      what_varied: ["follow_up_questions", "SFT_only_vs_SFT+DPO"]
73	      variation_style: "full_numbers"
74	      design_note: "Isolates contribution of each pipeline stage"
75	  supplementary_tables:
76	    in_appendix: true
77	    content: "Additional ablations, prompt templates, follow-up question examples"
78	    reason: "Main text focuses on core comparisons"
79	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57cf98c4-1710-433a-bd15-c3857d13e6af",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "9d48a5e8-c54e-4aae-8a1e-1ea18ca50f65",
  "sourceToolAssistantUUID": "57cf98c4-1710-433a-bd15-c3857d13e6af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T07:44:31.097Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q5kXZGVoEb3T64qCjEUhSK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/khan2024debating.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d48a5e8-c54e-4aae-8a1e-1ea18ca50f65",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e773996-9c5b-4f66-93d4-a59b9eb31f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 32 · 2026-05-21T07:44:31.106Z_

<details><summary>↩ Tool result · `toolu_01Q5kXZGVoEb3T64qCjEUhSK`</summary>

```text
1	paper_key: "khan2024debating"
2	title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
3	venue: "ICML 2024"
4	full_text_available: true
5	
6	research:
7	  baselines: ["Naive judge", "Consultancy (correct)", "Consultancy (incorrect)", "Non-interactive debate"]
8	  metrics:
9	    - {name: "judge_accuracy", direction: "higher_better"}
10	    - {name: "Elo_rating", direction: "higher_better"}
11	  datasets:
12	    - {name: "QuALITY", size: "reading comprehension"}
13	  ablation_dimensions: ["protocol_type", "interactivity", "debater_model", "judge_model", "BoN_size", "quote_system", "round_count", "word_limits", "majority_voting", "few_shot_count", "finetuning_data_type", "human_vs_LLM_judges", "persuasiveness_optimization"]
14	  training_recipe: {optimizer: "BoN + RL", lr: "N/A", hardware: "N/A"}
15	  method_family: "multi-agent debate for AI safety"
16	
17	positioning:
18	  core_claim: "Adversarial debate between LLM experts with persuasiveness optimization lets weaker judges identify truth better than non-adversarial consultancy"
19	  key_results: "Debate: 88% human / 76% LLM accuracy vs Consultancy: 78%/54% vs Naive: 60%/48%"
20	  limitations:
21	    - "Information asymmetry only (not reasoning gap)"
22	    - "RLHF-honest models only"
23	    - "Quote verification dependency"
24	    - "Single dataset (QuALITY)"
25	  relation_to_us: "complementary"
26	
27	narrative:
28	  story_type: "突破局限型"
29	  hook: "Scalable oversight — how do we verify AI behavior when it exceeds human capability?"
30	  tension: "Alignment techniques depend on human labels, but humans can't label superhuman behavior"
31	  key_insight: "Figures 3-4 mirror pair — persuasiveness helps debate (correct debater gains advantage) but hurts consultancy (incorrect consultant becomes more persuasive)"
32	  argument_chain: "alignment crisis → debate as theoretical solution → empirical setup with LLM proxy → 9 cumulative insights → persuasiveness as unsupervised training signal"
33	  contribution_framing: "Framed as 'insights' rather than 'contributions' — 9 numbered insights for cumulative evidence"
34	  intro_structure: "5 paragraphs: (1) scalable oversight problem, (2) debate proposal recap, (3) experimental approach, (4) key findings preview, (5) implications"
35	  notable_technique: "Numbered Insight 1-9 structure replaces traditional contribution list; Figure 3-4 mirror design as argumentative backbone"
36	
37	figures:
38	  figure_count: 17
39	  figure1:
40	    type: "method_overview"
41	    description: "Debate vs consultancy protocol comparison"
42	    narrative_role: "Establishes the two paradigms being compared"
43	    design_elements: ["side-by-side protocols", "agent roles", "information flow"]
44	    visual_style: "Schematic with two parallel protocol diagrams"
45	  result_figures:
46	    - figure_id: "Figure 2"
47	      viz_type: "bar_chart"
48	      what_compared: "Judge accuracy across protocols"
49	      how_gain_highlighted: "Debate consistently above consultancy"
50	      design_note: "Clear protocol comparison"
51	    - figure_id: "Figure 3"
52	      viz_type: "line_plot"
53	      what_compared: "Elo rating vs persuasiveness optimization for debate"
54	      how_gain_highlighted: "Correct-answer Elo grows with optimization"
55	      design_note: "Mirror pair with Figure 4 — debate's mechanism"
56	    - figure_id: "Figure 4"
57	      viz_type: "line_plot"
58	      what_compared: "Elo rating vs persuasiveness optimization for consultancy"
59	      how_gain_highlighted: "Incorrect consultant Elo grows — consultancy breaks"
60	      design_note: "Mirror with Fig3 showing opposite effect"
61	  ablation_figures:
62	    - figure_id: "Figures 5-17"
63	      viz_type: "mixed"
64	      dimensions_varied: ["13 ablation dimensions"]
65	      design_note: "Massive ablation suite — all visual, no tables"
66	  figure_narrative_role: "Fig1(protocol) → Fig2(main result) → Fig3-4(mechanism mirror) → Fig5-17(extensive ablations) — remarkably figure-heavy, only 1 table"
67	
68	tables:
69	  table_count: 1
70	  main_result_table:
71	    table_id: "Table 1"
72	    row_axis: "definitions"
73	    col_axis: "N/A"
74	    row_organization: "flat"
75	    col_organization: "flat"
76	    highlight_strategy: "N/A"
77	    statistical_reporting: "N/A"
78	    num_baselines: 0
79	    design_note: "Definitional table only — all quantitative results are figures"
80	  ablation_tables: []
81	  supplementary_tables:
82	    in_appendix: true
83	    content: "Additional experimental details"
84	    reason: "All main results presented visually"
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e773996-9c5b-4f66-93d4-a59b9eb31f46",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "61c729da-7ee3-47b1-a550-d38ac7d7deca",
  "sourceToolAssistantUUID": "2e773996-9c5b-4f66-93d4-a59b9eb31f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T07:44:31.238Z_

<details open><summary>🔧 Tool call — Read · `toolu_011qAudD4hRTHJhPfftp8CLP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/olausson2023linc.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61c729da-7ee3-47b1-a550-d38ac7d7deca",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1bdae550-e704-4eaf-ab0e-96b9d51675a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 34 · 2026-05-21T07:44:31.245Z_

<details><summary>↩ Tool result · `toolu_011qAudD4hRTHJhPfftp8CLP`</summary>

```text
1	paper_key: "olausson2023linc"
2	title: "LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers"
3	venue: "EMNLP 2023"
4	full_text_available: true
5	
6	research:
7	  baselines: ["Naive (direct)", "Scratchpad (FOL gen + LLM judge)", "CoT"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "ProofWriter", size: "OOD split"}
12	    - {name: "FOLIO", size: "204"}
13	  ablation_dimensions: ["K_majority_vote", "model_type", "proof_depth"]
14	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
15	  method_family: "neurosymbolic (LLM → FOL → Prover9)"
16	
17	positioning:
18	  core_claim: "Two-stage LLM-to-FOL-to-Prover9 pipeline with majority vote achieves near-perfect accuracy on synthetic FOL tasks and maintains robustness across proof depths"
19	  key_results: "ProofWriter: StarCoder++ LINC 82.1% vs 37.8% best baseline; GPT-3.5 LINC 96.4%; GPT-4 LINC 98.3%. FOLIO: gains for smaller models, not significant for GPT-4"
20	  limitations:
21	    - "FOL is lossy for naturalistic language"
22	    - "Scalability unclear with more premises"
23	    - "FOL expressiveness insufficient for higher-order/non-classical logic"
24	  relation_to_us: "foundation"
25	
26	narrative:
27	  story_type: "跨界迁移型"
28	  hook: "LLMs struggle with multi-step deduction despite general language understanding"
29	  tension: "CoT provides reasoning steps but can't guarantee logical soundness"
30	  key_insight: "Section 3 — the Scratchpad baseline isolates the prover's contribution: generating FOL alone (without symbolic execution) doesn't help"
31	  argument_chain: "LLM deduction weakness → separate understanding from reasoning → LLM parses, prover reasons → Scratchpad control proves prover is key → depth analysis confirms robustness"
32	  contribution_framing: "2 contributions: LINC system, Scratchpad diagnostic baseline"
33	  intro_structure: "4 paragraphs: (1) LLM reasoning gap, (2) neurosymbolic opportunity, (3) LINC and Scratchpad, (4) key findings"
34	  notable_technique: "Scratchpad as diagnostic baseline — isolates the symbolic prover's causal contribution beyond just generating FOL"
35	
36	figures:
37	  figure_count: 5
38	  figure1:
39	    type: "method_overview"
40	    description: "LINC pipeline: NL → LLM → FOL → Prover9 → answer, with K-way majority vote"
41	    narrative_role: "Establishes the two-stage architecture"
42	    design_elements: ["pipeline flow", "LLM and Prover9 components", "majority vote aggregation"]
43	    visual_style: "Left-to-right pipeline diagram"
44	  result_figures:
45	    - figure_id: "Figure 3"
46	      viz_type: "bar_chart"
47	      what_compared: "Methods across models on ProofWriter and FOLIO"
48	      how_gain_highlighted: "LINC bars clearly above baselines"
49	      design_note: "Grouped by model, color by method"
50	    - figure_id: "Figure 4"
51	      viz_type: "line_plot"
52	      what_compared: "Accuracy across proof depths (0-5)"
53	      how_gain_highlighted: "LINC maintains near-perfect accuracy while baselines degrade"
54	      design_note: "Strongest evidence for robustness — depth-accuracy curves"
55	    - figure_id: "Figure 5"
56	      viz_type: "qualitative_comparison"
57	      what_compared: "Error types: LINC vs CoT"
58	      how_gain_highlighted: "Only 21/74 errors shared — methods are complementary"
59	      design_note: "Error analysis Venn diagram / taxonomy"
60	  ablation_figures: []
61	  figure_narrative_role: "Fig1(pipeline) → Fig2(FOL examples) → Fig3(main results bars) → Fig4(depth analysis) → Fig5(error analysis)"
62	
63	tables:
64	  table_count: 0
65	  main_result_table:
66	    table_id: "N/A"
67	    row_axis: "N/A"
68	    col_axis: "N/A"
69	    row_organization: "N/A"
70	    col_organization: "N/A"
71	    highlight_strategy: "N/A"
72	    statistical_reporting: "p-values for significance"
73	    num_baselines: 3
74	    design_note: "No tables — all results presented as bar charts and line plots. Unusual but effective given small experimental grid"
75	  ablation_tables: []
76	  supplementary_tables:
77	    in_appendix: true
78	    content: "Prompt templates, FOL examples, additional error analysis"
79	    reason: "Qualitative content doesn't fit tabular format"
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bdae550-e704-4eaf-ab0e-96b9d51675a5",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "43b863cd-a923-46d6-a755-d0bb0f544a90",
  "sourceToolAssistantUUID": "1bdae550-e704-4eaf-ab0e-96b9d51675a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T07:44:31.864Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WFwNNxucP3K3wYgqfgzrL1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/pan2023logiclm.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43b863cd-a923-46d6-a755-d0bb0f544a90",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c066126-f4ac-419c-b207-2703d6ef661d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 36 · 2026-05-21T07:44:31.876Z_

<details><summary>↩ Tool result · `toolu_01WFwNNxucP3K3wYgqfgzrL1`</summary>

```text
1	paper_key: "pan2023logiclm"
2	title: "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning"
3	venue: "EMNLP Findings 2023"
4	full_text_available: true
5	
6	research:
7	  baselines: ["Standard Prompting", "CoT", "CoT-SC"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "Exe_Rate", direction: "higher_better"}
11	  datasets:
12	    - {name: "PrOntoQA", size: "500"}
13	    - {name: "ProofWriter", size: "600"}
14	    - {name: "FOLIO", size: "204"}
15	    - {name: "LogicalDeduction", size: "300"}
16	    - {name: "AR-LSAT", size: "230"}
17	  ablation_dimensions: ["self_refinement", "solver_type", "model_type", "problem_type"]
18	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
19	  method_family: "LLM + symbolic solver (Pyke/Prover9/python-constraint/Z3)"
20	
21	positioning:
22	  core_claim: "Reframing LLM's role from 'solving' to 'representing' — LLM formulates problems symbolically, dedicated solvers execute reasoning, with self-refinement for invalid formulations"
23	  key_results: "+39.2% over standard prompting, +18.4% over CoT (GPT-3.5); GPT-4: PrOntoQA 83.2, ProofWriter 79.66, FOLIO 78.92, LogicalDeduction 87.63, AR-LSAT 43.04"
24	  limitations:
25	    - "Low Exe_Rate on complex problems (FOLIO 79.9%, AR-LSAT 32.6% with GPT-4)"
26	    - "Self-refinement fixes grammar but not semantics"
27	    - "Formalization bottleneck on naturalistic language"
28	  relation_to_us: "foundation"
29	
30	narrative:
31	  story_type: "跨界迁移型"
32	  hook: "LLMs can understand language but fail at rigorous logical reasoning"
33	  tension: "Prompting strategies improve reasoning but can't guarantee faithfulness"
34	  key_insight: "Section 3 — separating 'understanding' (LLM) from 'reasoning' (solver) plays to each component's strength"
35	  argument_chain: "LLM reasoning unfaithful → separate understanding from reasoning → LLM formulates + solver executes → self-refinement handles errors → 5-dataset validation"
36	  contribution_framing: "3 contributions: framework, self-refinement mechanism, comprehensive evaluation"
37	  intro_structure: "5 paragraphs: (1) LLM reasoning promise/limitations, (2) faithfulness problem, (3) Logic-LM framework, (4) contributions, (5) paper structure"
38	  notable_technique: "Reframing the LLM's role from 'solver' to 'translator' — rhetorically powerful simplification"
39	
40	figures:
41	  figure_count: 4
42	  figure1:
43	    type: "method_overview"
44	    description: "Logic-LM pipeline: Problem Formulation → Symbolic Reasoning → Result Interpretation, with self-refinement loop"
45	    narrative_role: "Establishes the three-stage architecture with refinement"
46	    design_elements: ["pipeline flow", "self-refinement loop arrow", "4 solver icons"]
47	    visual_style: "Flowchart with feedback loop"
48	  result_figures:
49	    - figure_id: "Figure 3"
50	      viz_type: "line_plot"
51	      what_compared: "Accuracy across reasoning depths"
52	      how_gain_highlighted: "Logic-LM advantage grows with depth (widening gap at depth-5)"
53	      design_note: "Depth analysis showing symbolic reasoning's advantage on harder problems"
54	  ablation_figures:
55	    - figure_id: "Figure 4"
56	      viz_type: "bar_chart"
57	      dimensions_varied: ["with/without self-refinement", "solver_type"]
58	      design_note: "Isolates self-refinement contribution"
59	  figure_narrative_role: "Fig1(pipeline) → Fig2(example) → Fig3(depth analysis) → Fig4(ablation)"
60	
61	tables:
62	  table_count: 4
63	  main_result_table:
64	    table_id: "Table 1"
65	    row_axis: "methods"
66	    col_axis: "datasets × accuracy"
67	    row_organization: "by_category"
68	    col_organization: "grouped_by_dataset"
69	    highlight_strategy: "bold_best"
70	    statistical_reporting: "single run"
71	    num_baselines: 3
72	    design_note: "Clean comparison with Exe_Rate reported alongside accuracy"
73	  ablation_tables:
74	    - table_id: "Table 2"
75	      what_varied: ["self_refinement", "error_type"]
76	      variation_style: "full_numbers"
77	      design_note: "Breaks down Exe_Rate improvement by error category"
78	  supplementary_tables:
79	    in_appendix: true
80	    content: "Prompt templates, solver-specific results, error examples"
81	    reason: "Detailed error analysis too long for main text"
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c066126-f4ac-419c-b207-2703d6ef661d",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "df63673b-d8d0-4066-8148-835010d84b41",
  "sourceToolAssistantUUID": "8c066126-f4ac-419c-b207-2703d6ef661d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T07:44:31.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_013PEYd1p5cB4v4hUgZXyFLZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/snell2025scaling_tts.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df63673b-d8d0-4066-8148-835010d84b41",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "998a0bf5-99ff-4159-90b1-7c8ffba27ab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 38 · 2026-05-21T07:44:31.893Z_

<details><summary>↩ Tool result · `toolu_013PEYd1p5cB4v4hUgZXyFLZ`</summary>

```text
1	paper_key: "snell2025scaling_tts"
2	title: "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters"
3	venue: "ICLR 2025 (Oral)"
4	full_text_available: false
5	
6	research:
7	  baselines: ["greedy decoding", "majority voting", "best-of-N", "reward-model reranking"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "compute_efficiency", direction: "higher_better"}
11	  datasets:
12	    - {name: "MATH", size: "500"}
13	    - {name: "GSM8K", size: "1319"}
14	  ablation_dimensions: ["compute_budget", "search_strategy", "verifier_type", "model_scale"]
15	  training_recipe: {info: "process reward models for verification"}
16	  method_family: "test-time compute scaling"
17	
18	positioning:
19	  core_claim: "Optimal allocation of test-time compute (search + verification) can match or exceed 14x larger models"
20	  key_results: "Smaller model + optimal test-time compute matches 14x larger model on MATH"
21	  limitations: ["N/A"]
22	  relation_to_us: "foundation"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "998a0bf5-99ff-4159-90b1-7c8ffba27ab5",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "5f747bbb-201d-46fc-9842-08ceaf5d937e",
  "sourceToolAssistantUUID": "998a0bf5-99ff-4159-90b1-7c8ffba27ab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T07:44:32.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HR6zm56FCyACnnNnetsLxE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/multi_path_plan2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f747bbb-201d-46fc-9842-08ceaf5d937e",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fb311b5-376f-462a-8e58-029e14ca2848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 40 · 2026-05-21T07:44:32.086Z_

<details><summary>↩ Tool result · `toolu_01HR6zm56FCyACnnNnetsLxE`</summary>

```text
1	paper_key: "multi_path_plan2025"
2	title: "Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation"
3	venue: "arXiv 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["CoT", "SC-CoT", "ToT", "plan-then-solve"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "GSM8K", size: "1319"}
12	    - {name: "MATH", size: "500"}
13	    - {name: "ARC-Challenge", size: "2590"}
14	  ablation_dimensions: ["num_paths", "aggregation_strategy", "plan_granularity"]
15	  training_recipe: {info: "N/A"}
16	  method_family: "multi-path reasoning aggregation"
17	
18	positioning:
19	  core_claim: "Aggregating multiple reasoning plans before execution improves long chain-of-thought reasoning"
20	  key_results: "N/A"
21	  limitations: ["N/A"]
22	  relation_to_us: "complementary"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fb311b5-376f-462a-8e58-029e14ca2848",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "5db9db97-22f8-4957-ab06-8378bbe8fd84",
  "sourceToolAssistantUUID": "6fb311b5-376f-462a-8e58-029e14ca2848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T07:44:32.292Z_

<details open><summary>🔧 Tool call — Read · `toolu_011UJUUEsVPEqXGP1U95VN4z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2024mathshepherd.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5db9db97-22f8-4957-ab06-8378bbe8fd84",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60013c7a-0c0f-4d1a-b440-95b01c320b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 42 · 2026-05-21T07:44:32.306Z_

<details><summary>↩ Tool result · `toolu_011UJUUEsVPEqXGP1U95VN4z`</summary>

```text
1	paper_key: "wang2024mathshepherd"
2	title: "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations"
3	venue: "ACL 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["majority voting", "ORM (outcome reward model)", "PRM (process reward model)"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "GSM8K", size: "1319"}
12	    - {name: "MATH", size: "500"}
13	  ablation_dimensions: ["verification_granularity", "reward_model_size", "num_samples"]
14	  training_recipe: {info: "automated step-level annotation via completion-based verification"}
15	  method_family: "process reward model / step-level verification"
16	
17	positioning:
18	  core_claim: "Automated step-level verification annotations (without human labels) enable process reward models that outperform outcome-only verification"
19	  key_results: "GSM8K: 84.1% → 93.4% with Math-Shepherd PRM verification"
20	  limitations: ["N/A"]
21	  relation_to_us: "complementary"
22	
23	narrative: "N/A"
24	figures: "N/A"
25	tables: "N/A"
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60013c7a-0c0f-4d1a-b440-95b01c320b63",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "3c87cecb-867d-4f03-ad0e-f666c4a31b9f",
  "sourceToolAssistantUUID": "60013c7a-0c0f-4d1a-b440-95b01c320b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T07:44:32.753Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XHS2epgFuNHtA1CZwaqLug`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/hosseini2024vstar.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c87cecb-867d-4f03-ad0e-f666c4a31b9f",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92f84ddb-643a-42c2-9bf0-1e4aa44e20fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 44 · 2026-05-21T07:44:32.758Z_

<details><summary>↩ Tool result · `toolu_01XHS2epgFuNHtA1CZwaqLug`</summary>

```text
1	paper_key: "hosseini2024vstar"
2	title: "V-STaR: Training Verifiers for Self-Taught Reasoners"
3	venue: "NeurIPS 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["STaR", "REST-EM", "majority_voting", "ORM"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "GSM8K", size: "1319"}
12	    - {name: "MATH", size: "500"}
13	    - {name: "ARC-Challenge", size: "2590"}
14	  ablation_dimensions: ["verifier_training_data", "iteration_count", "generator_vs_verifier_scaling"]
15	  training_recipe: {info: "iterative self-training with DPO verifier"}
16	  method_family: "self-training with verifier"
17	
18	positioning:
19	  core_claim: "Training verifiers on both correct and incorrect solutions from self-taught reasoners creates a virtuous cycle improving both generator and verifier"
20	  key_results: "GSM8K: +4.7% over STaR; MATH: +2.1% over STaR with verification"
21	  limitations: ["N/A"]
22	  relation_to_us: "competitor"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92f84ddb-643a-42c2-9bf0-1e4aa44e20fd",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "6dac8cec-c9b8-4e4b-96e9-bcfaf7329d97",
  "sourceToolAssistantUUID": "92f84ddb-643a-42c2-9bf0-1e4aa44e20fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T07:44:32.923Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W5yrf8Cst994bV2PmnsTPE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/huang2024selfcorrect.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dac8cec-c9b8-4e4b-96e9-bcfaf7329d97",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1337345b-8fd3-4f7a-90e1-66a4437db74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 46 · 2026-05-21T07:44:32.928Z_

<details><summary>↩ Tool result · `toolu_01W5yrf8Cst994bV2PmnsTPE`</summary>

```text
1	paper_key: "huang2024selfcorrect"
2	title: "Large Language Models Cannot Self-Correct Reasoning Yet"
3	venue: "ICLR 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard prompting", "CoT", "self-refine", "multi-agent debate"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "GSM8K", size: "1319"}
12	    - {name: "CommonSenseQA", size: "1221"}
13	    - {name: "HotpotQA", size: "multi-hop"}
14	  ablation_dimensions: ["feedback_type", "oracle_vs_intrinsic", "iteration_count"]
15	  training_recipe: {info: "N/A — prompting-based study"}
16	  method_family: "self-correction analysis"
17	
18	positioning:
19	  core_claim: "LLMs cannot self-correct reasoning without external feedback; intrinsic self-correction often degrades performance"
20	  key_results: "Self-correction without oracle feedback consistently hurts accuracy (GSM8K: -2.4%)"
21	  limitations: ["N/A"]
22	  relation_to_us: "foundation"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1337345b-8fd3-4f7a-90e1-66a4437db74e",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "4e9257b6-8a60-4d0b-9c87-1513f943baa8",
  "sourceToolAssistantUUID": "1337345b-8fd3-4f7a-90e1-66a4437db74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T07:44:33.134Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AJGsVRJXoUg9AfQuj9HEqH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2023sc.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e9257b6-8a60-4d0b-9c87-1513f943baa8",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0f877c47-4df1-465e-bda6-59f3d9faa7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 48 · 2026-05-21T07:44:33.141Z_

<details><summary>↩ Tool result · `toolu_01AJGsVRJXoUg9AfQuj9HEqH`</summary>

```text
1	paper_key: "wang2023sc"
2	title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
3	venue: "ICLR 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["greedy CoT", "sample-and-rank", "beam search"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "GSM8K", size: "1319"}
12	    - {name: "SVAMP", size: "1000"}
13	    - {name: "AQuA", size: "254"}
14	    - {name: "StrategyQA", size: "2290"}
15	    - {name: "ARC-Challenge", size: "2590"}
16	  ablation_dimensions: ["num_samples", "temperature", "model_scale"]
17	  training_recipe: {info: "N/A — decoding strategy"}
18	  method_family: "self-consistency / majority voting"
19	
20	positioning:
21	  core_claim: "Sampling multiple reasoning paths and marginalizing over them via majority voting substantially improves CoT accuracy without any training"
22	  key_results: "GSM8K: +17.9% over greedy CoT with 40 samples (PaLM-540B)"
23	  limitations: ["N/A"]
24	  relation_to_us: "foundation"
25	
26	narrative: "N/A"
27	figures: "N/A"
28	tables: "N/A"
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f877c47-4df1-465e-bda6-59f3d9faa7e3",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "fd992d81-c601-4a74-bd9b-c9442630887d",
  "sourceToolAssistantUUID": "0f877c47-4df1-465e-bda6-59f3d9faa7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T07:44:33.344Z_

<details open><summary>🔧 Tool call — Read · `toolu_012RRRjFE5GitDzupLbWciye`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/li2023diverse.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd992d81-c601-4a74-bd9b-c9442630887d",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a398ca0-e09f-4aa2-8a16-7919262eee04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 50 · 2026-05-21T07:44:33.349Z_

<details><summary>↩ Tool result · `toolu_012RRRjFE5GitDzupLbWciye`</summary>

```text
1	paper_key: "li2023diverse"
2	title: "Making Language Models Better Reasoners with Step-Aware Verifier"
3	venue: "ACL 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["CoT", "SC-CoT", "voting_verifier"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "GSM8K", size: "1319"}
12	    - {name: "MATH", size: "500"}
13	  ablation_dimensions: ["verifier_granularity", "diverse_prompts", "sample_count"]
14	  training_recipe: {info: "step-aware verifier training"}
15	  method_family: "diverse prompting + step-aware verification"
16	
17	positioning:
18	  core_claim: "Combining diverse prompting strategies with step-level verification outperforms simple self-consistency"
19	  key_results: "GSM8K: +3.2% over SC-CoT with step-aware verifier"
20	  limitations: ["N/A"]
21	  relation_to_us: "competitor"
22	
23	narrative: "N/A"
24	figures: "N/A"
25	tables: "N/A"
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a398ca0-e09f-4aa2-8a16-7919262eee04",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "652b2c42-39e3-4727-b1b8-86b0be4215bd",
  "sourceToolAssistantUUID": "9a398ca0-e09f-4aa2-8a16-7919262eee04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T07:44:33.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Drqs7m7hBi5sifG7tkrYeF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/rc2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "652b2c42-39e3-4727-b1b8-86b0be4215bd",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b3090933-12b7-495b-9933-de41080623ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 52 · 2026-05-21T07:44:33.560Z_

<details><summary>↩ Tool result · `toolu_01Drqs7m7hBi5sifG7tkrYeF`</summary>

```text
1	paper_key: "rc2025"
2	title: "Representation Consistency for Accurate and Coherent LLM Answer Aggregation"
3	venue: "arXiv 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["majority_voting", "USC", "weighted_voting"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "coherence", direction: "higher_better"}
11	  datasets:
12	    - {name: "GSM8K", size: "1319"}
13	    - {name: "TriviaQA", size: "open-domain"}
14	    - {name: "MMLU", size: "multi-task"}
15	  ablation_dimensions: ["representation_type", "aggregation_method", "sample_count"]
16	  training_recipe: {info: "N/A — aggregation method"}
17	  method_family: "representation-based answer aggregation"
18	
19	positioning:
20	  core_claim: "Aggregating answers based on representation consistency (semantic similarity) outperforms surface-form majority voting for open-ended generation"
21	  key_results: "N/A"
22	  limitations: ["N/A"]
23	  relation_to_us: "competitor"
24	
25	narrative: "N/A"
26	figures: "N/A"
27	tables: "N/A"
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3090933-12b7-495b-9933-de41080623ca",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "e7198005-0d31-486a-8d87-dca04c75edfa",
  "sourceToolAssistantUUID": "b3090933-12b7-495b-9933-de41080623ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T07:44:33.966Z_

<details open><summary>🔧 Tool call — Read · `toolu_019hkHZjqbpNbKcZj4vHD7Yi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/ye2024satlm.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7198005-0d31-486a-8d87-dca04c75edfa",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0bf265bc-7c95-430f-9ed5-b831f78936ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 54 · 2026-05-21T07:44:33.972Z_

<details><summary>↩ Tool result · `toolu_019hkHZjqbpNbKcZj4vHD7Yi`</summary>

```text
1	paper_key: "ye2024satlm"
2	title: "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting"
3	venue: "NeurIPS 2023"
4	full_text_available: true
5	
6	research:
7	  baselines: ["Standard Prompting", "CoT", "ProgLM"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "selective_accuracy", direction: "higher_better"}
11	  datasets:
12	    - {name: "GSM", size: "1319"}
13	    - {name: "GSM-Sys", size: "subset"}
14	    - {name: "ALGEBRA", size: "textbook problems"}
15	    - {name: "LSAT", size: "230"}
16	    - {name: "BoardgameQA", size: "depth 1-3"}
17	    - {name: "CLUTRR", size: "kinship reasoning"}
18	    - {name: "ProofWriter", size: "depth-5"}
19	    - {name: "COLOR", size: "BIG-bench"}
20	    - {name: "REGEX", size: "StRegex"}
21	  ablation_dimensions: ["solver_type (SAT vs CoT vs None)", "declarative_vs_imperative", "exemplar_sensitivity", "model_generalization"]
22	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "code-davinci-002, gpt-3.5-turbo, text-davinci-003"}
23	  method_family: "declarative prompting + SAT/SMT solver (Z3)"
24	
25	positioning:
26	  core_claim: "Shifting LLMs from generating imperative programs to declarative specifications enables SAT solvers to handle both planning and execution, eliminating planning errors that plague program-aided LMs"
27	  key_results: "GSM-Sys: 69.4% (+23% over ProgLM); LSAT SoTA 37.4% (from 30.9%); BoardgameQA SoTA 80.7% (from 73.9%); GSM SC: 84.8% matching full-training-set models"
28	  limitations:
29	    - "Some problems naturally suit imperative procedures (SatLM slightly lags ProgLM on GSM greedy)"
30	    - "SAT solver expressiveness limited for quantifiers and nonlinear arithmetic"
31	    - "One-round parse-solve; no iterative refinement based on solver feedback"
32	  relation_to_us: "foundation"
33	
34	narrative:
35	  story_type: "突破局限型"
36	  hook: "CoT prompting falls short on problems requiring sophisticated planning and search"
37	  tension: "Program-aided LMs fix execution errors but not planning errors — LLM must both plan and execute in imperative paradigm"
38	  key_insight: "Section 2, paragraph 3 — 'Our work tackles both execution errors and, more importantly, planning errors' by shifting to declarative specifications where the solver handles both planning and execution"
39	  argument_chain: "CoT fails at planning → imperative programs still require LLM planning → declarative specs offload both planning+execution to solver → solver guarantees correctness → 8-dataset validation across 4 task types"
40	  contribution_framing: "2 key advantages framed as properties: (1) declarative spec closer to problem description, (2) solver guarantees correctness. Plus 3 analysis findings"
41	  intro_structure: "5 paragraphs: (1) CoT limitations for complex reasoning, (2) parse-plan-execute framework, (3) SatLM with declarative prompting, (4) results summary, (5) analysis findings"
42	  notable_technique: "The parse-plan-execute decomposition is reframed to show SatLM offloads 2/3 steps (plan+execute) while ProgLM only offloads 1/3 (execute) — powerful comparative framing"
43	
44	figures:
45	  figure_count: 4
46	  figure1:
47	    type: "problem_illustration"
48	    description: "Side-by-side comparison of CoT (imperative) vs SatLM (declarative) on a constraint satisfaction problem. Left shows LLM doing parse+plan+execute; right shows LLM only parsing into SAT specification, solver does the rest"
49	    narrative_role: "Immediately demonstrates the declarative vs imperative paradigm shift on a concrete LSAT-style problem"
50	    design_elements: ["side-by-side comparison", "code-style specification boxes", "color-coded errors in CoT", "SAT solver icon"]
51	    visual_style: "Two-column layout with input problem on top, showing the full reasoning trace (left) vs compact specification + solver (right). Green/red annotations mark correct/incorrect steps"
52	  result_figures:
53	    - figure_id: "Figure 2"
54	      viz_type: "qualitative_comparison"
55	      what_compared: "CoT vs ProgLM vs SatLM on arithmetic reasoning — showing specific errors"
56	      how_gain_highlighted: "Red annotations on errors in CoT and ProgLM; SatLM produces correct answer"
57	      design_note: "Concrete error examples make the planning-vs-execution distinction tangible"
58	    - figure_id: "Figure 3"
59	      viz_type: "qualitative_comparison"
60	      what_compared: "SatLM variant with CoT solver (declarative spec + LLM solving)"
61	      how_gain_highlighted: "Shows declarative prompting helps even without symbolic solver"
62	      design_note: "Isolates contribution of declarative formulation vs symbolic execution"
63	  ablation_figures: []
64	  figure_narrative_role: "Fig1(paradigm comparison) → Fig2(concrete error analysis) → Fig3(ablation variant) → Fig4(commonsense parsing examples)"
65	
66	tables:
67	  table_count: 7
68	  main_result_table:
69	    table_id: "Table 1"
70	    row_axis: "methods"
71	    col_axis: "datasets (GSM-Sys, GSM, ALGE, LSAT, BOARD, CLUTRR, PROOF, COLOR, REGEX)"
72	    row_organization: "by_category"
73	    col_organization: "grouped_by_dataset"
74	    highlight_strategy: "bold_best"
75	    statistical_reporting: "bootstrap significance tests (p<0.05)"
76	    num_baselines: 3
77	    design_note: "Split into greedy and self-consistency decoding blocks; 9 datasets is unusually comprehensive"
78	  ablation_tables:
79	    - table_id: "Table 2"
80	      what_varied: ["solver_type: SAT_SymSolver vs SAT_CoTSolver vs SAT_NoSolver"]
81	      variation_style: "full_numbers"
82	      design_note: "Isolates solver contribution — key insight that declarative prompting helps even without solver"
83	    - table_id: "Table 3"
84	      what_varied: ["error_type: planning vs execution"]
85	      variation_style: "full_numbers"
86	      design_note: "Error decomposition showing most CoTSolver errors are planning errors"
87	    - table_id: "Table 5"
88	      what_varied: ["selective prediction: correct, incorrect, error types (UNSAT, AMBIG)"]
89	      variation_style: "full_numbers"
90	      design_note: "Unique to SAT approach — solver feedback enables abstaining from uncertain predictions"
91	  supplementary_tables:
92	    in_appendix: true
93	    content: "Dataset statistics, prompts, exemplar variations (Table 7), cross-model results (Table 6)"
94	    reason: "Generalization analysis and prompt details too detailed for main text"
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bf265bc-7c95-430f-9ed5-b831f78936ff",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "46fc9e09-94d8-4861-b76b-3dd0773d6d1c",
  "sourceToolAssistantUUID": "0bf265bc-7c95-430f-9ed5-b831f78936ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T07:44:34.187Z_

<details open><summary>🔧 Tool call — Read · `toolu_0164DuswXKMhQHnZdRRJWHKM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2024symbcot.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46fc9e09-94d8-4861-b76b-3dd0773d6d1c",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f4375fd8-3024-4e41-a437-37b4537c6850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 56 · 2026-05-21T07:44:34.194Z_

<details><summary>↩ Tool result · `toolu_0164DuswXKMhQHnZdRRJWHKM`</summary>

```text
1	paper_key: "xu2024symbcot"
2	title: "Faithful Logical Reasoning via Symbolic Chain-of-Thought"
3	venue: "ACL 2024"
4	full_text_available: true
5	
6	research:
7	  baselines: ["Naive Prompting", "CoT", "CoT-SC", "ToT", "CR (Cumulative Reasoning)", "DetermLR", "Logic-LM"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "execution_rate", direction: "higher_better"}
11	    - {name: "faithfulness_rate", direction: "higher_better"}
12	  datasets:
13	    - {name: "PrOntoQA", size: "500"}
14	    - {name: "ProofWriter", size: "600"}
15	    - {name: "FOLIO", size: "204"}
16	    - {name: "LogicalDeduction", size: "300"}
17	    - {name: "AR-LSAT", size: "230"}
18	  ablation_dimensions: ["module_contribution (Translator/Planner/Solver/Verifier)", "symbolic_structure (FOL vs CO)", "model_type (GPT-3.5 vs GPT-4)", "reasoning_depth"]
19	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "GPT-3.5-turbo-0613, GPT-4-0613"}
20	  method_family: "fully LLM-based symbolic CoT (no external solver)"
21	
22	positioning:
23	  core_claim: "A fully LLM-based framework that integrates symbolic expressions and logic rules into CoT achieves better robustness, faithfulness, and accuracy than external-solver approaches, while scaling better with stronger models"
24	  key_results: "GPT-4 avg 88.47% (+7.88% over Logic-LM); 100% execution rate (vs Logic-LM ~80%); unfaithful reasoning reduced from 6% to 0% with Verifier; +24.3% improvement from GPT-3.5→GPT-4 (vs Logic-LM +19.9%)"
25	  limitations:
26	    - "Only evaluated FOL and Constraint Optimization symbolic structures"
27	    - "High API cost due to extended symbolic reasoning chains"
28	    - "Does not enhance LLM's planning capability — relies on LLM's inherent planning"
29	  relation_to_us: "competitor"
30	
31	narrative:
32	  story_type: "突破局限型"
33	  hook: "Achieving human-like logical reasoning capabilities is crucial for realizing AGI"
34	  tension: "Existing neurosymbolic systems (LINC, Logic-LM) use LLMs merely as translators, not enhancing LLM's own reasoning; over-reliance on external solvers causes inflexibility, information loss, and unexplainability"
35	  key_insight: "Section 3 — combining symbolic expressions with natural language in CoT leverages mutual strengths: 'freely expressed implicit intents and contextual information in natural language and rigorous expression in symbolic forms'"
36	  argument_chain: "CoT unfaithful for logic → external solvers lose information → hybrid symbolic+NL CoT → plan-then-solve with verification → 5-dataset validation + faithfulness analysis"
37	  contribution_framing: "3 contributions: (1) fully LLM-based framework without external tools, (2) integration of symbolic+NL expressions, (3) plan-then-solve + verification for faithfulness"
38	  intro_structure: "6 paragraphs: (1) AGI motivation, (2) CoT background, (3) CoT limitations for logic, (4) SymbCoT design with 3 aspects, (5) experimental results, (6) contribution list"
39	  notable_technique: "Positioning against existing neurosymbolic systems by reframing external solvers as a liability (information loss, inflexibility) rather than a strength"
40	
41	figures:
42	  figure_count: 8
43	  figure1:
44	    type: "problem_illustration"
45	    description: "Side-by-side comparison of CoT (overgeneralizes) vs SymbCoT (correctly reasons with symbolic premises and verification) on a logical reasoning problem"
46	    narrative_role: "Demonstrates CoT's unfaithfulness and SymbCoT's faithfulness on a concrete example"
47	    design_elements: ["side-by-side layout", "red X / green check marks", "highlighted error text", "symbolic formula display"]
48	    visual_style: "Two-column with color-coded correctness annotations, showing both the reasoning process and final answer"
49	  result_figures:
50	    - figure_id: "Figure 4"
51	      viz_type: "line_plot"
52	      what_compared: "Accuracy across reasoning depths (0-5) on ProofWriter"
53	      how_gain_highlighted: "SymbCoT maintains high accuracy while baselines degrade; red dual-head arrow shows improvement gap"
54	      design_note: "Critical depth analysis showing advantage grows with complexity — same pattern as LINC and Logic-LM"
55	    - figure_id: "Figure 5"
56	      viz_type: "bar_chart"
57	      what_compared: "Execution rate across 5 datasets: Logic-LM vs SymbCoT"
58	      how_gain_highlighted: "SymbCoT achieves 100% across all datasets vs Logic-LM's variable rates"
59	      design_note: "Strongest evidence against external-solver approaches"
60	    - figure_id: "Figure 8"
61	      viz_type: "bar_chart"
62	      what_compared: "GPT-3.5 vs GPT-4 improvement for each method"
63	      how_gain_highlighted: "SymbCoT shows largest improvement (+24.3%), demonstrating better scaling with model capability"
64	      design_note: "Model scaling argument — fully LLM-based approach benefits more from stronger models"
65	  ablation_figures:
66	    - figure_id: "Figure 3"
67	      viz_type: "grouped_bar"
68	      dimensions_varied: ["module combinations: full vs w/o Planner&Solver&Verifier vs w/o Translator&Planner&Solver&Verifier"]
69	      design_note: "6-panel ablation across datasets, color-coded by module configuration"
70	  figure_narrative_role: "Fig1(motivation) → Fig2(method overview) → Fig3(ablation) → Fig4(depth) → Fig5(execution rate) → Fig6(error analysis) → Fig7(faithfulness) → Fig8(model scaling)"
71	
72	tables:
73	  table_count: 2
74	  main_result_table:
75	    table_id: "Table 1"
76	    row_axis: "methods"
77	    col_axis: "datasets (PrOntoQA, ProofWriter, FOLIO) + Avg"
78	    row_organization: "by_category"
79	    col_organization: "grouped_by_dataset"
80	    highlight_strategy: "bold_best + underline_second"
81	    statistical_reporting: "delta improvement in brackets below best"
82	    num_baselines: 7
83	    design_note: "Split by GPT-3.5 and GPT-4 sections; includes many baselines (7) for comprehensive comparison"
84	  ablation_tables:
85	    - table_id: "Table 2"
86	      what_varied: ["symbolic representation: CO on LogicalDeduction and AR-LSAT"]
87	      variation_style: "full_numbers"
88	      design_note: "Demonstrates generalizability across symbolic structures"
89	  supplementary_tables:
90	    in_appendix: true
91	    content: "Symbolic structure details, dataset descriptions, baseline configurations, full prompt templates"
92	    reason: "Detailed prompt engineering and configuration too long for main text"
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4375fd8-3024-4e41-a437-37b4537c6850",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "bb799c9a-3ee9-44ba-af7d-c30e4f249c0e",
  "sourceToolAssistantUUID": "f4375fd8-3024-4e41-a437-37b4537c6850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T07:44:34.297Z_

<details open><summary>🔧 Tool call — Read · `toolu_0128MpjCZrvWQ1QkyDqe2Eoc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xiong2024uncertainty.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb799c9a-3ee9-44ba-af7d-c30e4f249c0e",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLiTDUy9Gr7oSn8XkSE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a645c982-0a42-4818-ac11-3e8cbe639912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0143SzNrB33xroVidCYdxBrB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15728,
      "cache_read_input_tokens": 0,
      "output_tokens": 2214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15728
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2214,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15728,
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

_source line 58 · 2026-05-21T07:44:34.302Z_

<details><summary>↩ Tool result · `toolu_0128MpjCZrvWQ1QkyDqe2Eoc`</summary>

```text
1	paper_key: "xiong2024uncertainty"
2	title: "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs"
3	venue: "ICLR 2024"
4	full_text_available: true
5	
6	research:
7	  baselines: ["Vanilla prompting", "white-box methods (logit-based)"]
8	  metrics:
9	    - {name: "ECE (Expected Calibration Error)", direction: "lower_better"}
10	    - {name: "AUROC", direction: "higher_better"}
11	    - {name: "AUPRC", direction: "higher_better"}
12	  datasets:
13	    - {name: "CommonsenseQA", size: "commonsense"}
14	    - {name: "TruthfulQA", size: "commonsense"}
15	    - {name: "GSM8K", size: "arithmetic"}
16	    - {name: "DateUnderstanding", size: "symbolic"}
17	    - {name: "Professional Law/Medicine/Psychology", size: "professional knowledge"}
18	    - {name: "Business Ethics", size: "ethics"}
19	  ablation_dimensions: ["prompting_strategy (Vanilla/CoT/Self-Probing/Multi-Step/Top-K)", "sampling_method (Self-Random/Prompting/Misleading)", "aggregation (Consistency/Avg-Conf/Pair-Rank)"]
20	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "GPT-3, GPT-3.5, GPT-4, Vicuna-13B, LLaMA-2-70B"}
21	  method_family: "black-box confidence elicitation / uncertainty estimation"
22	
23	positioning:
24	  core_claim: "LLMs are systematically overconfident when verbalizing confidence (concentrating in 80-100% range), but consistency-based multi-sample methods can substantially improve calibration, especially on structured reasoning tasks"
25	  key_results: "GSM8K AUROC: 54.8% → 92.7% with consistency-based sampling; white-box vs black-box gap is narrow (AUROC 0.522 vs 0.605); Top-K + Self-Random + Avg-Conf is recommended pipeline"
26	  limitations:
27	    - "Professional knowledge tasks remain persistently challenging for all methods"
28	    - "Black-box methods still trail white-box approaches"
29	    - "Verbalized confidence mimics human expression patterns (multiples of 5) rather than reflecting true uncertainty"
30	  relation_to_us: "complementary"
31	
32	narrative:
33	  story_type: "化繁为简型"
34	  hook: "LLMs' tendency to be overconfident poses potential risks for safe deployment"
35	  tension: "Existing uncertainty methods require model internals (logits, embeddings) — inapplicable to black-box APIs like GPT-4"
36	  key_insight: "Section 3 — organizing confidence elicitation as prompting × sampling × aggregation creates a systematic design space, revealing that sampling multiple responses is the most impactful component"
37	  argument_chain: "LLMs overconfident → need black-box uncertainty → systematic 3-component framework → prompting helps calibration but not failure prediction → sampling is the key lever → practical recommendation"
38	  contribution_framing: "3 contributions: (1) systematic framework for confidence elicitation, (2) comprehensive evaluation across 5 reasoning types and 5 models, (3) practical recommendations"
39	  intro_structure: "4 paragraphs: (1) LLM deployment risk from overconfidence, (2) black-box constraint, (3) framework overview and approach, (4) key findings and recommendations"
40	  notable_technique: "The prompting × sampling × aggregation decomposition turns an empirical study into a reusable design framework"
41	
42	figures:
43	  figure_count: 6
44	  figure1:
45	    type: "method_overview"
46	    description: "Three-component framework: prompting strategies (5 types) → sampling methods (3 types) → aggregation techniques (3 types)"
47	    narrative_role: "Establishes the systematic design space for confidence elicitation"
48	    design_elements: ["three-stage pipeline", "enumeration of options at each stage", "flow arrows"]
49	    visual_style: "Horizontal pipeline with branching options at each stage"
50	  result_figures:
51	    - figure_id: "confidence distribution figure"
52	      viz_type: "bar_chart"
53	      what_compared: "Distribution of verbalized confidence values"
54	      how_gain_highlighted: "Shows clustering in 80-100% range, illustrating overconfidence"
55	      design_note: "Powerful visual evidence for the overconfidence claim"
56	  ablation_figures:
57	    - figure_id: "component comparison figures"
58	      viz_type: "grouped_bar"
59	      dimensions_varied: ["prompting strategy", "sampling method", "aggregation technique"]
60	      design_note: "Systematic comparison across the 3-component design space"
61	  figure_narrative_role: "Fig1(framework) → confidence distribution → component-wise analysis → task-specific results"
62	
63	tables:
64	  table_count: 4
65	  main_result_table:
66	    table_id: "main results table"
67	    row_axis: "methods (prompting × sampling × aggregation combinations)"
68	    col_axis: "datasets × metrics (ECE, AUROC, AUPRC)"
69	    row_organization: "by_category"
70	    col_organization: "grouped_by_metric"
71	    highlight_strategy: "bold_best"
72	    statistical_reporting: "mean across datasets"
73	    num_baselines: 5
74	    design_note: "Large table covering 3 metrics × 8 datasets × multiple method combinations"
75	  ablation_tables:
76	    - table_id: "component ablation"
77	      what_varied: ["prompting strategy", "sampling method", "aggregation technique"]
78	      variation_style: "full_numbers"
79	      design_note: "Isolates each component's contribution systematically"
80	  supplementary_tables:
81	    in_appendix: true
82	    content: "Per-dataset breakdowns, per-model results, prompt templates"
83	    reason: "Full combinatorial results too large for main text"
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a645c982-0a42-4818-ac11-3e8cbe639912",
  "isSidechain": true,
  "promptId": "b154c21b-543a-4b5e-bd05-8da3ce46cc97",
  "agentId": "ad9e4baebe5f13e88",
  "type": "user",
  "uuid": "ccd99a97-c514-402e-89fa-71858529a982",
  "sourceToolAssistantUUID": "a645c982-0a42-4818-ac11-3e8cbe639912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-21T07:47:33.411Z_

I have successfully read all 28 YAML files from the `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/` directory. Here is the complete content of each file:

---

## 1. du2023improving.yaml
```yaml
paper_key: "du2023improving"
title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["single-agent CoT", "self-consistency", "self-verification"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "factual validity", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "N/A"}
    - {name: "math reasoning benchmarks", size: "N/A"}
    - {name: "biographical QA", size: "N/A"}
  ablation_dimensions: ["number of agents", "number of debate rounds"]
  training_recipe: {info: "black-box prompting, no training"}
  method_family: "multi-agent debate"

positioning:
  core_claim: "Multiple LLM instances debating over multiple rounds significantly enhances mathematical/strategic reasoning and factual validity compared to single-agent approaches"
  key_results: "Significant improvements in mathematical and strategic reasoning; reduced hallucinations and fallacious answers"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 2. chen2024usc.yaml
```yaml
paper_key: "chen2024usc"
title: "Universal Self-Consistency for Large Language Model Generation"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["standard self-consistency (majority voting)", "execution-based voting"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "consistency", direction: "higher_better"}
  datasets:
    - {name: "mathematical reasoning benchmarks", size: "N/A"}
    - {name: "code generation benchmarks", size: "N/A"}
    - {name: "long-context summarization", size: "N/A"}
    - {name: "open-ended QA", size: "N/A"}
  ablation_dimensions: ["task type", "number of samples"]
  training_recipe: {info: "prompting-based, no training"}
  method_family: "self-consistency"

positioning:
  core_claim: "LLMs themselves can select the most consistent answer among multiple candidates, extending self-consistency to free-form generation tasks where majority voting is inapplicable"
  key_results: "Matches standard self-consistency on math; matches execution-based voting on code generation without execution access"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 3. taubenfeld2025cisc.yaml
```yaml
paper_key: "taubenfeld2025cisc"
title: "Confidence Improves Self-Consistency in LLMs"
venue: "ACL Findings 2025"
full_text_available: false

research:
  baselines: ["standard self-consistency (unweighted majority voting)"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "sample efficiency (paths needed)", direction: "lower_better"}
  datasets:
    - {name: "4 reasoning datasets (unspecified)", size: "N/A"}
  ablation_dimensions: ["confidence scoring method", "number of sampled paths", "model choice"]
  training_recipe: {info: "prompting-based, no training; confidence scores from model logits"}
  method_family: "confidence-weighted self-consistency"

positioning:
  core_claim: "Weighted majority voting using model confidence scores (CISC) identifies correct answers with >40% fewer reasoning paths than standard self-consistency across 9 models and 4 datasets"
  key_results: ">40% reduction in sampled paths on average; outperforms standard self-consistency across 9 models and 4 datasets"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 4. dsc2025.yaml
```yaml
paper_key: "dsc2025"
title: "Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning"
venue: "NAACL Findings 2025"
full_text_available: false

research:
  baselines: ["Adaptive Self-Consistency (ASC)", "Early-stopping Self-Consistency (ESC)", "standard self-consistency"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "inference cost (number of samples)", direction: "lower_better"}
  datasets:
    - {name: "arithmetic reasoning benchmarks", size: "N/A"}
    - {name: "commonsense reasoning benchmarks", size: "N/A"}
    - {name: "symbolic reasoning benchmarks", size: "N/A"}
  ablation_dimensions: ["prior vs posterior difficulty estimation", "batch-level vs instance-level allocation"]
  training_recipe: {info: "prompting-based, no training; difficulty estimation from batch statistics"}
  method_family: "adaptive self-consistency"

positioning:
  core_claim: "Leveraging both prior and posterior difficulty information at the batch level enables adaptive inference resource allocation that significantly reduces self-consistency cost while maintaining comparable performance"
  key_results: "Consistently surpasses ASC and ESC in cost efficiency by a significant margin with comparable accuracy across 6 benchmarks"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 5. fover2025.yaml
```yaml
paper_key: "fover2025"
title: "FoVer: Efficient PRM Training Data Synthesis via Formal Verification"
venue: "ACL Findings 2026"
full_text_available: false

research:
  baselines: ["PRMs trained on human-annotated data", "PRMs trained on LLM-generated labels"]
  metrics:
    - {name: "accuracy on reasoning benchmarks", direction: "higher_better"}
    - {name: "step-level error detection", direction: "higher_better"}
  datasets:
    - {name: "12 reasoning benchmarks (math, logic, NLI, BBH)", size: "N/A"}
    - {name: "formal logic tasks", size: "N/A"}
    - {name: "theorem proving tasks", size: "N/A"}
  ablation_dimensions: ["formal verification tool (Z3 vs Isabelle)", "training data domain"]
  training_recipe: {info: "fine-tuning PRMs on synthesized step-level labels from Z3/Isabelle formal verification"}
  method_family: "formal verification for process reward models"

positioning:
  core_claim: "Formal verification tools (Z3, Isabelle) can automatically synthesize high-quality PRM training data with step-level error labels, improving reasoning across both formal and informal tasks without human annotation"
  key_results: "Improves PRMs on math, logic, NLI, and BBH benchmarks; generalizes from formal to informal reasoning"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 6. constraintllm2025.yaml
```yaml
paper_key: "constraintllm2025"
title: "ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming"
venue: "EMNLP 2025"
full_text_available: false

research:
  baselines: ["general-purpose LLMs on CP tasks"]
  metrics:
    - {name: "solving accuracy", direction: "higher_better"}
  datasets:
    - {name: "IndusCP", size: "140 industrial-level tasks"}
    - {name: "existing CP benchmarks", size: "N/A"}
  ablation_dimensions: ["Constraint-Aware Retrieval Module", "Tree-of-Thoughts framework", "guided self-correction"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", info: "multi-instruction supervised fine-tuning on open-source LLM"}
  method_family: "neuro-symbolic constraint programming"

positioning:
  core_claim: "First LLM specifically designed for CP modeling, combining constraint-aware retrieval with Tree-of-Thoughts and self-correction to achieve 2x improvement over baselines on industrial-level CP tasks"
  key_results: "State-of-the-art solving accuracy across multiple benchmarks; 2x improvement over baselines on IndusCP"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 7. llm_meets_cp2025.yaml
```yaml
paper_key: "llm_meets_cp2025"
title: "Large Language Model Meets Constraint Propagation"
venue: "IJCAI 2025"
full_text_available: false

research:
  baselines: ["standard LLM text generation", "original GenCP"]
  metrics:
    - {name: "constraint satisfaction rate", direction: "higher_better"}
    - {name: "generation feasibility", direction: "higher_better"}
    - {name: "LLM inference efficiency", direction: "higher_better"}
  datasets:
    - {name: "COLLIE benchmarks", size: "N/A"}
  ablation_dimensions: ["MLM integration for domain preview", "bidirectional vs unidirectional propagation"]
  training_recipe: {info: "no training; inference-time constraint satisfaction via Masked Language Models"}
  method_family: "constraint programming + language models"

positioning:
  core_claim: "Formulating constrained text generation as a CSP and integrating Masked Language Models for bidirectional constraint propagation significantly improves generation quality under strict content constraints"
  key_results: "Significant improvement on COLLIE benchmarks; more efficient LLM inference usage for constrained generation"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 8. satbench2025.yaml
```yaml
paper_key: "satbench2025"
title: "SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas"
venue: "EMNLP 2025"
full_text_available: false

research:
  baselines: ["o4-mini", "other frontier LLMs"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "SATBench", size: "2100 puzzles with adjustable difficulty"}
  ablation_dimensions: ["number of clauses (difficulty)", "SAT vs UNSAT problems"]
  training_recipe: {info: "evaluation benchmark, no training; automated puzzle generation from SAT formulas + LLM translation"}
  method_family: "SAT-based reasoning benchmark"

positioning:
  core_claim: "LLMs have systematic failures in search-based logical reasoning: even the strongest model (o4-mini) achieves only 65% on hard UNSAT problems (near 50% random baseline), exhibiting satisfiability bias, context inconsistency, and condition omission"
  key_results: "o4-mini: 65.0% on hard UNSAT (random baseline: 50%); systematic failures in satisfiability bias, context inconsistency, condition omission"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 9. logicagent2025.yaml
```yaml
paper_key: "logicagent2025"
title: "From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)"
venue: "ACL 2026"
full_text_available: false

research:
  baselines: ["standard CoT prompting", "other reasoning agents"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "RepublicQA", size: "N/A (college-level, Flesch-Kincaid Grade 11.94)"}
    - {name: "ProntoQA", size: "N/A"}
    - {name: "ProofWriter", size: "N/A"}
    - {name: "FOLIO", size: "N/A"}
    - {name: "ProverQA", size: "N/A"}
  ablation_dimensions: ["semiotic square components", "automated deduction vs reflective verification"]
  training_recipe: {info: "agent-based prompting framework, no training"}
  method_family: "multi-perspective reasoning agent"

positioning:
  core_claim: "Semiotic-square-guided multi-perspective reasoning jointly addresses logical and semantic complexity, achieving 6.25% improvement on RepublicQA and 7.05% on mainstream logic benchmarks"
  key_results: "+6.25% average on RepublicQA; +7.05% average on ProntoQA, ProofWriter, FOLIO, ProverQA"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 10. xu2026dylos.yaml
```yaml
paper_key: "xu2026dylos"
title: "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)"
venue: "EACL 2026"
full_text_available: true

research:
  baselines: ["Zero-shot", "CoT", "Logic-LM", "LINC", "SymbCoT", "Aristotle"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "routing_accuracy", direction: "higher_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogicalDeduction", size: "300"}
    - {name: "AR-LSAT", size: "230"}
  ablation_dimensions: ["solver_type", "routing_strategy", "model_scale", "LoRA_finetuning"]
  training_recipe: {optimizer: "LoRA", lr: "N/A", hardware: "N/A"}
  method_family: "LLM-symbolic hybrid with dynamic solver routing"

positioning:
  core_claim: "Dynamic composition of multiple symbolic solvers (Pyke/Prover9/Z3/MiniZinc) via LLM-based routing achieves robust logical reasoning across heterogeneous problem types"
  key_results: "92.1% mixed reasoning (GPT-4o), +27% over zero-shot; 7B models: 8-26% baseline → 41-59.6% with LoRA"
  limitations:
    - "Model scale dependency — small models struggle with formalization"
    - "Formalization bottleneck: 60-80% of small-model errors from formalization"
    - "Limited solver coverage: no probabilistic/temporal/mathematical reasoning"
  relation_to_us: "competitor"

narrative:
  story_type: "统一框架型"
  hook: "Material vs formal inference dichotomy — LLMs handle material, symbolic solvers handle formal, but no system integrates both dynamically"
  tension: "Existing hybrid methods are locked to a single solver type, failing on problems requiring different logical paradigms"
  key_insight: "Revealed in Section 3 — a router that classifies reasoning type enables dynamic solver dispatch with >98% accuracy"
  argument_chain: "heterogeneous logical tasks → single-solver limitation → classify-then-route → multi-solver composition → validated on mixed benchmarks"
  contribution_framing: "3 contributions each with quantitative evidence in the intro"
  intro_structure: "5 paragraphs: (1) material-formal dichotomy hook, (2) existing hybrid limitations, (3) DyLoS overview, (4) contributions with numbers, (5) paper structure"
  notable_technique: "Every contribution claim includes specific quantitative results; material-formal inference dichotomy used as recurring anchor"

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: "3-stage pipeline: decompose → route → solve, showing 4 solver types"
    narrative_role: "Establishes the system architecture immediately after the problem statement"
    design_elements: ["flow diagram", "solver icons", "color-coded stages"]
    visual_style: "Left-to-right pipeline with branching at routing stage"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Accuracy across datasets with different solvers"
      how_gain_highlighted: "DyLoS bar consistently highest"
      design_note: "Grouped by dataset, color by method"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "bar_chart"
      dimensions_varied: ["model_scale", "with/without_LoRA"]
      design_note: "Shows scaling behavior and LoRA impact"
  figure_narrative_role: "Fig1(architecture) → Fig2(routing) → Fig3(main results) → Fig4(scaling) → Fig5(error analysis)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 6
    design_note: "Separates LLM-only vs hybrid methods"
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["solver_selection", "routing_strategy"]
      variation_style: "full_numbers"
      design_note: "Shows each solver's standalone vs combined performance"
  supplementary_tables:
    in_appendix: true
    content: "Prompt templates, additional model results"
    reason: "Space constraints"
```

---

## 11. aristotle2025.yaml
```yaml
paper_key: "aristotle2025"
title: "Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework"
venue: "ACL 2025"
full_text_available: true

research:
  baselines: ["CoT", "ToT", "CR", "SymbCoT", "Logic-LM", "LINC"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "one_step_inference_accuracy", direction: "higher_better"}
    - {name: "visited_nodes", direction: "lower_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogiQA", size: "651"}
  ablation_dimensions: ["CNF_decomposition", "search_strategy", "resolution_principle", "Prolog_translation"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "symbolic logic pipeline (Prolog + CNF + resolution)"

positioning:
  core_claim: "A logic-complete framework integrating Prolog translation, CNF decomposition, and resolution principle into LLM reasoning achieves 99.7% one-step accuracy while reducing search by 52.6%"
  key_results: "+4.5% avg over SymbCoT (GPT-4), +5.4% (GPT-4o), +12.1% (Llama-3.1-405B); 99.7% one-step accuracy vs ToT's 74.0%"
  limitations:
    - "Requires all premises explicitly stated — fails on implicit knowledge (LogiQA: 31.2% vs CoT's 65.6%)"
    - "Computationally expensive multi-step search"
  relation_to_us: "competitor"

narrative:
  story_type: "突破局限型"
  hook: "Figure 1 teaser showing accuracy gap — quantifies the problem before explaining the solution"
  tension: "Existing neurosymbolic methods suffer from incomplete logical operations, leading to error accumulation in multi-step proofs"
  key_insight: "Sec 3.2 — replacing LLM self-evaluation with deterministic resolution principle eliminates the weakest link in the reasoning chain"
  argument_chain: "multi-step errors → incomplete symbolic integration → full Prolog pipeline → deterministic search → validated accuracy + efficiency"
  contribution_framing: "3 contributions: framework, logic-completeness proof, empirical validation"
  intro_structure: "6 paragraphs: (1) LLM reasoning importance, (2) existing method failures with Figure 1, (3) root cause analysis, (4) Aristotle overview, (5) contributions, (6) paper structure"
  notable_technique: "Teaser result figure in intro paragraph 2 — immediately quantifies the gap before any method description"

figures:
  figure_count: 8
  figure1:
    type: "teaser_result"
    description: "Bar chart comparing accuracy of existing methods showing performance gap"
    narrative_role: "Quantifies the problem in the intro before solution is described"
    design_elements: ["grouped bars", "accuracy numbers", "method labels"]
    visual_style: "Clean bar chart with clear performance gap visualization"
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "scatter"
      what_compared: "Accuracy vs efficiency tradeoff across methods"
      how_gain_highlighted: "Aristotle in upper-left (high accuracy, low nodes)"
      design_note: "Dual-axis: accuracy vs search efficiency"
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths"
      how_gain_highlighted: "Aristotle maintains accuracy at higher depths"
      design_note: "Shows robustness to depth"
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "grouped_bar"
      dimensions_varied: ["CNF", "resolution", "search_strategy"]
      design_note: "Red gradient coloring for ablation variants"
  figure_narrative_role: "Fig1(teaser gap) → Fig2(method) → Fig3(ablation) → Fig4(efficiency) → Fig5(depth) → Fig6-7(case studies) → Fig8(error analysis)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best + underline_second"
    statistical_reporting: "single run"
    num_baselines: 6
    design_note: "Categorizes methods into LLM-only, symbolic-augmented, and Aristotle"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["CNF", "resolution", "Prolog_translation", "search"]
      variation_style: "checkmark_grid"
      design_note: "Systematic component removal showing each module's contribution"
  supplementary_tables:
    in_appendix: true
    content: "Extended results, additional models, case studies"
    reason: "Main paper focuses on core 4 datasets"
```

---

## 12. qi2025symbolic_provers.yaml
```yaml
paper_key: "qi2025symbolic_provers"
title: "Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation"
venue: "ICLR 2025"
full_text_available: true

research:
  baselines: ["GPT-4o", "Claude-3.5-Sonnet", "Llama3.1-8B/70B", "Gemma2-9B/27B", "Mistral-7B/Large", "Qwen2.5-7B/32B/72B"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "ID_accuracy", direction: "higher_better"}
    - {name: "OOD_accuracy", direction: "higher_better"}
  datasets:
    - {name: "ProverQA", size: "1500 instances, 3 difficulty levels"}
    - {name: "ProofWriter", size: "for transfer eval"}
    - {name: "FOLIO", size: "for transfer eval"}
  ablation_dimensions: ["difficulty_level", "CoT_vs_direct", "finetuning_data_source", "ID_vs_OOD"]
  training_recipe: {optimizer: "SFT", lr: "N/A", hardware: "N/A"}
  method_family: "LLM + symbolic prover (Prover9) for benchmark generation"

positioning:
  core_claim: "Top-down generation combining LLM diversity with Prover9 rigor creates ProverQA benchmark that reveals even SOTA models barely exceed chance on hard FOL problems"
  key_results: "GPT-4o: 50.0%, Claude-3.5: 56.4% on hard; finetuning Llama3.1-8B on ProverQA: +34.6% ID, +7.5% OOD (vs -2.0% ProofWriter, -11.4% FOLIO)"
  limitations:
    - "Benchmark limited to FOL reasoning"
    - "Top-down generation may not cover all reasoning patterns"
  relation_to_us: "foundation"

narrative:
  story_type: "统一框架型"
  hook: "Existing benchmarks lack reliable ground truth labels and controllable difficulty"
  tension: "Bottom-up benchmark construction introduces label noise and uncontrolled complexity"
  key_insight: "Section 3 — top-down generation (goal → backward to premises) ensures logical coherence by construction"
  argument_chain: "benchmark limitations → top-down generation idea → Prover9 guarantees → difficulty control → model evaluation reveals gaps → finetuning transfer validates quality"
  contribution_framing: "3 contributions: generation framework, benchmark, comprehensive evaluation"
  intro_structure: "4 paragraphs: (1) importance of logical reasoning, (2) criteria for good benchmarks, (3) ProverGen framework, (4) contributions"
  notable_technique: "Table 1 checkmark grid as early positioning device — shows no existing benchmark meets all criteria"

figures:
  figure_count: 2
  figure1:
    type: "method_overview"
    description: "ProverGen pipeline: top-down generation with Prover9"
    narrative_role: "Establishes the generation framework"
    design_elements: ["pipeline flow", "Prover9 integration point"]
    visual_style: "Schematic flow diagram"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "bar_chart"
      what_compared: "Model accuracy across difficulty levels"
      how_gain_highlighted: "Performance drop at higher difficulty"
      design_note: "Grouped by difficulty, showing model capability gap"
  ablation_figures: []
  figure_narrative_role: "Fig1(method) → Fig2(results) — minimal figures, table-heavy paper"

tables:
  table_count: 6
  main_result_table:
    table_id: "Table 2"
    row_axis: "methods"
    col_axis: "difficulty levels × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_difficulty"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 10
    design_note: "Comprehensive model comparison across 3 difficulty levels"
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["finetuning_data_source", "ID_vs_OOD"]
      variation_style: "full_numbers"
      design_note: "Transfer learning comparison showing ProverQA's superiority"
  supplementary_tables:
    in_appendix: true
    content: "Additional model results, generation statistics"
    reason: "Main paper focuses on key comparisons"
```

---

## 13. dissecting2025.yaml
```yaml
paper_key: "dissecting2025"
title: "Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation"
venue: "EMNLP Findings 2025"
full_text_available: true

research:
  baselines: ["LLaMA-3.1-8B", "Gemma-2-9B", "Mistral-v0.3-7B", "CoT", "SFT-NL", "SFT-Symbolic"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "atomicity", direction: "higher_better"}
    - {name: "CSS", direction: "higher_better"}
    - {name: "NSD", direction: "higher_better"}
    - {name: "RFI", direction: "higher_better"}
  datasets:
    - {name: "FLD", size: "multi-depth"}
    - {name: "FOLIO", size: "204"}
    - {name: "ProntoQA", size: "500"}
  ablation_dimensions: ["supervision_type_NL_vs_symbolic", "reasoning_depth", "model_family"]
  training_recipe: {optimizer: "AdamW", lr: "1e-6", hardware: "4xA100, ~2h per model"}
  method_family: "evaluation framework (accuracy + soundness + probing)"

positioning:
  core_claim: "Three-dimensional evaluation (accuracy + stepwise soundness + representation probing) reveals NL supervision generalizes better but symbolic supervision produces more structurally sound reasoning chains"
  key_results: "SFT-NL: 67.5% on FLD (from 31.7%); symbolic has higher atomicity (24.7% vs 13.0%); probing shows SFT improves generation but not internalized understanding"
  limitations:
    - "Limited to propositional/FOL reasoning"
    - "Probing only captures linear representations"
  relation_to_us: "foundation"

narrative:
  story_type: "化繁为简型"
  hook: "LLMs show improved reasoning but we lack tools to understand what exactly improves"
  tension: "Single-metric evaluation (accuracy) masks critical differences in reasoning quality"
  key_insight: "Section 4 — decomposing evaluation into accuracy/soundness/probing reveals a fundamental NL-vs-symbolic tradeoff"
  argument_chain: "opaque evaluation → 3-dimensional framework → NL vs symbolic comparison → surprising probing results → implications for training design"
  contribution_framing: "3 contributions: evaluation framework, NL-vs-symbolic findings, probing insights"
  intro_structure: "5 paragraphs: (1) LLM reasoning progress, (2) evaluation limitations, (3) proposed framework, (4) key findings preview, (5) paper structure"
  notable_technique: "Previewing surprising findings in intro to create anticipation for the full analysis"

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: "Three-dimensional evaluation framework: accuracy, soundness, probing"
    narrative_role: "Establishes the evaluation methodology upfront"
    design_elements: ["three parallel tracks", "metric labels", "color coding"]
    visual_style: "Schematic diagram with three evaluation dimensions"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths for NL vs symbolic supervision"
      how_gain_highlighted: "Symbolic degrades more gracefully at higher depths"
      design_note: "Depth-accuracy curves are the strongest evidence"
    - figure_id: "Figure 4"
      viz_type: "heatmap"
      what_compared: "Probing results (CSS, NSD, RFI) across models and training types"
      how_gain_highlighted: "Color intensity shows where SFT helps vs doesn't"
      design_note: "Compact visualization of multi-dimensional probing results"
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "bar_chart"
      dimensions_varied: ["model_family", "supervision_type"]
      design_note: "Cross-model consistency check"
  figure_narrative_role: "Fig1(framework) → Fig2(accuracy overview) → Fig3(depth analysis) → Fig4(probing) → Fig5(cross-model)"

tables:
  table_count: 5
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × metrics (accuracy + soundness)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 6
    design_note: "Dual-metric reporting (accuracy and soundness side-by-side)"
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["supervision_type", "reasoning_depth"]
      variation_style: "full_numbers"
      design_note: "Depth-stratified comparison"
  supplementary_tables:
    in_appendix: true
    content: "Full probing results, additional model comparisons"
    reason: "Probing methodology details too extensive for main text"
```

---

## 14. crest2025.yaml
```yaml
paper_key: "crest2025"
title: "Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)"
venue: "NAACL 2025"
full_text_available: true

research:
  baselines: ["SFT", "RFT", "STaR", "REST-EM", "V-STaR", "DPO-vanilla"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "ReClor", size: "~6k"}
    - {name: "ARC-Challenge", size: "2590"}
    - {name: "CSQA", size: "~12k"}
  ablation_dimensions: ["follow_up_questions", "tolerance_parameter_t", "DPO_lambda", "sample_count_N"]
  training_recipe: {optimizer: "AdamW", lr: "5e-6", hardware: "4xA100"}
  method_family: "consistency-driven self-training"

positioning:
  core_claim: "Follow-up question consistency provides richer signal than binary answer correctness for filtering self-training rationales, enabling better SFT+DPO training"
  key_results: "+1.7-1.8% over best baseline on ReClor; consistent gains on ARC-C and CSQA across Llama-3-8B, Gemma-7B, Phi-2"
  limitations:
    - "Restricted to MCQ format"
    - "All follow-up questions weighted equally"
    - "No teacher-student setting explored"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Self-training with LLM-generated rationales is promising but suffers from false positive rationales"
  tension: "Binary correctness filtering passes rationales with right answers but wrong reasoning"
  key_insight: "Section 3.2 — follow-up questions stress-test rationale quality beyond just checking the final answer"
  argument_chain: "self-training promise → false positive problem → follow-up question consistency → filtered SFT + DPO → multi-model validation"
  contribution_framing: "3 contributions: consistency evaluation method, 4-stage training pipeline, empirical validation"
  intro_structure: "4 paragraphs: (1) self-training promise, (2) false positive problem, (3) CREST solution, (4) contributions"
  notable_technique: "Concrete example of a false positive rationale in intro to make the problem viscerally clear"

figures:
  figure_count: 4
  figure1:
    type: "problem_illustration"
    description: "Example showing a rationale that gets the right answer through wrong reasoning, and how follow-up questions expose it"
    narrative_role: "Makes the false positive problem concrete and motivates the solution"
    design_elements: ["correct vs incorrect rationale comparison", "follow-up question examples", "red/green highlighting"]
    visual_style: "Two-column comparison with text examples"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Methods across 3 datasets × 3 models"
      how_gain_highlighted: "CREST consistently highest or tied"
      design_note: "3×3 grid layout for comprehensive comparison"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      dimensions_varied: ["tolerance_t", "DPO_lambda", "sample_N"]
      design_note: "Sensitivity analysis with clear optimal ranges"
  figure_narrative_role: "Fig1(problem example) → Fig2(method pipeline) → Fig3(main results) → Fig4(sensitivity)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × models"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best + underline_second"
    statistical_reporting: "mean across 3 seeds"
    num_baselines: 6
    design_note: "Separate sections for each model family"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["follow_up_questions", "SFT_only_vs_SFT+DPO"]
      variation_style: "full_numbers"
      design_note: "Isolates contribution of each pipeline stage"
  supplementary_tables:
    in_appendix: true
    content: "Additional ablations, prompt templates, follow-up question examples"
    reason: "Main text focuses on core comparisons"
```

---

## 15. khan2024debating.yaml
```yaml
paper_key: "khan2024debating"
title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
venue: "ICML 2024"
full_text_available: true

research:
  baselines: ["Naive judge", "Consultancy (correct)", "Consultancy (incorrect)", "Non-interactive debate"]
  metrics:
    - {name: "judge_accuracy", direction: "higher_better"}
    - {name: "Elo_rating", direction: "higher_better"}
  datasets:
    - {name: "QuALITY", size: "reading comprehension"}
  ablation_dimensions: ["protocol_type", "interactivity", "debater_model", "judge_model", "BoN_size", "quote_system", "round_count", "word_limits", "majority_voting", "few_shot_count", "finetuning_data_type", "human_vs_LLM_judges", "persuasiveness_optimization"]
  training_recipe: {optimizer: "BoN + RL", lr: "N/A", hardware: "N/A"}
  method_family: "multi-agent debate for AI safety"

positioning:
  core_claim: "Adversarial debate between LLM experts with persuasiveness optimization lets weaker judges identify truth better than non-adversarial consultancy"
  key_results: "Debate: 88% human / 76% LLM accuracy vs Consultancy: 78%/54% vs Naive: 60%/48%"
  limitations:
    - "Information asymmetry only (not reasoning gap)"
    - "RLHF-honest models only"
    - "Quote verification dependency"
    - "Single dataset (QuALITY)"
  relation_to_us: "complementary"

narrative:
  story_type: "突破局限型"
  hook: "Scalable oversight — how do we verify AI behavior when it exceeds human capability?"
  tension: "Alignment techniques depend on human labels, but humans can't label superhuman behavior"
  key_insight: "Figures 3-4 mirror pair — persuasiveness helps debate (correct debater gains advantage) but hurts consultancy (incorrect consultant becomes more persuasive)"
  argument_chain: "alignment crisis → debate as theoretical solution → empirical setup with LLM proxy → 9 cumulative insights → persuasiveness as unsupervised training signal"
  contribution_framing: "Framed as 'insights' rather than 'contributions' — 9 numbered insights for cumulative evidence"
  intro_structure: "5 paragraphs: (1) scalable oversight problem, (2) debate proposal recap, (3) experimental approach, (4) key findings preview, (5) implications"
  notable_technique: "Numbered Insight 1-9 structure replaces traditional contribution list; Figure 3-4 mirror design as argumentative backbone"

figures:
  figure_count: 17
  figure1:
    type: "method_overview"
    description: "Debate vs consultancy protocol comparison"
    narrative_role: "Establishes the two paradigms being compared"
    design_elements: ["side-by-side protocols", "agent roles", "information flow"]
    visual_style: "Schematic with two parallel protocol diagrams"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "bar_chart"
      what_compared: "Judge accuracy across protocols"
      how_gain_highlighted: "Debate consistently above consultancy"
      design_note: "Clear protocol comparison"
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Elo rating vs persuasiveness optimization for debate"
      how_gain_highlighted: "Correct-answer Elo grows with optimization"
      design_note: "Mirror pair with Figure 4 — debate's mechanism"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Elo rating vs persuasiveness optimization for consultancy"
      how_gain_highlighted: "Incorrect consultant Elo grows — consultancy breaks"
      design_note: "Mirror with Fig3 showing opposite effect"
  ablation_figures:
    - figure_id: "Figures 5-17"
      viz_type: "mixed"
      dimensions_varied: ["13 ablation dimensions"]
      design_note: "Massive ablation suite — all visual, no tables"
  figure_narrative_role: "Fig1(protocol) → Fig2(main result) → Fig3-4(mechanism mirror) → Fig5-17(extensive ablations) — remarkably figure-heavy, only 1 table"

tables:
  table_count: 1
  main_result_table:
    table_id: "Table 1"
    row_axis: "definitions"
    col_axis: "N/A"
    row_organization: "flat"
    col_organization: "flat"
    highlight_strategy: "N/A"
    statistical_reporting: "N/A"
    num_baselines: 0
    design_note: "Definitional table only — all quantitative results are figures"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Additional experimental details"
    reason: "All main results presented visually"
```

---

## 16. olausson2023linc.yaml
```yaml
paper_key: "olausson2023linc"
title: "LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers"
venue: "EMNLP 2023"
full_text_available: true

research:
  baselines: ["Naive (direct)", "Scratchpad (FOL gen + LLM judge)", "CoT"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "ProofWriter", size: "OOD split"}
    - {name: "FOLIO", size: "204"}
  ablation_dimensions: ["K_majority_vote", "model_type", "proof_depth"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "neurosymbolic (LLM → FOL → Prover9)"

positioning:
  core_claim: "Two-stage LLM-to-FOL-to-Prover9 pipeline with majority vote achieves near-perfect accuracy on synthetic FOL tasks and maintains robustness across proof depths"
  key_results: "ProofWriter: StarCoder++ LINC 82.1% vs 37.8% best baseline; GPT-3.5 LINC 96.4%; GPT-4 LINC 98.3%. FOLIO: gains for smaller models, not significant for GPT-4"
  limitations:
    - "FOL is lossy for naturalistic language"
    - "Scalability unclear with more premises"
    - "FOL expressiveness insufficient for higher-order/non-classical logic"
  relation_to_us: "foundation"

narrative:
  story_type: "跨界迁移型"
  hook: "LLMs struggle with multi-step deduction despite general language understanding"
  tension: "CoT provides reasoning steps but can't guarantee logical soundness"
  key_insight: "Section 3 — the Scratchpad baseline isolates the prover's contribution: generating FOL alone (without symbolic execution) doesn't help"
  argument_chain: "LLM deduction weakness → separate understanding from reasoning → LLM parses, prover reasons → Scratchpad control proves prover is key → depth analysis confirms robustness"
  contribution_framing: "2 contributions: LINC system, Scratchpad diagnostic baseline"
  intro_structure: "4 paragraphs: (1) LLM reasoning gap, (2) neurosymbolic opportunity, (3) LINC and Scratchpad, (4) key findings"
  notable_technique: "Scratchpad as diagnostic baseline — isolates the symbolic prover's causal contribution beyond just generating FOL"

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: "LINC pipeline: NL → LLM → FOL → Prover9 → answer, with K-way majority vote"
    narrative_role: "Establishes the two-stage architecture"
    design_elements: ["pipeline flow", "LLM and Prover9 components", "majority vote aggregation"]
    visual_style: "Left-to-right pipeline diagram"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Methods across models on ProofWriter and FOLIO"
      how_gain_highlighted: "LINC bars clearly above baselines"
      design_note: "Grouped by model, color by method"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Accuracy across proof depths (0-5)"
      how_gain_highlighted: "LINC maintains near-perfect accuracy while baselines degrade"
      design_note: "Strongest evidence for robustness — depth-accuracy curves"
    - figure_id: "Figure 5"
      viz_type: "qualitative_comparison"
      what_compared: "Error types: LINC vs CoT"
      how_gain_highlighted: "Only 21/74 errors shared — methods are complementary"
      design_note: "Error analysis Venn diagram / taxonomy"
  ablation_figures: []
  figure_narrative_role: "Fig1(pipeline) → Fig2(FOL examples) → Fig3(main results bars) → Fig4(depth analysis) → Fig5(error analysis)"

tables:
  table_count: 0
  main_result_table:
    table_id: "N/A"
    row_axis: "N/A"
    col_axis: "N/A"
    row_organization: "N/A"
    col_organization: "N/A"
    highlight_strategy: "N/A"
    statistical_reporting: "p-values for significance"
    num_baselines: 3
    design_note: "No tables — all results presented as bar charts and line plots. Unusual but effective given small experimental grid"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Prompt templates, FOL examples, additional error analysis"
    reason: "Qualitative content doesn't fit tabular format"
```

---

## 17. pan2023logiclm.yaml
```yaml
paper_key: "pan2023logiclm"
title: "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning"
venue: "EMNLP Findings 2023"
full_text_available: true

research:
  baselines: ["Standard Prompting", "CoT", "CoT-SC"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "Exe_Rate", direction: "higher_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogicalDeduction", size: "300"}
    - {name: "AR-LSAT", size: "230"}
  ablation_dimensions: ["self_refinement", "solver_type", "model_type", "problem_type"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "LLM + symbolic solver (Pyke/Prover9/python-constraint/Z3)"

positioning:
  core_claim: "Reframing LLM's role from 'solving' to 'representing' — LLM formulates problems symbolically, dedicated solvers execute reasoning, with self-refinement for invalid formulations"
  key_results: "+39.2% over standard prompting, +18.4% over CoT (GPT-3.5); GPT-4: PrOntoQA 83.2, ProofWriter 79.66, FOLIO 78.92, LogicalDeduction 87.63, AR-LSAT 43.04"
  limitations:
    - "Low Exe_Rate on complex problems (FOLIO 79.9%, AR-LSAT 32.6% with GPT-4)"
    - "Self-refinement fixes grammar but not semantics"
    - "Formalization bottleneck on naturalistic language"
  relation_to_us: "foundation"

narrative:
  story_type: "跨界迁移型"
  hook: "LLMs can understand language but fail at rigorous logical reasoning"
  tension: "Prompting strategies improve reasoning but can't guarantee faithfulness"
  key_insight: "Section 3 — separating 'understanding' (LLM) from 'reasoning' (solver) plays to each component's strength"
  argument_chain: "LLM reasoning unfaithful → separate understanding from reasoning → LLM formulates + solver executes → self-refinement handles errors → 5-dataset validation"
  contribution_framing: "3 contributions: framework, self-refinement mechanism, comprehensive evaluation"
  intro_structure: "5 paragraphs: (1) LLM reasoning promise/limitations, (2) faithfulness problem, (3) Logic-LM framework, (4) contributions, (5) paper structure"
  notable_technique: "Reframing the LLM's role from 'solver' to 'translator' — rhetorically powerful simplification"

figures:
  figure_count: 4
  figure1:
    type: "method_overview"
    description: "Logic-LM pipeline: Problem Formulation → Symbolic Reasoning → Result Interpretation, with self-refinement loop"
    narrative_role: "Establishes the three-stage architecture with refinement"
    design_elements: ["pipeline flow", "self-refinement loop arrow", "4 solver icons"]
    visual_style: "Flowchart with feedback loop"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths"
      how_gain_highlighted: "Logic-LM advantage grows with depth (widening gap at depth-5)"
      design_note: "Depth analysis showing symbolic reasoning's advantage on harder problems"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "bar_chart"
      dimensions_varied: ["with/without self-refinement", "solver_type"]
      design_note: "Isolates self-refinement contribution"
  figure_narrative_role: "Fig1(pipeline) → Fig2(example) → Fig3(depth analysis) → Fig4(ablation)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 3
    design_note: "Clean comparison with Exe_Rate reported alongside accuracy"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["self_refinement", "error_type"]
      variation_style: "full_numbers"
      design_note: "Breaks down Exe_Rate improvement by error category"
  supplementary_tables:
    in_appendix: true
    content: "Prompt templates, solver-specific results, error examples"
    reason: "Detailed error analysis too long for main text"
```

---

## 18. snell2025scaling_tts.yaml
```yaml
paper_key: "snell2025scaling_tts"
title: "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters"
venue: "ICLR 2025 (Oral)"
full_text_available: false

research:
  baselines: ["greedy decoding", "majority voting", "best-of-N", "reward-model reranking"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "compute_efficiency", direction: "higher_better"}
  datasets:
    - {name: "MATH", size: "500"}
    - {name: "GSM8K", size: "1319"}
  ablation_dimensions: ["compute_budget", "search_strategy", "verifier_type", "model_scale"]
  training_recipe: {info: "process reward models for verification"}
  method_family: "test-time compute scaling"

positioning:
  core_claim: "Optimal allocation of test-time compute (search + verification) can match or exceed 14x larger models"
  key_results: "Smaller model + optimal test-time compute matches 14x larger model on MATH"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 19. multi_path_plan2025.yaml
```yaml
paper_key: "multi_path_plan2025"
title: "Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines: ["CoT", "SC-CoT", "ToT", "plan-then-solve"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
    - {name: "ARC-Challenge", size: "2590"}
  ablation_dimensions: ["num_paths", "aggregation_strategy", "plan_granularity"]
  training_recipe: {info: "N/A"}
  method_family: "multi-path reasoning aggregation"

positioning:
  core_claim: "Aggregating multiple reasoning plans before execution improves long chain-of-thought reasoning"
  key_results: "N/A"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 20. wang2024mathshepherd.yaml
```yaml
paper_key: "wang2024mathshepherd"
title: "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations"
venue: "ACL 2024"
full_text_available: false

research:
  baselines: ["majority voting", "ORM (outcome reward model)", "PRM (process reward model)"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
  ablation_dimensions: ["verification_granularity", "reward_model_size", "num_samples"]
  training_recipe: {info: "automated step-level annotation via completion-based verification"}
  method_family: "process reward model / step-level verification"

positioning:
  core_claim: "Automated step-level verification annotations (without human labels) enable process reward models that outperform outcome-only verification"
  key_results: "GSM8K: 84.1% → 93.4% with Math-Shepherd PRM verification"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 21. hosseini2024vstar.yaml
```yaml
paper_key: "hosseini2024vstar"
title: "V-STaR: Training Verifiers for Self-Taught Reasoners"
venue: "NeurIPS 2024"
full_text_available: false

research:
  baselines: ["STaR", "REST-EM", "majority_voting", "ORM"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
    - {name: "ARC-Challenge", size: "2590"}
  ablation_dimensions: ["verifier_training_data", "iteration_count", "generator_vs_verifier_scaling"]
  training_recipe: {info: "iterative self-training with DPO verifier"}
  method_family: "self-training with verifier"

positioning:
  core_claim: "Training verifiers on both correct and incorrect solutions from self-taught reasoners creates a virtuous cycle improving both generator and verifier"
  key_results: "GSM8K: +4.7% over STaR; MATH: +2.1% over STaR with verification"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 22. huang2024selfcorrect.yaml
```yaml
paper_key: "huang2024selfcorrect"
title: "Large Language Models Cannot Self-Correct Reasoning Yet"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["standard prompting", "CoT", "self-refine", "multi-agent debate"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "CommonSenseQA", size: "1221"}
    - {name: "HotpotQA", size: "multi-hop"}
  ablation_dimensions: ["feedback_type", "oracle_vs_intrinsic", "iteration_count"]
  training_recipe: {info: "N/A — prompting-based study"}
  method_family: "self-correction analysis"

positioning:
  core_claim: "LLMs cannot self-correct reasoning without external feedback; intrinsic self-correction often degrades performance"
  key_results: "Self-correction without oracle feedback consistently hurts accuracy (GSM8K: -2.4%)"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 23. wang2023sc.yaml
```yaml
paper_key: "wang2023sc"
title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
venue: "ICLR 2023"
full_text_available: false

research:
  baselines: ["greedy CoT", "sample-and-rank", "beam search"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "SVAMP", size: "1000"}
    - {name: "AQuA", size: "254"}
    - {name: "StrategyQA", size: "2290"}
    - {name: "ARC-Challenge", size: "2590"}
  ablation_dimensions: ["num_samples", "temperature", "model_scale"]
  training_recipe: {info: "N/A — decoding strategy"}
  method_family: "self-consistency / majority voting"

positioning:
  core_claim: "Sampling multiple reasoning paths and marginalizing over them via majority voting substantially improves CoT accuracy without any training"
  key_results: "GSM8K: +17.9% over greedy CoT with 40 samples (PaLM-540B)"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 24. li2023diverse.yaml
```yaml
paper_key: "li2023diverse"
title: "Making Language Models Better Reasoners with Step-Aware Verifier"
venue: "ACL 2023"
full_text_available: false

research:
  baselines: ["CoT", "SC-CoT", "voting_verifier"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
  ablation_dimensions: ["verifier_granularity", "diverse_prompts", "sample_count"]
  training_recipe: {info: "step-aware verifier training"}
  method_family: "diverse prompting + step-aware verification"

positioning:
  core_claim: "Combining diverse prompting strategies with step-level verification outperforms simple self-consistency"
  key_results: "GSM8K: +3.2% over SC-CoT with step-aware verifier"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 25. rc2025.yaml
```yaml
paper_key: "rc2025"
title: "Representation Consistency for Accurate and Coherent LLM Answer Aggregation"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines: ["majority_voting", "USC", "weighted_voting"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "coherence", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "TriviaQA", size: "open-domain"}
    - {name: "MMLU", size: "multi-task"}
  ablation_dimensions: ["representation_type", "aggregation_method", "sample_count"]
  training_recipe: {info: "N/A — aggregation method"}
  method_family: "representation-based answer aggregation"

positioning:
  core_claim: "Aggregating answers based on representation consistency (semantic similarity) outperforms surface-form majority voting for open-ended generation"
  key_results: "N/A"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 26. ye2024satlm.yaml
```yaml
paper_key: "ye2024satlm"
title: "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting"
venue: "NeurIPS 2023"
full_text_available: true

research:
  baselines: ["Standard Prompting", "CoT", "ProgLM"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "selective_accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM", size: "1319"}
    - {name: "GSM-Sys", size: "subset"}
    - {name: "ALGEBRA", size: "textbook problems"}
    - {name: "LSAT", size: "230"}
    - {name: "BoardgameQA", size: "depth 1-3"}
    - {name: "CLUTRR", size: "kinship reasoning"}
    - {name: "ProofWriter", size: "depth-5"}
    - {name: "COLOR", size: "BIG-bench"}
    - {name: "REGEX", size: "StRegex"}
  ablation_dimensions: ["solver_type (SAT vs CoT vs None)", "declarative_vs_imperative", "exemplar_sensitivity", "model_generalization"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "code-davinci-002, gpt-3.5-turbo, text-davinci-003"}
  method_family: "declarative prompting + SAT/SMT solver (Z3)"

positioning:
  core_claim: "Shifting LLMs from generating imperative programs to declarative specifications enables SAT solvers to handle both planning and execution, eliminating planning errors that plague program-aided LMs"
  key_results: "GSM-Sys: 69.4% (+23% over ProgLM); LSAT SoTA 37.4% (from 30.9%); BoardgameQA SoTA 80.7% (from 73.9%); GSM SC: 84.8% matching full-training-set models"
  limitations:
    - "Some problems naturally suit imperative procedures (SatLM slightly lags ProgLM on GSM greedy)"
    - "SAT solver expressiveness limited for quantifiers and nonlinear arithmetic"
    - "One-round parse-solve; no iterative refinement based on solver feedback"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "CoT prompting falls short on problems requiring sophisticated planning and search"
  tension: "Program-aided LMs fix execution errors but not planning errors — LLM must both plan and execute in imperative paradigm"
  key_insight: "Section 2, paragraph 3 — 'Our work tackles both execution errors and, more importantly, planning errors' by shifting to declarative specifications where the solver handles both planning and execution"
  argument_chain: "CoT fails at planning → imperative programs still require LLM planning → declarative specs offload both planning+execution to solver → solver guarantees correctness → 8-dataset validation across 4 task types"
  contribution_framing: "2 key advantages framed as properties: (1) declarative spec closer to problem description, (2) solver guarantees correctness. Plus 3 analysis findings"
  intro_structure: "5 paragraphs: (1) CoT limitations for complex reasoning, (2) parse-plan-execute framework, (3) SatLM with declarative prompting, (4) results summary, (5) analysis findings"
  notable_technique: "The parse-plan-execute decomposition is reframed to show SatLM offloads 2/3 steps (plan+execute) while ProgLM only offloads 1/3 (execute) — powerful comparative framing"

figures:
  figure_count: 4
  figure1:
    type: "problem_illustration"
    description: "Side-by-side comparison of CoT (imperative) vs SatLM (declarative) on a constraint satisfaction problem. Left shows LLM doing parse+plan+execute; right shows LLM only parsing into SAT specification, solver does the rest"
    narrative_role: "Immediately demonstrates the declarative vs imperative paradigm shift on a concrete LSAT-style problem"
    design_elements: ["side-by-side comparison", "code-style specification boxes", "color-coded errors in CoT", "SAT solver icon"]
    visual_style: "Two-column layout with input problem on top, showing the full reasoning trace (left) vs compact specification + solver (right). Green/red annotations mark correct/incorrect steps"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "qualitative_comparison"
      what_compared: "CoT vs ProgLM vs SatLM on arithmetic reasoning — showing specific errors"
      how_gain_highlighted: "Red annotations on errors in CoT and ProgLM; SatLM produces correct answer"
      design_note: "Concrete error examples make the planning-vs-execution distinction tangible"
    - figure_id: "Figure 3"
      viz_type: "qualitative_comparison"
      what_compared: "SatLM variant with CoT solver (declarative spec + LLM solving)"
      how_gain_highlighted: "Shows declarative prompting helps even without symbolic solver"
      design_note: "Isolates contribution of declarative formulation vs symbolic execution"
  ablation_figures: []
  figure_narrative_role: "Fig1(paradigm comparison) → Fig2(concrete error analysis) → Fig3(ablation variant) → Fig4(commonsense parsing examples)"

tables:
  table_count: 7
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets (GSM-Sys, GSM, ALGE, LSAT, BOARD, CLUTRR, PROOF, COLOR, REGEX)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "bootstrap significance tests (p<0.05)"
    num_baselines: 3
    design_note: "Split into greedy and self-consistency decoding blocks; 9 datasets is unusually comprehensive"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["solver_type: SAT_SymSolver vs SAT_CoTSolver vs SAT_NoSolver"]
      variation_style: "full_numbers"
      design_note: "Isolates solver contribution — key insight that declarative prompting helps even without solver"
    - table_id: "Table 3"
      what_varied: ["error_type: planning vs execution"]
      variation_style: "full_numbers"
      design_note: "Error decomposition showing most CoTSolver errors are planning errors"
    - table_id: "Table 5"
      what_varied: ["selective prediction: correct, incorrect, error types (UNSAT, AMBIG)"]
      variation_style: "full_numbers"
      design_note: "Unique to SAT approach — solver feedback enables abstaining from uncertain predictions"
  supplementary_tables:
    in_appendix: true
    content: "Dataset statistics, prompts, exemplar variations (Table 7), cross-model results (Table 6)"
    reason: "Generalization analysis and prompt details too detailed for main text"
```

---

## 27. xu2024symbcot.yaml
```yaml
paper_key: "xu2024symbcot"
title: "Faithful Logical Reasoning via Symbolic Chain-of-Thought"
venue: "ACL 2024"
full_text_available: true

research:
  baselines: ["Naive Prompting", "CoT", "CoT-SC", "ToT", "CR (Cumulative Reasoning)", "DetermLR", "Logic-LM"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "execution_rate", direction: "higher_better"}
    - {name: "faithfulness_rate", direction: "higher_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogicalDeduction", size: "300"}
    - {name: "AR-LSAT", size: "230"}
  ablation_dimensions: ["module_contribution (Translator/Planner/Solver/Verifier)", "symbolic_structure (FOL vs CO)", "model_type (GPT-3.5 vs GPT-4)", "reasoning_depth"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "GPT-3.5-turbo-0613, GPT-4-0613"}
  method_family: "fully LLM-based symbolic CoT (no external solver)"

positioning:
  core_claim: "A fully LLM-based framework that integrates symbolic expressions and logic rules into CoT achieves better robustness, faithfulness, and accuracy than external-solver approaches, while scaling better with stronger models"
  key_results: "GPT-4 avg 88.47% (+7.88% over Logic-LM); 100% execution rate (vs Logic-LM ~80%); unfaithful reasoning reduced from 6% to 0% with Verifier; +24.3% improvement from GPT-3.5→GPT-4 (vs Logic-LM +19.9%)"
  limitations:
    - "Only evaluated FOL and Constraint Optimization symbolic structures"
    - "High API cost due to extended symbolic reasoning chains"
    - "Does not enhance LLM's planning capability — relies on LLM's inherent planning"
  relation_to_us: "competitor"

narrative:
  story_type: "突破局限型"
  hook: "Achieving human-like logical reasoning capabilities is crucial for realizing AGI"
  tension: "Existing neurosymbolic systems (LINC, Logic-LM) use LLMs merely as translators, not enhancing LLM's own reasoning; over-reliance on external solvers causes inflexibility, information loss, and unexplainability"
  key_insight: "Section 3 — combining symbolic expressions with natural language in CoT leverages mutual strengths: 'freely expressed implicit intents and contextual information in natural language and rigorous expression in symbolic forms'"
  argument_chain: "CoT unfaithful for logic → external solvers lose information → hybrid symbolic+NL CoT → plan-then-solve with verification → 5-dataset validation + faithfulness analysis"
  contribution_framing: "3 contributions: (1) fully LLM-based framework without external tools, (2) integration of symbolic+NL expressions, (3) plan-then-solve + verification for faithfulness"
  intro_structure: "6 paragraphs: (1) AGI motivation, (2) CoT background, (3) CoT limitations for logic, (4) SymbCoT design with 3 aspects, (5) experimental results, (6) contribution list"
  notable_technique: "Positioning against existing neurosymbolic systems by reframing external solvers as a liability (information loss, inflexibility) rather than a strength"

figures:
  figure_count: 8
  figure1:
    type: "problem_illustration"
    description: "Side-by-side comparison of CoT (overgeneralizes) vs SymbCoT (correctly reasons with symbolic premises and verification) on a logical reasoning problem"
    narrative_role: "Demonstrates CoT's unfaithfulness and SymbCoT's faithfulness on a concrete example"
    design_elements: ["side-by-side layout", "red X / green check marks", "highlighted error text", "symbolic formula display"]
    visual_style: "Two-column with color-coded correctness annotations, showing both the reasoning process and final answer"
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths (0-5) on ProofWriter"
      how_gain_highlighted: "SymbCoT maintains high accuracy while baselines degrade; red dual-head arrow shows improvement gap"
      design_note: "Critical depth analysis showing advantage grows with complexity — same pattern as LINC and Logic-LM"
    - figure_id: "Figure 5"
      viz_type: "bar_chart"
      what_compared: "Execution rate across 5 datasets: Logic-LM vs SymbCoT"
      how_gain_highlighted: "SymbCoT achieves 100% across all datasets vs Logic-LM's variable rates"
      design_note: "Strongest evidence against external-solver approaches"
    - figure_id: "Figure 8"
      viz_type: "bar_chart"
      what_compared: "GPT-3.5 vs GPT-4 improvement for each method"
      how_gain_highlighted: "SymbCoT shows largest improvement (+24.3%), demonstrating better scaling with model capability"
      design_note: "Model scaling argument — fully LLM-based approach benefits more from stronger models"
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "grouped_bar"
      dimensions_varied: ["module combinations: full vs w/o Planner&Solver&Verifier vs w/o Translator&Planner&Solver&Verifier"]
      design_note: "6-panel ablation across datasets, color-coded by module configuration"
  figure_narrative_role: "Fig1(motivation) → Fig2(method overview) → Fig3(ablation) → Fig4(depth) → Fig5(execution rate) → Fig6(error analysis) → Fig7(faithfulness) → Fig8(model scaling)"

tables:
  table_count: 2
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets (PrOntoQA, ProofWriter, FOLIO) + Avg"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best + underline_second"
    statistical_reporting: "delta improvement in brackets below best"
    num_baselines: 7
    design_note: "Split by GPT-3.5 and GPT-4 sections; includes many baselines (7) for comprehensive comparison"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["symbolic representation: CO on LogicalDeduction and AR-LSAT"]
      variation_style: "full_numbers"
      design_note: "Demonstrates generalizability across symbolic structures"
  supplementary_tables:
    in_appendix: true
    content: "Symbolic structure details, dataset descriptions, baseline configurations, full prompt templates"
    reason: "Detailed prompt engineering and configuration too long for main text"
```

---

## 28. xiong2024uncertainty.yaml
```yaml
paper_key: "xiong2024uncertainty"
title: "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs"
venue: "ICLR 2024"
full_text_available: true

research:
  baselines: ["Vanilla prompting", "white-box methods (logit-based)"]
  metrics:
    - {name: "ECE (Expected Calibration Error)", direction: "lower_better"}
    - {name: "AUROC", direction: "higher_better"}
    - {name: "AUPRC", direction: "higher_better"}
  datasets:
    - {name: "CommonsenseQA", size: "commonsense"}
    - {name: "TruthfulQA", size: "commonsense"}
    - {name: "GSM8K", size: "arithmetic"}
    - {name: "DateUnderstanding", size: "symbolic"}
    - {name: "Professional Law/Medicine/Psychology", size: "professional knowledge"}
    - {name: "Business Ethics", size: "ethics"}
  ablation_dimensions: ["prompting_strategy (Vanilla/CoT/Self-Probing/Multi-Step/Top-K)", "sampling_method (Self-Random/Prompting/Misleading)", "aggregation (Consistency/Avg-Conf/Pair-Rank)"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "GPT-3, GPT-3.5, GPT-4, Vicuna-13B, LLaMA-2-70B"}
  method_family: "black-box confidence elicitation / uncertainty estimation"

positioning:
  core_claim: "LLMs are systematically overconfident when verbalizing confidence (concentrating in 80-100% range), but consistency-based multi-sample methods can substantially improve calibration, especially on structured reasoning tasks"
  key_results: "GSM8K AUROC: 54.8% → 92.7% with consistency-based sampling; white-box vs black-box gap is narrow (AUROC 0.522 vs 0.605); Top-K + Self-Random + Avg-Conf is recommended pipeline"
  limitations:
    - "Professional knowledge tasks remain persistently challenging for all methods"
    - "Black-box methods still trail white-box approaches"
    - "Verbalized confidence mimics human expression patterns (multiples of 5) rather than reflecting true uncertainty"
  relation_to_us: "complementary"

narrative:
  story_type: "化繁为简型"
  hook: "LLMs' tendency to be overconfident poses potential risks for safe deployment"
  tension: "Existing uncertainty methods require model internals (logits, embeddings) — inapplicable to black-box APIs like GPT-4"
  key_insight: "Section 3 — organizing confidence elicitation as prompting × sampling × aggregation creates a systematic design space, revealing that sampling multiple responses is the most impactful component"
  argument_chain: "LLMs overconfident → need black-box uncertainty → systematic 3-component framework → prompting helps calibration but not failure prediction → sampling is the key lever → practical recommendation"
  contribution_framing: "3 contributions: (1) systematic framework for confidence elicitation, (2) comprehensive evaluation across 5 reasoning types and 5 models, (3) practical recommendations"
  intro_structure: "4 paragraphs: (1) LLM deployment risk from overconfidence, (2) black-box constraint, (3) framework overview and approach, (4) key findings and recommendations"
  notable_technique: "The prompting × sampling × aggregation decomposition turns an empirical study into a reusable design framework"

figures:
  figure_count: 6
  figure1:
    type: "method_overview"
    description: "Three-component framework: prompting strategies (5 types) → sampling methods (3 types) → aggregation techniques (3 types)"
    narrative_role: "Establishes the systematic design space for confidence elicitation"
    design_elements: ["three-stage pipeline", "enumeration of options at each stage", "flow arrows"]
    visual_style: "Horizontal pipeline with branching options at each stage"
  result_figures:
    - figure_id: "confidence distribution figure"
      viz_type: "bar_chart"
      what_compared: "Distribution of verbalized confidence values"
      how_gain_highlighted: "Shows clustering in 80-100% range, illustrating overconfidence"
      design_note: "Powerful visual evidence for the overconfidence claim"
  ablation_figures:
    - figure_id: "component comparison figures"
      viz_type: "grouped_bar"
      dimensions_varied: ["prompting strategy", "sampling method", "aggregation technique"]
      design_note: "Systematic comparison across the 3-component design space"
  figure_narrative_role: "Fig1(framework) → confidence distribution → component-wise analysis → task-specific results"

tables:
  table_count: 4
  main_result_table:
    table_id: "main results table"
    row_axis: "methods (prompting × sampling × aggregation combinations)"
    col_axis: "datasets × metrics (ECE, AUROC, AUPRC)"
    row_organization: "by_category"
    col_organization: "grouped_by_metric"
    highlight_strategy: "bold_best"
    statistical_reporting: "mean across datasets"
    num_baselines: 5
    design_note: "Large table covering 3 metrics × 8 datasets × multiple method combinations"
  ablation_tables:
    - table_id: "component ablation"
      what_varied: ["prompting strategy", "sampling method", "aggregation technique"]
      variation_style: "full_numbers"
      design_note: "Isolates each component's contribution systematically"
  supplementary_tables:
    in_appendix: true
    content: "Per-dataset breakdowns, per-model results, prompt templates"
    reason: "Full combinatorial results too large for main text"
```

---

All 28 YAML files have been read and their complete contents are provided above in full detail, preserving every field and every value exactly as they appear in the original files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccd99a97-c514-402e-89fa-71858529a982",
  "isSidechain": true,
  "agentId": "ad9e4baebe5f13e88",
  "requestId": "req_011CbFLj62Yc5r7SAZ3awVjD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9076bcc-411c-4498-8ee5-658926df37f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a476873e-a266-4886-be23-a1b5b55d76bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Suh1TtQrjikxgyEAvyRJaE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 28615,
      "cache_read_input_tokens": 14980,
      "output_tokens": 21926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 21926,
          "cache_read_input_tokens": 14980,
          "cache_creation_input_tokens": 28615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28615,
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
