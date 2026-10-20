# Research conversation: Read ALL 25 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/ an

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa334bf6bcdbf7cc3.jsonl`
- **Structured JSON:** [`5be0abd267f5bbe60868.json`](../../sessions/5b/5be0abd267f5bbe60868.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-22T16:32:32.784Z_

Read ALL 25 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/ and return their FULL contents concatenated. The files are:

monitoring_ai_review.yaml, min_k_percent.yaml, reliable_detection.yaml, detection_possibilities.yaml, detectgpt.yaml, intrinsic_dimension.yaml, dsir.yaml, watermark_llm.yaml, curious_decline.yaml, markovian_chains.yaml, paraphrase_evades.yaml, qurating.yaml, fast_detectgpt.yaml, gltr.yaml, diveye.yaml, curse_of_recursion.yaml, ood_baseline.yaml, synthid_text.yaml, nucleus_sampling.yaml, dna_gpt.yaml, uchendu_attribution.yaml, writing_diversity.yaml, strong_model_collapse.yaml, broken_telephone.yaml, binoculars.yaml

Read every single file completely (do not truncate). Return all contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "509cb75d-757e-4287-af1c-a3d16da1da79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T16:32:36.846Z_

I'll read all 25 YAML files from the specified directory. Let me start by reading them all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "509cb75d-757e-4287-af1c-a3d16da1da79",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac74515d-cf9e-4c26-9a63-ff43d170e786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 3 · 2026-05-22T16:32:37.255Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bb5fxKwBjLNUyvSdqFjjyN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/monitoring_ai_review.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac74515d-cf9e-4c26-9a63-ff43d170e786",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dc0859d8-3904-43cf-83bf-2f1ce827a48a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 4 · 2026-05-22T16:32:37.262Z_

<details><summary>↩ Tool result · `toolu_01Bb5fxKwBjLNUyvSdqFjjyN`</summary>

```text
1	paper_key: "monitoring_ai_review"
2	title: "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews"
3	venue: "ICML 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["expert-written reference texts", "AI-generated reference texts"]
8	  metrics:
9	    - {name: "estimated LLM-modified fraction", direction: "descriptive"}
10	  datasets:
11	    - {name: "ICLR 2024 peer reviews", size: "unknown"}
12	    - {name: "NeurIPS 2023 peer reviews", size: "unknown"}
13	    - {name: "CoRL 2023 peer reviews", size: "unknown"}
14	    - {name: "EMNLP 2023 peer reviews", size: "unknown"}
15	  ablation_dimensions: ["reviewer confidence level", "submission deadline proximity", "rebuttal engagement"]
16	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
17	  method_family: "corpus-level statistical estimation (maximum likelihood)"
18	
19	positioning:
20	  core_claim: "Develops a maximum likelihood approach to estimate the fraction of LLM-modified text in large corpora, finding 6.5-16.9% of AI conference peer reviews are substantially LLM-modified."
21	  key_results: "N/A - abstract only"
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
  "parentUuid": "dc0859d8-3904-43cf-83bf-2f1ce827a48a",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "27dce84d-5e94-41ef-bc96-8e5d8433df08",
  "sourceToolAssistantUUID": "dc0859d8-3904-43cf-83bf-2f1ce827a48a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T16:32:38.248Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NWyLf6cFsE9dNnXCkaK2kP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/min_k_percent.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27dce84d-5e94-41ef-bc96-8e5d8433df08",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7390eafb-fb46-4985-88c2-fd7f3187dc50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 6 · 2026-05-22T16:32:38.254Z_

<details><summary>↩ Tool result · `toolu_01NWyLf6cFsE9dNnXCkaK2kP`</summary>

```text
1	paper_key: "min_k_percent"
2	title: "Detecting Pretraining Data from Large Language Models"
3	venue: "ICLR 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["reference model-based detection methods"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	    - {name: "improvement over previous methods", direction: "higher_better"}
11	  datasets:
12	    - {name: "WikiMIA", size: "dynamic benchmark"}
13	  ablation_dimensions: ["percentage k threshold", "copyrighted book detection", "contaminated downstream examples", "privacy auditing"]
14	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
15	  method_family: "zero-shot membership inference (token probability outlier detection)"
16	
17	positioning:
18	  core_claim: "Proposes Min-K% Prob, a reference-free method that detects pretraining data by identifying text with outlier low-probability tokens, achieving 7.4% improvement on WikiMIA over prior methods."
19	  key_results: "N/A - abstract only"
20	  limitations: ["N/A"]
21	  relation_to_us: "foundation"
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
  "parentUuid": "7390eafb-fb46-4985-88c2-fd7f3187dc50",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "ce04a3d3-9955-4498-9603-71699dc83aff",
  "sourceToolAssistantUUID": "7390eafb-fb46-4985-88c2-fd7f3187dc50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T16:32:38.782Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3eDcR9cPy9xZF3WGaV76Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/reliable_detection.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce04a3d3-9955-4498-9603-71699dc83aff",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e757cb9-cfc6-4350-b19b-fd7eb8619c0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 8 · 2026-05-22T16:32:38.809Z_

<details><summary>↩ Tool result · `toolu_01Q3eDcR9cPy9xZF3WGaV76Q`</summary>

```text
1	paper_key: "reliable_detection"
2	title: "Can AI-Generated Text be Reliably Detected?"
3	venue: "ICLR 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["watermarking-based detectors", "neural network-based detectors", "zero-shot classifiers", "retrieval-based detectors"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	    - {name: "detection accuracy under attack", direction: "higher_better"}
11	    - {name: "Total Variation distance", direction: "descriptive"}
12	  datasets:
13	    - {name: "passages of ~300 tokens", size: "unknown"}
14	  ablation_dimensions: ["recursive paraphrasing attack strength", "spoofing attack on watermarked LLMs"]
15	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
16	  method_family: "adversarial attack analysis on AI text detectors (recursive paraphrasing)"
17	
18	positioning:
19	  core_claim: "Demonstrates that AI text detectors are unreliable in practice via recursive paraphrasing attacks, and provides theoretical bounds connecting best-possible detector AUROC to Total Variation distance between human and AI text distributions."
20	  key_results: "N/A - abstract only"
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
  "parentUuid": "1e757cb9-cfc6-4350-b19b-fd7eb8619c0b",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "1db120b4-9fab-4ab3-ae57-d78ee7c49c9a",
  "sourceToolAssistantUUID": "1e757cb9-cfc6-4350-b19b-fd7eb8619c0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T16:32:38.844Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Na1R2ZiHLbfisoSX7fPRN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/detection_possibilities.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1db120b4-9fab-4ab3-ae57-d78ee7c49c9a",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d1e034d-d51d-49d5-99f7-408c44c97101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 10 · 2026-05-22T16:32:38.857Z_

<details><summary>↩ Tool result · `toolu_017Na1R2ZiHLbfisoSX7fPRN`</summary>

```text
1	paper_key: "detection_possibilities"
2	title: "Position: On the Possibilities of AI-Generated Text Detection"
3	venue: "ICML 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["RoBERTa-Large-Detector", "RoBERTa-Base-Detector", "GPTZero"]
8	  metrics:
9	    - {name: "sample complexity bounds", direction: "lower_better"}
10	    - {name: "detection accuracy", direction: "higher_better"}
11	  datasets:
12	    - {name: "Xsum", size: "unknown"}
13	    - {name: "Squad", size: "unknown"}
14	    - {name: "IMDb", size: "unknown"}
15	    - {name: "Kaggle FakeNews", size: "unknown"}
16	  ablation_dimensions: ["sample size", "sequence length", "generator model", "dataset domain"]
17	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
18	  method_family: "information-theoretic analysis of detection feasibility"
19	
20	positioning:
21	  core_claim: "Proves that distinguishing human from LLM text is consistently achievable (except when distributions are indistinguishable) and derives sample complexity bounds for reliable detection, validated across multiple datasets and generators (GPT-2, GPT-3.5-Turbo, Llama, Llama-2-13B/70B)."
22	  key_results: "N/A - abstract only"
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
  "parentUuid": "5d1e034d-d51d-49d5-99f7-408c44c97101",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "e5bc3c7a-3958-41a1-a6a6-974505d60b51",
  "sourceToolAssistantUUID": "5d1e034d-d51d-49d5-99f7-408c44c97101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T16:32:38.860Z_

<details open><summary>🔧 Tool call — Read · `toolu_016F5nfyjbFvN7cPHDbQFFWD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/detectgpt.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5bc3c7a-3958-41a1-a6a6-974505d60b51",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "509b9d52-b27d-4fab-a833-99f5d2bb3480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 12 · 2026-05-22T16:32:38.865Z_

<details><summary>↩ Tool result · `toolu_016F5nfyjbFvN7cPHDbQFFWD`</summary>

```text
1	paper_key: "detectgpt"
2	title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
3	venue: "ICML 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["zero-shot detection baselines (unspecified)"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	  datasets:
11	    - {name: "fake news articles (GPT-NeoX 20B)", size: "unknown"}
12	  ablation_dimensions: ["perturbation model choice (T5)", "source model"]
13	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
14	  method_family: "zero-shot detection via log-probability curvature (perturbation-based)"
15	
16	positioning:
17	  core_claim: "Discovers that LLM-sampled text occupies negative curvature regions of the model's log probability function, and leverages this via random perturbations for zero-shot detection, achieving 0.95 AUROC vs 0.81 for the strongest baseline."
18	  key_results: "N/A - abstract only"
19	  limitations: ["N/A"]
20	  relation_to_us: "competitor"
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
  "parentUuid": "509b9d52-b27d-4fab-a833-99f5d2bb3480",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "e77e932d-958c-496c-a60a-6ac57defad8f",
  "sourceToolAssistantUUID": "509b9d52-b27d-4fab-a833-99f5d2bb3480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T16:32:38.932Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VnMdKrMYNXM6FtHe4w51cS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/intrinsic_dimension.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e77e932d-958c-496c-a60a-6ac57defad8f",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c558a42c-1d8e-4b21-9b70-f322ad28729b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 14 · 2026-05-22T16:32:38.938Z_

<details><summary>↩ Tool result · `toolu_01VnMdKrMYNXM6FtHe4w51cS`</summary>

```text
1	paper_key: "intrinsic_dimension"
2	title: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"
3	venue: "NeurIPS 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["SOTA detectors (unspecified in abstract)"]
8	  metrics:
9	    - {name: "intrinsic dimensionality", direction: "descriptive"}
10	    - {name: "detection accuracy", direction: "higher_better"}
11	  datasets:
12	    - {name: "multi-language texts (alphabet-based + Chinese)", size: "unknown"}
13	  ablation_dimensions: ["language", "text domain", "generator model", "human writer proficiency level"]
14	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
15	  method_family: "intrinsic dimension estimation + persistent homology (topological features)"
16	
17	positioning:
18	  core_claim: "Proposes intrinsic dimensionality of text embeddings as a robust detection invariant, finding human texts average ~9 (alphabet-based) vs ~7.5 for AI-generated, with stable cross-domain and cross-model performance outperforming SOTA detectors."
19	  key_results: "N/A - abstract only"
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
  "parentUuid": "c558a42c-1d8e-4b21-9b70-f322ad28729b",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "2e381424-0995-49c7-8427-2630048b292b",
  "sourceToolAssistantUUID": "c558a42c-1d8e-4b21-9b70-f322ad28729b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T16:32:39.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_011ZxtKKejXJr5vaYW4WJoAw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/dsir.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e381424-0995-49c7-8427-2630048b292b",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e0ef7498-e134-49e8-a9f3-fef5f14a09af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 16 · 2026-05-22T16:32:39.014Z_

<details><summary>↩ Tool result · `toolu_011ZxtKKejXJr5vaYW4WJoAw`</summary>

```text
1	paper_key: "dsir"
2	title: "Data Selection for Language Models via Importance Resampling"
3	venue: "NeurIPS 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["expert curation", "random selection", "heuristic filtering"]
8	  metrics:
9	    - {name: "KL reduction", direction: "higher_better"}
10	    - {name: "GLUE benchmark score", direction: "higher_better"}
11	    - {name: "correlation with downstream accuracy", direction: "higher_better"}
12	  datasets:
13	    - {name: "The Pile", size: "100M documents"}
14	    - {name: "GLUE benchmark", size: "unknown"}
15	    - {name: "Wikipedia and books", size: "unknown"}
16	  ablation_dimensions: ["target distribution", "feature space", "n-gram hash features"]
17	  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "processes 100M docs in 4.5 hours"}
18	  method_family: "importance resampling for data selection (hashed n-gram features)"
19	
20	positioning:
21	  core_claim: "Proposes DSIR, a scalable data selection method using importance resampling with hashed n-gram features, achieving strong correlation (r=0.82) between KL reduction and downstream task performance."
22	  key_results: "N/A - abstract only"
23	  limitations: ["N/A"]
24	  relation_to_us: "orthogonal"
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
  "parentUuid": "e0ef7498-e134-49e8-a9f3-fef5f14a09af",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "c4519f56-e1d4-463f-b8b8-820123ab8fcb",
  "sourceToolAssistantUUID": "e0ef7498-e134-49e8-a9f3-fef5f14a09af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T16:32:39.191Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EEJKXR8JaT9hBcUcufUkAP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/watermark_llm.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4519f56-e1d4-463f-b8b8-820123ab8fcb",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23c5edee-79e3-4050-9632-6dd5429adcae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 18 · 2026-05-22T16:32:39.195Z_

<details><summary>↩ Tool result · `toolu_01EEJKXR8JaT9hBcUcufUkAP`</summary>

```text
1	paper_key: "watermark_llm"
2	title: "A Watermark for Large Language Models"
3	venue: "ICML 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["unwatermarked generation"]
8	  metrics:
9	    - {name: "p-value (statistical test)", direction: "lower_better"}
10	    - {name: "text quality (human evaluation)", direction: "higher_better"}
11	  datasets:
12	    - {name: "OPT model generations", size: "unknown"}
13	  ablation_dimensions: ["green list size", "soft promotion strength", "text length"]
14	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
15	  method_family: "token-level watermarking (green list / red list partitioning)"
16	
17	positioning:
18	  core_claim: "Proposes a watermarking framework for LLMs that embeds invisible signals by softly promoting 'green' tokens during sampling, detectable via a statistical test with interpretable p-values without API access, with negligible quality impact."
19	  key_results: "N/A - abstract only"
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
  "parentUuid": "23c5edee-79e3-4050-9632-6dd5429adcae",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "24e319ac-de89-4d8b-8526-dc773b62390a",
  "sourceToolAssistantUUID": "23c5edee-79e3-4050-9632-6dd5429adcae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T16:32:39.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F2XRch92MhqtbkC9GjuFf6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/curious_decline.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24e319ac-de89-4d8b-8526-dc773b62390a",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a09feb87-442f-486c-9f15-8b5fc1154053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 20 · 2026-05-22T16:32:39.270Z_

<details><summary>↩ Tool result · `toolu_01F2XRch92MhqtbkC9GjuFf6`</summary>

```text
1	paper_key: "curious_decline"
2	title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
3	venue: "NAACL 2024 Findings"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Human-generated text (ground truth baseline)"
9	    - "OPT-350M finetuned on human data only (Iteration 0)"
10	  metrics:
11	    - {name: "Type-Token Ratio (TTR)", direction: "higher_better"}
12	    - {name: "Distinct-2", direction: "higher_better"}
13	    - {name: "Distinct-3", direction: "higher_better"}
14	    - {name: "1-Self-BLEU", direction: "higher_better"}
15	    - {name: "Syntactic Diversity (Div_syn)", direction: "higher_better"}
16	    - {name: "Semantic Diversity (Div_sem)", direction: "higher_better"}
17	    - {name: "Perplexity", direction: "lower_better"}
18	  datasets:
19	    - {name: "XL-SUM", size: "306,522 train / 11,535 test", task: "news summarization"}
20	    - {name: "ACL Anthology bibliography", size: "40,512 train / 2,132 test", task: "scientific abstract generation"}
21	    - {name: "WritingPrompts", size: "272,600 train / 15,138 test", task: "story generation"}
22	  ablation_dimensions:
23	    - "Task entropy level (low/medium/high creativity demands)"
24	    - "Synthetic data filtering (RoBERTa-CoLA acceptability filter, bottom 20% discarded)"
25	    - "Human data mixing (60% human held out, 10% injected per iteration)"
26	    - "Number of recursive iterations (1-6)"
27	  training_recipe:
28	    model: "OPT-350M (fresh instance per iteration)"
29	    optimizer: "AdamW"
30	    epochs: 5
31	    hardware: "2x NVIDIA RTX A6000"
32	    decoding_news: "p=0.1, tau=0.3, max_new_tokens=50"
33	    decoding_abstract: "p=0.5, tau=0.5, max_new_tokens=300"
34	    decoding_story: "p=0.9, tau=0.7, max_new_tokens=500"
35	    total_compute: "~700 GPU hours for story generation alone"
36	  method_family: "Recursive finetuning on self-generated synthetic data (model collapse investigation)"
37	
38	positioning:
39	  core_claim: "Recursive training on synthetic data causes a remarkable, consistent decline in linguistic diversity—particularly syntactic diversity—even when task performance (perplexity) appears to improve, revealing that standard metrics mask a fundamental quality degradation."
40	  key_results: >
41	    Story generation TTR: Human 2.23% -> Iter1 0.84% -> Iter6 0.61%;
42	    Story Distinct-3: Human 70.6% -> Iter1 44.2% -> Iter6 38.6%;
43	    Story syntactic diversity: Human 4.84 -> Iter1 4.23 -> Iter6 1.96;
44	    Perplexity drops (improves) from 14.1 to 2.70 despite diversity collapse;
45	    Filtering synthetic data amplifies decline; mixing 10% human data per iteration insufficient to prevent it.
46	  limitations:
47	    - "Monolingual (English only); metrics rely on language-specific tools"
48	    - "OPT-350M only; larger models unexplored due to 700 GPU-hour cost"
49	    - "Cannot access real LM-generated web content; no reliable LM detection for web data"
50	    - "Single architecture (decoder-only); encoder-decoder unexplored"
51	  relation_to_us: "foundation"
52	
53	narrative:
54	  story_type: "突破局限型"
55	  hook: >
56	    Opens with scaling laws' promise of predictable improvement, then pivots sharply:
57	    high-quality data is running out (17 trillion tokens, 4-5% annual growth),
58	    and Meta's Llama 2 already consumed ~2 trillion—we are within an order of magnitude of exhaustion.
59	    This data scarcity frames synthetic data as simultaneously necessary and dangerous.
60	  tension: >
61	    Prior work on model collapse focused on task performance degradation (distribution tails disappearing,
62	    converging to uniform behaviors). But no one has systematically measured LINGUISTIC diversity—
63	    the quality dimension that matters for creative and varied text generation.
64	    The gap: we know synthetic training hurts performance, but we don't know how it reshapes language itself.
65	  key_insight: >
66	    Revealed through the three-task experimental ladder (Section 4): higher-entropy tasks
67	    (story generation) suffer the MOST diversity loss, and syntactic diversity collapses
68	    the fastest while semantic diversity stays deceptively stable. The counterintuitive finding
69	    is in Section 4.3—filtering synthetic data for quality AMPLIFIES diversity loss
70	    (because filters favor common patterns, removing diverse samples).
71	  argument_chain: >
72	    Data exhaustion crisis → synthetic data as inevitable supplement →
73	    prior work shows model collapse in performance → but what about linguistic diversity? →
74	    develop comprehensive diversity metrics (lexical + semantic + syntactic) →
75	    recursive finetuning across 3 tasks with varying entropy →
76	    diversity consistently declines, worst for creative tasks →
77	    syntactic diversity most vulnerable, semantic deceptively stable →
78	    mitigation attempts (filtering, mixing) fail → call for diversity-aware training
79	  contribution_framing: >
80	    Framed as two research questions rather than numbered contributions:
81	    (1) "How can linguistic diversity be quantified effectively?"
82	    (2) "Does recursive training on synthetic text reduce linguistic diversity?"
83	    Novel syntactic diversity metric via Weisfeiler-Lehman graph kernels on dependency trees
84	    is presented as a methodological contribution. The empirical finding is the main result.
85	  intro_structure: >
86	    4 paragraphs:
87	    P1 (Hook): Data exhaustion + scaling laws create tension
88	    P2 (Context): Three modes of synthetic data contamination (pretraining, finetuning, single-task)
89	    P3 (Gap): Model collapse known, but linguistic diversity unexamined
90	    P4 (This work): Metrics + experiments + key finding summary
91	  notable_technique: >
92	    The three-task design with explicitly varying "entropy levels" (low/medium/high creativity)
93	    creates a natural experimental gradient that makes the diversity-entropy interaction
94	    visible without additional analysis. The qualitative example in Table 1 (scientific abstracts
95	    progressively fixating on URLs and licensing statements) is a memorable illustration
96	    that makes the abstract metric decline tangible.
97	
98	figures:
99	  figure_count: 5
100	  figure1:
101	    type: "method_overview"
102	    description: >
103	      Diagram of the recursive tuning-generation process across 6 iterations.
104	      Shows Data(0) -> Base(1) -> Model(1) -> Data(1) -> Base(2) -> Model(2) -> ... chain.
105	      Each Base is a fresh OPT-350M instance finetuned on the previous iteration's data.
106	    narrative_role: >
107	      Establishes the experimental protocol immediately—readers understand the recursive
108	      pipeline before any results are presented. Critical for grasping why diversity degrades:
109	      each iteration's training data is entirely synthetic from the prior model.
110	    design_elements:
111	      - "Sequential flow diagram with numbered iterations"
112	      - "Clear Base/Model/Data distinction"
113	      - "Arrow-based pipeline showing data flow"
114	    visual_style: >
115	      Linear left-to-right pipeline diagram. Clean boxes for each component
116	      (Base, Model, Data) connected by arrows. Iteration numbers as labels.
117	      Minimal color, focuses on structural clarity.
118	  result_figures:
119	    - figure_id: "Figure 2"
120	      viz_type: "line_plot"
121	      what_compared: >
122	        Lexical diversity (Distinct-3) and syntactic diversity across iterations 1-6
123	        under three conditions: pure synthetic, with filtering, with mixed human data.
124	        Story generation task.
125	      how_gain_highlighted: >
126	        Human baseline shown as reference level; all three conditions decline below it.
127	        The counterintuitive finding (filtering amplifies decline) is visually striking
128	        as the filtered line drops faster than pure synthetic.
129	      design_note: >
130	        Two-panel layout (a: lexical, b: syntactic). Lines with markers for each condition.
131	        Human baseline as horizontal reference. The visual immediately communicates
132	        that all mitigation attempts fail—powerful for the paper's pessimistic message.
133	  ablation_figures:
134	    - figure_id: "Figure 2 (serves dual purpose)"
135	      viz_type: "line_plot"
136	      dimensions_varied:
137	        - "Data regime (pure synthetic vs. filtered vs. mixed human)"
138	        - "Iteration number (1-6)"
139	      design_note: >
140	        Ablation is embedded in the main result figure rather than separated,
141	        making the comparison immediate. Three lines per panel keeps it readable.
142	  figure_narrative_role: >
143	    Figure 1 (method overview) → Table 1 (qualitative degradation example) →
144	    Table 2 (comprehensive quantitative results) → Figure 2 (mitigation failure visualization).
145	    Appendix: Figure 3 (word frequency histograms), Figure 4 (t-SNE syntactic embeddings),
146	    Figure 5 (t-SNE semantic embeddings)—supporting evidence for mechanisms.
147	
148	tables:
149	  table_count: 3
150	  main_result_table:
151	    table_id: "Table 2"
152	    row_axis: "methods (iterations 1-6 + human baseline)"
153	    col_axis: "metrics (Perplexity, TTR, Distinct-2, Distinct-3, 1-Self-BLEU, Div_syn, Div_sem)"
154	    row_organization: "by_iteration"
155	    col_organization: "grouped_by_metric"
156	    highlight_strategy: "No bold/underline; human baseline as separate row for visual comparison"
157	    statistical_reporting: "Single run values (no std reported for main table)"
158	    num_baselines: 1
159	    design_note: >
160	      Three task panels (News, Abstract, Story) stacked vertically within one table.
161	      The table's power is in showing perplexity IMPROVING (2.48 → lower) while all diversity
162	      metrics worsen—the mismatch between standard evaluation and diversity is the visual punch.
163	      7 columns x ~24 rows, dense but organized by task sections.
164	  ablation_tables:
165	    - table_id: "Table 1"
166	      what_varied: ["Recursive iteration number (Human, Iter 1, 3, 5)"]
167	      variation_style: "full_numbers"
168	      design_note: >
169	        Qualitative example table showing actual generated abstract text across iterations.
170	        Not a metrics table—a TEXT table showing progressive fixation on URLs and
171	        licensing statements. Powerful because it makes the metric decline visceral.
172	        Functions as both example and ablation over iterations.
173	  supplementary_tables:
174	    in_appendix: true
175	    content: >
176	      Table 3: Average text lengths post-truncation (verifying fair comparison across iterations).
177	      Appendix also contains Figures 3-5 (word frequency histograms, t-SNE plots for
178	      syntactic and semantic embeddings).
179	    reason: >
180	      Length verification is a methodological detail; t-SNE plots support mechanistic
181	      claims but aren't essential for the main argument. Main text keeps only the
182	      metrics table and mitigation figure.
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a09feb87-442f-486c-9f15-8b5fc1154053",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "aba8bb02-1d4a-4280-a1e9-4b0ad10bb449",
  "sourceToolAssistantUUID": "a09feb87-442f-486c-9f15-8b5fc1154053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T16:32:39.296Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NzccPPLeh2KRquoSJQ3ZZM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/markovian_chains.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aba8bb02-1d4a-4280-a1e9-4b0ad10bb449",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ef774f3f-d16a-439b-9233-2b6357839595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 22 · 2026-05-22T16:32:39.301Z_

<details><summary>↩ Tool result · `toolu_01NzccPPLeh2KRquoSJQ3ZZM`</summary>

```text
1	paper_key: "markovian_chains"
2	title: "Markovian Generation Chains in Large Language Models"
3	venue: "arXiv 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: []
8	  metrics:
9	    - {name: "output convergence pattern", direction: "descriptive"}
10	    - {name: "sentence diversity", direction: "descriptive"}
11	  datasets:
12	    - {name: "simulated iterative LLM outputs", size: "unknown"}
13	  ablation_dimensions: ["temperature parameter", "initial input sentence", "iteration count", "task type (rephrasing vs translation)"]
14	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
15	  method_family: "Markov chain analysis of iterative LLM inference"
16	
17	positioning:
18	  core_claim: "Formalizes iterative LLM inference as Markovian generation chains, showing outputs either converge to recurrent sets or continue producing novel sentences, with diversity increasing or decreasing depending on temperature and initial input."
19	  key_results: "N/A - abstract only"
20	  limitations: ["N/A"]
21	  relation_to_us: "foundation"
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
  "parentUuid": "ef774f3f-d16a-439b-9233-2b6357839595",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "a301eb21-d1e4-4404-882f-402516344bd3",
  "sourceToolAssistantUUID": "ef774f3f-d16a-439b-9233-2b6357839595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T16:32:39.812Z_

<details open><summary>🔧 Tool call — Read · `toolu_0117w82j83FWq2ApE5C3rMKj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/paraphrase_evades.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a301eb21-d1e4-4404-882f-402516344bd3",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fbed608d-24f3-4310-a689-562f3ad6284a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 24 · 2026-05-22T16:32:39.816Z_

<details><summary>↩ Tool result · `toolu_0117w82j83FWq2ApE5C3rMKj`</summary>

```text
1	paper_key: "paraphrase_evades"
2	title: "Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense"
3	venue: "NeurIPS 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["watermarking detectors", "GPTZero", "DetectGPT", "OpenAI text classifier"]
8	  metrics:
9	    - {name: "detection accuracy", direction: "higher_better"}
10	    - {name: "false positive rate", direction: "lower_better"}
11	  datasets:
12	    - {name: "GPT3.5-davinci-003 generations", size: "unknown"}
13	    - {name: "T5-XXL fine-tuned generations", size: "15M generations"}
14	  ablation_dimensions: ["lexical diversity", "content reordering", "paraphrase strength"]
15	  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "unknown"}
16	  method_family: "adversarial paraphrasing attack + retrieval-based defense"
17	
18	positioning:
19	  core_claim: "Builds DIPPER (11B paraphraser) that drops DetectGPT accuracy from 70.3% to 4.6% at 1% FPR, and proposes a retrieval-based defense that searches previously generated sequences for semantic similarity, significantly outperforming existing detectors on paraphrased text."
20	  key_results: "N/A - abstract only"
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
  "parentUuid": "fbed608d-24f3-4310-a689-562f3ad6284a",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "c713a44c-d1c7-483a-80ae-3f8bc080c2ee",
  "sourceToolAssistantUUID": "fbed608d-24f3-4310-a689-562f3ad6284a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T16:32:39.851Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AqFDyvTp6GGgf8GhCFv7Gv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/qurating.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c713a44c-d1c7-483a-80ae-3f8bc080c2ee",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2ed21ab3-bb22-4d71-b519-0506661c65ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 26 · 2026-05-22T16:32:39.856Z_

<details><summary>↩ Tool result · `toolu_01AqFDyvTp6GGgf8GhCFv7Gv`</summary>

```text
1	paper_key: "qurating"
2	title: "QuRating: Selecting High-Quality Data for Training Language Models"
3	venue: "ICML 2024"
4	full_text_available: true  # via HuggingFace papers page; arXiv HTML not available
5	
6	research:
7	  baselines:
8	    - Uniform sampling
9	    - Uniform sampling +50% data
10	    - DSIR (Wikipedia target)
11	    - DSIR (Book target)
12	    - Perplexity filtering (low perplexity)
13	    - Inverse perplexity sampling
14	    - Criteria mix (combining all 4 criteria)
15	  metrics:
16	    - {name: "Perplexity", direction: "lower_better"}
17	    - {name: "Average ICL accuracy (10 tasks)", direction: "higher_better"}
18	    - {name: "ARC-easy", direction: "higher_better"}
19	    - {name: "ARC-challenge", direction: "higher_better"}
20	    - {name: "SciQA", direction: "higher_better"}
21	    - {name: "LogiQA", direction: "higher_better"}
22	    - {name: "BoolQ", direction: "higher_better"}
23	    - {name: "HellaSwag", direction: "higher_better"}
24	    - {name: "PIQA", direction: "higher_better"}
25	    - {name: "WinoGrande", direction: "higher_better"}
26	    - {name: "NQ", direction: "higher_better"}
27	    - {name: "MMLU", direction: "higher_better"}
28	  datasets:
29	    - {name: "SlimPajama (QuRatedPajama)", size: "260B tokens annotated, 30B tokens selected for training"}
30	    - {name: "AboutMe", size: "10M webpages (for bias analysis)"}
31	  ablation_dimensions:
32	    - Quality criterion (writing_style / facts_trivia / educational_value / required_expertise)
33	    - Sampling temperature tau (0.0 top-k / 1.0 / 2.0 / uniform)
34	    - Multi-task vs separate QuRater models
35	    - Random vs pre-trained QuRater initialization
36	    - Curriculum ordering (low-to-high vs high-to-low expertise)
37	  training_recipe:
38	    model_size: "1.3B parameters"
39	    base_model: "Sheared-Llama-1.3B (for QuRater); custom 1.3B LM (for downstream)"
40	    training_tokens: "30B tokens (selected from 260B)"
41	    annotation_cost: "520 H100 GPU hours for corpus annotation"
42	    judgment_source: "GPT-3.5-turbo, 250K pairwise comparisons"
43	    snippet_length: "256-512 tokens for pairwise judgments"
44	    tokenizer: "Llama tokenizer"
45	    sequence_length: 1024
46	  method_family: "Data quality filtering via learned quality ratings (pairwise preference + Bradley-Terry)"
47	
48	positioning:
49	  core_claim: "LLM-based pairwise quality judgments can be distilled into a lightweight scorer that enables quality-diversity balanced data selection, matching 50% more uniform training data with educational value filtering alone."
50	  key_results: "Educational value (tau=2.0): 46.7% avg ICL (+1.8% over uniform 30B baseline), matching uniform 45B baseline; QuRater validation accuracy >93%; GPT-3.5-turbo agreement with humans >91.9% across all criteria"
51	  limitations:
52	    - "Sensitive to LLM biases (language, positional bias in pairwise comparisons)"
53	    - "Results only on 1.3B models; unclear if findings transfer to larger scales"
54	    - "Documented social biases: gender (female roles suppressed), geography (Pacific Islands/SE Asia suppressed), topic (fashion/beauty suppressed by educational value)"
55	    - "Large-scale human quality validation still needed"
56	    - "Maintains original domain proportions; domain reweighting unexplored"
57	  relation_to_us: "complementary"  # QuRating's quality dimensions (especially writing style) inform what distinguishes human vs AI text; their finding that top-k quality selection hurts diversity parallels our interest in diversity loss from AI generation
58	
59	narrative:
60	  story_type: "化繁为简型"  # Turns vague "data quality" into 4 concrete measurable dimensions + simple sampling framework
61	  hook: "Data quality is acknowledged as critical for LLM pre-training but remains poorly defined and hard to measure at scale"
62	  tension: "Existing approaches either use rule-based heuristics (too coarse) or classifier-based filtering (limited to one notion of quality); no framework captures multiple qualitative dimensions"
63	  key_insight: "Pairwise comparisons produce more stable quality judgments than absolute ratings (Kendall tau 0.79 vs 0.61), and a simple temperature-controlled sampling balances quality and diversity better than top-k selection"
64	  argument_chain: "Vague quality notion → decompose into 4 intuitive criteria → pairwise LLM judgments → Bradley-Terry distillation → lightweight QuRater model → temperature-controlled sampling → downstream gains + bias analysis"
65	  contribution_framing: "Three contributions: (1) framework for quality rating via pairwise comparisons, (2) QuRatedPajama 260B corpus with ratings, (3) empirical evidence that educational value selection matches 50% more data"
66	  intro_structure: "~5 paragraphs: P1 motivation (data quality matters), P2 existing approaches and gaps, P3 proposed approach overview, P4 key findings preview, P5 contributions list"
67	  notable_technique: "The 'compute equivalence' framing — showing quality selection matches uniform+50% data is more compelling than reporting raw accuracy gains"
68	
69	figures:
70	  figure_count: 8  # 5 main + 3 appendix
71	  figure1:
72	    type: "method_overview"
73	    description: "Two-path flow diagram showing the QuRating pipeline: top path shows text pair comparison → LLM ranking → judgment collection → QuRater training; bottom path shows web-scale corpus → quality rating → data selection → LM training"
74	    narrative_role: "Provides complete system overview in one figure; establishes the two-stage approach (train rater, then use rater)"
75	    design_elements: ["flow diagram with boxes and arrows", "two parallel paths (annotation vs application)", "clear left-to-right progression"]
76	    visual_style: "Clean pipeline diagram; annotation pipeline on top, application pipeline on bottom; arrows connecting stages"
77	  result_figures:
78	    - figure_id: "Figure 3"
79	      viz_type: "bar_chart"
80	      what_compared: "Win rates of QuRating-selected models vs uniform baseline after instruction fine-tuning"
81	      how_gain_highlighted: "Bar heights directly show win rate advantage for each quality criterion"
82	      design_note: "Bridges pre-training quality selection to instruction-following, showing downstream transfer"
83	    - figure_id: "Figure 4"
84	      viz_type: "distribution_plot"
85	      what_compared: "Quality rating distributions across SlimPajama domains (Wikipedia, Book, StackExchange, Github, ArXiv)"
86	      how_gain_highlighted: "Shows within-domain variance is large, justifying fine-grained selection over domain-level filtering"
87	      design_note: "Validates the premise that quality varies within domains, not just between them"
88	  ablation_figures:
89	    - figure_id: "Figure 5"
90	      viz_type: "heatmap"
91	      dimensions_varied: ["criterion pairs (4x4 correlation matrix)"]
92	      design_note: "Correlation matrix showing criteria are complementary (r=0.29-0.55), justifying multi-dimensional approach"
93	    - figure_id: "Figure 6"
94	      viz_type: "scatter"
95	      dimensions_varied: ["perplexity vs ICL performance across tasks"]
96	      design_note: "Appendix figure demonstrating perplexity is a poor proxy for downstream ICL performance"
97	  figure_narrative_role: "Figure 1 (method overview) → Figure 2 (qualitative examples) → Figure 3 (downstream results) → Figure 4 (distribution analysis) → Figure 5 (criterion correlation) — moves from 'what we do' to 'does it work' to 'why it works'"
98	
99	tables:
100	  table_count: 10  # main tables + appendix tables
101	  main_result_table:
102	    table_id: "Table 1"
103	    row_axis: "methods"
104	    col_axis: "perplexity + 10 ICL tasks grouped by category (reading comprehension, commonsense reasoning, world knowledge) + average"
105	    row_organization: "by_category"  # grouped as: baselines, QuRating variants by criterion and temperature, other baselines
106	    col_organization: "grouped_by_dataset"  # tasks grouped into 3 categories
107	    highlight_strategy: "bold_best per column; comparison against uniform baseline"
108	    statistical_reporting: "single run numbers (no std reported in main table)"
109	    num_baselines: 5  # uniform, uniform+50%, DSIR x2, perplexity filtering
110	    design_note: "16 rows covering criterion x temperature grid; clear separation between QuRating variants and external baselines; the '+50% data' uniform row provides compute-equivalence reference point"
111	  ablation_tables:
112	    - table_id: "Table 6"
113	      what_varied: ["multi-task vs separate models", "random vs pre-trained initialization"]
114	      variation_style: "full_numbers"  # accuracy percentages at different confidence margins
115	      design_note: "Shows multi-task QuRater matches separate per-criterion models, justifying single-model approach"
116	    - table_id: "Table 2"
117	      what_varied: ["quality criterion", "demographic dimensions (topics, roles, regions)"]
118	      variation_style: "full_numbers"  # retention rates
119	      design_note: "Bias analysis table showing amplification/suppression patterns; uses sub-columns for each criterion"
120	  supplementary_tables:
121	    in_appendix: true
122	    content: "Detailed per-task perplexity (Table 8), per-task ICL scores (Table 9), corpus composition (Table 7), validation data sources (Tables 3-4), judgment dataset stats (Table 5), extensive document inspection at quality percentiles (Tables 10-40+)"
123	    reason: "Main table shows aggregated results; appendix provides per-task breakdowns and qualitative evidence at different quality levels"
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ed21ab3-bb22-4d71-b519-0506661c65ae",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "4d7ec690-f5be-4ec6-9e90-57717dfcebdb",
  "sourceToolAssistantUUID": "2ed21ab3-bb22-4d71-b519-0506661c65ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T16:32:40.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MiyY8arPkxYF7ZCLQMkmpJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/fast_detectgpt.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d7ec690-f5be-4ec6-9e90-57717dfcebdb",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "991de9cf-2fe3-4263-867f-71bb30bcaa93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 28 · 2026-05-22T16:32:40.048Z_

<details><summary>↩ Tool result · `toolu_01MiyY8arPkxYF7ZCLQMkmpJ`</summary>

```text
1	paper_key: "fast_detectgpt"
2	title: "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"
3	venue: "ICLR 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - DetectGPT
9	    - NPR
10	    - DNA-GPT
11	    - Likelihood
12	    - LogRank
13	    - Entropy
14	    - LRR
15	    - RoBERTa-base (OpenAI GPT-2 detector)
16	    - RoBERTa-large (OpenAI GPT-2 detector)
17	    - GPTZero
18	  metrics:
19	    - {name: "AUROC", direction: "higher_better"}
20	    - {name: "Relative Improvement", direction: "higher_better", note: "(new-old)/(1.0-old)"}
21	    - {name: "Speedup", direction: "higher_better"}
22	  datasets:
23	    - {name: "XSum", domain: "news articles"}
24	    - {name: "SQuAD", domain: "Wikipedia contexts"}
25	    - {name: "WritingPrompts", domain: "story writing"}
26	    - {name: "WMT16-en", domain: "English translation"}
27	    - {name: "WMT16-de", domain: "German translation"}
28	    - {name: "PubMedQA", domain: "biomedical research QA"}
29	  ablation_dimensions:
30	    - sampling_model_choice
31	    - normalization_effect
32	    - passage_length
33	    - decoding_strategy (top-p, top-k, temperature)
34	    - paraphrasing_attack_robustness
35	    - in_distribution_vs_out_distribution
36	  training_recipe:
37	    optimizer: "N/A (zero-shot, no training)"
38	    lr: "N/A"
39	    hardware: "Tesla A100 GPU"
40	    inference_time: "233 seconds for full evaluation (vs 79113 seconds for DetectGPT)"
41	  method_family: "zero-shot detection via probability curvature"
42	
43	positioning:
44	  core_claim: "Conditional probability curvature at token level is a more fundamental and efficient indicator of machine-generated text than perturbation-based probability curvature, achieving 340x speedup and ~75% relative accuracy improvement over DetectGPT."
45	  key_results: "White-box AUROC 0.9887 (+74.7% relative over DetectGPT); Black-box AUROC 0.9677 (+74.5% relative); ChatGPT detection AUROC 0.9615 (+78.3% relative); GPT-4 detection AUROC 0.9061 (+75.1% relative); 340x speedup (4 min vs 22 hours)"
46	  limitations:
47	    - "Theoretical explorations of why conditional probability curvature works are earmarked for future work"
48	    - "Relies on pre-trained models to span multiple domains/languages; no single model covers all linguistic territories in black-box setting"
49	    - "Focus predominantly on empirical advancements rather than theoretical foundations"
50	  relation_to_us: "competitor"
51	
52	narrative:
53	  story_type: "化繁为简型"
54	  hook: "LLMs have transformed productivity but create risks of fake news, malicious reviews, and plagiarism; the fluency of generated text makes detection 'challenging even for experts.'"
55	  tension: "DetectGPT is the leading zero-shot detector but requires ~100 model calls per passage for perturbation, creating prohibitive computational costs (22 hours for a benchmark)."
56	  key_insight: "Revealed in paragraph 4 of intro—'machines lean towards tokens with higher statistical probability' while 'humans craft sentences based on underlying meanings, intentions, and contexts rather than data statistics.' This asymmetry means conditional probability p(x̃|x) reaches maximum at machine-generated x (positive curvature ~3) vs near zero for human text."
57	  argument_chain: "LLMs create detection need → existing zero-shot methods work but are slow → core hypothesis about token-level selection difference → conditional probability curvature as efficient proxy → single forward pass via conditional independent sampling → 340x speedup + 75% accuracy gain → validated across white-box, black-box, real-world (ChatGPT/GPT-4), cross-domain, cross-language settings"
58	  contribution_framing: "Three numbered contributions: (1) unveiling/validating hypothesis, (2) proposing efficient method, (3) achieving SOTA. Framing emphasizes both conceptual insight and practical gains."
59	  intro_structure: "4 paragraphs: P1=context+risk (LLMs dual nature), P2=related work landscape (supervised vs zero-shot), P3=problem statement (DetectGPT's computational bottleneck), P4=solution+contributions (hypothesis + method + results)"
60	  notable_technique: "The connection revelation—showing the curvature numerator decomposes into Likelihood + Entropy baselines, positioning Fast-DetectGPT as a principled unification rather than just a speedup trick."
61	
62	figures:
63	  figure_count: 5
64	  figure1:
65	    type: "motivation"
66	    description: "Distribution of conditional probability curvatures for human-written vs machine-generated passages across four source models (GPT-2, OPT-2.7, Neo-2.7, GPT-J) on XSum dataset with 30-token prefix."
67	    narrative_role: "Visual proof of core hypothesis—clean separation between human (curvature≈0) and machine (curvature≈3) distributions motivates the entire method."
68	    design_elements: ["overlaid density distributions", "multiple source models in one plot", "clear separation visualization", "contrasting colors for human vs machine"]
69	    visual_style: "Histogram/density plot with overlaid distributions; human texts cluster at 0, machine texts at ~3; four model variants shown to demonstrate generality; single unified panel."
70	  result_figures:
71	    - figure_id: "Figure 3"
72	      viz_type: "line_plot"
73	      what_compared: "ROC curves for multiple detection methods on WritingPrompts dataset"
74	      how_gain_highlighted: "Fast-DetectGPT curve dominates upper-left region; log scale emphasizes differences at low false positive rates"
75	      design_note: "Log-scale ROC is unusual but effective for emphasizing practical operating points (low FPR); dashed random baseline."
76	    - figure_id: "Figure 4"
77	      viz_type: "line_plot"
78	      what_compared: "Detection AUROC vs passage word count for ChatGPT and GPT-4 generations"
79	      how_gain_highlighted: "Fast-DetectGPT shows consistent monotonic improvement; baselines plateau or are inconsistent"
80	      design_note: "Two subplots (ChatGPT/GPT-4) side-by-side; multiple colored lines per detector; demonstrates robustness to passage length."
81	    - figure_id: "Figure 5"
82	      viz_type: "bar_chart"
83	      what_compared: "Supervised vs zero-shot detectors on in-distribution (XSum, WMT16-en) and out-distribution (PubMedQA, WMT16-de) datasets"
84	      how_gain_highlighted: "Fast-DetectGPT bars consistently tallest; supervised detectors visibly degrade on out-distribution while Fast-DetectGPT maintains performance"
85	      design_note: "Grouped bars by dataset; clean separation of in-distribution vs out-distribution highlights generalization advantage of zero-shot approach."
86	  ablation_figures: []
87	  figure_narrative_role: "Figure 1 (motivation: hypothesis visualization) → Figure 2 (method: architecture comparison) → Figure 3 (validation: ROC curves) → Figure 4 (robustness: length sensitivity) → Figure 5 (generalization: cross-domain comparison). Clean progression from why → how → does it work → how robust → how general."
88	
89	tables:
90	  table_count: 9
91	  main_result_table:
92	    table_id: "Table 2"
93	    row_axis: "methods"
94	    col_axis: "source models (GPT-2, OPT-2.7, Neo-2.7, GPT-J, NeoX) × settings (white-box, black-box)"
95	    row_organization: "by_category"
96	    col_organization: "grouped_by_dataset"
97	    highlight_strategy: "† marks second-best; ♢ marks methods requiring multiple model calls; relative improvement percentages in bottom row"
98	    statistical_reporting: "AUROC values (single run implied, no std reported in main tables)"
99	    num_baselines: 8
100	    design_note: "Two-section layout (white-box / black-box) in single table enables direct setting comparison; symbolic markers (†, ♢) add information density without cluttering numbers."
101	  ablation_tables:
102	    - table_id: "Table 9 (Appendix F.1)"
103	      what_varied: ["decoding strategy (top-p, top-k, temperature)"]
104	      variation_style: "full_numbers"
105	      design_note: "Shows robustness across decoding strategies; relative improvements (95%, 81%, 99%) demonstrate method generality."
106	  supplementary_tables:
107	    in_appendix: true
108	    content: "Tables 4-9 cover: source model details (Table 4), detailed per-dataset results for open-source models (Table 5), additional breakdowns, and decoding strategy robustness (Table 9). Paraphrasing attack results also in appendix."
109	    reason: "Main paper keeps 3 tables for key claims (overview, detailed comparison, real-world); appendix holds exhaustive per-dataset/per-model/per-strategy breakdowns for reproducibility."
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "991de9cf-2fe3-4263-867f-71bb30bcaa93",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "7778f978-ea23-4914-b2dc-b74cdf08c568",
  "sourceToolAssistantUUID": "991de9cf-2fe3-4263-867f-71bb30bcaa93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T16:32:40.245Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JPveko4oDrbMDszs1Ub1Ac`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/gltr.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7778f978-ea23-4914-b2dc-b74cdf08c568",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbccecba-d638-400a-a2af-853e2fbf982e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 30 · 2026-05-22T16:32:40.250Z_

<details><summary>↩ Tool result · `toolu_01JPveko4oDrbMDszs1Ub1Ac`</summary>

```text
1	paper_key: "gltr"
2	title: "GLTR: Statistical Detection and Visualization of Generated Text"
3	venue: "ACL 2019"
4	full_text_available: false
5	
6	research:
7	  baselines: ["unaided human detection (54% accuracy)"]
8	  metrics:
9	    - {name: "human detection rate", direction: "higher_better"}
10	    - {name: "word probability", direction: "descriptive"}
11	    - {name: "absolute rank", direction: "descriptive"}
12	    - {name: "predicted distribution entropy", direction: "descriptive"}
13	  datasets:
14	    - {name: "human-subjects study data", size: "unknown"}
15	  ablation_dimensions: ["sampling scheme", "statistical test type (probability, rank, entropy)"]
16	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
17	  method_family: "statistical detection via token-level probability visualization"
18	
19	positioning:
20	  core_claim: "Proposes a visual forensic tool using three simple statistical tests (word probability, rank, entropy) that improves human detection of generated text from 54% to 72% without prior training."
21	  key_results: "N/A - abstract only"
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
  "parentUuid": "cbccecba-d638-400a-a2af-853e2fbf982e",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "dbf978db-17d5-44e5-979f-c3e16dbabda0",
  "sourceToolAssistantUUID": "cbccecba-d638-400a-a2af-853e2fbf982e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T16:32:40.796Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KFAfABSdHnPgBdRTu1mdby`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/diveye.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbf978db-17d5-44e5-979f-c3e16dbabda0",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3f16fb80-3e58-4c6a-8707-8f747f2f5a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 32 · 2026-05-22T16:32:40.806Z_

<details><summary>↩ Tool result · `toolu_01KFAfABSdHnPgBdRTu1mdby`</summary>

```text
1	paper_key: "diveye"
2	title: "Diversity Boosts AI-Generated Text Detection"
3	venue: "TMLR 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["zero-shot detectors (unspecified)", "fine-tuned detectors (unspecified)"]
8	  metrics:
9	    - {name: "detection accuracy improvement", direction: "higher_better"}
10	    - {name: "robustness to paraphrasing", direction: "higher_better"}
11	    - {name: "cross-domain generalization", direction: "higher_better"}
12	  datasets:
13	    - {name: "multiple benchmarks (unspecified in abstract)", size: "unknown"}
14	  ablation_dimensions: ["surprisal-based feature types", "auxiliary signal integration", "domain transfer", "adversarial robustness"]
15	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
16	  method_family: "surprisal-based diversity features for zero-shot detection (DivEye)"
17	
18	positioning:
19	  core_claim: "Proposes DivEye, a framework capturing rhythmic unpredictability fluctuations in text, outperforming zero-shot detectors by up to 33.2% and boosting existing detectors by up to 18.7% as an auxiliary signal, with robustness to paraphrasing and adversarial attacks."
20	  key_results: "N/A - abstract only"
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
  "parentUuid": "3f16fb80-3e58-4c6a-8707-8f747f2f5a64",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "c6e445e5-440c-43b1-b69e-e60222bd0b69",
  "sourceToolAssistantUUID": "3f16fb80-3e58-4c6a-8707-8f747f2f5a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T16:32:40.824Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FHu92yh73hbKyHobem7z2D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/curse_of_recursion.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6e445e5-440c-43b1-b69e-e60222bd0b69",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6864fcbf-2b17-4e5e-a96e-6f44db1a6723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 34 · 2026-05-22T16:32:40.828Z_

<details><summary>↩ Tool result · `toolu_01FHu92yh73hbKyHobem7z2D`</summary>

```text
1	paper_key: "curse_of_recursion"
2	title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
3	venue: "Nature 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["models trained on original (non-synthetic) data"]
8	  metrics:
9	    - {name: "distribution tail preservation", direction: "higher_better"}
10	    - {name: "model quality degradation", direction: "descriptive"}
11	  datasets:
12	    - {name: "recursively generated training data", size: "unknown"}
13	  ablation_dimensions: ["model architecture (VAE, GMM, LLM)", "generation recursion depth", "synthetic data fraction"]
14	  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "unknown"}
15	  method_family: "model collapse analysis (recursive training on synthetic data)"
16	
17	positioning:
18	  core_claim: "Demonstrates 'Model Collapse' — training on model-generated content causes irreversible distribution tail loss, shown across VAEs, GMMs, and LLMs, with implications for web-scraped training data as LLM content proliferates."
19	  key_results: "N/A - abstract only"
20	  limitations: ["N/A"]
21	  relation_to_us: "foundation"
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
  "parentUuid": "6864fcbf-2b17-4e5e-a96e-6f44db1a6723",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "8a4e5942-d7cd-4ffb-aba6-c8ba47e72206",
  "sourceToolAssistantUUID": "6864fcbf-2b17-4e5e-a96e-6f44db1a6723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T16:32:41.069Z_

<details open><summary>🔧 Tool call — Read · `toolu_017aHkuTm8bEGVjSvHqSHyWU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/ood_baseline.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a4e5942-d7cd-4ffb-aba6-c8ba47e72206",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "169f6e0d-24ae-491b-baef-4be3d7001e42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 36 · 2026-05-22T16:32:41.073Z_

<details><summary>↩ Tool result · `toolu_017aHkuTm8bEGVjSvHqSHyWU`</summary>

```text
1	paper_key: "ood_baseline"
2	title: "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks"
3	venue: "ICLR 2017"
4	full_text_available: false
5	
6	research:
7	  baselines: []
8	  metrics:
9	    - {name: "maximum softmax probability", direction: "higher_better"}
10	    - {name: "detection performance (AUROC implied)", direction: "higher_better"}
11	  datasets:
12	    - {name: "computer vision benchmarks (unspecified)", size: "unknown"}
13	    - {name: "NLP benchmarks (unspecified)", size: "unknown"}
14	    - {name: "ASR benchmarks (unspecified)", size: "unknown"}
15	  ablation_dimensions: ["task domain (CV, NLP, ASR)", "misclassification vs OOD detection"]
16	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
17	  method_family: "softmax probability baseline for OOD detection"
18	
19	positioning:
20	  core_claim: "Establishes a simple maximum softmax probability baseline for detecting misclassified and out-of-distribution examples across CV, NLP, and ASR, demonstrating the task is underexplored despite the baseline's effectiveness."
21	  key_results: "N/A - abstract only"
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
  "parentUuid": "169f6e0d-24ae-491b-baef-4be3d7001e42",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "513c80c8-75b1-4b9a-abf5-085f172c86fc",
  "sourceToolAssistantUUID": "169f6e0d-24ae-491b-baef-4be3d7001e42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T16:32:41.484Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FMSH7VsnYWTMeP4UdhEZHa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/synthid_text.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "513c80c8-75b1-4b9a-abf5-085f172c86fc",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "91b5f66b-674c-4cc0-861d-2a1dbbb9d0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 38 · 2026-05-22T16:32:41.489Z_

<details><summary>↩ Tool result · `toolu_01FMSH7VsnYWTMeP4UdhEZHa`</summary>

```text
1	paper_key: "synthid_text"
2	title: "Scalable Watermarking for Identifying Large Language Model Outputs"
3	venue: "Nature 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["Gumbel sampling (non-distortionary)", "Soft Red List sampling (distortionary)", "unwatermarked generation"]
8	  metrics:
9	    - {name: "TPR at fixed FPR", direction: "higher_better"}
10	    - {name: "perplexity", direction: "lower_better"}
11	    - {name: "human preference ratings", direction: "higher_better"}
12	  datasets:
13	    - {name: "ELI5 (Explain Like I'm 5)", size: "unknown"}
14	    - {name: "Gemini chatbot interactions", size: "~20M interactions"}
15	  ablation_dimensions: ["watermark type (distortionary vs non-distortionary)", "tournament sampling", "speculative sampling integration"]
16	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "production Gemini systems"}
17	  method_family: "production-scale text watermarking (tournament sampling + sliding-window seeds)"
18	
19	positioning:
20	  core_claim: "Introduces SynthID-Text, a production-ready watermarking method deployed on ~20M Gemini interactions, preserving text quality (no significant human preference difference) with high detection accuracy and minimal latency via tournament sampling integrated with speculative decoding."
21	  key_results: "N/A - abstract only"
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
  "parentUuid": "91b5f66b-674c-4cc0-861d-2a1dbbb9d0b4",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "5a691499-73f9-4c4a-8b1a-1a0bc521f689",
  "sourceToolAssistantUUID": "91b5f66b-674c-4cc0-861d-2a1dbbb9d0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T16:32:41.595Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GMgouxY3Yx7RYGz4ps6Ywv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/nucleus_sampling.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a691499-73f9-4c4a-8b1a-1a0bc521f689",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a240f867-ae4f-4094-b7ee-29dbbad25187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 40 · 2026-05-22T16:32:41.599Z_

<details><summary>↩ Tool result · `toolu_01GMgouxY3Yx7RYGz4ps6Ywv`</summary>

```text
1	paper_key: "nucleus_sampling"
2	title: "The Curious Case of Neural Text Degeneration"
3	venue: "ICLR 2020"
4	full_text_available: false
5	
6	research:
7	  baselines: ["beam search", "top-k sampling", "temperature sampling", "greedy decoding"]
8	  metrics:
9	    - {name: "text quality (human evaluation)", direction: "higher_better"}
10	    - {name: "text diversity", direction: "higher_better"}
11	    - {name: "distributional similarity to human text", direction: "higher_better"}
12	  datasets:
13	    - {name: "open-ended text generation benchmarks (unspecified)", size: "unknown"}
14	  ablation_dimensions: ["decoding strategy", "nucleus threshold p", "text length"]
15	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
16	  method_family: "decoding strategy (nucleus/top-p sampling)"
17	
18	positioning:
19	  core_claim: "Reveals distributional disparities between human and machine text under likelihood-based decoding, and proposes Nucleus Sampling (top-p) that dynamically truncates the unreliable tail of the probability distribution to generate diverse yet coherent text."
20	  key_results: "N/A - abstract only"
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
  "parentUuid": "a240f867-ae4f-4094-b7ee-29dbbad25187",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "9737244e-15f6-452b-9a8f-06396caf6cc8",
  "sourceToolAssistantUUID": "a240f867-ae4f-4094-b7ee-29dbbad25187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T16:32:42.195Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NyH4ETxQssN8jRTCGVMwYq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/dna_gpt.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9737244e-15f6-452b-9a8f-06396caf6cc8",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbd8950b-fabd-4445-a508-6e12b91feae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 42 · 2026-05-22T16:32:42.200Z_

<details><summary>↩ Tool result · `toolu_01NyH4ETxQssN8jRTCGVMwYq`</summary>

```text
1	paper_key: "dna_gpt"
2	title: "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text"
3	venue: "ICLR 2024"
4	full_text_available: true  # via ar5iv HTML rendering
5	
6	research:
7	  baselines:
8	    - GPTZero
9	    - "OpenAI's official classifier (fine-tuned on 34 models)"
10	    - DetectGPT  # white-box only comparison
11	  metrics:
12	    - {name: "AUROC", direction: "higher_better"}
13	    - {name: "TPR at 1% FPR", direction: "higher_better"}
14	  datasets:
15	    - {name: "Reddit ELI5", size: "150-300 instances, physics/biology, Jan 2022-Mar 2023"}
16	    - {name: "Scientific Abstracts", size: "150-300 instances, Nature, April 2023"}
17	    - {name: "PubMedQA", size: "150-300 instances, biomedical domain"}
18	    - {name: "Xsum", size: "150-300 instances, news summarization"}
19	    - {name: "WMT16", size: "English and German machine translation"}
20	  ablation_dimensions:
21	    - "truncation ratio gamma (0.02-0.98, optimal 0.5)"
22	    - "number of re-generations K (1-20, saturates ~10 black-box, ~5 white-box)"
23	    - "decoding temperature (0.7, 1.0, 1.4, 1.8)"
24	    - "revision attack ratio (0-0.5, using T5-3B span replacement)"
25	    - "starting n-gram n0 (1-6, optimal 4)"
26	    - "weight function f(n) (log(n), n, n*log(n), n*log^2(n), n^2, e^n)"
27	    - "maximum n-gram N (set to 25)"
28	    - "non-English language (German via WMT16)"
29	    - "proxy model size (OPT-125M, GPT2-124M as proxies)"
30	    - "model version drift over time (41-day interval)"
31	    - "sliding window for mixed human+AI content"
32	  training_recipe:
33	    optimizer: "N/A (training-free, zero-shot method)"
34	    lr: "N/A"
35	    hardware: "N/A (uses LLM API calls; K regenerations per sample)"
36	  method_family: "re-generation + divergence analysis (zero-shot, training-free)"
37	
38	positioning:
39	  core_claim: "Truncating text and comparing re-generated continuations via n-gram overlap (black-box) or probability divergence (white-box) provides training-free, explainable detection that outperforms trained classifiers including OpenAI's own."
40	  key_results: >
41	    GPT-4 on Reddit-ELI5: 99.63 AUROC, 87.34% TPR@1%FPR (vs GPTZero 94.50/36.00, OpenAI 71.64/5.00).
42	    White-box text-davinci-003: 100.00 AUROC on Reddit and Xsum.
43	    Robust under 50% text revision: 98.48 AUROC (vs GPTZero ~60, OpenAI ~50).
44	    German detection: ~98 AUROC white-box (vs GPTZero ~50 random chance).
45	  limitations:
46	    - "Evaluated only on decoder-only GPT-architecture models; cannot reliably detect non-decoder-only generated text"
47	    - "Tested only on 1000-2000 character texts; significantly shorter/longer texts may fail"
48	    - "Black-box detection requires K API calls per sample (cost/latency overhead)"
49	    - "Proxy model detection with small models (OPT-125M) only reaches 73-82 AUROC, leaving room for improvement"
50	    - "Dataset memorization issue: WikiText-103 shows dramatic degradation because model memorizes training data"
51	  relation_to_us: "competitor"  # directly competing zero-shot detection method; our depth-fingerprint approach is conceptually related but uses different signal
52	
53	narrative:
54	  story_type: "突破局限型"
55	  hook: >
56	    Opens with the societal urgency of ChatGPT/GPT-4 release sparking global AI safety discussions,
57	    positioning detection as a pressing real-world problem. First sentence: "The release of ChatGPT and
58	    GPT-4 by OpenAI has sparked global discussions on the effective utilization of AI-assistant writing."
59	  tension: >
60	    Three-layer tension build:
61	    (1) Training-based detectors become obsolete when models update — inflexibility problem.
62	    (2) Methods requiring token probabilities (e.g., DetectGPT) fail for closed-source APIs — accessibility problem.
63	    (3) Existing approaches lack interpretability — explainability problem.
64	    Each layer eliminates a class of prior methods, leaving no satisfactory existing solution.
65	  key_insight: >
66	    Revealed in Section 3 as the formal "Likelihood-Gap Hypothesis": machine text shows high consistency
67	    when regenerated from the same prefix (low divergence), while human text shows high diversity
68	    (high divergence). This is grounded in the empirical observation that "given appropriate preceding text,
69	    LLMs tend to output highly similar text across multiple runs of generations."
70	    The insight is first conceptually hinted in intro paragraph 4, then formalized mathematically as a boxed hypothesis.
71	  argument_chain: >
72	    societal urgency (ChatGPT release) → training-based methods inflexible →
73	    perturbation methods require white-box access → no method provides explainability →
74	    empirical observation: regeneration consistency differs for human vs machine →
75	    likelihood-gap hypothesis (formalized) → BScore (black-box) and WScore (white-box) algorithms →
76	    SOTA on 5 datasets × 5 models + robustness to revision/temperature/language/model-drift
77	  contribution_framing: >
78	    3 numbered contributions at end of introduction:
79	    (1) identify the divergence phenomenon with theoretical hypothesis,
80	    (2) develop zero-shot detection for both black/white-box,
81	    (3) demonstrate SOTA + robustness + explainability.
82	    Framing emphasizes novelty on three axes: theory, method, and practical properties.
83	  intro_structure: >
84	    4 paragraphs:
85	    P1 — societal context/urgency (ChatGPT release, AI writing concerns)
86	    P2 — gap identification (training-based obsolescence, white-box requirement, DetectGPT failure)
87	    P3 — explainability need (pressing demand for interpretable detection)
88	    P4 — approach introduction (two scenarios, core observation, contribution list)
89	  notable_technique: >
90	    Uses the "elimination ladder": each paragraph in the intro eliminates one category of existing
91	    methods (trained classifiers → perturbation methods → uninterpretable black-boxes), creating
92	    a narrowing funnel that leaves only the proposed approach as viable. This makes the contribution
93	    feel inevitable rather than arbitrary.
94	
95	figures:
96	  figure_count: 8  # 7 in main text + 1 in appendix (sliding window)
97	  figure1:
98	    type: "method_overview"
99	    description: >
100	      Split-panel workflow diagram showing the three-stage DNA-GPT pipeline:
101	      (Left) original text split at truncation point into X' (preceding) and Y0 (remaining);
102	      (Center) X' fed to LLM K times generating {Y1,...,Yk};
103	      (Right) BScore/WScore calculation comparing regenerations against Y0, with threshold classification.
104	    narrative_role: "Provides the method overview immediately after the introduction, anchoring the reader's understanding of the truncate-regenerate-compare pipeline before mathematical formalization."
105	    design_elements:
106	      - "flowchart with rectangular text boxes and directional arrows"
107	      - "explicit truncation point visualization"
108	      - "K parallel regeneration paths"
109	      - "equation notation integrated into diagram"
110	    visual_style: "Horizontal flowchart, clean boxes with arrows, mathematical notation embedded. Functional rather than decorative — prioritizes clarity of the pipeline stages."
111	  result_figures:
112	    - figure_id: "Figure 2"
113	      viz_type: "dual_histogram"
114	      what_compared: "Log-likelihood distributions of machine-generated vs human-written text continuations on Reddit prompts (text-davinci-003)"
115	      how_gain_highlighted: "Clear visual separation between two distributions demonstrates the likelihood-gap hypothesis is empirically supported"
116	      design_note: "Placed right after the hypothesis statement as immediate visual evidence. The non-overlapping distributions make the theoretical claim viscerally convincing."
117	    - figure_id: "Figure 6"
118	      viz_type: "grouped_bar_chart"
119	      what_compared: "German vs English detection performance across methods (white-box and black-box)"
120	      how_gain_highlighted: "GPTZero drops to ~50 AUROC (random chance) on German while DNA-GPT maintains ~88-98, creating dramatic visual contrast"
121	      design_note: "Cross-lingual robustness as a differentiator — baseline collapse on non-English makes DNA-GPT advantage unmistakable."
122	  ablation_figures:
123	    - figure_id: "Figure 3"
124	      viz_type: "line_plot"
125	      dimensions_varied: ["truncation ratio gamma"]
126	      design_note: "Shows inverted-U curve peaking at gamma=0.5; both extremes degrade. Clean parametric sweep visualization."
127	    - figure_id: "Figure 4"
128	      viz_type: "line_plot"
129	      dimensions_varied: ["number of re-generations K"]
130	      design_note: "Shows saturation behavior — AUROC plateaus at K=10, TPR at K=5. Justifies practical parameter choice."
131	    - figure_id: "Figure 5"
132	      viz_type: "grouped_bar_chart"
133	      dimensions_varied: ["decoding temperature (0.7, 1.0, 1.4, 1.8)"]
134	      design_note: "Baselines degrade sharply at high temperature while DNA-GPT shows ~2% drop. Robustness claim visualized."
135	    - figure_id: "Figure 7"
136	      viz_type: "line_plot"
137	      dimensions_varied: ["revision attack ratio (0.0-0.5)"]
138	      design_note: "DNA-GPT curve stays flat (~99-98 AUROC) while baselines plummet to 50-60. Most compelling robustness evidence."
139	  figure_narrative_role: >
140	    Figure 1 (method overview) → Figure 2 (hypothesis evidence via distribution separation) →
141	    Figures 3-4 (parameter sensitivity: truncation ratio, K) → Figure 5 (temperature robustness) →
142	    Figure 6 (cross-lingual generalization) → Figure 7 (revision attack robustness).
143	    Flow: understand pipeline → believe the signal exists → tune parameters → stress-test robustness.
144	
145	tables:
146	  table_count: 16  # 3 main + 13 appendix
147	  main_result_table:
148	    table_id: "Table 1"
149	    row_axis: "methods"
150	    col_axis: "datasets x metrics (AUROC + TPR@1%FPR)"
151	    row_organization: "by_category"  # grouped by target model (GPT-4, GPT-3.5-turbo, text-davinci-003), then baselines vs DNA-GPT variants within each group
152	    col_organization: "grouped_by_dataset"  # Reddit-ELI5, Scientific Abstracts, PubMedQA, Xsum columns, each with AUROC and TPR sub-columns
153	    highlight_strategy: "bold_best"
154	    statistical_reporting: "single-run point estimates (no std reported)"
155	    num_baselines: 3  # GPTZero, OpenAI classifier, DetectGPT (white-box only)
156	    design_note: >
157	      Three-level grouping (model → method → parameter variant) creates a comprehensive but dense table.
158	      DNA-GPT variants shown with different K and gamma settings to demonstrate parameter sensitivity
159	      within the main results table rather than relegating to ablation.
160	  ablation_tables:
161	    - table_id: "Table 2"
162	      what_varied: ["source model identity for model sourcing task"]
163	      variation_style: "full_numbers"
164	      design_note: "Novel task (model sourcing) presented as a separate table with pairwise model comparisons. Shows the method's unique capability beyond binary detection."
165	    - table_id: "Table 3"
166	      what_varied: ["open-source vs closed-source models", "black-box vs white-box setting"]
167	      variation_style: "full_numbers"
168	      design_note: "Demonstrates generalization to open-source models (GPT-NeoX-20B, LLaMa-13B) on Xsum and Reddit. Baselines show dramatic degradation."
169	  supplementary_tables:
170	    in_appendix: true
171	    content: >
172	      Tables 4-16 in appendix: prompt templates, detailed parameter sensitivity results
173	      (n-gram starting value, weight function, maximum n-gram), model version drift results,
174	      sliding window mixed-content results, proxy model performance, additional dataset results,
175	      and example evidence outputs with highlighted n-gram overlaps.
176	    reason: >
177	      Main paper keeps 3 tables focused on core claims (SOTA, model sourcing, open-source generalization).
178	      Exhaustive parameter sweeps and additional analyses relegated to appendix to maintain narrative flow
179	      while supporting reproducibility.
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbd8950b-fabd-4445-a508-6e12b91feae5",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "0ed337ca-6386-4563-8223-67214b1d4e98",
  "sourceToolAssistantUUID": "cbd8950b-fabd-4445-a508-6e12b91feae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T16:32:42.446Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CVdmqWcYXDSWPqSvEjukQ3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/uchendu_attribution.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ed337ca-6386-4563-8223-67214b1d4e98",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "10592a1c-6092-46d4-b8ef-ee4bb7652d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 44 · 2026-05-22T16:32:42.453Z_

<details><summary>↩ Tool result · `toolu_01CVdmqWcYXDSWPqSvEjukQ3`</summary>

```text
1	paper_key: "uchendu_attribution"
2	title: "Authorship Attribution for Neural Text Generation"
3	venue: "EMNLP 2020"
4	full_text_available: false
5	
6	research:
7	  baselines: ["human-written text baseline"]
8	  metrics:
9	    - {name: "classification accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "human-written + 8 generator outputs (CTRL, GPT, GPT2, GROVER, XLM, XLNET, PPLM, FAIR)", size: "unknown"}
12	  ablation_dimensions: ["attribution task type (same-method verification, human-vs-machine, k-way generator identification)", "generator model"]
13	  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "unknown"}
14	  method_family: "supervised authorship attribution (multi-class generator classification)"
15	
16	positioning:
17	  core_claim: "Formulates three authorship attribution problems for neural text (same-method verification, human-vs-machine, k-way identification) and evaluates classifiers across 8 generators, finding GPT2/GROVER/FAIR produce the most human-like text that confuses classifiers."
18	  key_results: "N/A - abstract only"
19	  limitations: ["N/A"]
20	  relation_to_us: "competitor"
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
  "parentUuid": "10592a1c-6092-46d4-b8ef-ee4bb7652d5f",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "41a90cef-d767-47ef-932e-6d19faed0aa9",
  "sourceToolAssistantUUID": "10592a1c-6092-46d4-b8ef-ee4bb7652d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T16:32:42.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J1tUJouGLS3rVYtWBdphxq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/writing_diversity.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41a90cef-d767-47ef-932e-6d19faed0aa9",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21eaaf21-9179-4f3b-a397-45ee8022fd71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 46 · 2026-05-22T16:32:42.725Z_

<details><summary>↩ Tool result · `toolu_01J1tUJouGLS3rVYtWBdphxq`</summary>

```text
1	paper_key: "writing_diversity"
2	title: "Does Writing with Language Models Reduce Content Diversity?"
3	venue: "ICLR 2024"
4	full_text_available: true  # arXiv HTML available at 2309.05196v3
5	
6	research:
7	  baselines:
8	    - Solo writing (no AI assistance)
9	    - GPT3-assisted writing (davinci base model)
10	    - InstructGPT-assisted writing (text-davinci-003)
11	  metrics:
12	    - {name: "Homogenization (avg pairwise Rouge-L similarity)", direction: "lower_better"}
13	    - {name: "Homogenization (avg pairwise BertScore similarity)", direction: "lower_better"}
14	    - {name: "Lexical diversity (unique n-gram fraction)", direction: "higher_better"}
15	    - {name: "Key point diversity (clustered unique arguments)", direction: "higher_better"}
16	    - {name: "5-gram distribution concentration", direction: "lower_better"}
17	  datasets:
18	    - {name: "Custom essay corpus", size: "300 argumentative essays, 38 writers, 10 topics from NY Times Student Opinion"}
19	  ablation_dimensions:
20	    - Model type (GPT3 base vs InstructGPT)
21	    - Text attribution (user-contributed vs model-contributed)
22	    - Diversity granularity (lexical n-gram vs semantic key-point)
23	    - Clustering threshold for key point diversity (0.5-0.8)
24	    - Per-topic vs aggregate analysis
25	  training_recipe:
26	    participants: "38 professional writers from Upwork (native English speakers)"
27	    task: "Argumentative essays ~300 words on 10 topics"
28	    design: "3 conditions x 10 topics x 10 essays = 300 essays"
29	    models_used: "OpenAI davinci (GPT3) and text-davinci-003 (InstructGPT)"
30	    decoding: "temperature=0.9, frequency_penalty=0.5, top_p=1.0"
31	    min_queries: ">=5 model suggestions required per essay"
32	    key_point_extraction: "gpt-3.5-turbo summarization (~6.86 key points/essay)"
33	  method_family: "Controlled human-AI co-writing experiment with diversity measurement"
34	
35	positioning:
36	  core_claim: "RLHF-tuned models (InstructGPT) significantly reduce content diversity in human-AI co-writing compared to base models (GPT3), and this reduction is entirely attributable to model-contributed text, not changes in user behavior."
37	  key_results: "InstructGPT homogenization: 0.1660 Rouge-L (+8.1% vs Solo 0.1536, p<0.05); GPT3: 0.1578 (not significant); 5-gram diversity: InstructGPT 0.977 vs Solo 0.991; key point diversity: InstructGPT 0.738 vs Solo 0.792 (p<0.05); model suggestion self-similarity: InstructGPT 0.20 vs GPT3 0.11 (p<0.05)"
38	  limitations:
39	    - "Single-turn suggestion interface may not reflect all real-world co-writing contexts"
40	    - "Upwork writers not representative of all demographics"
41	    - "Only OpenAI models tested; results may not generalize to other model families"
42	    - "Single-session study; repeated interactions over time could change dynamics"
43	  relation_to_us: "foundation"  # Directly establishes that RLHF models produce less diverse text — this is the mechanism behind detectable AI fingerprints in generation depth
44	
45	narrative:
46	  story_type: "突破局限型"  # Breaks through assumption that AI writing assistance is neutral; reveals hidden homogenization cost
47	  hook: "LLMs are transforming content creation, but millions of users relying on the same model risks 'algorithmic monoculture' — shifting content toward the mode"
48	  tension: "Prior work shows LLMs influence opinions and lack demographic representation, but no one has measured whether co-writing actually reduces the diversity of produced content"
49	  key_insight: "Section 5 (attribution analysis): the diversity loss is 100% attributable to model-contributed text — user writing behavior is unchanged across all conditions, but InstructGPT suggestions are inherently more homogeneous than GPT3 suggestions"
50	  argument_chain: "Monoculture risk → controlled experiment design → verify equal engagement → measure homogenization → measure diversity loss → attribute to model text → diagnose RLHF as cause"
51	  contribution_framing: "Implicit 3-fold: (1) controlled experiment measuring diversity impact, (2) diversity metrics at lexical and semantic levels, (3) attribution analysis pinpointing model text as cause. Contributions stated as findings rather than an explicit numbered list"
52	  intro_structure: "2 main paragraphs: P1 motivates the monoculture problem with prior evidence; P2 describes the experimental approach and previews findings. Notably compact intro."
53	  notable_technique: "The GPT3 vs InstructGPT comparison is the key rhetorical device — by showing GPT3 does NOT reduce diversity while InstructGPT DOES, the paper isolates RLHF/instruction-tuning as the causal factor, rather than AI assistance in general. This is more persuasive than just measuring one model."
54	
55	figures:
56	  figure_count: 13  # including appendix figures
57	  figure1:
58	    type: "motivation"
59	    description: "Boxplots showing corpus homogenization at key point level across three conditions (Solo, GPT3, InstructGPT) and 10 topics. InstructGPT displays highest median on 7/10 topics."
60	    narrative_role: "Immediately demonstrates the main finding visually — InstructGPT consistently elevates homogenization across topics"
61	    design_elements: ["horizontal boxplots", "per-topic breakdown", "outlier markers", "three-condition color coding"]
62	    visual_style: "Grid of boxplots organized by topic; three colors for three conditions; clean axis labels; emphasis on InstructGPT being consistently highest"
63	  result_figures:
64	    - figure_id: "Figure 2"
65	      viz_type: "boxplot"
66	      what_compared: "Homogenization scores (Rouge-L) across Solo, InstructGPT, GPT3 at key point level"
67	      how_gain_highlighted: "Visual separation of InstructGPT median from Solo/GPT3; boxplot spread shows consistency"
68	      design_note: "Aggregated view complementing per-topic Figure 1; boxplot chosen to show distribution, not just means"
69	    - figure_id: "Figure 3"
70	      viz_type: "line_plot"
71	      what_compared: "Frequency distributions of (a) top-50 unigrams and (b) top-50 5-grams across three conditions"
72	      how_gain_highlighted: "InstructGPT shows steeper curve on 5-grams (more concentrated), while unigrams overlap — reveals that diversity loss is in phrases, not individual words"
73	      design_note: "Two-panel figure; frequency rank on x-axis, probability on y-axis; overlapping lines make convergence/divergence immediately visible"
74	    - figure_id: "Figure 4"
75	      viz_type: "line_plot"
76	      what_compared: "Attribution analysis: (a) homogenization by authorship (user vs model), (b) 5-gram distributions separated by author"
77	      how_gain_highlighted: "Dashed lines (user text) overlap perfectly across conditions; solid lines (model text) diverge — visually proves model is the cause"
78	      design_note: "The dashed-vs-solid encoding is the key design choice; makes the causal attribution visually immediate without statistical explanation"
79	  ablation_figures:
80	    - figure_id: "Appendix figures"
81	      viz_type: "boxplot and line_plot variants"
82	      dimensions_varied: ["clustering threshold", "per-topic breakdown", "BertScore vs Rouge-L"]
83	      design_note: "Appendix replicates main analyses with alternative metrics/thresholds for robustness"
84	  figure_narrative_role: "Figure 1 (main result: homogenization by topic) → Figure 2 (aggregated homogenization) → Figure 3 (lexical diversity mechanism) → Figure 4 (causal attribution) — progressive deepening from 'what happens' to 'where it happens' to 'why it happens'"
85	
86	tables:
87	  table_count: 13  # including appendix tables
88	  main_result_table:
89	    table_id: "Table 3"
90	    row_axis: "metrics"  # n-gram sizes (unigram through 5-gram) in 3a; clustering thresholds in 3b
91	    col_axis: "conditions (Solo, GPT3, InstructGPT)"
92	    row_organization: "by_category"  # split into (a) lexical diversity and (b) key point diversity sub-tables
93	    col_organization: "flat"  # three conditions side by side
94	    highlight_strategy: "bold values indicate p<0.05 statistical significance"
95	    statistical_reporting: "permutation tests (1000 iterations); chi-square tests for distribution comparisons; independent t-tests for usage stats"
96	    num_baselines: 2  # Solo and GPT3 serve as baselines for InstructGPT
97	    design_note: "Split into 3a (n-gram diversity) and 3b (key point diversity) sub-tables; compact format showing both metrics in one numbered table; bold = significant rather than bold = best"
98	  ablation_tables:
99	    - table_id: "Table 1"
100	      what_varied: ["condition (Solo, GPT3, InstructGPT)"]
101	      variation_style: "full_numbers"
102	      design_note: "Usage statistics table verifying equal engagement across conditions (queries, acceptance rate, model-written %, word count); serves as manipulation check rather than result"
103	    - table_id: "Table 4"
104	      what_varied: ["condition (Solo vs InstructGPT)"]
105	      variation_style: "full_numbers"
106	      design_note: "Top-10 most frequent 5-grams comparison; qualitative evidence showing InstructGPT repeats topic-specific phrases much more (14x vs 6x); bridges quantitative metrics to intuitive understanding"
107	  supplementary_tables:
108	    in_appendix: true
109	    content: "Extended homogenization results with BertScore, per-topic diversity breakdowns, compression-based diversity analysis, additional usage statistics, model self-diversity measurements"
110	    reason: "Main text focuses on Rouge-L and key point metrics; appendix provides robustness checks with alternative metrics (BertScore, compression ratio) and finer-grained per-topic analysis"
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21eaaf21-9179-4f3b-a397-45ee8022fd71",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "f985efbc-0dc6-48e1-9cf8-c1fc86676438",
  "sourceToolAssistantUUID": "21eaaf21-9179-4f3b-a397-45ee8022fd71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T16:32:42.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wpa3nzXfdhxqsKFZXwcDk3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/strong_model_collapse.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f985efbc-0dc6-48e1-9cf8-c1fc86676438",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d3c82679-f746-454d-beba-7c7a3e250c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 48 · 2026-05-22T16:32:42.941Z_

<details><summary>↩ Tool result · `toolu_01Wpa3nzXfdhxqsKFZXwcDk3`</summary>

```text
1	paper_key: "strong_model_collapse"
2	title: "Strong Model Collapse"
3	venue: "ICLR 2025"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Training on real data only (p₂=0)"
9	    - "Theoretical predictions from Theorems 1-2"
10	    - "Weighted single-step mixing (Jain et al. 2024)"
11	    - "Dynamic multi-step mixing (Ferbach et al. 2024)"
12	  metrics:
13	    - {name: "Test Error (MSE)", direction: "lower_better"}
14	    - {name: "Collapse term ζ", direction: "lower_better", note: "additional error from synthetic data"}
15	  datasets:
16	    - {name: "Synthetic Gaussian data", size: "d=600, n=500", domain: "toy/theoretical validation"}
17	    - {name: "MNIST", size: "standard", domain: "image classification with two-layer networks"}
18	    - {name: "BabiStories (TinyStories reproduction)", size: "generated via Mixtral-8x7B", domain: "language modeling with GPT-2"}
19	  ablation_dimensions:
20	    - synthetic_data_fraction (p₂ from 0 to 1)
21	    - synthetic_data_quality (c² ∈ {0, 0.1, 0.5, 1})
22	    - model_size (width m, varying m/n ratio)
23	    - interpolation_threshold (underparametrized vs overparametrized)
24	    - regularization_strength (ridge parameter λ)
25	    - mitigation_strategy (weighted mixing vs multi-step distillation)
26	  training_recipe:
27	    optimizer: "Ridge regression (closed-form); GPT-2 standard training for LM experiments"
28	    lr: "N/A for ridge; standard for GPT-2"
29	    hardware: "Not specified"
30	    statistical_runs: "5 runs with error bars for random projections experiments"
31	  method_family: "theoretical analysis of model collapse (bias-variance decomposition with collapse term)"
32	
33	positioning:
34	  core_claim: "Even the smallest fraction of synthetic data (as little as 1%) causes irreversible model collapse—an additional error term ζ proportional to p₂² that persists regardless of dataset size, model scaling, or mixing strategy, unless synthetic data is completely removed."
35	  key_results: "Test error decomposes as B + V + ζ where ζ = Ω(p₂²c²) is the collapse term; larger models amplify collapse below interpolation threshold but may recover beyond it; weighted mixing and multi-step distillation cannot prevent collapse."
36	  limitations:
37	    - "Analysis restricted to linear models and random projections approximation (neural tangent kernel proxy)"
38	    - "Gaussian data assumption for theoretical results"
39	    - "Does not cover sophisticated mitigation strategies like data curation/filtering"
40	    - "Language modeling experiments on small scale (TinyStories/GPT-2) rather than full LLM systems"
41	    - "Label shift model (δ = w*₂ - w*₁) may not capture all forms of distribution mismatch in practice"
42	  relation_to_us: "foundation"
43	
44	narrative:
45	  story_type: "突破局限型"
46	  hook: "'Model Collapse refers to a critical degradation in the performance of AI models, particularly when a significant portion of their training data consists of synthetic data'—immediately framing a crisis relevant to all modern LLM training pipelines."
47	  tension: "Prior work showed collapse in iterative retraining loops, but practitioners assumed mixing real and synthetic data would be safe. The paper challenges this assumption: even 1% synthetic data breaks scaling laws."
48	  key_insight: "Formalized in Theorem 1 and Corollary 1 (Section 2-3)—the collapse term ζ = Ω(p₂²c²) is structurally irreducible. It emerges from a rigorous bias-variance decomposition where ζ is a third, previously unrecognized component. The insight is that collapse is not a finite-sample artifact but a fundamental property of mixed-distribution learning."
49	  argument_chain: "Model collapse is a real crisis → prior work studied iterative loops but not realistic mixing → two key questions (is collapse inevitable with mixing? do larger models suffer more?) → formal bias-variance-collapse decomposition → Theorem 1 (linear model) + Theorem 2 (random projections) → even 1% synthetic data creates persistent ζ → larger models amplify collapse below interpolation threshold → weighted/multi-step mixing cannot prevent collapse → validated on MNIST and GPT-2/BabiStories"
50	  contribution_framing: "Three contributions under Section 1.1 'Main Contributions': Result #1 (strong collapse persists with mixed data), Result #2 (model size amplifies collapse), Experimental Validation. Uses formal 'Result' numbering emphasizing theoretical novelty."
51	  intro_structure: "5 paragraphs: P1=definition+framing (model collapse as crisis), P2=problem context (empirical observations, scaling laws), P3=motivation (why this matters for ChatGPT/Llama-scale systems), P4=research questions (Q1: inevitable? Q2: model size effect?), P5=main contributions (three numbered results)"
52	  notable_technique: "Posing two sharp research questions (Q1, Q2) in the intro that structure the entire paper. Each theorem directly answers one question, making the paper's logic feel inevitable. Also the naming choice 'Strong Model Collapse' (vs implicit 'weak') creates a memorable taxonomy."
53	
54	figures:
55	  figure_count: 5
56	  figure1:
57	    type: "teaser_result"
58	    description: "Pareto diagram showing test error with mixed real+synthetic data vs real-only data. Points colored by synthetic data quality (squares=very high, diamonds=high, triangles=low, stars=very low). Colorbar shows m/n ratio (model size relative to data)."
59	    narrative_role: "Immediately conveys the main result visually—no amount of mixing avoids the collapse penalty. Points above the diagonal = worse than real-only training."
60	    design_elements: ["Pareto frontier", "shape encoding for quality levels", "colorbar for model size ratio", "diagonal reference line (real-only baseline)"]
61	    visual_style: "Scatter plot with multiple shape markers encoding categorical variable (data quality) and continuous colorbar encoding model size ratio. Clean 2D layout showing trade-off between real-only and mixed performance."
62	  result_figures:
63	    - figure_id: "Figure 3"
64	      viz_type: "line_plot"
65	      what_compared: "Theoretical predictions (dashed) vs empirical results (solid) for test error vs sample count across multiple synthetic data quality levels c²"
66	      how_gain_highlighted: "Perfect theory-experiment alignment validates the theoretical framework; multiple c² curves show collapse severity scales with quality"
67	      design_note: "Theory-experiment overlay (solid vs dashed) is the key design choice—demonstrates theoretical rigor. Multiple curves for c² ∈ {0, 0.1, 0.5, 1} show parametric dependence."
68	    - figure_id: "Figure 4"
69	      viz_type: "line_plot"
70	      what_compared: "Test error vs model size (m) for varying synthetic fractions p₂ across four data quality levels"
71	      how_gain_highlighted: "Darker lines (higher p₂) show worse performance; visible divergence from p₂=0 baseline; double-descent visible at m≈n"
72	      design_note: "Four subplots for quality levels; color gradient for p₂; error bars over 5 runs; vertical line at interpolation threshold m=n."
73	  ablation_figures:
74	    - figure_id: "Figure 2"
75	      viz_type: "line_plot"
76	      dimensions_varied: ["model size m", "decomposition components (B, V, ζ)"]
77	      design_note: "Illustrates the B+V+ζ decomposition across model sizes. Shows classical double-descent in bias curve; vertical line at m=n interpolation threshold; ζ term (collapse) shown in distinct color (red). Pedagogical figure explaining the theoretical framework."
78	  figure_narrative_role: "Figure 1 (teaser: collapse shown via Pareto diagram) → Figure 2 (framework: B+V+ζ decomposition illustrated) → Figure 3 (validation: theory matches experiment for linear model) → Figure 4 (extension: model size effects with double-descent) → Figure 5 (extension: additional model size analysis). Flow: claim → framework → validate → extend."
79	
80	tables:
81	  table_count: 0
82	  main_result_table:
83	    table_id: "N/A"
84	    row_axis: "N/A"
85	    col_axis: "N/A"
86	    row_organization: "N/A"
87	    col_organization: "N/A"
88	    highlight_strategy: "N/A"
89	    statistical_reporting: "N/A"
90	    num_baselines: 0
91	    design_note: "Notably, this theory-heavy paper uses NO tables in the main text. All results are communicated through figures (theory-experiment overlay plots) and theorem statements. This is typical for theoretical ML papers where the primary 'results' are theorems rather than benchmark numbers."
92	  ablation_tables: []
93	  supplementary_tables:
94	    in_appendix: true
95	    content: "Appendix contains experimental details (A.1-A.3) for toy, MNIST, and GPT-2 settings, but results are presented as figures rather than tables."
96	    reason: "Theory paper convention: theorems are the main results; figures validate theory vs experiment; tables would not add value since comparisons are between theoretical predictions and empirical measurements rather than between competing methods."
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3c82679-f746-454d-beba-7c7a3e250c82",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "25f2580f-e095-483f-bd28-deae3d684d4c",
  "sourceToolAssistantUUID": "d3c82679-f746-454d-beba-7c7a3e250c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T16:32:43.355Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DKZQizF8K73WXM7vxemNAN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/broken_telephone.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25f2580f-e095-483f-bd28-deae3d684d4c",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "359657e5-9d0f-4f39-9f73-55d3553d93a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39778,
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

_source line 50 · 2026-05-22T16:32:43.360Z_

<details><summary>↩ Tool result · `toolu_01DKZQizF8K73WXM7vxemNAN`</summary>

```text
1	paper_key: "broken_telephone"
2	title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
3	venue: "ACL 2025"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Iteration 0 (original human-written text)"
9	    - "Single-model chains vs. multi-model chains"
10	    - "Bilingual vs. multilingual chains"
11	  metrics:
12	    - {name: "BLEU", direction: "higher_better"}
13	    - {name: "ROUGE-1", direction: "higher_better"}
14	    - {name: "chrF", direction: "higher_better"}
15	    - {name: "METEOR", direction: "higher_better"}
16	    - {name: "BERTScore", direction: "higher_better"}
17	    - {name: "FActScore", direction: "higher_better"}
18	  datasets:
19	    - {name: "BookSum", size: "150 documents, 100-200 words each", domain: "book summaries"}
20	    - {name: "ScriptBase-alpha", size: "150 documents, 100-200 words each", domain: "movie scripts"}
21	    - {name: "News2024", size: "150 documents, 100-200 words each", domain: "news articles (2024 only)"}
22	  ablation_dimensions:
23	    - "Bridge language choice (FR, DE, NL, VN, ZH, TH — Latin vs. non-Latin scripts)"
24	    - "Chain complexity (bilingual vs. multilingual, 2 vs. 5 languages)"
25	    - "Number of models (1 vs. 2 vs. 3)"
26	    - "Temperature (1e-6, 0.25, 0.5, 0.75, 1.0)"
27	    - "Prompt constraint level (simple, base, constrained)"
28	    - "Task type (translation vs. rephrasing)"
29	  training_recipe:
30	    models:
31	      - "Llama-3.1-8B-Instruct (temp=0.6, top_p=0.9)"
32	      - "Mistral-7B-Instruct-v0.2 (temp=0.0)"
33	      - "Gemma-2-9B-it (temp=1.0, top_p=0.95)"
34	    max_tokens: 8000
35	    hardware: "54 GPU-days (36 on A100, 18 on A10)"
36	    factuality_judge: "Claude 3.5 Sonnet (for FActScore)"
37	    no_training: "Inference-only; no model finetuning involved"
38	  method_family: "Iterative inference-time generation (translation chains) measuring information distortion"
39	
40	positioning:
41	  core_claim: "Information distortion accumulates inevitably through iterative LLM generation, influenced by language proximity and chain complexity, but is partially mitigable through temperature control and constrained prompting—establishing that LLMs act as lossy information channels."
42	  key_results: >
43	    EN<->TH (Llama) FActScore gradient: -0.018/iter (News2024), -0.026/iter (BookSum);
44	    EN<->FR (Llama) FActScore gradient: -0.004/iter (much less distortion for Latin-script pairs);
45	    Multilingual 5-language chain: steepest gradient -0.038/iter;
46	    By iteration 100, all chains converge to similar low FActScore (~0.04) regardless of setup;
47	    Temperature 1e-6 stabilizes after 2 iterations; temperature 1.0 causes steepest decline;
48	    Qualitative: "A lorry driver has been fined" → "A small car received a compensation" by iteration 100.
49	  limitations:
50	    - "Datasets share similar characteristics; specialized/long-tail domains unexplored"
51	    - "Limited to 7-9B parameter models; larger models may behave differently"
52	    - "Default generation settings only; greedy/beam search unexplored"
53	    - "Translation as proxy task; other iterative generation scenarios (summarization, paraphrasing) less explored"
54	  relation_to_us: "complementary"
55	
56	narrative:
57	  story_type: "跨界迁移型"
58	  hook: >
59	    Opens with the observation that LLMs increasingly generate online content, then
60	    raises a concern about iterative processing: what happens when LLMs repeatedly
61	    consume and reprocess their own outputs? The "broken telephone" (Chinese whispers)
62	    analogy is introduced immediately as a vivid, universally understood frame for
63	    information distortion through sequential transmission.
64	  tension: >
65	    Unlike prior work on model collapse (which requires retraining), this paper targets
66	    inference-time distortion—each step is just prompting, no weight updates.
67	    The tension is: even without training, iterative generation should be safe... right?
68	    Translation as testbed makes the distortion measurable because there's an objective
69	    ground truth to compare against.
70	  key_insight: >
71	    Revealed through the language pair comparison in Experiment 1: distortion is not
72	    uniform—it depends critically on the bridge language. Latin-script pairs (EN<->FR)
73	    show near-zero degradation, while non-Latin pairs (EN<->TH) degrade 4-5x faster.
74	    This connects to training data representation and suggests the distortion reflects
75	    model competence boundaries. The convergence phenomenon (all setups reach ~0.04
76	    FActScore by iteration 100) suggests a universal "information floor."
77	  argument_chain: >
78	    LLMs generate increasing web content → iterative processing is inevitable →
79	    broken telephone analogy suggests distortion → choose translation as measurable testbed →
80	    Exp1: bilingual self-loop reveals language-dependent distortion →
81	    Exp2: multi-model collaboration adds/reduces noise depending on language →
82	    Exp3: multilingual chains accelerate distortion →
83	    ablations: temperature and prompt constraints partially mitigate →
84	    conclusion: distortion inevitable, mitigation possible but incomplete
85	  contribution_framing: >
86	    Three findings presented as bullet points (not numbered contributions):
87	    (1) Distortion depends on intermediate language choice (linguistic similarity + training data prevalence)
88	    (2) Greater chain complexity amplifies distortion
89	    (3) Temperature control and constrained prompting mitigate but cannot prevent distortion.
90	    Notably framed as empirical findings rather than methodological contributions.
91	  intro_structure: >
92	    4 paragraphs:
93	    P1 (Hook): LLMs generate content, iterative processing raises concerns
94	    P2 (Analogy): Broken telephone game as conceptual frame
95	    P3 (Research question): Do LLMs exhibit similar distortion?
96	    P4 (Approach + contributions): Translation testbed, three key findings listed
97	  notable_technique: >
98	    The broken telephone analogy is the paper's most effective narrative device—it transforms
99	    a technical measurement study into an intuitive story. The qualitative example
100	    (Table 1: lorry driver -> bus -> small car with explosions and compensation)
101	    is placed before any metrics, making readers viscerally understand the problem
102	    before seeing numbers. The three-experiment escalation (single-model bilingual →
103	    multi-model bilingual → multilingual multiplayer) creates natural narrative momentum.
104	
105	figures:
106	  figure_count: 6
107	  figure1:
108	    type: "method_overview"
109	    description: >
110	      Three-panel overview of the three experimental setups. Left: Bilingual Self-Loop
111	      (single model, EN<->FR/TH, 100 iterations). Middle: Bilingual Two-Player
112	      (two different models collaborating on same translation chain). Right: Multilingual
113	      Multiplayer (multiple languages and models in extended chains).
114	    narrative_role: >
115	      Establishes all three experiments at a glance, showing the escalation in complexity
116	      from left to right. Readers can reference back to this figure throughout the paper.
117	    design_elements:
118	      - "Three-panel layout showing experimental progression"
119	      - "Arrow-based translation flow diagrams"
120	      - "Model icons distinguishing Llama/Mistral/Gemma"
121	      - "Language labels (EN, FR, TH, ZH, DE) at each node"
122	    visual_style: >
123	      Horizontal three-panel layout. Each panel shows a circular or chain-like
124	      translation flow with arrows connecting language nodes. Different models
125	      distinguished by icons or colors. Clean, diagrammatic style typical of
126	      NLP experiment overviews.
127	  result_figures:
128	    - figure_id: "Figure 2"
129	      viz_type: "line_plot"
130	      what_compared: >
131	        Llama bilingual self-loop metrics (BLEU, ROUGE-1, chrF, METEOR, BERTScore, FActScore)
132	        across 100 iterations for 6 language pairs (FR, DE, NL, VN, ZH, TH) on News2024.
133	      how_gain_highlighted: >
134	        Language pairs naturally separate into two groups: Latin-script (FR/DE/NL) cluster
135	        high, non-Latin (VN/ZH/TH) cluster low, with TH showing steepest decline.
136	        The visual gap between clusters is the main finding.
137	      design_note: >
138	        Multi-subplot grid (one per metric). 6 lines per subplot distinguished by color.
139	        X-axis is iteration count (0-100), Y-axis is metric value. The consistent
140	        pattern across all 6 metrics reinforces the language-dependence finding.
141	    - figure_id: "Figure 3"
142	      viz_type: "line_plot"
143	      what_compared: >
144	        Bilingual two-player results comparing single-model vs. multi-model chains
145	        for EN<->FR and EN<->TH on News2024.
146	      how_gain_highlighted: >
147	        Shows that collaboration helps for Thai (reducing distortion) but hurts for
148	        French (increasing distortion)—a nuanced, non-obvious finding.
149	      design_note: >
150	        Paired comparison layout. Lines for single-model and multi-model chains
151	        shown together for direct comparison per language pair.
152	    - figure_id: "Figure 4"
153	      viz_type: "line_plot"
154	      what_compared: >
155	        Rephrasing experiments on 30 News2024 documents: individual models
156	        (Llama, Mistral, Gemma) vs. collaborative combinations over 100 iterations.
157	      how_gain_highlighted: >
158	        Collaborative setups show steeper decline than individual models,
159	        with Llama+Mistral+Gemma triple collaboration declining fastest.
160	      design_note: >
161	        Tests whether the translation finding generalizes to pure rephrasing.
162	        Multiple overlapping lines showing model and collaboration effects.
163	  ablation_figures:
164	    - figure_id: "Figure 5"
165	      viz_type: "line_plot"
166	      dimensions_varied:
167	        - "Temperature (1e-6, 0.25, 0.5, 0.75, 1.0)"
168	      design_note: >
169	        Temperature spectrum visualization for EN<->FR with Llama on 30 News2024 docs.
170	        Shows clear ordering: lower temperature = less degradation. Temperature 1e-6
171	        stabilizes after ~2 iterations (essentially deterministic). Clean parameter sweep.
172	    - figure_id: "Figure 6"
173	      viz_type: "line_plot"
174	      dimensions_varied:
175	        - "Prompt constraint level (simple, base, constrained)"
176	      design_note: >
177	        Shows more constrained prompts preserve higher relevance and factuality.
178	        Three lines with clear separation. On Llama, 30 News2024 docs, EN<->FR.
179	  figure_narrative_role: >
180	    Figure 1 (experimental overview) → Table 1 (qualitative distortion example) →
181	    Figure 2 (Exp1: language-dependent degradation curves) →
182	    Figure 3 (Exp2: multi-model collaboration effects) →
183	    Figure 4 (rephrasing as alternative task) →
184	    Figure 5 (temperature ablation) → Figure 6 (prompt constraint ablation).
185	    Narrative arc: setup → demonstrate problem → escalate complexity → explore mitigation.
186	
187	tables:
188	  table_count: 9
189	  main_result_table:
190	    table_id: "Table 2"
191	    row_axis: "datasets x models"
192	    col_axis: "language pairs (DE, FR, NL, TH, VN, ZH) with avg gradient + std error"
193	    row_organization: "by_category"
194	    col_organization: "grouped_by_language_pair"
195	    highlight_strategy: "Gradient values with standard errors; no bold/underline visible"
196	    statistical_reporting: "Average gradient +/- standard error across 150 documents"
197	    num_baselines: 0
198	    design_note: >
199	      FActScore gradients as primary metric—negative gradient = distortion rate per iteration.
200	      Organized as 3 datasets x 2 models = 6 rows, 6 language pairs as columns.
201	      The gradient representation is elegant: a single number captures 100 iterations of decline.
202	      Standard errors included for reliability. Compact but information-dense.
203	  ablation_tables:
204	    - table_id: "Table 1"
205	      what_varied: ["Iteration number (0, 2, 10, 50, 100)"]
206	      variation_style: "full_numbers"
207	      design_note: >
208	        Qualitative text example showing progressive distortion of a news article
209	        about a lorry driver. Not a metrics table—shows actual text at 5 snapshots
210	        across 100 iterations. Distortions highlighted in the text. Placed before
211	        quantitative results for immediate reader engagement. Functions as a
212	        motivating example that makes the abstract metric decline concrete.
213	    - table_id: "Tables 4-7 (Appendix)"
214	      what_varied: ["BLEURT scores across all experiments"]
215	      variation_style: "full_numbers"
216	      design_note: "Supplementary metric tables supporting main FActScore findings"
217	  supplementary_tables:
218	    in_appendix: true
219	    content: >
220	      Table 3: Default decoding parameters for each model.
221	      Tables 4-7: BLEURT scores across all four experiments.
222	      Table 8: Temperature variation detailed analysis.
223	      Additional appendix tables for comprehensive metric reporting.
224	    reason: >
225	      Main text focuses on FActScore gradient as the cleanest summary statistic.
226	      BLEURT and detailed parameter tables deferred to appendix to keep main text
227	      focused. Only 2 tables in main text (qualitative example + FActScore gradients)
228	      keeps the paper visually clean despite 450 documents x 100 iterations of data.
229	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "359657e5-9d0f-4f39-9f73-55d3553d93a3",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "40ddec7a-0c22-4649-a984-b48307d989e5",
  "sourceToolAssistantUUID": "359657e5-9d0f-4f39-9f73-55d3553d93a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T16:32:43.697Z_

<details open><summary>🔧 Tool call — Read · `toolu_0166Yrz9m58cqF89FVv9nz4h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/binoculars.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40ddec7a-0c22-4649-a984-b48307d989e5",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoA5TJeip8ipFUQsJp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dc71113c-a9b4-4554-9bac-0d306692672d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzMGCT8AANfAX2UUok2wDh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39778,
      "cache_read_input_tokens": 0,
      "output_tokens": 1917,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39778
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1917,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39778,
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

_source line 52 · 2026-05-22T16:32:43.702Z_

<details><summary>↩ Tool result · `toolu_0166Yrz9m58cqF89FVv9nz4h`</summary>

```text
1	paper_key: "binoculars"
2	title: "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"
3	venue: "ICML 2024"
4	full_text_available: true  # arXiv HTML v2 available
5	
6	research:
7	  baselines:
8	    - Ghostbuster
9	    - GPTZero
10	    - DetectGPT
11	    - Fast-DetectGPT
12	    - DNA-GPT
13	  metrics:
14	    - {name: "TPR at 0.01% FPR", direction: "higher_better"}
15	    - {name: "TPR at 0.1% FPR", direction: "higher_better"}
16	    - {name: "F1-Score", direction: "higher_better"}
17	    - {name: "AUC", direction: "higher_better"}
18	  datasets:
19	    - {name: "Ghostbuster News", size: "from Ghostbuster benchmark"}
20	    - {name: "Ghostbuster Creative Writing", size: "from Ghostbuster benchmark"}
21	    - {name: "Ghostbuster Student Essays", size: "from Ghostbuster benchmark"}
22	    - {name: "CCNews + LLaMA-2/Falcon generations", size: "custom dataset"}
23	    - {name: "PubMed + LLaMA-2/Falcon generations", size: "custom dataset"}
24	    - {name: "CNN + LLaMA-2/Falcon generations", size: "custom dataset"}
25	    - {name: "Orca (GPT-3/GPT-4 completions)", size: "millions of samples"}
26	    - {name: "M4 multilingual (Arxiv, Reddit, WikiHow, Wikipedia)", size: "multilingual benchmark"}
27	  ablation_dimensions:
28	    - "scoring model pairs (observer M1 x performer M2 combinations)"
29	    - "component contribution (PPL alone vs X-PPL alone vs ratio)"
30	    - "sequence length impact on detection"
31	    - "performer model fine-tuning steps (0, 1, 10, 50, 100, 500, full on Alpaca)"
32	    - "identical vs different M1/M2 models"
33	    - "ESL (English as Second Language) fairness"
34	    - "modified system prompts (default, Carl Sagan, non-robotic, pirate)"
35	    - "multilingual performance (Bulgarian, Urdu, low-resource languages)"
36	    - "famous/memorized text behavior"
37	    - "random token sequence behavior"
38	  training_recipe:
39	    optimizer: "N/A for main method (zero-shot inference)"
40	    lr: "5e-5 (for performer model fine-tuning ablation only)"
41	    hardware: "4 A5000 GPUs"
42	    fine_tuning_details: "Alpaca dataset, cosine annealing, 3% warmup, batch 65K tokens (32 samples x 2048 block), FSDP distributed"
43	  method_family: "dual-model perplexity ratio (zero-shot, training-free)"
44	
45	positioning:
46	  core_claim: "The ratio of perplexity to cross-perplexity from two closely related language models provides a simple, zero-shot detection score that achieves >90% TPR at 0.01% FPR on ChatGPT text, outperforming commercial detectors without any model-specific training."
47	  key_results: >
48	    News: 95% TPR @ 0.01% FPR.
49	    Creative Writing: 93% TPR @ 0.01% FPR.
50	    Student Essays: 98% TPR @ 0.01% FPR.
51	    ESL fairness: 99.67% accuracy on both original and grammar-corrected essays.
52	    Orca GPT-3: 92% accuracy. Orca GPT-4: 89.57%.
53	    Stylistic robustness: pirate voice prompting reduces sensitivity by only 1%.
54	  limitations:
55	    - "Only works on 'naturally occurring' text without adversarial evasion attempts"
56	    - "High false negative rate on GPT-4 (58% in March 2024 testing)"
57	    - "Low recall (but high precision) on low-resource languages (Bulgarian, Urdu)"
58	    - "Memorized famous texts sometimes classified as machine-generated (e.g., US Constitution scored 0.76)"
59	    - "Black-box nature: provides no explanation for predictions"
60	    - "Requires two forward passes through LLMs for each sample (computational cost)"
61	  relation_to_us: "competitor"  # directly competing zero-shot detection method; uses perplexity-based signal which is related to our depth analysis
62	
63	narrative:
64	  story_type: "化繁为简型"
65	  hook: >
66	    Opens with a bold contradiction of conventional wisdom: "Detecting text generated by modern large
67	    language models is thought to be hard" — then immediately reverses with "However, we find that a
68	    score based on contrasting two closely related language models is highly accurate." The surprise
69	    inversion grabs attention by promising a surprisingly simple solution to a supposedly hard problem.
70	  tension: >
71	    Multi-layered tension construction:
72	    (1) Model-specificity: "existing detectors rely on model-specific training data and often fail to transfer"
73	    (2) Wrong evaluation metrics: "many works focus on accuracy on balanced test sets and/or AUC...not well-suited for high-stakes detection" — reframes what success even means
74	    (3) Fairness concern: cites Liang et al. showing ESL essays wrongly flagged 48-76% by commercial detectors
75	    (4) The "capybara problem" (Section 3.2): entire dedicated section showing why naive perplexity fails — prompt context is unknown to detector, so high-perplexity text about "astrophysicist capybaras" is actually machine-generated
76	    Tension operates at both methodological and ethical levels.
77	  key_insight: >
78	    The capybara problem motivates the key insight: perplexity alone fails because prompt context is
79	    unknown, but the RATIO of perplexity to cross-perplexity normalizes for this. Cross-perplexity
80	    measures "how surprising one model's predictions are to another" — for machine text, both models
81	    predict similarly (low cross-perplexity), making the ratio distinctive. The insight is revealed
82	    through the capybara example (Table 1) where DetectGPT and GPTZero both fail but Binoculars succeeds.
83	  argument_chain: >
84	    detection is thought to be hard → existing methods are model-specific and use wrong metrics →
85	    ESL fairness is violated → naive perplexity fails due to unknown prompts (capybara problem) →
86	    insight: normalize perplexity by cross-perplexity to cancel prompt effects →
87	    Binoculars score B = log PPL / log X-PPL → SOTA at extremely low FPR (0.01%) →
88	    robust across models, languages, ESL text, and prompting styles
89	  contribution_framing: >
90	    Contributions stated implicitly rather than numbered bullets — woven into the prose.
91	    Core claims: (1) zero-shot SOTA without training data, (2) outperforms commercial systems,
92	    (3) transfers across LLM families. The implicit framing creates a sense of unified simplicity
93	    rather than a checklist of separate contributions.
94	  intro_structure: >
95	    2 main paragraphs (notably concise for a top venue):
96	    P1 — narrative hook: conventional wisdom is wrong, simple approach works
97	    (presents problem + surprising finding in same paragraph)
98	    P2 — method naming, key advantage (zero-shot), headline numbers (>90% TPR @ 0.01% FPR),
99	    breadth of applicability (multiple LLM families)
100	    The extreme brevity of intro is itself a stylistic choice matching the "simplicity" thesis.
101	  notable_technique: >
102	    The "capybara problem" — inventing a memorable, vivid name for a failure mode of prior methods.
103	    Section 3.2 + Table 1 create a concrete, almost humorous example (astrophysicist capybaras)
104	    that makes an abstract statistical concept (prompt-conditional perplexity) intuitively graspable.
105	    This named-problem technique makes the paper's contribution memorable and citeable.
106	
107	figures:
108	  figure_count: 15  # main paper + appendix
109	  figure1:
110	    type: "teaser_result"
111	    description: >
112	      Multi-dataset detection performance comparison showing ROC-style curves across three Ghostbuster
113	      datasets (News, Creative Writing, Student Essays). Binoculars shown against baselines
114	      (GPTZero, open-source detectors) with dramatic separation at low FPR.
115	    narrative_role: "Leads with the headline result — reader sees the performance gap before understanding the method. Creates motivation to keep reading for the 'how'."
116	    design_elements:
117	      - "three side-by-side panels for three domains"
118	      - "log-scale FPR axis to emphasize low-FPR regime"
119	      - "multiple baseline curves for comparison"
120	      - "Binoculars curve clearly dominant"
121	    visual_style: "Multi-panel ROC comparison, log-scale x-axis emphasizing the practically important low-FPR region. Clean lines, standard academic color palette."
122	  result_figures:
123	    - figure_id: "Figure 3"
124	      viz_type: "roc_curves"
125	      what_compared: "Detection methods on LLaMA-2-13B generations (log-scale FPR)"
126	      how_gain_highlighted: "Binoculars curve dominates at all FPR thresholds, especially at the extreme left (low FPR)"
127	      design_note: "Log-scale FPR axis is a deliberate methodological statement — the paper argues standard AUC hides poor low-FPR performance."
128	    - figure_id: "Figure 4"
129	      viz_type: "precision_recall_curves"
130	      what_compared: "ChatGPT detection across M4 domains (Arxiv, Reddit, WikiHow, Wikipedia)"
131	      how_gain_highlighted: "Binoculars maintains high precision across recall levels where baselines drop"
132	      design_note: "Multi-domain panels demonstrate generalization breadth."
133	    - figure_id: "Figure 5"
134	      viz_type: "bar_chart"
135	      what_compared: "Binoculars performance across various generative models"
136	      how_gain_highlighted: "Consistent high bars across model families"
137	      design_note: "Shows transfer capability — one detector, many source models."
138	    - figure_id: "Figure 9"
139	      viz_type: "bar_chart"
140	      what_compared: "F1-Score comparison across datasets"
141	      how_gain_highlighted: "Binoculars bars consistently tallest"
142	      design_note: "Supplementary metric for readers who prefer F1 over TPR@FPR."
143	  ablation_figures:
144	    - figure_id: "Figure 2"
145	      viz_type: "bar_chart"
146	      dimensions_varied: ["document size (number of tokens)"]
147	      design_note: "Shows detection maintains capability with few tokens — addresses practical concern about short texts."
148	    - figure_id: "Figure 7"
149	      viz_type: "distribution_plot"
150	      dimensions_varied: ["ESL original vs grammar-corrected essays"]
151	      design_note: "Score distributions overlap substantially for original and corrected ESL essays — directly addresses fairness concern from intro."
152	    - figure_id: "Figure 8"
153	      viz_type: "bar_chart"
154	      dimensions_varied: ["system prompt styles (default, Carl Sagan, non-robotic, pirate)"]
155	      design_note: "Robustness to stylistic prompting variation — only 1% sensitivity drop for pirate voice."
156	    - figure_id: "Figure 10"
157	      viz_type: "scatter_plot"
158	      dimensions_varied: ["sequence length vs Binoculars score"]
159	      design_note: "Demonstrates no strong correlation with length — score is length-agnostic."
160	    - figure_id: "Figure 11"
161	      viz_type: "distribution_plots"
162	      dimensions_varied: ["PPL alone vs X-PPL alone vs combined"]
163	      design_note: "Shows both components alone have poor separation; the ratio is key. Justifies the method design."
164	    - figure_id: "Figure 13"
165	      viz_type: "roc_curves"
166	      dimensions_varied: ["identical vs different M1/M2 models"]
167	      design_note: "Validates that using different (base vs instruct) models outperforms identical models."
168	    - figure_id: "Figure 14"
169	      viz_type: "histogram"
170	      dimensions_varied: ["random token sequences"]
171	      design_note: "Random tokens classified as human (mean ~1.35 vs ~1.0 for real human text) — edge case validation."
172	    - figure_id: "Figure 15"
173	      viz_type: "line_chart"
174	      dimensions_varied: ["performer model fine-tuning steps on Alpaca"]
175	      design_note: "Monotonic improvement with instruction tuning — explains why base+instruct pair works best."
176	  figure_narrative_role: >
177	    Figure 1 (teaser result — headline performance) → Section 3 method with capybara Table 1 →
178	    Figure 2 (document size robustness) → Figure 3 (detailed ROC comparison) →
179	    Figures 4-5 (cross-domain, cross-model generalization) → Figure 6 (multilingual) →
180	    Figure 7 (ESL fairness) → Figure 8 (prompt robustness) → Appendix figures (component analysis,
181	    random tokens, fine-tuning ablation).
182	    Flow: impress with results first → explain method → demonstrate breadth → address concerns → deep ablation.
183	    This "results-first" ordering is unusual and mirrors the intro's strategy of leading with the surprise.
184	
185	tables:
186	  table_count: 8  # primary tables + supplementary
187	  main_result_table:
188	    table_id: "Table 4"
189	    row_axis: "methods"
190	    col_axis: "datasets x metrics (AUC, TPR at 0.01%, 0.1%, 1%, 5% FPR)"
191	    row_organization: "by_category"  # individual components (Falcon PPL, Falcon X-PPL, LLaMA variants) then Binoculars variants
192	    col_organization: "grouped_by_dataset"
193	    highlight_strategy: "bold_best"
194	    statistical_reporting: "point estimates; confidence via separate Table 7 (standard errors for AUC and TPR)"
195	    num_baselines: 5  # Ghostbuster, GPTZero, DetectGPT, Fast-DetectGPT, DNA-GPT
196	    design_note: >
197	      Unusual: the main result table is Table 4 (not Table 1) because earlier tables serve
198	      methodological exposition. Table 1 is the capybara example, Table 2 is system prompt
199	      examples, Table 3 is model pair ablation. This ordering prioritizes method understanding
200	      over result reporting — the reader should understand WHY before seeing HOW WELL.
201	  ablation_tables:
202	    - table_id: "Table 1"
203	      what_varied: ["the capybara problem illustration — single example with scoring"]
204	      variation_style: "full_numbers"
205	      design_note: >
206	        Not a traditional ablation but a motivating example table. Shows one GPT-4 sample about
207	        'astrophysicist capybaras' with Falcon PPL (2.20), Binoculars score (0.73), DetectGPT (0.14),
208	        GPTZero (49.71%). Demonstrates failure of baselines on a concrete case. Placed in method
209	        section, not results — serves argumentative rather than evaluative purpose.
210	    - table_id: "Table 3"
211	      what_varied: ["scoring model pairs (observer M1 x performer M2)"]
212	      variation_style: "full_numbers"
213	      design_note: >
214	        Rows are different model pair combinations (Falcon-7B-Instruct, Llama-2-13B, etc.).
215	        Columns: PPL Scorer (M1), Cross-PPL Scorers (M1', M2), TPR @ 0.01% FPR, TPR @ 0.1% FPR,
216	        F1-Score, AUC. Best pair achieves 100% TPR at 0.01% FPR. Guides practitioner model selection.
217	    - table_id: "Table 5"
218	      what_varied: ["famous/memorized texts (US Constitution, 'I Have a Dream', songs, literary excerpts)"]
219	      variation_style: "full_numbers"
220	      design_note: >
221	        Rows: well-known texts. Columns: Human Sample, PPL, Cross PPL, Binoculars Score,
222	        Predicted as Human (checkmark/X). Reveals memorization failure mode — US Constitution
223	        misclassified. Honest about limitations rather than hiding them.
224	    - table_id: "Table 8"
225	      what_varied: ["newer model performance (GPT-4, Gemini)"]
226	      variation_style: "full_numbers"
227	      design_note: >
228	        Tests on models released after the method was developed.
229	        GPT-4: 58.13% false negative rate (major limitation).
230	        Gemini: 3.10% false negative rate (works well).
231	        Presented transparently as the method's biggest weakness.
232	  supplementary_tables:
233	    in_appendix: true
234	    content: >
235	      Table 2 (modified system prompt examples), Table 6 (multilingual details),
236	      Table 7 (confidence estimates with standard errors for AUC and TPR),
237	      additional ablation results for model fine-tuning and component analysis.
238	    reason: >
239	      Main paper front-loads the capybara motivation table and model pair ablation BEFORE
240	      the main results — unusual ordering that prioritizes understanding over performance showcase.
241	      Supplementary tables handle confidence intervals and edge cases to keep main narrative focused.
242	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc71113c-a9b4-4554-9bac-0d306692672d",
  "isSidechain": true,
  "promptId": "13e6ea77-bec0-4444-bf0c-71ff0b495169",
  "agentId": "aa334bf6bcdbf7cc3",
  "type": "user",
  "uuid": "2c17098d-02ee-408e-ab5c-17a91c9d9188",
  "sourceToolAssistantUUID": "dc71113c-a9b4-4554-9bac-0d306692672d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-22T16:37:46.776Z_

Here are the full contents of all 25 YAML files from `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/distill_tmp/`:

---

## 1. monitoring_ai_review.yaml

```yaml
paper_key: "monitoring_ai_review"
title: "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["expert-written reference texts", "AI-generated reference texts"]
  metrics:
    - {name: "estimated LLM-modified fraction", direction: "descriptive"}
  datasets:
    - {name: "ICLR 2024 peer reviews", size: "unknown"}
    - {name: "NeurIPS 2023 peer reviews", size: "unknown"}
    - {name: "CoRL 2023 peer reviews", size: "unknown"}
    - {name: "EMNLP 2023 peer reviews", size: "unknown"}
  ablation_dimensions: ["reviewer confidence level", "submission deadline proximity", "rebuttal engagement"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "corpus-level statistical estimation (maximum likelihood)"

positioning:
  core_claim: "Develops a maximum likelihood approach to estimate the fraction of LLM-modified text in large corpora, finding 6.5-16.9% of AI conference peer reviews are substantially LLM-modified."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 2. min_k_percent.yaml

```yaml
paper_key: "min_k_percent"
title: "Detecting Pretraining Data from Large Language Models"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["reference model-based detection methods"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "improvement over previous methods", direction: "higher_better"}
  datasets:
    - {name: "WikiMIA", size: "dynamic benchmark"}
  ablation_dimensions: ["percentage k threshold", "copyrighted book detection", "contaminated downstream examples", "privacy auditing"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot membership inference (token probability outlier detection)"

positioning:
  core_claim: "Proposes Min-K% Prob, a reference-free method that detects pretraining data by identifying text with outlier low-probability tokens, achieving 7.4% improvement on WikiMIA over prior methods."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 3. reliable_detection.yaml

```yaml
paper_key: "reliable_detection"
title: "Can AI-Generated Text be Reliably Detected?"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["watermarking-based detectors", "neural network-based detectors", "zero-shot classifiers", "retrieval-based detectors"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "detection accuracy under attack", direction: "higher_better"}
    - {name: "Total Variation distance", direction: "descriptive"}
  datasets:
    - {name: "passages of ~300 tokens", size: "unknown"}
  ablation_dimensions: ["recursive paraphrasing attack strength", "spoofing attack on watermarked LLMs"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "adversarial attack analysis on AI text detectors (recursive paraphrasing)"

positioning:
  core_claim: "Demonstrates that AI text detectors are unreliable in practice via recursive paraphrasing attacks, and provides theoretical bounds connecting best-possible detector AUROC to Total Variation distance between human and AI text distributions."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 4. detection_possibilities.yaml

```yaml
paper_key: "detection_possibilities"
title: "Position: On the Possibilities of AI-Generated Text Detection"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["RoBERTa-Large-Detector", "RoBERTa-Base-Detector", "GPTZero"]
  metrics:
    - {name: "sample complexity bounds", direction: "lower_better"}
    - {name: "detection accuracy", direction: "higher_better"}
  datasets:
    - {name: "Xsum", size: "unknown"}
    - {name: "Squad", size: "unknown"}
    - {name: "IMDb", size: "unknown"}
    - {name: "Kaggle FakeNews", size: "unknown"}
  ablation_dimensions: ["sample size", "sequence length", "generator model", "dataset domain"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "information-theoretic analysis of detection feasibility"

positioning:
  core_claim: "Proves that distinguishing human from LLM text is consistently achievable (except when distributions are indistinguishable) and derives sample complexity bounds for reliable detection, validated across multiple datasets and generators (GPT-2, GPT-3.5-Turbo, Llama, Llama-2-13B/70B)."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 5. detectgpt.yaml

```yaml
paper_key: "detectgpt"
title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
venue: "ICML 2023"
full_text_available: false

research:
  baselines: ["zero-shot detection baselines (unspecified)"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
  datasets:
    - {name: "fake news articles (GPT-NeoX 20B)", size: "unknown"}
  ablation_dimensions: ["perturbation model choice (T5)", "source model"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot detection via log-probability curvature (perturbation-based)"

positioning:
  core_claim: "Discovers that LLM-sampled text occupies negative curvature regions of the model's log probability function, and leverages this via random perturbations for zero-shot detection, achieving 0.95 AUROC vs 0.81 for the strongest baseline."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 6. intrinsic_dimension.yaml

```yaml
paper_key: "intrinsic_dimension"
title: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"
venue: "NeurIPS 2023"
full_text_available: false

research:
  baselines: ["SOTA detectors (unspecified in abstract)"]
  metrics:
    - {name: "intrinsic dimensionality", direction: "descriptive"}
    - {name: "detection accuracy", direction: "higher_better"}
  datasets:
    - {name: "multi-language texts (alphabet-based + Chinese)", size: "unknown"}
  ablation_dimensions: ["language", "text domain", "generator model", "human writer proficiency level"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "intrinsic dimension estimation + persistent homology (topological features)"

positioning:
  core_claim: "Proposes intrinsic dimensionality of text embeddings as a robust detection invariant, finding human texts average ~9 (alphabet-based) vs ~7.5 for AI-generated, with stable cross-domain and cross-model performance outperforming SOTA detectors."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 7. dsir.yaml

```yaml
paper_key: "dsir"
title: "Data Selection for Language Models via Importance Resampling"
venue: "NeurIPS 2023"
full_text_available: false

research:
  baselines: ["expert curation", "random selection", "heuristic filtering"]
  metrics:
    - {name: "KL reduction", direction: "higher_better"}
    - {name: "GLUE benchmark score", direction: "higher_better"}
    - {name: "correlation with downstream accuracy", direction: "higher_better"}
  datasets:
    - {name: "The Pile", size: "100M documents"}
    - {name: "GLUE benchmark", size: "unknown"}
    - {name: "Wikipedia and books", size: "unknown"}
  ablation_dimensions: ["target distribution", "feature space", "n-gram hash features"]
  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "processes 100M docs in 4.5 hours"}
  method_family: "importance resampling for data selection (hashed n-gram features)"

positioning:
  core_claim: "Proposes DSIR, a scalable data selection method using importance resampling with hashed n-gram features, achieving strong correlation (r=0.82) between KL reduction and downstream task performance."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "orthogonal"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 8. watermark_llm.yaml

```yaml
paper_key: "watermark_llm"
title: "A Watermark for Large Language Models"
venue: "ICML 2023"
full_text_available: false

research:
  baselines: ["unwatermarked generation"]
  metrics:
    - {name: "p-value (statistical test)", direction: "lower_better"}
    - {name: "text quality (human evaluation)", direction: "higher_better"}
  datasets:
    - {name: "OPT model generations", size: "unknown"}
  ablation_dimensions: ["green list size", "soft promotion strength", "text length"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "token-level watermarking (green list / red list partitioning)"

positioning:
  core_claim: "Proposes a watermarking framework for LLMs that embeds invisible signals by softly promoting 'green' tokens during sampling, detectable via a statistical test with interpretable p-values without API access, with negligible quality impact."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 9. curious_decline.yaml

```yaml
paper_key: "curious_decline"
title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
venue: "NAACL 2024 Findings"
full_text_available: true

research:
  baselines:
    - "Human-generated text (ground truth baseline)"
    - "OPT-350M finetuned on human data only (Iteration 0)"
  metrics:
    - {name: "Type-Token Ratio (TTR)", direction: "higher_better"}
    - {name: "Distinct-2", direction: "higher_better"}
    - {name: "Distinct-3", direction: "higher_better"}
    - {name: "1-Self-BLEU", direction: "higher_better"}
    - {name: "Syntactic Diversity (Div_syn)", direction: "higher_better"}
    - {name: "Semantic Diversity (Div_sem)", direction: "higher_better"}
    - {name: "Perplexity", direction: "lower_better"}
  datasets:
    - {name: "XL-SUM", size: "306,522 train / 11,535 test", task: "news summarization"}
    - {name: "ACL Anthology bibliography", size: "40,512 train / 2,132 test", task: "scientific abstract generation"}
    - {name: "WritingPrompts", size: "272,600 train / 15,138 test", task: "story generation"}
  ablation_dimensions:
    - "Task entropy level (low/medium/high creativity demands)"
    - "Synthetic data filtering (RoBERTa-CoLA acceptability filter, bottom 20% discarded)"
    - "Human data mixing (60% human held out, 10% injected per iteration)"
    - "Number of recursive iterations (1-6)"
  training_recipe:
    model: "OPT-350M (fresh instance per iteration)"
    optimizer: "AdamW"
    epochs: 5
    hardware: "2x NVIDIA RTX A6000"
    decoding_news: "p=0.1, tau=0.3, max_new_tokens=50"
    decoding_abstract: "p=0.5, tau=0.5, max_new_tokens=300"
    decoding_story: "p=0.9, tau=0.7, max_new_tokens=500"
    total_compute: "~700 GPU hours for story generation alone"
  method_family: "Recursive finetuning on self-generated synthetic data (model collapse investigation)"

positioning:
  core_claim: "Recursive training on synthetic data causes a remarkable, consistent decline in linguistic diversity—particularly syntactic diversity—even when task performance (perplexity) appears to improve, revealing that standard metrics mask a fundamental quality degradation."
  key_results: >
    Story generation TTR: Human 2.23% -> Iter1 0.84% -> Iter6 0.61%;
    Story Distinct-3: Human 70.6% -> Iter1 44.2% -> Iter6 38.6%;
    Story syntactic diversity: Human 4.84 -> Iter1 4.23 -> Iter6 1.96;
    Perplexity drops (improves) from 14.1 to 2.70 despite diversity collapse;
    Filtering synthetic data amplifies decline; mixing 10% human data per iteration insufficient to prevent it.
  limitations:
    - "Monolingual (English only); metrics rely on language-specific tools"
    - "OPT-350M only; larger models unexplored due to 700 GPU-hour cost"
    - "Cannot access real LM-generated web content; no reliable LM detection for web data"
    - "Single architecture (decoder-only); encoder-decoder unexplored"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: >
    Opens with scaling laws' promise of predictable improvement, then pivots sharply:
    high-quality data is running out (17 trillion tokens, 4-5% annual growth),
    and Meta's Llama 2 already consumed ~2 trillion—we are within an order of magnitude of exhaustion.
    This data scarcity frames synthetic data as simultaneously necessary and dangerous.
  tension: >
    Prior work on model collapse focused on task performance degradation (distribution tails disappearing,
    converging to uniform behaviors). But no one has systematically measured LINGUISTIC diversity—
    the quality dimension that matters for creative and varied text generation.
    The gap: we know synthetic training hurts performance, but we don't know how it reshapes language itself.
  key_insight: >
    Revealed through the three-task experimental ladder (Section 4): higher-entropy tasks
    (story generation) suffer the MOST diversity loss, and syntactic diversity collapses
    the fastest while semantic diversity stays deceptively stable. The counterintuitive finding
    is in Section 4.3—filtering synthetic data for quality AMPLIFIES diversity loss
    (because filters favor common patterns, removing diverse samples).
  argument_chain: >
    Data exhaustion crisis → synthetic data as inevitable supplement →
    prior work shows model collapse in performance → but what about linguistic diversity? →
    develop comprehensive diversity metrics (lexical + semantic + syntactic) →
    recursive finetuning across 3 tasks with varying entropy →
    diversity consistently declines, worst for creative tasks →
    syntactic diversity most vulnerable, semantic deceptively stable →
    mitigation attempts (filtering, mixing) fail → call for diversity-aware training
  contribution_framing: >
    Framed as two research questions rather than numbered contributions:
    (1) "How can linguistic diversity be quantified effectively?"
    (2) "Does recursive training on synthetic text reduce linguistic diversity?"
    Novel syntactic diversity metric via Weisfeiler-Lehman graph kernels on dependency trees
    is presented as a methodological contribution. The empirical finding is the main result.
  intro_structure: >
    4 paragraphs:
    P1 (Hook): Data exhaustion + scaling laws create tension
    P2 (Context): Three modes of synthetic data contamination (pretraining, finetuning, single-task)
    P3 (Gap): Model collapse known, but linguistic diversity unexamined
    P4 (This work): Metrics + experiments + key finding summary
  notable_technique: >
    The three-task design with explicitly varying "entropy levels" (low/medium/high creativity)
    creates a natural experimental gradient that makes the diversity-entropy interaction
    visible without additional analysis. The qualitative example in Table 1 (scientific abstracts
    progressively fixating on URLs and licensing statements) is a memorable illustration
    that makes the abstract metric decline tangible.

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: >
      Diagram of the recursive tuning-generation process across 6 iterations.
      Shows Data(0) -> Base(1) -> Model(1) -> Data(1) -> Base(2) -> Model(2) -> ... chain.
      Each Base is a fresh OPT-350M instance finetuned on the previous iteration's data.
    narrative_role: >
      Establishes the experimental protocol immediately—readers understand the recursive
      pipeline before any results are presented. Critical for grasping why diversity degrades:
      each iteration's training data is entirely synthetic from the prior model.
    design_elements:
      - "Sequential flow diagram with numbered iterations"
      - "Clear Base/Model/Data distinction"
      - "Arrow-based pipeline showing data flow"
    visual_style: >
      Linear left-to-right pipeline diagram. Clean boxes for each component
      (Base, Model, Data) connected by arrows. Iteration numbers as labels.
      Minimal color, focuses on structural clarity.
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      what_compared: >
        Lexical diversity (Distinct-3) and syntactic diversity across iterations 1-6
        under three conditions: pure synthetic, with filtering, with mixed human data.
        Story generation task.
      how_gain_highlighted: >
        Human baseline shown as reference level; all three conditions decline below it.
        The counterintuitive finding (filtering amplifies decline) is visually striking
        as the filtered line drops faster than pure synthetic.
      design_note: >
        Two-panel layout (a: lexical, b: syntactic). Lines with markers for each condition.
        Human baseline as horizontal reference. The visual immediately communicates
        that all mitigation attempts fail—powerful for the paper's pessimistic message.
  ablation_figures:
    - figure_id: "Figure 2 (serves dual purpose)"
      viz_type: "line_plot"
      dimensions_varied:
        - "Data regime (pure synthetic vs. filtered vs. mixed human)"
        - "Iteration number (1-6)"
      design_note: >
        Ablation is embedded in the main result figure rather than separated,
        making the comparison immediate. Three lines per panel keeps it readable.
  figure_narrative_role: >
    Figure 1 (method overview) → Table 1 (qualitative degradation example) →
    Table 2 (comprehensive quantitative results) → Figure 2 (mitigation failure visualization).
    Appendix: Figure 3 (word frequency histograms), Figure 4 (t-SNE syntactic embeddings),
    Figure 5 (t-SNE semantic embeddings)—supporting evidence for mechanisms.

tables:
  table_count: 3
  main_result_table:
    table_id: "Table 2"
    row_axis: "methods (iterations 1-6 + human baseline)"
    col_axis: "metrics (Perplexity, TTR, Distinct-2, Distinct-3, 1-Self-BLEU, Div_syn, Div_sem)"
    row_organization: "by_iteration"
    col_organization: "grouped_by_metric"
    highlight_strategy: "No bold/underline; human baseline as separate row for visual comparison"
    statistical_reporting: "Single run values (no std reported for main table)"
    num_baselines: 1
    design_note: >
      Three task panels (News, Abstract, Story) stacked vertically within one table.
      The table's power is in showing perplexity IMPROVING (2.48 → lower) while all diversity
      metrics worsen—the mismatch between standard evaluation and diversity is the visual punch.
      7 columns x ~24 rows, dense but organized by task sections.
  ablation_tables:
    - table_id: "Table 1"
      what_varied: ["Recursive iteration number (Human, Iter 1, 3, 5)"]
      variation_style: "full_numbers"
      design_note: >
        Qualitative example table showing actual generated abstract text across iterations.
        Not a metrics table—a TEXT table showing progressive fixation on URLs and
        licensing statements. Powerful because it makes the metric decline visceral.
        Functions as both example and ablation over iterations.
  supplementary_tables:
    in_appendix: true
    content: >
      Table 3: Average text lengths post-truncation (verifying fair comparison across iterations).
      Appendix also contains Figures 3-5 (word frequency histograms, t-SNE plots for
      syntactic and semantic embeddings).
    reason: >
      Length verification is a methodological detail; t-SNE plots support mechanistic
      claims but aren't essential for the main argument. Main text keeps only the
      metrics table and mitigation figure.
```

---

## 10. markovian_chains.yaml

```yaml
paper_key: "markovian_chains"
title: "Markovian Generation Chains in Large Language Models"
venue: "arXiv 2026"
full_text_available: false

research:
  baselines: []
  metrics:
    - {name: "output convergence pattern", direction: "descriptive"}
    - {name: "sentence diversity", direction: "descriptive"}
  datasets:
    - {name: "simulated iterative LLM outputs", size: "unknown"}
  ablation_dimensions: ["temperature parameter", "initial input sentence", "iteration count", "task type (rephrasing vs translation)"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "Markov chain analysis of iterative LLM inference"

positioning:
  core_claim: "Formalizes iterative LLM inference as Markovian generation chains, showing outputs either converge to recurrent sets or continue producing novel sentences, with diversity increasing or decreasing depending on temperature and initial input."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 11. paraphrase_evades.yaml

```yaml
paper_key: "paraphrase_evades"
title: "Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense"
venue: "NeurIPS 2023"
full_text_available: false

research:
  baselines: ["watermarking detectors", "GPTZero", "DetectGPT", "OpenAI text classifier"]
  metrics:
    - {name: "detection accuracy", direction: "higher_better"}
    - {name: "false positive rate", direction: "lower_better"}
  datasets:
    - {name: "GPT3.5-davinci-003 generations", size: "unknown"}
    - {name: "T5-XXL fine-tuned generations", size: "15M generations"}
  ablation_dimensions: ["lexical diversity", "content reordering", "paraphrase strength"]
  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "unknown"}
  method_family: "adversarial paraphrasing attack + retrieval-based defense"

positioning:
  core_claim: "Builds DIPPER (11B paraphraser) that drops DetectGPT accuracy from 70.3% to 4.6% at 1% FPR, and proposes a retrieval-based defense that searches previously generated sequences for semantic similarity, significantly outperforming existing detectors on paraphrased text."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 12. qurating.yaml

```yaml
paper_key: "qurating"
title: "QuRating: Selecting High-Quality Data for Training Language Models"
venue: "ICML 2024"
full_text_available: true  # via HuggingFace papers page; arXiv HTML not available

research:
  baselines:
    - Uniform sampling
    - Uniform sampling +50% data
    - DSIR (Wikipedia target)
    - DSIR (Book target)
    - Perplexity filtering (low perplexity)
    - Inverse perplexity sampling
    - Criteria mix (combining all 4 criteria)
  metrics:
    - {name: "Perplexity", direction: "lower_better"}
    - {name: "Average ICL accuracy (10 tasks)", direction: "higher_better"}
    - {name: "ARC-easy", direction: "higher_better"}
    - {name: "ARC-challenge", direction: "higher_better"}
    - {name: "SciQA", direction: "higher_better"}
    - {name: "LogiQA", direction: "higher_better"}
    - {name: "BoolQ", direction: "higher_better"}
    - {name: "HellaSwag", direction: "higher_better"}
    - {name: "PIQA", direction: "higher_better"}
    - {name: "WinoGrande", direction: "higher_better"}
    - {name: "NQ", direction: "higher_better"}
    - {name: "MMLU", direction: "higher_better"}
  datasets:
    - {name: "SlimPajama (QuRatedPajama)", size: "260B tokens annotated, 30B tokens selected for training"}
    - {name: "AboutMe", size: "10M webpages (for bias analysis)"}
  ablation_dimensions:
    - Quality criterion (writing_style / facts_trivia / educational_value / required_expertise)
    - Sampling temperature tau (0.0 top-k / 1.0 / 2.0 / uniform)
    - Multi-task vs separate QuRater models
    - Random vs pre-trained QuRater initialization
    - Curriculum ordering (low-to-high vs high-to-low expertise)
  training_recipe:
    model_size: "1.3B parameters"
    base_model: "Sheared-Llama-1.3B (for QuRater); custom 1.3B LM (for downstream)"
    training_tokens: "30B tokens (selected from 260B)"
    annotation_cost: "520 H100 GPU hours for corpus annotation"
    judgment_source: "GPT-3.5-turbo, 250K pairwise comparisons"
    snippet_length: "256-512 tokens for pairwise judgments"
    tokenizer: "Llama tokenizer"
    sequence_length: 1024
  method_family: "Data quality filtering via learned quality ratings (pairwise preference + Bradley-Terry)"

positioning:
  core_claim: "LLM-based pairwise quality judgments can be distilled into a lightweight scorer that enables quality-diversity balanced data selection, matching 50% more uniform training data with educational value filtering alone."
  key_results: "Educational value (tau=2.0): 46.7% avg ICL (+1.8% over uniform 30B baseline), matching uniform 45B baseline; QuRater validation accuracy >93%; GPT-3.5-turbo agreement with humans >91.9% across all criteria"
  limitations:
    - "Sensitive to LLM biases (language, positional bias in pairwise comparisons)"
    - "Results only on 1.3B models; unclear if findings transfer to larger scales"
    - "Documented social biases: gender (female roles suppressed), geography (Pacific Islands/SE Asia suppressed), topic (fashion/beauty suppressed by educational value)"
    - "Large-scale human quality validation still needed"
    - "Maintains original domain proportions; domain reweighting unexplored"
  relation_to_us: "complementary"  # QuRating's quality dimensions (especially writing style) inform what distinguishes human vs AI text; their finding that top-k quality selection hurts diversity parallels our interest in diversity loss from AI generation

narrative:
  story_type: "化繁为简型"  # Turns vague "data quality" into 4 concrete measurable dimensions + simple sampling framework
  hook: "Data quality is acknowledged as critical for LLM pre-training but remains poorly defined and hard to measure at scale"
  tension: "Existing approaches either use rule-based heuristics (too coarse) or classifier-based filtering (limited to one notion of quality); no framework captures multiple qualitative dimensions"
  key_insight: "Pairwise comparisons produce more stable quality judgments than absolute ratings (Kendall tau 0.79 vs 0.61), and a simple temperature-controlled sampling balances quality and diversity better than top-k selection"
  argument_chain: "Vague quality notion → decompose into 4 intuitive criteria → pairwise LLM judgments → Bradley-Terry distillation → lightweight QuRater model → temperature-controlled sampling → downstream gains + bias analysis"
  contribution_framing: "Three contributions: (1) framework for quality rating via pairwise comparisons, (2) QuRatedPajama 260B corpus with ratings, (3) empirical evidence that educational value selection matches 50% more data"
  intro_structure: "~5 paragraphs: P1 motivation (data quality matters), P2 existing approaches and gaps, P3 proposed approach overview, P4 key findings preview, P5 contributions list"
  notable_technique: "The 'compute equivalence' framing — showing quality selection matches uniform+50% data is more compelling than reporting raw accuracy gains"

figures:
  figure_count: 8  # 5 main + 3 appendix
  figure1:
    type: "method_overview"
    description: "Two-path flow diagram showing the QuRating pipeline: top path shows text pair comparison → LLM ranking → judgment collection → QuRater training; bottom path shows web-scale corpus → quality rating → data selection → LM training"
    narrative_role: "Provides complete system overview in one figure; establishes the two-stage approach (train rater, then use rater)"
    design_elements: ["flow diagram with boxes and arrows", "two parallel paths (annotation vs application)", "clear left-to-right progression"]
    visual_style: "Clean pipeline diagram; annotation pipeline on top, application pipeline on bottom; arrows connecting stages"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Win rates of QuRating-selected models vs uniform baseline after instruction fine-tuning"
      how_gain_highlighted: "Bar heights directly show win rate advantage for each quality criterion"
      design_note: "Bridges pre-training quality selection to instruction-following, showing downstream transfer"
    - figure_id: "Figure 4"
      viz_type: "distribution_plot"
      what_compared: "Quality rating distributions across SlimPajama domains (Wikipedia, Book, StackExchange, Github, ArXiv)"
      how_gain_highlighted: "Shows within-domain variance is large, justifying fine-grained selection over domain-level filtering"
      design_note: "Validates the premise that quality varies within domains, not just between them"
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "heatmap"
      dimensions_varied: ["criterion pairs (4x4 correlation matrix)"]
      design_note: "Correlation matrix showing criteria are complementary (r=0.29-0.55), justifying multi-dimensional approach"
    - figure_id: "Figure 6"
      viz_type: "scatter"
      dimensions_varied: ["perplexity vs ICL performance across tasks"]
      design_note: "Appendix figure demonstrating perplexity is a poor proxy for downstream ICL performance"
  figure_narrative_role: "Figure 1 (method overview) → Figure 2 (qualitative examples) → Figure 3 (downstream results) → Figure 4 (distribution analysis) → Figure 5 (criterion correlation) — moves from 'what we do' to 'does it work' to 'why it works'"

tables:
  table_count: 10  # main tables + appendix tables
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "perplexity + 10 ICL tasks grouped by category (reading comprehension, commonsense reasoning, world knowledge) + average"
    row_organization: "by_category"  # grouped as: baselines, QuRating variants by criterion and temperature, other baselines
    col_organization: "grouped_by_dataset"  # tasks grouped into 3 categories
    highlight_strategy: "bold_best per column; comparison against uniform baseline"
    statistical_reporting: "single run numbers (no std reported in main table)"
    num_baselines: 5  # uniform, uniform+50%, DSIR x2, perplexity filtering
    design_note: "16 rows covering criterion x temperature grid; clear separation between QuRating variants and external baselines; the '+50% data' uniform row provides compute-equivalence reference point"
  ablation_tables:
    - table_id: "Table 6"
      what_varied: ["multi-task vs separate models", "random vs pre-trained initialization"]
      variation_style: "full_numbers"  # accuracy percentages at different confidence margins
      design_note: "Shows multi-task QuRater matches separate per-criterion models, justifying single-model approach"
    - table_id: "Table 2"
      what_varied: ["quality criterion", "demographic dimensions (topics, roles, regions)"]
      variation_style: "full_numbers"  # retention rates
      design_note: "Bias analysis table showing amplification/suppression patterns; uses sub-columns for each criterion"
  supplementary_tables:
    in_appendix: true
    content: "Detailed per-task perplexity (Table 8), per-task ICL scores (Table 9), corpus composition (Table 7), validation data sources (Tables 3-4), judgment dataset stats (Table 5), extensive document inspection at quality percentiles (Tables 10-40+)"
    reason: "Main table shows aggregated results; appendix provides per-task breakdowns and qualitative evidence at different quality levels"
```

---

## 13. fast_detectgpt.yaml

```yaml
paper_key: "fast_detectgpt"
title: "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"
venue: "ICLR 2024"
full_text_available: true

research:
  baselines:
    - DetectGPT
    - NPR
    - DNA-GPT
    - Likelihood
    - LogRank
    - Entropy
    - LRR
    - RoBERTa-base (OpenAI GPT-2 detector)
    - RoBERTa-large (OpenAI GPT-2 detector)
    - GPTZero
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "Relative Improvement", direction: "higher_better", note: "(new-old)/(1.0-old)"}
    - {name: "Speedup", direction: "higher_better"}
  datasets:
    - {name: "XSum", domain: "news articles"}
    - {name: "SQuAD", domain: "Wikipedia contexts"}
    - {name: "WritingPrompts", domain: "story writing"}
    - {name: "WMT16-en", domain: "English translation"}
    - {name: "WMT16-de", domain: "German translation"}
    - {name: "PubMedQA", domain: "biomedical research QA"}
  ablation_dimensions:
    - sampling_model_choice
    - normalization_effect
    - passage_length
    - decoding_strategy (top-p, top-k, temperature)
    - paraphrasing_attack_robustness
    - in_distribution_vs_out_distribution
  training_recipe:
    optimizer: "N/A (zero-shot, no training)"
    lr: "N/A"
    hardware: "Tesla A100 GPU"
    inference_time: "233 seconds for full evaluation (vs 79113 seconds for DetectGPT)"
  method_family: "zero-shot detection via probability curvature"

positioning:
  core_claim: "Conditional probability curvature at token level is a more fundamental and efficient indicator of machine-generated text than perturbation-based probability curvature, achieving 340x speedup and ~75% relative accuracy improvement over DetectGPT."
  key_results: "White-box AUROC 0.9887 (+74.7% relative over DetectGPT); Black-box AUROC 0.9677 (+74.5% relative); ChatGPT detection AUROC 0.9615 (+78.3% relative); GPT-4 detection AUROC 0.9061 (+75.1% relative); 340x speedup (4 min vs 22 hours)"
  limitations:
    - "Theoretical explorations of why conditional probability curvature works are earmarked for future work"
    - "Relies on pre-trained models to span multiple domains/languages; no single model covers all linguistic territories in black-box setting"
    - "Focus predominantly on empirical advancements rather than theoretical foundations"
  relation_to_us: "competitor"

narrative:
  story_type: "化繁为简型"
  hook: "LLMs have transformed productivity but create risks of fake news, malicious reviews, and plagiarism; the fluency of generated text makes detection 'challenging even for experts.'"
  tension: "DetectGPT is the leading zero-shot detector but requires ~100 model calls per passage for perturbation, creating prohibitive computational costs (22 hours for a benchmark)."
  key_insight: "Revealed in paragraph 4 of intro—'machines lean towards tokens with higher statistical probability' while 'humans craft sentences based on underlying meanings, intentions, and contexts rather than data statistics.' This asymmetry means conditional probability p(x̃|x) reaches maximum at machine-generated x (positive curvature ~3) vs near zero for human text."
  argument_chain: "LLMs create detection need → existing zero-shot methods work but are slow → core hypothesis about token-level selection difference → conditional probability curvature as efficient proxy → single forward pass via conditional independent sampling → 340x speedup + 75% accuracy gain → validated across white-box, black-box, real-world (ChatGPT/GPT-4), cross-domain, cross-language settings"
  contribution_framing: "Three numbered contributions: (1) unveiling/validating hypothesis, (2) proposing efficient method, (3) achieving SOTA. Framing emphasizes both conceptual insight and practical gains."
  intro_structure: "4 paragraphs: P1=context+risk (LLMs dual nature), P2=related work landscape (supervised vs zero-shot), P3=problem statement (DetectGPT's computational bottleneck), P4=solution+contributions (hypothesis + method + results)"
  notable_technique: "The connection revelation—showing the curvature numerator decomposes into Likelihood + Entropy baselines, positioning Fast-DetectGPT as a principled unification rather than just a speedup trick."

figures:
  figure_count: 5
  figure1:
    type: "motivation"
    description: "Distribution of conditional probability curvatures for human-written vs machine-generated passages across four source models (GPT-2, OPT-2.7, Neo-2.7, GPT-J) on XSum dataset with 30-token prefix."
    narrative_role: "Visual proof of core hypothesis—clean separation between human (curvature≈0) and machine (curvature≈3) distributions motivates the entire method."
    design_elements: ["overlaid density distributions", "multiple source models in one plot", "clear separation visualization", "contrasting colors for human vs machine"]
    visual_style: "Histogram/density plot with overlaid distributions; human texts cluster at 0, machine texts at ~3; four model variants shown to demonstrate generality; single unified panel."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "ROC curves for multiple detection methods on WritingPrompts dataset"
      how_gain_highlighted: "Fast-DetectGPT curve dominates upper-left region; log scale emphasizes differences at low false positive rates"
      design_note: "Log-scale ROC is unusual but effective for emphasizing practical operating points (low FPR); dashed random baseline."
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Detection AUROC vs passage word count for ChatGPT and GPT-4 generations"
      how_gain_highlighted: "Fast-DetectGPT shows consistent monotonic improvement; baselines plateau or are inconsistent"
      design_note: "Two subplots (ChatGPT/GPT-4) side-by-side; multiple colored lines per detector; demonstrates robustness to passage length."
    - figure_id: "Figure 5"
      viz_type: "bar_chart"
      what_compared: "Supervised vs zero-shot detectors on in-distribution (XSum, WMT16-en) and out-distribution (PubMedQA, WMT16-de) datasets"
      how_gain_highlighted: "Fast-DetectGPT bars consistently tallest; supervised detectors visibly degrade on out-distribution while Fast-DetectGPT maintains performance"
      design_note: "Grouped bars by dataset; clean separation of in-distribution vs out-distribution highlights generalization advantage of zero-shot approach."
  ablation_figures: []
  figure_narrative_role: "Figure 1 (motivation: hypothesis visualization) → Figure 2 (method: architecture comparison) → Figure 3 (validation: ROC curves) → Figure 4 (robustness: length sensitivity) → Figure 5 (generalization: cross-domain comparison). Clean progression from why → how → does it work → how robust → how general."

tables:
  table_count: 9
  main_result_table:
    table_id: "Table 2"
    row_axis: "methods"
    col_axis: "source models (GPT-2, OPT-2.7, Neo-2.7, GPT-J, NeoX) × settings (white-box, black-box)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "† marks second-best; ♢ marks methods requiring multiple model calls; relative improvement percentages in bottom row"
    statistical_reporting: "AUROC values (single run implied, no std reported in main tables)"
    num_baselines: 8
    design_note: "Two-section layout (white-box / black-box) in single table enables direct setting comparison; symbolic markers (†, ♢) add information density without cluttering numbers."
  ablation_tables:
    - table_id: "Table 9 (Appendix F.1)"
      what_varied: ["decoding strategy (top-p, top-k, temperature)"]
      variation_style: "full_numbers"
      design_note: "Shows robustness across decoding strategies; relative improvements (95%, 81%, 99%) demonstrate method generality."
  supplementary_tables:
    in_appendix: true
    content: "Tables 4-9 cover: source model details (Table 4), detailed per-dataset results for open-source models (Table 5), additional breakdowns, and decoding strategy robustness (Table 9). Paraphrasing attack results also in appendix."
    reason: "Main paper keeps 3 tables for key claims (overview, detailed comparison, real-world); appendix holds exhaustive per-dataset/per-model/per-strategy breakdowns for reproducibility."
```

---

## 14. gltr.yaml

```yaml
paper_key: "gltr"
title: "GLTR: Statistical Detection and Visualization of Generated Text"
venue: "ACL 2019"
full_text_available: false

research:
  baselines: ["unaided human detection (54% accuracy)"]
  metrics:
    - {name: "human detection rate", direction: "higher_better"}
    - {name: "word probability", direction: "descriptive"}
    - {name: "absolute rank", direction: "descriptive"}
    - {name: "predicted distribution entropy", direction: "descriptive"}
  datasets:
    - {name: "human-subjects study data", size: "unknown"}
  ablation_dimensions: ["sampling scheme", "statistical test type (probability, rank, entropy)"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "statistical detection via token-level probability visualization"

positioning:
  core_claim: "Proposes a visual forensic tool using three simple statistical tests (word probability, rank, entropy) that improves human detection of generated text from 54% to 72% without prior training."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 15. diveye.yaml

```yaml
paper_key: "diveye"
title: "Diversity Boosts AI-Generated Text Detection"
venue: "TMLR 2026"
full_text_available: false

research:
  baselines: ["zero-shot detectors (unspecified)", "fine-tuned detectors (unspecified)"]
  metrics:
    - {name: "detection accuracy improvement", direction: "higher_better"}
    - {name: "robustness to paraphrasing", direction: "higher_better"}
    - {name: "cross-domain generalization", direction: "higher_better"}
  datasets:
    - {name: "multiple benchmarks (unspecified in abstract)", size: "unknown"}
  ablation_dimensions: ["surprisal-based feature types", "auxiliary signal integration", "domain transfer", "adversarial robustness"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "surprisal-based diversity features for zero-shot detection (DivEye)"

positioning:
  core_claim: "Proposes DivEye, a framework capturing rhythmic unpredictability fluctuations in text, outperforming zero-shot detectors by up to 33.2% and boosting existing detectors by up to 18.7% as an auxiliary signal, with robustness to paraphrasing and adversarial attacks."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 16. curse_of_recursion.yaml

```yaml
paper_key: "curse_of_recursion"
title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
venue: "Nature 2024"
full_text_available: false

research:
  baselines: ["models trained on original (non-synthetic) data"]
  metrics:
    - {name: "distribution tail preservation", direction: "higher_better"}
    - {name: "model quality degradation", direction: "descriptive"}
  datasets:
    - {name: "recursively generated training data", size: "unknown"}
  ablation_dimensions: ["model architecture (VAE, GMM, LLM)", "generation recursion depth", "synthetic data fraction"]
  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "unknown"}
  method_family: "model collapse analysis (recursive training on synthetic data)"

positioning:
  core_claim: "Demonstrates 'Model Collapse' — training on model-generated content causes irreversible distribution tail loss, shown across VAEs, GMMs, and LLMs, with implications for web-scraped training data as LLM content proliferates."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 17. ood_baseline.yaml

```yaml
paper_key: "ood_baseline"
title: "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks"
venue: "ICLR 2017"
full_text_available: false

research:
  baselines: []
  metrics:
    - {name: "maximum softmax probability", direction: "higher_better"}
    - {name: "detection performance (AUROC implied)", direction: "higher_better"}
  datasets:
    - {name: "computer vision benchmarks (unspecified)", size: "unknown"}
    - {name: "NLP benchmarks (unspecified)", size: "unknown"}
    - {name: "ASR benchmarks (unspecified)", size: "unknown"}
  ablation_dimensions: ["task domain (CV, NLP, ASR)", "misclassification vs OOD detection"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "softmax probability baseline for OOD detection"

positioning:
  core_claim: "Establishes a simple maximum softmax probability baseline for detecting misclassified and out-of-distribution examples across CV, NLP, and ASR, demonstrating the task is underexplored despite the baseline's effectiveness."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 18. synthid_text.yaml

```yaml
paper_key: "synthid_text"
title: "Scalable Watermarking for Identifying Large Language Model Outputs"
venue: "Nature 2024"
full_text_available: false

research:
  baselines: ["Gumbel sampling (non-distortionary)", "Soft Red List sampling (distortionary)", "unwatermarked generation"]
  metrics:
    - {name: "TPR at fixed FPR", direction: "higher_better"}
    - {name: "perplexity", direction: "lower_better"}
    - {name: "human preference ratings", direction: "higher_better"}
  datasets:
    - {name: "ELI5 (Explain Like I'm 5)", size: "unknown"}
    - {name: "Gemini chatbot interactions", size: "~20M interactions"}
  ablation_dimensions: ["watermark type (distortionary vs non-distortionary)", "tournament sampling", "speculative sampling integration"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "production Gemini systems"}
  method_family: "production-scale text watermarking (tournament sampling + sliding-window seeds)"

positioning:
  core_claim: "Introduces SynthID-Text, a production-ready watermarking method deployed on ~20M Gemini interactions, preserving text quality (no significant human preference difference) with high detection accuracy and minimal latency via tournament sampling integrated with speculative decoding."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 19. nucleus_sampling.yaml

```yaml
paper_key: "nucleus_sampling"
title: "The Curious Case of Neural Text Degeneration"
venue: "ICLR 2020"
full_text_available: false

research:
  baselines: ["beam search", "top-k sampling", "temperature sampling", "greedy decoding"]
  metrics:
    - {name: "text quality (human evaluation)", direction: "higher_better"}
    - {name: "text diversity", direction: "higher_better"}
    - {name: "distributional similarity to human text", direction: "higher_better"}
  datasets:
    - {name: "open-ended text generation benchmarks (unspecified)", size: "unknown"}
  ablation_dimensions: ["decoding strategy", "nucleus threshold p", "text length"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "decoding strategy (nucleus/top-p sampling)"

positioning:
  core_claim: "Reveals distributional disparities between human and machine text under likelihood-based decoding, and proposes Nucleus Sampling (top-p) that dynamically truncates the unreliable tail of the probability distribution to generate diverse yet coherent text."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 20. dna_gpt.yaml

```yaml
paper_key: "dna_gpt"
title: "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text"
venue: "ICLR 2024"
full_text_available: true  # via ar5iv HTML rendering

research:
  baselines:
    - GPTZero
    - "OpenAI's official classifier (fine-tuned on 34 models)"
    - DetectGPT  # white-box only comparison
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "TPR at 1% FPR", direction: "higher_better"}
  datasets:
    - {name: "Reddit ELI5", size: "150-300 instances, physics/biology, Jan 2022-Mar 2023"}
    - {name: "Scientific Abstracts", size: "150-300 instances, Nature, April 2023"}
    - {name: "PubMedQA", size: "150-300 instances, biomedical domain"}
    - {name: "Xsum", size: "150-300 instances, news summarization"}
    - {name: "WMT16", size: "English and German machine translation"}
  ablation_dimensions:
    - "truncation ratio gamma (0.02-0.98, optimal 0.5)"
    - "number of re-generations K (1-20, saturates ~10 black-box, ~5 white-box)"
    - "decoding temperature (0.7, 1.0, 1.4, 1.8)"
    - "revision attack ratio (0-0.5, using T5-3B span replacement)"
    - "starting n-gram n0 (1-6, optimal 4)"
    - "weight function f(n) (log(n), n, n*log(n), n*log^2(n), n^2, e^n)"
    - "maximum n-gram N (set to 25)"
    - "non-English language (German via WMT16)"
    - "proxy model size (OPT-125M, GPT2-124M as proxies)"
    - "model version drift over time (41-day interval)"
    - "sliding window for mixed human+AI content"
  training_recipe:
    optimizer: "N/A (training-free, zero-shot method)"
    lr: "N/A"
    hardware: "N/A (uses LLM API calls; K regenerations per sample)"
  method_family: "re-generation + divergence analysis (zero-shot, training-free)"

positioning:
  core_claim: "Truncating text and comparing re-generated continuations via n-gram overlap (black-box) or probability divergence (white-box) provides training-free, explainable detection that outperforms trained classifiers including OpenAI's own."
  key_results: >
    GPT-4 on Reddit-ELI5: 99.63 AUROC, 87.34% TPR@1%FPR (vs GPTZero 94.50/36.00, OpenAI 71.64/5.00).
    White-box text-davinci-003: 100.00 AUROC on Reddit and Xsum.
    Robust under 50% text revision: 98.48 AUROC (vs GPTZero ~60, OpenAI ~50).
    German detection: ~98 AUROC white-box (vs GPTZero ~50 random chance).
  limitations:
    - "Evaluated only on decoder-only GPT-architecture models; cannot reliably detect non-decoder-only generated text"
    - "Tested only on 1000-2000 character texts; significantly shorter/longer texts may fail"
    - "Black-box detection requires K API calls per sample (cost/latency overhead)"
    - "Proxy model detection with small models (OPT-125M) only reaches 73-82 AUROC, leaving room for improvement"
    - "Dataset memorization issue: WikiText-103 shows dramatic degradation because model memorizes training data"
  relation_to_us: "competitor"  # directly competing zero-shot detection method; our depth-fingerprint approach is conceptually related but uses different signal

narrative:
  story_type: "突破局限型"
  hook: >
    Opens with the societal urgency of ChatGPT/GPT-4 release sparking global AI safety discussions,
    positioning detection as a pressing real-world problem. First sentence: "The release of ChatGPT and
    GPT-4 by OpenAI has sparked global discussions on the effective utilization of AI-assistant writing."
  tension: >
    Three-layer tension build:
    (1) Training-based detectors become obsolete when models update — inflexibility problem.
    (2) Methods requiring token probabilities (e.g., DetectGPT) fail for closed-source APIs — accessibility problem.
    (3) Existing approaches lack interpretability — explainability problem.
    Each layer eliminates a class of prior methods, leaving no satisfactory existing solution.
  key_insight: >
    Revealed in Section 3 as the formal "Likelihood-Gap Hypothesis": machine text shows high consistency
    when regenerated from the same prefix (low divergence), while human text shows high diversity
    (high divergence). This is grounded in the empirical observation that "given appropriate preceding text,
    LLMs tend to output highly similar text across multiple runs of generations."
    The insight is first conceptually hinted in intro paragraph 4, then formalized mathematically as a boxed hypothesis.
  argument_chain: >
    societal urgency (ChatGPT release) → training-based methods inflexible →
    perturbation methods require white-box access → no method provides explainability →
    empirical observation: regeneration consistency differs for human vs machine →
    likelihood-gap hypothesis (formalized) → BScore (black-box) and WScore (white-box) algorithms →
    SOTA on 5 datasets × 5 models + robustness to revision/temperature/language/model-drift
  contribution_framing: >
    3 numbered contributions at end of introduction:
    (1) identify the divergence phenomenon with theoretical hypothesis,
    (2) develop zero-shot detection for both black/white-box,
    (3) demonstrate SOTA + robustness + explainability.
    Framing emphasizes novelty on three axes: theory, method, and practical properties.
  intro_structure: >
    4 paragraphs:
    P1 — societal context/urgency (ChatGPT release, AI writing concerns)
    P2 — gap identification (training-based obsolescence, white-box requirement, DetectGPT failure)
    P3 — explainability need (pressing demand for interpretable detection)
    P4 — approach introduction (two scenarios, core observation, contribution list)
  notable_technique: >
    Uses the "elimination ladder": each paragraph in the intro eliminates one category of existing
    methods (trained classifiers → perturbation methods → uninterpretable black-boxes), creating
    a narrowing funnel that leaves only the proposed approach as viable. This makes the contribution
    feel inevitable rather than arbitrary.

figures:
  figure_count: 8  # 7 in main text + 1 in appendix (sliding window)
  figure1:
    type: "method_overview"
    description: >
      Split-panel workflow diagram showing the three-stage DNA-GPT pipeline:
      (Left) original text split at truncation point into X' (preceding) and Y0 (remaining);
      (Center) X' fed to LLM K times generating {Y1,...,Yk};
      (Right) BScore/WScore calculation comparing regenerations against Y0, with threshold classification.
    narrative_role: "Provides the method overview immediately after the introduction, anchoring the reader's understanding of the truncate-regenerate-compare pipeline before mathematical formalization."
    design_elements:
      - "flowchart with rectangular text boxes and directional arrows"
      - "explicit truncation point visualization"
      - "K parallel regeneration paths"
      - "equation notation integrated into diagram"
    visual_style: "Horizontal flowchart, clean boxes with arrows, mathematical notation embedded. Functional rather than decorative — prioritizes clarity of the pipeline stages."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "dual_histogram"
      what_compared: "Log-likelihood distributions of machine-generated vs human-written text continuations on Reddit prompts (text-davinci-003)"
      how_gain_highlighted: "Clear visual separation between two distributions demonstrates the likelihood-gap hypothesis is empirically supported"
      design_note: "Placed right after the hypothesis statement as immediate visual evidence. The non-overlapping distributions make the theoretical claim viscerally convincing."
    - figure_id: "Figure 6"
      viz_type: "grouped_bar_chart"
      what_compared: "German vs English detection performance across methods (white-box and black-box)"
      how_gain_highlighted: "GPTZero drops to ~50 AUROC (random chance) on German while DNA-GPT maintains ~88-98, creating dramatic visual contrast"
      design_note: "Cross-lingual robustness as a differentiator — baseline collapse on non-English makes DNA-GPT advantage unmistakable."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      dimensions_varied: ["truncation ratio gamma"]
      design_note: "Shows inverted-U curve peaking at gamma=0.5; both extremes degrade. Clean parametric sweep visualization."
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      dimensions_varied: ["number of re-generations K"]
      design_note: "Shows saturation behavior — AUROC plateaus at K=10, TPR at K=5. Justifies practical parameter choice."
    - figure_id: "Figure 5"
      viz_type: "grouped_bar_chart"
      dimensions_varied: ["decoding temperature (0.7, 1.0, 1.4, 1.8)"]
      design_note: "Baselines degrade sharply at high temperature while DNA-GPT shows ~2% drop. Robustness claim visualized."
    - figure_id: "Figure 7"
      viz_type: "line_plot"
      dimensions_varied: ["revision attack ratio (0.0-0.5)"]
      design_note: "DNA-GPT curve stays flat (~99-98 AUROC) while baselines plummet to 50-60. Most compelling robustness evidence."
  figure_narrative_role: >
    Figure 1 (method overview) → Figure 2 (hypothesis evidence via distribution separation) →
    Figures 3-4 (parameter sensitivity: truncation ratio, K) → Figure 5 (temperature robustness) →
    Figure 6 (cross-lingual generalization) → Figure 7 (revision attack robustness).
    Flow: understand pipeline → believe the signal exists → tune parameters → stress-test robustness.

tables:
  table_count: 16  # 3 main + 13 appendix
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets x metrics (AUROC + TPR@1%FPR)"
    row_organization: "by_category"  # grouped by target model (GPT-4, GPT-3.5-turbo, text-davinci-003), then baselines vs DNA-GPT variants within each group
    col_organization: "grouped_by_dataset"  # Reddit-ELI5, Scientific Abstracts, PubMedQA, Xsum columns, each with AUROC and TPR sub-columns
    highlight_strategy: "bold_best"
    statistical_reporting: "single-run point estimates (no std reported)"
    num_baselines: 3  # GPTZero, OpenAI classifier, DetectGPT (white-box only)
    design_note: >
      Three-level grouping (model → method → parameter variant) creates a comprehensive but dense table.
      DNA-GPT variants shown with different K and gamma settings to demonstrate parameter sensitivity
      within the main results table rather than relegating to ablation.
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["source model identity for model sourcing task"]
      variation_style: "full_numbers"
      design_note: "Novel task (model sourcing) presented as a separate table with pairwise model comparisons. Shows the method's unique capability beyond binary detection."
    - table_id: "Table 3"
      what_varied: ["open-source vs closed-source models", "black-box vs white-box setting"]
      variation_style: "full_numbers"
      design_note: "Demonstrates generalization to open-source models (GPT-NeoX-20B, LLaMa-13B) on Xsum and Reddit. Baselines show dramatic degradation."
  supplementary_tables:
    in_appendix: true
    content: >
      Tables 4-16 in appendix: prompt templates, detailed parameter sensitivity results
      (n-gram starting value, weight function, maximum n-gram), model version drift results,
      sliding window mixed-content results, proxy model performance, additional dataset results,
      and example evidence outputs with highlighted n-gram overlaps.
    reason: >
      Main paper keeps 3 tables focused on core claims (SOTA, model sourcing, open-source generalization).
      Exhaustive parameter sweeps and additional analyses relegated to appendix to maintain narrative flow
      while supporting reproducibility.
```

---

## 21. uchendu_attribution.yaml

```yaml
paper_key: "uchendu_attribution"
title: "Authorship Attribution for Neural Text Generation"
venue: "EMNLP 2020"
full_text_available: false

research:
  baselines: ["human-written text baseline"]
  metrics:
    - {name: "classification accuracy", direction: "higher_better"}
  datasets:
    - {name: "human-written + 8 generator outputs (CTRL, GPT, GPT2, GROVER, XLM, XLNET, PPLM, FAIR)", size: "unknown"}
  ablation_dimensions: ["attribution task type (same-method verification, human-vs-machine, k-way generator identification)", "generator model"]
  training_recipe: {optimizer: "unknown", lr: "unknown", hardware: "unknown"}
  method_family: "supervised authorship attribution (multi-class generator classification)"

positioning:
  core_claim: "Formulates three authorship attribution problems for neural text (same-method verification, human-vs-machine, k-way identification) and evaluates classifiers across 8 generators, finding GPT2/GROVER/FAIR produce the most human-like text that confuses classifiers."
  key_results: "N/A - abstract only"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## 22. writing_diversity.yaml

```yaml
paper_key: "writing_diversity"
title: "Does Writing with Language Models Reduce Content Diversity?"
venue: "ICLR 2024"
full_text_available: true  # arXiv HTML available at 2309.05196v3

research:
  baselines:
    - Solo writing (no AI assistance)
    - GPT3-assisted writing (davinci base model)
    - InstructGPT-assisted writing (text-davinci-003)
  metrics:
    - {name: "Homogenization (avg pairwise Rouge-L similarity)", direction: "lower_better"}
    - {name: "Homogenization (avg pairwise BertScore similarity)", direction: "lower_better"}
    - {name: "Lexical diversity (unique n-gram fraction)", direction: "higher_better"}
    - {name: "Key point diversity (clustered unique arguments)", direction: "higher_better"}
    - {name: "5-gram distribution concentration", direction: "lower_better"}
  datasets:
    - {name: "Custom essay corpus", size: "300 argumentative essays, 38 writers, 10 topics from NY Times Student Opinion"}
  ablation_dimensions:
    - Model type (GPT3 base vs InstructGPT)
    - Text attribution (user-contributed vs model-contributed)
    - Diversity granularity (lexical n-gram vs semantic key-point)
    - Clustering threshold for key point diversity (0.5-0.8)
    - Per-topic vs aggregate analysis
  training_recipe:
    participants: "38 professional writers from Upwork (native English speakers)"
    task: "Argumentative essays ~300 words on 10 topics"
    design: "3 conditions x 10 topics x 10 essays = 300 essays"
    models_used: "OpenAI davinci (GPT3) and text-davinci-003 (InstructGPT)"
    decoding: "temperature=0.9, frequency_penalty=0.5, top_p=1.0"
    min_queries: ">=5 model suggestions required per essay"
    key_point_extraction: "gpt-3.5-turbo summarization (~6.86 key points/essay)"
  method_family: "Controlled human-AI co-writing experiment with diversity measurement"

positioning:
  core_claim: "RLHF-tuned models (InstructGPT) significantly reduce content diversity in human-AI co-writing compared to base models (GPT3), and this reduction is entirely attributable to model-contributed text, not changes in user behavior."
  key_results: "InstructGPT homogenization: 0.1660 Rouge-L (+8.1% vs Solo 0.1536, p<0.05); GPT3: 0.1578 (not significant); 5-gram diversity: InstructGPT 0.977 vs Solo 0.991; key point diversity: InstructGPT 0.738 vs Solo 0.792 (p<0.05); model suggestion self-similarity: InstructGPT 0.20 vs GPT3 0.11 (p<0.05)"
  limitations:
    - "Single-turn suggestion interface may not reflect all real-world co-writing contexts"
    - "Upwork writers not representative of all demographics"
    - "Only OpenAI models tested; results may not generalize to other model families"
    - "Single-session study; repeated interactions over time could change dynamics"
  relation_to_us: "foundation"  # Directly establishes that RLHF models produce less diverse text — this is the mechanism behind detectable AI fingerprints in generation depth

narrative:
  story_type: "突破局限型"  # Breaks through assumption that AI writing assistance is neutral; reveals hidden homogenization cost
  hook: "LLMs are transforming content creation, but millions of users relying on the same model risks 'algorithmic monoculture' — shifting content toward the mode"
  tension: "Prior work shows LLMs influence opinions and lack demographic representation, but no one has measured whether co-writing actually reduces the diversity of produced content"
  key_insight: "Section 5 (attribution analysis): the diversity loss is 100% attributable to model-contributed text — user writing behavior is unchanged across all conditions, but InstructGPT suggestions are inherently more homogeneous than GPT3 suggestions"
  argument_chain: "Monoculture risk → controlled experiment design → verify equal engagement → measure homogenization → measure diversity loss → attribute to model text → diagnose RLHF as cause"
  contribution_framing: "Implicit 3-fold: (1) controlled experiment measuring diversity impact, (2) diversity metrics at lexical and semantic levels, (3) attribution analysis pinpointing model text as cause. Contributions stated as findings rather than an explicit numbered list"
  intro_structure: "2 main paragraphs: P1 motivates the monoculture problem with prior evidence; P2 describes the experimental approach and previews findings. Notably compact intro."
  notable_technique: "The GPT3 vs InstructGPT comparison is the key rhetorical device — by showing GPT3 does NOT reduce diversity while InstructGPT DOES, the paper isolates RLHF/instruction-tuning as the causal factor, rather than AI assistance in general. This is more persuasive than just measuring one model."

figures:
  figure_count: 13  # including appendix figures
  figure1:
    type: "motivation"
    description: "Boxplots showing corpus homogenization at key point level across three conditions (Solo, GPT3, InstructGPT) and 10 topics. InstructGPT displays highest median on 7/10 topics."
    narrative_role: "Immediately demonstrates the main finding visually — InstructGPT consistently elevates homogenization across topics"
    design_elements: ["horizontal boxplots", "per-topic breakdown", "outlier markers", "three-condition color coding"]
    visual_style: "Grid of boxplots organized by topic; three colors for three conditions; clean axis labels; emphasis on InstructGPT being consistently highest"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "boxplot"
      what_compared: "Homogenization scores (Rouge-L) across Solo, InstructGPT, GPT3 at key point level"
      how_gain_highlighted: "Visual separation of InstructGPT median from Solo/GPT3; boxplot spread shows consistency"
      design_note: "Aggregated view complementing per-topic Figure 1; boxplot chosen to show distribution, not just means"
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Frequency distributions of (a) top-50 unigrams and (b) top-50 5-grams across three conditions"
      how_gain_highlighted: "InstructGPT shows steeper curve on 5-grams (more concentrated), while unigrams overlap — reveals that diversity loss is in phrases, not individual words"
      design_note: "Two-panel figure; frequency rank on x-axis, probability on y-axis; overlapping lines make convergence/divergence immediately visible"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Attribution analysis: (a) homogenization by authorship (user vs model), (b) 5-gram distributions separated by author"
      how_gain_highlighted: "Dashed lines (user text) overlap perfectly across conditions; solid lines (model text) diverge — visually proves model is the cause"
      design_note: "The dashed-vs-solid encoding is the key design choice; makes the causal attribution visually immediate without statistical explanation"
  ablation_figures:
    - figure_id: "Appendix figures"
      viz_type: "boxplot and line_plot variants"
      dimensions_varied: ["clustering threshold", "per-topic breakdown", "BertScore vs Rouge-L"]
      design_note: "Appendix replicates main analyses with alternative metrics/thresholds for robustness"
  figure_narrative_role: "Figure 1 (main result: homogenization by topic) → Figure 2 (aggregated homogenization) → Figure 3 (lexical diversity mechanism) → Figure 4 (causal attribution) — progressive deepening from 'what happens' to 'where it happens' to 'why it happens'"

tables:
  table_count: 13  # including appendix tables
  main_result_table:
    table_id: "Table 3"
    row_axis: "metrics"  # n-gram sizes (unigram through 5-gram) in 3a; clustering thresholds in 3b
    col_axis: "conditions (Solo, GPT3, InstructGPT)"
    row_organization: "by_category"  # split into (a) lexical diversity and (b) key point diversity sub-tables
    col_organization: "flat"  # three conditions side by side
    highlight_strategy: "bold values indicate p<0.05 statistical significance"
    statistical_reporting: "permutation tests (1000 iterations); chi-square tests for distribution comparisons; independent t-tests for usage stats"
    num_baselines: 2  # Solo and GPT3 serve as baselines for InstructGPT
    design_note: "Split into 3a (n-gram diversity) and 3b (key point diversity) sub-tables; compact format showing both metrics in one numbered table; bold = significant rather than bold = best"
  ablation_tables:
    - table_id: "Table 1"
      what_varied: ["condition (Solo, GPT3, InstructGPT)"]
      variation_style: "full_numbers"
      design_note: "Usage statistics table verifying equal engagement across conditions (queries, acceptance rate, model-written %, word count); serves as manipulation check rather than result"
    - table_id: "Table 4"
      what_varied: ["condition (Solo vs InstructGPT)"]
      variation_style: "full_numbers"
      design_note: "Top-10 most frequent 5-grams comparison; qualitative evidence showing InstructGPT repeats topic-specific phrases much more (14x vs 6x); bridges quantitative metrics to intuitive understanding"
  supplementary_tables:
    in_appendix: true
    content: "Extended homogenization results with BertScore, per-topic diversity breakdowns, compression-based diversity analysis, additional usage statistics, model self-diversity measurements"
    reason: "Main text focuses on Rouge-L and key point metrics; appendix provides robustness checks with alternative metrics (BertScore, compression ratio) and finer-grained per-topic analysis"
```

---

## 23. strong_model_collapse.yaml

```yaml
paper_key: "strong_model_collapse"
title: "Strong Model Collapse"
venue: "ICLR 2025"
full_text_available: true

research:
  baselines:
    - "Training on real data only (p₂=0)"
    - "Theoretical predictions from Theorems 1-2"
    - "Weighted single-step mixing (Jain et al. 2024)"
    - "Dynamic multi-step mixing (Ferbach et al. 2024)"
  metrics:
    - {name: "Test Error (MSE)", direction: "lower_better"}
    - {name: "Collapse term ζ", direction: "lower_better", note: "additional error from synthetic data"}
  datasets:
    - {name: "Synthetic Gaussian data", size: "d=600, n=500", domain: "toy/theoretical validation"}
    - {name: "MNIST", size: "standard", domain: "image classification with two-layer networks"}
    - {name: "BabiStories (TinyStories reproduction)", size: "generated via Mixtral-8x7B", domain: "language modeling with GPT-2"}
  ablation_dimensions:
    - synthetic_data_fraction (p₂ from 0 to 1)
    - synthetic_data_quality (c² ∈ {0, 0.1, 0.5, 1})
    - model_size (width m, varying m/n ratio)
    - interpolation_threshold (underparametrized vs overparametrized)
    - regularization_strength (ridge parameter λ)
    - mitigation_strategy (weighted mixing vs multi-step distillation)
  training_recipe:
    optimizer: "Ridge regression (closed-form); GPT-2 standard training for LM experiments"
    lr: "N/A for ridge; standard for GPT-2"
    hardware: "Not specified"
    statistical_runs: "5 runs with error bars for random projections experiments"
  method_family: "theoretical analysis of model collapse (bias-variance decomposition with collapse term)"

positioning:
  core_claim: "Even the smallest fraction of synthetic data (as little as 1%) causes irreversible model collapse—an additional error term ζ proportional to p₂² that persists regardless of dataset size, model scaling, or mixing strategy, unless synthetic data is completely removed."
  key_results: "Test error decomposes as B + V + ζ where ζ = Ω(p₂²c²) is the collapse term; larger models amplify collapse below interpolation threshold but may recover beyond it; weighted mixing and multi-step distillation cannot prevent collapse."
  limitations:
    - "Analysis restricted to linear models and random projections approximation (neural tangent kernel proxy)"
    - "Gaussian data assumption for theoretical results"
    - "Does not cover sophisticated mitigation strategies like data curation/filtering"
    - "Language modeling experiments on small scale (TinyStories/GPT-2) rather than full LLM systems"
    - "Label shift model (δ = w*₂ - w*₁) may not capture all forms of distribution mismatch in practice"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "'Model Collapse refers to a critical degradation in the performance of AI models, particularly when a significant portion of their training data consists of synthetic data'—immediately framing a crisis relevant to all modern LLM training pipelines."
  tension: "Prior work showed collapse in iterative retraining loops, but practitioners assumed mixing real and synthetic data would be safe. The paper challenges this assumption: even 1% synthetic data breaks scaling laws."
  key_insight: "Formalized in Theorem 1 and Corollary 1 (Section 2-3)—the collapse term ζ = Ω(p₂²c²) is structurally irreducible. It emerges from a rigorous bias-variance decomposition where ζ is a third, previously unrecognized component. The insight is that collapse is not a finite-sample artifact but a fundamental property of mixed-distribution learning."
  argument_chain: "Model collapse is a real crisis → prior work studied iterative loops but not realistic mixing → two key questions (is collapse inevitable with mixing? do larger models suffer more?) → formal bias-variance-collapse decomposition → Theorem 1 (linear model) + Theorem 2 (random projections) → even 1% synthetic data creates persistent ζ → larger models amplify collapse below interpolation threshold → weighted/multi-step mixing cannot prevent collapse → validated on MNIST and GPT-2/BabiStories"
  contribution_framing: "Three contributions under Section 1.1 'Main Contributions': Result #1 (strong collapse persists with mixed data), Result #2 (model size amplifies collapse), Experimental Validation. Uses formal 'Result' numbering emphasizing theoretical novelty."
  intro_structure: "5 paragraphs: P1=definition+framing (model collapse as crisis), P2=problem context (empirical observations, scaling laws), P3=motivation (why this matters for ChatGPT/Llama-scale systems), P4=research questions (Q1: inevitable? Q2: model size effect?), P5=main contributions (three numbered results)"
  notable_technique: "Posing two sharp research questions (Q1, Q2) in the intro that structure the entire paper. Each theorem directly answers one question, making the paper's logic feel inevitable. Also the naming choice 'Strong Model Collapse' (vs implicit 'weak') creates a memorable taxonomy."

figures:
  figure_count: 5
  figure1:
    type: "teaser_result"
    description: "Pareto diagram showing test error with mixed real+synthetic data vs real-only data. Points colored by synthetic data quality (squares=very high, diamonds=high, triangles=low, stars=very low). Colorbar shows m/n ratio (model size relative to data)."
    narrative_role: "Immediately conveys the main result visually—no amount of mixing avoids the collapse penalty. Points above the diagonal = worse than real-only training."
    design_elements: ["Pareto frontier", "shape encoding for quality levels", "colorbar for model size ratio", "diagonal reference line (real-only baseline)"]
    visual_style: "Scatter plot with multiple shape markers encoding categorical variable (data quality) and continuous colorbar encoding model size ratio. Clean 2D layout showing trade-off between real-only and mixed performance."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Theoretical predictions (dashed) vs empirical results (solid) for test error vs sample count across multiple synthetic data quality levels c²"
      how_gain_highlighted: "Perfect theory-experiment alignment validates the theoretical framework; multiple c² curves show collapse severity scales with quality"
      design_note: "Theory-experiment overlay (solid vs dashed) is the key design choice—demonstrates theoretical rigor. Multiple curves for c² ∈ {0, 0.1, 0.5, 1} show parametric dependence."
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Test error vs model size (m) for varying synthetic fractions p₂ across four data quality levels"
      how_gain_highlighted: "Darker lines (higher p₂) show worse performance; visible divergence from p₂=0 baseline; double-descent visible at m≈n"
      design_note: "Four subplots for quality levels; color gradient for p₂; error bars over 5 runs; vertical line at interpolation threshold m=n."
  ablation_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      dimensions_varied: ["model size m", "decomposition components (B, V, ζ)"]
      design_note: "Illustrates the B+V+ζ decomposition across model sizes. Shows classical double-descent in bias curve; vertical line at m=n interpolation threshold; ζ term (collapse) shown in distinct color (red). Pedagogical figure explaining the theoretical framework."
  figure_narrative_role: "Figure 1 (teaser: collapse shown via Pareto diagram) → Figure 2 (framework: B+V+ζ decomposition illustrated) → Figure 3 (validation: theory matches experiment for linear model) → Figure 4 (extension: model size effects with double-descent) → Figure 5 (extension: additional model size analysis). Flow: claim → framework → validate → extend."

tables:
  table_count: 0
  main_result_table:
    table_id: "N/A"
    row_axis: "N/A"
    col_axis: "N/A"
    row_organization: "N/A"
    col_organization: "N/A"
    highlight_strategy: "N/A"
    statistical_reporting: "N/A"
    num_baselines: 0
    design_note: "Notably, this theory-heavy paper uses NO tables in the main text. All results are communicated through figures (theory-experiment overlay plots) and theorem statements. This is typical for theoretical ML papers where the primary 'results' are theorems rather than benchmark numbers."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Appendix contains experimental details (A.1-A.3) for toy, MNIST, and GPT-2 settings, but results are presented as figures rather than tables."
    reason: "Theory paper convention: theorems are the main results; figures validate theory vs experiment; tables would not add value since comparisons are between theoretical predictions and empirical measurements rather than between competing methods."
```

---

## 24. broken_telephone.yaml

```yaml
paper_key: "broken_telephone"
title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
venue: "ACL 2025"
full_text_available: true

research:
  baselines:
    - "Iteration 0 (original human-written text)"
    - "Single-model chains vs. multi-model chains"
    - "Bilingual vs. multilingual chains"
  metrics:
    - {name: "BLEU", direction: "higher_better"}
    - {name: "ROUGE-1", direction: "higher_better"}
    - {name: "chrF", direction: "higher_better"}
    - {name: "METEOR", direction: "higher_better"}
    - {name: "BERTScore", direction: "higher_better"}
    - {name: "FActScore", direction: "higher_better"}
  datasets:
    - {name: "BookSum", size: "150 documents, 100-200 words each", domain: "book summaries"}
    - {name: "ScriptBase-alpha", size: "150 documents, 100-200 words each", domain: "movie scripts"}
    - {name: "News2024", size: "150 documents, 100-200 words each", domain: "news articles (2024 only)"}
  ablation_dimensions:
    - "Bridge language choice (FR, DE, NL, VN, ZH, TH — Latin vs. non-Latin scripts)"
    - "Chain complexity (bilingual vs. multilingual, 2 vs. 5 languages)"
    - "Number of models (1 vs. 2 vs. 3)"
    - "Temperature (1e-6, 0.25, 0.5, 0.75, 1.0)"
    - "Prompt constraint level (simple, base, constrained)"
    - "Task type (translation vs. rephrasing)"
  training_recipe:
    models:
      - "Llama-3.1-8B-Instruct (temp=0.6, top_p=0.9)"
      - "Mistral-7B-Instruct-v0.2 (temp=0.0)"
      - "Gemma-2-9B-it (temp=1.0, top_p=0.95)"
    max_tokens: 8000
    hardware: "54 GPU-days (36 on A100, 18 on A10)"
    factuality_judge: "Claude 3.5 Sonnet (for FActScore)"
    no_training: "Inference-only; no model finetuning involved"
  method_family: "Iterative inference-time generation (translation chains) measuring information distortion"

positioning:
  core_claim: "Information distortion accumulates inevitably through iterative LLM generation, influenced by language proximity and chain complexity, but is partially mitigable through temperature control and constrained prompting—establishing that LLMs act as lossy information channels."
  key_results: >
    EN<->TH (Llama) FActScore gradient: -0.018/iter (News2024), -0.026/iter (BookSum);
    EN<->FR (Llama) FActScore gradient: -0.004/iter (much less distortion for Latin-script pairs);
    Multilingual 5-language chain: steepest gradient -0.038/iter;
    By iteration 100, all chains converge to similar low FActScore (~0.04) regardless of setup;
    Temperature 1e-6 stabilizes after 2 iterations; temperature 1.0 causes steepest decline;
    Qualitative: "A lorry driver has been fined" → "A small car received a compensation" by iteration 100.
  limitations:
    - "Datasets share similar characteristics; specialized/long-tail domains unexplored"
    - "Limited to 7-9B parameter models; larger models may behave differently"
    - "Default generation settings only; greedy/beam search unexplored"
    - "Translation as proxy task; other iterative generation scenarios (summarization, paraphrasing) less explored"
  relation_to_us: "complementary"

narrative:
  story_type: "跨界迁移型"
  hook: >
    Opens with the observation that LLMs increasingly generate online content, then
    raises a concern about iterative processing: what happens when LLMs repeatedly
    consume and reprocess their own outputs? The "broken telephone" (Chinese whispers)
    analogy is introduced immediately as a vivid, universally understood frame for
    information distortion through sequential transmission.
  tension: >
    Unlike prior work on model collapse (which requires retraining), this paper targets
    inference-time distortion—each step is just prompting, no weight updates.
    The tension is: even without training, iterative generation should be safe... right?
    Translation as testbed makes the distortion measurable because there's an objective
    ground truth to compare against.
  key_insight: >
    Revealed through the language pair comparison in Experiment 1: distortion is not
    uniform—it depends critically on the bridge language. Latin-script pairs (EN<->FR)
    show near-zero degradation, while non-Latin pairs (EN<->TH) degrade 4-5x faster.
    This connects to training data representation and suggests the distortion reflects
    model competence boundaries. The convergence phenomenon (all setups reach ~0.04
    FActScore by iteration 100) suggests a universal "information floor."
  argument_chain: >
    LLMs generate increasing web content → iterative processing is inevitable →
    broken telephone analogy suggests distortion → choose translation as measurable testbed →
    Exp1: bilingual self-loop reveals language-dependent distortion →
    Exp2: multi-model collaboration adds/reduces noise depending on language →
    Exp3: multilingual chains accelerate distortion →
    ablations: temperature and prompt constraints partially mitigate →
    conclusion: distortion inevitable, mitigation possible but incomplete
  contribution_framing: >
    Three findings presented as bullet points (not numbered contributions):
    (1) Distortion depends on intermediate language choice (linguistic similarity + training data prevalence)
    (2) Greater chain complexity amplifies distortion
    (3) Temperature control and constrained prompting mitigate but cannot prevent distortion.
    Notably framed as empirical findings rather than methodological contributions.
  intro_structure: >
    4 paragraphs:
    P1 (Hook): LLMs generate content, iterative processing raises concerns
    P2 (Analogy): Broken telephone game as conceptual frame
    P3 (Research question): Do LLMs exhibit similar distortion?
    P4 (Approach + contributions): Translation testbed, three key findings listed
  notable_technique: >
    The broken telephone analogy is the paper's most effective narrative device—it transforms
    a technical measurement study into an intuitive story. The qualitative example
    (Table 1: lorry driver -> bus -> small car with explosions and compensation)
    is placed before any metrics, making readers viscerally understand the problem
    before seeing numbers. The three-experiment escalation (single-model bilingual →
    multi-model bilingual → multilingual multiplayer) creates natural narrative momentum.

figures:
  figure_count: 6
  figure1:
    type: "method_overview"
    description: >
      Three-panel overview of the three experimental setups. Left: Bilingual Self-Loop
      (single model, EN<->FR/TH, 100 iterations). Middle: Bilingual Two-Player
      (two different models collaborating on same translation chain). Right: Multilingual
      Multiplayer (multiple languages and models in extended chains).
    narrative_role: >
      Establishes all three experiments at a glance, showing the escalation in complexity
      from left to right. Readers can reference back to this figure throughout the paper.
    design_elements:
      - "Three-panel layout showing experimental progression"
      - "Arrow-based translation flow diagrams"
      - "Model icons distinguishing Llama/Mistral/Gemma"
      - "Language labels (EN, FR, TH, ZH, DE) at each node"
    visual_style: >
      Horizontal three-panel layout. Each panel shows a circular or chain-like
      translation flow with arrows connecting language nodes. Different models
      distinguished by icons or colors. Clean, diagrammatic style typical of
      NLP experiment overviews.
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      what_compared: >
        Llama bilingual self-loop metrics (BLEU, ROUGE-1, chrF, METEOR, BERTScore, FActScore)
        across 100 iterations for 6 language pairs (FR, DE, NL, VN, ZH, TH) on News2024.
      how_gain_highlighted: >
        Language pairs naturally separate into two groups: Latin-script (FR/DE/NL) cluster
        high, non-Latin (VN/ZH/TH) cluster low, with TH showing steepest decline.
        The visual gap between clusters is the main finding.
      design_note: >
        Multi-subplot grid (one per metric). 6 lines per subplot distinguished by color.
        X-axis is iteration count (0-100), Y-axis is metric value. The consistent
        pattern across all 6 metrics reinforces the language-dependence finding.
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: >
        Bilingual two-player results comparing single-model vs. multi-model chains
        for EN<->FR and EN<->TH on News2024.
      how_gain_highlighted: >
        Shows that collaboration helps for Thai (reducing distortion) but hurts for
        French (increasing distortion)—a nuanced, non-obvious finding.
      design_note: >
        Paired comparison layout. Lines for single-model and multi-model chains
        shown together for direct comparison per language pair.
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: >
        Rephrasing experiments on 30 News2024 documents: individual models
        (Llama, Mistral, Gemma) vs. collaborative combinations over 100 iterations.
      how_gain_highlighted: >
        Collaborative setups show steeper decline than individual models,
        with Llama+Mistral+Gemma triple collaboration declining fastest.
      design_note: >
        Tests whether the translation finding generalizes to pure rephrasing.
        Multiple overlapping lines showing model and collaboration effects.
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      dimensions_varied:
        - "Temperature (1e-6, 0.25, 0.5, 0.75, 1.0)"
      design_note: >
        Temperature spectrum visualization for EN<->FR with Llama on 30 News2024 docs.
        Shows clear ordering: lower temperature = less degradation. Temperature 1e-6
        stabilizes after ~2 iterations (essentially deterministic). Clean parameter sweep.
    - figure_id: "Figure 6"
      viz_type: "line_plot"
      dimensions_varied:
        - "Prompt constraint level (simple, base, constrained)"
      design_note: >
        Shows more constrained prompts preserve higher relevance and factuality.
        Three lines with clear separation. On Llama, 30 News2024 docs, EN<->FR.
  figure_narrative_role: >
    Figure 1 (experimental overview) → Table 1 (qualitative distortion example) →
    Figure 2 (Exp1: language-dependent degradation curves) →
    Figure 3 (Exp2: multi-model collaboration effects) →
    Figure 4 (rephrasing as alternative task) →
    Figure 5 (temperature ablation) → Figure 6 (prompt constraint ablation).
    Narrative arc: setup → demonstrate problem → escalate complexity → explore mitigation.

tables:
  table_count: 9
  main_result_table:
    table_id: "Table 2"
    row_axis: "datasets x models"
    col_axis: "language pairs (DE, FR, NL, TH, VN, ZH) with avg gradient + std error"
    row_organization: "by_category"
    col_organization: "grouped_by_language_pair"
    highlight_strategy: "Gradient values with standard errors; no bold/underline visible"
    statistical_reporting: "Average gradient +/- standard error across 150 documents"
    num_baselines: 0
    design_note: >
      FActScore gradients as primary metric—negative gradient = distortion rate per iteration.
      Organized as 3 datasets x 2 models = 6 rows, 6 language pairs as columns.
      The gradient representation is elegant: a single number captures 100 iterations of decline.
      Standard errors included for reliability. Compact but information-dense.
  ablation_tables:
    - table_id: "Table 1"
      what_varied: ["Iteration number (0, 2, 10, 50, 100)"]
      variation_style: "full_numbers"
      design_note: >
        Qualitative text example showing progressive distortion of a news article
        about a lorry driver. Not a metrics table—shows actual text at 5 snapshots
        across 100 iterations. Distortions highlighted in the text. Placed before
        quantitative results for immediate reader engagement. Functions as a
        motivating example that makes the abstract metric decline concrete.
    - table_id: "Tables 4-7 (Appendix)"
      what_varied: ["BLEURT scores across all experiments"]
      variation_style: "full_numbers"
      design_note: "Supplementary metric tables supporting main FActScore findings"
  supplementary_tables:
    in_appendix: true
    content: >
      Table 3: Default decoding parameters for each model.
      Tables 4-7: BLEURT scores across all four experiments.
      Table 8: Temperature variation detailed analysis.
      Additional appendix tables for comprehensive metric reporting.
    reason: >
      Main text focuses on FActScore gradient as the cleanest summary statistic.
      BLEURT and detailed parameter tables deferred to appendix to keep main text
      focused. Only 2 tables in main text (qualitative example + FActScore gradients)
      keeps the paper visually clean despite 450 documents x 100 iterations of data.
```

---

## 25. binoculars.yaml

```yaml
paper_key: "binoculars"
title: "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"
venue: "ICML 2024"
full_text_available: true  # arXiv HTML v2 available

research:
  baselines:
    - Ghostbuster
    - GPTZero
    - DetectGPT
    - Fast-DetectGPT
    - DNA-GPT
  metrics:
    - {name: "TPR at 0.01% FPR", direction: "higher_better"}
    - {name: "TPR at 0.1% FPR", direction: "higher_better"}
    - {name: "F1-Score", direction: "higher_better"}
    - {name: "AUC", direction: "higher_better"}
  datasets:
    - {name: "Ghostbuster News", size: "from Ghostbuster benchmark"}
    - {name: "Ghostbuster Creative Writing", size: "from Ghostbuster benchmark"}
    - {name: "Ghostbuster Student Essays", size: "from Ghostbuster benchmark"}
    - {name: "CCNews + LLaMA-2/Falcon generations", size: "custom dataset"}
    - {name: "PubMed + LLaMA-2/Falcon generations", size: "custom dataset"}
    - {name: "CNN + LLaMA-2/Falcon generations", size: "custom dataset"}
    - {name: "Orca (GPT-3/GPT-4 completions)", size: "millions of samples"}
    - {name: "M4 multilingual (Arxiv, Reddit, WikiHow, Wikipedia)", size: "multilingual benchmark"}
  ablation_dimensions:
    - "scoring model pairs (observer M1 x performer M2 combinations)"
    - "component contribution (PPL alone vs X-PPL alone vs ratio)"
    - "sequence length impact on detection"
    - "performer model fine-tuning steps (0, 1, 10, 50, 100, 500, full on Alpaca)"
    - "identical vs different M1/M2 models"
    - "ESL (English as Second Language) fairness"
    - "modified system prompts (default, Carl Sagan, non-robotic, pirate)"
    - "multilingual performance (Bulgarian, Urdu, low-resource languages)"
    - "famous/memorized text behavior"
    - "random token sequence behavior"
  training_recipe:
    optimizer: "N/A for main method (zero-shot inference)"
    lr: "5e-5 (for performer model fine-tuning ablation only)"
    hardware: "4 A5000 GPUs"
    fine_tuning_details: "Alpaca dataset, cosine annealing, 3% warmup, batch 65K tokens (32 samples x 2048 block), FSDP distributed"
  method_family: "dual-model perplexity ratio (zero-shot, training-free)"

positioning:
  core_claim: "The ratio of perplexity to cross-perplexity from two closely related language models provides a simple, zero-shot detection score that achieves >90% TPR at 0.01% FPR on ChatGPT text, outperforming commercial detectors without any model-specific training."
  key_results: >
    News: 95% TPR @ 0.01% FPR.
    Creative Writing: 93% TPR @ 0.01% FPR.
    Student Essays: 98% TPR @ 0.01% FPR.
    ESL fairness: 99.67% accuracy on both original and grammar-corrected essays.
    Orca GPT-3: 92% accuracy. Orca GPT-4: 89.57%.
    Stylistic robustness: pirate voice prompting reduces sensitivity by only 1%.
  limitations:
    - "Only works on 'naturally occurring' text without adversarial evasion attempts"
    - "High false negative rate on GPT-4 (58% in March 2024 testing)"
    - "Low recall (but high precision) on low-resource languages (Bulgarian, Urdu)"
    - "Memorized famous texts sometimes classified as machine-generated (e.g., US Constitution scored 0.76)"
    - "Black-box nature: provides no explanation for predictions"
    - "Requires two forward passes through LLMs for each sample (computational cost)"
  relation_to_us: "competitor"  # directly competing zero-shot detection method; uses perplexity-based signal which is related to our depth analysis

narrative:
  story_type: "化繁为简型"
  hook: >
    Opens with a bold contradiction of conventional wisdom: "Detecting text generated by modern large
    language models is thought to be hard" — then immediately reverses with "However, we find that a
    score based on contrasting two closely related language models is highly accurate." The surprise
    inversion grabs attention by promising a surprisingly simple solution to a supposedly hard problem.
  tension: >
    Multi-layered tension construction:
    (1) Model-specificity: "existing detectors rely on model-specific training data and often fail to transfer"
    (2) Wrong evaluation metrics: "many works focus on accuracy on balanced test sets and/or AUC...not well-suited for high-stakes detection" — reframes what success even means
    (3) Fairness concern: cites Liang et al. showing ESL essays wrongly flagged 48-76% by commercial detectors
    (4) The "capybara problem" (Section 3.2): entire dedicated section showing why naive perplexity fails — prompt context is unknown to detector, so high-perplexity text about "astrophysicist capybaras" is actually machine-generated
    Tension operates at both methodological and ethical levels.
  key_insight: >
    The capybara problem motivates the key insight: perplexity alone fails because prompt context is
    unknown, but the RATIO of perplexity to cross-perplexity normalizes for this. Cross-perplexity
    measures "how surprising one model's predictions are to another" — for machine text, both models
    predict similarly (low cross-perplexity), making the ratio distinctive. The insight is revealed
    through the capybara example (Table 1) where DetectGPT and GPTZero both fail but Binoculars succeeds.
  argument_chain: >
    detection is thought to be hard → existing methods are model-specific and use wrong metrics →
    ESL fairness is violated → naive perplexity fails due to unknown prompts (capybara problem) →
    insight: normalize perplexity by cross-perplexity to cancel prompt effects →
    Binoculars score B = log PPL / log X-PPL → SOTA at extremely low FPR (0.01%) →
    robust across models, languages, ESL text, and prompting styles
  contribution_framing: >
    Contributions stated implicitly rather than numbered bullets — woven into the prose.
    Core claims: (1) zero-shot SOTA without training data, (2) outperforms commercial systems,
    (3) transfers across LLM families. The implicit framing creates a sense of unified simplicity
    rather than a checklist of separate contributions.
  intro_structure: >
    2 main paragraphs (notably concise for a top venue):
    P1 — narrative hook: conventional wisdom is wrong, simple approach works
    (presents problem + surprising finding in same paragraph)
    P2 — method naming, key advantage (zero-shot), headline numbers (>90% TPR @ 0.01% FPR),
    breadth of applicability (multiple LLM families)
    The extreme brevity of intro is itself a stylistic choice matching the "simplicity" thesis.
  notable_technique: >
    The "capybara problem" — inventing a memorable, vivid name for a failure mode of prior methods.
    Section 3.2 + Table 1 create a concrete, almost humorous example (astrophysicist capybaras)
    that makes an abstract statistical concept (prompt-conditional perplexity) intuitively graspable.
    This named-problem technique makes the paper's contribution memorable and citeable.

figures:
  figure_count: 15  # main paper + appendix
  figure1:
    type: "teaser_result"
    description: >
      Multi-dataset detection performance comparison showing ROC-style curves across three Ghostbuster
      datasets (News, Creative Writing, Student Essays). Binoculars shown against baselines
      (GPTZero, open-source detectors) with dramatic separation at low FPR.
    narrative_role: "Leads with the headline result — reader sees the performance gap before understanding the method. Creates motivation to keep reading for the 'how'."
    design_elements:
      - "three side-by-side panels for three domains"
      - "log-scale FPR axis to emphasize low-FPR regime"
      - "multiple baseline curves for comparison"
      - "Binoculars curve clearly dominant"
    visual_style: "Multi-panel ROC comparison, log-scale x-axis emphasizing the practically important low-FPR region. Clean lines, standard academic color palette."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "roc_curves"
      what_compared: "Detection methods on LLaMA-2-13B generations (log-scale FPR)"
      how_gain_highlighted: "Binoculars curve dominates at all FPR thresholds, especially at the extreme left (low FPR)"
      design_note: "Log-scale FPR axis is a deliberate methodological statement — the paper argues standard AUC hides poor low-FPR performance."
    - figure_id: "Figure 4"
      viz_type: "precision_recall_curves"
      what_compared: "ChatGPT detection across M4 domains (Arxiv, Reddit, WikiHow, Wikipedia)"
      how_gain_highlighted: "Binoculars maintains high precision across recall levels where baselines drop"
      design_note: "Multi-domain panels demonstrate generalization breadth."
    - figure_id: "Figure 5"
      viz_type: "bar_chart"
      what_compared: "Binoculars performance across various generative models"
      how_gain_highlighted: "Consistent high bars across model families"
      design_note: "Shows transfer capability — one detector, many source models."
    - figure_id: "Figure 9"
      viz_type: "bar_chart"
      what_compared: "F1-Score comparison across datasets"
      how_gain_highlighted: "Binoculars bars consistently tallest"
      design_note: "Supplementary metric for readers who prefer F1 over TPR@FPR."
  ablation_figures:
    - figure_id: "Figure 2"
      viz_type: "bar_chart"
      dimensions_varied: ["document size (number of tokens)"]
      design_note: "Shows detection maintains capability with few tokens — addresses practical concern about short texts."
    - figure_id: "Figure 7"
      viz_type: "distribution_plot"
      dimensions_varied: ["ESL original vs grammar-corrected essays"]
      design_note: "Score distributions overlap substantially for original and corrected ESL essays — directly addresses fairness concern from intro."
    - figure_id: "Figure 8"
      viz_type: "bar_chart"
      dimensions_varied: ["system prompt styles (default, Carl Sagan, non-robotic, pirate)"]
      design_note: "Robustness to stylistic prompting variation — only 1% sensitivity drop for pirate voice."
    - figure_id: "Figure 10"
      viz_type: "scatter_plot"
      dimensions_varied: ["sequence length vs Binoculars score"]
      design_note: "Demonstrates no strong correlation with length — score is length-agnostic."
    - figure_id: "Figure 11"
      viz_type: "distribution_plots"
      dimensions_varied: ["PPL alone vs X-PPL alone vs combined"]
      design_note: "Shows both components alone have poor separation; the ratio is key. Justifies the method design."
    - figure_id: "Figure 13"
      viz_type: "roc_curves"
      dimensions_varied: ["identical vs different M1/M2 models"]
      design_note: "Validates that using different (base vs instruct) models outperforms identical models."
    - figure_id: "Figure 14"
      viz_type: "histogram"
      dimensions_varied: ["random token sequences"]
      design_note: "Random tokens classified as human (mean ~1.35 vs ~1.0 for real human text) — edge case validation."
    - figure_id: "Figure 15"
      viz_type: "line_chart"
      dimensions_varied: ["performer model fine-tuning steps on Alpaca"]
      design_note: "Monotonic improvement with instruction tuning — explains why base+instruct pair works best."
  figure_narrative_role: >
    Figure 1 (teaser result — headline performance) → Section 3 method with capybara Table 1 →
    Figure 2 (document size robustness) → Figure 3 (detailed ROC comparison) →
    Figures 4-5 (cross-domain, cross-model generalization) → Figure 6 (multilingual) →
    Figure 7 (ESL fairness) → Figure 8 (prompt robustness) → Appendix figures (component analysis,
    random tokens, fine-tuning ablation).
    Flow: impress with results first → explain method → demonstrate breadth → address concerns → deep ablation.
    This "results-first" ordering is unusual and mirrors the intro's strategy of leading with the surprise.

tables:
  table_count: 8  # primary tables + supplementary
  main_result_table:
    table_id: "Table 4"
    row_axis: "methods"
    col_axis: "datasets x metrics (AUC, TPR at 0.01%, 0.1%, 1%, 5% FPR)"
    row_organization: "by_category"  # individual components (Falcon PPL, Falcon X-PPL, LLaMA variants) then Binoculars variants
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "point estimates; confidence via separate Table 7 (standard errors for AUC and TPR)"
    num_baselines: 5  # Ghostbuster, GPTZero, DetectGPT, Fast-DetectGPT, DNA-GPT
    design_note: >
      Unusual: the main result table is Table 4 (not Table 1) because earlier tables serve
      methodological exposition. Table 1 is the capybara example, Table 2 is system prompt
      examples, Table 3 is model pair ablation. This ordering prioritizes method understanding
      over result reporting — the reader should understand WHY before seeing HOW WELL.
  ablation_tables:
    - table_id: "Table 1"
      what_varied: ["the capybara problem illustration — single example with scoring"]
      variation_style: "full_numbers"
      design_note: >
        Not a traditional ablation but a motivating example table. Shows one GPT-4 sample about
        'astrophysicist capybaras' with Falcon PPL (2.20), Binoculars score (0.73), DetectGPT (0.14),
        GPTZero (49.71%). Demonstrates failure of baselines on a concrete case. Placed in method
        section, not results — serves argumentative rather than evaluative purpose.
    - table_id: "Table 3"
      what_varied: ["scoring model pairs (observer M1 x performer M2)"]
      variation_style: "full_numbers"
      design_note: >
        Rows are different model pair combinations (Falcon-7B-Instruct, Llama-2-13B, etc.).
        Columns: PPL Scorer (M1), Cross-PPL Scorers (M1', M2), TPR @ 0.01% FPR, TPR @ 0.1% FPR,
        F1-Score, AUC. Best pair achieves 100% TPR at 0.01% FPR. Guides practitioner model selection.
    - table_id: "Table 5"
      what_varied: ["famous/memorized texts (US Constitution, 'I Have a Dream', songs, literary excerpts)"]
      variation_style: "full_numbers"
      design_note: >
        Rows: well-known texts. Columns: Human Sample, PPL, Cross PPL, Binoculars Score,
        Predicted as Human (checkmark/X). Reveals memorization failure mode — US Constitution
        misclassified. Honest about limitations rather than hiding them.
    - table_id: "Table 8"
      what_varied: ["newer model performance (GPT-4, Gemini)"]
      variation_style: "full_numbers"
      design_note: >
        Tests on models released after the method was developed.
        GPT-4: 58.13% false negative rate (major limitation).
        Gemini: 3.10% false negative rate (works well).
        Presented transparently as the method's biggest weakness.
  supplementary_tables:
    in_appendix: true
    content: >
      Table 2 (modified system prompt examples), Table 6 (multilingual details),
      Table 7 (confidence estimates with standard errors for AUC and TPR),
      additional ablation results for model fine-tuning and component analysis.
    reason: >
      Main paper front-loads the capybara motivation table and model pair ablation BEFORE
      the main results — unusual ordering that prioritizes understanding over performance showcase.
      Supplementary tables handle confidence intervals and edge cases to keep main narrative focused.
```

---

End of file contents. All 25 YAML files have been read in full with complete contents above.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c17098d-02ee-408e-ab5c-17a91c9d9188",
  "isSidechain": true,
  "agentId": "aa334bf6bcdbf7cc3",
  "requestId": "req_011CbHvoy2iheXxZNxnbHhD6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "97b4c47b-1e71-413b-8154-5b39a4da029e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/distiller_112a2d1e",
  "sessionId": "2630a67f-9f60-4e1c-908d-7c5103de8572",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SxNYyysf6MqCeVDeW8p4v9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 37637,
      "cache_read_input_tokens": 39109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37637,
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
