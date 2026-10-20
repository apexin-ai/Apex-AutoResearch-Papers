# Research conversation: Search the web for the paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ji et al. 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a670aa20606bd2bcb.jsonl`
- **Structured JSON:** [`3ed366787e1ed457e7dc.json`](../../sessions/3e/3ed366787e1ed457e7dc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-16T09:42:37.175Z_

Search the web for the paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ji et al. This should be from EMNLP 2025. I need to verify:
1. Is it actually an EMNLP 2025 paper? What recognition did it receive - "Outstanding Paper" or "SAC Highlight" or something else?
2. What is the VUF (Verbal Uncertainty Feature) methodology?
3. What models was it validated on? (claimed: Llama-3.1-8B, Mistral-7B, Qwen2.5-7B)
4. What hallucination reduction was achieved? (claimed: 31.9% relative on Llama-3.1-8B)
5. Does it use activation intervention on the residual stream?

Search with queries like:
- "Calibrating Verbal Uncertainty Linear Feature Hallucinations EMNLP 2025"
- "VUF direction hallucination reduction Ji"
- "EMNLP 2025 outstanding paper hallucination calibration"

Report precisely what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "97985efd-2e72-44f8-ab9f-0536b1c30628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:42:37.178Z_

```json
{
  "parentUuid": "97985efd-2e72-44f8-ab9f-0536b1c30628",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "595ef1a1-60c9-419b-a8df-081f7479aa5d",
  "timestamp": "2026-05-16T09:42:37.178Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T09:42:40.413Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0131Vdc2JKEDmCv8cFGMwuwD`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "595ef1a1-60c9-419b-a8df-081f7479aa5d",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62gca7a21nwuQj9eeY5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9e91ddd-03fb-4f68-9b77-1e4e67e67ef9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CaheFh1pp2P6zPw2qe8TDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 815,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 815,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 4 · 2026-05-16T09:42:40.416Z_

<details><summary>↩ Tool result · `toolu_0131Vdc2JKEDmCv8cFGMwuwD`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9e91ddd-03fb-4f68-9b77-1e4e67e67ef9",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "141e1cf3-b06e-4d05-8acc-c39591597012",
  "sourceToolAssistantUUID": "e9e91ddd-03fb-4f68-9b77-1e4e67e67ef9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T09:42:44.091Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0167KCQT6NfF4za7Eb1ukfFw`</summary>

```json
{
  "query": "Calibrating Verbal Uncertainty Linear Feature Hallucinations EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "141e1cf3-b06e-4d05-8acc-c39591597012",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62gsPMDTC2a16kAMiRu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b403aa8-033b-4fbf-9d9e-f016d9128b7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4NmZ8R9JqcoiVoLyFrdjN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 6 · 2026-05-16T09:42:44.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xh2y9pQRwZNo472iDoTRJB`</summary>

```json
{
  "query": "VUF direction hallucination reduction Ji EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b403aa8-033b-4fbf-9d9e-f016d9128b7e",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62gsPMDTC2a16kAMiRu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "966070f5-1695-4831-96e4-95631084fe66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4NmZ8R9JqcoiVoLyFrdjN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 7 · 2026-05-16T09:42:44.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019JG9RmGjPRf62UKoFtLX2m`</summary>

```json
{
  "query": "EMNLP 2025 outstanding paper hallucination calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "966070f5-1695-4831-96e4-95631084fe66",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62gsPMDTC2a16kAMiRu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2820f039-2917-40ee-8d65-28f73424a015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4NmZ8R9JqcoiVoLyFrdjN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 8 · 2026-05-16T09:42:48.299Z_

<details><summary>↩ Tool result · `toolu_01Xh2y9pQRwZNo472iDoTRJB`</summary>

```text
Web search results for query: "VUF direction hallucination reduction Ji EMNLP 2025"

Links: [{"title":"Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.631/"},{"title":"Mitigating Hallucinations in Large Vision-Language ...","url":"https://aclanthology.org/2025.emnlp-main.982.pdf"},{"title":"An Empirical Study on Hallucinations in Embodied Agents ...","url":"https://aclanthology.org/2025.findings-emnlp.1158.pdf"},{"title":"VIDHALLUC: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12408113/"},{"title":"MRFD: Multi-Region Fusion Decoding with Self- ...","url":"https://aclanthology.org/2025.findings-emnlp.858.pdf"},{"title":"Diving into Mitigating Hallucinations from a Vision ...","url":"https://aclanthology.org/2025.findings-emnlp.936.pdf"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"The Mirage of Hallucination Detection","url":"https://aclanthology.org/2025.findings-emnlp.1035.pdf"},{"title":"Mitigating Hallucinations in MLLMs with Attention Causal ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Seeing_Far_and_Clearly_Mitigating_Hallucinations_in_MLLMs_with_Attention_CVPR_2025_paper.pdf"},{"title":"How Much Do LLMs Hallucinate across Languages? On ...","url":"https://aclanthology.org/2025.emnlp-main.1481.pdf"}]

Based on the search results, I found a paper that appears to match your query. There is a paper titled "Diving into Mitigating Hallucinations from a Vision Perspective" published at EMNLP 2025.

However, the search results don't contain detailed information about a paper specifically titled with "VUF direction hallucination reduction" by Ji at EMNLP 2025. The papers in the search results discuss various approaches to mitigating hallucinations in vision-language models, but I cannot find an exact match for your specific query.

If you have more details about the paper (such as the full title, author names, or a DOI), I'd be happy to search again with that information to help you find the specific paper you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "966070f5-1695-4831-96e4-95631084fe66",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "642474ff-d898-4c4b-9ae7-07d6cfcc0772",
  "sourceToolAssistantUUID": "966070f5-1695-4831-96e4-95631084fe66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T09:42:50.191Z_

<details><summary>↩ Tool result · `toolu_0167KCQT6NfF4za7Eb1ukfFw`</summary>

```text
Web search results for query: "Calibrating Verbal Uncertainty Linear Feature Hallucinations EMNLP 2025"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.187@ACL"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to ...","url":"https://aclanthology.org/2025.emnlp-main.187.pdf"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"[Literature Review] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.themoonlight.io/en/review/calibrating-verbal-uncertainty-as-a-linear-feature-to-reduce-hallucinations"}]

Based on the search results, here's information about the paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" from EMNLP 2025:

## Paper Overview

The paper was written by Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda, and was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing.

## Main Problem

LLMs often adopt an assertive language style when making false claims, with such "overconfident hallucinations" misleading users and eroding trust.

## Key Findings

The authors found that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and shows that this has only moderate correlation with the actual "semantic uncertainty" of the model.

## Results

The mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, and the authors can intervene on verbal uncertainty at inference time and reduce confident hallucinations on short-form answers, achieving an average relative reduction of ~30%.

The paper addresses an important challenge in making language models more reliable by aligning how they express uncertainty with their actual internal confidence levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b403aa8-033b-4fbf-9d9e-f016d9128b7e",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "7afd4955-c460-438c-88b9-ecfc37e5e964",
  "sourceToolAssistantUUID": "2b403aa8-033b-4fbf-9d9e-f016d9128b7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T09:42:50.508Z_

<details><summary>↩ Tool result · `toolu_019JG9RmGjPRf62UKoFtLX2m`</summary>

```text
Web search results for query: "EMNLP 2025 outstanding paper hallucination calibration"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Awards - EMNLP 2025","url":"https://2025.emnlp.org/program/awards/"},{"title":"Re-evaluating Hallucination Detection in LLMs","url":"https://aclanthology.org/2025.emnlp-main.1761.pdf"},{"title":"An Empirical Study on Hallucinations in Embodied Agents ...","url":"https://aclanthology.org/2025.findings-emnlp.1158.pdf"},{"title":"Detecting LLM Hallucination Through Layer-wise ...","url":"https://aclanthology.org/2025.emnlp-main.1644.pdf"},{"title":"A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1809/"},{"title":"Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.67/"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Mitigating Geospatial Knowledge Hallucination in Large ...","url":"https://aclanthology.org/2025.findings-emnlp.45.pdf"},{"title":"HalluLens: LLM Hallucination Benchmark","url":"https://aclanthology.org/2025.acl-long.1176.pdf"}]

Based on the search results, I found relevant information about EMNLP 2025 and papers related to hallucination and calibration:

One paper highlighted by the Senior Area Chairs at EMNLP 2025 as particularly noteworthy is "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda.

Additionally, there are several other hallucination-related papers presented at EMNLP 2025. A paper called "Rewarding Doubt (2025)" integrates confidence calibration into reinforcement learning, penalising both over- and underconfidence so model certainty better matches correctness. 

Calibration metrics are gaining traction: modern systems are judged not only on accuracy but on how well they signal when they don't know.

The search results indicate a strong focus at EMNLP 2025 on the intersection of hallucination reduction and calibration of model uncertainty, with multiple papers addressing how to better measure and improve the reliability of large language models through improved confidence estimates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2820f039-2917-40ee-8d65-28f73424a015",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "fb3b5b8f-f312-4bf4-aeba-225d6ff8f31c",
  "sourceToolAssistantUUID": "2820f039-2917-40ee-8d65-28f73424a015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-16T09:42:53.533Z_

Now let me get more details from the ACL Anthology page and the EMNLP 2025 awards page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3b5b8f-f312-4bf4-aeba-225d6ff8f31c",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62hbY8VWvnPKAViZUKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1a56193-2c8f-4e94-b199-69674c8bde9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lz9sBUfHWxG6j11LBFwZ7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 10430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2796,
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

_source line 12 · 2026-05-16T09:42:54.017Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ByrkGKHX3vicody5ajFKqK`</summary>

```json
{
  "query": "site:2025.emnlp.org awards best paper outstanding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1a56193-2c8f-4e94-b199-69674c8bde9f",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62hbY8VWvnPKAViZUKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b1951c0-fd49-42a2-98d5-b107d481aaea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lz9sBUfHWxG6j11LBFwZ7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 10430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2796,
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

_source line 13 · 2026-05-16T09:42:54.476Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MNzaoPjtmvh1Dx2oKscu5m`</summary>

```json
{
  "query": "arxiv 2503.14477 verbal uncertainty linear feature methodology models Llama Mistral"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b1951c0-fd49-42a2-98d5-b107d481aaea",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62hbY8VWvnPKAViZUKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcb43bea-1aaa-4c05-8555-2611880999c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lz9sBUfHWxG6j11LBFwZ7k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 10430,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 10430,
          "cache_creation_input_tokens": 2796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2796,
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

_source line 14 · 2026-05-16T09:42:58.941Z_

<details><summary>↩ Tool result · `toolu_01ByrkGKHX3vicody5ajFKqK`</summary>

```text
Web search results for query: "site:2025.emnlp.org awards best paper outstanding"

Links: [{"title":"Awards - EMNLP 2025","url":"https://2025.emnlp.org/program/awards/"},{"title":"Keynotes - EMNLP 2025","url":"https://2025.emnlp.org/program/keynotes/"},{"title":"NAACL-HLT 2021 Instructions for Reviewers - EMNLP 2025","url":"https://2025.emnlp.org/reviewer/instructions/"},{"title":"Panel - EMNLP 2025","url":"https://2025.emnlp.org/program/panel/"},{"title":"Best Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/best_papers/"},{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"Conference Overview - EMNLP 2025","url":"https://2025.emnlp.org/program/"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"}]

I found information from the EMNLP 2025 Awards page. Here are the key details:

The Best Paper Committee was chaired by Owen Rambow (Stony Brook University) and Mirella Lapata (University of Edinburgh). A special committee, with assignments based on reviewer expertise, produced 92 reviews and selected four best paper nominations, from which the final awardees were chosen (including ARR-originating submissions with fewer initial nominations).

The Senior Area Chairs highlighted the following 35 papers as particularly noteworthy, with examples including papers like "PAFT: Prompt-Agnostic Fine-Tuning," "Constructions are Revealed in Word Distributions," and "To Mask or to Mirror: Human-AI Alignment in Collective Reasoning."

Additionally, EMNLP 2025 offers award categories including Special Theme Best paper award along with the main best paper awards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b1951c0-fd49-42a2-98d5-b107d481aaea",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "9fc3630e-9efc-4069-9e4a-74eec3e354da",
  "sourceToolAssistantUUID": "7b1951c0-fd49-42a2-98d5-b107d481aaea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T09:43:01.674Z_

<details><summary>↩ Tool result · `toolu_01MNzaoPjtmvh1Dx2oKscu5m`</summary>

```text
Web search results for query: "arxiv 2503.14477 verbal uncertainty linear feature methodology models Llama Mistral"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Revisiting Uncertainty Estimation and Calibration of Large ...","url":"https://arxiv.org/pdf/2505.23854"},{"title":"Revisiting Uncertainty Estimation and Calibration of Large Language Models","url":"https://arxiv.org/html/2505.23854v1"},{"title":"Alphaxiv","url":"https://www.alphaxiv.org/en/overview/2503.14477"},{"title":"Uncertainty Distillation: Teaching Language Models to Express Semantic Confidence","url":"https://arxiv.org/html/2503.14749"},{"title":"Can Large Language Models Express Uncertainty Like Human?","url":"https://arxiv.org/html/2509.24202"},{"title":"Investigating Human-Aligned Large Language Model Uncertainty","url":"https://arxiv.org/html/2503.12528v1"},{"title":"Can Language Models Verbalize Well-Defined Notions of Uncertainty?","url":"https://arxiv.org/html/2503.14749v2"}]

I found the paper arxiv 2503.14477. Here's what the research is about:

## Paper Summary

The paper is titled "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations".

### Key Findings

The researchers find that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and show that this has only moderate correlation with the actual "semantic uncertainty" of the model.

The framework discovers a linear verbal uncertainty feature (VUF) that controls model expression of uncertainty, and applies this insight to: (1) detect hallucinations arising from the miscalibration between high semantic uncertainty (SU) and low verbal uncertainty (VU); (2) mitigate hallucinations by intervening on activations along the VUF direction at inference time to make VU more aligned with model's SU.

### Results and Models Tested

The mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, and by intervening on verbal uncertainty at inference time, the researchers reduce confident hallucinations on short-form answers, achieving an average relative reduction of ~30%.

The research extracts VUFs from different datasets from Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, and tests results on models including Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, and Llama-3.1-70B-Instruct.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcb43bea-1aaa-4c05-8555-2611880999c2",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "6600b6ee-6075-4991-820f-e28dd115c5d3",
  "sourceToolAssistantUUID": "bcb43bea-1aaa-4c05-8555-2611880999c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T09:43:06.175Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01N2itps7ZaV47EhnVYafFYk`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6600b6ee-6075-4991-820f-e28dd115c5d3",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62iRKWAF5bMRW6uY2HW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a4f5703-ba1f-4e33-9e37-431b671fa71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017B5qBoWT4VKFpaLkSvXf31",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1663,
      "cache_read_input_tokens": 13226,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 13226,
          "cache_creation_input_tokens": 1663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1663,
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

_source line 17 · 2026-05-16T09:43:06.177Z_

<details><summary>↩ Tool result · `toolu_01N2itps7ZaV47EhnVYafFYk`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a4f5703-ba1f-4e33-9e37-431b671fa71f",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "5cc58b12-e452-4cee-9145-68d43f5240ff",
  "sourceToolAssistantUUID": "1a4f5703-ba1f-4e33-9e37-431b671fa71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T09:43:14.033Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017UTBFrumxuminrx8RCFseh`</summary>

```json
{
  "url": "https://2025.emnlp.org/program/awards/",
  "prompt": "List all award categories and winning papers. Specifically check if \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\" by Ji et al. received any award (Best Paper, Outstanding Paper, SAC Highlight, etc.). List every paper that won an award or was highlighted."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cc58b12-e452-4cee-9145-68d43f5240ff",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62ikn2rt7dZRoMcEhTf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d7fe226-2835-4f4d-89be-b5a970bc4c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERKymj5fKtZb925oXyvq8a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 14889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 19 · 2026-05-16T09:43:16.300Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012dWotrxp3VUUkAzXnZ5e5L`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.14477",
  "prompt": "Extract all details about this paper: full title, all authors, methodology (especially the VUF - Verbal Uncertainty Feature - how it works, what it intervenes on), models tested (Llama, Mistral, Qwen etc.), key results including hallucination reduction percentages, and whether it uses activation intervention on the residual stream. Also note the venue it was published at."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d7fe226-2835-4f4d-89be-b5a970bc4c06",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62ikn2rt7dZRoMcEhTf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b345a9e9-4a75-410f-b989-32d05a203b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERKymj5fKtZb925oXyvq8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 14889,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 14889,
          "cache_creation_input_tokens": 595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 595,
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

_source line 20 · 2026-05-16T09:43:19.544Z_

<details><summary>↩ Tool result · `toolu_017UTBFrumxuminrx8RCFseh`</summary>

```text
# EMNLP 2025 Awards Summary

## Award Categories and Winners

**Best Paper:**
- "Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index" by Xu et al.

**Outstanding Papers (7 total):**
1. LingGym by Yang et al.
2. Mind the Value-Action Gap by Shen et al.
3. DiscoSG by Lin et al.
4. Generative or Discriminative? by Kasa et al.
5. Measuring Chain of Thought Faithfulness by Tutek et al.
6. MiCRo by Shen et al.
7. Causal Interventions Reveal Shared Structure by Boguraev et al.

**Best Special Theme Paper:**
- "InterIDEAS: Philosophical Intertextuality via LLMs" by Yang et al.

**Best Resource Paper:**
- "Autoformalization in the Wild" by Zhang et al.

**Social Impact Award:**
- "AccessEval: Benchmarking Disability Bias in Large Language Models" by Panda et al.

**People's Choice Award:**
- "Randomly Removing 50% of Dimensions in Text Embeddings..." by Takeshita et al.

## SAC Highlights (35 papers)

Regarding your specific query: **"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations"** by Ji et al. **was recognized as a SAC Highlight**, not as a Best Paper or Outstanding Paper.

All 35 SAC-highlighted papers are listed in the document above.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d7fe226-2835-4f4d-89be-b5a970bc4c06",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "714e5480-8f3c-4d7d-bcaf-56b1c6415c64",
  "sourceToolAssistantUUID": "5d7fe226-2835-4f4d-89be-b5a970bc4c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T09:43:20.949Z_

<details><summary>↩ Tool result · `toolu_012dWotrxp3VUUkAzXnZ5e5L`</summary>

```text
# Paper Details: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations

**Full Title:** "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations"

**Authors:** Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, Nicola Cancedda

**Methodology:**
The researchers discovered that verbal uncertainty operates as a single linear feature within LLM representation spaces. They distinguish between "verbal uncertainty" (how confidently a model expresses claims linguistically) and "semantic uncertainty" (the model's actual confidence). Their key insight is that misalignment between these two types of uncertainty better predicts hallucinations than semantic uncertainty alone. The paper states: "we can intervene on verbal uncertainty at inference time" to reduce overconfident false statements.

**Models Tested:** 
The page does not specify which model architectures (Llama, Mistral, Qwen, etc.) were evaluated.

**Key Results:**
The intervention approach achieved "an average relative reduction of ~30%" in confident hallucinations on short-form answers.

**Activation Intervention Details:**
The content confirms inference-time intervention on verbal uncertainty but does not explicitly detail residual stream activation manipulation.

**Venue:** 
No publication venue is listed—this is a preprint (arXiv:2503.14477), submitted March 18, 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b345a9e9-4a75-410f-b989-32d05a203b02",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "f0c9c928-0059-4467-83f2-2121a60bf668",
  "sourceToolAssistantUUID": "b345a9e9-4a75-410f-b989-32d05a203b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T09:43:26.688Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WkB7waNCL6vTKbdKczaWLF`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.14477v1",
  "prompt": "Extract detailed methodology information about:\n1. The VUF (Verbal Uncertainty Feature) - how is it extracted? Is it a direction in activation space?\n2. Does the intervention happen on the residual stream? What layer(s)?\n3. What specific models were tested? (Look for Llama-3.1-8B, Mistral-7B, Qwen2.5-7B)\n4. What specific hallucination reduction percentages were achieved per model? Is 31.9% mentioned for Llama-3.1-8B?\n5. What datasets were used for evaluation?\n6. How is the linear feature identified - via probing, PCA, or other method?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0c9c928-0059-4467-83f2-2121a60bf668",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62jqkCuW49tfnfXF3Vv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "878b4dec-e73b-4e99-8498-8a31618c50d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E9agLYCBtUfsQ8GALzszA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 15484,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1188
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 15484,
          "cache_creation_input_tokens": 1188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1188,
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

_source line 23 · 2026-05-16T09:43:33.239Z_

<details><summary>↩ Tool result · `toolu_01WkB7waNCL6vTKbdKczaWLF`</summary>

```text
# Verbal Uncertainty Feature (VUF) Methodology Summary

## 1. VUF Extraction Method

The VUF is indeed a direction in activation space. Researchers use the **difference-in-means technique** to identify it. They collect question-answer pairs with high verbal uncertainty (VU) and low VU, then compute:

> "the difference between the model's mean last-token residual stream activations 𝐡(l)⁢(x)"

across these two sets. This produces a directional vector 𝐫VU(l) at each layer.

## 2. Intervention Location

Interventions occur on **residual stream activations across multiple layers**. The method applies:

> "h(l)⁢(x)←h(l)⁢(x)+αsu⁢(x)∗𝐫VU(l)"

specifically targeting layers from middle to final layers where VUFs are most prominent.

## 3. Models Tested

Three instruction-tuned models were evaluated:
- Llama-3.1-8B-Instruct
- Mistral-7B-Instruct-v0.3
- Qwen2.5-7B-Instruct

## 4. Hallucination Reduction Results

Per Table 3, average relative reductions across three datasets were:
- **Llama**: 32.4% → 22.3% (31.9% reduction)
- **Mistral**: 46.9% → 29.1% (38% reduction)
- **Qwen**: 48.1% → 34.6% (28% reduction)

## 5. Evaluation Datasets

- TriviaQA (10,000 training, 1,000 test samples)
- NQ-Open (10,000 training, 1,000 test samples)
- PopQA (10,000 training, 1,000 test samples)

## 6. Feature Identification Method

The paper employs **visualization via PCA** to confirm linear separability, showing distinct clustering of certain vs. uncertain representations. This validates the difference-in-means directional vector represents meaningful VU information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "878b4dec-e73b-4e99-8498-8a31618c50d6",
  "isSidechain": true,
  "promptId": "8e0bfd6d-3b8f-4cb8-bc33-ad7b2f34cfed",
  "agentId": "a670aa20606bd2bcb",
  "type": "user",
  "uuid": "655748ec-f522-4241-8ae4-98027ade2688",
  "sourceToolAssistantUUID": "878b4dec-e73b-4e99-8498-8a31618c50d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T09:43:53.278Z_

Now I have comprehensive information to provide a detailed report. Here is what I found:

---

## Findings Report

### 1. Publication Venue and Recognition

The paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ji et al. **is confirmed as an EMNLP 2025 main conference paper** (published as `2025.emnlp-main.187` in the ACL Anthology).

It received recognition as a **SAC (Senior Area Chair) Highlight** -- one of 35 papers highlighted as "particularly noteworthy." It did **NOT** receive "Outstanding Paper" or "Best Paper" status. Those are separate, higher-tier awards at EMNLP 2025.

### 2. VUF (Verbal Uncertainty Feature) Methodology

The VUF is a **direction in the residual stream activation space** of LLMs, identified using the **difference-in-means technique**:
- Collect question-answer pairs exhibiting high verbal uncertainty (VU) vs. low VU
- Compute the difference between the model's mean **last-token residual stream activations** h^(l)(x) across these two groups
- This produces a directional vector r_VU^(l) at each layer

The key insight is distinguishing "verbal uncertainty" (how confidently the model expresses claims linguistically) from "semantic uncertainty" (the model's actual internal confidence). The mismatch between these two is a better predictor of hallucinations than semantic uncertainty alone.

PCA visualization is used to confirm that certain vs. uncertain representations form linearly separable clusters.

### 3. Models Validated

Confirmed -- the paper tests on:
- **Llama-3.1-8B-Instruct**
- **Mistral-7B-Instruct-v0.3**
- **Qwen2.5-7B-Instruct**

(The claim of these three models is accurate.)

### 4. Hallucination Reduction

The specific results per model (average across TriviaQA, NQ-Open, PopQA):
- **Llama-3.1-8B**: 32.4% -> 22.3% confident hallucination rate = **31.9% relative reduction** (confirmed)
- **Mistral-7B**: 46.9% -> 29.1% = ~38% relative reduction
- **Qwen2.5-7B**: 48.1% -> 34.6% = ~28% relative reduction

The claimed 31.9% relative reduction on Llama-3.1-8B is **confirmed accurate**.

### 5. Activation Intervention on the Residual Stream

**Yes, confirmed.** The intervention formula is:

> h^(l)(x) <- h^(l)(x) + alpha * su(x) * r_VU^(l)

where alpha is a scaling factor and su(x) is the semantic uncertainty estimate. The intervention is applied to **residual stream activations across multiple layers** (middle to final layers where VUFs are most prominent). This steers the model toward expressing more verbal uncertainty when semantic uncertainty is high, thus reducing overconfident hallucinations.

---

## Summary of Verification

| Claim | Verdict |
|-------|---------|
| EMNLP 2025 paper | **Confirmed** (main conference, paper 187) |
| "Outstanding Paper" award | **Incorrect** -- it is a SAC Highlight (not Outstanding Paper) |
| VUF is a linear feature in activation space | **Confirmed** |
| Tested on Llama-3.1-8B, Mistral-7B, Qwen2.5-7B | **Confirmed** |
| 31.9% relative reduction on Llama-3.1-8B | **Confirmed** |
| Uses activation intervention on residual stream | **Confirmed** |

Sources:
- [ACL Anthology - Paper Page](https://aclanthology.org/2025.emnlp-main.187/)
- [arXiv:2503.14477](https://arxiv.org/abs/2503.14477)
- [arXiv HTML version](https://arxiv.org/html/2503.14477v1)
- [EMNLP 2025 Awards Page](https://2025.emnlp.org/program/awards/)
- [EMNLP 2025 Accepted Main Conference Papers](https://2025.emnlp.org/program/main_papers/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "655748ec-f522-4241-8ae4-98027ade2688",
  "isSidechain": true,
  "agentId": "a670aa20606bd2bcb",
  "requestId": "req_011Cb62kkK4KwMABuQbU5FDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c13474c6-448e-40cc-bab8-cebba7ec60f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58d3af57-1d7d-4d3c-9365-116ec456346a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pw29NTUBwm6epN8dvFydEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 16672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 764,
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
