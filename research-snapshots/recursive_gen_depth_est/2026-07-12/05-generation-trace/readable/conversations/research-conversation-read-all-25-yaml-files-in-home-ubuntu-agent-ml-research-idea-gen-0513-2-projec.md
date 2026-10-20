# Research conversation: Read all 25 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/ 

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af75b63db3ca0cde3.jsonl`
- **Structured JSON:** [`53866d5dedd4dd1a99ca.json`](../../sessions/53/53866d5dedd4dd1a99ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-21T14:54:32.380Z_

Read all 25 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/ and return their complete contents concatenated together. The files are:

dohmatob2024_demystified.yaml
alemohammad2024_mad.yaml
drayson2025_detection_prevents_collapse.yaml
bevendorff2025_two_paradigms.yaml
synthetic_eggs2026.yaml
li2024_mage.yaml
mohamed2025_broken_telephone.yaml
dohmatob2024_tale_of_tails.yaml
finlayson2024_closing.yaml
yi2026_escaping_collapse.yaml
binoculars2024.yaml
fast_detectgpt2024.yaml
diveye2026.yaml
verma2024_ghostbuster.yaml
penedo2024_fineweb.yaml
loki2025.yaml
tulchinskii2024_intrinsic_dim.yaml
editlens2026.yaml
cloc2025.yaml
qurating2024.yaml
mitchell2023_detectgpt.yaml
shi2025_closer_look.yaml
wu2025_detection_survey.yaml
kirchenbauer2023_watermark.yaml
dohmatob2025_strong_collapse.yaml

Read every single file completely and return all content. This is a read-only research task, do NOT write any files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "ab57d42c-7869-4ebb-9c45-3365df1548a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T14:54:32.385Z_

```json
{
  "parentUuid": "ab57d42c-7869-4ebb-9c45-3365df1548a6",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "14064f2c-ab08-464e-952d-80a24c43a55d",
  "timestamp": "2026-05-21T14:54:32.385Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T14:54:34.929Z_



I'll read all 25 YAML files from the distill_tmp directory. Let me fetch them all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14064f2c-ab08-464e-952d-80a24c43a55d",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3053287d-4eb7-4304-b836-9313f5117176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 4 · 2026-05-21T14:54:36.018Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W4mFh5bqoZiD6x1cGouUnq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2024_demystified.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3053287d-4eb7-4304-b836-9313f5117176",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e718a991-ea2d-44fc-83ae-5b8580ce26b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 5 · 2026-05-21T14:54:36.031Z_

<details><summary>↩ Tool result · `toolu_01W4mFh5bqoZiD6x1cGouUnq`</summary>

```text
1	paper_key: "dohmatob2024_demystified"
2	title: "Model Collapse Demystified: The Case of Regression"
3	venue: "NeurIPS 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["no-collapse baseline (real data only)", "adaptive regularization"]
8	  metrics:
9	    - {name: "test risk / prediction error", direction: "lower_better"}
10	    - {name: "scaling law exponent", direction: "context_dependent"}
11	  datasets:
12	    - {name: "synthetic high-dimensional regression", size: "theoretical"}
13	  ablation_dimensions: ["number of recursive generations", "spectral decay rate", "source condition", "regularization strength"]
14	  training_recipe: {optimizer: "closed-form / ridge regression", lr: "N/A", hardware: "theoretical"}
15	  method_family: "theoretical analysis of model collapse in regression"
16	
17	positioning:
18	  core_claim: "Analytic formulae characterizing model collapse in high-dimensional regression reveal modified scaling laws with crossover phenomena from fast to slow rates"
19	  key_results: "Derived closed-form expressions for collapse dynamics; proposed adaptive regularization as mitigation"
20	  limitations: ["limited to regression setting", "Gaussian assumptions"]
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
  "parentUuid": "e718a991-ea2d-44fc-83ae-5b8580ce26b3",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "5b89b091-f669-4d2d-b04b-d315cc6d076b",
  "sourceToolAssistantUUID": "e718a991-ea2d-44fc-83ae-5b8580ce26b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T14:54:36.413Z_

<details open><summary>🔧 Tool call — Read · `toolu_015TPgbEfGKwEpsf7tgtkeMF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/alemohammad2024_mad.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b89b091-f669-4d2d-b04b-d315cc6d076b",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b30008f4-51a4-44b6-9eb7-2d3a4391fde8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 7 · 2026-05-21T14:54:36.419Z_

<details><summary>↩ Tool result · `toolu_015TPgbEfGKwEpsf7tgtkeMF`</summary>

```text
1	paper_key: "alemohammad2024_mad"
2	title: "Self-Consuming Generative Models Go MAD"
3	venue: "ICLR 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["real data baseline", "mixed real+synthetic training"]
8	  metrics:
9	    - {name: "precision (quality)", direction: "higher_better"}
10	    - {name: "recall (diversity)", direction: "higher_better"}
11	    - {name: "FID", direction: "lower_better"}
12	  datasets:
13	    - {name: "FFHQ (image generation)", size: "70K"}
14	    - {name: "MNIST", size: "60K"}
15	  ablation_dimensions: ["fresh real data ratio", "number of autophagous generations", "quality-diversity tradeoff"]
16	  training_recipe: {optimizer: "N/A (generative models)", lr: "N/A", hardware: "N/A"}
17	  method_family: "theoretical + empirical analysis of autophagous (self-consuming) generative loops"
18	
19	positioning:
20	  core_claim: "Without sufficient fresh real data in each generation, self-consuming generative models are doomed to have quality or diversity progressively decrease (Model Autophagy Disorder)"
21	  key_results: "Three regimes identified: fully synthetic → collapse; synthetic+sampling bias → quality loss; synthetic+fresh data → stable if ratio sufficient"
22	  limitations: ["primarily image domain", "simplified generation pipeline"]
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
  "parentUuid": "b30008f4-51a4-44b6-9eb7-2d3a4391fde8",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "4aec09c3-2e7a-4312-9bae-6dbfe17f88fc",
  "sourceToolAssistantUUID": "b30008f4-51a4-44b6-9eb7-2d3a4391fde8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T14:54:36.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BeqG6H7WRRaNg84qyj7Trj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/drayson2025_detection_prevents_collapse.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aec09c3-2e7a-4312-9bae-6dbfe17f88fc",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91353ae6-aa22-4609-97ca-ddbe8b4d98d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 9 · 2026-05-21T14:54:36.893Z_

<details><summary>↩ Tool result · `toolu_01BeqG6H7WRRaNg84qyj7Trj`</summary>

```text
1	paper_key: "drayson2025_detection_prevents_collapse"
2	title: "Machine-generated text detection prevents language model collapse"
3	venue: "EMNLP 2025 Findings"
4	full_text_available: false
5	
6	research:
7	  baselines: ["training on purely human data", "training on unfiltered mixed data"]
8	  metrics:
9	    - {name: "perplexity", direction: "lower_better"}
10	    - {name: "text diversity", direction: "higher_better"}
11	    - {name: "downstream task performance", direction: "higher_better"}
12	  datasets:
13	    - {name: "GPT-2 generated text", size: "N/A"}
14	    - {name: "SmolLM2 generated text", size: "N/A"}
15	  ablation_dimensions: ["model family (GPT-2 vs SmolLM2)", "model size (124M to 1.7B)", "number of recursive generations", "detection threshold"]
16	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
17	  method_family: "detection-based filtering + importance resampling for collapse prevention"
18	
19	positioning:
20	  core_claim: "Using machine-generated text detectors to filter training data not only prevents model collapse but improves performance beyond training on purely human data"
21	  key_results: "Detection + resampling outperforms both pure human data and unfiltered mixed data across GPT-2 and SmolLM2 families"
22	  limitations: ["limited model families tested", "relies on detector quality"]
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
  "parentUuid": "91353ae6-aa22-4609-97ca-ddbe8b4d98d7",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "92ba562d-bc38-4f12-b8b3-cb602d3d7904",
  "sourceToolAssistantUUID": "91353ae6-aa22-4609-97ca-ddbe8b4d98d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T14:54:37.830Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UAry42pZ1LXrvrvA3K1Qns`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/bevendorff2025_two_paradigms.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92ba562d-bc38-4f12-b8b3-cb602d3d7904",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ae00ae4-6f63-4fcb-9e8f-178a2151d4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 11 · 2026-05-21T14:54:37.845Z_

<details><summary>↩ Tool result · `toolu_01UAry42pZ1LXrvrvA3K1Qns`</summary>

```text
1	paper_key: "bevendorff2025_two_paradigms"
2	title: "The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification"
3	venue: "ACL 2025 Findings"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Binoculars (Hans et al., 2024) zero-shot detector"
9	    - "SVM with TF-IDF word unigrams (800 features)"
10	    - "LoRA-fine-tuned Mistral-7B binary classifier"
11	    - "OpenAI RoBERTa-based GPT-2 detector (Solaiman et al., 2019)"
12	    - "Ghostbuster (Verma et al., 2024)"
13	    - "GPT-Sentinel (Chen et al., 2023)"
14	    - "DetectGPT (Mitchell et al., 2023)"
15	    - "Fast-DetectGPT (Bao et al., 2023)"
16	    - "DetectLLM (Su et al., 2023a)"
17	    - "LLMDet (Wu et al., 2023)"
18	  metrics:
19	    - {name: "False Negative Rate (FNR)", direction: "lower_better"}
20	    - {name: "False Positive Rate (FPR)", direction: "lower_better"}
21	    - {name: "AUROC", direction: "higher_better"}
22	    - {name: "Accuracy", direction: "higher_better"}
23	    - {name: "Precision-Recall curve", direction: "higher_better"}
24	    - {name: "c@1 (accuracy with non-answers)", direction: "higher_better"}
25	    - {name: "Cohen's d (effect size)", direction: "N/A"}
26	    - {name: "Character 3-gram entropy (bits)", direction: "N/A"}
27	    - {name: "MTLD (lexical diversity)", direction: "N/A"}
28	    - {name: "Flesch reading ease", direction: "N/A"}
29	    - {name: "Compression-based cosine (CBC)", direction: "lower_better"}
30	  datasets:
31	    - {name: "PAN'24 (extended with GPT-4o, 4o-mini, o1)", size: "1,359 human + 23,094 LLM texts, 15 LLMs"}
32	    - {name: "Human Detectors (HD)", size: "150 human + 150 LLM texts, 5 LLMs"}
33	    - {name: "Ghostbuster (GB) Essays", size: "994 human + 6,000 LLM texts, 6 LLMs"}
34	    - {name: "Ghostbuster (GB) Reuters", size: "1,000 human + 6,000 LLM texts, 6 LLMs"}
35	    - {name: "RAID", size: "153,217 human + 2,443,073 LLM texts, 6 LLMs"}
36	    - {name: "RAID (no attacks)", size: "12,766 human + 202,593 LLM texts, 6 LLMs"}
37	    - {name: "M4", size: "59,032 human + 57,253 LLM texts, 7 LLMs"}
38	    - {name: "MAGE", size: "152,382 human + 284,224 LLM texts, 131 model labels combined into 4 families"}
39	  ablation_dimensions:
40	    - "Model family used for training vs. testing (cross-model generalization)"
41	    - "In-domain vs. out-of-domain evaluation"
42	    - "Text length cutoffs (entropy analysis at increasing character lengths)"
43	    - "Feature set size in unmasking (top 250 vs. top 500 n-grams)"
44	    - "Operating point threshold (accuracy vs. low FPR vs. low FNR)"
45	    - "Genre-controlled vs. mixed-genre datasets"
46	    - "Dataset used for training (PAN vs. RAID)"
47	  training_recipe:
48	    optimizer: "Not specified for SVM; LoRA fine-tuning for Mistral-7B"
49	    lr: "Not specified"
50	    hardware: "3x A100 GPUs for 2x12h (Mistral-7B LoRA, 20M trainable parameters)"
51	  method_family: "Authorship analytics / computational stylometry applied to LLM detection"
52	
53	positioning:
54	  core_claim: "LLM detection is fundamentally an authorship verification (open-set one-class) problem, not an authorship attribution (closed-set binary classification) problem, and conflating the two paradigms explains the contradictory reports of detector success and failure."
55	  key_results: "SVM in-domain FNR 0-7%, FPR 0-3%; OpenAI o1 is undetectable by non-o1 detectors; Binoculars FPR near zero but fails completely on o1; GPT-4o is first model with entropy consistent with human text beyond 4,000 chars; word length alone yields remarkable detection accuracy on genre-controlled datasets (Cohen's d up to 4.11)"
56	  limitations:
57	    - "Key assumption that future LLMs will become increasingly human-like in style could be wrong -- LLMs may converge to a distinct 'mean style' centroid"
58	    - "Only a limited number of datasets and detectors were analyzed; more experiments needed to corroborate practical implications"
59	    - "Humans exposed to LLM writing may adopt LLM stylistic properties, creating a feedback loop"
60	  relation_to_us: "foundation"
61	
62	narrative:
63	  story_type: "突破局限型"
64	  hook: "Generative AI is everywhere -- then immediately juxtaposes contradictory evidence: detectors regularly 'beat' benchmarks yet OpenAI shut down their own detector after 6 months citing lack of accuracy."
65	  tension: "The conflicting reports of success and failure in LLM detection create a puzzle. The paper frames this as a fundamental misunderstanding: researchers build attribution-style detectors but evaluate them under verification assumptions, leading to systematic errors."
66	  key_insight: "Revealed in Section 3.3 via a scaling thought experiment: as you add more human authors to distinguish from an LLM, the attribution approach fails because the number of humans classified as LLM asymptotically approaches all of humanity. This is exactly what current research does by compiling ever-larger corpora. The insight bridges two previously disconnected communities (authorship analytics and LLM detection)."
67	  argument_chain: "Contradiction in detector reports -> bridge to authorship analytics (attribution vs verification) -> theoretical argument that attribution cannot scale (Section 3.3) -> empirical evidence that LLM text properties are converging toward human (Section 4, entropy/MTLD/readability) -> detector evaluation confirming attribution works in-domain but fails cross-model especially for o1 (Section 5) -> discussion of benchmark quality and evaluation metric issues (Section 6) -> conclusion that verification framing is necessary"
68	  contribution_framing: "Four numbered contributions at end of intro: (1) reconcile authorship analytics with LLM detection, showing it is verification; (2) corpus analysis of how LLM text differs from human text; (3) show SOTA detectors solve attribution well; (4) discuss benchmark quality and evaluation needs for verification."
69	  intro_structure: "4 paragraphs: P1 sets scene (LLM text is everywhere, risks, detector interest); P2 presents the contradiction (detectors beat benchmarks vs. serious concerns, OpenAI shutting down detector); P3 frames the explanation (mix-up of attribution vs verification, bridging two communities, explains why attribution fails at scale); P4 lists four contributions with section pointers."
70	  notable_technique: "The thought experiment in Section 3.3 is the rhetorical centerpiece -- it takes a simple two-author scenario and iteratively adds authors to show how attribution inherently breaks down. The paper also excels at connecting a 'new' problem (LLM detection) to a well-established field (authorship analytics) that developed independently, making the reader see that the wheel is being reinvented poorly."
71	
72	figures:
73	  figure_count: 21
74	  figure1:
75	    type: "problem_illustration"
76	    description: "Mean character 3-gram entropy over increasing text length with 95% confidence intervals across three datasets (PAN'24, RAID, M4). Shows per-model entropy curves diverging from human baseline after ~2,500-4,000 characters."
77	    narrative_role: "Core empirical evidence that LLM text has lower entropy than human text, but newer models (GPT-4o, o1) are closing the gap -- supporting the verification framing."
78	    design_elements: ["Multi-panel (a,b,c) by dataset", "Confidence interval shading", "Color-coded per model family", "Human baseline highlighted", "X-axis is text length, Y-axis is entropy"]
79	    visual_style: "Three-panel line plot with shaded confidence intervals. Clean academic style, models labeled directly on curves. Divergence point visible around 2,500 chars."
80	  result_figures:
81	    - figure_id: "Figure 4"
82	      viz_type: "heatmap"
83	      what_compared: "FNR and FPR of SVM, Binoculars, and Mistral-7B detectors across training model families (rows) vs test model families (columns)"
84	      how_gain_highlighted: "Diagonal shows best in-domain performance; o1 row/column visually stands out as failing for all non-o1 detectors"
85	      design_note: "Complex multi-panel figure (4a-4d) combining heatmaps for SVM cross-model, SVM on PAN, Binoculars on PAN, and Mistral on PAN/RAID. Packs maximum information by varying both training and test conditions."
86	    - figure_id: "Figure 5 (Appendix A)"
87	      viz_type: "line_plot"
88	      what_compared: "ROC vs Precision-Recall curves at different class prevalence ratios (P/N = 0.2 to 5.0)"
89	      how_gain_highlighted: "Directly shows ROC is invariant to prevalence while precision degrades, supporting the argument that AUROC is misleading"
90	      design_note: "Side-by-side comparison with color-coded prevalence ratios makes the divergence between ROC and PR curves visually immediate."
91	    - figure_id: "Figure 6 (Appendix B)"
92	      viz_type: "box_plot"
93	      what_compared: "Entropy distributions at 4,500 characters as a discriminator on PAN dataset, per model"
94	      how_gain_highlighted: "Box spread shows which models are separable from humans on entropy alone"
95	      design_note: "Single compact figure showing discriminability limits of a simple feature."
96	    - figure_id: "Figures 7-9 (Appendix D)"
97	      viz_type: "heatmap"
98	      what_compared: "AUROC of SVM, Binoculars, and fine-tuned Mistral across all datasets"
99	      how_gain_highlighted: "Color intensity shows where each detector type succeeds/fails"
100	      design_note: "Supplements Figure 4 with AUROC values; includes bar charts for per-dataset breakdown."
101	  ablation_figures:
102	    - figure_id: "Figure 3"
103	      viz_type: "line_plot"
104	      dimensions_varied: ["Model (Llama2-70b, GPT-3.5, GPT-4o, OpenAI o1)", "Feature set size (top 250 vs top 500 n-grams)", "Pairing type (Human/Human, LLM/LLM, Human/LLM)"]
105	      design_note: "8-panel grid (4 models x 2 feature sizes) showing unmasking curves with IQR shading. Reveals that older models are 'inconsistently' discriminable (high in top-250 but low in top-500), while newer models like o1 are more consistent -- key evidence for the verification argument."
106	    - figure_id: "Figures 18-19 (Appendix G)"
107	      viz_type: "line_plot"
108	      dimensions_varied: ["All 10 model families on PAN'24", "HD dataset models"]
109	      design_note: "Extended unmasking curves for all models, supplementing Figure 3's selected models."
110	    - figure_id: "Figures 20-21 (Appendix G)"
111	      viz_type: "density_plot"
112	      dimensions_varied: ["Compression-based cosine (CBC) score distributions across model pairings"]
113	      design_note: "KDE density plots showing CBC score separation between same-author and cross-author pairs."
114	  figure_narrative_role: "Figure 1 (entropy divergence) -> Figure 2 (human entropy varies by genre) -> Figure 3 (unmasking reveals inconsistency in older LLMs vs consistency in newer ones) -> Figure 4 (detector evaluation confirms attribution works in-domain but fails cross-model). Appendix figures (5-21) provide exhaustive supporting evidence for each main-text claim. The flow is: statistical properties of text -> stylometric analysis -> detector performance."
115	
116	tables:
117	  table_count: 6
118	  main_result_table:
119	    table_id: "N/A -- this paper primarily uses figures (heatmaps/line plots) for main results rather than traditional result tables"
120	    row_axis: "N/A"
121	    col_axis: "N/A"
122	    row_organization: "N/A"
123	    col_organization: "N/A"
124	    highlight_strategy: "N/A"
125	    statistical_reporting: "t-tests with Cohen's d effect sizes reported inline in text; Bonferroni correction for multiple comparisons"
126	    num_baselines: 3
127	    design_note: "Unusual for the field: main results are presented as heatmap figures (Figure 4) rather than tables. This is a deliberate choice that makes cross-model generalization patterns visually immediate. Statistical tests are reported inline rather than in tables."
128	  ablation_tables: []
129	  supplementary_tables:
130	    in_appendix: true
131	    content: "Tables 1-5 in appendix contain qualitative examples of low-quality/short texts from RAID, MAGE, M4, and BLOOMz datasets. Table 6 provides dataset statistics (text counts, human/LLM splits, number of LLMs per dataset)."
132	    reason: "Tables are used for qualitative evidence (bad data examples) and dataset metadata rather than quantitative results. All quantitative comparisons use figures. This split reflects the paper's emphasis on data quality critique -- the appendix tables serve as 'exhibit evidence' for the argument that benchmarks are flawed."
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ae00ae4-6f63-4fcb-9e8f-178a2151d4e2",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "9c437312-a320-4a16-8934-04300d42ae89",
  "sourceToolAssistantUUID": "9ae00ae4-6f63-4fcb-9e8f-178a2151d4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T14:54:38.325Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KZRkqaRqa8sGtTsPeaviAy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/synthetic_eggs2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c437312-a320-4a16-8934-04300d42ae89",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63181de2-e52d-43ae-a0a0-7e21347f430e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 13 · 2026-05-21T14:54:38.338Z_

<details><summary>↩ Tool result · `toolu_01KZRkqaRqa8sGtTsPeaviAy`</summary>

```text
1	paper_key: "synthetic_eggs2026"
2	title: "Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning"
3	venue: "ACL 2026 Findings"
4	full_text_available: false
5	
6	research:
7	  baselines: ["human data fine-tuning", "single-source synthetic fine-tuning", "multi-source synthetic fine-tuning"]
8	  metrics:
9	    - {name: "distribution collapse measures", direction: "lower_better"}
10	    - {name: "adversarial robustness", direction: "higher_better"}
11	    - {name: "self-preference bias", direction: "lower_better"}
12	    - {name: "output quality", direction: "higher_better"}
13	    - {name: "text diversity", direction: "higher_better"}
14	  datasets:
15	    - {name: "synthetic data from multiple LLM sources", size: "N/A"}
16	  ablation_dimensions: ["number of source models", "human vs synthetic ratio", "source model diversity"]
17	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
18	  method_family: "synthetic data diversity analysis for fine-tuning"
19	
20	positioning:
21	  core_claim: "Fine-tuning on diverse multi-source synthetic data mitigates distribution collapse while preserving output distribution breadth, but adversarial robustness decreases"
22	  key_results: "Multi-source synthetic > single-source for distribution collapse; human data best for reducing self-preference bias; synthetic data yields higher quality but lower robustness"
23	  limitations: ["limited to fine-tuning (not pre-training)", "specific LLM families"]
24	  relation_to_us: "complementary"
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
  "parentUuid": "63181de2-e52d-43ae-a0a0-7e21347f430e",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "f0c9aa40-e981-46ce-aba1-975d06ff8d70",
  "sourceToolAssistantUUID": "63181de2-e52d-43ae-a0a0-7e21347f430e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T14:54:38.823Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J6Vtpav5fZPZBkUwyxh1zo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/li2024_mage.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0c9aa40-e981-46ce-aba1-975d06ff8d70",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ff19a6e-ace0-448c-9477-2ec1f9674326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 15 · 2026-05-21T14:54:38.830Z_

<details><summary>↩ Tool result · `toolu_01J6Vtpav5fZPZBkUwyxh1zo`</summary>

```text
1	paper_key: "li2024_mage"
2	title: "MAGE: Machine-generated Text Detection in the Wild"
3	venue: "ACL 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Longformer (PLM-based classifier)"
9	    - "GLTR (GPT-2-XL + logistic regression)"
10	    - "FastText (word bi-gram features)"
11	    - "DetectGPT (zero-shot, T5-3B mask infill + GPT-J-6B scoring)"
12	    - "Human annotators"
13	    - "ChatGPT querying"
14	  metrics:
15	    - {name: "AUROC", direction: "higher_better"}
16	    - {name: "AvgRec (average of HumanRec and MachineRec)", direction: "higher_better"}
17	    - {name: "HumanRec (human text recall)", direction: "higher_better"}
18	    - {name: "MachineRec (machine text recall)", direction: "higher_better"}
19	  datasets:
20	    - {name: "MAGE testbed (custom)", size: "95,596 human + 236,554 machine-generated texts from 7 domains x 27 LLMs"}
21	    - {name: "Reddit ChangeMyView", size: "804 opinion statements"}
22	    - {name: "Yelp", size: "1,000 reviews"}
23	    - {name: "XSum", size: "1,000 news articles"}
24	    - {name: "TLDR", size: "777 news summaries"}
25	    - {name: "ELI5", size: "1,000 QA pairs"}
26	    - {name: "Reddit WritingPrompts", size: "1,000 stories"}
27	    - {name: "ROCStories", size: "1,000 stories"}
28	    - {name: "HellaSwag", size: "1,000 commonsense reasoning"}
29	    - {name: "SQuAD (Wikipedia)", size: "1,000 paragraphs"}
30	    - {name: "SciXGen", size: "1,000 scientific abstracts"}
31	    - {name: "CNN/DailyMail (frontier test)", size: "used in Testbed 7"}
32	    - {name: "DialogSum (frontier test)", size: "used in Testbed 7"}
33	    - {name: "PubMedQA (frontier test)", size: "used in Testbed 7"}
34	    - {name: "IMDb (frontier test)", size: "used in Testbed 7"}
35	  ablation_dimensions:
36	    - "In-distribution vs out-of-distribution (8 testbed scenarios)"
37	    - "Fixed-domain vs arbitrary-domain"
38	    - "Model-specific vs arbitrary-model"
39	    - "Unseen models (cross-validation over 7 model groups)"
40	    - "Unseen domains (cross-validation over 10 domains)"
41	    - "Decision boundary adjustment (0.1% in-domain data)"
42	    - "Paraphrasing attack robustness (gpt-3.5-turbo)"
43	    - "Prompt type (continuation vs topical vs specified)"
44	    - "PLM backbone comparison"
45	    - "Data balance effects"
46	    - "Randomness analysis"
47	  training_recipe:
48	    optimizer: "Adam"
49	    lr: "0.005"
50	    dropout: "0.1"
51	    epochs: "5"
52	    hardware: "8x V100 GPUs"
53	    validation_metric: "classification accuracy"
54	    gltr_lm: "GPT-2-XL"
55	    gltr_classifier: "logistic regression (scikit-learn, grid search)"
56	    fasttext_epochs: "100"
57	    detectgpt_mask_model: "T5-3B"
58	    detectgpt_scoring_model: "GPT-J-6B"
59	    detectgpt_mask_rate: "15%"
60	    detectgpt_perturbations: "100"
61	  method_family: "PLM-based binary classification (Longformer) + statistical/zero-shot baselines for machine-generated text detection"
62	
63	positioning:
64	  core_claim: "First comprehensive 'in-the-wild' testbed for machine-generated text detection spanning 7 domains and 27 LLMs, revealing that perplexity is a double-edged sword — it enables clustering but causes systematic false positives on low-perplexity human text."
65	  key_results: "Longformer achieves AUROC 0.99 in-distribution but drops to 0.95 on unseen models and 0.93 on unseen domains; with 0.1% boundary adjustment data, achieves 86.54% AvgRec on unseen domains + unseen model (GPT-4); paraphrasing attacks degrade AUROC to 0.75."
66	  limitations:
67	    - "Limited model coverage — new LLMs (Alpaca, Vicuna, etc.) continuously emerge and the testbed cannot keep up"
68	    - "Benchmark data bias — source texts may overlap with LLM pretraining data, so detection performance may not transfer to truly novel online text"
69	    - "Vulnerability to paraphrasing attacks (AvgRec drops to 62.92% even with boundary adjustment)"
70	    - "Perplexity bias causes systematic misclassification of low-perplexity human texts as machine-generated"
71	  relation_to_us: "competitor"
72	
73	narrative:
74	  story_type: "突破局限型"
75	  hook: "LLMs have achieved human-level text generation, creating urgent need for detection — but existing detection research only evaluates on specific domains or specific models, leaving open how detectors perform 'in the wild'."
76	  tension: "Prior work assumes controlled settings (known domain, known generator). In reality, detectors face texts from unknown LLMs across diverse domains. The paper asks: can detection still work when we don't know the source?"
77	  key_insight: "Perplexity is a double-edged sword — it is the fundamental feature separating human and machine text (machine text has lower perplexity), but detectors over-rely on it, systematically misclassifying low-perplexity human text. Diverse domains and models cause human-machine linguistic differences to converge, making detection harder."
78	  argument_chain: "problem (detection in controlled settings ≠ detection in the wild) → testbed construction (7 domains × 27 LLMs × 3 prompt types) → 8 progressive evaluation scenarios (in-distribution → OOD) → empirical finding (performance degrades with diversity, especially OOD) → analysis (linguistic convergence + perplexity bias) → mitigation (boundary adjustment with 0.1% data) → feasibility demonstration (86.54% on GPT-4 unseen domain)"
79	  contribution_framing: "Three contributions: (1) comprehensive testbed with texts from diverse human writings and LLMs, (2) empirical analysis revealing diminishing linguistic differences in open-domain settings, (3) discovery that perplexity serves as fundamental but biased clustering feature. Framed as 'first' comprehensive wild-scenario evaluation."
80	  intro_structure: "~5 paragraphs: (1) LLMs generate human-level text → detection needed, (2) existing work limited to specific domains/models, (3) two research questions about wild detection, (4) testbed construction description, (5) key findings and contributions."
81	  notable_technique: "Progressive difficulty design — 8 testbeds arranged from easiest (white-box, single domain, single model) to hardest (unseen domain + unseen model + paraphrasing attack), creating a compelling narrative arc that systematically reveals when and why detection fails."
82	
83	figures:
84	  figure_count: 15
85	  figure1:
86	    type: "problem_illustration"
87	    description: "Left side shows diverse input domains (News Title, Story Title, Question, Argument, Scientific Topic) as colored cards with arrows pointing to both Humans (stick figure at desk) and multiple LLMs (GPT-3.5, FLAN-T5, LLaMA, OPT, GLM, ...) listed vertically. The many-to-many arrows from domains to generators show the combinatorial explosion. Right side shows a 'Text' box passing through a magnifying glass 'Detector' with a question mark, leading to two possible outputs: 'Human' (messy scribble icon) and 'Machine' (clean stick figure). The layout flows left-to-right: sources → generators → mixed text → detection challenge."
88	    narrative_role: "Establishes the core challenge — detection must handle the combinatorial space of domains × generators, not just one domain or one model."
89	    design_elements: ["colored domain cards (purple/orange/green)", "many-to-many arrows showing combinatorial complexity", "magnifying glass as detector metaphor", "question mark conveying uncertainty", "stick figure icons for human vs machine"]
90	    visual_style: "Clean line-art style with selective color on domain cards (purple, orange, green pastels). Horizontal left-to-right flow. Minimal decorative elements. Black-and-white for the detection side. Simple but effective at conveying the many-to-many challenge."
91	  result_figures:
92	    - figure_id: "Figure 2"
93	      viz_type: "grouped_bar_or_line"
94	      what_compared: "OOD detection performance on unseen models, broken down by model family and prompt type"
95	      how_gain_highlighted: "Shows which model families are hardest to detect (OpenAI, FLAN-T5) and which prompt types are most challenging (specified prompts)"
96	      design_note: "Separates analysis by two dimensions (model family × prompt type) to give nuanced OOD understanding rather than single aggregate number"
97	    - figure_id: "Figure 3"
98	      viz_type: "bar_chart_or_line"
99	      what_compared: "Detection performance (AvgRec) on unseen domains, identifying ROC, XSum, TLDR as hardest"
100	      how_gain_highlighted: "Links difficulty to domain perplexity characteristics"
101	      design_note: "Per-domain breakdown reveals systematic pattern (low-perplexity domains harder) rather than just reporting aggregate OOD performance"
102	    - figure_id: "Figure 4"
103	      viz_type: "precision_recall_curve + bar_chart"
104	      what_compared: "(a) PR curves before/after boundary adjustment, (b) performance improvement with 0.1% in-domain data"
105	      how_gain_highlighted: "Direct before/after comparison shows dramatic improvement from minimal adaptation"
106	      design_note: "Two-panel figure pairs theoretical (PR curve) with practical (data requirement) perspectives"
107	  ablation_figures:
108	    - figure_id: "Figure 5"
109	      viz_type: "heatmap"
110	      dimensions_varied: ["domain diversity", "model diversity"]
111	      design_note: "Jensen-Shannon distance heatmap showing linguistic convergence as diversity increases — visual proof that the detection problem gets fundamentally harder with diversity"
112	    - figure_id: "Figure 6"
113	      viz_type: "bar_chart"
114	      dimensions_varied: ["named entity types (ORDINAL, DATE, etc.)"]
115	      design_note: "Shows entity distribution differences in fixed-domain setting as detection shortcuts that disappear with diversity"
116	    - figure_id: "Figures 7-9"
117	      viz_type: "histogram + scatter"
118	      dimensions_varied: ["perplexity distributions", "prediction correctness", "paraphrasing effects"]
119	      design_note: "Three-figure sequence builds the 'perplexity as double-edged sword' argument: (7) machine < human perplexity, (8) misclassified human texts have low perplexity, (9) paraphrasing shifts distributions"
120	  figure_narrative_role: "Figure 1 (problem illustration) → Figures 2-3 (OOD performance breakdown by model/domain) → Figure 4 (boundary adjustment solution) → Figures 5-6 (linguistic convergence analysis) → Figures 7-9 (perplexity analysis arc) → Figures 10-15 (appendix: prompts, data distributions, linguistic stats). The main paper figures follow a 'problem → results → analysis → mitigation' narrative arc."
121	
122	tables:
123	  table_count: 12
124	  main_result_table:
125	    table_id: "Table 3"
126	    row_axis: "methods (Longformer, FastText, GLTR, DetectGPT)"
127	    col_axis: "testbed scenarios (Testbed 2-6) × metrics (AUROC, AvgRec, HumanRec, MachineRec)"
128	    row_organization: "flat"
129	    col_organization: "grouped_by_testbed"
130	    highlight_strategy: "best results in bold across methods per testbed"
131	    statistical_reporting: "single run numbers (no std reported for main results)"
132	    num_baselines: 4
133	    design_note: "Comprehensive table spanning both in-distribution (Testbeds 2-4) and out-of-distribution (Testbeds 5-6) in one view, enabling direct comparison of how each method degrades from ID to OOD. Progressive difficulty across columns tells the degradation story."
134	  ablation_tables:
135	    - table_id: "Table 2"
136	      what_varied: ["white-box detection (Testbed 1) — easiest setting as reference point"]
137	      variation_style: "full_numbers"
138	      design_note: "Separated from main table to establish performance ceiling before showing degradation"
139	    - table_id: "Table 4"
140	      what_varied: ["decision boundary adjustment effect on Testbeds 5-6"]
141	      variation_style: "full_numbers (before vs after adjustment)"
142	      design_note: "Shows boundary adjustment dramatically improves domain-shift performance (AvgRec 68.40→81.78 for unseen domains)"
143	    - table_id: "Table 5"
144	      what_varied: ["challenging frontier tests (Testbed 7: unseen domain+model with GPT-4, Testbed 8: paraphrasing attack)"]
145	      variation_style: "full_numbers with before/after boundary adjustment"
146	      design_note: "Most challenging scenarios isolated in separate table — clean before/after comparison for the proposed mitigation"
147	    - table_id: "Table 1"
148	      what_varied: ["naive baselines (ChatGPT querying, human annotators)"]
149	      variation_style: "full_numbers"
150	      design_note: "Establishes that even humans (~54.5% AvgRec) and ChatGPT (~54.5% AvgRec) struggle at wild detection, motivating the need for dedicated methods"
151	    - table_id: "Tables 8-10"
152	      what_varied: ["randomness analysis", "PLM backbone comparison", "data balance effects"]
153	      variation_style: "full_numbers"
154	      design_note: "Robustness checks in appendix ensure main findings are not artifacts of specific choices"
155	  supplementary_tables:
156	    in_appendix: true
157	    content: "Table 6 (dataset statistics per domain), Table 7 (naive baseline test set composition), Tables 8-10 (robustness: randomness/backbone/balance), Table 11 (all methods on challenging test sets), Table 12 (length statistics)"
158	    reason: "Main paper focuses on the progressive testbed story (Tables 1-5). Appendix holds dataset details and robustness checks that support but don't drive the narrative."
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ff19a6e-ace0-448c-9477-2ec1f9674326",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "e52ec3f1-028f-40ea-ad72-1d5736669e03",
  "sourceToolAssistantUUID": "6ff19a6e-ace0-448c-9477-2ec1f9674326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T14:54:39.269Z_

<details open><summary>🔧 Tool call — Read · `toolu_019wp9gqo4XPV5bH6wRGWehG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mohamed2025_broken_telephone.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e52ec3f1-028f-40ea-ad72-1d5736669e03",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34dbde9c-131d-44fc-b6be-067186f6c8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 17 · 2026-05-21T14:54:39.282Z_

<details><summary>↩ Tool result · `toolu_019wp9gqo4XPV5bH6wRGWehG`</summary>

```text
1	paper_key: "mohamed2025_broken_telephone"
2	title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
3	venue: "ACL 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["single-pass generation", "various prompting strategies"]
8	  metrics:
9	    - {name: "information distortion rate", direction: "lower_better"}
10	    - {name: "semantic similarity to original", direction: "higher_better"}
11	    - {name: "factual accuracy degradation", direction: "lower_better"}
12	  datasets:
13	    - {name: "translation chain experiments", size: "N/A"}
14	  ablation_dimensions: ["number of iterative generations", "language choice", "chain complexity", "prompting strategy"]
15	  training_recipe: {optimizer: "N/A (inference only)", lr: "N/A", hardware: "N/A"}
16	  method_family: "empirical analysis of iterative LLM generation degradation"
17	
18	positioning:
19	  core_claim: "LLMs systematically distort information when outputs are repeatedly processed, with distortion accumulating over iterations analogous to the broken telephone effect"
20	  key_results: "Degradation is inevitable but mitigable through strategic prompting; language and chain complexity influence distortion rate"
21	  limitations: ["primarily translation-based experiments", "limited model coverage"]
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
  "parentUuid": "34dbde9c-131d-44fc-b6be-067186f6c8c3",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "7e696f49-9718-4d8f-9921-1037d853ea1f",
  "sourceToolAssistantUUID": "34dbde9c-131d-44fc-b6be-067186f6c8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T14:54:40.152Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D4Psckgxh2jxVWxyd4Cjmd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2024_tale_of_tails.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e696f49-9718-4d8f-9921-1037d853ea1f",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dda63efd-4be4-4029-9297-b5f3633a5bd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 19 · 2026-05-21T14:54:40.159Z_

<details><summary>↩ Tool result · `toolu_01D4Psckgxh2jxVWxyd4Cjmd`</summary>

```text
1	paper_key: "dohmatob2024_tale_of_tails"
2	title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
3	venue: "ICML 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Original (human/natural) data training"
9	    - "Pure synthetic data training"
10	    - "Mixed real+synthetic data training"
11	    - "Hutter LLM (deterministic lookup table)"
12	    - "Hutter++ (probabilistic bigram)"
13	    - "Capacity-limited associative memory"
14	  metrics:
15	    - {name: "test error (scaling law exponent)", direction: "lower_better"}
16	    - {name: "perplexity", direction: "lower_better"}
17	    - {name: "number of skills learned (GCD answers)", direction: "higher_better"}
18	    - {name: "total variation distance", direction: "lower_better"}
19	  datasets:
20	    - {name: "Wikitext-103", size: "~2M samples for fine-tuning"}
21	    - {name: "GCD arithmetic task (Zipfian)", size: "300K-300M samples"}
22	    - {name: "Synthetic bigram distributions", size: "variable"}
23	  ablation_dimensions:
24	    - "tail cutoff rank k (top-p/top-k truncation)"
25	    - "tail exponent narrowing beta_prime vs beta (temperature scaling)"
26	    - "number of recursive generations n"
27	    - "mixing proportion pi of real vs synthetic data"
28	    - "model capacity / embedding dimension d"
29	    - "Zipf exponent beta"
30	    - "training set size T"
31	  training_recipe:
32	    optimizer: "not explicitly specified in main text"
33	    lr: "not explicitly specified in main text"
34	    hardware: "not explicitly specified"
35	    details: "GCD transformer trained on up to 300M samples; Llama2-7B fine-tuned on Wikitext-103 ~2M samples; synthetic data generated with various top-p and temperature settings"
36	  method_family: "theoretical analysis of model collapse via scaling laws and tail distributions"
37	
38	positioning:
39	  core_claim: "Model collapse is fundamentally a change of scaling laws caused by synthetic data losing the heavy-tailed structure of natural distributions, leading to quantifiable and predictable degradation patterns including plateau effects, skill loss, and shifted scaling exponents."
40	  key_results: "Double scaling law E_test ~ T^(-(beta-1)/beta) + k^(-(beta-1)) predicts performance plateau on synthetic data; multi-generation collapse shows additive degradation E_test ~ T^(-c) + n*T0^(-c); grokking phenomenon when mixing pi-fraction real data creates plateau of length ~k^beta/pi before recovery; triplet scaling law E_test ~ T^(-(1-1/beta)) + d^(-c_q) + k^(-(beta-1)) for capacity-limited models"
41	  limitations:
42	    - "Theory assumes simplified models (Zipfian distributions, deterministic labels for some results)"
43	    - "Grokking theorem strictly holds only for deterministic ground-truth labels; probabilistic settings show attenuated S-shaped curves"
44	    - "Real LLMs involve complex conditional distributions not fully captured by the theoretical framework"
45	    - "Bigram and Hutter models are simplified abstractions of actual language model behavior"
46	    - "No experiments on larger-scale models beyond Llama2-7B"
47	  relation_to_us: "foundation"
48	
49	narrative:
50	  story_type: "突破局限型"
51	  hook: "Opens with the observation that AI model scaling laws have been a key predictive tool, but the ecosystem of online data is co-evolving to contain increasing amounts of synthetic data - asking whether future models will still improve or be 'doomed to degenerate up to total collapse'. Uses the striking statistic that ChatGPT contributes 0.1% of total words generated daily by the global population."
52	  tension: "Existing scaling law theory assumes training on natural (heavy-tailed) data distributions, but the inevitable contamination of training corpora with synthetic data fundamentally breaks these assumptions. Prior work on model collapse identified the phenomenon but lacked a theoretical framework connecting it to scaling laws and emergent abilities."
53	  key_insight: "The key insight is that heavy-tailed (Zipfian) distributions are what enable power-law scaling, and AI generation mechanisms (top-p sampling, temperature scaling, finite sampling) systematically destroy these tails through three mechanisms: tail cutting, tail narrowing, and finite sampling bias. This directly links distributional properties to scaling law behavior."
54	  argument_chain: "problem (synthetic data contamination is inevitable) -> observation (scaling laws depend on heavy-tailed distributions) -> mechanism (AI generation cuts/narrows tails via top-p, temperature, finite sampling) -> theory (double/triplet scaling laws predict plateau and degradation) -> multi-generation analysis (collapse compounds across iterations) -> mitigation (data mixing enables grokking recovery) -> experiments (GCD transformer + Llama2-7B validate predictions)"
55	  contribution_framing: "Four numbered contributions introduced with 'Our main findings are as follows': (1) Double Scaling Law, (2) Triplet Scaling Law for Memory-Limited Models, (3) Model Collapse over Multiple Generations, (4) Mitigation Strategies. Explicitly claims to be 'the first to theoretically and empirically analyze model collapse in the context of scaling laws and emergent abilities'."
56	  intro_structure: "5 paragraphs: P1=hook (scaling laws + synthetic data problem), P2=background (neural scaling laws and heavy tails), P3=problem statement (model collapse concern), P4=key insight (tail mechanisms), P5=contribution list (4 numbered findings)"
57	  notable_technique: "The 'tale of tails' metaphor is the central narrative device - it reframes the abstract concept of model collapse into a concrete, visual story about distribution tails. The three tail destruction mechanisms (cutting, narrowing, finite sampling) provide a clean taxonomy that makes complex theory intuitive. The paper also effectively uses the GCD arithmetic task as a controlled 'microscope' for studying skill emergence and loss, before scaling up to Llama2."
58	
59	figures:
60	  figure_count: 5  # main text; ~35 total including appendices
61	  figure1:
62	    type: "motivation"
63	    description: "Illustrates the three mechanisms by which AI generation destroys distribution tails: top-p nucleus sampling (tail cutting), temperature scaling with tau>1 (tail narrowing), and finite sample bias. Shows how these mechanisms affect a Zipfian frequency distribution and connects to skill loss using GCD calculation (answers 2 and 3) as concrete examples."
64	    narrative_role: "Establishes the paper's core conceptual framework - visually demonstrates WHY model collapse happens by showing the mechanistic link between generation procedures and tail destruction. This is the key figure that makes the abstract theory tangible."
65	    design_elements: ["distribution curves with shaded truncation regions", "before/after comparison of tails", "concrete skill examples (GCD answers)", "three-panel layout for three mechanisms"]
66	    visual_style: "Clean schematic diagrams with distribution curves; uses color to distinguish original vs truncated/narrowed distributions; combines mathematical distributions with concrete task examples"
67	  result_figures:
68	    - figure_id: "Figure 3"
69	      viz_type: "line_plot"
70	      what_compared: "Three panels illustrating main theoretical results: (Left) Double scaling law with Zipf exponent beta=3/2 showing plateau effect; (Middle) Model collapse across 5 generations showing progressive degradation; (Right) Grokking behavior showing plateau length and asymptotic recovery predictions"
71	      how_gain_highlighted: "Theoretical predictions shown as dashed lines overlaid on empirical curves; clear separation between original data scaling (power law) and synthetic data scaling (plateau)"
72	      design_note: "Three-panel layout maps directly to three main theorems; log-log scale makes power-law relationships linear; uses generation number as a visual variable to show progressive collapse"
73	    - figure_id: "Figure 4"
74	      viz_type: "line_plot"
75	      what_compared: "Three experimental validation panels: (Left) Llama2-7B perplexity scaling on Wikitext-103 across generations; (Middle) GCD transformer scaling on original vs synthetic data; (Right) Skills (GCD answers) learned on clean vs AI-generated data"
76	      how_gain_highlighted: "Direct visual comparison of original vs synthetic data curves; skill emergence on clean data vs skill loss on synthetic data is strikingly clear"
77	      design_note: "Mirrors the layout of Figure 3 (theory) to enable direct theory-vs-experiment comparison; this structural parallelism strengthens the validation narrative"
78	    - figure_id: "Figure 5"
79	      viz_type: "line_plot"
80	      what_compared: "Effect of mixing real data (T_real) with AI data (T_AI) - shows performance improvement up to saturation point with k=1000 and beta=3/2"
81	      how_gain_highlighted: "Shows the grokking transition clearly - performance plateaus then recovers as real data fraction increases"
82	      design_note: "Single focused plot isolates the mixing mitigation result; parameters annotated directly on figure"
83	  ablation_figures:
84	    - figure_id: "Figure 2"
85	      viz_type: "combined_distribution_and_perplexity"
86	      dimensions_varied: ["data source (original vs AI-generated)", "generation parameters (top-p, temperature)"]
87	      design_note: "Two-part figure combines perplexity diagram (top) with distribution comparison (bottom); effectively demonstrates that the theoretical tail-cutting/narrowing mechanisms manifest in real LLM outputs"
88	  figure_narrative_role: "Figure 1 (motivation: why tails matter) -> Figure 2 (empirical evidence: tails ARE destroyed in practice) -> Figure 3 (theory: predicted consequences) -> Figure 4 (validation: experiments match theory) -> Figure 5 (mitigation: data mixing helps). Clean motivation-theory-validation-solution arc."
89	
90	tables:
91	  table_count: 0
92	  main_result_table:
93	    note: "This paper has NO tables. All results are presented through mathematical theorems and figures with scaling curves. This is consistent with theoretical ML papers where the primary contributions are equations/bounds rather than benchmark comparisons."
94	  ablation_tables: []
95	  supplementary_tables:
96	    in_appendix: false
97	    content: "No tables in appendix either; appendices contain proofs (Appendices C-F), additional figures (Appendix B), and experimental details (Appendices G-H)"
98	    reason: "The paper is primarily theoretical - results are best expressed as scaling law equations and their visual verification, not tabular comparisons. The continuous nature of scaling curves makes line plots the natural presentation format."
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dda63efd-4be4-4029-9297-b5f3633a5bd9",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "75632975-ebfb-46f5-be85-a3b8144ea4b1",
  "sourceToolAssistantUUID": "dda63efd-4be4-4029-9297-b5f3633a5bd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T14:54:40.654Z_

<details open><summary>🔧 Tool call — Read · `toolu_019qVsaqbkop1J64Qcwevomz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/finlayson2024_closing.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75632975-ebfb-46f5-be85-a3b8144ea4b1",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3d16e9a-9c52-4cc3-a482-21fdb331fc63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 21 · 2026-05-21T14:54:40.658Z_

<details><summary>↩ Tool result · `toolu_019qVsaqbkop1J64Qcwevomz`</summary>

```text
1	paper_key: "finlayson2024_closing"
2	title: "Closing the Curious Case of Neural Text Degeneration"
3	venue: "ICLR 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["nucleus sampling (top-p)", "top-k sampling", "greedy decoding", "threshold-based truncation methods"]
8	  metrics:
9	    - {name: "text quality (human eval)", direction: "higher_better"}
10	    - {name: "text quality (automatic)", direction: "higher_better"}
11	    - {name: "degeneration rate", direction: "lower_better"}
12	  datasets:
13	    - {name: "open-ended text generation benchmarks", size: "N/A"}
14	  ablation_dimensions: ["truncation threshold", "entropy regime", "model size"]
15	  training_recipe: {optimizer: "N/A (decoding strategy)", lr: "N/A", hardware: "N/A"}
16	  method_family: "truncation sampling / decoding strategy analysis"
17	
18	positioning:
19	  core_claim: "The softmax bottleneck causes models to assign nonzero probability to impossible tokens; truncation sampling works by removing these, and a principled approach without arbitrary thresholds is possible"
20	  key_results: "Theoretical proof that threshold-free truncation using softmax bottleneck properties guarantees valid token sampling"
21	  limitations: ["focused on open-ended generation", "theoretical assumptions about softmax bottleneck"]
22	  relation_to_us: "orthogonal"
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
  "parentUuid": "a3d16e9a-9c52-4cc3-a482-21fdb331fc63",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "b16e3c9e-80f6-4248-8168-e84a01f1c830",
  "sourceToolAssistantUUID": "a3d16e9a-9c52-4cc3-a482-21fdb331fc63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T14:54:41.126Z_

<details open><summary>🔧 Tool call — Read · `toolu_012P5LQtreSsepUjePkL2Piz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/yi2026_escaping_collapse.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b16e3c9e-80f6-4248-8168-e84a01f1c830",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df72e7fd-54be-4cfa-af9c-63afd8e1044b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 23 · 2026-05-21T14:54:41.133Z_

<details><summary>↩ Tool result · `toolu_012P5LQtreSsepUjePkL2Piz`</summary>

```text
1	paper_key: "yi2026_escaping_collapse"
2	title: "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence"
3	venue: "ICLR 2026 (Poster)"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Unfiltered synthetic retraining (no verifier)"
9	    - "Real-data-only OLS estimator"
10	    - "VAE trained on full 60K MNIST (upper bound)"
11	  metrics:
12	    - {name: "MSE (parameter estimation error)", direction: "lower_better"}
13	    - {name: "FID (Frechet Inception Distance)", direction: "lower_better"}
14	    - {name: "ELBO (Evidence Lower Bound)", direction: "lower_better"}
15	  datasets:
16	    - {name: "Simulated linear regression", size: "dimension p=8, varying sample sizes (500->2000, 1000->4000, 2000->8000)"}
17	    - {name: "MNIST", size: "500 real images for init, 60K for discriminator training"}
18	  ablation_dimensions:
19	    - "Verifier bias (Delta: 0.0-0.7)"
20	    - "Verifier selectivity/radius (r: 0.05-0.5 for linear; top-10% for VAE)"
21	    - "Training sample size schedule (real->synthetic ratio)"
22	    - "Verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images)"
23	    - "Filtered vs unfiltered synthetic data"
24	  training_recipe:
25	    optimizer: "OLS (closed-form) for linear regression; standard SGD for CVAE"
26	    lr: "N/A for OLS; not specified for VAE"
27	    hardware: "Not specified"
28	    iterations: "60 rounds for linear regression; 40 rounds for VAE"
29	  method_family: "Verifier-guided synthetic data filtering for iterative model retraining"
30	
31	positioning:
32	  core_claim: "External verifier-based filtering of synthetic data prevents model collapse in the short term via bias-variance tradeoff, but long-term performance converges to the verifier's knowledge center rather than ground truth -- unless the verifier is perfectly unbiased."
33	  key_results: "Linear regression: filtered retraining keeps MSE near 0.05 across 60 iterations while unfiltered diverges to 0.3-0.8. VAE/MNIST: FID drops from ~110 to ~40 with 60K-trained verifier over 40 iterations; with only 500-image verifier, FID plateaus at ~130."
34	  limitations:
35	    - "Theoretical analysis restricted to linear regression; generalization to neural networks remains open"
36	    - "VAE verifier (discriminator) is relatively simple and may reject harder-to-generate modes"
37	    - "Synthetic retraining initialized with only 500 real images limits diversity recovery"
38	    - "Verifier quality directly bounds long-term performance ceiling -- biased verifier leads to biased convergence"
39	    - "No experiments on large language models or more complex generative tasks"
40	  relation_to_us: "complementary"
41	
42	narrative:
43	  story_type: "突破局限型"
44	  hook: "Synthetic data is increasingly used to train frontier generative models, but iterative retraining on self-generated data causes model collapse -- a well-documented performance degradation phenomenon."
45	  tension: "Prior work establishes collapse as seemingly inevitable under recursive self-training, but real practitioners already use external verification (human feedback, reward models). The question is: can verification provably escape collapse, and if so, what are the limits?"
46	  key_insight: "Verification creates a bias-variance tradeoff: filtering reduces variance (by discarding low-quality samples) but introduces bias (toward the verifier's knowledge center). Short-term gains are real but long-term convergence is to the verifier's center, not ground truth. Presented through Theorem 3.1 (one-round decomposition) and Theorem 4.1 (long-term contraction)."
47	  argument_chain: "model collapse problem -> prior work shows unfiltered retraining diverges -> introduce verifier-based filtering framework (Generate-Verify-Retrain) -> theoretical analysis: one-round improvement via bias-variance decomposition (Theorem 3.1) -> long-term convergence to verifier center (Theorem 4.1) -> empirical validation on linear regression + VAE/MNIST -> conclusion: verification helps but is fundamentally bounded by verifier quality"
48	  contribution_framing: "Three research questions framed as Q1 (does verification help short-term?), Q2 (do gains sustain long-term?), Q3 (empirical validation). Each answered with a theorem or experiment. Contribution count: 3 clearly delineated."
49	  intro_structure: "4 paragraphs: (1) motivation on synthetic data and model collapse concern, (2) research questions about verifier-based filtering, (3) prior literature context and gaps, (4) bullet-point contributions with theorem references"
50	  notable_technique: "Framing the two results as a deliberate tension -- short-term improvement (good news) vs long-term convergence to verifier center (cautionary news) -- creates a 'promise and peril' narrative arc that is more nuanced than a pure positive-result paper."
51	
52	figures:
53	  figure_count: 5
54	  figure1:
55	    type: "teaser_result"
56	    description: "Three-panel comparison showing VAE-generated MNIST digits: (left) original data, (center-top) with verified synthetic data after 40 rounds showing maintained quality, (center-bottom) without verification showing severe collapse/degradation. (right) upper bound from training on all 60K real images."
57	    narrative_role: "Immediately demonstrates the paper's core claim visually -- verification prevents collapse while unfiltered retraining produces unrecognizable outputs. Placed before any theory to motivate the reader."
58	    design_elements: ["Before/after comparison", "With/without verification contrast", "Real sample grids", "Upper bound reference", "Arrow annotations connecting panels"]
59	    visual_style: "Black background with white MNIST digit grids arranged horizontally. Arrows with text labels ('With Data Verification' / 'Without Data Verification') connect the initial model to the two outcomes. Clean, high-contrast layout. Roughly 4-panel horizontal arrangement."
60	  result_figures:
61	    - figure_id: "Figure 3"
62	      viz_type: "heatmap + heatmap"
63	      what_compared: "One-round improvement landscape as function of verifier bias (Delta) and selectivity radius (r). Left (3a): theory-predicted loss landscape. Right (3b): empirical simulation."
64	      how_gain_highlighted: "Green regions indicate improvement (log ratio > 0), red regions indicate degradation. Theory-empirical match validates the theoretical framework."
65	      design_note: "Diverging green-red colormap centered at 0 makes improvement/degradation regions immediately readable. Side-by-side theory vs empirical layout validates theoretical predictions visually. Axes are interpretable parameters (bias, radius)."
66	    - figure_id: "Figure 4a"
67	      viz_type: "line_plot"
68	      what_compared: "Convergence of parameter estimate to verifier center (theta_c) over 60 iterations for different verifier radii (r=0.1, 0.5, 1, 1.5) with biased verifier"
69	      how_gain_highlighted: "All curves converge to near-zero distance from theta_c, confirming Theorem 4.1. Smaller radius = faster convergence."
70	      design_note: "Clean line plot with distinct colors for each radius value. Y-axis is distance to verifier center, clearly showing contraction. Legend is simple and readable."
71	    - figure_id: "Figure 4b"
72	      viz_type: "line_plot"
73	      what_compared: "Filtered (solid) vs unfiltered (dashed) retraining across different sample size schedules (500->2000, 1000->4000, 2000->8000) over 60 iterations with unbiased verifier"
74	      how_gain_highlighted: "Solid lines (filtered) stay flat near 0.05 while dashed lines (unfiltered) diverge upward to 0.3-0.8. Dramatic visual separation between the two groups."
75	      design_note: "Solid vs dashed line encoding for filtered/unfiltered is effective. Three colors for three sample size conditions. The divergence of dashed lines visually dramatizes model collapse."
76	    - figure_id: "Figure 5a"
77	      viz_type: "line_plot"
78	      what_compared: "VAE FID scores over 40 iterations comparing different VAE training sample sizes and filtered vs unfiltered conditions"
79	      how_gain_highlighted: "Filtered curves decrease steadily; unfiltered curves increase (collapse). Separation grows over iterations."
80	      design_note: "Multiple colored lines with solid/dashed encoding. FID on y-axis with clear downward = better convention."
81	    - figure_id: "Figure 5b"
82	      viz_type: "line_plot"
83	      what_compared: "Effect of verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images) on FID over 40 iterations"
84	      how_gain_highlighted: "Clear monotonic relationship: more verifier training data = lower FID. 60K verifier achieves FID ~40; 500-image verifier plateaus at ~130."
85	      design_note: "Seven colored lines ordered by verifier quality create a clean gradient pattern. Demonstrates the paper's key insight that verification quality bounds final performance. Well-chosen range of verifier sizes."
86	  ablation_figures:
87	    - figure_id: "Figure 3"
88	      viz_type: "heatmap"
89	      dimensions_varied: ["Verifier bias (Delta)", "Verifier selectivity radius (r)"]
90	      design_note: "Effectively an ablation over the two key verifier hyperparameters. Heatmap format makes the full landscape visible at once rather than requiring multiple line plots."
91	    - figure_id: "Figure 5b"
92	      viz_type: "line_plot"
93	      dimensions_varied: ["Verifier training dataset size (quality proxy)"]
94	      design_note: "Ablation over verifier quality showing monotonic improvement. Seven conditions provide fine granularity."
95	  figure_narrative_role: "Figure 1 (teaser: visual proof of concept) -> Figure 2 (pipeline: method overview) -> Figure 3 (theory validation: one-round landscape) -> Figure 4 (long-term dynamics: convergence behavior) -> Figure 5 (real-world validation: VAE experiments). Progression from motivation to theory to practice."
96	
97	tables:
98	  table_count: 0
99	  main_result_table:
100	    table_id: "N/A"
101	    row_axis: "N/A"
102	    col_axis: "N/A"
103	    row_organization: "N/A"
104	    col_organization: "N/A"
105	    highlight_strategy: "N/A"
106	    statistical_reporting: "N/A"
107	    num_baselines: 0
108	    design_note: "Paper has no tables in main text. All results presented through figures (heatmaps and line plots). This is unusual but appropriate for a theory-focused paper where the key results are continuous landscapes and convergence dynamics rather than discrete benchmark comparisons."
109	  ablation_tables: []
110	  supplementary_tables:
111	    in_appendix: true
112	    content: "Appendix A: 1D Gaussian analysis toolkit. Appendix B: Full proofs of Theorems 3.1 and 4.1. Appendix C: VAE experiment details including data preprocessing, discriminator architecture specifications, synthetic generation procedures, and supplementary ELBO results."
113	    reason: "All heavy mathematical proofs and implementation details moved to appendix to keep main paper focused on the two theorems and their experimental validation. Consistent with theory-paper conventions."
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df72e7fd-54be-4cfa-af9c-63afd8e1044b",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "6e83bd25-1921-4455-893b-5d607fd85ed1",
  "sourceToolAssistantUUID": "df72e7fd-54be-4cfa-af9c-63afd8e1044b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T14:54:41.595Z_

<details open><summary>🔧 Tool call — Read · `toolu_019XWk5LCWEPKjnHRXKcez6r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/binoculars2024.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e83bd25-1921-4455-893b-5d607fd85ed1",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6be43fc8-0ab5-47fb-81bb-7c26e91bf28f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 25 · 2026-05-21T14:54:41.599Z_

<details><summary>↩ Tool result · `toolu_019XWk5LCWEPKjnHRXKcez6r`</summary>

```text
1	paper_key: "binoculars2024"
2	title: "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"
3	venue: "ICML 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["DetectGPT", "Fast-DetectGPT", "likelihood thresholding", "supervised classifiers"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	    - {name: "TPR@1%FPR", direction: "higher_better"}
11	    - {name: "TPR@0.01%FPR", direction: "higher_better"}
12	  datasets:
13	    - {name: "multi-domain text corpus (news, wiki, creative)", size: "N/A"}
14	    - {name: "ChatGPT-generated samples", size: "N/A"}
15	  ablation_dimensions: ["LLM pair choice", "document type", "source model"]
16	  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
17	  method_family: "zero-shot detection via contrastive LLM scoring"
18	
19	positioning:
20	  core_claim: "A simple score contrasting two closely related LLMs achieves SOTA zero-shot detection without any training data, detecting >90% of generated text at 0.01% FPR"
21	  key_results: ">90% detection of ChatGPT at 0.01% FPR; generalizes across LLMs without model-specific tuning"
22	  limitations: ["requires two LLMs at inference", "performance depends on LLM pair choice"]
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
  "parentUuid": "6be43fc8-0ab5-47fb-81bb-7c26e91bf28f",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "c3570412-20c7-4795-b0ac-76da0cbc349a",
  "sourceToolAssistantUUID": "6be43fc8-0ab5-47fb-81bb-7c26e91bf28f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T14:54:42.066Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LNwMuJq6jFPERpKmJa9r4q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/fast_detectgpt2024.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3570412-20c7-4795-b0ac-76da0cbc349a",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b684f695-8cd5-4ecc-aa9b-46ba4d546394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 27 · 2026-05-21T14:54:42.072Z_

<details><summary>↩ Tool result · `toolu_01LNwMuJq6jFPERpKmJa9r4q`</summary>

```text
1	paper_key: "fast_detectgpt2024"
2	title: "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"
3	venue: "ICLR 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["DetectGPT", "likelihood ratio", "rank-based methods", "supervised detectors"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	    - {name: "detection speed", direction: "higher_better"}
11	  datasets:
12	    - {name: "XSum", size: "N/A"}
13	    - {name: "SQuAD", size: "N/A"}
14	    - {name: "WritingPrompts", size: "N/A"}
15	  ablation_dimensions: ["source model", "scoring model", "perturbation vs sampling"]
16	  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
17	  method_family: "zero-shot detection via conditional probability curvature"
18	
19	positioning:
20	  core_claim: "Replacing DetectGPT's perturbation step with conditional probability sampling achieves 340x speedup with ~75% relative improvement in both white-box and black-box settings"
21	  key_results: "340x faster than DetectGPT; 75% relative improvement; 80% ChatGPT detection at 1% FPR"
22	  limitations: ["still requires model access for scoring", "performance varies by domain"]
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
  "parentUuid": "b684f695-8cd5-4ecc-aa9b-46ba4d546394",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "6decc50a-daa6-43ec-9076-0bb7abb6bd1a",
  "sourceToolAssistantUUID": "b684f695-8cd5-4ecc-aa9b-46ba4d546394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T14:54:43.008Z_

<details open><summary>🔧 Tool call — Read · `toolu_014t1XaxKp7MxKAmkQSNUTXH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/diveye2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6decc50a-daa6-43ec-9076-0bb7abb6bd1a",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dbae57a-adc2-4f74-b079-897ac2038886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 29 · 2026-05-21T14:54:43.014Z_

<details><summary>↩ Tool result · `toolu_014t1XaxKp7MxKAmkQSNUTXH`</summary>

```text
1	paper_key: "diveye2026"
2	title: "DivEye: Diversity Boosts AI-Generated Text Detection"
3	venue: "TMLR 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["DetectGPT", "Fast-DetectGPT", "Binoculars", "supervised fine-tuned classifiers"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	    - {name: "detection accuracy", direction: "higher_better"}
11	  datasets:
12	    - {name: "multi-domain benchmarks", size: "N/A"}
13	  ablation_dimensions: ["statistical features", "auxiliary signal integration", "paraphrasing robustness", "cross-domain transfer"]
14	  training_recipe: {optimizer: "N/A (zero-shot statistical)", lr: "N/A", hardware: "N/A"}
15	  method_family: "statistical feature-based detection using surprisal diversity"
16	
17	positioning:
18	  core_claim: "Human text exhibits richer variability in lexical and structural unpredictability (surprisal diversity) than LLM outputs, and this signal is interpretable, robust, and complements existing detectors"
19	  key_results: "Outperforms zero-shot detectors by up to 33.2%; improves existing detectors by up to 18.7% as auxiliary signal; robust to paraphrasing attacks"
20	  limitations: ["statistical features may not capture all AI text patterns", "performance on very short texts unclear"]
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
  "parentUuid": "6dbae57a-adc2-4f74-b079-897ac2038886",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "e0c48970-1788-4ad4-9a3c-f26bd7a497e8",
  "sourceToolAssistantUUID": "6dbae57a-adc2-4f74-b079-897ac2038886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T14:54:43.479Z_

<details open><summary>🔧 Tool call — Read · `toolu_011NKY9Puk2SSDLNV5oFGTu8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/verma2024_ghostbuster.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c48970-1788-4ad4-9a3c-f26bd7a497e8",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9457e321-dcda-45cb-a1f4-8733209d8f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 31 · 2026-05-21T14:54:43.486Z_

<details><summary>↩ Tool result · `toolu_011NKY9Puk2SSDLNV5oFGTu8`</summary>

```text
1	paper_key: "verma2024_ghostbuster"
2	title: "Ghostbuster: Detecting Text Ghostwritten by Large Language Models"
3	venue: "NAACL 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Perplexity-only (GPT-3 davinci perplexity threshold)"
9	    - "DetectGPT (Mitchell et al. 2023, unsupervised perturbation-based)"
10	    - "GPTZero (commercial detector)"
11	    - "RoBERTa fine-tuned (supervised neural baseline)"
12	    - "Human evaluation (17 participants)"
13	  metrics:
14	    - {name: "F1", direction: "higher_better"}
15	    - {name: "Accuracy", direction: "higher_better"}
16	    - {name: "Precision", direction: "higher_better"}
17	  datasets:
18	    - {name: "IvyPanda Student Essays", size: "7,000 docs (1K human + 1K ChatGPT same-prompt + 4K ChatGPT generalization)"}
19	    - {name: "Reuters 50-50 News Articles", size: "7,000 docs (same split structure)"}
20	    - {name: "r/WritingPrompts Creative Writing", size: "7,000 docs (same split structure)"}
21	    - {name: "Lang-8 non-native English", size: "evaluation only"}
22	    - {name: "TOEFL 11 (essay subset)", size: "evaluation only"}
23	    - {name: "TOEFL 91 (essay subset)", size: "evaluation only"}
24	  ablation_dimensions:
25	    - "Feature search depth (1, 2, 3, 4)"
26	    - "Model components (with/without ada, davinci, handcrafted features)"
27	    - "Random features vs selected features"
28	    - "Document length (10-1000 tokens)"
29	    - "Perturbation robustness (character/word/sentence/paragraph level)"
30	    - "Cross-domain generalization (in-domain vs out-of-domain)"
31	    - "Cross-model generalization (ChatGPT vs Claude)"
32	    - "Cross-prompt generalization (5 prompt variants)"
33	  training_recipe:
34	    classifier: "Logistic regression with L2 regularization, C=1"
35	    optimizer: "N/A (closed-form or standard sklearn solver)"
36	    lr: "N/A"
37	    hardware: "Not specified"
38	    feature_generation: "Recursive composition of vector/scalar functions up to depth 3, yielding 2534 candidate features"
39	    feature_selection: "Forward feature selection on validation set"
40	    weaker_models: "Unigram fertility, Kneser-Ney trigram, GPT-3 ada, GPT-3 davinci"
41	  method_family: "Feature-engineered classifier using proxy model probabilities"
42	
43	positioning:
44	  core_claim: "A structured search over compositions of weaker language model probabilities, combined with a simple linear classifier, can robustly detect AI-generated text without access to the target model's token probabilities."
45	  key_results: "99.0 F1 in-domain across all domains (+0.9 over RoBERTa, +5.9 over GPTZero); 97.0 F1 out-of-domain average (vs 85.1 RoBERTa); 92.2 F1 on Claude generalization; 99.5 F1 across prompt variants"
46	  limitations:
47	    - "Poor performance on documents under 100 tokens (F1 drops below 80 at 25 tokens)"
48	    - "Lower accuracy on non-native English speaker text (TOEFL 91: 74.7% accuracy, below GPTZero 92.3% and RoBERTa 96.7%)"
49	    - "Datasets limited to British/American English, not representative of all writing styles"
50	    - "Vulnerable to paraphrasing attacks (Undetectable.ai reduces recall from 99% to 62%)"
51	    - "Relies on API access to GPT-3 ada/davinci which may be deprecated"
52	  relation_to_us: "foundation"
53	
54	narrative:
55	  story_type: "突破局限型"
56	  hook: "Opens with the societal impact of ChatGPT's fluent text generation — schools restricting ChatGPT, authenticity concerns across education and journalism — establishing real-world urgency."
57	  tension: "Existing detectors (DetectGPT, GPTZero) show poor generalization across domains and models; supervised neural methods (RoBERTa) overfit to training distribution; zero-shot methods require target model token probabilities (a black-box limitation). Additionally, high false positive rates create ethical risks, disproportionately flagging non-native English speakers."
58	  key_insight: "Instead of requiring the target LLM's own probabilities, use a series of weaker, accessible language models as probability proxies, then let a structured combinatorial search discover discriminative feature compositions — the signal is in how different-quality models disagree on token predictions."
59	  argument_chain: "Problem (LLM text indistinguishable from human) → Existing solutions fail to generalize → Key insight: weaker model probability compositions are discriminative → Structured search over vector/scalar function compositions → Simple linear classifier achieves SOTA → Validated across 3 domains, cross-model (Claude), cross-prompt, perturbation robustness, and human comparison"
60	  contribution_framing: "Three contributions implicitly stated: (1) Ghostbuster method itself (structured search + linear classifier on weaker model probabilities), (2) three new benchmark datasets for AI text detection, (3) extensive evaluation including cross-domain, cross-model, cross-prompt generalization and robustness analysis. Framed via performance superiority: 'achieves 99.0 F1... 5.9 F1 higher than the best preexisting model.'"
61	  intro_structure: "3 paragraphs — P1: Problem establishment (ChatGPT impact, societal concerns); P2: Existing solution failures (poor generalization, false positives, bias against non-native speakers); P3: Ghostbuster introduction with headline numbers and method sketch"
62	  notable_technique: "Effective use of the 'black-box constraint' framing — positions the paper as solving a harder, more practical problem than prior work (no access to target model probabilities), which makes the strong results even more impressive. Also leverages the non-native speaker bias issue to establish ethical urgency."
63	
64	figures:
65	  figure_count: 6
66	  figure1:
67	    type: "method_overview"
68	    description: "Left-to-right pipeline diagram showing the three stages of Ghostbuster: (1) a text document is passed through three weaker language models (Unigram, Trigram, GPT-3) producing probability vectors, (2) vector functions (+, -, x, /, >, <) combine probability vectors, (3) scalar functions (||.||, max, var) reduce to features, (4) features fed to logistic regression classifier visualized as a scatter plot."
69	    narrative_role: "Provides immediate visual understanding of the full pipeline — reader grasps the method in one glance before the technical details."
70	    design_elements: ["Left-to-right flow", "Color-coded stages (blue models, purple vector ops, purple scalar ops, tan classifier)", "Mathematical operator symbols inside boxes", "Scatter plot as classifier visualization"]
71	    visual_style: "Clean horizontal pipeline with rounded-rectangle boxes. Pastel color scheme (light blue for models, lavender for function boxes, beige for classifier). Minimal text labels. Text snippet shown as input on the left. Arrows connect stages. Compact single-row layout."
72	  result_figures:
73	    - figure_id: "Figure 3"
74	      viz_type: "line_plot"
75	      what_compared: "F1 score degradation under increasing numbers of perturbations, split into local (character/word) and global (sentence/paragraph) perturbations"
76	      how_gain_highlighted: "Shows robustness envelope — performance stays above 80 F1 for most perturbation types until extreme levels; separate panels for local vs global perturbations make degradation patterns clear"
77	      design_note: "Two-panel layout (local left, global right) with shared y-axis (F1 Score) and color-coded lines per perturbation type. Legend inside plot. Clear visual separation of graceful degradation (character flips) vs catastrophic failure (paraphrasing). X-axis scales differ between panels (1-256 vs 0-10)."
78	    - figure_id: "Figure 4"
79	      viz_type: "line_plot"
80	      what_compared: "F1 score across document sizes (10-1000 tokens) for in-domain and various out-of-domain settings (Claude, WP, Reuters, Essay)"
81	      how_gain_highlighted: "All lines converge to ~95-100 F1 at 500+ tokens, visually demonstrating reliability at longer documents; short-document weakness is honestly shown"
82	      design_note: "Single plot with 5 color-coded lines (blue=In-Domain, orange=Claude, green=WP, red=Reuters, purple=Essay). Dark background with grid. Log-scale-like x-axis (10,25,50,100,250,500,1000). Clearly shows the critical 100-token threshold where performance becomes reliable."
83	  ablation_figures:
84	    - figure_id: "Figure 5"
85	      viz_type: "feature_list"
86	      dimensions_varied: ["Domain (News, Creative Writing, Essays)", "Selected features per domain"]
87	      design_note: "Lists the actual features selected by forward selection for each domain — not a traditional chart but a reference figure showing which compositions matter. Allows readers to see domain-specific vs shared features."
88	    - figure_id: "Figure 6"
89	      viz_type: "bar_chart"
90	      dimensions_varied: ["Dataset (WritingPrompts, Reuters, IvyPanda)", "Entropy rate under GPT-3"]
91	      design_note: "Entropy rate visualization comparing human vs AI text predictability across domains — supports the theoretical motivation for why probability-based features work."
92	  figure_narrative_role: "Figure 1 (method overview) → Figure 2 (motivating example: human vs AI text side-by-side) → Figure 3 (robustness analysis) → Figure 4 (document length sensitivity) → Figure 5 (feature analysis, appendix) → Figure 6 (theoretical motivation via entropy, appendix). Main paper figures (1-4) follow: explain method → show problem → stress-test → analyze boundary conditions."
93	
94	tables:
95	  table_count: 8
96	  main_result_table:
97	    table_id: "Table 2"
98	    row_axis: "methods"
99	    col_axis: "domains (News, Creative Writing, Student Essays, All Domains) x settings (In-Domain, Out-of-Domain)"
100	    row_organization: "by_category"
101	    col_organization: "grouped_by_dataset"
102	    highlight_strategy: "Best results implied by Ghostbuster row consistently highest; no explicit bold/underline formatting noted in HTML version"
103	    statistical_reporting: "Point estimates only, no confidence intervals or standard deviations"
104	    num_baselines: 4
105	    design_note: "Two major column groups (In-Domain | Out-of-Domain) with domain sub-columns. Clean structure shows both the in-domain ceiling and generalization gap simultaneously. Key insight: Ghostbuster's advantage is most visible in OOD columns where RoBERTa drops significantly (99.4→88.3 on News) while Ghostbuster stays high (99.5→97.9). The 'All Domains' column aggregates for quick comparison."
106	  ablation_tables:
107	    - table_id: "Table 4"
108	      what_varied: ["Feature search depth (1,2,3,4)", "Model components (ada, davinci, handcrafted)", "Feature selection method (random vs forward)"]
109	      variation_style: "full_numbers"
110	      design_note: "Comprehensive ablation with 9 conditions. Same column structure as Table 2 (domains x in/out-of-domain) enables direct comparison. Shows diminishing returns beyond depth 3, critical importance of GPT-3 models (without ada/davinci: 88.2 vs 99.0), and that handcrafted features add marginal value (98.9 without vs 99.0 with)."
111	  supplementary_tables:
112	    in_appendix: true
113	    content: "Table 1: Vector/scalar function definitions. Table 3: Generalization results (prompts, Claude, non-native). Tables 5-8: Dataset statistics, prompt templates, generation details."
114	    reason: "Table 1 is a reference table for the method's building blocks. Table 3 covers secondary evaluation axes. Tables 5-8 provide reproducibility details. Main paper keeps only the two most important tables (main results + ablations) to maintain narrative focus."
115	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9457e321-dcda-45cb-a1f4-8733209d8f8f",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "f27c921b-8866-4559-9181-d2499da8b178",
  "sourceToolAssistantUUID": "9457e321-dcda-45cb-a1f4-8733209d8f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T14:54:43.949Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D6sun6r5n1fRQdAy6A3ikA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/penedo2024_fineweb.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f27c921b-8866-4559-9181-d2499da8b178",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "475a1734-44cb-47f0-a5cb-09983fa6b8ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 33 · 2026-05-21T14:54:43.955Z_

<details><summary>↩ Tool result · `toolu_01D6sun6r5n1fRQdAy6A3ikA`</summary>

```text
1	paper_key: "penedo2024_fineweb"
2	title: "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale"
3	venue: "NeurIPS 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - RefinedWeb
9	    - C4
10	    - The Pile
11	    - SlimPajama
12	    - RedPajama v2
13	    - Dolma 1.6
14	    - Dolma 1.7
15	    - Matrix
16	    - CC-100
17	    - Colossal-OSCAR
18	  metrics:
19	    - {name: "Aggregate Accuracy (avg of 9 benchmarks)", direction: "higher_better"}
20	    - {name: "HellaSwag", direction: "higher_better"}
21	    - {name: "MMLU", direction: "higher_better"}
22	    - {name: "ARC", direction: "higher_better"}
23	    - {name: "PIQA", direction: "higher_better"}
24	    - {name: "WinoGrande", direction: "higher_better"}
25	    - {name: "OpenBookQA", direction: "higher_better"}
26	    - {name: "CommonSenseQA", direction: "higher_better"}
27	    - {name: "SIQA", direction: "higher_better"}
28	  datasets:
29	    - {name: "FineWeb", size: "15T tokens from 96 Common Crawl snapshots"}
30	    - {name: "FineWeb-Edu", size: "1.3T tokens (educational subset of FineWeb)"}
31	    - {name: "RefinedWeb", size: "500B tokens"}
32	    - {name: "C4", size: "172B tokens"}
33	    - {name: "The Pile", size: "340B tokens"}
34	    - {name: "SlimPajama", size: "627B tokens"}
35	    - {name: "RedPajama v2", size: "20T tokens"}
36	    - {name: "Dolma 1.6", size: "3T tokens"}
37	    - {name: "Dolma 1.7", size: "1.2T tokens"}
38	    - {name: "Matrix", size: "1.3T tokens"}
39	    - {name: "CC-100", size: "70B tokens"}
40	    - {name: "Colossal-OSCAR", size: "850B tokens"}
41	  ablation_dimensions:
42	    - text_extraction_method (WARC trafilatura vs WET htmlparser)
43	    - base_filtering (URL blocklist + language ID + quality/repetition filters)
44	    - deduplication_scope (global vs per-snapshot MinHash)
45	    - deduplication_parameters (n-gram size, hash count, bucket structure, similarity threshold)
46	    - C4_filter_components (terminal punctuation, JS removal, ToS, doc length, lorem ipsum)
47	    - custom_heuristic_filters (50+ candidate statistics, 17 tested in Table 2)
48	    - educational_quality_threshold (0-5 scale, threshold sweep)
49	    - training_scale (28B tokens for filter ablations vs 350B for dedup ablations)
50	  training_recipe:
51	    model: "1.82B parameters (including embeddings), Llama architecture"
52	    optimizer: "not explicitly stated (likely AdamW given Llama architecture)"
53	    lr: "not explicitly stated"
54	    batch_size: "~2M tokens global batch size"
55	    sequence_length: 2048
56	    tokenizer: "GPT-2 tokenizer"
57	    hardware: "H100 GPUs, ~80,000 GPU-hours for 70+ ablation models"
58	    filter_ablation_tokens: "~28B tokens"
59	    dedup_ablation_tokens: "350B tokens"
60	    edu_classifier_cost: "6,000 H100 GPU-hours for classifying 15T tokens"
61	  method_family: "large-scale web data curation pipeline (extraction + filtering + deduplication + quality classification)"
62	
63	positioning:
64	  core_claim: "Systematic, transparent web data curation with carefully ablated design choices produces 15T-token FineWeb and 1.3T-token FineWeb-Edu that outperform all existing open pretraining datasets, closing the gap between proprietary and public data knowledge."
65	  key_results: "FineWeb: ~52% aggregate accuracy at 350B tokens (top among all open datasets). FineWeb-Edu: MMLU 33%->37% (+12% relative), ARC 46%->57% (+24% relative), ~2% aggregate accuracy gain over FineWeb, reaching 33.6% MMLU at 38B tokens vs Matrix needing 300B tokens for similar."
66	  limitations:
67	    - "Entirely web content from Common Crawl; no books, speech transcripts, or other data types"
68	    - "Most ablation experiments at smaller scale (~28B tokens) due to compute constraints; dataset design at realistic pretraining scale could give more reliable guidance"
69	    - "Evaluation limited to academic benchmarks without instruction tuning or alignment; does not reflect current LLM usage patterns"
70	    - "Educational quality classifier may amplify biases in what Llama-3-70B-Instruct considers 'educational'"
71	  relation_to_us: "complementary"
72	
73	narrative:
74	  story_type: "化繁为简型"
75	  hook: "Opens with the ubiquity of LLMs and immediately pivots to the dirty secret: [REDACTED] pretraining datasets behind the best open models (Llama 3, Mixtral) are not public, and curation strategies are 'closely guarded trade secrets.' Frames a growing gap between proprietary and public knowledge."
76	  tension: "Despite LLM performance depending heavily on data quality, the community lacks both access to high-quality large-scale datasets AND knowledge of how to build them. Existing open datasets are either too small, poorly documented, or underperform. The reader is made to feel the asymmetry between what industry knows and what the public can access."
77	  key_insight: "Global deduplication across all 96 Common Crawl snapshots paradoxically HURTS performance because it upsamples lower-quality data from older crawls. The data removed by global dedup was actually higher quality than the data retained. Per-snapshot individual deduplication is the correct approach. This counterintuitive finding is the paper's most distinctive empirical contribution."
78	  argument_chain: "problem (data curation is a black box) -> foundation (review existing datasets/methods) -> systematic pipeline construction (text extraction -> base filtering -> deduplication -> C4 filters -> custom filters, each ablated independently) -> counterintuitive dedup finding drives design -> cumulative pipeline = FineWeb 15T -> educational filtering via LLM annotation + lightweight classifier = FineWeb-Edu 1.3T -> validation against 10 baselines at 350B scale"
79	  contribution_framing: "Contributions woven into intro prose rather than bulleted list. Six implicit contributions: (1) FineWeb 15T dataset, (2) FineWeb-Edu 1.3T educational subset, (3) systematic ablation of all design choices, (4) in-depth deduplication investigation, (5) datatrove curation codebase, (6) all ablation models publicly released. Framed as 'advancing understanding' not just 'beating baselines.'"
80	  intro_structure: "Single long paragraph (~15 sentences) that covers: LLM success -> data importance -> scale + quality matter -> curation as trade secrets -> open models with closed data -> knowledge gap concern -> FineWeb introduction -> FineWeb-Edu introduction -> ablation methodology -> public release commitment. Unusually dense single-paragraph intro rather than multi-paragraph."
81	  notable_technique: "The 'ablation-as-narrative' structure: each section of the pipeline (extraction, filtering, dedup) is presented as a mini-experiment with its own hypothesis, ablation, finding, and decision. This makes a data engineering paper read like a sequence of scientific investigations. The counterintuitive global-dedup finding (Section 3.4) serves as the paper's dramatic peak, breaking reader expectations."
82	
83	figures:
84	  figure_count: 27
85	  figure1:
86	    type: "motivation"
87	    description: "Line plot comparing aggregate accuracy (%) vs training tokens (billions, 0-28B) for two text extraction methods: WARC data processed with trafilatura (blue) vs WET default htmlparser (pink). Both start at ~33% and diverge steadily, with WARC reaching ~39.5% and WET plateauing at ~37.5% by 28B tokens."
88	    narrative_role: "Establishes the very first pipeline decision (text extraction) as consequential. Sets the pattern for all subsequent ablation figures: same axes, same comparison logic. Justifies the non-trivial compute cost of trafilatura over default WET."
89	    design_elements:
90	      - "Clean two-line comparison on same axes"
91	      - "Continuous training curves (not bar charts) showing the gap widens with scale"
92	      - "Minimal design: no grid clutter, clear legend below"
93	      - "Blue vs pink color coding for proposed vs baseline"
94	    visual_style: "Minimalist line plot, white background with faint horizontal gridlines. Two smoothly rising curves, blue (WARC/trafilatura) consistently above pink (WET). Legend below plot. Axes: y=Aggregate Acc (%), x=Training tokens (billions). Clean academic style, no unnecessary decoration."
95	  result_figures:
96	    - figure_id: "Figure 9"
97	      viz_type: "line_plot"
98	      what_compared: "Cumulative pipeline steps: base filtering vs +individual minhash vs +C4 filters vs full FineWeb, all at 350B token scale"
99	      how_gain_highlighted: "Four stacked training curves with clear vertical separation; FineWeb (orange) consistently on top, base filtering (green) consistently on bottom, showing each step adds measurable gain"
100	      design_note: "Uses same axis style as all ablation figures for visual continuity. Four colors clearly differentiated. Shows pipeline is monotonically improving—each step helps."
101	    - figure_id: "Figure 10"
102	      viz_type: "line_plot"
103	      what_compared: "FineWeb and FineWeb-Edu (Ours) vs 10 competing open datasets, all at 350B token scale"
104	      how_gain_highlighted: "FineWeb-Edu (orange) clearly on top reaching ~52%, FineWeb (green) in upper pack at ~50.5%. Color coding: 'Ours' in warm colors (orange, green) while competitors in cooler/darker colors. Visual dominance of FineWeb-Edu curve is immediate."
105	      design_note: "12 lines in one plot—aggressive but effective for showing FineWeb-Edu's dominance. Legend organized in 4 columns below. The visual message is clear even with crowded lines because the 'Ours' curves are distinctly above the pack."
106	    - figure_id: "Figure 11"
107	      viz_type: "line_plot"
108	      what_compared: "FineWeb-Edu vs competitors on MMLU specifically, showing token efficiency"
109	      how_gain_highlighted: "FineWeb-Edu reaches 33.6% at 38B tokens while Matrix needs 300B tokens for similar—10x token efficiency. The gap is visually dramatic."
110	      design_note: "Single-benchmark focus plot to highlight the most impressive result. Token efficiency narrative is more compelling than raw accuracy."
111	  ablation_figures:
112	    - figure_id: "Figure 6"
113	      viz_type: "bar_chart"
114	      dimensions_varied: ["individual C4 filter components"]
115	      design_note: "Bar chart showing each C4 filter's individual contribution to HellaSwag. Reveals terminal punctuation filter is most impactful but also most aggressive (removes ~30% tokens)."
116	    - figure_id: "Figure 7"
117	      viz_type: "bar_chart"
118	      dimensions_varied: ["custom filter combinations vs C4 vs baseline"]
119	      design_note: "Shows custom FineWeb filters outperform C4 while removing less data. Efficiency argument (better accuracy per token removed)."
120	    - figure_id: "Figure 8"
121	      viz_type: "histogram"
122	      dimensions_varied: ["deduplication method effect on punctuation distribution"]
123	      design_note: "Histogram of document-level punctuation ratios under different dedup methods. Reveals mechanism behind global dedup's failure: it shifts distribution toward low-punctuation (lower quality) documents."
124	    - figure_id: "Figure 16"
125	      viz_type: "line_plot"
126	      dimensions_varied: ["FineWeb-Edu educational quality threshold (0-5 scale)"]
127	      design_note: "Threshold sweep ablation for educational classifier. Shows threshold=3 is optimal; lower includes too much noise, higher is too aggressive."
128	  figure_narrative_role: "Fig 1-2 (text extraction + base filtering foundations) -> Fig 3-5 (dedup exploration: global failure -> individual success) -> Fig 6-8 (filter development: C4 decomposition -> custom filters -> mechanism analysis) -> Fig 9-10 (cumulative victory: pipeline steps + competitive comparison) -> Fig 11 (FineWeb-Edu headline result) -> Fig 12-16 (appendix: parameter details + threshold ablation) -> Fig 17-27 (bias analysis: distribution + association heatmaps). The narrative arc follows the pipeline construction chronologically, building evidence cumulatively."
129	
130	tables:
131	  table_count: 4
132	  main_result_table:
133	    table_id: "Table 2"
134	    description: "Full list of heuristic filters tested"
135	    row_axis: "candidate filter metrics with thresholds"
136	    col_axis: "metric | threshold | aggregate accuracy (%) | tokens removed (%)"
137	    row_organization: "by_performance"
138	    col_organization: "flat"
139	    highlight_strategy: "implicit ranking by aggregate accuracy (descending), no explicit bold/underline"
140	    statistical_reporting: "single-run accuracy and token removal percentage"
141	    num_baselines: 16
142	    design_note: "Unusual 'main table'—not a method-vs-baseline comparison but a filter candidate evaluation. The real main comparison is in Figure 10 (line plot), not a table. This reflects the paper's nature as a data engineering study where the 'results' are pipeline design choices, not model benchmarks. The table serves as a filter selection guide."
143	  ablation_tables: []
144	  supplementary_tables:
145	    in_appendix: true
146	    content: "Table 3 (bias analysis subgroups/terms). Additional dataset field documentation tables. The paper relies heavily on figures rather than tables for ablation results."
147	    reason: "Pipeline ablations are shown as training curves (line plots) because the temporal dynamics of how performance evolves with tokens is more informative than single-point numbers. Tables are reserved for enumeration tasks (filter list, bias terms, data fields)."
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "475a1734-44cb-47f0-a5cb-09983fa6b8ce",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "88992bf4-44ce-435a-94ab-78c84a6d78a5",
  "sourceToolAssistantUUID": "475a1734-44cb-47f0-a5cb-09983fa6b8ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T14:54:44.425Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RB6xxyRJLnkDcF9qGEJeUp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/loki2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88992bf4-44ce-435a-94ab-78c84a6d78a5",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40fc5df2-6ab3-44eb-a81d-ae8b0789fa13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 35 · 2026-05-21T14:54:44.431Z_

<details><summary>↩ Tool result · `toolu_01RB6xxyRJLnkDcF9qGEJeUp`</summary>

```text
1	paper_key: "loki2025"
2	title: "LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models"
3	venue: "ICLR 2025 Spotlight"
4	full_text_available: false
5	
6	research:
7	  baselines: ["22 open-source LMMs", "6 closed-source LMMs"]
8	  metrics:
9	    - {name: "coarse-grained judgment accuracy", direction: "higher_better"}
10	    - {name: "fine-grained anomaly selection accuracy", direction: "higher_better"}
11	    - {name: "explanation quality", direction: "higher_better"}
12	  datasets:
13	    - {name: "LOKI benchmark", size: "18K questions across 26 subcategories"}
14	  ablation_dimensions: ["modality (video/image/3D/text/audio)", "difficulty level", "task type (judgment/selection/explanation)"]
15	  training_recipe: {optimizer: "N/A (benchmark)", lr: "N/A", hardware: "N/A"}
16	  method_family: "multimodal synthetic data detection benchmark"
17	
18	positioning:
19	  core_claim: "First comprehensive benchmark for evaluating LMM ability to detect synthetic data across 5 modalities with both coarse and fine-grained evaluation"
20	  key_results: "LMMs show potential as synthetic detectors but reveal significant limitations; large gap between coarse judgment and fine-grained explanation"
21	  limitations: ["benchmark may not cover all generation methods", "multimodal focus may dilute text-specific insights"]
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
  "parentUuid": "40fc5df2-6ab3-44eb-a81d-ae8b0789fa13",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "811baeea-a2fa-4357-ae4d-2b1e7ae11cc8",
  "sourceToolAssistantUUID": "40fc5df2-6ab3-44eb-a81d-ae8b0789fa13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T14:54:45.362Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RS7pm5dmzdNQE6X6twJUSz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/tulchinskii2024_intrinsic_dim.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "811baeea-a2fa-4357-ae4d-2b1e7ae11cc8",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9b70d45-0b83-4d91-b4a3-71bd3086bc1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 37 · 2026-05-21T14:54:45.367Z_

<details><summary>↩ Tool result · `toolu_01RS7pm5dmzdNQE6X6twJUSz`</summary>

```text
1	paper_key: "tulchinskii2024_intrinsic_dim"
2	title: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"
3	venue: "NeurIPS 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["DetectGPT", "likelihood-based methods", "supervised classifiers"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	    - {name: "cross-domain accuracy", direction: "higher_better"}
11	    - {name: "cross-model accuracy", direction: "higher_better"}
12	  datasets:
13	    - {name: "multi-language text corpora (English, Chinese, etc.)", size: "N/A"}
14	  ablation_dimensions: ["language", "generator model", "text domain", "writer proficiency level"]
15	  training_recipe: {optimizer: "N/A (intrinsic dimension estimation)", lr: "N/A", hardware: "N/A"}
16	  method_family: "geometric / manifold-based detection via intrinsic dimensionality"
17	
18	positioning:
19	  core_claim: "Human texts have intrinsic dimensionality ~9 (alphabet languages) / ~7 (Chinese) while AI texts are ~1.5 lower, providing a language-agnostic, domain-invariant detection signal"
20	  key_results: "Outperforms SOTA in model-agnostic and cross-domain scenarios; stable across languages, domains, and writer proficiency levels"
21	  limitations: ["computational cost of dimension estimation", "may degrade with more human-like models"]
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
  "parentUuid": "e9b70d45-0b83-4d91-b4a3-71bd3086bc1f",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "e3503254-9108-4f8a-81dc-2b4b36cbbec4",
  "sourceToolAssistantUUID": "e9b70d45-0b83-4d91-b4a3-71bd3086bc1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T14:54:45.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_0167bZzA6KMuHk9CurpQmKuv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/editlens2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3503254-9108-4f8a-81dc-2b4b36cbbec4",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3190c773-3cd5-4802-89e6-909a64d9c68e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 39 · 2026-05-21T14:54:45.843Z_

<details><summary>↩ Tool result · `toolu_0167bZzA6KMuHk9CurpQmKuv`</summary>

```text
1	paper_key: "editlens2026"
2	title: "EditLens: Quantifying the Extent of AI Editing in Text"
3	venue: "ICLR 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["binary AI detectors (GPTZero, etc.)", "ternary classifiers"]
8	  metrics:
9	    - {name: "F1 (binary)", direction: "higher_better"}
10	    - {name: "F1 (ternary)", direction: "higher_better"}
11	    - {name: "regression correlation", direction: "higher_better"}
12	  datasets:
13	    - {name: "human-AI mixed editing dataset", size: "N/A"}
14	    - {name: "Grammarly editing data", size: "N/A"}
15	  ablation_dimensions: ["editing extent (continuous)", "similarity metric choice", "human annotation agreement"]
16	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
17	  method_family: "regression-based continuous AI editing quantification"
18	
19	positioning:
20	  core_claim: "First to formalize AI editing detection as continuous regression rather than binary/ternary classification, achieving SOTA on both classification and regression tasks"
21	  key_results: "Binary F1=94.7%, ternary F1=90.4%; validated against human annotators; practical Grammarly case study"
22	  limitations: ["requires original human text for metric validation", "continuous scoring may be hard to interpret"]
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
  "parentUuid": "3190c773-3cd5-4802-89e6-909a64d9c68e",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "a25a816b-030e-456d-b949-b2b2544aae4b",
  "sourceToolAssistantUUID": "3190c773-3cd5-4802-89e6-909a64d9c68e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T14:54:46.303Z_

<details open><summary>🔧 Tool call — Read · `toolu_012yyjzYB5VyEaX3xoPrfYeF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/cloc2025.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a25a816b-030e-456d-b949-b2b2544aae4b",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "477587cb-874f-4805-bb3d-23707b4d90fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 41 · 2026-05-21T14:54:46.309Z_

<details><summary>↩ Tool result · `toolu_012yyjzYB5VyEaX3xoPrfYeF`</summary>

```text
1	paper_key: "cloc2025"
2	title: "CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss"
3	venue: "CVPR 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard contrastive learning", "ordinal regression methods", "cross-entropy classification"]
8	  metrics:
9	    - {name: "MAE (mean absolute error)", direction: "lower_better"}
10	    - {name: "classification accuracy", direction: "higher_better"}
11	  datasets:
12	    - {name: "Adience (age estimation)", size: "N/A"}
13	    - {name: "Historical Colour Image Dating", size: "N/A"}
14	    - {name: "Knee Osteoarthritis", size: "N/A"}
15	    - {name: "Indian Diabetic Retinopathy Image", size: "N/A"}
16	    - {name: "Breast Carcinoma Subtyping", size: "N/A"}
17	  ablation_dimensions: ["margin type", "number of margins", "contrastive pair selection"]
18	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
19	  method_family: "contrastive learning for ordinal classification"
20	
21	positioning:
22	  core_claim: "Multi-margin N-pair loss enables flexible decision boundaries across adjacent ordinal categories, preserving class ordering while reducing overfitting to training bias"
23	  key_results: "Outperforms existing ordinal classification methods on 5 real-world datasets"
24	  limitations: ["image-focused evaluation", "limited to moderate number of ordinal classes"]
25	  relation_to_us: "complementary"
26	
27	narrative: "N/A"
28	figures: "N/A"
29	tables: "N/A"
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "477587cb-874f-4805-bb3d-23707b4d90fa",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "4d95b45c-c4eb-446d-aa4b-75f4c56b495c",
  "sourceToolAssistantUUID": "477587cb-874f-4805-bb3d-23707b4d90fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T14:54:46.773Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TaDPZTf8EwcQadvFJk25uB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/qurating2024.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d95b45c-c4eb-446d-aa4b-75f4c56b495c",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "918a602a-6979-4f9e-aa3c-5db7b5e72089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 43 · 2026-05-21T14:54:46.779Z_

<details><summary>↩ Tool result · `toolu_01TaDPZTf8EwcQadvFJk25uB`</summary>

```text
1	paper_key: "qurating2024"
2	title: "QuRating: Selecting High-Quality Data for Training Language Models"
3	venue: "ICML 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["uniform random sampling", "perplexity-based filtering"]
8	  metrics:
9	    - {name: "perplexity", direction: "lower_better"}
10	    - {name: "in-context learning accuracy", direction: "higher_better"}
11	    - {name: "training efficiency (steps to target)", direction: "lower_better"}
12	  datasets:
13	    - {name: "260B token pre-training corpus", size: "260B tokens"}
14	    - {name: "30B token subsets sampled by quality", size: "30B tokens"}
15	  ablation_dimensions: ["quality dimension (writing style, expertise, facts, educational value)", "quality threshold", "quality-diversity balance"]
16	  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "1.3B parameter LMs"}
17	  method_family: "LLM-based data quality rating for pre-training data selection"
18	
19	positioning:
20	  core_claim: "LLMs can learn quality ratings from pairwise judgments across 4 dimensions, and training on educational-value-selected data matches uniform sampling with 50% fewer steps"
21	  key_results: "Educational value selection most impactful; quality-diversity balance is critical; 1.3B models trained on 30B quality-filtered tokens"
22	  limitations: ["limited to 1.3B scale", "quality dimensions may not cover all aspects"]
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
  "parentUuid": "918a602a-6979-4f9e-aa3c-5db7b5e72089",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "2dc0143f-30d5-4823-a2d5-3e65c8872c4d",
  "sourceToolAssistantUUID": "918a602a-6979-4f9e-aa3c-5db7b5e72089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T14:54:47.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VE4MYUfRUiZpBs3mzmQtBv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mitchell2023_detectgpt.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dc0143f-30d5-4823-a2d5-3e65c8872c4d",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5d5cb5f-e0e9-4394-a8dc-43f5891b8f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 45 · 2026-05-21T14:54:47.712Z_

<details><summary>↩ Tool result · `toolu_01VE4MYUfRUiZpBs3mzmQtBv`</summary>

```text
1	paper_key: "mitchell2023_detectgpt"
2	title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
3	venue: "ICML 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["likelihood thresholding", "entropy-based methods", "supervised classifiers (RoBERTa)"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	  datasets:
11	    - {name: "XSum", size: "N/A"}
12	    - {name: "SQuAD", size: "N/A"}
13	    - {name: "WritingPrompts", size: "N/A"}
14	    - {name: "fake news (GPT-NeoX generated)", size: "N/A"}
15	  ablation_dimensions: ["perturbation model", "number of perturbations", "source model size"]
16	  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
17	  method_family: "zero-shot detection via log probability curvature"
18	
19	positioning:
20	  core_claim: "Machine-generated text occupies negative curvature regions of the source model's log probability function, enabling detection without training a classifier"
21	  key_results: "GPT-NeoX 20B fake news: AUROC 0.81 → 0.95 vs strongest baseline"
22	  limitations: ["requires perturbation model (slow)", "requires white-box or proxy model access", "short texts challenging"]
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
  "parentUuid": "d5d5cb5f-e0e9-4394-a8dc-43f5891b8f13",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "c5ea63b2-d1ab-4ec7-adf2-b9eaaf9585ae",
  "sourceToolAssistantUUID": "d5d5cb5f-e0e9-4394-a8dc-43f5891b8f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T14:54:48.336Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LYsQGYmQBowW2yhf9Kp9WY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/shi2025_closer_look.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5ea63b2-d1ab-4ec7-adf2-b9eaaf9585ae",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "968b3476-d59b-4e15-a95e-dfcc049f608a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 47 · 2026-05-21T14:54:48.350Z_

<details><summary>↩ Tool result · `toolu_01LYsQGYmQBowW2yhf9Kp9WY`</summary>

```text
1	paper_key: "shi2025_closer_look"
2	title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
3	venue: "NeurIPS 2025 (Spotlight)"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Vanilla replace paradigm (train on synthetic data only)"
9	    - "Vanilla accumulate-subsample paradigm (uniform subsampling from real + all synthetic)"
10	    - "Unconditional DDPM generation"
11	    - "Classifier-Free Guidance (CFG, scale=2)"
12	  metrics:
13	    - {name: "Generalization Score (GS)", direction: "higher_better", definition: "Average L2 distance in DINOv2 feature space between each generated image and its nearest training neighbor"}
14	    - {name: "FID (Frechet Inception Distance)", direction: "lower_better", definition: "InceptionV3-based distribution distance"}
15	    - {name: "Estimated Entropy (Kozachenko-Leonenko)", direction: "higher_better", definition: "KL entropy estimator with gamma=1 on DINOv2 features"}
16	  datasets:
17	    - {name: "CIFAR-10", size: "32,768 images (32x32)", note: "Also used nested subsets: 1024/2048/4096/8192/16384/32768"}
18	    - {name: "FFHQ", size: "8,192 images (downsampled to 32x32)"}
19	    - {name: "MNIST", size: "12,000 images"}
20	  ablation_dimensions:
21	    - "Dataset size (1024 to 32768 in powers of 2)"
22	    - "Training paradigm (replace vs accumulate-subsample)"
23	    - "Selection method (Greedy Selection vs Threshold Decay Filter vs vanilla)"
24	    - "Number of generated candidates (N vs 2N before selection)"
25	    - "Threshold decay rate alpha (sensitivity analysis)"
26	    - "Classifier-Free Guidance scale"
27	    - "Entropy vs variance as correlation target"
28	  training_recipe:
29	    model: "UNet-based DDPM (~16-19M parameters)"
30	    optimizer: "Adam"
31	    lr: "1e-4"
32	    weight_decay: "1e-6"
33	    batch_size: 128
34	    precision: "FP16 mixed"
35	    diffusion_steps: 1000
36	    epochs_cifar: 500
37	    epochs_ffhq: 1000
38	    hardware: "Single NVIDIA A100 GPU"
39	    feature_extractor: "DINOv2 (for distance/entropy computation)"
40	    unet_channels_cifar_ffhq: "[48, 48, 96, 96, 144, 144] with 6 down/up blocks"
41	    unet_channels_mnist: "[64, 128, 256, 512] with 4 down/up blocks"
42	  method_family: "Entropy-based data selection for mitigating model collapse in iterative generative training"
43	
44	positioning:
45	  core_claim: "Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by training data entropy shrinkage, not just variance collapse — and entropy-based data selection can effectively delay this transition."
46	  key_results: >
47	    Pearson r=0.91 between training data entropy and log(generalization score), dataset-size-independent.
48	    FFHQ accumulate-subsample: vanilla FID=75.7 vs Greedy Selection FID=44.7 at iteration 8.
49	    MNIST CFG: vanilla CFG FID=66.2 vs CFG+filtering FID=22.4 at iteration 8.
50	    Greedy Selection preferentially retains real data (65% real by iteration 8 vs 12.5% uniform baseline).
51	  limitations:
52	    - "No rigorous theoretical explanation for why entropy collapses — only empirical demonstration"
53	    - "Limited to image diffusion models; no validation on language models or discrete diffusion"
54	    - "Greedy Selection is computationally expensive (quadratic in dataset size)"
55	    - "Only tested on 32x32 resolution images with relatively small models (~16-19M params)"
56	    - "No formal analysis of how many iterations can be sustained before memorization"
57	  relation_to_us: "foundation"
58	
59	narrative:
60	  story_type: "突破局限型"
61	  hook: >
62	    Opens with the practical inevitability of synthetic data contamination: as diffusion models flood
63	    the internet with generated content, future training sets will inevitably contain synthetic data,
64	    creating a self-consuming loop. This is a real-world crisis framing, not hypothetical.
65	  tension: >
66	    Existing perspectives on model collapse (variance shrinkage, distribution shift) are shown to be
67	    theoretically valid but practically insufficient — variance collapse requires "an extremely large
68	    number of iterations" to manifest, making it "rarely a practical concern." This creates a gap:
69	    the community has mathematical frameworks that don't explain what practitioners actually observe.
70	  key_insight: >
71	    Revealed in paragraph 3 of the intro: the transition from generalization to memorization is the
72	    true practical manifestation of collapse. Models don't just get worse — they specifically lose the
73	    ability to generate novel content and start copying training data. The entropy of the training set
74	    (not the model) is the key diagnostic signal, with r=0.91 correlation to generalizability.
75	  argument_chain: >
76	    Real-world synthetic data contamination is inevitable →
77	    Existing collapse perspectives miss practical manifestations →
78	    We observe a generalization-to-memorization transition (Finding I) →
79	    Training data entropy shrinks across iterations (Finding II) →
80	    Entropy strongly correlates with generalization capability (Finding III, r=0.91) →
81	    Entropy-based data selection preserves diversity and delays collapse →
82	    Validated across 3 datasets, 2 paradigms, with CFG extension
83	  contribution_framing: >
84	    Three numbered contributions, each one sentence. Pattern: identify phenomenon → investigate
85	    driving factor → propose and validate mitigation. Clean problem-insight-solution structure.
86	    Contributions are framed as empirical discoveries rather than theoretical claims, matching the
87	    paper's predominantly experimental nature.
88	  intro_structure: >
89	    3 paragraphs + "Our Contributions" subsection.
90	    P1: Problem context — synthetic data proliferation and the self-consuming loop threat.
91	    P2: Critique of existing perspectives — variance collapse and distribution shift are insufficient.
92	    P3: Their perspective — generalization-to-memorization transition, entropy as diagnostic, proposed mitigation.
93	    Contributions: 3 numbered items following identify-investigate-propose pattern.
94	  notable_technique: >
95	    The paper uses a "practical insufficiency" argument to distinguish itself from prior theoretical
96	    work. Instead of claiming predecessors are wrong, it argues they are right but miss what matters
97	    in practice. This is a diplomatically effective positioning that avoids direct conflict while
98	    establishing clear novelty. The visual pairing of generated images with their nearest training
99	    neighbors (Figure 2 left) makes the abstract concept of "memorization" viscerally obvious.
100	
101	figures:
102	  figure_count: 9
103	  figure1:
104	    type: "method_overview"
105	    description: >
106	      Three-row pipeline diagram. Top row (green background): "Collapse Iteration" showing the
107	      replace paradigm where D1 → Training → M1 → Sampling → D2 → Training → M2 → ... → Dn.
108	      Middle row (blue background): "Mitigated Iteration" showing the accumulate-subsample paradigm
109	      with a pie chart merging real data and previously generated data, plus a funnel icon for
110	      "Selection" before constructing D2. Bottom right (orange background): "Evolution" panel showing
111	      pairs of generated images (top) and their nearest training counterparts (bottom) at Iterations
112	      1, 3, and n, with a horizontal arrow from "Generalization" to "Memorization" and "Degradation"
113	      labels between iteration pairs.
114	    narrative_role: >
115	      Serves as the roadmap for the entire paper: defines the two paradigms (collapse vs mitigated),
116	      introduces the selection intervention, and previews the core finding (generalization-to-memorization
117	      transition) — all in one figure. The reader immediately grasps the problem, the setup, and the
118	      paper's contribution.
119	    design_elements:
120	      - "Color-coded rows: green=collapse, blue=mitigated, orange=evolution"
121	      - "Pipeline arrows connecting dataset→model→sampling→dataset"
122	      - "Pie chart for data composition (real vs synthetic)"
123	      - "Funnel icon for selection step"
124	      - "Real face image pairs showing degradation progression"
125	      - "Horizontal arrow from Generalization to Memorization"
126	    visual_style: >
127	      Clean horizontal flow with three visually distinct rows. Pastel background colors (green,
128	      blue, orange) separate conceptual layers. Neural network icons for models, cylindrical icons
129	      for datasets. The bottom-right evolution panel uses real face images to ground the abstract
130	      pipeline in concrete visual evidence. Legend in bottom-left defines notation.
131	  result_figures:
132	    - figure_id: "Figure 2"
133	      viz_type: "qualitative_comparison + line_plot"
134	      what_compared: "Generated images vs their nearest training neighbors across iterations 1, 3, 8; GS decay curves for 6 dataset sizes"
135	      how_gain_highlighted: "Left panel shows progressive visual convergence (memorization). Right panel uses color-coded curves with labeled 'Generalization Regime' and 'Memorization Regime' regions."
136	      design_note: >
137	        Powerful dual-panel design: qualitative evidence (left) paired with quantitative curves (right).
138	        The image grid makes memorization viscerally obvious — generated faces become identical to
139	        training neighbors. The right panel uses a horizontal dashed line to separate regimes and
140	        annotated text labels for the two regions. Six dataset sizes in distinct colors show the
141	        dataset-size effect on collapse rate. Log-scale y-axis on GS.
142	    - figure_id: "Figure 4a"
143	      viz_type: "scatter"
144	      what_compared: "Estimated entropy (x-axis) vs generalization score (y-axis, log scale) across 6 dataset sizes"
145	      how_gain_highlighted: "Red dashed regression line through all points from all dataset sizes, demonstrating r=0.91 universal correlation. Points from different sizes align on the same line."
146	      design_note: >
147	        The key evidence figure. Log-scale y-axis linearizes the relationship. Color coding by dataset
148	        size (same palette as Figure 2) shows that different sizes fall on the same line — establishing
149	        a dataset-size-independent law. Clean white background, no clutter. Contrast with Figure 4b
150	        (variance) where the correlation is visibly weaker.
151	    - figure_id: "Figure 5"
152	      viz_type: "multi_panel_line_plot"
153	      what_compared: "Generalization Score over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter, across datasets and paradigms"
154	      how_gain_highlighted: "Three lines per panel; selection methods consistently above vanilla, showing sustained higher GS"
155	      design_note: "6 subfigures in a grid (datasets x paradigms). Independent y-axes per subfigure to show relative improvement. Clean legend with three line styles."
156	    - figure_id: "Figure 6"
157	      viz_type: "multi_panel_line_plot"
158	      what_compared: "FID over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter"
159	      how_gain_highlighted: "Selection methods consistently lower FID curves than vanilla across all panels"
160	      design_note: "Same grid layout as Figure 5 for parallel reading. FID improvement most dramatic on accumulate-subsample paradigm."
161	    - figure_id: "Figure 8"
162	      viz_type: "stacked_bar_chart_with_overlay_line"
163	      what_compared: "Proportion of selected images from each iteration source; blue bars = real data proportion vs red 1/n baseline line"
164	      how_gain_highlighted: "Blue bars (real data fraction) dramatically exceed the red 1/n line, especially in later iterations — the method naturally discovers that real data is more diverse"
165	      design_note: >
166	        Insightful visualization of an emergent behavior: the selection algorithm was not told to prefer
167	        real data, but the entropy-maximizing objective naturally selects more real images as synthetic
168	        data clusters tighten. The stacked bars show composition while the overlay line shows the
169	        null expectation. Multiple panels for different datasets/methods.
170	    - figure_id: "Figure 9"
171	      viz_type: "qualitative_comparison + line_plot"
172	      what_compared: "MNIST generation: unconditional (FID=74.4) vs CFG (FID=66.2) vs CFG+filtering (FID=22.4)"
173	      how_gain_highlighted: "Side-by-side digit grids show dramatic quality improvement; entropy plot shows filtering maintains diversity that CFG alone destroys"
174	      design_note: "Extension experiment demonstrating generality beyond unconditional setting. The 3x improvement in FID (66.2→22.4) is a compelling headline number."
175	  ablation_figures:
176	    - figure_id: "Figure 3"
177	      viz_type: "line_plot + 2D_scatter_projection"
178	      dimensions_varied: ["iteration number", "dataset entropy"]
179	      design_note: >
180	        Three-panel figure. Left: entropy decay curves over iterations for different dataset sizes.
181	        Middle and Right: 2D SVD projections of data distribution at iteration 1 (spread) vs
182	        iteration 21 (collapsed into tight clusters). The SVD projections make entropy collapse
183	        visually intuitive — you can see the distribution concentrating.
184	    - figure_id: "Figure 7"
185	      viz_type: "multi_panel_line_plot"
186	      dimensions_varied: ["selection method", "training paradigm", "dataset"]
187	      design_note: "Shows that selection methods maintain higher entropy across iterations. Same grid layout as Figures 5-6 for parallel comparison. Entropy serves as the mechanistic explanation for why GS and FID improve."
188	    - figure_id: "Figure 4b"
189	      viz_type: "scatter"
190	      dimensions_varied: ["variance vs generalization score as alternative to entropy"]
191	      design_note: "Deliberately placed next to Figure 4a to show that variance is a weaker predictor than entropy. The scatter is visibly more dispersed, making the entropy superiority obvious without needing statistics."
192	  figure_narrative_role: >
193	    Figure 1 (pipeline overview + generalization-to-memorization preview) →
194	    Figure 2 (Finding I: generalization-to-memorization transition, qualitative + quantitative) →
195	    Figure 3 (Finding II: entropy shrinkage + distribution collapse visualization) →
196	    Figure 4 (Finding III: entropy-GS correlation, the key evidence; entropy vs variance comparison) →
197	    Figures 5-7 (Mitigation results: GS/FID/entropy improvements with selection methods, parallel grid layout) →
198	    Figure 8 (Mechanistic insight: selection naturally prefers real data) →
199	    Figure 9 (Extension: CFG setting on MNIST).
200	    The flow follows a clear discover-understand-mitigate-extend arc.
201	
202	tables:
203	  table_count: 0
204	  main_result_table:
205	    table_id: "N/A"
206	    row_axis: "N/A"
207	    col_axis: "N/A"
208	    row_organization: "N/A"
209	    col_organization: "N/A"
210	    highlight_strategy: "N/A"
211	    statistical_reporting: "N/A"
212	    num_baselines: 0
213	    design_note: >
214	      Notable design choice: this paper has NO tables in the main text. All quantitative results
215	      are presented as line plots (Figures 5-7) and scatter plots (Figure 4). This is unusual for
216	      a NeurIPS paper but works because the key story is about trends over iterations (naturally
217	      suited to line plots) rather than point comparisons across methods. The absence of tables
218	      keeps the paper visually unified around its "curves over iterations" motif.
219	  ablation_tables:
220	    - table_id: "N/A (Appendix C)"
221	      what_varied: ["Number of generated candidates (N vs 2N)", "Threshold decay rate alpha"]
222	      variation_style: "Presented as figures/plots rather than tables"
223	      design_note: "Ablations are in the appendix and use the same figure-based presentation as the main paper."
224	  supplementary_tables:
225	    in_appendix: false
226	    content: "No tables even in appendix; all results presented as multi-panel line plots and scatter plots"
227	    reason: >
228	      The paper's central argument is about trajectories over iterations, not about static
229	      method-vs-method comparisons. Line plots naturally show this temporal evolution, making
230	      tables unnecessary. The only potential table content (FID/GS at specific iterations) is
231	      embedded in figure panels instead.
232	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "968b3476-d59b-4e15-a95e-dfcc049f608a",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "51c83084-c700-497d-8293-d8edaae3c379",
  "sourceToolAssistantUUID": "968b3476-d59b-4e15-a95e-dfcc049f608a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T14:54:48.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_013VTXdKVD1LQNYu7LMkPpic`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/wu2025_detection_survey.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51c83084-c700-497d-8293-d8edaae3c379",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11b7ecd1-6a98-475b-b98f-df125d7bd69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 49 · 2026-05-21T14:54:48.702Z_

<details><summary>↩ Tool result · `toolu_013VTXdKVD1LQNYu7LMkPpic`</summary>

```text
1	paper_key: "wu2025_detection_survey"
2	title: "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions"
3	venue: "Computational Linguistics, Vol. 51, Issue 1, 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["N/A (survey paper)"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	    - {name: "F1", direction: "higher_better"}
11	    - {name: "TPR@FPR", direction: "higher_better"}
12	  datasets:
13	    - {name: "various detection benchmarks surveyed", size: "N/A"}
14	  ablation_dimensions: ["method family (watermarking/statistical/neural/human-assisted)", "evaluation setting (in-domain/cross-domain/cross-model)", "attack type"]
15	  training_recipe: {optimizer: "N/A (survey)", lr: "N/A", hardware: "N/A"}
16	  method_family: "survey covering watermarking, statistics-based, neural-based, and human-assisted detection"
17	
18	positioning:
19	  core_claim: "Comprehensive taxonomy of LLM text detection methods organized into 4 families, with analysis of challenges including OOD generalization, adversarial attacks, and evaluation framework deficiencies"
20	  key_results: "Identifies key gaps: OOD robustness, attack resilience, real-world data handling, lack of standardized evaluation"
21	  limitations: ["survey scope limited to text modality", "rapidly evolving field"]
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
  "parentUuid": "11b7ecd1-6a98-475b-b98f-df125d7bd69a",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "de3a0e55-1b9a-4aca-946b-159ceb7da6af",
  "sourceToolAssistantUUID": "11b7ecd1-6a98-475b-b98f-df125d7bd69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T14:54:49.126Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YTDvdmutyiH4EVRTpkzdZu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/kirchenbauer2023_watermark.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de3a0e55-1b9a-4aca-946b-159ceb7da6af",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d42bcdaf-0409-4c1a-8d46-b401b9eae921",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 51 · 2026-05-21T14:54:49.133Z_

<details><summary>↩ Tool result · `toolu_01YTDvdmutyiH4EVRTpkzdZu`</summary>

```text
1	paper_key: "kirchenbauer2023_watermark"
2	title: "A Watermark for Large Language Models"
3	venue: "ICML 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["no watermark baseline", "post-hoc detection methods"]
8	  metrics:
9	    - {name: "p-value (watermark detection)", direction: "lower_better"}
10	    - {name: "text quality (perplexity)", direction: "lower_better"}
11	    - {name: "BLEU/ROUGE (quality preservation)", direction: "higher_better"}
12	  datasets:
13	    - {name: "OPT model outputs", size: "N/A"}
14	  ablation_dimensions: ["green list fraction", "watermark strength (delta)", "text length", "model size"]
15	  training_recipe: {optimizer: "N/A (decoding-time watermark)", lr: "N/A", hardware: "OPT multi-billion parameter models"}
16	  method_family: "statistical watermarking via green token promotion"
17	
18	positioning:
19	  core_claim: "Invisible watermarks can be embedded in LLM outputs by promoting 'green' tokens during generation, detectable from short spans without model access, with negligible quality impact"
20	  key_results: "Algorithmically detectable watermark with interpretable p-values; tested on OPT models; information-theoretic sensitivity analysis"
21	  limitations: ["vulnerable to paraphrasing attacks", "requires control of generation process", "green token bias may affect specific domains"]
22	  relation_to_us: "orthogonal"
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
  "parentUuid": "d42bcdaf-0409-4c1a-8d46-b401b9eae921",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "57bedf62-25c3-4cf8-a4fb-41172865fd24",
  "sourceToolAssistantUUID": "d42bcdaf-0409-4c1a-8d46-b401b9eae921",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-21T14:54:49.611Z_

<details open><summary>🔧 Tool call — Read · `toolu_0144bxqT84TmR7cZxiDD2Dee`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2025_strong_collapse.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57bedf62-25c3-4cf8-a4fb-41172865fd24",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuWmhVEUL3S3JbNJE8j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5230ec9-1df9-4f37-9053-99fe727ce1a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWvtsHfYo1RpcEEk5XSBWY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 0,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17498,
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

_source line 53 · 2026-05-21T14:54:49.626Z_

<details><summary>↩ Tool result · `toolu_0144bxqT84TmR7cZxiDD2Dee`</summary>

```text
1	paper_key: "dohmatob2025_strong_collapse"
2	title: "Strong Model Collapse"
3	venue: "ICLR 2025 Spotlight"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Training on pure real/original data (no synthetic contamination)"
9	    - "Training on pure synthetic data"
10	    - "Mixed real+synthetic data with various proportions p2"
11	    - "Weighted single-step mixing (data weighting strategies)"
12	    - "Dynamic multi-step mixing"
13	  metrics:
14	    - {name: "test error (E_test on real distribution)", direction: "lower_better"}
15	    - {name: "test loss (cross-entropy for language modeling)", direction: "lower_better"}
16	    - {name: "collapse term zeta (excess error from synthetic data)", direction: "lower_better"}
17	  datasets:
18	    - {name: "Gaussian synthetic data (random projections)", size: "n=500 samples, variable d"}
19	    - {name: "MNIST", size: "standard 60K/10K, used for regression with two-layer networks"}
20	    - {name: "BabiStories", size: "reproduction of TinyStories via Mixtral-8x7B; token counts up to ~3e10"}
21	  ablation_dimensions:
22	    - "synthetic data proportion p2 (fraction of training data that is synthetic)"
23	    - "model size m (network width for random projections, depth/layers for GPT-2)"
24	    - "synthetic data quality c^2 (distribution mismatch between real and synthetic)"
25	    - "total training set size n (scaling behavior)"
26	    - "parametrization rate psi=m/n (under- vs over-parameterized regime)"
27	    - "interpolation threshold crossing (m=n boundary)"
28	  training_recipe:
29	    optimizer: "not explicitly detailed in accessible text; standard SGD/Adam for neural network experiments"
30	    lr: "not explicitly detailed in accessible text"
31	    hardware: "not explicitly detailed in accessible text"
32	    details: "Random projections on Gaussian data (n=500); two-layer neural networks on MNIST (width m=2000); GPT-2 models (12-layer) on BabiStories; experiments vary p2 and model size systematically"
33	  method_family: "theoretical analysis of model collapse via bias-variance decomposition and operator-valued free probability theory"
34	
35	positioning:
36	  core_claim: "Model collapse persists even when mixing real and synthetic data, as long as the fraction of synthetic data does not vanish asymptotically — establishing a 'strong' form of collapse where no fixed-proportion mixing strategy can prevent performance degradation, and larger models amplify this effect in the under-parameterized regime."
37	  key_results: "E_test = B + V + zeta decomposition where zeta is irreducible collapse term; in scaling laws regime (phi->0+), zeta ~ p2^2 * tr(Delta) remains bounded unless p2->0; 1% synthetic data sufficient to cause collapse plateau; larger models amplify collapse when real/synthetic distributions differ significantly; double-descent pattern where over-parameterized models (past m=n threshold) partially mitigate but do not eliminate collapse"
38	  limitations:
39	    - "Theory focuses on supervised regression with label shifts — does not directly model generative/autoregressive training"
40	    - "Random projections model is a simplified approximation of actual neural networks (linearized regime)"
41	    - "Gaussian feature distribution assumption with diagonal covariance matrices"
42	    - "Proportionate scaling limit assumes d,n,m -> infinity with fixed ratios"
43	    - "For fully-trained neural networks the theory does not directly apply, though authors anticipate general trends hold"
44	    - "Does not address mitigation via data filtering, detection, or curation (only analyzes mixing/weighting)"
45	  relation_to_us: "foundation"
46	
47	narrative:
48	  story_type: "突破局限型"
49	  hook: "Opens with the observation that AI-generated content is increasingly contaminating web training corpora, and asks whether the standard approach of scaling up training data can still work when synthetic data is inevitably mixed in. Frames this as a fundamental threat to the scaling laws paradigm."
50	  tension: "Prior model collapse work showed degradation in recursive (iterative) generation settings, but left open whether strategic mixing of real and synthetic data could prevent collapse. The natural hope is that diluting synthetic data with sufficient real data would restore normal scaling — this paper proves that hope is false."
51	  key_insight: "The key insight is the bias-variance decomposition E_test = B + V + zeta, where zeta is an irreducible collapse term that persists as long as the synthetic data fraction p2 remains fixed (non-vanishing). This means no matter how much you scale total data n, the collapse term does not vanish — you must asymptotically eliminate synthetic data proportion entirely. Revealed through Theorem 1 (linear models) and Theorem 2 (random projections/neural approximation)."
52	  argument_chain: "problem (synthetic data contamination is unavoidable) -> question (can mixing/scaling overcome it?) -> theory (bias-variance decomposition reveals irreducible collapse term zeta) -> scaling law implication (zeta plateaus unless p2->0) -> model size analysis (bigger models amplify collapse below interpolation threshold) -> double-descent (reversal above interpolation threshold but not elimination) -> data mixing strategies (weighted/dynamic mixing cannot fix fundamental issue) -> experimental validation (random projections, MNIST, GPT-2 on BabiStories confirm theory)"
53	  contribution_framing: "Two main results explicitly labeled: Result #1 (Strong Model Collapse) — collapse persists with any fixed synthetic fraction; Result #2 (Model Size and Model Collapse) — bigger models amplify collapse except past interpolation threshold. Followed by experimental validation across three settings (toy, MNIST, language modeling)."
54	  intro_structure: "~5 paragraphs: P1=hook (AI-generated content proliferating in training data), P2=problem framing (model collapse definition and prior work), P3=research questions (can mixing help? does model size matter?), P4=main results summary (Result #1 and #2), P5=experimental validation overview and paper organization. Section 1.1 details contributions, Section 1.2 covers related work."
55	  notable_technique: "The 'strong' vs 'weak' framing is a powerful rhetorical device — it redefines the conversation by showing that even the most optimistic scenario (strategic mixing with fresh real data) still fails. The Pareto diagram (Figure 1) is an effective visual argument that immediately conveys the tradeoff. The paper also uses the mathematical elegance of the exact bias-variance-collapse decomposition to make a clean, falsifiable theoretical claim rather than just empirical observations."
56	
57	figures:
58	  figure_count: 8
59	  figure1:
60	    type: "motivation"
61	    description: "Pareto diagram showing test error on real data distribution: training on mixed data (y-axis) vs training on real data only (x-axis). Points colored by synthetic data quality (c^2) for a random projections model with n=500. Lines show Pareto frontiers for different quality levels. Demonstrates that mixed training always incurs excess error (points above diagonal) and the tradeoff worsens with lower synthetic data quality."
62	    narrative_role: "Immediately establishes the core claim visually — no combination of model size and data mixing achieves the performance of training on real data alone. Sets up the entire paper's argument in one figure."
63	    design_elements: ["Pareto frontier visualization", "diagonal reference line (ideal = no collapse)", "colorbar for parametrization rate psi=m/n", "multiple quality levels compared"]
64	    visual_style: "Scatter plot with Pareto frontiers; colorbar encoding model size; clean 2D layout that maps directly to the central question (mixed vs real-only performance)"
65	  result_figures:
66	    - figure_id: "Figure 3"
67	      viz_type: "line_plot"
68	      what_compared: "Strong model collapse in classical linear model — empirical confirmation of Corollary 1. Shows test error vs training set size for various synthetic data proportions p2, demonstrating that even small p2 causes scaling law plateau."
69	      how_gain_highlighted: "Direct comparison of p2=0 (ideal scaling law) vs p2>0 curves; the plateau/saturation effect is visually stark"
70	      design_note: "Log-log scale makes power-law behavior linear and the collapse plateau clearly visible as a horizontal asymptote; multiple p2 values show graduated severity"
71	    - figure_id: "Figure 4"
72	      viz_type: "line_plot"
73	      what_compared: "Impact of model size (network width m) on model collapse for various data quality levels c^2 and mixing ratios p2"
74	      how_gain_highlighted: "Shows test error as function of model size, revealing the double-descent pattern: collapse worsens up to interpolation threshold m=n, then partially reverses"
75	      design_note: "Multiple panels for different c^2 values; vertical line or inflection at m=n marks the interpolation threshold — the key theoretical prediction"
76	    - figure_id: "Figure 7"
77	      viz_type: "line_plot"
78	      what_compared: "Model collapse on MNIST with two-layer neural network (width m=2000) as function of synthetic data proportion"
79	      how_gain_highlighted: "Validates that theoretical predictions from random projections model transfer to real image data"
80	      design_note: "Bridges the theory-practice gap by testing on a real dataset"
81	    - figure_id: "Figure 8"
82	      viz_type: "line_plot"
83	      what_compared: "GPT-2 (12-layer) language model on BabiStories: (Left) test loss vs number of training tokens for various synthetic data proportions p2; (Right) test loss vs model depth showing larger models initially better but eventually worse"
84	      how_gain_highlighted: "Left panel shows clear scaling law plateau with synthetic contamination; Right panel shows the depth-dependent collapse reversal predicted by theory"
85	      design_note: "Most impactful experimental figure — demonstrates that theoretical predictions generalize to autoregressive language models despite theory being developed for regression"
86	  ablation_figures:
87	    - figure_id: "Figure 2"
88	      viz_type: "schematic_diagram"
89	      dimensions_varied: ["bias B", "variance V", "collapse term zeta"]
90	      design_note: "Illustrates the bias-variance-collapse decomposition E_test = B + V + zeta; shows how c^2 (synthetic data quality) and interpolation threshold m=n interact. Functions as both explanation and ablation — decomposing total error into its components."
91	    - figure_id: "Figure 5"
92	      viz_type: "line_plot"
93	      dimensions_varied: ["model size", "data quality", "mixing proportion"]
94	      design_note: "Shows double-descent curves as function of model parametrization; demonstrates the reversal past interpolation threshold"
95	  figure_narrative_role: "Figure 1 (Pareto motivation: collapse is unavoidable) -> Figure 2 (decomposition: why collapse happens via B+V+zeta) -> Figure 3 (theory validation: linear model confirms plateau) -> Figure 4 (model size: double-descent in collapse) -> Figure 5 (additional theory curves) -> Figure 6-7 (MNIST validation) -> Figure 8 (GPT-2 language model validation). Arc: visual claim -> theoretical mechanism -> toy validation -> model size effects -> real-world validation."
96	
97	tables:
98	  table_count: 0
99	  main_result_table:
100	    note: "This paper contains NO tables. All results are presented through mathematical theorems (Theorem 1, 2, Corollary 1) and scaling curve figures. This is consistent with theoretical ML papers where contributions are equations/bounds rather than benchmark comparisons."
101	  ablation_tables: []
102	  supplementary_tables:
103	    in_appendix: true
104	    content: "Appendices contain proofs (operator-valued free probability theory derivations), additional experimental figures, and experimental setup details (Appendix A.1: random projections hyperparameters, A.2: two-layer neural network configuration, A.3: language modeling training specifics)"
105	    reason: "Theoretical paper — results are best expressed as scaling law equations and their visual verification via figures, not tabular benchmark comparisons"
106	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5230ec9-1df9-4f37-9053-99fe727ce1a6",
  "isSidechain": true,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "agentId": "af75b63db3ca0cde3",
  "type": "user",
  "uuid": "b7712ef7-d1cb-4ff1-a296-e860e8bc8525",
  "sourceToolAssistantUUID": "f5230ec9-1df9-4f37-9053-99fe727ce1a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-21T15:05:05.815Z_

Here are the complete contents of all 25 YAML files:

---

**1. dohmatob2024_demystified.yaml**

```yaml
paper_key: "dohmatob2024_demystified"
title: "Model Collapse Demystified: The Case of Regression"
venue: "NeurIPS 2024"
full_text_available: false

research:
  baselines: ["no-collapse baseline (real data only)", "adaptive regularization"]
  metrics:
    - {name: "test risk / prediction error", direction: "lower_better"}
    - {name: "scaling law exponent", direction: "context_dependent"}
  datasets:
    - {name: "synthetic high-dimensional regression", size: "theoretical"}
  ablation_dimensions: ["number of recursive generations", "spectral decay rate", "source condition", "regularization strength"]
  training_recipe: {optimizer: "closed-form / ridge regression", lr: "N/A", hardware: "theoretical"}
  method_family: "theoretical analysis of model collapse in regression"

positioning:
  core_claim: "Analytic formulae characterizing model collapse in high-dimensional regression reveal modified scaling laws with crossover phenomena from fast to slow rates"
  key_results: "Derived closed-form expressions for collapse dynamics; proposed adaptive regularization as mitigation"
  limitations: ["limited to regression setting", "Gaussian assumptions"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**2. alemohammad2024_mad.yaml**

```yaml
paper_key: "alemohammad2024_mad"
title: "Self-Consuming Generative Models Go MAD"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["real data baseline", "mixed real+synthetic training"]
  metrics:
    - {name: "precision (quality)", direction: "higher_better"}
    - {name: "recall (diversity)", direction: "higher_better"}
    - {name: "FID", direction: "lower_better"}
  datasets:
    - {name: "FFHQ (image generation)", size: "70K"}
    - {name: "MNIST", size: "60K"}
  ablation_dimensions: ["fresh real data ratio", "number of autophagous generations", "quality-diversity tradeoff"]
  training_recipe: {optimizer: "N/A (generative models)", lr: "N/A", hardware: "N/A"}
  method_family: "theoretical + empirical analysis of autophagous (self-consuming) generative loops"

positioning:
  core_claim: "Without sufficient fresh real data in each generation, self-consuming generative models are doomed to have quality or diversity progressively decrease (Model Autophagy Disorder)"
  key_results: "Three regimes identified: fully synthetic → collapse; synthetic+sampling bias → quality loss; synthetic+fresh data → stable if ratio sufficient"
  limitations: ["primarily image domain", "simplified generation pipeline"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**3. drayson2025_detection_prevents_collapse.yaml**

```yaml
paper_key: "drayson2025_detection_prevents_collapse"
title: "Machine-generated text detection prevents language model collapse"
venue: "EMNLP 2025 Findings"
full_text_available: false

research:
  baselines: ["training on purely human data", "training on unfiltered mixed data"]
  metrics:
    - {name: "perplexity", direction: "lower_better"}
    - {name: "text diversity", direction: "higher_better"}
    - {name: "downstream task performance", direction: "higher_better"}
  datasets:
    - {name: "GPT-2 generated text", size: "N/A"}
    - {name: "SmolLM2 generated text", size: "N/A"}
  ablation_dimensions: ["model family (GPT-2 vs SmolLM2)", "model size (124M to 1.7B)", "number of recursive generations", "detection threshold"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "detection-based filtering + importance resampling for collapse prevention"

positioning:
  core_claim: "Using machine-generated text detectors to filter training data not only prevents model collapse but improves performance beyond training on purely human data"
  key_results: "Detection + resampling outperforms both pure human data and unfiltered mixed data across GPT-2 and SmolLM2 families"
  limitations: ["limited model families tested", "relies on detector quality"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**4. bevendorff2025_two_paradigms.yaml**

```yaml
paper_key: "bevendorff2025_two_paradigms"
title: "The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification"
venue: "ACL 2025 Findings"
full_text_available: true

research:
  baselines:
    - "Binoculars (Hans et al., 2024) zero-shot detector"
    - "SVM with TF-IDF word unigrams (800 features)"
    - "LoRA-fine-tuned Mistral-7B binary classifier"
    - "OpenAI RoBERTa-based GPT-2 detector (Solaiman et al., 2019)"
    - "Ghostbuster (Verma et al., 2024)"
    - "GPT-Sentinel (Chen et al., 2023)"
    - "DetectGPT (Mitchell et al., 2023)"
    - "Fast-DetectGPT (Bao et al., 2023)"
    - "DetectLLM (Su et al., 2023a)"
    - "LLMDet (Wu et al., 2023)"
  metrics:
    - {name: "False Negative Rate (FNR)", direction: "lower_better"}
    - {name: "False Positive Rate (FPR)", direction: "lower_better"}
    - {name: "AUROC", direction: "higher_better"}
    - {name: "Accuracy", direction: "higher_better"}
    - {name: "Precision-Recall curve", direction: "higher_better"}
    - {name: "c@1 (accuracy with non-answers)", direction: "higher_better"}
    - {name: "Cohen's d (effect size)", direction: "N/A"}
    - {name: "Character 3-gram entropy (bits)", direction: "N/A"}
    - {name: "MTLD (lexical diversity)", direction: "N/A"}
    - {name: "Flesch reading ease", direction: "N/A"}
    - {name: "Compression-based cosine (CBC)", direction: "lower_better"}
  datasets:
    - {name: "PAN'24 (extended with GPT-4o, 4o-mini, o1)", size: "1,359 human + 23,094 LLM texts, 15 LLMs"}
    - {name: "Human Detectors (HD)", size: "150 human + 150 LLM texts, 5 LLMs"}
    - {name: "Ghostbuster (GB) Essays", size: "994 human + 6,000 LLM texts, 6 LLMs"}
    - {name: "Ghostbuster (GB) Reuters", size: "1,000 human + 6,000 LLM texts, 6 LLMs"}
    - {name: "RAID", size: "153,217 human + 2,443,073 LLM texts, 6 LLMs"}
    - {name: "RAID (no attacks)", size: "12,766 human + 202,593 LLM texts, 6 LLMs"}
    - {name: "M4", size: "59,032 human + 57,253 LLM texts, 7 LLMs"}
    - {name: "MAGE", size: "152,382 human + 284,224 LLM texts, 131 model labels combined into 4 families"}
  ablation_dimensions:
    - "Model family used for training vs. testing (cross-model generalization)"
    - "In-domain vs. out-of-domain evaluation"
    - "Text length cutoffs (entropy analysis at increasing character lengths)"
    - "Feature set size in unmasking (top 250 vs. top 500 n-grams)"
    - "Operating point threshold (accuracy vs. low FPR vs. low FNR)"
    - "Genre-controlled vs. mixed-genre datasets"
    - "Dataset used for training (PAN vs. RAID)"
  training_recipe:
    optimizer: "Not specified for SVM; LoRA fine-tuning for Mistral-7B"
    lr: "Not specified"
    hardware: "3x A100 GPUs for 2x12h (Mistral-7B LoRA, 20M trainable parameters)"
  method_family: "Authorship analytics / computational stylometry applied to LLM detection"

positioning:
  core_claim: "LLM detection is fundamentally an authorship verification (open-set one-class) problem, not an authorship attribution (closed-set binary classification) problem, and conflating the two paradigms explains the contradictory reports of detector success and failure."
  key_results: "SVM in-domain FNR 0-7%, FPR 0-3%; OpenAI o1 is undetectable by non-o1 detectors; Binoculars FPR near zero but fails completely on o1; GPT-4o is first model with entropy consistent with human text beyond 4,000 chars; word length alone yields remarkable detection accuracy on genre-controlled datasets (Cohen's d up to 4.11)"
  limitations:
    - "Key assumption that future LLMs will become increasingly human-like in style could be wrong -- LLMs may converge to a distinct 'mean style' centroid"
    - "Only a limited number of datasets and detectors were analyzed; more experiments needed to corroborate practical implications"
    - "Humans exposed to LLM writing may adopt LLM stylistic properties, creating a feedback loop"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Generative AI is everywhere -- then immediately juxtaposes contradictory evidence: detectors regularly 'beat' benchmarks yet OpenAI shut down their own detector after 6 months citing lack of accuracy."
  tension: "The conflicting reports of success and failure in LLM detection create a puzzle. The paper frames this as a fundamental misunderstanding: researchers build attribution-style detectors but evaluate them under verification assumptions, leading to systematic errors."
  key_insight: "Revealed in Section 3.3 via a scaling thought experiment: as you add more human authors to distinguish from an LLM, the attribution approach fails because the number of humans classified as LLM asymptotically approaches all of humanity. This is exactly what current research does by compiling ever-larger corpora. The insight bridges two previously disconnected communities (authorship analytics and LLM detection)."
  argument_chain: "Contradiction in detector reports -> bridge to authorship analytics (attribution vs verification) -> theoretical argument that attribution cannot scale (Section 3.3) -> empirical evidence that LLM text properties are converging toward human (Section 4, entropy/MTLD/readability) -> detector evaluation confirming attribution works in-domain but fails cross-model especially for o1 (Section 5) -> discussion of benchmark quality and evaluation metric issues (Section 6) -> conclusion that verification framing is necessary"
  contribution_framing: "Four numbered contributions at end of intro: (1) reconcile authorship analytics with LLM detection, showing it is verification; (2) corpus analysis of how LLM text differs from human text; (3) show SOTA detectors solve attribution well; (4) discuss benchmark quality and evaluation needs for verification."
  intro_structure: "4 paragraphs: P1 sets scene (LLM text is everywhere, risks, detector interest); P2 presents the contradiction (detectors beat benchmarks vs. serious concerns, OpenAI shutting down detector); P3 frames the explanation (mix-up of attribution vs verification, bridging two communities, explains why attribution fails at scale); P4 lists four contributions with section pointers."
  notable_technique: "The thought experiment in Section 3.3 is the rhetorical centerpiece -- it takes a simple two-author scenario and iteratively adds authors to show how attribution inherently breaks down. The paper also excels at connecting a 'new' problem (LLM detection) to a well-established field (authorship analytics) that developed independently, making the reader see that the wheel is being reinvented poorly."

figures:
  figure_count: 21
  figure1:
    type: "problem_illustration"
    description: "Mean character 3-gram entropy over increasing text length with 95% confidence intervals across three datasets (PAN'24, RAID, M4). Shows per-model entropy curves diverging from human baseline after ~2,500-4,000 characters."
    narrative_role: "Core empirical evidence that LLM text has lower entropy than human text, but newer models (GPT-4o, o1) are closing the gap -- supporting the verification framing."
    design_elements: ["Multi-panel (a,b,c) by dataset", "Confidence interval shading", "Color-coded per model family", "Human baseline highlighted", "X-axis is text length, Y-axis is entropy"]
    visual_style: "Three-panel line plot with shaded confidence intervals. Clean academic style, models labeled directly on curves. Divergence point visible around 2,500 chars."
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "heatmap"
      what_compared: "FNR and FPR of SVM, Binoculars, and Mistral-7B detectors across training model families (rows) vs test model families (columns)"
      how_gain_highlighted: "Diagonal shows best in-domain performance; o1 row/column visually stands out as failing for all non-o1 detectors"
      design_note: "Complex multi-panel figure (4a-4d) combining heatmaps for SVM cross-model, SVM on PAN, Binoculars on PAN, and Mistral on PAN/RAID. Packs maximum information by varying both training and test conditions."
    - figure_id: "Figure 5 (Appendix A)"
      viz_type: "line_plot"
      what_compared: "ROC vs Precision-Recall curves at different class prevalence ratios (P/N = 0.2 to 5.0)"
      how_gain_highlighted: "Directly shows ROC is invariant to prevalence while precision degrades, supporting the argument that AUROC is misleading"
      design_note: "Side-by-side comparison with color-coded prevalence ratios makes the divergence between ROC and PR curves visually immediate."
    - figure_id: "Figure 6 (Appendix B)"
      viz_type: "box_plot"
      what_compared: "Entropy distributions at 4,500 characters as a discriminator on PAN dataset, per model"
      how_gain_highlighted: "Box spread shows which models are separable from humans on entropy alone"
      design_note: "Single compact figure showing discriminability limits of a simple feature."
    - figure_id: "Figures 7-9 (Appendix D)"
      viz_type: "heatmap"
      what_compared: "AUROC of SVM, Binoculars, and fine-tuned Mistral across all datasets"
      how_gain_highlighted: "Color intensity shows where each detector type succeeds/fails"
      design_note: "Supplements Figure 4 with AUROC values; includes bar charts for per-dataset breakdown."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      dimensions_varied: ["Model (Llama2-70b, GPT-3.5, GPT-4o, OpenAI o1)", "Feature set size (top 250 vs top 500 n-grams)", "Pairing type (Human/Human, LLM/LLM, Human/LLM)"]
      design_note: "8-panel grid (4 models x 2 feature sizes) showing unmasking curves with IQR shading. Reveals that older models are 'inconsistently' discriminable (high in top-250 but low in top-500), while newer models like o1 are more consistent -- key evidence for the verification argument."
    - figure_id: "Figures 18-19 (Appendix G)"
      viz_type: "line_plot"
      dimensions_varied: ["All 10 model families on PAN'24", "HD dataset models"]
      design_note: "Extended unmasking curves for all models, supplementing Figure 3's selected models."
    - figure_id: "Figures 20-21 (Appendix G)"
      viz_type: "density_plot"
      dimensions_varied: ["Compression-based cosine (CBC) score distributions across model pairings"]
      design_note: "KDE density plots showing CBC score separation between same-author and cross-author pairs."
  figure_narrative_role: "Figure 1 (entropy divergence) -> Figure 2 (human entropy varies by genre) -> Figure 3 (unmasking reveals inconsistency in older LLMs vs consistency in newer ones) -> Figure 4 (detector evaluation confirms attribution works in-domain but fails cross-model). Appendix figures (5-21) provide exhaustive supporting evidence for each main-text claim. The flow is: statistical properties of text -> stylometric analysis -> detector performance."

tables:
  table_count: 6
  main_result_table:
    table_id: "N/A -- this paper primarily uses figures (heatmaps/line plots) for main results rather than traditional result tables"
    row_axis: "N/A"
    col_axis: "N/A"
    row_organization: "N/A"
    col_organization: "N/A"
    highlight_strategy: "N/A"
    statistical_reporting: "t-tests with Cohen's d effect sizes reported inline in text; Bonferroni correction for multiple comparisons"
    num_baselines: 3
    design_note: "Unusual for the field: main results are presented as heatmap figures (Figure 4) rather than tables. This is a deliberate choice that makes cross-model generalization patterns visually immediate. Statistical tests are reported inline rather than in tables."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Tables 1-5 in appendix contain qualitative examples of low-quality/short texts from RAID, MAGE, M4, and BLOOMz datasets. Table 6 provides dataset statistics (text counts, human/LLM splits, number of LLMs per dataset)."
    reason: "Tables are used for qualitative evidence (bad data examples) and dataset metadata rather than quantitative results. All quantitative comparisons use figures. This split reflects the paper's emphasis on data quality critique -- the appendix tables serve as 'exhibit evidence' for the argument that benchmarks are flawed."
```

---

**5. synthetic_eggs2026.yaml**

```yaml
paper_key: "synthetic_eggs2026"
title: "Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning"
venue: "ACL 2026 Findings"
full_text_available: false

research:
  baselines: ["human data fine-tuning", "single-source synthetic fine-tuning", "multi-source synthetic fine-tuning"]
  metrics:
    - {name: "distribution collapse measures", direction: "lower_better"}
    - {name: "adversarial robustness", direction: "higher_better"}
    - {name: "self-preference bias", direction: "lower_better"}
    - {name: "output quality", direction: "higher_better"}
    - {name: "text diversity", direction: "higher_better"}
  datasets:
    - {name: "synthetic data from multiple LLM sources", size: "N/A"}
  ablation_dimensions: ["number of source models", "human vs synthetic ratio", "source model diversity"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "synthetic data diversity analysis for fine-tuning"

positioning:
  core_claim: "Fine-tuning on diverse multi-source synthetic data mitigates distribution collapse while preserving output distribution breadth, but adversarial robustness decreases"
  key_results: "Multi-source synthetic > single-source for distribution collapse; human data best for reducing self-preference bias; synthetic data yields higher quality but lower robustness"
  limitations: ["limited to fine-tuning (not pre-training)", "specific LLM families"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**6. li2024_mage.yaml**

```yaml
paper_key: "li2024_mage"
title: "MAGE: Machine-generated Text Detection in the Wild"
venue: "ACL 2024"
full_text_available: true

research:
  baselines:
    - "Longformer (PLM-based classifier)"
    - "GLTR (GPT-2-XL + logistic regression)"
    - "FastText (word bi-gram features)"
    - "DetectGPT (zero-shot, T5-3B mask infill + GPT-J-6B scoring)"
    - "Human annotators"
    - "ChatGPT querying"
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "AvgRec (average of HumanRec and MachineRec)", direction: "higher_better"}
    - {name: "HumanRec (human text recall)", direction: "higher_better"}
    - {name: "MachineRec (machine text recall)", direction: "higher_better"}
  datasets:
    - {name: "MAGE testbed (custom)", size: "95,596 human + 236,554 machine-generated texts from 7 domains x 27 LLMs"}
    - {name: "Reddit ChangeMyView", size: "804 opinion statements"}
    - {name: "Yelp", size: "1,000 reviews"}
    - {name: "XSum", size: "1,000 news articles"}
    - {name: "TLDR", size: "777 news summaries"}
    - {name: "ELI5", size: "1,000 QA pairs"}
    - {name: "Reddit WritingPrompts", size: "1,000 stories"}
    - {name: "ROCStories", size: "1,000 stories"}
    - {name: "HellaSwag", size: "1,000 commonsense reasoning"}
    - {name: "SQuAD (Wikipedia)", size: "1,000 paragraphs"}
    - {name: "SciXGen", size: "1,000 scientific abstracts"}
    - {name: "CNN/DailyMail (frontier test)", size: "used in Testbed 7"}
    - {name: "DialogSum (frontier test)", size: "used in Testbed 7"}
    - {name: "PubMedQA (frontier test)", size: "used in Testbed 7"}
    - {name: "IMDb (frontier test)", size: "used in Testbed 7"}
  ablation_dimensions:
    - "In-distribution vs out-of-distribution (8 testbed scenarios)"
    - "Fixed-domain vs arbitrary-domain"
    - "Model-specific vs arbitrary-model"
    - "Unseen models (cross-validation over 7 model groups)"
    - "Unseen domains (cross-validation over 10 domains)"
    - "Decision boundary adjustment (0.1% in-domain data)"
    - "Paraphrasing attack robustness (gpt-3.5-turbo)"
    - "Prompt type (continuation vs topical vs specified)"
    - "PLM backbone comparison"
    - "Data balance effects"
    - "Randomness analysis"
  training_recipe:
    optimizer: "Adam"
    lr: "0.005"
    dropout: "0.1"
    epochs: "5"
    hardware: "8x V100 GPUs"
    validation_metric: "classification accuracy"
    gltr_lm: "GPT-2-XL"
    gltr_classifier: "logistic regression (scikit-learn, grid search)"
    fasttext_epochs: "100"
    detectgpt_mask_model: "T5-3B"
    detectgpt_scoring_model: "GPT-J-6B"
    detectgpt_mask_rate: "15%"
    detectgpt_perturbations: "100"
  method_family: "PLM-based binary classification (Longformer) + statistical/zero-shot baselines for machine-generated text detection"

positioning:
  core_claim: "First comprehensive 'in-the-wild' testbed for machine-generated text detection spanning 7 domains and 27 LLMs, revealing that perplexity is a double-edged sword — it enables clustering but causes systematic false positives on low-perplexity human text."
  key_results: "Longformer achieves AUROC 0.99 in-distribution but drops to 0.95 on unseen models and 0.93 on unseen domains; with 0.1% boundary adjustment data, achieves 86.54% AvgRec on unseen domains + unseen model (GPT-4); paraphrasing attacks degrade AUROC to 0.75."
  limitations:
    - "Limited model coverage — new LLMs (Alpaca, Vicuna, etc.) continuously emerge and the testbed cannot keep up"
    - "Benchmark data bias — source texts may overlap with LLM pretraining data, so detection performance may not transfer to truly novel online text"
    - "Vulnerability to paraphrasing attacks (AvgRec drops to 62.92% even with boundary adjustment)"
    - "Perplexity bias causes systematic misclassification of low-perplexity human texts as machine-generated"
  relation_to_us: "competitor"

narrative:
  story_type: "突破局限型"
  hook: "LLMs have achieved human-level text generation, creating urgent need for detection — but existing detection research only evaluates on specific domains or specific models, leaving open how detectors perform 'in the wild'."
  tension: "Prior work assumes controlled settings (known domain, known generator). In reality, detectors face texts from unknown LLMs across diverse domains. The paper asks: can detection still work when we don't know the source?"
  key_insight: "Perplexity is a double-edged sword — it is the fundamental feature separating human and machine text (machine text has lower perplexity), but detectors over-rely on it, systematically misclassifying low-perplexity human text. Diverse domains and models cause human-machine linguistic differences to converge, making detection harder."
  argument_chain: "problem (detection in controlled settings ≠ detection in the wild) → testbed construction (7 domains × 27 LLMs × 3 prompt types) → 8 progressive evaluation scenarios (in-distribution → OOD) → empirical finding (performance degrades with diversity, especially OOD) → analysis (linguistic convergence + perplexity bias) → mitigation (boundary adjustment with 0.1% data) → feasibility demonstration (86.54% on GPT-4 unseen domain)"
  contribution_framing: "Three contributions: (1) comprehensive testbed with texts from diverse human writings and LLMs, (2) empirical analysis revealing diminishing linguistic differences in open-domain settings, (3) discovery that perplexity serves as fundamental but biased clustering feature. Framed as 'first' comprehensive wild-scenario evaluation."
  intro_structure: "~5 paragraphs: (1) LLMs generate human-level text → detection needed, (2) existing work limited to specific domains/models, (3) two research questions about wild detection, (4) testbed construction description, (5) key findings and contributions."
  notable_technique: "Progressive difficulty design — 8 testbeds arranged from easiest (white-box, single domain, single model) to hardest (unseen domain + unseen model + paraphrasing attack), creating a compelling narrative arc that systematically reveals when and why detection fails."

figures:
  figure_count: 15
  figure1:
    type: "problem_illustration"
    description: "Left side shows diverse input domains (News Title, Story Title, Question, Argument, Scientific Topic) as colored cards with arrows pointing to both Humans (stick figure at desk) and multiple LLMs (GPT-3.5, FLAN-T5, LLaMA, OPT, GLM, ...) listed vertically. The many-to-many arrows from domains to generators show the combinatorial explosion. Right side shows a 'Text' box passing through a magnifying glass 'Detector' with a question mark, leading to two possible outputs: 'Human' (messy scribble icon) and 'Machine' (clean stick figure). The layout flows left-to-right: sources → generators → mixed text → detection challenge."
    narrative_role: "Establishes the core challenge — detection must handle the combinatorial space of domains × generators, not just one domain or one model."
    design_elements: ["colored domain cards (purple/orange/green)", "many-to-many arrows showing combinatorial complexity", "magnifying glass as detector metaphor", "question mark conveying uncertainty", "stick figure icons for human vs machine"]
    visual_style: "Clean line-art style with selective color on domain cards (purple, orange, green pastels). Horizontal left-to-right flow. Minimal decorative elements. Black-and-white for the detection side. Simple but effective at conveying the many-to-many challenge."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "grouped_bar_or_line"
      what_compared: "OOD detection performance on unseen models, broken down by model family and prompt type"
      how_gain_highlighted: "Shows which model families are hardest to detect (OpenAI, FLAN-T5) and which prompt types are most challenging (specified prompts)"
      design_note: "Separates analysis by two dimensions (model family × prompt type) to give nuanced OOD understanding rather than single aggregate number"
    - figure_id: "Figure 3"
      viz_type: "bar_chart_or_line"
      what_compared: "Detection performance (AvgRec) on unseen domains, identifying ROC, XSum, TLDR as hardest"
      how_gain_highlighted: "Links difficulty to domain perplexity characteristics"
      design_note: "Per-domain breakdown reveals systematic pattern (low-perplexity domains harder) rather than just reporting aggregate OOD performance"
    - figure_id: "Figure 4"
      viz_type: "precision_recall_curve + bar_chart"
      what_compared: "(a) PR curves before/after boundary adjustment, (b) performance improvement with 0.1% in-domain data"
      how_gain_highlighted: "Direct before/after comparison shows dramatic improvement from minimal adaptation"
      design_note: "Two-panel figure pairs theoretical (PR curve) with practical (data requirement) perspectives"
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "heatmap"
      dimensions_varied: ["domain diversity", "model diversity"]
      design_note: "Jensen-Shannon distance heatmap showing linguistic convergence as diversity increases — visual proof that the detection problem gets fundamentally harder with diversity"
    - figure_id: "Figure 6"
      viz_type: "bar_chart"
      dimensions_varied: ["named entity types (ORDINAL, DATE, etc.)"]
      design_note: "Shows entity distribution differences in fixed-domain setting as detection shortcuts that disappear with diversity"
    - figure_id: "Figures 7-9"
      viz_type: "histogram + scatter"
      dimensions_varied: ["perplexity distributions", "prediction correctness", "paraphrasing effects"]
      design_note: "Three-figure sequence builds the 'perplexity as double-edged sword' argument: (7) machine < human perplexity, (8) misclassified human texts have low perplexity, (9) paraphrasing shifts distributions"
  figure_narrative_role: "Figure 1 (problem illustration) → Figures 2-3 (OOD performance breakdown by model/domain) → Figure 4 (boundary adjustment solution) → Figures 5-6 (linguistic convergence analysis) → Figures 7-9 (perplexity analysis arc) → Figures 10-15 (appendix: prompts, data distributions, linguistic stats). The main paper figures follow a 'problem → results → analysis → mitigation' narrative arc."

tables:
  table_count: 12
  main_result_table:
    table_id: "Table 3"
    row_axis: "methods (Longformer, FastText, GLTR, DetectGPT)"
    col_axis: "testbed scenarios (Testbed 2-6) × metrics (AUROC, AvgRec, HumanRec, MachineRec)"
    row_organization: "flat"
    col_organization: "grouped_by_testbed"
    highlight_strategy: "best results in bold across methods per testbed"
    statistical_reporting: "single run numbers (no std reported for main results)"
    num_baselines: 4
    design_note: "Comprehensive table spanning both in-distribution (Testbeds 2-4) and out-of-distribution (Testbeds 5-6) in one view, enabling direct comparison of how each method degrades from ID to OOD. Progressive difficulty across columns tells the degradation story."
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["white-box detection (Testbed 1) — easiest setting as reference point"]
      variation_style: "full_numbers"
      design_note: "Separated from main table to establish performance ceiling before showing degradation"
    - table_id: "Table 4"
      what_varied: ["decision boundary adjustment effect on Testbeds 5-6"]
      variation_style: "full_numbers (before vs after adjustment)"
      design_note: "Shows boundary adjustment dramatically improves domain-shift performance (AvgRec 68.40→81.78 for unseen domains)"
    - table_id: "Table 5"
      what_varied: ["challenging frontier tests (Testbed 7: unseen domain+model with GPT-4, Testbed 8: paraphrasing attack)"]
      variation_style: "full_numbers with before/after boundary adjustment"
      design_note: "Most challenging scenarios isolated in separate table — clean before/after comparison for the proposed mitigation"
    - table_id: "Table 1"
      what_varied: ["naive baselines (ChatGPT querying, human annotators)"]
      variation_style: "full_numbers"
      design_note: "Establishes that even humans (~54.5% AvgRec) and ChatGPT (~54.5% AvgRec) struggle at wild detection, motivating the need for dedicated methods"
    - table_id: "Tables 8-10"
      what_varied: ["randomness analysis", "PLM backbone comparison", "data balance effects"]
      variation_style: "full_numbers"
      design_note: "Robustness checks in appendix ensure main findings are not artifacts of specific choices"
  supplementary_tables:
    in_appendix: true
    content: "Table 6 (dataset statistics per domain), Table 7 (naive baseline test set composition), Tables 8-10 (robustness: randomness/backbone/balance), Table 11 (all methods on challenging test sets), Table 12 (length statistics)"
    reason: "Main paper focuses on the progressive testbed story (Tables 1-5). Appendix holds dataset details and robustness checks that support but don't drive the narrative."
```

---

**7. mohamed2025_broken_telephone.yaml**

```yaml
paper_key: "mohamed2025_broken_telephone"
title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
venue: "ACL 2025"
full_text_available: false

research:
  baselines: ["single-pass generation", "various prompting strategies"]
  metrics:
    - {name: "information distortion rate", direction: "lower_better"}
    - {name: "semantic similarity to original", direction: "higher_better"}
    - {name: "factual accuracy degradation", direction: "lower_better"}
  datasets:
    - {name: "translation chain experiments", size: "N/A"}
  ablation_dimensions: ["number of iterative generations", "language choice", "chain complexity", "prompting strategy"]
  training_recipe: {optimizer: "N/A (inference only)", lr: "N/A", hardware: "N/A"}
  method_family: "empirical analysis of iterative LLM generation degradation"

positioning:
  core_claim: "LLMs systematically distort information when outputs are repeatedly processed, with distortion accumulating over iterations analogous to the broken telephone effect"
  key_results: "Degradation is inevitable but mitigable through strategic prompting; language and chain complexity influence distortion rate"
  limitations: ["primarily translation-based experiments", "limited model coverage"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**8. dohmatob2024_tale_of_tails.yaml**

```yaml
paper_key: "dohmatob2024_tale_of_tails"
title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
venue: "ICML 2024"
full_text_available: true

research:
  baselines:
    - "Original (human/natural) data training"
    - "Pure synthetic data training"
    - "Mixed real+synthetic data training"
    - "Hutter LLM (deterministic lookup table)"
    - "Hutter++ (probabilistic bigram)"
    - "Capacity-limited associative memory"
  metrics:
    - {name: "test error (scaling law exponent)", direction: "lower_better"}
    - {name: "perplexity", direction: "lower_better"}
    - {name: "number of skills learned (GCD answers)", direction: "higher_better"}
    - {name: "total variation distance", direction: "lower_better"}
  datasets:
    - {name: "Wikitext-103", size: "~2M samples for fine-tuning"}
    - {name: "GCD arithmetic task (Zipfian)", size: "300K-300M samples"}
    - {name: "Synthetic bigram distributions", size: "variable"}
  ablation_dimensions:
    - "tail cutoff rank k (top-p/top-k truncation)"
    - "tail exponent narrowing beta_prime vs beta (temperature scaling)"
    - "number of recursive generations n"
    - "mixing proportion pi of real vs synthetic data"
    - "model capacity / embedding dimension d"
    - "Zipf exponent beta"
    - "training set size T"
  training_recipe:
    optimizer: "not explicitly specified in main text"
    lr: "not explicitly specified in main text"
    hardware: "not explicitly specified"
    details: "GCD transformer trained on up to 300M samples; Llama2-7B fine-tuned on Wikitext-103 ~2M samples; synthetic data generated with various top-p and temperature settings"
  method_family: "theoretical analysis of model collapse via scaling laws and tail distributions"

positioning:
  core_claim: "Model collapse is fundamentally a change of scaling laws caused by synthetic data losing the heavy-tailed structure of natural distributions, leading to quantifiable and predictable degradation patterns including plateau effects, skill loss, and shifted scaling exponents."
  key_results: "Double scaling law E_test ~ T^(-(beta-1)/beta) + k^(-(beta-1)) predicts performance plateau on synthetic data; multi-generation collapse shows additive degradation E_test ~ T^(-c) + n*T0^(-c); grokking phenomenon when mixing pi-fraction real data creates plateau of length ~k^beta/pi before recovery; triplet scaling law E_test ~ T^(-(1-1/beta)) + d^(-c_q) + k^(-(beta-1)) for capacity-limited models"
  limitations:
    - "Theory assumes simplified models (Zipfian distributions, deterministic labels for some results)"
    - "Grokking theorem strictly holds only for deterministic ground-truth labels; probabilistic settings show attenuated S-shaped curves"
    - "Real LLMs involve complex conditional distributions not fully captured by the theoretical framework"
    - "Bigram and Hutter models are simplified abstractions of actual language model behavior"
    - "No experiments on larger-scale models beyond Llama2-7B"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Opens with the observation that AI model scaling laws have been a key predictive tool, but the ecosystem of online data is co-evolving to contain increasing amounts of synthetic data - asking whether future models will still improve or be 'doomed to degenerate up to total collapse'. Uses the striking statistic that ChatGPT contributes 0.1% of total words generated daily by the global population."
  tension: "Existing scaling law theory assumes training on natural (heavy-tailed) data distributions, but the inevitable contamination of training corpora with synthetic data fundamentally breaks these assumptions. Prior work on model collapse identified the phenomenon but lacked a theoretical framework connecting it to scaling laws and emergent abilities."
  key_insight: "The key insight is that heavy-tailed (Zipfian) distributions are what enable power-law scaling, and AI generation mechanisms (top-p sampling, temperature scaling, finite sampling) systematically destroy these tails through three mechanisms: tail cutting, tail narrowing, and finite sampling bias. This directly links distributional properties to scaling law behavior."
  argument_chain: "problem (synthetic data contamination is inevitable) -> observation (scaling laws depend on heavy-tailed distributions) -> mechanism (AI generation cuts/narrows tails via top-p, temperature, finite sampling) -> theory (double/triplet scaling laws predict plateau and degradation) -> multi-generation analysis (collapse compounds across iterations) -> mitigation (data mixing enables grokking recovery) -> experiments (GCD transformer + Llama2-7B validate predictions)"
  contribution_framing: "Four numbered contributions introduced with 'Our main findings are as follows': (1) Double Scaling Law, (2) Triplet Scaling Law for Memory-Limited Models, (3) Model Collapse over Multiple Generations, (4) Mitigation Strategies. Explicitly claims to be 'the first to theoretically and empirically analyze model collapse in the context of scaling laws and emergent abilities'."
  intro_structure: "5 paragraphs: P1=hook (scaling laws + synthetic data problem), P2=background (neural scaling laws and heavy tails), P3=problem statement (model collapse concern), P4=key insight (tail mechanisms), P5=contribution list (4 numbered findings)"
  notable_technique: "The 'tale of tails' metaphor is the central narrative device - it reframes the abstract concept of model collapse into a concrete, visual story about distribution tails. The three tail destruction mechanisms (cutting, narrowing, finite sampling) provide a clean taxonomy that makes complex theory intuitive. The paper also effectively uses the GCD arithmetic task as a controlled 'microscope' for studying skill emergence and loss, before scaling up to Llama2."

figures:
  figure_count: 5  # main text; ~35 total including appendices
  figure1:
    type: "motivation"
    description: "Illustrates the three mechanisms by which AI generation destroys distribution tails: top-p nucleus sampling (tail cutting), temperature scaling with tau>1 (tail narrowing), and finite sample bias. Shows how these mechanisms affect a Zipfian frequency distribution and connects to skill loss using GCD calculation (answers 2 and 3) as concrete examples."
    narrative_role: "Establishes the paper's core conceptual framework - visually demonstrates WHY model collapse happens by showing the mechanistic link between generation procedures and tail destruction. This is the key figure that makes the abstract theory tangible."
    design_elements: ["distribution curves with shaded truncation regions", "before/after comparison of tails", "concrete skill examples (GCD answers)", "three-panel layout for three mechanisms"]
    visual_style: "Clean schematic diagrams with distribution curves; uses color to distinguish original vs truncated/narrowed distributions; combines mathematical distributions with concrete task examples"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Three panels illustrating main theoretical results: (Left) Double scaling law with Zipf exponent beta=3/2 showing plateau effect; (Middle) Model collapse across 5 generations showing progressive degradation; (Right) Grokking behavior showing plateau length and asymptotic recovery predictions"
      how_gain_highlighted: "Theoretical predictions shown as dashed lines overlaid on empirical curves; clear separation between original data scaling (power law) and synthetic data scaling (plateau)"
      design_note: "Three-panel layout maps directly to three main theorems; log-log scale makes power-law relationships linear; uses generation number as a visual variable to show progressive collapse"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Three experimental validation panels: (Left) Llama2-7B perplexity scaling on Wikitext-103 across generations; (Middle) GCD transformer scaling on original vs synthetic data; (Right) Skills (GCD answers) learned on clean vs AI-generated data"
      how_gain_highlighted: "Direct visual comparison of original vs synthetic data curves; skill emergence on clean data vs skill loss on synthetic data is strikingly clear"
      design_note: "Mirrors the layout of Figure 3 (theory) to enable direct theory-vs-experiment comparison; this structural parallelism strengthens the validation narrative"
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      what_compared: "Effect of mixing real data (T_real) with AI data (T_AI) - shows performance improvement up to saturation point with k=1000 and beta=3/2"
      how_gain_highlighted: "Shows the grokking transition clearly - performance plateaus then recovers as real data fraction increases"
      design_note: "Single focused plot isolates the mixing mitigation result; parameters annotated directly on figure"
  ablation_figures:
    - figure_id: "Figure 2"
      viz_type: "combined_distribution_and_perplexity"
      dimensions_varied: ["data source (original vs AI-generated)", "generation parameters (top-p, temperature)"]
      design_note: "Two-part figure combines perplexity diagram (top) with distribution comparison (bottom); effectively demonstrates that the theoretical tail-cutting/narrowing mechanisms manifest in real LLM outputs"
  figure_narrative_role: "Figure 1 (motivation: why tails matter) -> Figure 2 (empirical evidence: tails ARE destroyed in practice) -> Figure 3 (theory: predicted consequences) -> Figure 4 (validation: experiments match theory) -> Figure 5 (mitigation: data mixing helps). Clean motivation-theory-validation-solution arc."

tables:
  table_count: 0
  main_result_table:
    note: "This paper has NO tables. All results are presented through mathematical theorems and figures with scaling curves. This is consistent with theoretical ML papers where the primary contributions are equations/bounds rather than benchmark comparisons."
  ablation_tables: []
  supplementary_tables:
    in_appendix: false
    content: "No tables in appendix either; appendices contain proofs (Appendices C-F), additional figures (Appendix B), and experimental details (Appendices G-H)"
    reason: "The paper is primarily theoretical - results are best expressed as scaling law equations and their visual verification, not tabular comparisons. The continuous nature of scaling curves makes line plots the natural presentation format."
```

---

**9. finlayson2024_closing.yaml**

```yaml
paper_key: "finlayson2024_closing"
title: "Closing the Curious Case of Neural Text Degeneration"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["nucleus sampling (top-p)", "top-k sampling", "greedy decoding", "threshold-based truncation methods"]
  metrics:
    - {name: "text quality (human eval)", direction: "higher_better"}
    - {name: "text quality (automatic)", direction: "higher_better"}
    - {name: "degeneration rate", direction: "lower_better"}
  datasets:
    - {name: "open-ended text generation benchmarks", size: "N/A"}
  ablation_dimensions: ["truncation threshold", "entropy regime", "model size"]
  training_recipe: {optimizer: "N/A (decoding strategy)", lr: "N/A", hardware: "N/A"}
  method_family: "truncation sampling / decoding strategy analysis"

positioning:
  core_claim: "The softmax bottleneck causes models to assign nonzero probability to impossible tokens; truncation sampling works by removing these, and a principled approach without arbitrary thresholds is possible"
  key_results: "Theoretical proof that threshold-free truncation using softmax bottleneck properties guarantees valid token sampling"
  limitations: ["focused on open-ended generation", "theoretical assumptions about softmax bottleneck"]
  relation_to_us: "orthogonal"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**10. yi2026_escaping_collapse.yaml**

```yaml
paper_key: "yi2026_escaping_collapse"
title: "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence"
venue: "ICLR 2026 (Poster)"
full_text_available: true

research:
  baselines:
    - "Unfiltered synthetic retraining (no verifier)"
    - "Real-data-only OLS estimator"
    - "VAE trained on full 60K MNIST (upper bound)"
  metrics:
    - {name: "MSE (parameter estimation error)", direction: "lower_better"}
    - {name: "FID (Frechet Inception Distance)", direction: "lower_better"}
    - {name: "ELBO (Evidence Lower Bound)", direction: "lower_better"}
  datasets:
    - {name: "Simulated linear regression", size: "dimension p=8, varying sample sizes (500->2000, 1000->4000, 2000->8000)"}
    - {name: "MNIST", size: "500 real images for init, 60K for discriminator training"}
  ablation_dimensions:
    - "Verifier bias (Delta: 0.0-0.7)"
    - "Verifier selectivity/radius (r: 0.05-0.5 for linear; top-10% for VAE)"
    - "Training sample size schedule (real->synthetic ratio)"
    - "Verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images)"
    - "Filtered vs unfiltered synthetic data"
  training_recipe:
    optimizer: "OLS (closed-form) for linear regression; standard SGD for CVAE"
    lr: "N/A for OLS; not specified for VAE"
    hardware: "Not specified"
    iterations: "60 rounds for linear regression; 40 rounds for VAE"
  method_family: "Verifier-guided synthetic data filtering for iterative model retraining"

positioning:
  core_claim: "External verifier-based filtering of synthetic data prevents model collapse in the short term via bias-variance tradeoff, but long-term performance converges to the verifier's knowledge center rather than ground truth -- unless the verifier is perfectly unbiased."
  key_results: "Linear regression: filtered retraining keeps MSE near 0.05 across 60 iterations while unfiltered diverges to 0.3-0.8. VAE/MNIST: FID drops from ~110 to ~40 with 60K-trained verifier over 40 iterations; with only 500-image verifier, FID plateaus at ~130."
  limitations:
    - "Theoretical analysis restricted to linear regression; generalization to neural networks remains open"
    - "VAE verifier (discriminator) is relatively simple and may reject harder-to-generate modes"
    - "Synthetic retraining initialized with only 500 real images limits diversity recovery"
    - "Verifier quality directly bounds long-term performance ceiling -- biased verifier leads to biased convergence"
    - "No experiments on large language models or more complex generative tasks"
  relation_to_us: "complementary"

narrative:
  story_type: "突破局限型"
  hook: "Synthetic data is increasingly used to train frontier generative models, but iterative retraining on self-generated data causes model collapse -- a well-documented performance degradation phenomenon."
  tension: "Prior work establishes collapse as seemingly inevitable under recursive self-training, but real practitioners already use external verification (human feedback, reward models). The question is: can verification provably escape collapse, and if so, what are the limits?"
  key_insight: "Verification creates a bias-variance tradeoff: filtering reduces variance (by discarding low-quality samples) but introduces bias (toward the verifier's knowledge center). Short-term gains are real but long-term convergence is to the verifier's center, not ground truth. Presented through Theorem 3.1 (one-round decomposition) and Theorem 4.1 (long-term contraction)."
  argument_chain: "model collapse problem -> prior work shows unfiltered retraining diverges -> introduce verifier-based filtering framework (Generate-Verify-Retrain) -> theoretical analysis: one-round improvement via bias-variance decomposition (Theorem 3.1) -> long-term convergence to verifier center (Theorem 4.1) -> empirical validation on linear regression + VAE/MNIST -> conclusion: verification helps but is fundamentally bounded by verifier quality"
  contribution_framing: "Three research questions framed as Q1 (does verification help short-term?), Q2 (do gains sustain long-term?), Q3 (empirical validation). Each answered with a theorem or experiment. Contribution count: 3 clearly delineated."
  intro_structure: "4 paragraphs: (1) motivation on synthetic data and model collapse concern, (2) research questions about verifier-based filtering, (3) prior literature context and gaps, (4) bullet-point contributions with theorem references"
  notable_technique: "Framing the two results as a deliberate tension -- short-term improvement (good news) vs long-term convergence to verifier center (cautionary news) -- creates a 'promise and peril' narrative arc that is more nuanced than a pure positive-result paper."

figures:
  figure_count: 5
  figure1:
    type: "teaser_result"
    description: "Three-panel comparison showing VAE-generated MNIST digits: (left) original data, (center-top) with verified synthetic data after 40 rounds showing maintained quality, (center-bottom) without verification showing severe collapse/degradation. (right) upper bound from training on all 60K real images."
    narrative_role: "Immediately demonstrates the paper's core claim visually -- verification prevents collapse while unfiltered retraining produces unrecognizable outputs. Placed before any theory to motivate the reader."
    design_elements: ["Before/after comparison", "With/without verification contrast", "Real sample grids", "Upper bound reference", "Arrow annotations connecting panels"]
    visual_style: "Black background with white MNIST digit grids arranged horizontally. Arrows with text labels ('With Data Verification' / 'Without Data Verification') connect the initial model to the two outcomes. Clean, high-contrast layout. Roughly 4-panel horizontal arrangement."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "heatmap + heatmap"
      what_compared: "One-round improvement landscape as function of verifier bias (Delta) and selectivity radius (r). Left (3a): theory-predicted loss landscape. Right (3b): empirical simulation."
      how_gain_highlighted: "Green regions indicate improvement (log ratio > 0), red regions indicate degradation. Theory-empirical match validates the theoretical framework."
      design_note: "Diverging green-red colormap centered at 0 makes improvement/degradation regions immediately readable. Side-by-side theory vs empirical layout validates theoretical predictions visually. Axes are interpretable parameters (bias, radius)."
    - figure_id: "Figure 4a"
      viz_type: "line_plot"
      what_compared: "Convergence of parameter estimate to verifier center (theta_c) over 60 iterations for different verifier radii (r=0.1, 0.5, 1, 1.5) with biased verifier"
      how_gain_highlighted: "All curves converge to near-zero distance from theta_c, confirming Theorem 4.1. Smaller radius = faster convergence."
      design_note: "Clean line plot with distinct colors for each radius value. Y-axis is distance to verifier center, clearly showing contraction. Legend is simple and readable."
    - figure_id: "Figure 4b"
      viz_type: "line_plot"
      what_compared: "Filtered (solid) vs unfiltered (dashed) retraining across different sample size schedules (500->2000, 1000->4000, 2000->8000) over 60 iterations with unbiased verifier"
      how_gain_highlighted: "Solid lines (filtered) stay flat near 0.05 while dashed lines (unfiltered) diverge upward to 0.3-0.8. Dramatic visual separation between the two groups."
      design_note: "Solid vs dashed line encoding for filtered/unfiltered is effective. Three colors for three sample size conditions. The divergence of dashed lines visually dramatizes model collapse."
    - figure_id: "Figure 5a"
      viz_type: "line_plot"
      what_compared: "VAE FID scores over 40 iterations comparing different VAE training sample sizes and filtered vs unfiltered conditions"
      how_gain_highlighted: "Filtered curves decrease steadily; unfiltered curves increase (collapse). Separation grows over iterations."
      design_note: "Multiple colored lines with solid/dashed encoding. FID on y-axis with clear downward = better convention."
    - figure_id: "Figure 5b"
      viz_type: "line_plot"
      what_compared: "Effect of verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images) on FID over 40 iterations"
      how_gain_highlighted: "Clear monotonic relationship: more verifier training data = lower FID. 60K verifier achieves FID ~40; 500-image verifier plateaus at ~130."
      design_note: "Seven colored lines ordered by verifier quality create a clean gradient pattern. Demonstrates the paper's key insight that verification quality bounds final performance. Well-chosen range of verifier sizes."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "heatmap"
      dimensions_varied: ["Verifier bias (Delta)", "Verifier selectivity radius (r)"]
      design_note: "Effectively an ablation over the two key verifier hyperparameters. Heatmap format makes the full landscape visible at once rather than requiring multiple line plots."
    - figure_id: "Figure 5b"
      viz_type: "line_plot"
      dimensions_varied: ["Verifier training dataset size (quality proxy)"]
      design_note: "Ablation over verifier quality showing monotonic improvement. Seven conditions provide fine granularity."
  figure_narrative_role: "Figure 1 (teaser: visual proof of concept) -> Figure 2 (pipeline: method overview) -> Figure 3 (theory validation: one-round landscape) -> Figure 4 (long-term dynamics: convergence behavior) -> Figure 5 (real-world validation: VAE experiments). Progression from motivation to theory to practice."

tables:
  table_count: 0
  main_result_table:
    table_id: "N/A"
    design_note: "Paper has no tables in main text. All results presented through figures (heatmaps and line plots). This is unusual but appropriate for a theory-focused paper where the key results are continuous landscapes and convergence dynamics rather than discrete benchmark comparisons."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Appendix A: 1D Gaussian analysis toolkit. Appendix B: Full proofs of Theorems 3.1 and 4.1. Appendix C: VAE experiment details including data preprocessing, discriminator architecture specifications, synthetic generation procedures, and supplementary ELBO results."
    reason: "All heavy mathematical proofs and implementation details moved to appendix to keep main paper focused on the two theorems and their experimental validation. Consistent with theory-paper conventions."
```

---

**11. binoculars2024.yaml**

```yaml
paper_key: "binoculars2024"
title: "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["DetectGPT", "Fast-DetectGPT", "likelihood thresholding", "supervised classifiers"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "TPR@1%FPR", direction: "higher_better"}
    - {name: "TPR@0.01%FPR", direction: "higher_better"}
  datasets:
    - {name: "multi-domain text corpus (news, wiki, creative)", size: "N/A"}
    - {name: "ChatGPT-generated samples", size: "N/A"}
  ablation_dimensions: ["LLM pair choice", "document type", "source model"]
  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot detection via contrastive LLM scoring"

positioning:
  core_claim: "A simple score contrasting two closely related LLMs achieves SOTA zero-shot detection without any training data, detecting >90% of generated text at 0.01% FPR"
  key_results: ">90% detection of ChatGPT at 0.01% FPR; generalizes across LLMs without model-specific tuning"
  limitations: ["requires two LLMs at inference", "performance depends on LLM pair choice"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**12. fast_detectgpt2024.yaml**

```yaml
paper_key: "fast_detectgpt2024"
title: "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["DetectGPT", "likelihood ratio", "rank-based methods", "supervised detectors"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "detection speed", direction: "higher_better"}
  datasets:
    - {name: "XSum", size: "N/A"}
    - {name: "SQuAD", size: "N/A"}
    - {name: "WritingPrompts", size: "N/A"}
  ablation_dimensions: ["source model", "scoring model", "perturbation vs sampling"]
  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot detection via conditional probability curvature"

positioning:
  core_claim: "Replacing DetectGPT's perturbation step with conditional probability sampling achieves 340x speedup with ~75% relative improvement in both white-box and black-box settings"
  key_results: "340x faster than DetectGPT; 75% relative improvement; 80% ChatGPT detection at 1% FPR"
  limitations: ["still requires model access for scoring", "performance varies by domain"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**13. diveye2026.yaml**

```yaml
paper_key: "diveye2026"
title: "DivEye: Diversity Boosts AI-Generated Text Detection"
venue: "TMLR 2026"
full_text_available: false

research:
  baselines: ["DetectGPT", "Fast-DetectGPT", "Binoculars", "supervised fine-tuned classifiers"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "detection accuracy", direction: "higher_better"}
  datasets:
    - {name: "multi-domain benchmarks", size: "N/A"}
  ablation_dimensions: ["statistical features", "auxiliary signal integration", "paraphrasing robustness", "cross-domain transfer"]
  training_recipe: {optimizer: "N/A (zero-shot statistical)", lr: "N/A", hardware: "N/A"}
  method_family: "statistical feature-based detection using surprisal diversity"

positioning:
  core_claim: "Human text exhibits richer variability in lexical and structural unpredictability (surprisal diversity) than LLM outputs, and this signal is interpretable, robust, and complements existing detectors"
  key_results: "Outperforms zero-shot detectors by up to 33.2%; improves existing detectors by up to 18.7% as auxiliary signal; robust to paraphrasing attacks"
  limitations: ["statistical features may not capture all AI text patterns", "performance on very short texts unclear"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**14. verma2024_ghostbuster.yaml**

```yaml
paper_key: "verma2024_ghostbuster"
title: "Ghostbuster: Detecting Text Ghostwritten by Large Language Models"
venue: "NAACL 2024"
full_text_available: true

research:
  baselines:
    - "Perplexity-only (GPT-3 davinci perplexity threshold)"
    - "DetectGPT (Mitchell et al. 2023, unsupervised perturbation-based)"
    - "GPTZero (commercial detector)"
    - "RoBERTa fine-tuned (supervised neural baseline)"
    - "Human evaluation (17 participants)"
  metrics:
    - {name: "F1", direction: "higher_better"}
    - {name: "Accuracy", direction: "higher_better"}
    - {name: "Precision", direction: "higher_better"}
  datasets:
    - {name: "IvyPanda Student Essays", size: "7,000 docs (1K human + 1K ChatGPT same-prompt + 4K ChatGPT generalization)"}
    - {name: "Reuters 50-50 News Articles", size: "7,000 docs (same split structure)"}
    - {name: "r/WritingPrompts Creative Writing", size: "7,000 docs (same split structure)"}
    - {name: "Lang-8 non-native English", size: "evaluation only"}
    - {name: "TOEFL 11 (essay subset)", size: "evaluation only"}
    - {name: "TOEFL 91 (essay subset)", size: "evaluation only"}
  ablation_dimensions:
    - "Feature search depth (1, 2, 3, 4)"
    - "Model components (with/without ada, davinci, handcrafted features)"
    - "Random features vs selected features"
    - "Document length (10-1000 tokens)"
    - "Perturbation robustness (character/word/sentence/paragraph level)"
    - "Cross-domain generalization (in-domain vs out-of-domain)"
    - "Cross-model generalization (ChatGPT vs Claude)"
    - "Cross-prompt generalization (5 prompt variants)"
  training_recipe:
    classifier: "Logistic regression with L2 regularization, C=1"
    optimizer: "N/A (closed-form or standard sklearn solver)"
    lr: "N/A"
    hardware: "Not specified"
    feature_generation: "Recursive composition of vector/scalar functions up to depth 3, yielding 2534 candidate features"
    feature_selection: "Forward feature selection on validation set"
    weaker_models: "Unigram fertility, Kneser-Ney trigram, GPT-3 ada, GPT-3 davinci"
  method_family: "Feature-engineered classifier using proxy model probabilities"

positioning:
  core_claim: "A structured search over compositions of weaker language model probabilities, combined with a simple linear classifier, can robustly detect AI-generated text without access to the target model's token probabilities."
  key_results: "99.0 F1 in-domain across all domains (+0.9 over RoBERTa, +5.9 over GPTZero); 97.0 F1 out-of-domain average (vs 85.1 RoBERTa); 92.2 F1 on Claude generalization; 99.5 F1 across prompt variants"
  limitations:
    - "Poor performance on documents under 100 tokens (F1 drops below 80 at 25 tokens)"
    - "Lower accuracy on non-native English speaker text (TOEFL 91: 74.7% accuracy, below GPTZero 92.3% and RoBERTa 96.7%)"
    - "Datasets limited to British/American English, not representative of all writing styles"
    - "Vulnerable to paraphrasing attacks (Undetectable.ai reduces recall from 99% to 62%)"
    - "Relies on API access to GPT-3 ada/davinci which may be deprecated"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Opens with the societal impact of ChatGPT's fluent text generation — schools restricting ChatGPT, authenticity concerns across education and journalism — establishing real-world urgency."
  tension: "Existing detectors (DetectGPT, GPTZero) show poor generalization across domains and models; supervised neural methods (RoBERTa) overfit to training distribution; zero-shot methods require target model token probabilities (a black-box limitation). Additionally, high false positive rates create ethical risks, disproportionately flagging non-native English speakers."
  key_insight: "Instead of requiring the target LLM's own probabilities, use a series of weaker, accessible language models as probability proxies, then let a structured combinatorial search discover discriminative feature compositions — the signal is in how different-quality models disagree on token predictions."
  argument_chain: "Problem (LLM text indistinguishable from human) → Existing solutions fail to generalize → Key insight: weaker model probability compositions are discriminative → Structured search over vector/scalar function compositions → Simple linear classifier achieves SOTA → Validated across 3 domains, cross-model (Claude), cross-prompt, perturbation robustness, and human comparison"
  contribution_framing: "Three contributions implicitly stated: (1) Ghostbuster method itself (structured search + linear classifier on weaker model probabilities), (2) three new benchmark datasets for AI text detection, (3) extensive evaluation including cross-domain, cross-model, cross-prompt generalization and robustness analysis. Framed via performance superiority: 'achieves 99.0 F1... 5.9 F1 higher than the best preexisting model.'"
  intro_structure: "3 paragraphs — P1: Problem establishment (ChatGPT impact, societal concerns); P2: Existing solution failures (poor generalization, false positives, bias against non-native speakers); P3: Ghostbuster introduction with headline numbers and method sketch"
  notable_technique: "Effective use of the 'black-box constraint' framing — positions the paper as solving a harder, more practical problem than prior work (no access to target model probabilities), which makes the strong results even more impressive. Also leverages the non-native speaker bias issue to establish ethical urgency."

figures:
  figure_count: 6
  figure1:
    type: "method_overview"
    description: "Left-to-right pipeline diagram showing the three stages of Ghostbuster: (1) a text document is passed through three weaker language models (Unigram, Trigram, GPT-3) producing probability vectors, (2) vector functions (+, -, x, /, >, <) combine probability vectors, (3) scalar functions (||.||, max, var) reduce to features, (4) features fed to logistic regression classifier visualized as a scatter plot."
    narrative_role: "Provides immediate visual understanding of the full pipeline — reader grasps the method in one glance before the technical details."
    design_elements: ["Left-to-right flow", "Color-coded stages (blue models, purple vector ops, purple scalar ops, tan classifier)", "Mathematical operator symbols inside boxes", "Scatter plot as classifier visualization"]
    visual_style: "Clean horizontal pipeline with rounded-rectangle boxes. Pastel color scheme (light blue for models, lavender for function boxes, beige for classifier). Minimal text labels. Text snippet shown as input on the left. Arrows connect stages. Compact single-row layout."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "F1 score degradation under increasing numbers of perturbations, split into local (character/word) and global (sentence/paragraph) perturbations"
      how_gain_highlighted: "Shows robustness envelope — performance stays above 80 F1 for most perturbation types until extreme levels; separate panels for local vs global perturbations make degradation patterns clear"
      design_note: "Two-panel layout (local left, global right) with shared y-axis (F1 Score) and color-coded lines per perturbation type. Legend inside plot. Clear visual separation of graceful degradation (character flips) vs catastrophic failure (paraphrasing)."
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "F1 score across document sizes (10-1000 tokens) for in-domain and various out-of-domain settings (Claude, WP, Reuters, Essay)"
      how_gain_highlighted: "All lines converge to ~95-100 F1 at 500+ tokens, visually demonstrating reliability at longer documents; short-document weakness is honestly shown"
      design_note: "Single plot with 5 color-coded lines. Dark background with grid. Log-scale-like x-axis (10,25,50,100,250,500,1000). Clearly shows the critical 100-token threshold where performance becomes reliable."
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "feature_list"
      dimensions_varied: ["Domain (News, Creative Writing, Essays)", "Selected features per domain"]
      design_note: "Lists the actual features selected by forward selection for each domain — not a traditional chart but a reference figure showing which compositions matter."
    - figure_id: "Figure 6"
      viz_type: "bar_chart"
      dimensions_varied: ["Dataset (WritingPrompts, Reuters, IvyPanda)", "Entropy rate under GPT-3"]
      design_note: "Entropy rate visualization comparing human vs AI text predictability across domains."
  figure_narrative_role: "Figure 1 (method overview) → Figure 2 (motivating example: human vs AI text side-by-side) → Figure 3 (robustness analysis) → Figure 4 (document length sensitivity) → Figure 5 (feature analysis, appendix) → Figure 6 (theoretical motivation via entropy, appendix). Main paper figures (1-4) follow: explain method → show problem → stress-test → analyze boundary conditions."

tables:
  table_count: 8
  main_result_table:
    table_id: "Table 2"
    row_axis: "methods"
    col_axis: "domains (News, Creative Writing, Student Essays, All Domains) x settings (In-Domain, Out-of-Domain)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "Best results implied by Ghostbuster row consistently highest; no explicit bold/underline formatting noted in HTML version"
    statistical_reporting: "Point estimates only, no confidence intervals or standard deviations"
    num_baselines: 4
    design_note: "Two major column groups (In-Domain | Out-of-Domain) with domain sub-columns. Clean structure shows both the in-domain ceiling and generalization gap simultaneously."
  ablation_tables:
    - table_id: "Table 4"
      what_varied: ["Feature search depth (1,2,3,4)", "Model components (ada, davinci, handcrafted)", "Feature selection method (random vs forward)"]
      variation_style: "full_numbers"
      design_note: "Comprehensive ablation with 9 conditions. Same column structure as Table 2 enables direct comparison."
  supplementary_tables:
    in_appendix: true
    content: "Table 1: Vector/scalar function definitions. Table 3: Generalization results (prompts, Claude, non-native). Tables 5-8: Dataset statistics, prompt templates, generation details."
    reason: "Main paper keeps only the two most important tables (main results + ablations) to maintain narrative focus."
```

---

**15. penedo2024_fineweb.yaml**

```yaml
paper_key: "penedo2024_fineweb"
title: "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale"
venue: "NeurIPS 2024"
full_text_available: true

research:
  baselines:
    - RefinedWeb
    - C4
    - The Pile
    - SlimPajama
    - RedPajama v2
    - Dolma 1.6
    - Dolma 1.7
    - Matrix
    - CC-100
    - Colossal-OSCAR
  metrics:
    - {name: "Aggregate Accuracy (avg of 9 benchmarks)", direction: "higher_better"}
    - {name: "HellaSwag", direction: "higher_better"}
    - {name: "MMLU", direction: "higher_better"}
    - {name: "ARC", direction: "higher_better"}
    - {name: "PIQA", direction: "higher_better"}
    - {name: "WinoGrande", direction: "higher_better"}
    - {name: "OpenBookQA", direction: "higher_better"}
    - {name: "CommonSenseQA", direction: "higher_better"}
    - {name: "SIQA", direction: "higher_better"}
  datasets:
    - {name: "FineWeb", size: "15T tokens from 96 Common Crawl snapshots"}
    - {name: "FineWeb-Edu", size: "1.3T tokens (educational subset of FineWeb)"}
    - {name: "RefinedWeb", size: "500B tokens"}
    - {name: "C4", size: "172B tokens"}
    - {name: "The Pile", size: "340B tokens"}
    - {name: "SlimPajama", size: "627B tokens"}
    - {name: "RedPajama v2", size: "20T tokens"}
    - {name: "Dolma 1.6", size: "3T tokens"}
    - {name: "Dolma 1.7", size: "1.2T tokens"}
    - {name: "Matrix", size: "1.3T tokens"}
    - {name: "CC-100", size: "70B tokens"}
    - {name: "Colossal-OSCAR", size: "850B tokens"}
  ablation_dimensions:
    - text_extraction_method (WARC trafilatura vs WET htmlparser)
    - base_filtering (URL blocklist + language ID + quality/repetition filters)
    - deduplication_scope (global vs per-snapshot MinHash)
    - deduplication_parameters (n-gram size, hash count, bucket structure, similarity threshold)
    - C4_filter_components (terminal punctuation, JS removal, ToS, doc length, lorem ipsum)
    - custom_heuristic_filters (50+ candidate statistics, 17 tested in Table 2)
    - educational_quality_threshold (0-5 scale, threshold sweep)
    - training_scale (28B tokens for filter ablations vs 350B for dedup ablations)
  training_recipe:
    model: "1.82B parameters (including embeddings), Llama architecture"
    optimizer: "not explicitly stated (likely AdamW given Llama architecture)"
    lr: "not explicitly stated"
    batch_size: "~2M tokens global batch size"
    sequence_length: 2048
    tokenizer: "GPT-2 tokenizer"
    hardware: "H100 GPUs, ~80,000 GPU-hours for 70+ ablation models"
    filter_ablation_tokens: "~28B tokens"
    dedup_ablation_tokens: "350B tokens"
    edu_classifier_cost: "6,000 H100 GPU-hours for classifying 15T tokens"
  method_family: "large-scale web data curation pipeline (extraction + filtering + deduplication + quality classification)"

positioning:
  core_claim: "Systematic, transparent web data curation with carefully ablated design choices produces 15T-token FineWeb and 1.3T-token FineWeb-Edu that outperform all existing open pretraining datasets, closing the gap between proprietary and public data knowledge."
  key_results: "FineWeb: ~52% aggregate accuracy at 350B tokens (top among all open datasets). FineWeb-Edu: MMLU 33%->37% (+12% relative), ARC 46%->57% (+24% relative), ~2% aggregate accuracy gain over FineWeb."
  limitations:
    - "Entirely web content from Common Crawl; no books, speech transcripts, or other data types"
    - "Most ablation experiments at smaller scale (~28B tokens) due to compute constraints"
    - "Evaluation limited to academic benchmarks without instruction tuning or alignment"
    - "Educational quality classifier may amplify biases in what Llama-3-70B-Instruct considers 'educational'"
  relation_to_us: "complementary"

narrative:
  story_type: "化繁为简型"
  hook: "Opens with the ubiquity of LLMs and immediately pivots to the dirty secret: [REDACTED] pretraining datasets behind the best open models (Llama 3, Mixtral) are not public, and curation strategies are 'closely guarded trade secrets.'"
  tension: "Despite LLM performance depending heavily on data quality, the community lacks both access to high-quality large-scale datasets AND knowledge of how to build them."
  key_insight: "Global deduplication across all 96 Common Crawl snapshots paradoxically HURTS performance because it upsamples lower-quality data from older crawls."
  argument_chain: "problem (data curation is a black box) -> systematic pipeline construction -> counterintuitive dedup finding -> cumulative pipeline = FineWeb 15T -> educational filtering = FineWeb-Edu 1.3T -> validation against 10 baselines at 350B scale"
  contribution_framing: "Six implicit contributions woven into intro prose rather than bulleted list."
  intro_structure: "Single long paragraph (~15 sentences). Unusually dense single-paragraph intro."
  notable_technique: "The 'ablation-as-narrative' structure: each section of the pipeline is presented as a mini-experiment with its own hypothesis, ablation, finding, and decision."

figures:
  figure_count: 27
  figure1:
    type: "motivation"
    description: "Line plot comparing aggregate accuracy vs training tokens for two text extraction methods: WARC/trafilatura vs WET/htmlparser."
    narrative_role: "Establishes the very first pipeline decision as consequential. Sets the pattern for all subsequent ablation figures."
    design_elements: ["Clean two-line comparison", "Continuous training curves showing gap widens with scale", "Minimal design", "Blue vs pink color coding"]
    visual_style: "Minimalist line plot, white background with faint horizontal gridlines."
  result_figures:
    - figure_id: "Figure 9"
      viz_type: "line_plot"
      what_compared: "Cumulative pipeline steps at 350B token scale"
      how_gain_highlighted: "Four stacked training curves with clear vertical separation"
      design_note: "Shows pipeline is monotonically improving"
    - figure_id: "Figure 10"
      viz_type: "line_plot"
      what_compared: "FineWeb and FineWeb-Edu vs 10 competing open datasets at 350B token scale"
      how_gain_highlighted: "FineWeb-Edu clearly on top; warm colors for 'Ours' vs cooler colors for competitors"
      design_note: "12 lines in one plot—aggressive but effective"
    - figure_id: "Figure 11"
      viz_type: "line_plot"
      what_compared: "FineWeb-Edu vs competitors on MMLU specifically"
      how_gain_highlighted: "10x token efficiency demonstrated visually"
      design_note: "Single-benchmark focus for most impressive result"
  ablation_figures:
    - figure_id: "Figure 6"
      viz_type: "bar_chart"
      dimensions_varied: ["individual C4 filter components"]
      design_note: "Reveals terminal punctuation filter is most impactful"
    - figure_id: "Figure 7"
      viz_type: "bar_chart"
      dimensions_varied: ["custom filter combinations vs C4 vs baseline"]
      design_note: "Custom FineWeb filters outperform C4 while removing less data"
    - figure_id: "Figure 8"
      viz_type: "histogram"
      dimensions_varied: ["deduplication method effect on punctuation distribution"]
      design_note: "Reveals mechanism behind global dedup's failure"
    - figure_id: "Figure 16"
      viz_type: "line_plot"
      dimensions_varied: ["FineWeb-Edu educational quality threshold"]
      design_note: "Threshold sweep ablation; threshold=3 is optimal"
  figure_narrative_role: "Pipeline construction chronologically, building evidence cumulatively."

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 2"
    description: "Full list of heuristic filters tested"
    row_axis: "candidate filter metrics with thresholds"
    col_axis: "metric | threshold | aggregate accuracy (%) | tokens removed (%)"
    row_organization: "by_performance"
    col_organization: "flat"
    highlight_strategy: "implicit ranking by aggregate accuracy"
    statistical_reporting: "single-run accuracy and token removal percentage"
    num_baselines: 16
    design_note: "Unusual 'main table' — not method-vs-baseline but filter candidate evaluation. Real main comparison is in Figure 10."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Table 3 (bias analysis subgroups/terms)."
    reason: "Pipeline ablations shown as training curves because temporal dynamics are more informative than single-point numbers."
```

---

**16. loki2025.yaml**

```yaml
paper_key: "loki2025"
title: "LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models"
venue: "ICLR 2025 Spotlight"
full_text_available: false

research:
  baselines: ["22 open-source LMMs", "6 closed-source LMMs"]
  metrics:
    - {name: "coarse-grained judgment accuracy", direction: "higher_better"}
    - {name: "fine-grained anomaly selection accuracy", direction: "higher_better"}
    - {name: "explanation quality", direction: "higher_better"}
  datasets:
    - {name: "LOKI benchmark", size: "18K questions across 26 subcategories"}
  ablation_dimensions: ["modality (video/image/3D/text/audio)", "difficulty level", "task type (judgment/selection/explanation)"]
  training_recipe: {optimizer: "N/A (benchmark)", lr: "N/A", hardware: "N/A"}
  method_family: "multimodal synthetic data detection benchmark"

positioning:
  core_claim: "First comprehensive benchmark for evaluating LMM ability to detect synthetic data across 5 modalities with both coarse and fine-grained evaluation"
  key_results: "LMMs show potential as synthetic detectors but reveal significant limitations; large gap between coarse judgment and fine-grained explanation"
  limitations: ["benchmark may not cover all generation methods", "multimodal focus may dilute text-specific insights"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**17. tulchinskii2024_intrinsic_dim.yaml**

```yaml
paper_key: "tulchinskii2024_intrinsic_dim"
title: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"
venue: "NeurIPS 2023"
full_text_available: false

research:
  baselines: ["DetectGPT", "likelihood-based methods", "supervised classifiers"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "cross-domain accuracy", direction: "higher_better"}
    - {name: "cross-model accuracy", direction: "higher_better"}
  datasets:
    - {name: "multi-language text corpora (English, Chinese, etc.)", size: "N/A"}
  ablation_dimensions: ["language", "generator model", "text domain", "writer proficiency level"]
  training_recipe: {optimizer: "N/A (intrinsic dimension estimation)", lr: "N/A", hardware: "N/A"}
  method_family: "geometric / manifold-based detection via intrinsic dimensionality"

positioning:
  core_claim: "Human texts have intrinsic dimensionality ~9 (alphabet languages) / ~7 (Chinese) while AI texts are ~1.5 lower, providing a language-agnostic, domain-invariant detection signal"
  key_results: "Outperforms SOTA in model-agnostic and cross-domain scenarios; stable across languages, domains, and writer proficiency levels"
  limitations: ["computational cost of dimension estimation", "may degrade with more human-like models"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**18. editlens2026.yaml**

```yaml
paper_key: "editlens2026"
title: "EditLens: Quantifying the Extent of AI Editing in Text"
venue: "ICLR 2026"
full_text_available: false

research:
  baselines: ["binary AI detectors (GPTZero, etc.)", "ternary classifiers"]
  metrics:
    - {name: "F1 (binary)", direction: "higher_better"}
    - {name: "F1 (ternary)", direction: "higher_better"}
    - {name: "regression correlation", direction: "higher_better"}
  datasets:
    - {name: "human-AI mixed editing dataset", size: "N/A"}
    - {name: "Grammarly editing data", size: "N/A"}
  ablation_dimensions: ["editing extent (continuous)", "similarity metric choice", "human annotation agreement"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "regression-based continuous AI editing quantification"

positioning:
  core_claim: "First to formalize AI editing detection as continuous regression rather than binary/ternary classification, achieving SOTA on both classification and regression tasks"
  key_results: "Binary F1=94.7%, ternary F1=90.4%; validated against human annotators; practical Grammarly case study"
  limitations: ["requires original human text for metric validation", "continuous scoring may be hard to interpret"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**19. cloc2025.yaml**

```yaml
paper_key: "cloc2025"
title: "CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss"
venue: "CVPR 2025"
full_text_available: false

research:
  baselines: ["standard contrastive learning", "ordinal regression methods", "cross-entropy classification"]
  metrics:
    - {name: "MAE (mean absolute error)", direction: "lower_better"}
    - {name: "classification accuracy", direction: "higher_better"}
  datasets:
    - {name: "Adience (age estimation)", size: "N/A"}
    - {name: "Historical Colour Image Dating", size: "N/A"}
    - {name: "Knee Osteoarthritis", size: "N/A"}
    - {name: "Indian Diabetic Retinopathy Image", size: "N/A"}
    - {name: "Breast Carcinoma Subtyping", size: "N/A"}
  ablation_dimensions: ["margin type", "number of margins", "contrastive pair selection"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "contrastive learning for ordinal classification"

positioning:
  core_claim: "Multi-margin N-pair loss enables flexible decision boundaries across adjacent ordinal categories, preserving class ordering while reducing overfitting to training bias"
  key_results: "Outperforms existing ordinal classification methods on 5 real-world datasets"
  limitations: ["image-focused evaluation", "limited to moderate number of ordinal classes"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**20. qurating2024.yaml**

```yaml
paper_key: "qurating2024"
title: "QuRating: Selecting High-Quality Data for Training Language Models"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["uniform random sampling", "perplexity-based filtering"]
  metrics:
    - {name: "perplexity", direction: "lower_better"}
    - {name: "in-context learning accuracy", direction: "higher_better"}
    - {name: "training efficiency (steps to target)", direction: "lower_better"}
  datasets:
    - {name: "260B token pre-training corpus", size: "260B tokens"}
    - {name: "30B token subsets sampled by quality", size: "30B tokens"}
  ablation_dimensions: ["quality dimension (writing style, expertise, facts, educational value)", "quality threshold", "quality-diversity balance"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "1.3B parameter LMs"}
  method_family: "LLM-based data quality rating for pre-training data selection"

positioning:
  core_claim: "LLMs can learn quality ratings from pairwise judgments across 4 dimensions, and training on educational-value-selected data matches uniform sampling with 50% fewer steps"
  key_results: "Educational value selection most impactful; quality-diversity balance is critical; 1.3B models trained on 30B quality-filtered tokens"
  limitations: ["limited to 1.3B scale", "quality dimensions may not cover all aspects"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**21. mitchell2023_detectgpt.yaml**

```yaml
paper_key: "mitchell2023_detectgpt"
title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
venue: "ICML 2023"
full_text_available: false

research:
  baselines: ["likelihood thresholding", "entropy-based methods", "supervised classifiers (RoBERTa)"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
  datasets:
    - {name: "XSum", size: "N/A"}
    - {name: "SQuAD", size: "N/A"}
    - {name: "WritingPrompts", size: "N/A"}
    - {name: "fake news (GPT-NeoX generated)", size: "N/A"}
  ablation_dimensions: ["perturbation model", "number of perturbations", "source model size"]
  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot detection via log probability curvature"

positioning:
  core_claim: "Machine-generated text occupies negative curvature regions of the source model's log probability function, enabling detection without training a classifier"
  key_results: "GPT-NeoX 20B fake news: AUROC 0.81 → 0.95 vs strongest baseline"
  limitations: ["requires perturbation model (slow)", "requires white-box or proxy model access", "short texts challenging"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**22. shi2025_closer_look.yaml**

```yaml
paper_key: "shi2025_closer_look"
title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
venue: "NeurIPS 2025 (Spotlight)"
full_text_available: true

research:
  baselines:
    - "Vanilla replace paradigm (train on synthetic data only)"
    - "Vanilla accumulate-subsample paradigm (uniform subsampling from real + all synthetic)"
    - "Unconditional DDPM generation"
    - "Classifier-Free Guidance (CFG, scale=2)"
  metrics:
    - {name: "Generalization Score (GS)", direction: "higher_better", definition: "Average L2 distance in DINOv2 feature space between each generated image and its nearest training neighbor"}
    - {name: "FID (Frechet Inception Distance)", direction: "lower_better"}
    - {name: "Estimated Entropy (Kozachenko-Leonenko)", direction: "higher_better"}
  datasets:
    - {name: "CIFAR-10", size: "32,768 images (32x32)"}
    - {name: "FFHQ", size: "8,192 images (downsampled to 32x32)"}
    - {name: "MNIST", size: "12,000 images"}
  ablation_dimensions:
    - "Dataset size (1024 to 32768 in powers of 2)"
    - "Training paradigm (replace vs accumulate-subsample)"
    - "Selection method (Greedy Selection vs Threshold Decay Filter vs vanilla)"
    - "Number of generated candidates (N vs 2N before selection)"
    - "Threshold decay rate alpha (sensitivity analysis)"
    - "Classifier-Free Guidance scale"
    - "Entropy vs variance as correlation target"
  training_recipe:
    model: "UNet-based DDPM (~16-19M parameters)"
    optimizer: "Adam"
    lr: "1e-4"
    weight_decay: "1e-6"
    batch_size: 128
    precision: "FP16 mixed"
    diffusion_steps: 1000
    epochs_cifar: 500
    epochs_ffhq: 1000
    hardware: "Single NVIDIA A100 GPU"
    feature_extractor: "DINOv2"
  method_family: "Entropy-based data selection for mitigating model collapse in iterative generative training"

positioning:
  core_claim: "Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by training data entropy shrinkage, not just variance collapse — and entropy-based data selection can effectively delay this transition."
  key_results: "Pearson r=0.91 between training data entropy and log(generalization score), dataset-size-independent. FFHQ accumulate-subsample: vanilla FID=75.7 vs Greedy Selection FID=44.7 at iteration 8. MNIST CFG: vanilla CFG FID=66.2 vs CFG+filtering FID=22.4 at iteration 8."
  limitations:
    - "No rigorous theoretical explanation for why entropy collapses"
    - "Limited to image diffusion models; no validation on language models"
    - "Greedy Selection is computationally expensive (quadratic in dataset size)"
    - "Only tested on 32x32 resolution images with relatively small models"
    - "No formal analysis of how many iterations can be sustained before memorization"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Opens with the practical inevitability of synthetic data contamination."
  tension: "Existing perspectives on model collapse are theoretically valid but practically insufficient — variance collapse requires extremely large number of iterations."
  key_insight: "The transition from generalization to memorization is the true practical manifestation of collapse. Entropy of the training set is the key diagnostic signal, with r=0.91 correlation."
  argument_chain: "Synthetic data contamination inevitable → Existing perspectives miss practical manifestations → Generalization-to-memorization transition → Entropy shrinks → Entropy correlates with generalization → Entropy-based selection preserves diversity"
  contribution_framing: "Three numbered contributions following identify-investigate-propose pattern."
  intro_structure: "3 paragraphs + 'Our Contributions' subsection."
  notable_technique: "Uses 'practical insufficiency' argument to distinguish from prior theoretical work. Visual pairing of generated images with nearest training neighbors makes memorization viscerally obvious."

figures:
  figure_count: 9
  figure1:
    type: "method_overview"
    description: "Three-row pipeline diagram with color-coded rows (green=collapse, blue=mitigated, orange=evolution) showing the two paradigms and the generalization-to-memorization transition."
    narrative_role: "Roadmap for entire paper."
    design_elements: ["Color-coded rows", "Pipeline arrows", "Pie chart for data composition", "Funnel icon for selection", "Real face image pairs showing degradation", "Horizontal arrow from Generalization to Memorization"]
    visual_style: "Clean horizontal flow with three visually distinct rows using pastel backgrounds."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "qualitative_comparison + line_plot"
      what_compared: "Generated images vs nearest training neighbors across iterations; GS decay curves"
      how_gain_highlighted: "Left panel shows progressive visual convergence. Right panel uses labeled regime regions."
      design_note: "Powerful dual-panel design: qualitative + quantitative."
    - figure_id: "Figure 4a"
      viz_type: "scatter"
      what_compared: "Entropy vs generalization score across dataset sizes"
      how_gain_highlighted: "Red dashed regression line through all sizes demonstrating r=0.91 universal correlation."
      design_note: "The key evidence figure. Log-scale y-axis linearizes the relationship."
    - figure_id: "Figure 5"
      viz_type: "multi_panel_line_plot"
      what_compared: "GS over iterations for vanilla vs selection methods"
      how_gain_highlighted: "Selection methods consistently above vanilla"
      design_note: "6 subfigures grid (datasets x paradigms)."
    - figure_id: "Figure 8"
      viz_type: "stacked_bar_chart_with_overlay_line"
      what_compared: "Proportion of selected images from each iteration source"
      how_gain_highlighted: "Selection naturally prefers real data — emergent behavior."
      design_note: "Insightful visualization of emergent behavior."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot + 2D_scatter_projection"
      dimensions_varied: ["iteration number", "dataset entropy"]
      design_note: "SVD projections make entropy collapse visually intuitive."
    - figure_id: "Figure 4b"
      viz_type: "scatter"
      dimensions_varied: ["variance vs generalization score"]
      design_note: "Placed next to 4a to show variance is weaker predictor."
  figure_narrative_role: "Figure 1 → Figure 2 → Figure 3 → Figure 4 → Figures 5-7 → Figure 8 → Figure 9. Discover-understand-mitigate-extend arc."

tables:
  table_count: 0
  main_result_table:
    design_note: "NO tables in main text. All results as line/scatter plots. Works because story is about trends over iterations."
  ablation_tables: []
  supplementary_tables:
    in_appendix: false
    content: "No tables even in appendix; all figure-based."
    reason: "Central argument is about trajectories over iterations, not static comparisons."
```

---

**23. wu2025_detection_survey.yaml**

```yaml
paper_key: "wu2025_detection_survey"
title: "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions"
venue: "Computational Linguistics, Vol. 51, Issue 1, 2025"
full_text_available: false

research:
  baselines: ["N/A (survey paper)"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "F1", direction: "higher_better"}
    - {name: "TPR@FPR", direction: "higher_better"}
  datasets:
    - {name: "various detection benchmarks surveyed", size: "N/A"}
  ablation_dimensions: ["method family (watermarking/statistical/neural/human-assisted)", "evaluation setting (in-domain/cross-domain/cross-model)", "attack type"]
  training_recipe: {optimizer: "N/A (survey)", lr: "N/A", hardware: "N/A"}
  method_family: "survey covering watermarking, statistics-based, neural-based, and human-assisted detection"

positioning:
  core_claim: "Comprehensive taxonomy of LLM text detection methods organized into 4 families, with analysis of challenges including OOD generalization, adversarial attacks, and evaluation framework deficiencies"
  key_results: "Identifies key gaps: OOD robustness, attack resilience, real-world data handling, lack of standardized evaluation"
  limitations: ["survey scope limited to text modality", "rapidly evolving field"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**24. kirchenbauer2023_watermark.yaml**

```yaml
paper_key: "kirchenbauer2023_watermark"
title: "A Watermark for Large Language Models"
venue: "ICML 2023"
full_text_available: false

research:
  baselines: ["no watermark baseline", "post-hoc detection methods"]
  metrics:
    - {name: "p-value (watermark detection)", direction: "lower_better"}
    - {name: "text quality (perplexity)", direction: "lower_better"}
    - {name: "BLEU/ROUGE (quality preservation)", direction: "higher_better"}
  datasets:
    - {name: "OPT model outputs", size: "N/A"}
  ablation_dimensions: ["green list fraction", "watermark strength (delta)", "text length", "model size"]
  training_recipe: {optimizer: "N/A (decoding-time watermark)", lr: "N/A", hardware: "OPT multi-billion parameter models"}
  method_family: "statistical watermarking via green token promotion"

positioning:
  core_claim: "Invisible watermarks can be embedded in LLM outputs by promoting 'green' tokens during generation, detectable from short spans without model access, with negligible quality impact"
  key_results: "Algorithmically detectable watermark with interpretable p-values; tested on OPT models; information-theoretic sensitivity analysis"
  limitations: ["vulnerable to paraphrasing attacks", "requires control of generation process", "green token bias may affect specific domains"]
  relation_to_us: "orthogonal"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

**25. dohmatob2025_strong_collapse.yaml**

```yaml
paper_key: "dohmatob2025_strong_collapse"
title: "Strong Model Collapse"
venue: "ICLR 2025 Spotlight"
full_text_available: true

research:
  baselines:
    - "Training on pure real/original data (no synthetic contamination)"
    - "Training on pure synthetic data"
    - "Mixed real+synthetic data with various proportions p2"
    - "Weighted single-step mixing (data weighting strategies)"
    - "Dynamic multi-step mixing"
  metrics:
    - {name: "test error (E_test on real distribution)", direction: "lower_better"}
    - {name: "test loss (cross-entropy for language modeling)", direction: "lower_better"}
    - {name: "collapse term zeta (excess error from synthetic data)", direction: "lower_better"}
  datasets:
    - {name: "Gaussian synthetic data (random projections)", size: "n=500 samples, variable d"}
    - {name: "MNIST", size: "standard 60K/10K"}
    - {name: "BabiStories", size: "reproduction of TinyStories via Mixtral-8x7B"}
  ablation_dimensions:
    - "synthetic data proportion p2"
    - "model size m"
    - "synthetic data quality c^2"
    - "total training set size n"
    - "parametrization rate psi=m/n"
    - "interpolation threshold crossing (m=n boundary)"
  training_recipe:
    optimizer: "standard SGD/Adam for neural network experiments"
    lr: "not explicitly detailed"
    hardware: "not explicitly detailed"
    details: "Random projections on Gaussian data (n=500); two-layer neural networks on MNIST (width m=2000); GPT-2 models (12-layer) on BabiStories"
  method_family: "theoretical analysis of model collapse via bias-variance decomposition and operator-valued free probability theory"

positioning:
  core_claim: "Model collapse persists even when mixing real and synthetic data, as long as the fraction of synthetic data does not vanish asymptotically — establishing a 'strong' form of collapse where no fixed-proportion mixing strategy can prevent performance degradation, and larger models amplify this effect in the under-parameterized regime."
  key_results: "E_test = B + V + zeta decomposition where zeta is irreducible collapse term; 1% synthetic data sufficient to cause collapse plateau; larger models amplify collapse below interpolation threshold; double-descent pattern past m=n threshold"
  limitations:
    - "Theory focuses on supervised regression with label shifts"
    - "Random projections model is simplified"
    - "Gaussian feature distribution assumption"
    - "Proportionate scaling limit"
    - "Does not address mitigation via data filtering, detection, or curation"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Opens with the observation that AI-generated content is increasingly contaminating web training corpora, and asks whether scaling up training data can still work."
  tension: "Prior model collapse work showed degradation in recursive settings, but left open whether strategic mixing could prevent collapse. This paper proves that hope is false."
  key_insight: "The bias-variance decomposition E_test = B + V + zeta, where zeta is irreducible as long as synthetic fraction p2 is fixed (non-vanishing)."
  argument_chain: "problem → question (can mixing overcome?) → theory (bias-variance-collapse decomposition) → scaling law implication → model size analysis → double-descent → data mixing strategies fail → experimental validation"
  contribution_framing: "Two main results explicitly labeled: Result #1 (Strong Model Collapse) and Result #2 (Model Size and Model Collapse)."
  intro_structure: "~5 paragraphs with Section 1.1 (contributions) and Section 1.2 (related work)."
  notable_technique: "The 'strong' vs 'weak' framing redefines the conversation. The Pareto diagram is an effective visual argument. Mathematical elegance of the exact decomposition makes a clean, falsifiable theoretical claim."

figures:
  figure_count: 8
  figure1:
    type: "motivation"
    description: "Pareto diagram showing test error on real data: mixed training vs real-only training."
    narrative_role: "Immediately establishes that no combination of model size and mixing achieves real-data-only performance."
    design_elements: ["Pareto frontier", "diagonal reference line", "colorbar for parametrization rate", "multiple quality levels"]
    visual_style: "Scatter plot with Pareto frontiers; colorbar encoding model size."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Strong model collapse in classical linear model"
      how_gain_highlighted: "Direct comparison of p2=0 vs p2>0 curves; plateau is visually stark"
      design_note: "Log-log scale; multiple p2 values show graduated severity"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Impact of model size on collapse"
      how_gain_highlighted: "Double-descent pattern visible"
      design_note: "Vertical inflection at m=n marks interpolation threshold"
    - figure_id: "Figure 7"
      viz_type: "line_plot"
      what_compared: "Model collapse on MNIST with two-layer NN"
      how_gain_highlighted: "Validates theory transfers to real image data"
      design_note: "Bridges theory-practice gap"
    - figure_id: "Figure 8"
      viz_type: "line_plot"
      what_compared: "GPT-2 on BabiStories: test loss vs tokens and vs model depth"
      how_gain_highlighted: "Left: scaling law plateau. Right: depth-dependent collapse reversal."
      design_note: "Most impactful figure — theory generalizes to autoregressive LMs"
  ablation_figures:
    - figure_id: "Figure 2"
      viz_type: "schematic_diagram"
      dimensions_varied: ["bias B", "variance V", "collapse term zeta"]
      design_note: "Illustrates B+V+zeta decomposition"
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      dimensions_varied: ["model size", "data quality", "mixing proportion"]
      design_note: "Double-descent curves"
  figure_narrative_role: "Figure 1 (Pareto motivation) -> Figure 2 (decomposition) -> Figure 3 (linear model validation) -> Figure 4 (model size effects) -> Figures 5-7 (additional theory + MNIST) -> Figure 8 (GPT-2 validation). Visual claim -> mechanism -> toy -> real-world."

tables:
  table_count: 0
  main_result_table:
    note: "NO tables. All results via theorems and scaling curve figures."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Proofs, additional figures, experimental setup details."
    reason: "Theoretical paper — results expressed as equations and visual verification."
```

---

All 25 files read completely. Summary of the collection:

- **8 papers with full text and detailed narrative/figure/table analysis**: bevendorff2025_two_paradigms, li2024_mage, dohmatob2024_tale_of_tails, yi2026_escaping_collapse, verma2024_ghostbuster, penedo2024_fineweb, shi2025_closer_look, dohmatob2025_strong_collapse
- **17 papers with abstract-level research metadata only** (narrative/figures/tables marked N/A): dohmatob2024_demystified, alemohammad2024_mad, drayson2025_detection_prevents_collapse, synthetic_eggs2026, mohamed2025_broken_telephone, finlayson2024_closing, binoculars2024, fast_detectgpt2024, diveye2026, loki2025, tulchinskii2024_intrinsic_dim, editlens2026, cloc2025, qurating2024, mitchell2023_detectgpt, wu2025_detection_survey, kirchenbauer2023_watermark

The papers span two main research threads: **model collapse / synthetic data contamination** (Dohmatob x3, Alemohammad, Drayson, Yi, Shi, Mohamed, Synthetic Eggs, Finlayson) and **AI-generated text detection** (Bevendorff, Li/MAGE, Binoculars, Fast-DetectGPT, DivEye, Ghostbuster, Tulchinskii, EditLens, Mitchell/DetectGPT, Kirchenbauer/watermark, Wu/survey, LOKI), plus **data curation** (FineWeb, QuRating) and **ordinal classification** (CLOC).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7712ef7-d1cb-4ff1-a296-e860e8bc8525",
  "isSidechain": true,
  "agentId": "af75b63db3ca0cde3",
  "requestId": "req_011CbFuY3exYfwrMX5cS6mo9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1427e8fc-51ab-49e7-9363-ddfd302c86cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3HaN9SwHD1SmhnpTZjrww",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 49157,
      "cache_read_input_tokens": 8271,
      "output_tokens": 29453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 49157
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 29453,
          "cache_read_input_tokens": 8271,
          "cache_creation_input_tokens": 49157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 49157,
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
